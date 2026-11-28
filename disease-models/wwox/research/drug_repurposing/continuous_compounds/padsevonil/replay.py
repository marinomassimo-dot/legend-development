"""Replay the aggregate trial, PET-table and trough calibration comparisons."""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, ROUND_HALF_UP
from hashlib import sha256
import json
from math import hypot, sqrt
from pathlib import Path
from statistics import mean, stdev
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
Z95 = 1.959963984540054


def read_rows(filename):
    with (HERE / filename).open(encoding="utf-8", newline="") as handle:
        yield from csv.DictReader(handle, delimiter="\t")


def write_rows(path, header, data):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(data)


def percent(count, n):
    return (Decimal(100 * count) / n).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)


def count_from_percentage(n, reported):
    matches = [i for i in range(n + 1) if percent(i, n) == Decimal(reported)]
    if len(matches) != 1:
        raise ValueError(f"Percentage {reported} has {len(matches)} matches for n={n}")
    return matches[0]


def wilson(k, n):
    p = k / n
    scale = 1 + Z95**2 / n
    center = (p + Z95**2 / (2 * n)) / scale
    width = Z95 / scale * sqrt((p * (1 - p) + Z95**2 / (4 * n)) / n)
    return center - width, center + width


def risk_difference(k, n, ctl_k, ctl_n):
    p, ctl = k / n, ctl_k / ctl_n
    lo, hi = wilson(k, n)
    ctl_lo, ctl_hi = wilson(ctl_k, ctl_n)
    delta = p - ctl
    return delta, delta - hypot(p - lo, ctl_hi - ctl), delta + hypot(hi - p, ctl - ctl_lo)


def phase3_registry(path):
    outcomes = json.loads(path.read_text(encoding="utf-8"))["resultsSection"]["outcomeMeasuresModule"]["outcomeMeasures"]
    groups = {"OG000": "placebo", "OG001": "100", "OG002": "200", "OG003": "400"}
    for endpoint, label in (("75%", "primary"), ("50%", "secondary")):
        measure, = (m for m in outcomes if m["title"].startswith(f"{endpoint} Responder Rate"))
        denoms = {row["groupId"]: row["value"] for row in measure["denoms"][0]["counts"]}
        for group in measure["groups"]:
            gid = group["id"]
            assert gid in groups and (groups[gid] == "placebo" or groups[gid] in group["title"])
        for cls in measure["classes"]:
            for cat in cls["categories"]:
                for row in cat["measurements"]:
                    gid = row["groupId"]
                    yield {
                        "trial": "EP0092", "endpoint": f"{endpoint} {label}",
                        "arm_group": groups[gid], "denominator": denoms[gid], "observed_count": "",
                        "percent_printed": row["value"], "source": "NCT03739840 outcome-specific analysis set",
                    }


def replay_trials(sources, output):
    records = [*read_rows("trial_inputs.tsv"), *phase3_registry(sources / "NCT03739840.json")]
    counts = {}
    for row in records:
        n = int(row["denominator"])
        reported = row["percent_printed"]
        stated = row["observed_count"]
        k = int(stated) if stated else count_from_percentage(n, reported)
        if percent(k, n) != Decimal(reported):
            raise ValueError(f"Count and percentage differ: {row}")
        counts[(row["trial"], row["endpoint"], row["arm_group"])] = (k, n)

    rows = []
    for row in records:
        trial, endpoint, arm = (row[x] for x in ("trial", "endpoint", "arm_group"))
        if arm == "placebo":
            continue
        k, n = counts[(trial, endpoint, arm)]
        ctl_k, ctl_n = counts[(trial, endpoint, "placebo")]
        values = risk_difference(k, n, ctl_k, ctl_n)
        rows.append([trial, endpoint, arm, k, n, ctl_k, ctl_n,
                     *(f"{100 * value:.2f}" for value in values),
                     "printed" if row["observed_count"] else "unique from rounded percentage", row["source"]])
    write_rows(output / "trial_comparison.tsv",
               ("trial", "endpoint", "arm_group", "events", "n", "placebo_events", "placebo_n",
                "difference_pp", "unadjusted_95_low_pp", "unadjusted_95_high_pp", "arm_count_basis", "source"),
               rows)


def replay_pet(sources, output):
    xml = ET.parse(sources / "koole.xml")
    table, = (wrap for wrap in xml.findall(".//table-wrap") if " ".join(wrap.findtext("label", "").split()) == "Table 1")
    first, second, shifts = [], [], []
    for row in table.findall("./table/tbody/tr"):
        cells = ["".join(td.itertext()).strip() for td in row.findall("td")]
        initial = float(cells[3].rstrip("%"))
        first.append(initial)
        if cells[5].endswith("%"):
            followup = float(cells[5].rstrip("%"))
            second.append(followup)
            shifts.append(followup - initial)
    assert (len(first), len(second), len(shifts)) == (10, 7, 7)
    rows = [(key, len(values), f"{mean(values):.2f}", f"{stdev(values):.2f}",
             f"{min(values):.1f}", f"{max(values):.1f}") for key, values in
            (("table_post1", first), ("table_post2", second), ("within_person_post2_minus_post1", shifts))]
    rows += [("methods_post1_printed", 10, "82.10", "14.50", "57.0", "98.0"),
             ("methods_post2_printed", 7, "41.20", "21.20", "16.0", "63.0")]
    write_rows(output / "pet_consistency.tsv", ("readout", "n", "mean_pct_or_pp", "sd", "min", "max"), rows)


def occupancy(plasma, ec50):
    return 100 * plasma / (ec50 + plasma)


def replay_bridge(output):
    # Rademacher Appendix Figure S4A, page 9 at 120 dpi. Zero on log10 is 1 ng/mL.
    y_at_one, y_at_thousand, edge_px = 485, 223, 2
    low_bp, mid_bp, high_bp = 0.60, 0.65, 0.70
    low_ec50, mid_ec50, high_ec50 = 2.0, 3.1, 4.2
    rows = []
    for point in read_rows("trough_pixels.tsv"):
        y = int(point["y_marker"])

        def blood(y_pixel):
            return 10 ** (3 * (y_at_one - y_pixel) / (y_at_one - y_at_thousand))

        displayed = blood(y)
        plasma = displayed / mid_bp
        central = occupancy(plasma, mid_ec50)
        lo = occupancy(blood(y + edge_px) / high_bp, high_ec50)
        hi = occupancy(blood(y - edge_px) / low_bp, low_ec50)
        rows.append([point["week"], point["arm_group"], *(f"{number:.2f}" for number in (displayed, plasma, central, lo, hi))])
    write_rows(output / "trough_bridge.tsv",
               ("week", "arm_group", "blood_ng_ml_approx", "plasma_ng_ml_inferred", "sv2a_pct_inferred",
                "corner_low_pct", "corner_high_pct"), rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_directory", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    needed = {"koole.xml", "NCT03739840.json"}
    for row in read_rows("source_inputs.tsv"):
        name = row["local_filename"]
        if name in needed:
            source = args.source_directory / name
            if sha256(source.read_bytes()).hexdigest() != row["sha256"]:
                raise ValueError(f"{name} differs from the replay source")
            needed.remove(name)
    if needed:
        raise ValueError(f"Missing source manifest entries: {sorted(needed)}")
    args.out.mkdir(parents=True, exist_ok=True)
    replay_trials(args.source_directory, args.out)
    replay_pet(args.source_directory, args.out)
    replay_bridge(args.out)


if __name__ == "__main__":
    main()
