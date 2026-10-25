# Does the WWOX-KO organoid carry the HIF1A -> PDK -> PDH transcript signature that the ketogenic-diet hypothesis requires? — prediction fixed BEFORE the genes were read

Declared 2026-10-25 by the Orchestrator. Exploratory. Not medical advice; no dose, route or suitability.
Everything below that is not WWOX data is NOT WWOX EVIDENCE.

## Why this and not another candidate
The hypotheses ledger ranks HYP-20260709-01 (ketogenic diet with a WWOX-specific rationale) 13/15 and `proposed-to-L9`, the highest
of the drug-like, variant-independent entries; the two above it are an endpoint and an allele-specific assay. It is a Track A
candidate (the rationale is not tied to a variant). Its chain is: loss of WWOX de-represses HIF1A, which raises PDK, which inhibits
PDH, which shifts glycolysis over oxidative phosphorylation, which ketone bodies bypass by entering the TCA cycle downstream of PDH.
The evidence for the chain is from mouse embryonic fibroblasts and cancer cells (DL-MECH-020); the human data point the other way
(cerebral lactate "extremely low", one complete human metabolic screen entirely normal; DL-BIO-008), and the ledger itself lists
the direction of human WWOX-deficient metabolism as unmeasured. The ledger names the organoid as the cheap test. This asks of the
one WWOX-knockout neural transcriptome on hand only whether the transcript signature of the chain is there.

## What this can and cannot say
- CAN say: whether, in 15-week WWOX-KO cerebral organoids, genes of the HIF1A-PDK-PDH-glycolysis axis move in the direction the chain predicts.
- CANNOT say: that flux, ATP, lactate or PDH activity changes (transcript is not flux; PDH is regulated by phosphorylation, which
  a transcriptome does not see); that the effect is WWOX-dependent rather than a composition or maturation signature (the six-library
  limit and the genotype-composition confound apply here exactly as they did for Wnt); that a diet would help.

## Gene sets, fixed now, each with its role in the chain
- HIF1A targets, glycolytic: SLC2A1 (GLUT1), HK2, PFKP, ALDOA, PGK1, ENO1, LDHA, PKM, BNIP3.
- PDK axis: PDK1, PDK2, PDK3, PDK4 (the PDH kinases); the PDH complex PDHA1, PDHB, DLAT, DLD, and the phosphatases PDP1, PDP2.
- Oxidative arm: NDUFA4, COX4I1, COX5A, ATP5F1A, CS, SDHA (a deliberately broad, boring panel).
- HIF1A itself and its regulators: HIF1A, EPAS1, EGLN1, VHL, ARNT.
- Ketone-use enzymes (can the tissue use ketone bodies at all): OXCT1, ACAT1, BDH1, HMGCS2, SLC16A1 (MCT1).

## Prediction (written before running)
P1. The glycolytic HIF1A targets are higher in KO (consistent with the chain); I expect SLC2A1, HK2, LDHA, PGK1 up.
P2. PDK1 (the isoform HIF1A induces) is up, and the PDH subunits are not down; the oxidative panel is flat or down.
P3. HIF1A itself is not raised at transcript level (HIF1A is controlled by stability, not mRNA), so a transcript-flat HIF1A is expected and is NOT counted against the chain.
P4. OXCT1 is expressed, so the tissue has the means to use ketones; this is a feasibility check, not support for efficacy.
P5. Any signature found will be partly mirrored by maturation (glycolytic genes fall as neurons mature), so each readout is
    checked against the elapsed-culture-time slope from GSE150123 before it is read as WWOX-dependent.

## What would change the reading
- Glycolytic targets flat or down, PDK1 not up: the chain has no transcript support in neural tissue, and the ledger's own rationale rests on non-neural cells alone.
- Glycolytic targets up AND falling with culture time in GSE150123: the signature is as consistent with an immature tissue as with a metabolic block, and is reported as such.
- OXCT1/BDH1 absent: the tissue could not use ketones, an independent reason to doubt the rationale.

## Limits fixed in advance
Six libraries; genotype and composition confounded; one laboratory. Uncorrected across the gene sets except where stated; set-level
tests use gene-set permutation against random sets from the same expressed universe, which is a coherence test and is post-selected
by construction (the gene sets were chosen from the chain, before reading, which is the only protection offered).

---

# RESULT (appended 2026-10-25, after the run; the prediction above is unchanged)

Script: `hif1a_pdk_chain.py` (reuses `maturation_calibration.py`; inputs pinned by digest). Set-level test: mean KO-versus-WT log2 shift
of each pre-declared set against 10,000 random same-size sets from the expressed universe (total count >= 10, 19,694 genes),
seed 20261025. One bug of my own was found and fixed mid-run, declared here: the first output showed every culture-time slope as
exactly +0.00 with mean count 0.0, which no real gene gives; the cause was a lookup by Ensembl id into a table keyed by symbol.

## The prediction, point by point
- **P1 (glycolytic HIF1A targets up): 3 of 4 held.** SLC2A1 +1.40 (padj 1e-9), HK2 +2.18 (padj 9e-34), LDHA +0.75 (padj 5e-6); PGK1 -0.09 did not move.
  Set level: mean +0.59, P = 0.003 against random sets.
- **P2 (PDK1 up, PDH not down, oxidative arm flat or down): PDK1 was FALSIFIED.** PDK1 is -0.34, not up; PDK2 -0.13; PDK3 +0.56 and PDK4
  +0.31 are at 10 and 3 counts per million, too low to carry a conclusion. The PDK set is +0.17 (P = 0.22), indistinguishable from chance.
  PDHA1 is UP (+1.00, padj 6e-10). The oxidative panel is flat (COX4I1 -0.33, padj 0.046, the rest within +-0.25).
- **P3 held:** HIF1A itself is -0.24 at transcript level, as expected for a gene regulated by stability; not counted against the chain.
  EPAS1 (HIF2A) is up, +1.41; ARNT +0.54.
- **P4 held weakly:** OXCT1 is expressed but at only 7 to 8 counts per million; BDH1 5.5; HMGCS2 about 3. The tissue has the enzymes,
  at low abundance. This is a feasibility check and says nothing about efficacy.
- **P5 mattered.** The three glycolytic genes that are up are also the genes that fall with elapsed culture time in GSE150123:
  SLC2A1 -2.16 [-3.66, -0.66], HK2 -2.15 [-4.10, -0.19], LDHA -1.89 [-3.07, -0.71] per log10 day, each between-line interval excluding
  zero. (Elapsed culture time, in WWOX-unperturbed spheroids of another laboratory; not cellular maturation.) So the glycolytic
  elevation is as consistent with a less advanced tissue as with a metabolic block. This is the opposite of the Wnt case, where the
  pivotal genes were flat after day 60; here the confound is plausible and the signature cannot be read as support on its own.

## What survives, at the strength it has
The pattern is **glycolytic targets up, PDK1 down, PDH subunit PDHA1 up, oxidative arm flat.** The ledger's chain needs
PDK to rise so that PDH is inhibited; the transcript data supply the first link (glycolytic genes) and not the middle one (PDK), and
the first link is the one a younger tissue would also produce. A pure immaturity signature would predict PDK1 falling with the glycolytic
genes, and PDK1 does fall with culture time (-1.08, interval includes zero), yet in the KO PDK1 is lower while the glycolytic genes are higher,
so neither the chain nor simple immaturity predicts this pattern. It is recorded as a discrepancy and not explained.

## What this does not establish
Flux, lactate, ATP, PDH activity or PDH phosphorylation (PDH is controlled post-translationally, which a transcriptome does not see);
that the glycolytic shift is WWOX-dependent; that a ketogenic diet would help; anything about patients. Six libraries,
genotype and composition confounded, one laboratory.

## The experiment this points at, and why it is better than another transcript analysis
Seahorse OCR/ECAR on the KO organoids the Aqeilan laboratory already holds, which the ledger names as the cheap test, now has a sharper
question: not "is there a glycolytic shift" (the transcripts say there is, and age confounds it) but "is PDH flux lower, and does it
recover with a ketone substrate given downstream of PDH?" Run in a matched-stage comparison, with oligomycin-resistant and substrate-
specific arms, it can separate a metabolic block from a less mature tissue because immaturity would not predict a ketone-rescuable
flux deficit. That is a wet experiment and nothing here claims it was performed.

## Set-level tests, reproduced from the committed script (`hif1a_pdk_chain.py --set-level`, 10,000 draws, seed 20261025)
These replace the figures first quoted from a terminal fragment, which were not in the repository; they differ in the second decimal
only because the fragment drew its two tails in separate loops and the script in one (same seed, different consumption of the sequence;
Monte Carlo noise, no change in meaning).

| set | n | mean KO shift | P(random >= observed) |
|---|---|---|---|
| HIF1A glycolytic targets | 9 | +0.585 | **0.0026** |
| PDK axis (PDK1-4, PDH subunits, phosphatases) | 10 | +0.170 | 0.2265 |
| oxidative arm | 6 | -0.068 | 0.8326 |
| HIF1A and regulators | 5 | +0.378 | 0.0655 |
| ketone use | 5 | +0.309 | 0.1017 |

The universe mean shift is +0.086, so a set at +0.17 is barely above the background. The two sets not discussed in the result text
are reported here so that only the favourable ones do not appear: HIF1A-and-regulators and ketone-use enzymes are mildly up and neither
exceeds chance. Five sets were tested; with one set at P = 0.003, the other four are not corrected for multiplicity and none is claimed.
