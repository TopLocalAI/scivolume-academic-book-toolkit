English | [简体中文](README.zh-CN.md) | [日本語](./README.ja.md)

# SciVolume Academic Book Toolkit

**SciVolume Academic Book Toolkit** is an open-source collection of Markdown templates, editorial checklists, and a zero-dependency Python Crossref DOI verification script built for researchers, faculty, graduate students, and technical authors writing academic monographs, graduate textbooks, or scholarly non-fiction books. You can use it standalone in any Markdown, LaTeX, or Word workflow to draft a book proposal, map chapter-by-chapter argumentation, audit every bibliography entry against fabricated or mismatched citations, and check terminology, mathematical notation, figure numbering, and cross-references before submission. This toolkit is maintained by SciVolume, whose official website is [https://scivolume.ai](https://scivolume.ai).

---

## Repository Contents

```text
scivolume-academic-book-toolkit/
├── templates/                      # Bilingual templates (.md = EN, .zh-CN.md = ZH)
│   ├── book-proposal.md            # Academic book proposal template
│   ├── book-outline.md             # Full-book outline & chapter dependency map
│   ├── chapter-draft.md            # Single-chapter template (objectives, argument, figures, refs)
│   └── ai-disclosure.md            # Generic AI-assisted writing disclosure template
├── checklists/                     # Pre-submission editorial & citation checklists
│   ├── reference-verification.md   # 7-point per-reference anti-hallucination checklist
│   └── manuscript-consistency.md   # Full-book terminology, notation, figure & cross-ref checklist
└── tools/                          # Zero-dependency verification utilities
    ├── check_dois.py               # Pure-stdlib Crossref DOI checker (urllib)
    ├── README.md                   # Script documentation & verified sample output
    └── examples/
        └── refs-sample.bib         # Sample .bib (3 real Crossref works + 1 fabricated DOI)
```

### Templates (`templates/`)

| Document | English | 简体中文 | When to Use |
|---|---|---|---|
| **Book Proposal** | [`book-proposal.md`](templates/book-proposal.md) | [`book-proposal.zh-CN.md`](templates/book-proposal.zh-CN.md) | Pitching a monograph or textbook to an acquisitions editor (thesis, readership, comparable titles, annotated TOC, schedule) |
| **Full-Book Outline** | [`book-outline.md`](templates/book-outline.md) | [`book-outline.zh-CN.md`](templates/book-outline.zh-CN.md) | Planning chapter dependencies, word/figure budgets, and where core concepts and symbols are first defined |
| **Single-Chapter Draft** | [`chapter-draft.md`](templates/chapter-draft.md) | [`chapter-draft.zh-CN.md`](templates/chapter-draft.zh-CN.md) | Structuring chapter objectives, section-level claim–evidence chains, figure/table inventories, and verified references |
| **AI Usage Disclosure** | [`ai-disclosure.md`](templates/ai-disclosure.md) | [`ai-disclosure.zh-CN.md`](templates/ai-disclosure.zh-CN.md) | Logging AI assistance during drafting and preparing a generic front-matter or cover-letter disclosure statement |

### Checklists (`checklists/`)

| Checklist | English | 简体中文 | What It Audits |
|---|---|---|---|
| **Reference Verification** | [`reference-verification.md`](checklists/reference-verification.md) | [`reference-verification.zh-CN.md`](checklists/reference-verification.zh-CN.md) | Authors, title, year, journal/publisher, volume/issue/pages, DOI resolution & match, and whether the full text actually supports your claim |
| **Manuscript Consistency** | [`manuscript-consistency.md`](checklists/manuscript-consistency.md) | [`manuscript-consistency.zh-CN.md`](checklists/manuscript-consistency.zh-CN.md) | Canonical terminology, mathematical notation & units, sequential figure/table/equation numbering, and cross-chapter references |

---

## Quick Start: Verify DOIs Against Crossref

[`tools/check_dois.py`](tools/check_dois.py) uses only the Python 3 standard library (`urllib`)—no third-party packages required. It extracts DOIs from a `.bib`, `.md`, `.txt`, or `.tex` file, queries `https://api.crossref.org/works/<DOI>` with at least a 1-second interval between requests, prints the Crossref title and publication year for manual comparison, and separates network/API errors (`NETWORK_ERROR`) from non-existent DOIs (`NOT_FOUND`).

```bash
python3 tools/check_dois.py tools/examples/refs-sample.bib
```

Sample output on [`tools/examples/refs-sample.bib`](tools/examples/refs-sample.bib) (3 real scholarly references + 1 intentionally fabricated DOI):

```text
[1/4] DOI: 10.7208/chicago/9780226239873.001.0001 (@booth2016craft, line 9)
      Local    : The Craft of Research, Fourth Edition (2016)
      Status   : FOUND (exists in Crossref)
      Crossref : The Craft of Research, Fourth Edition (2016)
      Venue    : University of Chicago Press
...
[4/4] DOI: 10.1038/s41586-099-99999-z (@hallucinated2024synthetic, line 42)
      Local    : Automated Synthesis of Scholarly Monographs Without Source Grounding (2024)
      Status   : NOT_FOUND (does NOT exist in Crossref)
      Detail   : HTTP 404 Not Found (DOI not registered in Crossref)

--------------------------------------------------------------------
Summary: 4 checked | 3 found | 1 not found | 0 network error(s)
```

See [`tools/README.md`](tools/README.md) for all CLI options (`--delay`, `--timeout`, `--json`, `--strict`) and the complete sample run.

---

## Recommended Workflow for Writing an Academic Book Without Citation Hallucinations

1. **Lock the book spine before drafting chapters**: Fill out [`templates/book-outline.md`](templates/book-outline.md) so every chapter has a distinct thesis, word budget, prerequisite map, and designated home section for defining core terms and symbols.
2. **Ground every section in pre-verified sources**: In [`templates/chapter-draft.md`](templates/chapter-draft.md), map each section's claim to specific BibTeX keys and page numbers **before** expanding prose. If you use AI tools for drafting or translation, restrict them to your own notes and verified `.bib` records rather than letting models generate citations from memory.
3. **Run automated + manual citation checks**: Run `python3 tools/check_dois.py` to catch fabricated DOIs (`NOT_FOUND`) and swapped DOIs (where `Local` and `Crossref` titles disagree), then verify non-DOI books and full-text claim support with [`checklists/reference-verification.md`](checklists/reference-verification.md).
4. **Unify the assembled manuscript**: Before delivery, run through [`checklists/manuscript-consistency.md`](checklists/manuscript-consistency.md) and, where applicable, prepare transparent editorial notes with [`templates/ai-disclosure.md`](templates/ai-disclosure.md) after checking your target publisher's guidelines.

---

## Want to Automate This Workflow?

If you prefer an integrated workspace over maintaining standalone files, [SciVolume](https://scivolume.ai) supports serious non-fiction projects such as academic monographs and textbooks—from structuring an outline and drafting chapter by chapter (citing only author-approved references and uploaded PDF, DOCX, or BibTeX/RIS materials) to citation checking, scientific illustration (via SciDraw API), full-book translation across 6 languages, and export. Paid plans ($20/month Scholar, $50/month Pro, $150/month Studio, with annual billing options) export Word (`.docx`), LaTeX packages, EPUB 3, and print-ready PDF, while free accounts can browse public sample books along with sample full-book consistency and citation reports. Learn more at [https://scivolume.ai](https://scivolume.ai), [How SciVolume Writes a Sourced Book](https://scivolume.ai/blog/how-scivolume-writes-a-sourced-book), and [AI Academic Book Writing Tools Comparison](https://scivolume.ai/blog/ai-academic-book-writing-tools-comparison).

---

## License

- **Code** (`tools/*.py`): MIT License.
- **Documentation, templates, checklists, and images**: Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).
