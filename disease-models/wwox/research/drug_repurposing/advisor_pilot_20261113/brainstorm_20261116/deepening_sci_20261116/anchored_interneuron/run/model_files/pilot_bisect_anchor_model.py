#!/usr/bin/env python3
"""ANCHORED variant (SCI, 2026-11-17) of the pilot-bisection adapter: arms 91 to 94 replace the assumed J_I x0.7 of arm 9 by a factor derived from Breton 2021 Table 1 (see PREDICTIONS_ANCHORED_INTERNEURON_FROZEN_BEFORE_RUN.md). Arms 1 to 9 are unchanged.
Adapter for HE's harness: strength of each pilot arm at which the burst count crosses a threshold, per genotype setting (hypothesis generator, not evidence).
numpy only; imports the frozen rebound_oscillator.py from its own folder. PARAMS = {name: [default, low, high, note]}; simulate(params, seed) -> dict of floats.
geno: 0 S-KO, 1 S-HT (rebound f 0.69, excitatory 0.92, phasic 0.9: the last ASSUMED), 2 S-WT (all 1.0).
arm: 1 d-APV (J_N x0.3), 2 NMDAR pore blocker (J_N x0.8), 3 GluN2B NAM (J_N x0.95 and tau_N x0.9), 4 AMPA (J_A x0.8), 5 T-type (J_T x0.75), 6 synaptic GABA-A (J_I x1.2),
7 neurosteroid-type (J_tonic x1.2 and J_I x1.1), 8 sodium, pyramidal (sigma x0.9), 9 sodium with interneuron share (sigma x0.9 and J_I x0.7).
strength s scales each arm's log-multiplier: factor = multiplier ** s (s = 0 no arm, s = 1 the arm as listed, s up to 3 an arm three times as strong in log terms).
Each call simulates NSL slices of 600 s TWICE with the same random draws (without the arm and with it) and returns rel_bursts = bursts with arm / bursts without arm, the arm's
median duration over the baseline's, and the baseline and arm incidences. Weights, not concentrations."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m
PARAMS = {"geno": [0, 0, 2, "0 S-KO, 1 S-HT, 2 S-WT"], "arm": [1, 1, 94, "pilot arm code 1 to 9, or 91 to 94 (anchored interneuron share, see module doc)"], "strength": [1.0, 0.0, 3.0, "arm strength s (multiplier ** s)"]}
GENO = {0: (0.0, 0.0, 0.0), 1: (0.69, 0.92, 0.9), 2: (1.0, 1.0, 1.0)}
ARM = {1: {"J_N": 0.3}, 2: {"J_N": 0.8}, 3: {"J_N": 0.95, "tau_N": 0.9}, 4: {"J_A": 0.8}, 5: {"J_T": 0.75}, 6: {"J_I": 1.2}, 7: {"J_tonic": 1.2, "J_I": 1.1}, 8: {"sigma": 0.9}, 9: {"sigma": 0.9, "J_I": 0.7},
       91: {"sigma": 0.9, "J_I": 0.90}, 92: {"sigma": 0.9, "J_I": 0.80}, 93: {"sigma": 0.9, "J_I": 0.74}, 94: {"sigma": 0.9, "J_I": 0.48}}   # J_I factor = 1 - k*r*0.10 with (r,k) = (1,1), (1,2), (2.6,1), (2.6,2)
NSL, T_SIM = 40, 600.0
def _batch(g, arm, s, seed):
    lt, le, li = GENO[g]; rng = np.random.default_rng(int(seed)); sets = []
    for _ in range(NSL):
        P = dict(m.BASE); z = np.exp(rng.normal(0, 0.07, 4))
        P["J_T"] = m.BASE["J_T"] * (1 - 0.48 * lt) * z[0]; P["J_A"] = m.BASE["J_A"] * (1 - 0.10 * le) * z[1]
        P["J_N"] = m.BASE["J_N"] * (1 - 0.10 * le) * z[2]; P["J_tonic"] = m.BASE["J_tonic"] * z[3]; P["J_I"] = m.BASE["J_I"] * (1 + 1.08 * li)
        for k, f in ARM[arm].items(): P[k] *= f ** s
        sets.append(P)
    return {k: np.array([x[k] for x in sets], float) for k in m.BASE}
def _stats(res):
    n = np.array([sum(1 for d in r[1] if d > 0.1) for r in res]); durs = [d for r in res for d in r[1] if d > 0.1]
    return float(n.sum()), float(np.mean(n >= 1)), float(np.median(durs)) if durs else float("nan")
def simulate(params, seed):
    g = int(round(float(params.get("geno", 0)))); arm = int(round(float(params.get("arm", 1)))); s = float(params.get("strength", 1.0))
    r0 = m.simulate(_batch(g, arm, 0.0, seed), T_SIM, int(seed) + 1, nrep=1); r1 = m.simulate(_batch(g, arm, s, seed), T_SIM, int(seed) + 1, nrep=1)
    b0, i0, d0 = _stats(r0); b1, i1, d1 = _stats(r1)
    return dict(rel_bursts=(b1 / b0) if b0 > 0 else float("nan"), rel_duration=(d1 / d0) if (d0 == d0 and d1 == d1 and d0 > 0) else float("nan"),
                incidence_baseline=i0, incidence_arm=i1, n_bursts_baseline=b0, n_bursts_arm=b1)
if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--seed", type=int, default=1); ap.add_argument("--geno", type=int, default=0); ap.add_argument("--arm", type=int, default=1)
    ap.add_argument("--strength", type=float, default=1.0); a = ap.parse_args(); print(simulate({"geno": a.geno, "arm": a.arm, "strength": a.strength}, a.seed))
