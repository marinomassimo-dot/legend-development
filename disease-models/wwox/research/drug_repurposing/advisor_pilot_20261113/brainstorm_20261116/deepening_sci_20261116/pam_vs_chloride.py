#!/usr/bin/env python3
"""Sign of GABA-A potentiation against steady chloride in the frozen oscillator (hypothesis generator, not evidence). Predictions: PREDICTIONS_PAM_VS_CHLORIDE_FROZEN_BEFORE_RUN.md.
    python3 pam_vs_chloride.py --help
    python3 pam_vs_chloride.py run <out_tsv> [--nets 40]"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--nets", type=int, default=40); ap.add_argument("--seed", type=int, default=20261123); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    cs = [6, 9, 11, 12, 13, 14]; sets = []; lab = []
    for c0 in cs:
        for pam in (0.0, 0.3):
            for _ in range(a.nets):
                P = dict(m.BASE); P["c0"] = float(c0); P["pam"] = pam; sets.append(P); lab.append((c0, pam))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed, nrep=1); out = {}
    for l, r in zip(lab, res): out.setdefault(l, []).append(sum(1 for d in r[1] if d > 0.1))
    with open(a.out, "w") as f:
        f.write("c0_mM\tpam\tmean_bursts_per_600s\tratio_pam03_over_pam0\n")
        for c0 in cs:
            r0 = np.mean(out[(c0, 0.0)]); r3 = np.mean(out[(c0, 0.3)])
            f.write(f"{c0}\t0.0\t{r0:.1f}\t\n{c0}\t0.3\t{r3:.1f}\t{(r3 / r0 if r0 > 0 else float('nan')):.2f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
