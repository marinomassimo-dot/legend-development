"""Replay the Figure 8A survival and Figure 9B brain denominator cross-checks."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path
from statistics import mean, median, stdev
import subprocess
import sys


FIG8 = "904d326b5609a4954c5d237e8aa2ab7d854ac4049e127ffb6e072367a2eb56b7"
FIG9 = "6bbbd4f63433bea8c5647025e01a3fbe0d55c7b18966b8f2ac5a45224afdf963"


def decode(path, digest, width, height):
    if sha256(path.read_bytes()).hexdigest() != digest:
        raise SystemExit(f"Unexpected source bytes: {path}")
    raw = subprocess.check_output(["convert", str(path), "-colorspace", "sRGB", "-depth", "8", "rgb:-"])
    if len(raw) != 3 * width * height:
        raise SystemExit(f"Unexpected raster size: {path}")

    def pixel(x, y):
        start = 3 * (y * width + x)
        return tuple(raw[start:start + 3])

    return pixel


def orange(pixel):
    red, green, blue = pixel
    return red > 170 and red - blue > 80 and green - blue > 32 and red - green > 18


def survival_anchors(pixel):
    # First descending orange segment is overplotted by the PBS curve.
    # Find the left edge of the first visible orange plateau instead.
    first = min(x for x in range(216, 235) if orange(pixel(x, 71)))
    vertical_candidates = (
        ((225, 235), (112, 172)), ((244, 251), (201, 229)), ((253, 261), (248, 272)),
    )
    positions = [float(first - 1)]
    for (x0, x1), (y0, y1) in vertical_candidates:
        xs = [x for y in range(y0, y1) for x in range(x0, x1) if orange(pixel(x, y))]
        positions.append(float(median(xs)))
    return positions


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fig8", type=Path)
    parser.add_argument("fig9", type=Path)
    args = parser.parse_args()
    survival = decode(args.fig8, FIG8, 791, 1209)
    brain = decode(args.fig9, FIG9, 718, 911)
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("source", "quantity", "value", "unit", "basis"))

    ages = []
    for x, events in zip(survival_anchors(survival), (1, 3, 1, 1)):
        age = round((x - 100) * 40 / (447 - 100))
        ages.extend([age] * events)
        writer.writerow(("Fig8A", f"dC_only_KO_day_{age}", events, "events_approx", f"x={x:g}"))
    writer.writerow(("Fig8A", "dC_only_KO_raster_mean", f"{mean(ages):.3f}", "day", "curve_steps"))
    writer.writerow(("Fig8A", "dC_only_KO_raster_sample_SD", f"{stdev(ages):.3f}", "day", "curve_steps"))
    writer.writerow(("Fig8A", "minimum_SD_if_literal_reported_mean_and_median",
                     f"{(17.7 - 15) * (6 / 5) ** .5:.3f}", "day", "half_at_or_below_15_n6"))

    # The dT-WT median partly overlaps a marker. Record the visual row and use a
    # conservative two-pixel sensitivity for all median lines.
    values = {}
    for group, x, y in (
        ("WT_vehicle", 49, 596), ("WT_dT", 106, 572), ("KO_vehicle", 135, 606.5),
        ("KO_dC_plus_dT", 163, 606.5), ("KO_dT", 192, 601.5),
    ):
        assert any(max(brain(xx, yy)) < 100
                   for xx in range(x - 3, x + 4) for yy in range(int(y) - 1, int(y) + 2))
        value = (612 - y) * 800 / (612 - 498)
        values[group] = value
        writer.writerow(("Fig9B", f"P12_brain_{group}_median", f"{value:.2f}",
                         "mtDNA_over_nDNA", f"y={y:g};axis_y0=612;axis_y800=498"))
    for group in ("WT_vehicle", "WT_dT"):
        numerator, denominator = values["KO_dT"], values[group]
        ratio = numerator / denominator
        radius = 2 * 800 / (612 - 498)
        low = (numerator - radius) / (denominator + radius)
        high = (numerator + radius) / (denominator - radius)
        writer.writerow(("Fig9B", f"P12_brain_KO_dT_relative_to_{group}",
                         f"{ratio:.3f}", "relative_fraction", f"range_at_2px={low:.3f}-{high:.3f}"))


if __name__ == "__main__":
    main()
