#!/usr/bin/env python3
"""I16: graded astroglial K+ clearance on the S-KO / S-HT / S-WT genotype axis in the oscillator with an extracellular K+ variable (rebound_oscillator_k.py). Hypothesis
generator, not evidence. Predictions frozen first: PREDICTIONS_I16_FROZEN_BEFORE_RUN.md.
    python3 i16_k_buffering_test.py --help
    python3 i16_k_buffering_test.py run <out_tsv> [--slices 100]"""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator_k as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=100); ap.add_argument("--seed", type=int, default=20261119); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); s = 0.07
    sets = []; lab = []
    for t in (1, 3, 9, 19):
        for g, lam in (("S-KO", 0.0), ("S-HT", 0.5), ("S-WT", 1.0)):
            for _ in range(a.slices):
                P = dict(m.BASE); z = np.exp(rng.normal(0, s, 4))
                P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lam) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - 0.2 * lam) * z[1]
                P["J_N"] = m.BASE["J_N"] * (1 - 0.2 * lam) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]
                P["g_glia"] = 1 + t * lam
                sets.append(P); lab.append((t, g))
    # one-parameter look: g_glia only, no other change
    for gg in (0.5, 1.0, 2.0, 4.0):
        for _ in range(a.slices):
            P = dict(m.BASE); P["g_glia"] = gg; sets.append(P); lab.append((f"g{gg}", "only"))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1)
    out = {}
    for l, r in zip(lab, res): out.setdefault(l, []).append(r)
    with open(a.out, "w") as f:
        f.write("t_or_g\tgenotype\tincidence\tmedian_interval_s\tmedian_duration_s\n")
        for l, rs in out.items():
            inc = np.mean([sum(1 for d in r[1] if d > 0.1) >= 1 for r in rs])
            ints = [x for r in rs for x in np.diff([o for o, d in zip(r[0], r[1]) if d > 0.1])]
            durs = [d for r in rs for d in r[1] if d > 0.1]
            f.write(f"{l[0]}\t{l[1]}\t{inc:.2f}\t{np.median(ints) if ints else float('nan'):.1f}\t{np.median(durs) if durs else float('nan'):.3f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
