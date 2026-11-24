"""Sensitivity of cationic transporter counts to endothelial marker eligibility in GSE158684."""
import argparse
import csv
import gzip
from pathlib import Path
import sys
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("geo_dir", type=Path)
args = parser.parse_args()
markers = ("Cldn5", "Pecam1", "Kdr", "Flt1", "Mfsd2a", "Slco1a4")
targets = ("Slc7a1", "Slc7a2", "Kars", "Kars1")
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("genotype","min_umi","min_vascular_markers","nuclei","total_UMI","gene","positive","counts","CPM"))
for genotype in ("ctrl", "ko"):
    prefix = f"GSE158684_{genotype}_filtered_"
    with gzip.open(args.geo_dir / (prefix + "features.tsv.gz"), "rt") as stream:
        genes = [r[1] for r in csv.reader(stream, delimiter="\t")]
    with gzip.open(args.geo_dir / (prefix + "matrix.mtx.gz"), "rt") as stream:
        n = int(next(line for line in stream if not line.startswith("%")).split()[1])
        matrix = np.fromstring(stream.read(), dtype=np.int64, sep=" ").reshape(-1,3)
    depth = np.bincount(matrix[:,1]-1, weights=matrix[:,2], minlength=n)
    counts = {}
    for g in markers + targets:
        ids = [i for i, symbol in enumerate(genes, 1) if symbol == g]
        if not ids: continue
        selected = matrix[np.isin(matrix[:,0], ids)]
        counts[g] = np.bincount(selected[:,1]-1, weights=selected[:,2], minlength=n)
    vascular = sum((counts[g] > 0).astype(int) for g in markers)
    for min_umi in (500, 1000):
        for cutoff in (1, 2, 3):
            selected = (depth >= min_umi) & (vascular >= cutoff)
            total = int(depth[selected].sum())
            for g in targets:
                if g not in counts: continue
                molecular = counts[g][selected]
                c = int(molecular.sum())
                writer.writerow((genotype, min_umi, cutoff, int(selected.sum()), total, g,
                                 int((molecular > 0).sum()), c, f"{c*1e6/total:.3f}" if total else "NA"))
