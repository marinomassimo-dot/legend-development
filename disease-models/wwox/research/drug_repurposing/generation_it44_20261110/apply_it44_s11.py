"""IT44 P3: the S11 result reaches the consumers: INV-18 decisive_uncertainty (both tables), the compound view (V14), two open questions. Idempotent; marker [IT44]."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
T = "[IT44] Which family carries a lost resting conductance decides whether any opener is relevant: the TREK and TRAAK channels are blocked only at millimolar Ba2+ (a source reports no effect at 0.8 mM), so a current lost at 200 micromolar Ba2+ or less points to Kir-type channels (or TWIK-1), whereas the openers found in the catalogue act on the Ba2+-weak K2P subfamily; the only Kir2 opener reached is Kir2.1-only with no neuronal data; TASK-1, TASK-3 and THIK-1 were not reached."
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    rows = rd(f); h = rows[0]
    for r in rows[1:]:
        if r[h.index("inv_id")] == "INV-18" and "[IT44]" not in r[h.index("decisive_uncertainty")]: r[h.index("decisive_uncertainty")] += " " + T
    wr(f, rows)
P = "generation_it41_20261109/compound_view.tsv"; rows = rd(P); h = rows[0]
if not any(r[h.index("item_id")] == "V14" for r in rows):
    v = dict(order="14", item_id="V14", inv_id="INV-18", kind="unresolved", name_full="riluzole; BL-1249; flufenamic acid (K2P-type openers); zacopride (Kir2.1 opener)", origin="relation_search", relation_id="S11", where_done="in_silico_then_laboratory",
      label="Adding a resting K+ conductance with an opener: the openers that exist act on the weakly Ba2+-sensitive channel family",
      action="Opening of K2P-type (TREK, TRAAK) or Kir2-type channels to restore a resting K+ conductance.",
      rationale="The action was named without a compound; the search shows catalogued openers exist for the K2P family, so the question becomes whether a lost current would be of that family.",
      open_premise="That the lost current, if any, is Ba2+-sensitive and of a family an opener reaches: TREK and TRAAK are blocked only at millimolar Ba2+, and the one Kir2 opener reached is Kir2.1-only with no neuronal data; capacitance by genotype is unmeasured.",
      counter="The glutamate-release modulator active on K2P channels also blocks sodium channels and glutamate release at lower concentrations and needs about 100 micromolar for the K2P effect; its activation of one family member is transient; some potencies rest on a review, not a primary paper; selectivity of the research activator against other channels is not fully reached.",
      next_test="Measure capacitance, then the Ba2+-sensitive current per pF at a low and a high Ba2+ concentration; only a current blocked by low micromolar Ba2+ points to Kir-type channels; compare an opener with a blocker only after that.",
      moves="Up: a current blocked at low micromolar Ba2+ and smaller per pF in the mutant (the opener route is then narrow). Down: a Ba2+-sensitive share only at millimolar concentrations, equal per pF, or a lower capacitance with flat time constant.",
      source_rows="relation_s11_result_it44.md; verify_s11/VERDICTS.md; s11/search_rows (S11)", registry_note="Registry: GtoPdb activator rows on the K2P family, ChEMBL activity rows on TREK-1 from a review document; Kir2: PIP2 only (physiological).")
    rows.append([v.get(c, "") for c in h]); wr(P, rows)
M = "batch_sci_20261105/map/open_questions_map.tsv"; rows = rd(M); h = rows[0]
Q = [("IT44-Q01", "What is the Ba2+ concentration-response (50-200 micromolar window) of TASK-1, TASK-3 and THIK-1, and is any Kir2.2 or Kir2.3 opener published? INFERENZA; reading task; no rank; reopen condition: primary sources read.", "Decides which channel families can carry a Ba2+-sensitive resting conductance and whether any opener exists for them."),
     ("IT44-Q02", "What do the primary papers give for the EC50 and conditions of the approved glutamate-release modulator on TRAAK and TREK-1, and of the fenamate on TREK channels? INFERENZA; reading task; no rank.", "Decides whether the K2P opener rows rest on primary data (now a review document) before any comparison.")]
for qid, txt, dec in Q:
    if not any(r[0] == qid for r in rows):
        d = dict(qid=qid, source_ref="generation_it44_20261110/verify_s11/VERDICTS.md", question_text_max300=txt, decision_at_stake_max200=dec, kind="literature_executable", status="OPEN", published_on="task/it44", status_evidence="generation_it44_20261110/relation_s11_result_it44.md", last_touched="2026-11-10", blocking_reason="Not read in any package.", executable_zero_spend="yes", claimed_by="")
        rows.append([d.get(c, "") for c in h])
wr(M, rows); print("applied")
