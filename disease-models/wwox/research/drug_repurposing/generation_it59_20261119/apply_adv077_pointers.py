"""IT59 / ADV-077 (2026-11-19): dated pointers from the arm-table notes and from the open-question rows that appear on SCI's ordering page to that page, as the entry for a laboratory (ADV's instruction; pointers only, nothing moved, no tier change).
Ordering page: experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/ORDERING_PAGE.md (14 measurements ordered by the decision each could change; the order is SCI's judgement). Idempotent."""
import csv
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
OP = "experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/ORDERING_PAGE.md"
ROWS = {"IT57-Q01": "row 4 (E_GABA)", "RS-NP3A1": "rows 1 and 6 (deletion completeness, PV count and markers)", "IT59-Q01": "row 12 (WWOX-ERBB4 binding, after text 13a)",
        "IT59-Q02": "rows 8 and 9 (structural myelin endpoints; conduction re-measurement)", "IT59-Q03": "row 10 (heterozygote carrier latency)", "IT59-Q04": "row 7 (glucose tied to seizure timing)"}
ARM = ("\n\nUpdate 2026-11-19 (IT59, ADV-077; the text above is not edited): the entry for a laboratory is SCI's one-page ordering of the 14 measurements by the decision each could change (" + OP + "; the order is SCI's judgement, the sources give each row's content), read with the consolidated slice package and pup brief of the same folder (version 2, dated addenda folded in, history appendix keeps the dates); "
       "the packages exceed their word targets by about 20 percent and are not trimmed without the operator's word. A blind check of version 2 against the originals is recorded in `generation_it59_20261119/`. Hypothesis level; no dose.")
csv.field_size_limit(10**9)
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); i = rows[0].index("status_evidence")
for r in rows[1:]:
    if r[0] in ROWS and "ADV-077" not in r[i]:
        r[i] += " Dated 2026-11-19 (IT, ADV-077): entry for a laboratory: " + ROWS[r[0]] + " of SCI's ordering page, " + OP + "."
with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
pa = DR / "advisor_pilot_20261113/brainstorm_20261116/ARM_TABLE_V9_NOTES_IT_20261117.md"; s = pa.read_text(encoding="utf-8")
if "(IT59, ADV-077;" not in s: pa.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
print("ok")
