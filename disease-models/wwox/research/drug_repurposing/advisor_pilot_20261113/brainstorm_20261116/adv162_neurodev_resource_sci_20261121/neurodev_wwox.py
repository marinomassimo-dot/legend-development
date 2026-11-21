"""ADV-162: read Wwox (WWOX) and marker rows from the four NeuRoDev compact tables (figshare 30885428, folder with
stage/subclass pseudobulk and preferential expression; 3 sheets each = reference networks).
Usage: python3 -I neurodev_wwox.py <dir with the four xlsx>   (reads only; prints a report).
Unit: each column is a pooled cluster-pseudobulk aggregate (stage or subclass) across source studies, not a donor."""
import sys
import os
import statistics as st

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xlsx_min

FILES = ["stage_pseudobulk_expression.xlsx", "subclass_pseudobulk_expression.xlsx",
         "stage_preferential_expression.xlsx", "subclass_preferential_expression.xlsx"]
SHEETS = ["corticogenesis", "neurogenesis", "gliogenesis"]
MARK = ["WWOX", "GAPDH", "SLC17A7", "GAD1", "MBP", "SOX2", "GFAP", "PDGFRA"]


def main(d):
    for f in FILES:
        for i, sh in enumerate(SHEETS, start=1):
            rows = xlsx_min.read_rows(os.path.join(d, f), sheet="xl/worksheets/sheet%d.xml" % i)
            head = rows[0]
            print("\n#####", f, sh, "rows", len(rows), "cols", len(head))
            print("header:", head[:3], "...", head[-3:] if len(head) > 6 else "")
            # first column holds gene names (or the header's first cell is blank/index)
            names = [r[0] if r else None for r in rows[1:]]
            idx = {n: k + 1 for k, n in enumerate(names)}
            for g in MARK:
                if g in idx:
                    r = rows[idx[g]]
                    vals = [(head[j] if j < len(head) else j, r[j]) for j in range(1, len(r)) if isinstance(r[j], float)]
                    print(" ", g, ["%s=%.3f" % (h, v) for h, v in vals])
                else:
                    print(" ", g, "not a row")


if __name__ == "__main__":
    main(sys.argv[1])
