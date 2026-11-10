"""IT42 P3/P5: apply SCI42 S5 (dqp1105_row_sci42_20261110, rows 1-3, row 4 information for Harness, row 5 receipts recorded separately) and S6 (chloride_gradient_sci42_20261110, rows 1-6; row 7 no edit; row 8 receipts). Idempotent; marker [SCI42]. No new kind: 'excluded for comparison' is expressed in the label of a 'weakened' entry."""
import csv, io, json
from pathlib import Path
R = Path(__file__).resolve().parent.parent; T = "[SCI42] "; log = []
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
# S5 row 1: V09 and S6: V11 next_test
P = "generation_it41_20261109/compound_view.tsv"; rows = rd(P); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
for r in rows[1:]:
    if r[ix["item_id"]] == "V09" and not r[ix["label"]].startswith("Registry GluN2B row"):
        r[ix["label"]] = "The registry GluN2B row is a GluN2B measurement (113 micromolar) stored as nanomolar; DQP-1105 prefers GluN2C and GluN2D: excluded from the GluN2B comparison"
        r[ix["open_premise"]] = "Resolved at source: the paper's table gives GluN2B 113, GluN2C 7.0 and GluN2D 2.7 micromolar; the registry rows for GluN2B and GluN2C hold micromolar numbers entered as nanomolar (inference for the cause, data for the identity of the numbers)."
        r[ix["counter"]] = "No maximum per subunit is reported; the GluN2B value is a fitted IC50 with complete inhibition assumed. A registry value under a target can fail by unit, not only by subunit."
        r[ix["next_test"]] = "None; kept so the filing is not mistaken for evidence: the registry row is not evidence of GluN2B potency in nanomolar."
        r[ix["registry_note"]] = "Registry (GtoPdb 2026.3.1) rows under GluN2B (pIC50 6.95) and GluN2C (8.15) are pIC50 values computed from micromolar numbers entered as nanomolar (a thousand-fold; about 3.95 and 5.15 expected); the GluN2D row is correct. The assay text of the GluN2B row names GluN2C."
        log.append(("compound_view", "V09"))
    if r[ix["item_id"]] == "V11" and "gramicidin" not in r[ix["next_test"]]:
        r[ix["next_test"]] = "Re-record the sIPSC under glutamate block with a fixed threshold and per-animal summary first, then E_GABA by gramicidin perforated patch in littermates, then the age series; the lever, against a GABA-A potentiator and a non-GABAergic suppression matched to the same measured effect, only after these."
        log.append(("compound_view", "V11"))
wr(P, rows)
# S5 row 2: comparison_S1 pointer
q = R / "generation_it41_20261109/comparison_S1.md"; s = q.read_text(); u = "\n\n> **Update 2026-11-10 (IT42, SCI42 S5):** the DQP-1105 row was resolved at source: the registry GluN2B and GluN2C rows are micromolar numbers stored as nanomolar (a unit slip, not a subunit transfer); the compound is excluded from the GluN2B comparison. See entry V09 of the public list.\n"
if "SCI42 S5" not in s: q.write_text(s.rstrip() + u); log.append(("comparison_S1", "update"))
# S5 row 3: measure_it41 note
m = rd("generation_it41_20261109/measure_it41.tsv"); mh = m[0]
for r in m[1:]:
    if r[0].startswith("rows whose assay text names another subunit") and "unit slip" not in r[0]:
        r[0] += " (SCI42 S5: the counted case is a registry unit slip, not a subunit transfer)"; log.append(("measure_it41", "note"))
wr("generation_it41_20261109/measure_it41.tsv", m)
# S6 rows 1-2: needs
nj = R / "needs/needs.json"; d = json.loads(nj.read_text()); ns = {n["id"]: n for n in d["needs"]}
o = next(x for x in ns["NEED-GABA-CHLORIDE-GRADIENT"]["observed"] if x["id"] == "O1")
a1 = T + "The only inhibitory recording in the WWOX neocortical slice (34634460) used a 140 mM KCl pipette at -70 mV, so its amplitude cannot report the native chloride gradient; a raised native postsynaptic chloride cannot lower it through the driving force; a presynaptic chloride effect is not excluded."
if a1 not in o["limits"]: o["limits"] = o["limits"].rstrip() + " " + a1; log.append(("needs", "GABA-CHLORIDE O1"))
o = next(x for x in ns["NEED-INHIBITORY-HYPOFUNCTION"]["observed"] if x["id"] == "O1")
a2 = T + "Consequences of the 140 mM KCl internal solution with no antagonist named: unblocked excitatory events at -70 mV, a 4 x SD threshold that makes counted frequency amplitude-dependent, an undeclared frequency metric; the higher knockout input resistance argues against a pure artefact."
if a2 not in o["limits"]: o["limits"] = o["limits"].rstrip() + " " + a2; log.append(("needs", "INHIBITORY O1"))
nj.write_text(json.dumps(d, indent=1, ensure_ascii=False))
# S6 row 3: AB06 split (alternatives table: text pointer)
rows = rd("ampa_nmda_discrim_20261108/output/alternatives.tsv"); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
for r in rows[1:]:
    if r[0] == "AB06" and T not in r[ix["explanation"]]:
        r[ix["explanation"]] += " " + T + "Read as six separate explanations: supply, response, chloride gradient (untested by the datum), a change secondary to bursting, a maturational offset, an artefact (chloride_gradient_sci42_20261110/output/explanations.tsv)."; log.append(("alternatives", "AB06"))
wr("ampa_nmda_discrim_20261108/output/alternatives.tsv", rows)
# S6 row 4: M16
rows = rd("ampa_nmda_discrim_20261108/output/prediction_matrix.tsv"); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
for r in rows[1:]:
    if r[0] == "M16" and T not in r[ix["same_prediction_note_arm_does_not_separate"]]:
        r[ix["same_prediction_note_arm_does_not_separate"]] += " " + T + "A burst reduction by a GABA-A positive modulator is compatible with every explanation; only E_GABA (gramicidin), an evoked IPSC with agonist response, the tonic current and the age series separate them; synaptic-selective and extrasynaptic modulator classes are not interchangeable; the sign of a chloride-gradient manipulation is tied to E_GABA measured in the same cells."; log.append(("matrix", "M16"))
wr("ampa_nmda_discrim_20261108/output/prediction_matrix.tsv", rows)
# S6 row 5: INV-15 next_test
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    rows = rd(f); h = rows[0]
    for r in rows[1:]:
        if r[h.index("inv_id")] == "INV-15" and T not in r[h.index("next_test")]:
            r[h.index("next_test")] += " " + T + "Order of the inhibitory minimum experiment: M03 (re-record sIPSC with glutamate block, fixed threshold, per-animal summary), then M01 (E_GABA by gramicidin perforated patch, knockout, heterozygote and wild-type littermates), then M02 (age series with a survivor-selection control); M05 and M06 if M03 confirms the amplitude loss."; log.append((f, "INV-15"))
    wr(f, rows)
# S6 row 6: map rows
mp = "batch_sci_20261105/map/open_questions_map.tsv"; rows = rd(mp); h = rows[0]
add = [("IT42-Q02", "What is E_GABA in layer II/III pyramidal cells of the Wwox-deleted slice at P13-P17 against littermates? IPOTESI; no rank; reopen condition: M01 measured.", "Decides whether more GABA or a GABA-A potentiator can be expected to inhibit, and the sign of any chloride-gradient lever."),
       ("IT42-Q03", "Is the halved sIPSC amplitude reproduced under glutamate block, a fixed threshold and a per-animal summary? IPOTESI; no rank; reopen condition: M03 done.", "Decides whether the amplitude loss stands beyond the recording conditions (140 mM KCl pipette at -70 mV).")]
for q_, t_, dsn in add:
    if any(r[0] == q_ for r in rows[1:]): continue
    v = dict(qid=q_, source_ref="disease-models/wwox/research/drug_repurposing/chloride_gradient_sci42_20261110/output/new_measurements.tsv", question_text_max300=t_[:300], decision_at_stake_max200=dsn[:200], kind="wet_lab_measurement", status="OPEN", published_on="task/it42", status_evidence="chloride_gradient_sci42_20261110/README.md", last_touched="2026-11-10", blocking_reason="A new measurement in the burst preparation.", executable_zero_spend="no", claimed_by="")
    n = [""] * len(h)
    for k, x in v.items(): n[h.index(k)] = x
    rows.append(n); log.append(("map", q_))
wr(mp, rows)
for l in log: print(*l)
