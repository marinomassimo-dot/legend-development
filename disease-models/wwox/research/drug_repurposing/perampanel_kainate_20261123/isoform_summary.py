"""Summarize classifiable TPM fractions and conservative missing-assignment bounds."""
import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean

out=Path(__file__).parent/"results"
models=defaultdict(lambda:defaultdict(list))
with (out/"isoforms.tsv").open() as f:
    for row in csv.DictReader(f,delimiter="\t"):
        models[row["model"]][row["arm"]].append(row)
with (out/"isoform_summary.tsv").open("w") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["model","ctrl_fraction","KO_fraction","delta","LOO_min","LOO_max",
                "all_TPM_min","all_TPM_max","all_TPM_and_LOO_min","all_TPM_and_LOO_max"])
    for model,arms in models.items():
        wt,ko=arms["control"],arms["KO"]
        def avg(rows,key): return mean(float(r[key]) for r in rows)
        def contrasts(a,b):
            q="fraction_among_classified"
            return (avg(b,q)-avg(a,q),avg(b,"lower_all")-avg(a,"upper_all"),
                    avg(b,"upper_all")-avg(a,"lower_all"))
        full,lower,upper=contrasts(wt,ko)
        omissions=[contrasts(wt[:i]+wt[i+1:],ko) for i in range(len(wt))]
        omissions += [contrasts(wt,ko[:i]+ko[i+1:]) for i in range(len(ko))]
        w.writerow([model,avg(wt,"fraction_among_classified"),avg(ko,"fraction_among_classified"),
                    full,min(x[0] for x in omissions),max(x[0] for x in omissions),lower,upper,
                    min(x[1] for x in omissions),max(x[2] for x in omissions)])
