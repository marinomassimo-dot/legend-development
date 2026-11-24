"""Look up archived mouse Kars transcript TPM individually (no isoform localization assignment)."""
import argparse
import csv
import gzip
from pathlib import Path
from statistics import mean
import sys
import re
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("worktree", type=Path)
parser.add_argument("files", type=Path)
args = parser.parse_args()
sys.path.insert(0,str(args.worktree / "disease-models/wwox/research/drug_repurposing/ganaxolone_20261123"))
from analyze import reference
mapping, _ = reference(args.files)
biotype = {}
with gzip.open(next((args.files/"reference_ensembl_r92").glob("*.fa.gz")), "rt") as source:
    for line in source:
        if line.startswith(">") and " gene_symbol:Kars " in line:
            biotype[line.split()[0][1:]] = re.search(r"transcript_biotype:(\S+)", line)[1]
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("dataset","transcript","archived_biotype","wt_n","ko_n","wt_mean_TPM","KO_mean_TPM","KO_minus_WT_TPM"))
for acc, wt, ko in (("GSE158682","CRTX_S_Ctrl_","CRTX_S_KO_"),("GSE158681","S_Ctrl_","S_KO_")):
    with gzip.open(next((args.files/"geo"/acc).glob("*TPM_Table.txt.gz")),"rt") as f:
        rows = csv.reader(f,delimiter="\t")
        labels = next(rows)[3:]
        for row in rows:
            tid = row[0].split(".")[0]
            if mapping.get(tid) != "Kars": continue
            ctrl = [float(v) for name,v in zip(labels,row[3:]) if name.startswith(wt)]
            knockout = [float(v) for name,v in zip(labels,row[3:]) if name.startswith(ko)]
            out.writerow((acc,row[0],biotype.get(row[0],"version_unmatched"),len(ctrl),len(knockout),f"{mean(ctrl):.3f}",
                          f"{mean(knockout):.3f}",f"{mean(knockout)-mean(ctrl):.3f}"))
