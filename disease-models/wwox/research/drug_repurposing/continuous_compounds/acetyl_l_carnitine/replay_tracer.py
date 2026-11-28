"""Compare group means of carbon incorporation in Scafidi Tables 1–2."""

import csv
from pathlib import Path


def main():
    with Path(__file__).with_name("tracer_observations.tsv").open() as source:
        rows = {(row["analyte"], int(row["minutes"])): float(row["mean"])
                for row in csv.DictReader(source, delimiter="\t")}

    print("analyte\tcontrast\tratio_of_group_means")
    for analyte in dict.fromkeys(analyte for analyte, _ in rows):
        print(f"{analyte}\t120 min / 15 min\t{rows[analyte, 120] / rows[analyte, 15]:.4f}")

    for minutes in (15, 60, 120):
        c3_c4 = rows["Glutamate C3", minutes] / rows["Glutamate C4", minutes]
        print(f"Glutamate C3 / C4\t{minutes} min\t{c3_c4:.4f}")


if __name__ == "__main__":
    main()
