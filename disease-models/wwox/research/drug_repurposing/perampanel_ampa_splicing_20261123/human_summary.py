"""Summarize verified alternative splice-junction counts by biological library."""
import argparse
import csv
from itertools import combinations
from math import sqrt
from pathlib import Path
import numpy as np
from analyze import write


def wilson(f,n):
    if n==0:return ("NA","NA")
    proportion=f/n
    z=1.96
    mid=proportion+z*z/(2*n)
    radius=z*sqrt(proportion*(1-proportion)/n+z*z/(4*n*n))
    denom=1+z*z/n
    return (mid-radius)/denom,(mid+radius)/denom


def main(runpath,public,out):
    expected={r["run_accession"]:r for r in csv.DictReader(public.open(),delimiter="\t")}
    assert len(expected)==6
    runs={}
    qc,library,scores=[],[],[]
    for name,r in sorted(expected.items()):
        with (runpath/(name+".tsv")).open() as f:
            items=list(csv.DictReader(f,delimiter="\t"))
        assert len(items)==4
        for z in items:
            assert z["run"]==name and z["sample"]==r["sample_title"]
            assert z["compressed_md5"]==r["fastq_md5"] and z["bytes"]==r["fastq_bytes"]
            assert z["reads"]==r["read_count"]
            key=(z["rule"],int(z["Q"]))
            f,nof,c=[int(z[k]) for k in ("flip","flop","conflict")]
            group="KO" if "KO/WWOX" in z["sample"] else "WT"
            if group=="WT": assert "untreated" in z["sample"]
            runs.setdefault(key,[]).append((name,group,f,nof,c))
            library.append([name,group,*key,f,nof,c,f/(f+nof) if f+nof else "NA",*wilson(f,f+nof)])
        qc.append([name,r["read_count"],r["fastq_bytes"],r["fastq_md5"],items[0]["probe_sha256"]])
    for key,rows in sorted(runs.items()):
        wt=[i for i,t in enumerate(rows) if t[1]=="WT"]
        ko=[i for i,t in enumerate(rows) if t[1]=="KO"]
        assert len(wt)==2 and len(ko)==4
        counts=[f+b for _,_,f,b,_ in rows]
        if min(counts)==0:
            scores.append([*key,min(counts),*["NA"]*7,"not_measured"])
            continue
        v=np.array([f/(f+b) for _,_,f,b,_ in rows])
        def effect(w,k):
            return v[k].mean()-v[w].mean()
        d=effect(wt,ko)
        loo=[effect([i for i in wt if i!=j],[i for i in ko if i!=j]) for j in wt+ko]
        perm=[effect(list(w),[i for i in range(len(rows)) if i not in w]) for w in combinations(range(len(rows)),2)]
        if min(counts)<20: decision="coverage_limited"
        elif any(t[4] for t in rows):decision="conflicting_class_present"
        elif d>=.05 and min(loo)>0: decision="flip_enriched"
        elif d<=-.05 and max(loo)<0: decision="flip_depleted"
        else: decision="no_stable_five_point_shift"
        scores.append([*key,min(counts),v[wt].mean(),v[ko].mean(),d,min(loo),max(loo),
                       sum(x>=d-1e-12 for x in perm),sum(x<=d+1e-12 for x in perm),decision])
    write(out/"human_run_qc.tsv","run FASTQ_reads compressed_bytes md5 probe_sha256",qc)
    write(out/"human_libraries.tsv","run genotype rule min_Q flip_reads flop_reads conflict share read_Wilson_low read_Wilson_high",library)
    write(out/"human_contrasts.tsv","rule min_Q minimum_count WT_mean KO_mean delta omit_min omit_max of_15_ge of_15_le decision",scores)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("runpath","manifest","out"):p.add_argument(key,type=Path)
    a=p.parse_args()
    main(a.runpath,a.manifest,a.out)
