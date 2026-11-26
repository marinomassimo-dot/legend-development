"""Replay the prespecified WWOX glucosylceramide and myelin context panel."""

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sodium_benzoate"))
from coagonist_screen import bulk_panel, nuclei_panel, tsv


PANEL = (
    "Ugcg", "Gba", "Scarb2", "Gba2", "B4galt5", "B4galt6",
    "St3gal5", "Ugt8a", "Gal3st1", "Sgms1", "Psap",
)


def bulk_lipid_panel(files):
    # The held annotations call the same galactosyltransferase Ugt8a in mouse and UGT8 in human.
    for row in bulk_panel(files, (*PANEL, "Ugt8")):
        model, _, gene, *_ = row
        other_species_symbol = "UGT8A" if model == "human_organoid" else "UGT8"
        if gene != other_species_symbol:
            yield row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    bulk_columns = (
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean "
        "ko_mean log2_delta omit_min omit_max mapping"
    ).split()
    tsv(args.output / "contrasts.tsv", bulk_columns, bulk_lipid_panel(args.files))
    nuclei_columns = "pool cell_class gene nuclei all_UMI gene_UMI CPM".split()
    tsv(args.output / "nuclei.tsv", nuclei_columns, nuclei_panel(args.files, PANEL))


if __name__ == "__main__":
    main()
