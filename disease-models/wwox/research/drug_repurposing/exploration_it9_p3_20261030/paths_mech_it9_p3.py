#!/usr/bin/env python3
"""IT9 P3: for each selected candidate, shortest signed network paths (<= 3 hops) from the main target to the top seed gene, and ChEMBL curated mechanism rows (live). Usage: paths_mech_it9_p3.py --selected selected_core.tsv --out paths_mech.tsv"""
import argparse, collections, csv, importlib.util, json, os, sys, time, urllib.request
from pathlib import Path
H = Path(__file__).resolve().parent; D = H.parent; P2 = D / "generation_it9_p2_20261030"
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--selected", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
os.environ.setdefault("LEGEND_CATALOG_CACHE", str(D / "catalog/cache"))
spec = importlib.util.spec_from_file_location("seed_engine", P2 / "seed_engine.py"); se = importlib.util.module_from_spec(spec); sys.modules["seed_engine"] = se; spec.loader.exec_module(se)
adj = collections.defaultdict(list)
for s, t, sg in se.read_edges(): adj[s].append((t, sg))
def paths(src, dst, k=3):
    out = []; frontier = [(src, [src], 1)]
    for _ in range(k):
        nxt = []
        for n, p, sg in frontier:
            for t, s2 in adj.get(n, []):
                if t in p: continue
                np_, ns = p + [t], sg * (1 if s2 > 0 else -1)
                if t == dst: out.append((np_, ns))
                else: nxt.append((t, np_, ns))
        frontier = [(t, p, s) for t, p, s in nxt]
        if out: break
    return out
rows = []
for r in csv.DictReader(open(a.selected), delimiter="\t"):
    tg, sd = r["main_target"], r["top_seed"]; ps = paths(tg, sd) if tg and sd else []
    ptxt = "; ".join(("->".join(p) + " (net sign %+d)" % s) for p, s in ps[:3]) + (" [+%d more]" % (len(ps) - 3) if len(ps) > 3 else "")
    mech = ""
    cid = r["chembl_parent"]
    if cid:
        try:
            with urllib.request.urlopen("https://www.ebi.ac.uk/chembl/api/data/mechanism.json?limit=20&molecule_chembl_id=" + cid, timeout=60) as f: ms = json.load(f)["mechanisms"]
            mech = " | ".join(sorted({"%s: %s" % (m.get("action_type"), m.get("mechanism_of_action")) for m in ms})) or "none curated"
        except Exception as e: mech = "SERVICE_ERROR"
        time.sleep(0.3)
    rows.append([r["parent"], r["name"], tg, sd, len(ps), min((len(p) - 1 for p, s in ps), default=""), ptxt, mech])
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["parent", "name", "main_target", "top_seed", "n_shortest_paths", "path_length", "paths_(target_to_seed_gene)", "chembl_curated_mechanism_live"]); w.writerows(rows)
