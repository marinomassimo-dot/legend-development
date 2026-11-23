"""Measure the fixed NMDA pairs in the Hadwen primary cortical drug screen."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path

import numpy as np


def tsv(path, names, records):
    with path.open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(names)
        writer.writerows(records)


def read_screen(counts_path, matrix_path):
    with gzip.open(matrix_path, "rt") as source:
        metadata = {r[0]:r[1:] for r in csv.reader(source, delimiter="\t")
                    if r and r[0] in ("!Sample_geo_accession","!Sample_title","!Sample_description")}
    mapping = dict(zip(metadata["!Sample_description"], zip(metadata["!Sample_title"], metadata["!Sample_geo_accession"], strict=True), strict=True))
    with gzip.open(counts_path, "rt") as source:
        reader = csv.reader(source, delimiter="\t")
        ids = next(reader)[8:]
        ens, symbols, rows = [],[],[]
        for row in reader:
            ens.append(row[0].split(".")[0])
            symbols.append(row[3])
            rows.append(np.array(row[8:], dtype=np.int64))
    assert len(set(ids)) == len(ids) == len(mapping) == 227 and set(ids) == set(mapping)
    assert len(set(ens)) == len(ens)
    titles = [mapping[i][0].rsplit("[",1)[0].strip() for i in ids]
    return np.stack(rows), ens, symbols, ids, titles, [mapping[i][1] for i in ids]


def main(counts_path, matrix_path, pairs_path, output):
    output.mkdir(exist_ok=True, parents=True)
    counts, ids, symbols, libraries, agents, gsm = read_screen(counts_path, matrix_path)
    index = {x:i for i,x in enumerate(ids)}
    with pairs_path.open() as stream:
        pairs = {}
        for row in csv.DictReader(stream, delimiter="\t"):
            pair = pairs.setdefault(row["pair"], {})
            assert row["arm"] not in pair
            pair[row["arm"]] = row["ensembl"]
    assert len(pairs) == 20 and all(set(p)=={"hit","control"} for p in pairs.values())
    vehicle = np.array([i for i,n in enumerate(agents) if n.startswith("Vehicle-")])
    drug, = [i for i,n in enumerate(agents) if n.startswith("Memantine")]
    thyroid, = [i for i,n in enumerate(agents) if n.startswith("Levothyroxine")]
    block, = [i for i in vehicle if libraries[i].split(".")[1] == libraries[drug].split(".")[1]]
    assert len(vehicle)==9
    other = [i for i in range(len(agents)) if i not in vehicle and i!=drug]
    total = counts.sum(axis=0)
    common = counts[(counts > 0).all(axis=1)]
    reference = np.exp(np.mean(np.log(common),axis=1))
    ratio = np.median(common / reference[:,None],axis=0)
    denom_ratio = ratio / np.median(ratio) * np.median(total)
    coverage, pair_rows, score_rows, marker_rows, summary = [], [], [], [], []
    median_cpm = np.median(1e6*counts[:,vehicle]/total[vehicle],axis=1)
    for num,p in pairs.items():
        for arm,g in p.items():
            present = g in index
            coverage.append([num,arm,g,symbols[index[g]] if present else "",float(median_cpm[index[g]]) if present else ""])
    for method, denom in (("CPM",total),("median_ratio",denom_ratio)):
        y = np.log2(1 + 1e6 * counts / denom)
        for sample, genes in ((thyroid,["Pmp22"]),(drug,["Inhba","Bdnf","Homer1"])):
            for gene in genes:
                assert symbols.count(gene)==1
                val = y[symbols.index(gene)]
                marker_rows.append([method,agents[sample],gene,val[sample]-np.median(val[vehicle]),min(val[vehicle]),val[sample],max(val[vehicle])])
        for filter_name, floor in (("primary",1),("mapped_only",0)):
            retained = [(num,index[p["hit"]],index[p["control"]]) for num,p in pairs.items()
                        if all(g in index and median_cpm[index[g]]>=floor for g in p.values())]
            if len(retained)<2:
                raise ValueError(f"{filter_name} has too few pairs to estimate sensitivity")
            hit = y[[p[1] for p in retained]]
            ctrl = y[[p[2] for p in retained]]
            differences = hit-ctrl
            scores = differences.mean(axis=0)
            delta = scores[drug] - np.median(scores[vehicle])
            v_delta = [scores[v]-np.median(scores[vehicle[vehicle!=v]]) for v in vehicle]
            per_pair = differences[:,drug] - np.median(differences[:,vehicle],axis=1)
            loo = []
            for j,(num,h,c) in enumerate(retained):
                loo_score = np.delete(differences,j,axis=0).mean(axis=0)
                loo.append(loo_score[drug]-np.median(loo_score[vehicle]))
                pair_rows.append([method,filter_name,num,symbols[h],symbols[c],per_pair[j],loo[-1]])
            sign = np.sign(delta)
            same = int((np.sign(per_pair)==sign).sum())
            block_delta = scores[drug]-scores[block]
            passed = (len(retained)>=8 and sign!=0 and abs(delta)>max(abs(v) for v in v_delta)
                      and np.sign(block_delta)==sign and all(np.sign(v)==sign for v in loo)
                      and 3*same>=2*len(retained))
            summary.append([method,filter_name,len(retained),delta,hit[:,drug].mean()-np.median(hit[:,vehicle].mean(axis=0)),
                            ctrl[:,drug].mean()-np.median(ctrl[:,vehicle].mean(axis=0)),min(v_delta),max(v_delta),
                            block_delta,same,min(loo),max(loo),sum(scores[i]<scores[drug] for i in other),len(other),bool(passed)])
            for j,lib in enumerate(libraries):
                baseline = np.median(scores[vehicle[vehicle!=j]])
                score_rows.append([method,filter_name,gsm[j],lib,agents[j],scores[j],scores[j]-baseline])
    tsv(output/"coverage.tsv",["pair","arm","ensembl","symbol","median_vehicle_cpm"],coverage)
    tsv(output/"pairs.tsv",["normalization","filter","pair","hit","control","pair_change","aggregate_without_pair"],pair_rows)
    tsv(output/"summary.tsv",["normalization","filter","complete_pairs","delta","hit_delta","control_delta","vehicle_min","vehicle_max","same_block_delta","pairs_same_sign","omit_pair_min","omit_pair_max","other_drugs_below","other_drugs_total","passes_this_normalization"],summary)
    tsv(output/"libraries.tsv",["normalization","filter","GSM","library","agent","score","change"],score_rows)
    tsv(output/"markers.tsv",["normalization","agent","gene","delta","min_vehicle","treated","max_vehicle"],marker_rows)
    tsv(output/"sources.tsv",["input","sha256"],[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in (counts_path,matrix_path,pairs_path)])


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ("counts","matrix","pairs","out"):
        parser.add_argument(name,type=Path)
    args=parser.parse_args()
    main(args.counts,args.matrix,args.pairs,args.out)
