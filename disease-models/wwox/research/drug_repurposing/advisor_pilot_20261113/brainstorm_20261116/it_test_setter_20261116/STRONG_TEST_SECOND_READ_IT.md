# Second read of six strong-test categories, and the arms revealed (IT; non-canonical; not medical advice)

Written for: SCI (cites it in STRONG_TEST_FATE), ADV (closing synthesis). Reference genotype class only. SCI's execution: leap_sci_20261116/STRONG_TEST_FATE.tsv, strong_test_output/strong_test_values.tsv, strong_test_run.py (commit 6d16c004d in the shared store; the files had not landed on development/main when I read them). Key revealed AFTER SCI's categories were fixed: KEY_TS_REVEALED.json sha256 c7d04a8f3f60106475e92c4cec729ba4fb3bb8bc5b8b31e34d76d967aae9a17e equals the digest pushed before the run (c7d04a8f3f60106475e92c4cec729ba4fb3bb8bc5b8b31e34d76d967aae9a17e).
## Second read (IT read the setter's threshold and SCI's measured values; the six items agree; I could not recompute M30 because the held GSE52564 files are binary spreadsheets that SCI converted; M29 recounted from the matrices)
| Item | SCI | IT | Basis |
|---|---|---|---|
| M08 | R | R: agree (as written) | The setter's rejection is a disjunction; branch (c) Spearman of observed against projected change over the 7 listed genes without CCN2 is -0.71 (threshold <= 0): met; branches (a) 4 of 7 in agreement and (b) 2 of 4 named genes opposed are not met. It rests on one of three branches and n = 7 genes (a rank correlation of -0.71 on 7 points is not itself strong); it is a rejection of the composite-maturation reading as the setter wrote it. |
| M10 | U | U: agree | The setter's rejection needs 'no positive enrichment in the organoid and in each mouse contrast' or loss after composition adjustment; only P47T hallmark results are held (NES 1.54 to 2.06, q <= 0.0085, positive), and the organoid and P17 hallmark runs cannot be computed on this host (hallmark GMT absent): the evaluated branch does not reject, the others cannot be evaluated. SCI reports this as a deviation, correctly. |
| M12 | U | U: agree | The setter's rejection is an AND of table 5 (3 of 4 regions at ratio >= 0.90: met, 3 of 4) and the table 3 null contrast, which cannot be tested on the committed |cLFC| >= 0.585 file (Erbb4 is not among its rows): half a test; SCI reports it as a deviation. |
| M23 | U | U: agree; AUTHOR READS OWN ITEM (HIT-1) | The threshold's precondition (at least 4 children with explicit pre-treatment imaging) is met for 2 of 6; the count over all 6 (2 contradicting, 4 confirming) would not have rejected either. |
| M29 | R | R: agree | Snap25-positive nuclei 2320 of 3182 (0.7291) in the control pool and 2219 of 2920 (0.7599) in the knockout pool, recounted by IT from the matrices: knockout minus control +0.031, the rejection condition (>= -2 SE, about -0.022) met; the hypothesis (knockout pool depleted of neuronal nuclei) is rejected for these two pools. M29 is the PLANTED held-table item. |
| M30 | N | N: agree, with limits | The test could fail (a neuron/astrocyte FPKM ratio >= 2 for Slc6a1 or Slc6a11 in either species) and did not in mouse (0.31 and 0.06); the human neuron class has n = 1 (ratios 1.56 and 0.24); the 'neuron-enriched preparation' disjunct is not statable on held data, so N covers the astrocyte-enrichment disjunct only. Not recomputed by IT. |
Agreement 6 of 6 (one of them my own item, so 5 independent). Deviations are SCI's own (M10, M12, M23) and I confirm each is stated in its row.
## Arms revealed (strong-test categories by the setter's own definitions; counts only)
| Arm | n | setter 'could held data reject' = yes | strong R | strong N | strong U |
|---|---|---|---|---|---|
| A: memory-free baseline | 5 | 1 | 1 (M08) | 0 | 4 |
| B: repository, no perspective | 5 | 0 | 0 | 0 | 5 |
| ADV | 5 | 3 | 0 | 1 (M04) | 4 |
| HE | 4 | 2 | 0 | 2 (M11, M30) | 2 |
| IT | 5 | 1 | 0 | 0 | 5 |
| SCI | 5 | 1 | 0 | 1 (M17) | 4 |
| 29 hypotheses | 29 | 8 | 1 | 4 | 24 |
Planted: the held-table item (M29) setter yes, strong R (rejected); the new-recording item setter no, U: both as designed (n = 2).
## Reading
Only 8 of 29 (28 percent) of the hypotheses had any test that the held data could have rejected; 1 was rejected (an arm A hypothesis), 4 survived a test that could fail, and 24 are untestable on held data. The arms do not separate: yes-shares 0 to 3 of 4-5, one R, four N, at n 4 to 5: NOT SEPARABLE at n 5 (SCI's estimate: about 20 per arm). What the metric measures is how many hypotheses were ever testable in held data (the reach of the held tables), not how many were right. Cost: setter 91,819 tokens (harness notice), SCI's execution not read by IT.
