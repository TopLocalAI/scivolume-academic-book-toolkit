English | [简体中文](manuscript-consistency.zh-CN.md)

# Pre-Submission Full-Manuscript Consistency Checklist

> **Why book-level consistency fails**: Chapters are often drafted months apart, adapted from earlier articles, co-authored by multiple contributors, or translated in batches. Even when each chapter reads well in isolation, subtle drift in **terminology, mathematical notation, figure/table numbering, and cross-references** undermines reader trust and slows copy-editing. Run this full-book pass once all chapters are assembled.

---

## 1. Terminology, Acronyms & Proper Nouns

- [ ] **One concept, one canonical term**: Core domain concepts use the exact same preferred term from Chapter 1 through the Conclusion (no unexplained switching between near-synonyms such as *"cost function"*, *"loss objective"*, and *"risk functional"* when referring to the same quantity).
- [ ] **First-mention definition rule**: Every specialized term is clearly defined at its designated first appearance in the book (and cross-checked against the Glossary if one is included).
- [ ] **Acronym expansion policy**: Choose one rule—either expand each acronym at its **first occurrence in the entire book** or at its **first occurrence in each chapter**—and apply it consistently everywhere.
- [ ] **Spelling, hyphenation & capitalization**:
  - Consistent English variety (`US` vs. `UK` spelling, e.g., *modeling/modelling*, *optimize/optimise*) across text, figure labels, and headings.
  - Consistent hyphenation of compound modifiers (e.g., *small-sample regime*, *state-of-the-art*, *non-linear* vs. *nonlinear*).
  - Consistent capitalization of named theorems, models, historical periods, and institutions.
- [ ] **Bilingual / translated terms** *(if applicable)*: Original-language terms in parentheses appear according to a single rule (e.g., at first appearance only) and match the back-matter term index.

---

## 2. Mathematical Symbols, Notation & Units

- [ ] **No silent symbol collisions**: A single symbol does not change meaning across chapters without explicit scoping (e.g., avoid using $N$ for sample size in Chapter 2 and number of layers in Chapter 5 if both appear together in Chapter 6).
- [ ] **Typographic conventions for math objects**:
  - Scalars / variables: italic ($x, t, \alpha$)
  - Vectors: consistent style throughout (e.g., bold lowercase $\mathbf{x}$ or arrow $\vec{x}$, never mixed)
  - Matrices / tensors: consistent style throughout (e.g., bold uppercase $\mathbf{X}$)
  - Sets / spaces / operators: upright or calligraphic applied uniformly ($\mathbb{R}^d$, $\mathcal{H}$, $\operatorname{argmin}$, $\mathrm{d}x$)
- [ ] **Indexing & bounds**: Subscript/superscript conventions ($i = 1, \dots, n$ vs. $i = 0, \dots, n-1$) and transpose/inverse/estimator marks ($\mathbf{X}^\top$ vs. $\mathbf{X}^T$, $\hat{\theta}$ vs. $\widehat{\theta}$) are uniform across prose, display equations, and figure axes.
- [ ] **Units, numbers & statistical reporting**:
  - SI units with non-breaking space between number and unit (`15 ms`, `20 °C`).
  - Consistent decimal precision, thousands separators, confidence interval format, and $p$-value formatting.
- [ ] **Master Notation Table sync**: Every symbol listed in the front-matter Notation Table actually appears in the book with that exact definition, and all multi-chapter symbols are included.

---

## 3. Figures, Tables, Boxes & Equation Numbering

- [ ] **Sequential double-numbered scheme**: Figures (`Figure 1.1`, `Figure 1.2`, ...), Tables (`Table 1.1`, ...), Boxes (`Box 2.1`, ...), and Equations (`(1.1)`, `(1.2)`, ...) follow an unbroken sequence within each chapter—no skipped numbers, duplicate numbers, or leftover draft IDs (`Fig 3.2a_new`).
- [ ] **Every visual is called out in text**: Every figure, table, and box has at least one explicit in-text callout (`see Figure 4.3`), and its first callout precedes (or sits adjacent to) the visual placement.
- [ ] **Callout style uniformity**: Decide between `Figure 3.1` vs. `Fig. 3.1` in running text and parenthetical references, and standardize across all chapters.
- [ ] **Caption & axis consistency**:
  - Figure captions (typically below) and table titles (typically above) follow uniform punctuation and phrasing style.
  - Terminology, variable symbols, and capitalization inside figure labels/legends match the main text and equations.
  - Units are stated in every table column header and plot axis label.
- [ ] **Print legibility & permissions**: Line weights, font sizes, grayscale/colorblind contrast, vector/DPI specs, and source/credit lines (`Source: Adapted from ...`) are verified for every figure and table.

---

## 4. Cross-References & Structural Links

- [ ] **Zero broken cross-references**: Search the compiled PDF/DOCX/LaTeX output for `??`, `Error! Reference source not found`, `[ref]`, `Chapter X`, `Section 0`, `TODO`, or `TBD`.
- [ ] **Chapter-reordering audit**: After any chapter split, merge, or reordering, verify all prose pointers (`"as derived in Chapter 3"`, `"in the preceding chapter"`, `"Section 5.4 below"`, `"Appendix B"`) point to the exact intended target.
- [ ] **Fulfilled forward & backward promises**:
  - Every forward promise (*"We return to this limitation in Section 7.3"*) is actually fulfilled in Section 7.3.
  - Every backward assumption (*"Recall from Chapter 2 that..."*) was indeed covered in Chapter 2.
- [ ] **TOC, running headers & lists**:
  - Table of Contents, List of Figures, and List of Tables match the exact final wording and numbering of headings and captions in the body text.
  - Heading hierarchy depth (e.g., up to 3 levels: `3` → `3.1` → `3.1.1`) is consistent across chapters, with no single-child subheadings (`3.1.1` without `3.1.2`).
- [ ] **Bibliography & Index sync**: All in-text citations resolve to the final bibliography (`checklists/reference-verification.md`), and index entries map to accurate terms/anchors.

---

## 5. Final Sign-Off Log

| Check Area | Checked By | Date | Issues Found & Resolved |
|---|---|---|---|
| 1. Terminology & Acronyms | `[Name]` | `[YYYY-MM-DD]` | `[e.g., Unified 14 occurrences of synonym drift]` |
| 2. Symbols, Equations & Units | `[Name]` | `[YYYY-MM-DD]` | `[e.g., Resolved symbol collision on \lambda in Ch. 4]` |
| 3. Figure/Table/Equation Numbering | `[Name]` | `[YYYY-MM-DD]` | `[e.g., Renumbered Figs 5.3–5.6; fixed axis symbols]` |
| 4. Cross-References & TOC | `[Name]` | `[YYYY-MM-DD]` | `[e.g., Fixed 3 stale section pointers after Ch. 6 split]` |
