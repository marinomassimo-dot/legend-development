"""Cross-donor validation of a memantine response using physically measured L1000 landmarks."""
import argparse
import csv
import gzip
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import numpy as np


def write(path, fields, records):
    with path.open("w") as stream:
        w=csv.writer(stream,delimiter="\t",lineterminator="\n")
        w.writerow(fields.split())
        w.writerows(records)


def study_labels(workbook):
    with zipfile.ZipFile(workbook) as z:
        strings=["".join(v.itertext()) for v in ET.fromstring(z.read("xl/sharedStrings.xml"))]
        sheet=ET.fromstring(z.read("xl/worksheets/sheet5.xml"))
        labels={}
        for row in sheet.findall(".//{*}row"):
            cells=[]
            for c in row.findall("{*}c"):
                v=c.findtext("{*}v","")
                cells.append(strings[int(v)] if v and c.attrib.get("t")=="s" else v)
            if cells[0]=="MEMANTINE HYDROCHLORIDE":
                line,well=cells[1:3]
                assert line not in labels
                labels[line]=(well,cells[-1])
    assert len(labels)==24
    return labels


def probe_map(platform, annotation, hgnc):
    with platform.open() as f:
        for line in f:
            if line.startswith("!platform_table_begin"):break
        probes={r["ID"] for r in csv.DictReader(f,delimiter="\t") if r.get("FLAG")=="LM"}
    records=json.loads(hgnc.read_text())["response"]["docs"]
    symbols=defaultdict(set)
    for r in records:
        if r.get("entrez_id"):
            symbols[str(r["entrez_id"])].add(r["symbol"])
    mapped={}
    with gzip.open(annotation,"rt") as f:
        for line in f:
            if line.startswith("!platform_table_begin") or line.startswith("!annotation_table_begin"):break
        for r in csv.DictReader(f,delimiter="\t"):
            if r["ID"] in probes and len(symbols.get(r["Gene ID"],[]))==1:
                mapped[r["ID"]]=next(iter(symbols[r["Gene ID"]]))
    return probes,mapped


def disease(path):
    with gzip.open(path,"rt") as f:
        rows=csv.reader(f,delimiter="\t")
        names=next(rows)[1:]
        values={}
        sums=np.zeros(len(names))
        for r in rows:
            x=np.array(r[1:],float)
            sums+=x
            values[r[0]]=values.get(r[0],0)+x
    return names,{s:np.log2(1+x*1e6/sums) for s,x in values.items()}


def load_plate(path, probe_gene, allowed, labels, perturbagen="MEMANTINE HYDROCHLORIDE", dose="0.01_uM"):
    with gzip.open(path,"rt") as f:
        char={}
        for r in csv.reader(f,delimiter="\t"):
            if not r: continue
            if r[0]=="!Sample_geo_accession": access=r[1:]
            if r[0]=="!Sample_characteristics_ch1":
                # GEO omits the dose field for vehicle wells, shifting subsequent
                # characteristics up one row. Parse every cell by its own key.
                for j, entry in enumerate(r[1:]):
                    key,sep,value=entry.partition(": ")
                    if sep:
                        char.setdefault(key,[""]*(len(r)-1))[j]=value
            if r[0]=="!series_matrix_table_begin":break
        titles=next(csv.reader([f.readline()],delimiter="\t"))[1:]
        assert titles==access
        treat=[i for i,n in enumerate(char["perturbagen"]) if n.upper()==perturbagen and char["cell id"][i] in labels]
        if not treat:return {}
        keep=set()
        donors={}
        # For the auxiliary duplicated plate control, take one well per line to
        # match the one-well memantine design, selected by well ID alone.
        for i in sorted(treat,key=lambda j:char["well id"][j]):
            donor=char["cell id"][i]
            well,group=labels[donor]
            assert char["plate id"][i]==well.split("_")[0]
            if perturbagen=="MEMANTINE HYDROCHLORIDE":
                assert char["plate id"][i]+"_"+char["well id"][i]==well
            elif donor in donors:
                continue
            assert char["dosage"][i]==dose and char["duration"][i]=="6_hours"
            ctr=[j for j,n in enumerate(char["perturbagen"]) if n.upper()=="DMSO" and char["cell id"][j]==donor
                 and char["plate id"][j]==char["plate id"][i] and char["duration"][j]==char["duration"][i]]
            assert len(ctr)>=2 and donor not in donors
            keep.update([i,*ctr])
            donors[donor]=(i,ctr,group)
        ordered=sorted(keep)
        locations={i:j for j,i in enumerate(ordered)}
        by_gene=defaultdict(list)
        for line in f:
            if line.startswith("!series_matrix_table_end"):break
            key,_,rest=line.partition("\t")
            gene=probe_gene.get(key.strip('"'))
            if gene in allowed:
                v=np.fromstring(rest,sep="\t")
                assert len(v)==len(titles)
                by_gene[gene].append(v[ordered])
    symbols=sorted(by_gene)
    y=np.stack([np.median(by_gene[s],axis=0) for s in symbols])
    assert np.isfinite(y).all()
    result={}
    for d,(i,ctr,group) in donors.items():
        w=char["well id"][i]
        def dist(j):
            other=char["well id"][j]
            return (ord(w[0])-ord(other[0]))**2+(int(w[1:])-int(other[1:]))**2
        near=sorted(dist(j) for j in ctr)[1]
        neighbours=[locations[j] for j in ctr if dist(j)<=near]
        same=[locations[j] for j in ctr if w[0]==char["well id"][j][0]]
        v=y[:,[locations[j] for j in ctr]]
        result[d]=dict(symbols=symbols,treated=y[:,locations[i]],vehicles=v,near=y[:,neighbours],same=y[:,same],
                       plate=char["plate id"][i],well=w,gsm=access[i],group=group,vehicle_ids=[access[j] for j in ctr])
    return result


def main(args):
    out=args.out
    out.mkdir(exist_ok=True,parents=True)
    names,org=disease(args.organoids)
    labels=study_labels(args.workbook)
    landmarks,probe_gene=probe_map(args.platform,args.annotation,args.hgnc)
    plates=sorted(args.plates.glob("GSE*_series_matrix.txt.gz"))
    donors={}
    for plate in plates:
        p=load_plate(plate,probe_gene,org,labels)
        assert not (set(donors)&set(p)), "Duplicate treated line; check dose/plate grouping"
        donors.update(p)
    symbols=next(iter(donors.values()))["symbols"]
    assert all(v["symbols"]==symbols for v in donors.values())
    controls=sorted(d for d,v in donors.items() if v["group"]=="controls")
    other=sorted(d for d,v in donors.items() if v["group"]=="cases")
    ix={s:i for i,s in enumerate(symbols)}
    def diff(d):
        v=donors[d]
        return v["treated"]-np.median(v["vehicles"],axis=1)
    def score(x,up,down):
        return x[up].mean(axis=0)-x[down].mean(axis=0)
    design=[]
    for d,(well,g) in sorted(labels.items()):
        v=donors.get(d)
        design.append([d,g,well,v["gsm"] if v else "NA",v["vehicles"].shape[1] if v else 0,
                       ",".join(v["vehicle_ids"]) if v else "NA"])
    summ,per,gene_rows,orgrows, nullrows, qc=[],[],[],[],[],[]
    for scheme,train,hold in [("primary",controls[::2],controls[1::2]),("swapped",controls[1::2],controls[::2])]:
        training=np.stack([diff(d) for d in train])
        median=np.median(training,axis=0)
        stable=math.ceil(2*len(train)/3)
        v_train=np.stack([np.median(donors[d]["vehicles"],axis=1) for d in train])
        # Filter non-finite, zero/negative median normalized intensities and invariant drug-control measurements.
        ok=np.isfinite(median)&(np.median(v_train,axis=0)>0)&(np.ptp(training,axis=0)>0)
        up=[i for i in np.argsort(-median,kind="stable") if ok[i] and median[i]>0 and (training[:,i]>0).sum()>=stable][:10]
        down=[i for i in np.argsort(median,kind="stable") if ok[i] and median[i]<0 and (training[:,i]<0).sum()>=stable][:10]
        assert len(up)==len(down)==10
        for arm,genes in [("up",up),("down",down)]:
            for j in genes:gene_rows.append([scheme,arm,symbols[j],median[j],int((training[:,j]>0).sum()),len(train)])
        cache={}
        for role,group in [("discovery",train),("heldout",hold),("other_diagnosis",other)]:
            results=[]
            for d in group:
                v=donors[d]
                drug=diff(d)
                values=[score(v["treated"]-np.median(v[k],axis=1),up,down) if v[k].shape[1] else np.nan for k in ("near","same")]
                jack=([score(drug,[i for i in up if i!=j],down) for j in up]+[score(drug,up,[i for i in down if i!=j]) for j in down])
                hit,low=drug[up].mean(),drug[down].mean()
                results.append((hit,low,hit-low,*values))
                per.append([scheme,role,d,hit,low,hit-low,*values,min(jack),max(jack)])
                if role=="heldout":
                    vmat=v["vehicles"]
                    cache[d]=[]
                    for j in range(vmat.shape[1]):
                        a=score(vmat[:,j]-np.median(np.delete(vmat,j,axis=1),axis=1),up,down)
                        cache[d].append(a)
                        nullrows.append([scheme,d,v["vehicle_ids"][j],a])
            a=np.array(results)
            if role=="heldout":
                pseudo=np.concatenate(list(cache.values()))
                # Also match the statistic to the donor median by sampling one vehicle per held-out line.
                rng=np.random.default_rng(20261123)
                pseudo_medians=np.median(np.stack([rng.choice(cache[d],size=10000) for d in hold]),axis=0)
                hit,low,contrast=np.median(a[:,:3],axis=0)
                q95=float(np.quantile(pseudo,.95))
                donor_q95=float(np.quantile(pseudo_medians,.95))
                positive=int(sum(a[:,2]>0))
                passed=positive>=math.ceil(.8*len(hold)) and hit>0 and low<0 and contrast>q95
                summ.append([scheme,len(train),len(hold),positive,hit,low,contrast,q95,donor_q95,float(np.median(a[:,3])),float(np.nanmedian(a[:,4])),bool(passed)])
        # Disease-side scores are retained as exploratory if the donor validation failed.
        k=[i for i,n in enumerate(names) if n.startswith("cko")]
        w=[i for i,n in enumerate(names) if n.startswith("cwt")]
        assert len(k)==4 and len(w)==2
        mat=np.stack([org[s] for s in symbols])
        baseline=mat[:,w].mean(axis=1)
        delta=mat[:,k].mean(axis=1)-baseline
        ss=score(mat,up,down)
        loo=[np.mean(ss[[i for i in k if i!=j]])-np.mean(ss[[i for i in w if i!=j]]) for j in k+w]
        targets=up+down
        pool=np.array([i for i in range(len(symbols)) if i not in targets])
        closest=[pool[np.argsort(abs(baseline[pool]-baseline[j]),kind="stable")[:25]] for j in targets]
        rng=np.random.default_rng(20261123)
        null=[]
        for _ in range(2000):
            chosen=[]
            for cand in closest:
                chosen.append(rng.choice([i for i in cand if i not in chosen]))
            null.append(score(delta,chosen[:10],chosen[10:]))
        orgrows.append([scheme,delta[up].mean(),delta[down].mean(),score(delta,up,down),min(loo),max(loo),*np.quantile(null,[.025,.975])])
        qc.append([scheme,len(landmarks),len(probe_gene),len(ix),int(ok.sum()),",".join(train),",".join(hold)])
    write(out/"design.tsv","study_line study_group plate_well treated_GSM matched_vehicles vehicle_GSMs",design)
    write(out/"validation.tsv","scheme n_discovery n_heldout n_positive_heldout median_up median_down median_score pooled_vehicle_q95 vehicle_medians_q95 median_nearest_vehicle_score median_same_row_vehicle_score passes_frozen_rule",summ)
    write(out/"panels.tsv","scheme arm gene median_discovery_effect n_discovery_positive n_discovery",gene_rows)
    write(out/"donors.tsv","scheme split study_line up down difference nearest_controls same_row_controls omit_gene_min omit_gene_max",per)
    write(out/"vehicles.tsv","scheme line heldout_vehicle_GSM score",nullrows)
    write(out/"disease.tsv","scheme up down score omit_library_min omit_library_max matched_q025 matched_q975",orgrows)
    write(out/"coverage.tsv","scheme landmark_probe_ids annotated_probes mapped_WWOX_genes eligible_genes discovery_lines heldout_lines",qc)
    write(out/"sources.tsv","file sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in [args.workbook,args.platform,args.annotation,args.hgnc,args.organoids,*plates]])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for k in ("plates","workbook","platform","annotation","hgnc","organoids","out"):
        p.add_argument(k,type=Path)
    main(p.parse_args())
