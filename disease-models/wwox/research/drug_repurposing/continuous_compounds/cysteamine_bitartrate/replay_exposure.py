"""Replay approximate Fig. 3 values and exposure comparisons without fitting PK."""

import csv
from pathlib import Path


def main():
    with Path(__file__).with_name("csf_points.tsv").open() as source:
        points = list(csv.DictReader(source, delimiter="\t"))
    time = [float(point["time_min"]) for point in points]
    micromolar_per_pixel = 20 / (421 - 72)

    print("comparison\tvalue\tunit")
    for group in ("naive", "pretreated"):
        curve = [(421 - int(point[f"{group}_y"])) * micromolar_per_pixel for point in points]
        area = sum((t1 - t0) * (c0 + c1) / 2 for t0, t1, c0, c1 in zip(time, time[1:], curve, curve[1:]))
        for minute, concentration in zip(time, curve):
            print(f"rat_csf_{group}_{minute:g}_min\t{concentration:.2f}\tumol/L")
        print(f"rat_csf_{group}_area_of_group_means_0_to_60_min\t{area:.1f}\tumol*min/L")

    pediatric_total_peak = 1000 * 1.26 / 77.15
    pediatric_free_peak_guess = pediatric_total_peak * (1 - 0.52)
    print(f"pediatric_plasma_average_total_peak\t{pediatric_total_peak:.2f}\tumol/L")
    print(f"pediatric_plasma_arithmetic_free_peak\t{pediatric_free_peak_guess:.2f}\tumol/L")
    for nominal_bath in (10, 100, 1000):
        ratio = nominal_bath / pediatric_total_peak
        print(f"{nominal_bath}_uM_nominal_bath_over_pediatric_total_peak\t{ratio:.2f}\tratio_of_different_compartments")


if __name__ == "__main__":
    main()
