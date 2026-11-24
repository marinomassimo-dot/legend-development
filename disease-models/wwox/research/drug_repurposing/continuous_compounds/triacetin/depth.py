"""Standardize two library arms to shared capture-depth distributions by cell class."""
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "ganaxolone_20261123"))
from analyze import assigned_nuclei, tsv

TARGETS = {"exc": ["Nat8l"], "MFOL": ["Aspa", "Acss2", "Mbp"], "MOL": ["Aspa", "Acss2", "Mbp"]}


def run(files, output):
    genes = sorted({gene for entries in TARGETS.values() for gene in entries})
    pools = {(cell, arm): (depth, counts)
             for arm, cell, depth, counts in assigned_nuclei(files, [], [], genes) if cell in TARGETS}
    rows = []
    for cell, targets in TARGETS.items():
        for resolution in (1, 2, 4):
            bins = {arm: np.floor(resolution*np.log2(pools[cell, arm][0])).astype(int)
                    for arm in ("ctrl", "ko")}
            common = sorted(set(bins["ctrl"]) & set(bins["ko"]))
            for gene in targets:
                detected = {"ctrl": 0.0, "ko": 0.0}
                total = 0
                for group in common:
                    masks = {arm: values == group for arm, values in bins.items()}
                    weight = min(np.count_nonzero(mask) for mask in masks.values())
                    total += weight
                    for arm, mask in masks.items():
                        observed = pools[cell, arm][1][gene][mask]
                        detected[arm] += weight*np.mean(observed > 0)
                rows.append([cell, gene, resolution, total, detected["ctrl"]/total, detected["ko"]/total])
    tsv(output, "class gene bins_per_doubling common_weight ctrl_detection ko_detection".split(), rows)


if __name__ == "__main__":
    run(Path(sys.argv[1]), Path(sys.argv[2]))
