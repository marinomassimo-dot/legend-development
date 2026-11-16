#!/usr/bin/env python3
"""S-HT incidence test with rival graded components (ADV's extension of het_incidence_test.py). Hypothesis generator, not evidence.
Predictions frozen first: PREDICTIONS_RIVALS_FROZEN_BEFORE_RUN.md.
    python3 het_rivals_test.py --help
    python3 het_rivals_test.py run <out_tsv> [--slices 100] [--seed S]
Imports the frozen rebound_oscillator.py (same folder) unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=100); ap.add_argument("--seed", type=int, default=20261117); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed)
    comps = {"J_I": [0.3, 0.6, 1.0, 1.5, 2.0], "J_N_extra": [0.1, 0.2, 0.3, 0.4], "c0": [0.1, 0.2, 0.3, 0.4]}
    sets = []; lab = []
    for comp, ts in comps.items():
        for s in (0.05, 0.10):
            for t in ts:
                for g, lam in (("S-KO", 0.0), ("S-HT", 0.5), ("S-HT09", 0.9), ("S-WT", 1.0)):
                    if g == "S-HT09" and comp != "J_I":
                        continue
                    for _ in range(a.slices):
                        P = dict(m.BASE); z = np.exp(rng.normal(0, s, 4))
                        P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lam) * z[0]
                        P["J_A"] = m.BASE["J_A"] * (1 - 0.2 * lam) * z[1]
                        P["J_N"] = m.BASE["J_N"] * (1 - 0.2 * lam) * z[2]
                        P["J_tonic"] = m.BASE["J_tonic"] * z[3]
                        if comp == "J_I": P["J_I"] = m.BASE["J_I"] * (1 + t * lam)
                        elif comp == "J_N_extra": P["J_N"] *= (1 - t * lam)
                        else: P["c0"] = m.BASE["c0"] * (1 - t * lam)
                        sets.append(P); lab.append((comp, s, t, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1)
    nb = np.array([sum(1 for d in r[1] if d > 0.1) for r in res])
    out = {}
    for l, n in zip(lab, nb): out.setdefault(l, []).append(n)
    with open(a.out, "w") as f:
        f.write("component\tsigma_slice\tt\tgenotype\tincidence\tmedian_bursts_in_600s\n")
        for l, v in out.items():
            v = np.array(v); f.write(f"{l[0]}\t{l[1]}\t{l[2]}\t{l[3]}\t{np.mean(v >= 1):.2f}\t{np.median(v):.1f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
