"""IT59 (2026-11-20): dated lines on the open-questions map for the THIRD packet change (HE ADV-098 batches 7, 8 and 10 consumed; operator's morning mandate item 1) and two corrections:
IT52-Q01 (answer by molecule for ISRIB: one cell-reporter row), WO-21 and WO-27 (IT's own earlier wording 'a flat panel closes the candidate for this model' corrected to SCI's redefinition: a flat panel excludes ONE proposition),
WO-35 (Fig 5c wild-type arm: two sources disagree with the note; unresolved without the figure), WO-27 (tazemetostat and TMP195 carried as compound-level lines; no card). Lines are appended, never rewritten. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 22."
D = {
 "IT52-Q01": ("HE ADV-098 batch 8 consumed (identity by structure",
  " [IT 2026-11-20, HE ADV-098 batch 8 consumed (identity by structure, not by name): the by-molecule query now gives ONE database row for ISRIB, an ATF4 reporter in human H4 cells after 24 hours (IC50 2.7 nanomolar, one document): a cell readout of the stress-response output, not a binding and not an eIF2B measurement. No eIF2B activity row, no binding or selectivity row, no neuronal value and no second-laboratory value were found by those routes; no measured brain or plasma concentration was found; trazodone has no PERK, eIF2 alpha phosphorylation or stress-response row. The identity of the compound is by structure (its name is not found by the identity tool), so a name lookup would have missed it. Consequence: the evidence layer of INV-02's probe arm stays at literature plus one cell reporter; card E01 carries these facts at class level, not WWOX evidence." + REC + "]"),
 "WO-21": ("is withdrawn. On SCI's v3.1 redefinition",
  " [IT 2026-11-20, correction of IT's own earlier line above: 'S-flat closes it for THIS model' is withdrawn. On SCI's v3.1 redefinition (the operator's S-flat redefinition) a flat panel excludes ONE proposition (that GSK-3 beta restraint on tau is released in bulk cortex of the neuronal-deletion line at postnatal day 17, at the tested tau sites, above the margin fixed before data; six propositions are not excluded, listed in section 6.10); it does not close the candidate and it does not close the class. Cards D02 and the ranking text were corrected in place the same day (third packet change)." + REC + "]"),
 "WO-27": ("a flat panel closes GSK-3 for this model' is withdrawn",
  " [IT 2026-11-20, correction of IT's own earlier line above: 'a flat panel closes GSK-3 for this model' is withdrawn; a flat panel excludes ONE proposition (that GSK-3 beta restraint on tau is released in bulk cortex of the neuronal-deletion line at postnatal day 17, at the tested tau sites, above the margin fixed before data; SCI v3.1 section 6.10) and neither closes the candidate nor the class, so the forbidden reading stays forbidden in both directions. Compound-level facts added from HE batch 10 for two agents WITHOUT a card, no ranking input, not WWOX evidence: tazemetostat (EZH2 inhibitor; enzyme IC50 ranges about 500-fold across documents, and the Ki of 2.5 nanomolar is one origin quoted in five documents; P-glycoprotein limits its brain accumulation in mice, a mechanism for a missing exposure and not a measurement; label from age 16 and a juvenile rat finding) and TMP195 (class IIa HDAC inhibitor; two documents agree on the order of potency and differ 2- to 7-fold in value; cell activity weaker than enzyme activity; no exposure, no label). Class IIa HDACs and EZH2 are not WWOX premises found by SCI's screen." + REC + "]"),
 "WO-35": ("two sources disagree with the phrase",
  " [IT 2026-11-20, on SCI's ADV-101 increment 1: two sources disagree with the phrase 'no wild-type arm' above (the Fig 5c legend text, KO = 3 and WT = 3 with a PBS control; the ADV-074 producer's row); unresolved without the figure (Abu-Remaileh 2014 Fig 5c is not obtainable by lawful routes); no claim rests on the wild-type arm." + REC + "]"),
}
p = DR / "batch_sci_20261105/map/open_questions_map.tsv"
rows = list(csv.reader(open(p, newline="", encoding="utf-8"), delimiter="\t"))
i = rows[0].index("status_evidence"); j = rows[0].index("last_touched")
n = 0
for r in rows[1:]:
    if r[0] in D:
        mark, text = D[r[0]]
        if mark not in r[i]:
            r[i] += text; r[j] = "2026-11-20"; n += 1
with open(p, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
print("ok", n)
