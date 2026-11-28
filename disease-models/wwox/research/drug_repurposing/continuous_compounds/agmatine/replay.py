"""Replay rat distribution arithmetic and a two-blocker identifiability check."""
import argparse
import csv
import math
from pathlib import Path


def write_tsv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(fields)
        writer.writerows(rows)


def exposure(output):
    mass = 130.19  # Parent measured by the assay. The sulfate salt has a different mass.
    peaks = (
        ("rat IV terminal plasma", 59278, "ng/mL", "µmol/L", 15),
        ("rat IV terminal brain", 3138, "ng/g", "µmol/kg", 15),
        ("rat IV terminal spinal cord", 814, "ng/g", "µmol/kg", 120),
        ("rat oral serial plasma, lower source arm", 4730, "ng/mL", "µmol/L", 23.6),
        ("rat oral serial plasma, higher source arm", 14494, "ng/mL", "µmol/L", 45),
    )
    rows = [(label, peak, native, f"{peak / mass:.4f}", units, time)
            for label, peak, native, units, time in peaks]
    write_tsv(output / "rat_exposure.tsv",
              ("condition", "peak", "mass_units", "converted", "molar_units", "tmax_min"), rows)
    plasma_peak, brain_peak = peaks[0][1], peaks[1][1]
    ratios = (
        ("brain/plasma at common sampled Tmax", brain_peak, plasma_peak),
        ("brain/plasma using reported AUCs", 25246, 63658),
        ("spinal/plasma using reported AUCs", 18718, 63658),
    )
    write_tsv(output / "rat_partition.tsv", ("comparison", "tissue", "plasma", "ratio_mL_g"),
              [(k, n, d, f"{n / d:.6f}") for k, n, d in ratios])
    return brain_peak / mass


def voltage_sensitivity(output, illustrative_parent):
    # V in mV, magnesium in mM, and free parent/Kd in µM. Reference thermal voltage at 25 °C.
    rows = []
    for charge in (1, 2):
        for mg_mm in (0, 1):
            for cu in (1, illustrative_parent, 100, 300):
                for v in (-65, -35):
                    kd = 952 * math.exp(charge * 0.62 * v / 25.69)
                    ag = cu / kd
                    mg = mg_mm * math.exp(-0.062 * v) / 3.57

                    # Equal agonist conductance and reversal at 0 mV in both windows.
                    baseline = abs(v) / (1 + mg)
                    independent = baseline / (1 + ag)
                    exclusive = abs(v) / (1 + mg + ag)
                    metrics = (
                        cu, kd, baseline,
                        100 * (1 - independent / baseline), baseline - independent,
                        100 * (1 - exclusive / baseline), baseline - exclusive,
                    )
                    rows.append((charge, mg_mm, v, *(f"{value:.6f}" for value in metrics)))
    write_tsv(
        output / "voltage_replay.tsv",
        ("effective_charge", "Mg_mM", "Vm_mV", "illustrative_parent_uM", "apparent_Kd_uM",
         "baseline_current_arb", "independent_block_pct", "independent_current_loss_arb",
         "exclusive_block_pct", "exclusive_current_loss_arb"),
        rows,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    output = parser.parse_args().output
    output.mkdir(parents=True, exist_ok=True)
    # Borrow only the numerical value from µmol/kg as an illustrative bath input.
    # This is neither an extracellular conversion nor a bound on brain exposure.
    voltage_sensitivity(output, exposure(output))


if __name__ == "__main__":
    main()
