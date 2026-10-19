# HELD-partial wave 2026-10-19 — scientist-c (WWOX-direct partial receipts)

Task HELD-PARTIAL-WWOX-C-20261019 · branch task/HELD-PARTIAL-WWOX-C-20261019 · worktree
`.claude/worktrees/held-c`. English; nothing here is medical advice; public, disease-level edition.
Per paper: what it MEASURES (system, genotype, tissue, readout) and what that changes or fails to
change in the disease model. The negative is the product. No novelty is claimed; no hypothesis is
promoted to a claim.

Reading discipline: every re-read is `QUESTION_DRIVEN` (`reread_reason: inadequate_prior_coverage`,
`prior_receipt` set). The question below was written, and committed, **before** any owed section
(figure image, supplement, table) was opened. The comparison phase, where it is written, follows the
line `FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON`.
Receipts are staged under `receipt_staging/scientist-c/`, not appended.

## 0. Lot construction and de-duplication

Source rows: the HELD-partial sections of `metabolic_batch_selection_20261019.md` and
`interventions_batch_selection_20261019.md`, cross-checked against the ledger (a census of the
latest contemporaneous receipts per PMID) and `paper_packet.py packet`. Several selection rows are
stale: the ledger shows later receipts (waves 12 and 13, 2026-10-04) that closed some debts the
selection file still lists.

Excluded, with reason:

| PMID | Reason |
|---|---|
| 26355344, 27551439, 35984507, 41677633 | already re-read in this batch and staged under `receipt_staging/scientist-c/` (tasks METAB-G3-C and INTERV-H4-C, same actor) |
| 25649963 | only references owed (latest receipt: every body section read) |
| 33914858 | no owed section on the audited surface |
| 30158849 | review; owed = abstract, introduction, references only |
| scientist-a, -b, -d staged PMIDs | other lots (checked: no overlap with the twelve below) |

Lot (12): 35328751, 37897534, 38542478, 33195192, 42589397, 40875931, 36537114, 35460704,
33612478, 31543760, 24308844, 33958783.

## 1. Stated questions (written before the owed sections were opened)

| PMID | Held before reading | Question |
|---|---|---|
| 35328751 Baryla 2022 | Selection row: owed = figure panels (captions only), Figures S1-S6 (previously unavailable; now present on disk), references. | In the figure panels not yet seen as images (including S1-S6), what is measured per genotype/condition in the glucose-metabolism arm (cell type, WWOX manipulation, readout, n), and does any panel carry a direction or magnitude the running text states differently or omits? Is any neural cell type present? |
| 37897534 Cheng 2023 | Selection row: figures captions only; senescence escape via cytosolic ROS. | Which figure panels carry the ROS and NAC-rescue data, in which cells (Wwox-null MEF passage, human fibroblast knockdown, HEK293T), with what n and what readout, and does any panel connect to a metabolic (mitochondrial, glucose, lactate) readout? |
| 38542478 Zfra overrides WWOX | Selection row: figures captions only. | Do the figure panels contain any WWOX-null/knockdown arm with a metabolic, mitochondrial or ROS readout, or are all panels Zfra-treatment effects on a WWOX-replete background? |
| 33195192 Wwox-deficient skin, ERK | Receipt: figures captions only, references not read. | In the main-figure panels, which genotype (global null vs conditional), age and tissue carry the ERK and homeostasis readouts, and is a systemic (hypoglycaemia, growth) confounder visible in any panel? |
| 42589397 Hammouz 2026 | Selection row: figures and supplement not read; the supplement was read by a producer-only receipt. | In the main figures, what per-subtype WWOX/HIF1A ratio and survival direction is plotted, and does it agree in sign with the running text and the supplementary tables already read? |
| 40875931 Gao 2025 | Selection row: worth reopening only for "does any cohort record haemoglobin, anaemia or transfusion?" | Does any figure or table in the full text record haemoglobin, anaemia, transfusion, feeding, growth, hypoglycaemia or diet response in WWOX-DEE patients? |
| 36537114 Chong 2023 | Selection row: body not acquired (non-open-access). | Once a body is lawfully acquired: what does Table 1 and the text say about ketogenic-diet exposure and response, and how many individuals were exposed? |
| 35460704 Dong 2022 | Selection row: LDLR panel as image. | In the figure panels, what is the WWOX-variant carrier lipid phenotype versus controls, and is the LDLR panel about WWOX or about another gene? |
| 33612478 Liu 2021 | Selection row: figures, supplementary and references owed. | Which WWOX SNP/haplotype, which lipid trait, which direction and which sample, as drawn in the figures, and is any WWOX-specific signal isolated from the gene-gene and gene-environment panels? |
| 31543760 Kosla 2019 | Selection row: abstract/introduction not read, figure captions only. | In the figures (and the 23 undeclared on-disk files), is any differentially expressed gene set after WWOX knockdown in neural progenitors metabolic (lipid, glucose, mitochondrial) rather than synaptic/neurite? |
| 24308844 Schuchardt 2013 | Selection row: figures, methods, tables owed; binding biophysics. | Does any figure or table speak to metabolism or only to ErbB4 ICD / WW1 binding (negative expected)? |
| 33958783 Liu 2021 GWAS | Selection row: supplement not read. | Does the supplementary table carry a WWOX-locus effect size, direction and per-cohort consistency that the main text does not, and does it name any metabolic annotation? |
