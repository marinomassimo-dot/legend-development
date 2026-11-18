#!/usr/bin/env python3
"""Adapter for HE's harness: I19 drug-effect curve at three genotype settings and eight arms (hypothesis generator, not evidence). numpy only; imports the frozen
rebound_oscillator.py from its own folder. PARAMS = {name: [default, low, high, note]}; simulate(params, seed) -> dict of floats.
geno: 0 S-KO, 1 S-HT (held positions: rebound f 0.69, excitatory f 0.92, phasic 0.9 ASSUMED), 2 S-WT. arm: 0 none, 1 tonic x1.2, 2 T-type x0.75, 3 NMDAR x0.9,
4 noise x0.9, 5 T-type x1.25, 6 resource depletion x0.6, 7 phasic x1.2. Each call simulates 40 slices of 600 s (sigma 0.07); incidence = fraction with >= 1 burst."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
PARAMS = {"geno": [1, 0, 2, "0 S-KO, 1 S-HT, 2 S-WT (held positions of rebound, excitatory amplitude, phasic inhibition)"],
          "arm": [0, 0, 7, "0 none, 1 tonic x1.2, 2 T-type x0.75, 3 NMDAR x0.9, 4 noise x0.9, 5 T-type x1.25, 6 resource x0.6, 7 phasic x1.2"]}
GENO = {0: (0.0, 0.0, 0.0), 1: (0.69, 0.92, 0.9), 2: (1.0, 1.0, 1.0)}
ARM = {0: {}, 1: {"J_tonic": 1.2}, 2: {"J_T": 0.75}, 3: {"J_N": 0.9}, 4: {"sigma": 0.9}, 5: {"J_T": 1.25}, 6: {"kappa_r": 0.6}, 7: {"J_I": 1.2}}
NSL, T_SIM = 40, 600.0
def simulate(params, seed):
    g = int(round(float(params.get("geno", PARAMS["geno"][0])))); a = int(round(float(params.get("arm", PARAMS["arm"][0]))))
    lt, le, li = GENO[g]; rng = np.random.default_rng(int(seed)); sets = []
    for _ in range(NSL):
        P = dict(m.BASE); z = np.exp(rng.normal(0, 0.07, 4))
        P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lt) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - 0.10 * le) * z[1]
        P["J_N"] = m.BASE["J_N"] * (1 - 0.10 * le) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]; P["J_I"] = m.BASE["J_I"] * (1 + 1.08 * li)
        for k, f in ARM[a].items(): P[k] *= f
        sets.append(P)
    P = {k: np.array([x[k] for x in sets], float) for k in m.BASE}
    res = m.simulate(P, T_SIM, int(seed) + 1, nrep=1)
    n = np.array([sum(1 for d in r[1] if d > 0.1) for r in res]); durs = [d for r in res for d in r[1] if d > 0.1]
    bs = n[n >= 1]
    return dict(incidence=float(np.mean(n >= 1)), n_bursts=float(n.sum()), mean_bursts_in_bursting_slices=float(bs.mean()) if len(bs) else float("nan"),
                dur_median_s=float(np.median(durs)) if durs else float("nan"))
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--seed", type=int, default=1); a = ap.parse_args(); print(simulate({}, a.seed))
