"""IT44 P1/P6: consume SCI44 package A (pdh_pdk_sci44_20261110/consumer_delta.md rows 1, 2, 4, 5, 12, 13; rows 6-7 compound view in apply_sci44_view.py; rows 8-9 engine; row 10 identity facts in the README; row 11 relations; row 14 information; row 15 receipts recorded separately). Idempotent; marker [SCI44]."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
def edit(p, keycol, keyval, col, txt):
    rows = rd(p); h = rows[0]
    for r in rows[1:]:
        if r[h.index(keycol)] == keyval and "[SCI44]" not in r[h.index(col)]: r[h.index(col)] = (r[h.index(col)] + " " + txt).strip()
    wr(p, rows)
T = {("INV-07", "next_test"): "[SCI44] Read the step on marker-resolved or sorted material; the dominant kinase RNA differs by class and species (mouse neurons PDK2; human neurons PDK3; astrocytes PDK4 in both species; human oligodendrocytes PDK4): include PDK2-4 transcript and protein per class, a genetic knockdown of the dominant isoform before any compound, and the scaffold condition of any lipoamide-site tool. A restraint measured in one class does not transfer to another.",
     ("INV-07", "decisive_uncertainty"): "[SCI44] Lowering PDK is also a risk arm: documented harm directions (6 Hz proconvulsant at abstract level, only the combination of DCA and pyruvate helped in rat seizure, peripheral myelin proteins fell, neuropathy in the one randomised trial) and a lactate-supply role make the net direction by class unknown.",
     ("INV-19", "next_test"): "[SCI44] The lysates that serve INV-07 step 1 should be cell-class resolved (neurons, astrocytes, oligodendrocyte lineage) and keep lactate and pyruvate from the same wells.",
     ("INV-18", "next_test"): "[SCI44] Add a KATP arm to step 2b: perforated or cell-attached recording with ATP undisturbed, diazoxide and a sulfonylurea in KO and wild type, lactate or pyruvate add-back; state pipette ATP and glucose. Juvenile barrel-cortex neurons show KATP modulation of Vm, Rin and firing and lactate-driven KATP closure (34766906); this is a conditional metabolic upstream of the K branch (PH4), not a repair."}
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    for (inv, col), txt in T.items(): edit(f, "inv_id", inv, col, txt)
# row 12: open questions
M = "batch_sci_20261105/map/open_questions_map.tsv"; rows = rd(M); h = rows[0]
for r in rows[1:]:
    if r[0] == "IT43-Q02" and r[h.index("status")] == "OPEN":
        r[h.index("status")] = "CONCLUDED"; r[h.index("status_evidence")] = "pdh_pdk_sci44_20261110/README.md (answered at RNA level by cell class and species; protein not reached: see IT44-Q05)"; r[h.index("last_touched")] = "2026-11-11"
Q = [("IT44-Q03", "What are the pipette ATP and bath glucose of the Wwox recordings, and is lactate raised in the knockout slice? INFERENZA; premise for the lactate-closed KATP branch (PH4); reopen condition: Methods read or measured.", "Decides whether a metabolic upstream of the K branch can be tested.", "wet_lab_measurement", "no"),
     ("IT44-Q04", "Does the burst need lactate supply at matched suppression? IPOTESI (PH3); no rank; reopen condition: lactate measured in the slice.", "Decides whether the lactate-supply arm of PH3 exists.", "wet_lab_measurement", "no"),
     ("IT44-Q05", "What are the per-cell-type PDK protein amounts (reopen on the Sharma 2015 supplement when reachable)? INFERENZA; reading task.", "Turns an RNA share into a protein share for the kinase lever.", "literature_executable", "yes")]
for qid, txt, dec, kind, zs in Q:
    if not any(r[0] == qid for r in rows):
        d = dict(qid=qid, source_ref="pdh_pdk_sci44_20261110/consumer_delta.md row 12", question_text_max300=txt, decision_at_stake_max200=dec, kind=kind, status="OPEN", published_on="task/it44", status_evidence="pdh_pdk_sci44_20261110/README.md", last_touched="2026-11-11", blocking_reason="Not measured or not reached.", executable_zero_spend=zs, claimed_by="")
        rows.append([d.get(c, "") for c in h])
wr(M, rows)
# row 13: M01
edit("ampa_nmda_discrim_20261108/output/prediction_matrix.tsv", "arm_id", "M01", "readouts_specific", "[SCI44] Add pipette ATP and its concentration, bath glucose, lactate and pyruvate in the slice, and the recording mode (whole-cell versus perforated), for the K-branch and metabolic arms; one condition record then serves the pH and chloride questions, the capacitance and selection questions and the metabolic arms.")
print("applied")
