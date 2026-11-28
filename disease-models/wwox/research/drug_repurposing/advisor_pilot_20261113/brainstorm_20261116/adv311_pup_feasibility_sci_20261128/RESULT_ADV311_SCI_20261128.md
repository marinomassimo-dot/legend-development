# ADV-311 result (SCI, 2026-11-28): does the pup brief stay executable at the observed knockout frequencies?

Hypothesis-level arithmetic from held numbers only. No dose, no breeding advice, no cost, no contact. PREREG sha256 78ef5447d291740210ca29dd1a563986b8423feca5b8b588df908f2d739e660e (file `PREREG_ADV311_SCI_20261128.md`, frozen before the arithmetic and before the Ludes-Meyers, Repudi, Hussain 2023 passages were read). Script `arith_adv311.py`, output `arith_output.txt` (run with `python3 -I`). Receipts: see section 7. No delegate.

## 1. The two supplement sentences, verbatim (Cheng 2020, PMID 32000863)
Source: `files/fulltext/PMID32000863_Cheng2020_supplementary.pdf` (24 pages, sha256 0acb771cfe3a4c3644b41c10451504047adb715e69727c1889f72774151f8b7f), extracted with `pdftotext -layout`.
* **Supplementary page 3, lines 11 to 14 of the extracted page, Genotyping methods (the Methods section is headed on page 2):** "Neonatal mice at postnatal day 5~12 from Wwox+/- intercrosses were collected for genotyping and the percentages of Wwox-/- mice were 5.1% and 6.5% for WD1 (N=177) and WD234 (N=785), respectively."
* **Supplementary page 2:** "For PCR genotyping, tail genomic DNA was isolated from mice at postnatal day 5~10."
The paper gives no count of knockouts, no litter size, no number of litters, no genotyping age per pup and no statement about prenatal or perinatal loss. Counts implied by the printed percentages: 0.051 x 177 = 9.03 (9 knockouts) and 0.065 x 785 = 51.02 (51). WD1 and WD234 are the two lines (exon 1 and exons 2/3/4 deletions); WD1 vs WD234 do not differ (Fisher two-sided p = 0.61). The two sentences differ in age range (P5 to P12 here, P5 to P10 in the genotyping sentence): the P5~12 sentence is the one that carries the frequency. **Erratum to my own PREREG:** its disclosure line listed a Cheng Results statement "that some severely affected embryos died before birth" as seen. I searched the held Cheng text (died, before birth, perinatal, embryonic lethal, stillborn, litter, Mendelian, survival): there is no such statement; the only survival statement is "survived for less than a month" (Additional file 1 Figure S1d, main text). The embryo-stage findings (E12.5 smaller, growth delay) concern embryos that were collected, not loss.

## 2. Knockouts per litter and litters needed (L = 7, the brief's own value)
The brief's L = 7 is not from Cheng (no litter size there); the only held litter-size datum is Ludes-Meyers 2009: litters of 3 to 11, average 7.75, 10 matings, +/dCre x +/dCre. The brief's own check holds: 33 knockouts / 1.75 = 18.9, the brief's "about 19 litters".

| Frequency f (source) | n / N | Knockouts per litter, L = 7 | L = 5 | L = 9 |
|---|---|---|---|---|
| Cheng WD1, P5 to P12 | 9 / 177 = 0.051 (Wilson 95% 0.027 to 0.094) | 0.357 | 0.255 | 0.459 |
| Cheng WD234, P5 to P12 | 51 / 785 = 0.065 (0.050 to 0.084) | 0.455 | 0.325 | 0.585 |
| Ludes-Meyers 2009 EIIA-Cre null, P3 | 30 / 154 = 0.195 (0.140 to 0.264) | 1.364 | 0.974 | 1.753 |
| Mendelian (the brief's assumption) | 0.25 | 1.750 | 1.250 | 2.250 |

Mendelian over observed: 4.90 (WD1), 3.85 (WD234), 1.28 (Ludes-Meyers). Knockouts obtained from 20 litters of 7: 7.1 (WD1), 9.1 (WD234), 27.3 (Ludes-Meyers), 35.0 (Mendelian).

**Litters needed = ceil(n_KO / (7 x f)), n_KO taken from the brief and ADV-061 (section 3 of PUP_BRIEF_V2):**

| Scenario (knockouts) | WD1 | WD234 | Ludes-Meyers | Mendelian |
|---|---|---|---|---|
| Stage 1 pilot, 6 per knockout cell (6) | 17 | 14 | 5 | 4 |
| Stage 1 pilot, 8 per knockout cell (8) | 23 | 18 | 6 | 5 |
| One knockout arm of 11 (11) | 31 | 25 | 9 | 7 |
| Two knockout arms of 11, stage 2 vehicle + ethosuximide (22) | 62 | 49 | 17 | 13 |
| Three knockout arms of 11, the brief's planning minimum with the dose check (33) | 93 | 73 | 25 | 19 |
| Two arms of 31 (62) | 174 | 137 | 46 | 36 |
| Three arms of 31 (93) | 261 | 205 | 69 | 54 |
| Plan upper bound of the brief (150) | 421 | 330 | 110 | 86 |
| ADV-061 simple effect, 36 per arm x 2 (72) / 109 per arm x 2 (218) | 202 / 611 | 159 / 480 | 53 / 160 | 42 / 125 |
| Interaction, 22 per cell x 2 knockout cells (44) | 124 | 97 | 33 | 26 |
| Interaction, ADV-061 350 to 630 knockouts | 981 to 1765 | 770 to 1385 | 257 to 462 | 200 to 360 |

Sensitivity of the 33-knockout row to litter size: L = 5: 130 (WD1), 102 (WD234), 34 (Ludes-Meyers); L = 9: 72, 57, 19. At L = 7.75 (Ludes-Meyers average) the row is 84 and 65 for the two Cheng lines.
**Pre-genotyping loss is kept apart.** The table uses the frequency at genotyping as if it were the frequency at the assay age (an upper bound at later ages, see section 4). Any knockout lost before P5 to P12 lowers litters-per-knockout further and is not counted; any loss of knockouts after genotyping and before the assay lowers it too. Neither is recoverable from Cheng.

## 3. Prediction check
Predicted: every knockout arm of 10 or more needs more than 20 litters under both Cheng frequencies; only the pilot at 6 to 8 per cell stays near 20; the 3-arm plan of 33 needs 92 and 73; interaction numbers 980 to 1760 and 770 to 1380. Observed: 11 per arm needs 31 and 25 (met); pilot 17 to 23 (WD1) and 14 to 18 (WD234): **one miss, 8 per cell under WD1 is 23 litters, I wrote 22**; 33 knockouts needs 93 and 73 (I wrote 92 for WD1: ceiling of 92.4, rounding); interaction 981 to 1765 and 770 to 1385 (rounding). No observable separates E-A from E-B (as predicted): both give the same upper bound at later ages.

## 4. E-A against E-B
* Within the Cheng lines: **undetermined.** The sentence gives one frequency at one pooled age window; no birth count, no per-day count, no litter count. E-A (loss before genotyping) and E-B (stable population at P5 to P12) predict the same printed number.
* **Bound at later ages (both explanations):** the brief's assay ages lie between P12 and about P28 and knockouts die at about 3 to 4 weeks (Cheng main text; Repudi 2021 Brain Fig. 1 legend and text). If knockout loss between genotyping and the assay is no smaller than loss of the other genotypes, the knockout frequency at the assay age is at most the genotyping frequency; this is an assumption of direction, not a held measurement.
* **Across lines (a lead, not a test):** Ludes-Meyers genotyped 154 P3 pups from +/dCre intercrosses: WT 39, HET 85, KO 30 against expected 38.5, 77, 38.5; their stated chi-square p = 0.257, and my recomputation of chi-square(2 df) from the table gives 2.715, p = 0.257. 30/154 against Cheng 9/177 and 51/785: Fisher two-sided p = 5.8e-05 and 2.1e-06. A drop of knockout odds between P3 and P5 to P12 to 0.22 (WD1) and 0.29 (WD234) of the P3 odds would explain the difference **if the lines, laboratories, backgrounds and genotyping ages were comparable, which nothing held shows.** So the difference is compatible with E-A and equally with line and background (E-B or a line-specific birth frequency).
* **Counterexample against the "5 to 6 per cent is a property of the Wwox-null mouse":** Ludes-Meyers 19.5% (Wilson 14.0 to 26.4%) is Mendelian-compatible by the paper's own test. **By the letter of my frozen threshold (at least 20%) it is not met: 19.5% is 0.5 points below.** I report both and do not round it up. Repudi 2021 Brain states "Wwox-null mice are born at a Mendelian ratio" (Results, first paragraph, citing refs 19 and 20, of which ref 20 is Aqeilan 2008, not held) and "N-KO mice were born at a Mendelian ratio": **no counts, no age, no cross stated in the held text**; the supplement folder holds no genotype table. Hussain 2023 (P47T knock-in, not a null) reports expected Mendelian ratios from heterozygote breeding, "Supplementary Table 1", which I did not open. Ludes-Meyers also reports Wwox flox/flox crosses with normal litter size and genotype frequencies (no counts in the passage read).

## 5. The number that makes the brief infeasible as written
f* = K / (cap x L). For the brief's 33-knockout planning minimum: cap 20 litters, f* = 23.6%; cap 25, 18.9%; **cap 50, 9.4% (my frozen choice, not from a held source)**; cap 86 (the brief's own upper planning bound), 5.5%. Both Cheng frequencies are below 9.4%; against the cap of 86 the 33-knockout minimum fits for WD234 (6.5% is above 5.5%; 73 litters) and not for WD1 (5.1% is below 5.5%; 93 litters); the Ludes-Meyers frequency (19.5%) sits above 18.9%, so **under it the minimum needs 25 litters, within the brief's own scale.** For the 150-knockout upper bound the critical frequency is 24.9% at the 86 cap, i.e. Mendelian only.
Label: **the brief as written (19 litters for the 33-knockout minimum, 19 to 86 for the whole plan) does not hold at the Cheng frequencies: 73 to 93 and 73 to 421 litters respectively. Whether that is "infeasible" depends on a litter ceiling that no held source provides; the fixed ceiling of 50 is exceeded by the minimum under both Cheng lines.** The brief is not demonstrably infeasible at a P3 frequency like Ludes-Meyers.

## 6. What changes, and the registered missing observation
* The brief's sizing sentence ("a litter yields about 1.75 knockouts"; "19 to 86 litters") should be restated with the observed frequency as an alternative column (sentences Y1 to Y3 for IT).
* Neuron-specific preparation (Repudi N-KO and S-KO): **no held frequency or count**, and the held text does not state the cross, so the knockout fraction of such a cross cannot be set from held material (it depends on the cross, not only on Mendelian segregation). The alternative preparation cannot be sized from the held record.
* **Missing observation:** genotype counts at birth and at the assay age, by strain, deletion and background, with litters and deaths before genotyping, from the laboratory's own colony or from any source that prints counts (Cheng printed only percentages; Aqeilan 2008 is the cited source for the Mendelian statement and is not held).
* The brief's arms stay as written only if the laboratory's own colony gives a frequency near Mendelian at the assay age; otherwise stage 1 (pilot, 14 to 23 litters) is the only stage inside about 20 litters.

## 8. Addendum (2026-11-28, after the Aqeilan 2008 close-out)
Aqeilan 2008 (J Biol Chem 283:21629) is "not held" in sections 4 and 6 only in the sense that no copy sits in `files/fulltext/` on this machine; the ledger records a complete read (FTR-20260811-18487609-01). The re-fetch (`AQEILAN2008_CLOSEOUT_ADV311_SCI_20261128.md`, PMC page, plain request; the PMC PDF returned a reCAPTCHA page and was not read) gives: genotype analysis of newborns from a Wwox+/- intercross, "ratios consistent with the Mendelian distribution (7)", B6-129 hybrid, no counts, no litters, no age; KO indistinguishable up to 3 days, all KO dead by 3 weeks. No arithmetic row can be added (no counts). The frozen readings stand: E-A and E-B undetermined within the Cheng line.
