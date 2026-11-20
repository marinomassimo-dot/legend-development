#!/usr/bin/env python3
"""ADV-095 unit C: thyroid-signalling premise check, as registered in
PREREGISTRATION_UNIT_C_THYROID_PREMISE_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md
(sha256 47a290238bd1ed9a29812db34e4d0ebb34f76faceb02378a4528e7466d114a86).

Hypothesis level; no dose; not medical advice. Held data only, no network.
Usage: thyroid_premise_unit_c.py --files FILES_DIR --out OUT_DIR
"""
import argparse
import csv
import gzip
import os
import re

import numpy as np

SCORED = ["Hr", "Klf9", "Nrgn", "Pcp4", "Dio3"]
CONTEXT = ["Slc16a2", "Slco1c1", "Dio2", "Thra", "Thrb", "Mbp"]
CONFOUNDED = "Nrgn"
FLOOR = 1.0
NULL_N = 5000
SEED = 20261120

CONTRASTS = [  # name, file, KO columns, control columns, decides
    ("cortex_S", "geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz",
     ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
    ("hippo_S", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
     ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], False),
    ("hippo_N", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
     ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
    ("hippo_null", "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
     ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], False),
]


def load_t2g(files):
    t2g = {}
    for line in gzip.open(os.path.join(files, "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz"), "rt"):
        if line[0] == ">":
            m = re.search(r"gene_symbol:(\S+)", line)
            if m:
                t2g[line[1:].split()[0].split(".")[0]] = m.group(1)
    return t2g


def load_tpm(files, rel, t2g):
    gene, cols = {}, None
    for line in gzip.open(os.path.join(files, rel), "rt"):
        a = line.rstrip("\n").split("\t")
        if a[0] == "Name":
            cols = a[3:]
            continue
        g = t2g.get(a[0].split(".")[0])
        if g is not None:
            v = np.array(a[3:], float)
            gene[g] = gene.get(g, 0) + v
    return gene, {c: i for i, c in enumerate(cols)}


def l2r(v, ko, ctrl):
    return float(np.log2(v[ko].mean() + 0.1) - np.log2(v[ctrl].mean() + 0.1))


def main(files, out):
    os.makedirs(out, exist_ok=True)
    t2g = load_t2g(files)
    rng = np.random.default_rng(SEED)
    detail, verdicts = [], []
    cache = {}
    for name, rel, kocols, ccols, decides in CONTRASTS:
        if rel not in cache:
            cache[rel] = load_tpm(files, rel, t2g)
        data, cix = cache[rel]
        ko = [cix[c] for c in kocols]
        ctrl = [cix[c] for c in ccols]
        ctrl_mean = {g: float(v[ctrl].mean()) for g, v in data.items()}
        pool = np.array(sorted(g for g in data if ctrl_mean[g] >= FLOOR))
        pool_mean = np.array([ctrl_mean[g] for g in pool])
        scored, missing = [], []
        for g in SCORED:
            if g not in data:
                missing.append(g)
                detail.append([name, g, "scored", "not in table", "", "", ""])
                continue
            r = l2r(data[g], ko, ctrl)
            floor_ok = ctrl_mean[g] >= FLOOR
            detail.append([name, g, "scored" + (" (confounded)" if g == CONFOUNDED else ""), f"{ctrl_mean[g]:.3f}",
                           f"{float(data[g][ko].mean()):.3f}", f"{r:.3f}", "" if floor_ok else "below floor"])
            if floor_ok:
                scored.append((g, r))
        for g in CONTEXT:
            if g not in data:
                detail.append([name, g, "context", "not in table", "", "", ""])
                continue
            detail.append([name, g, "context", f"{ctrl_mean[g]:.3f}", f"{float(data[g][ko].mean()):.3f}",
                           f"{l2r(data[g], ko, ctrl):.3f}", "" if ctrl_mean[g] >= FLOOR else "below floor"])
        n = len(scored)
        panel = float(np.mean([r for _, r in scored])) if n else float("nan")
        neg = sum(1 for _, r in scored if r < 0)
        # matched null
        null = np.empty(NULL_N)
        for i in range(NULL_N):
            rs = []
            for g, _ in scored:
                lo, hi = ctrl_mean[g] * 0.75, ctrl_mean[g] * 1.25
                cand = pool[(pool_mean >= lo) & (pool_mean <= hi)]
                cand = cand[cand != g]
                pick = rng.choice(cand)
                rs.append(l2r(data[pick], ko, ctrl))
            null[i] = np.mean(rs)
        lo_e, hi_e = (np.percentile(null, [2.5, 97.5]) if n else (float("nan"),) * 2)
        # variant without the confounded member
        sc2 = [(g, r) for g, r in scored if g != CONFOUNDED]
        panel2 = float(np.mean([r for _, r in sc2])) if sc2 else float("nan")
        if n < 4:
            verdict = "UNDECIDED (fewer than four scored genes)"
        elif panel <= -0.3 and panel < lo_e and neg >= 4:
            verdict = "PREMISE_SUPPORTED_TH"
        elif panel >= -0.1 or panel > lo_e or neg < n / 2:
            verdict = "PREMISE_ABSENT_TH"
        else:
            verdict = "UNDECIDED"
        verdicts.append([name, "decides" if decides else "direction only", n, ";".join(missing), f"{panel:.3f}", neg,
                         f"{lo_e:.3f}", f"{hi_e:.3f}", f"{panel2:.3f}", verdict])
    with open(os.path.join(out, "thyroid_premise_genes.tsv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["contrast", "gene", "role", "control_mean_tpm", "ko_mean_tpm", "log2_ratio_ko_over_ctrl", "note"])
        w.writerows(detail)
    with open(os.path.join(out, "thyroid_premise_verdicts.tsv"), "w", newline="", encoding="utf8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["contrast", "role_in_rule", "n_scored", "missing_genes", "panel_mean_log2", "n_negative",
                    "null_p2.5", "null_p97.5", "panel_mean_without_Nrgn", "registered_verdict"])
        w.writerows(verdicts)
    for r in verdicts:
        print("\t".join(str(x) for x in r))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Thyroid-signalling premise check (ADV-095 unit C), registered rule, held data only.")
    ap.add_argument("--files", required=True, help="the files/ directory of the checkout (holds geo/ and reference_ensembl_r92/)")
    ap.add_argument("--out", required=True, help="output directory")
    a = ap.parse_args()
    main(a.files, a.out)
