# Metabolic wave 2026-10-19 — scientist-c, group G3 (mitochondria, iron, ferroptosis)

Task METAB-G3-C-20261019 · branch task/METAB-G3-C-20261019 · lot: group G3 of
`metabolic_batch_selection_20261019.md`, tier order. English; nothing here is medical advice; public,
disease-level edition. Per paper: what it MEASURES (system, genotype, tissue, readout) and what that
changes or fails to change in the disease model. The negative is the product. No novelty is claimed;
no hypothesis is promoted to a claim.

Reading discipline: first pass `SOURCE_FIRST` unless stated; comparison phase opened only after the
locators were captured (`FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON`,
named per paper). Receipts are staged under `receipt_staging/scientist-c/`, not appended.

---

## 1. PMID 26355344 — Sze 2015, Cell Death Dis (HELD-partial, re-read with a stated question)

context_policy: QUESTION_DRIVEN. Held before reading: the selection file's statement that the prior
receipt covered introduction and discussion only and results, methods, figures and tables were owed;
the prior receipt (it already carried a genre finding). Stated question: does this deposit contain
any Results, Methods, table or figure DATA on mitochondria under WWOX loss that the earlier reading
missed?

**First pass (artefact: NCBI efetch JATS of PMC4650446, the publisher PDF, and Figure 1 as a 200 dpi
page render; all in the shared `files/` tree).** The deposit is JATS `article-type="news"`: two PDF
pages, no abstract, no Methods, no Results, no table, ten references and exactly one figure, a
two-panel schematic. Figure 1 was opened as an image: panel a draws nucleolus-mitochondrion shuttling
of TPC6A, panel b draws routes i-iii of an aggregation cascade; it carries no axis, scale bar, n or
micrograph. The text restates, with reference numbers, the senior laboratory's own results (the
primary is a different PMID in this repository). The Europe PMC supplementary bundle for the deposit
contains only the figure in two formats.

**Answer to the stated question: no.** The sections the earlier receipt called "owed" do not exist in
this article, so the earlier partial coverage was in fact the whole text. The row is not an
unfinished primary; it is a finished News and Commentary. Its depth is therefore closed at
`complete_fulltext_read` for the article as published, with `abstract`, `methods`, `results`,
`tables`, `limitations` and `supplementary` recorded `not_present`, and `prior_receipt` naming the
partial event with `inadequate_prior_coverage`.

**What it measures:** nothing. It is a self-commentary by the founding laboratory.

**Comparison phase (PRIOR KNOWLEDGE ADMITTED: the registry records for this PMID, one hop).** The
paper registry and the tracking log hold a triage-only placeholder (tier B, "secondary full-text
target", pathway P5). The discovery ledger lead DL-MECH-019 lists this deposit as one of three
sources next to its two primaries. That counts a commentary as an independent source for an SDR
binding map it can only restate. Effect on the model: none gained; one source count corrected (a
commentary is not a fourth observation of the TPC6A-delta / SDR binding). The mitochondria-in-WWOX-null
-neurons question remains answered only by the primary (a separate partial row, listed in the selection
file under HELD with supplement captions owed) and the Drosophila respiration paper that is already
read. Selection-file consequence for the Orchestrator: a PMC XML larger than 5 kB did not imply a
Results section; "OA XML" in the route column should be paired with the JATS `article-type`.
