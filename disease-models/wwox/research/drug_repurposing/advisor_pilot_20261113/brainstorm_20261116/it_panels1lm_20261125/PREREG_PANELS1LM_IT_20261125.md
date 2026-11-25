# Pre-registration: do the printed densitometry values of Supp Fig 1L and 1M reproduce from their strips? (IT, 2026-11-25)

Actor `orchestrator` (IT), task ORCH-ROADMAP-IT59-20261119. Next increment proposed in the ADV-251 result (§ 8) and carried by IT checkpoint 14. Hypothesis level; reference genotype class; nothing is medical advice. Held raster only; no spend, no contact, no delegate. Written before any pixel of the 1L or 1M strips was extracted, rendered or viewed by this window.

## 0. Disclosure (known when written)
* Printed values, taken from earlier IT records and not re-read now: panel 1L, WT = 1, then 0.2, 0.4, 0.4, 0.9; panel 1M, WT = 1, then 0.1, 0.1, 0.3, 7 (JH WT, WPM S1, WPM D1, WPM D3, WPM S1 AAV9). The predecessor noted from an eye reading that the 1L wild-type lane looked saturated.
* ADV-251: on panel 1K the pre-registered 46 kDa window read the rescue lanes 6 to 6.6 times below the printed 0.8 and 1.4; read post hoc at their own position (about 16 rows higher) they were still 1.6 and 2.6 times below.
* The panel legend (File010, text layer) says the specific WWOX bands are the lower 46 kDa band **and an upper band at about 48 kDa**. The ADV-251 window held the 46 kDa position only.
* From the marker labels in the File012 text layer (no pixels), 48 and 46 kDa are about 8.4 pt apart on page 5, which is about 16 image rows: the offset ADV-251 observed. So a doublet window is expected to move the 1K numbers; that is not independent evidence. The labels are placed approximately (the 46 kDa band does not sit where the left-hand marker scale would put it), so they give a spacing, not a position.
* Image sizes and placements on pages 6 and 7: 1L strips 772 x 74 and 786 x 190 pixels; 1M strips 772 x 169 and 827 x 215 pixels (the lower image on each page is taken as the WWOX strip, from the right-hand labels).
* Source digests: File012 `18864bfbdd8329a8fa0044c38ef428fdd481dd84d9afc409e4874d157408dc45`; File010 `aa86f300c7f5333db95f5e0c80a462b8c7f2a290409cd7c5e61527a810dffc42`.

## 1. Question and comparator
Comparator, fixed now: the **printed value of each non-wild-type lane** (wild type = 1 on the same membrane) against **my read-off ratio of the same lane**: (WWOX net / HSP90 net) divided by the same quantity of the wild-type lane. Question: do the printed values of 1L and of 1M reproduce, and does adding the 48 kDa band to the window change the answer?

## 2. Method (frozen)
1. Extract the embedded images of pages 6 and 7 at native resolution; 8-bit grey; plain Python.
2. Lane centres from the column darkness profile of the HSP90 strip; lane half-width 40 % of the median pitch. Lane labels from a rendering of the figure, tied by order; a lane that cannot be tied is excluded and named. If the printed values on the rendering differ from § 0, the rendering is used and the difference is reported.
3. Row spacing of the doublet: D = 8.4 pt x (51.6 / 59.4) = 7.3 pt (pages 6 and 7 use a shorter marker spacing), converted with each strip's pixels per point (about 18 rows). Half-window h = 6 rows x (strip pixels per point / 1.946).
4. Lower-band row y0: the lowest local maximum of the wild-type lane's row-mean darkness profile that is at least 0.25 of that lane's maximum and lies within 1.5 D of the maximum.
5. Two window definitions: **V1** (46 kDa only) = y0 plus or minus h; **V2** (both specific bands) = from y0 - D - h to y0 + h. Same rows for all lanes. Background = median darkness of the same lane over rows 20 to 50 rows (scaled like h) above the window top and below the window bottom, clipped to the image.
6. HSP90: per-lane peak, plus or minus 8 rows (scaled), background by the same rule. (ADV-251 saw a tilted HSP90 row clipped by a fixed window.)
7. **Primary variant: V2, HSP90-normalised.** Also reported: V1 HSP90-normalised; V1 and V2 WWOX alone; V2 and V1 with each lane's window shifted by that lane's HSP90 peak offset.
8. Noise: the same-width window sum in blank rows of each lane; a lane whose net is below 3 times that noise is "below detection", left out of the code, and counted as consistent only when its printed value is 0.1 or lower.
9. Saturation of the wild-type lane: as ADV-251 § 2.7 (flat top of 3 or more rows at the image's darkest value, or peak grey within 3 levels of the image minimum). If saturated, every ratio is an upper bound and the result says so first.

## 3. Decision rule (frozen), per panel, with r = my ratio / printed value on the non-wild-type lanes
| Code | Condition |
|---|---|
| REPRODUCED | every r within 1/1.5 to 1.5 |
| UP_TO_ONE_FACTOR | not REPRODUCED, and every r within a factor 1.5 of the geometric mean of the r values (a shared wild-type or normaliser convention would explain it); the factor is reported |
| NOT_REPRODUCED | neither |

A code that differs between V1 and V2, or between the primary and a secondary variant, is reported as variant-dependent, with each code.

## 4. Predictions (scored in the result)
| | Prediction | p |
|---|---|---|
| P1 | under the primary variant 1M is at least UP_TO_ONE_FACTOR | 0.5 |
| P2 | at least one of the two panels is REPRODUCED under the primary variant | 0.3 |
| P3 | the rank order of the printed values is preserved in both panels (ties allowed) | 0.7 |
| P4 | the 1L wild-type lane is saturated | 0.5 |
| P5 | exploratory, panel 1K (already seen): under V2 both rescue ratios are within 1.5 of 0.8 and 1.4 | 0.35 |

## 5. Decision changed, consumers, limits
Whether the printed G372R values (0.1, 0.1, 0.3) are reproducible from the authors' own strip; whether the ADV-251 calibration failure comes from the band definition (then the sentence of `CC-20261125-ORCHESTRATOR-ADV251-KO-FLOOR-01` and the ADV-251 floor are re-read under V2). Consumers: map row RS-R9, radar question IT18, that candidate. Rejecting observation: if V2 and V1 give the same codes and ratios, the band definition is not the cause. Limits: JPEG display rasters, one blot per panel, read-off and not author data, cross-membrane statements only as orders of magnitude, no second reader.
