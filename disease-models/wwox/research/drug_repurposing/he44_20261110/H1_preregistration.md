# HE44 H1 — pre-registration of the activity-by-target test (written before any result was seen)

Need observed (SCI43 consumer row 9): azetukalner (CHEMBL5095264) has zero target rows in the catalogue, so the by-symbol path (`repurposing_search.py need`) does not reach it, yet ChEMBL holds a measured human EC50 on KCNQ2; the by-name path reaches it.
Component under test: `framework/scripts/target_activity.py` (to be written): gene symbol -> UniProt accession from the pinned GtoPdb target table -> the existing ChEMBL adapter by accession (exact target ids, single-protein and complex apart) -> activities by target with the adapter's coverage state. No manual table of names; no new vocabulary beyond the adapter's states.
Predictions, fixed now:
* **Known control, KCNQ2.** (a) the molecules with a catalogue mechanism row for KCNQ2 that also have a ChEMBL activity on a KCNQ2 target are returned with `reached_by_target_path = yes`; (b) azetukalner (CHEMBL5095264) is returned with `reached_by_target_path = no` and at least one human EC50 row, keeping type, relation, value, unit, assay organism and document; (c) no row carries an assigned direction (agonism, antagonism, selectivity): the fields stay empty.
* **Different real case chosen before the result, SLC6A1 (GAT-1, the V11 entry of the compound list).** (d) tiagabine (CHEMBL1027) is returned from the activity path; (e) the answer states its coverage (COMPLETE or TRUNCATED, with rows read of total); (f) if truncated, the output says so and never reads as "all compounds".
* **Failure behaviour.** (g) a symbol with no unique accession in the pinned table gives `UNRESOLVED_SYMBOL`, not an empty list; (h) an adapter failure gives `READ_ERROR`, not "no compounds".
A prediction not met is reported as not met.
