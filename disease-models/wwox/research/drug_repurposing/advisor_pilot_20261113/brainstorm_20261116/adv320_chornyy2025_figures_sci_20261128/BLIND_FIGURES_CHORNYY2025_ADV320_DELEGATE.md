# DELEGATE REPORT ADV-320: blind figure read, Chornyy et al. 2025 (PMID 41036104, PMC12481918)

Effort requested and used: HIGH (state-back as asked). Model: Sonnet 5.5 (from my own system statement; not read back from a transcript census). Extraction only; no interpretation. Reference-genotype class only; not medical advice.

Labels used throughout: PRINTED = text or number on the figure/legend/table; EYE = read from a plotted point or bar top against an axis tick (tick named); TEXT-ONLY = in the XML/PDF body text or legend, not on a panel.

## 0. Blindness disclosure (must be read first)
At the start, listing the output folder, I opened `PREREG_ADV320_CHORNYY2025_FIGURES_SCI_20261128.md` (it sat in the same folder) and so saw H1/H2 and the CLAIM 047 numbers before opening any figure. I did not use it to select or reword what I extracted; every panel below was read in full, but the reading is NOT fully blind with respect to the liver blot (Fig S1) and Fig 4C panels. The caller should weigh this.

## 1. Access routes and results
- Bucket listing `https://pmc-oa-opendata.s3.amazonaws.com/?list-type=2&prefix=PMC12481918` returned HTTP 200 with 12 keys under `PMC12481918.1/`: .json, .pdf (11.4 MB), .txt, .xml, fx1.jpg, gr1-gr5.jpg, mmc1.pdf (6.4 MB), mmc2.pdf (33.6 MB).
- No 429, 403 or challenge page on any request. No other host used. No e-mail or identity sent.
- The bucket gr1-gr5.jpg are REDUCED copies (726-748 px wide; EXIF says originals 2244-2906 px). Full-resolution main figures (2906 px wide, 500 ppi; Fig 3 is 2244 px) were extracted from the bucket's mmc2.pdf ("Article plus supplemental information", same bucket) with `pdfimages`. Supplementary figures S2, S3 are 2250 px; S4 is 1280x492 (171 ppi); **Fig S1 exists only as a 726x720 px raster at 100 ppi in both mmc1.pdf and mmc2.pdf** (no vector text; no higher-resolution copy reached). S1 values below are therefore coarser (about +/-3 units on the 0-150 axis).
- Saved in `/home/desktop/.claude/jobs/b0e37f80/tmp/adv320/figs/` (only images): fx1.jpg, gr1-gr5.jpg (bucket, reduced), Fig1..Fig5_fullres_from_mmc2_pdf.png, FigS1_from_mmc2_pdf_726x720.png, FigS2/S3/S4_from_mmc2_pdf.png. Crops and PDFs are in `scratch/` (crops, ex, mmc1.pdf, mmc2.pdf, article.pdf, text.txt).
- Read: XML stripped to text (Methods, Results, all five main legends, supplement title list); mmc1.pdf text (Table S1 and legends S1-S4). Every main figure (1-5), graphical abstract (fx1) and S1-S4 was opened whole, with enlarged crops for the quantitative panels (S1A, S1B left/right, S1 liver low bars, Fig 2B CNS and peripheral, Fig 3 liver row, Fig 4C left/right, Fig 5B, 5D both, S4A, S4B). Not opened separately as enlarged crops: the microscopy image panels (Fig 4A/B, 5A/C, S2, S3), which carry no numbers; they were described from the whole figure.
- Not reachable: Table S1 exists only as text in mmc1.pdf (read). Source data: "available upon request" (TEXT-ONLY), no file.

## 2. Methods facts relevant to n and replicate unit (TEXT-ONLY, XML)
- Cohort: 10 C57Bl/6 mice per promoter (5 M, 5 F) plus 3 extra for whole-organ images; fewer in some groups (p546 and MAG N=9; rMBP and control N=8). Neonatal P0-P1 single i.c.v., left ventricle, 5 uL. Doses (vg/animal): 7.50E10 for GFAP, gfa1405, gfaABC(1)D, p546, CAG, EFS; 7.00E10 tCAG; 8.50E10 CNP and rMBP; 8.00E10 MAG. Sacrifice 4 weeks.
- Three mice per construct for whole-organ images; remaining 10 per construct for all other assays (the same 10 animals feed qPCR, western, IHC by hemisphere).
- qPCR: 4-5 animals per construct; EGFP relative to beta-actin (delta CT); samples run in triplicate, 2-3 plates per promoter, 6-9 wells per sample, plates averaged.
- Western: 25 ug protein per lane, GAPDH (AF488) and GFP (AF568) fluorescent detection, all blots imaged at same exposure (1 s AF488; 101 s AF568); statistics two-way ANOVA between all groups; "p546 and gfa1405 heart blots had minor contrast enhancement for GAPDH band visualization"; images inverted and converted to black and white; post-processing in Photoshop. Tissues: BA1, BA2, BA3, heart, liver. (BA1-BA3 for western vs qPCR are different serial sections of the left hemisphere.)
- Fig 4 stats: one-way ANOVA, Tukey (Table S1). Fig 5 colocalization: one-way ANOVA; for CNP vs MAG unpaired t test.

## 3. Figure S1 (supplement; the liver/heart/brain western blot) [the panel the caller asked about]
Source: FigS1 (726x720 px). Legend PRINTED: "EGFP protein expression by Western blot in three brain regions and peripheral tissues of 4-week-old AAV9-EGFP injected mice. (A) Western blots of EGFP in BA1, BA2, BA3, heart, and liver of 4-week-old AAV9-p546-EGFP, AAV9-gfa1405-EGFP, AAV9-CNP-EGFP, and AAV9-CAG-EGFP injected mice (n=4 per treatment). GAPDH serves as a loading control. All fluorescence images were inverted and converted to black and white. Due to differences in transfer efficiency, p546 and gfa1405 heart blots had minor contrast enhancement for GAPDH band visualization. (B) Quantification of band intensity indicates CAG drives significantly greater protein expression in BA2 and heart over p546 and CNP. gfa1405 drives significantly greater protein expression in the liver over CAG. *** p <= 0.001, **** p <= 0.0001".

### S1A (blot images)
- Layout PRINTED: column headers WT, p546, gfa1405, CNP, CAG; row labels BA1, BA2, BA3, Heart, Liver; each row has a GAPDH band and an EGFP band label.
- Lanes: per tissue row, 1 WT lane plus 4 lanes for each of the 4 promoters = 17 lanes per tissue (EYE count). n=4 per treatment PRINTED (legend). Replicate unit of a lane: UNSTATED in legend (legend says n=4 per treatment; Methods: 10 animals per group, so each lane presumably one animal; this is not printed).
- Each promoter appears as its own strip with visible gaps and different background shading between strips (and the WT lane as a separate narrow strip); the legend does not say whether the strips come from one gel or one membrane (UNSTATED).
- Loading control: GAPDH (PRINTED).
- EYE description of bands (qualitative, no densitometry on the image):
  - BA1: EGFP band faint-visible in all 4 gfa1405 lanes, all 4 CNP lanes (very faint), all 4 CAG lanes; no visible EGFP band in p546 or WT.
  - BA2: EGFP bands visible in 4/4 gfa1405, 4/4 CNP (faint in lanes 3-4), 4/4 CAG; no visible band in p546 (very faint trace) or WT.
  - BA3: faint band in p546 lane 3 only; gfa1405 lanes 1-3 visible, lane 4 very faint; CNP lane 1 clearly visible, lanes 2-4 fading; CAG very faint in all 4.
  - Heart: EGFP band visible in 4/4 CAG lanes (lower than GAPDH band); no visible EGFP band in p546, gfa1405 or CNP. GAPDH band is pale in the p546 and gfa1405 heart strips (contrast enhanced per legend) and dark in WT, CNP, CAG.
  - Liver: EGFP band visible in 4/4 gfa1405 lanes; no discrete EGFP band in p546, CNP, CAG or WT (only faint background texture at the EGFP position in p546, CNP and CAG). GAPDH bands present in all lanes.
- Quantification shown in panel B (not on the images).

### S1B left: "Western Blot Brain Quantification"
- Axis PRINTED: y "EGFP Relative to GAPDH *100", ticks 0, 50, 100, 150. x: Brain Area 1, Brain Area 2, Brain Area 3. Four bars per area: p546 (red), gfa1405 (dark green), CNP (orange), CAG (yellow), legend in panel B right. Bars with individual dots; error-bar type UNSTATED (caps drawn). n per bar PRINTED only as "n=4 per treatment" (legend); dots visible are 3-4 per bar (some overlap).
- EYE bar tops (tick used: 0 at baseline, 50, 100, 150): 
  - BA1: p546 about 2; gfa1405 about 16; CNP about 12; CAG about 28.
  - BA2: p546 about 4; gfa1405 about 44; CNP about 21; CAG about 64.
  - BA3: p546 about 3; gfa1405 about 17; CNP about 25; CAG about 8.
- EYE individual dots: BA2 gfa1405 about 71, 60, ~44, ~1 (error bar from about 14 to about 75); BA2 CAG about 101, 69, 58, 30 (error bar about 35 to about 94); BA3 CNP one dot about 55 with others about 10-25; BA3 gfa1405 about 25, 22, 17, 3; BA1 CAG about 35, 34, 25, 20.
- PRINTED marks: BA2: bracket p546 to CAG "****"; bracket CNP to CAG "***". No marks printed on BA1 or BA3 and none joining gfa1405 with another group.

### S1B right: "Western Blot Peripheral Quantification"
- Axis PRINTED: y "EGFP Relative to GAPDH * 100", ticks 0, 50, 100, 150. x: Heart, Liver. Colour legend: p546 red, gfa1405 dark green, CNP orange, CAG yellow. Error-bar type UNSTATED. n "n=4 per treatment" (legend); dots visible 4 per bar where separable.
- EYE bar tops (0, 50, 100, 150 ticks; 1 unit about 1.1 px at native size, so +/-3):
  - Heart: p546 about 5; gfa1405 about 6; CNP about 6 (one dot about 14); CAG about 56.
  - Liver: p546 about 5; gfa1405 about 81; CNP about 6; CAG about 6 (dots about 5-8).
- EYE dots, liver gfa1405: about 104, 90, 79 (partly hidden by bar), 49; error bar caps about 104 and 57. Dots, heart CAG: about 72, 69, 61, 21; caps about 79 and 33.
- Liver points of p546, CNP and CAG all fall within about 3-9 and do not overlap the gfa1405 points (the lowest gfa1405 dot at about 49 is far above them). Heart points of p546, gfa1405, CNP are about 2-14.
- PRINTED marks: Heart: p546 to CAG "****"; CNP to CAG "****". Liver: gfa1405 to CAG "****". No mark printed between gfa1405 and p546 or CNP in liver, none between gfa1405 and others in heart.
- No brain-region versus liver ratio, no table of values, and no per-animal numbers are printed; the only printed number-like items are axis ticks and stars.
- TEXT-ONLY: the main text says "In the periphery, CAG and gfa1405 drove the greatest EGFP protein expression in the heart and liver, respectively" and "western blot quantification confirmed the significant protein expression in the liver (Figure S1)".

## 4. Figure 1 (full-res; schematic, no data)
Diagram of endogenous GFAP promoter segments A, B, C1-C6 (variable C region), D, bp; boxes per C segment with PRINTED notes (C1 "Best neuraxial targeting; Areas include: cerebellum, cerebral cortex, olfactory bulb, hippocampus, thalamus, and brain stem" check; C2 "Inhibitory Region" cross; C3 "2nd best neuraxial targeting; Strong targeting in cerebral cortex and cerebral nuclei; Minimal targeting in brain stem, midbrain, and thalamus" check; C4 "Localized expression to cerebral cortex, retrosplenial area, hippocampus, and hypothalamus only" cross; C5 "Diffuse distribution throughout the cerebral cortex with focuses in the orbital area only" check; C6 "Distribution found in cerebral cortex, retrosplenial area, and hippocampus only" check). "Based on Lee et al. 2008". Bottom diagram "gfaABCD1405 (gfa1405) promoter": A, B, C1, C3, C5, C6, D, bp (arrows from C1, C3, C5, C6). No n, no numbers.

## 5. Figure 2 (full-res)
### 2A: schematic. ssAAV9-EGFP, promoter-EGFP cassette; ICV injection, WT mouse (P0-P1), 4 weeks, brain split into Brain Area 1, 2, 3 (fresh frozen; qPCR and western) and fixed (microscopy); "Brain, Spinal Cord and Peripheral Tissues". No numbers.
### 2B left: "EGFP Expression in the CNS" (RT-qPCR)
- Axis PRINTED: y "Expression Normalized to Actin * 1000", broken axis: lower segment ticks 0-50 (0, 10, ..., 50), upper segment ticks 200, 400, 600, 800, 1000 (upper segment visibly extends below 200 to about 50). x: Brain Area 1, Brain Area 2, Brain Area 3, Cervical SC, Thoracic SC, Lumbar SC. Seven promoters in legend: CAG (yellow), EFS (grey), p546 (red), gfa1405 (dark green), CNP (orange), MAG (brown), rMBP (purple). Individual dots per animal; error bars (type UNSTATED); n PRINTED in legend: "N = 4-5 animals per promoter". Replicate unit: animal (legend), UNSTATED per plate.
- EYE bar tops (ticks 200/400/600 upper; 10-50 lower): BA1 CAG about 270, EFS about 42, p546 about 40, gfa1405 about 125, CNP about 105; BA2 CAG about 165, EFS about 35, p546 about 19, gfa1405 about 115, CNP about 168; BA3 CAG about 398, EFS about 4.5, p546 about 42, gfa1405 about 191, CNP about 606 (dots to about 910, error cap about 960). MAG and rMBP bars about 0-5 in all brain areas. Cervical SC: CAG about 12, p546 near 0, gfa1405 above 50 (bar through the break; dots about 34 and about 90+), CNP about 18, MAG about 5. Thoracic SC: gfa1405 about 35, CNP about 5, CAG about 2. Lumbar SC: CAG about 10, gfa1405 above 50 (dots about 32, 41, about 100), CNP about 8.
- PRINTED stats marks: none on this panel.
### 2B right: "EGFP Expression in Peripherial Tissues" (RT-qPCR, spelling as printed)
- Axis PRINTED: y "Expression Normalized to Actin * 1000", broken axis: lower ticks 0, 2, 4, 6, 8, 10; upper ticks 100, 200, 300, 400 (upper segment extends below 100 to about 13 by pixel geometry). x: Sciatic Nerve, Liver, Heart, Quad. Same seven promoters and colours. Dots per animal, error bars UNSTATED, n "4-5 animals per promoter" (legend).
- EYE, Liver: gfa1405 bar top about 107 (upper segment, 100 tick), dots about 160, 112, 94, 88, error cap about 139; CAG bar top about 8.4 (lower segment) with error cap to about 10 and dots about 2 and 0 plus two dots in the break region above the 10 tick (about 15-20 by upper-segment extrapolation, no tick); CNP bar extends through the break (above 10), dots about 8.7 and several near/above 10 (one about 50); p546 bar about 4.4, dots about 6.2, 5.7, 5, 3.9, 1.3; EFS about 0.8; MAG about 3.1 (dots 0.8-5.4); rMBP about 0.4.
- EYE, Heart: CAG bar top about 147 (upper segment), dots about 286, 140, 86, 73; p546 about 1.4 (dots to 3.3); gfa1405 about 1.7 (dots 0.1-4.2); CNP about 4.2 (dots 1.8-6.5); EFS, MAG, rMBP about 0.
- EYE, Sciatic nerve: CAG bar through the break (dots about 56, 6.7, 0, 0); CNP about 0.9 (dot to 2); others about 0.
- EYE, Quad: CAG bar top about 70 (upper segment; dots about 103, 75, 65, 40); all other promoters about 0.
- PRINTED stats marks: none.
- TEXT-ONLY: Results refer to "Figure 2C" for heart expression of MAG and rMBP; there is no panel C in the figure as supplied.

## 6. Figure 3 (full-res, 2244x1679), whole-organ fluorescence
- What: gross images, 8 groups per row labelled CAG, tCAG, p546, GFAP, gfa1405, gfaABC(1)D, CNP, CONTROL. A whole brain (dorsal); B spinal cord (CAG, tCAG, p546, CNP in top row; GFAP, gfa1405, gfaABC(1)D, CONTROL in bottom row); C heart; D liver; E skeletal muscle (quadriceps) (PRINTED legend: A whole brain, B spinal cord, C heart, D liver, E skeletal muscle; 4 weeks post-injection). MAG, rMBP, EFS not shown (TEXT-ONLY: excluded from imaging because of low mRNA).
- n: not printed on the figure or legend. Methods (TEXT-ONLY): 3 mice per construct for whole-organ imaging; the image shown per group is a single organ (UNSTATED which animal). No error bars, no scale bar, no numbers, no statistics. Panel images are composites with separate black backgrounds per tile.
- EYE description (qualitative only): A: strong green in CAG, p546 (stronger posterior cortex), CNP; moderate in GFAP and gfa1405; weak in gfaABC(1)D and tCAG; CONTROL grey-white. B: green visible in CAG, CNP, gfa1405, GFAP (weaker), p546 (weak); tCAG, gfaABC(1)D, CONTROL grey. C heart: CAG bright green, patchy; others dim green; CNP with a ragged edge; CONTROL dim. D liver: all eight livers show a dim green tint, including CONTROL; p546 and CAG look slightly greener than the rest; no panel is bright. E muscle: CAG and CNP bright green; others dim. Legend/text caution (TEXT-ONLY): whole-organ imaging "used solely as a qualitative readout".

## 7. Figure 4 (full-res)
- Legend PRINTED: (A) regions CTX, HIP, STR, TH, HY, MB, CB, P, MY, FT, CC (spl, g), V, OA; scale bar 1 mm. (B) sagittal sections with high-magnification images, 1 mm and 50 um scale bars. (C) boxplots "percent (%) of EGFP-positive area in the brain area" and "EGFP intensity in the brain (mean EGFP intensity in the brain area minus median EGFP intensity of the EGFP-negative brain area) in RFUs. Statistical comparisons to CAG are shown; comparisons between all other possible promoter pairs are shown in Table S1. n = 8-10; **** p<=0.0001, *** p<=0.001, ** p<=0.01, * p<=0.05."
- 4A: sagittal atlas-style diagram plus examples of glial and neuronal morphology (DAPI/EGFP) and a p546 sagittal section with high-magnification inset. 4B: sagittal sections plus insets for CAG, tCAG, EFS, CNP, GFAP, gfa1405, gfaABC(1)D, MAG (and p546 in A); no image shown for rMBP or Control (images only).
### 4C left: "EGFP distribution in the brain (%)"
- Axis PRINTED: y ticks 0, 10, 20, 30, 40, 50. x: CAG, tCAG, EFS, p546, GFAP, gfa1405, gfaABC(1)D, CNP, MAG, rMBP, Control. Boxplot with individual dots, line in box (median), whiskers (min-max reach the extreme dots); per-animal dots, 7-10 visible per group; n per group not printed beyond legend "n = 8-10". Replicate unit: UNSTATED on the figure (dots are presumably animals; text-only Methods: 10 animals per group; section/field averaging not stated).
- EYE (ticks 0-50): CAG box about 21.5 to 42.2, median about 38.7, whiskers about 19.5 to 42.3; tCAG about 0-3 (median about 1); EFS box about 5-8 (median about 6), max about 16.4; p546 box about 10.3 to 33.3, median about 23.2, whiskers about 7.9 to 41.9; GFAP box about 11 to 18.5, median about 17.2, whiskers about 8.3 to 24; gfa1405 box about 22.7 to 29.2, median about 26.5, whiskers about 18.8 to 35.3; gfaABC(1)D box about 4.5-6.3 (median about 5.2), whiskers about 3.5 to 9.5; CNP box about 15.2 to 30.1, whiskers about 13 to 37.2; MAG about 4.3-5.4 (median about 5); rMBP box about 0.8-3.8 (median about 1.6, max about 4.3); Control about 0.3.
- PRINTED marks (all from CAG): tCAG ****, EFS ****, p546 **, GFAP ****, gfaABC(1)D ****, CNP **, MAG ****, rMBP ****. No bracket is printed for gfa1405 or Control. Table S1 PRINTED (distribution, adjusted P): CAG vs gfa1405 0.321 ns; CAG vs p546 0.0097 **; CAG vs CNP 0.0035 **; CAG vs GFAP <0.0001 ****; CAG vs Control <0.0001 ****; gfa1405 vs p546 0.919 ns; gfa1405 vs CNP 0.8033 ns; gfa1405 vs GFAP 0.01 **; p546 vs CNP >0.9999 ns.
### 4C right: "EGFP intesity in the brain (RFU)" (spelling as printed)
- Axis PRINTED: y ticks 0, 400, 800, 1200. Same groups and box/dot style, same n legend ("n = 8-10").
- EYE (ticks 0, 400, 800, 1200; about 0.36 px per RFU, so +/-20): CAG box about 189 to 661, median about 572, whiskers about 133 to 911; p546 box about 53 to 286, median about 128, whiskers about 39 to 447; GFAP box about 239 to 547, median about 408, whiskers about 39 to 792; gfa1405 box about 303 to 511, median about 461, whiskers about 206 to 694; gfaABC(1)D box about 78-128, whisker max about 219; CNP box about 20-97, whisker max about 122; tCAG, EFS, MAG, rMBP, Control all below about 60 (MAG about 5).
- PRINTED marks (from CAG): tCAG ****, EFS ****, p546 ****, gfaABC(1)D ****, CNP ****, MAG ****, rMBP ****. No bracket for GFAP, gfa1405 or Control. Table S1 PRINTED (intensity): CAG vs GFAP 0.9237 ns; CAG vs gfa1405 0.9924 ns; CAG vs p546 <0.0001 ****; CAG vs CNP <0.0001 ****; CAG vs Control <0.0001 ****; gfa1405 vs p546 0.0009 ***; GFAP vs p546 0.0042 **; gfa1405 vs CNP <0.0001 ****.
- No mean value is printed on the figure; the boxplots show medians (line) not means. TEXT-ONLY numbers in Results: CAG up to 42% area and 474.8 RFU; tCAG 5.8% and 8.443; EFS 5%-9% (up to 16%) and 2.678; p546 41% and 154.0; gfa1405 35% and 412.1; GFAP about 24% and 387.7; gfaABC(1)D 9% and 91.54; CNP 37% and 45.51; MAG 5.5% and 9.548; rMBP 2%-4% and 3.258.
- Table S1 full text read from mmc1.pdf (all 55 pairwise adjusted P values, both columns); sample size "n=8-10 per group" PRINTED.

## 8. Figure 5 (full-res)
- Legend PRINTED (abridged): (A) confocal hippocampus, EGFP green, NeuN red, GFAP purple, DAPI blue; (B) "Percentage of EGFP-positive cells that colocalize with the astrocyte marker S100B (left, %) and the neuronal marker NeuN (right, %) ... for each promoter (n = 3)... One-way ANOVA ... only significant results are shown"; (C) CNP and MAG, Olig2 red, NeuN purple; (D) "Olig2 (left, %) and NeuN (right, %) for the MAG (n = 5) and CNP (n = 9) promoters". Stars: * p<=0.05, ** <=0.01, *** <=0.001, **** <=0.0001.
- 5A images: CAG, GFAP, gfa1405, gfaABC(1)D, p546 (scale bars not numerically labelled in the image; yellow bars). 5C images: CNP, MAG.
### 5B left: "EGFP/S100B colocalization (%)"
- Axis ticks 0, 20, 40, 60, 80; groups CAG, p546, GFAP, gfaABC(1)D, gfa1405; bars with dots, error bars (type UNSTATED), n = 3 dots per group PRINTED/visible. Replicate unit UNSTATED in the legend (Methods text-only: three replicates per group from 13 fields in 5 regions).
- EYE bar tops (ticks 0-80): CAG about 25 (dots about 36.7, 22.8, 15); p546 about 1.8 (dots about 1-2); GFAP about 34 (dots about 44, 30, 28); gfaABC(1)D about 47 (dots about 59, 57, 25; error cap about 66, lower about 28); gfa1405 about 35 (dots about 38, 38, 30).
- PRINTED marks: p546 to GFAP *; p546 to gfaABC(1)D **; p546 to gfa1405 *.
### 5B right: "EGFP/NeuN colocalization (%)"
- Ticks 0, 20, 40, 60, 80; same groups, n = 3 dots.
- EYE: CAG about 23 (dots about 27, 24, 18); p546 about 58 (dots about 72, 51, 50); GFAP about 12; gfaABC(1)D about 17; gfa1405 about 9 (these last three from the whole figure, dots 3 each).
- PRINTED marks: CAG to p546 ***; p546 to GFAP ****; p546 to gfaABC(1)D ****; p546 to gfa1405 ****.
### 5D left: "EGFP/Olig2 colocalization (%)"
- Ticks 0, 20, 40, 60, 80; CNP vs MAG. EYE: CNP bar about 14, 5 dots (about 16, 16, 15, 13, 10; error caps about 17 and 11); MAG bar about 43, 9 dots (about 65, 57, 49, 48, 44, 34, 34, 29, 25; caps about 56 and 29). PRINTED mark: CNP to MAG ***.
### 5D right: "EGFP/NeuN colocalization (%)"
- Ticks 0, 10, 20, 30, 40. EYE: CNP bar about 19.7, 5 dots (about 29.8, 21.2, 19.5, 14.3, 14.1; caps about 26 and 13.4); MAG bar about 9.5, 9 dots (about 13.5, 13, 10.2, 9.2, 8.1, 7.3, 6.3, 4.9, etc.; caps about 12.8 and 6.8). PRINTED mark: CNP to MAG **.
- Note (extraction only): legend says "MAG (n = 5) and CNP (n = 9)"; the plotted dots are 5 for CNP and 9 for MAG; Results text (TEXT-ONLY) says "MAG ... (n = 9)" and "CNP ... (n = 5)". Error-bar type UNSTATED. Replicate unit UNSTATED on the panel.
- TEXT-ONLY numbers in Results (colocalization): S100B CAG 36%, p546 1.9%, GFAP 44%, gfaABC(1)D 58%, gfa1405 37.7%; NeuN CAG 27%, p546 72%, GFAP 13%, gfaABC(1)D 19%, gfa1405 11.9%; CNP up to 16% oligodendrocytes and 21%-29% neurons; MAG up to 65% and 13.5%.

## 9. Supplementary figures S2-S4
- S2 (2250 px): confocal hippocampus, rows Merge, EGFP, NeuN, GFAP, DAPI; columns GFAP, gfaABC(1)D, gfa1405, CAG, p546. Yellow scale bars, size not printed in the image or legend. No numbers.
- S3 (2250 px): rows MAG, CNP; columns Merge, EGFP, Olig2, NeuN, DAPI. No numbers.
- S4 (1280x492): legend PRINTED: "(A) distribution percentage (%) and EGFP intensity ... for animals 4 weeks and 8 weeks post injection ... (n=7-10); (B) colocalization percentages with S100B and NeuN ... (n=3). ** p<=0.01, *** p<=0.001, **** p<=0.0001". Bars with dots, error bars type UNSTATED.
  - A left, distribution (ticks 0-50): EYE bars p546 4 wk about 22, gfa1405 4 wk about 26, p546 8 wk about 31, gfa1405 8 wk about 24. All four brackets PRINTED "ns".
  - A right, intensity (ticks 0, 200, ..., 1000): EYE bars p546 4 wk about 164, gfa1405 4 wk about 424, p546 8 wk about 248, gfa1405 8 wk about 382. PRINTED marks: p546 4 wk to gfa1405 4 wk **; p546 8 wk to gfa1405 8 wk ns; p546 4 wk to 8 wk ns; gfa1405 4 wk to 8 wk ns.
  - B left, S100B (ticks 0-50): EYE bars p546 4 wk about 1.8, gfa1405 4 wk about 35, p546 8 wk about 3, gfa1405 8 wk about 42; PRINTED p546 to gfa1405 at 4 wk ****, at 8 wk ****, 4 wk to 8 wk comparisons ns.
  - B right, NeuN (ticks 0-80): EYE bars p546 4 wk about 58, gfa1405 4 wk about 9, p546 8 wk about 43, gfa1405 8 wk about 6; PRINTED p546 to gfa1405 at 4 wk ***, at 8 wk **, 4 wk to 8 wk ns.
- The S4 4-week bars/dots and Fig 4C/5B 4-week p546 and gfa1405 values look like the same dataset redrawn (bar vs box); this is an observation of redrawing only, not a comparison of claims.

## 10. Graphical abstract (fx1.jpg)
Schematic: AAV9 eGFP, neonatal injection, cell types and promoters (astrocytes: GFAP, gfaABC1D, gfa1405; oligodendrocytes: CNP, MAG, rMBP; neurons: p546; ubiquitous: CAG, tCAG, EFS). No data.

## 11. Table 1 (XML table, PRINTED text)
Promoter, size (bp), cell type: GFAP 2,208 astrocytes; gfa1405 1,405 astrocytes; gfaABC(1)D 681 astrocytes; p546 546 primarily neurons, also glial cells; CAG 1,700 ubiquitous; tCAG 581 ubiquitous; EFS 240 ubiquitous; CNP 1,644 oligodendrocytes, Schwann cells; MAG 1,451 oligodendrocytes, Schwann cells; rMBP 1,613 oligodendrocytes, Schwann cells.

## 12. What I did not do or could not read
- No higher-resolution copy of Fig S1 than 726x720 px was reached; S1 values are EYE +/-3 units and lane-level band reading is qualitative only. Overlapping dots in low bars (p546, CNP, CAG liver; p546 BA1) were not separable, so a per-dot count of 4 is not verified there.
- Broken-axis upper segments (Fig 2B) have no tick below 100 (peripheral) or 200 (CNS); values read there in the transition zone are extrapolated and marked as such.
- No densitometry, no deconvolution of overlapping points, no comparison with text claims, no conclusions.
- Source data: not available (statement "available upon request"). Figure 2C (mentioned in the Results text) is not in the figure.
- Fig 4A/B, 5A/C, S2, S3 images were examined as whole figures only, no per-cell counting.
