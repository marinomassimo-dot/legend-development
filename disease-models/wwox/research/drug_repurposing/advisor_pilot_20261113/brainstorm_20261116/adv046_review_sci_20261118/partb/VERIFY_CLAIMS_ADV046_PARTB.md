# Claims to verify against the result files (blind: you get these claims and the files, nothing else)

Files (same folder): `part1_seedA.json`, `part1_seedB.json` (steady-state grid; fields `ratio_ctrl` = burst count ratio to the control set d=0,hcn=0,e=0; `ratio_vs_C0_same_depth` and its CI; kinds C0 = J_N scaling only, C1 = plus Ih knob `hcn`, C2 = plus phasic-inhibition rule with coupling `e`), `part2_cells.json` (time course; per cell, per window W1 = 0 to 30 min, W2 = 30 to 60, W3 = 60 to 120 min after the start of washout: `rate_over_pre` and `E`), `decision.json`, `score.json`, the script `adv046_b_compare.py` and the held reference `../../deepening_sci_20261116/homeostat_toy_cells.json` (cell `c_3600_1800`). All numbers below are rounded.

For each claim answer SUPPORTED / PARTLY (say what differs) / NOT SUPPORTED, quoting the file and field you used. Recompute from the JSON; do not trust `decision.json` without checking it against the other files.

C1. C0 control ratio falls monotonically with depth d = 0.05, 0.10, 0.15, 0.20, 0.30, 0.50: seed A 0.79, 0.65, 0.55, 0.42, 0.24, 0.05; seed B 0.86, 0.71, 0.52, 0.44, 0.26, 0.07. It crosses 0.5 between d = 0.15 and 0.20 on both seeds.
C2. Against the C0 cell at the same depth, C1 cells (Ih knob) have ratio below 1 at every depth 0.05 to 0.30 on both seeds: hcn = 0.1 between about 0.69 and 0.86; hcn = 0.2 between about 0.45 and 0.67; hcn = 0.4 between about 0.23 and 0.42. At d = 0.5 the C1 cells have control ratio at most 0.07 (floor).
C3. For the C2 cells (disinhibition rule): at e = 2 the control ratio never reaches 1.2 at d up to 0.30 (maximum about 1.12); at e = 4 it is 1.20 (seed A) and 1.18 (seed B) at d = 0.05, and peaks near 1.9 to 2.0 at d = 0.30; at e = 8 the peak is about 2.2 to 2.3 at d = 0.15; at e = 16 about 2.3 to 2.4 at d = 0.10.
C4. At d = 0.5 the C2 cells have control ratio between 1.22 and 1.35 on both seeds (not at floor), while the C0 cell has 0.05 (A) and 0.07 (B).
C5. In part 2, cell K2_3600 reproduces the held toy cell c_3600_1800 exactly: EARLY 2.5 and MID 1.9141 (same a0 and PRE rate).
C6. Slow-unblock cells without gain (K1): W2 rate over PRE 1.03, 0.80, 0.42, 0.15 for tau_off 10, 20, 40, 80 min, with E 0.99, 0.92, 0.77, 0.60. In every K1 cell-and-window whose rate over PRE is below 0.7, E is below 0.9.
C7. Across K1 cell-windows with rate below 0.95, the ratio ln(rate)/ln(E) lies between about 2.5 and 3.6.
C8. Gain-only cells (K2_3600, K2_1800): W1 rate about 1.61 and 1.52 (E about 1.08), W2 1.07 and 1.05, W3 1.07 and 1.08: no window after the first 30 minutes is above 1.3.
C9. Combined cells (K3): W2 rate 1.44 (K3_3600_20), 1.60 (K3_3600_40), 1.24 (K3_1800_20) with E 1.02, 0.96, 0.99. In K3_3600_40 W1 the rate is 1.04 with E 0.69, while K1_40 W1 is 0.07 and K2_3600 W1 is 1.61.
C10. The frozen decision rule gives verdict PARTLY (INF1 true on both seeds, INF2 false), and the log score of the 13 statements is -9.81 against -9.01 for coin flips (statement probabilities and outcomes are in `score.json`; the probabilities are in the preregistration, which you do not have: check only the arithmetic from `score.json`).
Also report anything in `adv046_b_compare.py` that would make a number above differ from what its own definitions say (for example a window or normalisation inconsistent with the claims' wording).
