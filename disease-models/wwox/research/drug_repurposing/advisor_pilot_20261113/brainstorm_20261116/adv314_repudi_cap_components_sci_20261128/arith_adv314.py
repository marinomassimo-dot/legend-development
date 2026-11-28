"""ADV-314 arithmetic on values read from Repudi 2021 Fig. 5D (no image is stored here).

Per-slice values are this session's readback of plotted markers (native raster of the held PDF,
page 11, image 1000 x 887; axis ticks give 14.1 px/ms in panel ii and 46.65 px/unit in panel iii).
Values marked approximate sat inside overlapping markers or error bars.
"""
from collections import Counter
from itertools import combinations
from statistics import mean, median

N2_CTRL = [12.91, 8.19, 4.79, 3.65, 4.29, 5.5, 6.75, 7.4]    # last three approximate
N2_KO = [16.2, 14.57, 5.57, 3.51, 6.13, 6.6, 6.75, 7.1]      # last three approximate
RATIO_CTRL = [5.66, 1.90, 0.94, 1.05, 3.03, 3.2, 3.3, 2.9]   # last three approximate
RATIO_KO = [1.17, 0.46, 0.47, 1.38, 0.70, 0.80, 0.95, 0.86]  # last four approximate; 0.86 hidden by the mean line


def exact_two_sided(u, n=8):
    counts = Counter(sum(c) - n * (n + 1) // 2 for c in combinations(range(1, 2 * n + 1), n))
    return min(1.0, 2 * sum(v for k, v in counts.items() if k <= u) / sum(counts.values()))


def pairs_above(ctrl, ko):
    return sum((k > c) + 0.5 * (k == c) for c in ctrl for k in ko)


print("rank-sum U implied by the printed P values (8 against 8, exact, two-sided)")
for u in (5, 7, 8, 26):
    print(f"  U={u}: P={exact_two_sided(u):.4f}")
for name, ctrl, ko in (("N2 latency", N2_CTRL, N2_KO), ("N1/N2 ratio", RATIO_CTRL, RATIO_KO)):
    above = pairs_above(ctrl, ko)
    print(f"{name}: KO>control pairs {above}/64, U={min(above, 64 - above)}; "
          f"mean {mean(ctrl):.2f} -> {mean(ko):.2f} (ln {__import__('math').log(mean(ko) / mean(ctrl)):+.3f}); "
          f"median {median(ctrl):.2f} -> {median(ko):.2f} (ln {__import__('math').log(median(ko) / median(ctrl)):+.3f})")
print("apparent speed if the printed 250 um vertical distance were the whole path (not a velocity the paper states)")
for name, ms in (("N1 control", 2.43), ("N1 S-KO", 3.17), ("N2 control", 6.64), ("N2 S-KO", 8.29)):
    print(f"  {name}: {0.25 / ms:.3f} m/s")
