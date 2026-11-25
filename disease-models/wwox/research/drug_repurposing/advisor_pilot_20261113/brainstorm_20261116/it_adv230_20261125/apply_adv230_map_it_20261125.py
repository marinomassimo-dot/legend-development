"""ADV-230 (IT, 2026-11-25): one dated line on the open-questions map row WO-10 (status_evidence); old text kept; idempotent (one marker).
Run from the repository root. Hypothesis level; no status, ranking, drug or priority change; no dose or treatment wording."""
import csv
from pathlib import Path
MAP = Path("disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv")
MARK = "[IT 2026-11-25 ADV-230"
LINE = (" [IT 2026-11-25 ADV-230 context pointer, no status change: a human gain-of-function responder contrast from the memantine case series (PMID 41489401, Table 1 and its clinical supplement) "
        "cannot attribute a memantine effect to a receptor population: in vitro data are one row per variant shared by the individuals of a set, and in the four same-variant sets age at start of treatment "
        "points the predicted way in one, against it in one, is mixed in one and is untestable in one; the contrasts are explained mostly by exposure and ascertainment (case report against registry, duration, co-medication). "
        "Missing in every source read: outcome definition and rater, exposure measurement, baseline seizure rate. Result: brainstorm_20261116/it_adv230_20261125/RESULT_ADV230_IT_20261125.md.]")
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
n = 0
for r in rows[1:]:
    if r[0] == "WO-10" and MARK not in r[h.index("status_evidence")]:
        r[h.index("status_evidence")] += LINE; r[h.index("last_touched")] = "2026-11-25"; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
