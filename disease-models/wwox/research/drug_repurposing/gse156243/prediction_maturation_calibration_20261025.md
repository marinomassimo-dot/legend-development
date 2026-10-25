# Can maturation alone account for the size of the Wnt elevation in the WWOX-KO organoid? — prediction fixed BEFORE the data were opened

Declared 2026-10-25 by the Orchestrator. Exploratory. Not medical advice; no dose, route or suitability.
Everything below that is not WWOX data is NOT WWOX EVIDENCE.

## The question
The Wnt readouts (AXIN2, LEF1, NKD1, APCDD1) are raised about 2.2-fold (log2 +1.1) in the GSE156243 KO organoids
(week 15, four KO against two WT libraries). The 2026 paper of the same laboratory shows in its own single-cell
data that canonical Wnt is higher in EARLY cells. The six libraries cannot say whether the KO elevation is a
WWOX-dependent signalling change or a maturation signature. A different, public, WWOX-free dataset can calibrate
one thing the six libraries cannot: how much these genes move with maturation ALONE in normal tissue.

## The dataset, and what it is not
GSE150123: 62 samples of human cortical spheroids sampled from about 25 to more than 650 days in culture, wild type
(NCBI GEO summary: long-term maturation). Different laboratory, protocol, line family and platform from GSE156243.
It calibrates the DIRECTION and rough SIZE of a maturation effect on these genes. It cannot correct the KO data,
cannot say what the KO tissue's true maturity is, and says nothing about WWOX.

## The calculation (fixed now)
1. In GSE150123, for each Wnt readout g and each maturation marker m, fit log2 expression against log10 days in culture
   and also fit log2 g against log2 m. The slope b(g|m) = d log2 g / d log2 m is the normal-development coupling.
2. Maturation markers, fixed now and chosen for presence in both datasets: progenitor (VIM, NES, SOX9, SOX2, PAX6, HES1),
   neuronal (STMN2, MAP2, SYT1, RBFOX3, TUBB3, SNAP25). A marker is used only if it is expressed in both datasets.
3. In GSE156243, take the KO-versus-WT log2 shift d_m of each marker from the deposited counts.
4. PREDICTED Wnt shift from maturation alone = b(g|m) x d_m, per gene and per marker, with the spread over markers.
5. Compare with the OBSERVED log2 shift of g. Report observed, predicted, and the fraction of observed explained.

## Prediction (written before running)
P1. In GSE150123 the Wnt readouts DECLINE with days in culture (negative slope), as the 2026 paper's single-cell
    result implies. If they do not decline, the maturation-confound mechanism has no support in independent tissue.
P2. The predicted shift is in the right direction (positive) for the KO, because the KO is less mature on neuronal markers.
P3. The predicted shift explains only PART of the observed +1.1: I expect between 20 and 70 percent, with a wide spread.
    This is a guess recorded so it can be wrong. A prediction of nearly all would make the Wnt elevation a maturation
    artefact on this evidence; nearly none would mean maturation does not touch these genes.

## What would change the reading
- Fraction explained near or above 100 percent in most marker choices: the elevation is plausibly maturation alone.
- Fraction near zero or negative: maturation, as these markers measure it, does not account for it.
- Large disagreement across markers (progenitor markers say one thing, neuronal another): the calibration does not
  constrain the question, and that is reported as the result.

## Limits fixed in advance
Two datasets from different laboratories are compared on log-scale slopes, never on absolute values. A slope fitted over
a 25-to-650-day range is applied to a difference that spans a much smaller maturity gap at one time point, which assumes
the relation is linear on the log scale over that range; this is checked, not assumed. Six KO/WT libraries remain six.
The result is a plausibility bound on one explanation, not a measurement of WWOX-dependent signalling.

---

# RESULT (appended 2026-10-25, after the run; the prediction above is unchanged)

Script: `maturation_calibration.py`. Data: GSE150123 (62 wild-type cortical-spheroid samples, 25 to 652 days, six iPSC
lines, 12 MB, fingerprinted in `files/geo/GSE150123/`, sha256 of the tar `347efe3e75ba167488cbe058645ffab1a1921869bc9ef161b6106a8374470a72`) and the
KO-versus-WT shifts from GSE156243. Declared deviations from the pre-registration are listed first because they matter.

## Deviations, declared
1. **The marker route was mis-specified and is abandoned.** The pre-registered chain was Wnt-on-marker slope times the marker's
   KO shift. The declared maturation markers hardly track the day axis in GSE150123 (within-line r² 0.00 to 0.25; STMN2, MAP2,
   SYT1, RBFOX3, SOX2 and NES are flat), so that route returned a predicted Wnt shift near zero for every gene. A null from an
   instrument that cannot see the thing is no evidence, and it is not reported as one. The direct route, Wnt against days, is used.
2. **P3 was wrong in form.** I predicted one fraction explained (20 to 70 percent); the data give a different answer per gene.
3. **Linearity was checked, and the check found something the linear fit hides.** The quadratic term in log10 days adds nothing
   (r² +0.00, |t| <= 0.3), but binning by day shows AXIN2 and NKD1 change almost entirely before about day 60 and are flat from there.

## What the calibration shows
- **P1 held for three of four genes.** Within-line slopes on log10 days: LEF1 -2.23 (r² 0.49), NKD1 -0.53, AXIN2 -0.40; the sign is
  stable leaving out any one of the six lines. **APCDD1 goes the other way, +1.24.** The four "canonical readouts" do not move
  together with maturation, so they should not be treated as one unit.
- **Between about day 60 and day 400, which brackets a 15-week organoid, AXIN2 and NKD1 are essentially flat** (within-line means within
  0.15 of zero from day 60 on). Maturation as it proceeds in normal spheroids does not move them in that window, so it cannot
  produce an elevation of 1.9-fold (AXIN2) or 2.7-fold (NKD1) there. The equivalent-age arithmetic, 0.4 and 0.2 days, is a symptom of
  this and should not be read as "the KO is undifferentiated".
- **LEF1 is the exception and the only one where maturation could matter:** it falls steadily from +1.11 (day 60 to 110) to -1.32 (day 400
  and later). The observed +1.15 would need the KO to be about a third of the WT age (about 32 days against 105). Large, not absurd.
- **APCDD1: maturation would lower it, it is raised.** Maturation does not explain it and runs against it.

## What this does not establish
- Not that the elevation is WWOX-dependent. Composition, regional identity and the other four things that differ between a
  Pasca spheroid and a WiBR3 organoid are untouched.
- Not that the spheroids calibrate the organoids. Different laboratory, protocol (feeder iPSC, serum-containing medium), lines and platform.
  Only slopes on a log scale were compared, never absolute values.
- Not that the KO follows the normal trajectory. The markers that would tell us the KO's true maturity track time poorly here.

## Reading, at the strength it has
EXPLORATORY. For **AXIN2 and NKD1** the maturation-confound explanation is **weakened** by independent normal-tissue data: those genes do not
change with maturation across the window that matters, and the observed elevation is large. For **LEF1** the confound remains
plausible. For **APCDD1** it is contradicted. This moves the question toward the remaining alternatives for AXIN2 and NKD1 (cell-type
composition within the organoid, regional identity, or a WWOX-dependent change) and does not choose among them. It is a bound on one
explanation, using a dataset that is not WWOX evidence.
