"""Per-library technical intervals from the validated organoid_summary.py output."""
import csv
from math import comb
from pathlib import Path
import sys


def upper_limit(successes, trials):
    """Invert the lower binomial tail for the two-sided 95% upper limit."""
    if successes == trials:
        return 1.0
    low, high = 0.0, 1.0
    for _ in range(60):
        p = (low + high) / 2
        tail = sum(comb(trials, k) * p**k * (1-p)**(trials-k) for k in range(successes+1))
        if tail > 0.025:
            low = p
        else:
            high = p
    return (low + high) / 2


def main(path):
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("run", "group", "included", "informative", "included_pct",
                  "lower_95_pct", "upper_95_pct", "status"))
    with path.open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            if row["status"] == "pending":
                out.writerow([row["run"], row["group"], "", "", "", "", "", "pending"])
                continue
            if (row["rule"], row["Q"]) != ("centered", "20"):
                continue
            n, k = int(row["informative"]), int(row["included"])
            assert 0 <= k <= n
            limits = (1-upper_limit(n-k,n), upper_limit(k,n)) if n else (0,1)
            pct = f"{100*k/n:.2f}" if n else "NA"
            out.writerow((row["run"], row["group"], k, n, pct, *(f"{100*v:.2f}" for v in limits), row["status"]))


if __name__ == "__main__":
    main(Path(sys.argv[1]))
