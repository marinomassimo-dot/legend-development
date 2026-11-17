# Pilot threshold-bisection scan: result (HE runs the frozen scan, SCI owns the model and the predictions; 2026-11-17; hypothesis generator, not evidence; not medical advice)

Written for: SCI (scores P1 to P4 literally), ADV. Frozen before the run: `freeze.json` sha256 `da37aa3bd623de40bac79f381438bc65b3ba754f4e59cd6c5406e61e182720fa` (sent to SCI at ~23:00Z on 2026-11-16, no wording change requested); adapter 2871a5db..., rebound_oscillator c050b8ff..., spec ab9a24cd...; harness with the new `bisect` design (11 tests). Run: 17 cells, bracket [0, 3] in strength s, 6 halvings (final bracket width 3/64 = 0.047), 5 seeds (base seed 1000), 565 rows (arm5_KO needed only the far-end check: not in bracket). `results.sha256` / `run_manifest.json` are in the folder; `RUN_LOAD_RECORD.txt`: start 2026-11-16T23:05:22Z at load 2.93, load 6 to 7 for most of the run (the publication gates of five sessions shared the 4 cores, 3 workers), end 2026-11-17T00:24:58Z at load 2.37: **the load affected timing only (80 minutes against an estimate near 66), not the scores**. One cell was re-simulated with `check` to confirm byte identity: `CHECK cell arm2_HT: rows 35; byte-identical True; largest relative difference 0`.
## Crossing strength per cell (the midpoint of the final bracket; the median over 5 seeds decides each halving; per-seed values of the last evaluations are in `PER_CELL_SEED_VALUES.tsv`)
| arm | S-KO | S-HT |
|---|---|---|
| 1 d-APV-type | 0.164 | 0.070 |
| 2 NMDAR pore | 0.914 | 0.398 |
| 3 GluN2B NAM (rel_duration below 0.8) | 1.945 | not bisected |
| 4 AMPA | 1.430 | 0.586 |
| 5 T-type | not within [0, 3] | 2.789 |
| 6 synaptic GABA-A | 1.711 | 0.445 |
| 7 neurosteroid-type | 0.539 | 0.258 |
| 8 sodium, pyramidal | 1.102 | 0.445 |
| 9 sodium with interneuron share | rel_bursts below 0.7 at 1.898 | rel_bursts ABOVE 1.5 at 0.398 |
## Predictions as registered (SCI's wording kept, mechanical form frozen): 8 of 9 PASS, 1 FAIL
P1 (S-KO order d-APV < neurosteroid-type < NMDAR pore < sodium pyramidal < AMPA < synaptic GABA-A < T-type): PASS (0.164 < 0.539 < 0.914 < 1.102 < 1.430 < 1.711 < not in bracket). P1b (T-type only above s = 2 or not within the bracket): PASS. P2a (GluN2B NAM does not cross within s <= 1): PASS (1.945). P2b (only above 1.5): PASS. **P3a (arm 9 at S-HT rises above 1.5 at s between 0.7 and 1.5): FAIL: it crosses at 0.398, i.e. the aggravation appears at a LOWER strength than predicted (the direction is right, the arm is about twice as sensitive in S-HT as predicted; at s = 3 the median rel_bursts is 2.67).** P3b (arm 9 at S-KO stays above 0.7 for s <= 1): PASS (crossing at 1.898). P4a, P4b, P4c (S-HT crossing smaller than S-KO for arms 6, 7, 8): PASS (0.445 < 1.711; 0.258 < 0.539; 0.445 < 1.102).
## What it says, and what not (model steps, not doses)
In this model the S-HT setting is more sensitive than S-KO for every suppressive arm (the crossing strength is 2 to 4 times smaller), and the single aggravating arm (sodium with an interneuron share) aggravates at S-HT at a fraction of the strength needed to suppress at S-KO: the near-threshold setting is where a mixed-component arm would show a rise. Several S-HT cells have a far-end median of 0.0 (the burst count falls to zero at s = 3), and S-HT baselines have about 10 bursts per 40 slices: read the S-HT crossings with the incidence fields and with the per-seed table, not as sharp numbers (5 seeds, median). Not shown: that any pilot arm reaches these strengths at any concentration; that the mapping of a drug class to a parameter is right (SCI's labelling, an assumption); that the model is right.
