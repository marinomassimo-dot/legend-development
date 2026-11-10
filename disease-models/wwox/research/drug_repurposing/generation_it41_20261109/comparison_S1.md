# IT41 P4/P6 — Case 1 search result: GluN2B-directed negative modulation, what the catalogue and the cached GtoPdb table hold

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Produced by `action_search.py` from `relations_it41.tsv` row S1 (question, rivals, universe and conditions fixed in `cases.md` before the search). Source rows are in `search_rows.tsv` (199 rows over four relations); distinct molecules in `molecules.tsv`. PubMed abstracts below are abstract-level reads, not readings; nothing here is receipted.

## What the search found

S1 returned 55 distinct molecules (cross-source records merged by catalogue parent; radiolabelled forms left out). Most are not what was asked:

* **Not ifenprodil-site modulators.** The GtoPdb rows under the GluN2B target are orthosteric ligands of the glutamate or glycine site, agonists and antagonists together (20 distinct molecules), channel blockers (6: ketamine, amantadine, Mg2+, dizocilpine…) and one antagonist with no site recorded. A symbol lookup that stopped at "GRIN2B" would present these as GluN2B-directed. They are neither subunit-directed nor negative allosteric modulators at the ifenprodil site.
* **ChEMBL curated mechanisms** attach four molecules to a two-gene GRIN1/GRIN2B assembly record (radiprodil, traxoprodil, rislenemdaz, EVT-101; the catalogue action is *antagonist*, and the packages read radiprodil as a negative modulator); the other 20 distinct molecules attach to a seven-gene family record (subunit unresolved). The two-gene record names where ChEMBL attached the mechanism; it is not a selectivity measurement.
* **Ifenprodil and Ro 25-6981 do not appear** among the GluN2B rows of the curated-mechanism and interaction tables in this snapshot; ChEMBL measured-activity rows exist for both (Harness identity table, P5): that is a different evidence level, not an absence.

## Molecules that came out of the search, with their weakest link

| Molecule | What the source row says | Weakest link | Label |
|---|---|---|---|
| radiprodil | ChEMBL assembly record; package values (rat GluN1/GluN2B 82 percent maximum, rat triheteromer 45 percent, human GluN1/GluN2B 91 percent; 40994429) | the maximum depends on the receptor assembly (rat 82 against 45); human 91 against rat 82 is within the spread; washout from oocytes | known reference (IT40 packages) |
| traxoprodil, rislenemdaz, EVT-101 | ChEMBL assembly record, max phase ≤ 2, no approval statement in the catalogue | no maximum-effect or assay-context row in the catalogue; named in earlier repository material (file count not a reading) | known reference, no new reading |
| onfasprodil (MIJ821) | GtoPdb: human GluN2B, negative allosteric modulator, one row, pIC50 8.08 (the 8.3 in the original-affinity field is the same datum as an IC50 in nM), sourced to a patent; selectivity "not determined"; no assay text or receptor site. Abstract of a phase 2 trial (PMID 40767837, doi 10.4088/JCP.23m15246): "selective NR2B negative allosteric modulator", intravenous infusion in adults with treatment-resistant depression; dizziness, transient amnesia, somnolence | the receptor site is not recorded, so it cannot yet serve as a same-site chemotype control for an ifenprodil-site NAM; adult psychiatric exposure, not a developmental epilepsy setting | **new combination** (the molecule has rows in an earlier relations table of the repository (IT15) but was never discussed as a comparator for this arm) |
| NP10679 | GtoPdb: inhibition of hGluN2B in oocytes **at pH 6.9**, pIC50 7.64; abstract of a phase 1 trial (PMID 36642931, doi 10.1002/cpdd.1217): a pH-sensitive, GluN2B-selective NAM, more potent at acidic pH | its potency depends on the bath pH; any slice arm would need the pH stated and matched, which the packages' condition list did not carry | **new for LEGEND** as a comparator (one table row and raw lookup files under another spelling); a condition, not a candidate; the registry flags it "approved" while ChEMBL gives maximum phase 1 (not carried) |
| DQP-1105 | GtoPdb row filed under rat Grin2b, "negative", pIC50 6.95; the assay text names **GluN1-1a co-expressed with GluN2C**; the same ligand has its own GluN2C row (pIC50 8.15) and a GluN2D row | the subunit the 6.95 belongs to is unresolved (it differs from both) | **no GluN2B statement drawn**: the value is not read as a GluN2B measurement |
| ifenprodil, Ro 25-6981 | tools of the packages; see P5 | identity and mechanism level, Harness | known reference |

## What changes in the decision

The minimum interpretable experiment stays the IT40b one: one ifenprodil-site NAM compared with d-APV only up to its measured removable share, with the d-APV threshold x and the NAM removable fraction measured first. The search adds three things to it:

1. **Condition:** bath pH must be stated and held (NP10679 shows that GluN2B-directed potency can be pH-dependent; the question for ifenprodil-site NAMs generally is a literature check, not asserted here).
2. **Comparator candidate, not a control yet:** onfasprodil could be a second NAM with human exposure if its site is documented; until then it does not count as a "same-site chemotype control" and is not a mechanism-separating control either.
3. **No GluN2B statement from catalogue rows on glutamate- or glycine-site ligands or channel blockers.**

What would make onfasprodil more interesting: a primary source stating the ifenprodil site and a maximum effect on triheteromers; less interesting: evidence that its maximum on triheteromers is as low as ifenprodil's (then it adds a chemotype, not a different ceiling); unresolved today.

## Limits

No ranking, no recommendation, no dose. The cached GtoPdb snapshot is version 2026.3.1 (a share-alike licence: the shareable edition carries no compound names; see P9). "New for LEGEND" means absent from the repository's discussion, not new to the literature; the latter needs its own check. The two abstracts were read via the PubMed tools and are not a full-text reading.
