"""Recalculate the leucine fold changes in a held fly supplement and audit identity."""
import csv
import json
from pathlib import Path
import sys


supplement, maf, samples, positive_assay = (Path(argument) for argument in sys.argv[1:])
sheets = {4: [], 7: []}
sheet = None
for line in supplement.read_text().splitlines():
    if line.startswith("## sheet"):
        sheet = next((number for number in sheets if f"'Supplementary Table {number}'" in line), None)
    elif sheet is not None:
        fields = line.split("\t")
        if fields[0].isdigit():
            sheets[sheet].append(fields)

reference, = [row for row in sheets[7] if row[4].casefold() == "l-leucine"]
peak = reference[0]
mass = float(reference[1])
rt = float(reference[2])
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("comparison", "quantity", "value"))
for label, index in (("OE_main", 9), ("OE_in_amyloid_background", 17),
                     ("OE_in_LacZ_background", 18)):
    writer.writerow((label, "relative_peak_area", f"{2 ** float(reference[index]):.5f}"))
writer.writerow(("OE_main", "adjusted_P", f"{float(reference[8]):.5f}"))
writer.writerow(("OE_amyloid_interaction", "adjusted_P", f"{float(reference[16]):.5f}"))
writer.writerow(("OE", "assigned_peak_ID", peak))
writer.writerow(("KD", "differential_rows", len(sheets[4])))
writer.writerow(("KD", "rows_in_5ppm_and_1s_window", sum(
    abs(float(row[1]) / mass - 1) <= 5e-6 and abs(float(row[2]) - rt) <= 1
    for row in sheets[4]
)))
writer.writerow(("KD", "exact_assigned_L_leucine", sum(
    row[4].casefold() == "l-leucine" for row in sheets[4]
)))
entries = json.loads(maf.read_text())["data"]["rows"]
maf_match = [row for row in entries if abs(float(row["mass_to_charge"]) / mass - 1) <= 5e-6
             and abs(float(row["retention_time"]) - rt) <= 1]
writer.writerow(("deposited_MAF", "entries_in_5ppm_and_1s_window", len(maf_match)))
for row in maf_match:
    writer.writerow(("deposited_MAF", "matched_identity", row["metabolite_identification"]))


# Inspect the published sample-to-spectrum crosswalk before any intensity fit.
sample_rows = json.loads(samples.read_text())["data"]["rows"]
assays = json.loads(positive_assay.read_text())["data"]["rows"]
kd_samples = {row["Sample Name"] for row in sample_rows
              if row["Sample Name"].endswith("_KDExp")
              and row["Characteristics[Sample type]"] == "experimental sample"}
for row in assays:
    sample = row["Sample Name"]
    if sample in kd_samples:
        writer.writerow(("KD_assay_registered_raw", sample, row["Raw Spectral Data File"]))
        writer.writerow(("KD_assay_registered_derived", sample, row["Derived Spectral Data File"]))
