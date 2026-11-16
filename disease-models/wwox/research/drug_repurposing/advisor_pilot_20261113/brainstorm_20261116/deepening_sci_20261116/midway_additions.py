#!/usr/bin/env python3
"""If the S-HT sIPSC sits midway between S-KO and controls (lam 0.5), which additional graded component brings the S-HT incidence into the binomial window? Hypothesis generator,
not evidence. Predictions in DECISION_RULES_SHT_SIPSC_FROZEN_BEFORE_HE_READS.md.
    python3 midway_additions.py --help
    python3 midway_additions.py run <out_tsv> [--slices 100]
Imports the frozen rebound_oscillator.py unchanged. numpy only; seeded."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=100); ap.add_argument("--seed", type=int, default=20261121); ap.add_argument("--T", type=float, default=600.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); sets = []; lab = []
    adds = [("none", 0.0)] + [("tonic", t) for t in (0.2, 0.4, 0.6)] + [("chloride", t) for t in (0.1, 0.2, 0.3)]
    for s in (0.05, 0.10):
        for comp, t in adds:
            for g, lam in (("S-KO", 0.0), ("S-HT", 0.5), ("S-WT", 1.0)):
                for _ in range(a.slices):
                    P = dict(m.BASE); z = np.exp(rng.normal(0, s, 4))
                    P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lam) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - 0.06 * lam) * z[1]
                    P["J_N"] = m.BASE["J_N"] * (1 - 0.06 * lam) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]
                    P["J_I"] = m.BASE["J_I"] * (1 + 1.08 * lam)       # phasic graded linearly; S-HT midway at lam 0.5
                    if comp == "tonic": P["J_tonic"] *= (1 + t * lam)
                    elif comp == "chloride": P["c0"] = m.BASE["c0"] * (1 - t * lam)
                    sets.append(P); lab.append((s, comp, t, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1)
    nb = np.array([sum(1 for d in r[1] if d > 0.1) for r in res]); out = {}
    for l, n in zip(lab, nb): out.setdefault(l, []).append(n)
    with open(a.out, "w") as f:
        f.write("sigma_slice\tadded_component\tt\tgenotype\tincidence\n")
        for l, v in out.items(): f.write(f"{l[0]}\t{l[1]}\t{l[2]}\t{l[3]}\t{np.mean(np.array(v) >= 1):.2f}\n")
    print(open(a.out).read()); return 0
if __name__ == "__main__":
    sys.exit(main())
