"""Sensitivity analysis using the deposited hg38 CAGE consensus clusters."""
import argparse
from bisect import bisect_left, bisect_right
from collections import defaultdict
import csv
import gzip
import hashlib
from pathlib import Path

import numpy as np

from analyze import GENES, PANELS, write_tsv


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("clusters", type=Path)
    parser.add_argument("refseq", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    by_locus = defaultdict(set)
    with gzip.open(args.refseq, "rt") as f:
        for record in csv.reader(f, delimiter="\t"):
            chrom, strand, start, end = record[2:6]
            tss = int(start) + 1 if strand == "+" else int(end)
            by_locus[chrom, strand].add((tss, record[12]))
    refs = {loc: sorted(entries) for loc, entries in by_locus.items()}
    coords = {loc: [pos for pos, gene in entries] for loc, entries in refs.items()}
    measures = ["hNSC", "hNSC_WWOX_del", "neurons", "neurons_WWOX_del"]
    clusters = {}
    prefix = "cage1_cCl_grange."
    with gzip.open(args.clusters, "rt") as f:
        for r in csv.DictReader(f):
            key = (r[prefix+"seqnames"], r[prefix+"strand"], int(r[prefix+"start"]), int(r[prefix+"end"]))
            values = np.array([float(r[k]) for k in measures])
            if key in clusters and not np.array_equal(values, clusters[key]):
                raise ValueError(f"Conflicting duplicate cluster: {key}")
            clusters[key] = values
    library_size = np.rint(1e6 / np.min(np.where(np.array(list(clusters.values())) > 0,
                                         np.array(list(clusters.values())), np.inf), axis=0))
    gene_rows, panel_rows, assignments = [], [], []
    for window in (100, 500):
        gene_values = {}
        for (chrom, strand, start, end), values in clusters.items():
            pos = coords.get((chrom, strand), [])
            candidates = refs.get((chrom, strand), [])[bisect_left(pos, start-window):bisect_right(pos, end+window)]
            genes = {g for _, g in candidates}
            if len(genes) == 1 and genes <= GENES:
                gene, = genes
                gene_values[gene] = gene_values.get(gene, 0) + values
                assignments.append([window, gene, chrom, strand, start, end, *values])
        for stage, c, k in [("precursor", 0, 1), ("differentiated", 2, 3)]:
            scores = {}
            for panel, members in PANELS.items():
                usable = []
                for gene in members:
                    if gene not in gene_values:
                        gene_rows.append([window, stage, panel, gene, "unmapped", *(["NA"] * 5)])
                        continue
                    v = gene_values[gene]
                    n = v * library_size / 1e6
                    assert np.max(abs(n - np.rint(n))) < 1e-5
                    ok = min(n[c], n[k]) >= 9.99999
                    delta = np.log2(1 + v[k]) - np.log2(1 + v[c])
                    gene_rows.append([window, stage, panel, gene, "usable" if ok else "low_counts",
                                      v[c], v[k], round(n[c]), round(n[k]), delta])
                    if ok:
                        usable.append(delta)
                if len(usable) >= len(members) - 1:
                    scores[panel] = np.mean(usable)
                panel_rows.append([window, stage, panel, len(usable), len(members),
                                   sum(d < 0 for d in usable), scores.get(panel, "NA")])
            d = scores["primary"] - scores["comparator"] if {"primary", "comparator"} <= scores.keys() else "NA"
            panel_rows.append([window, stage, "primary_minus_comparator", "NA", "NA", "NA", d])
    write_tsv(args.out/"promoter_panels.tsv", "window_bp stage panel usable total negative delta", panel_rows)
    write_tsv(args.out/"promoter_genes.tsv", "window_bp stage panel gene coverage ctrl_TPM loss_TPM ctrl_tags loss_tags delta", gene_rows)
    write_tsv(args.out/"promoter_assignments.tsv", "window_bp gene chrom strand start end " + " ".join(measures), assignments)
    with (args.out/"promoter_inputs.sha256").open("w") as out:
        for path in (args.clusters, args.refseq):
            print(hashlib.sha256(path.read_bytes()).hexdigest(), path.name, sep="  ", file=out)


if __name__ == "__main__":
    main()
