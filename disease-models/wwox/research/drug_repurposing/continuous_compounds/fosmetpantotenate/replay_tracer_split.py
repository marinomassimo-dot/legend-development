"""Reproduce the tracer split from source-corrected CoA fractions in Tables 7 and 8."""
import csv
import sys


ROWS = (
    ("Table 7", "oral", "liver", "6 h", 3, 58.6, 1.4, 40.0),
    ("Table 7", "oral", "liver", "24 h", 3, 58.0, 8.4, 34.0),
    ("Table 7", "intrastriatal", "brain", "6 h", 8, 61.0, 2.8, 36.2),
    ("Table 7", "intrastriatal", "brain", "12 h", 8, 50.0, 3.6, 46.4),
    ("Table 7", "intrastriatal", "brain", "24 h", 8, 45.0, 4.3, 50.7),
    ("Table 8", "ICV lower arm", "brain", "day 7", 6, 91.0, 5.0, 4.0),
    ("Table 8", "ICV lower arm", "brain", "day 10", 6, 86.0, 8.0, 6.0),
    ("Table 8", "ICV higher arm", "brain", "day 3", 6, 77.0, 8.0, 15.0),
    ("Table 8", "ICV higher arm", "brain", "day 7", 6, 59.0, 14.0, 27.0),
    ("Table 8", "ICV higher arm", "brain", "day 10", 6, 56.0, 16.0, 28.0),
)


def main():
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("source_29522513", "route", "tissue", "time", "mice_in_pool",
                  "unlabeled_pct", "recycled_or_exchanged_pct", "phosphate_retained_pct",
                  "total_labeled_pct", "retained_per_labeled_pct"))
    for row in ROWS:
        unlabeled, recycled, retained = row[-3:]
        assert abs(unlabeled + recycled + retained - 100) <= 0.5  # Published rounding
        labeled = recycled + retained
        out.writerow((*row, f"{labeled:.1f}", f"{100 * retained / labeled:.2f}"))


if __name__ == "__main__":
    main()
