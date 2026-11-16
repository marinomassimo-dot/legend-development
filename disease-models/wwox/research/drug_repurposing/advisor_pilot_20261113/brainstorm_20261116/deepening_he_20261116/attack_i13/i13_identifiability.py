#!/usr/bin/env python3
"""HE's identifiability check on SCI's single-compartment intrinsic-profile model (I13/I8).

    python3 i13_identifiability.py --model <intrinsic_profile_model.py as landed> --out <dir> [--seed 13] [--draws 3000] [--keep 40]

SCI's model keeps the ONE best of 3000 random wild-type parameter sets (seed 13) and applies manipulations to it. This script reuses the model's own functions (read from the landed file; the file is not modified)
and asks whether the verdict "a ~30% loss of the resting K+ leak reproduces the knockout profile; a tonic GABA-A loss does not" survives when the wild-type set is any of the best `keep` sets of the same search
(different seeds as well), instead of the single best. Held targets: S-KO RMP -73.62 mV, Rin 143.0 MOhm, sag 2.57 mV, rebound 1.86 mV (tolerances declared here before the run: RMP within 1.5 mV, Rin within 15%, sag within 0.5 mV,
rebound within 0.5 mV; 'reproduces' = all four). A wild-type set is ACCEPTED only if it reproduces the wild-type row itself within RMP 1.5 mV, Rin and tau 15%, sag and rebound 0.3 mV
(also declared before the run); the verdict is reported for the accepted sets, and for the single best set (SCI's choice) separately. Hypothesis generator, not evidence; every conductance ASSUMED. Not medical advice.
"""
import argparse, csv, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--model"); ap.add_argument("--out"); ap.add_argument("--seed", type=int, default=13); ap.add_argument("--draws", type=int, default=3000); ap.add_argument("--keep", type=int, default=40)
a = ap.parse_args()
if not (a.model and a.out):
    ap.print_help(); sys.exit(0)
import numpy as np
src = Path(a.model).read_text()
head = src.split("TARGET = ")[0].split("import numpy as np", 1)[1]          # functions only: rest, g_inst, g_ss, pulse_sim, metrics
ns = {"np": np}; exec("import sys\n" + head.replace("if len(sys.argv) != 3", "if False and len(sys.argv) != 3"), ns)
TARGET = (-79.25, 102.88, 18.55, 1.18, 0.96); KO = (-73.62, 143.03, 21.25, 2.57, 1.86)
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(a.seed); sets = []
for _ in range(a.draws):
    P = dict(gK=rng.uniform(2, 9), gG=rng.uniform(0.3, 4.0), gC=rng.uniform(0.2, 2.5), gh=rng.uniform(0.1, 4.0), gT=rng.uniform(1, 40), C=100.0)
    V0 = ns["rest"](P); G = ns["g_inst"](V0, P)
    if G <= 0: continue
    P["C"] = 18.55 * G; m = ns["metrics"](P)
    loss = abs(m[0] - TARGET[0]) + 3.0 * abs(np.log(m[1] / TARGET[1])) + abs(m[2] - TARGET[2]) / 18.55 + abs(m[3] - TARGET[3]) + abs(m[4] - TARGET[4])
    sets.append((loss, P, m))
sets.sort(key=lambda s: s[0])
def wt_ok(m):
    return abs(m[0] - TARGET[0]) <= 1.5 and abs(m[1] / TARGET[1] - 1) <= 0.15 and abs(m[2] / TARGET[2] - 1) <= 0.15 and abs(m[3] - TARGET[3]) <= 0.3 and abs(m[4] - TARGET[4]) <= 0.3
best1 = sets[:1]; sets = [s for s in sets[:a.keep] if wt_ok(s[2])]
print(f"accepted wild-type sets: {len(sets)} of the best {a.keep} of {a.draws} draws; best-1 loss {best1[0][0]:.3f}")
MAN = [("K+ leak x0.7", lambda W: {"gK": W["gK"] * 0.7}), ("K+ leak x0.5", lambda W: {"gK": W["gK"] * 0.5}), ("tonic GABA-A x0.5", lambda W: {"gG": W["gG"] * 0.5}), ("tonic GABA-A x0.0", lambda W: {"gG": 0.0}),
       ("tonic x0.5 and K+ leak x0.85", lambda W: {"gG": W["gG"] * 0.5, "gK": W["gK"] * 0.85}), ("Ih x2", lambda W: {"gh": W["gh"] * 2})]
def ok(m):
    return abs(m[0] - KO[0]) <= 1.5 and abs(m[1] / KO[1] - 1) <= 0.15 and abs(m[3] - KO[3]) <= 0.5 and abs(m[4] - KO[4]) <= 0.5
rows = [["wt_set(0=best single set; 1.. accepted sets)", "wt_loss", "gK", "gG", "gC", "gh", "gT", "wt_RMP", "wt_Rin", "manipulation", "RMP", "Rin", "tau", "sag", "rebound", "reproduces_KO_all_four"]]
tally = {n: 0 for n, _ in MAN}; partial = {n: [0, 0, 0, 0] for n, _ in MAN}
for i, (loss, W, m0) in enumerate(best1 + sets):
    for n, f in MAN:
        P = dict(W); P.update(f(W)); m = ns["metrics"](P); good = ok(m); tally[n] += good
        for k, (x, y, tol) in enumerate(((m[0], KO[0], 1.5), (m[1] / KO[1] - 1, 0, 0.15), (m[3], KO[3], 0.5), (m[4], KO[4], 0.5))):
            partial[n][k] += abs(x - y) <= tol
        rows.append([i, f"{loss:.3f}", *[f"{W[k]:.3f}" for k in ("gK", "gG", "gC", "gh", "gT")], f"{m0[0]:.2f}", f"{m0[1]:.1f}", n, *[f"{v:.3f}" for v in m], "yes" if good else "no"])
with open(out / "identifiability_runs.tsv", "w", newline="") as fh:
    csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
with open(out / "identifiability_summary.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["manipulation", "sets_run(best single + accepted)", "reproduces_all_four", "RMP_ok", "Rin_ok", "sag_ok", "rebound_ok"])
    for n, _ in MAN: w.writerow([n, len(sets) + 1, tally[n], *partial[n]])
print(open(out / "identifiability_summary.tsv").read())
