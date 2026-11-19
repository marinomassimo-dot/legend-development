"""ADV-095 unit A2: block, delay or loss of the oligodendrocyte lineage in the held P17 Wwox-deficient deposits.

Implements PREREGISTRATION_UNIT_A2_FROZEN_BEFORE_ANY_LINEAGE_VALUE_SCI_20261119.md (sha256 18bc22d6f0ab82e878479c310c079def047b3f3e7f81e3e4f57f619b5716ba71). Held files only; no network. Usage:

    python3 lineage_state_unit_a2.py run <files_dir> <out_dir>

<files_dir> is the repository files/ folder (geo/, reference_ensembl_r92/). Unit: one GEO sample treated as one animal (bulk); nuclei are descriptive (one pool per arm).
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import gzip
import re
from pathlib import Path

import numpy as np

FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)

STAGES = {
    "PAN": "Olig1 Olig2 Sox10".split(),
    "OPC": "Pdgfra Cspg4 Cspg5 Pcdh15".split(),
    "COP": "Gpr17 Neu4 Bmp4 Vcan".split(),
    "NFOL": "Tcf7l2 Itpr2 Enpp6 Bcas1 Tmem2 Fyn Casr".split(),
    "MFOL": "Mal Mog Opalin Serinc5 Mag".split(),
    "MOL": "Klk6 Apod Pmp22 Slc5a11 Ermn Hapln2".split(),
    "MYELIN_STRUCT": "Mbp Plp1 Mobp Cnp".split(),
}
RANKED = ["OPC", "COP", "NFOL", "MFOL", "MOL"]
LATE = "Grin2a Slc12a5 Nrgn Camk2a Scn8a".split()
REF = "Snap25 Rbfox3 Syt1 Stmn2 Tubb3 Map2".split()
REGIONAL = "Ttr Kl Folr1".split()
IEG = "Fos Egr1 Npas4 Arc Junb Nr4a1".split()
CLASSES_NUC = {
    "excitatory": "Slc17a7 Camk2a Satb2".split(), "inhibitory": "Gad1 Gad2 Slc32a1".split(),
    "astrocyte": "Aqp4 Aldh1l1 Slc1a2".split(), "microglia": "Cx3cr1 P2ry12 Csf1r".split(),
}
for k in RANKED:
    CLASSES_NUC[k] = STAGES[k]
NEEDED = sorted({g for v in list(STAGES.values()) + [LATE, REF, REGIONAL, IEG] + list(CLASSES_NUC.values()) for g in v})

t2g, e2s = {}, {}
for line in gzip.open(FILES / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz", "rt"):
    if line[0] == ">":
        m = re.search(r"gene_symbol:(\S+)", line)
        mg = re.search(r"gene:(ENSMUSG\d+)", line)
        if m:
            t2g[line[1:].split()[0].split(".")[0]] = m.group(1)
            if mg:
                e2s[mg.group(1)] = m.group(1)


def load_tpm(path):
    gene, cols = {}, None
    for line in gzip.open(FILES / path, "rt"):
        a = line.rstrip("\n").split("\t")
        if a[0] == "Name":
            cols = a[3:]
            continue
        g = t2g.get(a[0].split(".")[0])
        if g is not None:
            gene[g] = gene.get(g, 0) + np.array(a[3:], float)
    return gene, {c: i for i, c in enumerate(cols)}


CORT, CC = load_tpm("geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz")
HIPP, HC = load_tpm("geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz")
CONTRASTS = [
    ("D2_cortex_S", CORT, CC, ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
    ("D3_hippo_S", HIPP, HC, ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], False),
    ("D3_hippo_N", HIPP, HC, ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
    ("D3_hippo_null", HIPP, HC, ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], False),
]


def ols(y, X):
    return np.linalg.lstsq(X, y, rcond=None)[0]


def spearman(a, b):
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def gm(gene, cols, g, names):
    return np.log2(gene[g] + 1.0)[[cols[s] for s in names]]


missing = []
rows_set, rows_tok, rows_exp, rows_delay_gene, rows_corr = [], [], [], [], []

# ---------------------------------------------------------------- age slopes (E-MTAB-6798 brain P14 -> P28)
slope = {}
with open(FILES / "geo/E-MTAB-6798_mouse_timecourse/Mouse.RPKM.txt") as f:
    hdr = [h.strip('"') for h in f.readline().split()]
    i14 = [i for i, h in enumerate(hdr) if h.startswith("Brain.P14.")]
    i28 = [i for i, h in enumerate(hdr) if h.startswith("Brain.P28.")]
    for line in f:
        a = line.split()
        sym = e2s.get(a[0].strip('"'))
        if sym in NEEDED:
            v = np.array(a[1:], float)
            # the header has no leading row-name column: value i belongs to hdr[i]
            slope[sym] = (float(np.log2(v[i28] + 1).mean() - np.log2(v[i14] + 1).mean())) / 14.0
print("slope genes", len(slope), "n P14", len(i14), "n P28", len(i28))

# ---------------------------------------------------------------- per contrast
tokens = {}
for cname, gene, cols, ko, ctrl, tested in CONTRASTS:
    names = ko + ctrl
    n = len(names)
    kov = np.array([1.0] * len(ko) + [0.0] * len(ctrl))
    base = {g: np.mean(gm(gene, cols, g, ctrl)) for g in LATE + REF if g in gene}
    stage = np.array([np.mean([gm(gene, cols, g, [s])[0] - base[g] for g in LATE if g in gene])
                      - np.mean([gm(gene, cols, g, [s])[0] - base[g] for g in REF if g in gene]) for s in names])
    X = np.column_stack([np.ones(n), stage, kov])
    res = {}
    for k, gl in STAGES.items():
        got = [g for g in gl if g in gene]
        if len(got) < len(gl):
            missing.append((cname, k, ",".join(g for g in gl if g not in gene)))
        v = np.mean([gm(gene, cols, g, names) for g in got], axis=0)
        R = float(v[kov == 1].mean() - v[kov == 0].mean())
        c = float(ols(v, X)[2])
        loo = []
        if tested:
            for d in range(n):
                keep = [i for i in range(n) if i != d]
                loo.append(float(ols(v[keep], X[keep])[2]))
        res[k] = (R, c, loo, v)
        rows_set.append([cname, k, len(got), round(R, 3), round(c, 3), (f"{min(loo):.3f}..{max(loo):.3f}" if loo else "")] + [round(float(x), 3) for x in v])
    # gradient and tokens
    Rs = np.array([res[k][0] for k in RANKED])
    As = np.array([res[k][1] for k in RANKED])
    rho = spearman(np.arange(1, 6), As)
    # delay model: d_neuro through origin over covariate genes
    cov_genes = [g for g in LATE + REF if g in gene and g in slope]
    shifts = np.array([float(gm(gene, cols, g, ko).mean() - gm(gene, cols, g, ctrl).mean()) for g in cov_genes])
    sl = np.array([slope[g] for g in cov_genes])
    d_neuro = float(-(shifts * sl).sum() / (sl ** 2).sum())
    d_loo = []
    for drop in range(n):
        ko_k = [s for i, s in enumerate(names) if i != drop and kov[i] == 1]
        ct_k = [s for i, s in enumerate(names) if i != drop and kov[i] == 0]
        if len(ko_k) < 1 or len(ct_k) < 1:
            continue
        sh = np.array([float(gm(gene, cols, g, ko_k).mean() - gm(gene, cols, g, ct_k).mean()) for g in cov_genes])
        d_loo.append(float(-(sh * sl).sum() / (sl ** 2).sum()))
    set_slope = {k: float(np.mean([slope[g] for g in STAGES[k] if g in slope])) for k in RANKED}
    pred = np.array([-d_neuro * set_slope[k] for k in RANKED])
    f_expl = float(1 - ((Rs - pred) ** 2).sum() / (Rs ** 2).sum())
    ol_genes = [g for k in RANKED for g in STAGES[k] if g in gene and g in slope]
    sh_ol = np.array([float(gm(gene, cols, g, ko).mean() - gm(gene, cols, g, ctrl).mean()) for g in ol_genes])
    sl_ol = np.array([slope[g] for g in ol_genes])
    d_ol = float(-(sh_ol * sl_ol).sum() / (sl_ol ** 2).sum())
    for g, s_, sp in zip(cov_genes, shifts, sl):
        rows_delay_gene.append([cname, "covariate_gene", g, round(float(s_), 3), round(float(sp), 4)])
    for g, s_, sp in zip(ol_genes, sh_ol, sl_ol):
        rows_delay_gene.append([cname, "lineage_gene", g, round(float(s_), 3), round(float(sp), 4)])
    T_LOSS = res["PAN"][1] <= -0.5 and res["OPC"][1] <= -0.5
    T_BLOCK = res["OPC"][1] >= -0.3 and res["COP"][1] >= -0.3 and np.mean([res["MFOL"][1], res["MOL"][1]]) <= -0.5 and rho <= -0.8
    opc_pred_sign = np.sign(pred[0])
    T_DELAY = (0 < d_neuro <= 3) and all(x > 0 for x in d_loo) and f_expl >= 0.5 and (np.sign(Rs[0]) == opc_pred_sign or abs(Rs[0]) < 0.1)
    rej_loss = res["OPC"][1] > -0.3
    rej_block = res["OPC"][1] < -0.3 or res["COP"][1] < -0.3 or rho > -0.4
    rej_delay = f_expl < 0.3 or any(x <= 0 for x in d_loo) or (d_neuro > 0 and d_ol / d_neuro > 2)
    true = [k for k, t in (("LOSS", T_LOSS), ("BLOCK", T_BLOCK), ("DELAY", T_DELAY)) if t]
    reading = ("supported: " + true[0]) if len(true) == 1 else ("compatible with " + " and ".join(true) if true else "UNDECIDED")
    labelled = tested
    rows_tok.append([cname, "labelled" if labelled else "descriptive", f"stage_separation={stage[:len(ko)].mean() - stage[len(ko):].mean():.3f}",
                     f"rho_stage_rank_A1={rho:.2f}", f"d_neuro_days={d_neuro:.2f}", f"d_neuro_loo={min(d_loo):.2f}..{max(d_loo):.2f}" if d_loo else "",
                     f"f_explained={f_expl:.2f}", f"d_OL_days={d_ol:.2f}", f"d_OL_over_d_neuro={(d_ol / d_neuro) if d_neuro else float('nan'):.2f}",
                     f"T_LOSS={T_LOSS} T_BLOCK={T_BLOCK} T_DELAY={T_DELAY}", f"rej_LOSS={rej_loss} rej_BLOCK={rej_block} rej_DELAY={rej_delay}",
                     reading if labelled else "no label (descriptive)"])
    tokens[cname] = dict(reading=reading, d=d_neuro, f=f_expl)
    # predicted vs observed per set
    for k, p in zip(RANKED, pred):
        rows_exp.append([cname, k, round(res[k][0], 3), round(float(p), 3), round(set_slope[k], 4)])
    # per-animal other explanations
    ms = np.mean([res[k][3] for k in ("MFOL", "MOL")] + [res["MYELIN_STRUCT"][3]], axis=0)
    reg = np.mean([gm(gene, cols, g, names) for g in REGIONAL if g in gene], axis=0)
    ie = np.mean([gm(gene, cols, g, names) for g in IEG if g in gene], axis=0)
    for i, s in enumerate(names):
        rows_corr.append([cname, s, "KO" if kov[i] else "ctrl", round(float(ms[i]), 3), round(float(reg[i]), 3), round(float(ie[i]), 3), round(float(stage[i]), 3)])
    if tested:
        rows_corr.append([cname, "SPEARMAN_across_animals", "", f"mature_vs_regional={spearman(ms, reg):.2f}", f"mature_vs_IEG={spearman(ms, ie):.2f}",
                          f"mature_vs_stage={spearman(ms, stage):.2f}", "genotype confounds all three; descriptive"])

# ---------------------------------------------------------------- nuclei (descriptive)
def load_arm(tag):
    feats = [l.rstrip("\n").split("\t")[1] for l in gzip.open(FILES / f"geo/GSE158684/GSE158684_{tag}_filtered_features.tsv.gz", "rt")]
    idx = {g: i for i, g in enumerate(feats) if g in NEEDED}
    with gzip.open(FILES / f"geo/GSE158684/GSE158684_{tag}_filtered_matrix.mtx.gz", "rt") as f:
        for line in f:
            if line[0] != "%":
                ng, nc, nz = [int(x) for x in line.split()]
                break
        arr = np.fromstring(f.read(), dtype=np.int64, sep=" ").reshape(-1, 3)
    total = np.bincount(arr[:, 1] - 1, weights=arr[:, 2], minlength=nc)
    sel = {}
    for g, i in idx.items():
        m = arr[:, 0] == i + 1
        v = np.zeros(nc)
        v[arr[m, 1] - 1] = arr[m, 2]
        sel[g] = v
    keep = total >= 500
    return {g: np.log2(v[keep] / total[keep] * 1e6 + 1.0) for g, v in sel.items()}, int(keep.sum())


nuc = {tag: load_arm(tag) for tag in ("ctrl", "ko")}
score = {}
for tag, (expr, nk) in nuc.items():
    for cl, gl in CLASSES_NUC.items():
        got = [g for g in gl if g in expr]
        score[(tag, cl)] = np.mean([expr[g] for g in got], axis=0)
        if len(got) < len(gl):
            missing.append(("nuclei_" + tag, cl, ",".join(g for g in gl if g not in expr)))
p99 = {cl: np.percentile(np.concatenate([score[("ctrl", cl)], score[("ko", cl)]]), 99) for cl in CLASSES_NUC}
rows_nuc = []
for tag, (expr, nk) in nuc.items():
    M = np.column_stack([score[(tag, cl)] / (p99[cl] if p99[cl] > 0 else 1) for cl in CLASSES_NUC])
    cls = list(CLASSES_NUC)
    amax = M.argmax(1)
    ok = M.max(1) >= 0.2
    lab = np.array([cls[i] if o else "unassigned" for i, o in zip(amax, ok)])
    cnt = {c: int((lab == c).sum()) for c in cls + ["unassigned"]}
    assigned = nk - cnt["unassigned"]
    lineage = sum(cnt[k] for k in RANKED)
    mature = cnt["MFOL"] + cnt["MOL"]
    rows_nuc.append([tag, "nuclei_total", nk, "", ""])
    for c in cls + ["unassigned"]:
        rows_nuc.append([tag, "count_" + c, cnt[c], round(cnt[c] / nk, 4), ""])
    rows_nuc.append([tag, "lineage_share_of_assigned", lineage, round(lineage / max(assigned, 1), 4), ""])
    rows_nuc.append([tag, "OPC_share_of_lineage", cnt["OPC"], round(cnt["OPC"] / max(lineage, 1), 4), ""])
    rows_nuc.append([tag, "mature_MFOL_MOL_share_of_lineage", mature, round(mature / max(lineage, 1), 4), ""])
    mat_mask = np.isin(lab, ["MFOL", "MOL"])
    for g in ("Mbp", "Plp1", "Mog"):
        if g in expr and mat_mask.sum() > 0:
            rows_nuc.append([tag, "mean_log2cpm_" + g + "_in_mature_nuclei", int(mat_mask.sum()), round(float(expr[g][mat_mask].mean()), 3), ""])


def w(name, header, rws):
    with open(OUT / name, "w", newline="") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header)
        wr.writerows([list(r) + [""] * (len(header) - len(r)) for r in rws])


w("stage_set_results.tsv", ["contrast", "set", "n_genes", "R_raw", "A1_c", "c_leave_one_out", "v1", "v2", "v3", "v4", "v5", "v6", "v7"], rows_set)
w("readings.tsv", ["contrast", "status", "stage_separation", "rho_rank_A1", "d_neuro", "d_neuro_loo", "f_explained", "d_OL", "ratio", "tokens", "rejections", "reading"], rows_tok)
w("delay_expected_vs_observed.tsv", ["contrast", "set", "observed_R", "predicted_by_delay", "set_mean_slope_per_day"], rows_exp)
w("delay_gene_inputs.tsv", ["contrast", "gene_group", "gene", "observed_shift_R", "slope_per_day_P14_to_P28"], rows_delay_gene)
w("other_explanations_per_animal.tsv", ["contrast", "animal", "arm", "mature_score", "regional_panel", "IEG_panel", "stage_score"], rows_corr)
w("nuclei_descriptive.tsv", ["arm", "quantity", "n", "value", "note"], rows_nuc)
with open(OUT / "missing_genes.txt", "w") as f:
    f.write("dataset\tset\tregistered_genes_not_found\n")
    for r in missing:
        f.write("\t".join(r) + "\n")
print("done")
