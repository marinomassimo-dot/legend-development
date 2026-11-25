"""ADV-239 first-read influence: per-unit values and leave-one-out of carried small-n transcript quantities.
Implements PREREG_ADV239_SCI_20261125.md. Held files only; no network; stdlib + numpy; deterministic.

Usage: python3 -I influence_adv239.py <files_dir> <hallmark.gmt> <outdir>
  <files_dir> = the untracked data store holding deepening_downloads/, geo/ and reference_ensembl_r92/

tmm_factors and logcpm are copied verbatim from p47t_it12_20261031/p47t_reanalysis_it12.py (as ADV-233 did).
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import gzip, os, re
import numpy as np

FILES, GMT, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)


def tmm_factors(counts):
    """edgeR-style TMM, reference = library whose 75th-percentile-scaled count is closest to the mean of those"""
    lib = counts.sum(0).astype(float)
    q75 = np.array([np.percentile(counts[:, j][counts[:, j] > 0] / lib[j], 75) for j in range(counts.shape[1])])
    ref = int(np.argmin(np.abs(q75 - q75.mean())))
    f = np.ones(counts.shape[1])
    for j in range(counts.shape[1]):
        if j == ref: continue
        a, b = counts[:, j].astype(float), counts[:, ref].astype(float)
        ok = (a > 0) & (b > 0)
        a, b = a[ok], b[ok]
        la, lb = lib[j], lib[ref]
        M = np.log2((a / la) / (b / lb)); A = 0.5 * np.log2((a / la) * (b / lb))
        w = (la - a) / (la * a) + (lb - b) / (lb * b); w = 1 / w
        keepM = (M >= np.quantile(M, 0.30)) & (M <= np.quantile(M, 0.70))
        keepA = (A >= np.quantile(A, 0.05)) & (A <= np.quantile(A, 0.95))
        k = keepM & keepA
        f[j] = 2 ** (np.sum(w[k] * M[k]) / np.sum(w[k]))
    f = f / np.exp(np.mean(np.log(f)))
    return f, ref


def logcpm(counts, lib_eff, prior=2.0):
    avg = lib_eff.mean()
    pc = prior * lib_eff / avg
    return np.log2((counts + pc) / (lib_eff + 2 * pc) * 1e6)


UNITS, SUMMARY = [], []

# statements carried as "no change" / "not elevated" / "not raised" (PREREG: |E| < 0.20 -> not testable for absence)
ABSENCE = {
    "GSE215425": ("gene:Wwox", "gene:Erbb4"),
    "GSE158682": ("set:HIF_AXIS_K01", "gene:Hk2", "gene:Slc2a1", "gene:Ldha", "gene:Pgk1", "gene:Ndrg1", "gene:P4ha1",
                  "gene:Hif1a", "gene:Epas1", "ratio:Slc12a2/Slc12a5", "set:WNT_READOUT"),
}


def influence(dataset, contrast, item, ids, ismut, values, effect_fn, scale, threshold=None):
    """values: array (n_features, n_units); effect_fn(values, ismut_mask) -> float.
    Writes per-unit mean of the features, the full effect and every leave-one-out effect."""
    ids = list(ids)
    ismut = np.array(ismut, bool)
    full = float(effect_fn(values, ismut))
    unit = values.mean(0)
    for a, m, v in zip(ids, ismut, unit):
        UNITS.append((dataset, contrast, item, a, "mutant" if m else "control", "%.4f" % v))
    nm, nc = int(ismut.sum()), int((~ismut).sum())
    mu, cu = unit[ismut], unit[~ismut]
    sep = "all mutant above all control" if mu.min() > cu.max() else (
        "all mutant below all control" if mu.max() < cu.min() else "overlap")
    drops = []
    if nm >= 2 and nc >= 2:
        for k in range(len(ids)):
            keep = np.ones(len(ids), bool); keep[k] = False
            if ismut[keep].sum() < 1 or (~ismut[keep]).sum() < 1: continue
            drops.append((float(effect_fn(values[:, keep], ismut[keep])), ids[k]))
    flips = [i for e, i in drops if np.sign(e) != np.sign(full) and full != 0]
    if drops and full != 0:
        ratios = [(e / full, i) for e, i in drops]
        worst = min(ratios)
    else:
        worst = (float("nan"), "")
    crossed = []
    if threshold is not None:
        met = abs(full) >= threshold
        crossed = [i for e, i in drops if (abs(e) >= threshold) != met]
    if nm < 3 or nc < 3:
        disp = "not testable (an arm below 3)"
    elif item.split(" [")[0] in ABSENCE.get(dataset, ()) and abs(full) < 0.20:
        disp = "not testable for absence (|E| < 0.20)"
    elif flips or worst[0] < 0.50 or crossed:
        disp = "one-animal-driven"
    else:
        disp = "robust"
    rng_drop = ("%.3f" % min(e for e, i in drops), "%.3f" % max(e for e, i in drops)) if drops else ("", "")
    SUMMARY.append((dataset, contrast, item, str(nc), str(nm), scale, "%.3f" % full, rng_drop[0], rng_drop[1],
                    "%.3f" % worst[0], worst[1], ";".join(flips), ";".join(crossed), sep, disp))


# ---------------- GSE215425 (P47T), integer counts, TMM log2 CPM as IT12 ----------------
HALL = {}
for line in open(GMT):
    p = line.rstrip("\n").split("\t")
    HALL[p[0].replace("HALLMARK_", "")] = p[2:]
SETS = {k: HALL[k] for k in ("HYPOXIA", "GLYCOLYSIS", "APOPTOSIS", "TNFA_SIGNALING_VIA_NFKB", "IL6_JAK_STAT3_SIGNALING",
                             "INFLAMMATORY_RESPONSE", "MTORC1_SIGNALING", "CHOLESTEROL_HOMEOSTASIS",
                             "FATTY_ACID_METABOLISM")}
ros = [k for k in HALL if k.startswith("REACTIVE_OXI") or k.startswith("REACTIVE_OXY")]
assert len(ros) == 1, ros
SETS["REACTIVE_OXYGEN_SPECIES"] = HALL[ros[0]]
SETS["HIF_SEL_UP6"] = ["Adm", "Bhlhe40", "P4ha1", "Ankrd37", "Ddit4", "Egln3"]
SETS["HIF_FLAT6"] = ["Pgk1", "Aldoa", "Eno1", "Pkm", "Pfkp", "Ndrg1"]
SETS["NRF2_5"] = ["Nqo1", "Hmox1", "Gclm", "Srxn1", "Txnrd1"]
GENES = ["Hmox1", "Srxn1", "Nqo1", "Hdac5", "Slc2a1", "Erbb4", "Wwox"]

with gzip.open(os.path.join(FILES, "deepening_downloads/gse215425/GSE215425_processed_data.csv.gz"), "rt") as fh:
    head = fh.readline().rstrip("\n").split("\t")[2:]
    rows = [l.rstrip("\n").split("\t") for l in fh]
C = np.array([[float(v) for v in r[2:]] for r in rows])
by = {}
for i, r in enumerate(rows):
    s = r[1]
    if s not in by or C[i].sum() > C[by[s]].sum():
        by[s] = i


def diff_of_means(v, m):
    s = v.mean(0)
    return s[m].mean() - s[~m].mean()


for reg in ("HPC", "CTX", "PFC", "CB"):
    cols = [j for j, c in enumerate(head) if c.startswith(reg + "_")]
    ids = [head[j].split("_", 2)[2] for j in cols]
    mut = ["P47T" in head[j] for j in cols]
    cnt = C[:, cols]
    f, _ = tmm_factors(cnt[cnt.sum(1) > 0])
    lib_eff = cnt.sum(0) * f
    lc = logcpm(cnt, lib_eff)
    cpm_mean = (cnt / lib_eff * 1e6).mean(1)
    cen = lc - lc.mean(1, keepdims=True)
    for name, genes in SETS.items():
        idx = [by[g] for g in genes if g in by and cpm_mean[by[g]] >= 1]
        influence("GSE215425", reg, "set:" + name, ids, mut, cen[idx], diff_of_means, "set mean centred log2CPM")
    for g in GENES:
        if g not in by: continue
        influence("GSE215425", reg, "gene:" + g, ids, mut, lc[[by[g]]], diff_of_means, "log2CPM difference")

# ---------------- GSE158681 / GSE158682 (P17), transcript TPM summed to gene (Ensembl 92) ----------------
t2g = {}
for line in gzip.open(os.path.join(FILES, "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz"), "rt"):
    if line[0] != ">": continue
    tid = line[1:].split()[0].split(".")[0]
    m = re.search(r"gene_symbol:(\S+)", line)
    if m and "_PATCH" not in line.split(" ", 3)[2]:
        t2g[tid] = m.group(1)


def load_tpm(path):
    with gzip.open(path, "rt") as fh:
        h = fh.readline().rstrip("\n").split("\t")[3:]
        G = {}
        for l in fh:
            p = l.rstrip("\n").split("\t")
            s = t2g.get(p[0].split(".")[0])
            if s is None: continue
            v = np.array(p[3:], float)
            G[s] = G.get(s, 0) + v
    return h, G


def log2_ratio_of_means(v, m):
    """per gene log2((mean mutant + 0.5) / (mean control + 0.5)), averaged over genes; v holds linear TPM"""
    return float(np.mean(np.log2((v[:, m].mean(1) + 0.5) / (v[:, ~m].mean(1) + 0.5))))


def influence_tpm(dataset, contrast, item, h, G, ctrl, ko, genes):
    cols = [h.index(c) for c in ctrl + ko]
    got = [g for g in genes if g in G]
    v = np.array([G[g][cols] for g in got])
    mask = [False] * len(ctrl) + [True] * len(ko)
    # per-unit values are recorded on the log scale; the effect uses linear TPM
    ids = ctrl + ko
    full_ids = [c for c in ids]

    def eff(x, m):
        return log2_ratio_of_means(2 ** x - 0.5, m)

    influence(dataset, contrast, item + " [" + ",".join(got) + "]", full_ids, mask, np.log2(v + 0.5), eff,
              "log2 ratio of mean TPM (+0.5), mean over genes")


P17_SETS = {
    "gene:Pvalb": ["Pvalb"], "gene:Gad1": ["Gad1"], "gene:Npy": ["Npy"],
    "gene:Slc12a5": ["Slc12a5"], "gene:Slc12a2": ["Slc12a2"],
    "set:HIF_AXIS_K01": ["Hif1a", "Epas1", "Hk2", "Slc2a1", "Ldha", "Pgk1", "Ndrg1", "P4ha1"],
    "gene:Hk2": ["Hk2"], "gene:Slc2a1": ["Slc2a1"], "gene:Ldha": ["Ldha"], "gene:Pgk1": ["Pgk1"],
    "gene:Ndrg1": ["Ndrg1"], "gene:P4ha1": ["P4ha1"], "gene:Hif1a": ["Hif1a"], "gene:Epas1": ["Epas1"],
    "set:ASTRO_ACTIVATION_J01": ["Gfap", "Vim", "Serpina3n", "Lcn2", "Cd44"],
    "gene:Gfap": ["Gfap"], "gene:Serpina3n": ["Serpina3n"], "gene:Lcn2": ["Lcn2"],
    "set:WNT_READOUT": ["Axin2", "Lef1", "Nkd1", "Apcdd1"],
    "gene:Wwox": ["Wwox"], "gene:Ctgf": ["Ctgf"],
}
hh, GH = load_tpm(os.path.join(FILES, "geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz"))
cc, GC = load_tpm(os.path.join(FILES, "geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz"))
CONTRASTS = [
    ("GSE158682", "cortex Syn-Cre", cc, GC, ["CRTX_S_Ctrl_%d" % i for i in (1, 2, 3, 4)], ["CRTX_S_KO_%d" % i for i in (1, 2, 3)]),
    ("GSE158681", "hippo Syn-Cre", hh, GH, ["S_Ctrl_1", "S_Ctrl_2"], ["S_KO_1", "S_KO_2", "S_KO_3"]),
    ("GSE158681", "hippo Nestin-Cre", hh, GH, ["N_Ctrl_1", "N_Ctrl_2"], ["N_KO_1", "N_KO_2"]),
    ("GSE158681", "hippo germline null", hh, GH, ["WT_1", "WT_2", "WT_3"], ["KO_1", "KO_2"]),
]
for ds, name, h, G, ctrl, ko in CONTRASTS:
    for item, genes in P17_SETS.items():
        influence_tpm(ds, name, item, h, G, ctrl, ko, genes)
    # NKCC1:KCC2 ratio (F03)
    cols = [h.index(c) for c in ctrl + ko]
    ratio = np.log2((G["Slc12a2"][cols] + 0.5) / (G["Slc12a5"][cols] + 0.5))[None, :]
    influence(ds, name, "ratio:Slc12a2/Slc12a5", ctrl + ko, [False] * len(ctrl) + [True] * len(ko), ratio,
              diff_of_means, "difference of mean log2 ratio")

# ---------------- GSE156243 (human organoid), salmon counts, log2(CPM+1) ----------------
with gzip.open(os.path.join(FILES, "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"), "rt") as fh:
    oh = fh.readline().rstrip("\n").split("\t")[1:]
    orows = [l.rstrip("\n").split("\t") for l in fh]
OC = np.array([[float(v) for v in r[1:]] for r in orows])
cpm = OC / OC.sum(0) * 1e6
og = {r[0]: i for i, r in enumerate(orows)}
omut = ["cko" in c for c in oh]
ORG = {
    "set:WNT_READOUT": ["AXIN2", "LEF1", "NKD1", "APCDD1"],
    "set:ISR_ATF4_TARGETS": ["ATF4", "ATF5", "DDIT3", "CHAC1", "TRIB3", "ASNS", "PSAT1", "PHGDH", "PCK2", "SLC7A11", "SESN2", "GADD45A"],
    "gene:LDHA": ["LDHA"], "gene:HK2": ["HK2"], "gene:SLC2A1": ["SLC2A1"], "gene:EPAS1": ["EPAS1"], "gene:HIF1A": ["HIF1A"],
    "gene:PDK1": ["PDK1"], "gene:NFE2L2": ["NFE2L2"], "gene:CTGF": ["CTGF"], "gene:NPY": ["NPY"], "gene:GAD1": ["GAD1"],
    "gene:GAD2": ["GAD2"], "gene:MYC": ["MYC"], "gene:GRIA1": ["GRIA1"],
    "set:ASTRO_REACTIVE_J01": ["GFAP", "VIM", "SERPINA3", "CD44"],
}
for item, genes in ORG.items():
    got = [g for g in genes if g in og]
    if not got:
        SUMMARY.append(("GSE156243", "organoid", item, "2", "4", "", "", "", "", "", "", "", "", "", "gene not in table"))
        continue
    influence("GSE156243", "organoid", item + " [" + ",".join(got) + "]", oh, omut, np.log2(cpm[[og[g] for g in got]] + 1),
              diff_of_means, "difference of mean log2(CPM+1)")
r = np.log2((cpm[og["SLC12A2"]] + 1) / (cpm[og["SLC12A5"]] + 1))[None, :]
influence("GSE156243", "organoid", "ratio:SLC12A2/SLC12A5", oh, omut, r, diff_of_means, "difference of mean log2 ratio")

with open(os.path.join(OUT, "unit_values_adv239.tsv"), "w") as o:
    o.write("deposit\tcontrast\titem\tunit\tarm\tvalue\n")
    for x in UNITS:
        o.write("\t".join(x) + "\n")
with open(os.path.join(OUT, "influence_adv239.tsv"), "w") as o:
    o.write("deposit\tcontrast\titem\tn_control\tn_mutant\tscale\teffect_all\tmin_effect_leave_one_out\tmax_effect_leave_one_out\tmin_ratio_leave_one_out\tunit_at_min\t"
            "sign_flips\tthreshold_crossings\tseparation\tfirst_read\n")
    for x in SUMMARY:
        o.write("\t".join(x) + "\n")
print("rows", len(SUMMARY), "unit rows", len(UNITS))
