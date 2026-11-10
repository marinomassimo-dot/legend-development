"""IT43 P3: the S9 result reaches the compound view (V13, INV-07) and the investigations text; idempotent."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent
P = R / "generation_it41_20261109/compound_view.tsv"
rows = list(csv.reader(io.StringIO(P.read_text()), delimiter="\t")); h = rows[0]
if not any(r[h.index("item_id")] == "V13" for r in rows):
    v = dict(order="13", item_id="V13", inv_id="INV-07", kind="known_requalified", name_full="dichloroacetate; AZD7545; VER-246608",
      label="Lowering the kinases that restrain the pyruvate dehydrogenase step: a carded lever with typed, per-isoform rows, conditional on a premise that is unmeasured",
      action="Inhibition of the pyruvate dehydrogenase kinases, releasing the dehydrogenase step so more pyruvate is oxidised.",
      rationale="The lever was already carded; the search now gives a reference and a second, unrelated chemotype with rows on each kinase isoform, so a first experiment can compare them once the premise holds.",
      open_premise="That the dehydrogenase step is actually restrained in a WWOX-deficient human neural cell: no neural measurement of its amount, phosphorylation or activity exists, and the signs conflict (a lower kinase transcript in an organoid; a higher one with unchanged activity in a non-neural fibroblast line).",
      counter="The reference has a family record only (isoform unresolved); the two others rest on one assay each, different from each other, so their potencies are not compared; two isoforms have no row for one of them (unknown, not zero). Nothing is known about brain exposure or about which isoforms the relevant cells express. In the one randomised human trial of the reference, in a mitochondrial disease, all treated participants stopped the study drug, mostly for nerve toxicity (abstract level; efficacy not judgeable).",
      next_test="Measure the step's activity and flux with lactate, pyruvate and redox state in an isogenic human neural pair; only if it is restrained, compare the reference with the second chemotype on the same readout.",
      source_rows="s9/search_rows (relation S9); card E03; INV-07",
      registry_note="Registry rows: ChEMBL mechanism (inhibitor, family record); GtoPdb human inhibitor rows with pIC50 per isoform from two different assays.",
      moves="Up: a measured restraint of the step. Down: none found, which lowers the lead without refuting it in other cell types. Reopens with the opposite sign if the cells depend on lactate supply.",
      where_done="in_silico_then_laboratory", relation_id="S9")
    rows.append([v.get(c, "") for c in h])
    o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); P.write_text(o.getvalue())
print("applied")
