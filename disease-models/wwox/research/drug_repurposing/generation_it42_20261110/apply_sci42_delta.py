"""IT42 P3: apply the SCI42 package (glun2b_comparators_sci42_20261110/consumer_delta.md rows 1-8; row 9 format decision: no hypothesis_packages row; row 10 is information for Harness; row 11 receipts recorded separately). Idempotent; marker [SCI42]."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent; T = "[SCI42] "; log = []
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
# rows 1-2: compound view
P = "generation_it41_20261109/compound_view.tsv"; rows = rd(P); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
U = {
 "V06": dict(kind="unresolved", label="Human-exposure GluN2B negative modulator; site, maximum effect and triheteromer behaviour not measured in any source reached",
   rationale="A second scaffold (sharing the hydroxyaryl-ethanolamine arrangement of ifenprodil-type ligands: inference from structure) read after the ifenprodil-site tool, to ask whether a different scaffold removes the same measured percent of the isolated NMDA-receptor current.",
   counter="Two sponsor-authored clinical papers read at partial full text; the only potency is one patent calcium-flux IC50 (8.3 nM) on NR1/NR2B cells without Mg2+, with no stated Zn2+ chelator or pH.",
   next_test="None found by open routes (a patent and two clinical papers read; an analogue paper not reached); the measurement is the removable fraction in the isolated NMDA-receptor current, after the ifenprodil-site tool.",
   moves="Up: a primary source placing it at the ifenprodil site with a clearly different triheteromer maximum, or at a different documented site that gives a different comparison. Down: none reached; it stays a conditional second scaffold after the tool.",
   where_done="laboratory",
   registry_note_add="One applicant measurement copied into BindingDB, ChEMBL and GtoPdb (the GtoPdb link is by value identity); the patent assay has no maximum effect."),
 "V07": dict(kind="probe", label="pH-dependent GluN2B modulator: a pH-linked comparison, subordinate to a measured tissue pH; not a candidate",
   rationale="Potency is pH-dependent (declared about 6-fold; IC50 21 and 130 nM at pH 6.9 and 7.6, abstract level, same developer); for the series prototype the maximum moved little (76 to 83 percent, measured in oocytes).",
   open_premise="The pH of the recorded tissue is unmeasured; ifenprodil may itself be pH-sensitive (older abstracts) and a related clinical-stage modulator is declared not to be (a 2015 table not read).",
   counter="Phase 1 in healthy adults (partial full text); maximum effect, site, triheteromer and slice data absent; H1 and hERG actions declared.",
   next_test="Measure the tissue pH; if this compound is used, run the ifenprodil-site tool and the full competitive antagonist at the same two controlled pH values, with its recombinant maximum at each pH known first.",
   moves="Up: a measured tissue pH in the range where the dependence is large, with a drug-by-pH interaction larger than for the ifenprodil-site tool and the full antagonist at the same two pH values. Down: a tissue pH near physiological, or an interaction not larger than theirs. A burst effect that follows the pH is not a specificity signature.",
   where_done="both",
   registry_note_add="GtoPdb's approved flag conflicts with ChEMBL and the abstract (maximum phase 1); the value 7.64 is probably the same measurement as 21 nM (inference)."),
}
for r in rows[1:]:
    u = U.get(r[ix["item_id"]])
    if not u or r[ix["kind"]] == u["kind"]: continue
    add = u.pop("registry_note_add")
    for k, v in u.items(): r[ix[k]] = v
    if add not in r[ix["registry_note"]]: r[ix["registry_note"]] = (r[ix["registry_note"]].rstrip() + " " + add).strip()
    log.append(("compound_view", r[ix["item_id"]]))
wr(P, rows)
# row 3: comparisons note
q = R / "generation_it41_20261109/comparisons_it41.md"; s = q.read_text()
a = "| Alternative that emerged | A second GluN2B negative modulator with human exposure (onfasprodil), site not recorded |"
b = "| Alternative that emerged | A second GluN2B negative modulator with human exposure (onfasprodil); no source reached states its site or its maximum effect; read only as a second scaffold after the ifenprodil-site tool (SCI42) |"
if a in s: s = s.replace(a, b); log.append(("comparisons", "alternative row"))
add = "\n\n> **Update 2026-11-10 (IT42, SCI42):** the last row of the table above (\"No source places it\") is the actual state for onfasprodil. NP10679 enters only after the tissue pH is measured and its recombinant maximum at each pH is known (a pH-dependent comparison, not a candidate). Item 1 of the minimum experiment gains \"measured bath and tissue pH\".\n"
if "Update 2026-11-10 (IT42, SCI42)" not in s: s = s.rstrip() + add; log.append(("comparisons", "update"))
q.write_text(s)
# row 4: INV-05 next_test
NT = T + "Report bath pH (and bicarbonate or HEPES) as a measured value with magnesium and potassium; read the percent of evoked synaptic charge removed for every drug so the matched drive-reduction control can be matched; a pH-dependent GluN2B tool is considered only after the tissue pH is measured, with the ifenprodil-site tool and d-APV at the same two pH values."
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    rows = rd(f); h = rows[0]
    for r in rows[1:]:
        if r[h.index("inv_id")] == "INV-05" and NT not in r[h.index("next_test")]:
            r[h.index("next_test")] = r[h.index("next_test")].rstrip() + " " + NT; log.append((f, "INV-05"))
    wr(f, rows)
# rows 5-7: package tables
def edit(path, kc, key, col, add):
    rows = rd(path); h = rows[0]
    for r in rows[1:]:
        if r[h.index(kc)] == key and add not in r[h.index(col)]:
            r[h.index(col)] = r[h.index(col)].rstrip() + " " + add; log.append((path, key))
    wr(path, rows)
PK = "ampa_nmda_discrim_20261108/output/"
edit(PK + "prediction_matrix.tsv", "arm_id", "M01", "readouts_specific", T + "Add bath pH and how it is set (bicarbonate/CO2 or HEPES), measured at the recording site.")
edit(PK + "prediction_matrix.tsv", "arm_id", "M14", "arm_and_status", T + "Add pH as a graded state variable only after M01 gives the tissue pH (the NMDA-receptor current itself falls with protons in oocytes; transfer to the slice not shown).")
edit(PK + "prediction_matrix.tsv", "arm_id", "M05", "same_prediction_note_arm_does_not_separate", T + "A pH-dependent GluN2B NAM and a second scaffold are read only after the ifenprodil-site NAM has shown a removable share; neither has a measured site, maximum or triheteromer result; a drug-by-pH interaction larger than for ifenprodil and d-APV is compatible with a pH-sensitive GluN2B NAM and does not separate the explanations.")
edit(PK + "experiments.tsv", "exp_id", "BE2", "comparison_arms", T + "Add: a washout or reversibility test per drug; isolated-current and burst recordings from the same animals; the evoked-charge axis for every drug; bath-pH measurement; a conditional pH contrast of the pH-dependent modulator against the ifenprodil-site tool and d-APV; a conditional second-scaffold arm.")
# row 8: map
mp = "batch_sci_20261105/map/open_questions_map.tsv"; rows = rd(mp); h = rows[0]
if not any(r[0] == "IT42-Q01" for r in rows[1:]):
    v = dict(qid="IT42-Q01", source_ref="disease-models/wwox/research/drug_repurposing/glun2b_comparators_sci42_20261110/output/new_measurements.tsv#M01", question_text_max300="What is the tissue pH of the Wwox-deleted neocortical slice under the recording conditions, and does it differ from physiological? IPOTESI; no pathological pH is assumed.", decision_at_stake_max200="Decides whether a pH-dependent GluN2B tool is relevant at all; reopen condition: M01 measured.", kind="wet_lab_measurement", status="OPEN", published_on="task/it42", status_evidence="glun2b_comparators_sci42_20261110/README.md", last_touched="2026-11-10", blocking_reason="A new measurement in the burst preparation; not answerable from other preparations.", executable_zero_spend="no", claimed_by="")
    n = [""] * len(h)
    for k, x in v.items(): n[h.index(k)] = x
    rows.append(n); wr(mp, rows); log.append(("map", "IT42-Q01"))
for l in log: print(*l)
