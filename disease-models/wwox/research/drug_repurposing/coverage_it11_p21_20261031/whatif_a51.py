#!/usr/bin/env python3
"""What-if, NOT a classification input: if A51 were credited with the kinases named on its card (CSNK1A1, CDK7, CDK9; card text, attribution unverified), does the v4 network connect them to the Q6 MYC seed?
Read-only. Output: whatif_a51.tsv"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import importlib.util, csv
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.argv = ["x", "run"]
spec = importlib.util.spec_from_file_location("v4w", DR / "generation_it10_p1_20261031" / "engine_v4" / "seed_engine_v4.py")
m4 = importlib.util.module_from_spec(spec); sys.modules["v4w"] = m4; spec.loader.exec_module(m4)
m3, se = m4.m3, m4.se
edges = m4.read_edges4()
rows = []
for sn, lvl in (("Q6_expression_tiersAB", "expression"), ("Q6_protein_tiersAB", "protein")):
    seeds = se.load_seeds(str(DR / "generation_it9_p2_20261030" / "seeds_p1" / (sn + ".tsv")))
    g = m4.Graph4(edges, extras=["CSNK1A1", "CDK7", "CDK9"] + seeds.genes); g.level = lvl
    S = seeds.unit_matrix(g.idx, g.N)
    for regime, (mode, junc) in dict(all=("all", False), v3=("v3", False), v4=("v3", True)).items():
        m3.MODE = mode; m4.JUNCTION = junc
        V = g.influence_ind(S)
        for t in ("CSNK1A1", "CDK7", "CDK9"):
            v = float(V[0, g.idx[t]])
            rows.append(dict(seed_set=sn, regime=regime, target=t, out_edges=sum(1 for e in edges if e[0] == t), influence=f"{v:.6g}", chain=(g.best_chain(t, "MYC") or "") if v else ""))
with open(HERE / "whatif_a51.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
for r in rows:
    if r["regime"] == "v4": print(r["seed_set"][:12], r["target"], r["out_edges"], r["influence"], r["chain"][:140])
