# Cell-by-cell comparison, ADV-317 (SCI delegate) against ADV-318 (HE blind reading), Crawford 2010 (PMID 20858739), SCI bc, 2026-11-28

Hypothesis level; not medical advice. Compared: the SCI delegate's tables (`../crawford2010_recruitment_adv317_sci_20261128/BLIND_FIGURES_CRAWFORD2010_ADV317_DELEGATE.md`, eye reads) against HE's `BLIND_READING.md` (colour-band marker detection, sha of the source XML `ba8a080d...4184`). Script: `compare_adv317_adv318.py` (reads both files; prints every cell). Matching by figure, panel, group, series and x value; unit beside each value. Both readers worked from the same 800 px JPEGs and the same JATS text, independently (HE declares one exposure: a commit title naming ADV-317).

## Values
| Figure, panel | Cells matched | Largest difference | Cells beyond reader tolerance |
|---|---|---|---|
| Fig 8C, 8D (CAP amplitude, mV; N1 and N2; groups Normal, vehicle D20, vehicle D36, ligand D20, ligand D36; at 1, 2, 3, 4 mA) | 40 | 0.03 mV | 0 |
| Fig 9B (C2/C1, percent; N1 and N2; Normal, vehicle, ligand; 41 matched x-values from 2 to 8 ms) | 41 | 2 percentage points | 0 (HE marks one N1 Normal point at 6 ms not separable, `NR`; SCI delegate read about 88) |
| Fig 9 printed table (50 percent interval, ms, mean ± SD, n = 4 mice) | 6 | 0 | 0 |
| Fig 5C text values (myelin thickness um; g-ratio) | 6 | 0 (HE and the text give ± SEM; the SCI delegate also quotes the text; bar-top eye values 0.060, 0.027, 0.065 and 0.865, 0.947, 0.854 agree within rounding of the text 0.87, 0.94, 0.85) | 0 |

The only systematic difference: HE gives ONE value for vehicle D20 and D36 in Fig 8 (markers overlap); the SCI delegate separated them (N1 at 4 mA 0.59 and 0.55 against HE 0.56; N2 0.35 and 0.33 against 0.35). Within the stated tolerance (HE about 0.02 to 0.04 mV).

## Cells and statements that differ (report to ADV)
| # | Item | SCI side (before the comparison) | HE side | Resolution |
|---|---|---|---|---|
| 1 | Low-stimulus overlap, Fig 8C | RESULT: curves "coincide from 0 to about 0.7 to 1 mA" | HE lists points at 0 to 0.7 mA as 0.12 mV or less (not tabulated) and at 1.0 mA N1 normal 0.31 against vehicle 0.16 (SCI delegate 0.31 against 0.17) | SCI wording WRONG beyond 0.7 mA; corrected in the RESULT |
| 2 | Does the normal curve plateau, Fig 8C | RESULT limit: normal curves still rising at 4 mA, no plateau demonstrated | N1 normal 1.03, 1.04, 1.06, 1.07 at 3.3 to 4.0 mA (near plateau); N2 normal 0.71, 0.75, 0.80, 0.83 (still rising) | Limit true for N2 only; corrected |
| 3 | Error-bar type, Fig 8 | "UNSTATED" | legend unstated; the statistics section says mean ± SEM, n = animals | Both true; labelled by place |
| 4 | EM n and unit | three statements (legend four mice; Methods three animals for EM; more than 500 axons per mouse or per group) | the same disagreement stated with the three sentences verbatim (legend: at least four mice, at least 500 fibres per mouse; statistics: more than 500 axons from 8 to 10 fields per animal; quantification: at least 500 axons per treatment group) | no conflict; HE wording more exact |
| 5 | Items only HE has | not in the SCI delegate's report (it did not open Fig 10): Fig 10D dextran-red intensity bars 0.89, 0.43, 0.71 (n = 4, eye ±0.03) with a legend/panel disagreement on the ligand group; Suppl. Fig 2B NF200+ axons (spinal, not callosum) 363, 234, 347 and 389, 228, 343 | | Not used by ADV-317; available if a consumer needs them (single reader, eye) |
| 6 | Source disagreement on N2 SDs (text 0.10, 0.05, 0.16 against table 0.12, 0.20, 0.22) | found | found | agree |

## Exploratory, computed after the comparison from HE's Fig 8C and 8D table (not part of the frozen rule)
Vehicle divided by normal at each stimulus. N1: 0.52, 0.54, 0.58, 0.55, 0.58, 0.56, 0.55, 0.56, 0.53, 0.52, 0.54, 0.52, 0.52 (1.0 to 4.0 mA): flat, between 0.52 and 0.58. N2: 0.78 (1.0 mA, markers overlap), 0.53, 0.57, 0.55, 0.56, 0.49, 0.50, 0.50, 0.45, 0.45, 0.44, 0.41, 0.42: falls with stimulus. Reading (hypothesis): the vehicle N1 input-output curve is about half the normal curve at every stimulus from 1 mA, with no threshold shift readable at this resolution (a gain-type change in the responding population); N2 falls further at high stimulus. This does not change the frozen outcome for N1 ("both change": the N1 50 percent interval still moves 2.2 to 3.9 ms).
