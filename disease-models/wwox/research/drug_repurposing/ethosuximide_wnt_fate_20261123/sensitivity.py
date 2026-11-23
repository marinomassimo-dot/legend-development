"""Specificity of the ethosuximide WNT score and peripheral-lineage transfer."""
import argparse
import csv
import gzip
from collections import Counter
from pathlib import Path
import numpy as np
from analyze import TARGETS, disease, sheet, write


def null_triplets(counts,meta,out):
    with gzip.open(meta,"rt") as f:
        m={r[0]:r[1:] for r in csv.reader(f,delimiter="\t") if r and r[0] in ("!Sample_title","!Sample_description")}
    labels=dict(zip(m["!Sample_description"],m["!Sample_title"],strict=True))
    with gzip.open(counts,"rt") as f:
        rd=csv.reader(f,delimiter="\t")
        ids=next(rd)[8:]
        names,rows=[],[]
        for r in rd:
            names.append(r[3].upper())
            rows.append(np.array(r[8:],float))
    x=np.stack(rows)
    vehicle=np.array([i for i,t in enumerate(ids) if labels[t].startswith("Vehicle-")])
    drug,=[i for i,t in enumerate(ids) if labels[t].startswith("Ethosuximide [")]
    other=[i for i in range(len(ids)) if i not in vehicle and i!=drug]
    cpm=x*1e6/x.sum(axis=0)
    y=np.log2(1+cpm)
    v=y[:,vehicle]
    features=np.column_stack([v.mean(axis=1),v.std(axis=1,ddof=1)])
    enough=np.median(cpm[:,vehicle],axis=1)>=1
    counts=Counter(names)
    pool=np.array([i for i,g in enumerate(names) if enough[i] and counts[g]==1 and g not in TARGETS])
    target=[i for i,g in enumerate(names) if enough[i] and g in TARGETS]
    assert len(target)==3 and len(vehicle)==9
    z=features/features[pool].std(axis=0)
    closest=[pool[np.argsort(np.linalg.norm(z[pool]-z[i],axis=1),kind="stable")[:50]] for i in target]
    delta=y-np.median(v,axis=1)[:,None]
    observed=delta[target].mean(axis=0)
    null=[]
    rng=np.random.default_rng(20261123)
    for _ in range(10000):
        selected=[]
        for c in closest:selected.append(rng.choice([i for i in c if i not in selected]))
        null.append(delta[selected,drug].mean())
    write(out/"drug_specificity.tsv","n_gene_pool n_draws target_delta q025 median q975 n_decoys_at_least_target other_drugs_below n_other_drugs",
          [[len(pool),len(null),observed[drug],*np.quantile(null,[.025,.5,.975]),sum(np.array(null)>=observed[drug]),
            sum(observed[other]<observed[drug]),len(other)]])


def periphery(markers,counts,enrichment,out):
    with (out/"disease_markers.tsv").open() as f:
        exclusions={r["gene"] for r in csv.DictReader(f,delimiter="\t")}
    clusters=["Neural Crest","PNS Progenitors","PNS Neurons"]
    disease(markers,counts,out,clusters,exclusions,"peripheral")
    result=[]
    for r in sheet(enrichment):
        if r["Condition"] in ["CHIR_D","CHIR_E","RA_D","RA_E"] and r["Cluster"] in clusters:
            result.append([r[s] for s in ("Experiment","Control","Line","Condition","Cluster","oddsratio","padj","sample_size","score")])
    write(out/"peripheral_reference.tsv","experiment control line condition lineage odds_ratio adjusted_P sampled_cell_count author_score",result)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("drug_counts","drug_meta","enrichments","markers","wwox_counts","out"):
        p.add_argument(key,type=Path)
    a=p.parse_args()
    null_triplets(a.drug_counts,a.drug_meta,a.out)
    periphery(a.markers,a.wwox_counts,a.enrichments,a.out)
