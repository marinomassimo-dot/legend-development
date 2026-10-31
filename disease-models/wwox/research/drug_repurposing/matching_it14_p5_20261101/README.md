# IT14 P5: the minimal matching improvement and its measured value

Orchestrator, 2026-11-01 (Europe/Rome, shortly after midnight). Non-canonical; not medical advice. A known reference retrieved shows **coverage**, not predictive ability.

## Decision first

The limit that slowed IT13 and IT14 was a **join**, not a source: ChEMBL activity rows name a target (`target_chembl_id`) but not its genes, so a function-to-compound question across heteromeric or complex targets (NMDAR, GABA-A, Cav3) needed hand mapping (about 15 lines in the P6 trial). The smallest change that removes it extends the existing adapter `framework/adapters/chembl.py`: each activity hit now carries `target_type`, `target_gene_symbols` and `non_gene_target`, resolved through `target.json` in batches of 40 (the pattern the function already used for assays). **No new system, source, registry or dependency.** External resources tried in P6 (DrugCentral, Pharos, BindingDB, PDSP, PubChem, IUPHAR REST) added no relation, action or potency that the existing union lacked: WATCH or DISCARD with reasons in `scout_it14_p6_20261101`.

## What was changed

* `framework/adapters/chembl.py`: `_target_genes` and three added fields; a failed target lookup is declared in `note` and keeps the fields null (never read as 'no gene'); a target without a gene symbol (a placeholder 'Unchecked', a cell line, an organism) is flagged `non_gene_target` with null symbols.
* `framework/scripts/test_repurposing_adapter.py`: two regressions on behaviour actually introduced (component gene symbols and flagged placeholder; failed lookup declared, rows keep null genes) and the fixture extended. 30 tests, OK. The adapter selftest is green offline. The three protected behaviours are untouched: nothing here transfers evidence between molecules, counts one origin twice or turns an unknown into a negative (an unresolved target stays null).

## Measured value (declared set of IT14 P6; live ChEMBL REST, 2026-11-01; the five compounds with a ChEMBL identity in `declared_set.tsv`)

| Compound | Activity rows | Rows with gene symbols | Rows flagged no-gene | Declared genes | Declared genes reached by symbol |
|---|---|---|---|---|---|
| ethosuximide | 292 | 214 | 78 | 4 | 1 |
| bumetanide | 28 | 10 | 18 | 2 | 1 |
| radiprodil | 9 | 9 | 0 | 1 | 1 |
| apinocaltamide | 24 | 20 | 4 | 3 | 3 |
| memantine | 84 | 53 | 31 | 5 | 5 |
| **total** | **437** | **306 (70 percent)** | **131** | **15** | **11** |

Before: 0 of 437 rows carried a gene symbol (hand mapping needed for every query). After: 306 carry symbols directly, and the 131 without are labelled instead of silent. The 4 declared genes not reached are not a failure of the join: ethosuximide has no usable T-type or GIRK2 potency row in ChEMBL (the T-type and GIRK relations rest on literature, not on this source) and bumetanide's second declared gene has no activity row. Cost: one extra request per 40 distinct targets (6 requests for the largest compound). Selectivity ratios are still computed only inside one document (`scout_it14_p6_20261101/selectivity_p6.py`); family-complex targets give pseudo-ratios across origins, which the field now makes visible rather than fixing.

## Limits

Five compounds, among the best-curated in ChEMBL: coverage here says little about poorly curated ones. The counts are of rows and genes, not of verified pharmacological relations. P6's 'decisive datum' (memantine GluN1/GluN2A IC50 0.95 nM, document CHEMBL2396530) is **not new**: it is the outlier already flagged in `nmdar_pharmacology_it6_p9_20261029` (README section 5) and excluded from potency reading there; the primary paper (PMID 23692871) is not open access and was not read.
