"""IT43 P7 (DREAM): one connection used. INV-07 (is pyruvate dehydrogenase restrained?) and INV-19 (is BNIP3 raised through HIF1A?) both ask a HIF-axis question in the same isogenic WWOX-deficient
human neural system but were written as two separate measurement setups. Observation: HIF1A induces both the BNIP3 programme and the PDK genes. Relation proposed: one matched-oxygen sample series reads both.
Competing explanations: HIF-programme engaged (BNIP3 and the kinase axis move together); BNIP3 raised through another route (EGR1 or stress) with the step unrestrained; neither (a culture or oxygen artefact).
Pharmacological lever or question: PDK inhibition is conditional on the first reading; BNIP3-directed work on the second. Discriminating measure: BNIP3, the four kinase transcripts, phosphorylation at the three sites and activity before and after dephosphorylation, same lysates.
Consumers: INV-07 and INV-19 next_test and INV-07 decisive_uncertainty in both tables. Idempotent; marker [IT43]."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
ADD = {
 ("INV-07", "next_test"): "[IT43] The isogenic pair and the oxygen series of INV-19 can carry this measurement: amount and phosphorylation of the step at all three sites, activity before and after dephosphorylation, and the four kinase transcripts, read next to BNIP3 from the same lysates. Reading (IPOTESI): BNIP3, kinase and phosphorylation all up supports a HIF-linked restraint and keeps the kinase lever conditional on it; BNIP3 up with the step unrestrained leaves the lever down while INV-19 stands; neither up points to the culture or oxygen condition. The compound arms follow only after a restraint is measured.",
 ("INV-19", "next_test"): "[IT43] The step-1 lysates also serve INV-07 (phosphorylation and activity of the pyruvate dehydrogenase step and the four kinase transcripts); choose the cell material and oxygen series jointly so that one sample set answers both.",
 ("INV-07", "decisive_uncertainty"): "[IT43] The signs conflict between systems: the kinase transcript is lower in the organoid, and higher with lactate up and activity unchanged in a non-neural fibroblast line; no neural measurement exists (package metabolic_inv07_20261107). The one randomised human trial of the reference, in a mitochondrial disease, was stopped early for peripheral nerve toxicity (abstract level), a safety limit to read before any arm is proposed.",
}
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    rows = list(csv.reader(io.StringIO((R / f).read_text()), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
    for r in rows[1:]:
        for (inv, col), txt in ADD.items():
            if r[ix["inv_id"]] == inv and "[IT43]" not in r[ix[col]]: r[ix[col]] = (r[ix[col]] + " " + txt).strip()
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / f).write_text(o.getvalue())
print("applied")
