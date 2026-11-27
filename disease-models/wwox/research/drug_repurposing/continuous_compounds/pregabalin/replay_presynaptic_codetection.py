"""Compare WWOX presynaptic channel co-detection with shared sequencing depth weights."""

import argparse
from pathlib import Path
import sys

import numpy as np

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(COMPOUNDS / "creatine"), str(COMPOUNDS / "jbpos0101")]
from assess import assigned_nuclei, tsv
from replay_exposure_and_receptors import verified_expression

GENES = ("Cacna2d1", "Cacna2d2", "Cacna1a", "Cacna1b")
SETS = tuple((gene,) for gene in GENES) + tuple(
    (auxiliary, pore) for auxiliary in GENES[:2] for pore in GENES[2:]
)
DEPTH_BOUNDS = (500, 2000, 5000, 10000, np.inf)
ARM_NAMES = ("ctrl", "ko")


def detection_rows(files):
    pools = {(arm, cell): (depth, counts)
             for arm, cell, depth, counts in assigned_nuclei(files, [], [], GENES)
             if cell in ("exc", "inh")}
    for cell in ("exc", "inh"):
        data = {arm: pools[arm, cell] for arm in ARM_NAMES}
        bins = {arm: [((depth >= lo) & (depth < hi)) for lo, hi in zip(DEPTH_BOUNDS, DEPTH_BOUNDS[1:])]
                for arm, (depth, _) in data.items()}
        n = {arm: np.array([int(mask.sum()) for mask in masks]) for arm, masks in bins.items()}
        common = (n["ctrl"] >= 10) & (n["ko"] >= 10)
        if not common.any():
            raise ValueError(f"No shared sequencing-depth bin for {cell}")
        pooled_counts = n["ctrl"] + n["ko"]
        weights = pooled_counts[common] / pooled_counts[common].sum()
        for arm, (depth, counts) in data.items():
            for genes in SETS:
                positive = np.logical_and.reduce([counts[gene] > 0 for gene in genes])
                name = "+".join(genes)
                successes = np.array([int((positive & mask).sum()) for mask in bins[arm]])
                rates = successes[common] / n[arm][common]
                yield cell, arm, name, "all", len(depth), int(positive.sum()), f"{100 * positive.mean():.5f}"
                yield (
                    cell, arm, name, "shared-depth standardized", int(n[arm][common].sum()),
                    int(successes[common].sum()), f"{100 * np.dot(weights, rates):.5f}",
                )
                for j, (lo, hi) in enumerate(zip(DEPTH_BOUNDS, DEPTH_BOUNDS[1:])):
                    label = f"{lo}–<{hi}" if np.isfinite(hi) else f"{lo}+"
                    pct = f"{100 * successes[j] / n[arm][j]:.5f}" if n[arm][j] else ""
                    yield cell, arm, name, label, n[arm][j], successes[j], pct


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=Path(__file__).with_name("presynaptic_codetection.tsv"))
    args = parser.parse_args()
    verified_expression(args.files)
    tsv(args.out, ("assigned_class", "pool", "detection_set", "depth_comparison",
                   "nuclei", "positive_nuclei", "positive_pct"), detection_rows(args.files))


if __name__ == "__main__":
    main()
