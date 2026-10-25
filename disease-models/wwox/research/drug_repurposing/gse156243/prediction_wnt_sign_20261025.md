# GSE156243 — Wnt-axis sign test: prediction fixed BEFORE the permutation was run

Declared 2026-10-25 by the Orchestrator. Exploratory. NOT a Q230P result, NOT a child, NOT a rescue contrast: this is a
WWOX-knockout versus wild-type hESC-derived cerebral organoid contrast (week 15, four KO and two WT libraries).
Not medical advice; no dose, route or suitability. Everything below that is not WWOX data is NOT WWOX EVIDENCE.

## The question
The repurposing hypotheses on the Wnt/GSK3/CK1 side disagree in SIGN: one family (tankyrase inhibition, XAV939-like) assumes
loss of WWOX leaves the canonical Wnt readout TOO HIGH and that lowering it is the correction; the other (GSK3 inhibition,
CHIR99021-like, lithium) assumes it is TOO LOW. A drug cannot be chosen until the direction of the lesion is known in a
neural system. The 2026-10-24 read of the organoid list already showed seven canonical Wnt/β-catenin targets and
mediators on it, all UP. This test asks whether that coherence exceeds chance, and does not ask the question the
data cannot answer.

## What this can and cannot say
- CAN say: whether the WWOX-KO organoid transcriptome carries an excess of same-signed canonical Wnt readouts relative to
  gene sets of the same size drawn from the same expressed universe.
- CANNOT say: that the effect is Q230P-specific, that it is cell-autonomous (composition and maturation differ between
  KO and WT: neuronal markers lower, regional-identity genes raised and uneven), that Wnt activity is causal for the
  phenotype, or that any drug corrects it. It is one laboratory, one line, n = 4 against 2.

## Gene sets, fixed now
- W7 (observed, already seen): AXIN2, LEF1, TCF7L2, NKD1, APCDD1, WNT5A, CTNNB1.
- W-READOUT (stricter, transcriptional readouts only, excludes ligands and mediators): AXIN2, LEF1, NKD1, APCDD1.
- Null: 10,000 random gene sets of the same size drawn from the counts-file proxy universe (total count >= 10), seed 20261025.
  The test statistic is the number of set members that are padj <= 0.05 AND up, and separately the mean signed log2FC.
- Composition sensitivity: repeat after removing every gene in marker_sets_declared.tsv from BOTH the observed set and
  the null universe.

## Prediction (written before running)
P1. W-READOUT up-count (4 of 4) exceeds the null at p < 0.01.   Expected to HOLD.
P2. The result survives the composition removal.               Expected to be WEAKER; if p rises above 0.05 the
    Wnt signal is not separable from a maturation difference and the conclusion is downgraded accordingly.
P3. The Wnt-up result does NOT make the tankyrase family correct. It selects between the two sign hypotheses at the level
    of the readout only, and says nothing about CK1-alpha (no CSNK1A1 or GSK3 gene is on the list at all).

## What would falsify the reading
- W-READOUT not exceeding the null: the seven-up observation is a selection artefact of looking at a handful of
  well-known genes in a list of 1,897.
- The signal vanishing under composition removal: it is a maturation effect, not a WWOX-dependent Wnt change.

---

# RESULT (appended 2026-10-25, after the run; the prediction above is unchanged)

Script: `wnt_sign_permutation.py` (seed 20261025, 10,000 draws, expressed universe 19,694 = total count >= 10).

## What held
- **P1 held.** The four transcriptional Wnt readouts (AXIN2, LEF1, NKD1, APCDD1) are 4 of 4 up, mean log2FC +1.12,
  p = 0.0001 on the count and 0.0058 on the mean against random sets of the same size. The wider seven (adding TCF7L2,
  WNT5A, CTNNB1) is 7 of 7 up, p = 0.0001. The coherence is not a selection artefact of looking at a handful of
  famous genes. Of the 22 canonical Wnt genes checked, 7 are on the list, all up; none is down.
- **No GSK3 or CK1 gene is on the list at all** (0 of 7: GSK3A, GSK3B, CSNK1A1, CSNK1D, CSNK1E, TNKS, TNKS2), and none of
  CACNA1G/H/I. The data say nothing about those nodes, in either direction.

## What did NOT hold, and a design error of mine
- **The declared composition sensitivity (P2) was circular as written.** The marker file contains a `wnt_pathway`
  module holding AXIN2, LEF1 and WNT5A, so "remove every marker" removed the genes under test and left two. The first
  run did exactly that and gave 2 of 2. Corrected to remove only the seven composition modules. That corrected
  sensitivity is IDENTICAL to the full result (no Wnt gene sits in a composition module), which makes it a WEAK control:
  it shows only that those 77 declared markers do not account for the Wnt genes, not that composition in general does not.
- **The harder control is inconclusive and points the wrong way for the simple reading.** Across the six libraries the
  Wnt-readout score correlates +0.99 with a radial-glia/progenitor score, -0.97 with a neuronal score and +0.87 with a
  non-cortical regional-patterning score (OTX2, LHX5, GATA3, HOXA2, SHH, ATOH1, DRGX, log2FC up to +4.2). With four KO
  and two WT libraries every signal that differs by genotype will correlate this strongly, so the number does not show
  that Wnt FOLLOWS maturation; it shows the data cannot tell the two apart. Within the four KO libraries the two orderings
  agree (cko3 highest on both, cko4 lowest on both), which is suggestive and, at n = 4, not evidence.

## Reading, stated at the strength it has
EXPLORATORY HYPOTHESIS, weaker than it looked before the controls. In this WWOX-knockout organoid the canonical Wnt readout
is raised, coherently and beyond chance. Whether that is a WWOX-dependent change in Wnt signalling or a downstream
signature of an altered, less mature, regionally-shifted tissue CANNOT be decided from this dataset. It does not favour
the tankyrase-inhibitor family or the GSK3-inhibitor family; it only fixes the SIGN of the readout, and only in a knockout.

## The discriminating next test (not performed; needs a wet or a different-data step)
1. **A rescue contrast.** Re-express WWOX in the KO organoid (or compare isogenic KO with its parental line) and read
   AXIN2/LEF1/NKD1/APCDD1 together with the progenitor and regional panels. If Wnt returns to wild type while the
   progenitor and regional signatures do NOT, Wnt is a WWOX-dependent readout dissociable from maturation. If all move
   together, the Wnt change is part of the maturation phenotype and is not a drug target on this evidence.
2. **A maturation-matched comparison.** Compare KO against a younger wild-type time point matched on the neuronal score
   (the dataset has one time point, week 15, so this needs a different dataset or new libraries).
3. **A reporter read.** A TCF/LEF reporter in the KO line under the same conditions measures pathway activity directly
   instead of inferring it from transcript abundance, which composition also moves.
The minimum evidence needed for a drug experiment is (1): without a rescue arm no pharmacological result in this
organoid can be attributed to Wnt rather than to the maturation state.

---

# SECOND ANALYST, SAME DATA (appended 2026-10-25) — it agrees on direction and sharpens the limit

**Independent in the analyst, not in the data.** The second analysis chose its own marker panels and did not see
this file, which protects against my choices and my bias. It used the same six libraries, so it is a second
reading of one dataset and adds no biological replication. GSE156243 is the deposit of the 2021 organoid
paper (PMID 34268881) and the 2026 paper comes from the same laboratory; none of the Wnt observations in this
folder is a biologically independent confirmation of another. Agreement between two analysts of one dataset
means the arithmetic is robust to who does it, and nothing about whether the biology replicates.


A second analyst, who was told not to read this file or its script, took the raw counts and chose her own panels
(`independent_reanalysis_wnt_vs_maturation_20261025.md`). Verdict: **the data cannot decide** whether the Wnt
change is independent of composition, with a weak lean away from "downstream marker" and low confidence in
"independent". Same direction as above (all four readouts higher in all four KO libraries than in both WT); a
different conclusion on independence from a reader who took the raw gene lists at face value, who would
implicitly assume it is independent.

## A limit of my own result that must travel with it
My p = 0.0001 is a **gene-set** statistic: how unusual it is that four named genes all sit on the list and all go up,
against random sets of genes from the same universe. It is **not** a test across libraries. With two WT and four KO
libraries the smallest p any single gene can reach by permuting the genotype labels is 1/15 = 0.067, so no one gene
can do better. The two statements are both true and answer different questions; only the first is mine.

## Numbers from the second analysis worth keeping
- Per-gene log2 difference KO minus WT: AXIN2 0.94 [0.65, 1.23], APCDD1 1.22 [0.40, 2.05], LEF1 1.15 [-0.46, 2.76],
  NKD1 1.46 [-0.76, 3.67]. Two of four intervals include zero.
- After adjusting for a composition score (n = 6, 3 df) the KO coefficient on the Wnt score falls from 1.75 to
  1.0 to 1.4 depending on the adjuster and remains positive for three of four; per gene it is weaker, with APCDD1
  falling to 0.3 to 0.6 and its interval spanning zero. A noisy panel under-adjusts and unmeasured states cannot be removed.
- Inside the four KO libraries (the only variation not confounded with genotype) the Wnt score correlates -0.85
  with a neuronal panel and +0.67 with a progenitor panel, at near-zero power (significance needs |r| about 0.95
  at n = 4) and carried by one library: dropping cko3 gives -0.42.
- Leaving out any one library keeps the direction.

## What would decide it, agreed by both analyses
Single-cell or sorted-population RNA-seq of KO versus isogenic wild-type organoids, at least three per genotype,
comparing the four readouts WITHIN matched cell types; or the WWOX re-expression contrast specified above.
