"""Replay aggregate state reweighting, exposure scenarios and provoked mortality."""

import argparse
import csv
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from padsevonil.replay import risk_difference


def read_rows(filename):
    with (HERE / filename).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_rows(path, header, records):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(records)


def supplement_rates(path):
    with ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    result = {}
    for row in root.findall(".//{*}tbl/{*}tr"):
        cells = ["".join(cell.itertext()).strip() for cell in row.findall("{*}tc")]
        if cells and cells[0] in ("NR vs. Wake", "REM vs. Wake", "Dark vs. Light"):
            result[cells[0]] = tuple(map(float, cells[1:4]))
    return result


def values(row, error=0):
    zero, tick, value = (int(row[k]) for k in ("y_zero", "y_tick", "value_at_tick"))
    return tuple((zero - int(row[k]) + error) * value / (zero - tick)
                 for k in ("vehicle_y", "suvorexant_y"))


def weights(phase_rows, arm, offsets):
    raw = [values(row, error)[arm] for row, error in zip(phase_rows, offsets, strict=True)]
    return [value / sum(raw) for value in raw]


def scenarios(phase_rows, rates, *, phase_weighted):
    nrem, rem, dark = (rates[k] for k in ("NR vs. Wake", "REM vs. Wake", "Dark vs. Light"))
    phases = ("dark", "light") if phase_weighted else ("24h",)

    def score(nrem_rate, rem_rate, dark_rate, arm, pixel_offsets):
        total = 0
        for p, offsets in zip(phases, pixel_offsets, strict=True):
            fractions = weights(phase_rows[p], arm, offsets)
            phase_rate = sum(w * r for w, r in zip(fractions, (1.0, nrem_rate, rem_rate), strict=True))
            total += phase_rate * (dark_rate if p == "dark" else 1)
        return total

    exact = [(0, 0, 0)] * len(phases)
    central = score(nrem[0], rem[0], dark[0], 1, exact) / score(nrem[0], rem[0], dark[0], 0, exact)
    # The two arms' pixel readbacks have independent bounded error.
    endpoints = list(product(product((-2, 2), repeat=3), repeat=len(phases)))
    contrasts = []
    for n, r, d in product(nrem[1:], rem[1:], dark[1:]):
        vehicle = [score(n, r, d, 0, endpoint) for endpoint in endpoints]
        treated = [score(n, r, d, 1, endpoint) for endpoint in endpoints]
        contrasts.extend((min(treated) / max(vehicle), max(treated) / min(vehicle)))
    return central, min(contrasts), max(contrasts)


def state_replay(sources, output):
    rates = supplement_rates(sources / "rensing_EPI-67-3108-s001.docx")
    write_rows(output / "state_rate_inputs.tsv", ("contrast", "RR", "CI_low", "CI_high"),
               [(contrast, *values) for contrast, values in rates.items()])
    phase_rows = {phase: [] for phase in ("dark", "light", "24h")}
    observed = []
    for row in read_rows("figure_coordinates.tsv"):
        phase, label = row["phase_or_age"], row["state_or_endpoint"]
        if phase in phase_rows:
            phase_rows[phase].append(row)
        vehicle, treated = values(row)
        unit = "percent_classified_time" if phase in phase_rows else "seizures_per_week"
        observed.append((row["figure"], phase, label, unit, f"{vehicle:.3f}", f"{treated:.3f}"))
    for rows in phase_rows.values():
        assert [row["state_or_endpoint"] for row in rows] == ["wake", "nrem", "rem"]
    write_rows(output / "figure_readback.tsv", ("figure", "phase_or_age", "endpoint", "unit", "vehicle", "suvorexant"), observed)
    rows = []
    for name, phase_weighted in (("two_12h_phases", True), ("pooled_24h", False)):
        center, lo, hi = scenarios(phase_rows, rates, phase_weighted=phase_weighted)
        rows.append((name, f"{center:.4f}", f"{lo:.4f}", f"{hi:.4f}", "scenario_range_not_CI"))
    write_rows(output / "composition_only.tsv", ("weights", "central_RR", "corner_low", "corner_high", "interpretation"), rows)


def kinetic_replay(sources, output):
    root = ET.parse(sources / "kinetic_PMC3847553.1.xml")
    records = []
    for number, receptor in ((1, "OX1R"), (2, "OX2R")):
        table, = [t for t in root.findall("./body//table-wrap") if t.findtext("label") == f"Table {number}"]
        lines = []
        for row in table.findall(".//tr"):
            cells = ["".join(cell.itertext()).strip() for cell in row]
            if cells and cells[0].casefold() == "suvorexant":
                lines.append(cells)
        for species, line in zip(("human_CHO", "rat_HEK", "mouse_HEK"), lines, strict=True):
            for time, index in ((30, 1), (60, 4), (120, 7), (240, 10)):
                pki, sem, n = line[index:index + 3]
                records.append((species, receptor, time, pki, sem, n, f"{10 ** (9 - float(pki)):.4f}"))
    write_rows(output / "kinetic_replay.tsv", ("species_cells", "receptor", "preincubation_min", "apparent_pKi", "pKi_SEM", "assay_n", "apparent_nM"), records)

    bridge = []
    for fraction, interpretation in ((0.005, "FDA_PK002_bound_at_least_99_5pct_boundary"),
                                     (0.010, "Gotter_Fig7_assumption"),
                                     (0.015, "FDA_healthy_control_upper_observation")):
        # FDA human composite p. 29. The interval is for total geometric mean Cmax.
        free = 680 * fraction
        bridge.append((f"{100*fraction:.2f}", f"{free:.2f}", f"{620*fraction:.2f}",
                       f"{740*fraction:.2f}", f"{free/3.30:.3f}", interpretation))
    write_rows(output / "adult_exposure_scenarios.tsv", ("fu_percent", "free_Cmax_nM", "Cmax_total_CI_low_converted", "Cmax_total_CI_high_converted", "ratio_to_rat_derived_3_30nM", "assumption"), bridge)


def provoked_replay(output):
    rows = []
    for group, survivors in (("50", 4), ("100", 5), ("200", 5)):
        difference, low, high = risk_difference(survivors, 6, 2, 6)
        total = survivors + 2
        mass = {n: comb(total, n) * comb(12 - total, 6 - n)
                for n in range(max(0, total - 6), min(6, total) + 1)}
        p = sum(value for value in mass.values() if value <= mass[survivors]) / comb(12, 6)
        rows.append((group, survivors, 6, 2, 6, f"{difference:.3f}", f"{low:.3f}", f"{high:.3f}", f"{p:.4f}"))
    write_rows(output / "provoked_survival.tsv", ("study_arm_mg_per_kg", "survivors", "n", "control_survivors", "control_n", "crude_difference", "Newcombe_lo", "Newcombe_hi", "Fisher_two_sided"), rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_sources", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    for row in read_rows("source_inputs.tsv"):
        path = args.public_sources / row["file"]
        if sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"Unexpected content for {path}")
    state_replay(args.public_sources, args.out)
    kinetic_replay(args.public_sources, args.out)
    provoked_replay(args.out)


if __name__ == "__main__":
    main()
