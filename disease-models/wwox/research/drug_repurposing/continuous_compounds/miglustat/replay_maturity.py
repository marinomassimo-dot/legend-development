"""Replay pooled class weights and the maturity-band sensitivity analysis."""

import argparse
import csv
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "ganaxolone_20261123"))
from analyze import assigned_nuclei, tsv


MATURE_MARKERS = ("Klk6", "Apod", "Pmp22", "Slc5a11", "Ermn", "Hapln2")
MATURITY_TARGETS = ("Ugt8a", "Gal3st1")
COMPOSITION_TARGETS = ("UGCG", "GBA2", "UGT8A", "GAL3ST1")


def maturity_rows(files):
    samples = {}
    for arm, cell_class, depth, counts in assigned_nuclei(files, [], [], (*MATURITY_TARGETS, *MATURE_MARKERS)):
        if cell_class == "MOL":
            score = np.mean([np.log2(1 + counts[gene] * 1e6 / depth) for gene in MATURE_MARKERS], axis=0)
            samples[arm] = depth, score, counts
    cuts = np.quantile(np.concatenate([sample[1] for sample in samples.values()]), [1 / 3, 2 / 3])
    for arm, (depth, score, counts) in samples.items():
        bands = np.digitize(score, cuts)
        for index in range(3):
            selected = bands == index
            pooled_depth = depth[selected].sum()
            for gene in MATURITY_TARGETS:
                molecules = counts[gene][selected]
                yield (
                    arm, index + 1, gene, int(selected.sum()), round(float(score[selected].mean()), 5),
                    round(float(np.median(depth[selected])), 1), int(pooled_depth), int(molecules.sum()),
                    round(float(1e6 * molecules.sum() / pooled_depth), 5), int(np.count_nonzero(molecules)),
                )


def pooled_differences(nuclei_path):
    with nuclei_path.open(encoding="utf-8", newline="") as sample:
        rows = list(csv.DictReader(sample, delimiter="\t"))
    for gene in COMPOSITION_TARGETS:
        groups = {
            (row["pool"], row["cell_class"]): (int(row["all_UMI"]), int(row["gene_UMI"]))
            for row in rows if row["gene"] == gene
        }
        classes = sorted({cell for _, cell in groups})
        totals = {arm: sum(groups[arm, cell][0] for cell in classes) for arm in ("ctrl", "ko")}
        pooled = {
            arm: 1e6 * sum(groups[arm, cell][1] for cell in classes) / depth
            for arm, depth in totals.items()
        }
        within = mixture = 0.0
        for cell in classes:
            ctrl_depth, ctrl_count = groups["ctrl", cell]
            ko_depth, ko_count = groups["ko", cell]
            ctrl_weight, ko_weight = ctrl_depth / totals["ctrl"], ko_depth / totals["ko"]
            ctrl_cpm, ko_cpm = 1e6 * ctrl_count / ctrl_depth, 1e6 * ko_count / ko_depth
            within += (ko_cpm - ctrl_cpm) * (ctrl_weight + ko_weight) / 2
            mixture += (ko_weight - ctrl_weight) * (ctrl_cpm + ko_cpm) / 2
        delta = pooled["ko"] - pooled["ctrl"]
        if not np.isclose(delta, within + mixture):
            raise ValueError(f"Class decomposition failed for {gene}")
        yield (gene, *(f"{value:.6f}" for value in (pooled["ctrl"], pooled["ko"], delta, within, mixture)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    columns = "pool tertile gene cells mean_score median_depth pooled_depth UMI CPM detected_cells".split()
    tsv(args.output / "maturity_strata.tsv", columns, maturity_rows(args.files))
    columns = "gene ctrl_CPM ko_CPM difference within_class class_weights".split()
    tsv(args.output / "composition.tsv", columns, pooled_differences(HERE / "nuclei.tsv"))


if __name__ == "__main__":
    main()
