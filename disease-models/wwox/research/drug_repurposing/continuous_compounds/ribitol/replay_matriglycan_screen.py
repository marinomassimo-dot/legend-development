"""Screen the held neural RNA datasets for the ribitol-to-matriglycan pathway."""

import argparse
import csv
import gzip
import hashlib
from math import log2
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent / "jbpos0101")]
from replay_exposure_and_receptors import bulk_panel, tsv, verified_expression

CAGE_NAME = "GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz"
CAGE_SHA256 = "7e51e3cffa7491a7778a23516fd6e8bbe601b62cb5223536885a401219a392c2"
GENES = {
    "donor": ("Crppa", "Fggy"),
    "golgi_delivery": ("Slc35a1", "Slc35a4"),
    "phosphoribitol_transfer": ("Fktn", "Fkrp"),
    "upstream_acceptor": ("Pomt1", "Pomt2", "Pomgnt2", "B3galnt2", "Pomk"),
    "extension": ("Rxylt1", "B4gat1", "Large1"),
    "receptor_and_matrix": ("Dag1", "Lama1", "Lama2", "Col4a1", "Hspg2"),
    "lineage_context": ("Pax6", "Sox2", "Eomes", "Myc"),
}
ALIASES = {
    "Crppa": ("Ispd",),
    "Rxylt1": ("Tmem5",),
    "Large1": ("Large",),
    "B4gat1": ("B3gnt1",),
}


def ordered_symbols():
    for category, genes in GENES.items():
        for gene in genes:
            yield category, gene, (gene, *ALIASES.get(gene, ()))


def bulk_rows(files):
    symbol_groups = tuple(ordered_symbols())
    aliases = tuple(alias for _, _, candidates in symbol_groups for alias in candidates)
    models = {}
    for model, accession, symbol, *values in bulk_panel(files, aliases):
        models.setdefault((model, accession), {})[symbol] = values
    for (model, accession), results in models.items():
        for category, gene, candidates in symbol_groups:
            mapped = next((alias.upper() for alias in candidates
                           if results[alias.upper()][-1] == "mapped"), None)
            if mapped is None:
                yield (model, accession, category, gene.upper(), "", *results[gene.upper()])
            else:
                yield (model, accession, category, gene.upper(), mapped, *results[mapped])


def cage_rows(files):
    path = files / "geo" / "GSE126075" / CAGE_NAME
    if hashlib.sha256(path.read_bytes()).hexdigest() != CAGE_SHA256:
        raise ValueError("CAGE TPM input differs from the held snapshot.")
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        rows = {row["Gene"]: row for row in csv.DictReader(stream, delimiter="\t")}
    for cell, control, depletion in (
        ("progenitor", "hNSC", "hNSC_WWOX_del"),
        ("differentiated", "Neurons", "Neurons_WWOX_del"),
    ):
        for category, gene, aliases in ordered_symbols():
            mapped = next((symbol.upper() for symbol in aliases if symbol.upper() in rows), None)
            if mapped is None:
                yield cell, category, gene.upper(), "", 1, 1, "", "", "", "unmapped"
                continue
            control_value, depleted_value = (float(rows[mapped][column]) for column in (control, depletion))
            delta = log2(1 + depleted_value) - log2(1 + control_value)
            yield (cell, category, gene.upper(), mapped, 1, 1, f"{control_value:.6g}",
                   f"{depleted_value:.6g}", f"{delta:.6g}", "mapped")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    verified_expression(args.files)
    args.out.mkdir(parents=True, exist_ok=True)
    tsv(args.out / "bulk_matriglycan.tsv",
        "model accession category gene mapped_symbol ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_rows(args.files))
    tsv(args.out / "cage_matriglycan.tsv",
        "stage category gene mapped_symbol ctrl_n ko_n ctrl_TPM depletion_TPM log2_delta mapping".split(),
        cage_rows(args.files))


if __name__ == "__main__":
    main()
