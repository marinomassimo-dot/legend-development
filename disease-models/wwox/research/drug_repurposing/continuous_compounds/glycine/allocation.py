"""Sensitivity of the Grin1 exon 5 RNA contrast to the unclassified TPM denominator."""
import csv
import gzip
from pathlib import Path
from statistics import mean
import sys

here = Path(__file__).resolve().parent
files = Path(sys.argv[1])
with (here/"cassette_identity.tsv").open() as stream:
    labels = {row["transcript"]: row["supported_junction"] for row in csv.DictReader(stream, delimiter="\t")}
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("accession","control_prefix","KO_prefix","coding_delta_pp","delta_pp_if_all_unknown_skip",
                 "delta_pp_if_all_unknown_include","free_assignment_lower_pp","free_assignment_upper_pp",
                 "fixed_transcript_lower_pp","fixed_transcript_upper_pp",
                 "included_TPM_WT","included_TPM_KO","skipped_TPM_WT","skipped_TPM_KO"))
for acc, arms in [("GSE158681",[("S_Ctrl_","S_KO_"),("N_Ctrl_","N_KO_"),("WT_","KO_")]),
                  ("GSE158682",[("CRTX_S_Ctrl_","CRTX_S_KO_")])]:
    path, = (files/"geo"/acc).glob("*TPM_Table.txt.gz")
    with gzip.open(path,"rt") as source:
        rows = csv.reader(source, delimiter="\t")
        names = next(rows)[3:]
        counts = {c:[0.]*len(names) for c in set(labels.values())}
        unresolved = {}
        seen = set()
        for row in rows:
            if row[0] in labels:
                seen.add(row[0])
                if labels[row[0]] == "unknown":
                    unresolved[row[0]] = list(map(float,row[3:]))
                for i, val in enumerate(row[3:]):
                    counts[labels[row[0]]][i] += float(val)
        assert seen == labels.keys()
    inc, skip, unk = (counts[c] for c in ("included","skipped","unknown"))
    low = [a/(a+b+c) for a,b,c in zip(inc,skip,unk)]
    high = [(a+c)/(a+b+c) for a,b,c in zip(inc,skip,unk)]
    known = [a/(a+b) for a,b in zip(inc,skip)]
    for wt, ko in arms:
        def avg(values, prefix):
            return mean(v for v,n in zip(values,names) if n.startswith(prefix))
        def delta(case, ctrl):
            return 100*(avg(case,ko)-avg(ctrl,wt))
        total = [a+b+c for a,b,c in zip(inc,skip,unk)]
        coefficients = []
        for abundances in unresolved.values():
            weights = [x/t for x,t in zip(abundances,total)]
            coefficients.append(delta(weights, weights))
        minimum = delta(low,low) + sum(min(0,c) for c in coefficients)
        maximum = delta(low,low) + sum(max(0,c) for c in coefficients)
        vals = [delta(known,known),delta(low,low),delta(high,high),delta(low,high),delta(high,low),minimum,maximum,
                avg(inc,wt),avg(inc,ko),avg(skip,wt),avg(skip,ko)]
        writer.writerow([acc,wt,ko,*[f"{v:.3f}" for v in vals]])
