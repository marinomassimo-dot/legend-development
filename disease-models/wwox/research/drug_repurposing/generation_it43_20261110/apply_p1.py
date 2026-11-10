"""IT43 P1: the engine's role for Ro 25-6981 reaches the compound view and the open-questions map. Idempotent; marker [IT43].
Before: V02 listed 'ifenprodil; Ro 25-6981' as one probe. After: only ifenprodil is a probe (primary read of its maxima, D01-D03); Ro 25-6981
has abstract-level values and a transferred triheteromer behaviour (D05, D08, D11) so it moves to V08 (unresolved) and its public-source reading becomes IT43-Q01."""
import csv, io, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parent.parent; T = "[IT43] "
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
P = "generation_it41_20261109/compound_view.tsv"; rows = rd(P); ix = {k: i for i, k in enumerate(rows[0])}
for r in rows[1:]:
    if r[ix["item_id"]] == "V02" and "Ro 25-6981" in r[ix["name_full"]]:
        r[ix["name_full"]] = "ifenprodil"
        r[ix["source_rows"]] += "; comparison_engine_it43 (tier PRIMARY)"
    if r[ix["item_id"]] == "V08" and "moved here from the tool entry" not in r[ix["counter"]]:
        r[ix["name_full"]] = "traxoprodil; rislenemdaz; EVT-101; Ro 25-6981"
        r[ix["counter"]] += " A second ifenprodil-site tool, moved here from the tool entry: only abstract-level values were reached and its triheteromer behaviour is transferred from another compound, so it is not a tool for this comparison until its primary source is read."
        r[ix["next_test"]] += " For that second tool the first step is reading its primary source; no new measurement is needed for that."
        r[ix["source_rows"]] += "; comparison_engine_it43 (Ro 25-6981: tier TRANSFER)"
wr(P, rows)
M = "batch_sci_20261105/map/open_questions_map.tsv"; m = rd(M)
if not any(x[0] == "IT43-Q01" for x in m):
    h = m[0]; row = dict(qid="IT43-Q01", source_ref="generation_it43_20261110/compound_decisions_it43.tsv",
        question_text_max300="Does a primary source give the maximum inhibition, site and conditions of Ro 25-6981 on GluN1/GluN2B and on triheteromers? INFERENZA; reading task; no rank; reopen condition: primary text reached.",
        decision_at_stake_max200="Decides whether Ro 25-6981 can be named a second tool of the ifenprodil site (tier PRIMARY) or stays unresolved.",
        kind="literature_executable", status="OPEN", published_on="task/it43", status_evidence="generation_it43_20261110/README.md", last_touched="2026-11-10",
        blocking_reason="Primary full text not reached in any package.", executable_zero_spend="yes", claimed_by="")
    m.append([row.get(c, "") for c in h]); wr(M, m)
print("applied")
