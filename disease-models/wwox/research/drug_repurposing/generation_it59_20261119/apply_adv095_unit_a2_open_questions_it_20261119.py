"""IT59 (2026-11-19), ADV-097 item 3: SCI's unit A2 (lineage state, registered verdict UNDECIDED) carried into two existing open-question rows as dated lines, with ADV's wording on the myelin convergence.
No row is added, no status changes; cards and ranking inputs are not edited (ADV decision). Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 8."
WO27 = (" [IT 2026-11-19, ADV-097 consumption, on SCI's unit A2 (lineage state; registered verdict UNDECIDED; blind recompute of unit A matched): LOSS is rejected (stage-adjusted pan-lineage set -0.10, OPC set -0.07) and tissue-wide DELAY is rejected (a delay fitted on the neuronal covariate genes gives 4.4 days, outside the model's 0 to 3 day range, and predicts the early-stage sets higher where they are lower; explained fraction 0.03; delay-equivalent addendum for the mature set: 1, 2, 3 days of delay shift it by -0.03, -0.07, -0.10 against the observed raw -1.06, about 31 days needed). "
        "BLOCK as registered is not met only because the committed-precursor (COP) set is lower (-0.51 against a line of -0.3 that is uncalibrated and inside that set's leave-one-animal-out range); post hoc the progenitors are intact (OPC -0.07) and every stage from the committed precursor onward is lower by about -0.4 to -0.6: a deficit in progression from progenitor to committed precursor, block or fewer cells passing, not separable without cell-level data. "
        "IN-SILICO part that can still change the comparison: only what the held data cannot give (3 to 4 animals per arm, covariate collinear with genotype); the neuronal-support component is likely (the cortex deposit is a neuron-targeted deletion) and not separable. MEASUREMENT only an experiment supplies, and the priority experiment per A2 before any agent: a cell-level readout (lineage-stage counts and a differentiation challenge in knockout tissue or an OPC culture from it); the question whether the neuron still emits the activity-dependent axonal signal stays. "
        "WORDING (ADV): a myelin deficit is reported at two levels of one model (ultrastructure with neuronal-AAV9 rescue in the AAV9 papers; mature-oligodendrocyte transcripts in the P17 deposits): consistent in direction at two levels of one model and one laboratory's cohort family; no independent confirmation; not additive; mouse only." + REC + "]")
IT50 = (" [IT 2026-11-19, ADV-097 consumption, IT's reading of SCI's unit A2 (flagged as IT's, not SCI's): the matched step is progenitor to committed precursor, so a stage-resolved readout (committed-precursor and newly formed oligodendrocyte counts, not only the MBP-positive share) would separate a block from fewer cells passing; the conditioned-medium design is unchanged; the lineage defect follows a neuron-targeted deletion, so a neuron-side signal is the open question this row and WO-27 share." + REC + "]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] == "WO-27" and "on SCI's unit A2" not in r[i]:
        r[i] += WO27; r[j] = "2026-11-19"; n += 1
    if r[0] == "IT50-Q10" and "unit A2" not in r[i]:
        r[i] += IT50; r[j] = "2026-11-19"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
