#!/usr/bin/env python3
"""Descriptive per-gene rows for the targets and edge genes of group E in the two WWOX-deficient human neural datasets already held locally.
  target_gene_rows_p4c_e.py --help
  target_gene_rows_p4c_e.py run GEO_DIR     GEO_DIR holds GSE156243 and GSE126075 (the repository's files/geo)
GSE156243: organoid counts (4 KO, 2 WT), library-size scaling for display only (the existing gse156243/gene_rows_cpm.py is called);
GSE126075: CAGE TPM table, one library per arm; a gene missing from the table is ABSENT (not detected or not listed), never zero.
No normalisation model, no differential test."""
import csv, gzip, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
GENES = "WWOX HIF1A EPAS1 ARNT BNIP3 HK2 SLC2A1 LDHA LDHB PDK1 EGLN1 EGLN2 EGLN3 FOXO3 FOXO6 FOXO1 CSNK1A1 CSNK1D CSNK1E DYRK1A TGFBR1 PIN1 MYC MYCN METTL3 METTL14 USP13 NOTCH1 NOTCH2 NOTCH3 PSEN1 PSEN2 APH1A APH1B NCSTN PSENEN RBPJ HES1 XIAP THRA THRB SOX2 NES VIM".split()
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); sys.exit(0)
geo = Path(sys.argv[2])
subprocess.run([sys.executable, str(HERE.parent / "gse156243" / "gene_rows_cpm.py"), str(geo / "GSE156243" / "GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"), str(HERE / "organoid_target_gene_rows.tsv")] + GENES, check=True)
rows = {}
with gzip.open(geo / "GSE126075" / "GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz", "rt") as f:
    r = csv.reader(f, delimiter="\t"); h = next(r)
    for x in r:
        if x[0] in GENES:
            rows[x[0]] = x[1:]
with open(HERE / "hnpc_target_gene_rows.tsv", "w", newline="") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n"); w.writerow(["gene"] + h[1:])
    for g in GENES:
        w.writerow([g] + ([f"{float(a):.2f}" for a in rows[g]] if g in rows else ["ABSENT"] * (len(h) - 1)))
