# Kaplan-Meier measurement from Repudi 2021, Brain, Fig. 1C, 1F and 1I (SCI successor window, 2026-11-20; requested by ADV after the v3.1 survival flag; hypothesis level; a measurement of a published figure, not a claim about any person; no dose; not medical advice)

**Question.** The pup brief carried two survival statements for knockouts (about 4 weeks; about day 17 in the gene-addition comparator's panel). v3.1 section 6.4 found no text anchor for day 17. This file measures the held Kaplan-Meier curves of the paper that describes the line the experiment uses (neuronal deletion), to put a first-death day and a median under the choice of P14 and P18.

**Source.** Repudi et al. 2021, Brain (PMID 33914858), held operator-supplied PDF `files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.pdf`, page 6, Figure 1. Legend (held text): (C) global Wwox-null, WT n = 10, KO n = 11; (F) N-KO (Nestin-Cre) n = 14 against N-Control n = 12; (I) S-KO (synapsin-Cre) n = 15 against S-Control n = 13.

## 1. Method and resolution
* **Vector first:** the page has **0 vector drawing objects** and one embedded raster image (1000 by 1106 pixels, image xref 137); there is no vector route, so the curves were measured on pixels at native resolution (no rescaling). The second held copy (browser print) was not used.
* **Calibration, per panel:** the axes were found as the longest dark pixel runs; x ticks and the blue control line at 100 percent give the scale. Panel C: origin at the y-axis column, 6.00 pixels per day; F: 5.95 pixels per day; I: 6.00 pixels per day; vertical scale about 1.24 pixels per percent. The blue 100 percent row was found within 1 to 2 pixels of the row predicted from the tick marks (C 90 against 91; F 931 against 932; I 930 against 932).
* **Reading a step:** the red KO curve was isolated by colour; each vertical red run (a death day) gives its x position (the mean over its 1 to 2 columns) and its top and bottom levels. **Resolution: 1 pixel is about 0.17 day horizontally and about 0.8 percent vertically; the line is 1 to 2 pixels wide.**
* **Deaths per step** were taken as the step height divided by 100/n with n from the legend. **Internal check: the deaths per panel sum exactly to the legend n (C 11, F 14, I 15), and the step days fall within 0.1 day of whole days (the axis is read in whole days)**, so the days below are rounded to the nearest whole day. The x axis is "Age (days)"; that day 0 is the day of birth is assumed (the legend does not say).
* The KO curves carry no censoring ticks (all animals die); the control curves (blue) carry tick marks from about day 19 to 28 and stay at 100 percent.

## 2. Result
Deaths per day (nearest day), cumulative survival of the knockouts in brackets.
| Panel | n | Deaths by day | First death | Median (first day with survival below 50 percent) | Last death |
|---|---|---|---|---|---|
| **C, global Wwox-null** | 11 | 19: 1 (91 percent); 20: 1 (82); 21: 2 (64); 22: 3 (36); 23: 2 (18); 24: 1 (9); 25: 1 (0) | **day 19** | **day 22** | day 25 |
| **F, N-KO (the line this page uses)** | 14 | 19: 1 (93 percent); 20: 1 (86); 21: 2 (71); 22: 4 (43); 23: 2 (29); 24: 2 (14); 26: 2 (0) | **day 19** | **day 22** | day 26 |
| I, S-KO | 15 | 17: 1 (93 percent); 19: 2 (80); 20: 3 (60); 21: 4 (33); 22: 1 (27); 23: 1 (20); 24: 2 (7); 28: 1 (0) | **day 17** | **day 21** | day 28 |

**What it says for the design.**
* **N-KO (the neuronal-deletion line of this page): no death before day 19 in this cohort; 14 of 14 alive at day 18; 12 of 14 alive through day 20; 10 of 14 at day 21; 6 of 14 at day 22; none beyond day 26.** The global null (n = 11) is the same within a day (first death 19, median 22, last 25).
* **P14 and P18 are both before the first recorded death in the N-KO and global curves; P18 is one day before it.** That is inside the window but at its edge: a knockout pup at P18 is within days of the age at which half of this cohort has died, so a provoked-seizure test at P18 may confound with survival and condition, which the curves do not show. In the S-KO cohort one of 15 had already died by day 17.
* **A longitudinal arm to P20 or P25 would lose most N-KO animals** (4 of 14 dead by day 21, 8 of 14 by day 22): the Track 4 condition "only if the line survives past P20" holds for the first days only, and any readout after day 21 is a survivor readout.
* **"About day 17" is not supported for the N-KO or global curves here:** the earliest death is day 19 in both, and none reaches 0 percent before day 25. The IT trace (tx007 claim L1) quotes "0% by ~18 d" as an inherited attestation its author could not open; none of the three measured curves here reaches 0 percent before day 25 (C), 26 (F) or 28 (I). That value may describe a different paper or cohort (the Obeid 2026 figure, not held); this file does not establish that.
* **The Obeid 2026 panel was not measured:** the figure is not in the held files (only two supplementary PDFs); the open-access page returned a captcha page (PMC) and an HTTP 403 (Europe PMC) to a plain client, and neither was bypassed. The route stays open for a laboratory or operator-supplied copy.

## 3. Limits (state with the figure, always)
One cohort per panel, one laboratory; n of 11 to 15; the curve is a published figure of unknown rounding and the day scale is assumed to start at birth; deaths versus euthanasia at a humane endpoint were not checked in the Methods (the legend says "survival"); the number of deaths per step is inferred from step height and checked only by the sum; ±1 pixel (about 0.17 day) on every step day. It says nothing about condition (weight, seizures, righting) at P14 or P18, which is the pilot's first step ("colony survival and condition by age").

## 4. Reproduction (scratch script, not kept in the repository; the method in 1 is enough to redo it)
Extract image xref 137 of page 6 with PyMuPDF at native size; mark dark pixels (R, G, B below 100) and red pixels (R above 170, G and B below 100); take the longest dark row and column in each panel as the axes; step days are the mean x of contiguous columns whose red span exceeds 6 pixels; survival = (y of the x axis minus y of the lower end of the step) divided by the pixels per percent.
