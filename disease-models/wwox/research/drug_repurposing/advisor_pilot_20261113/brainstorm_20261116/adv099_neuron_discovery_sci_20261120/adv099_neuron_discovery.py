#!/usr/bin/env python3
"""ADV-099: unbiased neuron-internal discovery, as registered in
PREREGISTRATION_ADV099_NEURON_DISCOVERY_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md
(sha256 63faafa4912961209b040e7a0029382898d3d997544587b35229087bf312dde2).

Hypothesis level; no dose; not medical advice. Held data only, no network.
Usage: adv099_neuron_discovery.py --files FILES_DIR --out OUT_DIR [--selftest]
(--selftest runs the same code on a 3,000-gene subset to catch crashes; it is not the registered run.)
"""
import argparse
import csv
import gzip
import math
import os
import re

import numpy as np

SEED = 20261120
LATE = "Grin2a Slc12a5 Nrgn Camk2a Scn8a".split()
REF = "Snap25 Rbfox3 Syt1 Stmn2 Tubb3 Map2".split()
STAGES = {"OPC": "Pdgfra Cspg4 Cspg5 Pcdh15".split(), "COP": "Gpr17 Neu4 Bmp4 Vcan".split(),
          "NFOL": "Tcf7l2 Itpr2 Enpp6 Bcas1 Tmem2 Fyn Casr".split(), "MFOL": "Mal Mog Opalin Serinc5 Mag".split(),
          "MOL": "Klk6 Apod Pmp22 Slc5a11 Ermn Hapln2".split()}
CLASSES = {"excitatory": "Slc17a7 Camk2a Satb2".split(), "inhibitory": "Gad1 Gad2 Slc32a1".split(),
           "astrocyte": "Aqp4 Aldh1l1 Slc1a2".split(), "microglia": "Cx3cr1 P2ry12 Csf1r".split(), **STAGES}
NEURON_CLASSES = ["excitatory", "inhibitory"]
GLIAL = ["astrocyte", "microglia"] + list(STAGES)
PANEL_O_NEU = "STMN2 DCX TUBB3 MAP2 SNAP25 SYT1".split()
PANEL_O_PROG = "SOX2 PAX6 HES1 VIM NES FABP7".split()
THR_N, THR_O, THR_GROUP = 0.25, 0.5, 0.25
DET_FRAC, STAB_SPLITS, STAB_MIN = 0.10, 20, 18
NULL_N = 2000


def read_mtx(files, tag):
    feats = [l.rstrip("\n").split("\t")[1] for l in gzip.open(os.path.join(files, f"geo/GSE158684/GSE158684_{tag}_filtered_features.tsv.gz"), "rt")]
    with gzip.open(os.path.join(files, f"geo/GSE158684/GSE158684_{tag}_filtered_matrix.mtx.gz"), "rt") as f:
        for line in f:
            if line[0] != "%":
                ng, nc, nz = [int(x) for x in line.split()]
                break
        arr = np.fromstring(f.read(), dtype=np.int64, sep=" ").reshape(-1, 3)
    g = arr[:, 0] - 1
    c = arr[:, 1] - 1
    v = arr[:, 2].astype(float)
    total = np.bincount(c, weights=v, minlength=nc)
    return feats, g, c, v, total


def build(files, selftest):
    arms = {}
    for tag in ("ctrl", "ko"):
        feats, g, c, v, total = read_mtx(files, tag)
        keep = total >= 500
        newidx = -np.ones(len(total), int)
        newidx[keep] = np.arange(keep.sum())
        m = keep[c]
        arms[tag] = dict(feats=feats, g=g[m], c=newidx[c[m]], v=v[m], total=total[keep], n=int(keep.sum()))
    # shared gene index by symbol (first occurrence); both arms share the same feature list in 10x output
    assert arms["ctrl"]["feats"] == arms["ko"]["feats"]
    feats = arms["ctrl"]["feats"]
    sym2i = {}
    for i, s in enumerate(feats):
        sym2i.setdefault(s, i)
    return arms, feats, sym2i


def dense_gene(arm, gi, n):
    out = np.zeros(arm["n"])
    m = arm["g"] == gi
    out[arm["c"][m]] = np.log2(arm["v"][m] / arm["total"][arm["c"][m]] * 1e6 + 1.0)
    return out


def classify(arms, sym2i):
    need = sorted({g for v in CLASSES.values() for g in v} | set(LATE) | set(REF))
    expr = {t: {g: dense_gene(arms[t], sym2i[g], 0) for g in need if g in sym2i} for t in arms}
    score = {(t, cl): np.mean([expr[t][g] for g in gl if g in expr[t]], axis=0) for t in arms for cl, gl in CLASSES.items()}
    p99 = {cl: np.percentile(np.concatenate([score[("ctrl", cl)], score[("ko", cl)]]), 99) for cl in CLASSES}
    labs = {}
    cls = list(CLASSES)
    for t in arms:
        M = np.column_stack([score[(t, cl)] / (p99[cl] if p99[cl] > 0 else 1.0) for cl in cls])
        am = M.argmax(1)
        ok = M.max(1) >= 0.2
        labs[t] = np.array([cls[i] if o else "unassigned" for i, o in zip(am, ok)])
    return labs, expr


def class_matrices(arms, labs, cls):
    """entries restricted to one class: gene idx, position in class (0..N-1), value x=log2cpm+1, arm indicator per cell."""
    pos0 = -np.ones(arms["ctrl"]["n"], int)
    ids0 = np.where(labs["ctrl"] == cls)[0]
    pos0[ids0] = np.arange(len(ids0))
    pos1 = -np.ones(arms["ko"]["n"], int)
    ids1 = np.where(labs["ko"] == cls)[0]
    pos1[ids1] = np.arange(len(ids1)) + len(ids0)
    out_g, out_p, out_x, out_cpm = [], [], [], []
    for t, pos in (("ctrl", pos0), ("ko", pos1)):
        a = arms[t]
        m = pos[a["c"]] >= 0
        out_g.append(a["g"][m])
        out_p.append(pos[a["c"][m]])
        cpm = a["v"][m] / a["total"][a["c"][m]] * 1e6
        out_x.append(np.log2(cpm + 1.0))
        out_cpm.append(cpm)
    return (np.concatenate(out_g), np.concatenate(out_p), np.concatenate(out_x), np.concatenate(out_cpm), ids0, ids1)


def fit_arm_coef(G, P, X, ko, mat, w, ng):
    """OLS of x on [1, mat, ko] using only cells with weight w==1; zeros contribute nothing to the sums."""
    keep = w > 0
    n = keep.sum()
    Sm = mat[keep].sum()
    Sm2 = (mat[keep] ** 2).sum()
    nk = ko[keep].sum()
    Smk = (mat[keep] * ko[keep]).sum()
    Gm = np.array([[n, Sm, nk], [Sm, Sm2, Smk], [nk, Smk, nk]])
    ent = w[P] > 0
    g, p, x = G[ent], P[ent], X[ent]
    Sx = np.bincount(g, weights=x, minlength=ng)
    Sxm = np.bincount(g, weights=x * mat[p], minlength=ng)
    Sxk = np.bincount(g, weights=x * ko[p], minlength=ng)
    rhs = np.vstack([Sx, Sxm, Sxk])
    beta = np.linalg.solve(Gm, rhs)
    return beta[2]


def nuclei_effects(arms, labs, feats, sym2i, cls, rng, selftest):
    ng = len(feats)
    G, P, X, CPM, ids0, ids1 = class_matrices(arms, labs, cls)
    N = len(ids0) + len(ids1)
    ko = np.concatenate([np.zeros(len(ids0)), np.ones(len(ids1))])
    # maturity covariate per nucleus (z-scored within class), computed from entries of the class
    def panel_mean(genes, skip=None):
        gi = [sym2i[g] for g in genes if g in sym2i and g != skip]
        mask = np.isin(G, gi)
        s = np.bincount(P[mask], weights=X[mask], minlength=N)
        return s / max(len(gi), 1)
    late, ref = panel_mean(LATE), panel_mean(REF)
    m_full = late - ref
    mat = (m_full - m_full.mean()) / m_full.std()
    w_all = np.ones(N)
    c_adj = fit_arm_coef(G, P, X, ko, mat, w_all, ng)
    # genes in the maturity panels: leave-one-out covariate, done directly
    for g in LATE + REF:
        if g not in sym2i:
            continue
        gi = sym2i[g]
        mm = panel_mean(LATE, skip=g) - panel_mean(REF, skip=g)
        mm = (mm - mm.mean()) / mm.std()
        xg = np.zeros(N)
        m = G == gi
        xg[P[m]] = X[m]
        D = np.column_stack([np.ones(N), mm, ko])
        c_adj[gi] = np.linalg.lstsq(D, xg, rcond=None)[0][2]
    # detection and raw difference
    det0 = np.bincount(G[P < len(ids0)], weights=(X[P < len(ids0)] > 0).astype(float), minlength=ng) / len(ids0)
    det1 = np.bincount(G[P >= len(ids0)], weights=(X[P >= len(ids0)] > 0).astype(float), minlength=ng) / len(ids1)
    mean_x = np.bincount(G, weights=X, minlength=ng) / N
    mean0 = np.bincount(G[P < len(ids0)], weights=X[P < len(ids0)], minlength=ng) / len(ids0)
    mean1 = np.bincount(G[P >= len(ids0)], weights=X[P >= len(ids0)], minlength=ng) / len(ids1)
    analysed = np.maximum(det0, det1) >= DET_FRAC
    if selftest:
        sub = np.zeros(ng, bool)
        sub[:3000] = True
        analysed &= sub
    centre = np.median(c_adj[analysed])
    cprime = c_adj - centre
    # stability: stratified random half-splits
    stable_n = np.zeros(ng)
    for s in range(STAB_SPLITS):
        half = np.zeros(N)
        for ids in (np.arange(len(ids0)), np.arange(len(ids1)) + len(ids0)):
            sel = rng.permutation(ids)
            half[sel[: len(sel) // 2]] = 1
        cA = fit_arm_coef(G, P, X, ko, mat, half, ng)
        cB = fit_arm_coef(G, P, X, ko, mat, 1 - half, ng)
        cA = cA - np.median(cA[analysed])
        cB = cB - np.median(cB[analysed])
        stable_n += (np.sign(cA) == np.sign(cB)) & (np.sign(cA) != 0)
    return dict(analysed=analysed, cprime=cprime, c_adj=c_adj, raw=mean1 - mean0, stable=stable_n, det0=det0, det1=det1,
                mean_x=mean_x, n0=len(ids0), n1=len(ids1), centre=float(centre))


def class_mean_cpm(arms, labs, feats):
    ng = len(feats)
    out = {}
    for cl in NEURON_CLASSES + GLIAL:
        for t in arms:
            a = arms[t]
            ids = np.where(labs[t] == cl)[0]
            if len(ids) == 0:
                out[(cl, t)] = np.zeros(ng)
                continue
            sel = np.zeros(a["n"], bool)
            sel[ids] = True
            m = sel[a["c"]]
            cpm = a["v"][m] / a["total"][a["c"][m]] * 1e6
            out[(cl, t)] = np.bincount(a["g"][m], weights=cpm, minlength=ng) / len(ids)
    return out


def organoid(files):
    rows, genes = [], []
    with gzip.open(os.path.join(files, "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"), "rt") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        cols = ["cwt1", "cwt2", "cko1", "cko2", "cko3", "cko4"]
        ix = [head.index(c) for c in cols]
        for line in fh:
            a = line.rstrip("\n").split("\t")
            genes.append(a[0])
            rows.append([float(a[i]) for i in ix])
    M = np.array(rows)
    lib = M.sum(axis=0)
    cpm = M / lib * 1e6
    L = np.log2(cpm + 1.0)
    gi = {}
    for i, g in enumerate(genes):
        gi.setdefault(g, i)
    ko = np.array([0, 0, 1, 1, 1, 1], float)
    neu = [gi[g] for g in PANEL_O_NEU if g in gi]
    prog = [gi[g] for g in PANEL_O_PROG if g in gi]

    def mu_of(skip=None):
        nn = [i for i in neu if genes[i] != skip]
        pp = [i for i in prog if genes[i] != skip]
        return L[nn].mean(0) - L[pp].mean(0)

    mu = mu_of()
    D = np.column_stack([np.ones(6), mu, ko])
    beta = np.linalg.lstsq(D, L.T, rcond=None)[0]  # 3 x genes
    c_o = beta[2].copy()
    for g in PANEL_O_NEU + PANEL_O_PROG:
        if g in gi:
            mm = mu_of(skip=g)
            Dg = np.column_stack([np.ones(6), mm, ko])
            c_o[gi[g]] = np.linalg.lstsq(Dg, L[gi[g]], rcond=None)[0][2]
    analysed = cpm.mean(axis=1) >= 1.0
    centre = np.median(c_o[analysed])
    cprime = c_o - centre
    g1 = L[:, 2:4].mean(1) - L[:, :2].mean(1)
    g2 = L[:, 4:6].mean(1) - L[:, :2].mean(1)
    return genes, gi, analysed, cprime, g1, g2, float(centre)


def hallmark(files):
    sets = {}
    p = os.path.join(files, "reach_audit_downloads/MSigDB_Hallmark_2020.gmt")
    for line in open(p, encoding="utf8"):
        a = line.rstrip("\n").split("\t")
        sets[a[0]] = [x.split(",")[0].strip().upper() for x in a[2:] if x]
    return sets


def log_hyper_sf(k, K, n, Nn):
    """P(X >= k) for hypergeometric (population Nn, K successes, n draws)."""
    def lc(a, b):
        return math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)
    tot = 0.0
    for i in range(k, min(K, n) + 1):
        tot += math.exp(lc(K, i) + lc(Nn - K, n - i) - lc(Nn, n))
    return min(1.0, tot)


def bh(pvals):
    idx = sorted(range(len(pvals)), key=lambda i: pvals[i])
    q = [0.0] * len(pvals)
    m = len(pvals)
    prev = 1.0
    for rank, i in reversed(list(enumerate(idx, 1))):
        prev = min(prev, pvals[i] * m / rank)
        q[i] = prev
    return q


def corroboration(files, genes_mouse):
    t2g = {}
    for line in gzip.open(os.path.join(files, "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz"), "rt"):
        if line[0] == ">":
            m = re.search(r"gene_symbol:(\S+)", line)
            if m:
                t2g[line[1:].split()[0].split(".")[0]] = m.group(1)

    def load(rel):
        gene, cols = {}, None
        for line in gzip.open(os.path.join(files, rel), "rt"):
            a = line.rstrip("\n").split("\t")
            if a[0] == "Name":
                cols = a[3:]
                continue
            g = t2g.get(a[0].split(".")[0])
            if g is not None:
                gene[g] = gene.get(g, 0) + np.array(a[3:], float)
        return gene, {c: i for i, c in enumerate(cols)}

    sets = [("cortex_S", "geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz",
             ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"]),
            ("hippo_S", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"])]
    res = {}
    cache = {}
    for name, rel, ko, ctrl in sets:
        if rel not in cache:
            cache[rel] = load(rel)
        data, cix = cache[rel]
        names = ko + ctrl
        kov = np.array([1.0] * len(ko) + [0.0] * len(ctrl))
        base = {g: np.mean(np.log2(data[g] + 1)[[cix[s] for s in ctrl]]) for g in LATE + REF if g in data}
        def lg(g, nm):
            return np.log2(data[g] + 1)[[cix[s] for s in nm]]
        stage = np.array([np.mean([lg(g, [s])[0] - base[g] for g in LATE if g in data]) - np.mean([lg(g, [s])[0] - base[g] for g in REF if g in data]) for s in names])
        D = np.column_stack([np.ones(len(names)), stage, kov])
        out = {}
        for g in genes_mouse:
            if g in data:
                y = lg(g, names)
                out[g] = float(np.linalg.lstsq(D, y, rcond=None)[0][2])
        res[name] = out
    return res


def main(files, out, selftest):
    os.makedirs(out, exist_ok=True)
    rng = np.random.default_rng(SEED)
    arms, feats, sym2i = build(files, selftest)
    labs, expr = classify(arms, sym2i)
    counts = {(t, cl): int((labs[t] == cl).sum()) for t in arms for cl in list(CLASSES) + ["unassigned"]}
    with open(os.path.join(out, "class_counts.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["arm", "class", "n_nuclei"])
        for (t, cl), n in counts.items():
            w.writerow([t, cl, n])
    genes_o, gi_o, an_o, cprime_o, g1, g2, centre_o = organoid(files)
    mouse_up = [s.upper() for s in feats]
    # organoid pass flags per mouse feature index (by upper-case symbol); first occurrence on both sides
    n_matched = 0
    o_pass_up = np.zeros(len(feats), bool)
    o_pass_dn = np.zeros(len(feats), bool)
    o_an = np.zeros(len(feats), bool)
    o_c = np.zeros(len(feats))
    seen = set()
    for i, s in enumerate(feats):
        u = s.upper()
        if u in seen or u not in gi_o:
            continue
        seen.add(u)
        j = gi_o[u]
        if not an_o[j]:
            continue
        n_matched += 1
        o_an[i] = True
        o_c[i] = cprime_o[j]
        up = cprime_o[j] >= THR_O and g1[j] >= THR_GROUP and g2[j] >= THR_GROUP
        dn = cprime_o[j] <= -THR_O and g1[j] <= -THR_GROUP and g2[j] <= -THR_GROUP
        o_pass_up[i], o_pass_dn[i] = up, dn
    cpm_means = class_mean_cpm(arms, labs, feats)
    hall = hallmark(files)
    summary, repl_rows, null_rows, enrich_rows = [], [], [], []
    all_repl = {}
    for cls in NEURON_CLASSES:
        ne = nuclei_effects(arms, labs, feats, sym2i, cls, rng, selftest)
        an = ne["analysed"] & o_an
        n_up = an & (ne["cprime"] >= THR_N) & (ne["stable"] >= STAB_MIN)
        n_dn = an & (ne["cprime"] <= -THR_N) & (ne["stable"] >= STAB_MIN)
        with open(os.path.join(out, f"nuclei_effects_{cls}.tsv"), "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(["gene", "analysed", "raw_mean_log2cpm_ko_minus_ctrl", "maturity_adjusted_coef", "centred_coef", "stable_splits_of_20", "det_frac_ctrl", "det_frac_ko", "organoid_centred_coef"])
            for i in np.where(ne["analysed"])[0]:
                w.writerow([feats[i], int(an[i]), f"{ne['raw'][i]:.4f}", f"{ne['c_adj'][i]:.4f}", f"{ne['cprime'][i]:.4f}", int(ne["stable"][i]), f"{ne['det0'][i]:.3f}", f"{ne['det1'][i]:.3f}",
                            f"{o_c[i]:.4f}" if o_an[i] else ""])
        # bins by N class mean expression (deciles among genes analysed in both)
        idx = np.where(an)[0]
        order = idx[np.argsort(ne["mean_x"][idx])]
        bins = np.array_split(order, 10)
        for d, (nm, Nflag, Oflag) in (("UP", ("UP", n_up, o_pass_up)), ("DOWN", ("DOWN", n_dn, o_pass_dn))):
            obs = int((Nflag & Oflag).sum())
            nulls = np.empty(NULL_N, int)
            for k in range(NULL_N):
                cnt = 0
                for b in bins:
                    perm = rng.permutation(len(b))
                    cnt += int((Nflag[b] & Oflag[b][perm]).sum())
                nulls[k] = cnt
            p975 = float(np.percentile(nulls, 97.5))
            verdict = "REPLICATES_BEYOND_CHANCE" if obs > p975 else "NOTHING_REPLICATES_BEYOND_CHANCE"
            null_rows.append([cls, d, int(Nflag.sum()), int(Oflag[an].sum()), obs, f"{np.mean(nulls):.2f}", f"{p975:.1f}", verdict])
            rep_idx = np.where(Nflag & Oflag)[0]
            all_repl[(cls, d)] = rep_idx
            for i in rep_idx:
                glial_ratio = []
                for t in ("ctrl", "ko"):
                    neu_m = cpm_means[(cls, t)][i]
                    gl = max(cpm_means[(g_, t)][i] for g_ in GLIAL)
                    glial_ratio.append(gl / neu_m if neu_m > 0 else float("inf"))
                glial_flag = all(r > 4 for r in glial_ratio)
                repl_rows.append([cls, d, feats[i], f"{ne['cprime'][i]:.3f}", f"{o_c[i]:.3f}", int(ne["stable"][i]), f"{ne['det0'][i]:.2f}", f"{ne['det1'][i]:.2f}",
                                  "glial-enriched in nuclei" if glial_flag else ""])
            # enrichment if any replicate beyond chance and >= 10 genes
            if verdict == "REPLICATES_BEYOND_CHANCE" and len(rep_idx) >= 10:
                bg = {feats[i].upper() for i in np.where(an)[0]}
                hits = {feats[i].upper() for i in rep_idx}
                names, ps, ks = [], [], []
                for sname, members in hall.items():
                    M = len(set(members) & bg)
                    k = len(set(members) & hits)
                    if k >= 2 and M > 0:
                        names.append(sname)
                        ks.append((k, M))
                        ps.append(log_hyper_sf(k, M, len(hits), len(bg)))
                q = bh(ps) if ps else []
                for nm_, (k, M), p_, q_ in zip(names, ks, ps, q):
                    enrich_rows.append([cls, d, nm_, k, M, f"{p_:.4g}", f"{q_:.3g}", "q<0.1" if q_ < 0.1 else ""])
    # corroboration on replicated genes
    rep_mouse = sorted({feats[i] for idx in all_repl.values() for i in idx})
    corr = corroboration(files, rep_mouse) if rep_mouse else {}
    corr_rows = []
    for (cls, d), idx in all_repl.items():
        for name, vals in corr.items():
            got = [(feats[i], vals[feats[i]]) for i in idx if feats[i] in vals]
            if not got:
                continue
            want = 1 if d == "UP" else -1
            same = sum(1 for _, v in got if np.sign(v) == want)
            corr_rows.append([cls, d, name, len(idx), len(got), same, f"{np.median([v for _, v in got]):.3f}"])
    def wr(name, header, rows):
        with open(os.path.join(out, name), "w", newline="") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(header)
            w.writerows([list(r) + [""] * (len(header) - len(r)) for r in rows])
    wr("null_summary.tsv", ["class", "direction", "n_nuclei_pass", "n_organoid_pass_in_analysed", "observed_replicated", "null_mean", "null_p97.5", "verdict"], null_rows)
    wr("replicated_genes.tsv", ["class", "direction", "gene", "nuclei_centred_coef", "organoid_centred_coef", "stable_splits_of_20", "det_ctrl", "det_ko", "flag"], repl_rows)
    wr("hallmark_enrichment.tsv", ["class", "direction", "hallmark_set", "hits", "set_size_in_background", "p", "q_bh", "flag"], enrich_rows)
    wr("corroboration_bulk_neuronal_deletion.tsv", ["class", "direction", "bulk_contrast", "n_replicated", "n_found", "n_same_sign", "median_stage_adjusted_coef"], corr_rows)
    wr("run_facts.tsv", ["fact", "value"], [["genes_matched_between_systems_and_analysed_in_organoid", n_matched], ["organoid_global_shift_centre", f"{centre_o:.4f}"],
                                            ["nuclei_n_ctrl_excitatory", counts[("ctrl", "excitatory")]], ["nuclei_n_ko_excitatory", counts[("ko", "excitatory")]],
                                            ["nuclei_n_ctrl_inhibitory", counts[("ctrl", "inhibitory")]], ["nuclei_n_ko_inhibitory", counts[("ko", "inhibitory")]],
                                            ["selftest", int(selftest)]])
    for r in null_rows:
        print("\t".join(str(x) for x in r))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="ADV-099 neuron-internal discovery (registered rule, held data only).")
    ap.add_argument("--files", required=True, help="the files/ directory of the checkout")
    ap.add_argument("--out", required=True, help="output directory")
    ap.add_argument("--selftest", action="store_true", help="crash test on a 3,000-gene subset (not the registered run)")
    a = ap.parse_args()
    main(a.files, a.out, a.selftest)
