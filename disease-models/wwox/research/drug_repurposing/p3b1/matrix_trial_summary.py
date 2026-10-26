#!/usr/bin/env python3
"""Aggregate comparison of MATRIX rows fetched by matrix_scores_extract.py. Standard library only.

Emits COUNTS and AGREEMENT STATISTICS between disease nodes, never a per-drug score, rank or candidate list:
  - how many drugs the publisher scored for each node, and how many carry the publisher's training/evaluation flags;
  - whether two nodes that are different diseases receive the same ordering of drugs (Spearman rho on the publisher's
    `untransformed_treat_score`, overlap of the two top-50 sets). A high agreement between DEE28 and an unrelated
    sibling would mean the output reflects the node's neighbourhood, not the disease.
The flags are the publisher's curated labels (drug-disease pairs it treats as known), not predictions.

Usage: matrix_trial_summary.py <matrix_scores_raw.json> [<more raw files>...] > summary.json
"""
import json
import sys


def ranks(values):
    order = sorted(range(len(values)), key=lambda i: values[i])
    r, i = [0.0] * len(values), 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        for k in range(i, j + 1):
            r[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(a, b):
    ra, rb = ranks(a), ranks(b)
    n = len(a)
    ma, mb = sum(ra) / n, sum(rb) / n
    cov = sum((x - ma) * (y - mb) for x, y in zip(ra, rb))
    va, vb = sum((x - ma) ** 2 for x in ra), sum((y - mb) ** 2 for y in rb)
    return cov / (va * vb) ** 0.5


def main(paths):
    rows, meta = {}, {}
    for p in paths:
        d = json.load(open(p))
        rows.update(d["rows"])
        meta[p.split("/")[-2] if "/" in p else p] = d["meta"]
    flags = ["is_known_positive", "is_known_negative", "trial_sig_better", "trial_non_sig_better", "trial_sig_worse",
             "trial_non_sig_worse", "off_label", "ec_indications_list"]
    out = {"nodes": {}, "pairwise": {}}
    by = {}
    for t, rs in rows.items():
        by[t] = {r["source"]: r for r in rs}
        out["nodes"][t] = {"drugs_scored": len(rs), "flag_counts": {f: sum(1 for r in rs if r[f]) for f in flags},
                           "columns_present": sorted(rs[0].keys()) if rs else []}
    ts = sorted(by)
    for i, a in enumerate(ts):
        for b in ts[i + 1:]:
            common = sorted(set(by[a]) & set(by[b]))
            va = [by[a][s]["untransformed_treat_score"] for s in common]
            vb = [by[b][s]["untransformed_treat_score"] for s in common]
            top = lambda t: set(sorted(by[t], key=lambda s: -by[t][s]["untransformed_treat_score"])[:50])
            ta, tb = top(a), top(b)
            out["pairwise"][f"{a}|{b}"] = {"common_drugs": len(common), "spearman_rho": round(spearman(va, vb), 4),
                                           "top50_overlap": len(ta & tb), "top50_union": len(ta | tb)}
    out["fetch_meta"] = meta
    json.dump(out, sys.stdout, indent=1, sort_keys=True)


if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print(__doc__)
        raise SystemExit(0)
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    main(sys.argv[1:])
