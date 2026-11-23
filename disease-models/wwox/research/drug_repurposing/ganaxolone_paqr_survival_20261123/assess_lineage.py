"""Reproduce the targeted expression checks and graphical medians using public inputs."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
import sys
import numpy as np
import pymupdf

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ganaxolone_20261123"))
from analyze import load_target, tsv  # upstream public-matrix loader


GENES = {"PAQR6", "PAQR7", "PAQR8", "SOX2", "PROM1", "DCX", "WWOX"}


def profile(matrix_path, zone_path, organoid):
    records, ensembl = [], {}
    with gzip.open(matrix_path, "rt") as source:
        reader = csv.reader(source, delimiter="\t")
        labels = next(reader)[1:-1]
        for gene_id, *values, symbol in reader:
            if symbol in GENES:
                assert gene_id not in ensembl and symbol not in ensembl.values()
                ensembl[gene_id] = symbol
                for label, value in zip(labels, values, strict=True):
                    records.append(("GSE65000", label, label.split("_")[1], symbol, float(value)))
    assert set(ensembl.values()) == GENES
    with gzip.open(zone_path, "rt") as source:
        reader = csv.reader(source, delimiter="\t")
        labels = next(reader)[1:]
        for gene_id, *values in reader:
            if gene_id in ensembl:
                for label, value in zip(labels, values, strict=True):
                    records.append(("GSE38805", label, label.rsplit("_", 1)[1], ensembl[gene_id], float(value) if value != "NA" else None))
    labels, data = load_target(organoid, GENES)
    for symbol in sorted(GENES):
        for label, value in zip(labels, data[symbol], strict=True):
            records.append(("GSE156243", label, label[:3], symbol, value))
    return records


def figure_medians(path):
    # Three box boundaries per color: Q3, median and Q1. Whiskers are narrower.
    image = pymupdf.Pixmap(str(path))
    assert (image.width, image.height) == (614, 886)
    pixels = np.asarray(image.samples_mv).reshape(image.height, image.width, image.n)
    for name, lo, hi in (("WT", 436, 453), ("KO", 458, 475), ("W-AAV", 480, 497)):
        red, green, blue = pixels[690:831, lo:hi, :3].transpose(2, 0, 1).astype(int)
        masks = {"WT": (blue - red > 45) & (blue - green > 45),
                 "KO": (red - blue > 45) & (red - green > 45),
                 "W-AAV": (blue - green > 35) & (red - green > 35)}
        lines = np.where(masks[name].sum(axis=1) >= 12)[0] + 690
        groups = np.split(lines, np.where(np.diff(lines) > 1)[0] + 1)
        assert len(groups) == 3
        median = np.mean(groups[1])
        # Axis at rows 848 (0%) and 646 (50%).
        yield name, median, (848 - median) * 50 / 202


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("florio", "fietz", "organoid", "ev2", "out"):
        parser.add_argument(name, type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    records = profile(args.florio, args.fietz, args.organoid)
    groups = {}
    for series, sample, group, gene, value in records:
        groups.setdefault((series, group, gene), []).append(value)
    tsv(args.out / "target_values.tsv", ["study", "sample", "group", "gene", "FPKM_or_organoid_CPM"], records)
    summaries = []
    for key, values in sorted(groups.items()):
        arr = np.array([v for v in values if v is not None])
        summaries.append([*key, len(values), len(arr), arr.min() if arr.size else "NA",
                          np.median(arr) if arr.size else "NA", arr.max() if arr.size else "NA",
                          sum(arr >= 0.1), sum(arr >= 1), sum(arr >= 5)])
    tsv(args.out / "summary.tsv", "study group gene n_total n_observed min median max ge0.1 ge1 ge5".split(), summaries)
    matched = {}
    for series, sample, group, gene, value in records:
        if series == "GSE38805":
            matched.setdefault((sample.rsplit("_", 1)[0], gene), {})[group] = value
    tsv(args.out / "paired_regions.tsv", ["specimen", "gene", "VZ_minus_CP_log2plus1"],
        ([*key, np.log2(1 + val["VZ"]) - np.log2(1 + val["CP"])
          if val["CP"] is not None and val["VZ"] is not None else "NA"] for key, val in sorted(matched.items())))
    tsv(args.out / "figure_EV2H.tsv", ["group", "median_row", "approximate_percent"], figure_medians(args.ev2))
    tsv(args.out / "inputs.tsv", ["input", "sha256"], ([p.name, hashlib.sha256(p.read_bytes()).hexdigest()]
        for p in (args.florio, args.fietz, args.organoid, args.ev2)))


if __name__ == "__main__":
    main()
