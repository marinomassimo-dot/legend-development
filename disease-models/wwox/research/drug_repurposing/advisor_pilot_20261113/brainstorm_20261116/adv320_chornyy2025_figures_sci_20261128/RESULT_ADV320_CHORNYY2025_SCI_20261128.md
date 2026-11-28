# ADV-320 result (SCI bc, 2026-11-28): Chornyy 2025 figures (PMID 41036104) against CLAIM 047 bounds (1) and (2)

Hypothesis level; reference genotype class only; not medical advice; the source never names WWOX (T3 for engineering bounds, T5 for WWOX biology). Frozen note: `PREREG_ADV320_CHORNYY2025_FIGURES_SCI_20261128.md` (sha256 4b8dc53954a3395fa85c81c90c5da09e8a641a74a5996d17168ff51c621c484d, written 2026-11-28T12:09:22Z before any figure was opened). Delegate: legend-delegate, sonnet 5.5, effort high stated in the dispatch; report verbatim in `BLIND_FIGURES_CHORNYY2025_ADV320_DELEGATE.md`. Figures: PMC open-data bucket PMC12481918 (no 429 or challenge) plus full-resolution extraction from the bucket's `mmc2.pdf`; Fig S1 exists only as a 726 x 720 px raster, so its values are eye reads (about ±3 units).

## Disclosures
* **The delegate was NOT blind to the frozen note.** I put the note in the delegate's output folder (my error); the delegate opened it before any figure and states that it did not use it to select what it extracted. Weigh the liver-blot and Fig 4C readings accordingly: they are printed values and bar tops, but the reading is not independent of H1/H2. No second reader has been run; a blind re-read of Fig S1B and Fig 4C is the open check.
* I did not open any figure myself in this increment (delegate report only).

## 1. Bound (1): liver protein, Fig S1 (labels: EYE = bar top or dot against a tick; PRINTED = on the figure)
| Item | Value | Source |
|---|---|---|
| Western, EGFP relative to GAPDH × 100, liver, n = 4 per treatment (animal presumed; lane unit UNSTATED) | gfa1405 about 81 (dots about 104, 90, 79, 49); CAG about 6; CNP about 6; p546 about 5 (all dots 3 to 9) | S1B right, EYE ±3 |
| Same, brain areas BA1, BA2, BA3 for gfa1405 | about 16, 44, 17 (CAG about 28, 64, 8) | S1B left, EYE |
| Printed marks | liver: gfa1405 to CAG ****; BA2: p546 to CAG ****, CNP to CAG ***; no mark joins gfa1405 with p546 or CNP in liver | PRINTED |
| qPCR liver, EGFP/actin × 1000, n = 4 to 5 animals (animal) | gfa1405 about 107 (dots about 160, 112, 94, 88); CAG about 8.4; p546 about 4.4; CNP broken axis, above 10 | Fig 2B right, EYE; no marks |
| Whole-organ liver fluorescence | all eight livers dim green including control; n = 3 per construct (text), image shown per group single, no scale | Fig 3D, qualitative |
Error-bar type UNSTATED in S1B and Fig 2B; whether the lanes of one tissue come from one gel is UNSTATED (strips with gaps; heart GAPDH contrast enhanced for p546 and gfa1405 per the legend).

## 2. Bound (2): area and intensity, Fig 4C (boxplots; line = MEDIAN; n = 8 to 10 PRINTED; replicate unit UNSTATED on the figure)
| Statistic | CAG | p546 | gfa1405 | Source |
|---|---|---|---|---|
| EGFP-positive area, median (percent, eye) | about 38.7 | about 23.2 | about 26.5 | 4C left |
| same, box (25th to 75th) | about 21.5 to 42.2 | about 10.3 to 33.3 | about 22.7 to 29.2 | 4C left |
| same, whisker top (maximum) | about 42.3 | about 41.9 | about 35.3 | 4C left |
| Text "up to" values | 42 percent | 41 percent | 35 percent | Results text |
| Intensity, median (RFU, eye ±20) | about 572 | about 128 | about 461 | 4C right |
| Text intensity | 474.8, "Mean EGFP intensity" | 154.0 | 412.1 | Results text; no mean is printed on the figure |
Table S1 (printed adjusted P, distribution): CAG against p546 0.0097 (**), against CNP 0.0035 (**), against gfa1405 0.321 (ns). Intensity: CAG against p546 less than 0.0001 (****), gfa1405 against p546 0.0009 (***).

## 3. Frozen rule applied
* **H1 (quantitative as stated) vs H2 (rank among low values, my lean 60 percent): H1 holds for bound (1); my H2 lean was WRONG.** n = 4 (at least 3) per promoter; gfa1405 liver points (about 49 to 104) do not overlap the other three (3 to 9); the absolute liver level is not small beside the brain values of the same promoter; qPCR shows the same ordering. Limits that remain: the only printed test is gfa1405 against CAG; error-bar type and gel layout UNSTATED; one four-promoter western subset (the integrator amendment of CLAIM 047 already holds); animal-level raw data "on request" only.
* **Counterexample 1** (another promoter equal or above gfa1405 in the liver panel): NOT observed. **Counterexample 2** (gfa1405 liver above its own brain protein by a large factor): partly met, with no threshold frozen (my omission): gfa1405 liver about 81 against its brain areas about 16, 44 and 17, i.e. about 1.8, 4.9 and 4.8 times (eye; brain areas are sampled sections, so not a whole-organ ratio).
* **Bound (2) is the finding.** The text compares p546 "41 percent" with CAG "up to 42 percent" of brain area (CLAIM 047: ratio 0.98 recomputed from those two printed values). On the figure these are the WHISKER MAXIMA (about 41.9 and 42.3); the medians are about 23.2 and 38.7 (ratio about 0.60, eye) and the paper's own Table S1 gives CAG against p546 adjusted P 0.0097. The intensity pair (154.0, 474.8) is described as a mean in the text for CAG, and the figure prints medians only (eye 128 and 572; ratio about 0.22 against the text-number ratio 0.324). So "reach at 0.98 of CAG" mixes maxima for area with means for intensity: the claim's "restriction costs intensity, not reach" holds for the maxima and not for the typical animal.

## 4. What changes (consumer: IT, then ADV; edits to CLAIM 047 only through IT after the source check)
| Item | Change |
|---|---|
| CLAIM 047 bound (1) | Keeps its wording; gains n = 4 per promoter, the printed test (gfa1405 against CAG only), the qPCR concordance and the eye values above. |
| CLAIM 047 bound (2) | Needs narrowing: say "maximum animal" for 41 and 42 percent; add the median ratio about 0.60 (eye) and the printed P 0.0097; the 0.324 intensity ratio mixes a mean with a median-based figure. |
| Working-model Trial-readiness (generic) line citing it | Check for the 0.98 or "same reach" phrasing at IT's next pass. |
| Compound roles, WWOX statements | None. |
Not done: a blind re-read of Fig S1B and Fig 4C (the delegate saw the frozen note); no receipt for the figures beyond the one recorded with this result.
