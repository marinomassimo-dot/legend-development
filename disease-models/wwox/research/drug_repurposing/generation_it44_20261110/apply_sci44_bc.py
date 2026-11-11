"""IT44b: SCI44 packages B (Ro 25-6981) and C (K+ shares) consumed. B rows 1, 3, 4, 5; C rows 1, 2, 3, 5; the package A correction (the Wwox internal solution holds 2 mM Na2ATP). Idempotent; markers [SCI44-B], [SCI44-C]. Receipts (B row 6, C row 6) are recorded separately."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
def edit(p, keycol, keyval, col, txt, marker):
    rows = rd(p); h = rows[0]
    for r in rows[1:]:
        if r[h.index(keycol)] == keyval and marker not in r[h.index(col)]: r[h.index(col)] = (r[h.index(col)] + " " + txt).strip()
    wr(p, rows)
# manifest: package B registered for INV-05
M = R / "hypothesis_packages.tsv"; t = M.read_text()
if "ro25_6981_sci44_20261110" not in t:
    M.write_text(t.rstrip("\n") + "\nro25_6981_sci44_20261110\tro25_6981_sci44_20261110\tpharmacological_comparison\tINV-05\tINV-05 second ifenprodil-site tool: Ro 25-6981 comparison row C-RO1 with new_measurements M-R1, M-R2 and decisive D01-D14 (SCI44 package B)\n")
# C row 1 and the package A correction: INV-18 next_test
T = "[SCI44-C] The KATP arm of step 2b carries a size expectation: in juvenile barrel cortex the KATP share of resting conductance is about 11-17 percent (INFERENZA, upper bound, ATP-free whole-cell, glutamatergic regular-spiking cells, species and temperature unstated), so a KATP deficit alone would not account for 28 percent; state pipette ATP, record per-cell temperature and cell identity. The Wwox whole-cell internal solution contains 2 mM Na2ATP, so a lactate-closed KATP conductance is weakened for the published values and kept for ATP-undisturbed recordings."
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"): edit(f, "inv_id", "INV-18", "next_test", T, "[SCI44-C]")
# C row 2: M01 ; B row 5: the NAM arm
P = "ampa_nmda_discrim_20261108/output/prediction_matrix.tsv"
edit(P, "arm_id", "M01", "readouts_specific", "[SCI44-C] Add per-cell temperature, species and strain, cell identity (morphology) and the pipette ATP concentration (2 mM in the Wwox internal solution) to the measured conditions.", "[SCI44-C]")
edit(P, "arm_id", "M05", "readouts_specific", "[SCI44-B] A second ifenprodil-site tool (Ro 25-6981) is read only after the first tool has shown a removable share, in the same preparation at a saturating concentration, with a zinc-chelator arm (M-R1) to read the triheteromer ceiling.", "[SCI44-B]")
# open questions: B row 4, C row 3
Mp = "batch_sci_20261105/map/open_questions_map.tsv"; rows = rd(Mp); h = rows[0]
for r in rows[1:]:
    if r[0] == "IT43-Q01" and r[h.index("status")] == "OPEN":
        r[h.index("status")] = "IN_PROGRESS"; r[h.index("status_evidence")] = "ro25_6981_sci44_20261110/README.md (diheteromer potency and site read in primary sources; maximum inhibition and triheteromer not reached; reopen: Hedegaard Fig 3, Science 2017 Fig 4A and supplement, Hansen 2014 supplement, Fischer 1997 full text)"; r[h.index("last_touched")] = "2026-11-11"
if not any(r[0] == "IT44-Q06" for r in rows):
    d = dict(qid="IT44-Q06", source_ref="potassium_shares_sci44_20261110/consumer_delta.md row 3", question_text_max300="Is the diazoxide-sensitive, sulfonylurea-occluded current per pF smaller in the Wwox knockout layer II/III neuron with ATP undisturbed? IPOTESI (PH4); no rank; reopen conditions: the preprint when reachable, a pyramidal-typed KATP dataset.", decision_at_stake_max200="Decides whether a metabolic upstream of the potassium branch exists beyond the dialysed whole-cell values.", kind="wet_lab_measurement", status="OPEN", published_on="task/it44", status_evidence="potassium_shares_sci44_20261110/README.md", last_touched="2026-11-11", blocking_reason="A new measurement in the burst preparation.", executable_zero_spend="no", claimed_by="")
    rows.append([d.get(c, "") for c in h])
wr(Mp, rows)
# compound view: V08 back to the three assembly-record compounds, V18 new (Ro 25-6981), V17 updated
CV = "generation_it41_20261109/compound_view.tsv"; rows = rd(CV); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
for r in rows[1:]:
    if r[ix["item_id"]] == "V08" and "second ifenprodil-site tool" in r[ix["counter"]]:
        r[ix["name_full"]] = "traxoprodil; rislenemdaz; EVT-101"
        r[ix["counter"]] = "No maximum effect, species or assay context in the catalogue; no approval statement in the catalogue."
        r[ix["next_test"]] = "Read primary sources for maximum effect and site only if a further chemotype is needed."
        r[ix["source_rows"]] = "search_rows S1 (ChEMBL)"
    if r[ix["item_id"]] == "V17" and "2 mM Na2ATP" not in r[ix["open_premise"]]:
        r[ix["open_premise"]] = "The published whole-cell recordings used 2 mM Na2ATP in the pipette, which would mask a lactate-closed conductance; bath glucose and whether lactate is raised in the knockout slice are not measured."
        r[ix["counter"]] = "One laboratory's pooled cells; the pyramidal share is inferred and the KATP share of resting conductance is about 11-17 percent (upper bound), so alone it would not account for the 28 percent loss; the two sulfonylureas also act on other currents and a bath drug may act through network or astrocytic routes; no Wwox neuron has been tested."
if not any(r[ix["item_id"]] == "V18" for r in rows):
    v = dict(order="18", item_id="V18", inv_id="INV-05", kind="probe", name_full="Ro 25-6981", origin="comparison_package", relation_id="S1", where_done="both",
      label="A second ifenprodil-site tool: primary potency and site are read, no maximum inhibition and no triheteromer figure",
      action="Negative allosteric modulation of GluN2B-containing receptors at the interface site, as a second tool of the same site.",
      rationale="A second tool of the same site controls chemotype only; with primary potency and site now read it can be used after the first tool has shown a removable share.",
      open_premise="The percent of the isolated current removed in the Wwox slice (not measured) and the maximum on triheteromers (not reached in any text read).",
      counter="No maximum inhibition in any text read; a native value reported by eye is not transferable; two of the sources share one recording solution and are not independent; the salt differs between papers.",
      next_test="Use only after the first tool has shown a removable share, in the same preparation at a saturating concentration, with a zinc-chelator arm to read the triheteromer ceiling.",
      moves="Up: a removable share already seen with the first tool and a second tool of the same site agreeing. Down: a ceiling like the first tool's, which adds a chemotype and nothing else.",
      source_rows="ro25_6981_sci44_20261110; engine_check", registry_note="Salt differs between papers (maleate, hydrochloride, unstated); primary IC50 about 42-59 nM on GluN1/GluN2B in oocytes, -40 mV, 30 uM glycine, EDTA.")
    rows.append([v.get(c, "") for c in h])
wr(CV, rows); print("applied")
