"""Summarize selected windows in Saab et al., Figure 4A,D, and Bakiri Fig. 2C models."""
import argparse
import hashlib
from pathlib import Path
from statistics import mean

import pymupdf

SOURCE_HASH = "3fb70c394894f4a5e0307e1bdb092dd059ca5a2751d54cb57d569678150d576f"
# Tick centers for time 0 and 240, then normalized CAP 0 and 1, in PDF points.
AXES = {
    "glucose": (86.3645, 198.2645, 220.4915, 169.7765),
    "lactate": (86.5235, 198.4255, 342.3305, 291.6135),
}
COLORS = {(0.743, 0.754, 0.757): "control", (1.000, 0.670, 0.680): "cKO"}
WINDOWS = [(230, 240), (220, 230), (200, 210), (130, 140), (40, 50)]


def read_curves(page, calibration):
    x0, x240, y0, y1 = calibration
    curves = {"control": {}, "cKO": {}}
    for path in page.get_drawings():
        color = tuple(round(v, 3) for v in (path["fill"] or ()))
        r = path["rect"]
        if color not in COLORS or not 0.09 < r.width < 0.11 or len(path["items"]) != 1:
            continue
        x, y = (r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2
        time = 240 * (x - x0) / (x240 - x0)
        cap = (y0 - y) / (y0 - y1)
        if not (-0.3 < time < 240.3 and -0.25 < cap < 1.5):
            continue
        t = round(time * 2) / 2
        if t in curves[COLORS[color]]:
            raise ValueError(f"Duplicated graphical observation at {t}")
        curves[COLORS[color]][t] = cap
    return curves


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_pdf", type=Path)
    pdf = parser.parse_args().source_pdf
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != SOURCE_HASH:
        raise ValueError("Expected the cited institutional PDF")
    with pymupdf.open(pdf) as doc:
        data = {fuel: read_curves(doc[7], axis) for fuel, axis in AXES.items()}
    print("minutes\tpoints_per_curve\tGlc_control\tGlc_cKO\tLac_control\tLac_cKO\tinteraction_pp")
    for start, end in WINDOWS:
        values = []
        grid = [start + i / 2 for i in range(2 * (end - start) + 1)]
        for fuel in AXES:
            for genotype in ("control", "cKO"):
                curve = data[fuel][genotype]
                values.append(mean(curve[t] for t in grid))
        gc, gk, lc, lk = values
        print(f"{start}-{end}\t{len(grid)}\t" + "\t".join(f"{v:.4f}" for v in values)
              + f"\t{100 * ((lk - lc) - (gk - gc)):.2f}")
    print("\nconcentration_uM\tbrief_single_block_pct\tbrief_mixture_block_pct")
    for c in (0.36, 1.0):
        print(f"{c}\t{100*c/(c+54):.2f}\t{51*c/(c+4.6)+49*c/(c+220):.2f}")


if __name__ == "__main__":
    main()
