"""ADV-303 (IT): oligodendrocyte-lineage stage-marker set medians by region, P47T over WT (GSE215425 processed counts).
Run: python3 -I stage_markers_adv303.py --counts GSE215425_processed_data.csv.gz --sterol sterol_sets_frozen.json --out results
tmm_factors and logcpm are copied unchanged from composition_bound_adv198.py (SCI, ADV-198) / p47t_reanalysis_it12.py."""
import argparse, csv, gzip, itertools, json, os
import numpy as np

def tmm_factors(counts):
    lib = counts.sum(0).astype(float)
    q75 = np.array([np.percentile(counts[:, j][counts[:, j] > 0] / lib[j], 75) for j in range(counts.shape[1])])
    ref = int(np.argmin(np.abs(q75 - q75.mean())))
    f = np.ones(counts.shape[1])
    for j in range(counts.shape[1]):
        if j == ref: continue
        a, b = counts[:, j].astype(float), counts[:, ref].astype(float)
        ok = (a > 0) & (b > 0); a, b = a[ok], b[ok]
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
    avg = lib_eff.mean(); pc = prior * lib_eff / avg
    return np.log2((counts + pc) / (lib_eff + 2 * pc) * 1e6)

SETS = {
 "OPC": ["Pdgfra", "Cspg4", "Ptprz1", "Cspg5", "Vcan"],
 "COMMITTED_NEWLY_FORMED": ["Gpr17", "Neu4", "Bcas1", "Enpp6", "Itpr2", "Tcf7l2", "Tmem2"],
 "MATURE": ["Mbp", "Plp1", "Mobp", "Mog", "Mag", "Mal", "Opalin", "Aspa", "Ermn", "Klk6", "Cnp"],
}
ap = argparse.ArgumentParser()
ap.add_argument("--counts", required=True); ap.add_argument("--sterol", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
SETS["LIPOGENIC_S1"] = json.load(open(a.sterol))["sterol_core"]
rows = list(csv.reader(gzip.open(a.counts, "rt"), delimiter="\t")); hdr = rows[0]
res = {}; log = []
for reg in ("CB", "HPC", "CTX", "PFC"):
    cols = [j for j, h in enumerate(hdr) if h.startswith(reg + "_")]
    labels = [hdr[j] for j in cols]; geno = np.array([1 if "P47T" in l else 0 for l in labels])
    sym = {}
    for r in rows[1:]:
        v = np.array([float(r[j]) for j in cols]); sym[r[1]] = sym.get(r[1], 0) + v
    genes = list(sym); C = np.array([sym[g] for g in genes])
    f, ref = tmm_factors(C[C.sum(1) > 0]); lib_eff = C.sum(0) * f
    lc = logcpm(C, lib_eff); cpm = C / lib_eff * 1e6
    keep = (cpm >= 1).sum(1) >= 3; gi = {g: i for i, g in enumerate(genes) if keep[i]}
    n = len(labels); idx = np.arange(n); nm = int(geno.sum())
    def lfc(sel_wt, sel_mu): return lc[:, sel_mu].mean(1) - lc[:, sel_wt].mean(1)
    L = lfc(np.where(geno == 0)[0], np.where(geno == 1)[0])
    log.append(f"{reg}: libraries {labels}; genes kept {int(keep.sum())}; global median log2FC {np.median(L[keep]):.3f}")
    res[reg] = {}
    for name, gl in SETS.items():
        present = [g for g in gl if g in gi]; missing = [g for g in gl if g not in gi]
        if len(present) < 3:
            res[reg][name] = dict(n_present=len(present), median=None, status="UNDETERMINED", missing=missing); continue
        ii = [gi[g] for g in present]
        obs = float(np.median(L[ii]))
        # exact permutation over genotype labels
        cnt = tot = 0
        for comb in itertools.combinations(range(n), nm):
            mu = np.array(comb); wt = np.array([k for k in range(n) if k not in comb])
            s = float(np.median((lc[:, mu].mean(1) - lc[:, wt].mean(1))[ii])); tot += 1
            if abs(s) >= abs(obs) - 1e-12: cnt += 1
        loo = []
        for k in range(n):
            wt = np.array([j for j in np.where(geno == 0)[0] if j != k]); mu = np.array([j for j in np.where(geno == 1)[0] if j != k])
            loo.append(float(np.median(lfc(wt, mu)[ii])))
        per_gene = {g: round(float(L[gi[g]]), 3) for g in present}
        res[reg][name] = dict(n_present=len(present), n_declared=len(gl), median=round(obs, 3), perm_p=round(cnt / tot, 4),
                              loo_min=round(min(loo), 3), loo_max=round(max(loo), 3), frac_up=round(float(np.mean([v > 0 for v in per_gene.values()])), 2),
                              per_gene=per_gene, missing=missing, status="OK")
        log.append(f"{reg} {name}: {len(present)}/{len(gl)} genes, median {obs:+.3f}, perm p {cnt/tot:.3f}, LOO [{min(loo):+.3f},{max(loo):+.3f}], missing {missing}")
json.dump(res, open(os.path.join(a.out, "stage_markers_adv303.json"), "w"), indent=1)
open(os.path.join(a.out, "run_log_adv303.txt"), "w").write("\n".join(log) + "\n")
print("\n".join(log))
