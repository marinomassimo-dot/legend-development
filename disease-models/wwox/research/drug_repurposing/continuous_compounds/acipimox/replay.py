"""Replay acipimox concentration scales, reported outcomes and WWOX RNA contrasts."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(COMPOUNDS / name) for name in ("sodium_benzoate", "jbpos0101")]
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified_expression

MOLAR_MASS = 154.12
NAD_PANEL = ("Naprt", "Nampt", "Nmnat1", "Nmnat2", "Nmnat3", "Nadsyn1", "Sarm1", "Hcar2", "Slc25a51")


def axis_value(y, zero, tick, at_tick):
    return (zero - y) * at_tick / (zero - tick)


def ratios():
    # Van de Weijer 2015, Abstract and Fig. 4C text. Arithmetic on means only.
    yield "adult T2D crossover", "plasma NEFA", 759, 1135, "umol/L", f"{100 * (1135 / 759 - 1):.2f}"
    yield "adult T2D crossover", "muscle ATP luminescence", 35.2, 70.0, "RLU/mg protein", f"{100 * (70 / 35.2 - 1):.2f}"
    # Fig. 5, PDF page 8, pdftoppm -scale-to 1600. Bars exclude error bars.
    for metric, zero, tick, top, control_y, acipimox_y, unit in (
        ("NAD plus at 3 h", 373, 200, 3, 291, 235, "umol/L assay"),
        ("basal respiration at 24 h", 744, 526, 100, 696, 684, "pmol O2/s/mL"),
        ("FCCP respiration at 24 h", 744, 526, 100, 607, 555, "pmol O2/s/mL"),
    ):
        control = axis_value(control_y, zero, tick, top)
        treated = axis_value(acipimox_y, zero, tick, top)
        yield "C2C12 Figure 5 approximate", metric, f"{control:.3f}", f"{treated:.3f}", unit, f"{100 * (treated / control - 1):.2f}"


def adult_exposure():
    # Efthymiopoulos 1993, primary abstract following a single oral exposure.
    for role, mass in (("range minimum", 2.56), ("mean", 5.74), ("range maximum", 8.38)):
        total_um = 1000 * mass / MOLAR_MASS
        yield role, mass, f"{total_um:.3f}", f"{10000 / total_um:.2f}"


def brain_plot():
    # Shen 2022 Fig. 5 raster 3692×1070 and Fig. 4 raster 2283×1449.
    # Matched group/time means; no individual PK or tissue dilution inferred.
    for arm, time, tissue_zero, tissue_25, tissue_top, plasma_point in (
        ("normoxia", 1, 937, 206, 926, 747),
        ("normoxia", 2, 937, 206, 930, 903),
        ("hypoxia", 1, 936, 197, 928, 286),
        ("hypoxia", 2, 936, 197, 930, 531),
    ):
        brain = axis_value(tissue_top, tissue_zero, tissue_25, 25)
        plasma = axis_value(plasma_point, 1184, 121, 20)
        yield arm, time, tissue_zero, tissue_25, tissue_top, plasma_point, f"{brain:.3f}", f"{plasma:.3f}", f"{brain/plasma:.4f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="Directory with pinned GEO source files")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "replayed_contrasts.tsv", "preparation readout control acipimox unit change_percent_vs_control".split(), ratios())
    tsv(args.output / "adult_exposure.tsv", "plasma_cmax_statistic ug_mL total_uM ratio_10mM_to_total_plasma".split(), adult_exposure())
    tsv(args.output / "rat_figures.tsv", "oxygen_group time_h brain_zero_y brain_25_y brain_bar_y plasma_point_y brain_homogenate_ug_mL plasma_ug_mL matrix_quotient".split(), brain_plot())
    verified_expression(args.files)
    tsv(args.output / "wwox_nad_bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, NAD_PANEL))
    tsv(args.output / "wwox_nad_nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, NAD_PANEL))


if __name__ == "__main__":
    main()
