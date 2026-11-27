"""Reproduce metformin exposure comparisons and the WWOX AMPK expression check."""

import argparse
from collections import defaultdict
import csv
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
METFORMIN_PARENT_MASS = 129.16
METFORMIN_HCL_MASS = 165.62
GENES = (
    "Prkaa1", "Prkaa2", "Prkab1", "Prkab2", "Prkag1", "Stk11",
    "Camkk2", "Psenen", "Atp6ap1", "Acaca", "Acacb", "Rptor",
    "Slc22a1", "Slc22a2", "Slc22a3", "Slc29a4", "Slc47a1", "Slc47a2",
    "Myrf", "Mbp", "Plp1", "Ugt8",
)
NUCLEAR_GENES = ("Psenen", "Atp6ap1", "Acaca", "Acacb", "Prkaa1", "Prkaa2", "Prkab1", "Prkab2")


def ng_per_ml_to_um(value, mass=METFORMIN_PARENT_MASS):
    return value / mass


def exposure_rows():
    # Koenig et al., Results, CSF collection and analysis, week 8 fasting.
    for matrix, amount in (("plasma", 951.9), ("CSF", 95.6)):
        yield "Koenig", "week 8 fasting", matrix, ng_per_ml_to_um(amount), "µM parent equivalent"
    yield "Koenig", "week 8 fasting", "CSF/plasma ratio of means", 100 * 95.6 / 951.9, "%"
    yield (
        "Koenig", "week 8 fasting", "CSF if mass expressed as HCl",
        ng_per_ml_to_um(95.6, METFORMIN_HCL_MASS), "µM salt-equivalent sensitivity",
    )

    for bath, context in (
        (5, "Ma primary mouse hepatocytes"),
        (10, "Mohammadnia human oligodendroglia"),
        (200, "Narine rodent OL lower bath"),
        (1000, "Narine rodent OL highest bath"),
    ):
        yield (
            context, "Koenig mean CSF reference", "nominal bath / adult CSF",
            bath / ng_per_ml_to_um(95.6), "fold",
        )

    # Chaudhari et al., Table 3, adult saline-perfused whole brain and paired plasma.
    for arm, brain, plasma in (
        ("male day 7", 438.3, 2385),
        ("male day 30", 509.9, 2926),
        ("female day 7", 431.2, 1679),
        ("female day 30", 675.1, 2853),
    ):
        yield "Chaudhari", arm, "total perfused whole-brain parent", brain / METFORMIN_PARENT_MASS, "µmol/kg wet tissue"
        yield "Chaudhari", arm, "total brain / plasma ratio of means", brain / plasma, "mL/g"

    # Sharma et al., final Results §§3.7–3.8, Figs. 3–4; adult mouse perfused region and CSF.
    for arm, brain, csf in (
        ("90 mg/kg at 30 min", 1.04, .09),
        ("150 mg/kg at 30 min", 1.83, .11),
        ("30 mg/kg at 120 min", .17, .0036),
        ("90 mg/kg at 120 min", .61, .038),
        ("150 mg/kg at 120 min", 1.21, .024),
    ):
        yield "Sharma", arm, "brain in reported volume units", ng_per_ml_to_um(1000 * brain), "µM reported-volume equivalent"
        yield "Sharma", arm, "CSF", ng_per_ml_to_um(1000 * csf), "µM parent equivalent"
        yield "Sharma", arm, "brain / CSF ratio of means", brain / csf, "reported-volume quotient"

    # Azmi et al., Fig. 3D legend; 480 axons may denote the per-mouse control number.
    yield "Azmi", "P14 metformin", "sampled-field density", 561 / 5685, "axon profiles/µm²"
    for counts in (480, 2 * 480):
        yield "Azmi", f"P14 control if {counts} total profiles", "sampled-field density", counts / 5358, "axon profiles/µm²"


def nuclear_weighting(rows):
    # The UMI-weighted decomposition applies to the assigned subset of two pooled libraries.
    counts = defaultdict(dict)
    for pool, cell_class, symbol, _, depth, gene_count, _ in rows:
        counts[symbol, pool][cell_class] = depth, gene_count
    for symbol in sorted({symbol for symbol, _ in counts}):
        control, knockout = counts[symbol, "ctrl"], counts[symbol, "ko"]
        if control.keys() != knockout.keys():
            raise ValueError("Mismatched nuclear marker classes")
        control_total = sum(depth for depth, _ in control.values())
        knockout_total = sum(depth for depth, _ in knockout.values())
        control_cpm = knockout_cpm = weight_change = within_change = 0.0
        for cell_class, (control_depth, control_count) in control.items():
            knockout_depth, knockout_count = knockout[cell_class]
            cpm_c = 1e6 * control_count / control_depth
            cpm_k = 1e6 * knockout_count / knockout_depth
            weight_c = control_depth / control_total
            weight_k = knockout_depth / knockout_total
            control_cpm += cpm_c * weight_c
            knockout_cpm += cpm_k * weight_k
            weight_change += (weight_k - weight_c) * (cpm_c + cpm_k) / 2
            within_change += (weight_k + weight_c) * (cpm_k - cpm_c) / 2
        delta = knockout_cpm - control_cpm
        assert abs(delta - weight_change - within_change) < 1e-8
        yield symbol, *(f"{value:.3f}" for value in (control_cpm, knockout_cpm, weight_change, within_change, delta))


def expression_replay(files, out):
    sys.path.insert(0, str(HERE.parent / "jbpos0101"))
    from replay_exposure_and_receptors import bulk_panel, nuclei_panel, tsv, verified_expression

    verified_expression(files)
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "wwox_ampk_bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(files, GENES))
    nuclei = list(nuclei_panel(files, NUCLEAR_GENES))
    tsv(out / "wwox_ampk_nuclear_coverage.tsv", "pool class gene nuclei all_UMI gene_UMI CPM".split(), nuclei)
    tsv(out / "wwox_ampk_nuclear_weighting.tsv",
        "gene ctrl_assigned_CPM ko_assigned_CPM mixture_weight_delta within_class_delta raw_delta".split(),
        nuclear_weighting(nuclei))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expression", type=Path, help="Root directory of the held expression and annotation files")
    parser.add_argument("--out", type=Path, default=HERE, help="Output directory for the WWOX RNA comparison")
    args = parser.parse_args()
    if args.expression:
        expression_replay(args.expression, args.out)
        return
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "condition", "measure", "value", "unit"))
    writer.writerows((source, condition, measure, f"{value:.4f}", unit)
                     for source, condition, measure, value, unit in exposure_rows())


if __name__ == "__main__":
    main()
