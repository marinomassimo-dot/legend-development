# Glial-reactivity thread: what the organoid panel is asked, and what would count, fixed BEFORE the data were opened

Declared 2026-10-29 by `scientist-a` (task `task/it6-p10`). Exploratory; not WWOX evidence of benefit; no medical advice.
Everything not measured in a WWOX-deficient system is NOT WWOX EVIDENCE.

## The question
The mouse records say glial reactivity is raised in constitutive and missense models (astroglial markers up, cytokine
transcripts up), is lowered by neuron-restricted gene replacement, and goes the OTHER way in a Wwox-mutant rat cortex
(lower GFAP and Iba1 expression). All of those brains seize or have seized. The GSE156243 organoids (WWOX knockout against
wild type, week 15, four against two libraries, one laboratory) are a human neuron-containing tissue in which the
astroglial lineage is present but there is no microglia and no behavioural seizure. They can therefore answer one narrow
thing about the transcriptome: is a reactive or inflammatory astroglial programme present when neuronal WWOX is lost
WITHOUT overt seizures and WITHOUT microglia, or is the difference in this tissue a lineage-maturity difference?

## Gene sets (fixed now; symbols as HGNC)
- microglia_presence: AIF1, P2RY12, TMEM119, CX3CR1, CSF1R, PTPRC, TREM2
- astroglial_lineage_homeostatic: GFAP, AQP4, S100B, ALDH1L1, SLC1A2, SLC1A3, GJA1, GLUL, KCNJ10, ADK, SOX9, NFIA, HOPX, FABP7
- reactive_pan: C3, SERPINA3, LCN2, CD44, CHI3L1, VIM, TIMP1, CEBPD, STAT3, SOCS3
- cytokine_inflammasome: IL1B, IL6, TNF, NLRP3, IL1R1, NFKB1, RELA, CCL2, CXCL8, TGFB1

## Predictions (written before running; each can be wrong)
P1. Microglia markers are at or near zero in all six libraries (no microglia in a cortical organoid), so the microglial
    arm of the glial question is untestable in this tissue. If AIF1/P2RY12/TMEM119/CX3CR1 are clearly expressed, the
    tissue is not the one assumed and every later line is read with that.
P2. The astroglial lineage markers differ between KO and WT in the direction of the already-known maturity shift of
    this deposit (KO less mature on neuronal markers), not as a coherent reactive signature.
P3. The pan-reactive markers (C3, SERPINA3, LCN2, CHI3L1) are NOT raised in the KO libraries.
P4. The cytokine/inflammasome set is not raised (KO/WT mean CPM ratio below 1.5 for IL1B, IL6, TNF, NLRP3).

## Decision rule (descriptive, six libraries cannot carry a test)
A gene counts as RAISED only if all four KO libraries exceed the larger of the two WT libraries in CPM AND the
KO/WT mean-CPM ratio is at least 1.5; LOWERED is the mirror image; otherwise NOT SEPARATED. A set counts as a
"seizure-independent reactive programme" only if at least half of the reactive_pan genes expressed above 5 CPM in any
library are RAISED. Genes with fewer than 20 raw counts in every library are reported as NOT INFORMATIVE, never as
unchanged.

## What would change the reading
- Reactive_pan majority RAISED: gliosis is at least partly a neuron-intrinsic, seizure-independent human signal and the
  seizure-driven explanation loses its monopoly (still one laboratory, 4 v 2 libraries).
- No reactive signature and a maturity shift only (P2+P3 as predicted): the human tissue offers no support for a
  seizure-independent reactive programme, which fits (does not prove) the seizure-driven reading.
- Anything else is reported as it comes.

## Limits fixed in advance
Bulk RNA, six libraries, four against two, different library counts, no test, no cell-type resolution, week 15 only.
A transcript is not a protein and an organoid astroglia is not a gliotic adult cortex. No dose, route or suitability.
