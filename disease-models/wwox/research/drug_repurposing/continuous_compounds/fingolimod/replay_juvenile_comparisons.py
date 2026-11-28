"""Replay the four-arm figure and annotated cross-context contrasts."""

import argparse
from hashlib import sha256
from pathlib import Path
from statistics import mean
from subprocess import check_output, run
from tempfile import TemporaryDirectory

import numpy as np


PDF_DIGEST = "d00e406ea093a8db44a6fc17c76c4ae7d9f42b2bcc1cfeefca19bcdd869d7e81"
PHOSPHATE_MW = 387.5  # g/mol, PubChem CID 11452022


def figure_means(pdf):
    if sha256(pdf.read_bytes()).hexdigest() != PDF_DIGEST:
        raise ValueError("Expected the pinned PMC6371042 PDF.")
    with TemporaryDirectory() as directory:
        prefix = Path(directory) / "figure3"
        run(["pdfimages", "-j", "-f", "6", "-l", "6", str(pdf), str(prefix)], check=True)
        pixels = check_output(["convert", str(prefix) + "-000.jpg", "-depth", "8", "rgb:-"])

    image = np.frombuffer(pixels, dtype=np.uint8).reshape(2087, 1547, 3).astype(int)
    red, green, blue = image.transpose(2, 0, 1)
    vehicle = (blue > 82) & (blue > red + 45) & (blue > green + 45)
    parent = (red > 160) & (red > green + 65) & (green > blue + 30)
    magenta = (red > 50) & (blue > green + 38) & (red > green + 37)
    groups = (
        ("vehicle", 1067, 1150, vehicle),
        ("fingolimod", 1190, 1274, parent),
        ("neural_stem_cells", 1313, 1397, magenta),
        ("combination", 1436, 1521, magenta),
    )

    # Read the long mean line and ignore the narrower cap and observation marks.
    tick_dark = np.all(image[:, 1038:1045] < 115, axis=2).sum(axis=1) >= 6
    upper = mean(y for y in range(437, 450) if tick_dark[y])
    lower = mean(y for y in range(752, 763) if tick_dark[y])
    for group, start, end, color in groups:
        coverage = color[445:715, start:end].sum(axis=1)
        center = mean(np.flatnonzero(coverage == coverage.max()).tolist()) + 445
        percentage = 60 + 40 * (lower - center) / (lower - upper)
        yield group, percentage


def contrasts(pdf):
    means = dict(figure_means(pdf))
    for group, value in means.items():
        yield "Zhang_2019_Fig3C_mean_" + group, value, "percent"
    parent_effect = means["fingolimod"] - means["vehicle"]
    combined_effect = means["combination"] - means["neural_stem_cells"]
    yield "Zhang_2019_Fig3C_fingolimod_minus_vehicle", parent_effect, "percentage_point"
    yield "Zhang_2019_Fig3C_combination_minus_neural_stem_cells", combined_effect, "percentage_point"
    yield "Zhang_2019_Fig3C_descriptive_additive_interaction", combined_effect - parent_effect, "percentage_point"
    yield "Bechet_2020_Fig1C_twitcher_MBP_fingolimod_over_vehicle", 94.66 / 47.51, "ratio"
    yield "Bechet_2020_Fig1C_twitcher_MOG_fingolimod_over_vehicle", 82.75 / 59.97, "ratio"
    yield "Slowik_2015_Table2_acute_PLP_fingolimod_minus_vehicle", 81.6 - 86.4, "percentage_point"
    yield "Slowik_2015_Table2_acute_LFB_fingolimod_minus_vehicle", 66.3 - 50.9, "percentage_point"
    yield "Slowik_2015_Fig3C_acute_APP_fingolimod_over_vehicle", 104 / 215, "ratio"
    yield "Foster_2007_Table3_rat_CSF_total_phosphate", 0.23 * 1000 / PHOSPHATE_MW, "nM"
    yield "Foster_2007_Table3_rat_plasma_total_phosphate", 7.35 * 1000 / PHOSPHATE_MW, "nM"
    yield "FDA_label_pediatric_MS_total_phosphate", 1.10 * 1000 / PHOSPHATE_MW, "nM"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article_pdf", type=Path, help="PMC6371042 PDF as listed in the dossier")
    print("contrast\tvalue\tunit")
    for contrast, value, unit in contrasts(parser.parse_args().article_pdf):
        print(f"{contrast}\t{value:.4f}\t{unit}")
