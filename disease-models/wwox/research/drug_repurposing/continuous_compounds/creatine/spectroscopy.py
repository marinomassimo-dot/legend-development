"""Recalculate published regional contrasts and the dependence on the phosphorus reference."""
import argparse
import csv
import hashlib
from math import sqrt
from pathlib import Path
from statistics import mean
from xml.etree import ElementTree

HERE = Path(__file__).resolve().parent


def save(name, header, rows):
    with (HERE / name).open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header.split())
        writer.writerows(rows)


def run(kondo):
    assert hashlib.sha256(kondo.read_bytes()).hexdigest() == "e3bce149725f2306e493d18839203c84786575894951cac7344f3edd27b508d2"
    table, = [t for t in ElementTree.parse(kondo).findall(".//table-wrap")
              if t.findtext("label", "").split() == ["Table", "2"]]
    groups = ["placebo", "low", "middle", "high"]
    values = {}
    metabolite = None
    for row in table.findall(".//tr"):
        cells = ["".join(c.itertext()).strip() for c in row]
        if cells[0].startswith(("PCr/TP", "β-NTP/TP", "PME/TP", "PDE/TP")):
            metabolite = cells[0].split("/")[0]
        if cells[0] in ("Frontal lobe, baseline", "Frontal lobe, final"):
            visit = cells[0].split()[-1]
            values[metabolite, visit] = [float(cell.split()[0]) for cell in cells[1:5]]
    arms = []
    for i, group in enumerate(groups):
        start, end = [values["PCr", v][i] for v in ("baseline", "final")]
        beta0, beta1 = [values["β-NTP", v][i] for v in ("baseline", "final")]
        pcr_tp_change = 100 * (end / start - 1)
        pcr_beta_change = 100 * ((end / beta1) / (start / beta0) - 1)
        # With unobserved TP, unchanged absolute PCr is compatible with this TP multiplier.
        tp_change_for_constant_pcr = 100 * (start / end - 1)
        arms.append((group, start, end, pcr_tp_change, pcr_tp_change - (arms[0][3] if arms else pcr_tp_change),
                     pcr_beta_change, pcr_beta_change - (arms[0][5] if arms else pcr_beta_change),
                     tp_change_for_constant_pcr))
    save("phosphorus.tsv", "group pre_PCr_TP post_PCr_TP pct_change diff_vs_placebo_pp pct_change_PCr_betaNTP diff_vs_placebo_beta_pp equal_absolute_PCr_TP_change_pct", arms)

    # Original accepted manuscript Table 3, creatine then placebo pre/post values.
    regions = [("left_prefrontal", 6.9, 6.7, 6.7, 6.9, 2, 5.7),
               ("left_hippocampus", 7.0, 6.8, 6.7, 6.6, 5, 7.8),
               ("occipital", 7.9, 8.1, 7.7, 7.8, 3, 4.9)]
    rows = []
    for region, c0, c1, p0, p1, missing, cv in regions:
        delta = (c1 - c0) - (p1 - p0)
        rows.append((region, 21-missing, c1-c0, p1-p0, delta, delta-.2, delta+.2,
                     mean([c0,p0])*cv/100))
    save("total_creatine.tsv", "region evaluable_n active_change_mmol_L placebo_change_mmol_L difference rounding_lower rounding_upper pilot_CV_times_mid_baseline_mmol_L", rows)
    # Fig. 2A post-placebo endpoints, conservative after visual tolerance.
    # Lowest and highest points are approximately 4.9 and 8.0 mmol/L.
    lower_bound = (7.9 - 5.0) / sqrt(2*(10-1))
    assert lower_bound > .68


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kondo", type=Path)
    run(parser.parse_args().kondo)
