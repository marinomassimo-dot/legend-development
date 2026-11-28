#!/usr/bin/env python3
"""Replay a descriptive set of PS synthesis, transfer and leaflet RNA contrasts."""

import argparse
import csv
import gzip
import math
from pathlib import Path
import re
from statistics import mean

GENES = ("PTDSS1", "PTDSS2", "OSBPL5", "OSBPL8", "PRELID3B", "PISD", "PCYT2", "ANO6", "XKR8", "ATP8A2")
NUCLEI = (
    "advisor_pilot_20261113/brainstorm_20261116/"
    "adv099_neuron_discovery_sci_20261120/out"
)


def read_rows(path):
    with gzip.open(path, "rt") as source:
        yield from csv.DictReader(source, delimiter="\t")


def collect_mouse(files, filename, numerator, denominator, transcript_to_gene):
    grouped = {}
    for row in read_rows(files / "geo" / filename):
        gene = transcript_to_gene.get(row["Name"].split(".")[0])
        if gene is None:
            continue
        sample_values = grouped.setdefault(gene, [0.0] * (len(numerator) + len(denominator)))
        for index, column in enumerate(numerator + denominator):
            sample_values[index] += float(row[column])
    return {
        gene: (values[: len(numerator)], values[len(numerator):])
        for gene, values in grouped.items()
    }


def collect_human(files, numerator, denominator):
    totals = dict.fromkeys(numerator + denominator, 0.0)
    grouped = {}
    for row in read_rows(files / "geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz"):
        gene = row["gene"]
        values = [float(row[column]) for column in totals]
        for column, value in zip(totals, values):
            totals[column] += value
        if gene in GENES:
            if gene in grouped:
                raise ValueError(f"Duplicate target gene {gene}")
            grouped[gene] = values
    for gene, values in grouped.items():
        cpm = [value * 1_000_000 / totals[column] for column, value in zip(totals, values)]
        yield gene, (cpm[: len(numerator)], cpm[len(numerator):])


def emit_bulk(series, unit, data, n_ko, n_control):
    for gene in GENES:
        if gene not in data:
            print(f"{series}\t{gene}\t{n_ko}\t{n_control}\t{unit}\tNA\tNA\tNA\tNA\tNA")
            continue
        ko, control = data[gene]
        effect = mean(map(math.log2, [x + 1 for x in ko])) - mean(map(math.log2, [x + 1 for x in control]))
        extremes = [math.log2((a + 1) / (b + 1)) for a in ko for b in control]
        print(f"{series}\t{gene}\t{n_ko}\t{n_control}\t{unit}\t{mean(ko):.3f}\t{mean(control):.3f}\t{effect:.3f}\t{min(extremes):.3f}\t{max(extremes):.3f}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="LEGEND files directory containing obtained GEO inputs")
    options = parser.parse_args()
    files = options.files
    transcript_to_gene = {}
    with gzip.open(files / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz", "rt") as reference:
        for header in reference:
            if header.startswith(">"):
                symbol = re.search(r"gene_symbol:(\S+)", header)
                if symbol and symbol[1].upper() in GENES:
                    transcript_to_gene[header[1:].split()[0].split(".")[0]] = symbol[1].upper()

    print("series\tgene\tn_KO\tn_control\tunit\tmean_KO\tmean_control\tlog2_diff_or_centered\tpair_min\tpair_max")
    comparisons = (
        ("GSE158681_hippocampus", "GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
         ("S_KO_1", "S_KO_2", "S_KO_3"), ("S_Ctrl_1", "S_Ctrl_2")),
        ("GSE158682_cortex", "GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz",
         ("CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"),
         ("CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4")),
    )
    for series, filename, ko, control in comparisons:
        data = collect_mouse(files, filename, ko, control, transcript_to_gene)
        emit_bulk(series, "TPM", data, len(ko), len(control))

    human_ko, human_control = ("cko1", "cko2", "cko3", "cko4"), ("cwt1", "cwt2")
    human = dict(collect_human(files, human_ko, human_control))
    emit_bulk("GSE156243_organoid", "CPM", human, len(human_ko), len(human_control))

    project = Path(__file__).resolve().parents[2]
    for cell_class in ("excitatory", "inhibitory"):
        source = project / NUCLEI / f"nuclei_effects_{cell_class}.tsv"
        with source.open() as table:
            effects = {row["gene"].upper(): row for row in csv.DictReader(table, delimiter="\t")}
        for gene in GENES:
            row = effects.get(gene)
            estimate = row["centred_coef"] if row and row["analysed"] == "1" else "NA"
            print(f"GSE158684_{cell_class}\t{gene}\t1_pool\t1_pool\tcentred_log2_CPM\tNA\tNA\t{estimate}\tNA\tNA")


if __name__ == "__main__":
    main()
