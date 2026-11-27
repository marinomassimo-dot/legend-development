"""Check whether WWOX expression supports a shared increase in precursor loss."""
import argparse
import csv
import gzip
from pathlib import Path
import sys

import numpy as np


GENES = ("Pank4", "Coasy", "Ppcs", "Ppcdc", "Crat", "Slc25a16", "Slc25a42")
RATIO = "PANK4_minus_COASY_log_expression"


def bulk_rows(files, models, verify, hashes, reference, load_target):
    ref, = (files / "reference_ensembl_r92").glob("*.fa.gz")
    verify(ref, hashes)
    transcript_map, _ = reference(files)
    with gzip.open(ref, "rt") as handle:
        coasy_transcripts = [line[1:].split(".")[0] for line in handle
                             if line.startswith(">") and " gene:ENSMUSG00000001755." in line]
    if not coasy_transcripts:
        raise ValueError("Missing mouse Coasy stable locus")
    transcript_map.update(dict.fromkeys(coasy_transcripts, "Coasy"))
    for accession, model, ctrl_prefix, ko_prefix, n_ctrl, n_ko in models:
        human = accession == "GSE156243"
        symbols = [gene.upper() if human else gene for gene in GENES]
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (files / "geo" / accession).glob(pattern)
        verify(source, hashes)
        names, measured = load_target(source, symbols, None if human else transcript_map)
        ctrl = [i for i, name in enumerate(names) if name.startswith(ctrl_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert (len(ctrl), len(ko)) == (n_ctrl, n_ko)
        expr = {gene.upper(): np.log2(1 + measured[gene]) for gene in symbols}
        expr[RATIO] = expr["PANK4"] - expr["COASY"]
        for measure, score in expr.items():
            def contrast(omit):
                return score[[i for i in ko if i != omit]].mean() - score[[i for i in ctrl if i != omit]].mean()

            sensitivity = [contrast(i) for i in ctrl + ko]
            yield (accession, model, n_ctrl, n_ko, "CPM" if human else "TPM", measure,
                   score[ctrl].mean(), score[ko].mean(), contrast(None), min(sensitivity), max(sensitivity))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.drug_repurposing / "continuous_compounds" / "copper_histidinate"))
    from replay_copper_comparison import MODELS, load_target, reference, verify

    sys.path.insert(0, str(args.drug_repurposing / "continuous_compounds" / "thiamine"))
    from cell_types import run as run_nuclear_assignment

    manifest = args.drug_repurposing / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as handle:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(handle, delimiter="\t")}
    args.output.mkdir(parents=True, exist_ok=True)
    with (args.output / "bulk_partition.tsv").open("w") as handle:
        out = csv.writer(handle, delimiter="\t", lineterminator="\n")
        out.writerow(("accession", "preparation", "WT_libraries", "KO_libraries", "abundance_unit", "gene_or_contrast",
                      "WT_mean_log", "KO_mean_log", "KO_minus_WT", "LOO_min", "LOO_max"))
        for row in bulk_rows(args.files, MODELS, verify, hashes, reference, load_target):
            out.writerow((*row[:6], *(f"{value:.6f}" for value in row[6:])))
    nuclei = args.files / "geo" / "GSE158684"
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            verify(nuclei / f"GSE158684_{arm}_filtered_{suffix}", hashes)
    run_nuclear_assignment(args.files, genes=GENES, output_dir=args.output)


if __name__ == "__main__":
    main()
