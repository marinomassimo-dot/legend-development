"""ADV-198 analysis (SCI): composition bound for the P47T cerebellar sterol signature.
Run: python3 composition_bound_adv198.py --counts GSE215425_processed_data.csv.gz --frozen frozen --out results
TMM and logCPM functions are reused from p47t_it12_20261031/p47t_reanalysis_it12.py (IT12), unchanged."""
import argparse, csv, gzip, json, os
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

ap = argparse.ArgumentParser()
ap.add_argument("--counts", required=True); ap.add_argument("--frozen", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
rows = list(csv.reader(gzip.open(a.counts, "rt"), delimiter="\t"))
hdr = rows[0]
cols = [j for j, h in enumerate(hdr) if h.startswith("CB_")]
labels = [hdr[j] for j in cols]
geno = np.array([1 if "P47T" in l else 0 for l in labels])
sym = {}
for r in rows[1:]:
    v = np.array([float(r[j]) for j in cols])
    sym[r[1]] = sym.get(r[1], 0) + v
genes = list(sym); C = np.array([sym[g] for g in genes])
f, ref = tmm_factors(C[C.sum(1) > 0])
lib_eff = C.sum(0) * f
lc = logcpm(C, lib_eff); cpm = C / lib_eff * 1e6
keep = (cpm >= 1).sum(1) >= 3
gi = {g: i for i, g in enumerate(genes) if keep[i]}
wt, mu = np.where(geno == 0)[0], np.where(geno == 1)[0]
def lfc(idx_wt, idx_mu): return lc[:, idx_mu].mean(1) - lc[:, idx_wt].mean(1)
L0 = lfc(wt, mu)
G = float(np.median(L0[keep]))
sets = json.load(open(os.path.join(a.frozen, "sterol_sets_frozen.json")))
marks = json.load(open(os.path.join(a.frozen, "marker_sets_frozen.json")))
def setstat(gl, w, m):
    ii = [gi[g] for g in gl if g in gi]
    l = lfc(w, m)[ii]
    return len(ii), float(l.mean()), float((l > 0).mean())
out = []
out.append(f"libraries: {labels}; genes kept {int(keep.sum())}; TMM factors {np.round(f,3).tolist()}; global median log2FC G = {G:.3f}")
res = {}
for name, gl in (("S1_sterol_core", sets["sterol_core"]), ("S2_hallmark_cholesterol_mouse", sets["hallmark_cholesterol_homeostasis_mouse_title_case"])):
    n, d, up = setstat(gl, wt, mu)
    loo = []
    for k in range(len(labels)):
        w = [i for i in wt if i != k]; m = [i for i in mu if i != k]
        loo.append(setstat(gl, np.array(w), np.array(m))[1])
    res[name] = dict(n_used=n, n_declared=len(gl), mean_log2FC=d, frac_up=up, loo_min=min(loo), loo_max=max(loo))
    out.append(f"{name}: used {n}/{len(gl)} d={d:.3f} frac_up={up:.2f} LOO [{min(loo):.3f},{max(loo):.3f}]")
cls = {}
for c, gl in marks.items():
    n, d, up = setstat(gl, wt, mu)
    loo = []
    for k in range(len(labels)):
        w = [i for i in wt if i != k]; m = [i for i in mu if i != k]
        loo.append(setstat(gl, np.array(w), np.array(m))[1] if sum(g in gi for g in gl) else float("nan"))
    cls[c] = dict(n_used=n, n_declared=len(gl), mean_log2FC=d, frac_up=up, loo_min=float(np.nanmin(loo)) if n else None, loo_max=float(np.nanmax(loo)) if n else None, kept=bool(n >= 8))
    out.append(f"class {c}: used {n}/{len(gl)} L={d:.3f} frac_up={up:.2f} LOO [{cls[c]['loo_min']},{cls[c]['loo_max']}] kept={n>=8}")
kept = {c: v for c, v in cls.items() if v["kept"]}
out.append(f"kept classes: {len(kept)}")
if kept:
    B = max(v["mean_log2FC"] for v in kept.values()); Bhi = max(v["loo_max"] for v in kept.values())
    cmax = max(kept, key=lambda c: kept[c]["mean_log2FC"])
    out.append(f"B = max L(c) = {B:.3f} ({cmax}); B_hi (max over classes of LOO max) = {Bhi:.3f}")
    for name, v in res.items():
        out.append(f"{name}: d - B = {v['mean_log2FC']-B:.3f}; LOO min d - B_hi = {v['loo_min']-Bhi:.3f}")
os.makedirs(a.out, exist_ok=True)
with open(os.path.join(a.out, "composition_bound_adv198.json"), "w") as fh: json.dump(dict(G=G, sterol=res, classes=cls), fh, indent=1, sort_keys=True)
with open(os.path.join(a.out, "run_log_adv198.txt"), "w") as fh: fh.write("\n".join(out) + "\n")
print("\n".join(out))
