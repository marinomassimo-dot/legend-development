#!/usr/bin/env python3
"""IT11 P1.3: sensitivity of the origin-aware deepening order to the doubtful grouping choices. Variants (B was dropped as not applicable, see below): (default) two human deposits fold to one origin, one article at two readout
levels is two origins, a seed row counts at 10 percent of the strongest contribution; (A) the two deposits stay two origins; (B) levels of one article merge into one origin [NOT APPLICABLE: the engine refuses mixed readout levels within a run, so the seeds that contribute to one family always share one level and a merge cannot act; reported as such, not as a result];
(C) threshold 0.05; (D) threshold 0.25. For each question/hypothesis the top 8 under each variant is compared with the default (shared names) and the names entering/leaving are listed.
Complementary measures at two readout levels are not replicates (they may add information without being independent); a re-analysis of the same material is not a new origin.
Writes results/origin_sensitivity.tsv.   origin_sensitivity_it11.py
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, importlib.util, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
saved = list(sys.argv); sys.argv = ["x", "run"]
spec = importlib.util.spec_from_file_location("dz", HERE / "dispose_it10.py"); dz = importlib.util.module_from_spec(spec); spec.loader.exec_module(dz); sys.argv = saved
V4 = HERE / "results_v4"; DR = dz.DR
orig_c = dz.canonical_origins_checked; orig_cont = dz.contributing_origins
def variant(name):
    dz.canonical_origins_checked = orig_c; dz.contributing_origins = orig_cont
    if name == "A_deposits_two":
        def f(seed):
            out = []
            for k, ok in dz.origin_keys(seed):
                out.append((k, ok))
            return [(k, ok) for k, ok in out if k not in dz._OVR.get(seed["seed_id"], ())] or out
        dz.canonical_origins_checked = f
    elif name == "B_levels_merged":
        def f(seed):
            return [(re.sub(r"\|[a-z_]+$", "", k), ok) for k, ok in orig_c(seed)]
        dz.canonical_origins_checked = f
    elif name in ("C_thr005", "D_thr025"):
        thr = 0.05 if name == "C_thr005" else 0.25
        dz.contributing_origins = lambda rows, idx, sn, frac=thr: orig_cont(rows, idx, sn, frac)
def top8(rows_out, it9):
    sel = dz.deepening(rows_out, V4, DR, it9)
    d = {}
    for r in sel:
        if r[2] == "origin_aware": d.setdefault((r[0], r[1]), []).append(r[4])
    return d
dz.canonical_origins_checked(dz.rd(DR / "generation_it9_p1_20261030" / "seeds.tsv")[0])   # initialise the override table
res = {}
for v in ("default", "A_deposits_two", "C_thr005", "D_thr025"):
    variant(v)
    rows_out, _, it9 = dz.build(V4, DR)
    res[v] = top8(rows_out, it9)
out = []
for k in sorted(res["default"]):
    base = res["default"][k]
    for v in ("A_deposits_two", "C_thr005", "D_thr025"):
        cur = res[v].get(k, [])
        out.append([k[0], k[1], v, len(set(base) & set(cur)), "; ".join(sorted(set(cur) - set(base)))[:120], "; ".join(sorted(set(base) - set(cur)))[:120]])
with open(HERE / "results" / "origin_sensitivity.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["question", "hypothesis", "variant", "shared_with_default_of_8", "entering", "leaving"]); w.writerows(out)
for r in out:
    if r[3] < 8: print(r)
print("variants x lists:", len(out), "identical to default:", sum(1 for r in out if r[3] == 8))
