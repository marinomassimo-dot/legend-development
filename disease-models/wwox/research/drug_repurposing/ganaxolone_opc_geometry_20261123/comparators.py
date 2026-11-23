"""Challenge the fixed six-gene result with normal development and acquired injury."""
import argparse
from collections import defaultdict
import csv
import gzip
import re
from pathlib import Path
import numpy as np
from geometry import write
from lineage import FAST, COMPARATORS


def score(y):
    return np.mean([np.log2(1+y[g]) for g in FAST],axis=0)-np.mean([np.log2(1+y[g]) for g in COMPARATORS],axis=0)


def main(files,out):
    genes=set(FAST+COMPARATORS)
    tx=defaultdict(set)
    with gzip.open(next((files/"reference_ensembl_r92").glob("*.fa.gz")),"rt") as f:
        for line in f:
            if not line.startswith(">"):continue
            s=re.search(r" gene_symbol:(\S+)",line)
            if s and s[1] in genes:tx[s[1]].add(re.search(r" gene:(\w+)",line)[1])
    assert set(tx)==genes and all(len(v)==1 for v in tx.values())
    lookup={next(iter(v)):g for g,v in tx.items()}
    path=files/"geo/E-MTAB-6798_mouse_timecourse/Mouse.RPKM.txt"
    with path.open() as f:
        h=[t.strip('"') for t in next(f).split()]
        y={}
        for line in f:
            key,vals=line.split(" ",1)
            g=lookup.get(key.strip('"'))
            if g:
                assert g not in y
                y[g]=np.fromstring(vals,sep=" ")
                assert len(y[g])==len(h)
    s=score(y)
    stages={day:[i for i,n in enumerate(h) if n.startswith(f"Brain.P{day}.")] for day in (0,3,14,28,63)}
    rows=[]
    for day,idx in stages.items():
        rows.append([day,len(idx),s[idx].mean(),min(s[idx]),max(s[idx])])
    write(out/"development.tsv","day samples mean_score minimum maximum",rows)
    with gzip.open(files/"deepening_downloads/gse319769/counts_fixed.tsv.gz","rt") as f:
        rd=csv.reader(f,delimiter="\t");h=next(rd)[1:]
        totals=np.zeros(len(h));y={}
        for r in rd:
            x=np.array(r[1:],float);totals+=x
            if r[0] in genes:y[r[0]]=y.get(r[0],0)+x
    s=score({g:v*1e6/totals for g,v in y.items()})
    days=sorted({int(re.match(r"iaka(\d+)_",n)[1]) for n in h if re.match(r"iaka(\d+)_",n)})
    rows=[]
    for day in days:
        ko=[i for i,n in enumerate(h) if n.startswith(f"iaka{day}_")]
        wt=[i for i,n in enumerate(h) if n.startswith(f"iasl{day}_")]
        assert len(wt)>1 and len(ko)>1
        def delta(omit=None):
            return s[[i for i in ko if i!=omit]].mean()-s[[i for i in wt if i!=omit]].mean()
        loo=[delta(i) for i in ko+wt]
        rows.append([day,len(ko),len(wt),delta(),min(loo),max(loo)])
    write(out/"injury.tsv","day kainate_n saline_n delta omit_min omit_max",rows)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",type=Path);p.add_argument("out",type=Path)
    a=p.parse_args();main(a.files,a.out)
