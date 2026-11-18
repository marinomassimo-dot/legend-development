#!/usr/bin/env python3
"""S-HT held-data test: can the fitted network reproduce graded burst incidence (S-WT 0/11, S-HT 4/23, S-KO 36/42 slices) from graded features while the intrinsic step
features stay at the knockout value?  Hypothesis generator, not evidence.  Predictions: PREDICTIONS_HET_FROZEN_BEFORE_RUN.md (frozen before the run).
    python3 het_incidence_test.py --help
    python3 het_incidence_test.py run <out_tsv> [--slices 100] [--seed S]
Imports the frozen rebound_oscillator.py unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=100); ap.add_argument("--seed", type=int, default=20261116); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed)
    combos = [(s, e, t) for s in (0.05, 0.10) for e in (0.1, 0.2, 0.3) for t in (0.0, 0.3, 0.6, 1.3)]
    geno = {"S-KO": 0.0, "S-HT": 0.5, "S-WT": 1.0}
    sets = []; lab = []
    for (s, e, t) in combos:
        for g, lam in geno.items():
            for _ in range(a.slices):
                P = dict(m.BASE)
                z = np.exp(rng.normal(0, s, 4))
                P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lam) * z[0]
                P["J_A"] = m.BASE["J_A"] * (1 - e * lam) * z[1]
                P["J_N"] = m.BASE["J_N"] * (1 - e * lam) * z[2]
                P["J_tonic"] = m.BASE["J_tonic"] * (1 + t * lam) * z[3]
                sets.append(P); lab.append((s, e, t, g))
    keys = list(m.BASE)
    P = {k: np.array([x[k] for x in sets], float) for k in keys}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1)
    nb = np.array([sum(1 for d in r[1] if d > 0.1) for r in res])
    out = {}
    for l, n in zip(lab, nb):
        out.setdefault(l, []).append(n)
    with open(a.out, "w") as f:
        f.write("sigma_slice\te_mEPSC_fraction\tt_tonic_fraction\tgenotype\tincidence\tmedian_bursts_in_600s\n")
        for l, v in out.items():
            v = np.array(v); f.write(f"{l[0]}\t{l[1]}\t{l[2]}\t{l[3]}\t{np.mean(v >= 1):.2f}\t{np.median(v):.1f}\n")
    print(open(a.out).read())
    return 0
if __name__ == "__main__":
    sys.exit(main())
