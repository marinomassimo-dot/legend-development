# Prospective out-of-sample prediction ledger (SCI, 2026-11-16 23:0xZ; registered BEFORE any of the target data exist in our hands; hashed; scorer: IT; baselines: a memory-free delegate given the same task text, and the naive rule 'same sign as the nearest held line' / 'central value of the held range')
Written for: IT (scorer), ADV, HE. Each line: target dataset (not held now), quantity, my prediction as a range and the probability I put on it (a log score can then be computed), and what the baselines would say. The ledger is a MODEL-based register, not evidence; once hashed it is not edited (a change is a new version with a new digest).
| id | target (not held now) | quantity | my prediction (range, probability) | naive baseline |
|---|---|---|---|---|
| L1 | authors' per-cell sIPSC values, Breton 2021 Fig. 4 (S-WT, S-HT, S-KO) | position f = (S-HT - S-KO)/(S-WT - S-KO) of the mean sIPSC amplitude | f between 0.75 and 1.10, probability 0.65; f between 0.25 and 0.75, probability 0.30; below 0.25, 0.05 | f = 0.5 (midway) |
| L2 | the same authors' sIPSC | S-HT against S-WT mean frequency | within +/-25%, probability 0.6 | no difference |
| L3 | authors' burst event lists (119 bursts, 18 slices, 9 animals) | rho(preceding interval, duration), pooled with slice as cluster | between 0.00 and +0.35, probability 0.65 (two-stage-like +0.18); above +0.35 (rival-like +0.37) probability 0.30 | 0 |
| L4 | the same lists | rho(duration, following interval), pooled with slice as cluster | between +0.05 and +0.40, probability 0.65 | 0 |
| L5 | any WWOX-deficient cortical transcriptome not yet held (third line or later age), cortex | Gabrd log2 fold against wild type | between -1.3 and -0.3, probability 0.65 (sign negative 0.8) | same sign as the nearest line (negative) |
| L6 | same | Npy and Gfap log2 fold | both positive, probability 0.75 | same sign as nearest line |
| L7 | L2/3 pyramidal cells of S-KO and wild type at P13 to P17, THIP 1 to 10 uM evoked current | ratio S-KO over wild type | between 0.5 and 1.2, probability 0.6 (a clear deficit, below 0.5, probability 0.25) | 1.0 |
| L8 | same cells, endogenous tonic current (no exogenous GABA) | ratio S-KO over wild type | between 0.6 and 1.4, probability 0.6 | 1.0 |
| L9 | P47T/P47T slices at P13 to P17 (if ever recorded) | fraction of neocortical slices with spontaneous bursts | between 0.0 and 0.6, probability 0.7 | the S-KO value (0.86) |
| L10 | public chronic-seizure cortical transcriptomes (a transfer test; datasets to be selected before opening, ADV candidate [4]) | Gabrd direction in the seizure model | negative, probability 0.55 (the 'consequence' reading predicts the same sign as in the WWOX lines) | same sign as WWOX lines |
Scoring rule fixed now: per line, the probability assigned to the observed bin (log score); the engine 'improves' only if a later version beats this one and both baselines on a second ledger of this kind (see ENGINE_EVAL_INPUT_SCI.md).
