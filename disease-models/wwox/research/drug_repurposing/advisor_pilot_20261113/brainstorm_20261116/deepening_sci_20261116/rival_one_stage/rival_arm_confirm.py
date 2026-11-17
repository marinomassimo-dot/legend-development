#!/usr/bin/env python3
"""CONFIRMATION RUN (S-KO only, more slices): pilot arms in the two-stage oscillator and in its one-stage rival, same settings (S-KO, S-HT, S-WT with held sizes), same arms. Hypothesis generator, not evidence.
Predictions: PREDICTIONS_ONE_STAGE_RIVAL_FROZEN_BEFORE_FIT.md (hashed before the fit).
    python3 rival_arm_comparison.py --help
    python3 rival_arm_comparison.py run <rival_fit.json> <out_tsv> [--slices 60]
Imports the frozen rebound_oscillator.py unchanged. numpy only; seeded."""
import argparse, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # frozen rebound_oscillator.py lives in the parent folder
import numpy as np
import rebound_oscillator as m
ARMS = {"0_none": {}, "0b_none_replicate": {}, "5_Ttype_x0.75": {"J_T": 0.75}, "7_neurosteroid": {"J_tonic": 1.2, "J_I": 1.1}, "8_Na_pyramidal": {"sigma": 0.9}, "9_Na_with_interneuron": {"sigma": 0.9, "J_I": 0.7}, "10_resource_x0.6": {"kappa_r": 0.6}}
GENO = {"S-KO": (0.0, 0.0, 0.0)}
def run_model(name, B, a, rng):
    sets = []; lab = []
    for arm, ch in ARMS.items():
        for g, (lt, le, li) in GENO.items():
            for _ in range(a.slices):
                P = dict(B); z = np.exp(rng.normal(0, 0.07, 4))
                P["J_T"] = B["J_T"] * (1 - 0.48 * lt) * z[0]; P["J_A"] = B["J_A"] * (1 - 0.10 * le) * z[1]
                P["J_N"] = B["J_N"] * (1 - 0.10 * le) * z[2]; P["J_tonic"] = B["J_tonic"] * z[3]; P["J_I"] = B["J_I"] * (1 + 1.08 * li)
                for k, f in ch.items(): P[k] *= f
                sets.append(P); lab.append((name, arm, g))
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, a.T, a.seed + 1, nrep=1); out = {}
    for l, r in zip(lab, res): out.setdefault(l, []).append(r)
    rows = []
    for l, rs in out.items():
        n = [sum(1 for d in r[1] if d > 0.1) for r in rs]; durs = [d for r in rs for d in r[1] if d > 0.1]
        ints = [x for r in rs for x in np.diff([o for o, d in zip(r[0], r[1]) if d > 0.1])]; bs = [x for x in n if x >= 1]
        rows.append((*l, f"{np.mean(np.array(n) >= 1):.2f}", f"{np.mean(bs) if bs else float('nan'):.1f}", f"{np.median(durs) if durs else float('nan'):.3f}", f"{np.median(ints) if ints else float('nan'):.1f}"))
    return rows
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd"); ap.add_argument("fit"); ap.add_argument("out")
    ap.add_argument("--slices", type=int, default=200); ap.add_argument("--seed", type=int, default=20261127); ap.add_argument("--T", type=float, default=2000.0)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    rng = np.random.default_rng(a.seed); rb = dict(m.BASE); rb.update({"J_T": 0.0, "J_a": 0.0, "kappa_c": 0.0}); rb.update(json.load(open(a.fit))["params"])
    rows = run_model("two_stage", dict(m.BASE), a, rng) + run_model("one_stage", rb, a, rng)
    with open(a.out, "w") as f:
        f.write("model\tarm\tgenotype\tincidence\tbursts_per_bursting_slice\tmedian_duration_s\tmedian_interval_s\n")
        for r in rows: f.write("\t".join(r) + "\n")
    print(len(rows), "rows"); return 0
if __name__ == "__main__":
    sys.exit(main())
