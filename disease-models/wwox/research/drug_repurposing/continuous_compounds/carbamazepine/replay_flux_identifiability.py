"""Show why equal steady pools can conceal opposite cargo degradation rates."""
import csv
from math import exp
import sys


def fraction_degraded(rate, time):
    """A labelled pulse starts in the first of two serial first-order pools."""
    scaled_time = rate * time
    return 1 - (1 + scaled_time) * exp(-scaled_time)


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("scenario", "entry_rate", "transfer_and_degradation_rate",
                     "early_pool", "late_pool", "degraded_fraction_at_t_1",
                     "degraded_fraction_at_t_4"))
    for name, entry, rate in (
        ("reference", 1, 1),
        ("increased_throughput", 3, 1.5),
        ("decreased_throughput", .5, .25),
    ):
        pool_at_steady_state = entry / rate
        writer.writerow((name, entry, rate, pool_at_steady_state, pool_at_steady_state,
                         f"{fraction_degraded(rate, 1):.6f}", f"{fraction_degraded(rate, 4):.6f}"))


if __name__ == "__main__":
    main()
