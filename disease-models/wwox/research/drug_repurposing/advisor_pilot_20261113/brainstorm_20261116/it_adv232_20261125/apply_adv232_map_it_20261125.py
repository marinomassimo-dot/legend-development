"""ADV-232 (IT, 2026-11-25): one dated line on the open-questions map row IT-ADV222-NQA (status_evidence); old text kept; idempotent.
Run from the repository root. Hypothesis level; no status, ranking, drug or priority change."""
import csv
from pathlib import Path
MAP = Path("disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv")
MARK = "[IT 2026-11-25 ADV-232"
LINE = (" [IT 2026-11-25 ADV-232 feasibility, no status change: step 1 finds no held Wwox counterpart for any of the four panel families (band power, ratios, coherence, Granger); "
        "nearest held recordings are event counts (neonatal single-channel ECoG; adult hypomorph video-EEG, bilateral, n 3 against 3) and one anaesthetised pup field recording with normalised power. "
        "Missing recording named in the result; the adult hypomorph raw EEG and the neonatal ECoG files are the nearest holders (no contact made). "
        "Cortical PV counts are not held for Wwox; hippocampal PV counts are lower (opposite regional pattern to the template). Changes nothing for the portfolio compounds yet. "
        "Result: brainstorm_20261116/it_adv232_20261125/RESULT_ADV232_IT_20261125.md.]")
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
for r in rows[1:]:
    if r[0] == "IT-ADV222-NQA" and MARK not in r[h.index("status_evidence")]:
        r[h.index("status_evidence")] += LINE; r[h.index("last_touched")] = "2026-11-25"; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
