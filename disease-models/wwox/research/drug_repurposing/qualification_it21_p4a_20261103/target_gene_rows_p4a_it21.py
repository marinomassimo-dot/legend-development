#!/usr/bin/env python3
"""Descriptive per-gene rows for the targets and edge genes of the six IT21 P4a proposals, in the two WWOX-deficient human neural datasets held locally.
  target_gene_rows_p4a_it21.py --help
  target_gene_rows_p4a_it21.py run GEO_DIR     GEO_DIR holds GSE156243 and GSE126075 (the shared checkout's files/geo; read only)
GSE156243: organoid counts (4 KO, 2 WT), library-size scaling for display only (the existing gse156243/gene_rows_cpm.py is called);
GSE126075: CAGE TPM table, one library per arm; a gene missing from the table is ABSENT (not detected or not listed), never zero.
No normalisation model, no differential test; a ratio of 4 against 2 libraries is a description, not a result."""
import csv, gzip, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
GENES = ("WWOX HDAC1 HDAC2 HDAC3 HDAC4 HDAC5 HDAC6 HDAC7 HDAC8 HDAC9 SLC2A1 HIF1A EPAS1 HK2 LDHA KDM4A KDM4B KDM4C KDM4D EGLN1 EGLN2 EGLN3 HIF1AN "
         "BTK TEC ITK BMX TXK STAT3 NPY EZH2 EZH1 EED SUZ12 IL6 TNF IL1B MAPK1 MAPK3 BCL3 BRD4 SIRT1 SIRT2 SIRT3 MYC GFAP AIF1 CX3CR1 SOX2 NES").split()
if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    sys.exit(0)
geo = Path(sys.argv[2])
subprocess.run([sys.executable, str(HERE.parent / "gse156243" / "gene_rows_cpm.py"), str(geo / "GSE156243" / "GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"),
                str(HERE / "organoid_target_gene_rows.tsv")] + GENES, check=True)
rows = {}
with gzip.open(geo / "GSE126075" / "GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz", "rt") as f:
    r = csv.reader(f, delimiter="\t")
    h = next(r)
    for x in r:
        if x[0] in GENES:
            rows[x[0]] = x[1:]
with open(HERE / "hnpc_target_gene_rows.tsv", "w", newline="") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow(["gene"] + h[1:])
    for g in GENES:
        w.writerow([g] + ([f"{float(a):.2f}" for a in rows[g]] if g in rows else ["ABSENT"] * (len(h) - 1)))
