#!/usr/bin/env python3
"""IT28 P10 pilot (see PRE_DECLARATION.md): do the human-derived seed directions replicate in the P47T partial-loss mouse more often than expression-matched decoys?
Usage: pilot_it28.py run   (writes pilot_result.json and pilot_seeds.tsv). Offline, numpy + standard library."""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import csv, gzip, json, collections
from pathlib import Path
import numpy as np
H = Path(__file__).resolve().parent
D = H.parent
REG = ("PFC", "CTX", "HPC")
MIN = 0.15
t = collections.defaultdict(dict)
for r in csv.DictReader(gzip.open(D / "verification_it27_p1_20261104/results/p1a_all_regions_own_results.tsv.gz", "rt"), delimiter="\t"):
    if r["region"] in REG:
        t[r["symbol"]][r["region"]] = (float(r["log2FoldChange"]), float(r["baseMean"]))
genes = {g: d for g, d in t.items() if len(d) == 3}
up = {g.upper(): g for g in genes}
seeds = []
for q in ("Q2", "Q3", "Q8"):
    for r in csv.DictReader(open(D / f"generation_it22_p1_20261103/inputs_it22/seeds_p1/{q}_expression_tiersAB.tsv"), delimiter="\t"):
        if r["kind"] == "gene" and r["direction"] in ("up", "down") and r["direction_status"] == "defined" and r["gene"].upper() in up:
            seeds.append((r["gene"], up[r["gene"].upper()], 1 if r["direction"] == "up" else -1, q))
names = list(genes)
bm = np.array([np.mean([genes[g][x][1] for x in REG]) for g in names])
dec = np.digitize(bm, np.quantile(bm, np.linspace(0, 1, 11)[1:-1]))
L = np.array([[genes[g][x][0] for x in REG] for g in names])


def concordant(lfc, s):
    sg = np.where(np.abs(lfc) >= MIN, np.sign(lfc), 0)
    return bool(np.all(sg == s))


obs = [concordant(L[names.index(m)], s) for _, m, s, _ in seeds]
rng = np.random.default_rng(20261105)
pool = {k: np.where(dec == k)[0] for k in range(10)}
sdec = [dec[names.index(m)] for _, m, _, _ in seeds]
N = 100000
cnt = np.zeros(N, dtype=int)
for _, k in enumerate(sdec):
    idx = rng.choice(pool[k], size=N)
    s = rng.choice([-1, 1], size=N)
    sg = np.where(np.abs(L[idx]) >= MIN, np.sign(L[idx]), 0)
    cnt += np.all(sg == s[:, None], axis=1)
o = int(sum(obs))
res = dict(n_seed_genes=len(seeds), observed_concordant=o, null_mean=float(cnt.mean()), null_p_ge_observed=float((cnt >= o).mean()), draws=N, decoy_pool_genes=len(names))
json.dump(res, open(H / "pilot_result.json", "w"), indent=1)
with open(H / "pilot_seeds.tsv", "w") as f:
    f.write("question\tseed_gene\tseed_direction\tlog2FC_PFC\tlog2FC_CTX\tlog2FC_HPC\tconcordant\n")
    for (g, m, s, q), c in zip(seeds, obs):
        f.write(f"{q}\t{g}\t{'up' if s>0 else 'down'}\t" + "\t".join(f"{genes[m][x][0]:+.2f}" for x in REG) + f"\t{c}\n")
print(json.dumps(res))
