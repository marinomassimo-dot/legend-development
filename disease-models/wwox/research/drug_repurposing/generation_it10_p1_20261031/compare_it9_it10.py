#!/usr/bin/env python3
"""IT9 vs IT10 on one declared perimeter: the seed-specific, unflagged opposes/mimics families of Q2, Q4, Q5, Q6 (same seeds, same compound universe, same nulls).
Per question: families (distinct normalised names) in IT9 v3 and in IT10 v4, kept/lost/gained, share also found by the plain target search (the external-only
reference: compounds that hit a seed gene directly, no WWOX direction or network), share with >=2 evidence origins, and names new to LEGEND (not in any card,
unit, IT9 record). The answer-key is not an input. Writes results/it9_vs_it10.tsv.   compare_it9_it10.py
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, collections, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
norm = lambda s: re.sub(r"[^a-z0-9]+", "", s.lower())
known = {norm(r["name"]) for r in rd(DR / "ranking_it8_p9_20261029" / "unit_members.tsv") if r["family_id"].startswith("FAM:")} | {norm(r["compound"]) for r in rd(DR / "ranking_it8_p9_20261029" / "it9_records.tsv")}
def load(d):
    out = collections.defaultdict(dict)
    for q in ("Q2", "Q4", "Q5", "Q6"):
        for r in rd(Path(d) / f"candidates_{q}.tsv"):
            if r["arm"] in ("opposes", "mimics") and r["seed_specific_all_three_nulls"] == "1" and "UNCERTAIN_ACTIVE_MOIETY" not in r["family_flags"]:
                out[q].setdefault((r["arm"], norm(r["name"])), r)
    return out
a = load(DR / "generation_it9_p2_20261030" / "v3" / "results"); b = load(HERE / "results_v4")
orig = {}
for q in ("Q2", "Q4", "Q5", "Q6"):
    for r in rd(HERE / "results" / f"dispositions_{q}.tsv"):
        orig[(q, r["arm"], norm(r["name"]))] = int(r["n_origins"])
rows = []
for q in ("Q2", "Q4", "Q5", "Q6"):
    for arm in ("opposes", "mimics"):
        A = {k[1] for k in a[q] if k[0] == arm}; B = {k[1] for k in b[q] if k[0] == arm}
        direct = sum(1 for k in B if b[q][(arm, k)]["also_found_by_direct_search"] == "1")
        two = sum(1 for k in B if orig.get((q, arm, k), 1) >= 2)
        new = sum(1 for k in B if k not in known)
        rows.append([q, arm, len(A), len(A & B), len(A - B), len(B - A), len(B), direct, two, new])
with open(HERE / "results" / "it9_vs_it10.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["question", "arm", "it9_names", "kept", "lost", "gained", "it10_names", "it10_also_direct_search", "it10_two_or_more_origins", "it10_new_to_legend"]); w.writerows(rows)
for r in rows: print(r)
