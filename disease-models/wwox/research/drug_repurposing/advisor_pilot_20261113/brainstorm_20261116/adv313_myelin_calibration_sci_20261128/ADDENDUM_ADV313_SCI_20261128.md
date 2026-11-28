# ADV-313 dated addendum (SCI, 2026-11-28): cells corrected after two blind readings

Hypothesis level; reference genotype class only; nothing here is medical advice. This is the only addendum. The original table, result and sentences are not edited; where they differ from this file, this file is the later reading.

Sources of the corrections: `../adv313_consumers_it31_20261128/BLIND_ADV313_K_IT31.md` (IT31, two blind readers) and `../adv315_blind_calibration_he_20261128/RESULT_ADV315_HE_20261128.md` (HE, one blind delegate plus HE's own comparison). SCI rechecked the cells marked "text" below against the held XML on 2026-11-28; "figure" marks what SCI did not reopen.

## 1. Table cells (`CALIBRATION_TABLE_ADV313_SCI_20261128.tsv`): 13 corrections, 12 distinct cells

| # | Row, column | Read instead | Found by | SCI recheck |
|---|---|---|---|---|
| 1 | Crawford 2010, age | female PLP-EGFP C57BL/6J, 6 weeks old at ovariectomy, EAE induced 2 weeks later; electron microscopy at day 36 after induction (Figure 5 legend). HE: no velocity timepoint is printed | IT31, HE (same cell) | text |
| 2 | Mu 2019 (PMID 31140740), same_animals | cohort, at matched coronal levels +0.16 and -1.59 mm; whether the electron-microscopy tissue is from the recorded slices is not stated | IT31 | text (a phrase search found no such statement) |
| 3 | Nr2f1 heterozygotes, n_and_stimulus (EM) | N = 3 for the myelinated-fibre counts (Figure 4N, 4Q). The g-ratio 0.63 against 0.74 is cited to Figure 4R, S; the Figure 4 "Data information" line read gives no N for those panels. Figure 5 (miconazole) has N = 2 for panel M | IT31 | text |
| 4 | STZ rat (PMID 34576288), n_and_stimulus (recording) | cervical and lumbar both stimulated in 5 animals per group; the remaining animals lumbar only | IT31 | text |
| 5 | STZ rat, age | 13 weeks old at induction, tested 23 weeks later (about 36 weeks) | IT31 | text |
| 6 | Astrocyte exocytosis block, structural_readout | "axon diameter and number unchanged" is not one statement: the text says no change in axon diameter or number of myelinated axons in one place and in the number of unmyelinated axons in another (both SI Figure S3Q, R) | IT31 | text |
| 7 | Fig4 knockout, structural_readout | printed in the text, not only read by eye: P21 myelinated axons 79 +- 2 percent (control), 9 +- 3 (SynCre), 12 +- 1 (Olig2Cre); P60 to 75: 92 +- 2, 16 +- 4, 12 +- 2. The computed ln -1.88 does not change | IT31 | text |
| 8 | Palma 2022, structural_readout | the text says the number of myelinated axons was reduced and prints no count. The 287 to 249 pair is a Figure 4A reading carried from ADV-304 (HE's blind figure reading: 288 to 250) | HE | text (no count found) |
| 9 | Crawford, structural_readout | the means of "myelin sheath thickness" and g-ratio **include unmyelinated axons** (Figure 5C scatter plots hold axons at g = 1.0 and thickness 0 in every group, most in vehicle EAE). Read "mean myelin thickness over all axons, unmyelinated included"; ln -0.80 mixes loss of myelinated axons with thinner sheaths | HE | figure (not reopened) |
| 10 | Crawford, age (HE's cell) | counted with row 1 | HE | |
| 11 | Crawford, n_and_stimulus | the paper disagrees with itself: Methods say 3 mice perfused for electron microscopy; the Figure 5 legend says at least 4 mice per group were analysed | HE | text |
| 12 | Mu, conduction_readout | add: **N1 half-width lower with cuprizone** at both levels (P < 0.001, calculated at 1 mA; Figure 4E, I), N2 half-width not affected (2 mA); N2 area higher (HE) | HE | text for half-width |
| 13 | Mu, n_and_stimulus | cuprizone CAP **8 to 10 mice per group** (Figure 4 legend), not 6 to 10 | HE | text |

HE reports 42 numeric values compared with none differing beyond figure-reading precision. No correction above changes the label READABLE, the direction counts or the no-rank-agreement reading.

## 2. Wording that goes with the cells

* Cuprizone N1 velocity reads **"not significantly different from sham at one 0.75 mm distance"**, not "unchanged". HE notes that Appendix S2 gives "0.75 mm or 1 mm" (a delegate's reading of the supplement, not rechecked).
* The sham series of the cuprizone figure and of the stroke figure **look partly shared** (HE and HE's delegate, by eye, not pixel-verified; no statement of a shared control was found). Do not write them as independent controls.
* Sentences K1 to K3 of `SENTENCES_FOR_IT_ADV313_SCI_20261128.md`: IT31 graded K1 MUST CHANGE and K2, K3 ADD; do not use them as written. IT31's proposed K1' to K3' are in its file (HE saw no need to change K1 to K3; the two readings differ and the stricter one is followed here).
