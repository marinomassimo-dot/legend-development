"""Recalculate the frozen N2A transfer prediction in GEO GSE110256."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path

import numpy as np

PRIMARY = ["Ccng2", "Cdkn1b", "Rbl2", "Gadd45a"]
COMPARATOR = ["Cdkn1a", "Bcl2l11", "Cat", "Sod2", "Eif4ebp1"]


def metadata(path):
    with gzip.open(path, "rt") as source:
        rows = {r[0]: r[1:] for r in csv.reader(source, delimiter="\t")
                if r and r[0] in ("!Sample_geo_accession", "!Sample_description", "!Sample_title")}
    names = [s.rsplit("[", 1)[0].strip() for s in rows["!Sample_title"]]
    return dict(zip(rows["!Sample_description"], zip(names, rows["!Sample_geo_accession"], strict=True), strict=True))


def write(path, fields, records):
    with path.open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(records)


def main(counts_path, matrix_path, out):
    out.mkdir(exist_ok=True, parents=True)
    meta = metadata(matrix_path)
    with gzip.open(counts_path, "rt") as stream:
        reader = csv.reader(stream, delimiter="\t")
        header = next(reader)
        ids = header[8:]
        assert len(set(ids)) == len(ids) == len(meta) == 227 and set(ids) == set(meta)
        genes, data = [], []
        for r in reader:
            genes.append(r[3])
            data.append(np.fromiter(map(int, r[8:]), dtype=np.int64, count=len(ids)))
    x = np.stack(data)
    assert (x >= 0).all()
    lookup = PRIMARY + COMPARATOR
    assert all(genes.count(g) == 1 for g in lookup)
    idx = [genes.index(g) for g in lookup]
    names = [meta[i][0] for i in ids]
    vehicle = np.array([i for i,n in enumerate(names) if n.startswith("Vehicle-")])
    drug = names.index("Ethosuximide")
    assert len(vehicle) == 9 and names.count("Ethosuximide") == 1
    same_block = [i for i, label in enumerate(ids) if label.split(".")[1] == ids[drug].split(".")[1] and i != drug]
    all_other = [i for i in range(len(ids)) if i not in vehicle and i != drug]
    totals = x.sum(axis=0)
    cpm = 1e6 * x[idx] / totals
    assert (np.median(cpm[:,vehicle],axis=1) >= 1).all()
    common = x[(x > 0).all(axis=1)]
    reference = np.exp(np.mean(np.log(common), axis=1))
    ratio = np.median(common / reference[:,None], axis=0)
    effective = ratio / np.median(ratio) * np.median(totals)
    gene_rows, screen_rows, sum_rows = [], [], []
    for method, denom in (("CPM",totals), ("median_ratio",effective)):
        y = np.log2(1 + 1e6 * x[idx] / denom)
        effects = np.empty_like(y)
        for i in range(len(ids)):
            controls = vehicle[vehicle != i]
            effects[:,i] = y[:,i] - np.median(y[:,controls],axis=1)
        primary = effects[:len(PRIMARY)].mean(axis=0)
        gap = primary - effects[len(PRIMARY):].mean(axis=0)
        number_up = (effects[:len(PRIMARY)] > 0).sum(axis=0)
        passed = number_up[drug] >= 3 and primary[drug] > 0 and gap[drug] > max(0, max(gap[vehicle]))
        sum_rows.append([method, primary[drug], gap[drug], number_up[drug], min(gap[vehicle]), max(gap[vehicle]),
                         sum(gap[all_other] < gap[drug]), len(all_other), sum(gap[same_block] < gap[drug]),len(same_block),bool(passed)])
        for k,g in enumerate(lookup):
            gene_rows.append([method,g,"primary" if g in PRIMARY else "comparator",x[idx[k],drug],np.median(cpm[k,vehicle]),effects[k,drug]])
        for i,k in enumerate(ids):
            screen_rows.append([method,meta[k][1],names[i],k,int(totals[i]),primary[i],gap[i],number_up[i]])
    write(out/"summary.tsv", ["normalization","primary","primary_minus_comparator","n_primary_up","vehicle_gap_min","vehicle_gap_max","n_other_drugs_below_gap","n_other_drugs","n_identifier_block_below_gap","n_identifier_block_others","pass"],sum_rows)
    write(out/"genes.tsv", ["normalization","symbol","panel","ethosuximide_counts","median_vehicle_cpm","log2_delta"],gene_rows)
    write(out/"screen.tsv", ["normalization","GSM","agent","library","total_gene_counts","primary","primary_minus_comparator","n_primary_up"],screen_rows)
    write(out/"sources.tsv", ["input","sha256"],[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in (counts_path,matrix_path)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    for argument in ("counts", "matrix", "out"):
        parser.add_argument(argument, type=Path)
    a = parser.parse_args()
    main(a.counts, a.matrix, a.out)
