"""IT58 / ADV-067 (2026-11-19): map SCI's lithium-regimen decision into the INV-09 package in ONE pass. Mapping only: every statement is SCI's (LITHIUM_REGIMEN_DECISION_ADV067_SCI_20261119.md, sections 1, 4, 5),
appended under a marker to the cell it bears on; the original text stays. Hypothesis level; no dose, no schedule. Idempotent. Run after build_packages.py, apply_k2_mapping_adv066.py and apply_kcc2_withdrawal_adv066.py."""
import csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
NOTE = "advisor_pilot_20261113/brainstorm_20261116/adv067_lithium_regimen_sci_20261118/LITHIUM_REGIMEN_DECISION_ADV067_SCI_20261119.md"
M = "[ADV-067 mapping, 2026-11-19, IT, from SCI's note (sections 1, 4, 5), mapped not authored:"
HYP = {
 "L2": {"weakening_result": M + " from the image of the one held experiment the proportional reduction by lithium looks similar in the three genotypes (an eye reading), which fits a general effect or a regimen artefact better than a knockout-enhanced GSK-3 effect. Source: " + NOTE + "]",
        "next_decision": M + " a second GSK-3 inhibitor of another class is MORE necessary, because the single regimen cannot exclude a lithium-specific or regimen artefact and a different chemotype with its own artefact check is the only discriminator in the design. Source: " + NOTE + "]"},
 "L3": {"next_decision": M + " one regimen (the repeated pretreatment of the one held experiment) is the main contrast, not two: no regimen in the table shows a clear sign flip and the acute pro-convulsant result is one abstract with unreadable interval and method; a single acute injection is an optional comparator arm only; a lithium-alone arm carries a sedation, righting-reflex and weight readout at the time of the provoked seizure and the interval from the last injection to the seizure is recorded. Source: " + NOTE + "]"},
}
CMP = {"C-GS1": {"mechanism_discriminating_control": M + " lithium-alone arm with a sedation, righting-reflex and weight readout at the time of the provoked seizure; interval from the last injection to the seizure recorded; one regimen as the main contrast; a second GSK-3 inhibitor of another class is more necessary. Source: " + NOTE + "]"}}
def edit(path, key_col, edits):
    rows = list(csv.reader(open(path, encoding="utf-8"), delimiter="\t")); h = rows[0]; n = 0
    for r in rows[1:]:
        for col, txt in edits.get(r[0], {}).items():
            i = h.index(col)
            if M not in r[i]: r[i] = r[i] + " " + txt; n += 1
    with open(path, "w", newline="", encoding="utf-8") as f: csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
    return n
base = HERE / "inv09_lithium_gsk3_regimen" / "output"
print("hypotheses cells changed:", edit(base / "hypotheses.tsv", "hypothesis_id", HYP), "| comparison cells changed:", edit(base / "comparison.tsv", "row_id", CMP))
