"""Use the published myelin signature to check the scope of the anatomical sensitivity."""
import argparse
import csv
import importlib.util
from pathlib import Path

import numpy as np

from analyze import write


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("files","training","previous","out"):
        parser.add_argument(name,type=Path)
    args=parser.parse_args()
    spec=importlib.util.spec_from_file_location("myelin_source",args.previous/"analyze.py")
    source=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    with (args.previous/"results/signature.tsv").open() as f:
        panel={r["gene"]:r["direction"] for r in csv.DictReader(f,delimiter="\t")}
    markers=["Aqp1","Prlr","Kcne2","Folr1"]
    tx,sex=source.reference(args.files)
    available=set(panel)|set(markers)
    samples,expression=source.source_matrix(args.training,sex|set("Mbp Plp1 Mobp Mag Mog Cnp".split()))
    models=[(a,samples,expression,a+"_M_plus_",a+"_M_minus_",False) for a in ["E3","E4","WT"]]
    for series,case,ctrl in [("GSE158681","S_KO_","S_Ctrl_"),("GSE158682","CRTX_S_KO_","CRTX_S_Ctrl_")]:
        p,=(args.files/"geo"/series).glob("*TPM_Table.txt.gz")
        models.append((series,*source.load_target(p,available,tx),case,ctrl,True))
    p=args.files/"deepening_downloads/gse319769/counts_fixed.tsv.gz"
    models.append(("kainate_d14",*source.load_target(p,available),"iaka14_","iasl14_",True))
    rows=[]
    for name,samples,x,t,c,tissue in models:
        ti,ci=source.contrast_indices(samples,t,c)
        keep=ti+ci
        group=np.array([1]*len(ti)+[0]*len(ci))
        x={g:np.log2(1+v[keep]) for g,v in x.items() if g in available}
        base=np.column_stack([np.ones(len(keep)),group])
        for kind,omits in [("full",[]),("without_Ttr_Col3a1",["Ttr","Col3a1"])]:
            v,_=source.score(x,[g for g in panel if panel[g]=="up"],[g for g in panel if panel[g]=="down" and g not in omits])
            modifiers=[("base",base)]
            if tissue:
                assert all(g in x for g in markers)
                z=np.mean([x[g] for g in markers],axis=0)
                modifiers.append(("with_choroid",np.column_stack([base,z-z.mean()])))
            for model,X in modifiers:
                idx=np.arange(len(keep))
                def effect(i):
                    mask=idx!=i
                    if np.linalg.matrix_rank(X[mask])!=X.shape[1]:
                        return None
                    return np.linalg.lstsq(X[mask],v[mask],rcond=None)[0][1]
                ds=[]
                for j in idx:
                    d=effect(j)
                    if d is not None:
                        ds.append(d)
                rows.append([name,len(ti),len(ci),kind,model,effect(-1),min(ds),max(ds),len(ds)])
    write(args.out/"original_contexts.tsv","context cases controls panel model effect loo_min loo_max estimable_loo",rows)


if __name__=="__main__":
    main()
