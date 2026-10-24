#!/usr/bin/env python3
"""Does the WWOX-KO organoid carry an excess of same-signed canonical Wnt readouts over chance?

Exploratory, one laboratory, KO versus WT cerebral organoids (GSE156243). NOT a Q230P result.
The prediction, the gene sets and the null were fixed in prediction_wnt_sign_20261025.md BEFORE this ran.

The null is a permutation over gene sets of the same size drawn from the expressed universe, never a
hypergeometric test on the whole genome, because the authors' lists are pre-filtered on pvalue < 0.01 and
fold change > 1.2: a classical enrichment against all genes would count the pre-filter as signal.

    python3 wnt_sign_permutation.py [--draws 10000] [--seed 20261025] [--json]
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import random
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
COUNTS = ROOT / "files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"
LIST = HERE / "derived/list_padj_le_0.05.tsv"
MARKERS = HERE / "marker_sets_declared.tsv"

W7 = ["AXIN2", "LEF1", "TCF7L2", "NKD1", "APCDD1", "WNT5A", "CTNNB1"]
W_READOUT = ["AXIN2", "LEF1", "NKD1", "APCDD1"]
MIN_TOTAL_COUNT = 10


def expressed_universe() -> list[str]:
    genes = []
    with gzip.open(COUNTS, "rt", encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter="\t")
        next(reader)
        for row in reader:
            if sum(float(x) for x in row[1:]) >= MIN_TOTAL_COUNT:
                genes.append(row[0])
    return genes


def signed_table() -> dict[str, float]:
    """symbol -> log2FC for genes on the padj<=0.05 list. Absent means not significant, not zero."""
    out = {}
    with LIST.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            out[row["symbol"]] = float(row["log2FoldChange"])
    return out


def marker_genes() -> set[str]:
    """Genes of the COMPOSITION modules only.

    The declared marker file also holds a `wnt_pathway` module, which contains AXIN2, LEF1 and WNT5A: the
    very genes under test. Removing it would make the composition sensitivity circular, leaving two genes
    and measuring nothing about robustness. First run 2026-10-25 did exactly that and is kept as a recorded
    deviation in prediction_wnt_sign_20261025.md; this function is the corrected design.
    """
    genes: set[str] = set()
    with MARKERS.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if row["module"] == "wnt_pathway":
                continue
            genes.update(g.strip() for g in row["genes"].split(","))
    return genes


def statistic(gene_set: list[str], sig: dict[str, float]) -> tuple[int, float]:
    """(members that are significant AND up, mean signed log2FC counting non-significant as 0)."""
    up = sum(1 for g in gene_set if sig.get(g, 0.0) > 0)
    mean = statistics.fmean(sig.get(g, 0.0) for g in gene_set)
    return up, mean


def permutation(observed: list[str], universe: list[str], sig: dict[str, float],
                draws: int, seed: int) -> dict:
    rng = random.Random(seed)
    k = len(observed)
    obs_up, obs_mean = statistic(observed, sig)
    ge_up = ge_mean = 0
    for _ in range(draws):
        sample = rng.sample(universe, k)
        up, mean = statistic(sample, sig)
        ge_up += up >= obs_up
        ge_mean += mean >= obs_mean
    return {"set_size": k, "observed_up": obs_up, "observed_mean_log2fc": round(obs_mean, 4),
            "p_up_count": (ge_up + 1) / (draws + 1), "p_mean": (ge_mean + 1) / (draws + 1),
            "draws": draws, "seed": seed}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--draws", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20261025)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    universe = expressed_universe()
    sig = signed_table()
    removed = marker_genes()
    universe_nocomp = [g for g in universe if g not in removed]

    report = {
        "universe_expressed": len(universe),
        "universe_without_composition_markers": len(universe_nocomp),
        "significant_listed": len(sig),
        "sets": {},
    }
    for name, genes in (("W7", W7), ("W_READOUT", W_READOUT)):
        present = [g for g in genes if g in set(universe)]
        report["sets"][name] = {
            "members": genes,
            "in_expressed_universe": len(present),
            "full": permutation(present, universe, sig, args.draws, args.seed),
        }
        stripped = [g for g in present if g not in removed]
        report["sets"][name]["composition_removed"] = (
            permutation(stripped, universe_nocomp, sig, args.draws, args.seed)
            | {"members_after_removal": stripped})
    if args.json:
        print(json.dumps(report, indent=1))
    else:
        print(f"expressed universe {report['universe_expressed']}  "
              f"(without composition markers {report['universe_without_composition_markers']}); "
              f"padj<=0.05 listed {report['significant_listed']}")
        for name, block in report["sets"].items():
            for variant in ("full", "composition_removed"):
                r = block[variant]
                print(f"{name:10s} {variant:20s} n={r['set_size']} up={r['observed_up']} "
                      f"meanLFC={r['observed_mean_log2fc']:+.3f}  p(up count)={r['p_up_count']:.4f}  "
                      f"p(mean)={r['p_mean']:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
