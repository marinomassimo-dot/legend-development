#!/usr/bin/env python3
"""I1 class predictions: scan mechanism classes and one-at-a-time parameter changes on the fitted rebound oscillator (hypothesis generator, not evidence).
    python3 predict_classes.py --help
    python3 predict_classes.py run <out_dir> [--seed S] [--T 900] [--nrep 16]
Writes class_scan.tsv and oat_scan.tsv (rows = parameter set; columns = summary) plus results.sha256. numpy only; seeded."""
import argparse, hashlib, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import rebound_oscillator as m

CLASSES = [  # id, label, link acted on, list of (magnitude label, {param: ("mul"|"set", value)})
 ("C1", "T-type-like blockade", "trigger (J_T)", [("x0.75", {"J_T": ("mul", .75)}), ("x0.5", {"J_T": ("mul", .5)}), ("x0.25", {"J_T": ("mul", .25)})]),
 ("C2", "NMDAR-active, strong", "sustainer (J_N)", [("x0.95", {"J_N": ("mul", .95)}), ("x0.9", {"J_N": ("mul", .9)}), ("x0.85", {"J_N": ("mul", .85)})]),
 ("C3", "GABA-A positive modulation", "phasic+tonic GABA-A", [("pam0.3", {"pam": ("set", .3)}), ("pam0.6", {"pam": ("set", .6)}), ("pam1.0", {"pam": ("set", 1.0)})]),
 ("C4", "KCC2 enhancement", "chloride extrusion (tau_c)", [("x0.75", {"tau_c": ("mul", .75)}), ("x0.5", {"tau_c": ("mul", .5)}), ("x0.35", {"tau_c": ("mul", .35)})]),
 ("C5", "KCC2 inhibition / chloride loading", "chloride extrusion (tau_c)", [("x1.5", {"tau_c": ("mul", 1.5)}), ("x2", {"tau_c": ("mul", 2.0)}), ("x3", {"tau_c": ("mul", 3.0)})]),
 ("C6", "adenosine augmentation", "A1 weight (J_a)", [("x1.15", {"J_a": ("mul", 1.15)}), ("x1.3", {"J_a": ("mul", 1.3)}), ("x1.4", {"J_a": ("mul", 1.4)})]),
 ("C6b", "adenosine A1 antagonism", "A1 weight (J_a)", [("x0.8", {"J_a": ("mul", .8)}), ("x0.6", {"J_a": ("mul", .6)}), ("x0.4", {"J_a": ("mul", .4)})]),
 ("C7", "HCN blockade", "depolarising tonic share", [("0.3", {"hcn_block": ("set", .3)}), ("0.6", {"hcn_block": ("set", .6)}), ("1.0", {"hcn_block": ("set", 1.0)})]),
 ("C8", "presynaptic brake (NPY-like)", "recurrent excitation", [("0.03", {"brake": ("set", .03)}), ("0.06", {"brake": ("set", .06)}), ("0.10", {"brake": ("set", .10)})]),
 ("C8b", "brake removal (NPY-pathway blocker)", "recurrent excitation", [("-0.03", {"brake": ("set", -.03)}), ("-0.06", {"brake": ("set", -.06)}), ("-0.10", {"brake": ("set", -.10)})]),
 ("C9", "persistent-sodium-type reduction", "noise-driven ignition (sigma)", [("x0.9", {"sigma": ("mul", .9)}), ("x0.8", {"sigma": ("mul", .8)}), ("x0.7", {"sigma": ("mul", .7)})]),
 ("C10", "tonic GABA increase only", "tonic GABA-A", [("x1.2", {"tonic_gaba": ("set", 1.2)}), ("x1.5", {"tonic_gaba": ("set", 1.5)}), ("x2", {"tonic_gaba": ("set", 2.0)})]),
 ("C11", "metabolic: slower resource depletion", "resource (kappa_r)", [("x0.8", {"kappa_r": ("mul", .8)}), ("x0.6", {"kappa_r": ("mul", .6)}), ("x0.4", {"kappa_r": ("mul", .4)})]),
]
OAT = ["J_T", "J_N", "J_A", "J_I", "J_a", "J_tonic", "tau_c", "tau_a", "tau_h", "tau_r", "tau_N", "kappa_r", "kappa_c", "kappa_a", "b0", "sigma"]
OATMUL = [0.6, 0.8, 0.9, 1.1, 1.2, 1.4]
COLS = ["rate_per_min", "n_bursts", "int_q1", "int_med", "int_q3", "int_shape", "dur_q1", "dur_med", "dur_q3", "dur_shape"]

def build(changes):
    P = dict(m.BASE)
    for k, (op, v) in changes.items():
        P[k] = P[k] * v if op == "mul" else v
    return P

def run_sets(sets, T, seed, nrep):
    keys = list(m.BASE)
    P = {k: np.array([s[k] for s in sets], float) for k in keys}
    return m.stats(P, T, seed, nrep)

def fmt(x):
    return "NA" if x is None or (isinstance(x, float) and not np.isfinite(x)) else (f"{x:.3f}" if isinstance(x, float) else str(x))

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("cmd"); ap.add_argument("out_dir"); ap.add_argument("--seed", type=int, default=20261116)
    ap.add_argument("--T", type=float, default=900.0); ap.add_argument("--nrep", type=int, default=16)
    a = ap.parse_args(argv)
    if a.cmd != "run":
        print(__doc__); return 0
    os.makedirs(a.out_dir, exist_ok=True)
    sets = [dict(m.BASE)]; lab = [("BASE", "baseline", "-")]
    for cid, name, link, mags in CLASSES:
        for ml, ch in mags:
            sets.append(build(ch)); lab.append((cid, name, ml))
    res = run_sets(sets, a.T, a.seed, a.nrep)
    with open(f"{a.out_dir}/class_scan.tsv", "w") as f:
        f.write("\t".join(["id", "class", "magnitude"] + COLS) + "\n")
        for l, r in zip(lab, res):
            f.write("\t".join(list(l) + [fmt(r[c]) for c in COLS]) + "\n")
    sets = []; lab = []
    for k in OAT:
        for mu in OATMUL:
            s = dict(m.BASE); s[k] = m.BASE[k] * mu; sets.append(s); lab.append((k, f"x{mu}"))
    res = run_sets(sets, a.T, a.seed + 1, a.nrep)
    with open(f"{a.out_dir}/oat_scan.tsv", "w") as f:
        f.write("\t".join(["param", "multiplier"] + COLS) + "\n")
        for l, r in zip(lab, res):
            f.write("\t".join(list(l) + [fmt(r[c]) for c in COLS]) + "\n")
    with open(f"{a.out_dir}/results.sha256", "w") as f:
        for fn in ("class_scan.tsv", "oat_scan.tsv"):
            f.write(hashlib.sha256(open(f"{a.out_dir}/{fn}", "rb").read()).hexdigest() + "  " + fn + "\n")
    print(open(f"{a.out_dir}/results.sha256").read())
    return 0

if __name__ == "__main__":
    sys.exit(main())
