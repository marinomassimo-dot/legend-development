"""IT59 (2026-11-20), ADV-097 item 3: SCI's GSK-3 follow-up (v2.2 premise panel, one-unit note with the harm cell, verifier report; gsk3_shared_premise_sci_20261120, on main 67abc7d7e)
carried as dated lines on WO-21 (GSK-3 / lithium, INV-09) and WO-27 (the broad hub). Class level; no row added; cards, units, ranking inputs and the claim registry not edited. Idempotent."""
import csv
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
REC = " Record: advisor_pilot_20261113/brainstorm_20261116/adv097_consumption_it_20261119/CONSUMPTION_RECORD_ADV097_IT_20261119.md section 17."
MARK = "on SCI's v2.2 GSK-3 premise panel"
D = {
 "WO-21": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + " and one-unit note: the shared discriminator now exists as a DESIGN (v2.2 A.6: tau pS396 and pS404 over total tau, the regulatory sites over their totals, beta-catenin, in the frozen hemisphere of the animals the v2 broad experiment already uses; no animal added; a large-effect detector: 12 knockout against 8 wild type detects about 1.3 SD, 0.5 SD would need about 64 per genotype). "
           "Decision per outcome fixed before data: S-up keeps the candidate and opens a GSK-3-inhibitor arm; S-flat closes it for THIS model (bulk cortex, P17, neuronal-deletion line, effects below the margin, minority populations not excluded; Q230P effect on binding untested, so a transfer to the missense class is not shown); S-down read first for composition. "
           "The pS9 tension between Wang 2012 and Cheng 2020 can be addressed in tissue for the first time (pS9 over TOTAL GSK3-beta, not over actin as in Cheng's Fig 7c). Harm cell written: embryonic cortical progenitors (Ma 2017 knockdown in a subset of cells, not a drug; Kim 2009 double deletion), lithium label limits, no infant data for any GSK-3 inhibitor found. Nothing here ranks the two candidates; no number goes into a card until ADV accepts compound-level units." + REC + "]"),
 "WO-27": (" [IT 2026-11-20, ADV-097 consumption, " + MARK + " and one-unit note: the two broad candidates are put on one unit (action, context, benefit, endpoint) and NOT ranked: they share the context and tissue, not benefit or endpoint. Each outcome of the shared experiment is named for each candidate: a flat panel closes GSK-3 for this model and leaves the oligodendrocyte class unchanged (it never depended on the panel); an elevated panel keeps GSK-3 and gives the lineage readout an independent cousin (exploratory association, n = 12, no causal statement; GSK-3 inside the lineage has a divided sign, so a bulk panel cannot say neuronal from lineage-internal). "
           "Forbidden reading: 'S-flat closes GSK-3, therefore the oligodendrocyte class wins'. Both flat panel and negative lineage arm would leave the broad objective without a premise-supported candidate: a result, not a failure. In-silico uncertainty that can still change this comparison: none identified beyond the large-effect limit of the panel; the essential experimental measure is the panel and the v2 tier-1 lineage readout in the same animals." + REC + "]"),
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
