#!/usr/bin/env python3
"""IT24 P6 feasibility: does the displayed single chain hide target-level structure the engine already computes?
The engine score is a signed sum over seeds and over every admissible walk from every target of the family (dispose_it10.explain); the displayed chain is one walk.
This reads the engine's per-seed contributions (main target of each seed's strongest walk) and decomposes each family, per seed set, by target:
  targets with a net-positive contribution, targets with a net-negative one (a signed conflict between targets of ONE compound), seed overlap between positive targets
  (REDUNDANT: the same seeds reached through several targets; COMPLEMENTARY: different seeds), and the share of the positive mass the dominant target carries.
Usage: multitarget_feasibility_it24.py --eng DIR --out DIR   (DIR = generation_it22_p1_20261103/eng_merged)"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, glob, gzip, json, os, re
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--eng", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
    out = []
    for f in sorted(glob.glob(os.path.join(a.eng, "contributions_p1_*.tsv.gz"))):
        sset = os.path.basename(f)[len("contributions_p1_"):-len(".tsv.gz")]
        if re.search(r"_(adm|indeg|reach)$", sset):
            continue                      # the four null/variants are separate runs; the base run is the one displayed
        by = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(float)))
        for r in csv.DictReader(gzip.open(f, "rt"), delimiter="\t"):
            c = float(r["contrib_total"])
            for t in {r["main_target_hop0"], r["main_target_hops1to3"]} - {""}:
                by[r["family_id"]][t][r["seed_id"]] += c
        for fam, tg in by.items():
            net = {t: sum(s.values()) for t, s in tg.items()}
            pos = {t: {k for k, v in s.items() if v > 0} for t, s in tg.items() if net[t] > 0}
            neg = [t for t in tg if net[t] < 0]
            posmass = {t: sum(v for v in tg[t].values() if v > 0) for t in pos}
            tot = sum(posmass.values())
            red = ""
            if len(pos) >= 2:
                ts = sorted(pos)
                j = [len(pos[x] & pos[y]) / len(pos[x] | pos[y]) for i, x in enumerate(ts) for y in ts[i + 1:]]
                m = sum(j) / len(j)
                red = "REDUNDANT" if m >= 0.8 else ("COMPLEMENTARY" if m < 0.5 else "PARTLY_OVERLAPPING")
            kind = "CONFLICT_BETWEEN_TARGETS" if pos and neg else ("MULTI_POSITIVE" if len(pos) >= 2 else ("SINGLE_TARGET" if len(pos) == 1 else "NO_POSITIVE_TARGET"))
            out.append(dict(seed_set=sset, family_id=fam, n_targets=len(tg), n_pos=len(pos), n_neg=len(neg), kind=kind, overlap=red,
                            dominant_share=f"{max(posmass.values()) / tot:.3f}" if tot else "", targets_pos=";".join(sorted(pos)), targets_neg=";".join(sorted(neg))))
    os.makedirs(a.out, exist_ok=True)
    cols = list(out[0])
    with open(os.path.join(a.out, "target_decomposition.tsv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    s = collections.defaultdict(collections.Counter)
    for r in out:
        s[r["seed_set"]][r["kind"]] += 1
        if r["overlap"]:
            s[r["seed_set"]]["overlap_" + r["overlap"]] += 1
    json.dump({k: dict(v) for k, v in s.items()}, open(os.path.join(a.out, "summary.json"), "w"), indent=1, sort_keys=True)
    print(json.dumps({k: dict(v) for k, v in s.items()}, indent=1, sort_keys=True))


main()
