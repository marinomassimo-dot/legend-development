"""Check standard-assigned GPC and replay knockdown contrasts from MTBLS12344."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "l_leucine"))
from fly_leucine_eic import assay_map, contrast, integration, ranked, save, spectra


def replay(metadata_dir, maf_path, spectra_dir, output):
    output.mkdir(parents=True, exist_ok=True)
    samples, stems, _ = assay_map(
        metadata_dir / "s_MTBLS12344.txt",
        metadata_dir / "a_MTBLS12344_LC-MS_alternating_hilic_metabolite_profiling.txt",
        metadata_dir / "a_MTBLS12344_LC-MS_alternating_hilic_metabolite_profiling-1.txt",
    )
    with maf_path.open(newline="") as source:
        header = csv.DictReader(source, delimiter="\t")
        assignment, = (r for r in header
                       if r["metabolite_identification"] == "sn-glycero-3-Phosphocholine")
    assert assignment["reliability"] == "MSI:1"
    mass = float(assignment["mass_to_charge"])
    rt = float(assignment["retention_time"])
    pooled = [f"Pool{group}_{i}" for group in (1, 2) for i in range(1, 7)]
    blanks = [f"Matrix_Blank_{i}" for i in range(1, 7)]

    def spectrum_path(name):
        return spectra_dir / (stems[name] + ".mzXML")

    def extract(name):
        return spectra(spectrum_path(name), stems[name], target_mass=mass)

    qc = {name: extract(name) for name in pooled + blanks}
    grid = np.arange(rt - 25, rt + 25.1, 0.5)
    profile = np.mean([np.interp(grid, *qc[name][:2]) for name in pooled], axis=0)
    summit = int(np.argmax(profile))
    apex = float(grid[summit])
    interior = 0 < summit < len(grid) - 1 and profile[summit] > 0
    secondary = max((float(profile[i] / profile[summit])
                     for i in range(1, len(grid) - 1)
                     if interior and 6 <= abs(grid[i] - apex) <= 15
                     and profile[i - 1] < profile[i] >= profile[i + 1]), default=0)
    areas = {name: integration(data, apex) for name, data in qc.items()}
    pool_area = float(np.median([areas[name] for name in pooled]))
    blank_area = float(np.median([areas[name] for name in blanks]))

    def agreement(names):
        rho = np.corrcoef(ranked([areas[name] for name in names]),
                          ranked([float(assignment[name]) for name in names]))[0, 1]
        return float(rho) if np.isfinite(rho) else None

    rank = agreement(pooled)
    passed = (interior and pool_area > 0 and pool_area >= 3 * blank_area
              and rank is not None and rank >= 0.70 and secondary < 0.30)
    report = {
        "mass": mass, "annotated_rt_s": rt, "apex_s": apex, "gate_pass": bool(passed),
        "pooled_n": len(pooled), "blank_n": len(blanks), "pool_median_area": pool_area,
        "blank_median_area": blank_area, "pooled_spearman": rank,
        "pool1_spearman": agreement(pooled[:6]), "pool2_spearman": agreement(pooled[6:]),
        "secondary_peak_fraction": secondary,
        "filled_experimental_cells_in_maf": sum(bool(assignment[name]) for name in samples),
    }
    (output / "fly_gpc_qc.json").write_text(json.dumps(report, indent=2) + "\n")
    save(output / "fly_gpc_qc.tsv", ("assay", "stem", "area", "reported_area", "sha256"),
         [(name, stems[name], f"{areas[name]:.9g}", assignment[name],
           hashlib.sha256(spectrum_path(name).read_bytes()).hexdigest()) for name in qc])

    if not passed:
        raise SystemExit("GPC peak failed the prespecified pooled and blank checks. See fly_gpc_qc.json.")
    sample_areas(output, samples, stems, extract, spectrum_path, apex)


def sample_areas(output, samples, stems, extract, spectrum_path, apex):
    inputs, rows, by_arm, comparisons = [], [], {}, []
    for name, row in sorted(samples.items()):
        if not name.endswith("_KDExp"):
            continue
        arm = row["Factor Value[Wwox manipulation]"]
        background = row["Factor Value[Amyloid]"]
        data = extract(name)
        inputs.append((name, stems[name], hashlib.sha256(spectrum_path(name).read_bytes()).hexdigest()))
        for shift in (0, -5, 5):
            area = integration(data, apex, shift)
            normalized = area / data[2]
            by_arm.setdefault((background, shift, arm), []).append((area, normalized))
            rows.append((name, background, arm, shift, f"{area:.9g}", f"{data[2]:.9g}",
                         f"{normalized:.9g}"))

    for background in ("LacZ", "AB42"):
        for shift in (0, -5, 5):
            control = np.array(by_arm[background, shift, "RNAi Control"])
            kd = np.array(by_arm[background, shift, "Wwox RNAi"])
            assert len(control) == len(kd) == 5
            for col, label in enumerate(("raw", "TIC_normalized")):
                # A zero-area sample makes this geometric-mean contrast undefined.
                values = ["NA"] * 4
                if np.all(control[:, col] > 0) and np.all(kd[:, col] > 0):
                    values = [f"{estimate:.6f}" for estimate in contrast(control[:, col], kd[:, col])]
                comparisons.append((background, shift, label, len(control), len(kd), *values))

    save(output / "fly_gpc_spectra.tsv", ("assay", "stem", "sha256"), inputs)
    save(output / "fly_gpc_areas.tsv", ("assay", "background", "arm", "shift_s", "area", "TIC",
         "normalized"), rows)
    save(output / "fly_gpc_contrasts.tsv", ("background", "shift_s", "normalization", "control_n",
         "knockdown_n", "KD_over_control", "omit_min", "omit_max", "permutation_p"), comparisons)


if __name__ == "__main__":
    CLI = argparse.ArgumentParser(description=__doc__)
    CLI.add_argument("metadata", type=Path)
    CLI.add_argument("maf", type=Path)
    CLI.add_argument("spectra", type=Path)
    CLI.add_argument("output", type=Path)
    options = CLI.parse_args()
    replay(options.metadata, options.maf, options.spectra, options.output)
