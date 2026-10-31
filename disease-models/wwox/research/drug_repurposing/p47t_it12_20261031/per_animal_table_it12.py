#!/usr/bin/env python3
"""IT12 P2-P47T: per-animal pivot (set scores and Nptx2/Bdnf log2 CPM) to show animal-level heterogeneity across regions.
Usage: per_animal_table_it12.py run set_scores_per_animal_it12.tsv identity_it12.tsv OUT.tsv   (stdlib; --help prints this)"""
import sys, csv, collections
if len(sys.argv) < 2 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
T = collections.defaultdict(dict)
for r in csv.DictReader(open(sys.argv[2]), delimiter="\t"):
    T[(r["region"], r["animal"], r["genotype"])][r["set"]] = r["score_log2_centered"]
for r in csv.DictReader(open(sys.argv[3]), delimiter="\t"):
    if r["check"].startswith("marker_log2CPM_Nptx2") or r["check"].startswith("marker_log2CPM_Bdnf"):
        reg, gt, an = r["region"], None, r["item"].split("_", 2)
        gtp = "P47T" if "P47T" in r["item"] else "WT"
        T[(reg, an[2], gtp)][r["check"].replace("marker_log2CPM_", "") + "_log2CPM"] = r["value"]
cols = ["Nptx2_log2CPM", "Bdnf_log2CPM", "HIF_SEL_UP6", "HIF_FLAT6", "NRF2_5", "ASTRO", "ACTIVITY_IEG", "IT7_OBS6"]
with open(sys.argv[4], "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["region", "animal", "genotype"] + cols)
    for (reg, an, gt), d in sorted(T.items(), key=lambda kv: (["HPC", "CTX", "PFC", "CB"].index(kv[0][0]), kv[0][2], kv[0][1])):
        w.writerow([reg, an, gt] + [d.get(c, "") for c in cols])
