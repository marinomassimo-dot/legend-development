# Tool identity for IT41: four diagnoses and the path that carries them (Harness, 2026-11-09)

Not medical advice; no dose, schedule or route. Identity and pharmacology are kept apart. Nothing here is a ranking or a claim.

Inputs read: `mechsearch_it40_20261109/identity_check.tsv` (IT40), the catalogue (`catalog.jsonl.gz`, ChEMBL_37 2026-05-01 and DGIdb as served 2024-06-10), `catalog/ligand_reconciliation.tsv`, GtoPdb 2026.3.1 (cached), the ChEMBL adapter (live, 2026-11-09) and PubChem name/CID lookups for the structure keys.

## What the four cases really were

| Case | IT40 verdict | What is true in the sources | Where the break was |
|---|---|---|---|
| GYKI 52466 | name mismatch, same compound undetermined | The record `CAT:DGIDB:9abeaf54a97b` is displayed as Gyki53784 and lists GYKI-52466 as a synonym. Its GtoPdb ligand (4210) has the flat key LFBZZHVSGAHQPP-UHFFFAOYSA-N, equal to ChEMBL `CHEMBL275006` (pref name GYKI-52466) and to PubChem CID 3538 (GYKI 52466, C17H15N3O2). But PubChem CID 3074805 titled GYKI 53784 / LY303070 is a different structure (C19H20N4O3, the stereo form of the GYKI 53655 structure). The label GYKI53784 sits on two structures across sources; the GtoPdb comment "active isomer, non-competitive" fits the second | grouping and identity: a synonym hit was read as a mismatch, and the record's GRIA1-4 rows cannot be attributed to the GYKI 52466 structure. The ChEMBL twin was `out_of_selection` in the reconciliation, so the structure check never ran |
| Ro 25-6981 | record without the intended target | ChEMBL `CHEMBL305195` has no name and no mechanism row, so it was reached only through the DGIdb concept record (target DRD1, one DTC claim). Its ChEMBL key equals PubChem CID 6604887 (Ro 25-6981). ChEMBL holds 27 measured activities, 20 on GRIN2B (human and rat) | pharmacological relation: IT40 read only the curated mechanism table and DGIdb. "No mechanism row" was reported as "no intended target" |
| ifenprodil | present without GluN2B | `CHEMBL305187` is a molecule without a mechanism row; GtoPdb 5472 has no interaction rows in this version. ChEMBL holds 112 measured activities: GRIN2B 36 rows, but also SIGMAR1 (20), TMEM97 (12), EBP (6), alpha-1 adrenergic | same: the level of evidence was not distinguished. The GluN2B rows are measured activity, not a curated mechanism, and the compound is not shown to be selective |
| Brilliant Blue FCF | not in catalogue | ChEMBL holds it without a name: `CHEMBL3184128` (disodium salt, key SGHZXLIDFTYFHQ-UHFFFAOYSA-L, equal to PubChem CID 19700 FD&C Blue No. 1) with parent `CHEMBL3350615`; one measured activity row, mouse Pannexin-1. Brilliant Blue G (`CHEMBL4173394`) is a different compound | coverage: a name lookup cannot see a nameless record, and the catalogue selection did not take it. The identity rests on a structure-key match with a second registry, written as a declaration |

## The path

`framework/scripts/compound_identity.py` (`resolve`, `target_evidence`, CLI `python3 framework/scripts/compound_identity.py "<name>" --genes G1,G2 [--offline]`). It adds, over the existing catalogue, reconciliation and chembl adapter:

* the match kind (`NAME_EXACT`, `SYNONYM_EXACT`, `SEPARATOR_VARIANT`, `NAME_PARTIAL`, `SYNONYM_PARTIAL`, `DECLARED`, `NOT_FOUND_BY_NAME`), the record name beside the query, the ChEMBL references with their basis and whether they are in the catalogue;
* identity declarations with basis, source and date (`catalog/tool_identity_declarations.tsv`, nine rows, including `distinct_from` and `label_conflict`) as the qualified addition path for a nameless record; there is no other exception list;
* per expected gene the highest evidence level read: `CURATED_MECHANISM`, `SOURCE_INTERACTION`, `MEASURED_ACTIVITY_HUMAN`, `MEASURED_ACTIVITY_OTHER_SPECIES`, and the three non-evidence states `EMPTY_RESULT`, `NOT_READ`, `READ_ERROR`; selectivity is always `NOT_ASSESSED` and the other genes seen are listed;
* a label conflict keeps the conflicted record's source rows out of the attribution (listed as `unattributed_source_rows`).

Ten offline regressions: `framework/scripts/test_compound_identity.py`.

## Fixed inputs for IT41: `identity_table.tsv` (live ChEMBL read 2026-11-09)

| Query | Identity | Expected gene: level (rows) |
|---|---|---|
| GYKI 52466 | `SYNONYM_EXACT` via the record named Gyki53784; declared `CHEMBL275006`; label conflict | GRIA1: measured, other species (7); GRIA2: measured, human (9). The DGIdb rows are not attributed |
| NBQX | `NAME_EXACT` (record Nbqx, `CHEMBL222519`) | GRIA1, GRIA2: source interaction (39, 40) |
| perampanel | `NAME_EXACT` (`CHEMBL1214124`) | GRIA1, GRIA2: curated mechanism |
| GYKI 53655 | `DECLARED` (`CHEMBL267450`), with the catalogue record Gyki53655 (`CAT:DGIDB:8111763ff62c`) found as `SEPARATOR_VARIANT`; **distinct from GYKI 52466** (C19H20N4O3 against C17H15N3O2) | GRIA1, GRIA2: source interaction (3 DGIdb rows each); ChEMBL holds 4 measured activity rows in total. This is the compound the IT41 slice papers name; evidence for one of the two GYKI compounds is not evidence for the other |
| Ro 25-6981 | `SYNONYM_EXACT` via the DGIdb record of `CHEMBL305195`; declared | GRIN2B: measured, human (20 rows). Not curated; not shown selective (GRIN2A, alpha-1 adrenergic and DRD1 also measured) |
| ifenprodil | `NAME_EXACT` (`CHEMBL305187`; the tartrate `CHEMBL1886888` is a separate partial hit) | GRIN2B: measured, human (36). Sigma-1, TMEM97, EBP and alpha-1 measured too |
| Brilliant Blue FCF | `DECLARED` (`CHEMBL3184128`; distinct from Brilliant Blue G) | PANX1: measured, mouse (1 row) |

## Limits

* The structure keys of PubChem and the GtoPdb names are the registries' deposited records; a PubChem title is not an authority on which paper's compound a tool name means. The GYKI conflict is a conflict between registries, not a ruling on the compound. The primary papers' own names for their compound are with IT41 (`names_used.tsv`).
* A ChEMBL activity row says a gene was reported with an assay of that molecule; it does not give direction, potency used here, or selectivity. No potency value is carried.
* `NOT_FOUND_BY_NAME` and `EMPTY_RESULT` are statements about this query and these sources on this date.
* Cached GtoPdb is version 2026.3.1; DGIdb is the 2024-06-10 download in the catalogue.

## Removal

Delete `compound_identity.py`, its test, `catalog/tool_identity_declarations.tsv`, this folder and the README row in `framework/scripts/README.md`. Nothing else reads them.

## Added with the second push (IT41 package A)

The slice papers in `ampa_comparison_it41_20261109/output/names_used.tsv` name **GYKI 53655**, not GYKI 52466. The first name lookup missed its record because the catalogue spells it `Gyki53655` without a space: `SEPARATOR_VARIANT` now finds it (a reproducible defect of space-sensitive normalisation, shared by `compound_catalog.find`, left unchanged there). Two `distinct_from` declarations keep the two GYKI compounds apart in both directions. Unresolved here: `d-APV` is stored as `D-Ap5` and is not found by that name (`NOT_FOUND_BY_NAME`); IT40's identity_check handles it as `d-APV (D-Ap5)` and no declaration was written because the equivalence of the spelling was not re-read in a registry in this package.
