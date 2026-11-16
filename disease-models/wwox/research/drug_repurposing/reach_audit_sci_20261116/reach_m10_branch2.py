#!/usr/bin/env python3
"""Reach audit, M10 branch 2: hallmark mTORC1 enrichment in the organoid contrast (GSE156243, 4 KO v 2 WT), unadjusted and after removing the
maturation axis (a per-gene calibration slope from GSE150123 regressed out of the per-gene statistic). Uses the public Enrichr MSigDB_Hallmark_2020 library
downloaded to files/reach_audit_downloads (digest in access.tsv). A POST-HOC reach demonstration of the setter's branch 2, a deviation (the setter named
'adjustment for the composite score'; this adjusts by calibration slope), not scored.

    python3 reach_m10_branch2.py --help
    python3 reach_m10_branch2.py run <repo_root> <files_dir> <out_tsv>

Statistic: Welch t of log2(CPM+1), KO v WT (n 4 v 2). ES: weighted (p = 1) running sum over the ranked genes; permutation p from 5,000 gene-label permutations; NES = ES over the mean
|ES| of same-sign permutations; BH q over the 50 hallmark sets. Gene-label permutation is anti-conservative (genes are not exchangeable). Not medical advice.
"""
import sys
if len(sys.argv) != 5 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, importlib.util, math, random, statistics
from pathlib import Path
import numpy as np
REPO, FILES, OUT = Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
DR = REPO / "disease-models/wwox/research/drug_repurposing"
cnt = {}
for l in gzip.open(FILES / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz", "rt"):
    a = l.rstrip("\n").split("\t")
    if a[0] == "gene": cols = a[1:]; continue
    cnt[a[0].upper()] = np.array(a[1:], float)
lib = np.array(list(cnt.values())).sum(axis=0); ki = [i for i, c in enumerate(cols) if c.startswith("cko")]; wi = [i for i, c in enumerate(cols) if c.startswith("cwt")]
genes = [g for g, v in cnt.items() if (v / lib * 1e6)[ki + wi].mean() >= 1]
L = {g: np.log2(cnt[g] / lib * 1e6 + 1) for g in genes}
def welch(g):
    k, w = L[g][ki], L[g][wi]; se = math.sqrt(k.var(ddof=1) / len(k) + w.var(ddof=1) / len(w)) or 1e-9; return (k.mean() - w.mean()) / se
t = {g: welch(g) for g in genes}
spec = importlib.util.spec_from_file_location("mc", DR / "gse156243/maturation_calibration.py"); mc = importlib.util.module_from_spec(spec); sys.argv = ["x"]; spec.loader.exec_module(mc)
s2e = mc.symbol_to_ensg(); want = {g: s2e[g] for g in genes if g in s2e}
meta, cc = mc.calibration_matrix(want); samples = [s for s in cc if s in meta]
lines = [meta[s]["iPSc line"] for s in samples]; days = [math.log2(float(meta[s]["differentiation day"])) for s in samples]
xm = {l: statistics.mean(d for d, ll in zip(days, lines) if ll == l) for l in set(lines)}; xs = np.array([d - xm[l] for d, l in zip(days, lines)]); den = float((xs ** 2).sum())
slope = {}
for g in want:
    y = np.array([math.log2(cc[s]["genes"].get(g, 0) / cc[s]["total"] * 1e6 + 1) for s in samples])
    ym = {l: y[[i for i, ll in enumerate(lines) if ll == l]].mean() for l in set(lines)}; slope[g] = float((xs * np.array([y[i] - ym[lines[i]] for i in range(len(y))])).sum() / den)
common = [g for g in genes if g in slope and math.isfinite(slope[g]) and math.isfinite(float(t[g]))]
sv = np.array([slope[g] for g in common]); tv = np.array([t[g] for g in common]); b = float(((sv - sv.mean()) * (tv - tv.mean())).sum() / ((sv - sv.mean()) ** 2).sum())
adj = {g: float(t[g] - b * slope[g]) for g in common}
hall = {}
for l in open(FILES / "reach_audit_downloads/MSigDB_Hallmark_2020.gmt"):
    p = l.rstrip("\n").split("\t"); hall[p[0]] = [x for x in p[2:] if x]
rng = random.Random(20261116)
def es(order, ranks, S):
    # order: genes sorted by stat desc; weighted running sum
    hit = np.array([g in S for g in order]); w = np.abs(ranks) * hit
    if hit.sum() == 0: return 0.0
    up = np.cumsum(w / w.sum()); dn = np.cumsum((~hit) / (~hit).sum()); r = up - dn; return float(r[np.argmax(np.abs(r))])
def run(stat):
    order = sorted(stat, key=lambda g: -stat[g]); ranks = np.array([stat[g] for g in order]); res = {}
    for hname, gl in hall.items():
        S = {g.upper() for g in gl} & set(order)
        if len(S) < 10: continue
        obs = es(order, ranks, S); pm = []
        for _ in range(1000):
            pm.append(es(order, ranks, set(rng.sample(order, len(S)))))
        same = [abs(x) for x in pm if (x >= 0) == (obs >= 0)] or [1]
        p = (sum(1 for x in pm if (abs(x) >= abs(obs)) and ((x >= 0) == (obs >= 0))) + 1) / (len(pm) + 1); res[hname] = (len(S), obs, obs / statistics.mean(same), p)
    ps = sorted(v[3] for v in res.values()); m = len(ps)
    q = {}
    for h, v in res.items(): q[h] = min(1.0, min(p * m / (i + 1) for i, p in enumerate(ps) if p >= v[3]))
    return {h: (*v, q[h]) for h, v in res.items()}
rows = []
for name, stat in (("unadjusted", {g: t[g] for g in common}), ("adjusted for maturation slope", adj)):
    r = run(stat)
    for h in ("mTORC1 Signaling", "Glycolysis", "Hypoxia"):
        n, e, nes, p, q = r[h]; rows.append((name, h, n, round(e, 3), round(nes, 2), round(p, 4), round(q, 4)))
rows.append(("note", "slope coefficient on the per-gene t statistic", len(common), round(b, 3), "", "", ""))
with open(OUT, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["ranking", "hallmark", "n_genes_in_set_present", "ES", "NES", "perm_p_1000", "BH_q_50_sets"]); w.writerows(rows)
for r in rows: print(r)
