English | [简体中文](chapter-draft.zh-CN.md)

# Single-Chapter Writing Template

> **How to use**: Duplicate this template for each chapter (`chapter-01.md`, `chapter-02.md`, ...). Fill out Sections 1–4 **before** writing full prose—especially if using AI writing or translation assistance—so every paragraph stays anchored to a clear argument, planned visuals, and verified sources.

---

## Chapter Metadata

- **Chapter Number & Title**: `Chapter [N]: [Chapter Title]`
- **Part**: `Part [I/II/III]: [Part Title]`
- **Target Word Count**: `[e.g., 8,500–10,000 words]`
- **Prerequisite Chapters**: `[e.g., Chapter 2 (Section 2.1 notation)]`
- **New Terms / Symbols Defined Here**: `[List terms and symbols formally introduced in this chapter]`
- **Draft Status**: `[Outline / First Draft / Citation Audit / Revised / Final]`

---

## 1. Chapter Objectives & Reader Takeaways

### 1.1 Core Question & Central Thesis
- **Driving Question**: `[What specific question does this chapter answer?]`
- **Central Claim (Thesis)**: `[State the main argument or conclusion of this chapter in 1–2 declarative sentences.]`

### 1.2 Concrete Objectives
After reading this chapter, the reader will be able to:
1. `[Objective 1: Define / explain core concept or mechanism X and its underlying assumptions.]`
2. `[Objective 2: Derive / apply method Y to problem class Z.]`
3. `[Objective 3: Evaluate empirical evidence, trade-offs, and failure modes of X/Y.]`

### 1.3 Cross-Chapter Continuity
- **Incoming Bridge (from Ch. `[N-1]`)**: `[What unresolved tension or foundation from the previous chapter launches this one?]`
- **Outgoing Bridge (to Ch. `[N+1]`)**: `[What capability or open question at the end of this chapter motivates the next one?]`

---

## 2. Argumentation Structure & Section Blueprint

### 2.1 Claim–Evidence–Analysis Matrix
> Map every section's logical role before drafting prose so no section degenerates into an unfocused literature dump.

| Section | Sub-Claim (What this section proves/establishes) | Primary Evidence / Data / Derivation | Verified Anchor Citations (`@citekey`, page/sec.) | Key Counterargument or Boundary Condition | Target Words |
|---|---|---|---|---|---|
| `N.1` | `[Motivating gap & roadmap]` | `[Concrete phenomenon / motivating example]` | `[@key1, pp. 14–18]` | `[Why naive solution fails]` | `[1,200]` |
| `N.2` | `[Theoretical / conceptual formulation]` | `[Formal definition + Proof / Mechanism]` | `[@key2, Sec. 3; @key3]` | `[Assumes condition C holds]` | `[2,800]` |
| `N.3` | `[Empirical validation / Case study]` | `[Dataset D / Historical archive / Experiment]` | `[@key4; @key5, Table 2]` | `[Measurement limits & external validity]` | `[3,000]` |
| `N.4` | `[Comparative discussion & synthesis]` | `[Cross-method comparison table]` | `[@key2; @key6]` | `[Trade-off between accuracy and cost]` | `[1,500]` |
| `N.5` | `[Summary & bridge to next chapter]` | `[Synthesis of N.1–N.4 takeaways]` | — | `[Scope left for Chapter N+1]` | `[500]` |

### 2.2 Drafting Workspace

#### `N.1 [Opening & Problem Framing]`
`[Draft prose here. Open with the concrete problem, state the chapter thesis explicitly, and preview Sections N.2–N.4.]`

#### `N.2 [Core Concept / Theoretical Development]`
`[Draft prose here. State definitions before theorems/claims; align all mathematical notation with the book-wide symbol table.]`

#### `N.3 [Empirical Analysis / Worked Case / Application]`
`[Draft prose here. Walk through data, derivations, or case evidence; reference planned figures and tables explicitly in the text.]`

#### `N.4 [Limitations, Edge Cases & Discussion]`
`[Draft prose here. Address competing interpretations, boundary conditions, and unresolved edge cases candidly.]`

#### `N.5 [Chapter Summary]`
`[Bullet or concise paragraph recap of the 3–5 main takeaways + transition sentence to Chapter N+1.]`

---

## 3. Figures, Tables & Equations Inventory

> Every visual element must earn its space by clarifying a structure, trend, or comparison faster than prose alone, and must be called out explicitly in the text (e.g., *"as shown in Figure 3.2"*).

| ID | Type (`Fig` / `Table` / `Box`) | Planned Caption & Core Takeaway | First In-Text Callout | Source / Rights Status | File Path & Format Specs | Status |
|---|---|---|---|---|---|---|
| `Fig N.1` | Schematic | `[Architecture / conceptual relationship of X and Y]` | `Sec. N.2` | `[Original by author (CC BY 4.0)]` | `figures/chN-fig01.svg` (vector) | `[Planned]` |
| `Fig N.2` | Data plot | `[Empirical comparison across conditions A, B, C]` | `Sec. N.3` | `[Re-plotted from public data @key4]` | `figures/chN-fig02.pdf` (300+ DPI) | `[Drafted]` |
| `Table N.1` | Comparison table | `[Assumptions, complexity, and failure modes of methods]` | `Sec. N.4` | `[Original synthesis]` | Inline Markdown / LaTeX | `[Done]` |

### Numbered Equations Log *(if applicable)*
- `Eq. (N.1)`: `[Name/meaning — symbols checked against global notation table? Yes/No]`
- `Eq. (N.2)`: `[Name/meaning — symbols checked against global notation table? Yes/No]`

---

## 4. Reference Requirements & Source-Grounding Rules

### 4.1 Chapter Citation Standards
1. **Primary Sources First**: Cite the original work that introduced a theorem, dataset, concept, or empirical finding rather than relying solely on secondary review articles or textbooks.
2. **Zero Unverified AI Citations**: Never allow an LLM or drafting assistant to invent bibliography entries or guess DOIs from memory. Every cited work must exist in your verified `.bib` file **before** or **during** paragraph drafting.
3. **Page / Section Pinpointing**: When citing books, monographs, or long papers, record exact page numbers, chapters, or theorem/table numbers (`[@booth2016craft, ch. 7, pp. 105–112]`) so claims can be audited quickly.
4. **Claim–Source Fidelity**: Verify in the original text that the cited work genuinely supports your exact statement (not merely a loosely related keyword).

### 4.2 Chapter Reference Verification Table
> Run `python3 tools/check_dois.py` on your `.bib` file and verify full-text alignment before marking this chapter complete.

| Citekey | DOI / ISBN | `check_dois.py` Result | Metadata Matched? | Full Text Read & Supports Claim? | Exact Page / Section Cited |
|---|---|---|---|---|---|
| `@key1` | `10.xxxx/...` | `[FOUND]` | `[Yes]` | `[Yes — checked by Author]` | `[pp. 14–18]` |
| `@key2` | `10.xxxx/...` | `[FOUND]` | `[Yes]` | `[Yes — checked by Author]` | `[Sec. 3.2, Table 1]` |
| `@bookKey` | `ISBN 978-...` | `[N/A — ISBN checked]` | `[Yes]` | `[Yes — checked by Author]` | `[Ch. 4, pp. 88–94]` |

---

## 5. Pre-Handoff Chapter Sign-Off

- [ ] Chapter thesis stated clearly in Section `N.1` and substantiated across `N.2`–`N.4`.
- [ ] All terms and mathematical symbols match the book-wide glossary and notation table.
- [ ] Every figure and table is numbered sequentially, cited in the main text, and cleared of third-party copyright issues.
- [ ] Zero `[TODO]` or `[CITATION NEEDED]` placeholders remain.
- [ ] Every reference in this chapter passed `tools/check_dois.py` (or manual ISBN/catalog lookup) and full-text claim verification (`checklists/reference-verification.md`).
