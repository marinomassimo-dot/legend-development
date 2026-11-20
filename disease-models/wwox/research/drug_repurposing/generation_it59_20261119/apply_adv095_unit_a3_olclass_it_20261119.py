"""IT59 (2026-11-19), ADV-097 item 3: SCI's unit A3 (activity-dependent branch STOPPED at its registered first test) and the CLASS-LEVEL reading of the oligodendrocyte-class agent producer report
(partial, producer output UNVERIFIED: no number is carried) added to WO-27 as one more dated line. No row is added; no status change; cards and ranking inputs are not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 9."
WO27 = (" [IT 2026-11-19, ADV-097 consumption, on SCI's unit A3 and the oligodendrocyte-class agent report: (a) A3 (registered verdict STOP THE BRANCH): no neuronal-activity route is opened on the held data; the activity-regulated deficit is a cortex BULK finding (adjusted -1.26, every leave-one-animal-out fit negative) that the held nuclei, which are hippocampal, cannot localise to a cell type (excitatory neurons -0.05 against a line of -0.3); the across-contrast coupling with the oligodendrocyte deficit does not hold; the stop does not refute a neuronal deficit in the cortex, it says the held data cannot test it; REOPENING needs a cortical nuclei or cell-type-resolved deposit of the neuron-targeted deletion (a supply need recorded for ADV, not a quote). "
        "So the oligodendrocyte-class unit stays the only broad route under test; the non-cell-autonomy reading is kept as an explanation without a route. (b) CLASS-LEVEL reading only of the agent unit (PARTIAL; producer output NOT verified; no affinity, juvenile exposure or label was retrieved; NO number is carried): two classes are the candidates under test for oligodendrocyte differentiation, the muscarinic-antagonist class represented by clemastine and the thyromimetic class (which therefore did enter the screen, through this unit and as a class), with null results in myelin-deficient rat models and a timing window for the thyromimetic Triac reported by the producer; a catalogue match is not support (verified pharmacology record: none for either class). "
        "IN-SILICO part still able to change the comparison: the verifier pass and the exposure round (SCI), which decide whether either class survives; MEASUREMENT only an experiment supplies: the cell-level lineage readout named in the A2 line above." + REC + "]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] == "WO-27" and "on SCI's unit A3" not in r[i]:
        r[i] += WO27; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
