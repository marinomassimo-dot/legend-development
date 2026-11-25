"""IT 2026-11-24 (ADV decision): the IT30 conditional-question ids of the open-questions map follow the pinned commit 852a26aca (five rows);
the TSV on main was renumbered by commit 8b01ff1da (clonazepam inserted as 04, vigabatrin now 06, class rows 07 to 09 added).
(1) source_ref of IT30-CQ4 and IT30-CQ5 now points at the current anchors (#CQ-IT30-05 rapamycin, #CQ-IT30-06 vigabatrin); the pinned ids stay in a dated note.
(2) the vigabatrin qualifier goes into the status_evidence of IT30-CQ5 (the question cell is at its 300-character cap), as a dated line.
(3) four missing rows are added: IT30-CQ6 (clonazepam, TSV CQ-IT30-04), IT30-CQ7 to IT30-CQ9 (class rows CQ-IT30-07 to 09), and the source-items index is aligned.
Idempotent; appended, never rewritten; no status change of an existing row. Run from the repository root. Hypothesis level; no ranking, drug or priority change."""
import csv
from pathlib import Path
DR = Path("disease-models/wwox/research/drug_repurposing")
MAP = DR / "batch_sci_20261105/map/open_questions_map.tsv"
IDX = DR / "batch_sci_20261105/map/source_items_index.tsv"
TSV = DR / "context_it30_20261105/results/conditional_questions_it30.tsv"
REF = "disease-models/wwox/research/drug_repurposing/context_it30_20261105/results/conditional_questions_it30.tsv"
MARK = "[IT 2026-11-24 id alignment"
NOTE4 = (" [IT 2026-11-24 id alignment: this row was built on the pinned commit 852a26aca (five rows, rapamycin = CQ-IT30-04); the TSV on main was renumbered by commit 8b01ff1da, "
         "where rapamycin is CQ-IT30-05 and CQ-IT30-04 is clonazepam (row IT30-CQ6 below); source_ref now names the current anchor, the bracketed id in the question text is the pinned one.]")
NOTE5 = (" [IT 2026-11-24 id alignment: pinned-commit id CQ-IT30-05, current id CQ-IT30-06 (see IT30-CQ4); source_ref now names the current anchor. "
         "Dated qualifier on the adverse leg (question cell at its 300-character cap), from the held scn1lab paper as read by SCI in ADV-216 (FTR-20261124-24002024-01): "
         "vigabatrin gave higher electrographic burst frequency in 6 of 7 fish at one 1 mM bath concentration, no group test reported; the same paper's locomotion assay is opposite in sign (about -30 percent, not significant): "
         "the two assays disagree for the same drug, so 'adverse' means aggravation untested, not shown. No WWOX content. No status or ranking change.]")
DEC = "Conditional question: names the context that must be matched before the compound is read as a lever; no class transfer."
tsv = {r["question_id"]: r for r in csv.DictReader(open(TSV, newline="", encoding="utf-8"), delimiter="\t")}
NEW = [("IT30-CQ6", "CQ-IT30-04", "literature_executable", "yes"), ("IT30-CQ7", "CQ-IT30-07", "wet_lab_measurement", "no"),
       ("IT30-CQ8", "CQ-IT30-08", "wet_lab_measurement", "no"), ("IT30-CQ9", "CQ-IT30-09", "wet_lab_measurement", "no")]
rows = list(csv.reader(open(MAP, newline="", encoding="utf-8"), delimiter="\t")); h = rows[0]
ix = {k: h.index(k) for k in h}
n = 0
for r in rows[1:]:
    if r[0] == "IT30-CQ4" and MARK not in r[ix["status_evidence"]]:
        r[ix["source_ref"]] = REF + "#CQ-IT30-05"; r[ix["status_evidence"]] += NOTE4; r[ix["last_touched"]] = "2026-11-24"; n += 1
    if r[0] == "IT30-CQ5" and MARK not in r[ix["status_evidence"]]:
        r[ix["source_ref"]] = REF + "#CQ-IT30-06"; r[ix["status_evidence"]] += NOTE5; r[ix["last_touched"]] = "2026-11-24"; n += 1
have = {r[0] for r in rows}
for qid, tid, kind, ex in NEW:
    if qid in have: continue
    t = tsv[tid]
    q = ("[%s; %s; %s] %s" % (tid, t["compound"], t["theme"], t["question"]))[:300]
    ev = ("main:%s#%s (renumbered by commit 8b01ff1da; added to the map by IT on 2026-11-24, the map was built on the pinned commit 852a26aca)" % (REF, tid))
    row = [""] * len(h)
    row[ix["qid"]] = qid; row[ix["source_ref"]] = REF + "#" + tid; row[ix["question_text_max300"]] = q; row[ix["decision_at_stake_max200"]] = DEC
    row[ix["kind"]] = kind; row[ix["status"]] = "OPEN"; row[ix["published_on"]] = "main"; row[ix["status_evidence"]] = ev
    row[ix["last_touched"]] = "2026-11-24"; row[ix["blocking_reason"]] = "Conditional question in the IT30 context table; it neither qualifies nor ranks the compound or class. Row added late (the map predates the renumbering)."
    row[ix["executable_zero_spend"]] = ex; row[ix["claimed_by"]] = ""
    assert len(q) <= 300 and len(DEC) <= 200
    rows.append(row); n += 1
with open(MAP, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
idx = list(csv.reader(open(IDX, newline="", encoding="utf-8"), delimiter="\t")); m = 0
for r in idx[1:]:
    if r[2] == "IT30-CQ4" and r[0] == "CQ-IT30-04": r[0] = "CQ-IT30-05"; r[4] = "renumbered on main by 8b01ff1da; pinned id was CQ-IT30-04"; m += 1
    if r[2] == "IT30-CQ5" and r[0] == "CQ-IT30-05": r[0] = "CQ-IT30-06"; r[4] = "renumbered on main by 8b01ff1da; pinned id was CQ-IT30-05"; m += 1
have_i = {(r[0], r[2]) for r in idx[1:]}
for qid, tid, _, _ in NEW:
    if (tid, qid) not in have_i:
        idx.append([tid, "task/it30 context_it30_20261105/results/conditional_questions_it30.tsv (on main)", qid, "primary", "added 2026-11-24", ""]); m += 1
with open(IDX, "w", newline="", encoding="utf-8") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(idx)
print("map edits", n, "index edits", m)
