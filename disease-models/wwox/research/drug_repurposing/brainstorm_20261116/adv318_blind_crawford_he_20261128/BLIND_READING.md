# ADV-318: blind second reading of Crawford et al. 2010 (PMID 20858739, doi 10.1093/brain/awq237), HE, 2026-11-28

Nothing here is medical advice. A reading for the consumer of ADV-317, not a claim.

## Blindness and sources
- Opened: the assignment message; from the receipt ledger only the source path and DOI fields of this PMID;
  `files/fulltext/PMID20858739_Crawford2010_PMC_efetch_20261128.xml` (sha256 `ba8a080dc5b37224a8d7eb55d288a9ca3d96f92052fa8b2eb4e13839ce524184`);
  `files/figures/PMID20858739/` figures 5, 8, 9, 10 and `supp_figures.pdf` (3 pages).
- Not opened: SCI's frozen note, the ADV-317 folder, any SCI result, any receipt content.
- One exposure to declare: a commit title on main seen at session start names ADV-317 a "recruitment test". No content.
- Read in the XML: methods (animals-per-group, quantification, electrophysiology, statistics), results on myelin, axon damage,
  conduction, refractoriness, tracts (in part); legends of figures 4 to 10. The XML carries no page numbers. Figures 1 to 4, 6, 7 not
  viewed as images and the legends of figures 1 to 3 not read.
- No delegate. Figures are the 800 px JPEGs.

## What is printed

| Item | Normal | Vehicle EAE | ER-beta ligand EAE |
|---|---|---|---|
| CAP N1 input-output curve (Fig. 8C) | printed (one series, day not stated) | printed, Day 20 and Day 36 | printed, Day 20 and Day 36 |
| CAP N2 input-output curve (Fig. 8D) | printed (as above) | printed, Day 20 and Day 36 | printed, Day 20 and Day 36 |
| C2/C1 vs interpulse interval, N1 and N2 (Fig. 9B) | printed, 1.5 to 8 ms | printed | printed |
| 50 % interpulse interval table (Fig. 9B) | printed | printed | printed |
| g ratio (text, Fig. 5C) | printed | printed | printed |
| Corpus callosum axon count or density | NOT PRINTED | NOT PRINTED | NOT PRINTED |
| Spinal anterior funiculus NF200+ axons (Suppl. Fig. 2B) | plotted | plotted | plotted |
| Numeric table of the CAP amplitudes or C2/C1 points | NOT PRINTED | NOT PRINTED | NOT PRINTED |
| Stimulus intensity of the paired pulses (C1, C2) | NOT PRINTED ("a defined strength") | NOT PRINTED | NOT PRINTED |

## Fig. 8C and 8D: CAP amplitude (mV, y axis "CAP response, mV") against stimulus strength (mA)
Read from plotted points: colour-band detection of marker centres in pixel columns, checked on 3x crops; axis ticks calibrated per panel.
One pixel is about 0.004 mV; take ±0.02 mV, ±0.04 where marked `*` (markers overlap or hidden under another series).
Vehicle Day 20 and Day 36 overlap: one value for both. Points at 0 to 0.7 mA are 0.12 mV or less and are not listed.
n = 4 mice per group, 3 sections per mouse, 12 sections (legend). Pulses 200 us at 0.2 Hz, 0.3 to 4.0 mA (methods).
Error-bar type is not named in the legend; the statistics section says mean ± SEM, n = animals.

| mA | N1 normal | N1 vehicle | N1 ligand D20 | N1 ligand D36 | N2 normal | N2 vehicle | N2 ligand D20 | N2 ligand D36 |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.31 | 0.16* | 0.17* | 0.23* | 0.09* | 0.07* | 0.08* | 0.08* |
| 1.3 | 0.41 | 0.22 | 0.26 | 0.36 | 0.17 | 0.09 | 0.13* | 0.13* |
| 1.5 | 0.48 | 0.28 | 0.35 | 0.46* | 0.23 | 0.13 | 0.18* | 0.18* |
| 1.7 | 0.58 | 0.32 | 0.40 | 0.50 | 0.29 | 0.16 | 0.22* | 0.22* |
| 2.0 | 0.65 | 0.38 | 0.47 | 0.61 | 0.39 | 0.22 | 0.28* | 0.28* |
| 2.3 | 0.75 | 0.42 | 0.54 | 0.69 | 0.49 | 0.24 | 0.33* | 0.34* |
| 2.5 | 0.83 | 0.46 | 0.59 | 0.74 | 0.54 | 0.27 | 0.35 | 0.39 |
| 2.7 | 0.88 | 0.49 | 0.63 | 0.78 | 0.58 | 0.29 | 0.38 | 0.44 |
| 3.0 | 0.97 | 0.51 | 0.68 | 0.81 | 0.67 | 0.30 | 0.42 | 0.49 |
| 3.3 | 1.03 | 0.54 | 0.72 | 0.84 | 0.71 | 0.32 | 0.43 | 0.52 |
| 3.5 | 1.04 | 0.56 | 0.74 | 0.85 | 0.75 | 0.33 | 0.44 | 0.54 |
| 3.7 | 1.06 | 0.55 | 0.76 | 0.85 | 0.80 | 0.33 | 0.45 | 0.56 |
| 4.0 | 1.07 | 0.56 | 0.79 | 0.90 | 0.83 | 0.35 | 0.45 | 0.60 |

## Fig. 9B: C2/C1 (%, y axis) against interpulse interval (ms)
Same reading method; about 0.5 % per pixel; take ±2 points, ±4 where marked `*`; `NR` = marker not separable, no value.
n = 4 (legend, mice). The day is not stated for panel B (the legend says "later time point" for panel A).
At 6.5 to 8 ms the three N1 groups overlap: one cluster, about 85 to 91.

| ms | N1 normal | N1 vehicle | N1 ligand | N2 normal | N2 vehicle | N2 ligand |
|---|---|---|---|---|---|---|
| 2.0 | 43 | 13 | 21 | 25 | 11 | 19 |
| 2.5 | 56 | 16 | 31 | 34 | 20 | 27 |
| 3.0 | 61 | 28 | 45 | 39* | 28 | 39* |
| 3.5 | 71 | 41 | 56 | 45* | 39* | 46* |
| 4.0 | 77 | 49 | 66 | 50* | 49 | 54* |
| 4.5 | 76* | 61 | 73 | 50 | 57* | 61* |
| 5.0 | 82* | 67 | 79* | 55 | 63* | 62* |
| 5.5 | 85* | 77 | 84* | 59 | 69* | 71* |
| 6.0 | NR | 81 | 87* | 63 | 72* | 72* |
| 6.5 | 88* | 88* | 88* | 67 | 74* | 74* |
| 7.0 | 89* | 89* | 89* | 69 | 75* | 74* |
| 7.5 | 89* | 90* | 88* | 71 | 78 | 75* |
| 8.0 | 90* | 91* | 90* | 73 | 79* | 78* |

50 % interpulse interval (table under Fig. 9B, ms; legend says mean ± SD): N1 normal 2.2 ± 0.21, vehicle 3.9 ± 0.15,
ligand 3.0 ± 0.11; N2 normal 3.1 ± 0.12, vehicle 3.5 ± 0.20, ligand 3.1 ± 0.22.
**Source disagrees with itself:** the results text gives the same N2 means with other spreads (± 0.10, ± 0.05, ± 0.16).
The plotted N2 C2/C1 plateaus near 73 to 79 %, N1 near 90 %.

## Single-point amplitudes and their stimulus intensity
- Fig. 8B: example traces, evoked at **4 mA**, Day 36; scale bar 0.5 mV, 2 ms. No numeric amplitude; not measured here.
- Results text: N1 and N2 "~50 % of normal" at Day 20, no stimulus intensity given. At 4 mA the plotted vehicle/normal
  ratios are about 0.52 (N1) and 0.42 (N2).
- Fig. 8 legend: significance against normal "at 2-4 mA stimulus strength".

## g ratio, myelin thickness, axon counts
| Measure (corpus callosum, electron microscopy, Day 36) | Normal | Vehicle EAE | Ligand EAE |
|---|---|---|---|
| g ratio (text; Fig. 5C ii) | 0.87 ± 0.004 | 0.94 ± 0.026 | 0.85 ± 0.012 |
| Myelin thickness, um (text; Fig. 5C i) | 0.060 ± 0.002 | 0.027 ± 0.001 | 0.065 ± 0.002 |

- n and unit, three statements that do not agree: Fig. 5 legend "at least four mice ... minimum of 500 fibres from each mouse";
  statistics section ">500 axons from 8 to 10 random caudal area fields per animal"; quantification section "at least 500
  axons ... in each treatment group". The methods also say 3 animals per group were perfused for electron microscopy.
- Fraction of unmyelinated axons: no number printed (the text says "increased numbers"; the scatter plots show points at g = 1.0).
- Scatter plots of g ratio and myelin thickness against axon diameter (Fig. 5C iii, iv): printed, not digitised.

Corpus callosum tract measure (Fig. 10D, "dextran red intensity", bar tops, about ±0.03; an intensity, not an axon count;
n = 4): normal 0.89, vehicle 0.43, ligand 0.71. The results text's "nearly 80 % of callosal axons ... were labelled" refers
to Fig. 10C and D. **Source disagrees with itself:** the Fig. 10 legend says the ligand group is not significantly different
from normal, while the panel carries `*` over the ligand bar (and `**` over vehicle).
Caspr pairs (Fig. 7B) are node counts, not axon counts; not read.

Suppl. Fig. 2B, "NF200+ axons in AF" (spinal cord, not callosum; read from bar tops, about ±10; unit and field area not
printed; n = 4 in the legend): intact mice normal 363, vehicle 234, ligand 347; ovariectomised normal 389, vehicle 228, ligand 343.

## Limits
One reader. Digitised values are estimates from a small raster; no vector figure was available in what was opened.
