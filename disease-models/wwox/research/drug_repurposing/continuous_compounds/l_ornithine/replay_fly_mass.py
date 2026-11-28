"""Screen an exact-mass ion in the held MTBLS12344 positive-mode spectra."""
import argparse
import csv
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np

MASS = 117.053826475 + 1.007276466621


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("leucine_tools", type=Path)
    parser.add_argument("spectra_dir", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    spec = spec_from_file_location("extractor", args.leucine_tools / "fly_leucine_eic.py")
    extract = module_from_spec(spec)
    spec.loader.exec_module(extract)
    extract.MASS = MASS

    with (args.leucine_tools / "fly_assay_crosswalk.tsv").open() as handle:
        sample_rows = [row for row in csv.DictReader(handle, delimiter="\t")
                       if row["polarity"] == "positive" and row["assay"].endswith("_KDExp")]
    samples = [row["derived_stem"] for row in sample_rows]
    pools = sorted(p.stem for p in args.spectra_dir.glob("pooled_*.mzXML"))
    blanks = sorted(p.stem for p in args.spectra_dir.glob("matrix_blank_*.mzXML"))
    assert len(samples) == len(set(samples)) == 20 and len(pools) == 12 and len(blanks) == 6
    expected = {}
    for name in ("fly_leucine_qc.tsv", "fly_leucine_sample_inputs.tsv"):
        with (args.leucine_tools / name).open() as handle:
            expected.update({row["stem"]: row["sha256"] for row in csv.DictReader(handle, delimiter="\t")})

    def read_spectrum(stem):
        path = args.spectra_dir / f"{stem}.mzXML"
        if sha256(path.read_bytes()).hexdigest() != expected[stem]:
            raise ValueError(f"Unexpected held spectrum fingerprint for {stem}")
        return extract.spectra(path, stem)

    data = {name: read_spectrum(name) for name in pools + blanks}
    start = max(data[name][0][0] for name in pools + blanks)
    stop = min(data[name][0][-1] for name in pools + blanks)
    grid = np.arange(np.ceil(start) + 20, np.floor(stop) - 19, 1)
    trace = np.median([np.interp(grid, *data[name][:2]) for name in pools], axis=0)
    found = np.flatnonzero((trace[1:-1] > trace[:-2]) & (trace[1:-1] >= trace[2:])) + 1
    centers = []
    for i in sorted(found, key=lambda j: (-trace[j], grid[j])):
        if all(abs(grid[i] - other) >= 30 for other in centers):
            centers.append(grid[i])

    args.out.mkdir(exist_ok=True)
    peak_rows = []
    passed = []
    for center in sorted(centers):
        supporting = sum(np.count_nonzero(s[(r >= center-15) & (r <= center+15)]) >= 3
                         for r, s, _ in (data[name] for name in pools))
        pooled = float(np.median([extract.integration(data[name], center) for name in pools]))
        blank = float(np.median([extract.integration(data[name], center) for name in blanks]))
        good = supporting >= 6 and pooled > 0 and pooled >= 3 * blank
        peak_rows.append((center, supporting, f"{pooled:.7g}", f"{blank:.7g}", good))
        if good:
            passed.append(center)
    extract.save(args.out / "fly_mass_qc.tsv",
                 ("peak_s", "supporting_pools_of_12", "pool_median_area", "blank_median_area", "pass"),
                 peak_rows)

    contrasts = []
    if passed:
        for stem in samples:
            data[stem] = read_spectrum(stem)
        for center in passed:
            for offset in (0, -5, 5):
                groups = {}
                for row in sample_rows:
                    dt = data[row["derived_stem"]]
                    area = extract.integration(dt, center, offset)
                    groups.setdefault((row["background"], row["wwox_arm"]), []).append((area, area / dt[2]))
                for background in ("LacZ", "AB42"):
                    ctrl = np.asarray(groups[background, "RNAi Control"])
                    kd = np.asarray(groups[background, "Wwox RNAi"])
                    assert len(ctrl) == len(kd) == 5
                    for j, mode in enumerate(("area", "area_over_TIC")):
                        good = np.all(ctrl[:, j] > 0) and np.all(kd[:, j] > 0)
                        result = extract.contrast(ctrl[:, j], kd[:, j]) if good else ("NA",) * 4
                        contrasts.append((center, offset, background, mode,
                                          sum(ctrl[:, j] > 0), sum(kd[:, j] > 0), *result))
    extract.save(args.out / "fly_mass_contrasts.tsv",
                 ("peak_s", "offset_s", "background", "normalization", "control_nonzero_of_5",
                  "KD_nonzero_of_5", "KD_over_control", "leave_one_out_min", "leave_one_out_max",
                  "unadjusted_permutation_p"), contrasts)
    print(f"m/z {MASS:.9f}, {len(centers)} nonoverlapping pooled maxima, {len(passed)} pass QC")


if __name__ == "__main__":
    main()
