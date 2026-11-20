#!/usr/bin/env python3
"""PARAMETRIC SENSITIVITY adapter for the bisect study (HE, ADV-096, 2026-11-19; hypothesis generator, not evidence; not medical advice).

Wraps SCI's FROZEN bisect adapter (pilot_bisect_harness_model.py) and SCI's FROZEN rebound_oscillator.py, both imported unchanged from this adapter's own folder (frozen with it by
`sim_harness.py freeze --also`). Four parameter changes on the oscillator's own BASE parameters (no structural alternative: every variant is the same circuit structure with other parameter values) are applied for one call and restored after; at their defaults the call is the frozen adapter's, bit for bit.
**Kv7 is NOT in the model.** `kv7_offset` is a STAND-IN: an additive offset on the drive b0 (positive: more depolarised, as with a Kv7 blocker; negative: as with an opener). The sign and size are an
ASSUMPTION, not a current, and nothing here is evidence about Kv7. Chloride dynamics are in the model: `cl_tau_mult` scales tau_c (the extrusion time constant). `ji_mult` scales J_I (phasic
inhibition, the interneuron share of the drive), `nmda_mult` scales J_N (NMDAR gain). Weights, not concentrations. A class that keeps its rank across variants is
robust to THESE parameters only, not shown correct."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pilot_bisect_harness_model as base
import rebound_oscillator as m

PARAMS = dict(base.PARAMS)
PARAMS.update({"ji_mult": [1.0, 0.5, 1.5, "multiplier on J_I (phasic inhibition: interneuron share)"],
               "cl_tau_mult": [1.0, 0.5, 2.0, "multiplier on tau_c (chloride extrusion time constant)"],
               "nmda_mult": [1.0, 0.8, 1.25, "multiplier on J_N (NMDAR gain)"],
               "kv7_offset": [0.0, -0.05, 0.05, "ASSUMED stand-in for intrinsic Kv7 depolarisation: additive offset on the drive b0 (Kv7 is NOT in the model)"]})
EDIT = {"ji_mult": ("J_I", "*"), "cl_tau_mult": ("tau_c", "*"), "nmda_mult": ("J_N", "*"), "kv7_offset": ("b0", "+")}


def simulate(params, seed):
    saved = dict(m.BASE)
    try:
        for key, (name, op) in EDIT.items():
            v = float(params.get(key, PARAMS[key][0]))
            m.BASE[name] = saved[name] * v if op == "*" else saved[name] + v
        return base.simulate(params, seed)
    finally:
        m.BASE.clear()
        m.BASE.update(saved)
