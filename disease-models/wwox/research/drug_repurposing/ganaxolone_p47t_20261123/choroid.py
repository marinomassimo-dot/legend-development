"""Measure sensitivity of the primary hippocampal contrast to choroid markers."""
import argparse
import csv
from pathlib import Path

import numpy as np

from analyze import metadata, p47t, write


def fit(X,y):
    if np.linalg.matrix_rank(X) < X.shape[1]:
        raise ValueError("Non-identifiable genotype contrast")
    return np.linalg.lstsq(X,y,rcond=None)[0]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("files","signature","out"):
        parser.add_argument(name,type=Path)
    args=parser.parse_args()
    source=args.files/"deepening_downloads/gse215425"
    counts,=source.glob("*processed_data*")
    series,=source.glob("*series_matrix*")
    samples,expression=p47t(counts)
    meta=metadata(series,samples)
    with args.signature.open() as f:
        dirs={r["gene"]:r["direction"] for r in csv.DictReader(f,delimiter="\t")}
    keep=[i for i,v in enumerate(meta) if v[0]=="HPC"]
    sex=np.array([0.5 if meta[i][2]=="F" else -0.5 for i in keep])
    genotype=np.array([int(meta[i][1]=="P47T/P47T") for i in keep])
    basic=np.column_stack([np.ones(len(keep)),genotype,sex,sex*genotype])
    markers=[g for g in ("Aqp1","Prlr","Kcne2","Folr1") if g not in dirs]
    z=np.mean([expression[g][keep] for g in markers],axis=0)
    design=np.column_stack([basic,z-z.mean()])
    def residual(v):
        return v-basic@fit(basic,v)
    zr=residual(z)
    def within_group_corr(v):
        return float(np.corrcoef(zr,residual(v))[0,1])
    results=[]
    for name,omit in [("full",[]),("without_Ttr",["Ttr"]),("without_Ttr_Col3a1",["Ttr","Col3a1"])]:
        arms=[[expression[g][keep] for g,d in dirs.items() if d==a and g not in omit] for a in ("up","down")]
        score=np.mean(arms[0],axis=0)-np.mean(arms[1],axis=0)
        for label,X in [("base",basic),("with_choroid",design)]:
            loo=[]
            for j in range(len(keep)):
                included=np.arange(len(keep))!=j
                if np.linalg.matrix_rank(X[included])==X.shape[1]:
                    loo.append(fit(X[included],score[included])[1])
            coef=fit(X,score)
            results.append([name,label,coef[1],min(loo),max(loo),len(loo),len(score)-len(coef),within_group_corr(score)])
    write(args.out/"choroid.tsv","score model equal_sex_effect loo_min loo_max estimable_loo residual_df within_cell_corr_with_marker",results)
    write(args.out/"choroid_markers.tsv","marker equal_sex_effect within_cell_corr_with_index",
          [(g,fit(basic,expression[g][keep])[1],within_group_corr(expression[g][keep])) for g in [*markers,"Ttr","Col3a1"]])
    write(args.out/"choroid_libraries.tsv","sample marker_index Ttr Col3a1 "+" ".join(markers),
          [[samples[i],z[j], expression["Ttr"][i],expression["Col3a1"][i],*[expression[g][i] for g in markers]] for j,i in enumerate(keep)])


if __name__=="__main__":
    main()
