"""Check whether acute rat neuronal Wnt3a responses transfer to direct mouse drug exposure."""
import argparse
from collections import Counter, defaultdict
import csv
import gzip
import hashlib
from io import BytesIO
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import numpy as np

from analyze import TARGETS, write
from npc_transfer import expression, arm_values, orthologs


def reference(archive):
    with zipfile.ZipFile(archive) as outer:
        match, = [name for name in outer.namelist() if "Table 3" in name]
        payload = outer.read(match)
    with zipfile.ZipFile(BytesIO(payload)) as book:
        strings = ["".join(r.itertext()) for r in ET.fromstring(book.read("xl/sharedStrings.xml"))]
        rows = []
        for _, row in ET.iterparse(book.open("xl/worksheets/sheet1.xml"), events=("end",)):
            if not row.tag.endswith("}row"):
                continue
            values = {}
            for cell in row:
                val = cell.findtext("{*}v","")
                values[cell.get("r").rstrip("0123456789")] = strings[int(val)] if cell.get("t")=="s" else val
            row.clear()
            gene = values.get("B","")
            if not gene or gene=="id" or gene.upper() in TARGETS:
                continue
            try:
                baseline_a,baseline_b,fc,p = [float(values[k]) for k in "DEGH"]
            except (KeyError,ValueError):
                continue
            q = values.get("I","")
            rows.append((gene,fc,p,float(q) if q not in ("","NA","#N/A") else np.nan,baseline_a,baseline_b))
    counts = Counter(row[0] for row in rows)
    eligible = [r for r in rows if counts[r[0]]==1 and min(r[4:])>0 and np.isfinite(r[1]) and r[2]<.05]
    return [sorted((r for r in eligible if r[1]*sign>0),key=lambda r:(r[2],r[0]))[:20] for sign in [1,-1]]


def rat_to_mouse(hgnc_path, mouse_path, rat_path):
    mouse = orthologs(hgnc_path,mouse_path)
    human = json.loads(hgnc_path.read_text())["response"]["docs"]
    used = Counter(r for h in human for r in h.get("rgd_id",[]))
    rat = {ids[0]:mouse[h["symbol"]] for h in human if len(ids:=h.get("rgd_id",[]))==1 and
           used[ids[0]]==1 and h["symbol"] in mouse}
    by_name = defaultdict(set)
    with gzip.open(rat_path,"rt") as stream:
        for record in csv.DictReader(stream,delimiter="\t"):
            for rid in record["dbXrefs"].split("|"):
                if rid.startswith("RGD:"):
                    for name in [record["Symbol"],*record["Synonyms"].split("|")]:
                        if name != "-":
                            by_name[name].add(rid)
    return {name:rat[next(iter(ids))] for name,ids in by_name.items() if len(ids)==1 and next(iter(ids)) in rat}


def analyze(args):
    groups = reference(args.archive)
    arms = [[r[0] for r in grp] for grp in groups]
    samples,x = expression(args.counts,True)
    with gzip.open(args.meta,"rt") as stream:
        meta = {r[0]:r[1:] for r in csv.reader(stream,delimiter="\t") if r and r[0] in ("!Sample_title","!Sample_description")}
    labels = dict(zip(meta["!Sample_description"], meta["!Sample_title"],strict=True))
    ctrl = np.array([i for i,t in enumerate(samples) if labels[t].startswith("Vehicle-")])
    drug, = [i for i,s in enumerate(samples) if labels[s].startswith("Ethosuximide [")]
    assert len(samples)==227 and len(ctrl)==9
    screen = [i for i in range(len(samples)) if i not in ctrl]
    block = [i for i in screen if samples[i].split(".")[1]==samples[drug].split(".")[1]]
    folded = defaultdict(list)
    for symbol in x:
        folded[symbol.upper()].append(symbol)
    modes = {"symbol":{g:folded[g.upper()][0] for arm in arms for g in arm if len(folded[g.upper()])==1},
             "orthology":rat_to_mouse(args.hgnc,args.mouseinfo,args.ratinfo)}
    summary,coverage,robustness = [],[],[]
    for mode,lookup in modes.items():
        # Avoid double-counting a mouse gene under different historical rat symbols.
        repeated = Counter(lookup[g] for arm in arms for g in arm if g in lookup)
        lookup = {g:m for g,m in lookup.items() if repeated[m]==1}
        panels,rows = arm_values(arms,x,ctrl,lookup,True)
        coverage.extend([[mode,*r] for r in rows])
        def changes(ref):
            return [np.mean(y-np.median(y[:,ref],axis=1)[:,None],axis=0) for y in panels]
        up,down = changes(ctrl)
        component = panels[0]-np.median(panels[0][:,ctrl],axis=1)[:,None]
        loo = [np.delete(component,k,axis=0).mean(axis=0) for k in range(len(component))]
        ranks = [1+sum(a[i]>a[drug] for i in screen) for a in loo]
        vehicle_up = [np.mean(panels[0][:,i]-np.median(panels[0][:,ctrl[ctrl!=i]],axis=1)) for i in ctrl]
        robustness.append([mode,len(component),sum(component[:,drug]>0),up[drug],
                           min(vehicle_up),max(vehicle_up),min(ranks),max(ranks)])
        score = (up-down)/2
        null = []
        for j in ctrl:
            u,d = changes(ctrl[ctrl!=j])
            null.append((u[j]-d[j])/2)
        rank = 1+sum(score[i]>score[drug] for i in screen)
        decision = "partial_coverage"
        if min(map(len,panels))>=8:
            decision = "inconclusive"
            if up[drug]>0>down[drug] and score[drug]>max(null) and rank<=21:
                decision = "activation_like"
            if up[drug]<0<down[drug] and score[drug]<min(null) and rank>=198:
                decision = "inhibition_like"
        summary.append([mode,*map(len,panels),up[drug],down[drug],score[drug],min(null),max(null),rank,
                        1+sum(score[i]>score[drug] for i in block),len(block),1+sum(up[i]>up[drug] for i in screen),decision])
    out=args.out
    out.mkdir(exist_ok=True,parents=True)
    write(out/"rat_acute_reference.tsv","arm n n_FDR_lt_005 min_nominal_P max_nominal_P",
          [[name,len(group),sum(r[3]<.05 for r in group),min(r[2] for r in group),max(r[2] for r in group)]
           for name,group in zip(["up","down"],groups,strict=True)])
    write(out/"rat_acute_drug.tsv","mapping n_up n_down up_delta down_delta score vehicle_min vehicle_max rank_of_218 block_rank block_n up_only_rank decision",summary)
    write(out/"rat_acute_coverage.tsv","mapping arm rat_gene mouse_symbol eligible median_vehicle_CPM",coverage)
    write(out/"rat_acute_up_only.tsv","mapping n n_positive mean_delta vehicle_min vehicle_max leave_one_gene_best_rank leave_one_gene_worst_rank",robustness)
    write(out/"rat_acute_inputs.tsv","input sha256",[(v.name,hashlib.sha256(v.read_bytes()).hexdigest()) for k,v in vars(args).items() if k!="out"])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("archive","counts","meta","hgnc","mouseinfo","ratinfo","out"):
        p.add_argument(key,type=Path)
    analyze(p.parse_args())
