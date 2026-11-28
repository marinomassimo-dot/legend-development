"""Replay matched-assay ratios and a conditional product-only exposure balance."""

import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent


def write_table(name, columns, rows):
    with (HERE / name).open("w", newline="", encoding="utf-8") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def main():
    with (HERE / "assay_inputs.tsv").open(encoding="utf-8") as stream:
        inputs = {
            (row["assay"], row["molecule"]): row
            for row in csv.DictReader(stream, delimiter="\t")
        }
    tocopherol = "alpha_tocopherol"
    parent = "alpha_tocotrienol"
    quinone = "alpha_tocotrienol_quinone"
    hydroquinone = "alpha_tocotrienol_hydroquinone"

    def rescue_ec50(assay, molecule):
        return float(inputs[(assay, molecule)]["ec50_uM"])

    pairs = [
        ("Q7_RSL3", tocopherol, parent),
        ("Q7_RSL3", parent, quinone),
        ("Q7_RSL3", parent, hydroquinone),
        ("Pfa1_Gpx4_deletion", tocopherol, parent),
    ]
    write_table(
        "matched_ratios.tsv",
        ("assay", "numerator", "denominator", "ec50_ratio"),
        [
            (assay, first, second, f"{rescue_ec50(assay, first) / rescue_ec50(assay, second):.4f}")
            for assay, first, second in pairs
        ],
    )
    parent_ec50 = rescue_ec50("Q7_RSL3", parent)
    bounds = []
    for product in (quinone, hydroquinone):
        product_ec50 = rescue_ec50("Q7_RSL3", product)
        for relative_recovery in (0.1, 0.25, 0.5, 1, 2, 5):
            fraction = product_ec50 / (relative_recovery * parent_ec50)
            bounds.append((product, relative_recovery, f"{fraction:.5f}", int(fraction <= 1)))
    write_table(
        "product_only_bound.tsv",
        ("product", "relative_effective_recovery", "required_fraction", "fraction_at_most_one"),
        bounds,
    )


if __name__ == "__main__":
    main()
