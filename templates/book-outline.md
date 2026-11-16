English | [简体中文](book-outline.zh-CN.md)

# Full-Book Outline & Chapter Architecture Template

> **Purpose**: Keep the entire book structurally coherent before and during chapter drafting. Unlike a brief proposal TOC, this working architecture maps chapter dependencies, word and figure budgets, where core concepts are first defined, and how the central thesis progresses from Chapter 1 to the Conclusion.

---

## 1. Book-Level Anchor

- **Book Title**: `[Working title and subtitle]`
- **Unifying Research Question**: `[What overarching question holds every chapter together?]`
- **Central Thesis / Spine**: `[1–3 sentences stating the core argument or analytical framework developed across the book.]`
- **Scope Boundaries**:
  - **In Scope**: `[Topics, periods, methods, or systems explicitly covered]`
  - **Out of Scope**: `[Topics intentionally excluded so chapters do not drift]`
- **Baseline Reader Profile**: `[Assumed background at Page 1]`
- **Citation & Bibliography Convention**: `[e.g., Author-date (Chicago / APA 7) or Numbered (IEEE / Vancouver); master BibTeX file path: refs/book.bib]`

---

## 2. Structural Arc & Chapter Dependency Map

> Verify that no chapter uses a concept, symbol, or method before the chapter that introduces it, and mark optional/advanced chapters for modular readers or instructors.

| Chapter | Part | Role in the Book's Arc | Prerequisite Chapters | Key Concepts / Symbols Introduced First Here | Target Words | Planned Figs / Tables | Draft Status |
|---|---|---|---|---|---|---|---|
| Ch. 1 | I | Problem framing & roadmap | None | `[Core domain terms A, B]` | `[7,500]` | `[2 / 1]` | `[Planned]` |
| Ch. 2 | I | Theoretical / mathematical foundations | Ch. 1 | `[Notation set X, Theorem 2.1]` | `[9,000]` | `[3 / 2]` | `[Drafting]` |
| Ch. 3 | II | Core methodology / mechanism | Ch. 2 | `[Algorithm / Analytical model M]` | `[10,000]` | `[4 / 2]` | `[Planned]` |
| Ch. 4 | II | Empirical / domain application I | Ch. 2, Ch. 3 | `[Dataset D1, evaluation metric E]` | `[9,500]` | `[4 / 3]` | `[Planned]` |
| Ch. 5 | II | Empirical / domain application II *(modular)* | Ch. 2, Ch. 3 | `[Case study protocol C]` | `[9,500]` | `[3 / 2]` | `[Planned]` |
| Ch. 6 | III | Synthesis, limitations & open problems | Ch. 1–5 | `[Synthesis taxonomy]` | `[7,000]` | `[1 / 2]` | `[Planned]` |
| **Total** | — | — | — | — | **`[52,500+]`** | **`[17 / 12]`** | — |

---

## 3. Part- and Chapter-Level Blueprint

### Front Matter
- **Preface**: Why this book exists, how different reader groups can navigate it (e.g., linear reading vs. fast-track syllabus paths), acknowledgments, and AI-assisted tool disclosure if applicable.
- **Notation & Abbreviations Table**: Master list of mathematical symbols, units, and acronyms used across multiple chapters.

---

### Part I: `[Part I Title — Problem Space & Foundations]`
- **Part Objective**: `[What shared foundation does the reader gain by the end of Part I?]`

#### Chapter 1: `[Chapter Title]`
- **Chapter Thesis**: `[One-sentence claim of Chapter 1]`
- **Bridge In**: Opens the book from a concrete motivating problem or paradox.
- **Section Skeleton**:
  - `1.1 [Motivating problem & historical context]` (`[~1,800 words]`)
  - `1.2 [Limitations of existing approaches]` (`[~2,000 words]`)
  - `1.3 [Overview of the book's analytical framework]` (`[~2,200 words]`)
  - `1.4 [How to read this book & chapter organization]` (`[~1,500 words]`)
- **Anchor Sources (Verified)**: `[@citekey1; @citekey2; @citekey3]`
- **Bridge Out → Ch. 2**: `[Why the motivating problem requires the formal definitions introduced in Chapter 2.]`

#### Chapter 2: `[Chapter Title]`
- **Chapter Thesis**: `[One-sentence claim of Chapter 2]`
- **Bridge In ← Ch. 1**: `[Connects problem statement in 1.2–1.3 to formal foundations.]`
- **Section Skeleton**:
  - `2.1 [Core definitions & assumptions]` (`[~2,500 words]`)
  - `2.2 [Baseline model / canonical theory]` (`[~3,000 words]`)
  - `2.3 [Boundary conditions & common misconceptions]` (`[~2,500 words]`)
  - `2.4 [Chapter summary & bibliographic notes]` (`[~1,000 words]`)
- **Anchor Sources (Verified)**: `[@citekey4; @citekey5]`
- **Bridge Out → Ch. 3**: `[Identifies what the baseline model cannot resolve without Chapter 3's method.]`

---

### Part II: `[Part II Title — Core Arguments, Methods & Case Studies]`
- **Part Objective**: `[How Part II develops, tests, and applies the central thesis across distinct dimensions or cases.]`

#### Chapter 3: `[Chapter Title]`
- **Chapter Thesis**: `[...]`
- **Bridge In ← Ch. 2**: `[...]`
- **Section Skeleton**:
  - `3.1 [...]` (`[~... words]`)
  - `3.2 [...]` (`[~... words]`)
  - `3.3 [...]` (`[~... words]`)
  - `3.4 [Summary & key takeaways]` (`[~... words]`)
- **Anchor Sources (Verified)**: `[@...]`
- **Bridge Out → Ch. 4**: `[...]`

*(Duplicate chapter block for Chapters 4..N-1)*

---

### Part III: `[Part III Title — Integration, Implications & Future Directions]`
- **Part Objective**: `[Pull threads together, address cross-cutting limitations, and articulate concrete open research questions.]`

#### Chapter N: `[Concluding Chapter Title]`
- **Chapter Thesis**: `[...]`
- **Bridge In ← Preceding Chapters**: `[...]`
- **Section Skeleton**:
  - `N.1 [Cross-chapter synthesis of findings]`
  - `N.2 [Methodological, empirical, or normative limitations]`
  - `N.3 [Open research agenda & practical implications]`
- **Anchor Sources (Verified)**: `[@...]`

---

## 4. Back Matter & Reference Apparatus Plan

- **Appendix A (`[Title]`)**: `[Long proofs, technical protocols, survey instruments, or data schemas moved out of main chapters to preserve narrative flow]`
- **Glossary**: `[Estimated number of defined core terms: e.g., 60–80 terms]`
- **Bibliography Policy**: `[Single unified bibliography at end of book vs. per-chapter references + cumulative bibliography — confirm early!]`
- **Index Plan**: `[Subject index only vs. combined Author + Subject index; maintain candidate index terms while drafting each chapter]`

---

## 5. Structural Self-Check Before Drafting Chapters

- [ ] Every chapter has a distinct one-sentence thesis rather than just a topic label.
- [ ] Word counts across chapters are reasonably balanced (no accidental 3,000-word stub next to a 22,000-word chapter without structural justification).
- [ ] Every technical term or mathematical symbol has a single designated "home section" where it is formally defined before being used elsewhere.
- [ ] Lengthy background derivations or raw tables that interrupt the core argument are assigned to appendices.
- [ ] Primary anchor references for each chapter are already verified and stored in the project `.bib` library.
