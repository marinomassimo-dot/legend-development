#!/usr/bin/env python3
"""Descriptive CPM panel of the GSE156243 counts table (4 WWOX-knockout vs 2 wild-type libraries, week-15 cerebral organoids,
one laboratory) for the W2 therapeutic package (scientist-c, 2026-10-27). NO normalisation model, NO differential test:
counts per million for display only, plus the SLC12A2/SLC12A5 ratio per library. Composition-confounded by construction
(see ../gse156243/independent_reanalysis_wnt_vs_maturation_20261025.md). NOT WWOX-DEE EVIDENCE; transcripts are not function.
Usage: organoid_panel.py <counts.gz> <out.tsv>     (counts: files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz)"""
import csv
import gzip
import sys

GENES = ["WWOX", "SLC12A2", "SLC12A5", "GRIN1", "GRIN2A", "GRIN2B", "GRIN2C", "GRIN2D", "GRIA1", "GRIA2", "GRIA3", "GRIA4",
         "GABRB2", "GABRB3", "GAD1", "OLIG1", "OLIG2", "SOX10", "PDGFRA", "MBP", "PLP1", "CHRM1", "CHRM3", "HSPA1A", "HSPA8"]
if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0 if sys.argv[1:2] in (["-h"], ["--help"]) else 2)
rows = {}
with gzip.open(sys.argv[1], "rt") as f:
    r = csv.reader(f, delimiter="\t")
    head = next(r)
    for x in r:
        rows[x[0]] = [float(v) for v in x[1:]]
sums = [sum(v[i] for v in rows.values()) for i in range(6)]
cpm = {g: [rows[g][i] / sums[i] * 1e6 for i in range(6)] for g in GENES if g in rows}
with open(sys.argv[2], "w") as o:
    o.write("gene\t" + "\t".join(head[1:]) + "\traw_min_across_libraries\n")
    for g in GENES:
        if g not in cpm:
            o.write(g + "\tABSENT\n")
            continue
        o.write(g + "\t" + "\t".join(f"{v:.2f}" for v in cpm[g]) + f"\t{min(rows[g]):g}\n")
    a, b = cpm["SLC12A2"], cpm["SLC12A5"]
    o.write("SLC12A2_over_SLC12A5\t" + "\t".join(f"{a[i] / b[i]:.2f}" for i in range(6)) + "\t\n")
