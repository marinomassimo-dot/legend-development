"""IT59 (2026-11-19), ADV-097 item 3: two dated lines on existing open-question rows after HE's normalisation note (ADV-096 stage 1). No row is added; no status changes.
IT56-Q14 (CONCLUDED): unchanged, with the reason. IT56-Q01 (OPEN): the single row now says which part is an in-silico uncertainty that can still change the comparison and which
part only a measurement can settle. Idempotent (marker text). The text above each line in the cell is not edited."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
M = "ADV-097 consumption 2026-11-19"
Q14 = (" [IT 2026-11-19, ADV-097 consumption, on HE's normalisation note: UNCHANGED. The proposed arm order rests on which agents have an in vivo Wwox-null measurement, not on the simulated class order; "
       "that order is partly imposed by the per-arm multipliers (d-APV and the pore blocker perturb the same parameter and tie), so it supplies no ranking of classes here. Record: adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md]")
Q01 = (" [IT 2026-11-19, ADV-097 consumption, on HE's normalisation note: two parts, one row. (a) IN-SILICO uncertainty that can still change the comparison: the tonic-inhibition challenger's simulated position depends on the neurosteroid-type arm's composite "
       "(J_tonic x1.2 with J_I x1.1, a chosen ratio) and on the same-parameter normalisation; HE's parametric-sensitivity stage can show whether the composite's position survives other ratios and a few joint scenarios (not structural alternatives). "
       "(b) The MEASUREMENT only an experiment can supply: the tonic conductance and its carrier in Wwox-deficient layer 2/3 neurons; no analysis replaces it, and it is selected only if the in-silico part leaves the challenger competitive. Record: adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
for r in rows[1:]:
    if r[0] == "IT56-Q14" and M not in r[i]:
        r[i] += Q14.replace("ADV-097 consumption", M); r[j] = "2026-11-19"
    if r[0] == "IT56-Q01" and M not in r[i]:
        r[i] += Q01.replace("ADV-097 consumption", M); r[j] = "2026-11-19"
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok")
