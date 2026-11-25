"""ADV-244: per-library counts of T-run lengths from the matched reads, all pattern hits and (post hoc) only hits
whose flanks continue as WWOX exon 1 (upstream ...ATGGCAGC, downstream GGCTGGAC..., over the bases the read has).
The reference flanks are those of the wild-type reads and of Fig EV1C of PMID 34268881.

Usage: python3 -I summarise_adv244.py <dir of *_matched.tsv> <out.tsv>
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv, glob, os, re

COMP = str.maketrans("ACGTN", "TGCAN")
UP, DOWN = "CCATGGCAGC", "GGCTGGACGACACGGACAGTGAGG"
with open(sys.argv[2], "w") as o:
    o.write("library\trun\tfilter\tT1\tT2\tT3\tT5\tother\tcall\n")
    for f in sorted(glob.glob(os.path.join(sys.argv[1], "*_matched.tsv"))):
        lib, run = os.path.basename(f).split("_")[:2]
        rows = list(csv.DictReader(open(f), delimiter="\t"))
        for filt in ("pattern_only", "wwox_flanks"):
            c = collections.Counter()
            for r in rows:
                s = r["sequence"] if r["orientation"] == "fwd" else r["sequence"].translate(COMP)[::-1]
                m = re.search(r"GCTGCGC(T+)ACGCGG", s)
                if filt == "wwox_flanks":
                    up, dn = s[:m.start()], s[m.end():]
                    n_up, n_dn = min(len(up), len(UP)), min(len(dn), len(DOWN))
                    if up[len(up) - n_up:] != UP[len(UP) - n_up:] or dn[:n_dn] != DOWN[:n_dn]:
                        continue
                c[len(m.group(1))] += 1
            t3, t5 = c[3], c[5]
            call = "control" if lib.startswith("cwt") else (
                "mixed" if t3 >= 3 and t5 >= 3 else "KO1" if t5 >= 3 and t3 < t5 / 5 else
                "KO2" if t3 >= 3 and t5 < t3 / 5 else "unassigned")
            if any(k not in (1, 2, 3, 5) for k in c):
                call = "unassigned"
            o.write("%s\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%s\n" % (lib, run, filt, c[1], c[2], t3, t5,
                    sum(v for k, v in c.items() if k not in (1, 2, 3, 5)), call))
print("written", sys.argv[2])
