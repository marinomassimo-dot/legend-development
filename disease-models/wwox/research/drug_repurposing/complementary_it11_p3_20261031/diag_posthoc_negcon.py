#!/usr/bin/env python3
"""IT11 P3 POST-HOC diagnostic (not pre-declared; run after the T1 results were seen; labelled as such in the README).
Question: do the two CRISPR negative controls (no-guide, 164 of 384 wells on a plate; non-targeting, 10 wells) differ from each
other, and does re-referencing knockout profiles to the non-targeting mean (the control that, by the plate tags, shares the
tracrRNA condition with the knockout wells) change the declared hit rate?
Usage: diag_posthoc_negcon.py --profiles ALL_PCA_corrected.parquet --meta JUMP_METADATA_DIR --target JUMP_TARGET_DIR --out DIR
Run with python -I; needs numpy, pandas, pyarrow."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, json, os
import numpy as np, pandas as pd, pyarrow.parquet as pq
ap = argparse.ArgumentParser()
for k in ("profiles", "meta", "target", "out"): ap.add_argument("--" + k, required=True)
a = ap.parse_args(); rng = np.random.default_rng(20261031)
t = pq.read_table(a.profiles).to_pandas(); xc = [c for c in t.columns if c.startswith("X_")]
X = t[xc].to_numpy(np.float32); meta = t[["Metadata_Source", "Metadata_Plate", "Metadata_JCP2022"]].merge(
    pd.read_csv(os.path.join(a.meta, "plate.csv.gz")), on=["Metadata_Source", "Metadata_Plate"], how="left"); del t
j = meta.Metadata_JCP2022.astype(str).to_numpy(); pt = meta.Metadata_PlateType.astype(str).to_numpy(); src = meta.Metadata_Source.to_numpy()
unit = lambda v: v / np.where(np.linalg.norm(v, axis=-1, keepdims=True) == 0, 1, np.linalg.norm(v, axis=-1, keepdims=True))
cr = (pt == "CRISPR") & (src == "source_13")
ng, nt = X[cr & (j == "JCP2022_800001")], X[cr & (j == "JCP2022_800002")]
r = dict(n_noguide=int(len(ng)), n_nontargeting=int(len(nt)))
mng, mnt = ng.mean(0), nt.mean(0)
r["norm_mean_noguide"] = float(np.linalg.norm(mng)); r["norm_mean_nontargeting"] = float(np.linalg.norm(mnt)); r["cos_means_noguide_vs_nontargeting"] = float(unit(mng) @ unit(mnt))
isko = cr & np.char.startswith(j.astype("U20"), "JCP2022_8") & ~np.isin(j, ["JCP2022_800001", "JCP2022_800002"])
d = pd.DataFrame({"j": j[isko], "i": np.where(isko)[0]}).groupby("j")["i"].apply(np.array); d = d[d.map(len) >= 3]
KO = np.stack([X[v].mean(0) for v in d.values]); syms = pd.read_csv(os.path.join(a.meta, "crispr.csv.gz")).set_index("Metadata_JCP2022").Metadata_Symbol
ksym = [syms.get(k, k) for k in d.index]
mKO = KO.mean(0); r["norm_mean_of_all_KO_profiles"] = float(np.linalg.norm(mKO))
dirv = unit(mnt - mng)
r["cos_meanKO_vs_(nontargeting-noguide)"] = float(unit(mKO) @ dirv)
sel = rng.choice(len(KO), 2000, replace=False); U = unit(KO[sel]); C = U @ U.T
r["mean_cos_between_random_knockout_profiles"] = float((C.sum() - np.trace(C)) / (C.size - len(sel)))
KO2 = KO - mnt                                       # re-referenced to the non-targeting mean
U2 = unit(KO2[sel]); C2 = U2 @ U2.T
r["mean_cos_between_random_knockout_profiles_after_nontargeting_rereference"] = float((C2.sum() - np.trace(C2)) / (C2.size - len(sel)))
# declared primary statistic recomputed with re-referenced knockouts, source_13 compounds
tgc = pd.read_csv(os.path.join(a.target, "JUMP-Target-1_crispr_metadata.tsv"), sep="\t"); G = set(tgc.gene.dropna()) & set(ksym)
tg = pd.read_csv(os.path.join(a.target, "JUMP-Target-2_compound_metadata.tsv"), sep="\t"); tg = tg[tg.control_type.fillna("") != "negcon"].drop_duplicates("InChIKey")
comp = pd.read_csv(os.path.join(a.meta, "compound.csv.gz"))[["Metadata_JCP2022", "Metadata_InChIKey"]]
tg = tg.merge(comp, left_on="InChIKey", right_on="Metadata_InChIKey"); tg["true"] = tg.target_list.fillna("").str.split("|").map(lambda l: [g for g in l if g in G])
design = {r_.Metadata_JCP2022: r_.true for r_ in tg.itertuples() if r_.true}; gs = {}
for c, gl in design.items():
    for g in gl: gs.setdefault(g, []).append(c)
t2 = (pt == "TARGET2") & (src == "source_13") & np.isin(j, tg.Metadata_JCP2022.to_numpy())
cd = pd.DataFrame({"j": j[t2], "i": np.where(t2)[0]}).groupby("j")["i"].apply(np.array); cd = cd[cd.map(len) >= 4]
ids = list(cd.index); M = np.stack([X[v].mean(0) for v in cd.values]); idx = {c: n for n, c in enumerate(ids)}
row = {s: n for n, s in enumerate(ksym)}
def hit_rate(K, Mx, thr=0.10):
    cos = unit(K) @ unit(Mx).T; N = cos.shape[1]; pct = (np.argsort(np.argsort(-cos, 1), 1) + 1) / N
    hits, q = [], []
    for g, cl in gs.items():
        s = [idx[c] for c in cl if c in idx]
        if not s or g not in row: continue
        hits.append(pct[row[g], s].min() <= thr); q.append((pct[:, s].min(1) <= thr).mean())
    H, nm = float(np.mean(hits)), float(np.mean(q)); sims = (rng.random((20000, len(q))) < np.array(q)).mean(1)
    return dict(n=len(q), H=H, null=nm, ratio=H / nm, p=float(((sims >= H - 1e-12).sum() + 1) / 20001))
r["declared_statistic_original_KO"] = hit_rate(KO, M)
r["POSTHOC_statistic_KO_minus_nontargeting_mean"] = hit_rate(KO2, M)
r["POSTHOC_statistic_KO_minus_nontargeting_mean_compounds_minus_their_mean"] = hit_rate(KO2, M - M.mean(0))
json.dump(r, open(os.path.join(a.out, "posthoc_negcon_diagnostic.json"), "w"), indent=1); print(json.dumps(r, indent=1))
