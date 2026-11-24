"""Smallest attainable untied, exact two-sided rank-sum p for three rats per group."""
from collections import Counter
from itertools import combinations
import csv
import sys

allocations = Counter(sum(group) - 6 for group in combinations(range(1, 7), 3))
assert sum(allocations.values()) == 20
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("U", "allocations", "two_sided_tail_probability"))
for u, count in sorted(allocations.items()):
    tail = sum(n for rank, n in allocations.items() if abs(rank - 4.5) >= abs(u - 4.5))
    writer.writerow((u, count, tail / 20))
