# ADV-316 step 2b, blind figure reader, PMID 42395553: delegate report, verbatim (2026-11-28)

Delegate: legend-delegate, sonnet 5.5, effort HIGH stated in the dispatch (brief named no values and no sentences). It received the whole text file and the page renders of Figures 3, 5, 6, 7 and Supplementary Figures 1 to 3 (`files/figures/PMID42395553_r3/`, 110 dpi renders of the held PDF pages 29, 31 to 39). Report recovered from the session transcript and not edited by SCI. Figures 1, 2 and 4 were read in step 2 (see FIRST_READ_42395553).

BLIND FIGURE READ, PMID 42395553 (Petrozziello 2026 bioRxiv): Figures 3, 5, 6, 7 and Supplementary Figures 1-3
Hypothesis level, not medical advice. Method: full text read to its end (Methods, legends, Table 1). Every panel was opened at 110 dpi and re-cropped at 400-800 dpi from the PDF into /tmp/hz42395553/img. No network or repository file other than the two named in the dispatch was opened.
Conventions: "eye" = value read from the axis ticks, accuracy about plus or minus 0.05 of the axis range. "printed" = verbatim from the legend or figure. All bars are mean with a one-sided error cap (read as SEM, as the legends say). All quantified panels except Fig 3A, 3B, 3C and 7D are bars without individual points, so n and the replicate unit cannot be seen.
Arithmetic check done by me from printed numbers: p recomputed from every printed F and df, and exact Mann-Whitney p from U and n. All agree except two items, flagged below as A1 and A2.

## FIGURE 3 (page 29), human post-mortem prefrontal cortex (PFC), western blot

**3A**
- Plot: y = "WWOX (%GAPDH)", axis 0-150. x = Control, HD. Dot plot with a central line and caps.
- Blot above: one Control lane and one HD lane, WWOX row plus GAPDH row. The HD WWOX band is visibly darker than the Control band. GAPDH is similar, with a faint smear in the HD lane. No ladder.
- Eye: Control line about 40 (caps about 35 to 44). HD line about 65 (caps about 60 to 69).
- Points counted: Control 13 (matches printed "n=13"). HD 17 distinct points visible against printed "n=18"; one may be hidden behind the median line.
- Replicate unit: UNSTATED, but one point per donor is implied by Table 1.
- Range: Control about 14-64. HD about 31-101. Low HD points (about 31-35) lie inside the Control range.
- Test: printed "Mann-Whitney U test=31, p=0.0005". One bracket Control-HD, "***". Consistent. By normal approximation, U=31 fits 18 vs 13 (p about 0.0006) better than 17 vs 13 (about 0.0009).
- Legend says "mean±SEM". Methods say "median and interquartile range or mean±SEM". The panel shows a line with caps, so the type cannot be told from the picture.

**3B**
- Plot: x = "CAG repeat" (35-55), y = "WWOX" (0-200, no unit). Scatter with a drawn regression line that is nearly flat (slightly downward). No r or p on the plot.
- Printed: "Spearman's correlation, r=0.05302, p=0.8397".
- Points: 18 distinguishable (CAG 40, 41x2, 42x2, 43x2, 44x2, 45, 46, 48x2, 49x2, 50, 51x2). The legend says "in PFC" without saying HD-only, but the points are HD.
- Mismatch with Table 1: Table 1 lists CAG allele 1 for 17 HD cases (HD6, 19, 20, 21 are "Not determined"). Table 1 has no case with CAG 45 or 46 and has three at 44. The plot has 45 and 46 and only two clearly visible at 44.
- The WWOX value of the CAG-45 point (about 100) equals that of the age-56 point in 3C. Table 1 lists the age-56 case (HD6) as CAG "Not determined".
- I cannot resolve this by eye. Fig 3B n is stated nowhere in the legend.

**3C**
- Plot: x = "Age of death" (0-100), y = "WWOX" (0-200). Flat to slightly rising line. Printed "r=0.05891, p=0.8164".
- Points: 18, with ages 36 to 78. These match Table 1 HD1-18 ages, with HD6 (56) included. HD19-21 (ages 58, 74, 41) are not plotted.
- No bracket or mark. No legend-versus-picture mismatch.
- Legend key "*** p<0.001" fits 3A.

## FIGURE 5 (pages 31-32), SH-SY5Y human neuroblastoma cells

**5A**
- Immunofluorescence (IF) images: γ-H2AX (red), DAPI (blue), merge. Rows: Vehicle, CPT (10 µM), rWWOX 10, 100, 150 ng/mL. Scale bar present; the legend says 50 µm.
- Vehicle and 10 ng/mL are dim with a few bright nuclei. CPT has many bright nuclei. 100 and 150 ng/mL show higher diffuse red in many nuclei plus some bright nuclei (150 most diffuse).
- Number of fields per image: one field shown. Methods say "At least 4 random images per condition".

**5B**
- Plot: y = "γ-H2AX (Intensity Density)", axis 0-40000. Bars with a colour key only (no x labels).
- Eye: Vehicle about 30,200 (cap about 30,500). CPT about 36,700 (cap about 38,300). 10 ng/mL about 31,500. 100 ng/mL about 33,200. 150 ng/mL about 33,500.
- Brackets, all anchored at Vehicle: **** to CPT, * to 100 ng/mL, ** to 150 ng/mL. 10 ng/mL has no bracket and no mark, matching the legend (p=0.6018).
- Printed test: "One-way ANOVA ... F(4,42)=13.96; p<0.0001". Tukey p printed: CPT <0.0001, 100 ng/mL 0.0139, 150 ng/mL 0.0038. Marks match.
- n: UNSTATED. The df imply 47 observations over 5 groups (about 9-10 per group). The unit is UNSTATED. Methods say images per condition, so images or fields are a possibility, but the legend does not say.
- Eye differences from vehicle: CPT about +6,500 (about 22%). 100 and 150 ng/mL about +3,000 (about 10%).

**5C**
- Blot: one NTC lane and one WWOXOE lane. WWOX row: NTC faint, OE strong. GAPDH row: similar.
- NTC band sits slightly lower than the OE band, which looks thicker and higher. No ladder, so size is not readable.
- Bar: y = "WWOX/GAPDH (IDVs)", 0-2.5. NTC = 1.0 (eye, so the bar is normalised to NTC; caps to about 1.36). OE about 1.9 (cap about 2.04).
- By eye the shown lane pair looks like a larger fold difference than the 1.9 bar. A single lane pair cannot settle this.
- Test: printed "Mann-Whitney U test=1, p=0.0476". Bracket "*". n: UNSTATED.
- Arithmetic: exact two-sided p=0.0476 at U=1 arises only for group sizes 3 and 6 among n up to 12. It does not arise for 4 vs 4 (which gives 0.0571). The group sizes are not written anywhere I can see.

**5D**
- IF images, γ-H2AX shown in GREEN, mCherry in red, DAPI in blue, merge. Rows: NTC, CPT (10 µM), WWOXOE. The legend says green and red, which is correct.
- All three rows, including NTC, show clear mCherry signal. The legend and text define NTC as "non-transfected control"; Methods describe a control plasmid with mCherry (ORF_Stuffer). The picture is as expected for a control-plasmid line and not for a non-transfected line. The legend does not explain this.
- NTC green is diffuse, cytoplasmic and nuclear. CPT has many bright nuclei. WWOXOE has moderately brighter nuclei with some foci.

**5E**
- Plot: y = "γ-H2AX (Intensity Density)", 0-150,000,000. Bars NTC, CPT, WWOXOE.
- Eye: NTC about 41M (cap 44M). CPT about 104M (cap 114M). WWOXOE about 82M (cap 100M).
- Brackets: ** NTC-CPT, * NTC-WWOXOE.
- Printed: "F(2,12)=8.643; p=0.0047" (recomputed p=0.0047), Tukey CPT p=0.0037 (**), WWOXOE p=0.0314 (*). Marks match.
- n: UNSTATED. The df imply 15 observations, about 5 per group. Unit UNSTATED.
- Scale note: NTC here is about 4×10^7, while Vehicle in 5B is about 3×10^4. The legend does not explain the roughly 1000-fold scale difference between 5B and 5E.
- Fig 5 legend key lists "* ** ****", all of which occur across B, C and E.

## FIGURE 6 (pages 33-34), post-mortem HD PFC lysates, immuno-depletion, SH-SY5Y

**6A**
- Blot: 9 lanes labelled HD1, HD1+, HD1-, HD2, HD2+, HD2-, HD3, HD3+, HD3-. Ladder at left (250 to 10). Arrow "WWOX" at about 58-60 kDa by the ladder (between 55 and 72).
- No loading-control row (no GAPDH or other) and no IgG-only or mock-depleted lane.
- HD lanes: strong bands at about 78, 68, 55 and 43 kDa. HD+ lanes: one very large saturated band spanning about 52-68 kDa with a smear below it.
- HD- lanes: weak bands, a fainter doublet near 55-62 kDa plus a band at about 40-47 kDa. HD- lanes are weaker than HD lanes at several positions, not only at the arrow.
- The same catalogue antibody (#ab137726) is listed in Methods for depletion and for blotting. The secondary listed in Methods is goat anti-rabbit. The figure does not show which bands are the antibody.
- The legend says "(n=3)", matching 3 donors.

**6B**
- Plot: y = "WWOX (IDVs)", 0-25000. Bars HD, HD+, HD-.
- Eye: HD about 12,800 (cap 13,700). HD+ about 17,900 (cap 19,300). HD- about 3,200 (cap 3,800).
- Brackets: * HD-HD+, **** HD+-HD-, *** HD-HD. Legend p: 0.0210, <0.0001, 0.0009. Marks match.
- Printed test: "F(4,6)=62.79; p<0.0001". Only three groups are plotted, so numerator df 4 looks like a typo for 2 (F(2,6) gives the same p<0.0001). n: UNSTATED beyond "n=3" for panel A. There is no per-donor point and no GAPDH normalisation.

**6C**
- IF images, γ-H2AX red, DAPI, merge. Rows: Vehicle, CPT (10 µM), HD, HD+, HD- (each 25 ng/mL).
- Vehicle dim. CPT many bright nuclei. HD, HD+: dim diffuse red with scattered bright nuclei. HD-: dim, with a few bright nuclei.
- No row for a mock-depleted lysate.

**6D**
- Plot: y = "γH2AX (Intensity Density)", 0-40000.
- Eye: Vehicle about 30,700. CPT about 36,700 (cap 39,000). HD about 35,400. HD+ about 35,400. HD- about 31,700 (cap 32,400).
- Brackets (all from Vehicle): ** CPT, * HD, * HD+. HD- has no bracket (legend p=0.9608). There is no bracket for HD vs HD- or HD+ vs HD-.
- Printed: "F(4,27)=5.699; p=0.0019" (recomputed 0.0019). Tukey: CPT p=0.0037 (**), HD p=0.0473 (*), HD+ p=0.0424 (*). Marks match.
- n: UNSTATED. The df imply 32 observations, so 6-7 per group. Unit UNSTATED.
- Legend key lists *** and ****, which do not occur in D (they occur in B).
- Eye difference HD vs HD- is about 3,700, but it is not tested in the figure.

## FIGURE 7 (pages 35-36), RPE-1 AAVS1-CAG115 cells

**7A**
- Blot: 12 lanes in two strips with a gap between lane 6 and lane 7. Lanes: NTC #1 to #6 alternating with WWOXOE #1 to #6. WWOX row: each OE lane has a strong band, each NTC lane a very faint band. GAPDH row: roughly even; OE #1 and OE #4/5 slightly weaker.
- Bar: y = "WWOX/GAPDH (IDVs)", 0-50. NTC about 1 (eye). OE about 40 (cap about 43).
- Printed: "Mann-Whitney U test=0, p=0.0022". This is exactly the exact value for 6 vs 6 with U=0. Bracket "**". Matches.
- The legend says "six clones"; the Methods say "six parallel populations".

**7B**
- IF images, γ-H2AX red, DAPI, merge. Rows: NTC, CPT (10 µM), WWOXOE. Few cells per field, single nuclei resolved.
- NTC: a mix of dim and a few moderate nuclei. CPT: several bright nuclei. OE: more bright nuclei than NTC.

**7C**
- Plot: y = "γ-H2AX (Intensity Density)", 0-60,000,000.
- Eye: NTC about 38.6M (cap 41.2M). CPT about 53.6M (cap 54.5M). OE about 47.2M (cap 48.5M).
- Brackets: *** NTC-CPT, ** NTC-OE. Legend Tukey p: 0.0002 and 0.0081. Marks match.
- Printed: "F(2,11)=18.07; p=0.003". Recomputing from F(2,11)=18.07 gives p about 0.0003, not 0.003. This is a probable typo, flagged as A2.
- n: UNSTATED. The df imply 14 observations. Unit UNSTATED.

**7D**
- Plot: y = "Avg. repeat gain" (0-4), x = "Days in culture" (0, 14, 28, 42). Individual trajectories as dashed lines with points; key "Control OE" (open grey circles) and "hWWOX OE" (purple filled).
- Control line count: 6 (6 distinct open points at day 28 and 42). Purple: at least 4 visible, overlaps likely, so 6 is consistent.
- Eye, day 14: control about 0.8-0.9 for five lines and 1.74 for one; purple about 1.0-1.4.
- Eye, day 28: control about 0.87-3.05; purple about 1.87-2.82.
- Eye, day 42: control about 1.97-4.05; purple about 2.4-3.1.
- No mean line, no brackets, no per-time-point mark.
- The legend says "Representative traces" and "Data are shown as mean±SEM". Neither matches the panel, which shows individual populations.
- Printed: multiple linear regression, "Days in vitro ... p<2×10⁻¹⁶, ... WWOX overexpression had no effect (p=0.877)". Not shown on the panel.
- Naming: "Control OE" in the panel key vs "NTC" elsewhere in the same figure.

## SUPPLEMENTARY FIGURE 1 (page 37), SH-SY5Y

**S1A**
- IF images. Rows: Vehicle, CPT (10 µM), HD 10 ng/mL, HD 25 ng/mL, Control 25 ng/mL. Scale bars present.
- HD 25 shows more bright nuclei than HD 10 or Control. Vehicle dim.
- The legend says "homogenates" where the text says "lysates".

**S1B**
- Plot: y = "γ-H2AX (Intensity Density)", 0-40000.
- Eye: Vehicle about 30,000. CPT about 36,500 (cap 38,100). 10 ng/mL HD about 31,200. 25 ng/mL HD about 33,200 (cap 33,700). 25 ng/mL Control about 31,600.
- Brackets: **** Vehicle-CPT, * Vehicle-25 HD. No mark on 10 HD or Control, matching the legend.
- Printed: "F(4,34)=11.81; p<0.0001". Tukey CPT <0.0001, 10 HD 0.8218, Control 0.5273, 25 HD 0.0211. Marks match.
- n: UNSTATED. The df imply 39 observations. The unit and the number of lysate donors are UNSTATED here (Methods give n=3 control and 3 HD).
- No bracket for 25 ng/mL HD vs 25 ng/mL Control. Eye difference between them is about 1,600, which is not tested.
- Observation: the Vehicle, CPT, 10 ng/mL and 25 ng/mL bar heights and error caps resemble those in Fig 5B (Vehicle 30.2k, CPT 36.7k, rWWOX 10 31.5k, rWWOX 100 33.2k) and the Vehicle/CPT bars in Fig 6D. The images in S1A, 5A and 6C differ, and the F df differ (4,34), (4,42), (4,27). Whether vehicle/CPT data are shared across experiments is UNSTATED.

## SUPPLEMENTARY FIGURE 2 (page 38), SH-SY5Y, MTT after rWWOX 24 h and 48 h

- Plot: title "SH-SY5Y cells". y = "Cell viability (MTT Assay)", 0-0.10 (no unit). x = rWWOX 0, 1, 10, 100, 500 ng/mL, for 24 h (white) and 48 h (black).
- Eye, 24 h: 0 about 0.076 (cap 0.083). 1 about 0.067 (cap 0.078). 10 about 0.070 (cap 0.073). 100 about 0.024 (cap 0.033). 500 about 0.008 (cap 0.012).
- Eye, 48 h: 0 about 0.061 (cap 0.077). 1 about 0.061 (cap 0.078). 10 about 0.019 (cap 0.040). 100 about 0.004 (cap 0.007). 500 about 0.009 (cap 0.039, very large).
- n: UNSTATED. The df F(4,20) imply 30 observations, so 3 per cell. The unit is UNSTATED.
- Marks: many horizontal lines without end ticks.
  - 24 h lines: 0 to 500, 0 to 100, 1 to 500, 10 to 500, 10 to 100. Stars: ** above the top line, * above 1-500, * above 10-500. The 0-100 and 10-100 lines have no star of their own.
  - 48 h lines: 0 to 500, 0 to 100, 0 to 10, 1 to 500, 1 to 100, 1 to 10. Stars: * above 0-500, * above 1-500. The other four lines have no star of their own.
  - A top bracket "**" joins the 24 h and 48 h groups (the time main effect).
- Legend p vs figure marks: legend 24 h p=0.0004 (500 ng/mL) would be "***" under the legend's own scale, but no *** appears. 24 h p=0.0086 would be "**". 48 h p=0.0460 (*), 0.0030 (**), 0.0081 (**) are all drawn under a single "*". Lines for comparisons that the legend never reports (for example 1 vs 500, 10 vs 500, 1 vs 10) are drawn.
- Legend key typo: "Scale bar 50µm. p>0.05." There is no image or scale bar in this figure.
- Printed ANOVA: dose F(4,20)=21.15 p<0.0001, time F(1,20)=10.67 p=0.0037, interaction F(4,20)=3.280 p=0.0320. All recomputed p agree.

## SUPPLEMENTARY FIGURE 3 (page 39), SH-SY5Y, siRNA

**S3A**
- Blot: one siControl lane, one siWWOX lane. WWOX: strong vs faint. GAPDH: roughly equal.
- Bar: y = "WWOX/GAPDH (IDVs)", 0-100. siControl about 81 (cap 92). siWWOX about 38 (cap 44). By eye the bar shows about a 53% reduction; the shown lane pair looks like a larger reduction.
- Printed: "n=4 replicates, Mann-Whitney U test=0, p=0.0286". This equals the exact p for 4 vs 4 with U=0. Bracket "*".

**S3B**
- IF images: siControl, siWWOX, CPT (10 µM). siControl has a few bright spots. siWWOX is nearly dark. CPT is bright and diffuse. DAPI looks blurrier than in other figures.
- Whether the CPT row is siControl plus CPT or untransfected plus CPT is UNSTATED. Whether there is an untreated or vehicle group is UNSTATED; none is shown.

**S3C**
- Plot: y = "γ-H2AX (Intensity Density)", 0-2.0×10^7. The axis title overlaps the tick labels.
- Eye: siControl about 12.2×10^6 (cap 13.0×10^6). siWWOX about 10.9×10^6 (cap 11.4×10^6). CPT about 17.8×10^6 (cap 18.5×10^6).
- Brackets: ** siControl-siWWOX, **** siWWOX-CPT, **** siControl-CPT. Legend p: 0.0044, <0.0001, <0.0001. Marks match.
- Printed: "F(2,13)=164.1; p<0.0001". n: UNSTATED beyond "n=4 replicates" for A. The df imply 16 observations.
- Eye difference siWWOX vs siControl is about 1.3×10^6 (about 11%), against about 53% by the WWOX bar in S3A.

## TEXT VS FIGURE

| # | Results sentence (verbatim) | Verdict | Why |
|---|---|---|---|
| 1 | "WWOX levels were increased in HD PFC compared to control PFC (Figure 3A)." | SUPPORTS | HD about 65 vs Control about 40 by eye; bracket with ***; the lane pair is consistent. HD n=17 visible vs "n=18". |
| 2 | "However, WWOX levels did not correlate with either CAG repeat length (Figure 3B) or age at death (Figure 3C) in HD samples." | SUPPORTS (no visible trend) | Both fitted lines are near flat and the printed r are 0.05. The 3B point set (18, with CAG 45 and 46) does not match Table 1 allele-1 values (17, no 45 or 46). |
| 3 | "treatment with rWWOX ... significant decreases observed at 100 or 500ng/mL after 24h and at 10, 100 or 500ng/mL after 48h (Supplementary Figure 2)" | SUPPORTS in direction | Bars fall as described. Mapping of every mark to the pair it covers is not readable (see S2 marks), and "cell death" is an MTT readout here. The 24 h p=0.0004 for 500 ng/mL is marked "**" not "***". |
| 4 | "g-H2AX levels were increased in CPT-treated cells and in cells treated with either 100 or 150ng/mL of rWWOX compared to vehicle-treated cells (Figure 5A and B)." | SUPPORTS | Marks and bars agree. The 100/150 increase is small (about 10%, +3,000 on 40,000 by eye). The Supp 2 figure shows MTT at 100 ng/mL, 24 h about 0.024 vs vehicle 0.076 (same dose and time as 5B). |
| 5 | "WWOX overexpression was confirmed by western blotting demonstrating higher WWOX levels in WWOXOE compared to non-transfected control (NTC) cells (Figure 5C)." | SUPPORTS | Blot and bar agree (OE about 1.9 vs NTC 1.0). A single lane pair is shown, and n is UNSTATED. The sizes of the two groups behind U=1, p=0.0476 are not written; 3 and 6 reproduce it, 4 and 4 does not. |
| 6 | "g-H2AX levels were increased in both CPT-treated cells and WWOXOE cells compared to NTC cells (Figure 5D and E)." | SUPPORTS on the bars; images cannot settle OE | Bars: NTC about 41M, OE about 82M, CPT about 104M with ** and *. The images show OE only modestly above NTC. NTC cells show mCherry signal (see 5D). |
| 7 | "...lower WWOX levels in siWWOX-treated cells compared to siControl-treated cells (Supplementary Figure 3A)." | SUPPORTS | Blot and bar (about 81 vs about 38) agree, with n=4 and * . |
| 8 | "...g-H2AX levels were decreased in siWWOX-treated cells compared to both siControl- and CPT-treated cells (Supplementary Figure 3B and C)." | SUPPORTS | Bars about 10.9M (siWWOX), 12.2M (siControl), 17.8M (CPT) with ** and ****. Size about 11% vs siControl. |
| 9 | "neither control PFC lysates nor the lower concentration of HD lysates altered g-H2AX levels compared to vehicle-treated cells (Supplementary Figure 1), indicating that the increase in g-H2AX is both concentration-dependent and specific to HD." | CANNOT SETTLE the second half | First half is supported (no marks; 10 HD about 31.2k, Control about 31.6k vs Vehicle about 30.0k). The 25 HD bar (about 33.2k) is above Control (about 31.6k) by about 1.6k, but no HD-vs-Control bracket is shown. Control PFC is tested at one concentration only. |
| 10 | "Immuno-depletion was confirmed by western blotting (Figure 6A). ... a significant decrease in WWOX levels in WWOX-depleted lysates (HD-), compared to HD and WWOX-enriched (HD+) lysates (Figure 6B)." | PARTLY SUPPORTS | HD- bands are weaker than HD/HD+ at the arrow, and 6B bars agree (about 3.2k vs 12.8k vs 17.9k) with the marked p. But no loading control or mock-depleted lane is shown; other bands also drop in HD-; the HD+ band is saturated; the band assignment cannot be settled from the picture. F(4,6) is a probable typo for F(2,6). |
| 11 | "Treatment with HD or HD+ lysates (25ng/mL/24h) increased g-H2AX levels, whereas HD- lysates had no effect (Figure 6C and D)." | SUPPORTS vs vehicle only; CANNOT SETTLE "reduced by depletion" | Marks vs Vehicle only: HD about 35.4k (*), HD+ about 35.4k (*), HD- about 31.7k (no mark). There is no HD-vs-HD- bracket. A mock-depleted lysate group is not shown. The figure title ("WWOX immuno-depletion reduced HD-induced g-H2AX accumulation") rests on an untested HD vs HD- contrast of about 3.7k. |
| 12 | "...WWOX overexpression was confirmed by western blotting revealing higher WWOX levels in all six clones compared to NTC cells (Figure 7A)." | SUPPORTS | Six OE lanes each stronger than the paired NTC lane; U=0, p=0.0022 matches 6 vs 6. |
| 13 | "g-H2AX levels were increased in RPE-1AAVS1-CAG115 cells overexpressing WWOX (WWOXOE) compared to NTC cells, similar to CPT-treated cells (Figure 7B and C)." | SUPPORTS direction; CANNOT SETTLE "similar" | NTC about 38.6M, OE about 47.2M, CPT about 53.6M, with ** and ***. No OE-vs-CPT bracket. OE is about 22% above NTC and CPT about 39%. The printed "p=0.003" for the ANOVA is probably 0.0003. |
| 14 | "WWOX overexpression did not alter the rate of CAG repeat instability at any time point (Figure 7D)." | CANNOT SETTLE (no contradiction seen) | The figure shows only individual traces with overlapping ranges at day 14, 28 and 42 and no per-time-point test. The regression (div+group, p=0.877) is in the legend, not drawn. By eye at day 14 the purple lines sit mostly above the controls (about 1.0-1.4 vs about 0.8-0.9 for five of six controls). |

## Flags, for the record
- A1 (F(4,6) in Fig 6B): only three groups plotted; probable typo for F(2,6). The p does not change.
- A2 (F(2,11)=18.07 in Fig 7C): recomputed p about 0.0003 vs printed 0.003.
- Legend items the picture does not show: Fig 7D "mean±SEM" and "Representative traces"; Supp Fig 2 "Scale bar 50µm. p>0.05."
- n and the replicate unit are not stated for 5B, 5C, 5E, 6B, 6D, 7C, S1B, S2, S3C. Only dfs imply totals.
- Absent groups in Fig 6: no mock/IgG-depleted lysate and no loading control.

## What I could not read or establish
- Which of the 18 points in Fig 3B correspond to which Table 1 case, and whether an HD point is hidden in 3A.
- Whether vehicle/CPT bar values are shared across Fig 5B, Supp Fig 1B and Fig 6D, because shared data are not stated.
- The band identity of WWOX in the Fig 6A lanes, and the size of the WWOX band in other blots (only Fig 6A has a ladder).
- Replicate counts and unit (cell, field or well) for every bar graph.
- Group sizes behind Fig 5C.
- Per-time-point values in Fig 7D (overlapping points).
- Figure 4 and Figures 1-2 were not in scope and were not read.
- I did not open framework/protocols/delegation_budget.md because the dispatch forbade any other repository file.
