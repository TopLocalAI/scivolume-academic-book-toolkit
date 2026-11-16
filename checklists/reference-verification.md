English | [简体中文](reference-verification.zh-CN.md)

# Reference Verification Checklist (Anti-Hallucination & Citation Audit)

> **Why this checklist matters**: In academic books—especially when drafting, translating, or reformatting with AI tools—citation errors rarely look obviously broken. Common failure modes include **plausible-looking fabricated titles** paired with real scholar names, **non-existent DOIs**, **real DOIs attached to the wrong article ("swapped DOIs")**, and **real papers cited for claims they never made**. Every reference in your manuscript should pass all 7 verification items below before submission.

---

## Step 0: Automated Batch Pre-Screen

1. Run [`tools/check_dois.py`](../tools/check_dois.py) on your `.bib` library or chapter files:
   ```bash
   python3 tools/check_dois.py path/to/references.bib --strict
   ```
2. Flag every `NOT_FOUND` entry for immediate investigation or removal.
3. For any `NETWORK_ERROR` entry, re-run after checking network connectivity—never treat a transient network failure as proof that a DOI is fake, and never assume it is valid without re-checking.
4. Separate entries **without a DOI** (archival sources, older monographs, standards, policy reports, non-Crossref publications) into a manual lookup list to verify via ISBN, publisher catalog, WorldCat, PubMed, arXiv, or national library catalogs.

---

## Step 1: Per-Reference 7-Point Verification Checklist

Check **every** bibliography entry against these 7 items:

### 1. Authors / Editors
- [ ] Every author's surname and given name/initials match the published work exactly (no misspelled names, dropped middle initials that alter identity, or truncated co-author lists unless required by your citation style's *et al.* threshold).
- [ ] Author order matches the original publication.
- [ ] For edited volumes, book editors (`ed.` / `eds.`) are not confused with chapter authors.
- *AI Hallucination Watch*: LLMs frequently combine two real researchers in the same field as co-authors on a paper they never wrote together.

### 2. Title & Subtitle
- [ ] Main title and subtitle match the official publication word for word.
- [ ] Proper nouns, chemical/mathematical symbols, species names, and capitalization rules (sentence case vs. title case per your style guide) are preserved accurately.
- [ ] Book edition (`2nd ed.`, `4th ed.`, `Revised ed.`) is specified when citing anything other than a first edition, since pagination and claims often change across editions.
- *AI Hallucination Watch*: Paraphrased or keyword-stuffed titles that echo your own manuscript sentence are a classic sign of a fabricated reference.

### 3. Publication Year
- [ ] Publication year matches the canonical version of record (distinguish *Online First / Early View* year from final print volume year consistently).
- [ ] In-text parenthetical year (e.g., `Smith (2021)`) matches the bibliography entry year (`2021`).
- [ ] Multiple works by the same author(s) in the same year are disambiguated (`2021a`, `2021b`) consistently in both text and bibliography.
- [ ] Preprints (`arXiv`, `bioRxiv`, `SSRN`) that have since been peer-reviewed and published in a journal or proceedings are updated to their published version of record.

### 4. Journal, Conference, or Publisher
- [ ] Journal title (or standard ISO 4 abbreviation, applied consistently across the book) belongs to a real, verifiable venue.
- [ ] Conference proceedings include the accurate conference name/acronym and publisher (e.g., ACM, IEEE, PMLR, ACL).
- [ ] Books and monographs list the exact publisher name (and publication city if required by your house style).
- *AI Hallucination Watch*: Watch out for "chimera journal names" that blend words from two real journals (e.g., *Journal of Computational and Applied Machine Intelligence*).

### 5. Volume, Issue, Page Range / Article Number / ISBN
- [ ] Volume number, issue number, and inclusive page range (`436–444`) or electronic article identifier (`e2304129120`, `Article 14`) match the publisher record.
- [ ] Cited chapter in an edited volume includes both chapter inclusive pages and book editor(s).
- [ ] Books without DOIs include a verified 10- or 13-digit ISBN where available.
- *AI Hallucination Watch*: Generative models routinely guess plausible volume and page numbers even when citing a real paper—always verify numbers against Crossref or the publisher landing page.

### 6. DOI Resolution & Metadata Match
- [ ] The DOI resolves cleanly (`FOUND` in `check_dois.py` or `https://doi.org/<DOI>` HTTP 200).
- [ ] **Crucial**: The landing page / Crossref record returned by that DOI shows the **exact same title, authors, and year** as your bibliography entry—not a completely different article!
- [ ] DOI formatting follows your target press's style consistently across all entries (either `https://doi.org/10.xxxx/...` URLs everywhere or `doi:10.xxxx/...` everywhere).

### 7. Claim–Source Alignment (Does the Content Actually Support Your Text?)
- [ ] **Original source inspected**: An author has opened the actual paper, book chapter, or dataset—not just read an abstract snippet or secondary citation.
- [ ] **Substantive support**: The cited passage genuinely establishes the theorem, empirical number, historical fact, or argument attributed to it in your manuscript.
- [ ] **No stance inversion**: A view that the cited author *criticized* or *hypothesized as a baseline* is not mistakenly cited as the cited author's own conclusion.
- [ ] **Accurate numerical/quote transcription**: Any quoted wording, sample size, effect size, $p$-value, or date matches the source verbatim, with exact page/table/section recorded (`pp. 105–107`, `Table 3`).
- [ ] **Primary over secondary**: Where a review paper merely summarizes an earlier primary study, you have checked and cited the original primary study (or explicitly cited both).

---

## Step 2: Cross-Checking In-Text Citations vs. Bibliography

- [ ] Every in-text citation has a corresponding entry in the chapter or book bibliography (zero orphan citations).
- [ ] Every bibliography entry is actually cited in the text (unless the press explicitly requests a separate *Further Reading* list, labeled as such).
- [ ] Duplicate BibTeX entries for the same work under different keys (`@smith2020` and `@smith_2020_ml`) have been merged.
- [ ] Retracted articles or superseded errata have been checked (verify if any foundational empirical source has a published retraction or correction notice).

---

## Step 3: Copy-Paste Audit Log Table (Per Chapter)

| Citekey | 1. Authors | 2. Title | 3. Year | 4. Venue/Press | 5. Vol/Issue/Pages | 6. DOI Resolves & Matches | 7. Full Text Supports Claim (Page/Sec.) | Reviewer & Date |
|---|---|---|---|---|---|---|---|---|
| `@booth2016craft` | `[x]` | `[x]` | `[x]` | `[x]` | `[x]` | `[x]` | `[x] Ch. 7, pp. 105–112` | `[Initials, YYYY-MM-DD]` |
| `@lecun2015deep` | `[x]` | `[x]` | `[x]` | `[x]` | `[x]` | `[x]` | `[x] p. 438` | `[Initials, YYYY-MM-DD]` |
| `@...` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | `[ ]` | |
