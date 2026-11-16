#!/usr/bin/env python3
"""Expected sign and size per pilot arm in the frozen oscillator at S-KO, S-HT, S-WT (held sizes). Hypothesis generator, not evidence. Predictions: PREDICTIONS_PILOT_ARMS_FROZEN_BEFORE_RUN.md.
    python3 pilot_arms_table.py --help
    python3 pilot_arms_table.py run <out_tsv> [--slices 80]
Imports the frozen rebound_oscillator.py (same folder) unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
ARMS = {"0_none": {}, "1_dAPV": {"J_N": 0.3}, "2_NMDAR_pore_x0.8": {"J_N": 0.8}, "3_GluN2B_NAM": {"J_N": 0.95, "tau_N": 0.9}, "4_AMPA_x0.8": {"J_A": 0.8}, "5_Ttype_x0.75": {"J_T": 0.75},
        "6_phasic_x1.2": {"J_I": 1.2}, "7_neurosteroid": {"J_tonic": 1.2, "J_I": 1.1}, "8_Na_pyramidal": {"sigma": 0.9}, "9_Na_with_interneuron": {"sigma": 0.9, "J_I": 0.7}}
GENO = {"S-KO": (0.0, 0.0, 0.0), "S-HT": (0.69, 0.92, 0.9), "S-WT": (1.0, 1.0, 1.0)}
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=80); ap.add_argument("--seed", type=int, default=20261125); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); sets = []; lab = []
    for arm, ch in ARMS.items():
        for g, (lt, le, li) in GENO.items():
            for _ in range(a.slices):
                P = dict(m.BASE); z = np.exp(rng.normal(0, 0.07, 4))
                P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lt) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - 0.10 * le) * z[1]
                P["J_N"] = m.BASE["J_N"] * (1 - 0.10 * le) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]; P["J_I"] = m.BASE["J_I"] * (1 + 1.08 * li)
                for k, f in ch.items(): P[k] *= f
                sets.append(P); lab.append((arm, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1); out = {}
    for l, r in zip(lab, res): out.setdefault(l, []).append(r)
    with open(a.out, "w") as f:
        f.write("arm\tgenotype\tincidence\tmean_bursts_in_bursting_slices\tmedian_duration_s\n")
        for l, rs in out.items():
            n = [sum(1 for d in r[1] if d > 0.1) for r in rs]; durs = [d for r in rs for d in r[1] if d > 0.1]; bs = [x for x in n if x >= 1]
            f.write(f"{l[0]}\t{l[1]}\t{np.mean(np.array(n) >= 1):.2f}\t{np.mean(bs) if bs else float('nan'):.1f}\t{np.median(durs) if durs else float('nan'):.3f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
