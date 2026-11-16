#!/usr/bin/env python3
"""S-HT incidence with the held sizes of sIPSC and sEPSC differences (see PREDICTIONS_HELD_SIZES_FROZEN_BEFORE_RUN.md). Hypothesis generator, not evidence.
    python3 het_held_sizes_test.py --help
    python3 het_held_sizes_test.py run <out_tsv> [--slices 100]
Imports the frozen rebound_oscillator.py unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=100); ap.add_argument("--seed", type=int, default=20261120); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); sets = []; lab = []
    for s in (0.05, 0.10):
        for e in (0.06, 0.10, 0.20):
            for t in (1.08, 1.5):
                for g, lam in (("S-KO", 0.0), ("S-HT05", 0.5), ("S-HT09", 0.9), ("S-WT", 1.0)):
                    for _ in range(a.slices):
                        P = dict(m.BASE); z = np.exp(rng.normal(0, s, 4))
                        P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lam) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - e * lam) * z[1]
                        P["J_N"] = m.BASE["J_N"] * (1 - e * lam) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]
                        P["J_I"] = m.BASE["J_I"] * (1 + t * lam)
                        sets.append(P); lab.append((s, e, t, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1)
    nb = np.array([sum(1 for d in r[1] if d > 0.1) for r in res]); out = {}
    for l, n in zip(lab, nb): out.setdefault(l, []).append(n)
    with open(a.out, "w") as f:
        f.write("sigma_slice\te_sEPSC\tt_phasic\tgenotype\tincidence\n")
        for l, v in out.items(): f.write(f"{l[0]}\t{l[1]}\t{l[2]}\t{l[3]}\t{np.mean(np.array(v) >= 1):.2f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
