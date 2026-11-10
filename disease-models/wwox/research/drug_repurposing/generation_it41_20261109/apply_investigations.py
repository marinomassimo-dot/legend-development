"""IT41 P10: add to INV-05 and INV-18 the decision, the in-silico work, the new measure, the reopen condition and the priority, in the `feasibility` cell. Idempotent; marker [IT41]."""
import csv, io
from pathlib import Path
p = Path(__file__).resolve().parent.parent / "ranking_it8_p9_20261029/investigations_it20.tsv"
ADD = {
 "INV-05": "[IT41] Decision: whether a GluN2B-directed comparison is the better question (needs the d-APV abolition threshold x and one modulator's removable fraction, read at the burst). Possible in silico or from public sources: a primary source for the site and maximum effect of a second modulator; qualification of the AMPA tools. New measure: isolated NMDA-receptor current, x, removable fraction, measured bath magnesium and pH. Reopen if: a second modulator is shown to have a different ceiling at the same site, or the AMPA-tool qualification is delivered. Priority: first among the compound-facing investigations, because it is the cheapest measurement that decides whether the other arms are asked.",
 "INV-18": "[IT41] Decision: whether any HCN-directed tool arm is run. Possible in silico: an ortholog and isoform census of the tools. New measure: sag and rebound at matched potential and deflection, with capacitance and access resistance by genotype. Reopen if: the excess sag persists at matched conditions. Priority: after the matched recording and after INV-05's minimum experiment; no HCN compound is nominated before it.",
}
rows = list(csv.reader(io.StringIO(p.read_text()), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
for r in rows[1:]:
    a = ADD.get(r[ix["inv_id"]])
    if a and a not in r[ix["feasibility"]]: r[ix["feasibility"]] = (r[ix["feasibility"]].rstrip() + " " + a).strip(); print("added", r[ix["inv_id"]])
out = io.StringIO(); csv.writer(out, delimiter="\t", lineterminator="\n").writerows(rows); p.write_text(out.getvalue())
