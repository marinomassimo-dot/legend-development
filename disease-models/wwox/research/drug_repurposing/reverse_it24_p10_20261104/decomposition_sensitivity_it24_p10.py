#!/usr/bin/env python3
"""IT24 P10: does the P6 target-count label (SINGLE / MULTI_POSITIVE / CONFLICT) survive (a) dropping the pairs withheld at the IT24 P1 action refresh and (b) a mass floor on a target's share?
Re-implements the P6 rule on the committed contributions (read-only). Usage: decomposition_sensitivity_it24_p10.py OUT.tsv"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, collections, re
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
ENG = DR / "generation_it22_p1_20261103" / "eng_merged"
EX = {(r["family_id"], r["gene"]) for r in csv.DictReader(open(DR / "generation_it21_p2_20261103" / "source_exclusions_it24.tsv"), delimiter="\t")}
P = list(csv.DictReader(open(DR / "generation_it22_p1_20261103" / "results_p4" / "proposals_it21.tsv"), delimiter="\t"))
need = {(p["seed_set"], p["family_id"], "oppose" if p["hypothesis"] == "H_HARM" else "mimic"): p for p in P}
by = collections.defaultdict(lambda: collections.defaultdict(float))
for ss in {k[0] for k in need}:
    for r in csv.DictReader(gzip.open(ENG / f"contributions_p1_{ss}.tsv.gz", "rt"), delimiter="\t"):
        for t in {r["main_target_hop0"], r["main_target_hops1to3"]} - {""}:
            by[(ss, r["family_id"])][t] += float(r["contrib_total"])


def kind(net, floor):
    tot = sum(abs(v) for v in net.values()) or 1
    net = {t: v for t, v in net.items() if abs(v) / tot >= floor}
    pos = [t for t, v in net.items() if v > 0]; neg = [t for t, v in net.items() if v < 0]
    return "CONFLICT" if pos and neg else ("MULTI_POSITIVE" if len(pos) >= 2 else ("SINGLE" if len(pos) == 1 else "NONE"))


rows, c = [], collections.Counter()
for (ss, fam, ori), p in need.items():
    d = by.get((ss, fam)) or {}
    sg = 1 if ori == "oppose" else -1
    base = {t: sg * v for t, v in d.items()}
    nox = {t: v for t, v in base.items() if (fam, t) not in EX}
    k0, k1, k2, k3 = kind(base, 0), kind(nox, 0), kind(base, 0.01), kind(base, 0.05)
    c[("base", k0)] += 1; c[("withheld_dropped", k1)] += 1; c[("floor1pct", k2)] += 1; c[("floor5pct", k3)] += 1
    if len({k0, k1, k2, k3}) > 1:
        rows.append(dict(proposal_id=p["proposal_id"], compound=p["compound"], seed_set=ss, handed_over="", base=k0, withheld_dropped=k1, floor1pct=k2, floor5pct=k3))
H = {r["proposal_id"] for r in csv.DictReader(open(DR / "generation_it22_p1_20261103" / "results_p4" / "handoff_it21.tsv"), delimiter="\t")}
for r in rows:
    r["handed_over"] = "yes" if r["proposal_id"] in H else ""
with open(sys.argv[1], "w", newline="") as fh:
    w = csv.DictWriter(fh, list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
for k in sorted(c): print(k, c[k])
print(len(rows), "proposal rows whose label changes under at least one variant;", sum(1 for r in rows if r["handed_over"]), "handed over")
