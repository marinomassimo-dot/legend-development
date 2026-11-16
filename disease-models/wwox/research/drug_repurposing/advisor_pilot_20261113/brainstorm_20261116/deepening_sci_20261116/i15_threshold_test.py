#!/usr/bin/env python3
"""I15 distance to threshold in the frozen oscillator: the resting-drive increment dx (K+ challenge) or the NMDAR multiplier m (Mg2+ challenge) at which 50% of slices burst,
per genotype and per graded component. Hypothesis generator, not evidence. Predictions frozen first: PREDICTIONS_I15_FROZEN_BEFORE_RUN.md.
    python3 i15_threshold_test.py --help
    python3 i15_threshold_test.py run <out_tsv> [--slices 60] [--seed S]
Imports the frozen rebound_oscillator.py (same folder) unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
DX = [0.0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.13, 0.16]
MM = [1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
VARIANTS = {"tonic": ("J_tonic", 0.8), "chloride": ("c0", 0.3), "phasic": ("J_I", 2.0), "nmda_step": ("J_N_extra", 0.4)}
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=60); ap.add_argument("--seed", type=int, default=20261118); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); s = 0.07
    sets = []; lab = []
    for var, (comp, t) in VARIANTS.items():
        for axis, grid in (("K", DX), ("Mg", MM)):
            for v in grid:
                for g, lam in (("S-KO", 0.0), ("S-HT", 0.5), ("S-WT", 1.0)):
                    for _ in range(a.slices):
                        P = dict(m.BASE); z = np.exp(rng.normal(0, s, 4))
                        P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lam) * z[0]
                        P["J_A"] = m.BASE["J_A"] * (1 - 0.2 * lam) * z[1]
                        P["J_N"] = m.BASE["J_N"] * (1 - 0.2 * lam) * z[2]
                        P["J_tonic"] = m.BASE["J_tonic"] * z[3]
                        if comp == "J_tonic": P["J_tonic"] *= (1 + t * lam)
                        elif comp == "c0": P["c0"] = m.BASE["c0"] * (1 - t * lam)
                        elif comp == "J_I": P["J_I"] = m.BASE["J_I"] * (1 + t * lam)
                        else: P["J_N"] *= (1 - t * lam)
                        if axis == "K": P["b0"] = m.BASE["b0"] + v
                        else: P["J_N"] *= v
                        sets.append(P); lab.append((var, axis, v, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1)
    nb = np.array([sum(1 for d in r[1] if d > 0.1) for r in res])
    out = {}
    for l, n in zip(lab, nb): out.setdefault(l, []).append(n)
    inc = {l: float(np.mean(np.array(v) >= 1)) for l, v in out.items()}
    with open(a.out, "w") as f:
        f.write("variant\taxis\tvalue\tgenotype\tincidence\n")
        for l, v in inc.items(): f.write(f"{l[0]}\t{l[1]}\t{l[2]}\t{l[3]}\t{v:.2f}\n")
    # 50% crossing by linear interpolation
    rows = []
    for var in VARIANTS:
        for axis, grid in (("K", DX), ("Mg", MM)):
            for g in ("S-KO", "S-HT", "S-WT"):
                y = [inc[(var, axis, v, g)] for v in grid]; cross = None
                if y[0] >= 0.5: cross = grid[0]
                else:
                    for i in range(1, len(grid)):
                        if y[i] >= 0.5 > y[i - 1]:
                            cross = grid[i - 1] + (0.5 - y[i - 1]) / (y[i] - y[i - 1]) * (grid[i] - grid[i - 1]); break
                rows.append((var, axis, g, cross))
    with open(a.out.replace(".tsv", "_threshold50.tsv"), "w") as f:
        f.write("variant\taxis\tgenotype\tthreshold50\n")
        for r in rows: f.write(f"{r[0]}\t{r[1]}\t{r[2]}\t{'none_in_scan' if r[3] is None else f'{r[3]:.3f}'}\n")
    print(open(a.out.replace(".tsv", "_threshold50.tsv")).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
