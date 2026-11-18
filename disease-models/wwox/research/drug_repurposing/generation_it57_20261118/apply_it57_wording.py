"""IT57: INV-04 and INV-09 `next_test` gain the design consequences of the day's strands (idempotent; --check). INV-04's clause was tested by blind readers (result_it57.md); INV-09's clause is sourced wording not reader-tested."""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cells_it57 as C
DR = HERE.parent
B04 = C.BEFORE_INV04

def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; k = 0
        i = h.index("inv_id"); j = h.index("next_test")
        for r in rows[1:]:
            if r[i] == "INV-04" and "[IT57;" not in r[j]:
                assert r[j].endswith(B04), r[j][-80:]
                r[j] = r[j] + C.ADD_INV04; k += 1
            if r[i] == "INV-09" and "[IT57;" not in r[j]:
                r[j] = r[j] + C.ADD_INV09; k += 1
        if not check and k:
            csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
        n += k
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
