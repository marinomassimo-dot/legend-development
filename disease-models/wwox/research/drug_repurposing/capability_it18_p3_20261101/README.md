# IT18 P3: an action-direction source whose origin is not ChEMBL or GtoPdb

Non-canonical research material; not medical advice; computational, pharmacological compatibility only. Public edition, WWOX-DEE genotype class. Package written 2026-11-01 by ACTOR_ID scientist.

## Design (written and committed before the comparison was run)

**Gap chosen.** IT18 P0 (`../diagnosis_it18_20261101/README.md`, row "Compound-target-action") and IT17 P3 (`../evaluation_it17_p3_20261101/README.md`, "Not shown") leave two limits on the one field the IT18 matching question (`../matching_it18_p4_20261101/PRE_REGISTRATION.md`) depends on, the compound's action direction at a target: (1) 83 percent of the module's human ChEMBL mechanism pairs have no GtoPdb counterpart, and (2) where they do, ChEMBL and GtoPdb share literature, so their 0.997 agreement is not independent confirmation; six discordances stay unresolved at source. The existing cache does not close this: in the module's DGIdb file only the ChEMBL and GuideToPharmacology rows carry an interaction type (TTD, DTC, NCI, PharmGKB, TdgClinicalTrial, TEND and FDA rows: type NULL, except 94 DTC "inhibitor"), so DGIdb adds no third direction.

**Capability under test.** A third action source whose rows state the origin of the action label: DrugCentral `drug.target.interaction.tsv.gz` (column `ACTION_TYPE`, origin in `MOA_SOURCE`, else `ACT_SOURCE`), joined to the catalogue by the UniChem ChEMBL->DrugCentral whole-source map (`src1src34`, same route and terms as the catalogue's other UniChem maps). IT14 P6 kept DrugCentral at WATCH because it added no *pair* for eight declared compounds; this is a different question (an independent *direction* on pairs the module already has), not a re-run.

**Two routes for the same capability.** (A) direct file plus map, offline after one download; (B) ToolUniverse 1.5.8 `DrugCentral_get_targets` (backend MyChem.info, one call per compound), in a throwaway venv in the scratchpad, on a sample of 20 compounds: the six discordant-pair compounds' parents plus 16 drawn by sorted sha256 of the parent id from the matching universe and the rest of the catalogue. Measured for both: rows, action labels, origin field present, truncation, errors, wall time, requests, disk, dependencies, removability.

**Rules fixed now.**
- Direction vocabulary: the IT17 ChEMBL map (`CHEMBL_DEC`/`CHEMBL_INC` in `direction_task.py`) plus `GATING INHIBITOR` -> DECREASE; partial agonist, modulator, allosteric modulator, binding agent, antibody binding, substrate, releasing agent, chaperone, other -> no direction. Human rows only.
- Origin classes of a DrugCentral action: SHARED = CHEMBL or IUPHAR; INDEPENDENT = DRUG LABEL, SCIENTIFIC LITERATURE, KEGG DRUG, EXPERT CURATOR; OTHER = anything else (WOMBAT-PK, DRUGBANK, DRUG MATRIX, PDSP, UNKNOWN). Origin = `MOA_SOURCE` when filled, else `ACT_SOURCE`. "Independent" means a different curation origin, not a proof of truth: DrugCentral curators may have read ChEMBL or IUPHAR.
- Measures over the module's 11,917 human direct ChEMBL mechanism pairs (IT17 construction, parent ChEMBL id x UniProt): pairs with a determinate DrugCentral direction, by origin class; agreement with the module's direction; pairs with no determinate GtoPdb counterpart that gain one; the six IT17 discordant pairs (DrugCentral label and origin). On the IT18 matching universe: compound x need counts only (compounds with an INDEPENDENT determinate direction on a need target gene); no per-compound label of the universe is written here, so the P4 lock is not anticipated.
- Outcome rule: **adoption** only if INDEPENDENT determinate coverage adds at least 100 module pairs with no determinate GtoPdb counterpart and agreement with the module there has a Wilson lower bound of at least 0.90; **optional circumscribed use** if it adds fewer pairs but resolves at least one discordance or covers at least 10 matching-universe compounds; otherwise **waiting** or **discard** with the reason. ToolUniverse is preferred over route A only if it returns the same labels with the origin field at lower total cost.

## Amendment (after the first run, before any outcome was written)

The registered UniChem join left 530 DrugCentral structures with a human action unjoined (1,019 rows; bromocriptine, cabergoline, carvedilol and mibefradil among them). ToolUniverse found bromocriptine where route A did not, which is how the miss was noticed. Amendment: a second join by **exact full standard InChIKey** between DrugCentral structures (computed with RDKit from `structures.molV2.sdf.gz` by `dc_inchikeys.py`) and the catalogue's records; never by the first InChIKey block alone (stereoisomers are not interchangeable); UniChem wins where both answer (3,607 structs agree, 0 differ); 231 structs added. Both figures are reported; the outcome rule is applied to the **registered** figure.

## Results

All 11,917 module pairs (DEV and EVAL together; the split is not used because nothing LEGEND decides is scored here). Files: `comparison_registered.tsv`, `comparison_amended.tsv`, `results_*.json` (Wilson intervals, input and script digests), `discordant_*.tsv`.

| Measure | Today: GtoPdb | DrugCentral, any origin (registered / amended) | DrugCentral, INDEPENDENT origin (registered / amended) |
|---|---|---|---|
| Pairs with a determinate direction | 1,933 | 2,483 / 2,753 | 511 / 656 |
| Agreement with the module's ChEMBL direction | 1,890 / 1,896 = 0.997 (0.993-0.999) | 2,458 / 2,466 and 2,723 / 2,732, both 0.997 | 502 / 504 = 0.996 (0.986-0.999) and 644 / 646 |
| New determinate pairs where GtoPdb has no direction | - | 1,556 / 1,697 | **293 / 379** |
| Agreement on those new pairs | - | 1,553 / 1,694 | **292 / 293 = 0.997 (0.981-0.999)** and 378 / 379 |
| Module, GtoPdb and INDEPENDENT DrugCentral all determinate: all three agree | - | - | 210 / 211 (registered) |
| IT17 six discordant pairs with a DrugCentral label | - | 4 / 5 | **0 / 0** |
| Matching universe (186 compounds): directed compound x need units with a direction | 76 units | 18 / 19 | **1 / 2** |
| Matching universe: uncertain-need units with a direction | 129 units | 32 / 39 | 6 / 12 |

What the numbers say:
- **A third, differently curated direction exists for 293 (379) pairs the current path cannot check**, and it agrees with the module in all but one. Its origin is DRUG LABEL, SCIENTIFIC LITERATURE or KEGG DRUG, so this agreement does not rest on the ChEMBL-GtoPdb shared literature in the way the IT17 figure does; it may still rest on a curator reading ChEMBL.
- **The two INDEPENDENT disagreements are one DrugCentral error and one semantic difference**, not module errors: olodaterol at ADRB2, DrugCentral "ANTAGONIST" from literature against module and GtoPdb agonist (olodaterol is a beta-2 agonist in general pharmacology; not re-sourced); voxelotor at haemoglobin alpha, module "positive modulator" (oxygen affinity) against label "inhibitor" (polymerisation): the direction depends on which function is meant. A third source has its own errors, so it is a check, not an arbiter.
- **The six IT17 discordances are not resolved independently.** DrugCentral labels alfuzosin ANTAGONIST at the three alpha-1 receptors and bromocriptine ANTAGONIST at D4, siding with GtoPdb, but the origins are CHEMBL and IUPHAR: alfuzosin's DrugCentral label is a ChEMBL-origin record that differs from today's ChEMBL record (a version or correction difference, worth a ChEMBL check, not a third vote). Pralidoxime has only a CHEMBL-origin ACTIVATOR (siding with the module); repinotan has no row. The bromocriptine row is reached only through the amended join.
- **For the IT18 matching question the gain is small**: an INDEPENDENT direction for 1 (2) of 76 directed units and 6 (12) of 129 uncertain ones; any origin, 18 (19) of 76. No per-compound label of the universe is written here, so the P4 lock is not anticipated. DrugCentral covers approved drugs mostly; the WWOX-relevant tool compounds (subunit-selective NMDAR antagonists, T-type blockers in development) are largely outside it.

Route comparison (`routes.tsv`, `tu_route_comparison_*.tsv`, sample `tu_sample.txt`: the four discordant parents, 8 matching-universe and 8 other module parents by sorted SHA-256). On the 20 compounds both routes return identical labels on every shared pair (route A 8 pairs registered, 14 amended; route B 14). ToolUniverse 1.5.8 reads DrugCentral through MyChem.info, release **2023-11-01**, drops `moa_source` (the field the origin class needs), returns absence as status "error" (12 of 20), and costs a 108-distribution, about 480 MB environment and about 0.73 s per compound (about 51 min projected for the 4,181 parents) against about 4 s offline for the whole table. Its one advantage, identity resolution, is now covered by the exact-InChIKey join.

## Outcome

**Adoption, scoped to direction checking** (registered rule met: 293 new INDEPENDENT pairs, Wilson lower bound 0.981). Integrated through the adapter convention as `framework/adapters/drugcentral.py` (request by `chembl_id` through the UniChem map, by declared `struct_id`, or by `gene`; rows verbatim plus `action_origin` and `action_origin_class`; tests in `framework/scripts/test_repurposing_adapter.py`, class `DrugCentralActionOrigin`; `ACKNOWLEDGEMENTS.md` re-rendered). The bulk comparison stays in this package (`dc_direction.py`). It is a third check on the stored direction, not a reason to change any card or match by itself, and not a source for the matching decision.

**ToolUniverse for this capability: discard** (older release, origin field dropped, absence reported as an error, heavier and slower; the direct file gives the same labels). Its role as a probe is unchanged: it exposed the UniChem identity miss.

## Limits

- "INDEPENDENT" is a curation origin. DrugCentral does not state which rows its curators derived from ChEMBL or IUPHAR reading; agreement is therefore weaker evidence than a primary paper.
- Origin rule assumption: when `MOA_SOURCE` is empty the action label is taken to come from `ACT_SOURCE`; not documented by DrugCentral, inferred from the table.
- 575 action rows stay unjoined after the amendment (no UniChem entry and no exact InChIKey match in the catalogue); the adapter's `chembl_id` route uses UniChem only (no RDKit at run time), so a miss there is `NO_MATCH_FOUND` with a note to query by `struct_id`.
- WOMBAT-PK and DRUG MATRIX origins (OTHER) were not counted as independent; their terms are not stated on the licence page.
- The olodaterol and voxelotor readings rest on general pharmacology, not on the cited papers or labels.
- Route B time is a projection from 20 calls; the uv cache was warm, so the 2 s install time is not a cold-install figure.

## Files and cleanup

`dc_direction.py` (offline comparison, `--inchikeys` for the amendment), `dc_inchikeys.py` (needs RDKit in a throwaway venv), `tu_trial.py` (sample, ToolUniverse run in a throwaway venv, offline route comparison), `test_capability_p3.py` (4 tests, `-v`), outputs above, `cache_SHA256SUMS.txt`. Third-party files (DrugCentral TSV and SDF, UniChem map, derived InChIKey table, MyChem/ToolUniverse responses, ToolUniverse tool source and licence pages read) are only in the gitignored `files/drug_repurposing_it18/capability_it18_p3_20261101/cache/` (2.6 MB). Both virtual environments (ToolUniverse about 480 MB, RDKit about 130-200 MB) and the scratch downloads were deleted; nothing was installed system-wide; the shared uv wheel cache was left as it was. No key, account, e-mail or contact address was used or sent.

Reproduce: `python3 dc_direction.py compare --catalog ../catalog/catalog.jsonl.gz --gtopdb-dir <catalog cache>/gtopdb --dc <cache>/drug.target.interaction.tsv.gz --unichem <cache>/src1src34.txt.gz --needs ../needs/needs.json [--inchikeys <cache>/dc_struct_inchikey.tsv] --out-json ... --out-tsv ... --out-disc ...`

## Sources and terms

DrugCentral (University of New Mexico), CC BY-SA 4.0, https://drugcentral.org ; citation links on the site: https://doi.org/10.1093/nar/gkac1085 and https://doi.org/10.1093/nar/gkw993. UniChem (EMBL-EBI), EMBL-EBI Terms of Use. ChEMBL (CC BY-SA 3.0) and the IUPHAR/BPS Guide to PHARMACOLOGY (CC BY-SA 4.0) through the catalogue. Labels in the TSVs here are DrugCentral-, ChEMBL- and GtoPdb-derived and keep share-alike. MyChem.info (BioThings) was queried through ToolUniverse (Apache-2.0) for the route comparison only.
