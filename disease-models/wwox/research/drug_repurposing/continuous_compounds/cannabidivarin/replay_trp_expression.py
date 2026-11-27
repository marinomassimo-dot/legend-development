"""Recompute the prespecified CBDV-relevant transcript and cell-class checks."""
import argparse
import csv
from pathlib import Path
import sys


TARGETS = tuple("Trpv1 Trpv2 Trpa1 Trpv3 Gpr55".split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    compounds = args.drug_repurposing / "continuous_compounds"
    sys.path.insert(0, str(compounds / "copper_histidinate"))
    from replay_copper_comparison import verify

    sys.path.insert(0, str(compounds / "thiamine"))
    from cell_types import run as summarize_nuclei
    from screen import run as summarize_bulk

    manifest = args.drug_repurposing / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as handle:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(handle, delimiter="\t")}
    reference, = (args.files / "reference_ensembl_r92").glob("*.fa.gz")
    verify(reference, hashes)
    geo = args.files / "geo"
    for gse, pattern in [("GSE158681", "*TPM_Table.txt.gz"), ("GSE158682", "*TPM_Table.txt.gz"),
                         ("GSE156243", "*count_table.txt.gz")]:
        source, = (geo / gse).glob(pattern)
        verify(source, hashes)
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            verify(geo / "GSE158684" / f"GSE158684_{arm}_filtered_{suffix}", hashes)
    args.output.mkdir(parents=True, exist_ok=True)
    summarize_bulk(args.files, target_genes=TARGETS, output=args.output / "trp_bulk.tsv",
                   missing_value="NA")
    summarize_nuclei(args.files, genes=TARGETS, output_dir=args.output)


if __name__ == "__main__":
    main()
