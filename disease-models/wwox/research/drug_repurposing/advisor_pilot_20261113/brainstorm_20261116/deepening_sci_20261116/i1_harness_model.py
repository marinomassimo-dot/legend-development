#!/usr/bin/env python3
"""Adapter exposing rebound_oscillator.py (I1, hypothesis generator, not evidence) through the interface HE's harness expects:
PARAMS = {name: [default, low, high, note]} and simulate(params, seed) -> dict of plain floats. numpy only, no network.
The adapter imports rebound_oscillator.py from its own folder; copy both files together to freeze them."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m

NOTE = {"J_N": "NMDAR recurrent weight (sustainer)", "J_T": "T-type-like rebound weight (trigger)", "J_a": "adenosine A1 weight",
        "J_I": "phasic GABA-A weight", "J_tonic": "tonic GABA-A weight", "tau_c": "KCC2 extrusion time constant s", "tau_a": "adenosine clearance s",
        "tau_h": "T-type-like recovery s", "tau_r": "resource recovery s", "pam": "GABA-A positive modulation (relative, mechanism level)",
        "brake": "presynaptic brake on recurrent excitation (NPY-like), 0 to 1", "hcn_block": "HCN blockade fraction 0 to 1",
        "tonic_gaba": "tonic GABA level multiplier", "c0": "resting chloride mM"}
PARAMS = {}
for k, v in m.BASE.items():
    lo, hi = (v * 0.5, v * 1.5) if v > 0 else ((v * 1.5, v * 0.5) if v < 0 else (0.0, 1.0))
    if k in ("pam", "brake", "hcn_block"):
        lo, hi = 0.0, 1.0 if k != "pam" else 2.0
    PARAMS[k] = [float(v), float(lo), float(hi), NOTE.get(k, "ASSUMED, see rebound_oscillator.py")]
T_SIM, NREP = 600.0, 8

def simulate(params, seed):
    P = {k: float(params.get(k, PARAMS[k][0])) for k in PARAMS}
    row = m.stats(P, T_SIM, int(seed), NREP)[0]
    f = lambda x: float(x)
    return dict(isi_median_s=f(row["int_med"]), isi_gamma_shape=f(row["int_shape"]), dur_median_s=f(row["dur_med"]),
                dur_gamma_shape=f(row["dur_shape"]), n_bursts=f(row["n_bursts"]), rate_per_min=f(row["rate_per_min"]),
                isi_q1_s=f(row["int_q1"]), isi_q3_s=f(row["int_q3"]), dur_q1_s=f(row["dur_q1"]), dur_q3_s=f(row["dur_q3"]))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--seed", type=int, default=1); a = ap.parse_args()
    print(simulate({}, a.seed))
