"""Convert aggregate source values and replay the non-pooled amiloride comparisons."""
import csv
from pathlib import Path
import sys


def replay(path, output):
    with path.open(encoding="utf-8") as handle:
        inputs = {row["id"]: row for row in csv.DictReader(handle, delimiter="\t")}

    def value(identifier):
        return float(inputs[identifier]["value"])

    output = csv.writer(output, delimiter="\t", lineterminator="\n")
    output.writerow(["id", "reference", "statistic", "value", "unit"])
    molecular_weight = value("free_base_mw")
    plasma = {
        key: value(key) / molecular_weight
        for key, row in inputs.items()
        if row["kind"] == "plasma"
    }
    for identifier, micromolar in plasma.items():
        output.writerow([identifier, "free_base_mw", "total plasma Cmax", f"{micromolar:.5f}", "uM"])

    for identifier, row in inputs.items():
        if row["kind"] == "bath":
            for comparator, micromolar in plasma.items():
                ratio = value(identifier) / micromolar
                output.writerow([identifier, comparator, "nominal bath / total plasma",
                                 f"{ratio:.2f}", "fold"])
        elif row["kind"] == "response":
            comparator = row["reference"]
            if row["unit"] != inputs[comparator]["unit"]:
                raise ValueError(f"Different units for {identifier} and {comparator}")
            fraction = value(identifier) / value(comparator)
            output.writerow([identifier, comparator, "relative change from source means",
                             f"{100 * (fraction - 1):.2f}", "percent"])


if __name__ == "__main__":
    replay(Path(__file__).with_name("source_inputs.tsv"), sys.stdout)
