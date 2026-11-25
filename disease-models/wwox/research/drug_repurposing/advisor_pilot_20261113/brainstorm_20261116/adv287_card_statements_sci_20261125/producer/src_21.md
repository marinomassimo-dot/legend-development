# src_21 — P11 DR-P11-004 measured_result_note (replacement for n=7; route1 reserve, draw_order 15): "the DQ/SQ p of 0.09 (only the 'Normal' row is printed, 4 against 0) is not reproduced and depends on the assumed group sizes (0.055 uncorrected chi-square and 0.114 Fisher for 26 and 22; 0.030 to 0.075 and 0.096 to 0.128 for the other sizes tried);"

Card: P11_magnesium_nmdar_gate, /drug_assertions/DR-P11-004/measured_result_note. Source: Yadav 2022, Iran J Child Neurol, PMID 35222658, PMC8752995 (open-label randomised trial of intramuscular then oral magnesium in West syndrome, children 3 months to 5 years; human; not WWOX). Held: files/fulltext/PMID35222658_ADV272_PMC8752995_epmc_20261125.xml (58,575 bytes). Reading depth: full text, all four tables read in full from the XML; all p values recomputed here with Python (own implementations of the uncorrected chi-square, Yates and two-sided Fisher exact tests; scipy is not installed). Not an Obeid source.

## Pre-source arithmetic (done before opening the XML)
Printed in the sentence: 4 against 0, p 0.09 (paper), 0.055 and 0.114 for group sizes 26 and 22; ranges 0.030 to 0.075 (chi-square) and 0.096 to 0.128 (Fisher) for "other sizes". The sentence prints no group sizes for the ranges, so the ranges cannot be recomputed from the sentence alone; the 26/22 pair can.

## Whole source tables (Table 1 to 4 of the paper, as printed in the XML; counts intervention / non-intervention)
Table 1 (baseline; header: Intervention n=26, Non-intervention n=22): >60 DQ row 3/3; Sex M/F 21,5 / 15,7 p 0.32; socio-economic middle/lower 19,7 / 14,8 p 0.48; nutrition normal/moderate/severe 8,6,12 / 11,3,8 p 0.38; serum Mg normal/low 18,8 / 13,9 p 0.46; serum Mg mean 2.10 +/- 0.52 vs 2.04 +/- 0.55 mg/dl p 0.71; spasms/day <5, 5-10, >10: 11,10,5 / 5,10,7 p 0.32; spasms per episode single/series 3,23 / 7,17 p 0.09; other seizures present/absent 11,15 / 12,10 p 0.31; baseline DQ <30, 30-60: 8,15 / 7,12 p 0.97 (with the >60 row 3 / 3 the DQ rows total 26 and 22).
Table 2 (outcomes after 3 months; headers n=26 and n=22): first row "Abnormal 22 / 22" (unlabelled in the XML); Clinical response No/Partial/Complete 6,7,13 / 7,4,11 p 0.69; "Final EEG in initial abnormal EEG (n=26)" Normal/Abnormal 11,2 / 6,7 p 0.04 (counts total 13 in each group); DQ/SQ Normal 4 / 0 p 0.09 (this is the only DQ/SQ row printed; the table footer carries only the abbreviation line "DQ- development quotient; SQ- social quotient").
Table 3 (clinical response by initial serum Mg): intervention Low 4,2,3 (total 9) and Normal 2,3,13 (18) p 0.003; non-intervention Low 4,4,0 (8) and Normal 3,2,8 (13) p 0.42.
Table 4: totals 13 / 11 / 24; Normal 5,5,21 p 0.004; Low 8,6,3.
Text: Results "neuro-developmental outcome (p=0.09)"; Discussion "(P=0.094)" and "Although the difference in the DQ/SQ level was nearly significant (p= 0.09)". The Methods say DQ/SQ assessment was repeated at 3 months with the developmental screening test or the Vineland social maturity scale. The text names no test statistic and no group size for the DQ/SQ comparison.

## Recomputation: DQ/SQ "Normal" 4 of n1 against 0 of n2 (2x2 [[4, n1-4],[0, n2]])
| n1 (intervention) / n2 (non-intervention) | where the size comes from | uncorrected chi-square p | Yates p | Fisher exact p (two-sided) |
|---|---|---|---|---|
| 26 / 22 | Table 1 and 2 headers | 0.055 | 0.162 | 0.114 |
| 22 / 22 | the unlabelled "Abnormal 22 / 22" row of Table 2 | 0.036 | 0.116 | 0.108 |
| 13 / 13 | EEG row counts | 0.030 | 0.103 | 0.096 |
| 24 / 24 | Table 4 total (24) for each | 0.037 | 0.117 | 0.109 |
| 26 / 26 | | 0.037 | 0.118 | 0.110 |
| 13 / 11 | Table 4 totals by arm (13, 11) | 0.044 | 0.143 | 0.098 |
| 24 / 22 | | 0.045 | 0.139 | 0.110 |
| 12 / 12 | no source in the paper | 0.028 | 0.100 | 0.093 |
Sizes giving the sentence's upper bounds (0.075 chi-square, 0.128 Fisher): about 15/10, 19/13, 24/17 or 25/18; none is a size read from the paper. The sentence does not say which sizes it tried, so its stated ranges (0.030 to 0.075 and 0.096 to 0.128) cannot be verified size by size; the lower ends (0.030 and 0.096) are exactly 13/13, and every paper-derived size above lies inside both ranges. Group sizes 26/22 give the printed 0.055 and 0.114 exactly. No paper-derived size gives 0.09 by chi-square (0.028 to 0.055) or Yates (0.100 to 0.162); a Fisher p of 0.093 occurs only at 12/12, a size with no support in the text. Side finding: Table 1's spasms-per-episode p of 0.09 (3,23 vs 7,17) recomputes as uncorrected chi-square 0.085, Yates 0.172, Fisher 0.152, so the same printed 0.09 appears twice in the paper.

## Check of the other claims in the sentence
"Only the 'Normal' row is printed, 4 against 0": true (Table 2 DQ/SQ has one row). "Depends on the assumed group sizes": true (0.028 to 0.168 chi-square across the sizes tried above). The sentence's own arithmetic against its printed numbers: no inconsistency.
