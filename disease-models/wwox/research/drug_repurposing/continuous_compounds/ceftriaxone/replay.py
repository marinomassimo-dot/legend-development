"""Reproduce clinical exposure and safety contrasts plus a two-site clearance counterexample."""
import argparse
import csv
import hashlib
from pathlib import Path
import re
from xml.etree import ElementTree

HERE = Path(__file__).resolve().parent


def rows(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write(output, name, fields, values):
    with (output / f"{name}.tsv").open("w", newline="") as handle:
        table = csv.writer(handle, delimiter="\t", lineterminator="\n")
        table.writerow(fields.split())
        table.writerows(values)


def read_text(element):
    return " ".join("".join(element.itertext()).split())


def local_primary(source, output):
    body = ElementTree.parse(source / "PMC8032948.xml").findall("./body//p")
    paragraphs = [read_text(line) for line in body]
    values = []
    for region, figure in (("hippocampus", 1), ("cortex", 2), ("striatum", 3)):
        def extract(panel):
            marker = f"Figure {figure}{panel}, saline n = "
            sentence = next(s for s in paragraphs if marker in s)
            chunk = sentence.split(marker, 1)[1].split(").", 1)[0]
            samples = re.match(r"(\d+), ceftriaxone n = (\d+)", chunk)
            if panel == "A":
                result = re.search(r"\bp = ([\d.]+)", chunk)
            else:
                result = re.search(r"treatment p = ([\d.]+)", chunk)
            return samples.group(1), samples.group(2), result.group(1)

        for panel, endpoint, unit in (("A", "total_GLT1", "animals"),
                                       ("F", "peak_iGluSnFR", "slices"),
                                       ("G", "decay_tau", "slices")):
            values.append((region, endpoint, unit, *extract(panel), f"Fig. {figure}{panel}"))
    write(output, "healthy_mouse", "region endpoint unit control_n treated_n reported_p locator", values)


def compare_exposure(output, data):
    # 554.6 g/mol is the parent ceftriaxone moiety. 1 mg/L is 1000 / 554.6 micromolar.
    molecular_mass = 554.6
    cell_nominal = data["Lee_HFA", "ceftriaxone_exposure"]
    values = []
    for item in rows(HERE / "inputs.tsv"):
        if item["unit"] not in ("mg/L", "uM"):
            continue
        original = float(item["value"])
        micromolar = 1000 * original / molecular_mass if item["unit"] == "mg/L" else original
        values.append((item["context"], item["measure"], original, item["unit"],
                       f"{micromolar:.3f}", f"{micromolar / cell_nominal:.3f}", item["locator"]))
    write(output, "exposure", "context measure original_value original_unit micromolar "
          "ratio_to_HFA_nominal locator", values)


def compare_aggregate(output, data):
    n_active = int(data["ALS_phase3", "n_active"])
    n_placebo = int(data["ALS_phase3", "n_placebo"])
    values = []
    for event in ("cholelithiasis", "serious_hepatobiliary"):
        x = int(data["ALS_phase3", event + "_active"])
        y = int(data["ALS_phase3", event + "_placebo"])
        active_pct, placebo_pct = 100 * x / n_active, 100 * y / n_placebo
        values.append((event, x, n_active, y, n_placebo, f"{active_pct:.2f}",
                       f"{placebo_pct:.2f}", f"{active_pct - placebo_pct:.2f}"))
    write(output, "als_safety", "event treated_n treated_total placebo_n placebo_total "
          "treated_pct placebo_pct absolute_difference_pp", values)
    wt = data["R6_2_slope", "WT_saline"]
    treated = data["R6_2_slope", "KO_treated"]
    write(output, "striatum_no_net_flux", "WT_saline_slope R6_2_treated_slope "
          "ratio_of_means WT_change_pct R6_2_change_pct",
          [(wt, treated, f"{treated / wt:.3f}",
            data["R6_2_uptake", "WT_change"], data["R6_2_uptake", "KO_change"])])


def replay_geometry(output):
    # Unit-volume compartments. Integrated dN/dt = -(uptake + dispersion) N after
    # an input pulse. Integrated dF/dt = dispersion * N - far_clearance * F.
    far_clearance = 4.0
    values = []
    for name, amount, uptake, dispersion in (
        ("baseline", 1.0, 8.0, 4.0),
        ("greater_near_uptake", 1.0, 12.0, 4.0),
        ("greater_dispersion", 1.0, 8.0, 8.0),
        ("less_input", 0.75, 8.0, 4.0),
    ):
        tau_s = 1 / (uptake + dispersion)
        area_near = amount * tau_s
        area_far = dispersion * area_near / far_clearance
        values.append((name, amount, uptake, dispersion, far_clearance, f"{1000 * tau_s:.2f}",
                       f"{area_near:.5f}", f"{area_far:.5f}", f"{uptake * area_near:.5f}"))
    write(output, "geometry_counterexample", "scenario normalized_input near_uptake_per_s "
          "dispersion_per_s far_loss_per_s near_tau_ms near_AUC_normalized_s far_AUC_normalized_s "
          "normalized_mass_cleared_near", values)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    for row in rows(HERE / "sources.tsv"):
        if row["file"]:
            raw = (args.sources / row["file"]).read_bytes()
            if hashlib.sha256(raw).hexdigest() != row["sha256"]:
                raise ValueError(f"Source checksum mismatch: {row['file']}")
    args.output.mkdir(parents=True, exist_ok=True)
    data = {(row["context"], row["measure"]): float(row["value"]) for row in rows(HERE / "inputs.tsv")}
    local_primary(args.sources, args.output)
    compare_exposure(args.output, data)
    compare_aggregate(args.output, data)
    replay_geometry(args.output)


if __name__ == "__main__":
    main()
