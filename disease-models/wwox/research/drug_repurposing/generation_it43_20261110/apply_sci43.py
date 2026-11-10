"""IT43 P5: consume the SCI43 delivery (potassium_conductances_sci43_20261110/consumer_delta.md rows 1-7 and 11; row 8 no change proposed; row 9 is information for Harness; row 10 receipts recorded separately).
Texts are the delivery's own, applied unchanged except where the row says 'add'. Idempotent by the marker [SCI43] or the replaced sentence. Rows 4-5 add three tool rows (Ba2+, a K2P blocker group, linopirdine) to the comparators table with the fields the delivery gives and NOT_IN_FILES elsewhere."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent; log = []
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
def edit(p, keycol, keyval, col, fn, tag):
    rows = rd(p); h = rows[0]
    for r in rows[1:]:
        if r[h.index(keycol)] == keyval:
            new = fn(r[h.index(col)])
            if new != r[h.index(col)]: r[h.index(col)] = new; log.append(f"{tag}: {p} {keyval} {col}")
    wr(p, rows)
add = lambda txt: (lambda v: v if txt[:7] in v else (v + " " + txt).strip())
# rows 1-2: investigations (both tables)
T1 = "[SCI43] Order of arms: (0) capacitance measured directly by genotype and the cell-selection rule stated (pyramidal identity was confirmed from Rin and tau); (1) the same cells with and without synaptic blockers, in bursting and non-bursting slices; (2) Ba2+-sensitive current per pF and Rin share (a low micromolar concentration; a higher concentration and a K2P-blocker group as 2b); (3) XE-991-sensitive current at about −55 to −45 mV, not at rest, with a second Kv7 blocker; (4) current sensitive to an Ih blocker, repeated with a second Ih blocker; (5) dynamic-clamp leak of about 2.7 nS as sufficiency only, with a control leak at the WT rest; (6) an opener only after step 3. An implied reversal near E_K does not separate a K+ loss from a smaller cell with a shunt."
T2 = "[SCI43] Measured shares in wild-type neurons of other preparations: a Ba2+-sensitive resting conductance about 23 percent (adult mouse L2/3 auditory cortex, one preprint, verifier could not open it), a KCNQ2-dependent share about 20 percent when the cell rests near −67 mV (P15–P20), Ih about 6 percent (same preprint), Kv7 expected small at the Wwox rest (activation near −70 mV; XE-991 weak at hyperpolarised potentials). The Wwox pair implies a net loss of about 28 percent of the resting conductance (2.7 nS). A blocker effect shows contribution, not alteration."
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    edit(f, "inv_id", "INV-18", "next_test", add(T1), "row1"); edit(f, "inv_id", "INV-18", "decisive_uncertainty", add(T2), "row2")
# row 3: compound view V10
P = "generation_it41_20261109/compound_view.tsv"
edit(P, "item_id", "V10", "next_test", lambda v: v.replace("Nominate nothing before a difference current reversing near the potassium equilibrium potential and a matched-effect control that fails to reproduce the fall.", "Nominate nothing before a Ba2+- or XE-991-sensitive difference current smaller per pF in Wwox neurons with capacitance measured directly and the junction potential measured; a reversal near E_K alone does not separate a K+ loss from a smaller cell with a shunt; a matched-effect control that fails to reproduce the fall."), "row3")
edit(P, "item_id", "V10", "open_premise", lambda v: v if "starts near" in v else v + " Kv7 current starts near −70 mV, so an opener's expected action is in the spiking range, not at the Wwox rest.", "row3")
edit(P, "item_id", "V10", "moves", lambda v: v if "smaller cell with a shunt" in v else v + " Down: a smaller cell with a shunt gives the same implied reversal.", "row3")
# rows 4-5: comparators and probes
CTX = "Read in SCI43: XE-991 is state-dependent (no effect on recombinant Kv7.2 at −70 mV, half-inhibition near −51 mV; 28483800), so a difference current is read at a depolarised holding potential; retigabine rescued mAHP and spike count in an Ank2-cKO L2/3 model, with no Rin or rest change in the text and no neuronal Kv7 current measured (37321992, Fig 7 viewed). Potencies are copied by the sources, not primary."
OLD = "Reused from the IT13/IT14 packages; not re-read; the report mentioned in the brief was not available."
C = "comparators_it39_20261109/output/comparators.tsv"
edit(C, "comparator", "XE991 and a Kv7 opener (existing lead)", "context_of_the_measurement", lambda v: CTX if v == OLD else v, "row4")
rows = rd(C); h = rows[0]
if not any(r[h.index("comparator")] == "Ba2+ (difference-current probe)" for r in rows):
    src = "potassium_conductances_sci43_20261110/output/tools_roles.tsv; D05, D06, D09"
    new = [("Ba2+ (difference-current probe)", "mechanism_separating", "Ba2+-sensitive resting current; Kir2-type and K2P-type not separable; glial Kir4.1 not excluded", "Read in SCI43 (tools_roles.tsv)", "Selectivity NOT_ASSESSED", "Branch D: whether a Ba2+-sensitive resting conductance is smaller per pF in Wwox neurons", "A smaller Ba2+ current alone does not separate Kir2-type from K2P-type or neuron from glia"),
           ("K2P blocker group (A1899, fluoxetine in a pooled group)", "mechanism_separating", "K2P blockers raised the membrane resistance of adult S1 L2/3 pyramidal dendrites (40595546, text read; figures not viewed)", "Adult, dendritic, pooled group; none in P13-P17 somatic recordings", "Selectivity NOT_ASSESSED", "Whether a K2P-type leak contributes to Rin at rest", "A pooled blocker group does not identify the isoform"),
           ("linopirdine (second Kv7 chemotype)", "mechanism_separating", "Kv7 blocker used as a second chemotype beside XE-991", "Read in SCI43 (tools_roles.tsv)", "Selectivity NOT_ASSESSED", "Whether an XE-991-sensitive effect repeats with a second chemotype", "Agreement of two blockers does not show a lesion")]
    for n in new:
        rows.append([("INV-18" if k == "inv_id" else n[0] if k == "comparator" else n[1] if k == "role" else n[2] if k == "target_and_action" else n[3] if k == "context_of_the_measurement" else n[4] if k == "selectivity_limits" else "NOT_IN_FILES" if k == "exposure_or_development_note" else n[5] if k == "what_it_separates" else n[6] if k == "what_it_does_not_separate" else src) for k in h]); log.append("row4: comparator " + n[0])
    wr(C, rows)
edit("hcn_20261107/output/probes.tsv", "probe_id", "P05", "source_facts", lambda v: CTX if "Reused from the IT13/IT14 packages" in v else v, "row5")
edit("hcn_20261107/output/probes.tsv", "probe_id", "P05", "limits", lambda v: v if "voltage dependence" in v else v + " The XE-991 null effect at rest is expected from its voltage dependence and does not show a small Kv7 share.", "row5")
# row 6: open questions
M = "batch_sci_20261105/map/open_questions_map.tsv"; rows = rd(M); h = rows[0]
Q = [("IT43-Q03", "Is the Ba2+-sensitive (Kir2-type or K2P-type) current per pF smaller in Wwox-deficient layer II/III neurons, with capacitance measured directly and synaptic blockers on? IPOTESI; reopen condition: ladder steps 0 and 2 done.", "Decides whether a resting-K+ branch exists."),
     ("IT43-Q04", "What is the capacitance by genotype, and is the pyramidal-cell selection by Rin and tau biasing the contrast? IPOTESI.", "Decides whether any K arm is needed."),
     ("IT43-Q05", "Is an XE-991-sensitive current at -55 to -45 mV or the train-evoked mAHP different by genotype? IPOTESI.", "Decides whether a Kv7 spiking-range arm exists.")]
for qid, txt, dec in Q:
    if not any(r[0] == qid for r in rows):
        d = dict(qid=qid, source_ref="potassium_conductances_sci43_20261110/output/experiment_ladder.tsv", question_text_max300=txt, decision_at_stake_max200=dec, kind="wet_lab_measurement", status="OPEN", published_on="task/it43", status_evidence="potassium_conductances_sci43_20261110/README.md", last_touched="2026-11-10", blocking_reason="A new measurement in the burst preparation.", executable_zero_spend="no", claimed_by="")
        rows.append([d.get(c, "") for c in h]); log.append("row6: " + qid)
wr(M, rows)
# row 7: CP-MH1
CP = "generation_it40_20261109/conditional_proposals_it40.tsv"
edit(CP, "proposal_id", "CP-MH1", "compound_or_probe_named_by_package", add("[SCI43] K2P blockers (A1899, fluoxetine in a pooled group) raised the membrane resistance of adult S1 L2/3 pyramidal dendrites (40595546, text read; figures not viewed); none in P13–P17 somatic recordings; Kir2 tools not read."), "row7")
edit(CP, "proposal_id", "CP-MH1", "catalogue_by_action", add("[SCI43] azetukalner (CHEMBL5095264) is not reached by the symbol lookup (zero target rows); reached by name only."), "row7")
# row 11: M01
edit("ampa_nmda_discrim_20261108/output/prediction_matrix.tsv", "arm_id", "M01", "readouts_specific", add("[SCI43] Add capacitance measured directly (transient or membrane test), access resistance and bridge balance by genotype, the measured liquid junction potential of the actual solutions, and the cell-selection rule (pyramidal identity was confirmed from Rin and tau in the source paper)."), "row11")
print("\n".join(log) or "nothing to apply")
