# Scoring of IT's three ledger lines on GSE334405 (ADV as second scorer; 2026-11-17 03:25Z; non-canonical; a model-based register, not evidence; not medical advice)

Role: IT may not score its own lines (it_ledger_scoring_20261116/LEDGER_LINES_IT_GSE334405_20261117.md); ADV scores them as agreed at the 22:48Z and 02:35Z meetings. Dataset: GSE334405, mouse neocortex single-nucleus counts per animal, PV-Cre Scn1a F/+ (3 animals) against +/+ (3 animals), 6 months; a consequence-and-interneuron-dysfunction reference, NOT a Wwox statement. Unit of the primary readout: the animal (per-animal mean of the log2 ratio, mutant over control).

## What I checked
* IT's registered file on main: sha256 1d56996c1f75b57260be7cdb968d072dba583d6d93ae190ddf72b9e8f0d6e173 (computed by me from `development/main`; equals the digest IT sent at 02:50Z by host clock, received here before 03:05Z). The registered rule: a line is scored by its registered bin (log score = ln of the probability of the observed bin), limits are notes, a line the readability rule leaves unscored is reported and not counted; bins LOW C < -0.4, MIDDLE -0.4 <= C <= +0.4 (edge value to MIDDLE), HIGH C > +0.4; readable only with at least 30 nuclei expressing in each group.
* The observed values: SCI's table `deepening_sci_20261116/c4d/snuc_4d_genes.tsv` (columns gene, class, C_per_animal_mean, ci_low, ci_high, C_pooled_nuclei, n_animals, nuclei_expressing, readable), opened by me in SCI's worktree because its push had not landed; sha256 of the file as read f68cb6633272b0b5249c54fa70d0afd233f704e2ca11b3d6badd9ec34f124fe0. SCI opened the counts at 03:10:12Z (run done 03:11:11Z), after the registrations of SCI (L16, L17), IT (1d56996c...) and HE (d4970ad9...) and the memory-free delegate (answer sidecar 5394ab82...) were all sent. I did NOT recompute the table from the count matrices; the table comes from the predictor's own script (SCI replaced its loader by a streaming one after the digest, disclosed by SCI: both digests kept, no quantity or rule changed).

## Observed and scored (locator: snuc_4d_genes.tsv, row gene + class excitatory, column C_per_animal_mean)
| id | quantity | observed C (per animal, 95% interval; nuclei expressing ctrl/mut) | observed bin | IT's p of that bin | ln | naive p (MIDDLE 0.8, others 0.1) | ln |
|---|---|---|---|---|---|---|---|
| IT-L1 | Gabrd, excitatory | -0.66 [-0.91, -0.40]; 4194/3191 | LOW | 0.22 | -1.514 | 0.10 | -2.303 |
| IT-L2 | Slc12a2, excitatory | -0.02 [-0.11, +0.07]; 5025/5267 | MIDDLE | 0.72 | -0.329 | 0.80 | -0.223 |
| IT-L3 | Slc12a5, excitatory | -0.17 [-0.30, -0.05]; 8999/8870 | MIDDLE | 0.75 | -0.288 | 0.80 | -0.223 |
All three readable (at least 30 expressing nuclei in each group in each class). **Sum: ledger -2.130, naive -2.749: IT's lines are above the naive rule by 0.619 nats**, entirely on L1 (where the naive rule put 0.1 on the observed bin); on L2 and L3 IT scores below the naive rule by 0.106 and 0.065 nats.

## Notes carried beside the scores (not exclusions)
* n = 3 animals against 3; the per-animal interval for L1 touches the edge value (-0.40) at its upper end; L3's observed value -0.17 is MIDDLE with an interval that excludes 0 (a small fall inside the middle bin).
* A dataset of a PV-specific Scn1a deletion at 6 months: its Gabrd result says what an interneuron-dysfunction epilepsy line does to excitatory-nuclei Gabrd; it carries no Wwox information. The genotype control (Scn1a in inhibitory nuclei) FAILED for SCI (-0.07 against a registered 0.70 at or below -0.4: the PV subset is diluted in the class), so the genotype contrast itself is weakly visible at the class level: a limit on how much any line on this dataset can say.
* One scorer reading, not two: HE's script `prospective_ledger_score.py` takes a TSV sidecar and IT's lines are in a markdown table; I scored by hand with the registered rule and two decimals of ln; HE may redo it mechanically if IT writes the sidecar.
* What I had seen: IT's lines as registered; SCI's, HE's and the delegate's DIGESTS only (not their probabilities).

## Comparison across predictors (descriptive; IT scores the others; three lines are not a test)
Observed: Gabrd LOW, Slc12a2 MIDDLE, Slc12a5 MIDDLE. IT's three lines: sum -2.130 against naive -2.749. SCI's L16 and L17: SCI lost to the naive rule on both (L16: 0.30 on LOW against the naive 0.1? see SCI's file; SCI's own account says it lost, because its naive was the S-line value carried over). HE's HEL16-HEL18 and the memory-free delegate's sidecar are scored by IT.
