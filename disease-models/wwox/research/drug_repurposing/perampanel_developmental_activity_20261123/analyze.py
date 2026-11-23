"""Estimate group bar heights in Figure 5C from the original PDF's embedded raster."""
import argparse
import hashlib
import zipfile
from pathlib import Path
from statistics import median

import numpy as np
import pymupdf

PANELS = {
    # tick at zero, top tick, top tick value, centers of the five bars in the source raster
    "PDGFRa": (659.5, 367, 100, [1730, 1802, 1870, 1941, 2012]),
    "BCAS1": (1056, 753, 100, [1736, 1810, 1882, 1954, 2027]),
    "PLP": (1470, 1151, 60, [1732, 1806, 1881, 1955, 2027]),
}


def read_top(img, center_x, zero_y, cutoff, width):
    # Walk from just above the baseline until the broad, continuous colored bar ends.
    y = int(zero_y) - 4
    while (img[y, center_x-width:center_x+width+1].min(axis=1) < cutoff).mean() > 0.9:
        y -= 1
    return y + 1


def bar_summary(img, bottom, top, value, centers):
    means, spreads = [], []
    for center in centers:
        estimates = [(bottom - read_top(img, center + offset, bottom, cutoff, width) - 1.5)
                     * value / (bottom - top)
                     for width in (15, 17) for cutoff in (205, 220, 230) for offset in (-1, 0, 1)]
        means.append(median(estimates))
        spreads.append(max(estimates) - min(estimates))
    return means, max(spreads)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_pdf", type=Path)
    parser.add_argument("supplement_docx", type=Path)
    args = parser.parse_args()
    pdf = args.source_pdf
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != "73b62bd4247866a99401cdb3c9c9448ee6e298b0906e50851bdf8dfba20aeab1":
        raise ValueError("Expected the archived publisher PDF")
    with pymupdf.open(pdf) as doc:
        pix = pymupdf.Pixmap(doc, doc[9].get_images()[0][0])
        assert (pix.width, pix.height, pix.n) == (2079, 1488, 3)
        img = np.frombuffer(pix.samples, np.uint8).reshape((1488, 2079, 3))
    print("marker\tControl1\tTTX\tTTX_plus_AMPA\tControl2\tNBQX\tTTX-C1\tTTX_AMPA-TTX\tNBQX-C2\tmax_read_spread_pp")
    for marker, (bottom, top, value, centers) in PANELS.items():
        means, spread = bar_summary(img, bottom, top, value, centers)
        c1, ttx, add, c2, nbqx = means
        print(marker, *(f"{v:.2f}" for v in [*means, ttx-c1, add-ttx, nbqx-c2, spread]), sep="\t")

    with zipfile.ZipFile(args.supplement_docx) as z:
        png = z.read("word/media/image5.png")
    if hashlib.sha256(png).hexdigest() != "fbafc7096e2f47a3be9f145d7f66ea375dd2eb280138cf90e4adfb17cd71acca":
        raise ValueError("Unexpected Fig. S5 source")
    pix = pymupdf.Pixmap(png)
    rgba = np.frombuffer(pix.samples, np.uint8).reshape((1819, 1678, 4))
    # Pixmap alpha is premultiplied; composite on white before measuring bar boundaries.
    img = (rgba[:, :, :3].astype(np.int16) + 255 - rgba[:, :, 3, None]).astype(np.uint8)
    supplementary = {
        "PDGFRa": (684.5, 297.5, 80, [1335, 1408, 1480]),
        "BCAS1": (1090.5, 713.5, 100, [1339, 1411, 1483]),
        "PLP": (1503.5, 1158.5, 50, [1330, 1395, 1460]),
    }
    print("S5_marker\tControl\tGi\tGi_plus_AMPA\tGi-control\taddback-Gi\tmax_read_spread_pp")
    for marker, (bottom, top, value, centers) in supplementary.items():
        means, spread = bar_summary(img, bottom, top, value, centers)
        control, gi, add = means
        print(marker, *(f"{v:.2f}" for v in [*means, gi-control, add-gi, spread]), sep="\t")


if __name__ == "__main__":
    main()
