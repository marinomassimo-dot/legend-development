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

---

## 2. PMID 36364214 — Liu 2022, Molecules: "WWOX Modulates ROS-Dependent Senescence in Bladder Cancer" (tier 1, new)

context_policy: SOURCE_FIRST (selection row's one-line "why it matters" was the only thing held; the
registry was opened only after the locators were captured).

**What it MEASURES.** System: AY-27 rat bladder carcinoma cells in vitro, and an F344 rat orthotopic
AY-27 tumour, day 14. Manipulation: lentiviral WWOX OVERexpression (LV-WWOX, about 2-fold over empty
vector by Western blot, Fig 1b: roughly 5.0 control, 6.2 LV, 12.5 LV-WWOX in the paper's units).
Readouts: proliferation (MTS) and wound closure; WWOX and TNF-alpha by Western blot and
immunofluorescence; ROS as DHE-positive area; SA-beta-gal positive cells; p21 and p27 by Western
blot; tumour volume; p21 IHC. Every comparison is LV-WWOX against uninfected cells and empty vector.
There is no knockdown, knockout, null, neuronal or mitochondrial arm.

**First-pass observations (figures opened at native size).**
- ROS is one DHE stain (control about 13 percent, LV about 31, LV-WWOX about 90 percent positive
  area, Fig 3f). The text says "superoxide and hydrogen peroxide"; DHE reports superoxide-type
  oxidation and not hydrogen peroxide, and no scavenger or mitochondrial probe accompanies it.
- "ROS-dependent" senescence rests on exendin-4 (Fig 4c): one unquantified micrograph per
  condition; no ROS measurement under exendin-4 is reported. Exendin-4 is introduced by citation as a
  ROS-reducing agent; the paper does not show that it did that here. The causal word in the title is
  therefore carried by an illustration.
- Fig 2a shows the LV-WWOX culture as sparse rounded clusters, and the authors' own conclusion says
  "cytotoxicity and the induction of senescence"; overexpression toxicity is a live competitor to a
  senescence-specific reading, and p21/p27 rises (1.4 to 2.6-fold) are modest.
- The abstract claims increased SASP; the body contains the term only in the introduction and
  defines it there (measured in this session on the text rendering: two hits, abstract and
  introduction); no SASP assay is reported. TNF-alpha is the only secreted-factor-type readout.
- Fig 5b: bar heights read by eye are about 12.3 (control), 13.1 (LV), 3.7 mm3 (LV-WWOX). The
  quoted 30.49 and 28.60 percent equal LV-WWOX as a fraction of control and of LV, so the tumour
  volume fell by roughly 70 percent in this plot while the abstract and text say 30.49 percent
  reduction (INFERENZA from approximate bar heights; the values are not tabulated; no n per group is
  stated in the legend or text; recorded as a `panel_qualifies_text` locator).
- Fig 5d compares unlike compartments: control and LV p21 fields are tumour sheets, the LV-WWOX
  field is folded urothelium over connective tissue; no score. It does not show p21 in tumour cells.
- Methods contain an epirubicin-hydrogel cytotoxicity assay and a lentivirus release assay that the
  Results never report, and the Discussion cites GFP-/RFP-tagged proteins where Methods describe
  antibodies, so the Methods text is not fully the experiment that was run.

FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: admitted the registry records
for this PMID (two unprocessed stubs, one discovery-ledger mention), CLAIM 009 and CLAIM 034 (the sign
of the WWOX-ROS relation), and the dossier of the Drosophila Wwox/ROS paper.

**Comparison.** The repository holds the WWOX-ROS sign as a context-dependent question: CLAIM 009
(deficiency read as coherent with ROS increase, held `in observation`) carries a counter-directional
note from a diabetic mouse photoreceptor (knockdown lowers superoxide), and the Drosophila paper
reads dose and ROS as positively related (overexpression lines raise the CM-H2DCFDA-positive
fraction, loss-of-function mutants lower it). Liu 2022 is a third system with the same local sign
(WWOX up, ROS up), obtained by overexpression in a tumour line. It therefore adds one more
observation that the "deficiency means high ROS" shortcut is not a law, and nothing toward the
opposite law: it has no loss arm, so it cannot say whether loss lowers ROS in bladder cells. A
discovery-ledger line (the corpus note following DL-MECH-057) lists this PMID among already-read
records; no receipt existed, so the earlier "read" was a declaration, and this is its first receipted
reading.

**What it changes in the disease model: almost nothing, and the direction of the nothing matters.**
Transfer to the reference genotype is poor on four independent axes: direction (gain, not loss),
tissue and species (rat urothelial carcinoma, not neurons), no mitochondrial quantity measured, and
the ROS-dependence claim is illustrated rather than shown. What survives: a third system for the
local sign (PAPER-level support for the context principle in CLAIM 034, MINOR), and a methodological
caution for any ROS-lowering rationale (NAC, CoQ10, creatine) built on CLAIM 009: the sign of the
WWOX-ROS relation has now been seen positive in a fly, a mouse photoreceptor and a rat tumour line,
and in none of them in a WWOX-null neuron. RL-003 (metabolic line) is not changed.
