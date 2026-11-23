"""Model regional RNA mixtures in same-age, separately directed forebrain spheroids."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path

import numpy as np

from analyze import PANELS, write


def profiles(path, symbols):
    with gzip.open(path,"rt") as source:
        header=next(csv.reader([next(source)]))
        if any(header.count(s)!=1 for s in symbols):
            raise ValueError(f"{path}: ambiguous or missing target genes")
        ids=[header.index(s) for s in symbols]
        pooled=np.zeros(len(ids))
        equal=np.zeros(len(ids))
        n_cells=n_keep=total=0
        for line in source:
            x=np.fromstring(line,sep=",",dtype=np.int64)
            if x.size!=len(header) or x.min()<0:
                raise ValueError(f"Malformed cell {n_cells+1} in {path}")
            n=x.sum()
            pooled+=x[ids]
            total+=n
            n_cells+=1
            if n>=500:
                equal+=x[ids]*1e6/n
                n_keep+=1
        assert n_keep>0 and total>0
    return {"pooled":pooled*1e6/total,"equal_cell":equal/n_keep},(n_cells,n_keep,total)


def main(hcs,hss,disease,out):
    with disease.open() as f:
        rows=list(csv.DictReader(f,delimiter="\t"))
    symbols=sorted(r["symbol"] for r in rows if r["control_mean_CPM"]!="absent" and float(r["control_mean_CPM"])>=1)
    target=np.array([float(next(r["delta"] for r in rows if r["symbol"]==s)) for s in symbols])
    panels={p:[symbols.index(s) for s in gs if s in symbols] for p,gs in PANELS.items()}
    pal,pinfo=profiles(hcs,symbols)
    sub,sinfo=profiles(hss,symbols)
    output,details=[],[]
    for method in pal:
        a,b=pal[method],sub[method]
        grid=np.linspace(0,1,11)
        contrasts=np.log2(1+(1-grid[:,None])*a+grid[:,None]*b)-np.log2(1+a)
        mark=panels["interneuron"]
        errors=np.mean((contrasts[:,mark]-target[mark])**2,axis=1)
        best=int(np.argmin(errors))
        for i,k in enumerate(grid):
            v=contrasts[i]
            means=[v[ix].mean() for ix in panels.values()]
            output.append([method,k,i==best,errors[i],*means,v[symbols.index("GABRB3")]])
        for i,s in enumerate(symbols):
            details.append([method,s,target[i],a[i],b[i],contrasts[best,i],contrasts[best,i]-target[i]])
    write(out/"region_grid.tsv","method subpallial_RNA_weight best_fit marker_MSE receptor effector interneuron neuronal GABRB3",output)
    write(out/"region_genes.tsv","method symbol observed_WWOX_log2_delta pallium_CPM subpallium_CPM best_mix_log2_delta predicted_minus_observed",details)
    write(out/"region_sources.tsv","file sha256 cells cells_at_least_500 total_molecules",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest(),*info) for p,info in [(hcs,pinfo),(hss,sinfo)]])


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("hcs","hss","disease","out"):
        parser.add_argument(name,type=Path)
    a=parser.parse_args()
    main(a.hcs,a.hss,a.disease,a.out)
