"""Sex-balanced adult P47T hippocampal gene and (when complete) junction contrasts."""
import argparse
import csv
from collections import defaultdict
import gzip
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


def junction_effects(path,out):
    source=read(out/"p47t_sources.tsv")
    files={p.stem:p for p in path.glob("SRR*.tsv")}
    assert set(files)=={r["run"] for r in source}, "A complete 20-lane series is required."
    animals=defaultdict(lambda:np.zeros(4,dtype=np.int64))
    probe_sha=hashlib.sha256((out/"junction_probes.tsv").read_bytes()).hexdigest()
    for r in source:
        rows=read(files[r["run"]])
        assert len(rows)==4 and {(x["rule"],x["Q"]) for x in rows}=={
            (rule,q) for rule in ("any","centered") for q in ("20","30")}
        for x in rows:
            assert x["animal"]==r["animal"] and x["compressed_md5"]==r["md5"]
            assert x["arm"]==r["arm"] and x["sex"]==r["sex"] and x["probe_sha256"]==probe_sha
            assert x["bytes"]==r["bytes"] and x["reads"]==r["fragments"]
            key=(x["rule"],x["Q"],r["animal"],r["arm"],r["sex"])
            animals[key]+=np.array([int(x[s]) for s in ("insert","skip","conflict","reads")])
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
            res.append([rule,q,min(denominators),*totals,passed,*contrast(fracs,groups)])
    tsv(out/"p47t_contrasts.tsv",
        "rule Q least_reads_in_one_animal WT_reads KO_reads coverage_pass sex_balanced_delta female_delta male_delta omit_min omit_max".split(),res)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("counts",type=Path)
    p.add_argument("--junctions",type=Path)
    a=p.parse_args()
    gene_effects(a.counts,ROOT/"results")
    if a.junctions: junction_effects(a.junctions,ROOT/"results")
