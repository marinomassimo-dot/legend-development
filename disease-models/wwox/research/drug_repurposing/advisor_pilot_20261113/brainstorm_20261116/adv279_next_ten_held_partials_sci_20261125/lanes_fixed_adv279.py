"""Band signal near the band row in each lane of an uncropped blot raster (read-only).

Usage: python3 lanes_fixed_adv279.py <page raster png, 2352x1716, extracted with pdfimages -png and converted to sRGB>

The raster is the single image of 12967_2026_8708_MOESM7_ESM.pdf (PMID 42875792; PDF sha256 prefix 5960195c56acf6d0).
Lane centres were read from the image by eye. The band row of a panel is the median peak row of the control and
heterozygous lanes that show a peak. For every lane two numbers are printed: the largest signal within 6 pixels of
that row, and the largest signal in an equally wide window 40 pixels below it, where no band is expected (the noise
a "best row" search returns). Signal = mean darkness of a 17 x 7 pixel box minus the mean of boxes 14 pixels above
and below (8-bit units). A screening measure on a published raster, not densitometry of the original scan.
"""
import sys

if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import pymupdf

pix = pymupdf.Pixmap(sys.argv[1])
pix = pymupdf.Pixmap(pymupdf.csGRAY, pix)
w, data = pix.width, pix.samples


def strip(x, y, half_w, half_h):
    vals = [255 - data[yy * w + xx] for xx in range(x - half_w, x + half_w + 1) for yy in range(y - half_h, y + half_h + 1)]
    return sum(vals) / len(vals)


def signal(x, y):
    return strip(x, y, 8, 3) - (strip(x, y - 14, 8, 2) + strip(x, y + 14, 8, 2)) / 2


CONC = ["vehicle", "1 nM", "10 nM", "100 nM", "1 uM", "10 uM"]
PANELS = {
    "24 h": (["CON vehicle a", "CON vehicle b"], [186, 220, 251, 283, 316, 347, 378, 413, 447, 480, 512, 545, 578, 613]),
    "48 h": (["CON vehicle"], [1021, 1056, 1089, 1123, 1157, 1190, 1223, 1257, 1292, 1327, 1361, 1396, 1433]),
    "72 h": (["CON vehicle"], [1816, 1850, 1884, 1919, 1953, 1987, 2019, 2053, 2087, 2121, 2155, 2189, 2223]),
}
print("panel\tlane\tx\tband_row\tmax_at_band_row\tmax_off_band")
for panel, (con, xs) in PANELS.items():
    names = con + ["Het " + c for c in CONC] + ["HOM " + c for c in CONC]
    assert len(names) == len(xs)
    rows = []
    for name, x in zip(names, xs):
        if name.startswith("HOM"):
            continue
        sig, y = max((signal(x, y), y) for y in range(1605, 1645))
        if sig > 8:
            rows.append((sig, y, x))
    ys = sorted(r[1] for r in rows)
    mid = ys[len(ys) // 2]
    for name, x in zip(names, xs):
        band = max(signal(x, y) for y in range(mid - 6, mid + 7))
        off = max(signal(x, y) for y in range(mid + 34, mid + 47))
        print("%s\t%s\t%d\t%d\t%.1f\t%.1f" % (panel, name, x, mid, band, off))
    print("# %s: band row = median of %d CON/Het lanes with a visible peak; rows %s" % (panel, len(rows), ys), file=sys.stderr)
