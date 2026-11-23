"""Cross-check neural progenitor T-type channel RNA across three independent human sources."""
import argparse
import csv
import gzip
import hashlib
from collections import defaultdict
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ganaxolone_20261123"))
from analyze import load_target, tsv

GENES = {"CACNA1G", "CACNA1H", "CACNA1I", "DCX", "SOX2", "WWOX"}


def analyze_sorted(matrix, out):
    with gzip.open(matrix, "rt") as file:
        reader = csv.reader(file, delimiter="\t")
        groups = [v.split("_")[1] for v in next(reader)[1:-1]]
        rows = []
        for _, *data, gene in reader:
            if gene in GENES:
                for group in sorted(set(groups)):
                    v = np.array([float(x) for x, label in zip(data, groups, strict=True) if label == group])
                    rows.append([gene, group, len(v), v.min(), np.median(v), v.max(),
                                 *[int(sum(v >= f)) for f in (0.1, 1, 5)]])
    assert len(rows) == len(GENES) * len(set(groups))
    tsv(out/"sorted.tsv", "gene class n min median max ge0.1 ge1 ge5".split(), rows)


def analyze_single(matrix, metadata, out):
    with metadata.open() as stream:
        meta = {r["Cell"]: r for r in csv.DictReader(stream, delimiter="\t")}
    rg = {"vRG", "RG-div1", "RG-div2"}
    lineage = {"IPC-nEN1", "IPC-nEN2", "IPC-nEN3", "nEN-early1", "nEN-early2"}
    with gzip.open(matrix, "rt") as file:
        cells = file.readline().rstrip().split("\t")[1:]
        assert set(cells) == set(meta) and len(cells) == len(meta)
        groups = defaultdict(lambda: defaultdict(list))
        for i, cell in enumerate(cells):
            row = meta[cell]
            cluster = row["WGCNAcluster"]
            if row["RegionName"] == "Cortex" and 10 <= float(row["Age_in_Weeks"]) <= 20 and cluster in rg | lineage:
                groups[row["Name"]]["RG" if cluster in rg else "transition"].append(i)
        matched = {k:v for k,v in groups.items() if min(len(v["RG"]), len(v["transition"])) >= 5}
        individual, stats = [], []
        for line in file:
            label, data = line.rstrip().split("\t", 1)
            g = label.split("|")[-1]
            if g not in GENES:
                continue
            vec = np.fromstring(data, sep="\t")
            assert len(vec) == len(cells)
            for floor, mask in (("positive", vec>0), ("ge1", vec>=1)):
                rates = []
                for sample, indices in sorted(matched.items()):
                    fr = []
                    for key in ("RG", "transition"):
                        selected = mask[indices[key]]
                        individual.append([g, floor, sample, key, len(selected), sum(selected), selected.mean()])
                        fr.append(selected.mean())
                    rates.append(fr)
                r, n = np.asarray(rates).T
                stats.append([g, floor, len(r), np.median(r), np.median(n), np.median(n-r), sum(n>r), sum(n<r)])
    assert len(stats) == 2*len(GENES)
    tsv(out/"atlas_samples.tsv", "gene floor sample class cells detected fraction".split(), individual)
    tsv(out/"atlas_summary.tsv", "gene floor matched_groups median_RG median_transition median_paired_diff positive negative".split(), stats)


def analyze_organoid(matrix, out):
    labels, counts = load_target(matrix, GENES)
    assert set(counts) == GENES
    ko = [i for i,k in enumerate(labels) if k.lower().startswith("cko")]
    wt = [i for i,k in enumerate(labels) if k.lower().startswith("cwt")]
    assert len(ko) == 4 and len(wt) == 2
    rows = []
    for g, cpm in sorted(counts.items()):
        expr = np.log2(1 + cpm)
        def delta(exclude):
            return np.mean([expr[i] for i in ko if i!=exclude]) - np.mean([expr[i] for i in wt if i!=exclude])
        loo = [delta(i) for i in ko+wt]
        rows.append([g, *cpm, delta(None), min(loo), max(loo)])
    tsv(out/"organoid.tsv", ["gene", *labels, "KO_minus_WT", "omit_min", "omit_max"], rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("sorted", "matrix", "meta", "organoid", "out"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    analyze_sorted(args.sorted, args.out)
    analyze_single(args.matrix, args.meta, args.out)
    analyze_organoid(args.organoid, args.out)
    paths = (args.sorted, args.matrix, args.meta, args.organoid)
    tsv(args.out/"sources.tsv", ["filename", "sha256"], ([p.name, hashlib.sha256(p.read_bytes()).hexdigest()] for p in paths))


if __name__ == "__main__":
    main()
