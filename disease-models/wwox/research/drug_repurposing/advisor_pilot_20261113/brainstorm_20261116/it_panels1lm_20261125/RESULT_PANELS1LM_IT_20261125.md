# Result: do the printed densitometry values of Supp Fig 1L and 1M reproduce from their strips? (IT, 2026-11-25)

Actor `orchestrator` (IT), task ORCH-ROADMAP-IT59-20261119. Hypothesis level; reference genotype class; nothing here is medical advice. Held raster only (File012 pages 6 and 7; File010 page 2); no spend, no contact. Pre-registration `PREREG_PANELS1LM_IT_20261125.md` (commit `2a8c63a0f`, before any pixel of these strips was extracted), its amendment `AMENDMENT_PANELS1LM_IT_20261125.md` (UTC time and digest in the two companion files; written after the strips were looked at, before any ratio was computed), and a blind verifier's report as delivered. Every number below is a read-off from a JPEG, **not author data**.

## 1. Answer first

1. **A mismatch with the shown image is not an error by itself.** The authors' Methods say: "Blots were repeated and quantified 2–3 times per experiment in Bio-Rad's Image Lab software. Representative images of those repeated experiments are shown" (File009, Immunoblot analysis). A printed value may summarise repeats. The pages carry no densitometry formula, no n per value and no replicate spread. This limits what a check on the shown membrane can say; it is stated before any verdict.
2. **Panel 1L: the four printed values reproduce** (every ratio between printed and read value within 1.5) under the pre-registered primary variant, and in the blind verifier's reading: LM-iPS 0.2 (read 0.18 and 0.16), WSM S2 AAV9 0.4 (0.49, 0.45), WSM S5 AAV9 0.4 (0.45, 0.39), LM-iPS AAV9 0.9 (1.20, 1.07). **The result depends on where the window sits and on HSP90 normalisation:** a window fixed on the wild-type 46 kDa rows misses the bands of LM-iPS and of the rescued lanes, which sit about 18 rows (IT) higher, and then fails (read 0.04 to 0.5); without HSP90 normalisation all four fail in both readings (read over printed 0.47 to 0.78 here; 1.8 to 3.1 fold off in the verifier's). The published composite's own pixels reproduce them too (verifier: 0.14, 0.39, 0.35, 0.85).
3. **Panel 1M: the printed 0.1, 0.1 and 0.3 reproduce on the shown membrane; the printed 7 does not.** Verifier: 0.10, 0.10, 0.24 (all within 1.5, "sensitive" at the edge). IT: 0.10, 0.10, 0.19 on the single band and 0.13, 0.07, 0.22 with a background taken below the bands (exploratory); the registered primary variant gives 0.08, 0.04 (below noise), 0.05 (below noise) because its upper background rows lie on a strong upper band; its code is NOT_REPRODUCED. **For WPM S1 AAV9 (printed 7, relative to JH WT) no read-off exceeds about 2.1 (IT) or 2.2 (verifier), with or without HSP90 normalisation, on the shown image and on the composite's pixels.** The verifier notes that S1 AAV9 over untreated S1 reads about 9 (IT: 8 to 21 by window), so a number of that order arises with a non-wild-type reference; what computation produced 7 cannot be established from these files.
4. **The original 1M membrane has seven lanes; the published panel shows five.** WPM D1 AAV9 and WPM D3 AAV9 are not in the panel. Their legend restricts L and M to lines "included in the sc-RNA-seq experiment", so an omission by design is possible; no inference about conduct is drawn. **WPM D1 AAV9 reads about 0.13 (verifier; IT 0.13 to 0.31 by window) of wild type, about one tenth of S1 AAV9 and D3 AAV9 (verifier: 0.97 and 1.24, near wild-type level), and not clearly above its untreated line** (verifier: 1.2 times, range 0.2 to 1.8; IT: 1.3 to 8 times by window). Which WPM D clone fed the functional AAV9 arm (Fig 6, "WPM D AAV9-WWOX n = 4") is not stated; the Methods say at least two clones per line were used for each genotype.
5. **Both HSP90 strips of 1M are clipped:** 34 to 72 percent of the pixels in each lane's band window sit at grey 5 or below (IT; the verifier counts 470 to 950 pixels at 0 to 5 per window). HSP90 normalisation on that membrane rests on saturated loading bands and probably compresses loading differences; the WWOX bands of WT lower (darkest grey 31) and S1 AAV9 lower (53 in IT's window, 47 verifier) are not clipped, so clipping does not explain the failure of 7; D3 AAV9 sits near the floor (10 in IT's window), so its ratio may be an underestimate. 1L HSP90 is not clipped.
6. **A premise in my pre-registration was wrong.** I wrote that the legend declares both a 46 kDa and an upper ~48 kDa band specific for panels K to M. The footnote's asterisk is attached, in the legend text, to "a wildtype control*" in the sentence about the iPSC clones (the legend's mislabelled "(G)"), not to K to M; the earlier ADV-241 note carried the same reading. What the strips show on their own: in 1K, 1L and 1M the rescued and LM-iPS bands sit above the wild-type band by about the spacing that the marker labels give for 48 against 46 kDa (16 to 18 rows). The two-band window V2 was therefore chosen with a premise that does not hold, and was justified afterwards by what the strips show; the verifier, who did not have that premise, read each lane's band where it sits and reached the same 1L result.

## 2. Measurements

IT, primary variant (V2: both band rows, HSP90 per lane, registered background; amended anchor), V1 (the 46 kDa rows only), and the verifier's lower band per lane with its range over 216 analysis choices. Ratios to the wild-type lane of the same membrane; "below" = net under 3 times blank-window noise.

| Panel, lane | Printed | IT V2 | IT V1 | Verifier |
|---|---|---|---|---|
| 1L WSM S2 | none | 0.019 | 0.024 | 0.023 |
| 1L WSM S5 | none | 0.012 (below) | 0.009 | 0.009 |
| 1L LM-iPS | 0.2 | 0.175 | 0.042 | 0.16 [0.14 to 0.18] |
| 1L WSM S2 AAV9 | 0.4 | 0.488 | 0.103 | 0.45 [0.41 to 0.49] |
| 1L WSM S5 AAV9 | 0.4 | 0.450 | 0.147 | 0.39 [0.35 to 0.44] |
| 1L LM-iPS AAV9 | 0.9 | 1.204 | 0.511 | 1.07 [0.92 to 1.19] |
| 1M WPM S1 | 0.1 | 0.080 | 0.102 | 0.10 [0.07 to 0.13] |
| 1M WPM D1 | 0.1 | 0.037 (below) | 0.098 | 0.10 [0.07 to 0.12] |
| 1M WPM D3 | 0.3 | 0.049 (below) | 0.189 | 0.24 [0.18 to 0.29] |
| 1M WPM S1 AAV9 | **7** | 1.68 | 0.82 | 0.97 [0.61 to 1.21] |
| 1M WPM D1 AAV9 (not in panel) | none | 0.31 | 0.13 | 0.13 [0.02 to 0.21] |
| 1M WPM D3 AAV9 (not in panel) | none | 1.30 | 0.42 | 1.24 [0.93 to 1.42] |

Codes by the frozen rule, primary variant: **1L REPRODUCED** (variant-dependent: V1 NOT_REPRODUCED; without HSP90 UP_TO_ONE_FACTOR); **1M NOT_REPRODUCED** (every variant, because of the 7). Full variant table: `out_panels1lm.txt`. Exploratory below-only background variants (post hoc, marked *): 1M WPM S1, D1, D3 read 0.126, 0.067, 0.222 (ratios to print 1.26, 0.67, 0.74), 7 reads 1.29. Exploratory panel 1K (already seen; both bands): rescue lanes 0.31 and 0.51 against printed 0.8 and 1.4, a common factor of about 2.6; the knockout lanes 0.04 (below noise) and 0.09.

Saturation of the wild-type lane (frozen rule): not saturated in 1L (darkest grey 24) or 1M (31). Lane-by-lane clipping: `out_clip_panels1lm.txt`, `out_clip_hsp_panels1lm.txt`.

## 3. Predictions scored

| | Prediction | Outcome |
|---|---|---|
| P1 | 1M at least UP_TO_ONE_FACTOR (primary) | **Not met** (NOT_REPRODUCED, because of the printed 7) |
| P2 | at least one panel REPRODUCED (primary) | Met (1L) |
| P3 | printed rank order preserved in both panels (primary) | **Not met** in 1M under the registered background (D3 0.049 below S1 0.080); preserved in the verifier's and the below-background reads |
| P4 | 1L wild-type lane saturated | **Not met** (darkest grey 24, no pixel at the floor in the window) |
| P5 | 1K rescue ratios within 1.5 of 0.8 and 1.4 under V2 | **Not met** (0.31 and 0.51; factor 2.6, uniform) |

## 4. Deviations, errors and what was seen before what

1. The pre-registered anchor rule (§2.4) takes the wild-type lane's maximum, which on both strips is a strong upper band not shown in the composite. Replaced by the amendment (largest value between 0.30 and 0.80 of the strip height) after the strips were viewed and before any ratio was computed.
2. **A code error:** the first output mapped lanes with the marker lane counted as a sample lane on 1L (and on 1K), so every 1L value was shifted by one lane; I had seen that output (and a "below noise" wild-type lane) before the fix. Corrected by requiring the marker run on 1L and by taking 1K's lane centres from ADV-251. The first-run output is kept as `out_panels1lm_first_run_with_lane_bug.txt`.
3. The HSP90 strips' border rows (top 8, bottom 6) were trimmed for 1L and 1M: a frame line and a stray band corrupted the lane finder and the peak search.
4. The registered background (rows 20 to 50 above the window) falls on the strong upper band in several lanes of 1M and 1L; the below-only background variants were added after I saw negative and implausible nets, and are exploratory.
5. The pre-registration's legend premise was wrong (§1.6).
6. The verifier was not shown the Methods sentence on repeats and read the legend footnote correctly; I did not ask it to compare its method with mine, so the agreement on 1L is two methods on one image, not two images.

## 5. What this settles for the consumers (no registry file is edited here)

* **CLAIM 002 and the range "0.4× to 7×":** the top of the range is the printed 7, which neither reader reproduces from the shown image; the read-off range across the rescued lanes (shown and not shown) is about 0.13 to 1.7 by IT's windows, 0.13 to 1.24 by the verifier's. The printed values are kept as printed; the sentence in `commit_candidates/CC-20261125-ORCHESTRATOR-PANELS1LM-RESCUE-RANGE-01.md` (PROPOSED) says so with the Methods caveat.
* **`CC-20261125-ORCHESTRATOR-ADV251-KO-FLOOR-01`:** its sentence says the printed rescue values were missed "by a factor of about 6". With the higher rescue band inside the window the factor is about 2.6 and common to both lanes; about 6 holds for the 46 kDa rows only. The knockout floor under both bands is 0.04 (below noise) and 0.09, against 0.07 and 0.15 on the 46 kDa rows; the rule FLOOR_AT_OR_ABOVE_0.1 (larger lane 0.08 or more) is met by 0.09 and not by a margin. A dated revision is added to that candidate.
* **RS-R9 (gate G0) and radar question IT18:** the printed G372R values 0.1, 0.1 and 0.3 are reproducible on their own membrane (to within the stated limits), which is the one new element; the floor on a different membrane (0.04 to 0.15 by band definition) is not separable from the two 0.1 lines; G0 stays unmet. One dated line each.
* **ADV-241's note on 1K** ("the upper band sits at the same strength in the knockout lanes"): the read-off does not show it (V2 window nets: knockout lanes 70 and 109, rescue lanes 567 and 604, same units); the note's other point stands.
* **Not changed:** any printed value, the ranking, any card.

## 6. Limits

JPEG display exports of unknown linearity; one blot per panel; no uncropped membrane (HSP90 and WWOX strips are separate images, registration assumed from the page layout); lane identity rests on label order; the near-empty lanes are placed by position only; the co-migration of the rescue and LM-iPS bands with the wild-type band is not shown (IT and verifier both see them at a different row); HSP90 clipped on 1M; read-off, not author data; verifier is one reader on one image.

## 7. DREAM

Not consumed: the authors say printed values come from repeated quantifications, so a printed densitometry number anywhere in the repository is a summary of unseen blots, not a value of the shown image; the earlier habit of calibrating a read-off against it (ADV-251) tests only whether the shown image agrees with the summary. A question for the held set: which other printed ratios under a blot in a held supplement are used as anchors by a card or claim, and does the same methods sentence apply? Consumer: CLAIM 002's deferred qualification list.
