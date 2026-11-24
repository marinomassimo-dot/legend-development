"""Audit Tatsuta et al. Fig. 2b from rounded group summaries; no animal-level data."""
from math import gamma, hypot, pi, sqrt

control, treated = 2.8, 6.8
error_control, error_treated = 0.3, 2.1
n = 4
df = 2 * n - 2


def two_sided_p(statistic):
    """Integrate the t density between 0 and |t| (midpoint quadrature)."""
    width = abs(statistic) / 10000
    normalizer = gamma((df + 1) / 2) / (sqrt(df * pi) * gamma(df / 2))
    central = sum((1 + ((i + 0.5) * width) ** 2 / df) ** (-(df + 1) / 2)
                  for i in range(10000)) * width * normalizer
    return 1 - 2 * central


if __name__ == "__main__":
    print("error_interpretation\tfold\tt_pooled\tdf\tp_two_sided")
    for label, divisor in [("SEM_as_reported", 1), ("SD_sensitivity", sqrt(n))]:
        t = (treated - control) / (hypot(error_control, error_treated) / divisor)
        print(f"{label}\t{treated / control:.3f}\t{t:.3f}\t{df}\t{two_sided_p(t):.4f}")
