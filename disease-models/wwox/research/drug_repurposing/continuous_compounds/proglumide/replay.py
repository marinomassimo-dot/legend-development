"""Reproduce the proglumide concentration comparisons and WWOX CCK RNA screen."""

import argparse
from pathlib import Path
import sys

COMPOUNDS = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(COMPOUNDS / name) for name in ("sodium_benzoate", "jbpos0101")]
from coagonist_screen import bulk_panel, nuclei_panel, tsv
from replay_exposure_and_receptors import verified_expression

MOLAR_MASS = 334.41
PANEL = ("Cck", "Cckar", "Cckbr")

# Hsu 2022 Results §3.3, Fig. 3B. n recovered by summing Table 1 categories.
ADULT_SERUM = (("control", 4, 7847), ("Child-Pugh A", 4, 9721), ("Child-Pugh B", 3, 10635))

# Jensen 1994 Table 3 and Deschodt-Lanckman 1982 Discussion, Fig. 4.
ASSAY_SCALE = (
    ("human CCK1 competition IC50", 660),
    ("human CCK2 competition IC50", 4130),
    ("rat unsulfated CCK8 cleavage apparent Ki", 1300),
    ("rat sulfated CCK8 cleavage Fig4 condition", 2000),
)


def axis_value(pixel, zero, tick, value_at_tick):
    return value_at_tick * (zero - pixel) / (zero - tick)


def comparisons():
    for group, n, ng_ml in ADULT_SERUM:
        total_um = ng_ml / MOLAR_MASS
        for assay, scale_um in ASSAY_SCALE:
            yield "adult_serum_vs_assay", group, n, assay, f"{total_um:.3f}", scale_um, f"{scale_um / total_um:.2f}"

    # Sakatani 1989 Fig. 5, PDF page 6, pdftoppm -scale-to 1350.
    for site, n, csf_point, serum_point in (("third ventricle", 6, 232, 449), ("lateral ventricle", 4, 241, 424)):
        csf_um = axis_value(csf_point, 362, 234, 100) * 1000 / MOLAR_MASS
        serum_um = axis_value(serum_point, 668, 412, 1000) * 1000 / MOLAR_MASS
        yield "dog_CSF_vs_serum", site, n, "180 min", f"{csf_um:.3f}", f"{serum_um:.3f}", f"{csf_um / serum_um:.3f}"
        for assay, scale_um in ASSAY_SCALE:
            yield "dog_CSF_vs_assay", site, n, assay, f"{csf_um:.3f}", scale_um, f"{scale_um / csf_um:.2f}"


def cleavage_graph_results():
    # Deschodt-Lanckman 1982 Fig. 4, PDF page 6, pdftoppm -scale-to 1200.
    # Use the 180-min zero at the corresponding x; both comparisons are within matrix.
    for tissue, zero, vehicle, drug in (("brain", 396, 182, 263), ("pancreas", 396, 350, 352)):
        yield tissue, zero, vehicle, drug, f"{100 * (drug - vehicle) / (zero - vehicle):.1f}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path, help="Directory with pinned GEO source files")
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tsv(args.output / "concentration_comparisons.tsv",
        "comparison cohort n assay reference_uM comparator_uM labeled_ratio".split(), comparisons())
    tsv(args.output / "cleavage_graph.tsv",
        "preparation zero_pixel_y control_pixel_y treated_pixel_y decrease_percent_at_180_min".split(),
        cleavage_graph_results())
    verified_expression(args.files)
    tsv(args.output / "wwox_cck_bulk.tsv",
        "model accession gene ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        bulk_panel(args.files, PANEL))
    tsv(args.output / "wwox_cck_nuclei.tsv", "pool cell_class gene nuclei all_UMI gene_UMI CPM".split(),
        nuclei_panel(args.files, PANEL))


if __name__ == "__main__":
    main()
