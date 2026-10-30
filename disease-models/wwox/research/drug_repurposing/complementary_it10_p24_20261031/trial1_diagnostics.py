#!/usr/bin/env python3
"""Post-hoc diagnostics for trial 1 (declared as non-blind in the README). Needs the same inputs as trial1_jump.py."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import os, json, numpy as np, pandas as pd, pyarrow.parquet as pq
prof, meta, out = sys.argv[1:4]
t = pq.read_table(prof).to_pandas(); xc = [c for c in t.columns if c.startswith("X_")]
X = t[xc].to_numpy(np.float32); j = t["Metadata_JCP2022"].astype(str).to_numpy().astype("U32"); pl = t["Metadata_Plate"].to_numpy()
unit = lambda v: v / np.where(np.linalg.norm(v, axis=-1, keepdims=True) == 0, 1, np.linalg.norm(v, axis=-1, keepdims=True))
rng = np.random.default_rng(1)
isg = np.char.startswith(j, "JCP2022_8"); isc = ~(isg | np.char.startswith(j, "JCP2022_9"))
G = pd.DataFrame({"j": j[isg], "i": np.where(isg)[0]}).groupby("j")["i"].apply(np.array)
NEG = ["JCP2022_800001", "JCP2022_800002"]
cdf = pd.DataFrame({"j": j[isc], "plate": pl[isc], "i": np.where(isc)[0]})
n = cdf.groupby("j")["plate"].nunique(); cdf = cdf[cdf.j.isin(n[n >= 2].index) & ~cdf.j.isin(["JCP2022_033924", "JCP2022_999999"])]
grp = cdf.groupby("j")["i"].apply(np.array); M = unit(np.stack([X[v].mean(0) for v in grp.values])); ids = list(grp.index)
W = unit(X[G["JCP2022_807699"]].mean(0)); cw = M @ W
r = {}
r["norm_wwox_mean_profile"] = float(np.linalg.norm(X[G["JCP2022_807699"]].mean(0)))
nm = np.array([np.linalg.norm(X[G[k]].mean(0)) for k in rng.choice([k for k in G.index if len(G[k]) >= 3], 300, replace=False)])
r["norm_null_genes_mean_profile_median"] = float(np.median(nm)); r["norm_wwox_percentile_among_null_by_norm"] = float((nm < r["norm_wwox_mean_profile"]).mean() * 100)
# per-well norms and single-well cosines
wells = G["JCP2022_807699"]; r["wwox_well_norms"] = [float(np.linalg.norm(X[i])) for i in wells]
U = unit(X[wells]); r["wwox_pairwise_cos_matrix"] = np.round(U @ U.T, 2).tolist()
r["wwox_plates"] = [str(pl[i]) for i in wells]
# do the WWOX top opposers repeat for random genes?
top_w = set(np.argsort(cw)[:100]); jac = []
for k in rng.choice([k for k in G.index if k not in NEG and len(G[k]) >= 3], 60, replace=False):
    c = M @ unit(X[G[k]].mean(0)); jac.append(len(top_w & set(np.argsort(c)[:100])))
r["top100_opposed_shared_with_random_genes_mean"] = float(np.mean(jac)); r["max_shared"] = int(np.max(jac))
# compound-profile norm of the opposers (single noisy wells?)
cnt = np.array([len(v) for v in grp.values]); r["wells_per_compound_median"] = float(np.median(cnt)); r["wells_per_opposer_median"] = float(np.median(cnt[list(top_w)]))
r["mean_compound_cos_to_wwox"] = float(cw.mean())
# PLK inhibitors in JUMP?
comp = pd.read_csv(os.path.join(meta, "compound.csv.gz")); sk = dict(zip(comp.Metadata_JCP2022, comp.Metadata_InChIKey.astype(str).str.split("-").str[0]))
P = unit(X[G["JCP2022_805264"]].mean(0)); cp = M @ P; order = np.argsort(-cp); rank = {ids[o]: n for n, o in enumerate(order)}
skel = {"BI-2536": "XQVVPGYIWAGRNI", "volasertib": "SXNJFOWDRLKDSF", "GSK461364": "ZHJGWYRLJUCMRT", "onvansertib": "QHLVBNKYJGBCQJ", "TAK-960": "GWRSATNRNFYMDI", "rigosertib": "OWBFCJROIKNMGD"}
inv = {}
for jc, s in sk.items(): inv.setdefault(s, []).append(jc)
r["plk_inhibitors_in_jump"] = {k: [(jc, rank.get(jc)) for jc in inv.get(s, [])] for k, s in skel.items()}
json.dump(r, open(os.path.join(out, "trial1_diagnostics.json"), "w"), indent=1); print(json.dumps(r, indent=1)[:3500])
