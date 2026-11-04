# IT24 P2: chemical identity recovered from data the repository already holds (2026-11-04)

Non-canonical research material. Not medical advice. Zero queries, zero spend: every route below reads tables already in the repository or its catalogue cache.

## Problem (verified)

IT23 reported that 115 of the 158 LEGEND Q2/Q4/Q8 rows (IT22 final stage table, `generation_it22_p1_20261103/results_p4/proposals_it21.tsv`) were "DGIdb-only families with no InChIKey" and could not be
compared with the LINCS-style signature lists by identity. That comparison read only the catalogue record's own InChIKey (`signature_it23_20261103/reproduce_dseqr_cmap_comparison.py`, `leg_key`).
Two identity routes the generator and the catalogue already hold were not used by that consumer.

## Routes (`identity_census_it24.py`, reads the committed catalogue and the catalogue cache; no network)

| Route | Meaning | Merged into a ChEMBL family? |
|---|---|---|
| R0 | the family's own catalogue InChIKey | yes (it is the record) |
| R1 | merged claim-name bridge (`attribution_screen_it21.bridge_claim_name_ligands` / `family_bridge`, the same function the generator uses for H2) | yes, by the existing rule |
| R2 | unmerged reconciliation decision (related_not_merged, unresolved) with a known GtoPdb structure | **no**: structure known, relation to the ChEMBL family kept apart (stereoisomers, isotopologues, ester twins) |
| R3 | GtoPdb ligand named by the record's own concept id (`ids.iuphar_ligand`), one ligand, not labelled or radioactive, reconciliation not rejected | **no**: the structure of the record, not asserted equal to any ChEMBL family |
| none | nothing | stays UNKNOWN |

## Result (rows, families and distinct substances counted separately)

| Table | Rows | Families | R0 | R1 | R2 | R3 | none | Distinct structures (skeleton) with a key |
|---|---|---|---|---|---|---|---|---|
| Q2/Q4/Q8, IT22 final | 158 | 158 | 43 | 23 | 4 | 66 | 22 | 43 + 23 + 4 + 65 (R3 has two rows sharing one skeleton) |
| all questions, IT22 final | 1,000 | 868 | 273 | 112 | 29 | 488 | 98 | rows differ from families because a family is proposed under several questions |

Of the 115 rows IT23 called incomparable, **93 now carry a structure** (23 + 4 + 66) and **22 remain unresolved** (no ligand id, no key): 81 percent recovered at no query cost. No family was merged by name.
The 22 and the 98 (all questions) are category 4, data really missing; a small public query could address part of them but name-only matching is not accepted as identity.

## Effect on the IT23 comparison

Recomputed against the stored top-20 lists of the nine IT23 scenarios (`signature_it23_20261103/scenarios.tsv`, 180 rows, 11 with unresolved perturbagen identity):
**0 hits** with the 136 resolvable LEGEND rows (was 0 with 43). The IT23 zero stands, and it now rests on 136 of 158 rows instead of 43. It is a zero on the top 20 only; the returned-depth
comparison (300 per tail) needs the service output, which is not stored, and is not recomputed. R2 and R3 rows are compared on the InChIKey skeleton and are not asserted to be the ChEMBL substance.

## What this is not

A software and coverage gain, not predictive accuracy and not a new hypothesis. The generator's hand-over (H2) already used R1; R2/R3 are NOT used by the generator, which still needs a ChEMBL identity for hand-over.

## Regression

`test_identity_census_it24.py` (3 tests): one route per row and no structure for unresolved; related forms (valemetostat, tulmimetostat) never reported as a merge; counts add up. Merge and false-merge
behaviour itself stays covered by `generation_it21_p2_20261103/test_attribution_it21.py` (`test_family_bridge_joins_only_merged_and_never_by_name`, the estradiol ester twin) and `catalog/test_catalog_build.py`.

Reproduce: `LEGEND_CATALOG_CACHE=<catalogue cache> python3 identity_census_it24.py --proposals ../generation_it22_p1_20261103/results_p4/proposals_it21.tsv --questions Q2,Q4,Q8 --out q248`
