#!/usr/bin/env python3
"""IT9 P3 step 1: seed-specific pool from the P2 proposals (both nulls), with main target, hop, hub-ness and promiscuity.
Usage: pool_build_it9_p3.py --out pool_raw.tsv   (offline; needs the P2 results folder; run from anywhere)."""
import argparse, csv, glob, gzip, importlib.util, os, sys
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
P2 = HERE.parent / "generation_it9_p2_20261030"
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--out", required=True)
ap.add_argument("--zthr", type=float, default=3.0)
a = ap.parse_args()
os.environ.setdefault("LEGEND_CATALOG_CACHE", str(HERE.parent / "catalog" / "cache"))
spec = importlib.util.spec_from_file_location("seed_engine", P2 / "seed_engine.py"); se = importlib.util.module_from_spec(spec); sys.modules["seed_engine"] = se; spec.loader.exec_module(se)
R = P2 / "results"
def L(f): return {r["family_id"]: r for r in csv.DictReader(gzip.open(f, "rt"), delimiter="\t")}
sets = sorted({os.path.basename(f)[len("proposals_p1_"):-7] for f in glob.glob(str(R / "proposals_p1_*.tsv.gz")) if "indeg" not in f})
rows_all, meta_all = se.load_actions(str(R))
out = []
for s in sets:
    A = L(R / f"proposals_p1_{s}.tsv.gz"); B = L(R / f"proposals_p1_{s}_indeg.tsv.gz")
    fams = {}
    for f, r in A.items():
        z1, z2 = float(r["Z_ind_robust"]), float(B[f]["Z_ind_robust"])
        if z1 > a.zthr and z2 > a.zthr: fams[f] = ("opposes", z1, z2)
        elif z1 < -a.zthr and z2 < -a.zthr: fams[f] = ("mimics", z1, z2)
    print(s, len(fams), file=sys.stderr)
    if not fams: continue
    class NS: pass
    n = NS(); n.seeds = str(P2 / "seeds_p1" / (s + ".tsv")); n.actions = str(R); n.allow_mixed_levels = False
    eng, _, _ = se.make_engine(n, rows=rows_all, meta=meta_all)
    g = eng.g
    deg = g.indeg + g.outdeg
    thr = np.percentile(deg[: g.Ng], 95)
    tab = se.seed_contrib_table(eng, list(fams))
    by = {}
    for r in tab: by.setdefault(r["family_id"], []).append(r)
    for f, (arm, z1, z2) in fams.items():
        cs = sorted(by.get(f, []), key=lambda x: -abs(float(x["contrib_total"])))
        top = cs[0] if cs else None
        if top:
            h0, h1 = abs(float(top["contrib_hop0"])), abs(float(top["contrib_hops1to3"]))
            hop, tg = ("hop0", top["main_target_hop0"]) if h0 > h1 else ("hops1-3", top["main_target_hops1to3"])
            seedg = top["gene"]; sd = top["seed_direction"]
        else: hop = tg = seedg = sd = ""
        di = int(deg[g.idx[tg]]) if tg in g.idx else -1
        seeds = sorted({c["gene"] + ":" + c["seed_direction"] for c in cs if abs(float(c["contrib_total"])) > 0})
        genes = {c["gene"] for c in cs}
        p = A[f]
        out.append(dict(set=s, arm=arm, family_id=f, name=p["name"], Z_total=round(z1, 3), Z_indeg=round(z2, 3), n_signed_targets=p["n_signed_targets"], n_targets_in_graph=p["n_targets_in_graph"],
                        top_seed_gene=seedg, top_seed_direction=sd, hop=hop, main_target=tg, main_target_degree=di, hub_threshold=int(thr), hub_target=int(di >= thr), seed_own_target=int(tg in genes and hop == "hop0"),
                        seeds_contributing=";".join(seeds), conditional=int(p["uncertain_seed_mass"] not in ("0", "0.0", "")), guard=p["evaluation_forbidden_on"]))
cols = list(out[0]); 
with open(a.out, "w", newline="") as fh:
    w = csv.DictWriter(fh, cols, delimiter="\t"); w.writeheader(); w.writerows(out)
print(len(out), "rows", file=sys.stderr)
