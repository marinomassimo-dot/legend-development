"""Test a ligand-supply explanation in untreated WWOX brain and direct memantine data."""
import argparse
from collections import defaultdict
import csv
import gzip
import hashlib
from pathlib import Path
import re

import numpy as np


ASTRO = ["ALDH1L1","GLUL","SLC1A3"]
GENES = ["GDNF","GFRA1","RET","NCAM1","GAD1","GAD2","MAP2","SNAP25","BDNF","NTF3","NGF",*ASTRO]


def write(path,fields,rows):
    with path.open("w") as f:
        w=csv.writer(f,delimiter="\t",lineterminator="\n")
        w.writerow(fields.split())
        w.writerows(rows)


def counts(path,mouse=False):
    offset=8 if mouse else 1
    with gzip.open(path,"rt") as f:
        reader=csv.reader(f,delimiter="\t")
        samples=next(reader)[offset:]
        total=np.zeros(len(samples))
        records={}
        for row in reader:
            values=np.array(row[offset:],float)
            total+=values
            symbol=row[3 if mouse else 0].upper()
            if symbol in GENES:
                records[symbol]=records.get(symbol,0)+values
    return samples,records,{g:x*1e6/total for g,x in records.items()}


def drug(count_path,meta,out):
    ids,raw,cpm=counts(count_path,True)
    with gzip.open(meta,"rt") as stream:
        m={r[0]:r[1:] for r in csv.reader(stream,delimiter="\t") if r and r[0] in ("!Sample_title","!Sample_description")}
    labels=dict(zip(m["!Sample_description"],m["!Sample_title"],strict=True))
    ctrl=[i for i,t in enumerate(ids) if labels[t].startswith("Vehicle-")]
    all_drugs=[i for i in range(len(ids)) if i not in ctrl]
    treated,=[i for i,t in enumerate(ids) if labels[t].startswith("Memantine·HCl [")]
    block=[i for i in all_drugs if ids[i].split(".")[1]==ids[treated].split(".")[1]]
    assert len(ctrl)==9 and len(all_drugs)==218
    rows=[]
    for g,x in sorted(cpm.items()):
        rank=sum(x[i]>x[treated] for i in all_drugs)+1
        worst=sum(x[i]>=x[treated] for i in all_drugs)
        passes=np.median(x[ctrl])>=1 and x[treated]>max(x[ctrl]) and worst<=21
        rows.append([g,int(raw[g][treated]),int(min(raw[g][ctrl])),int(max(raw[g][ctrl])),x[treated],np.median(x[ctrl]),
                     min(x[ctrl]),max(x[ctrl]),np.log2(1+x[treated])-np.median(np.log2(1+x[ctrl])),
                     rank,worst,1+sum(x[i]>x[treated] for i in block),len(block),passes])
    write(out/"drug.tsv","gene drug_count vehicle_min_count vehicle_max_count drug_CPM vehicle_median_CPM vehicle_min_CPM vehicle_max_CPM log2_delta rank_high rank_low block_rank block_n pass",rows)


def atlas(path,out):
    with gzip.open(path,"rt") as stream:
        reader=csv.reader(stream)
        titles=next(reader)[1:]
        values={r[0].upper():np.array(r[1:],float) for r in reader if r[0].upper() in GENES}
    groups=defaultdict(list)
    for i,full in enumerate(titles):
        label=full.strip().lower()
        if label.startswith("mouse"): continue
        if label.startswith("fetal ctx"): group="fetal_astro"
        elif any(w in label for w in ("tumor","hippocampus","cultured","epilepsy")): continue
        elif "ctx" in label: group="postnatal_"+label.split()[-1]
        elif "whole cortex" in label:group="postnatal_bulk"
        else:continue
        groups[group].append(i)
    assert len(groups["fetal_astro"])==6 and len(groups["postnatal_astro"])==12
    write(out/"purified_reference.tsv","group gene n median_FPKM min_FPKM max_FPKM n_ge_1",
          [[grp,g,len(ix),np.median(x[ix]),min(x[ix]),max(x[ix]),sum(x[ix]>=1)]
           for grp,ix in sorted(groups.items()) for g,x in sorted(values.items())])


def transcripts(path):
    ids=defaultdict(set)
    mapping={}
    with gzip.open(path,"rt") as f:
        for line in f:
            if not line.startswith(">"):continue
            symbol=re.search(r" gene_symbol:(\S+)",line)
            if symbol and (g:=symbol[1].upper()) in GENES:
                gene_id=re.search(r" gene:(\w+)",line)[1]
                ids[g].add(gene_id)
                mapping[line[1:].split(".",1)[0]]=g
    if set(ids)!=set(GENES) or any(len(v)!=1 for v in ids.values()):
        raise ValueError(f"Ambiguous gene mappings: {ids}")
    return mapping


def mouse_values(path,mapping):
    with gzip.open(path,"rt") as f:
        reader=csv.reader(f,delimiter="\t")
        samples=next(reader)[3:]
        result={}
        for row in reader:
            g=mapping.get(row[0].split(".",1)[0])
            if g:
                result[g]=result.get(g,0)+np.array(row[3:],float)
    assert set(result)==set(GENES)
    return samples,result


def disease(groups,out):
    rows,summary=[],[]
    for name,samples,data,control,mutant in groups:
        wt=[i for i,s in enumerate(samples) if s.startswith(control)]
        ko=[i for i,s in enumerate(samples) if s.startswith(mutant)]
        assert min(len(wt),len(ko))>=2
        y={g:np.log2(1+x) for g,x in data.items()}
        markers=[g for g in ASTRO if data[g][wt].mean()>=1]
        if len(markers)>=2:
            y["GDNF_vs_astro"]=y["GDNF"]-np.mean([y[g] for g in markers],axis=0)
        stats={}
        for g,v in y.items():
            def effect(omit=None):
                return v[[i for i in ko if i!=omit]].mean()-v[[i for i in wt if i!=omit]].mean()
            d=effect()
            loo=[effect(i) for i in wt+ko]
            stats[g]=(d,min(loo),max(loo))
            rows.append([name,g,len(ko),len(wt),data[g][wt].mean() if g in data else "NA",
                         data[g][ko].mean() if g in data else "NA",d,min(loo),max(loo)])
        detected=data["GDNF"][wt].mean()>=1
        receiver=data["GFRA1"][ko].mean()>=1
        summary.append([name,detected,receiver,stats["GDNF"][2]<0,",".join(markers),
                        stats.get("GDNF_vs_astro",[0,0,np.nan])[2]<0,
                        detected and receiver and stats["GDNF"][2]<0])
    write(out/"disease.tsv","model gene KO_n WT_n WT_mean KO_mean log2_delta omit_min omit_max",rows)
    write(out/"disease_summary.tsv","model baseline_ligand_detected KO_receiver_detected ligand_lower_all_omissions reference_markers adjusted_ligand_lower_all_omissions supply_criterion",summary)


def main(a):
    out=a.out
    out.mkdir(exist_ok=True,parents=True)
    geo=a.files/"geo"
    org,=(geo/"GSE156243").glob("*count_table.txt.gz")
    astro,=(geo/"GSE73721").glob("*.csv.gz")
    hp,=(geo/"GSE158681").glob("*TPM_Table.txt.gz")
    cx,=(geo/"GSE158682").glob("*TPM_Table.txt.gz")
    fasta=a.files/"reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz"
    drug(a.counts,a.meta,out)
    atlas(astro,out)
    mapping=transcripts(fasta)
    hs,_,hx=counts(org)
    mhip=mouse_values(hp,mapping)
    mcx=mouse_values(cx,mapping)
    disease([("human_organoid",hs,hx,"cwt","cko"),("mouse_global_hippocampus",*mhip,"WT_","KO_"),
             ("mouse_neuronal_hippocampus",*mhip,"S_Ctrl_","S_KO_"),
             ("mouse_progenitor_hippocampus",*mhip,"N_Ctrl_","N_KO_"),
             ("mouse_neuronal_cortex",*mcx,"CRTX_S_Ctrl_","CRTX_S_KO_")],out)
    write(out/"inputs.tsv","input sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest())
          for p in (a.counts,a.meta,astro,org,hp,cx,fasta)])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("files","counts","meta","out"):
        p.add_argument(key,type=Path)
    main(p.parse_args())
