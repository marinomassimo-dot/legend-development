"""IT 2026-11-25 (ADV request, wording only): (1) open-questions map row ADV228-Q01 -> CONCLUDED, pointing to SCI's ADV-231 (disposition 4, not resolvable);
(2) one dated bracket appended to the Result cell of the carried P47T 'IL6-JAK-STAT3 positive in all three regions' row of partial_benefit_it6_p10_20261029/README.md.
No number changes; Q02 stays open. Idempotent (one marker each). Run from the repository root."""
import csv
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
MAP = DR / "batch_sci_20261105/map/open_questions_map.tsv"
README = DR / "partial_benefit_it6_p10_20261029/README.md"
R231 = "advisor_pilot_20261113/brainstorm_20261116/adv231_stat3_echo_sci_20261125/RESULT_ADV231_STAT3_ECHO_SCI_20261125.md"
EV = (" [SCI ADV-231, 2026-11-25; closed by IT 2026-11-25 on ADV's instruction] CONCLUDED, disposition 4, not resolvable: only 3 of 6 target genes are measurable in the P17 tables; Socs3 is lower in cortex but at low expression "
      "(controls spread 1.74 to 12.29 TPM, knockouts about 1 TPM) and not measurable in hippocampus; Stat3 is higher in two hippocampal knockout contrasts, not in the null or cortex; no target reaches a verdict in the P47T tables. "
      "Companion question ADV228-Q02 (phosphorylated STAT3 and JAK2) stays OPEN. Result: " + R231 + ".")
MARK_M = "[SCI ADV-231, 2026-11-25; closed by IT"
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
for r in rows[1:]:
    if r[0] == "ADV228-Q01" and MARK_M not in r[h.index("status_evidence")]:
        r[h.index("status_evidence")] += EV; r[h.index("status")] = "CONCLUDED"; r[h.index("last_touched")] = "2026-11-25"; n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
OLD = "positive in all three regions; transcriptomic inference, not a cytokine measurement |"
NEW = ("positive in all three regions; transcriptomic inference, not a cytokine measurement [ADV-231, 2026-11-25: the axis signal in P47T is carried by two of five animals (M6, F8) in PFC, HPC and CTX; "
       "a state, not shown to be a pathway; ADV-233 tests the other carried signatures] |")
t = README.read_text(encoding="utf-8")
if "[ADV-231, 2026-11-25" not in t:
    assert t.count(OLD) == 1, t.count(OLD)
    t = t.replace(OLD, NEW); README.write_text(t, encoding="utf-8"); n += 1
print("edits", n)
