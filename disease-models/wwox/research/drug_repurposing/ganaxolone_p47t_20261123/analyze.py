"""Test the frozen myelin challenge in an independent Wwox P47T expression study."""
import argparse
from collections import defaultdict
import csv
import gzip
import hashlib
from pathlib import Path
import re

import numpy as np
import xlrd


CLASSES = ["Astrocyte", "Neuron", "OPC", "NFO", "MO", "Microglia", "Endothelial"]
MARKERS = ["Aif1", "C1qa", "C1qb", "Tyrobp"]
REGIONS = {"HPC":"Hippocampus", "PFC":"Prefrontal cortex", "CTX":"Parietal cortex", "CB":"Cerebellum"}


def write(path, fields, records):
    with path.open("w") as out:
        writer=csv.writer(out,delimiter="\t",lineterminator="\n")
        writer.writerow(fields.split())
        for row in records:
            writer.writerow(f"{v:.6f}" if isinstance(v,(float,np.floating)) else v for v in row)


def metadata(path,samples):
    fields={}
    with gzip.open(path,"rt") as source:
        for row in csv.reader(source,delimiter="\t"):
            if not row:
                continue
            if row[0] in ("!Sample_title","!Sample_geo_accession"):
                fields[row[0]]=row[1:]
            if row[0]=="!Sample_characteristics_ch1" and row[1].startswith(("region:","genotype:")):
                key=row[1].split(":",1)[0]
                fields[key]=[v.split(": ",1)[1] for v in row[1:]]
    assert samples==fields["!Sample_title"] and len(set(samples))==37
    meta=[]
    for i,name in enumerate(samples):
        region,group,animal=name.split("_")
        assert fields["genotype"][i].endswith(group)
        assert REGIONS[region].lower()==fields["region"][i].lower()
        assert re.fullmatch(r"[MF]\d+",animal)
        meta.append((region,group,animal[0],animal,fields["!Sample_geo_accession"][i]))
    assert len({v[3] for v in meta})==10
    return meta


def p47t(path):
    expr={}
    with gzip.open(path,"rt") as src:
        rows=csv.reader(src,delimiter="\t")
        samples=next(rows)[2:]
        total=np.zeros(len(samples))
        for _,symbol,*cells in rows:
            v=np.array(cells,dtype=float)
            assert np.all(v>=0) and np.all(v==np.rint(v))
            total+=v
            if symbol and symbol!="NA":
                expr[symbol]=expr.get(symbol,0)+v
    return samples,{g:np.log2(1+v*1e6/total) for g,v in expr.items()}


def profiles(folder):
    maps=[]
    paths=[]
    for cell in CLASSES:
        sources=sorted(folder.glob(f"*_{cell}[12].xls.gz"))
        assert len(sources)==2
        reps=[]
        for path in sources:
            workbook=xlrd.open_workbook(file_contents=gzip.open(path).read())
            sheet=workbook.sheet_by_index(0)
            assert sheet.cell_value(0,0)=="gene.symbol"
            expr=defaultdict(list)
            for i in range(1,sheet.nrows):
                symbol=str(sheet.cell_value(i,0)).strip()
                if symbol and symbol!="NA":
                    expr[symbol].append(float(sheet.cell_value(i,1)))
            # Exclude ambiguous symbols in the sorted-cell reference.
            reps.append({g:v[0] for g,v in expr.items() if len(v)==1})
            paths.append(path)
        maps.append({g:(reps[0][g]+reps[1][g])/2 for g in reps[0].keys() & reps[1].keys()})
    return {g:np.array([m[g] for m in maps]) for g in set.intersection(*(set(m) for m in maps))},paths


def effects(meta,region):
    """Return descriptive sample weights for within-sex, crude and omission effects."""
    keep=[i for i,v in enumerate(meta) if v[0]==region]
    def weights(keep, sex=None):
        out=np.zeros(len(meta))
        for group,sign in [("P47T/P47T",1),("WT/WT",-1)]:
            use=[i for i in keep if meta[i][1]==group and (sex is None or meta[i][2]==sex)]
            if not use:
                return None
            out[use]=sign/len(use)
        return out
    def equal(keep):
        vals=[weights(keep,s) for s in ["M","F"]]
        return None if any(v is None for v in vals) else np.mean(vals,axis=0)
    main={"female":weights(keep,"F"),"male":weights(keep,"M"),"crude":weights(keep),"equal_sex":equal(keep)}
    jack=[equal([j for j in keep if j!=i]) for i in keep]
    return main,[v for v in jack if v is not None],len(jack)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ["files","signature","out"]:
        parser.add_argument(name,type=Path)
    args=parser.parse_args()
    args.out.mkdir(exist_ok=True,parents=True)
    source=args.files/"deepening_downloads/gse215425"
    counts,=source.glob("*processed_data*")
    series,=source.glob("*series_matrix*")
    samples,expression=p47t(counts)
    meta=metadata(series,samples)
    ref,paths=profiles(args.files/"geo/GSE52564_raw")
    with args.signature.open() as f:
        directions={r["gene"]:r["direction"] for r in csv.DictReader(f,delimiter="\t")}
    assert len(directions)==50
    write(args.out/"coverage.tsv","gene direction bulk reference",[(g,d,int(g in expression),int(g in ref)) for g,d in directions.items()])
    universe=sorted(expression.keys() & ref.keys())
    x=np.array([np.log2(1+ref[g]) for g in universe])
    x/=x.std(axis=0)
    genes=[g for g in directions if g in set(universe)]
    pool=[i for i,g in enumerate(universe) if g not in directions and g not in MARKERS]
    pool_x=x[pool]
    candidates=[]
    rows=[]
    for g in genes:
        distance=np.linalg.norm(pool_x-x[universe.index(g)],axis=1)
        ix=np.argsort(distance,kind="stable")[:20]
        candidates.append([pool[j] for j in ix])
        rows.extend((g,directions[g],k+1,universe[pool[j]],distance[j]) for k,j in enumerate(ix))
    write(args.out/"neighbors.tsv","target direction rank control distance",rows)
    seed=20261123
    rng=np.random.default_rng(seed)
    draws=[]
    for _ in range(2000):
        chosen=np.empty(len(genes),int)
        used=set()
        for i in rng.permutation(len(genes)):
            options=[j for j in candidates[i] if j not in used]
            if not options:
                raise ValueError(f"No unused nearest neighbor for {genes[i]}")
            chosen[i]=rng.choice(options)
            used.add(chosen[i])
        draws.append(chosen)
    draws=np.array(draws)
    up=np.array([directions[g]=="up" for g in genes])
    assert min(up.sum(),(~up).sum())>=15
    expression_matrix=np.array([expression[g] for g in universe])
    score={}
    for name,gs in [("full",[g for g in directions if g in expression]),("matched_subset",genes)]:
        arms=[[g for g in gs if directions[g]==d] for d in ("up","down")]
        assert min(map(len,arms))>=15
        score[name]=np.mean([expression[g] for g in arms[0]],axis=0)-np.mean([expression[g] for g in arms[1]],axis=0)
    score["generic_microglial"]=np.mean([expression[g] for g in MARKERS],axis=0)
    score["reference_neighbors"]=np.zeros(len(samples))
    draw_scores=np.empty((len(draws),len(samples)))
    for i in range(len(samples)):
        sampled=expression_matrix[:,i][draws]
        draw_scores[:,i]=sampled[:,up].mean(axis=1)-sampled[:,~up].mean(axis=1)
    score["reference_neighbors"]=draw_scores.mean(axis=0)
    score["subset_minus_neighbors"]=score["matched_subset"]-score["reference_neighbors"]
    panels,bench,contrib=[],[],[]
    for region in REGIONS:
        weights,jack,n=effects(meta,region)
        for label,s in score.items():
            ds=[s@v for v in jack]
            panels.append([region,label,*[s@weights[g] for g in ["equal_sex","female","male","crude"]],n,len(ds), min(ds),max(ds)])
        decoy=draw_scores@weights["equal_sex"]
        target=score["matched_subset"]@weights["equal_sex"]
        bench.append([region,len(decoy),target,*np.quantile(decoy,[.025,.5,.95,.975]),np.mean(decoy<target)])
        for g,d in directions.items():
            if g in expression:
                contrib.append([region,g,d,expression[g]@weights["equal_sex"]])
    write(args.out/"panels.tsv","region panel equal_sex female male crude total_loo estimable_loo loo_min loo_max",panels)
    write(args.out/"benchmarks.tsv","region draws matched_target q025 median q95 q975 fraction_below_target",bench)
    write(args.out/"genes.tsv","region gene arm equal_sex_delta",contrib)
    write(args.out/"libraries.tsv","sample region genotype sex animal accession "+" ".join(score),
          [[s,*meta[i],*[v[i] for v in score.values()]] for i,s in enumerate(samples)])
    with (args.out/"inputs.sha256").open("w") as out:
        for path in [args.signature,counts,series,*paths]:
            with path.open("rb") as f:
                print(hashlib.file_digest(f,"sha256").hexdigest(),path.name,sep="  ",file=out)


if __name__=="__main__":
    main()
