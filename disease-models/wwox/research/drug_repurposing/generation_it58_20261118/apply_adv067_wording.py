"""IT58 / ADV-067 (2026-11-19): INV-09 `next_test` gains one dated clause that supersedes, for the lithium regimen, the IT57 clause ('the regimen is a design variable'), which stays in the cell as history.
Wording is SCI's decision (LITHIUM_REGIMEN_DECISION_ADV067_SCI_20261119.md sections 1, 4, 5), mapped by IT. Idempotent; --check reports without writing."""
import csv, sys
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
ADD = (" [IT58; ADV-067, SCI 2026-11-19] This replaces the statement above that the lithium regimen is a design variable: one regimen (the repeated pretreatment of the one held experiment) is the main contrast and a single acute injection is an optional "
       "comparator arm only; a lithium-alone arm carries a sedation, righting-reflex and weight readout at the time of the provoked seizure, and the interval from the last injection to the seizure is recorded; the second inhibitor of another class is more necessary, "
       "because a regimen or lithium-specific artefact cannot otherwise be excluded; from the image of that experiment the proportional reduction looks similar in the three genotypes (an eye reading), which fits a general effect or a regimen artefact better than a knockout-enhanced one. "
       "Every pup sign here is a transfer from adult data.")
def main(check=False):
    csv.field_size_limit(10**9); n = 0
    for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
        p = DR / f; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; i = h.index("inv_id"); j = h.index("next_test"); k = 0
        for r in rows[1:]:
            if r[i] == "INV-09" and "[IT58; ADV-067" not in r[j]:
                r[j] = r[j] + ADD; k += 1
        if not check and k:
            csv.writer(open(p, "w", newline="", encoding="utf-8"), delimiter="\t", lineterminator="\n").writerows(rows)
        n += k
    print(("would change " if check else "changed ") + str(n))
if __name__ == "__main__":
    main("--check" in sys.argv)
