"""Cross-check WNT activity after ethosuximide and regional fate in human organoids."""
import argparse
import csv
import gzip
import hashlib
from collections import Counter, defaultdict
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

import numpy as np


TARGETS = ["AXIN2","LEF1","NKD1","APCDD1"]
CLUSTERS = ["Telencephalic Progenitors","Diencephalic Progenitors","Hindbrain Progenitors",
            "Spinal Cord Progenitors","CNS Neurons"]


def write(path, fields, records):
    with path.open("w") as f:
        writer=csv.writer(f,delimiter="\t",lineterminator="\n")
        writer.writerow(fields.split())
        writer.writerows(records)


def sheet(path):
    with zipfile.ZipFile(path) as book:
        strings=["".join(s.itertext()) for s in ET.fromstring(book.read("xl/sharedStrings.xml"))]
        root=ET.fromstring(book.read("xl/worksheets/sheet1.xml"))
        rows=[]
        for row in root.findall(".//{*}row"):
            values={}
            for c in row.findall("{*}c"):
                col=re.match("[A-Z]+",c.attrib["r"])[0]
                v=c.findtext("{*}v","")
                values[col]=strings[int(v)] if c.attrib.get("t")=="s" else v
            rows.append(values)
    keys=rows[0]
    return [{name:r.get(k,"") for k,name in keys.items()} for r in rows[1:]]


def drug(counts,matrix,out):
    with gzip.open(matrix,"rt") as f:
        meta={r[0]:r[1:] for r in csv.reader(f,delimiter="\t")
              if r and r[0] in ("!Sample_title","!Sample_description")}
    labels=dict(zip(meta["!Sample_description"],meta["!Sample_title"],strict=True))
    with gzip.open(counts,"rt") as f:
        reader=csv.reader(f,delimiter="\t")
        ids=next(reader)[8:]
        rows,symbols=[],[]
        for r in reader:
            rows.append(np.array(r[8:],dtype=np.int64))
            symbols.append(r[3])
    x=np.stack(rows)
    assert len(set(ids))==227 and set(ids)==set(labels)
    i,=[j for j,t in enumerate(ids) if labels[t].startswith("Ethosuximide [")]
    ctrl=np.array([j for j,t in enumerate(ids) if labels[t].startswith("Vehicle-")])
    block=[j for j,t in enumerate(ids) if t.split(".")[1]==ids[i].split(".")[1] and j!=i]
    assert len(ctrl)==9
    totals=x.sum(axis=0)
    common=x[(x>0).all(axis=1)]
    sf=np.median(common / np.exp(np.mean(np.log(common),axis=1))[:,None],axis=0)
    loc=[]
    for gene in TARGETS:
        matches=[j for j,g in enumerate(symbols) if g.upper()==gene]
        assert len(matches)==1
        loc.append(matches[0])
    cpm=x[loc]*1e6/totals
    med=np.median(cpm[:,ctrl],axis=1)
    keep=med>=1
    genes,stats=[],[]
    for name,denom in [("CPM",totals),("median_ratio",sf/np.median(sf)*np.median(totals))]:
        y=np.log2(1+x[loc]*1e6/denom)
        d=y-np.median(y[:,ctrl],axis=1)[:,None]
        score=d[keep].mean(axis=0)
        null=[np.mean(y[keep,k]-np.median(y[keep][:,ctrl[ctrl!=k]],axis=1)) for k in ctrl]
        stats.append([name,sum(keep),int(sum(d[keep,i]>0)),score[i],min(null),max(null),sum(score[block]<score[i]),
                      len(block),sum(keep)>=3 and sum(d[keep,i]>0)>=3 and score[i]>max(0,max(null))])
        for k,g in enumerate(TARGETS):genes.append([name,g,med[k],bool(keep[k]),int(x[loc[k],i]),d[k,i]])
    write(out/"drug_summary.tsv","normalization n_eligible n_up delta min_vehicle max_vehicle n_block_below block_size passes",stats)
    write(out/"drug_genes.tsv","normalization gene vehicle_median_CPM eligible treated_count delta",genes)


def reference(path,out):
    data=sheet(path)
    group=defaultdict(dict)
    for r in data:
        if not re.fullmatch(r"(CHIR|RA|XAV939)_[A-E]",r["Condition"]):continue
        if r["Cluster"] not in CLUSTERS:continue
        key=(r["Experiment"],r["Control"],r["Line"],r["Condition"])
        assert r["Cluster"] not in group[key]
        group[key][r["Cluster"]]=r
    grid,summary=[],[]
    for keys,clusters in sorted(group.items()):
        for c in CLUSTERS:
            r=clusters.get(c,{})
            grid.append([*keys,c,*[r.get(x,"NA") for x in ("oddsratio","padj","sample_size","score")]])
        def direction(c):
            r=clusters.get(c)
            if r is None:return "absent"
            if float(r["padj"])>=.01:return "uncertain"
            return "up" if float(r["oddsratio"])>1 else "down"
        up=[c for c in CLUSTERS[1:4] if direction(c)=="up"]
        summary.append([*keys,direction(CLUSTERS[0]),",".join(up) or "none",direction(CLUSTERS[-1]),
                        direction(CLUSTERS[0])=="down" and bool(up)])
    write(out/"reference.tsv","experiment control line condition lineage odds_ratio adjusted_P sampled_cell_count author_score",grid)
    write(out/"reference_summary.tsv","experiment control line condition telencephalic enriched_regional CNS_neurons directional_match",summary)


def disease(markers,counts,out,clusters=CLUSTERS,exclude=(),prefix="disease"):
    lookup=defaultdict(list)
    for r in sheet(markers):
        group=r["group"].replace("Cortical Hem / Diencephalic Progenitors","Diencephalic Progenitors")
        if group in clusters and float(r["logFC"])>0 and float(r["padj"])<.05 and r["feature"] not in TARGETS:
            lookup[group].append((float(r["auc"]),float(r["logFC"]),r["feature"]))
    top={g:sorted(values,key=lambda t:(-t[0],-t[1],t[2]))[:12] for g,values in lookup.items()}
    duplicates=Counter(v[2] for values in top.values() for v in values)
    with gzip.open(counts,"rt") as f:
        rd=csv.reader(f,delimiter="\t")
        titles=next(rd)[1:]
        arr={}
        sums=np.zeros(len(titles))
        for r in rd:
            x=np.array(r[1:],float)
            arr[r[0]]=arr.get(r[0],0)+x
            sums+=x
    ctrl=[i for i,t in enumerate(titles) if t.startswith("cwt")]
    ko=[i for i,t in enumerate(titles) if t.startswith("cko")]
    assert len(ctrl)==2 and len(ko)==4
    def contrast(x,omit=None):
        return x[[i for i in ko if i!=omit]].mean()-x[[i for i in ctrl if i!=omit]].mean()
    stats,genes=[],[]
    for grp in clusters:
        panels={"primary":[],"mapped":[]}
        for auc,fc,g in top[grp]:
            included=g in arr and duplicates[g]==1 and g not in exclude
            base=delta="NA"
            if included:
                cpm=arr[g]*1e6/sums
                base=cpm[ctrl].mean()
                y=np.log2(1+cpm)
                delta=contrast(y)
                panels["mapped"].append(y)
                if base>=1:panels["primary"].append(y)
            genes.append([grp,g,auc,fc,duplicates[g],base,delta])
        for typ,vals in panels.items():
            n=len(vals)
            if n<2:
                stats.append([grp,typ,n,*["NA"]*5,False]);continue
            y=np.stack(vals)
            avg=y.mean(axis=0)
            d=contrast(avg)
            loo=[contrast(avg,i) for i in ctrl+ko]
            gene_loo=[contrast(np.delete(y,i,axis=0).mean(axis=0)) for i in range(n)]
            stable=n>=4 and all(np.sign(z)==np.sign(d) for z in loo+gene_loo)
            stats.append([grp,typ,n,d,min(loo),max(loo),min(gene_loo),max(gene_loo),stable])
    write(out/f"{prefix}_markers.tsv","lineage gene source_AUC source_logFC panels_with_marker WT_mean_CPM WWOX_delta",genes)
    write(out/f"{prefix}_scores.tsv","lineage filter n delta omit_library_min omit_library_max omit_gene_min omit_gene_max passes_stability",stats)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("drug_counts","drug_meta","enrichments","markers","wwox_counts","out"):
        p.add_argument(key,type=Path)
    a=p.parse_args()
    a.out.mkdir(exist_ok=True,parents=True)
    drug(a.drug_counts,a.drug_meta,a.out)
    reference(a.enrichments,a.out)
    disease(a.markers,a.wwox_counts,a.out)
    write(a.out/"sources.tsv","input sha256",[(v.name,hashlib.sha256(v.read_bytes()).hexdigest()) for k,v in vars(a).items() if k!="out"])
