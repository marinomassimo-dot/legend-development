"""IT41 P6/P5: apply the AMPA-comparison proposals (ampa_comparison_it41_20261109/consumer_delta.md rows 1-10) to their consumers. Idempotent; marker [IT41a]."""
import csv, io, json
from pathlib import Path
R = Path(__file__).resolve().parent.parent
T = "[IT41a] "; log = []
def tsv_rows(path): return list(csv.reader(io.StringIO((R / path).read_text()), delimiter="\t"))
def tsv_write(path, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / path).write_text(o.getvalue())
def edit(path, keycol, key, col, add=None, replace=None):
    rows = tsv_rows(path); h = rows[0]; hit = [r for r in rows[1:] if r[h.index(keycol)] == key]
    assert hit, (path, key)
    for r in hit:
        v = r[h.index(col)]
        if replace and replace[0] in v: r[h.index(col)] = v.replace(*replace); log.append((path, key, col, "replace"))
        elif add and add not in v: r[h.index(col)] = v.rstrip() + " " + add; log.append((path, key, col, "add"))
    tsv_write(path, rows)
P = "ampa_nmda_discrim_20261108/output/"
# 1-3 probes
edit(P + "probes.tsv", "probe", "NBQX", "mechanism_source", add=T + "Binding Ki 0.077 uM at GluA2 and 2.6, 5.4, 3.4 uM at GluK1-3, 152 uM at GluK5 (radioligand, sf9 membranes, 4 C; a binding window of 34- to 70-fold, not a current); surmountability and glycine-site action stay abstract-level; no functional IC50 read (35955932 Table 1 and Methods, partial full text).")
edit(P + "probes.tsv", "probe", "NBQX", "depth", replace=("use_only", "partial (binding table read)"))
edit(P + "probes.tsv", "probe", "Perampanel", "mechanism_source", add=T + "Same collar pocket as GYKI 53655 and CP-465,022 in structures (27618672, 36857176); GluK2 IC50 58 uM against 0.89 uM on GluA2 (same laboratory, different protocols: not like-for-like); kainate-evoked current at the AMPA IC50 in neurons (25229608, re-read by the verifier); GluK5-containing receptors at abstract level; ictal events abolished at 10 uM in human dysplasia slices (34653311, not block-verified); the AMPA IC50 shifted 0.4 to 0.9 uM over 10-100 uM AMPA.")
edit(P + "probes.tsv", "probe", "GYKI 52466", "depth", replace=("carried_from_citing_paper (no first-hand read)", "abstract_only (kinetics originate in Donevan 1993, not read in full)"))
rows = tsv_rows(P + "probes.tsv"); h = rows[0]
if not any(r[0] == "GYKI 53655" for r in rows[1:]):
    n = [""] * len(h); n[0] = "GYKI 53655"; n[1] = "2,3-Benzodiazepine noncompetitive AMPA/kainate antagonist (distinct structure from GYKI 52466; name mismatch for the identity delivery)"
    n[2] = "27618672, 27838344, 35103859 (partial full text); 7678966, 9076748 (abstracts)"; n[3] = "Recombinant GluA (IC50 14.5 uM, cyclothiazide possibly present); mouse slices: IC50 2.5 uM on the evoked EPSC, 80.5 percent block (entorhinal) and 89 percent (barrel cortex layer V) at 10 uM, reversible in cingulate slices at 33-34 C; Down-state potential unchanged (-62.7 against -63.5 mV, entorhinal)"
    n[4] = "Kainate window at abstract level only (under 30 percent inhibition of GluR5/GluR6 at 100 uM for 2,3-benzodiazepines); NMDA-receptor neutrality not measured in the Wwox preparation"
    n[5] = "No verified block with a burst readout in any slice paper read; the achieved block at 10 uM (80-89 percent) is a variable, at the edge of the 90 percent design value"; n[6] = "partial_fulltext_read"
    rows.append(n); tsv_write(P + "probes.tsv", rows); log.append((P + "probes.tsv", "GYKI 53655", "new row", ""))
# 4-6 package tables
edit(P + "hypotheses.tsv", "hyp_id", "BH1", "discriminating_experiment", add=T + "Verified-block tool = a noncompetitive 2,3-benzodiazepine (GYKI 53655 where tissue data exist); independent partner = NBQX (competitive); perampanel = same-site cross-check with an occlusion test (agreement across tools at one site is not independent confirmation); name the arm AMPA/kainate unless the window is measured; the evoked Up-state result of barrel cortex (persisting under 10 uM GYKI 53655, abolished by d-AP5 afterwards) is transfer, not evidence about the Wwox burst; keep the kill condition (survival under a verified block).")
edit(P + "prediction_matrix.tsv", "arm_id", "M07", "same_prediction_note_arm_does_not_separate", add=T + "State the achieved block as a variable (80-89 percent at 10 uM in tissue for the 2,3-benzodiazepine); the tool statement of the arm is as in BH1.")
edit(P + "prediction_matrix.tsv", "arm_id", "M08", "same_prediction_note_arm_does_not_separate", add=T + "NBQX with d-APV compares two surmountable tools (shared weakness); a noncompetitive tool with d-APV compares unlike tools; perampanel's AMPA IC50 shifted about two-fold over 10-100 uM AMPA in culture, so non-surmountability is graded.")
edit(P + "experiments.tsv", "exp_id", "BE1", "comparison_arms", add=T + "Add measurements M-A1 to M-A7 of ampa_comparison_it41_20261109/output/new_measurements.tsv (block time course, NMDA-receptor EPSC at the working concentration, intrinsic properties, block at low and high stimulation, kainate component, occlusion test, washout order).")
# 7 comparators
C = "comparators_it39_20261109/output/comparators.tsv"; rows = tsv_rows(C); h = rows[0]
src = {r["row_id"]: r for r in csv.DictReader(open(R / "ampa_comparison_it41_20261109/output/comparison.tsv", encoding="utf-8"), delimiter="\t")}
spec = [("C1", "NBQX", "mechanism_separating"), ("C2", "GYKI 53655", "functional_outcome"), ("C3", "perampanel", "mechanism_separating")]
for rid, name, role in spec:
    if any(r[0] == "INV-05" and r[1] == name for r in rows[1:]): continue
    s = src[rid]; n = [""] * len(h)
    v = dict(inv_id="INV-05", comparator=name, role=role, target_and_action=s["compound_or_probe"] + " | identity: " + s["identity_status"], context_of_the_measurement=s["source_locator_depth"], selectivity_limits=s["documented_action_and_limits"],
             exposure_or_development_note=s["measurement_that_makes_it_interpretable"], what_it_separates=s["outcome_favourable"], what_it_does_not_separate=s["explanations_not_separated"], source_file_and_row="ampa_comparison_it41_20261109/output/comparison.tsv:" + rid)
    for k, x in v.items(): n[h.index(k)] = x
    rows.append(n); log.append((C, name, "new row", ""))
tsv_write(C, rows)
# 8 needs
nj = R / "needs/needs.json"; d = json.loads(nj.read_text()); n = next(x for x in d["needs"] if x["id"] == "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR")
add = (T + "Transfer, not Wwox: in mouse slices a noncompetitive 2,3-benzodiazepine at 10 uM removed 80.5 percent (entorhinal) and 89 percent (barrel cortex layer V) of the evoked peak; evoked Up states of barrel cortex layer V persisted under it and were abolished by d-AP5 afterwards (27838344; the pulse supplied depolarisation and the block was verified in other cells); no slow non-NMDA component in barrel cortex layers III and V (35103859). Perampanel and the benzodiazepine share one pocket, so agreement between them is not independent confirmation. This does not settle AMPA-receptor dependence of the spontaneous bursts; the open measurements are in ampa_comparison_it41_20261109/output/new_measurements.tsv.")
if add not in n["counter_evidence"]: n["counter_evidence"].append(add); log.append(("needs", n["id"], "counter_evidence", ""))
nj.write_text(json.dumps(d, indent=1, ensure_ascii=False))
# 9 card packet
p = R / "cards/F04_nmdar_intervention_class.packet.json"; k = json.loads(p.read_text())
a9 = "The two noncompetitive AMPA tools (perampanel and the 2,3-benzodiazepine) share one binding pocket in structures, so agreement between them is not independent confirmation; no AMPA drug has been applied to a Wwox system."
if a9 not in k["not_known"]: k["not_known"].append(a9); p.write_text(json.dumps(k, indent=1, ensure_ascii=False) + "\n"); log.append(("F04", "not_known", "", ""))
# 10 next investigations
q = R / "generation_it40_20261109/next_investigations_it40.md"; s = q.read_text()
note = "\n\n> **Update 2026-11-10 (IT41):** A1 is partly answered by `ampa_comparison_it41_20261109/` (NBQX binding window, structures and kinetics of the noncompetitive tools read; primary mechanism papers for NBQX and GYKI 52466 stay abstract-level or unreached); A2 is answered in kind by Harness's `identity_it41_20261109/` (GYKI 52466 and GYKI 53655 are different structures; Ro 25-6981 and ifenprodil have measured-activity rows; Brilliant Blue FCF is in ChEMBL without a name); B3 (BE1) is served by `comparison.tsv`.\n"
if "Update 2026-11-10 (IT41)" not in s: q.write_text(s.rstrip() + note); log.append(("next_investigations_it40.md", "", "update", ""))
for l in log: print(*l)
