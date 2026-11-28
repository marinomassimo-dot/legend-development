"""Replay the WWOX oxysterol-pathway expression comparisons."""

import argparse
import csv
from itertools import chain
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "clemizole"))
from replay_receptors_and_exposure import bulk_panel, formatted, verified_expression

PANEL = ("Cyp46a1", "Ch25h", "Cyp27a1", "Sqle", "Abca1")


def main(files):
    verified_expression(files)
    print(
        "model\taccession\tgene\tctrl_n\tko_n\tctrl_positive\tko_positive\t"
        "ctrl_mean\tko_mean\tlog2_delta\tomit_min\tomit_max\tmapping"
    )
    for row in formatted(bulk_panel(files, PANEL)):
        print("\t".join(map(str, row)))


def regional_alleles(files, output):
    sys.path.insert(0, str(COMPOUNDS / "celecoxib"))
    from replay_comparison import adult_p47t, juvenile_and_organoid, write_tsv

    manifest = COMPOUNDS.parent / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as stream:
        expected = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    header = ("accession", "model", "gene", "unit", "ctrl_n", "ko_n", "delta_log2",
              "omit_min", "omit_max", "omit_activity_high")
    comparisons = chain(juvenile_and_organoid(files, expected, PANEL),
                        adult_p47t(files, expected, PANEL))
    write_tsv(output, header, comparisons)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="Shared checkout's files directory")
    parser.add_argument("--regional-alleles", type=Path, metavar="TSV",
                        help="Write the extended regional and allelic comparison to this path")
    args = parser.parse_args()
    if args.regional_alleles is None:
        main(args.files)
    else:
        regional_alleles(args.files, args.regional_alleles)
