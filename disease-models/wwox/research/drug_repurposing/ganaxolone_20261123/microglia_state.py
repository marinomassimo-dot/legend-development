"""Standardize two pooled microglia profiles to common developmental-state RNA fractions."""
import argparse
import csv
from pathlib import Path
import numpy as np
from analyze import assigned_nuclei,tsv


STATE="Spp1 Gpnmb Igf1 Clec7a Lpl Cd9 Cd63 Lgals3 Fabp5 Itgax Apoe Tyrobp".split()


def calculate(data,indices,threshold,depth_bins=False):
    ui,di,si=indices
    sizes=np.concatenate([x.sum(1) for x in data])
    cuts=np.quantile(sizes,[1/3,2/3])
    details=[]
    strata=[]
    totals=[]
    def signal(cpm):
        log=np.log2(1+cpm)
        return log[ui].mean(),log[di].mean()
    for arm,x in zip(["ctrl","ko"],data,strict=True):
        depth=x.sum(1)
        detected=(x[:,si]>0).sum(axis=1)
        group=(detected>=threshold).astype(int)
        if depth_bins:group+=2*np.digitize(depth,cuts)
        strata.append({})
        summed=x.sum(0)
        totals.append(signal(summed*1e6/summed.sum()))
        for label in sorted(set(group)):
            y=x[group==label].sum(0)
            count=int(sum(group==label))
            fraction=y.sum()/summed.sum()
            cps=y*1e6/y.sum()
            u,d=signal(cps)
            strata[-1][label]=(fraction,cps,count,int(y.sum()))
            details.append([arm,threshold,depth_bins,label%2,label//2,count,y.sum(),fraction,u,d])
    joint=sorted(set(strata[0])&set(strata[1]))
    support=all(set(s)==set(joint) for s in strata) and len(joint)==(6 if depth_bins else 2)
    occupied=[s[k] for s in strata for k in joint]
    enough=support and all(item[2]>=20 and item[3]>=8000 for item in occupied)
    common_weight=sum((strata[0][k][0]+strata[1][k][0])/2 for k in joint)
    norm=[]
    for s in strata:
        blended=sum((strata[0][k][0]+strata[1][k][0])/2*s[k][1] for k in joint)/common_weight
        norm.append(signal(blended))
    overall=np.asarray(totals[1])-totals[0]
    adjusted=np.asarray(norm[1])-norm[0]
    return (overall[0]-overall[1],adjusted[0]-adjusted[1],*overall,*adjusted,common_weight,
            min(a[2] for a in occupied),enough),details


def main(files,signature,out):
    with signature.open() as f:
        rows=list(csv.DictReader(f,delimiter="\t"))
    up,down=([r["gene"] for r in rows if r["direction"]==s] for s in ["up","down"])
    assert not (set(STATE)&set(up+down)) and not (set(STATE)&{"Cx3cr1","P2ry12","Csf1r"})
    profiles=[(arm,depth,genes) for arm,cell,depth,genes in assigned_nuclei(files,up,down,STATE) if cell=="microglia"]
    present=set.intersection(*(set(genes) for _,_,genes in profiles))
    groups=[[g for g in panel if g in present] for panel in (up,down,STATE)]
    names=sum(groups,[])
    assert len(set(names))==len(names)
    indices=[[names.index(g) for g in panel] for panel in groups]
    matrices=[]
    for arm,depth,genes in profiles:
        x=np.column_stack([genes[g] for g in names]).astype(np.int64)
        residual=depth.astype(np.int64)-x.sum(1)
        assert np.all(residual>=0)
        matrices.append(np.column_stack([x,residual]))
    assert [len(x) for x in matrices]==[167,171]
    summary,details=[],[]
    for t,bins in [(1,False),(2,False),(3,False),(2,True)]:
        result,dr=calculate(matrices,indices,t,bins)
        raw,adj,*_=result
        assert np.isclose(raw,3.0548497261630994-2.097773238449647)
        summary.append([t,bins,*result,adj/raw])
        details.extend(dr)
    # Post-primary audit: require a more distinctive developmental-state marker.
    restricted=[g for g in "Spp1 Gpnmb Igf1 Clec7a Lpl Lgals3 Itgax".split() if g in names]
    restricted_indices=[names.index(g) for g in restricted]
    specificity=[]
    for arm,x in zip(["ctrl","ko"],matrices,strict=True):
        n=(x[:,restricted_indices]>0).sum(axis=1)
        for floor in (1,2):
            subset=n>=floor
            specificity.append([arm,",".join(restricted),floor,int(subset.sum()),int(x[subset].sum())])
    tsv(out/"state_restricted_support.tsv","pool available_markers threshold nuclei UMIs".split(),specificity)
    genes=[]
    for g,panel in zip(names,["up"]*len(groups[0])+["down"]*len(groups[1])+["state"]*len(groups[2]),strict=True):
        j=names.index(g)
        genes.append([g,panel,*[int(x[:,j].sum()) for x in matrices]])
    rng=np.random.default_rng(20261123)
    thinning=[]
    for _ in range(100):
        sample=[np.stack([rng.multivariate_hypergeometric(row,500) for row in x]) for x in matrices]
        result,_=calculate(sample,indices,2)
        thinning.append([result[0],result[1],result[-1],result[-2]])
    tsv(out/"state_summary.tsv","n_markers with_depth_tertile raw_delta adjusted_delta raw_up raw_down adjusted_up adjusted_down common_RNA_weight smallest_cell_count all_strata_adequate fraction_retained".split(),summary)
    tsv(out/"state_strata.tsv","pool n_markers with_depth_tertile state_positive depth_tertile nuclei UMIs RNA_weight up_score down_score".split(),details)
    tsv(out/"state_gene_support.tsv","gene arm ctrl_UMIs KO_UMIs".split(),genes)
    tsv(out/"state_thinning.tsv","raw_delta adjusted_delta all_strata_adequate smallest_cell_count".split(),thinning)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("files","signature","out"):p.add_argument(key,type=Path)
    a=p.parse_args()
    main(a.files,a.signature,a.out)
