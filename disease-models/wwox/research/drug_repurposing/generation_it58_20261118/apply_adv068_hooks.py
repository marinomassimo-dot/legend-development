"""IT58 / ADV-068 (2026-11-19): SCI's per-animal PV result mapped into its consumers in ONE pass (mapping only; the wording is SCI's, message to IT and the note
advisor_pilot_20261113/brainstorm_20261116/adv068_pv_per_animal_sci_20261119/PV_PER_ANIMAL_RESULT_ADV068_SCI_20261119.md). Hooks: NEED-INHIBITORY-HYPOFUNCTION counter_evidence (qualification only, no direction or
status change), open questions RS-NP3A1 and IT56-Q08R (dated line in status_evidence), the arm-table notes (dated line). Idempotent."""
import csv, json
from pathlib import Path
DR = Path(__file__).resolve().parent.parent
NOTE = "advisor_pilot_20261113/brainstorm_20261116/adv068_pv_per_animal_sci_20261119/PV_PER_ANIMAL_RESULT_ADV068_SCI_20261119.md"
CE = ("SCI 2026-11-19 (ADV-068, in silico, per animal; wording supplied by SCI, mapped here by IT; " + NOTE + "): the pre-registered stop was met at its boundary (cortex, 3 against 4 animals): the PV gene set falls by 0.65 and the "
      "late-maturing set by 0.33 (ratio 0.51), one gene (Slc12a5) decides it; the transcript pattern is PV-weighted, not PV-specific, and leans to a delay or state change with a PV component; the cell level is undecided "
      "(RP-019 stays 'transferred, not measured'). An interneuron-loss premise specific to PV is therefore not supported at transcript level.")
RS = (" Dated 2026-11-19 (IT, on SCI's ADV-068): per-animal transcripts (cortex, 3 against 4) lean to 'delay or state with a PV component' rather than PV-specific loss: PV set -0.65, late-maturing set -0.33 (ratio 0.51), one gene decides; the cell-level question stays open "
      "and needs the per-animal immunostaining or nucleus-resolved snRNA this row names. Source: " + NOTE + ".")
Q8R = (" Dated 2026-11-19 (IT, on SCI's ADV-068): stays optional and lowest priority; the transcript evidence does not support a PV-specific premise, the generic GABA-A arm is unaffected; no PV drug arm is added. Source: " + NOTE + ".")
ARM = ("\n\nUpdate 2026-11-19 (IT58, on SCI's ADV-068; the text above is not edited): consequence for the pilot arm list: a tissue measurement can be added (PV count and signal per cell, one late-maturing marker, one myelin marker, age-matched controls, two ages), not a PV drug arm; "
       "the PV chemogenetic tool arm (IT56-Q08R) stays optional and lowest priority; the PPxY partner branch (ERBB4, NETO2) still has no row and was not touched by this step. Hypothesis level; no dose.")
# 1 need
p = DR / "needs/needs.json"; raw = p.read_text(encoding="utf-8"); d = json.loads(raw)
items = d if isinstance(d, list) else d["needs"]
n = [x for x in items if x["id"] == "NEED-INHIBITORY-HYPOFUNCTION"][0]
if not any("ADV-068" in c for c in n["counter_evidence"]):
    n["counter_evidence"].append(CE); p.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
# 2 open questions
csv.field_size_limit(10**9)
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t")); i = rows[0].index("status_evidence")
for r in rows[1:]:
    if r[0] == "RS-NP3A1" and "ADV-068" not in r[i]: r[i] += RS
    if r[0] == "IT56-Q08R" and "ADV-068" not in r[i]: r[i] += Q8R
with open(p, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
# 3 arm table
p = DR / "advisor_pilot_20261113/brainstorm_20261116/ARM_TABLE_V9_NOTES_IT_20261117.md"; s = p.read_text(encoding="utf-8")
if "on SCI's ADV-068" not in s: p.write_text(s.rstrip("\n") + ARM + "\n", encoding="utf-8")
print("ok")
