# Can maturation alone account for the size of the Wnt elevation in the WWOX-KO organoid? — prediction fixed BEFORE the data were opened

Declared 2026-10-25 by the Orchestrator. Exploratory. Not medical advice; no dose, route or suitability.
Everything below that is not WWOX data is NOT WWOX EVIDENCE.

## The question
The Wnt readouts (AXIN2, LEF1, NKD1, APCDD1) are raised about 2.2-fold (log2 +1.1) in the GSE156243 KO organoids
(week 15, four KO against two WT libraries). The 2026 paper of the same laboratory shows in its own single-cell
data that canonical Wnt is higher in EARLY cells. The six libraries cannot say whether the KO elevation is a
WWOX-dependent signalling change or a maturation signature. A different, public, WWOX-free dataset can calibrate
one thing the six libraries cannot: how much these genes move with ELAPSED CULTURE TIME alone in WWOX-unperturbed tissue.

## The dataset, and what it is not
GSE150123: 62 samples of human cortical spheroids sampled from about 25 to more than 650 days in culture, from six iPSC
lines, WWOX-UNPERTURBED (no WWOX manipulation; WWOX genotype not otherwise characterised, so neither "wild type" nor
WWOX-null is claimed) (NCBI GEO summary: long-term maturation). The dataset records elapsed culture time, not cellular maturation. Different laboratory, protocol, line family and platform from GSE156243.
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

Script: `maturation_calibration.py`. Data: GSE150123 (62 WWOX-unperturbed cortical-spheroid samples, 25 to 652 days, six iPSC
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

## What the calibration shows (all of it from `maturation_calibration.py --time-course`, reproducible)
The 62 samples are six iPSC lines with 7, 13, 21, 18, 2 and 1 samples; they are repeated measures, not 62 independent
replicates. After centring on the line, the line with one sample carries no information, so **five lines are informative**
and the between-line uncertainty below is wide. Two interval types are given because they can disagree: a t interval on the
per-line slopes (df = lines - 1) and a line-cluster bootstrap. With five clusters the bootstrap resamples only five objects and
tends to understate the uncertainty, so **the t interval is the one to lean on**. The input files are pinned by sha256 in the
script, which refuses to run if they changed. The line with two samples has the steepest slope for every gene, which is what a
very small cluster does.

| gene | full range, mean of 5 line slopes per log10 day, t interval | day >= 60, mean of 4 line slopes, t interval (cluster bootstrap) | quadratic |
|---|---|---|---|
| LEF1 | -2.25 [-3.65, -0.86] | **-3.28 [-4.05, -2.51]** (-3.60, -2.79) | none evident |
| NKD1 | -0.68 [-1.17, -0.18] | **-0.02 [-0.39, +0.34]** (-0.22, +0.22) | none evident |
| AXIN2 | -0.52 [-1.06, +0.02] | **-0.05 [-0.84, +0.75]** (-0.38, +0.03) | none evident |
| APCDD1 | +1.06 [+0.46, +1.67] | +1.62 [-0.31, +3.54] (+0.60, +2.44) | none evident |

- **NKD1: a flat time course from day 60 is supported** (interval about +-0.4 log2 per log10 day). **AXIN2: weaker**; the pooled
  slope is -0.22 and the bootstrap just reaches zero, and with four informative lines the t interval is +-0.8. "Flat" here
  means no detectable slope with that precision, not a measured zero.
- **LEF1 is the gene where culture age matters and matters more after day 60** (-3.28, steeper than over the whole range):
  of the four it is the one where a younger-than-reference state would plausibly raise the readout.
- **APCDD1 rises with culture time in every line and in every leave-one-line-out fit**; its size after day 60 is imprecise.
- **No curvature is evident** (quadratic coefficients near zero). The naive t statistics in the script's output treat samples as
  independent and overstate precision; they are printed only to show the contrast and are not evidence of linearity.
- The sign of every gene's pooled slope is stable leaving out any one line (see the script output).

## What this does not establish
- Not that the elevation is WWOX-dependent. Composition, regional identity and the other four things that differ between a
  Pasca spheroid and a WiBR3 organoid are untouched.
- Not that the spheroids calibrate the organoids. Different laboratory, protocol (feeder iPSC, serum-containing medium), lines and platform.
  Only slopes on a log scale were compared, never absolute values.
- Not that the KO follows the reference culture-age trajectory. The markers that would tell us the KO's true maturity track time poorly here.

## Reading, at the strength it has
EXPLORATORY. These data are evidence **against a simple, transferable culture-age explanation** for the KO elevation of AXIN2
and NKD1: across the post-day-60 window that a 15-week organoid sits in, elapsed culture time does not detectably move NKD1 (and
barely AXIN2) in these spheroids, while the KO elevation is 1.9- and 2.7-fold. **They are not evidence that maturation or
cell composition cannot explain the KO signal.** Elapsed time is not maturation; the KO may be at a different cellular state
than any culture age in another laboratory's spheroids; composition within the organoid (the 2026 paper shows radial glia carry
the Wnt activation), regional identity, and a WWOX-dependent change all remain open, and these data choose between none of them.
LEF1 is the one readout for which a younger-state explanation stays plausible. APCDD1 runs against it. Five informative
lines, one laboratory, one protocol; slopes only, never absolute values. The earlier "equivalent age" arithmetic (the KO would
need to be 0.4 or 0.2 days old) is **withdrawn as an interpretation**: it divides an observed shift by a slope that is not
distinguishable from zero in the relevant window, so it is a symptom of that, not a statement about the KO's age.
