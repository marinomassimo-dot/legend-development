#!/usr/bin/env python3
"""IT10 P2.4 trial 1: JUMP Cell Painting, WWOX knockout profile vs compound profiles (see PRE_DECLARATION.md).
Usage: trial1_jump.py --profiles PARQUET --meta DIR --repo ROOT --out DIR   (run with python -I in an isolated venv)"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, gzip, json, csv, os
import numpy as np, pandas as pd, pyarrow.parquet as pq
ap = argparse.ArgumentParser()
for k in ("profiles", "meta", "repo", "out"): ap.add_argument("--" + k, required=True)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
rng = np.random.default_rng(20261030)
t = pq.read_table(a.profiles).to_pandas()
xc = [c for c in t.columns if c.startswith("X_")]
X = t[xc].to_numpy(np.float32); j = t["Metadata_JCP2022"].to_numpy(); pl = t["Metadata_Plate"].to_numpy()
src = t["Metadata_Source"].to_numpy()
isg = np.char.startswith(j.astype(str), "JCP2022_8"); isc = ~(np.char.startswith(j.astype(str), "JCP2022_8") | np.char.startswith(j.astype(str), "JCP2022_9"))
print("wells", len(t), "crispr", isg.sum(), "orf", np.char.startswith(j.astype(str), "JCP2022_9").sum(), "compound-like", isc.sum())
W, ORF, PLK1 = "JCP2022_807699", "JCP2022_911201", "JCP2022_805264"
NEG = {"JCP2022_800001", "JCP2022_800002"}
def unit(v): n = np.linalg.norm(v, axis=-1, keepdims=True); return v / np.where(n == 0, 1, n)
def mean_pair_cos(idx):
    """mean cosine among wells of distinct plates"""
    U = unit(X[idx]); C = U @ U.T; p = pl[idx]; m = p[:, None] != p[None, :]
    return float(C[m].mean()) if m.any() else float("nan"), int(len(set(p)))
# gene wells
gdf = pd.DataFrame({"j": j[isg], "i": np.where(isg)[0]})
gi = gdf.groupby("j")["i"].apply(np.array).to_dict()
nwell = {k: len(v) for k, v in gi.items()}
res = {"wells_total": int(len(t)), "wwox_ko_wells": nwell.get(W, 0), "wwox_ko_plates": int(len(set(pl[gi[W]]))), "sources_of_wwox_ko": sorted(set(src[gi[W]]))}
cand = [k for k in gi if k not in NEG and k not in (W, PLK1) and nwell[k] >= 3]
pick = list(rng.choice(cand, 1000, replace=False))
def stat(k): return mean_pair_cos(gi[k])[0]
nullstat = np.array([stat(k) for k in pick]); nullstat = nullstat[~np.isnan(nullstat)]
w_stat, w_np = mean_pair_cos(gi[W]); p_stat, _ = mean_pair_cos(gi[PLK1])
res["gate"] = {"wwox_mean_pair_cos": w_stat, "null_mean": float(nullstat.mean()), "null_p95": float(np.percentile(nullstat, 95)), "null_p99": float(np.percentile(nullstat, 99)),
               "wwox_percentile_in_null": float((nullstat < w_stat).mean() * 100), "plk1_mean_pair_cos": p_stat, "plk1_percentile": float((nullstat < p_stat).mean() * 100),
               "n_null": int(len(nullstat)), "pass": bool(w_stat >= np.percentile(nullstat, 95))}
# negative-control wells
res["negcon_wells"] = int(np.isin(j, list(NEG)).sum())
# ORF gate
oi = np.where(j == ORF)[0]; res["orf_wells"] = int(len(oi))
if len(oi) > 1:
    ogene = pd.DataFrame({"j": j[np.char.startswith(j.astype(str), "JCP2022_9")], "i": np.where(np.char.startswith(j.astype(str), "JCP2022_9"))[0]}).groupby("j")["i"].apply(np.array).to_dict()
    ocand = [k for k in ogene if len(ogene[k]) >= 3 and k != ORF]
    opick = list(rng.choice(ocand, 1000, replace=False)); onull = np.array([mean_pair_cos(ogene[k])[0] for k in opick]); onull = onull[~np.isnan(onull)]
    os_ = mean_pair_cos(oi)[0]
    res["orf_gate"] = {"wwox_orf_mean_pair_cos": os_, "null_p95": float(np.percentile(onull, 95)), "percentile": float((onull < os_).mean() * 100), "pass": bool(os_ >= np.percentile(onull, 95))}
# gene mean profiles
def gmean(k): return unit(X[gi[k]].mean(0))
Pw, Pp = gmean(W), gmean(PLK1); Pn = unit(np.stack([X[gi[k]].mean(0) for k in pick]))
# compounds
ci = np.where(isc)[0]; cdf = pd.DataFrame({"j": j[ci], "plate": pl[ci], "i": ci})
nplate = cdf.groupby("j")["plate"].nunique(); keep = set(nplate[nplate >= 2].index)
keep -= {"JCP2022_033924", "JCP2022_999999"}
cdf = cdf[cdf.j.isin(keep)]
grp = cdf.groupby("j")["i"].apply(np.array)
ids = list(grp.index); M = np.stack([X[v].mean(0) for v in grp.values]); M = unit(M)
res["compounds_with_ge2_plates"] = len(ids)
cw, cp = M @ Pw, M @ Pp; cn = M @ Pn.T
mu, sd = cn.mean(1), cn.std(1) + 1e-9
zw, zp = (cw - mu) / sd, (cp - mu) / sd
# catalogue map by InChIKey skeleton
comp = pd.read_csv(os.path.join(a.meta, "compound.csv.gz"))[["Metadata_JCP2022", "Metadata_InChIKey"]]
sk = dict(zip(comp.Metadata_JCP2022, comp.Metadata_InChIKey.astype(str).str.split("-").str[0]))
cat = {}
for l in gzip.open(os.path.join(a.repo, "disease-models/wwox/research/drug_repurposing/catalog/catalog.jsonl.gz"), "rt"):
    r = json.loads(l); s = r["ids"].get("skeleton_key")
    if s: cat.setdefault(s, []).append(("FAM:" + r["id"], r["name"] or r["id"]))
df = pd.DataFrame({"jcp": ids, "skeleton": [sk.get(i, "") for i in ids], "cos_wwox": cw, "z_wwox": zw, "cos_plk1": cp, "z_plk1": zp})
df["catalogue_names"] = df.skeleton.map(lambda s: ";".join(sorted({n for _, n in cat.get(s, [])})))
df["catalogue_families"] = df.skeleton.map(lambda s: ";".join(sorted({f for f, _ in cat.get(s, [])})))
df["in_catalogue"] = df.catalogue_names != ""
res["compounds_mapped_to_catalogue"] = int(df.in_catalogue.sum())
# PLK1 control
plk = ["BI-2536", "VOLASERTIB", "GSK461364", "ONVANSERTIB", "RIGOSERTIB", "TAK-960", "ON-01910", "BI-6727", "GSK-461364A", "NMS-P937"]
top = df.sort_values("z_plk1", ascending=False).head(100)
res["plk1_control_top100_hits"] = [n for n in top.catalogue_names if any(p in n.upper() for p in plk)]
res["plk1_control_pass"] = len(res["plk1_control_top100_hits"]) > 0
res["plk1_top10_names"] = [n or s for n, s in zip(top.catalogue_names.head(10), top.skeleton.head(10))]
# candidates from IT9 v3 and SigCom
R = os.path.join(a.repo, "disease-models/wwox/research/drug_repurposing")
it9 = {}
for q in ("Q2", "Q5", "Q6"):
    for r in csv.DictReader(open(f"{R}/generation_it9_p2_20261030/v3/results/candidates_{q}.tsv"), delimiter="\t"):
        it9.setdefault(r["family_id"], []).append((q, r["arm"], r["name"]))
df["it9_listed"] = df.catalogue_families.map(lambda s: ";".join(sorted({f for f in s.split(";") if f in it9})))
res["it9_candidate_families_total"] = len(it9)
res["it9_candidate_families_with_jump_profile"] = int(sum(1 for f in it9 if f in set(";".join(df.catalogue_families).split(";"))))
sig = pd.read_csv(f"{R}/gse156243/derived/sigcom_reverser_summary.tsv", sep="\t"); s1 = {n.upper() for n in sig[sig.set == "S1"].head(100).pert_name.astype(str)}
df["sigcom_s1_top100"] = df.catalogue_names.map(lambda s: any(n.upper() in s1 for n in s.split(";") if n))
df.sort_values("z_wwox").head(300).to_csv(os.path.join(a.out, "jump_wwox_ko_most_opposed_top300.tsv"), sep="\t", index=False)
df.sort_values("z_wwox", ascending=False).head(100).to_csv(os.path.join(a.out, "jump_wwox_ko_most_similar_top100.tsv"), sep="\t", index=False)
df[df.it9_listed != ""][["jcp", "skeleton", "catalogue_names", "cos_wwox", "z_wwox", "it9_listed"]].to_csv(os.path.join(a.out, "jump_it9_candidates_z.tsv"), sep="\t", index=False)
sp = df[(df.z_wwox <= -3)].sort_values("z_wwox").head(100)
res["specific_opposers_z_le_-3_top100"] = int(len(sp)); res["specific_opposers_in_catalogue"] = int(sp.in_catalogue.sum())
res["specific_opposers_in_it9"] = int((sp.it9_listed != "").sum()); res["specific_opposers_in_sigcom_s1"] = int(sp.sigcom_s1_top100.sum())
res["specific_opposers_new"] = int(((sp.it9_listed == "") & (~sp.sigcom_s1_top100) & sp.in_catalogue).sum())
res["z_wwox_distribution"] = {"min": float(zw.min()), "p1": float(np.percentile(zw, 1)), "median": float(np.median(zw)), "max": float(zw.max())}
json.dump(res, open(os.path.join(a.out, "trial1_summary.json"), "w"), indent=1)
print(json.dumps(res, indent=1)[:4000])
