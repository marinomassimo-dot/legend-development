"""Standardize astroglial RNA detection to equal capture-depth weights in two pooled libraries."""
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "ganaxolone_20261123"))
from analyze import assigned_nuclei, tsv


def run(files, output):
    genes = ["Phgdh", "Psat1", "Psph"]
    pools = {arm: (depth, counts) for arm, cell, depth, counts in assigned_nuclei(files, [], [], genes)
             if cell == "astro"}
    rows = []
    for resolution in [1, 2, 4]:
        bins = {arm: np.floor(np.log2(depth) * resolution).astype(int)
                for arm, (depth, _) in pools.items()}
        for gene in genes:
            detected = {arm: 0.0 for arm in pools}
            weights = 0
            for group in sorted(set(bins["ctrl"]) & set(bins["ko"])):
                selected = {arm: bins[arm] == group for arm in pools}
                weight = min(np.count_nonzero(idx) for idx in selected.values())
                weights += weight
                for arm, (_, counts) in pools.items():
                    detected[arm] += weight * np.mean(counts[gene][selected[arm]] > 0)
            rows.append([resolution, gene, weights, detected["ctrl"] / weights, detected["ko"] / weights])
    tsv(output, "bins_per_doubling gene common_weight ctrl_detection ko_detection".split(), rows)


if __name__ == "__main__":
    run(Path(sys.argv[1]), Path(sys.argv[2]))
