"""Test whether ethosuximide resembles a condition-matched GSK3 inhibitor profile."""
import argparse
from collections import defaultdict
import csv
import gzip
import hashlib
from pathlib import Path
import random

import h5py
import numpy as np


SB = "SB-216763"
TESTS = ["CHIR-99021", "GSK-3-inhibitor-IX", "ethosuximide"]
CONDITIONS = [("MCF7", "6"), ("MCF7", "24"), ("PC3", "24")]


def records(path):
    with gzip.open(path, "rt") as source:
        yield from csv.DictReader(source, delimiter="\t")


def write(path, fields, rows):
    with path.open("w") as stream:
        writer=csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(fields.split())
        writer.writerows(rows)


def main(folder, out, complete_background=False, swap=False):
    out.mkdir(exist_ok=True, parents=True)
    def meta(name):
        path,=folder.glob("*_"+name+".txt.gz")
        return path
    anchor = "GSK-3-inhibitor-IX" if swap else SB
    tests = [SB if name==anchor else name for name in TESTS]
    names = {anchor,*tests}
    compound_rows=list(records(meta("pert_info")))
    chemicals={r["pert_id"]:r for r in compound_rows if r["pert_type"]=="trt_cp"}
    named_connectivity={r["inchi_key_prefix"] for r in chemicals.values() if r["pert_iname"] in names}
    study={c:defaultdict(list) for c in CONDITIONS}
    for r in records(meta("sig_info")):
        condition=r["cell_id"],r["pert_time"]
        if condition not in study or r["pert_type"]!="trt_cp" or r["pert_dose_unit"]!="µM" or r["pert_time_unit"]!="h":
            continue
        if float(r["pert_dose"])!=10:
            continue
        pid=r["pert_id"]
        if pid not in chemicals or (r["pert_iname"] not in names and chemicals[pid]["inchi_key_prefix"] in named_connectivity):
            continue
        study[condition][r["pert_iname"]].append(r)
    wanted_metrics={r["sig_id"] for condition in CONDITIONS for name in names for r in study[condition][name]}
    metrics={r["sig_id"]:r for r in records(meta("sig_metrics")) if r["sig_id"] in wanted_metrics}
    assert set(metrics)==wanted_metrics
    rows_qc=[]
    for condition, drugs in study.items():
        for name in sorted(names):
            for r in drugs[name]:
                m=metrics[r["sig_id"]]
                c=chemicals[r["pert_id"]]
                rows_qc.append([*condition,name,r["sig_id"],r["pert_id"],c["pubchem_cid"],c["inchi_key"],
                                len(r["distil_id"].split("|")),m["distil_nsample"],m["distil_cc_q75"],m["distil_ss"],m["tas"]])
    write(out/"profiles.tsv","cell hours compound sig_id pert_id PubChem InChIKey instances metadata_n cc_q75 strength TAS",rows_qc)
    gene_data=list(records(meta("gene_info")))
    lm={g["pr_gene_id"]:g["pr_gene_symbol"] for g in gene_data if g["pr_is_lm"]=="1"}
    markers=["AXIN2","NKD1","APCDD1","LEF1"]
    write(out/"markers.tsv","symbol present measured_landmark",[[s,any(g["pr_gene_symbol"]==s for g in gene_data),s in lm.values()] for s in markers])
    results,background,signatures=[],[],[]
    path,=folder.glob("*.gctx")
    with h5py.File(path) as database:
        index={s:i for i,s in enumerate(database["0/META/COL/id"].asstr()[:])}
        gene_ids=database["0/META/ROW/id"].asstr()[:]
        indices=np.array([i for i,g in enumerate(gene_ids) if g in lm])
        symbols=[lm[gene_ids[i]] for i in indices]
        assert len(indices)==len(lm)==978
        matrix=database["0/DATA/0/matrix"]
        assert matrix.shape==(len(index),len(gene_ids))
        def profile(group):
            return np.median([matrix[index[r["sig_id"]],:][indices] for r in group],axis=0)
        for condition,drugs in study.items():
            reference=profile(drugs[anchor])
            order=np.argsort(reference,kind="stable")
            down,up=order[:20],order[-20:]
            for direction,genes in [("up",up),("down",down)]:
                signatures.extend([[*condition,direction,symbols[g],reference[g]] for g in genes])
            cache = {}
            def scores(group):
                key=tuple(r["sig_id"] for r in group)
                if key not in cache:
                    value=profile(group)
                    cache[key]=(float(np.corrcoef(value,reference)[0,1]),
                                float((np.mean(value[up])-np.mean(value[down]))/2))
                return cache[key]
            others={k:v for k,v in drugs.items() if k not in names}
            for test in tests:
                if not drugs[test]:
                    continue
                q=np.array(scores(drugs[test]))
                prefixes={r["sig_id"].split(":")[0] for r in drugs[test]}
                matched={k:[r for r in v if r["sig_id"].split(":")[0] in prefixes] for k,v in others.items()}
                pools=[("all",others,200),("same_plate",{k:v for k,v in matched.items() if v},150)]
                for label,pool,maximum in pools:
                    population=sorted(pool)
                    rng=random.Random("|".join((*condition,label,"0" if label=="all" else ",".join(sorted(prefixes)),"20261123")))
                    selected=population if complete_background else sorted(rng.sample(population,min(len(pool),maximum)))
                    null=[]
                    for k in selected:
                        s=scores(pool[k])
                        null.append(s)
                        if not complete_background:
                            background.append([*condition,test,label,k,len(pool[k]),*s])
                    if not null:
                        results.append([*condition,test,label,len(pool),0,*q,*["NA"]*5])
                        continue
                    distribution=np.array(null)
                    limits=np.quantile(distribution,.95,axis=0)
                    passed=bool(np.all(q>limits) and np.all(q>0))
                    results.append([*condition,test,label,len(pool),len(null),*q,*limits,
                                    *(np.sum(distribution>=q,axis=0)),passed])
    destination="scores_all_chemicals.tsv" if complete_background else "scores.tsv"
    write(out/destination,"cell hours compound reference_pool pool_size sampled correlation signed_score correlation_p95 signed_p95 n_corr_ge n_signed_ge both_pass",results)
    if not complete_background:
        write(out/"background.tsv","cell hours query reference_pool background_compound profiles correlation signed_score",background)
    write(out/"reference_landmarks.tsv","cell hours arm gene reference_consensus_z",signatures)
    paths=[meta(i) for i in ("pert_info","sig_info","sig_metrics","gene_info")]
    write(out/"metadata_inputs.tsv","input sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("folder",type=Path)
    p.add_argument("out",type=Path)
    p.add_argument("--all-controls",action="store_true",help="Enumerate all eligible background chemicals.")
    p.add_argument("--swap",action="store_true",help="Use GSK-3-inhibitor-IX as the anchor.")
    a=p.parse_args()
    main(a.folder,a.out,a.all_controls,a.swap)
