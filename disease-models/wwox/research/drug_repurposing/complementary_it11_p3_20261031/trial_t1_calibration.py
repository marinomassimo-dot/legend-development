#!/usr/bin/env python3
"""IT11 P3 trial T1 (see PRE_DECLARATION.md): matched-design calibration of knockout-to-compound morphological
matching in JUMP cpg0016 and the position of WWOX on the calibrated curve.

Usage:
  trial_t1_calibration.py --profiles ALL_v1.0c_PCA_corrected.parquet --meta JUMP_METADATA_DIR \
      --target JUMP_TARGET_DIR --rephub compound_rephub_annot.csv.gz --depmap OmicsExpression_U2OS.csv.gz \
      --crispr-a CRISPR_v1.0a_PCA_corrected.parquet --crispr-b CRISPR_v1.0b_PCA_corrected.parquet --out RESULTS_DIR
  JUMP_METADATA_DIR holds plate.csv.gz well.csv.gz crispr.csv.gz compound.csv.gz (jump-cellpainting/datasets/metadata).
  JUMP_TARGET_DIR holds JUMP-Target-1_crispr_metadata.tsv and JUMP-Target-2_compound_metadata.tsv.
Run with python -I in an environment having numpy, pandas, pyarrow. Reads public files only; sends nothing anywhere."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, json, os
import numpy as np, pandas as pd, pyarrow.parquet as pq

ap = argparse.ArgumentParser()
for k in ("profiles", "meta", "target", "rephub", "depmap", "crispr-a", "crispr-b", "out"):
    ap.add_argument("--" + k, required=True)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
rng = np.random.default_rng(20261031)
NEG = ["JCP2022_800001", "JCP2022_800002"]
THR_G2C, THR_C2G = 0.10, 0.05
res = {}
import time
_T0 = time.time()
def log(m): print('[%5.0fs] %s' % (time.time() - _T0, m), file=sys.stderr, flush=True)

def unit(v):
    n = np.linalg.norm(v, axis=-1, keepdims=True); return v / np.where(n == 0, 1, n)

# ---------------------------------------------------------------- load
t = pq.read_table(a.profiles).to_pandas()
xc = [c for c in t.columns if c.startswith("X_")]
X = t[xc].to_numpy(np.float32)
meta = t[["Metadata_Source", "Metadata_Plate", "Metadata_Well", "Metadata_JCP2022"]].copy(); del t
pl = pd.read_csv(os.path.join(a.meta, "plate.csv.gz"))
meta = meta.merge(pl, on=["Metadata_Source", "Metadata_Plate"], how="left")
j = meta.Metadata_JCP2022.astype(str).to_numpy()
ptype = meta.Metadata_PlateType.astype(str).to_numpy(); src = meta.Metadata_Source.to_numpy(); plate = meta.Metadata_Plate.to_numpy()
cr = pd.read_csv(os.path.join(a.meta, "crispr.csv.gz")); sym = dict(zip(cr.Metadata_JCP2022, cr.Metadata_Symbol))
res["wells"] = int(len(meta)); res["pcs"] = int(X.shape[1])

log('loaded profiles')
# ---------------------------------------------------------------- knockout profiles (source_13 CRISPR plates)
isko = (ptype == "CRISPR") & (src == "source_13") & np.char.startswith(j.astype("U20"), "JCP2022_8") & ~np.isin(j, NEG)
kdf = pd.DataFrame({"j": j[isko], "i": np.where(isko)[0]})
kidx = kdf.groupby("j")["i"].apply(np.array)
kidx = kidx[kidx.map(len) >= 3]
kids = list(kidx.index); ksym = [sym.get(k, k) for k in kids]
KO_mean = np.stack([X[v].mean(0) for v in kidx.values]); KO_med = np.stack([np.median(X[v], 0) for v in kidx.values])
KO_norm = np.linalg.norm(KO_mean, axis=1)
norm_pct = (pd.Series(KO_norm).rank(method="average") - 1) / (len(KO_norm) - 1) * 100
sym2row = {s: i for i, s in enumerate(ksym)}
res["n_ko_profiles"] = len(kids)
isneg = (ptype == "CRISPR") & (src == "source_13") & np.isin(j, NEG)
res["negcon_wells"] = int(isneg.sum())

# ---------------------------------------------------------------- designed pairs
tgc = pd.read_csv(os.path.join(a.target, "JUMP-Target-1_crispr_metadata.tsv"), sep="\t")
G = set(tgc.gene.dropna()) & set(ksym)
tg = pd.read_csv(os.path.join(a.target, "JUMP-Target-2_compound_metadata.tsv"), sep="\t")
tg = tg[tg.control_type.fillna("") != "negcon"].drop_duplicates("InChIKey")
comp = pd.read_csv(os.path.join(a.meta, "compound.csv.gz"))[["Metadata_JCP2022", "Metadata_InChIKey"]]
tg = tg.merge(comp, left_on="InChIKey", right_on="Metadata_InChIKey", how="inner")
tg["true"] = tg.target_list.fillna("").str.split("|").map(lambda l: [g for g in l if g in G])
design = {r.Metadata_JCP2022: r.true for r in tg.itertuples() if r.true}
res["G_genes_with_ko"] = len(G); res["jump_target2_compounds"] = int(tg.Metadata_JCP2022.nunique())
res["compounds_with_designed_gene"] = len(design); res["designed_pairs"] = int(sum(len(v) for v in design.values()))
gene_sets = {}
for c, gl in design.items():
    for g in gl: gene_sets.setdefault(g, []).append(c)
res["genes_with_designed_compound"] = len(gene_sets)

# ---------------------------------------------------------------- compound profiles per source on TARGET2 plates
t2 = (ptype == "TARGET2") & np.isin(j, tg.Metadata_JCP2022.to_numpy())
cdf = pd.DataFrame({"s": src[t2], "j": j[t2], "i": np.where(t2)[0]})
def comp_profiles(source_filter, stat="mean", min_wells=4):
    d = cdf[cdf.s.isin(source_filter)]
    g = d.groupby("j")["i"].apply(np.array); g = g[g.map(len) >= min_wells]
    f = (lambda v: X[v].mean(0)) if stat == "mean" else (lambda v: np.median(X[v], 0))
    return list(g.index), np.stack([f(v) for v in g.values])
def per_source_profiles():
    out = {}
    for s in sorted(cdf.s.unique()):
        ids, M = comp_profiles([s]); out[s] = (ids, M)
    return out

# ---------------------------------------------------------------- core metric
def g2c(KO, ids, M, genes_sets, stratum_rows=None, thr=THR_G2C, npc=None, center=False, label=""):
    """gene -> compound. KO: (n_ko, D) profiles; ids/M: compounds. Returns dict."""
    KOu, Mu = KO, M
    if npc: KOu, Mu = KO[:, :npc], M[:, :npc]
    if center: KOu = KOu - KOu.mean(0); Mu = Mu - Mu.mean(0)
    cos = unit(KOu) @ unit(Mu).T                      # (n_ko, N)
    N = cos.shape[1]
    rank = np.argsort(np.argsort(-cos, axis=1), axis=1) + 1   # 1 = most similar
    pct = rank / N; pct_neg = (N + 1 - rank) / N
    idx = {c: n for n, c in enumerate(ids)}
    rows = []
    for g, cl in genes_sets.items():
        s = [idx[c] for c in cl if c in idx]
        if not s or g not in sym2row: continue
        r = sym2row[g]
        pg = pct[r, s].min(); pgn = pct_neg[r, s].min()
        allp = pct[:, s].min(1); allpn = pct_neg[:, s].min(1)
        rows.append(dict(gene=g, k=len(s), p=float(pg), p_neg=float(pgn), hit=bool(pg <= thr), hit_neg=bool(pgn <= thr),
                         q_all=float((allp <= thr).mean()), qn_all=float((allpn <= thr).mean()),
                         norm_pct=float(norm_pct[r]), _allp=allp, _allpn=allpn, _row=r))
    return rows, cos

def summarise(rows, mask_fn=None, strat_rows=None, n_mc=20000):
    sub = [r for r in rows if (mask_fn is None or mask_fn(r))]
    n = len(sub)
    if n == 0: return dict(n=0)
    H = np.mean([r["hit"] for r in sub]); Hn = np.mean([r["hit_neg"] for r in sub])
    def null(key_all, rowsel):
        q = np.array([(r[key_all][rowsel] <= THR_G2C).mean() if rowsel is not None else (r[key_all] <= THR_G2C).mean() for r in sub])
        return q
    out = dict(n=n, H=float(H), H_neg=float(Hn))
    for nm, rowsel in (("allrows", None), ("matched", strat_rows)):
        if nm == "matched" and strat_rows is None: continue
        q = null("_allp", rowsel); qn = null("_allpn", rowsel)
        draws = rng.random((n_mc, n)) < q
        sims = draws.mean(1)
        out[f"null_mean_{nm}"] = float(q.mean()); out[f"ratio_{nm}"] = float(H / q.mean()) if q.mean() > 0 else None
        out[f"p_{nm}"] = float(((sims >= H - 1e-12).sum() + 1) / (n_mc + 1))
        sn = (rng.random((n_mc, n)) < qn).mean(1)
        out[f"null_mean_neg_{nm}"] = float(qn.mean()); out[f"p_neg_{nm}"] = float(((sn >= Hn - 1e-12).sum() + 1) / (n_mc + 1))
    return out

def strata_report(rows, tag):
    rep = {}
    npct = norm_pct.to_numpy()
    defs = {"all": (lambda r: True, None), "S_low(<50)": (lambda r: r["norm_pct"] < 50, npct < 50),
            "S_mid(50-80)": (lambda r: 50 <= r["norm_pct"] < 80, (npct >= 50) & (npct < 80)),
            "S_high(>=80)": (lambda r: r["norm_pct"] >= 80, npct >= 80), "S_near(80-95)": (lambda r: 80 <= r["norm_pct"] <= 95, (npct >= 80) & (npct <= 95))}
    for k, (fn, sel) in defs.items(): rep[k] = summarise(rows, fn, sel)
    return rep

def classify(rep):
    o, h, nr = rep["all"], rep["S_high(>=80)"], rep["S_near(80-95)"]
    def ratio(d): return min([d.get("ratio_allrows") or 0, d.get("ratio_matched") or d.get("ratio_allrows") or 0])
    def pmax(d): return max(d.get("p_allrows", 1), d.get("p_matched", d.get("p_allrows", 1)))
    cal = ratio(o) >= 2 and pmax(o) < 0.01
    hi = ratio(h) >= 2 and pmax(h) < 0.05
    near_ok = nr.get("n", 0) >= 15
    near = ratio(nr) >= 1.5
    if cal and hi and near_ok and near: return "USABLE-AT-WWOX-STRENGTH"
    if cal and hi and not near_ok: return "UNDERPOWERED(S_near n<15)"
    return "NOT-DEMONSTRATED-AT-WWOX-STRENGTH" + (" (CALIBRATED-OVERALL)" if cal else " (not calibrated overall)")

def strip(rows): return [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]

log('profiles per source ready; primary')
# ---------------------------------------------------------------- primary
ids13, M13 = comp_profiles(["source_13"])
res["compounds_source13_target2_ge4wells"] = len(ids13)
rows, cos13 = g2c(KO_mean, ids13, M13, gene_sets)
prim = strata_report(rows, "primary"); prim["classification"] = classify(prim)
res["primary_g2c"] = prim
plk = [r for r in strip(rows) if r["gene"] == "PLK1"]; res["PLK1_inside_G"] = plk
rows_noplk = [r for r in rows if r["gene"] != "PLK1"]
res["primary_g2c_without_PLK1"] = {k: v for k, v in strata_report(rows_noplk, "noplk").items() if k in ("all", "S_high(>=80)")}
pd.DataFrame(strip(rows)).sort_values("p").to_csv(os.path.join(a.out, "t1_primary_per_gene.tsv"), sep="\t", index=False)
res["wwox_in_G"] = "WWOX" in G

# compound -> gene (secondary)
idx13 = {c: n for n, c in enumerate(ids13)}
cosT = cos13.T                                    # (N, n_ko)
nko = cosT.shape[1]; c2g_rows = []
for c, gl in design.items():
    if c not in idx13: continue
    rr = [sym2row[g] for g in gl if g in sym2row]
    if not rr: continue
    rk = np.argsort(np.argsort(-cosT[idx13[c]])) + 1
    c2g_rows.append((c, len(rr), float(rk[rr].min() / nko)))
q = np.array([1 - (1 - THR_C2G) ** k for _, k, _ in c2g_rows]); hit = np.array([p <= THR_C2G for _, _, p in c2g_rows])
draws = (rng.random((20000, len(q))) < q).mean(1)
res["secondary_c2g"] = dict(n=len(q), H=float(hit.mean()), null_mean_approx=float(q.mean()), p=float(((draws >= hit.mean() - 1e-12).sum() + 1) / 20001),
                            median_percentile=float(np.median([p for _, _, p in c2g_rows])))

log('primary + c2g done; cross-source')
# ---------------------------------------------------------------- cross-source arm
ps = per_source_profiles(); xs = {}
for s, (ids, M) in ps.items():
    if s == "source_13": continue
    rws, _ = g2c(KO_mean, ids, M, gene_sets)
    rep = strata_report(rws, s); xs[s] = dict(n_compounds=len(ids), all=rep["all"], S_high=rep["S_high(>=80)"], classification=classify(rep))
res["cross_source_per_source"] = xs
# mean over other sources
common = None
for s, (ids, M) in ps.items():
    if s == "source_13": continue
    common = set(ids) if common is None else common & set(ids)
ids_o = sorted(common & set(ids13)); res["cross_source_common_compounds"] = len(ids_o)
Mo = np.mean([unit(np.stack([dict(zip(ps[s][0], ps[s][1]))[c] for c in ids_o])) for s in ps if s != "source_13"], axis=0) if ids_o else None
if Mo is not None:
    rws, _ = g2c(KO_mean, ids_o, Mo, gene_sets); rep = strata_report(rws, "others")
    res["cross_source_mean_of_other_sources"] = dict(all=rep["all"], S_high=rep["S_high(>=80)"], classification=classify(rep))
    # same restricted compound set within source 13, for a like-for-like comparison
    d13 = dict(zip(ids13, M13)); rws13, _ = g2c(KO_mean, ids_o, np.stack([d13[c] for c in ids_o]), gene_sets); rep13 = strata_report(rws13, "s13_restricted")
    res["within_source13_same_compound_set"] = dict(all=rep13["all"], S_high=rep13["S_high(>=80)"], classification=classify(rep13))
# identity retrieval across sources
idr = {}
for s, (ids, M) in ps.items():
    if s == "source_13": continue
    com = [c for c in ids if c in idx13]
    if len(com) < 20: continue
    A = unit(np.stack([M13[idx13[c]] for c in com])); B = unit(np.stack([dict(zip(ids, M))[c] for c in com]))
    S = A @ B.T; rk = np.argsort(np.argsort(-S, axis=1), axis=1).diagonal() + 1
    idr[s] = dict(n=len(com), top5pct=float((rk / len(com) <= 0.05).mean()), top1=float((rk == 1).mean()), mean_cos_same=float(S.diagonal().mean()), mean_cos_diff=float((S.sum() - S.trace()) / (S.size - len(com))))
res["identity_retrieval_source13_vs_source"] = idr

log('cross-source done; sensitivity')
# ---------------------------------------------------------------- sensitivity variants
sens = {}
for nm, kw, KO, (ids, M) in (("V1_50PCs", dict(npc=50), KO_mean, (ids13, M13)), ("V2_centred", dict(center=True), KO_mean, (ids13, M13)),
                             ("V3_median", {}, KO_med, comp_profiles(["source_13"], "median"))):
    rws, _ = g2c(KO, ids, M, gene_sets, **kw); rep = strata_report(rws, nm)
    sens[nm] = dict(all=rep["all"], S_high=rep["S_high(>=80)"], S_near=rep["S_near(80-95)"], classification=classify(rep))
res["sensitivity"] = sens
def high_above(d): return (min(d["S_high"].get("ratio_allrows") or 0, d["S_high"].get("ratio_matched") or d["S_high"].get("ratio_allrows") or 0)) >= 1.5
flags = [high_above(dict(S_high=prim["S_high(>=80)"]))] + [high_above(v) for v in sens.values()]
if "cross_source_mean_of_other_sources" in res: flags.append(high_above(res["cross_source_mean_of_other_sources"]))
res["stability_S_high_above_1.5x_null"] = dict(flags=flags, n_true=int(sum(flags)), of=len(flags), stable=bool(sum(flags) in (0, 1, len(flags) - 1, len(flags))))

log('sensitivity done; broad panel')
# ---------------------------------------------------------------- broad panel (cross-source, secondary)
rh = pd.read_csv(a.rephub); rh = rh[rh.Metadata_target.notna()].drop_duplicates("Metadata_InChIKey")
comp_all = pd.read_csv(os.path.join(a.meta, "compound.csv.gz"))[["Metadata_JCP2022", "Metadata_InChIKey"]].merge(rh, on="Metadata_InChIKey", how="inner")
isc = (ptype == "COMPOUND") & np.isin(j, comp_all.Metadata_JCP2022.to_numpy())
d = pd.DataFrame({"j": j[isc], "pl": plate[isc], "i": np.where(isc)[0]})
g = d.groupby("j").agg(i=("i", lambda s: np.array(s)), npl=("pl", "nunique")); g = g[g.npl >= 2]
idsr = list(g.index); Mr = np.stack([X[v].mean(0) for v in g.i.values])
mo = comp_all.set_index("Metadata_JCP2022")
bset = {}
for c in idsr:
    mt = str(mo.loc[c, "Metadata_moa"]).lower()
    if any(w in mt for w in ("inhibitor", "antagonist", "blocker", "depleting")):
        for gg in str(mo.loc[c, "Metadata_target"]).split("|"):
            if gg in sym2row: bset.setdefault(gg, []).append(c)
rwsb, _ = g2c(KO_mean, idsr, Mr, bset, thr=0.05)
# g2c uses THR_G2C for hit flags; recompute with 5 percent
def rehit(rows, thr):
    for r in rows:
        r["hit"] = r["p"] <= thr; r["hit_neg"] = r["p_neg"] <= thr; r["q_all"] = float((r["_allp"] <= thr).mean())
    return rows
rwsb = rehit(rwsb, 0.05)
def summ_thr(rows, thr, fn=None, sel=None, n_mc=20000):
    sub = [r for r in rows if fn is None or fn(r)]; n = len(sub)
    if not n: return dict(n=0)
    H = np.mean([r["hit"] for r in sub]); q = np.array([(r["_allp"] <= thr).mean() if sel is None else (r["_allp"][sel] <= thr).mean() for r in sub])
    sims = (rng.random((n_mc, n)) < q).mean(1)
    return dict(n=n, H=float(H), null_mean=float(q.mean()), ratio=float(H / q.mean()), p=float(((sims >= H - 1e-12).sum() + 1) / (n_mc + 1)))
npct = norm_pct.to_numpy()
res["broad_panel_rephub"] = dict(universe=len(idsr), genes=len(rwsb), all=summ_thr(rwsb, 0.05),
                                 S_high=summ_thr(rwsb, 0.05, lambda r: r["norm_pct"] >= 80, npct >= 80),
                                 S_near=summ_thr(rwsb, 0.05, lambda r: 80 <= r["norm_pct"] <= 95, (npct >= 80) & (npct <= 95)),
                                 S_low=summ_thr(rwsb, 0.05, lambda r: r["norm_pct"] < 50, npct < 50))
dm = pd.read_csv(a.depmap).set_index("Symbol").TPM.to_dict()
expr = lambda r: dm.get(r["gene"], 0) >= 1
res["broad_panel_rephub"]["expressed_U2OS"] = summ_thr(rwsb, 0.05, expr)
res["broad_panel_rephub"]["not_expressed_U2OS"] = summ_thr(rwsb, 0.05, lambda r: not expr(r))
res["primary_g2c_expressed_U2OS"] = summarise(rows, expr)

log('broad panel done; WWOX arm')
# ---------------------------------------------------------------- WWOX arm
def ap_scores(U, pos_groups, negU):
    """mean AP per group: each own well queries; positives = other own wells; background = negcon wells."""
    out = []
    for gi in pos_groups:
        P = U[gi]; aps = []
        for q in range(len(gi)):
            others = np.delete(np.arange(len(gi)), q)
            s_pos = P[others] @ P[q]; s_neg = negU @ P[q]
            allv = np.concatenate([s_pos, s_neg]); lab = np.concatenate([np.ones(len(s_pos)), np.zeros(len(s_neg))])
            o = np.argsort(-allv); l = lab[o]; cum = np.cumsum(l); prec = cum / (np.arange(len(l)) + 1)
            aps.append((prec * l).sum() / l.sum())
        out.append(np.mean(aps))
    return np.array(out)
def detect(Xall, jj, ptype_, src_, label, nperm=2000):
    isk = (ptype_ == "CRISPR") & (src_ == "source_13") & np.char.startswith(jj.astype("U20"), "JCP2022_8") & ~np.isin(jj, NEG)
    ng = (ptype_ == "CRISPR") & (src_ == "source_13") & np.isin(jj, NEG)
    U = unit(Xall); negU = U[ng]
    dfk = pd.DataFrame({"j": jj[isk], "i": np.where(isk)[0]}).groupby("j")["i"].apply(np.array); dfk = dfk[dfk.map(len) >= 3]
    obs = ap_scores(U, [v for v in dfk.values], negU)
    # null: random groups of 5 negcon wells vs the remaining negcon wells
    ni = np.where(ng)[0]; nullap = []
    for _ in range(nperm):
        pick = rng.choice(len(ni), 5, replace=False); rest = np.delete(np.arange(len(ni)), pick)
        nullap.append(ap_scores(np.concatenate([U[ni[pick]], U[ni[rest]]]), [np.arange(5)], U[ni[rest]])[0])
    nullap = np.array(nullap)
    pv = (np.searchsorted(np.sort(nullap), obs, side="left")); pv = 1 - pv / len(nullap); pv = np.maximum(pv, 1 / (len(nullap) + 1))
    order = np.argsort(pv); m = len(pv); q = np.empty(m); prev = 1.0
    for rank_i in range(m - 1, -1, -1):
        qq = min(prev, pv[order[rank_i]] * m / (rank_i + 1)); q[order[rank_i]] = qq; prev = qq
    gl = [sym.get(k, k) for k in dfk.index]; w = gl.index("WWOX"); p1 = gl.index("PLK1") if "PLK1" in gl else None
    nm = np.array([np.linalg.norm(Xall[v].mean(0)) for v in dfk.values]); npc_ = (pd.Series(nm).rank() - 1) / (len(nm) - 1) * 100
    # leave-one-run-out cosine for WWOX and distribution over all genes
    def loro(v):
        P = U[v]; return float(np.mean([P[q_] @ unit(np.delete(P, q_, 0).mean(0)) for q_ in range(len(v))]))
    lo = np.array([loro(v) for v in dfk.values])
    r = dict(file=label, n_genes=len(gl), wwox_wells=int(len(dfk.values[w])), wwox_mAP=float(obs[w]), wwox_p=float(pv[w]), wwox_q=float(q[w]),
             wwox_detected=bool(q[w] < 0.05), genes_detected_q05=int((q < 0.05).sum()), wwox_mAP_percentile=float((obs < obs[w]).mean() * 100),
             wwox_norm=float(nm[w]), wwox_norm_percentile=float(npc_[w]), wwox_loro_cos=float(lo[w]), wwox_loro_percentile=float((lo < lo[w]).mean() * 100),
             null_mAP_mean=float(nullap.mean()), null_mAP_p95=float(np.percentile(nullap, 95)), n_perm=int(nperm))
    if p1 is not None: r.update(plk1_mAP=float(obs[p1]), plk1_q=float(q[p1]), plk1_norm_percentile=float(npc_[p1]), plk1_loro_percentile=float((lo < lo[p1]).mean() * 100))
    return r
res["wwox_detectability"] = {"ALL_v1.0c": detect(X, j, ptype, src, "ALL v1.0c PCA_corrected")}
log("detect ALL done")
for lab, f in (("CRISPR_v1.0a", getattr(a, "crispr_a")), ("CRISPR_v1.0b", getattr(a, "crispr_b"))):
    tt = pq.read_table(f).to_pandas(); xx = tt[[c for c in tt.columns if c.startswith("X_")]].to_numpy(np.float32)
    m2 = tt[["Metadata_Source", "Metadata_Plate", "Metadata_JCP2022"]].merge(pl, on=["Metadata_Source", "Metadata_Plate"], how="left")
    res["wwox_detectability"][lab] = detect(xx, m2.Metadata_JCP2022.astype(str).to_numpy(), m2.Metadata_PlateType.astype(str).to_numpy(), m2.Metadata_Source.to_numpy(), lab)

log('detectability done; lists')
# ---------------------------------------------------------------- WWOX query lists and generic-activity checks (always computed; interpretation is conditional)
wr = sym2row["WWOX"]; cw = cos13[wr]; order = np.argsort(-cw)
tg_names = dict(zip(tg.Metadata_JCP2022, tg.pert_iname))
lst = [dict(direction="most_similar", rank=n + 1, jcp=ids13[o], name=tg_names.get(ids13[o]), cos=float(cw[o])) for n, o in enumerate(order[:30])]
lst += [dict(direction="most_opposed", rank=n + 1, jcp=ids13[o], name=tg_names.get(ids13[o]), cos=float(cw[o])) for n, o in enumerate(order[::-1][:30])]
pd.DataFrame(lst).to_csv(os.path.join(a.out, "t1_wwox_query_lists_NOT_INTERPRETED_unless_declared_outcome.tsv"), sep="\t", index=False)
cn = np.linalg.norm(M13, axis=1)
res["wwox_generic_activity"] = dict(corr_cos_vs_compound_norm=float(np.corrcoef(cw, cn)[0, 1]), n_compounds=len(ids13))
top = set(order[:30]); ov = []
for r_ in rng.choice(len(ksym), 200, replace=False):
    ov.append(len(top & set(np.argsort(-cos13[r_])[:30])))
res["wwox_generic_activity"]["top30_overlap_with_random_gene_mean"] = float(np.mean(ov)); res["wwox_generic_activity"]["top30_overlap_max"] = int(np.max(ov))
res["wwox_expression_U2OS_log2tpm1"] = float(dm.get("WWOX", np.nan))

json.dump(res, open(os.path.join(a.out, "t1_results.json"), "w"), indent=1, default=float)
print(json.dumps({k: res[k] for k in ("primary_g2c", "wwox_detectability", "stability_S_high_above_1.5x_null")}, indent=1, default=float)[:6000])
