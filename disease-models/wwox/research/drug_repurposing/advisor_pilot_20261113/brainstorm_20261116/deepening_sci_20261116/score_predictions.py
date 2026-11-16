#!/usr/bin/env python3
"""Score the predictions frozen in PREDICTIONS_FROZEN_BEFORE_RUN.md against class_scan.tsv (largest magnitude of each class).
    python3 score_predictions.py --help
    python3 score_predictions.py run <class_scan.tsv> <out_tsv>
'up' = change > +15 percent, 'down' = < -15 percent, '~0' = within 15 percent. A silent network (fewer than 3 bursts) scores the interval as 'up (silent)' and the duration as 'n/a'.
The predicted signs are copied here from the frozen file (sha256 in predictions_frozen.sha256); editing them after a run would be visible by hash."""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv
PRED = {"C1": ("up", "~0", "x0.25"), "C2": ("up", "down", "x0.85"), "C3": ("down", "~0|up", "pam1.0"), "C4": ("up", "down", "x0.35"), "C5": ("down", "up", "x3"),
        "C6": ("up", "~0", "x1.4"), "C7": ("up", "~0", "1.0"), "C8": ("up", "down", "0.10"), "C9": ("up", "~0", "x0.7"), "C10": ("up", "~0", "x2")}
rows = list(csv.DictReader(open(sys.argv[2]), delimiter="\t"))
base = [r for r in rows if r["id"] == "BASE"][0]
def f(x):
    return None if x == "NA" else float(x)
def cls(new, old):
    if new is None:
        return None
    d = new / old - 1
    return "up" if d > .15 else ("down" if d < -.15 else "~0")
out = []; right = wrong = na = 0
for cid, (pi, pd, mag) in PRED.items():
    r = [x for x in rows if x["id"] == cid and x["magnitude"] == mag][0]
    silent = r["int_med"] == "NA" or float(r["n_bursts"]) < 3
    gi = "up (silent)" if silent else cls(f(r["int_med"]), f(base["int_med"]))
    gd = "n/a" if silent else cls(f(r["dur_med"]), f(base["dur_med"]))
    di = "" if silent else f"{f(r['int_med']) / f(base['int_med']) - 1:+.0%}"
    dd = "" if silent else f"{f(r['dur_med']) / f(base['dur_med']) - 1:+.0%}"
    oki = gi.split()[0] == pi
    okd = None if gd == "n/a" else (gd in pd.split("|"))
    for ok in (oki, okd):
        if ok is None: na += 1
        elif ok: right += 1
        else: wrong += 1
    out.append((cid, mag, pi, gi, di, "right" if oki else "wrong", pd, gd, dd, "n/a" if okd is None else ("right" if okd else "wrong")))
with open(sys.argv[3], "w") as fo:
    fo.write("id\tmagnitude\tpred_INT\tgot_INT\tdINT\tINT_call\tpred_DUR\tgot_DUR\tdDUR\tDUR_call\n")
    for o in out: fo.write("\t".join(o) + "\n")
    fo.write("\t".join(["#TOTAL", "", f"right {right}", f"wrong {wrong}", f"n/a {na}"] + [""] * 5) + "\n")
for o in out: print(o)
print("right", right, "wrong", wrong, "n/a", na)
