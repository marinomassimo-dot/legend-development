"""IT59 (2026-11-20), ADV-097 items 2 and 3: SCI's dated v2 revision of the two unit C priority experiments (UNIT_C_PRIORITY_EXPERIMENTS_V2_REVISION_SCI_20261120; v1 kept) carried as one more dated line on WO-20, WO-27 and IT56-Q14,
with two remarks flagged as IT's reading. Class-level; no dose, concentration or exposure number is carried. No row added, no status change; cards and ranking inputs not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 13."
MARK = "on SCI's v2 revision of the priority experiments"
D = {
 "WO-20": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + " (v1 kept; v2 supersedes it only where it says so): the bridge experiment IS ordering row 3 and stage 2 of the pup brief P2, specified once by pointer; v2 adds TWO knockout ages and a wild-type series of three ages (the age floor is claimed only from the wild-type series, not from the knockout ages); a measured brain and serum exposure at each age and dose with a T-type engagement control, the null being interpretable only against BOTH potency readings (a null between the two readings is 'uninterpretable between potencies', a null below the lower one a 'dose null'); a tonic-inhibition arm with a decision rule fixed before data (protection per sedation margin; ties named; ethosuximide stays the lead by prior position on a full tie); a power statement; a mandatory spontaneous-burden readout if the line shows events, else the result is labelled a provoked-seizure lead; an eight-row decision table in which every row names a decision. "
          "POWER: positive-specific against positive-general is NOT reachable unless the pilot standard deviation is about the optimistic value, which the held Cheng figures do not support: the specificity question collapses to 'underpowered' and the experiment is read as a provoked-seizure lead in the knockout; the interval-spanning outcome (no decision) is therefore the most likely single outcome at feasible n, which makes the pilot the first step (its decision: set n or stop). IT's reading, flagged: this experiment cannot settle whether the ethosuximide effect is WWOX-specific; that stays the INV-04 design question (WO-20's interaction term) or the binary generalised-seizure outcome." + REC + "]"),
 "WO-27": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + " (v1 kept): the broad head-to-head now has aligned windows for both classes with the route difference declared (stated 'under these windows and routes', not route-independent); engagement controls (a terminal brain level in satellite pups, an ex vivo OPC differentiation readout from the same litters, a thyroid-response transcript for the thyromimetic, a response in treated wild-type littermates for clemastine: an arm without that response is a failed engagement, not a negative); n fixed from the held per-animal spread (a half-deficit rescue reachable, a quarter-deficit rescue declared not reachable); the benchmark's functional tier (weight, survival, motor, glucose) as a second tier; a named decision for every outcome including 'carry to a functional-endpoint study' (tier 1 only: partial against the benchmark by construction), 'do not carry forward as a disease-directed candidate' (effect only at the higher dose or only in wild type) and 'uninterpretable, repeat named' (failed engagement). "
          "IT's reading, flagged: the thyroid-response transcript used as the thyromimetic engagement control (Hairless) is expressed in mature oligodendrocytes, which the same cortex shows lower; in treated knockouts it could rise because of more mature cells rather than thyroid engagement, so it is not independent of the outcome: prefer a thyroid-response readout not enriched in the lineage (or a peripheral thyroid-axis readout) as the engagement control." + REC + "]"),
 "IT56-Q14": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + ": the bridge priority experiment is stated once (ordering row 3 and stage 2 of the pup brief by pointer, plus the named additions); its eight-row decision table replaces the five outcome classes of v1; the earlier arm-order reading of this row is unchanged." + REC + "]"),
}
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] in D and MARK not in r[i]:
        r[i] += D[r[0]]; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
