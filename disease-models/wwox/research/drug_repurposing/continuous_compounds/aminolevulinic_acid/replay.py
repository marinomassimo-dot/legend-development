"""Reproduce aggregate FLVCR1, factorial, Leigh and exposure comparisons."""
import argparse
import csv
from hashlib import sha256
from itertools import product
from pathlib import Path
import re
from statistics import mean
import sys
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent), str(HERE.parents[5] / "framework" / "scripts")]
from padsevonil.replay import risk_difference
from xlsx_to_text import read_workbook


def read_tsv(name):
    with (HERE / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path, header, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def figure7(sources, output):
    text = read_workbook(sources / "flvcr1_42003_2026_9691_MOESM3_ESM.xlsx")
    section = text.split("## sheet 'Fig. 7a'", 1)[1].split("\n## sheet", 1)[0]
    panels = {}
    columns = {}
    for line in section.splitlines():
        fields = line.split("\t")
        if len(fields) != 18:
            continue
        for offset in (0, 9):
            name, *data = fields[offset:offset + 9]
            if len(name) == 1 and name in "ABCDEFGH":
                columns[offset] = name
                panels[name] = {}
            elif name in ("Controls", "Patients", "Carriers", "Het"):
                key = "carriers" if name in ("Carriers", "Het") else name.lower()
                panels[columns[offset]][key] = tuple(
                    [float(v) for v in part if v] for part in (data[:4], data[4:]))
    out = []
    for panel, groups in panels.items():
        control = groups["controls"]
        for group, (basal, treated) in groups.items():
            before, after = mean(basal), mean(treated)
            out.append((panel, group, len(basal), len(treated), f"{before:.5f}", f"{after:.5f}",
                        f"{after/before:.5f}", f"{after/mean(control[1]):.5f}"))
    write_tsv(output / "flvcr1_figure7.tsv", ("panel", "donor_group", "n_untreated", "n_treated", "mean_untreated_native_units",
              "mean_treated_native_units", "treated_over_untreated", "treated_over_treated_control"), out)
    rows = []
    for group in ("patients", "controls", "carriers"):
        etc = groups_fold(panels["F"][group])
        citrate = groups_fold(panels["A"][group])
        rows.append((group, f"{etc:.5f}", f"{citrate:.5f}", f"{etc/citrate:.5f}"))
    write_tsv(output / "flvcr1_activity_sensitivity.tsv", ("donor_group", "ETC_fold", "citrate_synthase_fold", "ratio_of_folds"), rows)


def groups_fold(pair):
    baseline, after = pair
    return mean(after) / mean(baseline)


def factorial(output):
    out = []
    for line in read_tsv("factorial_coordinates.tsv"):
        zero, tick = (int(line[k]) for k in ("axis_zero_y", "axis_500_percent_y"))
        step = 5 / (zero - tick)
        means = [(zero - int(line[k])) * step for k in ("ALA_y", "SFC_y", "combination_y")]
        a, iron, both = means
        all_means = [[x - 2*step, x + 2*step] for x in means]
        bounds = [(z - x - y + 1, z/(x*y)) for x, y, z in product(*all_means)]
        add, mul = zip(*bounds, strict=True)
        out.append((line["ALA_uM"], line["SFC_uM"], *(f"{x:.4f}" for x in
                    (a, iron, both, both-a-iron+1, min(add), max(add), both/(a*iron), min(mul), max(mul)))))
    write_tsv(output / "factorial_replay.tsv", ("ALA_uM", "SFC_uM", "ALA_fold_MRR", "SFC_fold_MRR", "combined_fold_MRR",
              "additive_residual", "additive_low_2px", "additive_high_2px", "multiplicative_ratio", "multiplicative_low_2px", "multiplicative_high_2px"), out)


def table(path, label):
    root = ET.parse(path)
    match, = [t for t in root.findall(".//{*}table-wrap") if t.findtext("{*}label") == label]
    for row in match.findall(".//{*}tr"):
        yield [" ".join("".join(c.itertext()).split()) for c in row]


def leigh(sources, output):
    path = sources / "phase3_PMC13379092.1.xml"
    data = {}
    for fields in table(path, "Table 3"):
        label = fields[0]
        if label.startswith(("All", "Age of onset")):
            strata = label
            data[strata] = (int(fields[1]), int(fields[3]))
        elif label.startswith("Inadequate efficacy"):
            n, control_n = data[strata]
            data[strata] = (int(fields[1]), n, int(fields[3]), control_n)
    age = [data[k] for k in data if k.startswith("Age of onset")]
    weights = [n*m/(n+m) for _, n, _, m in age]
    mh = sum(w*(a/n-b/m) for w,(a,n,b,m) in zip(weights, age, strict=True))/sum(weights)
    original = data["All"]
    rows = [("efficacy", name, *counts) for name, counts in data.items()]
    rows.extend(("missing treated endpoint", name, a, 14, 7, 14)
                for name, a in (("no failure", 2), ("failure", 3)))
    safety = next(row for row in table(path, "Table 5") if row[0] == "Serious adverse events")
    rows.append(("safety", "at least one serious event", int(safety[3].split()[0]), 14, int(safety[5].split()[0]), 14))
    out = []
    for measure, group, a, n, b, m in rows:
        diff, lo, hi = risk_difference(a, n, b, m)
        out.append((measure, group, a, n, b, m, f"{100*diff:.3f}", f"{100*lo:.3f}", f"{100*hi:.3f}"))
    out.append(("efficacy", "MH age-weighted treatment minus placebo", *original, f"{100*mh:.3f}", "NA", "NA"))
    write_tsv(output / "leigh_trial.tsv", ("measure", "population_or_method", "events_active", "n_active", "events_control", "n_control", "risk_difference_pp",
              "newcombe_low_pp", "newcombe_high_pp"), out)


def exposure(sources, output):
    path = sources / "phase2_PMC12387954.1.xml"
    parent_row, = [row for row in table(path, "Table 3") if row[0].startswith("Cmax (μmol")]
    n = int(parent_row[1])
    peak, sd = (float(x.strip()) for x in parent_row[2].split("±"))
    _, reported_low, reported_max = (float(x) for x in re.findall(r"[\d.]+", parent_row[3]))
    adult = 20.90 * 1000 / 131.13
    rows = [(ref, prep, c, f"{c/peak:.3f}", f"{c/reported_max:.3f}", f"{c/adult:.3f}")
            for ref, prep, c in (("Bertino Fig. 7", "nominal FLVCR1 fibroblast medium", 5000),
                                ("Shimura Fig. 3B", "nominal normal fibroblast medium", 50),
                                ("Shimura Fig. 3B", "nominal normal fibroblast medium", 200))]
    write_tsv(output / "exposure_bridge.tsv", ("source", "preparation", "nominal_ALA_uM", "over_Leigh_mean_total_peak",
              "over_highest_Leigh_total_peak", "over_adult_surgical_total_peak"), rows)
    write_tsv(output / "plasma_inputs.tsv", ("source", "n", "mean_or_geomean_uM", "SD_uM", "min_uM", "max_uM"),
              [("Leigh exploratory Table 3", n, peak, sd, reported_low, reported_max),
               ("PMDA adult surgical product review", 12, f"{adult:.3f}", "NA", "NA", "NA")])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    for row in read_tsv("source_inputs.tsv"):
        if sha256((args.sources / row["file"]).read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"Source mismatch: {row['file']}")
    args.out.mkdir(parents=True, exist_ok=True)
    figure7(args.sources, args.out)
    factorial(args.out)
    leigh(args.sources, args.out)
    exposure(args.sources, args.out)


if __name__ == "__main__":
    main()
