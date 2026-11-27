"""Replay aggregate ammonia, labeled product and functional-outcome comparisons."""

import argparse
from collections import defaultdict
from html import unescape
import json
from pathlib import Path
import re
from statistics import mean, median, stdev
import sys

COMPOUNDS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(COMPOUNDS / "sodium_benzoate"))
sys.path.insert(0, str(COMPOUNDS / "jbpos0101"))
from coagonist_screen import bulk_panel, tsv
from replay_exposure_and_receptors import verified, verified_expression


FINGERPRINTS = {
    "Valproate_Palomino_pmc.html": "c369eb4c154efbc0b5f4bcd93c0adb21c9c2240548ed021e5a214df74412341f",
    "Valproate_Palomino.pdf": "679ba089b9c6db57230a2123c0d798179a6d302a82ff762d136c73154f0c2616",
    "Long_term_Alfadhel.pdf": "0dad2d5f7742d6d72c13d0256f03d87d8cdd56f189e196bc2ebce14990a55474",
    "Carbaglu_DailyMed.pdf": "4509ae27c627a9a6d32c5d35feed764484a9e02662f264444fcd11992f285b60",
    "Tracer_AhMew_PMC3297024.html": "29b69cf3143a4fac4807f3ef6dfaa403368f3fe74dde503ede3c64caed89ca68",
    "Tracer_ncg_bicarbonate.html": "ecfbd095721cc7bc48fb4c3e685f64928619f61e302bd0a5082561585adfc8b0",
    "AhMew_Fig2A.jpg": "e9789037095b4fd4f3dfcc24df0fdccad350fa802db12004606b8985f9a119a2",
    "AhMew_Fig2B.jpg": "f14605fa8f4c17ee15101a9fa4bc8dd6195aa3f2b0d994ae7a4ad3c6cbfc9217",
    "NCT01599286.json": "29125d690e15447510bdf77e138b6a1de9cd30bbfc3bdce61a2de404bf1ac60b",
    "NCT02426775.json": "0eb3e1ade2cf1e03bda75fd57479dcb50f4e6cf781b2c155b0a5f63ae89d9966",
}
GENES = ("Nags", "Cps1", "Otc", "Ass1", "Asl", "Arg1", "Arg2", "Glul", "Gls", "Gls2", "Glud1", "Slc1a2")


def table_rows(text, header):
    """Read simple tables from the fingerprinted PMC HTML without exporting source rows."""
    tables = re.findall(r"<table\b[^>]*>(.*?)</table>", text, flags=re.S | re.I)
    def visible(value):
        return " ".join(unescape(re.sub(r"<[^>]+>", " ", value)).split())

    table, = [body for body in tables if header in visible(body)]
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr>", table, flags=re.S | re.I):
        cells = re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", row, flags=re.S | re.I)
        yield [visible(cell) for cell in cells]


def valproate_rows(text):
    first, second, *rows = table_rows(text, "Other treatments")
    assert len(rows) == 25 and all(len(row) == 18 for row in rows)
    assert first[6] == "Ammonia levels (μmol/L)"
    assert second[3:6] == ["Basal", "After 2 h", "After 24 h"]
    groups = (
        ("all", rows),
        ("no_listed_additional_nitrogen_therapy", [row for row in rows if row[11] == "No"]),
        ("listed_additional_nitrogen_therapy", [row for row in rows if row[11] != "No"]),
        ("valproate_eventually_withdrawn", [row for row in rows if row[13] == "Yes"]),
        ("valproate_maintained", [row for row in rows if row[13] == "No"]),
    )
    for group, entries in groups:
        before, hour2, hour24 = zip(*(tuple(map(float, row[8:11])) for row in entries))
        repeat = sum(row[14] == "Yes" for row in entries)
        for hour, after in ((2, hour2), (24, hour24)):
            drop = [base - result for base, result in zip(before, after)]
            mean_drop, mean_baseline = mean(drop), mean(before)
            yield (group, len(entries), hour, mean_baseline, stdev(before), mean(after), stdev(after),
                   mean_drop, stdev(drop), median(drop), mean_drop / mean_baseline,
                   sum(value > 0 for value in drop), sum(value <= 50 for value in after), repeat)


def episode_rows(data):
    assert data["protocolSection"]["designModule"]["enrollmentInfo"]["count"] == 35
    result = data["resultsSection"]
    primary, = result["outcomeMeasuresModule"]["outcomeMeasures"]
    assert primary["unitOfMeasure"] == "Hazard Ratio"
    assert primary["dispersionType"] == "95% Confidence Interval"
    denoms = {d["units"]: {r["groupId"]: int(r["value"]) for r in d["counts"]} for d in primary["denoms"]}
    diagnosis = {group["id"]: group["title"] for group in primary["groups"]}
    for class_data in primary["classes"]:
        for category in class_data["categories"]:
            for row in category["measurements"]:
                group = row["groupId"]
                yield (diagnosis[group], denoms["Participants"][group], denoms["Episodes"][group],
                       float(row["value"]), float(row["lowerLimit"]), float(row["upperLimit"]))
    started, = [m for m in result["participantFlowModule"]["periods"][0]["milestones"] if m["type"] == "STARTED"]
    assert sum(int(row["numUnits"]) for row in started["achievements"]) == 106


def long_trial_rows(data):
    # Alfadhel Table 1 counts are recovered uniquely from rounded means and n.
    protocol = data["protocolSection"]
    registry_n = protocol["designModule"]["enrollmentInfo"]["count"]
    assert registry_n == 33 and data["hasResults"] is False
    active_n, standard_n, missing_n = 16, 17, 5
    active_events, standard_events = round(6.31 * active_n), round(12.76 * standard_n)
    mean_standard = standard_events / standard_n
    for missing_events_each in (None, 0, 16, (mean_standard * (active_n + missing_n) - active_events) / missing_n, 41):
        n = active_n if missing_events_each is None else active_n + missing_n
        added = 0 if missing_events_each is None else missing_events_each * missing_n
        active_mean = (active_events + added) / n
        yield (registry_n, n, standard_n, active_events, standard_events, missing_events_each,
               active_mean, mean_standard, active_mean / mean_standard, 0.4945, 0.2904, 0.8422)


def tracer_points():
    # Ah Mew Fig. 2 grouped estimated mean line centers, in pixels of supplied JPEGs.
    time = (0, 15, 30, 45, 60, 90, 120, 180, 240)
    pre_a = (379, 341, 302, 264, 231, 191, 190, 299, 440)
    post_a = (387, 348, 308, 269, 238, 198, 197, 305, 443)
    pre_b = (444, 431, 414, 392, 366, 321, 285, 280, 354)
    post_b = (433, 412, 380, 348, 314, 244, 188, 155, 233)
    for minute, a, b, c, d in zip(time, pre_a, post_a, pre_b, post_b):
        yield (minute, a, b, c, d, (451 - a) * 0.6 / (451 - 80), (451 - b) * 0.6 / (451 - 80),
               (449 - c) * 5 / (449 - 70), (449 - d) * 5 / (449 - 70))


def trapezoids(times, values):
    return sum((t1 - t0) * (y0 + y1) / 2 for t0, t1, y0, y1 in zip(times, times[1:], values, values[1:]))


def tracer_sensitivity(points):
    for index, start in ((0, 0), (1, 15), (2, 30)):
        times, _, _, _, _, precursor_before, precursor_after, urea_before, urea_after = zip(*points[index:])
        pre, post, u0, u1 = (trapezoids(times, values)
                             for values in (precursor_before, precursor_after, urea_before, urea_after))
        ratio_product = u1 / u0
        ratio_precursor = post / pre
        yield start, times[-1], pre, post, u0, u1, ratio_precursor, ratio_product, ratio_product / ratio_precursor


def healthy_bicarbonate_rows(text):
    header, *runs = table_rows(text, "Observed (270 min)")
    assert len(runs) == 6
    for minute, i, j in ((270, 1, 2), (300, 4, 5)):
        subjects = defaultdict(list)
        for row in runs:
            subjects[row[0].rstrip("AB")].append(float(row[i]) / float(row[j]))
        assert len(subjects) == 5
        values = [mean(repeats) for repeats in subjects.values()]
        yield minute, len(runs), len(subjects), mean(values), median(values), sum(v > 1 for v in values)


def rounded(rows):
    for row in rows:
        yield (f"{value:.6g}" if isinstance(value, float) else "NA" if value is None else value for value in row)


def main(files, out):
    source = files / "deepening_downloads/carglumic_acid_20261127"
    inputs = {name: verified(source / name, digest) for name, digest in FINGERPRINTS.items()}
    out.mkdir(parents=True, exist_ok=True)
    points = list(tracer_points())
    tables = (
        ("valproate_aggregates.tsv", "group n hour baseline_mean_uM baseline_SD_uM follow_up_mean_uM follow_up_SD_uM paired_drop_mean_uM paired_drop_SD_uM paired_drop_median_uM drop_ratio_of_means n_lower_ammonia n_at_or_below_50_uM n_recurrence", valproate_rows(inputs["Valproate_Palomino_pmc.html"].decode())),
        ("acute_episode_trial.tsv", "diagnosis n_participants n_episodes HR CI95_lower CI95_upper", episode_rows(json.loads(inputs["NCT01599286.json"]))),
        ("long_trial_missingness.tsv", "registry_actual_n n_active n_standard observed_active_events observed_standard_events imputed_events_per_missing_active mean_active_visits mean_standard_visits crude_mean_ratio published_RR published_CI95_lo published_CI95_hi", long_trial_rows(json.loads(inputs["NCT02426775.json"]))),
        ("propionic_tracer_plot.tsv", "minute precursor_pre_y_px precursor_post_y_px urea_pre_y_px urea_post_y_px precursor_pre_atom_pct_excess precursor_post_atom_pct_excess labeled_urea_pre_uM labeled_urea_post_uM", points),
        ("propionic_tracer_sensitivity.tsv", "start_minute end_minute precursor_pre_atom_pct_min precursor_post_atom_pct_min urea_pre_uM_min urea_post_uM_min precursor_post_pre urea_post_pre quotient_of_post_pre_ratios", tracer_sensitivity(points)),
        ("healthy_bicarbonate.tsv", "minute n_runs n_people mean_subject_observed_expected median_subject_observed_expected n_people_above_one", healthy_bicarbonate_rows(inputs["Tracer_ncg_bicarbonate.html"].decode())),
    )
    for filename, header, rows in tables:
        tsv(out / filename, header.split(), rounded(rows))
    verified_expression(files)
    tsv(out / "wwox_bulk_nitrogen.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, GENES))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    main(args.files, args.out)
