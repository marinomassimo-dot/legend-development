"""Test late allopregnanolone-associated panel directions in WWOX-null organoids."""
import argparse
import csv
import gzip
import hashlib
import itertools
import json
import tarfile
from collections import Counter
from pathlib import Path

import numpy as np

PANELS = {
    "receptor": "GABRA1 GABRA5 GABRB1 GABRB3 GABRG2".split(),
    "effector": "SLC32A1 SLC6A1 SLC6A11 KCNJ3 GPHN GABARAP GABBR2 GABBR1".split(),
    "interneuron": "GAD1 GAD2 CALB2 SST".split(),
    "neuronal": "TUBB3 MAP2 RBFOX3 SNAP25".split(),
}


def write(path, fields, data):
    with path.open("w") as stream:
        w = csv.writer(stream, delimiter="\t", lineterminator="\n")
        w.writerow(fields.split())
        w.writerows(data)


def disease(path):
    with gzip.open(path, "rt") as source:
        reader = csv.reader(source, delimiter="\t")
        titles = next(reader)[1:]
        names, rows = [], []
        for r in reader:
            names.append(r[0])
            rows.append(np.array(r[1:],float))
    raw = np.stack(rows)
    assert np.isfinite(raw).all() and (raw>=0).all()
    # Resolve duplicate symbols before per-gene scores. Include every row in the library total.
    distinct = sorted(set(names))
    ids = {s:i for i,s in enumerate(distinct)}
    combined = np.zeros((len(distinct),len(titles)))
    np.add.at(combined,[ids[n] for n in names],raw)
    return distinct,titles,combined * 1e6 / raw.sum(axis=0)


def reference(archive, meta, hgnc, symbols):
    docs = json.loads(hgnc.read_text())["response"]["docs"]
    all_ids = [(d["symbol"],d["ensembl_gene_id"]) for d in docs if d.get("ensembl_gene_id")]
    freq = Counter(g for _,g in all_ids)
    lookup = {name:g for name,g in all_ids if freq[g]==1}
    with gzip.open(meta,"rt") as source:
        for r in csv.reader(source,delimiter="\t"):
            if not r: continue
            if r[0]=="!Sample_title": titles=r[1:]
            if r[0]=="!Sample_characteristics_ch1":
                if r[1].startswith("iPSc line:"): lines=[x.partition(": ")[2] for x in r[1:]]
                if r[1].startswith("differentiation day:"): days=[int(x.partition(": ")[2]) for x in r[1:]]
    values = {}
    with tarfile.open(archive) as src:
        for m in src:
            if not m.name.endswith(".csv.gz"): continue
            with gzip.open(src.extractfile(m),"rt") as stream:
                reader = csv.reader(stream)
                title = next(reader)[1]
                expr = {r[0]:float(r[1]) for r in reader}
            total=sum(expr.values())
            assert total>0 and title not in values
            values[title]=[np.log2(1+expr[g]*1e6/total) if (g:=lookup.get(s)) in expr else np.nan for s in symbols]
    assert set(values)==set(titles) and len(values)==62
    return np.array([values[k] for k in titles]).T,np.array(lines),np.array(days)


def slopes(values,lines,days,mask):
    v=values[:,mask]
    t=np.log2(days[mask].astype(float))
    labels=lines[mask]
    centered=np.zeros(t.size)
    informative=[]
    for label in sorted(set(labels)):
        sel=labels==label
        centered[sel]=t[sel]-t[sel].mean()
        if len(set(t[sel]))>1: informative.append(label)
    return v.mean(axis=1), v@centered/(centered@centered), informative


def main(files,out):
    out.mkdir(exist_ok=True,parents=True)
    base=files/"geo"
    counts,= (base/"GSE156243").glob("*count_table.txt.gz")
    hgnc,= (base/"GSE156243").glob("hgnc_complete_set*.json")
    archive,meta=[base/"GSE150123"/s for s in ["GSE150123_RAW.tar","GSE150123_series_matrix.txt.gz"]]
    syms,titles,cpm=disease(counts)
    index={s:i for i,s in enumerate(syms)}
    case=[i for i,t in enumerate(titles) if t.startswith("cko")]
    ctrl=[i for i,t in enumerate(titles) if t.startswith("cwt")]
    assert len(case)==4 and len(ctrl)==2 and len(titles)==6
    base_cpm=cpm[:,ctrl].mean(axis=1)
    y=np.log2(1+cpm)
    delta=y[:,case].mean(axis=1)-y[:,ctrl].mean(axis=1)
    def contrast(v, drop=None):
        return v[[i for i in case if i!=drop]].mean()-v[[i for i in ctrl if i!=drop]].mean()
    lib, genes, stats, alloc, decoys = [],[],[],[],[]
    for name,p in PANELS.items():
        for s in p:
            i=index.get(s)
            genes.append([name,s,"absent" if i is None else base_cpm[i],"NA" if i is None else delta[i]])
    for method, floor in (("primary",1),("mapped_only",0)):
        panel_ids={p:[index[s] for s in symbols if s in index and base_cpm[index[s]]>=floor] for p,symbols in PANELS.items()}
        effects={}
        for p, ix in panel_ids.items():
            assert ix
            effects[p]=y[ix].mean(axis=0)
        effects["receptor_minus_effector"]=effects["receptor"]-effects["effector"]
        for p,v in effects.items():
            loo=[contrast(v,i) for i in range(len(titles))]
            contained=panel_ids.get(p,[])
            stats.append([method,p,len(contained) if contained else "NA",contrast(v),min(loo),max(loo),
                          sum(delta[i]>0 for i in contained) if contained else "NA"])
            lib.extend([method,p,titles[i],v[i]] for i in range(len(titles)))
        for two in itertools.combinations(range(6),2):
            others=sorted(set(range(6))-set(two))
            alloc.append([method,",".join(titles[i] for i in two),list(two)==ctrl,
                          *[np.mean(effects[p][others])-np.mean(effects[p][list(two)]) for p in ("receptor","effector","receptor_minus_effector")]])
    ref,lines,days=reference(archive,meta,hgnc,syms)
    unique_targets=[index[s] for p in PANELS.values() for s in p if s in index]
    for name,mask in [("day40_to_160",(days>=40)&(days<=160)),("all_days",np.ones(len(days),bool))]:
        avg,slope,informative=slopes(ref,lines,days,mask)
        features=np.column_stack([np.log2(1+base_cpm),avg,slope])
        eligible=np.isfinite(features).all(axis=1) & (base_cpm>=1)
        eligible[unique_targets]=False
        pool=np.where(eligible)[0]
        standard=features/np.std(features[pool],axis=0)
        rng=np.random.default_rng(20261123)
        receptor=[index[s] for s in PANELS["receptor"] if s in index and base_cpm[index[s]]>=1]
        effector=[index[s] for s in PANELS["effector"] if s in index and base_cpm[index[s]]>=1]
        targets=receptor+effector
        if not np.isfinite(standard[targets]).all():
            raise ValueError(f"{name}: targets lacked an independent reference feature")
        nearest=[pool[np.argsort(np.linalg.norm(standard[pool]-standard[t],axis=1),kind="stable")[:50]] for t in targets]
        samples=[]
        for _ in range(2000):
            chosen=[]
            for cand in nearest:
                options=[i for i in cand if i not in chosen]
                chosen.append(rng.choice(options))
            cut=len(receptor)
            samples.append(delta[chosen[:cut]].mean()-delta[chosen[cut:]].mean())
        obs=delta[receptor].mean()-delta[effector].mean()
        decoys.append([name,int(sum(mask)),len(informative),",".join(informative),len(pool),len(samples),obs,
                       *np.quantile(samples,[.025,.5,.975]),float(np.mean(np.asarray(samples)<obs))])
    write(out/"genes.tsv","panel symbol control_mean_CPM delta",genes)
    write(out/"summary.tsv","filter panel n_genes delta omit_library_min omit_library_max n_increased",stats)
    write(out/"library_scores.tsv","filter panel library score",lib)
    write(out/"allocations.tsv","filter control_pair observed_labels receptor effector receptor_minus_effector",alloc)
    write(out/"development_controls.tsv","age_window libraries informative_lines line_names decoy_gene_pool draws observed q025 median q975 percentile_fraction",decoys)
    write(out/"sources.tsv","input sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in (counts,hgnc,archive,meta)])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.files,a.out)
