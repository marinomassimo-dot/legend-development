"""ADV-068: per-animal PV signature against late-maturing and reference gene sets in the public P17 Wwox deposits (GSE158681 hippocampus, GSE158682 cortex).

Implements PREREGISTRATION_FROZEN_BEFORE_ANY_COUNT_SCI_20261119.md exactly (sha256 d4cb2273...). Held files only; no network. Usage:

    python3 pv_per_animal_analysis.py run <files_dir> <out_dir>

Unit: one GEO sample treated as one animal. Verdict rules are applied only to contrasts with at least three animals per arm.
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import gzip
import itertools
import math
import re
from pathlib import Path

import numpy as np

FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)

SETS = {
    "REF_STABLE": ["Snap25", "Rbfox3", "Syt1", "Stmn2", "Tubb3", "Map2"],
    "PV_SET": ["Pvalb", "Syt2", "Kcnc1", "Kcnc2"],
    "INT_NONPV": ["Gad1", "Gad2", "Slc32a1", "Sst", "Vip", "Npy", "Cck", "Calb2", "Htr3a", "Lhx6", "Dlx1", "Dlx2", "Dlx5"],
    "LATE_NONPV": ["Grin2a", "Slc12a5", "Nrgn", "Camk2a", "Scn8a"],
    "OL_GUARD": ["Mbp", "Plp1", "Mog", "Mobp"],
    "AST_GUARD": ["Gfap", "Aqp4", "Aldh1l1"],
    "MIC_GUARD": ["Cx3cr1", "P2ry12", "Tmem119", "Csf1r"],
    "DELETION": ["Wwox"],
}
ALL_GENES = sorted({g for v in SETS.values() for g in v})

# transcript -> gene symbol from the pinned Ensembl release-92 cDNA headers
t2g = {}
for line in gzip.open(FILES / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz", "rt"):
    if line[0] != ">":
        continue
    tid = line[1:].split()[0].split(".")[0]
    m = re.search(r"gene_symbol:(\S+)", line)
    if m:
        t2g[tid] = m.group(1)

CONTRASTS = [
    # name, file, control columns, knockout columns, primary
    ("cortex_S", "geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz",
     ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], True),
    ("hippo_S", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
     ["S_Ctrl_1", "S_Ctrl_2"], ["S_KO_1", "S_KO_2", "S_KO_3"], False),
    ("hippo_N", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
     ["N_Ctrl_1", "N_Ctrl_2"], ["N_KO_1", "N_KO_2"], False),
    ("hippo_null", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
     ["WT_1", "WT_2", "WT_3"], ["KO_1", "KO_2"], False),
]


def load(path):
    gene_tpm, cols, missing_tx = {}, None, 0
    for line in gzip.open(FILES / path, "rt"):
        a = line.rstrip("\n").split("\t")
        if a[0] == "Name":
            cols = a[3:]
            continue
        g = t2g.get(a[0].split(".")[0])
        if g is None:
            missing_tx += 1
            continue
        if g in ALL_GENES:
            v = np.array(a[3:], float)
            gene_tpm[g] = gene_tpm.get(g, 0) + v
    return gene_tpm, cols, missing_tx


def sig(vals, genes):
    got = [g for g in genes if g in vals]
    return float(np.mean([vals[g] for g in got])) if got else float("nan"), len(got)


rows_gene, rows_animal, rows_contrast, rows_rule = [], [], [], []
cache = {}
for name, path, ctrl, ko, primary in CONTRASTS:
    if path not in cache:
        cache[path] = load(path)
    gt, cols, miss = cache[path]
    idx = {c: i for i, c in enumerate(cols)}
    present = [g for g in ALL_GENES if g in gt]
    L = {g: np.log2(gt[g] + 1.0) for g in present}
    for g in present:
        for c in ctrl + ko:
            rows_gene.append([name, g, c, "KO" if c in ko else "ctrl", round(float(gt[g][idx[c]]), 3), round(float(L[g][idx[c]]), 4)])
    ctrl_mean = {g: float(np.mean([L[g][idx[c]] for c in ctrl])) for g in present}
    animals = {}
    for c in ko:
        lfc = {g: float(L[g][idx[c]]) - ctrl_mean[g] for g in present}
        animals[c] = ("KO", lfc)
    for c in ctrl:  # leave-one-out
        others = [x for x in ctrl if x != c]
        lfc = {g: float(L[g][idx[c]]) - float(np.mean([L[g][idx[x]] for x in others])) for g in present}
        animals[c] = ("ctrl_loo", lfc)
    sigval = {}
    for c, (arm, lfc) in animals.items():
        s = {k: sig(lfc, v)[0] for k, v in SETS.items()}
        ref = s["REF_STABLE"]
        norm = {k: (s[k] - ref) for k in ("PV_SET", "INT_NONPV", "LATE_NONPV")}
        sigval[c] = (arm, s, norm)
        rows_animal.append([name, c, arm] + [round(s[k], 3) for k in SETS] + [round(norm[k], 3) for k in ("PV_SET", "INT_NONPV", "LATE_NONPV")])
    kos = [sigval[c] for c in ko]
    ctrls = [sigval[c] for c in ctrl]

    def kmean(key, normed=False):
        return float(np.mean([(k[2][key] if normed else k[1][key]) for k in kos]))

    n_c, n_k = len(ctrl), len(ko)
    contrast = {k: kmean(k) for k in SETS}
    contrast_n = {k: kmean(k, True) for k in ("PV_SET", "INT_NONPV", "LATE_NONPV")}
    rows_contrast.append([name, n_c, n_k] + [round(contrast[k], 3) for k in SETS] + [round(contrast_n[k], 3) for k in ("PV_SET", "INT_NONPV", "LATE_NONPV")])
    # per-gene mean log2FC in KO for the PV and late sets (description)
    for g in SETS["PV_SET"] + SETS["LATE_NONPV"] + ["Wwox"]:
        if g in present:
            rows_rule.append([name, "gene_log2FC", g, round(float(np.mean([animals[c][1][g] for c in ko])), 3), "; ".join(f"{c}:{animals[c][1][g]:.2f}" for c in ko)])
    # decision
    comp = (contrast["OL_GUARD"] <= -1.0) or (abs(contrast["REF_STABLE"]) >= 0.3)
    pv, lt, it = contrast_n["PV_SET"], contrast_n["LATE_NONPV"], contrast_n["INT_NONPV"]
    # animal-level separation for R-A: every KO animal's normalised PV value below the lowest control's
    ko_pv = [k[2]["PV_SET"] for k in kos]
    ct_pv = [k[2]["PV_SET"] for k in ctrls]
    separated = bool(max(ko_pv) < min(ct_pv))
    if n_c < 3 or n_k < 3:
        verdict = "STOP_S (fewer than three animals per arm): descriptive only, no rule verdict"
    elif pv > -0.5:
        verdict = "R-C no PV deficit in this contrast (reference-normalised PV_SET above -0.5)"
    elif lt <= -0.25:
        verdict = "R-B falls together: PRE-REGISTERED STOP (no PV-specific lever follows)"
    elif abs(lt) <= 0.2 and abs(it) <= 0.2 and separated:
        verdict = "R-A PV-specific pattern"
    else:
        verdict = "R-D mixed or uninformative"
    rows_rule.append([name, "verdict", "primary" if primary else "descriptive", verdict,
                      f"n_ctrl={n_c}; n_ko={n_k}; composition_caveat={comp}; PV_norm={pv:.3f}; LATE_norm={lt:.3f}; INT_norm={it:.3f}; "
                      f"OL_raw={contrast['OL_GUARD']:.3f}; REF_raw={contrast['REF_STABLE']:.3f}; every_KO_PV_below_lowest_ctrl={separated}; "
                      f"KO_PV_norm_values={[round(x,3) for x in ko_pv]}; ctrl_loo_PV_norm_values={[round(x,3) for x in ct_pv]}"])


def w(name, header, rows):
    with open(OUT / name, "w", newline="") as f:
        cw = csv.writer(f, delimiter="\t", lineterminator="\n")
        cw.writerow(header)
        cw.writerows(rows)


w("per_gene_per_animal.tsv", ["contrast", "gene", "sample", "arm", "TPM_gene_sum", "log2_TPM_plus1"], rows_gene)
w("per_animal_signatures.tsv", ["contrast", "sample", "arm"] + [f"{k}_log2FC" for k in SETS] + ["PV_SET_refnorm", "INT_NONPV_refnorm", "LATE_NONPV_refnorm"], rows_animal)
w("contrast_summary.tsv", ["contrast", "n_ctrl", "n_ko"] + [f"{k}_log2FC" for k in SETS] + ["PV_SET_refnorm", "INT_NONPV_refnorm", "LATE_NONPV_refnorm"], rows_contrast)
w("rules_and_gene_values.tsv", ["contrast", "kind", "item", "value", "detail"], rows_rule)
print("done; genes present:", sorted({r[1] for r in rows_gene}))
