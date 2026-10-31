#!/usr/bin/env python3
"""IT13 P3a: E/I composition, activity and channel panels in P17 mouse Wwox-deleted brain (GSE158681 hippocampus, GSE158682 cortex).
Panels and statistic are declared in PRE_ANALYSIS.md (committed before any panel value was opened). Needs numpy only. Deterministic (seed 20261031).
Usage: p3a_e_i_panels.py <hippo.txt.gz> <cortex.txt.gz> <Ensembl92 cdna.fa.gz> <out_dir>
Transcript level only; RNA is not protein is not current."""
import sys
if len(sys.argv) != 5 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
import gzip, re, os, itertools, json
import numpy as np
hippo, cortex, fasta, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
SEED, NDRAW = 20261031, 10000

tx2g, gsym, patch = {}, {}, set()
for l in gzip.open(fasta, "rt"):
    if l[0] != ">": continue
    tid = l[1:].split(" ", 1)[0]; gid = re.search(r"gene:(\S+)", l).group(1)
    if "_PATCH" in l.split(" ", 3)[2]: patch.add(tid); continue
    tx2g[tid] = gid; m = re.search(r"gene_symbol:(\S+)", l); gsym[gid] = m.group(1) if m else ""
sym2id = {}
for g, s in gsym.items():
    if s: sym2id.setdefault(s, []).append(g)

def load(path):
    f = gzip.open(path, "rt"); head = f.readline().rstrip("\n").split("\t"); ids, rows = [], []
    for l in f:
        p = l.rstrip("\n").split("\t"); ids.append(p[0]); rows.append(p[3:])
    animals = head[3:]; M = np.array(rows, dtype=float)
    gl = sorted(set(tx2g[i] for i in ids if i in tx2g)); gi = {g: k for k, g in enumerate(gl)}
    G = np.zeros((len(gl), M.shape[1]))
    for k, i in enumerate(ids):
        if i in tx2g: G[gi[tx2g[i]]] += M[k]
    return animals, gl, gi, G

PANELS = {
 "PAN": "Snap25 Syt1 Rbfox3 Stmn2 Map2 Syp Nefl Eno2", "EXC": "Slc17a7 Camk2a Neurod2 Neurod6 Satb2 Tbr1",
 "INH_ALL": "Gad1 Gad2 Slc32a1 Dlx1 Dlx2 Dlx5 Lhx6", "PV": "Pvalb Kcnc1 Kcnc2 Lhx6", "SST_NPY": "Sst Npy Cort Nos1",
 "VIP_CCK": "Vip Cck Calb2 Htr3a", "IEG": "Fos Fosb Npas4 Arc Egr1 Egr2 Egr4 Junb Nr4a1 Bdnf Btg2 Dusp1",
 "ASTRO": "Gfap Aqp4 Aldh1l1 Slc1a3", "MYELIN": "Mbp Plp1 Mog Mag Mobp"}
PANELS = {k: v.split() for k, v in PANELS.items()}
INDIV = ("Slc12a2 Slc12a5 Kcnq2 Kcnq3 Kcnj3 Kcnj6 Kcnj9 Kcnj10 Hcn1 Hcn2 Cacna1g Cacna1h Scn1a Scn2a Scn8a Gabra1 Gabra2 Gabrb2 Gabrb3 "
         "Gabrg2 Grin1 Grin2a Grin2b Grin2c Grin2d Gria1 Gria2 Panx1 Atp1a3 Kcna2 Grm3 Wwox Pvalb Sst Npy Vip Gad1 Gad2").split()
CONTR = [
 ("H_S", "hippo", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], 1),
 ("H_N", "hippo", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], 1),
 ("H_null", "hippo", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], 1),
 ("C_S", "cortex", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], 1),
 ("CC_SW", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], 0),
 ("CC_NW", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], 0),
 ("CC_SN", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["N_Ctrl_1", "N_Ctrl_2"], 0)]
D = {"hippo": load(hippo), "cortex": load(cortex)}
rng = np.random.default_rng(SEED)

def ids_of(symbols):
    r, miss = [], []
    for s in symbols:
        c = sym2id.get(s, [])
        (r if len(c) == 1 else miss).append(c[0] if len(c) == 1 else s)
    return r, miss

res_sets, res_genes, res_sel = [], [], []
for name, tis, ko, ct, primary in CONTR:
    animals, gl, gi, G = D[tis]
    kc = [animals.index(a) for a in ko]; cc = [animals.index(a) for a in ct]
    mk, mc = G[:, kc].mean(1), G[:, cc].mean(1)
    R = np.log2((mk + 0.5) / (mc + 0.5))
    for thr in (1.0, 0.5, 2.0):
        meas = np.maximum(mk, mc) >= thr
        cen = float(np.median(R[meas])); Rc = R - cen
        mean_expr = np.log2((mk + mc) / 2 + 0.5)
        # decile bins of measurable genes
        mi = np.where(meas)[0]; qs = np.quantile(mean_expr[mi], np.linspace(0, 1, 11)); bins = np.clip(np.searchsorted(qs, mean_expr[mi], side="right") - 1, 0, 9)
        by_bin = [mi[bins == b] for b in range(10)]
        pos = {g: k for k, g in enumerate(mi)}
        setrec = {}
        for sname, syms in PANELS.items():
            gids, miss = ids_of(syms)
            idx = [gi[g] for g in gids if g in gi and meas[gi[g]]]
            if not idx: continue
            obs = float(Rc[idx].mean())
            sel_b = [bins[pos[i]] for i in idx]
            draws = np.mean([Rc[by_bin[b][rng.integers(0, len(by_bin[b]), NDRAW)]] for b in sel_b], axis=0)
            lo, hi = np.quantile(draws, [0.025, 0.975])
            rank2 = float(np.mean(np.abs(draws) >= abs(obs)))
            an = np.log2(G[idx][:, kc] + 0.5).mean(0), np.log2(G[idx][:, cc] + 0.5).mean(0)
            # exact permutation p for the animal-level difference of means
            allv = np.concatenate(an); n1 = len(kc); obsd = an[0].mean() - an[1].mean()
            cnt = tot = 0
            for comb in itertools.combinations(range(len(allv)), n1):
                m = np.zeros(len(allv), bool); m[list(comb)] = True
                dd = allv[m].mean() - allv[~m].mean(); tot += 1; cnt += abs(dd) >= abs(obsd) - 1e-12
            loo = "".join("+" if np.delete(Rc[idx], k).mean() > 0 else "-" for k in range(len(idx))) if len(idx) > 1 else ("+" if Rc[idx[0]] > 0 else "-")
            sep = bool(an[0].min() > an[1].max() or an[0].max() < an[1].min())
            res_sets.append([name, primary, thr, sname, len(syms), len(idx), "%.3f" % obs, "%.3f" % lo, "%.3f" % hi, "%.3f" % rank2,
                             "%.3f" % (cnt / tot), int(sep), loo, ";".join("%.2f" % v for v in an[0]), ";".join("%.2f" % v for v in an[1]), ",".join(miss)])
            setrec[sname] = (obs, draws)
        if thr == 1.0:
            # selectivity contrasts
            for a, b in [("INH_ALL", "PAN"), ("PV", "PAN"), ("SST_NPY", "PAN"), ("INH_ALL", "EXC"), ("EXC", "PAN")]:
                if a in setrec and b in setrec:
                    ob = setrec[a][0] - setrec[b][0]; nd = setrec[a][1] - setrec[b][1]
                    res_sel.append([name, primary, a + "-" + b, "%.3f" % ob, "%.3f" % np.quantile(nd, .025), "%.3f" % np.quantile(nd, .975)])
    # individual genes (thr 1.0 gate)
    for g in INDIV:
        c = sym2id.get(g, [])
        if len(c) != 1 or c[0] not in gi: res_genes.append([name, primary, g, "absent", "", "", "", ""]); continue
        k = gi[c[0]]
        res_genes.append([name, primary, g, "measurable" if max(mk[k], mc[k]) >= 1 else "below1TPM", "%.2f" % mk[k], "%.2f" % mc[k], "%.3f" % R[k],
                          ";".join("%.1f" % v for v in G[k, kc]) + "|" + ";".join("%.1f" % v for v in G[k, cc])])

def w(fn, head, rows):
    with open(os.path.join(out, fn), "w") as f:
        f.write("\t".join(head) + "\n")
        for r in rows: f.write("\t".join(map(str, r)) + "\n")
w("panel_summary.tsv", "contrast primary thr_tpm panel n_declared n_measurable mean_centred_log2 null_lo null_hi rank_two_sided animal_perm_p animal_separated loo_signs animal_scores_KO animal_scores_ctl unresolved_symbols".split(), res_sets)
w("selectivity.tsv", "contrast primary contrast_def observed null_lo null_hi".split(), res_sel)
w("genes_individual.tsv", "contrast primary gene status mean_tpm_KO mean_tpm_ctl log2_ratio animal_tpm_KO|ctl".split(), res_genes)
print("done", len(res_sets), len(res_sel), len(res_genes))
