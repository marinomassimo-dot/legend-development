# GSE156243 - independent reanalysis: is the Wnt readout separable from organoid composition?

Status: EXPLORATORY, analyst-independent. Not medical advice; no dose, no suitability.
Contrast: WWOX knockout (cko1-4) vs wild type (cwt1-2), hESC-derived cerebral organoids, week 15, one laboratory.
This is a KNOCKOUT contrast: not Q230P, not a patient, not a rescue. Blind to the repository's own
Wnt prediction/permutation files and marker panels by design; panels below were chosen from memory of the
published single-cell cortical-organoid literature (NOT WWOX EVIDENCE; citations recalled, not re-verified
in this session): Pollen 2015 Cell; Camp 2015 PNAS; Nowakowski 2017 Science; Kanton 2019 Nature; Qian 2016 Cell;
Pellegrini 2020 Science (choroid-plexus organoids).

## Method
Salmon table (35,337 genes), CPM per library, log2(CPM+1). Library sizes 30.0-41.2 M. Panel score = mean of per-gene
z-scores across the 6 libraries.
- Wnt transcriptional readouts: AXIN2, LEF1, NKD1, APCDD1 (score "WNT"). Mediators/ligands (TCF7L2, WNT5A, CTNNB1) kept apart.
- RG (progenitor/radial glia): SOX2 PAX6 HES1 VIM NES FABP7 SLC1A3 PTPRZ1 TTYH1 HOPX SFRP1.
- NEU (neuronal): STMN2 DCX MAP2 SYT1 TUBB3 SNAP25 NEUROD2 NEUROD6 SLA GAP43 MAPT.
- CTX (dorsal-cortical identity): FOXG1 EMX1 EMX2 TBR1 LHX2 BCL11B SATB2.
- MID (non-cortical / hem-choroid-plexus-type identity): TTR LMX1A OTX2.
Models are z-scale OLS, y ~ 1 + KO + composition covariate(s); with n = 6 and 1 covariate there are 3 residual df.
Welch/OLS intervals use t quantiles; exact permutation over the 15 possible 2-vs-4 labelings.

## Results
1. Genotype contrast, unadjusted. All four Wnt readouts are higher in all four KO libraries than in both WT libraries
   (log2 KO-WT, Welch 95% CI): AXIN2 0.94 [0.65,1.23]; APCDD1 1.22 [0.40,2.05]; LEF1 1.15 [-0.46,2.76]; NKD1 1.46 [-0.76,3.67].
   Score difference 1.75 z (KO mean minus WT mean); KO min > WT max. With 2 vs 4 libraries there are only 15 labelings, so the
   smallest attainable exact permutation p is 1/15 = 0.067 (|difference| criterion); every readout sits exactly at that floor, i.e. no gene
   can look better than p = 0.067 by permutation whatever its effect size.
   The authors' DESeq2 padj (AXIN2 0.0126, LEF1 0.0122, NKD1 4.6e-4, APCDD1 8.6e-4) rests on parametric dispersion with n = 2 controls
   and is not reproducible as a rank statistic. Mediators: TCF7L2 +0.74 [0.33,1.15], CTNNB1 +0.61 [0.00,1.22], WNT5A +1.13 [-0.05,2.31].
2. Composition differs by genotype too: KO-WT in z units: RG +0.52, NEU -0.83, CTX -0.43, MID +1.52. Genotype is therefore partly
   collinear with every composition score (|r| 0.27-0.83 with KO). The Wnt shift (1.75) exceeds the RG, NEU and CTX shifts; it is
   comparable to the MID shift. Versus 20,000 random 4-gene sets of matched expression, a mean-z KO-WT of 1.75 is in the top 0.01%
   (null 95th pct 1.06) - but this is a statement about coordination of the four genes, not about independence of composition,
   and ~6% of genes are called DE here.
3. Inside the four knockouts (the only variation not confounded with genotype; n = 4). Pearson r, Wnt score vs RG +0.67, NEU -0.85,
   CTX -0.64, MID -0.01. With n = 4 an |r| below 0.95 is not significant and the 95% interval of r = 0.9 spans -0.45 to 1.00, so this
   comparison has almost no power: it can only detect near-perfect covariation. Direction is as a maturation story predicts (less neuronal,
   more Wnt; cko3 is lowest NEU/CTX and highest Wnt) but it is carried largely by one library: dropping cko3 turns r(Wnt,NEU) from -0.85
   to -0.42 and r(Wnt,CTX) to +0.41. Wnt does not track the hem/choroid-plexus-like panel (TTR is high in cko1/cko4, low in cko2/cko3).
   Within-KO Wnt score SD is 0.36 z against a genotype gap of 1.75 z.
4. Adjustment (n = 6, df = 3). KO coefficient on the Wnt score, z units [95% CI]: unadjusted 1.75 [0.92,2.58]; +RG 1.38 [0.40,2.37];
   +NEU 1.29 [0.26,2.32]; +CTX 1.66 [0.69,2.63]; +MID 1.81 [-0.17,3.80]; +RG-NEU axis 1.01 [0.71,1.31];
   +PC1 of the four panels 1.41 [-0.04,2.85]; +RG+NEU+CTX (df = 1) 1.02 [-1.66,3.70]. Per gene the pattern is weaker and heterogeneous:
   APCDD1 falls to 0.29-0.57 with NEU/axis/PC1 adjustment (CI includes 0), NKD1 CIs include 0 under most adjustments, AXIN2 and LEF1 hold
   more often. Resampling panel genes (3,000 draws) gives an adjusted KO coefficient median 1.13 [0.51,1.62] (RG-NEU axis) and 1.34 [0.65,1.82] (NEU),
   >0 in 99.9% - robust to which panel genes are used, not to the unobserved. Extrapolating the within-KO slope to the genotype shift
   in composition predicts 0.1-0.7 of the observed 1.75 z, with bootstrap intervals that cover 0 to the whole effect.
5. Leave-one-library-out: unadjusted score difference stays 1.64-2.01 z with every gene KO>WT on every drop; RG-NEU-adjusted
   coefficient 0.85-1.22 (df = 2, SEs tiny and not trustworthy). Direction is stable; precision is not testable.

## What six libraries can and cannot support
Can: a consistent KO>WT direction across all four readouts and all libraries; that the effect is not removed by any single
published-style composition covariate. Cannot: separate genotype from composition. With 2 WT libraries, genotype and any
composition difference are collinear by construction; a covariate adjustment removes only the part of composition measured
by noisy panel scores (measurement error leaves residual confounding, so the adjusted coefficient is biased toward the
unadjusted one), and cannot remove unmeasured states (hem, choroid-plexus, neural-crest-like, cell-cycle, hypoxia/metabolic
stress). A correlation across all six libraries is not reported as evidence here for that reason. The within-KO comparison,
the only unconfounded one, has near-zero power at n = 4. Authors' padj with two controls is not a protection.

## Verdict
(c) The data cannot decide, with a weak lean away from (b): the point estimates survive adjustment (about 25-45% attenuation for the
single-axis adjustments) and Wnt does not follow the MID panel inside the knockouts, but every adjusted interval is wide and the
within-KO estimate is compatible with composition explaining anywhere from ~0 to all of the shift. Confidence in (a): low. Confidence that
(b) is excluded: none.

Same conclusion as a reader taking the raw gene lists at face value? Same direction (Wnt readouts raised in KO, verified), different
conclusion about independence: the lists alone read as "Wnt up"; they do not address composition, and a face-value reader would
implicitly take (a).

## Single dataset that would decide
Single-cell (or sorted-population) RNA-seq of WWOX-KO vs isogenic WT organoids, >= 3 organoids per genotype from independent
batches, comparing AXIN2/LEF1/NKD1/APCDD1 within matched cell types (radial glia vs radial glia, neuron vs neuron). An acute
rescue (re-expression) in the same system would add a causal arm. NOT WWOX EVIDENCE: this is a design recommendation.
