"""SCI 2026-11-19 (ADV-085): print the rows of the interneuron, GABAergic, myelin and maturation genes in Expanded View Tables EV1 and EV2 of Steinberg 2021 (derived text) and list the genes in neither table.  Run:  python3 -I ev_genes_sci_20261119.py"""
import sys
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
rows = [l.rstrip("\n").split("\t") for l in open("/home/desktop/legend-development/files/fulltext/PMID34268881_assets/Table_EV1_EV2_derived.txt", encoding="utf-8")]
want = {"PVALB", "SST", "VIP", "NPY", "CALB1", "CALB2", "GAD1", "GAD2", "SLC32A1", "SLC17A7", "SLC17A6", "GABRB2", "GABRB3", "GABRA1", "GABRG2", "KCNC1", "KCNC2", "KCNC3", "LHX6", "SOX6", "NKX2-1", "DLX1", "DLX2", "DLX5", "DLX6", "ERBB4",
        "ACAN", "BCAN", "HAPLN1", "SLC12A5", "SLC12A2", "MBP", "SOX10", "OLIG2", "PDGFRA", "RELN", "CNTNAP2"}
found = set()
for r in rows:
    if len(r) >= 7 and r[0] in ("EV1_up", "EV2_down") and r[2] in want:
        found.add(r[2])
        print(r[0], r[2], "padj", r[5], "log2FC", r[6], "| p", r[4])
print("not in either list:", sorted(want - found))
