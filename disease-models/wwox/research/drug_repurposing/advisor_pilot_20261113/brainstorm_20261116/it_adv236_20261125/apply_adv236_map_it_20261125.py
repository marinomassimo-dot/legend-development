"""ADV-236 (IT, 2026-11-25): (1) adds map row IT-ADV236-NQ1 (cortical PV density in Wwox-deficient mice, the regional-PV observation); (2) one dated line on IT-ADV222-NQA.
Idempotent; old text kept; no status change on existing rows. Run from the repository root. Hypothesis level."""
import csv
from pathlib import Path
MAP = Path("disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv")
RES = "advisor_pilot_20261113/brainstorm_20261116/it_adv236_20261125/RESULT_ADV236_IT_20261125.md"
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
NEW = {"qid": "IT-ADV236-NQ1", "source_ref": RES + "#4",
 "question_text_max300": "Is cortical PV-interneuron density lower, unchanged or higher in a Wwox-deficient mouse, per animal, at an age matched to the hippocampal count (hippocampus 44 percent lower, 2-week-old knockout)?",
 "decision_at_stake_max200": "Whether the PV-circuit premise carried over from the CSNK2B template (cortical PV density lower) is tested in Wwox at all; it gates the cortical endpoint panel of NQ-A.",
 "kind": "wet_lab_measurement", "status": "OPEN", "published_on": "main",
 "status_evidence": "[IT 2026-11-25 ADV-236] Cortical PV counts are not held for any Wwox model; only hippocampal stereology is (Hussain 2019). No per-animal count is public; the request wording is drafted for the operator, not sent (REQUEST_TO_AUTHORS_EEG_DRAFT_IT_20261125.md). Distinct from RS-NP3A1 (Pvalb transcript) and IT56-Q08R (chemogenetic PV activation). Result: " + RES + ".",
 "last_touched": "2026-11-25", "blocking_reason": "No held source answers it; per-animal counts are not public; needs author data or new sections.",
 "executable_zero_spend": "no", "claimed_by": ""}
if not any(r[0] == NEW["qid"] for r in rows[1:]):
    rows.append([NEW.get(c, "") for c in h]); n += 1
MARK = "[IT 2026-11-25 ADV-236"
LINE = (" [IT 2026-11-25 ADV-236 access check, no status change: none of the four held Wwox papers makes per-animal recordings or counts public (data statements: RNA-seq deposit only; \"Not relevant\"; upon reasonable request; none). "
        "Only Hussain 2023 Supplementary Figure S3 gives group averages of seizures and spikes per hour (n 3); none of the four panel families. Disposition: only by author contact or new recording; request wording drafted for the operator, not sent. Result: " + RES + ".]")
for r in rows[1:]:
    if r[0] == "IT-ADV222-NQA" and MARK not in r[h.index("status_evidence")]:
        r[h.index("status_evidence")] += LINE; r[h.index("last_touched")] = "2026-11-25"; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("edits", n)
