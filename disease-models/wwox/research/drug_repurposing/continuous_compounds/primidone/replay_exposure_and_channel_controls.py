"""Replay primidone exposure, published channel controls and the animal EEG contrast."""

import argparse
import csv
from io import BytesIO
from math import comb
from pathlib import Path
import sys
from zipfile import ZipFile

DATA_DIGEST = "879316767312475104e46ef25a42398a6789850595fe5de07536a75e1e18afc8"
SATO_DIGEST = "bbb8b23c6dcf23e41cc8b64d9e3d00be8f1795cf2f93378869fcf6b108c62013"
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "metformin"))
from replay_native_target_coverage import checked_bytes, worksheet_rows


def exposure_rows(sato):
    checked_bytes(sato, SATO_DIGEST)
    # Sato, printed page 470 Table I, mean rows across the same three adults.
    panel = (
        ("primidone Cmax", 41.2, 40.6, "µM"),
        ("phenobarbital Cmax", 1.3, 8.2, "µM"),
        ("PEMA Cmax", 1.7, 11.0, "µM"),
        ("primidone AUC", 1916, 1042, "µM·h"),
        ("phenobarbital AUC", 288, 1554, "µM·h"),
        ("PEMA AUC", 143, 724, "µM·h"),
        ("primidone Tmax", 12, 8, "h"),
        ("phenobarbital Tmax", 52, 44, "h"),
        ("PEMA Tmax", 36, 28, "h"),
    )
    for label, control, phenytoin, unit in panel:
        yield "Sato Table I", label, control, unit, "without phenytoin"
        yield "Sato Table I", label, phenytoin, unit, "with phenytoin"
    yield "Sato Table I", "phenobarbital/primidone AUC", f"{288 / 1916:.4f}", "ratio of means", "without phenytoin"
    yield "Sato Table I", "phenobarbital/primidone AUC", f"{1554 / 1042:.4f}", "ratio of means", "with phenytoin"
    yield "Sato Table I", "AUC ratio shift", f"{(1554 / 1042) / (288 / 1916):.2f}", "fold", "same 3 adults, separate windows"

    unbound = 4.4 / 1.2
    yield "Becker Fig. 2", "equal normalized exposure PB/PRM", f"{unbound:.3f}", "unbound molar ratio", "rat calcium assay"
    plasma_ratio = unbound * 0.81 / 0.43
    yield "Becker and Houghton tissue assumption", "illustrative total plasma PB/PRM", f"{plasma_ratio:.3f}", "molar ratio", "81% and 43% projected fractions"
    yield "Becker and Houghton tissue assumption", "illustrative total plasma PB/PRM", f"{plasma_ratio * 232.23 / 218.25:.3f}", "mass ratio", "scenario using a CSF ultrafiltration assumption"


def workbook(archive, filename):
    name, = (name for name in archive.namelist() if name.rsplit("/", 1)[-1] == filename)
    return ZipFile(BytesIO(archive.read(name)))


def channel_rows(data):
    with ZipFile(BytesIO(checked_bytes(data, DATA_DIGEST))) as archive:
        with workbook(archive, "Figure4-c,d.xlsx") as figure4:
            row_number, row = next((i, cells) for i, cells in worksheet_rows(figure4, "Figure 4-d")
                                   if cells.get("B", "").strip() == "Y921A")
        for inhibitor, column in (("primidone", "E"), ("isosakuranetin", "C")):
            fold = 10 ** float(row[column])
            yield "Bazeli Fig. 4d workbook", f"Y921A {inhibitor}", f"{fold:.2f}", "fold IC50 vs WT", f"row {row_number}, {column}, back-transform log10"

        with workbook(archive, "Figure6-c,e,f.xlsx") as figure6:
            summary = {cells["B"]: (i, cells) for i, cells in worksheet_rows(figure6, "Figure6d-%of inhibition")
                       if cells.get("B") in {"10", "30", "300"}}
        for concentration, labels in (
            ("10", (("I999S/WT", "H"), ("F1150S/WT", "J"))),
            ("30", (("I999S/WT", "H"), ("F1150S/WT", "J"))),
            ("300", (("I999S only", "E"), ("F1150S only", "C"))),
        ):
            row_number, cells = summary[concentration]
            for variant, column in labels:
                yield "Bazeli Fig. 6d workbook", f"{variant} at {concentration} µM primidone", f"{100 * float(cells[column]):.2f}", "% stimulated inhibition", f"row {row_number}, {column}"

    # The fits use different readouts. Their ratios are descriptors, not a binding constant.
    for variant, stimulated, basal in (("I999S/WT", 85.2, 5.4), ("F1150S/WT", 222, 3.5)):
        yield "Bazeli Results Fig. 6d/e", variant, f"{stimulated / basal:.2f}", "ratio of reported IC50", "steroid-challenged fluorescence divided by basal fluorescence sensitivity"


def circuit_rows():
    # Fig. 4i is a binary per-mouse reanalysis at fixed group margins.
    group = 10
    total_events = 3
    observed_ways = comb(group, total_events)
    all_ways = comb(2 * group, total_events)
    counts = [comb(group, x) * comb(group, total_events - x) for x in range(total_events + 1)]
    p_value = sum(ways for ways in counts if ways <= observed_ways) / all_ways
    yield "Gyéresi Fig. 4i", "three WT vs zero Trpm3-null with seizure", f"{p_value:.4f}", "Fisher two-sided p", "10 mice per group, one 24 h recording"
    yield "Gyéresi Fig. 4i", "zero of ten upper limit", f"{100 * (1 - 0.025**(1 / group)):.2f}", "% two-sided exact 95% upper bound", "binomial within sampled interval"
    yield "Gyéresi Fig. 4h", "Trpm3-null mean spike count / WT", f"{150.8 / 1240:.4f}", "ratio of means", "ictal and interictal spikes"
    for label, value in (("Trpm3-null", 115.5), ("acute isosakuranetin", 114.7)):
        yield "Gyéresi Fig. 2d", label + " minus WT", f"{value - 215.6:+.1f}", "percentage points of EPSP baseline", "exploratory LTP, neurons nested in mice"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sato_pdf", type=Path)
    parser.add_argument("bazeli_zip", type=Path)
    args = parser.parse_args()
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "contrast", "value", "unit", "boundary"))
    writer.writerows(exposure_rows(args.sato_pdf))
    writer.writerows(channel_rows(args.bazeli_zip))
    writer.writerows(circuit_rows())


if __name__ == "__main__":
    main()
