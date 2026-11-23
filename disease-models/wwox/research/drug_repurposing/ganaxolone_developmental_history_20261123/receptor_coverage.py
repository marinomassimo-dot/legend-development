"""Audit whether the six subunits in the direct pharmacology are detectable in bulk RNA."""
import argparse
from pathlib import Path
import numpy as np
from analyze import disease, reference, write

ASSEMBLIES = {"a1b2g2": ["GABRA1","GABRB2","GABRG2"],
              "a4b3d": ["GABRA4","GABRB3","GABRD"]}


def main(base,out):
    human=base/"GSE156243"
    counts,=human.glob("*count_table.txt.gz")
    hgnc,=human.glob("hgnc_complete_set*.json")
    genes,titles,cpm=disease(counts)
    symbols=sum(ASSEMBLIES.values(),[])
    ref=base/"GSE150123"
    y,lines,days=reference(ref/"GSE150123_RAW.tar",ref/"GSE150123_series_matrix.txt.gz",hgnc,symbols)
    ctrl=[i for i,t in enumerate(titles) if t.startswith("cwt")]
    ko=[i for i,t in enumerate(titles) if t.startswith("cko")]
    assert len(ctrl)==2 and len(ko)==4
    rows,covered,development=[],[],[]
    for name,panel in ASSEMBLIES.items():
        data=np.stack([cpm[genes.index(g)] for g in panel])
        for g,values in zip(panel,data,strict=True):
            z=np.log2(1+values)
            rows.append([name,g,np.mean(values[ctrl]),np.mean(values[ko]),np.mean(z[ko])-np.mean(z[ctrl])])
        for group,indices in [("WT",ctrl),("KO",ko)]:
            for threshold in (.1,1,5):
                covered.append([name,group,threshold,sum(np.all(data[:,indices]>=threshold,axis=0)),len(indices)])
        ri=[symbols.index(g) for g in panel]
        for (line,day) in sorted(set(zip(lines,days,strict=True))):
            mask=(lines==line)&(days==day)
            intensity=np.expm1(y[ri][:,mask]*np.log(2))
            development.append([name,line,day,sum(mask),int(np.all(np.isfinite(intensity))),
                                sum(np.all(intensity>=1,axis=0)),*np.median(intensity,axis=1)])
    write(out/"receptor_composition.tsv","assembly subunit WT_mean_CPM KO_mean_CPM KO_minus_WT_log2",rows)
    write(out/"receptor_detectability.tsv","assembly group threshold_CPM all_three_detected libraries",covered)
    write(out/"receptor_reference_ages.tsv","assembly line age_days libraries all_mapped n_libraries_all_ge1 median_alpha_CPM median_beta_CPM median_gamma_or_delta_CPM",development)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("geo",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.geo,a.out)
