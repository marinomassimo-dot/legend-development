#!/usr/bin/env python3
"""Iteration 3 (scientist-d, SD-IT3-LINCS-LOCAL-20261027): OFFLINE evaluation of the GSE156243 WWOX-KO query sets S1/S3/K1/K2/N1-N3
against the whole GSE92742 level 5 (MODZ) matrix, so that no service cap applies, with per-signature permutation nulls built from the same
matrix. Declaration: lincs_it3_local_level5_20261027.md (written before the first run). Not WWOX evidence; a reversal score is not rescue.

Usage:  lincs_it3_local_level5.py extract <this dir> <geo dir> <cache dir>   decompress-free read of the gctx (see the md for the gunzip step)
        lincs_it3_local_level5.py score   <this dir> <geo dir> <cache dir>   gene-set scores of every extracted signature, 1000 matched-random + 1000 label-permuted nulls
        lincs_it3_local_level5.py report  <this dir> <geo dir> <cache dir>   per-signature z, hit counts, covariates, funnel, WWOX CGS comparator -> derived/lincs_it3_*
<geo dir>   holds GSE92742_Broad_LINCS_{gene_info,sig_info,sig_metrics,pert_info,cell_info}.txt.gz and (for 'extract') the gunzipped
            GSE92742_Broad_LINCS_Level5_COMPZ.MODZ_n473647x12328.gctx (gunzip -k the .gz; checksum recorded in the md).
<cache dir> scratch, git-ignored; receives extract.npy (float32, rows = trt_cp and trt_sh.cgs signatures), extract_rows.tsv, scores.npy.
Needs numpy and h5py (h5py 3.16.0 used). Deterministic: seeds fixed below. --help and no arguments print this text and exit."""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 5 or _sys.argv[1] not in ("extract", "score", "report"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, json, math, os, random, statistics, time
import numpy as np
STAGE, G, D, C = _sys.argv[1:5]
GCTX = "GSE92742_Broad_LINCS_Level5_COMPZ.MODZ_n473647x12328.gctx"
COUNTS = "/home/desktop/legend-development/files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"
NRAND, SEED = 1000, 20261201
NAMED = ["S1", "S3", "K1", "K2", "N1", "N2", "N3"]
os.makedirs(C, exist_ok=True)
def tab(fn): return list(csv.DictReader(gzip.open(f"{D}/{fn}", "rt"), delimiter="\t"))
def log(*a): print(time.strftime("%H:%M:%S"), *a, flush=True)

# ------------------------------------------------------------------ stage 1: extract rows of interest
if STAGE == "extract":
    import h5py
    f = h5py.File(f"{D}/{GCTX}", "r")
    m = f["0/DATA/0/matrix"]; col = [x.decode() for x in f["0/META/COL/id"][:]]; row = [x.decode() for x in f["0/META/ROW/id"][:]]
    log("matrix", m.shape, "chunks", m.chunks, "dtype", m.dtype, "cols", len(col), "rows", len(row))
    assert m.shape == (len(col), len(row)), "unexpected orientation"
    info = {r["sig_id"]: r for r in tab("GSE92742_Broad_LINCS_sig_info.txt.gz")}
    keep = [i for i, s in enumerate(col) if info.get(s, {}).get("pert_type") in ("trt_cp", "trt_sh.cgs")]
    log("signatures in matrix", len(col), "kept (trt_cp + trt_sh.cgs)", len(keep))
    out = np.lib.format.open_memmap(f"{C}/extract.npy", mode="w+", dtype="float32", shape=(len(keep), len(row)))
    step, w, t0 = 5000, 0, time.time()
    for a in range(0, len(col), step):
        sel = [i for i in keep if a <= i < a + step]
        if not sel: continue
        blk = m[a:a + step, :]
        out[w:w + len(sel)] = blk[[i - a for i in sel]]; w += len(sel)
        if (a // step) % 10 == 0: log("rows read", a, "elapsed s", round(time.time() - t0))
    out.flush(); assert w == len(keep)
    with open(f"{C}/extract_rows.tsv", "w") as o:
        o.write("row\tsig_id\n"); [o.write(f"{k}\t{col[i]}\n") for k, i in enumerate(keep)]
    json.dump({"entrez_columns": row}, open(f"{C}/extract_genes.json", "w"))
    log("extract done", out.shape); raise SystemExit(0)

# ------------------------------------------------------------------ shared inputs
genes = json.load(open(f"{C}/extract_genes.json"))["entrez_columns"]
gi = {r["pr_gene_symbol"]: r["pr_gene_id"] for r in tab("GSE92742_Broad_LINCS_gene_info.txt.gz")}
gcol = {e: k for k, e in enumerate(genes)}
q = {**json.load(open(f"{G}/derived/query_sets.json")), **json.load(open(f"{G}/derived/query_sets_it2_nulls.json"))}
def cols(symbols): return [gcol[gi[s]] for s in symbols if s in gi and gi[s] in gcol]
SETS = {k: (cols(q[k]["up"]), cols(q[k]["down"])) for k in NAMED}
s1u, s1d = SETS["S1"]; rnd = random.Random(SEED)
# expression deciles of the organoid contrast (mean log2 CPM over the six libraries) for matched random draws
cnt = {}
with gzip.open(COUNTS, "rt") as fh:
    fh.readline()
    for l in fh:
        x = l.rstrip("\n").split("\t"); cnt[x[0]] = [float(v) for v in x[1:]]
tot = [sum(v[i] for v in cnt.values()) for i in range(6)]
meanl = {g: statistics.mean(math.log2(v[i] / tot[i] * 1e6 + 1) for i in range(6)) for g, v in cnt.items()}
sym_of = {gcol[e]: s for s, e in gi.items() if e in gcol}
pool_syms = sorted(s for s in sym_of.values() if s in meanl)
order = sorted(pool_syms, key=lambda s: meanl[s]); dec = {s: min(9, i * 10 // len(order)) for i, s in enumerate(order)}
s1set = set(s1u) | set(s1d); pool = {}
for c in sorted(sym_of):
    s = sym_of[c]
    if s in dec and c not in s1set: pool.setdefault(dec[s], []).append(c)
def matched():
    used, out = set(), []
    for arm in (s1u, s1d):
        a = []
        for c in arm:
            cand = [x for x in pool[dec.get(sym_of.get(c), 0)] if x not in used]; x = rnd.choice(cand); used.add(x); a.append(x)
        out.append(a)
    return tuple(out)
def permuted():
    allg = s1u + s1d; rnd.shuffle(allg); return allg[:len(s1u)], allg[len(s1u):]
rnd = random.Random(SEED)
MSETS = [matched() for _ in range(NRAND)]; PSETS = [permuted() for _ in range(NRAND)]
ALL = [SETS[k] for k in NAMED] + MSETS + PSETS
names = NAMED + [f"M{i:04d}" for i in range(NRAND)] + [f"P{i:04d}" for i in range(NRAND)]
rows = [l.rstrip("\n").split("\t") for l in open(f"{C}/extract_rows.tsv")][1:]
sigs = [r[1] for r in rows]; sigpos = {s: i for i, s in enumerate(sigs)}

# ------------------------------------------------------------------ stage 2: scores
if STAGE == "score":
    X = np.load(f"{C}/extract.npy", mmap_mode="r")
    W = np.zeros((len(genes), len(ALL)), dtype="float32")
    for j, (u, d) in enumerate(ALL):
        W[u, j] += 1.0 / len(u); W[d, j] -= 1.0 / len(d)
    S = np.lib.format.open_memmap(f"{C}/scores.npy", mode="w+", dtype="float32", shape=(X.shape[0], len(ALL))); stat = np.zeros((X.shape[0], 2), dtype="float32")
    t0 = time.time()
    for a in range(0, X.shape[0], 2000):
        blk = np.asarray(X[a:a + 2000]); S[a:a + 2000] = blk @ W
        stat[a:a + 2000, 0] = np.abs(blk).mean(1); stat[a:a + 2000, 1] = (np.abs(blk) > 2).mean(1)
        if (a // 2000) % 10 == 0: log("scored", a, "elapsed s", round(time.time() - t0))
    # PCA of compound signatures on a fixed random subsample (centred), then projection of every row
    rr = np.random.RandomState(SEED)
    sub = np.sort(rr.choice(X.shape[0], 10000, replace=False)); A = np.asarray(X[sub]); mu = A.mean(0); A -= mu
    U, s, Vt = np.linalg.svd(A, full_matrices=False); V = Vt[:5].T.astype("float32"); del A
    P = np.zeros((X.shape[0], 5), dtype="float32")
    for a in range(0, X.shape[0], 2000): P[a:a + 2000] = (np.asarray(X[a:a + 2000]) - mu) @ V
    S.flush(); np.save(f"{C}/rowstats.npy", stat); np.save(f"{C}/pcs.npy", P)
    json.dump({"sets": names, "pca_var_explained_top5": [float(x) for x in (s[:5] ** 2 / (s ** 2).sum())],
               "n_in_space": {k: [len(SETS[k][0]), len(SETS[k][1])] for k in NAMED}}, open(f"{C}/score_meta.json", "w"))
    log("score done", S.shape); raise SystemExit(0)

# ------------------------------------------------------------------ stage 3: report
S = np.load(f"{C}/scores.npy"); stat = np.load(f"{C}/rowstats.npy"); P = np.load(f"{C}/pcs.npy"); meta = json.load(open(f"{C}/score_meta.json"))
info = {r["sig_id"]: r for r in tab("GSE92742_Broad_LINCS_sig_info.txt.gz")}
met = {r["sig_id"]: r for r in tab("GSE92742_Broad_LINCS_sig_metrics.txt.gz")}
ptype = np.array([info[s]["pert_type"] for s in sigs]); cp = np.where(ptype == "trt_cp")[0]; cgs = np.where(ptype == "trt_sh.cgs")[0]
nN = len(NAMED); M = S[:, nN:nN + NRAND]; Pm = S[:, nN + NRAND:]
mM, sM = M.mean(1), M.std(1) + 1e-9; mP, sP = Pm.mean(1), Pm.std(1) + 1e-9
def zM(j): return (S[:, j] - mM) / sM
def zP(j): return (S[:, j] - mP) / sP
ZM = {k: zM(i) for i, k in enumerate(NAMED)}; ZP = {k: zP(i) for i, k in enumerate(NAMED)}
out = {"stage": "report", "n_signatures_extracted": len(sigs), "n_trt_cp": int(len(cp)), "n_trt_sh_cgs": int(len(cgs)), "n_in_space_up_down": meta["n_in_space"],
       "pca_var_explained_top5": meta["pca_var_explained_top5"], "nrand": NRAND, "seed": SEED}
# 3a hit counts per set over compound signatures (both tails), against the distribution of the same count for the matched-random sets themselves
Zr = (M[cp] - mM[cp, None]) / sM[cp, None]
rl, rh = (Zr <= -3).sum(0), (Zr >= 3).sum(0)
def pct(v, x): return float((v < x).mean())
cnt_tab = {}
for k in NAMED:
    lo, hi = int((ZM[k][cp] <= -3).sum()), int((ZM[k][cp] >= 3).sum())
    cnt_tab[k] = {"reverse_zM_le_-3": lo, "mimic_zM_ge_3": hi, "pct_of_random_sets_below_rev": pct(rl, lo), "pct_of_random_sets_below_mim": pct(rh, hi)}
out["hit_counts_compound_signatures"] = {"sets": cnt_tab, "random_matched_reverse_quantiles_50_95_99_max": [float(np.quantile(rl, x)) for x in (.5, .95, .99, 1)],
                                          "random_matched_mimic_quantiles_50_95_99_max": [float(np.quantile(rh, x)) for x in (.5, .95, .99, 1)]}
# 3b score-vector correlations across compound signatures (shared axis between S1 and the pseudo-contrasts / nulls)
def corr(a, b): return float(np.corrcoef(a[cp], b[cp])[0, 1])
out["raw_score_correlation_with_S1_over_compound_signatures"] = {k: corr(S[:, 0], S[:, i]) for i, k in enumerate(NAMED) if k != "S1"}
out["raw_score_correlation_with_S1_random_matched_median_p5_p95"] = [float(x) for x in np.quantile([corr(S[:, 0], S[:, nN + j]) for j in range(100)], [.5, .05, .95])]
# 3c covariates of stress / proliferation / transcriptional activity and their explanatory power for the S1 score
def f(x, d=np.nan):
    try: return float(x)
    except Exception: return d
tas = np.array([f(met[s]["tas"]) for s in sigs]); cc = np.array([f(met[s]["distil_cc_q75"]) for s in sigs]); ng = np.array([f(met[s]["ngenes_modulated_up_lm"]) + f(met[s]["ngenes_modulated_dn_lm"]) for s in sigs])
cc[cc < -600] = np.nan
dose = np.array([f(info[s]["pert_dose"]) if f(info[s]["pert_dose"]) > 0 else np.nan for s in sigs]); tm = np.array([f(info[s]["pert_time"]) for s in sigs])
cov = np.column_stack([tas, ng, stat[:, 0], stat[:, 1], P[:, :3], np.log10(dose), tm])
covn = ["tas", "ngenes_modulated_lm", "mean_abs_z", "frac_abs_z_gt2", "PC1", "PC2", "PC3", "log10_dose", "time_h"]
ok = np.where(np.isfinite(cov[cp]).all(1))[0]; idx = cp[ok]
Xd = np.column_stack([np.ones(len(idx)), (cov[idx] - cov[idx].mean(0)) / cov[idx].std(0)])
def adjust(z):
    b, *_ = np.linalg.lstsq(Xd, z[idx], rcond=None); res = z[idx] - Xd @ b
    return res, float(1 - res.var() / z[idx].var()), dict(zip(["intercept"] + covn, [round(float(v), 3) for v in b]))
resid, r2 = {}, {}
for k in ("S1", "K1", "K2"):
    resid[k], r2[k], coef = adjust(ZM[k])
    if k == "S1": out["S1_zM_regression_coefficients_standardised_covariates"] = coef
out["covariate_R2_of_zM_over_compound_signatures"] = r2; out["covariate_names"] = covn; out["n_compound_signatures_with_all_covariates"] = int(len(idx))
# 3d compound-level funnel, applied identically to S1, the pseudo-contrasts, the N sets and random matched sets (paired control)
comp = np.array([info[sigs[i]]["pert_id"] for i in idx]); cell = np.array([info[sigs[i]]["cell_id"] for i in idx]); iname = {}
for i in idx: iname.setdefault(info[sigs[i]]["pert_id"], info[sigs[i]]["pert_iname"])
cellcode = np.unique(cell, return_inverse=True)[1]; uc, inv = np.unique(comp, return_inverse=True); srt = np.argsort(inv, kind="stable"); starts = np.r_[0, np.cumsum(np.bincount(inv))[:-1]]
Zm_idx = (M[idx] - mM[idx, None]) / sM[idx, None]
def cmin(Z, sign):  # per-compound extreme over signatures; Z is (len(idx), ncols)
    return np.minimum.reduceat(sign * Z[srt], starts, axis=0)
cm = cmin(Zm_idx, 1)  # most negative z per compound for each random set
top100 = np.argsort(cm, axis=0)[:100]; fh_rev = np.bincount(top100.ravel(), minlength=len(uc)) / NRAND
cmx = cmin(Zm_idx, -1); top100x = np.argsort(cmx, axis=0)[:100]; fh_mim = np.bincount(top100x.ravel(), minlength=len(uc)) / NRAND
del Zm_idx, cm, cmx, Zr
def ncell_hits(mask):  # distinct cell lines with a hit, per compound
    h = np.where(mask)[0]; key = np.unique(inv[h].astype(np.int64) * 100000 + cellcode[h])
    return np.bincount(key // 100000, minlength=len(uc))
def funnel(zm, zp, res, sign, kset):
    thr = -3 if sign == 1 else 3
    t = lambda a: (a <= thr) if sign == 1 else (a >= thr)
    s1 = t(zm[idx]); s2 = s1 & t(zp[idx]); s3 = s2 & t(res)
    n1, n2, n3 = ncell_hits(s1), ncell_hits(s2), ncell_hits(s3)
    kshared = np.zeros(len(uc), bool)
    for kk in kset:
        h = t(ZM[kk][idx]); kshared[np.unique(inv[h])] = True
    fh = (fh_rev if sign == 1 else fh_mim) >= 0.05
    steps = {"C0_any_signature_zM": int((np.bincount(inv[s1], minlength=len(uc)) > 0).sum()), "C1_ge2_cells_zM": int((n1 >= 2).sum()), "C2_and_label_perm_zP": int((n2 >= 2).sum()),
             "C3_and_covariate_adjusted": int((n3 >= 2).sum()), "C4_not_hit_in_other_pseudo_contrasts": int(((n3 >= 2) & ~kshared).sum()),
             "C5_not_frequent_hitter_ge5pct": int(((n3 >= 2) & ~kshared & ~fh).sum())}
    return steps, np.where((n3 >= 2) & ~kshared & ~fh)[0], n1, n2, n3, kshared
res_all = {k: resid[k] for k in resid}
fun = {}
for tail, sign in (("reverse", 1), ("mimic", -1)):
    fun[tail] = {}
    for k in ("S1", "S3", "K1", "K2", "N1", "N2", "N3"):
        rs = resid.get(k)
        if rs is None: rs = adjust(ZM[k])[0]
        fun[tail][k] = funnel(ZM[k], ZP[k], rs, sign, [x for x in ("K1", "K2") if x != k])[0]
    # random matched sets: the same funnel (30 draws), residualised the same way
    rows_ = []
    for j in range(30):
        zmj = (S[:, nN + j] - mM) / sM; zpj = (S[:, nN + j] - mP) / sP; ZMj = zmj; rs = adjust(zmj)[0]
        rows_.append(funnel(zmj, zpj, rs, sign, ["K1", "K2"])[0])
    fun[tail]["random_matched_30_draws_median_and_max"] = {c: [float(np.median([r[c] for r in rows_])), int(max(r[c] for r in rows_))] for c in rows_[0]}
out["funnel_compounds_surviving_each_stage"] = fun
# 3e the compounds that survive for S1 (both tails) with identity, cells, context
tabl = []
for tail, sign in (("reverse", 1), ("mimic", -1)):
    st, surv, n1, n2, n3, ks = funnel(ZM["S1"], ZP["S1"], resid["S1"], sign, ["K1", "K2"])
    thr = -3 if sign == 1 else 3
    for u in surv:
        m_ = (inv == u) & ((ZM["S1"][idx] <= thr) if sign == 1 else (ZM["S1"][idx] >= thr)) & ((resid["S1"] <= thr) if sign == 1 else (resid["S1"] >= thr))
        sg = [sigs[idx[i]] for i in np.where(m_)[0]]
        tabl.append({"tail": tail, "pert_id": uc[u], "pert_iname": iname[uc[u]], "cells_with_hit": sorted({info[s]["cell_id"] for s in sg}),
                     "signatures": [{"sig_id": s, "dose": info[s]["pert_idose"], "time": info[s]["pert_itime"], "zM": round(float(ZM["S1"][sigpos[s]]), 2), "zP": round(float(ZP["S1"][sigpos[s]]), 2)} for s in sg][:6],
                     "frequent_hitter_rate_random_top100": round(float((fh_rev if sign == 1 else fh_mim)[u]), 4)})
out["S1_survivors_n"] = {t: sum(1 for r in tabl if r["tail"] == t) for t in ("reverse", "mimic")}
with open(f"{G}/derived/lincs_it3_S1_survivors.tsv", "w") as o:
    o.write("tail\tpert_id\tpert_iname\tcells_with_hit\tn_sigs_shown\tfirst_sig\tfirst_dose\tfirst_time\tfirst_zM\tfirst_zP\tfreq_random_top100\n")
    for r in tabl:
        s0 = r["signatures"][0]; o.write("\t".join(str(x) for x in (r["tail"], r["pert_id"], r["pert_iname"], ",".join(r["cells_with_hit"]), len(r["signatures"]), s0["sig_id"], s0["dose"], s0["time"], s0["zM"], s0["zP"], r["frequent_hitter_rate_random_top100"])) + "\n")
# 3f context strata of the S1 hits (raw zM <= -3 and >= 3, all compound signatures): cell line, time, dose, with the share of all compound signatures as denominator
def strata(field, fn):
    allv = np.array([fn(info[sigs[i]][field]) for i in cp]); res = {}
    for v in sorted(set(allv.tolist()), key=lambda x: str(x)):
        m_ = allv == v; n = int(m_.sum())
        if n < 500: continue
        res[str(v)] = {"n_signatures": n, "rev_hit_rate": round(float((ZM["S1"][cp][m_] <= -3).mean()), 4), "mim_hit_rate": round(float((ZM["S1"][cp][m_] >= 3).mean()), 4),
                       "K1_rev": round(float((ZM["K1"][cp][m_] <= -3).mean()), 4), "K1_mim": round(float((ZM["K1"][cp][m_] >= 3).mean()), 4)}
    return res
out["context_hit_rates"] = {"cell_id": strata("cell_id", str), "pert_time_h": strata("pert_time", str), "pert_idose": strata("pert_idose", str)}
# 3g WWOX shRNA CGS signatures as a genetic comparator (knockdown resembling the knockout contrast means a positive score / mimic direction)
ci = [i for i in cgs if info[sigs[i]]["pert_iname"] == "WWOX"]
bg = {k: {"n_cgs": int(len(cgs)), "pct_zM_ge_3": round(float((ZM[k][cgs] >= 3).mean()), 4), "pct_zM_le_-3": round(float((ZM[k][cgs] <= -3).mean()), 4)} for k in ("S1", "K1", "K2")}
def pr(k, i): return round(float((ZM[k][cgs] < ZM[k][i]).mean()), 3)
cgs_cell = np.array([info[sigs[i]]["cell_id"] for i in cgs])
def prc(k, i):  # percentile among the CGS signatures of the SAME cell line (cross-context control, added 2026-10-28, see the md)
    m_ = cgs_cell == info[sigs[i]]["cell_id"]; return round(float((ZM[k][cgs][m_] < ZM[k][i]).mean()), 3), int(m_.sum())
for k in bg: bg[k]["pct_zM_ge_2"] = round(float((ZM[k][cgs] >= 2).mean()), 4)
out["WWOX_CGS_signatures"] = {"background_over_all_cgs": bg, "rows": [{"sig_id": sigs[i], "cell": info[sigs[i]]["cell_id"], "time_h": info[sigs[i]]["pert_time"], "S1_raw": round(float(S[i, 0]), 3), "S1_zM": round(float(ZM["S1"][i]), 2),
                                                                       "S1_zP": round(float(ZP["S1"][i]), 2), "S1_zM_percentile_among_cgs": pr("S1", i), "S1_zM_percentile_same_cell_line_and_n": prc("S1", i), "K1_zM": round(float(ZM["K1"][i]), 2), "K2_zM": round(float(ZM["K2"][i]), 2),
                                                                       "S3_zM": round(float(ZM["S3"][i]), 2)} for i in ci]}
json.dump(out, open(f"{G}/derived/lincs_it3_local_level5_summary.json", "w"), indent=1)
log("report done"); print(json.dumps({k: out[k] for k in ("hit_counts_compound_signatures", "raw_score_correlation_with_S1_over_compound_signatures", "covariate_R2_of_zM_over_compound_signatures", "funnel_compounds_surviving_each_stage", "S1_survivors_n")}, indent=1))
