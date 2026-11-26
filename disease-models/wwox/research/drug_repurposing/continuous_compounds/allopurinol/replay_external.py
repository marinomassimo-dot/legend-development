"""Replay the allopurinol figure scales, cortical-well means and model sign check."""

import argparse
import csv
from math import comb
from pathlib import Path
from statistics import mean, median
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[6] / "framework" / "scripts"))
from xlsx_to_text import sheet_names


def column(workbook, tab, letter):
    root = ET.fromstring(workbook.read(dict(sheet_names(workbook))[tab]))
    values = []
    for cell in root.iterfind(".//{*}c"):
        address = cell.attrib["r"]
        if address.rstrip("0123456789") != letter or int(address[len(letter):]) < 4:
            continue
        value = cell.findtext("{*}v")
        if value is not None and cell.attrib.get("t", "n") == "n":
            values.append(float(value))
    return values


def cortical_wells(workbook):
    for tab, panel, readout, columns in (
        ("Fig 3", "3D", "normalized MAP2-positive neuron count", ("AY", "AZ", "BA")),
        ("Fig 3", "3F", "normalized GFAP-positive astrocyte count", ("CA", "CB", "CD")),
        ("Fig 8", "8B", "normalized excitatory/inhibitory synapse marker ratio", ("A", "B", "E")),
    ):
        exposure = "allopurinol plus probenecid" if panel == "8B" else "allopurinol"
        for group, letter in zip(("healthy", "MPS IIIA vehicle", exposure), columns):
            values = column(workbook, tab, letter)
            yield f"Greenberg {panel}", f"{readout}, {group}", "ratio", len(values), mean(values), median(values)


def tracer_figure():
    # Coordinates are from the published jpg panels, measured on the original axes.
    kidney_baseline = 5 * (1362 - 1250) / (1362 - 1010)
    yield "Tran 3B", "kidney AMP M+5, separate tracer-only cohort", "fractional abundance %", 8, kidney_baseline, "NA"
    # Y is from the top of the bitmap. Panel D uses filled-bar edges, never dot counts.
    for minute, vehicle, allopurinol in ((30, 769, 534), (60, 783, 647), (300, 792, 610)):
        for group, y in (("vehicle", vehicle), ("allopurinol", allopurinol)):
            label = f"blood hypoxanthine M+5, {group}, {minute} min"
            yield "Tran 4C", label, "fractional abundance %", 5, 30 * (806 - y) / (806 - 451), "NA"
    for metabolite, tissue, y, maximum in (
        ("hypoxanthine", "brain", 1647, 35),
        ("hypoxanthine", "kidney", 1517, 35),
        ("IMP", "brain", 1650, 12),
        ("IMP", "kidney", 1473, 12),
        ("AMP", "brain", 1653, 12),
        ("AMP", "kidney", 1444, 12),
    ):
        label = f"{tissue} {metabolite} M+5, allopurinol then tracer"
        yield "Tran 4D", label, "fractional abundance %", 5, maximum * (1664 - y) / (1664 - 1308), "NA"


def model_sign():
    # Chu 2022, Eq. 1 plus Eq. 3 and Table 2. These are instantaneous branch splits.
    salvage_rate = 0.5
    oxidation_rate = 0.2
    half_max = 0.68
    for combined in (0.0, half_max, 9 * half_max):
        inhibition = combined / (half_max + combined)
        for approach, activity in (("published EFF multiplier", inhibition), ("residual activity 1-EFF", 1 - inhibition)):
            salvage = salvage_rate / (salvage_rate + oxidation_rate * activity)
            yield "Chu Eq. 3", f"{approach}, C={combined:g} mg/L", "instantaneous salvage fraction", "NA", salvage, "NA"


def exact_probability(exposed_events, exposed_n, control_events, control_n):
    events = exposed_events + control_events
    weights = [
        comb(exposed_n, a) * comb(control_n, events - a)
        for a in range(max(0, events - control_n), min(events, exposed_n) + 1)
    ]
    observed = comb(exposed_n, exposed_events) * comb(control_n, control_events)
    return sum(w for w in weights if w <= observed) / comb(exposed_n + control_n, events)


def clinical_table():
    for endpoint, exposed, control in (("mortality", 13, 10), ("aEEG recovery within 24 h", 7, 7), ("status epilepticus", 8, 5)):
        difference = exposed / 17 - control / 15
        yield "Benders Table 1", endpoint, "risk difference allopurinol minus vehicle", "17/15", difference, "NA"
        yield "Benders Table 1", endpoint, "two-sided Fisher p", "17/15", exact_probability(exposed, 17, control, 15), "NA"
    adult_micromolar = 3_000 / 136.11
    yield "US label section 12.3", "adult oral total parent Cmax", "micromolar", "NA", adult_micromolar, "NA"
    yield "Greenberg Fig. 3 vs label", "nominal 2200 uM / adult total parent Cmax", "ratio", "NA", 2200 / adult_micromolar, "NA"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_workbook", type=Path)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("locator", "contrast", "unit", "n", "estimate", "median_if_applicable"))
    with ZipFile(args.source_workbook) as workbook:
        for rows in (cortical_wells(workbook), tracer_figure(), model_sign(), clinical_table()):
            for row in rows:
                writer.writerow(f"{v:.6g}" if isinstance(v, float) else v for v in row)


if __name__ == "__main__":
    main()
