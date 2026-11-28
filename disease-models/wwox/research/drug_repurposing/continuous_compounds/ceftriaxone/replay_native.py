"""Check whether the astrocytic Slc1a2 direction depends on its own assignment marker."""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
MODULE = HERE.parents[1]
sys.path.insert(0, str(MODULE / "ganaxolone_20261123"))
sys.path.insert(0, str(HERE.parent / "copper_histidinate"))
from analyze import assigned_nuclei, tsv
from replay_copper_comparison import verify

TARGETS = ("Slc1a2", "Slc1a3", "Slc7a11", "Atp1a2", "Glul", "Aqp4", "Aldh1l1")


def main(files, output):
    import csv

    with (MODULE / "memantine_magnesium_20261123" / "inputs.tsv").open() as handle:
        digests = {row["input"]: row["sha256"] for row in csv.DictReader(handle, delimiter="\t")}
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            path = files / "geo" / "GSE158684" / f"GSE158684_{arm}_filtered_{suffix}"
            verify(path, digests)
    rows = []
    for method, excluded in (("original", ()), ("without_Slc1a2", ("Slc1a2",))):
        for arm, label, depth, counts in assigned_nuclei(files, [], [], TARGETS, exclude_markers=excluded):
            if label != "astro":
                continue
            for group, keep in (
                ("assigned", depth > 0),
                ("assigned_and_independent_double_positive", (counts["Aqp4"] > 0) & (counts["Aldh1l1"] > 0)),
            ):
                denominator = int(depth[keep].sum())
                for gene in TARGETS:
                    count = int(counts[gene][keep].sum())
                    rows.append((method, group, arm, gene, int(keep.sum()), denominator,
                                 count, f"{1e6 * count / denominator:.3f}"))
    output.mkdir(parents=True, exist_ok=True)
    tsv(output / "astrocyte_marker_sensitivity.tsv",
        "classifier subset pool gene nuclei total_UMI gene_UMI gene_CPM".split(), rows)


if __name__ == "__main__":
    _, files, output = sys.argv
    main(Path(files), Path(output))
