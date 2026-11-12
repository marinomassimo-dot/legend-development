# IT47 P2: SCI46 consumed to the end, with the expression follow-up

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Read in full: `keap1_nrf2_sci46_20261111/README.md`, `consumer_delta.md` (12 rows) and the engine tables; `nrf2_expression_sci46_20261111/README.md` (predictions, results, 4 delta rows).

## What IT46 had already taken, and the state of every delta row
| Delta | Recipient | State |
|---|---|---|
| P1 row 1 | V19 name, counter | taken in IT46 (binder named; counter sentence) |
| P1 row 2 | engine aliases | taken in IT46 |
| P1 row 3 | statement that cannot raise the tier | IT46 text guard; **replaced by the package cells** (relation, direction) in HE47 H1 with SCI47 filling the cells |
| P1 row 4 | condition keys (loss arm, readout class) | Harness HE46 H4 (landed): the binder's two potency statements now read NOT_COMPARABLE |
| P1 row 5 | open questions | taken in IT46 (Q03 note, Q05-Q09) |
| P1 row 6 | INV-08 steps X0-X3 | taken in IT46 |
| P1 row 7 | NEED-REDOX-NRF2 text | **not applied, by decision**: `needs.json` is an input digest of the ranking; a needs change goes through the reviewed path, and INV-08 and V19 already carry the content |
| P1 rows 8, 11 | identity declarations, recipe | Harness (landed) |
| P1 row 9 | receipts | recorded in IT46 (27) |
| P1 row 10 | the 57-row value table | **no consumer existed** (only SCI46's own scripts wrote it). IT47: `assay_rows_summary.py` counts it mechanically (below) |
| P1 row 12 | shared preparation | taken in IT46 (X0) |
| Expression row 1 | INV-08 readouts | taken in IT46 (clause SCI46q); wording reviewed here |
| Expression row 2 | M-K1 and NH1 dated note | SCI-owned files; SCI47 package B |
| Expression row 3 | W01/W05 composition caveat | carried by the INV-08 clause and by the generator's context column; the package has no README to receive a dated line |
| Expression row 4 | HCAR2 route needs a microglia-like cell | taken in IT46; **softened here** |

## A mechanical consumer for the value table (new)
`generation_it47_20261112/assay_rows_summary.py` classes the 57 rows by compound role and cell class (neuron or brain, astrocyte, microglia, non-neural), counts those with an NRF2-loss arm, those with a verified loss, and the database copies. Result (`assay_rows_summary_it47.tsv`): the non-covalent binder has **no astrocyte row**, 11 rows in a human neuronal line (2 with a loss arm, both partial or inadequate), 8 rows in primary microglia (6 with a loss arm, 4 verified), 19 in non-neural cells (17 database copies). The covalent class has 4 rows in astrocytes (2 with a loss arm) and 2 in neurons or brain.
**It checked a sentence that was live on the page and found it too strong.** V19 carried, from IT45, "no neuron or astrocyte data exist for any of these compounds". The table holds abstract-level data in primary mixed neuron-astrocyte cortical cultures with an Nrf2-knockout arm for one electrophile (a second electrophile's knockout result is not stated in the abstract), data in neurons and astrocytes without a loss arm for the two fumarates, and a neurotoxicity series for a covalent triterpenoid in a human neuronal line. For the non-covalent binder the statement stands. A dated correction was added to V19 (`apply_it47_sci46.py`), the old sentence kept.

## Wording reviewed (RNA is not function)
A clause was added to INV-08: a low RNA value is not an absent function; a gene readable in neurons is not an NRF2-specific readout; KEAP1 RNA does not show that the protein is available to a binder; the HCAR2 route of a fumarate is not expected to be tested in a culture without microglia **unless Hcar2 protein is shown in the cells used** (the held RNA reads Hcar2 only in microglia). The distinction between RNA, protein, localisation, activity and function stays in the INV-08 steps (nuclear NRF2 protein, NQO1 enzyme activity, a risk panel). Exposure and adequacy of the perturbation are carried by the IT46 P4 audit and SCI46's occlusion arm; alternative explanations by the package's H1-H6 (now read by the generator, P1).
Rankings and directions were **not** changed by any table.

## Limits
The cell-class assignment of the value rows is by keyword on the cell field (a reviewer should read the listing in `assay_rows_it47.tsv`); `depth` and `kind` are SCI46's declarations; the count does not weigh the quality of a loss arm.
