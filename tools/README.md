English | [简体中文](README.zh-CN.md)

# DOI Reference Checker (`check_dois.py`)

`check_dois.py` is a zero-dependency Python 3 script (standard library `urllib` only) that extracts DOIs from `.bib`, `.md`, `.txt`, or `.tex` files and queries the public Crossref REST API (`https://api.crossref.org/works/<DOI>`) one by one to check whether each DOI actually exists.

For every extracted DOI, the script prints:
- Whether the DOI exists in Crossref (`FOUND`), does not exist (`NOT_FOUND`, HTTP 404), or failed due to a network/API issue (`NETWORK_ERROR`, reported separately and never conflated with `NOT_FOUND`).
- The Crossref-recorded **title**, **publication year**, and **venue/publisher** alongside your local `.bib` title and year so you can catch both fabricated DOIs and "swapped DOI" hallucinations (where an AI attaches a real DOI from Paper A to a fabricated citation for Paper B).

## Requirements

- Python 3.8+ (uses standard library modules only — no `pip install` required)
- Internet access to `https://api.crossref.org`

## Usage

Run from the repository root:

```bash
# Check a BibTeX file
python3 tools/check_dois.py tools/examples/refs-sample.bib

# Check a Markdown chapter draft or plain-text reference list
python3 tools/check_dois.py chapters/chapter-02.md

# Emit structured JSON output
python3 tools/check_dois.py tools/examples/refs-sample.bib --json

# Return exit code 1 if any DOI is NOT_FOUND or NETWORK_ERROR (for CI scripts)
python3 tools/check_dois.py tools/examples/refs-sample.bib --strict
```

### Command-Line Options

| Option | Default | Description |
|---|---|---|
| `input_file` | *(required)* | Path to `.bib`, `.txt`, `.md`, or `.tex` file |
| `--delay SECONDS` | `1.0` | Pause between consecutive Crossref requests (enforces a minimum of `1.0` second) |
| `--timeout SECONDS` | `15.0` | Per-request HTTP timeout in seconds |
| `--json` | `false` | Print machine-readable JSON output |
| `--strict` | `false` | Exit with code `1` when one or more DOIs are `NOT_FOUND` or `NETWORK_ERROR` |

The script sends `User-Agent: scivolume-academic-book-toolkit/0.1` and enforces at least a 1.0-second interval between requests.

## Verified Sample Run (`tools/examples/refs-sample.bib`)

[`examples/refs-sample.bib`](examples/refs-sample.bib) includes 3 real academic references verified in Crossref (a monograph, a journal article, and a conference paper) plus 1 intentionally fabricated DOI (`10.1038/s41586-099-99999-z`).

Command:

```bash
python3 tools/check_dois.py tools/examples/refs-sample.bib
```

Actual output:

```text
Input file : tools/examples/refs-sample.bib
Unique DOIs: 4 (Crossref API interval: 1.0s)

[1/4] DOI: 10.7208/chicago/9780226239873.001.0001 (@booth2016craft, line 9)
      Local    : The Craft of Research, Fourth Edition (2016)
      Status   : FOUND (exists in Crossref)
      Crossref : The Craft of Research, Fourth Edition (2016)
      Venue    : University of Chicago Press

[2/4] DOI: 10.1038/nature14539 (@lecun2015deep, line 20)
      Local    : Deep learning (2015)
      Status   : FOUND (exists in Crossref)
      Crossref : Deep learning (2015)
      Venue    : Nature

[3/4] DOI: 10.1145/3442188.3445922 (@bender2021parrots, line 30)
      Local    : On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? (2021)
      Status   : FOUND (exists in Crossref)
      Crossref : On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜 (2021)
      Venue    : Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency

[4/4] DOI: 10.1038/s41586-099-99999-z (@hallucinated2024synthetic, line 42)
      Local    : Automated Synthesis of Scholarly Monographs Without Source Grounding (2024)
      Status   : NOT_FOUND (does NOT exist in Crossref)
      Detail   : HTTP 404 Not Found (DOI not registered in Crossref)

--------------------------------------------------------------------
Summary: 4 checked | 3 found | 1 not found | 0 network error(s)
```

## What This Script Checks — and What Still Needs Manual Review

1. **DOI existence vs. metadata match**: A `FOUND` result confirms the DOI is registered in Crossref. Always compare `Local` and `Crossref` titles/years in the output to make sure the DOI actually belongs to the cited work.
2. **Non-Crossref DOIs & ISBN-only books**: Crossref covers the majority of scholarly journals, conference proceedings, and academic presses, but DOIs registered through other agencies (such as DataCite for datasets/preprints or CNKI/mEDRA) may return `NOT_FOUND` in Crossref. Verify those via `https://doi.org/<DOI>` or publisher catalogs.
3. **Claim-to-source alignment**: Resolving a DOI does not prove that the cited source supports your sentence in the manuscript. Complete the full 7-point check in [`../checklists/reference-verification.md`](../checklists/reference-verification.md) before submission.
