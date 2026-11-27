"""Reconstruct plotted normalized means in Breton Figure 3D from its original pixels."""
import argparse
import csv
from hashlib import sha256
from pathlib import Path
import subprocess

import numpy as np


FINGERPRINT = "96564f24e75f786879a68b74a6d274b23a4e12c2a14fd84139a2a92b41422381"
WIDTH = 1894
HEIGHT = 1900
PLOT_ROWS = {
    "d1_frequency": (870, 1114, 1254),
    "d2_duration": (1220, 1463, 1250),
    "d3_amplitude": (1557, 1798, 1250),
}
CONDITIONS = {
    "baseline": 0,
    "dAPV": 1,
    "CBX": 2,
    "BB-FCF": 3,
    "dAPV_washout": 4,
    "CBX_washout": 5,
    "BB-FCF_washout": 6,
}
BRACKETS = {
    ("d1_frequency", "CBX"): ("*", "0.008"),
    ("d2_duration", "CBX"): ("**", "0.0274"),
    ("d2_duration", "CBX_washout"): ("*", "0.0036"),
}


def first_fill(blue, top, axis, bar_x, fraction):
    interior = np.c_[blue[top:axis, bar_x - 21:bar_x - 12],
                     blue[top:axis, bar_x + 12:bar_x + 21]]
    have_fill = np.flatnonzero(interior.mean(axis=1) >= fraction)
    return int(top + have_fill[0]) if len(have_fill) else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("figure", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    if sha256(args.figure.read_bytes()).hexdigest() != FINGERPRINT:
        raise ValueError("Use the native high-resolution Figure 3 JPEG")
    rgb = subprocess.check_output(["convert", str(args.figure), "-depth", "8", "rgb:-"])
    red, green, blue_channel = np.frombuffer(rgb, np.uint8).reshape(HEIGHT, WIDTH, 3).astype("int16").transpose(2, 0, 1)
    mask = (blue_channel > red + 35) & (blue_channel > green + 35) & (red < 100) & (green < 100) & (blue_channel > 90)

    rows = []
    for panel, (top, axis, baseline_x) in PLOT_ROWS.items():
        baseline_top = first_fill(mask, top, axis, baseline_x, 0.60)
        span = axis - baseline_top
        for condition, index in CONDITIONS.items():
            x = baseline_x + int(round(index * 85.7))
            bar_top = first_fill(mask, top, axis, x, 0.60)
            if condition == "dAPV":
                assert bar_top is None
                values = ("0", "NA", "NA") if panel == "d1_frequency" else ("NA", "NA", "NA")
            else:
                assert bar_top is not None
                estimate = (axis - bar_top) / span
                candidates = []
                for fraction in (0.45, 0.75):
                    trial_bar = first_fill(mask, top, axis, x, fraction)
                    trial_base = first_fill(mask, top, axis, baseline_x, fraction)
                    for shift in (-2, 2):
                        for outline in (-2, 2):
                            result = (axis + shift - trial_bar + outline) / (axis + shift - trial_base)
                            candidates.append(max(0.0, result))
                values = (f"{estimate:.3f}", f"{min(candidates):.3f}", f"{max(candidates):.3f}")
            marker, p = BRACKETS.get((panel, condition), ("NA", "NA"))
            rows.append((panel, condition, *values, marker, p))
    with args.output.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(("panel", "condition", "normalized_pixel_estimate", "sensitivity_min", "sensitivity_max",
                         "visible_marker_vs_baseline", "caption_p"))
        writer.writerows(rows)


if __name__ == "__main__":
    main()
