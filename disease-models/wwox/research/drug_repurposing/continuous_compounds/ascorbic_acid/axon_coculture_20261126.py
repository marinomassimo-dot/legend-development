"""Digitize Repudi Fig. 6D box medians, then calculate a count-denominator threshold."""
import csv
import hashlib
from pathlib import Path
import subprocess
import sys

source = Path(sys.argv[1])
assert hashlib.sha256(source.read_bytes()).hexdigest() == "113522bb09b42a2dc0252bc1d7b112b66e3a68323ab1348c042f0ac8c8e8fa4c"
raster = subprocess.check_output(["pdftoppm", "-f", "12", "-l", "12", "-r", "170",
                                  "-singlefile", str(source)])
magic, shape, scale, pixels = raster.split(b"\n", 3)
width, height = [int(n) for n in shape.split()]
assert magic == b"P6" and scale == b"255"
assert len(pixels) == width * height * 3


def is_colored(x, y, arm):
    i = 3 * (y * width + x)
    r, g, b = pixels[i:i+3]
    return r > 150 and r > g + 75 and r > b + 75 if arm == "KO" else b > 150 and b > g + 75 and b > r + 75


def central_line(x, arm, visible_median=None):
    window = range(779, 937) if visible_median is None else visible_median
    rows = [y for y in window if sum(is_colored(i, y, arm)
            for i in range(x - 4, x + 5)) >= 6]
    runs = []
    for y in rows:
        if not runs or y - runs[-1][-1] > 1:
            runs.append([y])
        else:
            runs[-1].append(y)
    if visible_median is None:
        assert len(runs) == 5, (x, runs)
        line = runs[2]
    else:
        assert len(runs) == 1, (x, runs)
        line, = runs
    return sum(line) / len(line)


# Panel D, axes calibrated to visually identified 0 and 70% tick centers.
zero_y, seventy_y = 983.0, 741.5
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("category", "WT_median_y_px", "KO_median_y_px", "WT_pct",
              "KO_pct", "KO_minus_WT_pp", "KO_over_WT_fraction"))
for category, wt_x, ko_x in [
        ("premyelinating", 985, 1019),
        ("myelinating", 1077, 1111),
        ("degraded", 1169, 1203)]:
    # Overlapping box/whisker lines in the third pair require a visible center-line window.
    wt_window, ko_window = (range(914, 920), range(908, 914)) if category == "degraded" else (None, None)
    wy, ky = central_line(wt_x, "WT", wt_window), central_line(ko_x, "KO", ko_window)
    wt, ko = [(zero_y - y) * 70 / (zero_y - seventy_y) for y in (wy, ky)]
    out.writerow((category, wy, ky, round(wt, 2), round(ko, 2),
                  round(ko - wt, 2), round(ko / wt, 3)))
