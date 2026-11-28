"""Re-extract the standard-assigned leucine feature from positive mzXML."""
import argparse
import base64
import csv
import hashlib
from itertools import combinations
import json
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zlib

import numpy as np


MASS = 132.1019
TARGET_RT = 587.2
PPM = 5e-6


def metadata(path):
    with path.open() as stream:
        return json.load(stream)["data"]["rows"]


def assay_map(sample_path, positive_path, negative_path):
    samples = {row["Sample Name"]: row for row in metadata(sample_path)
               if row["Characteristics[Sample type]"] == "experimental sample"}
    mappings = []
    audit = []
    for label, path in (("positive", positive_path), ("negative", negative_path)):
        names = {}
        for row in metadata(path):
            name = row["MS Assay Name"]
            stem = Path(row["Derived Spectral Data File"]).stem
            names[name] = stem
            if name in samples:
                expected = name.split("_")[0]
                raw_stem = Path(row["Raw Spectral Data File"]).stem
                assert name == row["Extract Name"] and stem == raw_stem == expected
                audit.append((label, name, row["Sample Name"], row["Extract Name"],
                              raw_stem, stem, samples[name]["Factor Value[Wwox manipulation]"],
                              samples[name]["Factor Value[Amyloid]"]))
        mappings.append(names)
    for name in samples:
        assert mappings[0][name] == mappings[1][name]
    return samples, mappings[0], audit


def spectra(path, stem, *, target_mass=MASS):
    captured = []
    for _, scan in ET.iterparse(path):
        if not scan.tag.endswith("}scan") and scan.tag != "scan":
            continue
        if scan.attrib["msLevel"] == "1" and scan.attrib.get("polarity") == "+":
            retention = re.fullmatch(r"PT(\d+(?:\.\d+)?)S", scan.attrib["retentionTime"])
            assert retention, stem
            peaks = next((child for child in scan if child.tag.endswith("peaks")), None)
            if peaks is not None and peaks.text:
                blob = base64.b64decode(peaks.text)
                compression = peaks.attrib.get("compressionType", "none")
                if compression == "zlib":
                    blob = zlib.decompress(blob)
                else:
                    assert compression == "none", (stem, compression)
                byte_order = peaks.attrib.get("byteOrder", "network")
                assert byte_order in {"network", "big", "little"}
                precision = int(peaks.attrib["precision"])
                assert precision in {32, 64}
                assert peaks.attrib.get("pairOrder", "m/z-int") == "m/z-int"
                endian = "<" if byte_order == "little" else ">"
                arr = np.frombuffer(blob, dtype=f"{endian}f{precision // 8}").reshape(-1, 2)
                masses, signal = arr.T
                in_window = np.abs(masses / target_mass - 1) <= PPM
                signal_sum = float(signal.astype(float).sum())
                total = float(scan.attrib.get("totIonCurrent", signal_sum))
                captured.append((float(retention.group(1)), float(signal[in_window].astype(float).sum()), total))
        scan.clear()
    rt, intensity, tic = np.asarray(captured, dtype=float).T
    assert len(rt) > 100 and np.all(np.diff(rt) > 0), stem
    return rt, intensity, float(tic.sum())


def ranked(values):
    order = sorted(range(len(values)), key=values.__getitem__)
    rank = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start + 1
        while end < len(order) and values[order[end]] == values[order[start]]:
            end += 1
        for entry in order[start:end]:
            rank[entry] = (start + end - 1) / 2
        start = end
    return rank


def save(path, columns, rows):
    with path.open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)


def integration(data, apex, offset=0):
    retention, intensity, _ = data
    window = (retention >= apex - 15 + offset) & (retention <= apex + 15 + offset)
    assert sum(window) >= 3
    trapezoid = np.trapezoid if hasattr(np, "trapezoid") else np.trapz
    return float(trapezoid(intensity[window], retention[window]))


def contrast(ctrl, kd):
    log_ctrl = np.log2(ctrl)
    log_kd = np.log2(kd)
    effect = float(log_kd.mean() - log_ctrl.mean())
    omitted = [
        *(log_kd.mean() - np.delete(log_ctrl, i).mean() for i in range(len(ctrl))),
        *(np.delete(log_kd, i).mean() - log_ctrl.mean() for i in range(len(kd))),
    ]
    joined = np.concatenate((log_ctrl, log_kd))
    permuted = []
    for selected in combinations(range(len(joined)), len(kd)):
        mask = np.zeros(len(joined), dtype=bool)
        mask[list(selected)] = True
        permuted.append(joined[mask].mean() - joined[~mask].mean())
    p_value = float(np.mean(np.abs(permuted) >= abs(effect) - 1e-12))
    return (2 ** effect, 2 ** min(omitted), 2 ** max(omitted), p_value)


def compare_samples(args, samples, registered, apex, file_for):
    by_arm = {}
    input_rows = []
    areas = []
    for name in sorted(sample for sample in samples if sample.endswith("_KDExp")):
        row = samples[name]
        genotype, background = row["Factor Value[Wwox manipulation]"], row["Factor Value[Amyloid]"]
        data = spectra(file_for(name), registered[name])
        tic = data[2]
        input_rows.append((name, registered[name], hashlib.sha256(file_for(name).read_bytes()).hexdigest()))
        for offset in (0, -5, 5):
            value = integration(data, apex, offset)
            areas.append((name, genotype, background, offset, f"{value:.9g}", f"{tic:.9g}",
                          f"{value / tic:.9g}"))
            by_arm.setdefault((background, offset, genotype), []).append((value, value / tic))
    save(args.out / "fly_leucine_sample_areas.tsv", ("assay", "genotype", "background", "offset_seconds",
         "area", "TIC", "area_over_TIC"), areas)
    save(args.out / "fly_leucine_sample_inputs.tsv", ("assay", "stem", "sha256"), input_rows)

    results = []
    for background in ("LacZ", "AB42"):
        for offset in (0, -5, 5):
            ctrl = np.asarray(by_arm[background, offset, "RNAi Control"])
            kd = np.asarray(by_arm[background, offset, "Wwox RNAi"])
            assert len(ctrl) == len(kd) == 5
            for col, label in enumerate(("area", "area_over_TIC")):
                if np.all(ctrl[:, col] > 0) and np.all(kd[:, col] > 0):
                    values = [f"{item:.6g}" for item in contrast(ctrl[:, col], kd[:, col])]
                else:
                    values = [""] * 4
                results.append((background, offset, label, len(ctrl), len(kd), *values))
    save(args.out / "fly_leucine_contrasts.tsv",
         ("background", "offset_seconds", "normalization", "control_n", "KD_n",
          "KD_over_control", "omit_min_ratio", "omit_max_ratio", "two_sided_permutation_P"), results)


def run(args):
    args.out.mkdir(exist_ok=True, parents=True)
    samples, registered, crosswalk = assay_map(args.samples, args.positive, args.negative)
    save(args.out / "fly_assay_crosswalk.tsv", ("polarity", "assay", "listed_sample_name",
         "extract", "raw_stem", "derived_stem", "wwox_arm", "background"), crosswalk)
    if args.spectra is None:
        return

    with args.maf.open() as stream:
        assigned, = (row for row in csv.DictReader(stream, delimiter="\t")
                     if row["metabolite_identification"] == "L-Leucine")
    assert float(assigned["mass_to_charge"]) == MASS
    assert float(assigned["retention_time"]) == TARGET_RT

    def file_for(name):
        return args.spectra / (registered[name] + ".mzXML")

    pools = [*("Pool1_" + str(i) for i in range(1, 7)), *("Pool2_" + str(i) for i in range(1, 7))]
    blanks = [f"Matrix_Blank_{i}" for i in range(1, 7)
              if f"Matrix_Blank_{i}" in registered and file_for(f"Matrix_Blank_{i}").exists()]
    assert len(blanks) >= 2
    data = {name: spectra(file_for(name), registered[name]) for name in pools + blanks}
    grid = np.arange(TARGET_RT - 25, TARGET_RT + 25.1, 0.5)
    mean_pooled = np.mean([np.interp(grid, *data[pool][:2]) for pool in pools], axis=0)
    i = int(np.argmax(mean_pooled))
    apex = float(grid[i])
    primary_finite = 0 < i < len(grid) - 1 and mean_pooled[i] > 0
    secondary = [float(mean_pooled[j] / mean_pooled[i]) for j in range(1, len(grid) - 1)
                 if primary_finite and 6 <= abs(grid[j] - apex) <= 15
                 and mean_pooled[j - 1] < mean_pooled[j] >= mean_pooled[j + 1]]
    integrals = {name: integration(data[name], apex) for name in data}
    def qc_rank(names):
        return float(np.corrcoef(ranked([integrals[name] for name in names]),
                                 ranked([float(assigned[name]) for name in names]))[0, 1])

    spearman = qc_rank(pools)
    within_pool_sets = {key: qc_rank([name for name in pools if name.startswith(key)])
                        for key in ("Pool1_", "Pool2_")}
    median_blank = float(np.median([integrals[name] for name in blanks]))
    median_pool = float(np.median([integrals[name] for name in pools]))
    clear_of_blank = median_pool > 0 and median_pool >= 3 * median_blank
    passes = (primary_finite and math.isfinite(spearman) and spearman >= 0.7
              and clear_of_blank and max(secondary, default=0) < 0.3)
    save(args.out / "fly_leucine_qc.tsv", ("name", "stem", "area", "reported_area", "sha256"),
         [(name, registered[name], f"{integrals[name]:.6g}", assigned[name],
           hashlib.sha256(file_for(name).read_bytes()).hexdigest()) for name in data])
    report = {"apex_s": apex, "pools": len(pools), "blanks": len(blanks),
              "median_pool_area": median_pool, "median_blank_area": median_blank,
              "spearman_vs_deposit": spearman if math.isfinite(spearman) else None,
              "spearman_within_pool_label_sets": {key: value if math.isfinite(value) else None
                                                  for key, value in within_pool_sets.items()},
              "strongest_secondary_fraction": max(secondary, default=0),
              "gate_pass": passes}
    (args.out / "fly_leucine_qc.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report))
    if args.compare and passes:
        compare_samples(args, samples, registered, apex, file_for)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("samples", type=Path)
    parser.add_argument("positive", type=Path)
    parser.add_argument("negative", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--maf", type=Path)
    parser.add_argument("--spectra", type=Path)
    parser.add_argument("--compare", action="store_true")
    run(parser.parse_args())
