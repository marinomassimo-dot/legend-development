"""Recalculate human NAD contrasts from the two original open primary records."""
import csv
from pathlib import Path
from statistics import mean, median
import sys
import xml.etree.ElementTree as ET

from openpyxl import load_workbook

raw = Path(sys.argv[1])
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("population", "contrast", "unit", "n", "increases", "mean", "median", "min", "max",
                 "leave_one_out_mean_min", "leave_one_out_mean_max"))


def summarize(group, label, unit, values):
    omissions = [mean(values[:i] + values[i + 1:]) for i in range(len(values))]
    stats = (mean(values), median(values), min(values), max(values), min(omissions), max(omissions))
    writer.writerow([group, label, unit, len(values), sum(v > 0 for v in values),
                     *(round(v, 4) for v in stats)])


def records(book, sheet):
    rows = iter(book[sheet].values)
    header = next(row for row in rows if row[0] == "Subject")
    return [dict(zip((str(h).strip() for h in header), row)) for row in rows if row[0]]


def changes(rows, time, endpoint, metric):
    pairs = {}
    for row in rows:
        day = row[time]
        if day in (0, endpoint) and isinstance(row[metric], (int, float)):
            entry = pairs.setdefault(row["Subject"], {})
            assert day not in entry
            entry[day] = row[metric]
    return {s: 100 * (v[endpoint] / v[0] - 1) for s, v in pairs.items()
            if 0 in v and endpoint in v and v[0] > 0}


table = ET.parse(raw / "human_acute.xml").find(".//table-wrap")
active, retest = [], []
for tr in table.findall(".//tr"):
    cells = ["".join(c.itertext()).strip() for c in tr]
    if cells[0].isdigit():
        a, b, c, d = (float(cells[i]) for i in (4, 6, 8, 10))
        active.append(b - a)
        retest.append(d - c)
assert len(active) == len(retest) == 9
summarize("healthy_7T", "post_NR_minus_initial", "mM", active)
summarize("healthy_7T", "untreated_repeat_minus_initial", "mM", retest)
summarize("healthy_7T", "active_change_minus_later_retest_change", "mM",
          [a - r for a, r in zip(active, retest)])

mrs = load_workbook(raw / "human_mrs.xlsx", read_only=True, data_only=True)
blood = load_workbook(raw / "human_blood.xlsx", read_only=True, data_only=True)
for brain_sheet, blood_sheet, days, endpoint, groups in [
    ("Stage_1_NR_brain", "LCMS_Stage_1", "Time (days)", 8, ["NR"]),
    ("Stage_2_brain", "LCMS_Stage_2", "Time (weeks)", 4, ["HC", "PwPs"]),
]:
    brain_rows = records(mrs, brain_sheet)
    blood_rows = records(blood, blood_sheet)
    for group in groups:
        label = f"{brain_sheet}_{group}"
        selected = [r for r in brain_rows if r.get("Status", r.get("Treatment")) == group]
        peripheral = [r for r in blood_rows if r["Group"] == group]
        blood_change = changes(peripheral, days, endpoint, "Total NAD (µM)")
        summarize(label, "blood_total_NAD", "percent", list(blood_change.values()))
        for denominator in ("ATP-alpha", "PCr", "all phosphates"):
            brain_change = changes(selected, days, endpoint, "total NAD/" + denominator)
            summarize(label, "brain_total_NAD/" + denominator, "percent", list(brain_change.values()))
            if denominator == "ATP-alpha":
                common = sorted(brain_change.keys() & blood_change.keys())
                assert len(common) == len(brain_change)
                summarize(label, "brain_change_minus_blood_change", "percentage_points",
                          [brain_change[s] - blood_change[s] for s in common])
