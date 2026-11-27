"""Recompute the public Wu and Sasaki figure-source contrasts."""

import argparse
import csv
from io import BytesIO
from pathlib import Path
from statistics import mean
import sys
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "metformin"))
from replay_native_target_coverage import checked_bytes, worksheet_rows


def sheet(directory, name, digest, tab):
    with ZipFile(BytesIO(checked_bytes(directory / name, digest))) as archive:
        return dict(worksheet_rows(archive, tab))


def contrasts(directory):
    wu = sheet(
        directory, "wu-fig4-s1.xlsx",
        "77028cbe568d961403d1151fbb7007a669683c78d022dd327ab5b51276d41aa1", "Fig4-supp1A",
    )[12]
    technical = [float(wu[col]) for col in "EFG"]
    yield "Wu Fig. 4 supp. 1A", "row 12 NAM concentration", "", 10 ** float(wu["D"]), "µM"
    yield "Wu Fig. 4 supp. 1A", "PC6 signal inhibition", len(technical), mean(technical), "%"

    turnover = sheet(
        directory, "sasaki-fig4-data1.xlsx",
        "e981fc65ec26d68213da3069ffbff0413c51cae2a826e3f02a5d9e7098c4a947", "Fig 4b",
    )
    for genotype, uncut in (("WT", 4), ("Sarm1 KO", 6)):
        rates = []
        for condition, index in (("uncut", uncut), ("cut", uncut + 1)):
            row = turnover[index]
            values = [float(row[column]) for column in "CDEFGHIJK"]
            rate = -mean(values)
            if abs(rate - float(row["P"])) > 1e-6:
                raise ValueError(f"Unexpected agreement with the published mean in row {index}")
            rates.append(rate)
            yield "Sasaki Fig. 4b", f"{genotype} {condition} light NAD loss", len(values), rate, "%/h"
        yield "Sasaki Fig. 4b", f"{genotype} cut/uncut light NAD loss", "", rates[1] / rates[0], "fold"

    morphology = sheet(
        directory, "sasaki-fig4-data2.xlsx",
        "c12647ce4a84372c6276b415bebbc0ece32c44ecf10243663d38acad2228d896", "Sheet1",
    )
    for hours, start in ((0, 3), (9, 10), (24, 17)):
        for name, col in (("control", "A"), ("NAM 1 mM", "B")):
            values = [float(morphology[i][col]) for i in range(start, start + 4)]
            yield "Sasaki Fig. 4 supp. 1", f"{hours} h {name} degeneration index", len(values), mean(values), "index"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("study_panel", "endpoint", "n_values", "value", "unit"))
    writer.writerows((panel, endpoint, n, f"{value:.5f}", unit)
                     for panel, endpoint, n, value, unit in contrasts(parser.parse_args().sources))
