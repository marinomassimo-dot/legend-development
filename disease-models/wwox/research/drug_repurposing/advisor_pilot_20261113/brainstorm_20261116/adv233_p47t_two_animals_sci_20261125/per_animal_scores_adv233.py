"""ADV-233 per-animal set scores and matched random-set counter-check. Implements PREREG_ADV233_SCI_20261125.md section 2.
Writes per_animal_scores_adv233.tsv and random_sets_adv233.tsv into the folder given as the third argument. Held files only.
tmm_factors and logcpm are copied verbatim from p47t_it12_20261031/p47t_reanalysis_it12.py.

Usage: python3 -I per_animal_scores_adv233.py <GSE215425_processed.csv.gz> <mh.gmt> <outdir>
"""
import sys

if len(sys.argv) != 4:
    print(__doc__)
    raise SystemExit(0)
import gzip, os
import numpy as np

counts_p, gmt_p, out = sys.argv[1:4]

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

H = ["TNFA_SIGNALING_VIA_NFKB", "IL6_JAK_STAT3_SIGNALING", "INFLAMMATORY_RESPONSE", "HYPOXIA", "GLYCOLYSIS",
     "CHOLESTEROL_HOMEOSTASIS", "FATTY_ACID_METABOLISM", "MTORC1_SIGNALING"]
sets = {}
for l in open(gmt_p):
    p = l.rstrip("\n").split("\t")
    n = p[0].replace("HALLMARK_", "")
    if n in H:
        sets[n] = p[2:]
assert len(sets) == len(H), sorted(sets)
sets["NRF2_5"] = ["Nqo1", "Hmox1", "Gclm", "Srxn1", "Txnrd1"]
sets["REACTIVE_PAN_organoid_list"] = ["C3", "Cd44", "Vim", "Timp1", "Cebpd", "Stat3", "Socs3", "Lcn2", "Chil1", "Serpina3n"]
with gzip.open(counts_p, "rt") as fh:
    head = fh.readline().rstrip("\n").split("\t")[2:]
    rows = [l.rstrip("\n").split("\t") for l in fh]
sym = [r[1] for r in rows]
C = np.array([[float(v) for v in r[2:]] for r in rows])
by = {}
for i, s in enumerate(sym):
    if s not in by or C[i].sum() > C[by[s]].sum():
        by[s] = i
rng = np.random.default_rng(20261125)
A, R = [], []
for reg in ("HPC", "CTX", "PFC", "CB"):
    cols = [j for j, c in enumerate(head) if c.startswith(reg + "_")]
    animals = [head[j].split("_", 2)[2] for j in cols]
    geno = ["P47T" if "P47T" in head[j] else "WT" for j in cols]
    cnt = C[:, cols]
    f, ref = tmm_factors(cnt[cnt.sum(1) > 0])
    lib_eff = cnt.sum(0) * f
    lc = logcpm(cnt, lib_eff)
    cpm_mean = (cnt / lib_eff * 1e6).mean(1)
    cen = lc - lc.mean(1, keepdims=True)
    expr = [i for s, i in by.items() if cpm_mean[i] >= 1]
    expr = np.array(sorted(expr))
    q = np.quantile(lc[expr].mean(1), [0.2, 0.4, 0.6, 0.8])
    qbin = np.digitize(lc[expr].mean(1), q)
    pos = {g: k for k, g in enumerate(expr)}
    pool = [expr[qbin == b] for b in range(5)]
    m6, f8 = animals.index("M6"), animals.index("F8")
    for name, genes in sets.items():
        idx = [by[g] for g in genes if g in by and cpm_mean[by[g]] >= 1]
        sc = cen[idx].mean(0)
        order = list(np.argsort(-sc))
        for k, a in enumerate(animals):
            A.append((reg, name, a, geno[k], "%.4f" % sc[k], str(order.index(k) + 1), str(len(idx))))
        top2 = set(order[:2]) == {m6, f8}
        need = np.bincount([qbin[pos[i]] for i in idx], minlength=5)
        hits = 0
        for _ in range(1000):
            pick = np.concatenate([rng.choice(pool[b], size=need[b], replace=False) for b in range(5) if need[b]])
            s = cen[pick].mean(0)
            hits += set(np.argsort(-s)[:2]) == {m6, f8}
        R.append((reg, name, str(len(idx)), str(top2), "%.3f" % (hits / 1000.0)))
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "per_animal_scores_adv233.tsv"), "w") as o:
    o.write("region\tset\tanimal\tgenotype\tscore_centred_log2cpm\trank_desc\tn_genes\n")
    for r in A:
        o.write("\t".join(r) + "\n")
with open(os.path.join(out, "random_sets_adv233.tsv"), "w") as o:
    o.write("region\tset\tn_genes\treal_set_M6_F8_are_top2\trandom_sets_fraction_M6_F8_top2\n")
    for r in R:
        o.write("\t".join(r) + "\n")
print("wrote", len(A), len(R))
