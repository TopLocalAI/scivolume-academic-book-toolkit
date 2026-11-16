#!/usr/bin/env python3
"""Verify DOIs in a plain-text, Markdown, LaTeX, or BibTeX (.bib) file via Crossref.

Uses only the Python 3 standard library (urllib). Queries
https://api.crossref.org/works/<DOI> one by one with at least a 1-second delay
between requests, prints whether each DOI exists along with the Crossref title
and publication year for manual comparison, and distinguishes network/API
errors from non-existent DOIs (HTTP 404).
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

CROSSREF_API_BASE = "https://api.crossref.org/works/"
USER_AGENT = "scivolume-academic-book-toolkit/0.1"
MIN_INTERVAL_SECONDS = 1.0

# Matches standard DOI strings (10.xxxx/...), including LaTeX-escaped underscores (\_).
DOI_PATTERN = re.compile(
    r"(?i)\b(10\.\d{4,9}/(?:\\_|[-._;()/:A-Za-z0-9])+)"
)
HTML_TAG_PATTERN = re.compile(r"<[^>]+>")


@dataclass
class ExtractedDOI:
    doi: str
    line: int
    citekey: Optional[str] = None
    local_title: Optional[str] = None
    local_year: Optional[str] = None


@dataclass
class CheckResult:
    doi: str
    status: str  # "FOUND" | "NOT_FOUND" | "NETWORK_ERROR"
    line: int
    citekey: Optional[str] = None
    local_title: Optional[str] = None
    local_year: Optional[str] = None
    crossref_title: Optional[str] = None
    crossref_year: Optional[int] = None
    crossref_venue: Optional[str] = None
    error_detail: Optional[str] = None


def clean_doi(raw: str) -> str:
    """Normalize LaTeX escapes and strip trailing prose/BibTeX punctuation."""
    doi = raw.replace(r"\_", "_").strip()
    while doi:
        if doi[-1] in ".,;:!?'\"":
            doi = doi[:-1]
        elif doi[-1] == ")" and doi.count(")") > doi.count("("):
            doi = doi[:-1]
        else:
            break
    return doi


def clean_text_field(value: str) -> str:
    """Collapse whitespace, strip outer braces/HTML tags, and unescape entities."""
    text = HTML_TAG_PATTERN.sub("", value)
    text = html.unescape(text)
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def parse_bib_context(text: str) -> List[Tuple[int, int, str, Optional[str], Optional[str]]]:
    """Return (start_offset, end_offset, citekey, title, year) for BibTeX entries."""
    entries: List[Tuple[int, int, str, Optional[str], Optional[str]]] = []
    header_re = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)
    for match in header_re.finditer(text):
        citekey = match.group(1).strip()
        brace_start = text.find("{", match.start())
        if brace_start == -1:
            continue
        depth = 0
        end_pos = len(text)
        for idx in range(brace_start, len(text)):
            ch = text[idx]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    end_pos = idx + 1
                    break
        block = text[match.start() : end_pos]
        local_title = _extract_bib_field(block, "title")
        local_year = _extract_bib_field(block, "year")
        entries.append((match.start(), end_pos, citekey, local_title, local_year))
    return entries


def _extract_bib_field(block: str, field_name: str) -> Optional[str]:
    field_re = re.compile(
        rf"(?im)^\s*{re.escape(field_name)}\s*=\s*(\{{|\")"
    )
    match = field_re.search(block)
    if not match:
        return None
    opener = match.group(1)
    start = match.end()
    if opener == '"':
        end = block.find('"', start)
        if end == -1:
            return None
        return clean_text_field(block[start:end])
    depth = 1
    for idx in range(start, len(block)):
        if block[idx] == "{":
            depth += 1
        elif block[idx] == "}":
            depth -= 1
            if depth == 0:
                return clean_text_field(block[start:idx])
    return None


def extract_dois(text: str, is_bib: bool = False) -> List[ExtractedDOI]:
    """Extract unique DOIs in order of first appearance."""
    bib_entries = parse_bib_context(text) if is_bib else []
    seen: Dict[str, ExtractedDOI] = {}

    for match in DOI_PATTERN.finditer(text):
        doi = clean_doi(match.group(1))
        if not doi or "/" not in doi:
            continue
        key = doi.lower()
        if key in seen:
            continue

        offset = match.start()
        line_num = text.count("\n", 0, offset) + 1
        citekey = None
        local_title = None
        local_year = None

        for start, end, entry_key, entry_title, entry_year in bib_entries:
            if start <= offset < end:
                citekey = entry_key
                local_title = entry_title
                local_year = entry_year
                break

        seen[key] = ExtractedDOI(
            doi=doi,
            line=line_num,
            citekey=citekey,
            local_title=local_title,
            local_year=local_year,
        )

    return list(seen.values())


def extract_crossref_year(message: dict) -> Optional[int]:
    for field in ("published", "published-print", "published-online", "issued"):
        block = message.get(field)
        if isinstance(block, dict):
            parts = block.get("date-parts")
            if (
                isinstance(parts, list)
                and parts
                and isinstance(parts[0], list)
                and parts[0]
                and isinstance(parts[0][0], int)
            ):
                return parts[0][0]
    return None


def extract_crossref_title(message: dict) -> str:
    titles = message.get("title") or []
    subtitles = message.get("subtitle") or []
    main_title = clean_text_field(titles[0]) if titles else ""
    subtitle = clean_text_field(subtitles[0]) if subtitles else ""
    if main_title and subtitle and subtitle.lower() not in main_title.lower():
        return f"{main_title}: {subtitle}"
    return main_title or "(no title recorded in Crossref)"


def extract_crossref_venue(message: dict) -> Optional[str]:
    containers = message.get("container-title") or []
    if containers:
        venue = clean_text_field(containers[0])
        if venue:
            return venue
    publisher = message.get("publisher")
    if isinstance(publisher, str) and publisher.strip():
        return clean_text_field(publisher)
    return None


def query_crossref(item: ExtractedDOI, timeout: float) -> CheckResult:
    encoded_doi = urllib.parse.quote(item.doi, safe="")
    url = f"{CROSSREF_API_BASE}{encoded_doi}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw_bytes = resp.read()
        payload = json.loads(raw_bytes.decode("utf-8"))
        message = payload.get("message", {})
        return CheckResult(
            doi=item.doi,
            status="FOUND",
            line=item.line,
            citekey=item.citekey,
            local_title=item.local_title,
            local_year=item.local_year,
            crossref_title=extract_crossref_title(message),
            crossref_year=extract_crossref_year(message),
            crossref_venue=extract_crossref_venue(message),
        )
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return CheckResult(
                doi=item.doi,
                status="NOT_FOUND",
                line=item.line,
                citekey=item.citekey,
                local_title=item.local_title,
                local_year=item.local_year,
                error_detail="HTTP 404 Not Found (DOI not registered in Crossref)",
            )
        return CheckResult(
            doi=item.doi,
            status="NETWORK_ERROR",
            line=item.line,
            citekey=item.citekey,
            local_title=item.local_title,
            local_year=item.local_year,
            error_detail=f"HTTP {exc.code} {exc.reason}",
        )
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        return CheckResult(
            doi=item.doi,
            status="NETWORK_ERROR",
            line=item.line,
            citekey=item.citekey,
            local_title=item.local_title,
            local_year=item.local_year,
            error_detail=f"{type(exc).__name__}: {exc}",
        )


def print_human_report(
    file_path: pathlib.Path, results: List[CheckResult], interval: float
) -> None:
    total = len(results)
    print(f"Input file : {file_path}")
    print(f"Unique DOIs: {total} (Crossref API interval: {interval:.1f}s)\n")

    for idx, res in enumerate(results, start=1):
        loc = f"line {res.line}"
        if res.citekey:
            loc = f"@{res.citekey}, {loc}"
        print(f"[{idx}/{total}] DOI: {res.doi} ({loc})")

        if res.local_title or res.local_year:
            local_yr = res.local_year or "?"
            local_ti = res.local_title or "(no local title)"
            print(f"      Local    : {local_ti} ({local_yr})")

        if res.status == "FOUND":
            yr = str(res.crossref_year) if res.crossref_year is not None else "unknown"
            print("      Status   : FOUND (exists in Crossref)")
            print(f"      Crossref : {res.crossref_title} ({yr})")
            if res.crossref_venue:
                print(f"      Venue    : {res.crossref_venue}")
        elif res.status == "NOT_FOUND":
            print("      Status   : NOT_FOUND (does NOT exist in Crossref)")
            print(f"      Detail   : {res.error_detail}")
        else:
            print(
                "      Status   : NETWORK_ERROR "
                "(verification inconclusive; NOT treated as non-existent)"
            )
            print(f"      Detail   : {res.error_detail}")
        print()

    found_count = sum(1 for r in results if r.status == "FOUND")
    missing_count = sum(1 for r in results if r.status == "NOT_FOUND")
    error_count = sum(1 for r in results if r.status == "NETWORK_ERROR")

    print("-" * 68)
    print(
        f"Summary: {total} checked | {found_count} found | "
        f"{missing_count} not found | {error_count} network error(s)"
    )


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Extract DOIs from a .bib or plain-text/Markdown/LaTeX file and "
            "verify each DOI against the public Crossref API."
        )
    )
    parser.add_argument(
        "input_file",
        type=pathlib.Path,
        help="Path to the .bib, .txt, .md, or .tex file to check",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=MIN_INTERVAL_SECONDS,
        help="Delay in seconds between Crossref API requests (minimum 1.0s, default: 1.0)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=15.0,
        help="Per-request HTTP timeout in seconds (default: 15.0)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Print output as JSON instead of human-readable text",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with status code 1 if any DOI is NOT_FOUND or NETWORK_ERROR",
    )
    args = parser.parse_args(argv)

    if not args.input_file.is_file():
        print(f"Error: file not found: {args.input_file}", file=sys.stderr)
        return 2

    interval = max(args.delay, MIN_INTERVAL_SECONDS)
    content = args.input_file.read_text(encoding="utf-8", errors="replace")
    is_bib = args.input_file.suffix.lower() == ".bib"
    extracted = extract_dois(content, is_bib=is_bib)

    if not extracted:
        if args.as_json:
            print(json.dumps({"file": str(args.input_file), "results": []}, indent=2))
        else:
            print(f"Input file : {args.input_file}")
            print("No DOIs found in file.")
        return 0

    results: List[CheckResult] = []
    for idx, item in enumerate(extracted):
        if idx > 0:
            time.sleep(interval)
        results.append(query_crossref(item, timeout=args.timeout))

    if args.as_json:
        payload = {
            "file": str(args.input_file),
            "summary": {
                "checked": len(results),
                "found": sum(1 for r in results if r.status == "FOUND"),
                "not_found": sum(1 for r in results if r.status == "NOT_FOUND"),
                "network_error": sum(1 for r in results if r.status == "NETWORK_ERROR"),
            },
            "results": [r.__dict__ for r in results],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print_human_report(args.input_file, results, interval=interval)

    if args.strict and any(r.status != "FOUND" for r in results):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
