#!/usr/bin/env python3
"""P7: the P6 gene sets measured in the WWOX-KO organoid (GSE156243), same method as P6 (see P7_DECLARATION.md).
Usage: python3 -I p7_organoid_same_sets.py <counts.txt.gz> <P6 per_gene_in_sets.tsv> <out_dir>"""
import sys, gzip, csv, json, hashlib
import numpy as np
counts, p6, out = sys.argv[1:4]
rows = list(csv.reader(gzip.open(counts, "rt"), delimiter="\t"))
assert rows[0] == ["gene", "cko1", "cko2", "cko3", "cko4", "cwt1", "cwt2"]
genes = [r[0] for r in rows[1:]]; gi = {g: i for i, g in enumerate(genes)}
M = np.array([[float(x) for x in r[1:]] for r in rows[1:]])
cpm = M / M.sum(0) * 1e6
ko, wt = cpm[:, :4].mean(1), cpm[:, 4:].mean(1)
kocnt, wtcnt = M[:, :4].mean(1), M[:, 4:].mean(1)
uni = (kocnt >= 10) & (wtcnt >= 10)
R = np.log2((ko + .5) / (wt + .5)); Rc = R - np.median(R[uni])
ml = np.log10((kocnt + wtcnt) / 2 + 1)
sets = {}
for r in csv.DictReader(open(p6), delimiter="\t"):
    if r["contrast"] == "C_hNPC": sets.setdefault(r["set"], []).append(r["symbol"])
# members declared but absent from the P6 table (not in CAGE matrix) are re-added from the declared lists
extra = {"ISR_targets": ["SLC7A11"], "UPR_branches": ["PPP1R15A"], "Glycolysis_lactate": ["PKM"], "PDK_family": ["PDK4"],
         "Lactate_transporters": ["SLC16A3"], "Mito_import": ["TOMM70", "TIMM23"], "OXPHOS_nuclear": ["NDUFA11"]}
for k, v in extra.items(): sets[k] = sorted(set(sets.get(k, [])) | set(v))
rng = np.random.default_rng(20261029)
idx = np.where(uni)[0]; qs = np.quantile(ml[idx], np.linspace(0, 1, 11)[1:-1]); dec = np.digitize(ml[idx], qs)
res = []
for s, mem in sets.items():
    m = np.array([gi[g] for g in mem if g in gi and uni[gi[g]]])
    row = dict(set=s, n_declared=len(mem), n_measurable=len(m), mean_centred_R=None)
    if len(m) >= 3:
        md = np.digitize(ml[m], qs); pools = {d: idx[(dec == d) & ~np.isin(idx, m)] for d in range(10)}
        need = {d: int((md == d).sum()) for d in range(10)}
        obs = float(Rc[m].mean())
        nul = np.array([Rc[np.concatenate([rng.choice(pools[d], k, replace=False) for d, k in need.items() if k])].mean() for _ in range(10000)])
        row.update(mean_centred_R=round(obs, 3), null_lo=round(float(np.quantile(nul, .025)), 3), null_hi=round(float(np.quantile(nul, .975)), 3),
                   rank_two_sided=round(float(min(1, 2 * min((nul <= obs).mean(), (nul >= obs).mean()))), 4), mean_uncentred_R=round(float(R[m].mean()), 3))
    res.append(row)
keys = ["set", "n_declared", "n_measurable", "mean_centred_R", "null_lo", "null_hi", "rank_two_sided", "mean_uncentred_R"]
with open(f"{out}/p7_organoid_set_summary.tsv", "w") as f:
    f.write("\t".join(keys) + "\n")
    for r in res: f.write("\t".join(str(r.get(k, "")) for k in keys) + "\n")
key = ["ATF4", "ASNS", "CHAC1", "TRIB3", "DDIT3", "PHGDH", "PSAT1", "PSPH", "SLC7A11", "ATF5", "PCK2", "SESN2", "GADD45A", "LDHA", "LDHB", "HK2", "PDK1", "PDK2", "PDK3", "PDK4", "SLC16A1", "SOX2", "PAX6", "HES5", "FABP7", "VIM", "NES", "WWOX"]
with open(f"{out}/p7_organoid_key_genes.tsv", "w") as f:
    f.write("gene\tmeasurable\tko_cpm\twt_cpm\tko_count_mean\twt_count_mean\tR_centred\tR_uncentred\n")
    for g in key:
        if g in gi:
            i = gi[g]; f.write(f"{g}\t{bool(uni[i])}\t{ko[i]:.2f}\t{wt[i]:.2f}\t{kocnt[i]:.1f}\t{wtcnt[i]:.1f}\t{Rc[i]:.3f}\t{R[i]:.3f}\n")
json.dump(dict(counts_sha256=hashlib.sha256(open(counts, "rb").read()).hexdigest(), p6_table_sha256=hashlib.sha256(open(p6, "rb").read()).hexdigest(),
               n_genes=len(genes), n_measurable=int(uni.sum()), median_uncentred_R=float(np.median(R[uni])), seed=20261029),
          open(f"{out}/p7_params.json", "w"), indent=1)
