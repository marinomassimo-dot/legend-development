"""ADV-070: stage-adjusted re-read of IT13 P3a's channel, receptor, transporter and activity seeds in the held P17 Wwox-deletion deposits.

Implements PREREGISTRATION_FROZEN_BEFORE_ANY_ADJUSTED_VALUE_SCI_20261119.md exactly
(sha256 1f9f782bce3ae022494956e53334d98331e6deaca7c91b0995d2d700d170ddad). Held files only; no network. Usage:

    python3 stage_adjusted_reread.py run <files_dir> <p3a_genes_individual.tsv> <out_dir>
"""
import sys

if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import gzip
import re
from pathlib import Path

import numpy as np

FILES, P3A, OUT = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
OUT.mkdir(parents=True, exist_ok=True)

LATE = ["Grin2a", "Slc12a5", "Nrgn", "Camk2a", "Scn8a"]
REF = ["Snap25", "Rbfox3", "Syt1", "Stmn2", "Tubb3", "Map2"]
SEEDS = ("Slc12a2 Slc12a5 Kcnq2 Kcnq3 Kcnj3 Kcnj6 Kcnj9 Kcnj10 Hcn1 Hcn2 Cacna1g Cacna1h Scn1a Scn2a Scn8a Gabra1 Gabra2 Gabrb2 Gabrb3 "
         "Gabrg2 Grin1 Grin2a Grin2b Grin2c Grin2d Gria1 Gria2 Panx1 Atp1a3 Kcna2 Grm3").split()
REFINT = "Pvalb Sst Npy Vip Gad1 Gad2".split()
SETS = {"IEG": "Fos Fosb Npas4 Arc Egr1 Egr2 Egr4 Junb Nr4a1 Bdnf Btg2 Dusp1".split(), "PV_panel": "Pvalb Kcnc1 Kcnc2 Lhx6".split()}
ITEMS = [(g, "channel_receptor_transporter") for g in SEEDS] + [(g, "reference_interneuron") for g in REFINT] + [("Wwox", "deletion_check")] + \
        [(k, "set") for k in SETS]
NEEDED = sorted(set(SEEDS + REFINT + ["Wwox"] + LATE + REF + [g for v in SETS.values() for g in v]))

HIPPO = FILES / "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz"
CORTEX = FILES / "geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz"
FASTA = FILES / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz"

t2g = {}
for line in gzip.open(FASTA, "rt"):
    if line[0] != ">":
        continue
    m = re.search(r"gene_symbol:(\S+)", line)
    if m:
        t2g[line[1:].split()[0].split(".")[0]] = m.group(1)


def load(path):
    gene, cols = {}, None
    for line in gzip.open(path, "rt"):
        a = line.rstrip("\n").split("\t")
        if a[0] == "Name":
            cols = a[3:]
            continue
        g = t2g.get(a[0].split(".")[0])
        if g in NEEDED:
            gene[g] = gene.get(g, 0) + np.array(a[3:], float)
    return gene, {c: i for i, c in enumerate(cols)}


DATA = {"hippo": load(HIPPO), "cortex": load(CORTEX)}
CONTR = [
    ("H_S", "hippo", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], True),
    ("H_N", "hippo", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], True),
    ("H_null", "hippo", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], True),
    ("C_S", "cortex", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
    ("CC_SW", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
    ("CC_NW", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
    ("CC_SN", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
]

# P3a reference values (read, not recomputed)
p3a = {}
for r in csv.DictReader(open(P3A), delimiter="\t"):
    p3a[(r["contrast"], r["gene"])] = float(r["log2_ratio"]) if r["log2_ratio"] not in ("", "NA") else None


def stage_score(gene, cols, case, ctrl, omit=()):
    """per-animal ADV-068 late-set score; baseline = mean over all control animals; seeds in the sets are omitted (leave-self-out)"""
    L = lambda g: np.log2(gene[g] + 1.0)
    late = [g for g in LATE if g in gene and g not in omit]
    ref = [g for g in REF if g in gene and g not in omit]
    base = lambda g: np.mean([L(g)[cols[c]] for c in ctrl])
    out = {}
    for a in case + ctrl:
        out[a] = float(np.mean([L(g)[cols[a]] - base(g) for g in late]) - np.mean([L(g)[cols[a]] - base(g) for g in ref]))
    return out


def ols_c(y, x, ko):
    X = np.column_stack([np.ones(len(y)), x, ko])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return float(beta[1]), float(beta[2])


rows = []
for cname, tis, case, ctrl, deletion in CONTR:
    gene, cols = DATA[tis]
    n_case, n_ctrl = len(case), len(ctrl)
    qualifies = deletion and n_case >= 3 and n_ctrl >= 3
    animals = case + ctrl
    ko = np.array([1.0] * n_case + [0.0] * n_ctrl)
    score_all = stage_score(gene, cols, case, ctrl)
    for name, cat in ITEMS:
        members = SETS[name] if cat == "set" else [name]
        present = [g for g in members if g in gene]
        if not present:
            rows.append([cname, name, cat, "not_present", "", "", "", "", "", "", "", "", ""])
            continue
        mean_case = np.mean([[gene[g][cols[a]] for a in case] for g in present])
        mean_ctrl = np.mean([[gene[g][cols[a]] for a in ctrl] for g in present])
        if max(mean_case, mean_ctrl) < 1.0 and cat != "set":
            rows.append([cname, name, cat, "below_TPM_1", "", "", "", "", "", "", "", "", ""])
            continue
        omit = tuple(g for g in members if g in LATE or g in REF)
        score = stage_score(gene, cols, case, ctrl, omit) if omit else score_all
        y = np.array([np.mean([np.log2(gene[g][cols[a]] + 0.5) for g in present]) for a in animals])
        x = np.array([score[a] for a in animals])
        delta = float(y[:n_case].mean() - y[n_case:].mean())
        b, c = ols_c(y, x, ko)
        loo = []
        if len(animals) - 1 >= 4:
            for d in range(len(animals)):
                keep = [i for i in range(len(animals)) if i != d]
                if len(set(ko[keep])) == 2:
                    loo.append(ols_c(y[keep], x[keep], ko[keep])[1])
        loo_min, loo_max = (min(loo), max(loo)) if loo else (None, None)
        stable = None if not loo else bool(all(np.sign(v) == np.sign(c) for v in loo))
        p3a_ratio = p3a.get((cname, name)) if cat != "set" else None
        # background from P3a control-against-control contrasts
        bg = [abs(p3a[(k, name)]) for k in ("CC_SW", "CC_NW", "CC_SN") if p3a.get((k, name)) is not None] if cat != "set" else []
        bgmax = max(bg) if bg else None
        bgflag = None if bgmax is None else bool(bgmax > 0.25)
        # label
        if not deletion:
            label = "BACKGROUND_CONTRAST"
        elif not qualifies:
            label = f"DESCRIPTIVE (n {n_case} v {n_ctrl}: fewer than three per arm)"
        elif abs(delta) < 0.5:
            label = "NO_SHIFT"
        elif stable is False:
            label = "UNSTABLE"
        elif np.sign(c) == np.sign(delta) and abs(c) >= 0.3 and abs(c) >= 0.5 * abs(delta):
            label = "STANDS"
        else:
            label = "EXPLAINED_BY_STAGE"
        rows.append([cname, name, cat, "measured", round(delta, 3), round(b, 3), round(c, 3),
                     "" if loo_min is None else round(loo_min, 3), "" if loo_max is None else round(loo_max, 3),
                     "" if stable is None else stable, "" if p3a_ratio is None else round(p3a_ratio, 3),
                     "" if bgflag is None else bgflag, label])

hdr = ["contrast", "item", "category", "status", "raw_delta_log2", "slope_on_stage_score", "genotype_term_c", "c_loo_min", "c_loo_max",
       "c_sign_stable_loo", "p3a_log2_ratio", "background_flag_p3a_gt_0.25", "label"]
with open(OUT / "stage_adjusted_by_contrast.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(hdr)
    w.writerows(rows)

# per-item summary: C_S label, literal-reading label, agreement across the four deletion contrasts
summ = []
by = {}
for r in rows:
    by.setdefault(r[1], {})[r[0]] = r
for name, cat in ITEMS:
    d = by.get(name, {})
    cs = d.get("C_S")
    if not cs or cs[3] != "measured":
        summ.append([name, cat, "not measured in C_S", "", "", "", "", "", ""])
        continue
    agree = 0
    shifted = 0
    for k in ("H_S", "H_N", "H_null", "C_S"):
        r = d.get(k)
        if r and r[3] == "measured":
            if abs(r[4]) >= 0.5:
                shifted += 1
                if np.sign(r[6]) == np.sign(r[4]) and abs(r[6]) >= 0.3:
                    agree += 1
    summ.append([name, cat, cs[12], cs[4], cs[6], cs[11] if cs[11] != "" else "", shifted, agree, "DESCRIPTIVE (literal 'three or fewer' reading: no contrast qualifies)"])
with open(OUT / "seed_summary.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["item", "category", "C_S_label", "C_S_raw_delta", "C_S_genotype_term_c", "background_flag_p3a", "n_deletion_contrasts_with_abs_delta_ge_0.5",
                "of_which_c_keeps_sign_and_ge_0.3", "label_under_literal_three_or_fewer_reading"])
    w.writerows(summ)
# stage score table
with open(OUT / "stage_scores_per_animal.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["contrast", "animal", "arm", "stage_score_full_covariate"])
    for cname, tis, case, ctrl, deletion in CONTR:
        gene, cols = DATA[tis]
        sc = stage_score(gene, cols, case, ctrl)
        for a in case:
            w.writerow([cname, a, "case", round(sc[a], 3)])
        for a in ctrl:
            w.writerow([cname, a, "control", round(sc[a], 3)])
# sign agreement with P3a
agree = tot = 0
for r in rows:
    if r[3] == "measured" and r[10] != "" and r[0] in ("H_S", "H_N", "H_null", "C_S") and abs(r[10]) >= 0.2:
        tot += 1
        agree += int(np.sign(r[4]) == np.sign(r[10]))
print(f"sign agreement of the raw per-animal delta with P3a's log2 ratio (|P3a| >= 0.2): {agree} of {tot}")
for s in summ:
    print("\t".join(str(v) for v in s[:8]))
