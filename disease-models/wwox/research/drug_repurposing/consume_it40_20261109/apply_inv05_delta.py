"""IT40b: apply the INV-05 narrow-comparison proposals (nmda_composition_discrim_20261109/consumer_delta.md rows 1-8) to their consumers. Idempotent; every added text carries [IT40b]. Row 9 is a built surface and needs regeneration only."""
import csv, io, json
from pathlib import Path
R = Path(__file__).resolve().parent.parent
T = "[IT40b] "
log = []
def tsv_edit(path, keyfield, key, col, fn, header_first=True):
    p = R / path; rows = list(csv.reader(io.StringIO(p.read_text()), delimiter="\t")); h = rows[0]
    hits = [r for r in rows[1:] if r[h.index(keyfield)] == key]
    assert hits, (path, key)
    for r in hits:
        new = fn(r[h.index(col)], r)
        if new != r[h.index(col)]: log.append((path, key, col)); r[h.index(col)] = new
    out = io.StringIO(); csv.writer(out, delimiter="\t", lineterminator="\n").writerows(rows); p.write_text(out.getvalue())
def app(text, add): return text if add in text else text.rstrip() + " " + add
# row 1
NEW = "(one ifenprodil-site GluN2B NAM; a second NAM controls chemotype only, same site and same triheteromer ceiling; compare with d-APV only up to the NAM's measured removable share; measure the d-APV abolition threshold x and the NAM removable fraction first)"
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    tsv_edit(f, "inv_id" if "it20" in f else "inv_id", "INV-05", "next_test", lambda t, r: t.replace("(two unrelated NAMs)", NEW) if "(two unrelated NAMs)" in t else t)
# rows 2 and 3
C = "comparators_it39_20261109/output/comparators.tsv"
tsv_edit(C, "comparator", "ifenprodil", "selectivity_limits", lambda t, r: app(t, T + "Primary values (oocytes, -40 mV, 100 uM glutamate plus 50 uM glycine; 24607230, partial full text): GluN2B IC50 72 nM, maximum 88 percent; GluN2A unchanged at 3 uM; triheteromer IC50 450 nM, maximum 32 percent, 50 percent with 300 nM Zn2+."))
for c in ("ifenprodil", "Ro 25-6981"):
    tsv_edit(C, "comparator", c, "what_it_does_not_separate", lambda t, r: app(t, T + "It does not separate a GluN2A pool from an insensitive triheteromer pool."))
    tsv_edit(C, "comparator", c, "what_it_separates", lambda t, r: t.replace("Second unrelated GluN2B NAM beside Ro 25-6981 (tool before clinical compound).", "A second NAM of the same ifenprodil site controls chemotype only (same site, same triheteromer ceiling).").replace("One of two unrelated GluN2B NAMs (tool before clinical compound) proposed so that a burst effect is not read as one chemotype's off-target action.", "One of two NAMs of the same ifenprodil site; the pair controls chemotype only, not site or ceiling (tool before clinical compound)."))
tsv_edit(C, "comparator", "Ro 25-6981", "selectivity_limits", lambda t, r: app(t, T + "Maximum and conditions of the primary paper remain unread (abstract level)."))
tsv_edit(C, "comparator", "radiprodil", "selectivity_limits", lambda t, r: app(t, T + "Species matter: rat GluN1/GluN2B maximum 82 percent against rat triheteromer 45 percent (human GluN1/GluN2B 91 percent); the oocyte bath held 10 uM EDTA (40994429 Table 1)."))
# rows 4-6 (package tables of the earlier delivery)
P = "ampa_nmda_discrim_20261108/output/"
tsv_edit(P + "hypotheses.tsv", "hyp_id", "BH2", "discriminating_experiment", lambda t, r: app(t, T + "Use the like-for-like 82 against 45 percent (rat); the removable share of the NAM is bounded above by 0.88 times the GluN2B diheteromer share plus 0.32 times the triheteromer share (0.50 times the triheteromer share with Zn2+) (INFERENZA); read the percent removed at the burst."))
tsv_edit(P + "prediction_matrix.tsv", "arm_id", "M04", "readouts_specific", lambda t, r: app(t, T + "Measure the abolition threshold x."))
tsv_edit(P + "prediction_matrix.tsv", "arm_id", "M05", "same_prediction_note_arm_does_not_separate", lambda t, r: app(t, T + "A NAM plateau below x is unresolved, not support for total gain; a left shift is composition only after the percent removed is measured at the burst."))
tsv_edit(P + "prediction_matrix.tsv", "arm_id", "M06", "same_prediction_note_arm_does_not_separate", lambda t, r: app(t, T + "TCN-201 maxima in the source: 91 / 72 / 0 percent on GluN2A / triheteromer / GluN2B at 3 uM glycine; the three-share solution is fragile (near-collinear: determinant about 0.12, condition number about 32, INFERENZA; maxima are low-glycine values; tonic Zn2+ moves the NAM coefficient from 0.32 to 0.50)."))
tsv_edit(P + "experiments.tsv", "exp_id", "BE2", "comparison_arms", lambda t, r: app(t, T + "Add arms: NAM with and without a Zn2+ chelator; equilibration time and a vehicle arm; burst-level NMDA-receptor charge; glycine or D-serine for both the NAM and the TCN-201 arms; a d-APV series against raised glutamate (new_measurements M-N2, M-N8 to M-N12)."))
# row 7
nj = R / "needs/needs.json"; d = json.loads(nj.read_text()); n = next(x for x in d["needs"] if x["id"] == "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR")
for f, txt in (("counter_evidence", T + "Recombinant ceilings (transfer, not Wwox): an ifenprodil-site GluN2B NAM removes at most 88 percent of GluN1/GluN2B current and only 32 percent of GluN1/GluN2A/GluN2B triheteromer current (50 percent with 300 nM Zn2+) (24607230, oocytes); a burst fall to a NAM therefore cannot be read as total NMDA-receptor gain unless the percent removed at the burst is measured."),
               ("inferred", T + "The removable share of a GluN2B NAM is bounded by composition and Zn2+ (INFERENZA from recombinant values); a plateau below the d-APV effect does not by itself separate GluN2A-containing receptors from insensitive triheteromers. Open measurements are listed in nmda_composition_discrim_20261109/output/new_measurements.tsv.")):
    if txt not in n[f]: n[f].append(txt); log.append(("needs", n["id"], f))
nj.write_text(json.dumps(d, indent=1, ensure_ascii=False))
# row 8 (packet; no concentrations on cards)
p = R / "cards/F04_nmdar_intervention_class.packet.json"; k = json.loads(p.read_text())
add = "The removable share of a GluN2B-selective negative modulator is bounded by receptor composition and by zinc (recombinant values, transfer); no subunit-selective drug has been applied to a Wwox system."
if add not in k["not_known"]: k["not_known"].append(add); p.write_text(json.dumps(k, indent=1, ensure_ascii=False) + "\n"); log.append(("F04", "not_known", 0))
for l in log: print(*l)
