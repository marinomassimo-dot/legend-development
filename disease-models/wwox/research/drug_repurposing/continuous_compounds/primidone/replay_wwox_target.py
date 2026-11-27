"""Replay target and steroid handling RNA coverage without treating unmapped as zero."""

import argparse
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
TARGETS = ("Trpm3", "Trpm1", "Sts", "Sult2b1", "Cyp11a1", "Abcc1")
BULK_HEADER = "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping"


def nuclear_rows(files, assigned_nuclei):
    for pool, cell_class, depth, genes in assigned_nuclei(files, [], [], TARGETS):
        denominator = int(depth.sum())
        for target in TARGETS:
            prefix = (pool, cell_class, target.upper(), len(depth), denominator)
            if target not in genes:
                yield (*prefix, "", "", "unmapped")
                continue
            count = int(genes[target].sum())
            yield (*prefix, count, f"{1e6 * count / denominator:.6g}", "mapped")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(HERE.parent / "jbpos0101"))
    from replay_exposure_and_receptors import bulk_panel, tsv, verified_expression
    from coagonist_screen import assigned_nuclei

    verified_expression(args.files)
    args.out.mkdir(parents=True, exist_ok=True)
    tsv(args.out / "wwox_bulk.tsv", BULK_HEADER.split(), bulk_panel(args.files, TARGETS))
    tsv(args.out / "wwox_nuclei.tsv", "pool class gene nuclei all_UMI gene_UMI CPM mapping".split(),
        nuclear_rows(args.files, assigned_nuclei))


if __name__ == "__main__":
    main()
