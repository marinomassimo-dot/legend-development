# SCI read of Breton 2021 Supplementary Fig. S4, S1 and S2 (window 9bb60ab5; written before the blind reader was dispatched; hypothesis level; not medical advice; reference genotype class only)

Mouse neocortical slices, layer II/III. Values read from `image4.tiff` (1431 x 408 px) by pixel profile. Calibration: a1 y 9.48 px/Hz (0 Hz at row 327.9), x 1.18 px/pA; a2 y 9.05 px/Hz (0 at 327.75), x 1.70 px/pA. Read error about +/- 2 px = +/- 0.2 Hz on a centre, +/- 0.4 Hz on a half bar. "bar" = half length of the error bar. n from Table 1 (cells/animals): pyramidal S-WT 13/5, S-HT 15/6, S-KO 40/15. Animals are the replication unit for inference; the figure gives no per-animal value.

## S4 a1 (raw current; caption: mean +/- SEM)

| current pA | S-WT Hz (bar) | S-HT Hz (bar) | S-KO Hz (bar) | KO minus WT | over combined bar | star |
|---|---|---|---|---|---|---|
| 40 | about 0.6 (hidden) | about 1.1 | 2.7 (0.9) | about 2.1 | not computed | no |
| 60 | 1.8 (1.3) | about 5.6 | 6.3 (1.3) | 4.5 | 2.4 | no |
| 80 | 3.0 (1.5) | 9.3 (2.1) | 10.4 (1.6) | 7.4 | 3.4 | yes |
| 100 | 6.0 (2.0) | 12.4 (2.4) | 14.0 (1.9) | 8.0 | 2.9 | yes |
| 120 | 9.9 (2.3) | 15.4 (2.3) | 17.5 (2.0) | 7.7 | 2.5 | yes |
| 140 | 13.2 (2.7) | 18.6 (1.7) | 21.0 (2.0) | 7.9 | 2.4 | yes |
| 160 | 17.0 (2.3) | 20.6 (1.6) | 23.7 (2.1) | 6.7 | 2.2 | no |

At -40 to 20 pA all groups sit at 0. HT values at 60 pA read by eye. The "over combined bar" ratio is an EXPLORATORY screen, not a test.

* P1 (KO above WT at every starred step): **holds** (80, 100, 120, 140 pA).
* P3 (steps where KO is not above WT): none from 40 to 160 pA; at 20 pA and below all are zero.
* P4 (S-HT within one combined bar of S-KO at the starred steps): **yes at all four** (differences 1.1, 1.6, 2.1, 2.4 Hz).

## S4 a2 (current referred to rheobase: 0 = 20 pA below rheobase)

| x pA | S-WT Hz (bar) | S-HT Hz (bar) | S-KO Hz (bar) | KO minus WT | over combined bar |
|---|---|---|---|---|---|
| 20 | 4.06 (hidden in marker, at most about 0.7) | 8.15 (hidden) | 5.99 (hidden, at most about 0.7) | 1.9 | at least about 2.0 |
| 40 | 10.1 (about 0.8) | about 12 | 11.9 (hidden) | 1.8 | at least about 1.7 |
| 60 | 12.07 (1.1) | about 16 | 16.0 (0.9) | 3.9 | 2.8 |
| 80 | 16.0 (1.2) | 17.9 (0.9) | 20.0 (1.2) | 4.0 | 2.4 |
| 100 | 22.0 (1.3) | 20.0 (1.0) | 22.0 (1.2) | 0.0 | 0 |
| 120 | no point | 22.0 | 24.0 (1.3) | - | - |
| 140 | no point | 23.9 (1.2) | 26.0 (1.3) | - | - |

* **P2 fails** under the frozen screen at 60 and 80 pA (two consecutive steps), and at 20 pA borderline.
* **Observation not foreseen by the PREREG:** every a2 centre that I read lies within 0.15 Hz of an even number (4, 6, 8, 10, 12, 16, 18, 20, 22, 24, 26). With 500 ms pulses one spike is 2 Hz. Means over 13 to 40 cells would not be expected to fall on that grid, so the a2 points look like medians or single-sweep counts, and what the a2 bars are is not stated (the caption's "mean +/- standard error" sentence closes a1). The screen's premise (bars = SEM of means) is therefore not established for a2. a1 centres are not on that grid.
* The caption states p > 0.05 for all a2 combinations (unpaired t-test). The plotted points and bars do not obviously agree with that for KO against WT at 60 and 80 pA; the figure alone cannot decide which is right.

## S4 b1, b2 (interneurons; S-CTL = S-WT + S-HT, 5 cells/4 animals; S-KO 6/5)

Bars of roughly 20 to 70 Hz; the group differences are smaller than one bar at every step by eye. **P5 holds.**

## Verdicts by the frozen rules (section 3)

* **F-a:** MUST CHANGE if the a2 bars are SEM of means (P2 fails at consecutive steps); ADD if the caption's p statement is taken as authoritative for a2 (the screen's premise not established). Both readings are reported and not merged. P1 holds and the stars mark KO against WT under both.
* **F-b ("increased firing"):** under the first reading UNCHANGED (excess in a1 and at 20 to 80 pA in a2; none at 100 pA); under the second reading MUST CHANGE (excess only with raw current, and the claim record states a null on the slope, not that the excess is absent once current is referred to rheobase).
* **P4** is a new qualifier either way: the figure does not show the raw-current excess to be specific to the homozygous knockout; S-HT sits with S-KO.

## S1 (image1) and S2 (image2): what the images print

* S1 C: box at about 3 to 5.5 Hz phase and 130 to 215 Hz amplitude; S1 E: delta phase with about 30 to 140 Hz. S1 D: 102 bursts, no clear trend; S1 F: 41 bursts of one animal. S1 G, per animal (n = 9): rho positive in 8 animals and strongly negative in animal 3; p below 0.05 by eye only for animals 1 (positive) and 3 (negative). The caption's "no significant correlation or negative correlation in 8/9" agrees with this (seven not significant plus one negative).
* S2: two example sets of simultaneous LFP and whole-cell recordings during bursts, at holding -70 mV (inward currents), -30 mV (mixed) and 0 mV (outward currents). No counts, no groups, no n, no statistic; whether the sets are different cells or animals is not printed.
