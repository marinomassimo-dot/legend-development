"""Rank the three-gene panel across Hadwen's displayed, PC-adjusted robust z scores.

Provide one tab-separated file per gene, named Axin2.tsv, Nkd1.tsv and Apcdd1.tsv.
Copy both positive and negative tables for that gene from the public application,
retaining all drugs. Values rounded to zero may be displayed in both tables.
"""
import argparse
import csv
from decimal import Decimal
from pathlib import Path
from statistics import mean

from analyze import write


def main(folder,out):
    cohort={}
    target="Ethosuximide (700 uM)"
    values=[]
    for gene in ("Axin2","Nkd1","Apcdd1"):
        by={}
        with (folder/(gene+".tsv")).open() as f:
            for row in csv.reader(f,delimiter="\t"):
                if not row or row[0]=="Drug":continue
                if len(row)!=3:raise ValueError(f"{gene}: expected drug, z score, author P-value")
                n,z,p=row
                pair=Decimal(z),p
                if n in by and by[n]!=pair:raise ValueError(f"Conflicting duplicate for {n} in {gene}")
                by[n]=pair
        assert target in by and len(by)==218
        values.append([gene,by[target][0],by[target][1]])
        cohort[gene]=by
    names=set.intersection(*(set(v) for v in cohort.values()))
    assert len(names)==218
    scores={n:mean(v[n][0] for v in cohort.values()) for n in names}
    observed=scores[target]
    write(out/"author_processing.tsv","gene displayed_robust_z author_adjusted_P",values)
    write(out/"author_rank.tsv","drug mean_displayed_z n_drugs higher equal_including_target lower",
          [[target,float(observed),len(scores),sum(v>observed for v in scores.values()),
            sum(v==observed for v in scores.values()),sum(v<observed for v in scores.values())]])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("folder",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.folder,a.out)
