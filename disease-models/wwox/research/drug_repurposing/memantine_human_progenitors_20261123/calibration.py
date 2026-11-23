"""Calibrate donor-split detection and within-clone cross-platform agreement."""
import argparse
import csv
import gzip
import math
from pathlib import Path

import numpy as np

from analyze import disease, load_plate, probe_map, study_labels, write


def ranks(x):
    _,inverse,counts=np.unique(x,return_inverse=True,return_counts=True)
    mid=np.cumsum(counts)-(counts+1)/2
    return mid[inverse]


def corr(a,b):
    return float(np.corrcoef(ranks(a),ranks(b))[0,1])


def main(a):
    labels=study_labels(a.workbook)
    _,pg=probe_map(a.platform,a.annotation,a.hgnc)
    _,org=disease(a.organoids)
    cohorts={}
    for drug,dose in [("TRICHOSTATIN A","0.13_uM"),("METHYLPARABEN","10_uM")]:
        donors={}
        for path in sorted(a.plates.glob("GSE*_series_matrix.txt.gz")):
            donors.update(load_plate(path,pg,org,labels,drug,dose))
        cohorts[drug]=donors
    donors=cohorts["TRICHOSTATIN A"]
    controls=sorted(d for d,v in donors.items() if v["group"]=="controls")
    result=[]
    for scheme,tr,ho in [("primary",controls[::2],controls[1::2]),("swapped",controls[1::2],controls[::2])]:
        def delta(d):
            v=donors[d]
            return v["treated"]-np.median(v["vehicles"],axis=1)
        data=np.stack([delta(d) for d in tr])
        median=np.median(data,axis=0)
        stable=math.ceil(2*len(tr)/3)
        ok=(np.median(np.stack([np.median(donors[d]["vehicles"],axis=1) for d in tr]),axis=0)>0)&(np.ptp(data,axis=0)>0)
        up=[i for i in np.argsort(-median,kind="stable") if ok[i] and median[i]>0 and (data[:,i]>0).sum()>=stable][:10]
        down=[i for i in np.argsort(median,kind="stable") if ok[i] and median[i]<0 and (data[:,i]<0).sum()>=stable][:10]
        assert len(up)==len(down)==10
        def score(v):
            return v[up].mean()-v[down].mean()
        hits=[delta(d)[up].mean() for d in ho]
        lows=[delta(d)[down].mean() for d in ho]
        observed=[score(delta(d)) for d in ho]
        null=[]
        for d in ho:
            v=donors[d]["vehicles"]
            null.extend(score(v[:,i]-np.median(np.delete(v,i,axis=1),axis=1)) for i in range(v.shape[1]))
        result.append([scheme,len(ho),sum(x>0 for x in observed),np.median(hits),np.median(lows),np.median(observed),np.quantile(null,.95)])
    write(a.out/"plate_positive_control.tsv","scheme n_heldout n_positive median_up median_down median_score vehicle_q95",result)

    # RNA-seq used additional clones. Require exact line and same-line vehicle in both assays.
    with gzip.open(a.seqmeta,"rt") as f:
        meta={}
        for r in csv.reader(f,delimiter="\t"):
            if not r:continue
            if r[0]=="!Sample_title": titles=r[1:]
            if r[0]=="!Sample_characteristics_ch1":
                meta[r[1].partition(": ")[0]]=[s.partition(": ")[2] for s in r[1:]]
            if r[0]=="!series_matrix_table_begin":break
    with gzip.open(a.seqcounts,"rt") as f:
        rd=csv.reader(f,delimiter="\t")
        seqnames=next(rd)
        assert set(seqnames)==set(titles)
        sums=np.zeros(len(seqnames))
        seq={}
        for r in rd:
            x=np.array(r[1:],float)
            sums+=x
            seq[r[0]]=seq.get(r[0],0)+x
    order=[titles.index(s) for s in seqnames]
    lines=np.array([meta["cell id"][i].replace(".","-") for i in order])
    treatment=np.array([meta["treatment"][i] for i in order])
    rows=[]
    for d,v in sorted(cohorts["METHYLPARABEN"].items()):
        sample=(lines==d)&(treatment=="MPB")
        ctrl=(lines==d)&(treatment=="DMSO")
        if not (sample.any() and ctrl.any()):continue
        pairs=[(i,s) for i,s in enumerate(v["symbols"]) if s in seq and (seq[s][ctrl]*1e6/sums[ctrl]).mean()>=1]
        lidx=[i for i,s in pairs]
        sy=np.stack([np.log2(1+seq[s]*1e6/sums) for i,s in pairs])
        st=sy[:,sample].mean(axis=1)
        sv=sy[:,ctrl].mean(axis=1)
        lt=v["treated"][lidx]
        lv=np.median(v["vehicles"][lidx],axis=1)
        rows.append([d,len(pairs),int(sample.sum()),int(ctrl.sum()),corr(lt,st),corr(lv,sv),corr(lt-lv,st-sv)])
    write(a.out/"cross_platform_control.tsv","exact_line landmark_genes RNA_drug RNA_vehicle rho_treated_expression rho_vehicle_expression rho_drug_change",rows)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("plates","workbook","platform","annotation","hgnc","organoids","seqmeta","seqcounts","out"):
        p.add_argument(k,type=Path)
    main(p.parse_args())
