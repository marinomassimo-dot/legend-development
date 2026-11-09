# Dream across sessions: what LEGEND now holds in pieces (Harness, 2026-11-09)

Reference analysed: `main` e2b1faaf (IT40 landed at 31919734; IT41 package A exists only on its task branch f02e7d4a and is read as an unpublished producer output). Selector: `dream_pass.py consumers --since 2026-11-08` and `pointers`. Not medical advice; nothing here is a claim, a rank or a gene arc. Three themes, no exhaustive scan.

## 1. A label that sits on two structures: did an older consumer inherit it? (control: link rejected)

* Observed: the label GYKI53784 is attached to the GYKI 52466 structure in the catalogue record `CAT:DGIDB:9abeaf54a97b` (GtoPdb 4210, ChEMBL CHEMBL275006) and to a different structure (C19H20N4O3) in PubChem CID 3074805 (`identity_it41_20261109/README.md`).
* Question: could a live card or the coverage matrix have counted the record's eight DGIdb rows toward GYKI 52466?
* Reopened: `coverage/coverage_matrix.json` row FAM:CAT:DGIDB:9abeaf54a97b (`cards: []`) and the F04 card identity text (names "GYKI 52466" only as a tool in the AMPAR class).
* Result: no inheritance. The matrix row is not attached to any card, and the card never reads the record. **Already correctly unconsumed; nothing to change.** This is the rejected-link control.

## 2. Record granularity and attributed selectivity (present, not yet used)

* Observed: F04's identity text calls class (C) "subunit-selective negative allosteric modulators: GluN2B (tools Ro 25-6981 and ifenprodil ...)". ChEMBL (adapter, 2026-11-09) holds for ifenprodil 112 measured activity rows: GRIN2B 36, and also sigma-1 (20), TMEM97 (12), EBP (6) and alpha-1 adrenergic rows; Ro 25-6981 has 27 rows, GRIN2B 20, with GRIN2A, alpha-1 adrenergic and DRD1 also reported (`identity_it41_20261109/identity_table.tsv`). Neither molecule has a curated mechanism row; the NMDAR family records in the catalogue carry seven genes at once.
* Proposed relation: "subunit-selective" in the card is a class label taken from the literature; the catalogue and ChEMBL sources neither confirm nor refute selectivity (activity rows carry no potency here).
* Rivals: the label is right within NMDAR subunits and says nothing across targets (fits the rows above); or the off-target rows are low-potency assay breadth (would not matter for a slice experiment); or the rows are mis-assigned. Not separated by what was read.
* Decision touched: how the card words the tools for the INV-05 comparison, and which control a GluN2B arm needs (a sigma-1 or alpha-1 component could move a burst readout). Discriminating measure: potency per target for the two tools in the same assay conditions, read from the primary papers behind the ChEMBL rows (not read here).
* Class: **present but unused** (the rows were in ChEMBL; no consumer carried them). Consumer: card F04 `limits` (scientific owner). Delta (not applied): "Selectivity of ifenprodil and Ro 25-6981 is stated here between NMDAR subunits only; ChEMBL_37 reports measured activity of both on other targets (counts in `identity_it41_20261109/identity_table.tsv`); potency not compared." Application status: **delivery available, consumer not updated, not used**.

## 3. The AMPA tool the papers use is not the one the earlier package names (new combination, unpublished input)

* Observed: the earlier AMPA/NMDA package and the F04 identity text name GYKI 52466 (and NBQX) as the AMPAR tools. IT41 package A's `names_used.tsv` records that the slice papers it read name GYKI 53655 (Yelshanskaya, Digby, Dominguez-Sala) and use CNQX or perampanel elsewhere; only abstract-level items name GYKI 52466.
* Relation: GYKI 53655 is a third structure, distinct from GYKI 52466 (C19H20N4O3 against C17H15N3O2; ChEMBL CHEMBL267450 against CHEMBL275006).
* Rivals: the name in the earlier package is a shorthand for the class; or the papers' compound was the one named and the earlier tool row is simply not the compound used. Not separated.
* Decision touched: which compound an AMPA arm can cite evidence for. Discriminating step: reopen the Methods of the three papers for the compound name and supplier; depth here is the producer's table (partial full-text reads), originals not reopened by Harness.
* Class: **new combination in the repository**; novelty against the literature not assessed. Consumer: the IT41 comparison row C2 (Orchestrator) and F04 identity text. Delta: cite `identity_it41_20261109` for the GYKI 53655 / GYKI 52466 distinction. Status: delivered to the Orchestrator by message; **consumer not yet updated**.

## What changed in the work that follows

Nothing was promoted and no card or ranking was edited. The comparison for INV-05 should (a) cite evidence only for the GYKI compound the paper used, and (b) carry the other measured targets of the GluN2B tools as a control line. Both are open deltas for their owners.

## Cost and limits

Observed cost: the active session only, two reads of card and coverage JSON, no delegate, no new batch. Not independently verified by a second reader. The ChEMBL row counts are counts of reported activity rows, not evidence of action.
