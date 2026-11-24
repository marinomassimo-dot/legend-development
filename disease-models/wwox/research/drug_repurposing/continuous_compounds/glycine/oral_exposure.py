"""Two-sided exact sign test using reported paired direction counts (PMID 19556112)."""
import csv
from math import comb
import sys

writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("analysis", "increases", "n", "two_sided_p_assuming_no_ties"))
for label, gains, n in [("reported", 10, 11), ("omit_one_increase", 9, 10)]:
    tail = sum(comb(n, k) for k in range(n-gains+1)) / 2**n
    writer.writerow((label, gains, n, 2*tail))
