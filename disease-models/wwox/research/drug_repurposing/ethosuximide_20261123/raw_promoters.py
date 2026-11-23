"""Recount public strand-specific CAGE BED files with assembly calibration."""
import argparse
from bisect import bisect_right
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
import csv
import gzip
import hashlib
from pathlib import Path
from statistics import median

import numpy as np

from analyze import GENES, PANELS, write_tsv


def unique_intervals(refseq, width, wanted):
    # For every expressed target, exclude overlaps with all other annotated
    # genes on its strand, including genes outside the requested panels.
    events = defaultdict(lambda: defaultdict(Counter))
    with gzip.open(refseq, "rt") as f:
        for record in csv.reader(f, delimiter="\t"):
            chrom, strand, start, end = record[2:6]
            tss = int(start) if strand == "+" else int(end) - 1
            changes = events[chrom.encode(), strand.encode()]
            changes[max(0, tss-width)][record[12]] += 1
            changes[tss+width+1][record[12]] -= 1
    out = {}
    for locus, changes in events.items():
        starts, ends, genes = [], [], []
        active = Counter()
        for pos in sorted(changes):
            if len(active) == 1:
                g, = active
                if g in wanted:
                    starts.append(prev)
                    ends.append(pos)
                    genes.append(g)
            for gene, change in changes[pos].items():
                active[gene] += change
                if active[gene] == 0:
                    del active[gene]
            prev = pos
        if starts:
            out[locus] = (starts, ends, genes)
    return out


def count_library(path, regions):
    bins = defaultdict(list)
    for key, loci in regions.items():
        for locus, (starts, ends, genes) in loci.items():
            covered = {b for x, y in zip(starts, ends) for b in range(x >> 12, ((y-1) >> 12)+1)}
            for b in covered:
                bins[locus + (b,)].append((key, starts, ends, genes))
    counts = defaultdict(Counter)
    chromosomes = Counter()
    malformed = 0
    with gzip.open(path, "rb") as f:
        for line in f:
            fields = line.rstrip().split(b"\t")
            if len(fields) != 6 or fields[-1] not in {b"+", b"-"}:
                malformed += 1
                continue
            chrom, start, end, _, _, strand = fields
            chromosomes[chrom] += 1
            pos = int(start) if strand == b"+" else int(end) - 1
            for key, starts, ends, genes in bins.get((chrom, strand, pos >> 12), ()):
                i = bisect_right(starts, pos)-1
                if i >= 0 and pos < ends[i]:
                    counts[key][genes[i]] += 1
    return sum(chromosomes.values()), dict(counts), chromosomes, malformed


def ranks(vector):
    unique, ix, counts = np.unique(vector, return_inverse=True, return_counts=True)
    return (np.cumsum(counts) - 0.5 * (counts - 1))[ix]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("geo", "beds", "hg19", "hg38", "out"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    table, = args.geo.glob("*all_genes_all_samples_merged.txt.gz")
    with gzip.open(table, "rt") as f:
        rows = csv.DictReader(f, delimiter="\t")
        arms = ["hNSC", "hNSC_WWOX_del", "Neurons", "Neurons_WWOX_del"]
        deposited = {r["Gene"]: [float(r[c]) for c in arms] for r in rows}
    eligible = sorted(g for g, vals in deposited.items() if g not in GENES and min(vals) >= 3)
    controls = [eligible[i] for i in np.linspace(0, len(eligible)-1, 120, dtype=int)]
    regions = {(a, w): unique_intervals(ref, w, GENES.union(controls))
               for a, ref in [("hg19", args.hg19), ("hg38", args.hg38)] for w in (100, 500)}
    input_beds = [next(args.beds.glob(f"GSM35909{i}_*.bed.gz")) for i in range(48, 52)]
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(count_library, p, regions) for p in input_beds]
        library = [f.result() for f in futures]
    sizes = np.array([v[0] for v in library])
    write_tsv(args.out/"raw_chromosomes.tsv", "library chromosome records",
              [(arm, chrom.decode(), n) for arm, lib in zip(arms, library) for chrom, n in sorted(lib[2].items())]
              + [(arm, "malformed", lib[3]) for arm, lib in zip(arms, library)])
    # Infer the deposited tag totals from the complete table of mapped clusters.
    clusters, = args.geo.glob("*F5mapped.txt.gz")
    with gzip.open(clusters, "rt") as src:
        records = csv.DictReader(src)
        values = np.array([[float(r[a.replace("Neurons", "neurons")]) for a in arms] for r in records])
    inferred = np.rint(1e6 / np.min(np.where(values > 0, values, np.inf), axis=0))
    assert np.max(abs(values * inferred/1e6 - np.rint(values * inferred/1e6))) < 1e-5
    check, rhos = [], defaultdict(list)
    for k in regions:
        for i, arm in enumerate(arms):
            count = library[i][1].get(k, {})
            rho = np.corrcoef(ranks([count.get(g, 0) for g in controls]),
                              ranks([deposited[g][i] for g in controls]))[0, 1]
            check.append([*k, arm, rho, sum(count.get(g, 0) > 0 for g in controls), sizes[i], int(inferred[i])])
            if k[1] == 100:
                rhos[k[0]].append(rho)
    write_tsv(args.out/"raw_calibration.tsv", "assembly width library spearman detectable_of_120 reads inferred_tags", check)
    write_tsv(args.out/"raw_calibrators.tsv", "gene", [(g,) for g in controls])
    with (args.out/"raw_inputs.sha256").open("w") as out:
        for path in [*input_beds, args.hg19, args.hg38]:
            digest = hashlib.sha256()
            with path.open("rb") as f:
                for block in iter(lambda: f.read(1048576), b""):
                    digest.update(block)
            print(digest.hexdigest(), path.name, sep="  ", file=out)
    first, second = sorted(rhos, key=lambda a: median(rhos[a]), reverse=True)
    if median(rhos[first]) <= 0.6 or median(rhos[first]) - median(rhos[second]) <= 0.2:
        raise ValueError(f"Unresolved reference build: {rhos}")
    gene_rows, panel_rows = [], []
    for width in (100, 500):
        k = first, width
        for norm, totals in [("BED", sizes), ("deposited", inferred)]:
            for stage, c, t in [("precursor", 0, 1), ("differentiated", 2, 3)]:
                scores = {}
                for panel, members in PANELS.items():
                    ds = []
                    for g in members:
                        n1, n2 = [library[i][1].get(k, {}).get(g, 0) for i in (c, t)]
                        d = np.log2(1 + 1e6 * n2 / totals[t]) - np.log2(1 + 1e6 * n1 / totals[c])
                        ok = min(n1, n2) >= 10
                        gene_rows.append([*k, norm, stage, panel, g, n1, n2, int(ok), d])
                        if ok:
                            ds.append(d)
                    if len(ds) >= len(members)-1:
                        scores[panel] = np.mean(ds)
                    panel_rows.append([*k, norm, stage, panel, len(ds), sum(d < 0 for d in ds), scores.get(panel, "NA")])
                relative = scores["primary"]-scores["comparator"] if {"primary","comparator"} <= scores.keys() else "NA"
                panel_rows.append([*k, norm, stage, "primary_minus_comparator", "NA", "NA", relative])
    write_tsv(args.out/"raw_genes.tsv", "assembly width norm stage panel gene ctrl_tags loss_tags usable delta", gene_rows)
    write_tsv(args.out/"raw_panels.tsv", "assembly width norm stage panel usable negative delta", panel_rows)


if __name__ == "__main__":
    main()
