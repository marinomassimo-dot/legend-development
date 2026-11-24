"""Aggregate hippocampal glycine transport and cleavage RNA by annotated nuclear class."""
from pathlib import Path
import csv
import sys

repo, files = map(Path,sys.argv[1:3])
sys.path.insert(0,str(repo/"disease-models/wwox/research/drug_repurposing/ganaxolone_20261123"))
from analyze import assigned_nuclei

genes = ["Slc6a9","Gldc","Amt"]
writer = csv.writer(sys.stdout,delimiter="\t",lineterminator="\n")
writer.writerow(("pool","class","nuclei","UMI","gene","gene_UMI","positive_nuclei","CPM"))
for arm, cell, depth, values in assigned_nuclei(files,[],[],genes):
    for gene in genes:
        n = int(values[gene].sum())
        writer.writerow((arm,cell,len(depth),int(depth.sum()),gene,n,
                         int((values[gene]>0).sum()),f"{n*1e6/depth.sum():.3f}"))
