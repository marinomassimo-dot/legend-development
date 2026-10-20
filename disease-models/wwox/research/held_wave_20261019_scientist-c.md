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

---

## 2. PMID 35328751 — Baryla 2022 (WWOX/HIF1A axis and glucose metabolism, human fibroblasts) — receipt FTR-20261019-35328751-04

**What it MEASURES.** System: immortalised human skin fibroblast line 1BR.3.N, in vitro, four
oxygen x glucose conditions (19% or 1% O2; 5.5 or 25 mM glucose), 6 h (HRE reporter, fractionation,
immunofluorescence) or 48 h (uptake, qPCR, enzymes, whole-lysate blots). Genotype: a CRISPR/Cas9
sgRNA depletion called "KO" (protein about 0.05 versus 0.43 WWOX/GAPDH, mRNA about 3-fold lower,
polyclonal) and a lentiviral overexpression arm (hundreds-fold by blot and qPCR, about 2.5-3-fold by
immunofluorescence). Readouts: HRE-luciferase, 2-deoxyglucose uptake (uM, serum-free), mRNA of 13
glycolytic/TCA genes, HK/LDH/PDH/CS activity, lactate, HK2/PKM2/LDHA/GLUT1 protein, HIF1alpha
distribution. No neural cell, no animal, no respiration, ATP or ROS readout.

**Question and answer (stated before opening the figures).** Panels 1-4, 7-12 and S1-S6 were opened as
images. The text is faithfully drawn from the panels for the quantities it quotes; what the panels add
is condition structure the Discussion does not carry.

1. Uptake does not rise with WWOX loss in general. Figure 3: knockdown exceeds control only in
   normoxia normoglycaemia; no knockdown-versus-control bracket in normoxia hyperglycaemia or hypoxia
   normoglycaemia; lower than control in hypoxia hyperglycaemia. The Discussion sentence "glucose
   uptake, both insulin-dependent and independent, was upregulated in WWOX KO cells" is true of one
   condition of four (entry 14 `panel_qualifies_text`). The overexpression arm (Figure S1b) also
   lowers uptake in both hypoxia conditions, so uptake is not monotonic in WWOX dose.
2. Hypoxia plus hyperglycaemia is not a depleted-versus-replete contrast: WWOX mRNA is not lower in
   knockdown there (Figure 4a, no bracket) and the Figure 8 text says total protein is unchanged.
   The reduced uptake and PFK1/PKM2 changes reported for that condition cannot be read as WWOX dose
   effects.
3. The transporter arm is mRNA plus function: GLUT1 protein shows no knockdown bracket in any
   condition (Figure 7e); GLUT4 protein is never measured despite an eight-fold SLC2A4 mRNA rise.
4. Overexpression and knockdown move several nodes in the same direction (PDK and ENO1 mRNA up in
   normoxia normoglycaemia in both, Figure S2 versus 4; lactate up in both, S3d versus 5): the
   readouts are not dose-faithful. Only HK2 and LDHA protein agree across arms (up with loss, down
   with gain, normoxia normoglycaemia).
5. Internal inconsistencies found: Methods 4.6 fractionation at 6 h versus Figure S4 caption 48 h;
   uptake run in serum-free medium for 48 h in every condition (a serum-deprivation confound that
   the paper's Methods state and its Results do not mention); densitometry scales differ between
   Figure 1d (about 350-fold) and S4 (about 9-24-fold) for the same cells; panels show a single
   representative blot lane per genotype; micrographs carry no scale bar.

**What it does not support.** Any neural or developmental statement; any in vivo statement; "knockout"
(partial depletion); a general rise in glucose uptake; an oxidative-arm change (citrate synthase and
PDH unchanged, already locator 3). The only readout that moves the same way under every loss
condition remains medium lactate (entry 7, prior reading).

**Comparison phase.** FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: the
2026-10-04 manifest locators (read before appending). Effect: the earlier receipt's partial status is
reduced to references and abstract; the supplement (all of S1-S6) is now read as images. Consequence for
the model: no baseline claim changes; RL-003's metabolic-biomarker line gains the explicit statement
that a carrier-detectable *uptake* readout would need the oxygen, glucose and serum condition named,
and that lactate (fibroblast) is the one direction-stable readout. Class: MINOR, no commit candidate
needed beyond the manifest (no registry record text is contradicted).

---

## 3. PMID 37897534 — Cheng 2023 (Wwox loss, senescence escape, genome instability) — receipt FTR-20261019-37897534-03

**What it MEASURES.** System: primary mouse embryonic fibroblasts, serial passage in vitro (early,
intermediate, late; passages 1, 8, 20), several Wwox-/- clones against Wwox+/- (heterozygote) and, in
places, Wwox+/+; plus lentiviral shWWOX in HEK293T and human dermal fibroblasts (supplement). Readouts:
gamma-H2AX, SA-beta-gal, p16/p21/p53 protein, promoter methylation, microsatellite instability, DHE
flow cytometry, NAC rescue, Agilent redox-gene heatmap. No mitochondrial, glucose, lactate or ATP
readout anywhere.

**Question and answer.** The ROS panel is Figure 6a, which an earlier wave recorded as not read after a
classifier halt; it opened without difficulty. (1) The ROS datum is one representative DHE histogram per
passage with no quantification, n or clone identifier: at early passage the genotypes overlap, at late
passage the null curve is right-shifted. (2) The NAC rescue is real at its stated endpoints (SA-beta-gal
about 1.5% null versus 35% null+NAC versus 35% wild type; p16, p21, p53 restored while WWOX stays absent)
but ROS is not re-measured in NAC-treated cells. (3) The p53 mutations that the model figure says ROS
"causes" were found in one null clone of several; no panel sequences NAC-treated cells. (4) p16 or p21
re-expression alone restores senescence in null cells (Figure 3), so the lesion is downstream of WWOX,
not rescued by WWOX re-supply (no WWOX re-expression arm exists). (5) Supplementary Figure 8: an
early-passage redox transcript signature (G6pdx, Nfe2l2, Nqo1, Sod3, others; all higher in null,
one sample per genotype, unexplained gene selection) precedes any measurable ROS difference.
(6) Comparator is the heterozygote in most panels.

**Connection to the metabolic theme: the only link is ROS, and ROS is one trace in a culture-adapted
fibroblast system.** The paper cannot be cited as showing a WWOX-null metabolic state; the
G6pdx/Nfe2l2/Nqo1 heatmap is the one place it touches metabolism (pentose-phosphate and NRF2 axis) and
is an unreplicated transcript panel on newly isolated cells.

**Comparison phase.** FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON:
the manifest's prior seven locators. No prior locator is contradicted; entry 1 (the NAC rescue as the
only therapeutic-direction lead) is qualified: the lead is "an antioxidant restores the senescence
phenotype in passaged null MEFs", with no ROS confirmation in treated cells and no relation to
neurons. MINOR; no commit candidate (no registry record text is contradicted).
