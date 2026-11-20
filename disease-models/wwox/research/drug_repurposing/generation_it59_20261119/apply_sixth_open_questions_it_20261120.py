"""IT59 (2026-11-20): dated lines on WO-34 (glial density before the first spike) and IT59-Q04 (metabolic state against seizures and death) for SCI's ADV-104 and ADV-101 increment 2,
the fifth packet change's open-question side. Lines are appended, never rewritten; no status changes. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = (" Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/"
       "CONSUMPTION_RECORD_ADV097_IT_20261119.md section 26.")
SCI = "advisor_pilot_20261113/brainstorm_20261116/"
D = {
 "WO-34": ("[IT 2026-11-20, SCI's ADV-104",
  " [IT 2026-11-20, SCI's ADV-104 (held texts first, pre-registered stop rule): the timing of glial change against seizure onset CANNOT be placed in any held line; every glial measurement held is at postnatal days 14 to 20 (germline null: area fractions at two weeks, cells at day 19, area fractions at day 20; the neuronal-deletion line has no held glial measurement, only a P17 bulk-transcript reactive-astrocyte signal, composition not excluded), while seizures start at day 9 (neuronal-deletion line) or within a few days after birth (germline null); 'not measured' before onset, not 'not present'. The axis is therefore carried as a READOUT beside glucose, not as an arm; neuronal restoration moves glial state together with everything else, glial-restricted deletion gave no phenotype in the held text, and the independent-modifiability route is contested in the nearest studied model (Rett, abstract level). The row stays OPEN: its decisive datum is the per-animal glial series before the first spike (the card J01 next measurement). SCI note: " + SCI + "glia_axis_adv104_sci_20261120/ADV104_GLIAL_INFLAMMATORY_AXIS_SCI_20261120.md." + REC + "]"),
 "IT59-Q04": ("[IT 2026-11-20, SCI's ADV-101 increment 2",
  " [IT 2026-11-20, SCI's ADV-101 increment 2 (held sheets and cards, no new paper): only two interventions on the axis carry any exposure statement and neither is usable for a pup (dichloroacetate: no brain concentration in mice and no juvenile exposure found, millimolar-range potency; a ketogenic diet: no ketone, glucose or intake value in any Wwox-deficient animal or child); no third was found by the sheets and searches used (not an absence claim). On held data the axis is a COVARIATE TO MEASURE, NOT AN ARM; SCI's conditions, fixed in its pre-registration: it would become the preferred broad candidate if glucose is already low at or before day 9 in the neuronal-deletion or progenitor-targeted pups AND a glucose or fuel-supply arm changes the spike rate, the seizure score or survival without WWOX restoration; it would be parked if those pups are normoglycaemic across days 7 to 14 while seizing and dying, if glucose falls only after the first seizure, or if a supply arm corrects glucose and weight but not the EEG or survival. The digoxin figure (Fig 5c) stays unresolved: the legend says three knockout and three wild-type mice with a PBS control, the earlier note WO-35 disagrees and cites no figure reading, and the figure is not held. This row stays OPEN. SCI note: " + SCI + "glycaemia_axis_adv101_sci_20261120/ADV101_INCREMENT2_Q3_Q4_SCI_20261120.md." + REC + "]"),
}
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
assert not [q for q in D if q not in {r[0] for r in rows[1:]}]
n = 0
for r in rows[1:]:
    if r[0] in D and D[r[0]][0] not in r[i]:
        r[i] += D[r[0]][1]; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
