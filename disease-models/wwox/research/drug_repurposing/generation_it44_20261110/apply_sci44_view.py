"""IT44 P1/P6: SCI44 consumer_delta rows 6 and 7: V13 refined and three new compound-view entries (lactate-side probe, pyruvate-entry probe and fuel control, KATP probes). Idempotent."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
P = "generation_it41_20261109/compound_view.tsv"
rows = list(csv.reader(io.StringIO((R / P).read_text()), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
V13 = dict(label="Lowering the kinases that restrain the pyruvate dehydrogenase step: a carded lever with typed, per-isoform rows, conditional on an unmeasured premise; the first probe depends on the dominant kinase of the cell class and on the assay scaffold",
  open_premise="That the dehydrogenase step is actually restrained in a WWOX-deficient human neural cell, per cell class: no neural measurement of its amount, phosphorylation or activity exists, the dominant kinase differs by class and species, and the signs conflict (a lower kinase transcript in an organoid; a higher one with unchanged activity in a non-neural fibroblast line).",
  counter="The reference has a family record only; the two others rest on one assay each; one of them is an activator when the assay lacks the scaffold core and an inhibitor when it has it; two isoforms have no row for one compound (unknown, not zero). Lowering the kinases is also a risk arm: harm directions are documented (a proconvulsant effect at abstract level, benefit only for a combination in a rat seizure model, a fall of peripheral myelin proteins, nerve toxicity in the one randomised human trial) and a lactate-supply role makes the net direction by class unknown. Nothing is known about brain exposure.",
  next_test="Premise measurement per cell class on sorted or marker-resolved material, with a genetic knockdown of the dominant isoform first; compare the reference with the second chemotype only if a restraint is measured.",
  registry_note="Registry rows: ChEMBL mechanism (inhibitor, family record); GtoPdb inhibitor rows with pIC50 per isoform from two assays. AZD7545: the species recorded as human is not supported by its abstract (rat-indexed) and the 2003 primary was not reached; core-bound inhibition (PDK1, PDK3) versus core-free stimulation (PDK3, PDK4) in a later paper. VER-246608: Table 1 IC50 values reproduce the pIC50 rows (E1-only assay, species not named). The reference is a millimolar inhibitor and isoform-dependent.")
NEW = [
 dict(order="15", item_id="V15", inv_id="INV-07", kind="probe", name_full="oxamate (sodium oxamate); stiripentol (comparator)", origin="comparison_package", relation_id="A4-R2", where_done="in_silico_then_laboratory",
  label="A lactate-side probe: the sign depends on the cell compartment",
  action="Inhibition of lactate dehydrogenase to lower lactate production, as a probe of the supply side of the same metabolic node.",
  rationale="A lever on the other side of the node from the kinase: if lactate supply to neurons matters, lowering it could help or harm depending on the compartment.",
  open_premise="That lactate is raised in the knockout slice and that the burst needs lactate supply: neither is measured.",
  counter="The evidence is outside WWOX (adult mouse status epilepticus and slice activity); resting properties were never measured; the comparator has a mixed mechanism (GABA-A potentiation) and its enzyme value is copied from a review; no typed catalogue row exists for the enzyme, so the search by symbol reaches nothing.",
  next_test="Measure lactate and pyruvate in the slice with the premise series; only then a matched-suppression comparison against a non-metabolic route.",
  moves="Up: lactate raised in the knockout and a burst fall that tracks lactate supply. Down: lactate unchanged, or a fall explained by GABA-A potentiation or pH.",
  source_rows="pdh_pdk_sci44_20261110 tools_roles; engine", registry_note="No typed ChEMBL or GtoPdb row for LDHA/LDHB; two DGIdb listings (a class label and a code)."),
 dict(order="16", item_id="V16", inv_id="INV-07", kind="probe", name_full="UK-5099 (pyruvate entry); triheptanoin (fuel control)", origin="comparison_package", relation_id="A4-R3", where_done="in_silico_then_laboratory",
  label="A probe at the opposite end of the node and a fuel control, to separate a dehydrogenase defect from a supply defect",
  action="Block of mitochondrial pyruvate entry as a probe, and an alternative fuel that bypasses the dehydrogenase step as a control.",
  rationale="Activity alone cannot separate a restrained dehydrogenase step from a supply problem; a fuel that bypasses the step and a block of entry give the two opposite expectations.",
  open_premise="That any WWOX preparation shows a restraint or a supply defect; the direction label of the entry block is an inference.",
  counter="Neuronal culture and epileptic-mouse data only; protection by the entry block is not benefit; the fuel's effect was measured as enzyme activity, not flux.",
  next_test="Run both with the premise series: a fuel that restores function points to supply; an entry block that protects points away from release of the dehydrogenase step.",
  moves="Up: function restored by the fuel but not by kinase inhibition. Down: no change with the fuel in cells where the step is unrestrained.",
  source_rows="pdh_pdk_sci44_20261110 tools_roles; a4", registry_note="Pyruvate-entry blocker typed in GtoPdb only (a name-route gap in the identity join); the fuel is a catalogue record."),
 dict(order="17", item_id="V17", inv_id="INV-18", kind="probe", name_full="diazoxide; tolbutamide; glibenclamide (KATP tools)", origin="comparison_package", relation_id="A4-R4", where_done="in_silico_then_laboratory",
  label="ATP-sensitive K+ channel tools: a conditional metabolic upstream of the potassium branch",
  action="Open or occlude ATP-sensitive K+ channels to test whether a lactate-closed resting conductance contributes to input resistance.",
  rationale="In juvenile barrel cortex these channels change membrane potential, input resistance and firing, and lactate can close them: a metabolic upstream of the resting-conductance question, capped at about half of the implied loss.",
  open_premise="The pipette ATP and bath glucose of the recordings, and whether lactate is raised in the knockout slice; whole-cell dialysis can mask the effect.",
  counter="One verifier-read source; the pyramidal share of the pooled cells is inferred; no Wwox neuron has been tested.",
  next_test="Add a perforated or cell-attached arm with ATP undisturbed to the potassium ladder, with an opener, a sulfonylurea and lactate or pyruvate add-back, stating pipette ATP and glucose.",
  moves="Up: an opener-sensitive and sulfonylurea-occluded current smaller per pF in the mutant. Down: no difference with ATP undisturbed.",
  source_rows="pdh_pdk_sci44_20261110 tools_roles; a4/katp", registry_note="Reached by the unchanged relation path (ChEMBL mechanism and GtoPdb rows)."),
]
for r in rows[1:]:
    if r[ix["item_id"]] == "V13" and "scaffold core" not in r[ix["counter"]]:
        for k, v in V13.items(): r[ix[k]] = v
for v in NEW:
    if not any(r[ix["item_id"]] == v["item_id"] for r in rows): rows.append([v.get(c, "") for c in h])
o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / P).write_text(o.getvalue()); print("applied")
