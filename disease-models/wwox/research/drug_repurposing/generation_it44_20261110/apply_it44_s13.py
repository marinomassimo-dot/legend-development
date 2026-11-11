"""IT44 P8: the S13 result reaches the INV-05 comparators table (one row for the clinically available pore-blocker class) and the M01 condition record (the Mg2+ coupling). Idempotent; marker [IT44]."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
def rd(p): return list(csv.reader(io.StringIO((R / p).read_text()), delimiter="\t"))
def wr(p, rows):
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / p).write_text(o.getvalue())
C = "comparators_it39_20261109/output/comparators.tsv"; rows = rd(C); h = rows[0]
NAME = "Clinically available use-dependent NMDA-receptor pore blockers (a class)"
if not any(r[h.index("comparator")] == NAME for r in rows):
    v = {"inv_id": "INV-05", "comparator": NAME, "role": "mechanism_separating", "target_and_action": "Use-dependent block of the NMDA-receptor channel at or near the magnesium site, any subunit (catalogue family records, subunit unresolved)",
         "context_of_the_measurement": "Not read in a primary source in this package; the class is named at card level (F01). The relation S13 returns the class from the catalogue; no removable fraction at a clinically plausible exposure is in any source read.",
         "selectivity_limits": "Family records show no subunit selectivity; several compounds of the class have other main actions (INFERENZA, not read here); selectivity NOT_ASSESSED",
         "exposure_or_development_note": "NOT_IN_FILES", "what_it_separates": "Total gain from a general reduction of excitation, once the abolition threshold x is measured: a burst fall near x at the removed fraction favours total gain",
         "what_it_does_not_separate": "GluN2B weight from GluN2A or total gain (no subunit selectivity); and a potency that tracks bath magnesium is a state effect, not a subunit effect",
         "source_file_and_row": "generation_it44_20261110/relation_s13_result_it44.md; s13/search_rows.tsv"}
    rows.append([v.get(k, "NOT_IN_FILES") for k in h]); wr(C, rows)
P = "ampa_nmda_discrim_20261108/output/prediction_matrix.tsv"; rows = rd(P); h = rows[0]; ci = h.index("readouts_specific")
for r in rows[1:]:
    if r[h.index("arm_id")] == "M01" and "magnesium site" not in r[ci]:
        r[ci] += " [IT44] For a use-dependent pore blocker the measured bath Mg2+ is also a condition of the drug comparison: these blockers act at or near the Mg2+ site, so their apparent potency changes with it."
wr(P, rows); print("applied")
