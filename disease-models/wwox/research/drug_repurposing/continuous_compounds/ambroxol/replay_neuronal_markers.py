"""Replay visual bar-top digitization for matched bafilomycin arms."""

import argparse
import csv
from pathlib import Path


def signal(row, y_key):
    top, bottom = float(row["anchor_upper_y_px"]), float(row["anchor_lower_y_px"])
    hi, lo = float(row["anchor_upper_value"]), float(row["anchor_lower_value"])
    fraction = (float(row[y_key]) - top) / (bottom - top)
    return hi + fraction * (lo - hi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("coordinates", type=Path)
    args = parser.parse_args()
    with args.coordinates.open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            baseline = signal(row, "vehicle_y_px")
            challenged = signal(row, "challenged_y_px")
            print(row["study"], row["panel"], row["condition"],
                  f"{baseline:.2f}", f"{challenged:.2f}",
                  f"{challenged - baseline:+.2f}", f"{challenged / baseline:.2f}", sep="\t")


if __name__ == "__main__":
    main()
