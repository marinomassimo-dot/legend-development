"""IT41 light queue: apply the Wwox-loss Drosophila feasibility proposals (fly_wwox_feasibility_it41_20261110/consumer_delta.md rows 1-3) and a dated correction line where an IT30 note carried the superseded 2005 rescue. Idempotent; marker [IT41c]. Row 4 (needs): no entry mentions model organisms as a model; nothing added."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent; T = "[IT41c] "; log = []
def edit(path, key_col, key_prefix, col, add):
    p = R / path; rows = list(csv.reader(io.StringIO(p.read_text()), delimiter="\t")); h = rows[0]
    for r in rows[1:]:
        if r[h.index(key_col)].startswith(key_prefix) and add not in r[h.index(col)]:
            r[h.index(col)] = r[h.index(col)].rstrip() + " " + add; log.append((path, key_prefix, col))
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); p.write_text(o.getvalue())
edit("modifiers_it12_p1b_20261031/usability_table.tsv", "dataset", "Drosophila Wwox genetics", "finding", T + "The 2005 radiation-sensitivity phenotype of 16007179 is superseded: 21075834 states that background mutations, not the targeted Wwox mutations, caused it, and 16007179 carries an erratum; no published rescue of any Wwox-loss phenotype was found in the sources opened (fly_wwox_feasibility_it41_20261110, partial and abstract-level reads).")
edit("recovery_it10_p23_20261031/paths_verdicts.tsv", "path", "b_genetic_modifiers_suppressors", "material_that_exists", T + "Correction: the clause 'Wwox1 fly mutant is viable and radiation-sensitive, rescued by Wwox cDNA' describes a 2005 phenotype that 21075834 attributes to background mutations; the fly rows are modifiers of other genes' phenotypes and are not a recovery path (fly_wwox_feasibility_it41_20261110).")
# map row
mp = R / "batch_sci_20261105/map/open_questions_map.tsv"; rows = list(csv.reader(io.StringIO(mp.read_text()), delimiter="\t")); h = rows[0]
if not any(r[0] == "IT41-Q04" for r in rows[1:]):
    v = dict(qid="IT41-Q04", source_ref="disease-models/wwox/research/drug_repurposing/fly_wwox_feasibility_it41_20261110/output/feasibility.tsv#FE06,FE10-FE12", question_text_max300="Does a rescuable Wwox-loss readout in the fly (sleep, lifespan) change with Nmdar1 gene dosage? Precondition: reconcile the two fly sleep datasets that disagree on the light phase. IPOTESI; no rank.", decision_at_stake_max200="Whether a genetic fly arm can say anything about NMDA-receptor dependence; the fly cannot separate GluN2A from GluN2B or AMPA from kainate.", kind="literature_executable", status="OPEN", published_on="task/it41", status_evidence="fly_wwox_feasibility_it41_20261110/README.md", last_touched="2026-11-10", blocking_reason="Reconciliation of two sleep datasets is a public-data task; any experiment is a new measurement and is not commissioned here.", executable_zero_spend="partial", claimed_by="")
    n = [""] * len(h)
    for k, x in v.items(): n[h.index(k)] = x
    rows.append(n); log.append(("map", "IT41-Q04"))
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); mp.write_text(o.getvalue())
# dated correction line on the IT30 note
q = R / "rs_r6_it30_20261106/README.md"; s = q.read_text(); u = "\n\n> **Update 2026-11-10 (IT41):** the fly Wwox1 transgene rescue of radiation sensitivity named above is superseded: PMID 21075834 attributes that phenotype to background mutations, and no published rescue of a Wwox-loss phenotype was found (fly_wwox_feasibility_it41_20261110).\n"
if "Update 2026-11-10 (IT41)" not in s: q.write_text(s.rstrip() + u); log.append(("rs_r6 README", "update"))
for l in log: print(*l)
