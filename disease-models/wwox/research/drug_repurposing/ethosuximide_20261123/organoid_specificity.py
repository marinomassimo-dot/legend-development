"""Descriptive organoid sensitivity to sample labels and expression-matched gene selection."""
import argparse
import csv
import gzip
from itertools import combinations
from pathlib import Path

import numpy as np

from analyze import GENES, PANELS, write_tsv


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("counts", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    with gzip.open(args.counts, "rt") as f:
        rows = csv.reader(f, delimiter="\t")
        names = next(rows)[1:]
        data = {}
        for gene, *entries in rows:
            data[gene] = data.get(gene, 0) + np.asarray(entries, dtype=float)
    symbols = list(data)
    mat = np.array(list(data.values()))
    x = np.log2(1 + 1e6*mat/mat.sum(axis=0))
    primary = [symbols.index(g) for g in PANELS["primary"]]
    comparator = [symbols.index(g) for g in PANELS["comparator"]]
    samples = np.arange(len(names))
    observed_controls = [i for i, n in enumerate(names) if n.startswith("cwt")]
    perm = []
    for group in combinations(samples, 2):
        select = np.isin(samples, group)
        d = x[:, ~select].mean(axis=1)-x[:, select].mean(axis=1)
        if list(group) == observed_controls:
            d_obs = d
        perm.append([",".join(names[i] for i in group), np.mean(d[primary]),
                     np.mean(d[primary])-np.mean(d[comparator])])
    write_tsv(args.out/"organoid_allocations.tsv", "control_libraries primary primary_minus_comparator", perm)
    # Match the nearest 200 non-panel genes per target by pooled log-expression.
    expression = x.mean(axis=1)
    eligible = np.array([i for i, s in enumerate(symbols) if s not in GENES])
    pools = [eligible[np.argsort(abs(expression[eligible]-expression[i]), kind="stable")[:200]] for i in primary]
    rng = np.random.default_rng(20261123)
    draws = np.column_stack([rng.choice(pool, 100000) for pool in pools])
    unique = np.all(np.diff(np.sort(draws, axis=1),axis=1)>0,axis=1)
    null = d_obs[draws[unique]]
    obs = d_obs[primary].mean()
    write_tsv(args.out/"organoid_matched.tsv", "draws_unique observed null_median null_q025 null_q975 fraction_mean_as_low fraction_all_negative_and_as_low",
              [[len(null), obs, np.median(null.mean(axis=1)), *np.quantile(null.mean(axis=1), [0.025,0.975]),
                np.mean(null.mean(axis=1) <= obs), np.mean((null.mean(axis=1) <= obs) & np.all(null < 0,axis=1))]])


if __name__ == "__main__":
    main()
