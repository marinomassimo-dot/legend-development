"""Challenge the exploratory GFRA1 increase with previously fitted regional mixtures."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
import numpy as np
from analyze import write

SYMBOLS=["GDNF","GFRA1","RET","GAD1","GAD2"]


def profile(path):
    with gzip.open(path,"rt") as source:
        header=next(csv.reader([next(source)]))
        assert all(header.count(s)==1 for s in SYMBOLS)
        idx=[header.index(s) for s in SYMBOLS]
        pooled=np.zeros(len(idx))
        total=0
        equal=np.zeros(len(idx))
        eligible=0
        bins={False:[],True:[]}
        for line in source:
            x=np.fromstring(line,sep=",",dtype=np.int64)
            assert x.size==len(header) and x.min()>=0
            library=x.sum()
            v=x[idx]
            pooled+=v
            total+=library
            if library>=500:
                eligible+=1
                equal+=v*1e6/library
                bins[bool(v[3]+v[4])].append(v[:3])
    return {"pooled":pooled*1e6/total,"equal_cell":equal/eligible},bins


def main(hcs,hss,disease,out):
    pal,pbins=profile(hcs)
    sub,sbins=profile(hss)
    with disease.open() as f:
        observed={r["gene"]:float(r["log2_delta"]) for r in csv.DictReader(f,delimiter="\t")
                  if r["model"]=="human_organoid"}
    rows=[]
    for method,w in [("pooled",.3),("equal_cell",.2)]:
        a,b=pal[method],sub[method]
        delta=np.log2(1+(1-w)*a+w*b)-np.log2(1+a)
        maximum=np.log2(1+b)-np.log2(1+a)
        for k,g in enumerate(SYMBOLS):
            rows.append([method,w,g,a[k],b[k],observed[g],delta[k],maximum[k]])
    write(out/"region.tsv","method fixed_subpallial_weight gene pallial_CPM subpallial_CPM observed_KO_delta fixed_mix_delta all_subpallial_delta",rows)
    cells=[]
    for region,bins in [("pallium",pbins),("subpallium",sbins)]:
        for positive,lst in bins.items():
            values=np.array(lst)
            for i,g in enumerate(SYMBOLS[:3]):
                cells.append([region,positive,g,len(lst),np.count_nonzero(values[:,i]),values[:,i].sum()])
    write(out/"region_detection.tsv","region GAD1_or_GAD2_detected gene n_cells n_gene_detected molecules",cells)
    write(out/"region_inputs.tsv","input sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in (hcs,hss)])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("hcs","hss","disease","out"):
        p.add_argument(key,type=Path)
    a=p.parse_args()
    main(a.hcs,a.hss,a.disease,a.out)
