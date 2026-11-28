# ADV-320 delegate table against HE's blind ADV-323 table, Chornyy et al. 2025 (PMID 41036104), cell by cell (SCI bd, 2026-11-28)

Hypothesis level; reference genotype class only; not medical advice. Inputs: `BLIND_FIGURES_CHORNYY2025_ADV320_DELEGATE.md` (D; sections 3 and 7; NOT blind to the frozen note) and `../adv323_blind_chornyy_he_20261128/BLIND_READING.md` (H; blind, sections 1 and 3; one reader plus one HE spot check). Script `compare_adv320_adv323.py` (run `python3 -P -E`; values typed from the two files; ranges in H count as agreement when D lies inside). **No counterexample threshold was frozen for ADV-320**, so this comparison tests agreement of readings only, not any pass rule.

## Result: the two readings agree on every cell that bounds CLAIM 047
| Panel (unit, n) | Paired cells | Beyond tolerance | Largest difference |
|---|---|---|---|
| Fig 4C left, percent EGFP-positive area (box plot, n = 8 to 10; Q1, median, Q3, whisker min, whisker max; 11 promoters) | 43 | 1 | EFS median 6 (D) against 5.4 (H): 0.6 points |
| Fig 4C right, intensity RFU (same statistics; 6 promoters where D gave a number) | 26 | 0 | CAG median 572 (D) against 578 (H): 6 RFU (D tolerance 20, H 4) |
| Fig S1B, EGFP/GAPDH x 100 (n = 4 per treatment; bar tops and the 8 individual dots of liver gfa1405 and heart CAG) | 28 | 0 | BA2 p546 bar 4 against 3: 1.0 (tolerance 3 and 1.5) |

Cells that carry the claim, by figure, panel and promoter:
* Fig 4C left, median percent area: CAG 38.7 (D) and 38.7 (H); p546 23.2 and 23.3; gfa1405 26.5 and 26.5. Median ratio p546/CAG 0.599 (D) and 0.602 (H).
* Fig 4C left, whisker maximum (the text's "up to"): CAG 42.3 and 42.2; p546 41.9 and 41.8; gfa1405 35.3 and 35.4. Ratio 0.991 in both; the text 41/42 gives 0.976.
* Fig 4C right, median RFU: CAG 572 and 578; p546 128 and 124; gfa1405 461 and 464. Median ratio p546/CAG 0.224 (D) and 0.215 (H); the text numbers 154.0 and 474.8 (called means in the text; the figure prints medians) give 0.324.
* Fig S1B liver: gfa1405 about 81 (D) and 80.4 (H), dots 104, 90, 79, 49 in both; p546, CNP and CAG about 5 to 6 in both; brackets printed: gfa1405 to CAG **** only, in both. Table S1: every pair both readers quote is equal (HE compared all 55 pairs with the PDF text layer: 55 of 55).

## Cells that differ or that only one reader gave
| Cell | D | H | Reading |
|---|---|---|---|
| Fig 4C left, EFS median (percent) | about 6 | about 5.4 | 0.6, above H's edge tolerance 0.3; EFS box sits at 4.7 to 7.9 in H; no effect on the claim |
| Fig 4C left, gfaABC(1)D Q1 | 4.5 | 3.5 to 4.0 (dots overlap) | 0.5 to 1.0 |
| Fig 4C left, MAG Q1 and rMBP Q3 | 4.3; 3.8 | 4.0; 4.0 | 0.2 to 0.3 |
| Fig 4C, medians of CNP (both panels), tCAG, EFS, MAG, rMBP, Control (right) | not given | CNP 16.8 % and 61 RFU; low-end cells as ranges (asterisk = overlapped by the axis) | H is more complete at the low end; D only says "below about 60" |
| Fig S1B error-bar type, post-hoc test, exact P | UNSTATED (error bars); post-hoc not flagged | NOT PRINTED; bars consistent with SD (gfa1405 liver SD of the four dots 23.5, SEM would be 11.7; inference, not a statement); Methods "two-way ANOVA between all groups", post-hoc and exact P NOT PRINTED | H adds the SD inference and the missing post-hoc test; D did not flag the post-hoc test |
| Text against plot, tCAG maximum percent area | text 5.8 listed as text only; plot read 0 to 3 | text 5.8, plot 3.1: flagged as the only mismatch among the text maxima | the plots agree; D did not flag the text contradiction |
| Text means against plot for EFS, rMBP, MAG intensity (2.678, 3.258, 9.548 RFU) | listed text only; "boxplots show medians" | flagged: plotted clusters 8 to 35, up to 28, and 3 to 6 | open: not resolved by either reader |
| Intensity variable wording (Fig 4 legend, Methods, Fig S4: whole brain area against EGFP-positive area) | not recorded | three wordings recorded | open |
| Figure 2C cited in the text, absent from the figure | flagged | flagged | agree |
| Fig 5D n (legend MAG 5, CNP 9; plotted 5 CNP, 9 MAG) | flagged | not read (Fig 5 out of scope) | not compared |

## Consequences
* ADV-320 bound (2) stands on two readings: the text's 41 and "up to 42" percent are Fig 4C whisker maxima; medians about 23 and 39 (ratio about 0.60); Table S1 CAG against p546 adjusted P 0.0097. IT may narrow CLAIM 047 on this basis. The intensity ratio from medians is 0.22 (D) and 0.21 (H) against 0.324 from the text numbers; the claim should say which statistic each number is. HE's tCAG 5.8 against 3.1 does not touch p546, CAG or gfa1405.
* Bound (1) stands: n = 4 per promoter (legend), gfa1405 liver about 81 against 5 to 6, error-bar type and post-hoc test NOT PRINTED.
* **Correction to RESULT_ADV320, section 3, counterexample 2 (my positional labelling):** liver gfa1405 about 81 over its brain areas is BA1 5.1 times, BA2 1.8 times, BA3 4.8 times (brain bar tops 16, 44, 17), not "1.8, 4.9 and 4.8" in the order listed. With H's brain values (16, 45, 17): 5.0, 1.8, 4.7. Still no threshold was frozen, so this is a description, not a pass or fail.
* The one blind reader (H) and the non-blind reader (D) agree, so the non-blindness of D left no visible trace in these cells; it does not prove independence for panels H did not re-measure (the low-end overlapped boxes, the percent panel, Fig S1B at 1.5 units).
