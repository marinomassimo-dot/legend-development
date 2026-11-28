"""Calibrate plotted group means from Santangeli (2001) using saved axis pixels."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    with (HERE / "thesis_plot_points.tsv").open() as data:
        points = csv.DictReader(data, delimiter="\t")
        print("endpoint\tcompound\texposure_uM\tmean_percent_control\tsem_percent_points\t"
              "digitization_sensitivity_pp\treported_significant\tpdf_page\tfigure")
        for row in points:
            zero, top, scale, mean, upper, lower = (
                float(row[column])
                for column in (
                    "y_zero_px", "y_top_px", "top_units", "y_mean_px", "y_sem_top_px", "y_sem_bottom_px"
                )
            )
            factor = scale / (zero - top)
            # Three pixels per endpoint comfortably cover graph marker and axis reading.
            movement = abs(zero - mean)
            low = (movement - 6) * scale / (zero - top + 6)
            high = (movement + 6) * scale / (zero - top - 6)
            estimate = (zero - mean) * factor
            sensitivity = max(estimate - low, high - estimate)
            sem = (lower - upper) * factor / 2
            print(
                f'{row["endpoint"]}\t{row["compound"]}\t{row["exposure_uM"]}\t{estimate:.1f}\t'
                f'{sem:.1f}\t{sensitivity:.1f}\t{row["reported_significant"]}\t'
                f'{row["pdf_page"]}\t{row["figure"]}'
            )


if __name__ == "__main__":
    main()
