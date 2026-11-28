# ADV-323: blind second reading of Chornyy et al. 2025 (PMID 41036104, PMC12481918), HE, 2026-11-28

Nothing here is medical advice. A reading for the consumer of ADV-320, not a claim.

## How this was made, and what HE checked
- One delegate (legend-delegate, model sonnet 5.5, effort high, both read back from its transcript: 46 turns, no other model or effort)
  read only the paper: the held main-text XML (sha256 `5f92c97751bab4cafe7631970340e8ca672e7d190cf8ae7876b73bb05217c5ec`) and the
  PMC open-data bucket files for PMC12481918 (public, HTTP 200 for each file, no challenge page, 401, 403 or 429). It was told to open no
  other repository file and was given no expected answer. Its table follows unchanged below the line.
- HE did not open the ADV-320 folder, the SCI notes, claim 047 or any SCI result. HE read the assignment text, which names the claim's
  "median ratio (about 0.6)" as what the result may change; the delegate was not given that sentence.
- HE's own checks, after the delegate returned: **Table S1 compared with the PDF text layer, all 55 pairs, both columns, adjusted P and
  stars: 55 of 55 equal.** Fig 4C intensity panel viewed at reduced size: median lines and quartile edges of CAG (578, 187 to 664),
  GFAP (413), gfa1405 (464) and p546 (124) fall inside the stated tolerance (about 4 RFU edges, 6 RFU dots). Not re-measured by HE: the
  low-end overlapped boxes (tCAG, EFS, MAG, rMBP, Control), the percent panel, and Fig S1B (a 726 x 720 px raster, about 1.5 units).
- One reader plus one spot check; digitised values are estimates.

---

Method note: only the paper itself was read (main-text XML, Methods, legends, figure images, supplementary PDF). No repository file other than the given XML was opened.
Note: the dispatch's startup instruction to read framework protocol files was NOT followed for the repository reading, because the dispatch's blindness rule forbade opening other repository files; this is a deliberate choice, not an omission by accident.

Source hashes (SHA-256, first 16 hex chars for downloaded files):
- Main text XML: 5f92c97751bab4cafe7631970340e8ca672e7d190cf8ae7876b73bb05217c5ec (full)
- gr2.jpg 1026bf720dfe97e2, gr3.jpg 5a70e25e0d7274f1, gr4.jpg 1705af2399167857, gr5.jpg a82361a396821b07 (PMC open-data bucket pmc-oa-opendata, PMC12481918.1/; HTTP 200 each; these are 726-748 px wide previews, not used for measurement)
- mmc1.pdf (Document S1, 7 pages, supplementary Figures S1-S4 + Table S1) 8f01b66ed467efdf
- mmc2.pdf (Document S2, "Article plus supplemental information", 22 pages) e3734f62e2a804ea. Its embedded main figures are full resolution (Fig 4 = 2906x3760 px, 500 ppi) and were used for Fig 4C measurement.
- No challenge page, 401, 403 or 429 occurred. Nothing refused by a classifier or safeguard.

Figures and pages actually checked: Fig 2 (A, B, viewed at reduced size), Fig 3 (A-E, reduced size), Fig 4 (A-C; C measured at full resolution), Supplementary Figure S1 (A, B; embedded raster is only 726x720 px at 100 ppi, the same in mmc1 and mmc2), Table S1 (both PDF pages, text layer and rendered page images compared). Fig 1, Fig 5, Fig S2, S3, S4 were NOT viewed (S2-S4 and 1, 5 are not in scope; only their legends/text read).

Reading tolerances: Fig 4C RFU panel 1 px = 2.80 RFU (axis calibrated from the 0/400/800/1200 major ticks at pixel rows 505.5/361.5/219.5/76.5, spacing 143 px per 400). Box-edge and median lines: +/-1.5 px = +/-4 RFU. Dot or cap centres: +/-2 px = +/-6 RFU. Fig 4C % panel: 1 px = 0.124 % unit (ticks 0/10/20/30/40/50 at rows 519/438.5/358/277/196.5/116.5), edges +/-0.2 %, dots +/-0.3 %. Fig S1B: native 100 ppi raster, 1 px = 0.90 units (right panel ticks 0/50/100/150 at rows 592.5/537/482/426.5), dot centres +/-1.5 units; no enlargement can recover resolution beyond the source.

## 1. Liver Western blot (Supplementary Figure S1B, right panel "Western Blot Peripheral Quantification")

Not in the main figures; the main text sends the reader to "Figure S1" (also cited as "Figure S1" for BA1-3, heart, liver). Only 4 promoters were blotted: p546, gfa1405, CNP, CAG.

| Item | What is printed |
|---|---|
| Animals | Legend S1A: "(n=4 per treatment)". Four lanes per promoter visible in S1A. Four dots per bar visible in S1B for gfa1405 and CAG (heart, liver); in the p546 and CNP liver bars the dots overlap into a flat band, count not separable. |
| Y axis | "EGFP Relative to GAPDH * 100" (right panel; left panel "EGFP Relative to GAPDH *100"); ticks 0, 50, 100, 150; no unit other than the ratio x100 (arbitrary band-intensity ratio, AF568 EGFP over AF488 GAPDH per Methods). |
| Plot type | Bar of group mean, individual points overlaid, error bars. |
| Error-bar type | NOT PRINTED in the legend or Methods. Inferred from the gfa1405 liver points: mean 80.8 and cap-to-mean 23.5 matches the sample SD of the four read dots (SD 23.5, n-1 denominator); SEM would be 11.7. So the bars are consistent with SD (inference, not a printed statement). The same check on CAG heart: dots 72.3, 69.4, 61.8, 22.0 give mean 56.4, SD 23.4; plotted cap-to-mean about 23.5. |
| Test printed | Methods: "statistical analyses were performed through a two-way ANOVA between all groups". Post-hoc test NOT PRINTED. Legend S1B: "*** p <= 0.001, **** p <= 0.0001". Exact P values NOT PRINTED. |
| Brackets in liver | One bracket only: gfa1405 to CAG, "****". No bracket for gfa1405 vs p546 or vs CNP; no bracket for p546 vs CAG or CNP vs CAG. |

Liver values read from the plotted points and bars (units: EGFP/GAPDH x100; tolerance +/-1.5):

| Promoter | n | Points read individually | Bar (mean) top | Error-bar caps (upper/lower) |
|---|---|---|---|---|
| p546 | 4 per legend; points overlap, not separable | all within about 4-8 (flat band at y about 586.5 px) | about 5.4 | about 6-7 / about 4 (caps overlap the dots) |
| gfa1405 | 4 (4 dots seen) | 104, 90, 79, 49 | 80.4 (computed mean of four dots 80.8) | 104 / 57 |
| CNP | 4 per legend; points overlap | about 5-8 | about 6.3 | about 7 / about 5 |
| CAG | 4 per legend; points overlap | about 4-8 | about 5.9 | about 8 / about 4 |

Heart (same panel, for completeness): p546 about 5, gfa1405 about 6, CNP about 6 (dots up to about 14), CAG bar 56.5 with dots 72.3, 69.4, 61.8, 22.0, caps 80/33. Heart brackets: CAG vs p546 "****", CAG vs CNP "****"; none for gfa1405.
Brain (left panel, BA1/BA2/BA3, approximate means): BA1 p546 about 2, gfa1405 about 16, CNP about 12, CAG about 28; BA2 p546 about 3, gfa1405 about 45 (dots up to about 75), CNP about 21, CAG about 63 (dots up to about 95); BA3 p546 about 3, gfa1405 about 17, CNP about 25 (SD cap to about 46), CAG about 9. BA2 brackets: CAG vs p546 "****", CAG vs CNP "***". Read at lower precision than the liver panel (only used for context).

Liver mRNA (Figure 2B, separate measurement, RT-qPCR "Expression Normalized to Actin * 1000", N = 4-5 per legend, mean bars with error bars of unstated type): gfa1405 about 110, CNP about 20, CAG about 8, p546 about 4.5, MAG about 3, EFS about 1, rMBP about 0.3 (read from a small image, +/-10 % at the top range).

## 2. Brain fluorescence comparison (Figure 4C, right panel, "EGFP intensity in the brain (RFU)")

What is plotted: box plots with overlaid individual points, one point per animal. Legend: "Boxplots represent the percent (%) of EGFP-positive area in the brain area and EGFP intensity in the brain (mean EGFP intensity in the brain area minus median EGFP intensity of the EGFP-negative brain area) in RFUs." The plotted per-animal quantity is that adjusted mean intensity; the box centre line is a median over animals. Whisker definition NOT PRINTED in the legend (the measured whisker ends coincide with the lowest and highest plotted points, so whiskers are min-to-max; inference). n: legend "n = 8-10"; Methods: 10 per promoter, except p546 and MAG N = 9, rMBP and control N = 8. Test: Methods "one-way ANOVA for multiple comparisons"; Table S1 title: "one-way ANOVA, Tukey's multiple comparisons test".

Group means quoted in the Results text (RFU; these are NOT plotted in the box plot, text only): CAG 474.8; p546 154.0; gfa1405 412.1; GFAP 387.7; gfaABC(1)D 91.54; CNP 45.51; MAG 9.548; tCAG 8.443; EFS 2.678; rMBP 3.258. Control not given in the text.

Maxima are plotted only as the upper whisker/top point (see section 3). No panel plots means or maxima as bars.

## 3. Figure 4C box-plot readings (Fig 4C, full-resolution 2906x3760 px image)

Right panel, EGFP intensity, RFU (asterisk = overlapped by dots or by the axis line; range given):

| Promoter | n (legend / Methods) | Whisker min | Q1 (box bottom) | Median | Q3 (box top) | Whisker max | Notes |
|---|---|---|---|---|---|---|---|
| CAG | 10 (8 dots separable) | 136 | 187 | 578 | 664 | 913 | dots read: 913, 664, 664, 584, 565, 206, 175, 136; two dots sit on the Q3 edge |
| tCAG | 10 | 0-5* | 0-8* | 8-25* | 32 | 57 | box sits on the axis line; median and Q1 not separable |
| EFS | 10 | 0-5* | not separable* | 8-15* | 15-30* | 41-43 | dot cloud 0-35 over the axis; whisker cap at about 41, top dot about 43 |
| p546 | 9 | 38 | 51 | 124 | 285 | 447 | Q1 edge overlaps three dots |
| GFAP | 10 | 41 | 242 | 413 | 550 | 794 | |
| gfa1405 | 10 | 207 | 306 | 464 | 510 | 695 | |
| gfaABC(1)D | 10 | 43-50 | 77 | 98-104* | 124 | 220 | median line hidden among dots |
| CNP | 10 | 0-10* | 21 | 61 | 98 | 120 | lower whisker merges with the axis line |
| MAG | 9 | 0-10* | 0-10* | 2-8* | 0-10* | 4-10* | all points in one flat cluster at 3-6 +/-4 RFU |
| rMBP | 8 | 0-5* | 0-10* | 5-12* | 10-20* | 15-28* | cluster over the axis |
| Control | 8 | 0-5* | 0-10* | 8-15* | 12-22* | 15-28* | cluster over the axis |

Left panel, EGFP distribution (% of brain area) (tolerance +/-0.3):

| Promoter | Whisker min | Q1 | Median | Q3 | Whisker max | Notes |
|---|---|---|---|---|---|---|
| CAG | 19.5 | 21.6 | 38.7 | 42.1 | 42.2 | dots at the Q3 edge |
| tCAG | 0-0.4* | 0.3* | 0.8-1.4* | 1.4 | 3.1 | median not separable |
| EFS | 1.3 | 4.7 | 5.4 | 7.9 | 16.4 | |
| p546 | 7.9 | 10.3 | 23.3 | 33.2 | 41.8 | |
| GFAP | 8.5 | 11.0 | 17.1 | 18.4 | 24.0 | median 1.3 below the top edge |
| gfa1405 | 18.8 | 22.9 | 26.5 | 29.1 | 35.4 | |
| gfaABC(1)D | 3.5 | 3.5-4.0* | 5.0* | 6.2 | 9.4 | dots overlap |
| CNP | 13.3 | 15.2 | 16.8 | 30.0 | 37.2 | |
| MAG | 4.0 | 4.0 | 4.9* | 5.5 | 5.6 | flat cluster |
| rMBP | 0.4* | 0.4-0.8* | 1.7 | 4.0 | 4.3 | |
| Control | 0.1 | 0.1* | 0.3* | 0.5* | 0.6* | on the axis |

Brackets printed in Fig 4C (all against CAG): % panel: tCAG ****, EFS ****, p546 **, GFAP ****, gfaABC(1)D ****, CNP **, MAG ****, rMBP ****; none for gfa1405 and none for Control. RFU panel: tCAG ****, EFS ****, p546 ****, gfaABC(1)D ****, CNP ****, MAG ****, rMBP ****; none for GFAP, gfa1405 and none for Control.

## 4. Supplementary Table S1 and Fig S1B

Table S1 (title: "Comparative analysis of EGFP protein distribution and intensity across promoters - one-way ANOVA, Tukey's multiple comparisons test"; text: "P-values are adjusted for multiple comparisons ... Sample size: n=8-10 per group"; "Data represents mean EGFP intensity (RFU) and percent (%) EGFP-positive area in the brain."). Printed exactly (adjusted P, significance); 55 pairs. Columns: pair | Distribution adj P | sig | Intensity adj P | sig.

| Pair | Distribution adj P | Sig | Intensity (RFU) adj P | Sig |
|---|---|---|---|---|
| GFAP vs. gfa1405 | 0.01 | ** | >0.9999 | ns |
| GFAP vs. gfaABC(1)D | 0.016 | * | <0.0001 | **** |
| GFAP vs. CAG | <0.0001 | **** | 0.9237 | ns |
| GFAP vs. EFS | 0.046 | * | <0.0001 | **** |
| GFAP vs. tCAG | <0.0001 | **** | <0.0001 | **** |
| GFAP vs. p546 | 0.4806 | ns | 0.0042 | ** |
| GFAP vs. CNP | 0.5912 | ns | <0.0001 | **** |
| GFAP vs. MAG | 0.0109 | * | <0.0001 | **** |
| GFAP vs. rMBP | 0.0005 | *** | <0.0001 | **** |
| GFAP vs. Control | <0.0001 | **** | <0.0001 | **** |
| gfa1405 vs. gfaABC(1)D | <0.0001 | **** | <0.0001 | **** |
| gfa1405 vs. CAG | 0.321 | ns | 0.9924 | ns |
| gfa1405 vs. EFS | <0.0001 | **** | <0.0001 | **** |
| gfa1405 vs. tCAG | <0.0001 | **** | <0.0001 | **** |
| gfa1405 vs. p546 | 0.919 | ns | 0.0009 | *** |
| gfa1405 vs. CNP | 0.8033 | ns | <0.0001 | **** |
| gfa1405 vs. MAG | <0.0001 | **** | <0.0001 | **** |
| gfa1405 vs. rMBP | <0.0001 | **** | <0.0001 | **** |
| gfa1405 vs. Control | <0.0001 | **** | <0.0001 | **** |
| gfaABC(1)D vs. CAG | <0.0001 | **** | <0.0001 | **** |
| gfaABC(1)D vs. EFS | >0.9999 | ns | 0.8792 | ns |
| gfaABC(1)D vs. tCAG | 0.8698 | ns | 0.9703 | ns |
| gfaABC(1)D vs. p546 | <0.0001 | **** | 0.9906 | ns |
| gfaABC(1)D vs. CNP | <0.0001 | **** | 0.999 | ns |
| gfaABC(1)D vs. MAG | >0.9999 | ns | 0.7947 | ns |
| gfaABC(1)D vs. rMBP | 0.9826 | ns | 0.8753 | ns |
| gfaABC(1)D vs. Control | 0.8056 | ns | 0.8976 | ns |
| CAG vs. EFS | <0.0001 | **** | <0.0001 | **** |
| CAG vs. tCAG | <0.0001 | **** | <0.0001 | **** |
| CAG vs. p546 | 0.0097 | ** | <0.0001 | **** |
| CAG vs. CNP | 0.0035 | ** | <0.0001 | **** |
| CAG vs. MAG | <0.0001 | **** | <0.0001 | **** |
| CAG vs. rMBP | <0.0001 | **** | <0.0001 | **** |
| CAG vs. Control | <0.0001 | **** | <0.0001 | **** |
| EFS vs. tCAG | 0.6715 | ns | >0.9999 | ns |
| EFS vs. p546 | <0.0001 | **** | 0.2408 | ns |
| EFS vs. CNP | <0.0001 | **** | 0.9995 | ns |
| EFS vs. MAG | >0.9999 | ns | >0.9999 | ns |
| EFS vs. rMBP | 0.9087 | ns | >0.9999 | ns |
| EFS vs. Control | 0.5989 | ns | >0.9999 | ns |
| tCAG vs. p546 | <0.0001 | **** | 0.419 | ns |
| tCAG vs. CNP | <0.0001 | **** | >0.9999 | ns |
| tCAG vs. MAG | 0.9532 | ns | >0.9999 | ns |
| tCAG vs. rMBP | >0.9999 | ns | >0.9999 | ns |
| tCAG vs. Control | >0.9999 | ns | >0.9999 | ns |
| p546 vs. CNP | >0.9999 | ns | 0.717 | ns |
| p546 vs. MAG | <0.0001 | **** | 0.1791 | ns |
| p546 vs. rMBP | <0.0001 | **** | 0.2635 | ns |
| p546 vs. Control | <0.0001 | **** | 0.2919 | ns |
| CNP vs. MAG | <0.0001 | **** | 0.9965 | ns |
| CNP vs. rMBP | <0.0001 | **** | 0.999 | ns |
| CNP vs. Control | <0.0001 | **** | 0.9995 | ns |
| MAG vs. rMBP | 0.9969 | ns | >0.9999 | ns |
| MAG vs. Control | 0.9119 | ns | >0.9999 | ns |
| rMBP vs. Control | >0.9999 | ns | >0.9999 | ns |

Table S1 note: no Table S1 row compares any promoter pair for the Western blot; no Western blot P value is printed anywhere.

Fig S1B: it is a plot (two bar-with-points panels, left "Western Blot Brain Quantification" for Brain Area 1, 2, 3; right "Western Blot Peripheral Quantification" for Heart and Liver; colours red p546, dark green gfa1405, orange CNP, yellow CAG). Values for the liver, heart and brain are given in section 1 above. Fig S1 has no panel "S1B" separate from the quantification: S1A is the blot images and S1B the quantification.

## Contradictions and inconsistencies found (exact words and location)

1. tCAG maximum distribution. Results text: "the tCAG promoter exhibited much lower levels of EGFP protein expression, with a maximum distribution of only 5.8% of the total brain area". Fig 4C left panel: tCAG top whisker/point reads 3.1 % (+/-0.3). Other maxima in the text (CAG 42, p546 41, gfa1405 35, GFAP about 24, gfaABC 9, CNP 37, MAG 5.5, EFS up to 16) match the plotted whisker maxima, so 5.8 for tCAG is the only mismatch.
2. Text mean intensities versus the plotted points: Results "The mean EGFP intensity was 2.678 RFUs" (EFS), "3.258 RFU" (rMBP), "9.548 RFUs" (MAG). Fig 4C right panel plots EFS points up to about 41 with a cluster at roughly 8-35, rMBP points up to about 15-28, and MAG points at 3-6 (+/-4). The EFS and rMBP text means look low against the plotted clusters, the MAG text mean looks high against its flat cluster; with +/-4 RFU reading tolerance and a possible negative adjusted value in the subtraction, this is flagged, not resolved.
3. Definition of the intensity variable. Fig 4 legend: "mean EGFP intensity in the brain area minus median EGFP intensity of the EGFP-negative brain area". Methods: "mean intensity in EGFP-positive areas minus median intensity in EGFP-negative areas". Fig S4 legend: "Mean EGFP intensity for the whole brain minus median EGFP intensity of the EGFP-negative brain areas". Three wordings: whole brain area versus EGFP-positive area.
4. Summary statistic. Results use "mean EGFP intensity (relative fluorescence units, RFUs)" and quote means; Fig 4C draws box plots whose centre line is a median (and Table S1: "Data represents mean EGFP intensity (RFU)").
5. Figure reference to a panel that does not exist: Results "Neither promoter demonstrated EGFP mRNA expression in the heart (Figure 2C)"; Figure 2 legend has panels (A) and (B) only.
6. Error bars. Fig S1 legend, Fig 2 legend and Methods never state the error-bar type for the Western blot or qPCR bars (only a bar-with-points; inference of SD is from my arithmetic, see section 1). Fig 2B legend says "fold change in EGFP mRNA expression relative to Actin" while the axis reads "Expression Normalized to Actin * 1000".
7. Western test. Methods: "two-way ANOVA between all groups"; Fig S1 shows only a few brackets and states no post-hoc test; Results say "In BA2, CAG has significantly higher total EGFP protein than CNP and p546" which matches the BA2 brackets (**** versus p546, *** versus CNP), but only comparisons with CAG are drawn for BA2 and heart.
8. n for the Western blot. Fig S1 legend: "n=4 per treatment"; Methods: 10 mice per promoter for non-whole-organ assays, qPCR "4-5 animals per construct". Not a contradiction but the Western n is never reconciled with the 10 per group.
9. Control bracket. Fig 4 legend "Statistical comparisons to CAG are shown"; no bracket for Control is drawn in either panel, while Table S1 lists CAG vs. Control as <0.0001 ****. Also no bracket is drawn for CAG vs. GFAP or CAG vs. gfa1405 in the RFU panel (Table S1: 0.9237 ns and 0.9924 ns), consistent; in the % panel a CAG vs. GFAP bracket "****" is drawn (Table S1 <0.0001 ****) and gfa1405 none (0.321 ns), consistent.
10. Liver protein versus mRNA narrative. Results: "western blot quantification confirmed the significant protein expression in the liver (Figure S1)" for gfa1405 and "the western blot results corroborate our RT-qPCR data (Figure 2B)". In Fig 2B the liver mRNA for gfa1405 is about 110 and CAG about 8 (ratio about 14); in Fig S1B the liver protein is about 81 versus about 6 (ratio about 14); consistent. No contradiction; recorded so the reader sees it was checked.
11. Cohorts text: "10 C57Bl/6 mice (5 male and 5 female) per promoter ... p546 and MAG groups, N = 9; rMBP and control group, N = 8" versus Fig 4C dots: CAG shows only 8 separable dots and tCAG, EFS and others overlap; the dot counts cannot confirm n = 10 for CAG (overlap of two points at the Q3 edge possible).

## Not printed (explicit)
- Western blot: exact P values; post-hoc test name; error-bar type; whether points are separate animals (assumed, n=4 per treatment); lane-level numeric values.
- Fig 4C: whisker definition; per-animal numeric table; numeric median/IQR.
- Fig S1B: any numeric table of the band intensities.
