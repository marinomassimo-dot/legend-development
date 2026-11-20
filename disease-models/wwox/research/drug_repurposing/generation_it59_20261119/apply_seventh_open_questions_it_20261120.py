"""IT59 (2026-11-20): one dated line on WO-24 (T-type involvement) for the body of Uebele 2009 as read by SCI in the blind scoring of RP-005 (ADV-109 item 1): the TTA-A2 temperature effect
is time-of-day dependent; folded into the NEXT card packet change, not a card change now. Appended, never rewritten; no status change. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
MARK = "[IT 2026-11-20, the body of Uebele 2009"
TEXT = (" [IT 2026-11-20, the body of Uebele 2009 (TTA-A2, PMID 19451696; read by SCI for the blind scoring of RP-005, one plain GET of the PMC article page, not a receipt; figures not opened as images) bears on the class-level harm and confounder readout "
 "(v3.1 6.15) and differs from the abstract-level sentence carried by card EB-ETX-01: the text gives core temperature after TTA-A2 as a direction and never a number; the only plot (Figure 6C, telemetry) is in mice fed a high-fat diet for 2 weeks, not in normal-weight animals, and the effect is TIME-OF-DAY DEPENDENT (lower in the inactive phase, higher in the active phase); "
 "the animals are adult where an age is stated (telemetry mice 'adult', rats 135 days old) and no juvenile or pup arm exists in the paper; TTA-A2 is not reported in any Cav3.1-null animal (the null mice appear only on a high-fat diet, with food intake 'lower overall' in the body where the abstract says 'without changes in food intake'); "
 "food intake under TTA-A2 was reduced in the high-fat-diet experiments and not different on normal chow. Consequence for a pup design (SCI's note, not decided here): core temperature beside the energy variables would need sampling at fixed clock times against vehicle, which the laboratory would have to state, because a pup has no mature circadian rhythm. "
 "No card text is changed by this line: the card sentence is abstract-level, labelled so, and its correction waits for the next card packet change (the package is on hold). This row stays OPEN. Record: prospective_rp005_adv106_20261120/RESULT_RP005_ADV106_IT_20261120.md section 6; SCI scoring: prospective_rp005_adv106_20261120/SCORING_RP005_ADV106_SCI_20261120.md.]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] == "WO-24" and MARK not in r[i]:
        r[i] += TEXT; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
