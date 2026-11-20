"""ADV-095 unit A3: is the replicated activity-regulated transcript deficit neuron-specific, and does it track the oligodendrocyte-lineage deficit across contrasts?

Implements PREREGISTRATION_UNIT_A3_FROZEN_BEFORE_ANY_CELLTYPE_VALUE_SCI_20261119.md (sha256 f3e01b311dc2a8e7276e8ed80e42badf8ff0d3a8e596dc5adddd6b088f5aaf19). Held files only; no network. Usage:

    python3 activity_celltype_unit_a3.py run <files_dir> <out_dir>

<files_dir> is the repository files/ folder (geo/, reference_ensembl_r92/). Unit: one GEO sample = one animal (bulk), one library (organoid); nuclei are descriptive (one pool per arm).
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

ACT = "Fos Fosb Npas4 Arc Egr1 Egr2 Egr4 Junb Nr4a1 Bdnf Btg2 Dusp1".split()
NEURON_CTRL = "Snap25 Rbfox3 Syt1 Stmn2 Tubb3 Map2".split()
M3A = "Mbp Plp1 Mog Mobp Mag Cnp Enpp6".split()
LATE = "Grin2a Slc12a5 Nrgn Camk2a Scn8a".split()
REF = NEURON_CTRL
STAGES = {"OPC": "Pdgfra Cspg4 Cspg5 Pcdh15".split(), "COP": "Gpr17 Neu4 Bmp4 Vcan".split(),
          "NFOL": "Tcf7l2 Itpr2 Enpp6 Bcas1 Tmem2 Fyn Casr".split(), "MFOL": "Mal Mog Opalin Serinc5 Mag".split(),
          "MOL": "Klk6 Apod Pmp22 Slc5a11 Ermn Hapln2".split()}
CLASSES = {"excitatory": "Slc17a7 Camk2a Satb2".split(), "inhibitory": "Gad1 Gad2 Slc32a1".split(),
           "astrocyte": "Aqp4 Aldh1l1 Slc1a2".split(), "microglia": "Cx3cr1 P2ry12 Csf1r".split(), **STAGES}
PANELS_D1 = {"PROLIF": "MKI67 TOP2A CCNB1 CCNA2 CDK1 UBE2C CENPF PCNA MCM2 MCM6 TYMS".split(),
             "PROG": "SOX2 PAX6 HES1 VIM NES FABP7".split(), "NEU": "STMN2 DCX TUBB3 MAP2 SNAP25 SYT1".split()}
NEEDED = sorted({g for v in [ACT, NEURON_CTRL, M3A, LATE] + list(CLASSES.values()) for g in v})

t2g = {}
for line in gzip.open(FILES / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz", "rt"):
    if line[0] == ">":
        m = re.search(r"gene_symbol:(\S+)", line)
        if m:
            t2g[line[1:].split()[0].split(".")[0]] = m.group(1)


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


def gm(gene, cols, g, names):
    return np.log2(gene[g] + 1.0)[[cols[s] for s in names]]


missing = []
rows_bulk, rows_cls = [], []
bulk = {}
for cname, gene, cols, ko, ctrl, tested in CONTRASTS:
    names = ko + ctrl
    n = len(names)
    kov = np.array([1.0] * len(ko) + [0.0] * len(ctrl))
    base = {g: np.mean(gm(gene, cols, g, ctrl)) for g in LATE + REF if g in gene}
    stage = np.array([np.mean([gm(gene, cols, g, [s])[0] - base[g] for g in LATE if g in gene])
                      - np.mean([gm(gene, cols, g, [s])[0] - base[g] for g in REF if g in gene]) for s in names])
    X = np.column_stack([np.ones(n), stage, kov])
    for label, gl in (("ACT", ACT), ("NEURON_CTRL", NEURON_CTRL), ("M3a_OL_MATURE", M3A)):
        got = [g for g in gl if g in gene]
        if len(got) < len(gl):
            missing.append((cname, label, ",".join(g for g in gl if g not in gene)))
        v = np.mean([gm(gene, cols, g, names) for g in got], axis=0)
        R = float(v[kov == 1].mean() - v[kov == 0].mean())
        c = float(ols(v, X)[2])
        loo = []
        if tested:
            for d in range(n):
                keep = [i for i in range(n) if i != d]
                loo.append(float(ols(v[keep], X[keep])[2]))
        bulk[(cname, label)] = (R, c, loo)
        rows_bulk.append([cname, label, len(got), round(R, 3), round(c, 3), (f"{min(loo):.3f}..{max(loo):.3f}" if loo else ""),
                          "labelable" if tested else "descriptive"])

# organoid (D1), same formulas as unit A
WT, KO = ["cwt1", "cwt2"], ["cko1", "cko2", "cko3", "cko4"]
LIBS = WT + KO
CL = {"cko1+cko2": [2, 3], "cko3+cko4": [4, 5]}
rows = {}
with gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt") as fh:
    head = fh.readline().rstrip("\n").split("\t")
    ix = {c: i for i, c in enumerate(head)}
    for line in fh:
        a = line.rstrip("\n").split("\t")
        rows[a[0]] = np.array([float(a[ix[c]]) for c in LIBS])
g1 = list(rows)
M1 = np.array([rows[g] for g in g1])
L1 = np.log2(M1 / M1.sum(axis=0) * 1e6 + 1.0)
gi1 = {g: i for i, g in enumerate(g1)}
KO1 = np.array([0, 0, 1, 1, 1, 1], float)


def d1_cov(omit=()):
    pl = [g for g in PANELS_D1["PROLIF"] if g in gi1 and g not in omit]
    pg = [g for g in PANELS_D1["PROG"] if g in gi1 and g not in omit]
    nu = [g for g in PANELS_D1["NEU"] if g in gi1 and g not in omit]
    return L1[[gi1[g] for g in pl]].mean(0), L1[[gi1[g] for g in nu]].mean(0) - L1[[gi1[g] for g in pg]].mean(0)


for label, gl in (("ACT", ACT), ("NEURON_CTRL", NEURON_CTRL)):
    got = [g.upper() for g in gl if g.upper() in gi1]
    if len(got) < len(gl):
        missing.append(("D1_organoid", label, ",".join(g for g in gl if g.upper() not in gi1)))
    prolif, mat = d1_cov(set(got))
    v = L1[[gi1[g] for g in got]].mean(0)
    y = v - prolif
    Xo = np.column_stack([np.ones(6), mat, KO1])
    b = ols(y, Xo)
    adj = y - b[1] * mat
    for k, idx in CL.items():
        R = float(v[idx].mean() - v[:2].mean())
        A = float(adj[idx].mean() - adj[:2].mean())
        rows_bulk.append(["D1_organoid_" + k, label, len(got), round(R, 3), round(A, 3), "", "descriptive (reference moved: see unit A)"])
    bulk[("D1", label)] = (float(v[2:].mean() - v[:2].mean()), float(b[2]), [])

# nuclei
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
    return {g: np.log2(v[keep] / total[keep] * 1e6 + 1.0) for g, v in sel.items()}


nuc = {tag: load_arm(tag) for tag in ("ctrl", "ko")}
score = {}
for tag, expr in nuc.items():
    for cl, gl in CLASSES.items():
        score[(tag, cl)] = np.mean([expr[g] for g in gl if g in expr], axis=0)
p99 = {cl: np.percentile(np.concatenate([score[("ctrl", cl)], score[("ko", cl)]]), 99) for cl in CLASSES}
labs, per = {}, {}
for tag, expr in nuc.items():
    cls = list(CLASSES)
    M = np.column_stack([score[(tag, cl)] / (p99[cl] if p99[cl] > 0 else 1) for cl in cls])
    amax = M.argmax(1)
    ok = M.max(1) >= 0.2
    lab = np.array([cls[i] if o else "unassigned" for i, o in zip(amax, ok)])
    labs[tag] = lab
    act_genes = [g for g in ACT if g in expr]
    nc_genes = [g for g in NEURON_CTRL if g in expr]
    if len(act_genes) < len(ACT):
        missing.append(("nuclei_" + tag, "ACT", ",".join(g for g in ACT if g not in expr)))
    act = np.mean([expr[g] for g in act_genes], axis=0)
    ctl = np.mean([expr[g] for g in nc_genes], axis=0)
    for cl in cls + ["all_assigned"]:
        m = (lab != "unassigned") if cl == "all_assigned" else (lab == cl)
        per[(tag, cl)] = (int(m.sum()), float(act[m].mean()) if m.sum() else float("nan"), float(ctl[m].mean()) if m.sum() else float("nan"),
                          {g: float(expr[g][m].mean()) for g in act_genes} if m.sum() else {})
for cl in list(CLASSES) + ["all_assigned"]:
    n0, a0, c0, g0 = per[("ctrl", cl)]
    n1, a1, c1, g1_ = per[("ko", cl)]
    rows_cls.append([cl, n0, n1, round(a0, 3), round(a1, 3), round(a1 - a0, 3), round(c0, 3), round(c1, 3), round(c1 - c0, 3)])
genes_cls = [[cl, g, round(per[("ctrl", cl)][3].get(g, float("nan")), 3), round(per[("ko", cl)][3].get(g, float("nan")), 3)]
             for cl in ("excitatory", "inhibitory", "astrocyte", "microglia", "OPC") for g in ACT if g in per[("ctrl", cl)][3]]

# rules
d = {r[0]: r[5] for r in rows_cls}
dctl = {r[0]: r[8] for r in rows_cls}
glia = [d[c] for c in ("astrocyte", "microglia", "OPC")]
neuron_specific = d["excitatory"] <= -0.3 and np.mean(glia) > -0.15 and abs(dctl["excitatory"]) <= 0.2
global_ = np.mean(glia) <= -0.3 or abs(dctl["excitatory"]) > 0.2 and dctl["excitatory"] <= -0.3
c_ok = bulk[("D2_cortex_S", "ACT")][1] <= -0.3 and all(x < 0 for x in bulk[("D2_cortex_S", "ACT")][2])
org_ok = bulk[("D1", "ACT")][1] <= -0.3
replicated = c_ok and org_ok
verdict = [["neuron_specific_in_nuclei", str(bool(neuron_specific)), f"excitatory dACT={d['excitatory']:.3f}; mean glia dACT={np.mean(glia):.3f}; excitatory dNEURON_CTRL={dctl['excitatory']:.3f}"],
           ["global_not_neuron_specific", str(bool(global_)), "glial dACT at most -0.3 or depth control moved"],
           ["replicated_second_deposit_after_adjustment", str(bool(replicated)), f"cortex A1={bulk[('D2_cortex_S','ACT')][1]:.3f} all LOO negative={c_ok}; organoid pooled A1={bulk[('D1','ACT')][1]:.3f}"],
           ["branch_per_registered_stop_rule", "CONTINUE_TO_AGENT_ROUND" if (neuron_specific and replicated) else "STOP", "stop if not neuron-specific or not replicated"]]
coupling = []
for cn in ("D2_cortex_S", "D3_hippo_S", "D3_hippo_N", "D3_hippo_null"):
    a, m3 = bulk[(cn, "ACT")], bulk[(cn, "M3a_OL_MATURE")]
    coupling.append([cn, round(a[0], 3), round(a[1], 3), round(m3[0], 3), round(m3[1], 3)])
coupling.append(["D1_organoid_pooled", round(bulk[("D1", "ACT")][0], 3), round(bulk[("D1", "ACT")][1], 3), "", "(no oligodendrocyte lineage)"])


def w(name, header, rws):
    with open(OUT / name, "w", newline="") as f:
        wr = csv.writer(f, delimiter="\t", lineterminator="\n")
        wr.writerow(header)
        wr.writerows([list(r) + [""] * (len(header) - len(r)) for r in rws])


w("bulk_activity_panels.tsv", ["dataset", "panel", "n_genes", "R_raw", "A1_adjusted_or_c", "c_leave_one_out", "status"], rows_bulk)
w("nuclei_activity_by_class.tsv", ["class", "n_nuclei_ctrl", "n_nuclei_ko", "ACT_ctrl", "ACT_ko", "dACT_ko_minus_ctrl", "NEURON_CTRL_ctrl", "NEURON_CTRL_ko", "dNEURON_CTRL"], rows_cls)
w("nuclei_activity_genes_by_class.tsv", ["class", "gene", "mean_log2cpm_ctrl", "mean_log2cpm_ko"], genes_cls)
w("coupling_activity_vs_mature_OL.tsv", ["dataset", "ACT_R", "ACT_A1", "M3a_R", "M3a_A1"], coupling)
w("rule_verdicts.tsv", ["rule", "value", "detail"], verdict)
with open(OUT / "missing_genes.txt", "w") as f:
    f.write("dataset\tpanel\tregistered_genes_not_found\n")
    for r in missing:
        f.write("\t".join(r) + "\n")
print("done")
