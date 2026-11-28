"""Replay the specific L-fucose compartment comparisons from primary figures."""

import argparse
from hashlib import sha256
from pathlib import Path
from statistics import mean

import pymupdf

MOLAR_MASS = 164.16
INPUTS = {
    "xu-mmc1.pdf": "a1a8959ca0cf865a269c06b93fdf0cd7c71f9db9c0ec3d369f89ebf2115527b7",
    "sciadv.adt4123-f5.jpg": "6439ad831395ae23b04c9feeb00f81278b9c8223912251aa8375d4febd315cd8",
    "415_2026_14211_Fig2_HTML.png": "a0f97dfe880b3d87fc0c55514b37720a10a28cd69b080ff8882e7bce941c573b",
}


def pinned(directory, filename):
    path = directory / filename
    if sha256(path.read_bytes()).hexdigest() != INPUTS[filename]:
        raise ValueError(f"Unexpected figure edition for {filename}")
    return path


def xu_donor(path):
    # Fig. S2, p. 9. Heights of the first four bars relative to the WT bar.
    with pymupdf.open(path) as source:
        rects = [
            item["rect"] for item in source[8].get_drawings()
            if item["fill"] == (0.0, 0.0, 0.0)
            and 90 < item["rect"].x0 < 169
            and 17 < item["rect"].width < 17.5
            and abs(item["rect"].y1 - 396.45) < 0.03
        ]
    samples = sorted(rects, key=lambda rect: rect.x0)
    if len(samples) != 4:
        raise ValueError("Could not verify the four Fig. S2 bars")
    return [rect.height / samples[0].height for rect in samples]


def forebrain_means(path):
    image = pymupdf.Pixmap(str(path))
    # Panel 5A bars, excluding left and right vertical strokes and the error bars.
    for xmin, xmax, ymin, ymax in (
        (96, 117, 155, 180), (126, 146, 178, 202),
        (181, 201, 124, 151), (211, 229, 148, 175),
    ):
        full_rows = [
            y for y in range(ymin, ymax)
            if all(max(image.pixel(x, y)[:3]) < 100 for x in range(xmin, xmax))
        ]
        if len(full_rows) not in (2, 3):
            raise ValueError(f"Expected an unobscured forebrain bar near x={xmin}")
        # Fig. 5A ordinate ticks at 0 (218.5 px) and 0.4 (52.5 px).
        yield 0.4 * (218.5 - mean(full_rows)) / (218.5 - 52.5)


def highest_csf_point(path):
    image = pymupdf.Pixmap(str(path))
    # Fig. 2C largest labeled-in-teal CSF point. Use core-color pixels.
    rows = [
        y for x in range(1444, 1474) for y in range(106, 137)
        if image.pixel(x, y)[:3] == (102, 146, 162)
    ]
    if not rows:
        raise ValueError("No teal point found in the pinned Fig. 2C region")
    # Fig. 2C ordinate ticks at 0 (440 px) and 6 mg/L (65 px).
    return 6 * (440 - mean(rows)) / (440 - 65)


def rows(inputs):
    for label, value in zip(
        ("WT_vehicle", "Fut8_het_vehicle", "Fut8_het_fucose_lower", "Fut8_het_fucose_higher"),
        xu_donor(pinned(inputs, "xu-mmc1.pdf")), strict=True,
    ):
        yield "Xu_FigS2_brain_GDP_fucose", label, "ratio_to_WT", value
    for label, value in zip(
        ("WT_control_diet", "5xFAD_control_diet", "WT_fucose_diet", "5xFAD_fucose_diet"),
        forebrain_means(pinned(inputs, "sciadv.adt4123-f5.jpg")), strict=True,
    ):
        yield "Di_Lucente_Fig5A_free_fucose", label, "ug_per_mL_extract", value
    # Xu Fig. 1D printed bar labels. Use single core-fucose species and their sum.
    for label, wt, mutant, treated in (
        ("major_core_mono_fucose", 79.5, 57.9, 63.2),
        ("total_core_mono_fucose", 358.9, 277.8, 294.4),
        ("total_core_and_Lewis_di_fucose", 64.4, 54.4, 66.1),
    ):
        yield "Xu_Fig1D_glycan_classes", label, "fraction_of_baseline_deficit_recovered", (
            (treated - mutant) / (wt - mutant)
        )
    peak = highest_csf_point(pinned(inputs, "415_2026_14211_Fig2_HTML.png"))
    for label, mg_l in (
        ("case_baseline_text", 0.48), ("reference_IQR_lower", 0.60),
        ("reference_IQR_upper", 0.84), ("case_highest_plotted_point", peak),
    ):
        yield "Moomann_Fig2C_CSF_free_fucose", label, "micromol_per_L", mg_l * 1000 / MOLAR_MASS
    yield ("CSF_vs_slice_scale_check", "nominal_200_uM_bath_over_case_maximum",
           "concentration_ratio", 200 * MOLAR_MASS / (1000 * peak))


def main(inputs):
    print("source\tcomparison\tunit\tvalue")
    for source, label, unit, value in rows(inputs):
        print(f"{source}\t{label}\t{unit}\t{value:.4f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path)
    main(parser.parse_args().inputs)
