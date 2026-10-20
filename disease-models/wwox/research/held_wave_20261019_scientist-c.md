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

---

## 4. PMID 38542478 — Chen 2024 review "Zfra overrides WWOX in suppressing neurodegeneration" — receipt FTR-20261019-38542478-02

**What it MEASURES.** Nothing new: a perspective review. The seven figures are curcumin/calebin-A
structures (Fig 1), a table of percentage ranges "tabulated and summarized" from a cited DRG study
(Fig 2A), two summary schematics (Figs 3, 7), a Zfra-conjugation schematic (Fig 4), a heatmap of
fold-increases in WWOX co-immunoprecipitation from peptide-treated 4T1-bearing BALB/c mice with PBS
as the zero reference (Fig 5B) and three-field pT12-WWOX immunostains of 11-month Wwox+/- versus +/+
cortex (Fig 6A), all cited from earlier work.

**Question and answer.** No figure contains a WWOX-null or knockdown arm with a metabolic,
mitochondrial or ROS readout; every treatment panel is Zfra or WWOX-peptide effect on a WWOX-replete
background. The one genotype-level panel (6A) is a heterozygote cortex immunostain with no counts, no
animal number and no antibody control. The negative is complete for the figures. Entry 3 (the high-glucose
Y33 phosphorylation sentence) therefore stays a cited sentence with no panel behind it in this article.

**Effect on the model.** None. The review is a source of citations, not of observations; Fig 5B
supports at most "peptide-treated WWOX-replete mice show co-IP changes in cancer-bearing animals", not
any neural or metabolic statement. Receipt closes figures; depth carried at the prior receipt's level.
MINOR; no commit candidate.

---

## 5. PMID 33195192 — Chou 2020 (Wwox-/- mouse skin, ERK, homeostasis) — receipt FTR-20261019-33195192-03

**What it MEASURES.** System: constitutive whole-body Wwox knockout mouse and littermates, skin and body
temperature, mostly P20-P21 (one to two weeks before the lethality window the Introduction states);
primary keratinocytes; HaCaT shWWOX. Readouts: epidermal thickness and hydration, K5/K10, Ki67, BrdU,
hair-follicle length and stem markers, pERK, p63, and (Figure 8) subcutaneous fat layer, FABP4 and
skin surface temperature.

**Question and answer.** (1) Genotype/age/tissue: whole-body null versus +/+ and +/-, P20-P21, dorsal skin
(heterozygote indistinguishable from wild type on every quantified endpoint). (2) The metabolic content
of the paper is Figure 8, which no earlier locator covered: the subcutaneous fat layer is about 10 um in
the null versus about 270 um in controls (n = 3), the few remaining FABP4 cells are shrunken and
lipid-free, and dorsal skin surface temperature is 31.3 C versus 35.8 C (n = 15 versus 12). (3) A
systemic confounder is visible but unquantified: the Figure 4 photographs show the null pup smaller
from P2 and the smallest at P14-P20, and the article reports no body weight, glycaemia or intake. The
causal sentence "the loss of subcutaneous fat causes hypothermia" is untested; fat loss and hypothermia
are equally two readouts of one wasting state. (4) pERK (Figure 7A) is a region-level comparison, 25
regions from 3 mice. (5) Onset: follicle length equal at P0, shorter from P3 onward, consistent with a
systemic growth effect superimposed on the local keratinocyte phenotype that the paper does not
separate.

**What it does not support.** A cell-autonomous adipose defect (no conditional or adipocyte-specific
arm); that fat loss drives hypothermia; any neural statement; any ERK readout as a biomarker (already
rejected, DIS-027).

**Effect on the model.** PAPER 129's role sentence names the pERK observation and the dose statement but
not Figure 8. The figure is a second independent constitutive-null readout of lipid or energy
economy next to the serum-lipid and hypoglycaemia reports already in the record, with the same
failure-to-thrive confound. Candidate: `CC-20261019-SCIENTIST-C-HELD-01` (MINOR).

---

## 6. PMID 42589397 — Hammouz 2026 (WWOX/HIF1A balance, breast and ovarian tumours) — receipt FTR-20261019-42589397-05

**What it MEASURES.** System: bulk tumour RNA-seq cohorts (618 patients, five strata: four breast
subtypes and ovarian carcinoma). The "genotype" is a stratum of the WWOX/HIF1A transcript ratio
(subtype-specific maxstat cutpoint), not a WWOX perturbation. Readouts: Notch-gene differential
expression, KEGG over-representation, Hallmark GSEA, MCPcounter immune scores.

**Question and answer.** The question I wrote assumed a survival panel among the main figures. There is
none: Figures 1-5 are Notch-gene violins, a KEGG bubble plot, a Hallmark heatmap and two immune-score
boxplot sets; the Kaplan-Meier curves are in the supplement. That part of the question is closed as
mis-specified (an error of the lot construction, not of the paper). What the figures do carry for the
metabolic theme is Figure 3: glycolysis and hypoxia Hallmark sets are enriched in the low-ratio group in
four of five strata, MYC targets in the high-ratio group in all five, and there is no oxidative
phosphorylation row in Figure 3 or Figure 2 although the Results say high ratios go with "enhanced
oxidative phosphorylation". The glycolytic signature does not track prognosis (low-ratio is the
better-DFS group in luminal A, luminal B and OV, the worse in basal-like), HIF1A sits in the ratio's
denominator so the low group is partly selected for high HIF1A transcript (Figure 1, p = 5.9e-08), and
the enrichments are exploratory trends at FDR up to 0.25.

**What it does not support.** Any statement about WWOX loss or neural tissue; an oxidative-phosphorylation
shift (no panel); a prognostic role of the glycolytic signature.

**Comparison phase.** FIRST-PASS OBSERVATIONS COMPLETE -> PRIOR KNOWLEDGE ADMITTED FOR COMPARISON: the
manifest's seven locators (all text) and CLAIM 025's evidence boundary. Effect: CLAIM 025's boundary
stays; the glycolysis-for-low-ratio statement, if cited for RL-003, must carry the circularity and the
non-tracking-of-DFS qualifications. The manifest keeps five inherited waived deep-dive slots
(group, field density, multihop, cross-query, retraction): its verdict is PASS with those five declared
gaps, unchanged by this re-read.

---

## 7. PMID 35460704 — Dong 2022 (exome sequencing, hypoalphalipoproteinaemia) — receipt FTR-20261019-35460704-03

**What it MEASURES.** A human cohort with low HDL-C, exome sequencing, rare damaging heterozygous variants in
104 HDL candidate genes against controls; WWOX is one of eleven candidate genes with the highest
occurrence count (four occurrences, three distinct missense alleles; no association, no copy-number event).

**Question and answer.** The row asked about the LDLR panel. Figure 2, acquired from the PMC OA bucket
(it had never been on disk) and opened as an image, is a map and table of 14 rare heterozygous LDLR
variants with per-carrier lipids (HDL-C 23-36, LDL-C above 170 in most). It contains no WWOX datum.
The question "what is the WWOX carrier lipid phenotype in the figure panels" is therefore answered:
none is plotted; WWOX appears only in Supplemental Table S4, already read.

**Effect on the model.** None; the earlier boundary (an occurrence count inside a candidate list, no
comparator, a benign-annotated common allele carrying two of four occurrences) is untouched. The re-read
closes the figure debt; references remain unread.

---

## 8. PMID 33612478 — Liu 2021 (TUBB and WWOX SNPs, haplotypes, dyslipidaemia) — receipt FTR-20261019-33612478-02

**What it MEASURES.** A cross-sectional sample of Maonan adults in southern China (864 normolipidaemic
and 1129 dyslipidaemic; Table 3's header prints 1229, a typo the haplotype counts of 1728 and 2258
haplotypes confirm), four common SNPs (two TUBB, WWOX rs2222896 and rs2548861), serum lipids, haplotypes
and gene-environment interactions. A genotype-association study of common variants; no WWOX function,
expression or perturbation.

**Question and answer (figures opened for the first time).** Which SNP, trait, direction: the rs2222896 G
allele goes with higher LDL-C and lower HDL-C and ApoA1 in the normal group (Figure 1 B, C, D), the
rs2548861 T allele only in the dyslipidaemic group; haplotypes G-G and G-T raise, A-T and A-G lower, the
dyslipidaemia odds. The effects behind the stars are about 0.1-0.2 per carrier (Tables 4, 7) and are
invisible at the plotted axis scale. Is any WWOX-specific signal isolated? No: the TUBB and WWOX SNPs
are in moderate-to-high LD (D' 0.34-0.79, Figure 2), the gene-gene interaction trees cluster them, and
the dyslipidaemia-group comparisons are selected on the outcome. Three findings the earlier text-only
reading could not see: (i) Table 6 prints the G-T haplotype odds ratio as 111.055 with a CI of
7.818-15.633 that excludes it (the geometric midpoint is 11.05: a stray digit, inferred from the
arithmetic), against an adjusted 15.08 (9.24-24.60) in Figure 4; (ii) D' between the two WWOX SNPs is
0.87 and 0.81, so "weak LD" in the Discussion describes r2 only; (iii) a haplotype of two common SNPs with an
odds ratio of 11-15 and frequencies 0.020 against 0.190 is unexplained by the paper and is not replicated.

**What it does not support.** Any statement about WWOX function, dose, loss-of-function or a rare damaging
allele (SNP selection was restricted to common variants, as the existing locator records); a lipid
effect specific to WWOX; the authors themselves withdraw the rs2548861 HDL-C association.

**Effect on the model.** Strengthens the existing negative: the best this record can be cited for is a
hypothesis-generating common-variant association in one population with a flagged internal error.
MINOR; the printed-OR error is passed to the Orchestrator through the commit candidate.
