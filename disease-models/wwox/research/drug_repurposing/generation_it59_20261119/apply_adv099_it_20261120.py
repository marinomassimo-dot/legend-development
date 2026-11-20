"""IT59 (2026-11-20), ADV-097 item 3: SCI's ADV-099 (unbiased neuron-internal discovery in the two held neuron-resolved systems; registered NOTHING_REPLICATES_BEYOND_CHANCE in all four cells, mapping not run by the stop rule)
carried as one dated line on WO-27, the hub row of the broad objective, together with SCI's v2.1 dated line (peripheral thyroid-axis readout replaces the Hairless engagement control: IT's remark taken). Class-level; no row added; no status change;
cards and ranking inputs not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 14."
WO27 = (" [IT 2026-11-20, ADV-097 consumption, on SCI's ADV-099 and v2.1: (a) ADV-099 (unbiased neuron-internal discovery; registered verdict NOTHING_REPLICATES_BEYOND_CHANCE in all four cells, excitatory and inhibitory neurons, up and down, between the held hippocampal nuclei and the human organoid bulk; blind recompute reproduced the verdict): the observed replicated gene counts equal what shuffling gives, so the 182 listed gene rows are what chance gives and are NOT candidates; the mapping steps (enrichment, druggability, agent classes, endpoint placement) were NOT run by the stop rule; no new candidate class is named. The nuclei and the organoid are not independent of the arms they come from (one pool per arm; organoid = two groups of knockout libraries, clonal identity not stated). "
        "Consequence for the broad objective: a neuron-intrinsic route is not opened on the held data (second null after A3); the oligodendrocyte-class unit stays the only broad route under test; the in-silico uncertainty about a neuron-intrinsic route is exhausted on the two held neuron-resolved systems. (b) v2.1 (SCI): IT's remark taken: the thyromimetic engagement control is now a peripheral thyroid-axis readout plus a thyroid-response transcript not enriched in the oligodendrocyte lineage, replacing the oligodendrocyte-enriched transcript; the bridge pilot is stated as the first step with the decision 'set n or stop', specificity staying the INV-04 design question." + REC + "]")
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] == "WO-27" and "on SCI's ADV-099 and v2.1" not in r[i]:
        r[i] += WO27; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
