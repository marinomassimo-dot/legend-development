"""Count three sterol transcripts per assigned hippocampal oligodendroglial stage."""
import csv
from pathlib import Path
import sys

repo, files = map(Path, sys.argv[1:3])
sys.path.insert(0,str(repo/"disease-models/wwox/research/drug_repurposing/ganaxolone_20261123"))
from analyze import assigned_nuclei

genes = ["Sqle", "Lss", "Dhcr24"]
stages = ("OPC", "COP", "NFOL", "MFOL", "MOL")
rows = {}
for arm, stage, depth, values in assigned_nuclei(files, [], [], genes):
    if stage in stages:
        for gene in genes:
            rows[arm, stage, gene] = (len(depth), int(depth.sum()), int(values[gene].sum()),
                                       int((values[gene] > 0).sum()))
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("gene","stage","control_nuclei","control_depth","control_gene_UMI","control_positive",
              "KO_nuclei","KO_depth","KO_gene_UMI","KO_positive","control_CPM","KO_CPM","delta_CPM"))
for gene in genes:
    for stage in stages:
        control, ko = [rows[arm,stage,gene] for arm in ("ctrl","ko")]
        c, k = [1e6*row[2]/row[1] for row in (control,ko)]
        out.writerow((gene,stage,*control,*ko,round(c,3),round(k,3),round(k-c,3)))
