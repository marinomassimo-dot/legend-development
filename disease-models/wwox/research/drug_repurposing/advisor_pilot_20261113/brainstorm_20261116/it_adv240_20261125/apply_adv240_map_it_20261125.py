"""ADV-240 (IT, 2026-11-25): one dated line on map row ADV228-Q03 (status unchanged); idempotent. Run from the repository root."""
import csv
from pathlib import Path
MAP = Path("disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv")
RES = "brainstorm_20261116/it_adv240_20261125/RESULT_ADV240_IT_20261125.md"
MARK = "[IT 2026-11-25 ADV-240"
LINE = (" [IT 2026-11-25 ADV-240 measured base, status unchanged: 12 WWOX cases among 788 solved cases (1.5 percent; 1.3 to 1.6 by leave-one-series-out; about 1.2 percent with the approximate rows) "
        "in seven published series with a gene-countable table; 4 of 14 series opened contain WWOX (two large ones carry 10 of the 12); subtotals: infantile spasms 4 of 51, early-infantile DEE 6 of 72. "
        "Not an incidence: tertiary-centre infantile-onset cohorts, solved cases as denominator. Access-limited series listed in the result. Result: " + RES + ".]")
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
for r in rows[1:]:
    if r[0] == "ADV228-Q03" and MARK not in r[h.index("status_evidence")]:
        r[h.index("status_evidence")] += LINE; r[h.index("last_touched")] = "2026-11-25"; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
