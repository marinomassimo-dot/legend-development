"""ADV-095 unit A: pre-registered premise screen of the broad-recovery mechanisms on the held WWOX-deficient data.

Implements PREREGISTRATION_UNIT_A_FROZEN_BEFORE_ANY_VALUE_SCI_20261119.md (sha256 2275a7781317618cca2ba1bf9ca1f360bfc157e846d7c1ce80f532e215ca6133).
Held files only; no network. Usage:

    python3 premise_screen_unit_a.py run <files_dir> <out_dir>

<files_dir> is the repository files/ folder (geo/, i18_proteome/, reference_ensembl_r92/). Unit: one library (D1) or one GEO sample treated as one animal (D2, D3).
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import gzip
import itertools
import re
from pathlib import Path

import numpy as np

FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)
SEED, N_NULL = 20261119, 1000
rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------- registered sets (human symbols)
SETS = {  # name: (genes, premise direction +1 higher / -1 lower in knockout)
    "M1_WNT_TARGETS": ("AXIN2 LEF1 NKD1 APCDD1 SP5 TCF7 DKK1 NOTUM TNFRSF19 SOX9".split(), -1),
    "M2_ISR_ATF4": ("ATF4 DDIT3 ASNS TRIB3 CHAC1 PSAT1 PHGDH SHMT2 MTHFD2 SLC7A11 SESN2 ATF3 CEBPG PCK2 SLC1A5 EIF4EBP1".split(), +1),
    "M3a_OL_MATURE": ("MBP PLP1 MOG MOBP MAG CNP ENPP6".split(), -1),
    "M3b_OPC_LINEAGE": ("PDGFRA CSPG4 OLIG1 OLIG2 SOX10 NKX2-2".split(), -1),
    "M4_NRF2_TARGETS": ("NQO1 HMOX1 GCLC GCLM TXNRD1 SRXN1 FTH1 FTL G6PD GSR PRDX1".split(), -1),
    "M5_GLYCOLYSIS_PDK": ("PDK1 PDK2 PDK3 PDK4 LDHA SLC16A1 HK2 PFKP PKM SLC2A1".split(), +1),
    "M6_MYC_TARGETS": ("NCL NPM1 ODC1 CAD SRM PPAT GNL3 NOP56 NOP58 DDX21 EIF4A1 RCC1".split(), +1),
    "E1_ASTRO_REACTIVE": ("GFAP VIM C3 LCN2 CD44 SERPINA3 STAT3".split(), +1),
    "DELETION_WWOX": (["WWOX"], -1),
}
DESCR = {"M7_M8_DESCRIPTION": "HDAC4 HDAC5 HDAC7 HDAC9 MEF2C EZH2 EED SUZ12".split()}
PANELS_D1 = {"PROLIF": "MKI67 TOP2A CCNB1 CCNA2 CDK1 UBE2C CENPF PCNA MCM2 MCM6 TYMS".split(),
             "PROG": "SOX2 PAX6 HES1 VIM NES FABP7".split(), "NEU": "STMN2 DCX TUBB3 MAP2 SNAP25 SYT1".split()}
LATE = "Grin2a Slc12a5 Nrgn Camk2a Scn8a".split()
REF = "Snap25 Rbfox3 Syt1 Stmn2 Tubb3 Map2".split()
OL_GUARD = "Mbp Plp1 Mog Mobp".split()
MOUSE_ALIAS = {"SERPINA3": "Serpina3n"}


def mouse(sym):
    return MOUSE_ALIAS.get(sym, sym.title() if sym != "NKX2-2" else "Nkx2-2")


def pct_band(a):
    return np.percentile(a, [2.5, 97.5])


# ---------------------------------------------------------------- D1 organoid
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
mean1 = L1.mean(axis=1)
KO1 = np.array([0, 0, 1, 1, 1, 1], float)

# ---------------------------------------------------------------- D2 / D3 mouse
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
            v = np.array(a[3:], float)
            gene[g] = gene.get(g, 0) + v
    return gene, {c: i for i, c in enumerate(cols)}


CORT, CORT_COLS = load_tpm("geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz")
HIPP, HIPP_COLS = load_tpm("geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz")
MOUSE_CONTRASTS = [  # name, data, cols, KO samples, control samples, tested
    ("D2_cortex_S", CORT, CORT_COLS, ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
    ("D3_hippo_S", HIPP, HIPP_COLS, ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], False),
    ("D3_hippo_N", HIPP, HIPP_COLS, ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
    ("D3_hippo_null", HIPP, HIPP_COLS, ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], False),
]


def ols(y, X):
    return np.linalg.lstsq(X, y, rcond=None)[0]


def ols_many(Y, X):
    """Y: n x k; returns beta 3 x k via pseudo-inverse"""
    return np.linalg.pinv(X) @ Y


out_sets, out_gene, out_ctrl, out_cov = [], [], [], []

# ================================================================= D1
def d1_cov(omit=()):
    pl = [g for g in PANELS_D1["PROLIF"] if g in gi1 and g not in omit]
    pg = [g for g in PANELS_D1["PROG"] if g in gi1 and g not in omit]
    nu = [g for g in PANELS_D1["NEU"] if g in gi1 and g not in omit]
    return L1[[gi1[g] for g in pl]].mean(0), L1[[gi1[g] for g in nu]].mean(0) - L1[[gi1[g] for g in pg]].mean(0)


def d1_stats(v, prolif, mat):
    """raw cluster shifts, adjusted cluster shifts, c and loo range for one set value vector v (6 libs)"""
    y = v - prolif
    X = np.column_stack([np.ones(6), mat, KO1])
    b = ols(y, X)
    adj = y - b[1] * mat
    res = {"R": {}, "A1": {}}
    for k, idx in CL.items():
        res["R"][k] = float(v[idx].mean() - v[:2].mean())
        res["A1"][k] = float(adj[idx].mean() - adj[:2].mean())
    loo = []
    for d in range(6):
        keep = [i for i in range(6) if i != d]
        loo.append(float(ols(y[keep], X[keep])[2]))
    # N2 alone (ADV-069 form: raw set value on maturity, no prolif subtraction)
    c_n2 = float(ols(v, X)[2])
    return res, float(b[2]), loo, c_n2


prolif_all, mat_all = d1_cov()
sep_d1 = float(mat_all[2:].mean() - mat_all[:2].mean())
out_cov.append(["D1_organoid", "maturity_NEU_minus_PROG", "KO_mean_minus_WT_mean", round(sep_d1, 3),
                "per library: " + ";".join(f"{l}={m:.2f}" for l, m in zip(LIBS, mat_all)),
                "PROLIF per library: " + ";".join(f"{l}={m:.2f}" for l, m in zip(LIBS, prolif_all))])

missing = {}
setgenes1 = {}
for name, (gl, dr) in SETS.items():
    got = [g for g in gl if g in gi1]
    if len(got) < len(gl):
        missing[("D1", name)] = [g for g in gl if g not in gi1]
    setgenes1[name] = got

d1_res = {}
splits1 = [c for c in itertools.combinations(range(6), 4)]
for name, got in setgenes1.items():
    if len(got) < 1:
        continue
    omit = set(got)
    prolif, mat = d1_cov(omit)
    v = L1[[gi1[g] for g in got]].mean(0)
    res, c, loo, c_n2 = d1_stats(v, prolif, mat)
    # null
    pool = np.array([i for i in np.where(np.abs(mean1 - mean1[[gi1[g] for g in got]].mean()) <= 0.5)[0]
                     if g1[i] not in omit and g1[i] not in sum(PANELS_D1.values(), [])])
    nulls = {k: [] for k in CL}
    for _ in range(N_NULL):
        dr = rng.choice(pool, size=len(got), replace=False)
        r, _, _, _ = d1_stats(L1[dr].mean(0), prolif_all, mat_all)
        for k in CL:
            nulls[k].append(r["A1"][k])
    # permutation of KO labels (15 splits of 6 libs into 4 + 2), c with covariate
    y = v - prolif
    cp = []
    for ko in splits1:
        lab = np.zeros(6)
        lab[list(ko)] = 1
        cp.append(ols(y, np.column_stack([np.ones(6), mat, lab]))[2])
    cp = np.array(cp)
    perm_p = float((np.abs(cp) >= abs(c) - 1e-12).mean())
    floor = abs(float(y[0] - y[1]))
    d1_res[name] = dict(res=res, c=c, loo=loo, nulls={k: np.array(n) for k, n in nulls.items()}, floor=floor, perm_p=perm_p, n=len(got), c_n2=c_n2)
    for k in CL:
        lo, hi = pct_band(d1_res[name]["nulls"][k])
        out_sets.append(["D1_organoid", name, k, len(got), round(res["R"][k], 3), round(res["A1"][k], 3),
                         round(c, 3), f"{min(loo):.3f}..{max(loo):.3f}", f"{lo:.3f}..{hi:.3f}", round(floor, 3), round(perm_p, 3), round(c_n2, 3)])
    for g in got:
        out_gene.append(["D1_organoid", name, g] + [round(float(L1[gi1[g], i]), 3) for i in range(6)])

# ================================================================= D2 / D3 (mouse)
def stage_scores(gene, cols, ko, ctrl, omit=()):
    base = lambda g: np.mean([np.log2(gene[g] + 1)[cols[c]] for c in ctrl])
    late = [g for g in LATE if g in gene and g not in omit]
    ref = [g for g in REF if g in gene and g not in omit]
    sc = {}
    for a in ko + ctrl:
        sc[a] = float(np.mean([np.log2(gene[g] + 1)[cols[a]] - base(g) for g in late]) - np.mean([np.log2(gene[g] + 1)[cols[a]] - base(g) for g in ref]))
    return sc


def ol_scores(gene, cols, ko, ctrl, omit=()):
    gs = [g for g in OL_GUARD if g in gene and g not in omit]
    if not gs:
        return None
    base = {g: np.mean([np.log2(gene[g] + 1)[cols[c]] for c in ctrl]) for g in gs}
    return {a: float(np.mean([np.log2(gene[g] + 1)[cols[a]] - base[g] for g in gs])) for a in ko + ctrl}


for cname, gene, cols, ko, ctrl, tested in MOUSE_CONTRASTS:
    names = ko + ctrl
    n = len(names)
    kov = np.array([1.0] * len(ko) + [0.0] * len(ctrl))
    allg = list(gene)
    Lm = np.array([np.log2(gene[g] + 1.0)[[cols[s] for s in names]] for g in allg])
    gim = {g: i for i, g in enumerate(allg)}
    meanm = Lm.mean(1)
    sc_full = stage_scores(gene, cols, ko, ctrl)
    x_full = np.array([sc_full[s] for s in names])
    sep = float(x_full[:len(ko)].mean() - x_full[len(ko):].mean())
    out_cov.append([cname, "stage_score_late_minus_reference", "KO_mean_minus_control_mean", round(sep, 3),
                    "per sample: " + ";".join(f"{s}={sc_full[s]:.2f}" for s in names), f"n_KO={len(ko)} n_ctrl={len(ctrl)}"])
    splits = list(itertools.combinations(range(n), len(ko))) if tested else []
    for name, (gl, dr) in SETS.items():
        got = [mouse(g) for g in gl if mouse(g) in gim]
        if len(got) < len(gl):
            missing[(cname, name)] = [mouse(g) for g in gl if mouse(g) not in gim]
        if not got:
            continue
        omit = set(got)
        sc = stage_scores(gene, cols, ko, ctrl, omit)
        x = np.array([sc[s] for s in names])
        v = Lm[[gim[g] for g in got]].mean(0)
        X = np.column_stack([np.ones(n), x, kov])
        b = ols(v, X)
        R = float(v[kov == 1].mean() - v[kov == 0].mean())
        c = float(b[2])
        loo = []
        if tested:
            for d in range(n):
                keep = [i for i in range(n) if i != d]
                loo.append(float(ols(v[keep], X[keep])[2]))
        # A2 stage + OL guard (D2 only; not for OL sets that share genes with the guard)
        c2 = ""
        if tested and not name.startswith("M3"):
            ol = ol_scores(gene, cols, ko, ctrl, omit)
            o = np.array([ol[s] for s in names])
            c2 = round(float(ols(v, np.column_stack([np.ones(n), x, o, kov]))[3]), 3)
        lo_hi, perm_p, floor = "", "", ""
        if tested:
            pool = np.array([i for i in np.where(np.abs(meanm - meanm[[gim[g] for g in got]].mean()) <= 0.5)[0]
                             if allg[i] not in omit and allg[i] not in LATE + REF + OL_GUARD])
            Xp = np.column_stack([np.ones(n), x_full, kov])
            draws = np.array([rng.choice(pool, size=len(got), replace=False) for _ in range(N_NULL)])
            Y = np.array([Lm[d].mean(0) for d in draws]).T
            nullc = ols_many(Y, Xp)[2]
            lo, hi = pct_band(nullc)
            lo_hi = f"{lo:.3f}..{hi:.3f}"
            cp = []
            for kos in splits:
                lab = np.zeros(n)
                lab[list(kos)] = 1
                cp.append(ols(v, np.column_stack([np.ones(n), x, lab]))[2])
            perm_p = round(float((np.abs(np.array(cp)) >= abs(c) - 1e-12).mean()), 3)
            ctrl_idx = [i for i in range(n) if kov[i] == 0]
            lm = [float(np.mean([v[j] for j in ctrl_idx if j != d])) for d in ctrl_idx]
            floor = round(max(lm) - min(lm), 3)
            d2_null = nullc
            if cname == "D2_cortex_S":
                d1_res.setdefault("_d2", {})[name] = dict(R=R, c=c, loo=loo, lohi=(lo, hi), floor=float(floor), perm_p=float(perm_p), n=len(got), c2=c2)
        out_sets.append([cname, name, "all_KO", len(got), round(R, 3), round(c, 3), round(c, 3),
                         (f"{min(loo):.3f}..{max(loo):.3f}" if loo else ""), lo_hi, floor, perm_p, c2])
        for g in got:
            out_gene.append([cname, name, g] + [round(float(Lm[gim[g], i]), 3) for i in range(n)])
    # description-only transcripts
    if tested:
        for g in DESCR["M7_M8_DESCRIPTION"]:
            mg = mouse(g)
            if mg in gim:
                y = Lm[gim[mg]]
                bb = ols(y, np.column_stack([np.ones(n), x_full, kov]))
                out_gene.append([cname, "M7_M8_DESCRIPTION", mg, f"R={y[kov == 1].mean() - y[kov == 0].mean():.3f}", f"A1_c={bb[2]:.3f}"])
    if tested:
        # controls
        sc_ref = [v for v in [REF]]
        refv = Lm[[gim[g] for g in REF if g in gim]].mean(0)
        out_ctrl.append([cname, "REF_STABLE shift (R)", round(float(refv[kov == 1].mean() - refv[kov == 0].mean()), 3), "negative control: expected |shift| < 0.3"])
        wv = Lm[gim["Wwox"]]
        out_ctrl.append([cname, "WWOX shift (R)", round(float(wv[kov == 1].mean() - wv[kov == 0].mean()), 3), "positive control: expected negative"])

# D1 controls
refv1 = L1[[gi1[g] for g in PANELS_D1["NEU"] if g in gi1]].mean(0)
out_ctrl.append(["D1_organoid", "NEU panel shift KO minus WT (R)", round(float(refv1[2:].mean() - refv1[:2].mean()), 3), "negative control reference; maturity covariate itself"])
wv1 = L1[gi1["WWOX"]]
out_ctrl.append(["D1_organoid", "WWOX shift (R)", round(float(wv1[2:].mean() - wv1[:2].mean()), 3), "positive control: expected negative"])

# ================================================================= labels
def qual(R, A, nullhi, floor, drn):
    """Q (drn=+1 premise direction as given) per pre-registration: |R|,|A| >= 0.3 same sign as drn, outside null band, above floor"""
    lo, hi = nullhi
    sgn = np.sign(drn)
    ok_sign = np.sign(R) == sgn and np.sign(A) == sgn
    ok_mag = abs(R) >= 0.3 and abs(A) >= 0.3
    ok_null = (A > hi) if sgn > 0 else (A < lo)
    return bool(ok_sign and ok_mag and ok_null and abs(A) > floor)


labels = []
d2 = d1_res.get("_d2", {})
for name, (gl, dr) in SETS.items():
    if name == "DELETION_WWOX" or name not in d1_res:
        continue
    r1 = d1_res[name]
    r2 = d2.get(name)
    q1 = all(qual(r1["res"]["R"][k], r1["res"]["A1"][k], pct_band(r1["nulls"][k]), r1["floor"], dr) for k in CL)
    q1o = all(qual(r1["res"]["R"][k], r1["res"]["A1"][k], pct_band(r1["nulls"][k]), r1["floor"], -dr) for k in CL)
    r1_ok = {k: abs(r1["res"]["R"][k]) >= 0.3 for k in CL}
    a1_fail = any(r1_ok[k] and (abs(r1["res"]["A1"][k]) < 0.3 or np.sign(r1["res"]["A1"][k]) != np.sign(r1["res"]["R"][k])) for k in CL)
    if r2:
        q2 = qual(r2["R"], r2["c"], r2["lohi"], r2["floor"], dr) and all(np.sign(x) == np.sign(r2["c"]) for x in r2["loo"])
        q2o = qual(r2["R"], r2["c"], r2["lohi"], r2["floor"], -dr) and all(np.sign(x) == np.sign(r2["c"]) for x in r2["loo"])
        a2_fail = abs(r2["R"]) >= 0.3 and (abs(r2["c"]) < 0.3 or np.sign(r2["c"]) != np.sign(r2["R"]))
        r2_flat = abs(r2["R"]) < 0.3
    else:
        q2 = q2o = a2_fail = False
        r2_flat = True
    r1_flat = not any(r1_ok.values())
    if name.startswith("M3"):
        lab = "M3_SEE_COMBINED_ROW"
    elif q1 and q2:
        lab = "PREMISE_SUPPORTED_T"
    elif q1o and q2o:
        lab = "PREMISE_OPPOSITE_T"
    elif a1_fail or a2_fail:
        lab = "ADJUSTMENT_DEPENDENT"
    elif q1 or q2 or q1o or q2o:
        lab = "PARTIAL"
    elif r1_flat and r2_flat:
        lab = "FLAT"
    else:
        lab = "MIXED"
    labels.append([name, "higher" if dr > 0 else "lower", lab, f"D1_Q={q1} D1_Qopp={q1o} D2_Q={q2} D2_Qopp={q2o} D1_adjfail={a1_fail} D2_adjfail={a2_fail}"])
# M3 combined (mouse D2 only)
a, b_ = d2.get("M3a_OL_MATURE"), d2.get("M3b_OPC_LINEAGE")
if a and b_:
    block = (b_["R"] >= -0.3 and a["R"] <= -1.0) and (b_["c"] >= -0.3 and a["c"] <= -1.0)
    loss = (a["R"] <= -0.5 and b_["R"] <= -0.5) and (a["c"] <= -0.5 and b_["c"] <= -0.5)
    labels.append(["M3_combined", "block vs loss", "DIFFERENTIATION_BLOCK" if block else ("LINEAGE_LOSS" if loss else "NEITHER"),
                   f"mature R={a['R']:.2f} A1={a['c']:.2f}; OPC R={b_['R']:.2f} A1={b_['c']:.2f}; mouse cortex only; composition-confounded by construction"])
labels.append(["M7_class_IIa_HDAC_MEF2", "n/a", "UNDECIDED_NO_RNA_READOUT", "registered"])
labels.append(["M8_EZH2", "n/a", "UNDECIDED_NO_RNA_READOUT", "registered"])

# ================================================================= unbiased replicated-gene list
def per_gene_c_d1():
    prolif, mat = prolif_all, mat_all
    y = L1 - prolif
    X = np.column_stack([np.ones(6), mat, KO1])
    return ols_many(y.T, X)[2]


c1 = per_gene_c_d1()
cname, gene, cols, ko, ctrl, _ = MOUSE_CONTRASTS[0]
names = ko + ctrl
kov = np.array([1.0] * len(ko) + [0.0] * len(ctrl))
sc = stage_scores(gene, cols, ko, ctrl)
x = np.array([sc[s] for s in names])
allg = list(gene)
Lm = np.array([np.log2(gene[g] + 1.0)[[cols[s] for s in names]] for g in allg])
c2 = ols_many(Lm.T, np.column_stack([np.ones(len(names)), x, kov]))[2]
cov_genes = {g.upper() for g in LATE + REF}
mouse_i = {g.upper(): i for i, g in enumerate(allg)}
cand = []
for g in g1:
    u = g.upper()
    if u in cov_genes or u not in mouse_i:
        continue
    i1, i2 = gi1[g], mouse_i[u]
    if mean1[i1] < 3 or Lm[i2, 4:].mean() < 3:
        continue
    a_, b_2 = c1[i1], c2[i2]
    if np.sign(a_) == np.sign(b_2) and a_ != 0:
        cand.append((min(abs(a_), abs(b_2)), u, a_, b_2))
cand.sort(reverse=True)
with open(OUT / "unbiased_replicated_genes.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["direction", "rank", "symbol", "A1_c_organoid_D1", "A1_c_cortex_D2", "min_abs"])
    for dirn, sg in (("up_in_KO", 1), ("down_in_KO", -1)):
        r = 0
        for m, u, a_, b_2 in cand:
            if np.sign(a_) == sg:
                r += 1
                if r > 40:
                    break
                w.writerow([dirn, r, u, round(float(a_), 3), round(float(b_2), 3), round(float(m), 3)])

# ================================================================= D4 protein echo
prot = {}
with open(FILES / "i18_proteome/zeng2024_table_s1_parsed.tsv") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        prot[r["symbol"].upper()] = (float(r["log2fc"]), float(r["bh_adj_p"]))
echo = []
for name, (gl, dr) in SETS.items():
    det = [(g, prot[g]) for g in gl if g in prot]
    if det:
        echo.append([name, len(gl), len(det), round(float(np.mean([v[0] for _, v in det])), 3), sum(1 for _, v in det if v[1] < 0.05),
                     "; ".join(f"{g}:{v[0]:+.2f}({v[1]:.2g})" for g, v in det)])
    else:
        echo.append([name, len(gl), 0, "", 0, "none detected"])
for g in DESCR["M7_M8_DESCRIPTION"]:
    if g in prot:
        echo.append(["M7_M8_" + g, 1, 1, round(prot[g][0], 3), int(prot[g][1] < 0.05), f"{g}:{prot[g][0]:+.2f}({prot[g][1]:.2g})"])

# ================================================================= write
def w(name, header, rws):
    with open(OUT / name, "w", newline="") as f:
        wr = csv.writer(f, delimiter="\t")
        wr.writerow(header)
        wr.writerows(rws)


w("set_results.tsv", ["dataset", "set", "contrast_or_cluster", "n_genes_detected", "R_raw_shift", "A1_adjusted_shift_or_c", "c_genotype_term", "c_leave_one_out_range",
                      "null_band_2.5_97.5_of_A1", "noise_floor", "label_permutation_p", "N2_alone_c_or_A2_stage_plus_OL_c"], out_sets)
w("labels.tsv", ["set", "premise_direction_in_KO", "label", "detail"], labels)
w("controls.tsv", ["dataset", "control", "value", "expectation"], out_ctrl)
w("covariate_separation.tsv", ["dataset", "covariate", "contrast", "value", "per_sample", "extra"], out_cov)
w("gene_values.tsv", ["dataset", "set", "gene"] + [f"v{i}" for i in range(1, 8)], out_gene)
w("protein_echo_D4.tsv", ["set", "n_registered", "n_detected", "mean_log2fc_silenced_vs_control", "n_BH_below_0.05", "detail"], echo)
with open(OUT / "missing_genes.txt", "w") as f:
    for k, v in missing.items():
        f.write(f"{k[0]}\t{k[1]}\t{','.join(v)}\n")
print("done", len(out_sets), "set rows;", len(labels), "labels")
