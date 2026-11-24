"""Aggregate hippocampal GABA receptor subunit UMIs in the two GSE158684 pools."""
import csv
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parents[1] / "ganaxolone_20261123"))
from analyze import assigned_nuclei

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("pool", "class", "nuclei", "total_UMI", "Gabra3_UMI", "Gabra1_UMI",
                 "Gabra3_CPM", "Gabra1_CPM", "Gabra3_over_Gabra1", "both_positive_nuclei"))
for arm, cell, depth, counts in assigned_nuclei(Path(sys.argv[1]), [], [], ["Gabra3", "Gabra1"]):
    if cell not in ("exc", "inh"):
        continue
    a3, a1 = counts["Gabra3"], counts["Gabra1"]
    writer.writerow((arm, cell, len(depth), int(depth.sum()), int(a3.sum()), int(a1.sum()),
                     f"{1e6*a3.sum()/depth.sum():.3f}", f"{1e6*a1.sum()/depth.sum():.3f}",
                     f"{a3.sum()/a1.sum():.4f}" if a1.sum() else "NA",
                     int(((a3 > 0) & (a1 > 0)).sum())))
