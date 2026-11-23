"""Check two specific ordinate comparisons in original Figure 2E, without exporting artwork."""
import argparse
from math import log10
import numpy as np
import pymupdf

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("article_pdf")
args = parser.parse_args()
with pymupdf.open(args.article_pdf) as doc:
    image, = doc[3].get_images()
    pix = pymupdf.Pixmap(doc, image[0])
    pixels = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
assert pixels.shape[:2] == (1324, 1350)


def ordinate(concentration):
    col = round(886.5 + 65.2 * log10(concentration))
    red, green, blue = pixels[850:1194, col, :3].T
    ys, = np.where((red > 180) & (green < 100) & (blue > 45) & (blue < 190))
    assert 1 <= len(ys) <= 16
    return (1194 - 850 - np.median(ys)) / 314


for lo, hi in [(20, 200), (30, 150)]:
    fraction = (0.5 - ordinate(lo)) / (ordinate(hi) - ordinate(lo))
    estimate = 10 ** (log10(lo) + fraction * log10(hi / lo))
    print(f"50% absolute crossing (log interpolation between {lo}/{hi} µM): {estimate:.1f} µM")
print(f"Fraction inhibited at reported 697 µM: {ordinate(697):.3f}")
