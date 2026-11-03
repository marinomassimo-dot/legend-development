#!/usr/bin/env python3
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print("IT22 P8 verifier recomputation (recompute_attr.py): read-only recomputation of attribution states from the raw Guide to Pharmacology file; needs LEGEND_CATALOG_CACHE; writes nothing but its own output tables.")
    raise SystemExit(0)
"""Independent recomputation of GtoPdb attribution from the raw interactions file (verifier; written without importing the producer code)."""
import csv, collections, statistics, sys, os, math
CACHE = os.environ.get("LEGEND_CATALOG_CACHE")
def rd(p):
    rows = list(csv.reader(open(p, encoding="utf-8")))
    return [dict(zip(rows[1], r)) for r in rows[2:]]
LIG = rd(CACHE + "/gtopdb/ligands.csv")
INT = [r for r in rd(CACHE + "/gtopdb/interactions.csv") if r["Target Species"] == "Human" and r["Ligand ID"]]
def ligs(name):
    n = name.lower()
    return [l["Ligand ID"] for l in LIG if l["Name"].lower() == n]
def raw_rows(lid):
    return [r for r in INT if r["Ligand ID"] == lid]
def typed(lids):
    d = collections.defaultdict(list)
    for r in INT:
        if r["Ligand ID"] not in lids: continue
        g = r["Target Gene Symbol"].upper()
        if not g or "|" in g: continue
        nm = r["Original Affinity Median nm"]
        if nm:
            nm = float(nm)
        elif r["Affinity Median"]:
            nm = 10 ** (9 - float(r["Affinity Median"]))
        else: continue
        t = r["Original Affinity Units"]
        if t in ("", "-"):
            a = r["Affinity Units"]
            t = a[1:] if a.startswith("p") else (a or "?")
            if t in ("-", ""): t = "?"
        rel = r["Original Affinity Relation"] or "="
        d[(g, t)].append((nm, rel, r["Assay Description"][:60]))
    return d
def summarize(d):
    out = {}
    for k, v in d.items():
        ex = [x for x in v if x[1] == "="]
        use = ex or v
        out[k] = (statistics.median(x[0] for x in use), "=" if ex else use[0][1], len(use), sorted({x[1] for x in v}))
    return out
def state(out, main):
    main = main.upper()
    genes = {g for g, t in out}
    if main not in genes: return "UNMEASURED", None
    if len(genes) == 1: return "SINGLE", None
    best = None
    res = []
    for (g, t), (nm, rel, n, rels) in out.items():
        if g != main: continue
        for (g2, t2), (nm2, rel2, n2, rels2) in out.items():
            if g2 == main or t2 != t: continue
            res.append((nm / nm2, t, g2, nm, rel, nm2, rel2))
    return "PAIRS", sorted(res)[:4]
if __name__ == "__main__":
    name, main = sys.argv[1], sys.argv[2]
    ids = ligs(name)
    out = summarize(typed(set(ids)))
    print(name, ids)
    for k in sorted(out): print("  ", k, out[k])
    print("  ->", state(out, main))
