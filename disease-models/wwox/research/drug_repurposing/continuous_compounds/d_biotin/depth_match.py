"""Compare nuclear RNA at the same distribution of sequencing-depth strata."""
from pathlib import Path
import csv
import sys
import numpy as np

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent.parent / 'ganaxolone_20261123'))
from analyze import assigned_nuclei

files = Path(sys.argv[1])
markers = ["Acaca", "Pcx", "Hlcs"]
bins = [500, 1000, 2000, 4000, 8000, np.inf]
stages = ["astro", "OPC", "COP", "NFOL", "MFOL", "MOL"]
data = {(arm, cell): (depth, counts)
        for arm, cell, depth, counts in assigned_nuclei(files, [], [], markers) if cell in stages}
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("class", "gene", "included_strata", "ctrl_n", "ko_n", "ctrl_total_n", "ko_total_n",
                 "ctrl_standardized_CPM", "ko_standardized_CPM", "delta_CPM"))
for stage in stages:
    for marker in markers:
        weights, rates = [], []
        support = np.array([0, 0])
        for low, high in zip(bins, bins[1:]):
            sizes, means = [], []
            for arm in ("ctrl", "ko"):
                depth, counts = data[arm, stage]
                keep = (depth >= low) & (depth < high)
                sizes.append(int(keep.sum()))
                means.append(1e6*counts[marker][keep].sum()/depth[keep].sum() if keep.any() else np.nan)
            if min(sizes) >= 3:
                support += sizes
                weights.append(min(sizes))
                rates.append(means)
        if not weights:
            raise ValueError(f"No supported sequencing-depth stratum for {stage}")
        ctrl, ko = np.average(rates, axis=0, weights=weights)
        writer.writerow((stage, marker, len(weights), *support, len(data["ctrl",stage][0]),
                         len(data["ko",stage][0]), round(ctrl,4), round(ko,4), round(ko-ctrl,4)))
