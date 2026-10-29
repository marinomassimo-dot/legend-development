# P8 — ChEMBL activity and assay-context capability: executed and measured (2026-10-29)

Decision: the existing one-file ChEMBL adapter (`framework/adapters/chembl.py`) was **extended**, not duplicated. It gained
accession resolution (`uniprot`), activity rows with assay context (`target` and/or `molecule`) and declared truncation.
No new adapter, framework or gate. Licence unchanged: CC BY-SA 3.0, key-less; rows are consumed here as data with
attribution, not redistributed in the shareable package (class B).

The real need: package P9 (neuronal pharmacology, NMDA receptor) needed potency, species, preparation and assay context per
compound and receptor entity. Before this, the module had only curated mechanism rows (no numbers).

## The four required tests, on the live service (ChEMBL release as reported by the adapter in `raw_activities.json`)

| Test | Query | Result | What it shows |
|---|---|---|---|
| Positive control | ifenprodil on human single-protein targets | GluN2B (CHEMBL1904): 14 rows, median 10 nM (5.8-340); GluN2A (CHEMBL1972): 2 rows, 39.5-146 uM; GluN2C 29 uM; GluN2D 76 uM | the known GluN2B selectivity of ifenprodil is recovered, with the unit, relation and document kept (12 documents on GluN2B) |
| Ambiguous case | memantine, ketamine, dextromethorphan, amantadine, dizocilpine on the five human single-protein subunit targets | **0 rows on every single-protein target**; the same molecules hold 100, 347, 319, 584 and 33 rows on heteromeric-complex and group targets (e.g. memantine: CHEMBL1907604 GRIN1/GRIN2A 9 rows, CHEMBL1907603 GRIN1/GRIN2B 8 rows, CHEMBL2094124 group 3 rows) and on rat targets | an HTTP 200 with an empty list is not "no data": pore blockers are curated against complexes. The first version of the pull (subunit-first) would have reported "no memantine potency data"; the molecule-first mode reads every target and the result is stated per target entity |
| Incomplete result | five tool compounds (Ro 25-6981, NVP-AAM077/PEAQX, TCN-201, NAB-14, D-AP5) | `NO_MATCH_FOUND` by exact name or synonym; the free-text search returns unnamed molecules (no pref_name, no synonym) as nearest hits | not absence: ChEMBL lists research compounds by structure, without names. Resolving them needs a structure key and was not attempted (no InChIKey was invented from memory); the **tool-compound potencies are therefore not covered by this pull**, and the card must say so |
| Error and truncation | unit tests with injected faults (`ChemblActivities` in `test_repurposing_adapter.py`) | HTTP 500 on the activity page is `QUERY_ERROR`; a failing assay batch is declared and rows keep `assay_context: null`; a page cap is reported as `TRUNCATED: n of N`; a filter that matches no row is `NO_MATCH_FOUND` with "never absence" | the failure modes are states, not silence |

## What it added over the pre-existing capability, measured
- Per row: relation, value, units, pChEMBL, document, `data_validity_comment`, and assay organism / cell type / assay type /
  confidence, so a human target measured in frog oocytes or HEK cells is visibly that (first row read: human GluN2B target,
  assay in frog oocytes).
- 189 receptor rows over 12 resolved compounds in one run of about 3 minutes, 0 truncated, 0 errors.
- Limits: ChEMBL potencies come from heterogeneous assays (binding vs electrophysiology, voltage, glycine/glutamate and Mg2+
  conditions are not in the fields); a median across assays is a description of the literature, not a property of the drug.
  The state (open channel, agonist, voltage) of the receptor is **not** a ChEMBL field and has to be read from the documents.

## Files
`pull_nmdar_activities.py` (reproducible), `raw_activities.json` (every row), `activity_summary.tsv` (per compound x target).
