"""Sex-balanced adult P47T hippocampal gene and (when complete) junction contrasts."""
import argparse
import csv
from collections import defaultdict
import gzip
from itertools import combinations, product
import hashlib
from pathlib import Path
from statistics import mean

import numpy as np
from kainate_transfer import tsv

ROOT=Path(__file__).parent
GENES=["Grik1","Grik2","Grik4","Grik5","Neto1","Neto2"]


def read(path):
    with path.open() as stream:
        return list(csv.DictReader(stream,delimiter="\t"))


def contrast(y,groups):
    by_sex=[]
    for sex in ("F","M"):
        mutant=[v for v,(g,s) in zip(y,groups) if s==sex and g=="P47T"]
        wt=[v for v,(g,s) in zip(y,groups) if s==sex and g=="WT"]
        by_sex.append(mean(mutant)-mean(wt))
    omissions=[]
    for i in range(len(y)):
        rem=[j for j in range(len(y)) if i!=j]
        delta=[]
        for sex in ("F","M"):
            delta.append(mean(y[j] for j in rem if groups[j]==("P47T",sex))-
                         mean(y[j] for j in rem if groups[j]==("WT",sex)))
        omissions.append(mean(delta))
    return [mean(by_sex),*by_sex,min(omissions),max(omissions)]


def read_sensitivity(block):
    """Bounds after reclassifying at most one observed fragment in each animal."""
    val=[]
    for direction in (-1,1):
        frac=[]
        groups=[]
        for _,_,_,group,sex,ins,skip,_,_ in block:
            n=ins+skip
            change=direction if group=="P47T" else -direction
            frac.append(min(n,max(0,ins+change))/n)
            groups.append((group,sex))
        val.append(contrast(frac,groups)[0])
    return val


def permutation(y,groups):
    """Enumerate all animal-label assignments preserving the numbers of each sex."""
    by_sex=[[i for i,(_,s) in enumerate(groups) if s==sex] for sex in ("F","M")]
    n_mut=[sum(groups[i][0]=="P47T" for i in indices) for indices in by_sex]
    observed=abs(contrast(y,groups)[0])
    count=greater=0
    for arms in product(*(combinations(ix,n) for ix,n in zip(by_sex,n_mut))):
        means=[]
        for ix,chosen in zip(by_sex,arms):
            means.append(mean(y[i] for i in chosen)-mean(y[i] for i in ix if i not in chosen))
        count+=1
        greater+=abs(mean(means))>=observed-1e-12
    return greater,count

def gene_effects(path,out):
    expected="d654f6bdd2a4ac5b3e24741f16962503a711575c72aa92a2c729a7a0cf04c18c"
    assert hashlib.sha256(path.read_bytes()).hexdigest()==expected
    with gzip.open(path,"rt") as source:
        reader=csv.reader(source,delimiter="\t")
        labels=next(reader)[2:]
        cols=[i for i,n in enumerate(labels) if n.startswith("HPC_")]
        names=[labels[i] for i in cols]
        denominator=np.zeros(len(cols))
        counts=defaultdict(lambda:np.zeros(len(cols)))
        for _,name,*v in reader:
            vals=np.array([int(v[i]) for i in cols])
            denominator+=vals
            if name in GENES: counts[name]+=vals
    groups=[(n.split("_")[1].split("/")[0],n.split("_")[2][0]) for n in names]
    assert len(set(names))==10
    scores={g:np.log2(1+v*1e6/denominator) for g,v in counts.items()}
    for partner,core in (("Grik5","Grik2"),("Neto1","Grik1"),("Grik4","Grik1")):
        scores[partner+"_minus_"+core]=scores[partner]-scores[core]
    markers=read(ROOT.parent/"ganaxolone_p47t_20261123/results/choroid_libraries.tsv")
    marker={r["sample"]:float(r["marker_index"]) for r in markers}
    sex=np.array([s=="F" for _,s in groups],float)
    ko=np.array([g=="P47T" for g,_ in groups],float)
    design=np.column_stack([np.ones(10),ko,sex,ko*sex,[marker[n] for n in names]])
    assert np.linalg.matrix_rank(design)==5
    rows=[]
    for g,v in scores.items():
        fit=np.linalg.lstsq(design,v,rcond=None)[0]
        rows.append([g,*contrast(v,groups),fit[1]+.5*fit[3]])
    tsv(out/"p47t_genes.tsv",
        "measure sex_balanced_delta female_delta male_delta omit_min omit_max choroid_adjusted".split(),rows)


def junction_effects(path,out,alternate=None):
    source=read(out/"p47t_sources.tsv")
    probe_sha=hashlib.sha256((out/"junction_probes.tsv").read_bytes()).hexdigest()
    animals=defaultdict(lambda:np.zeros(4,dtype=np.int64))
    receipts,crosschecks=[],[]
    for r in source:
        ena=path/(r["run"]+".tsv")
        ncbi=alternate/(r["run"]+".tsv") if alternate else None
        have_ncbi=ncbi is not None and ncbi.exists()
        if not ena.exists() and not have_ncbi:
            raise ValueError(f"{r['run']} is missing; a complete 20-lane series is required.")
        if ena.exists() and have_ncbi:
            from p47t_sra import verify_anchor
            verify_anchor(ena,ncbi)
            crosschecks.append([r["run"],r["animal"],r["fragments"]])
        using_ena=ena.exists()
        rows=read(ena if using_ena else ncbi)
        assert len(rows)==4 and {(x["rule"],x["Q"]) for x in rows}=={
            (rule,q) for rule in ("any","centered") for q in ("20","30")}
        for x in rows:
            assert x["animal"]==r["animal"] and x["arm"]==r["arm"] and x["sex"]==r["sex"]
            assert x["probe_sha256"]==probe_sha and x["reads"]==r["fragments"]
            if using_ena:
                assert x["compressed_md5"]==r["md5"] and x["bytes"]==r["bytes"]
            else:
                assert x["source"]=="NCBI_full_quality" and len(x["archive_sha256"])==64 and "-" in x["archive_etag"]
            key=(x["rule"],x["Q"],r["animal"],r["arm"],r["sex"])
            animals[key]+=np.array([int(x[s]) for s in ("insert","skip","conflict","reads")])
            receipts.append([r["run"],r["animal"],r["arm"],r["sex"],
                             "ENA" if using_ena else "NCBI",x["bytes"],x.get("compressed_md5",""),
                             x.get("archive_etag",""),x.get("archive_sha256",""),probe_sha,
                             x["rule"],x["Q"],x["reads"],x["insert"],x["skip"],x["conflict"]])
    tsv(out/"p47t_lane_receipts.tsv",
        "run animal arm sex archive bytes ENA_MD5 NCBI_ETag NCBI_SHA256 probe_SHA256 rule Q reads insert skip conflict".split(),
        receipts)
    tsv(out/"p47t_crossarchive.tsv",["run","animal","fragments_matched_all_four_strata"],crosschecks)
    data=[[rule,q,a,g,s,*vals] for (rule,q,a,g,s),vals in sorted(animals.items())]
    tsv(out/"p47t_animals.tsv","rule Q animal genotype sex insert skip conflict fragments".split(),data)
    res=[]
    for rule in ("centered","any"):
        for q in ("20","30"):
            block=[v for v in data if v[0]==rule and v[1]==q]
            denominators=[v[5]+v[6] for v in block]
            assert min(denominators)>0
            fracs=[v[5]/d for v,d in zip(block,denominators)]
            groups=[(v[3],v[4]) for v in block]
            totals=[sum(d for d,(g,s) in zip(denominators,groups) if g==arm) for arm in ("WT","P47T")]
            passed=min(denominators)>=12 and min(totals)>=75
            animal_means = [mean(f for f,(g,_) in zip(fracs,groups) if g==arm) for arm in ("WT","P47T")]
            res.append([rule,q,min(denominators),*totals,passed,*animal_means,
                        animal_means[1]-animal_means[0],*contrast(fracs,groups),
                        *read_sensitivity(block),*permutation(fracs,groups)])
    tsv(out/"p47t_contrasts.tsv",
        "rule Q least_reads_in_one_animal WT_reads P47T_reads coverage_pass unweighted_WT_mean unweighted_P47T_mean unweighted_delta sex_balanced_delta female_delta male_delta omit_min omit_max one_reclassification_min one_reclassification_max two_sided_permutations_at_least_as_extreme all_permutations".split(),res)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("counts",type=Path)
    p.add_argument("--junctions",type=Path)
    p.add_argument("--ncbi-counts",type=Path)
    a=p.parse_args()
    gene_effects(a.counts,ROOT/"results")
    if a.junctions: junction_effects(a.junctions,ROOT/"results",a.ncbi_counts)
