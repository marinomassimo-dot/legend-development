"""ADV-069: DNA-damage / p53-response signature in the public organoid deposit GSE156243 (WWOX-knockout against wild-type cerebral organoids, week 15).

Implements PREREGISTRATION_FROZEN_BEFORE_ANY_COUNT_SCI_20261119.md exactly (sha256 c0b475ee7e36de1c33820460da29bb2e004efc9d34757cb7a56ca307c2627a6f).
Held file only; no network. Usage:

    python3 ddr_signature_analysis.py run <count_table.gz> <out_dir>
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__)
    raise SystemExit(0)

import csv
import gzip
from pathlib import Path

import numpy as np

COUNTS, OUT = Path(sys.argv[2]), Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)

SETS = {
    "P53_RESP": ["CDKN1A", "GADD45A", "MDM2", "BBC3", "BAX", "PPM1D", "SESN1", "DDB2", "ZMAT3", "TP53I3", "RRM2B", "FAS", "TNFRSF10B", "AEN"],
    "REPAIR_S": ["BRCA1", "BRCA2", "RAD51", "RAD51AP1", "RAD54L", "FANCD2", "FANCI", "EXO1", "TIMELESS", "CLSPN"],
    "DDR_CORE": ["ATM", "ATR", "CHEK1", "CHEK2", "TP53", "MDC1", "TP53BP1", "H2AFX", "NBN", "MRE11", "RAD50"],
    "CC_NEG": ["CDKN1B", "CDKN1C", "CDKN2C", "RB1", "RBL2", "BTG1", "BTG2"],
}
NORM = {
    "PROLIF": ["MKI67", "TOP2A", "CCNB1", "CCNA2", "CDK1", "UBE2C", "CENPF", "PCNA", "MCM2", "MCM6", "TYMS"],
    "PROG": ["SOX2", "PAX6", "HES1", "VIM", "NES", "FABP7"],
    "NEU": ["STMN2", "DCX", "TUBB3", "MAP2", "SNAP25", "SYT1"],
}
WT = ["cwt1", "cwt2"]
KO = ["cko1", "cko2", "cko3", "cko4"]
CLUSTERS = {"cko1+cko2": ["cko1", "cko2"], "cko3+cko4": ["cko3", "cko4"]}
LIBS = WT + KO
SEED = 20261119
N_NULL = 2000

rows = {}
with gzip.open(COUNTS, "rt") as fh:
    header = fh.readline().rstrip("\n").split("\t")
    idx = {c: i for i, c in enumerate(header)}
    for line in fh:
        a = line.rstrip("\n").split("\t")
        rows[a[0]] = np.array([float(a[idx[c]]) for c in LIBS])
genes = list(rows)
mat = np.array([rows[g] for g in genes])
cpm = mat / mat.sum(axis=0) * 1e6
L = np.log2(cpm + 1.0)
gidx = {g: i for i, g in enumerate(genes)}
mean_expr = L.mean(axis=1)
li = {c: i for i, c in enumerate(LIBS)}

missing = {}


def present(names, label):
    got = [g for g in names if g in gidx]
    lost = [g for g in names if g not in gidx]
    if lost:
        missing[label] = lost
    return got


def libvals(glist):
    """per-library mean log2(CPM+1) over the genes"""
    return L[[gidx[g] for g in glist]].mean(axis=0)


setgenes = {k: present(v, k) for k, v in SETS.items()}
normgenes = {k: present(v, k) for k, v in NORM.items()}
nv = {k: libvals(v) for k, v in normgenes.items()}
wtmean = lambda v: float(np.mean([v[li[c]] for c in WT]))


def shift(v):
    return {c: float(v[li[c]] - wtmean(v)) for c in KO}


prolif_shift = shift(nv["PROLIF"])
maturity = nv["NEU"] - nv["PROG"]

rng = np.random.default_rng(SEED)
out_rows, detail = [], []
X_full = np.column_stack([np.ones(6), maturity, np.array([0, 0, 1, 1, 1, 1], float)])


def ols_c(y, X):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    return float(beta[2])


for name, gl in setgenes.items():
    v = libvals(gl)
    adj_lib = {c: shift(v)[c] - prolif_shift[c] for c in KO}
    raw_lib = shift(v)
    # noise floor: wild-type pair, N1-adjusted
    nf = abs((v[li["cwt1"]] - nv["PROLIF"][li["cwt1"]]) - (v[li["cwt2"]] - nv["PROLIF"][li["cwt2"]]))
    # null pool matched on mean expression
    set_mean = float(np.mean(mean_expr[[gidx[g] for g in gl]]))
    pool = np.where(np.abs(mean_expr - set_mean) <= 0.5)[0]
    excl = set(gidx[g] for g in gl) | set(gidx[g] for k in normgenes.values() for g in k)
    pool = np.array([p for p in pool if p not in excl])
    null_adj = {k: [] for k in CLUSTERS}
    draws = [rng.choice(pool, size=len(gl), replace=False) for _ in range(N_NULL)]
    for dr in draws:
        nvv = L[dr].mean(axis=0)
        sh = {c: float(nvv[li[c]] - wtmean(nvv)) - prolif_shift[c] for c in KO}
        for k, libs in CLUSTERS.items():
            null_adj[k].append(float(np.mean([sh[c] for c in libs])))
    # N2: genotype term after maturity, with leave-one-library-out
    c_full = ols_c(v, X_full)
    loo = []
    for drop in range(6):
        keep = [i for i in range(6) if i != drop]
        loo.append(ols_c(v[keep], X_full[keep]))
    res = {"set": name, "n_genes": len(gl), "n_pool": len(pool), "noise_floor_N1": round(nf, 3), "c_genotype_after_maturity": round(c_full, 3),
           "c_loo_min": round(min(loo), 3), "c_loo_max": round(max(loo), 3)}
    passes, signs = {}, {}
    for k, libs in CLUSTERS.items():
        raw = float(np.mean([raw_lib[c] for c in libs]))
        adj = float(np.mean([adj_lib[c] for c in libs]))
        nl = np.array(null_adj[k])
        pct = float((nl < adj).mean() + 0.5 * (nl == adj).mean())
        lo, hi = np.percentile(nl, [2.5, 97.5])
        ok = abs(adj) >= 0.3 and (adj < lo or adj > hi) and abs(adj) > nf
        passes[k], signs[k] = ok, np.sign(adj)
        res.update({f"{k}_raw_shift": round(raw, 3), f"{k}_N1_adjusted_shift": round(adj, 3), f"{k}_null_percentile": round(pct, 3),
                    f"{k}_null_band_2.5_97.5": f"{lo:.2f}..{hi:.2f}", f"{k}_exceeds_noise_and_0.3_and_null": ok})
    same_sign = signs["cko1+cko2"] == signs["cko3+cko4"] and signs["cko1+cko2"] != 0
    n_pass = sum(passes.values())
    clusters_ok = (n_pass == 2) and same_sign
    sgn = signs["cko1+cko2"]
    n2_ok = abs(c_full) >= 0.3 and np.sign(c_full) == sgn and all(np.sign(x) == np.sign(c_full) for x in loo)
    if clusters_ok and n2_ok:
        verdict = "S-ok (signal present in both clusters and after both normalisations)"
    elif clusters_ok and not n2_ok:
        verdict = "STOP S2 (lost after composition normalisation N2)"
    elif n_pass == 1 or (n_pass == 2 and not same_sign):
        verdict = "STOP S1 (signal in one cluster only, or opposite signs)"
    else:
        verdict = "ABSENT (no signal in either cluster after N1; not a label named in the pre-registration, same logic as a stop)"
    res["verdict"] = verdict
    out_rows.append(res)
    for g in gl:
        detail.append([name, g, *[round(float(L[gidx[g], li[c]]), 3) for c in LIBS]])

keys = list(out_rows[0].keys())
with open(OUT / "set_results.tsv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys, delimiter="\t", lineterminator="\n")
    w.writeheader()
    w.writerows(out_rows)
with open(OUT / "gene_log2cpm_by_library.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["set", "gene"] + LIBS)
    w.writerows(detail)
with open(OUT / "normalisation_panels.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["panel", "n_genes", "per_library_mean_log2cpm_" + "_".join(LIBS), "KO_shift_vs_WT_" + "_".join(KO)])
    for k, v in nv.items():
        s = shift(v)
        w.writerow([k, len(normgenes[k])] + [";".join(f"{x:.3f}" for x in v), ";".join(f"{s[c]:.3f}" for c in KO)])
    w.writerow(["maturity_NEU_minus_PROG", "", ";".join(f"{x:.3f}" for x in maturity), ""])
with open(OUT / "missing_genes.txt", "w") as f:
    f.write(repr(missing) + "\n")
for r in out_rows:
    print(r["set"], r["verdict"], "| c =", r["c_genotype_after_maturity"], "| clusters:", r["cko1+cko2_N1_adjusted_shift"], r["cko3+cko4_N1_adjusted_shift"])
print("missing:", missing)
