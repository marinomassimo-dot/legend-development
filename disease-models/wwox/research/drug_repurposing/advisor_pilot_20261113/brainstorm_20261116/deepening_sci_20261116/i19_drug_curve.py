#!/usr/bin/env python3
"""I19 drug-effect curve across the S-KO / S-HT / S-WT settings with held sizes (hypothesis generator, not evidence). Predictions: PREDICTIONS_I19_CURVE_FROZEN_BEFORE_RUN.md.
    python3 i19_drug_curve.py --help
    python3 i19_drug_curve.py run <out_tsv> [--slices 80]
Imports the frozen rebound_oscillator.py (same folder) unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
ARMS = {"none": {}, "A1_tonic_x1.2": {"J_tonic": 1.2}, "A2_Ttype_x0.75": {"J_T": 0.75}, "A3_NMDAR_x0.9": {"J_N": 0.9}, "A4_noise_x0.9": {"sigma": 0.9},
        "A5_Ttype_x1.25": {"J_T": 1.25}, "A6_resource_x0.6": {"kappa_r": 0.6}}
GENO = {"S-KO": (0.0, 0.0, 0.0), "S-HT": (0.69, 0.92, 0.9), "S-HT_phasic0.7": (0.69, 0.92, 0.7), "S-WT": (1.0, 1.0, 1.0)}
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=80); ap.add_argument("--seed", type=int, default=20261124); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); sets = []; lab = []
    for arm, ch in ARMS.items():
        for g, (lt, le, li) in GENO.items():
            for _ in range(a.slices):
                P = dict(m.BASE); z = np.exp(rng.normal(0, 0.07, 4))
                P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lt) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - 0.10 * le) * z[1]
                P["J_N"] = m.BASE["J_N"] * (1 - 0.10 * le) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]
                P["J_I"] = m.BASE["J_I"] * (1 + 1.08 * li)
                for k, f in ch.items(): P[k] *= f
                sets.append(P); lab.append((arm, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1); out = {}
    for l, r in zip(lab, res): out.setdefault(l, []).append(r)
    with open(a.out, "w") as f:
        f.write("arm\tgenotype\tincidence\tmean_bursts_in_bursting_slices\tmedian_duration_s\n")
        for l, rs in out.items():
            n = [sum(1 for d in r[1] if d > 0.1) for r in rs]; durs = [d for r in rs for d in r[1] if d > 0.1]
            bs = [x for x in n if x >= 1]
            f.write(f"{l[0]}\t{l[1]}\t{np.mean(np.array(n) >= 1):.2f}\t{np.mean(bs) if bs else float('nan'):.1f}\t{np.median(durs) if durs else float('nan'):.3f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
