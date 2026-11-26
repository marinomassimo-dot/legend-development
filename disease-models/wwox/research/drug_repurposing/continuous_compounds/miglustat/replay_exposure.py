"""Compare observed human CSF exposure and published assay scales."""

import csv
from pathlib import Path
import sys


def main():
    inputs = Path(__file__).with_name("exposure_inputs.tsv")
    with inputs.open(encoding="utf-8", newline="") as handle:
        values = {row["key"]: float(row["value"]) for row in csv.DictReader(handle, delimiter="\t")}

    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("csf_observation", "uM_parent", "CSF_over_GBA2_Ki", "GCS_IC50_over_CSF"))
    for label in ("csf_trough_min", "csf_trough_max"):
        parent = values[label] / values["parent_mass"]
        writer.writerow((
            label, f"{parent:.6g}", f"{parent / values['human_gba2_ki']:.6g}",
            f"{values['gcs_ic50'] / parent:.6g}",
        ))


if __name__ == "__main__":
    main()
