"""Replay the cortical diazoxide drug-minus-baseline contrasts in eLife Figure 4."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path
from statistics import median
import sys

import xlrd


SOURCE_HASHES = {
    "elife-71424-fig4-data1.xls": "58c2e5a1114901e1a54eaf03bff800cbafefa53349f5256d7a88d70a01049337",
    "elife-71424-fig4-data2.xls": "de61bba56a68d7dc1c7dbec290ad1880874e326a007ae84648c6fd06ce894b47",
}
CELL_CLASSES = {"RS": "regular_spiking_Glu", "FS-Pvalb": "fast_spiking_Pvalb"}


def source_rows(source):
    if sha256(source.read_bytes()).hexdigest() != SOURCE_HASHES[source.name]:
        raise ValueError(f"Published workbook fingerprint differs for {source.name}")
    sheet = xlrd.open_workbook(source).sheet_by_index(0)
    header = sheet.row_values(0)
    return [dict(zip(header, sheet.row_values(i))) for i in range(1, sheet.nrows)]


def contrasts(source_directory):
    recordings = source_rows(source_directory / "elife-71424-fig4-data1.xls")
    labels = source_rows(source_directory / "elife-71424-fig4-data2.xls")
    recordings = [row for row in recordings if row["Cell type"] in CELL_CLASSES]
    labels = [row for row in labels if row["Cell type"] in CELL_CLASSES]
    by_id = {row["cell Id"]: row for row in labels}
    if len(by_id) != len(labels) or len(by_id) != len(recordings) or set(by_id) != {row["cell Id"] for row in recordings}:
        raise ValueError("Figure 4 cell IDs failed the one-to-one join")
    groups = {category: [] for category in CELL_CLASSES.values()}
    for row in recordings:
        kind = row["Cell type"]
        label = by_id[row["cell Id"]]
        if kind != label["Cell type"]:
            raise ValueError(f"Cell classification differs for {row['cell Id']}")
        base_ns = 1000 / row["R Ctrl"]
        drug_ns = 1000 / row["R Diazo"]
        groups[CELL_CLASSES[kind]].append({
            "responsive": label["K-ATP Pharmacology"] == "Responsive",
            "dVm_mV": row["Vm Diazo"] - row["Vm Ctrl"],
            "dG_nS": drug_ns - base_ns,
            "dG_pct": 100 * (drug_ns / base_ns - 1),
        })
    return groups


def show(groups, writer):
    writer.writerow(("subset", "class", "n_cells", "n_reported_responsive", "n_dG_positive",
                     "median_dVm_mV", "median_dG_nS", "median_dG_pct", "omit_one_dG_min_nS",
                     "omit_one_dG_max_nS"))
    for use_responsive_only in (False, True):
        subset = "reported_responsive" if use_responsive_only else "all_reported"
        for name, full in groups.items():
            cells = [cell for cell in full if cell["responsive"]] if use_responsive_only else full
            conductance = [cell["dG_nS"] for cell in cells]
            omission = [median(conductance[:i] + conductance[i + 1 :]) for i in range(len(cells))] if len(cells) > 1 else []
            writer.writerow((subset, name, len(cells), sum(cell["responsive"] for cell in cells),
                             sum(value > 0 for value in conductance), f"{median(cell['dVm_mV'] for cell in cells):.4f}",
                             f"{median(conductance):.4f}", f"{median(cell['dG_pct'] for cell in cells):.4f}",
                             f"{min(omission):.4f}" if omission else "NA",
                             f"{max(omission):.4f}" if omission else "NA"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_directory", type=Path)
    args = parser.parse_args()
    show(contrasts(args.source_directory), csv.writer(sys.stdout, delimiter="\t", lineterminator="\n"))


if __name__ == "__main__":
    main()
