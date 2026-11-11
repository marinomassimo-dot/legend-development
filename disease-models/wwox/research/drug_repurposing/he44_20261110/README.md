# HE44 — capabilities made operative: activities without a mechanism row, the quantity kept to the consumer, retrieval states in the listing, names and links, cost of waiting (Harness, 2026-11-10)

Non-canonical working note. Not medical advice; no pharmacological reading is made here (that stays with the scientific producers). Task record `ledger/tasks/plan/PLAN-HE44-OPERATIVE-CAPABILITIES-20261110.json`. Base: HE43 candidate `19d09ce3` on main `380a4ee3`.

## 1. What was operative after HE43 (H0), read from calls in the code, not from declarations
| Component | Declared | Called by (merged tree) |
|---|---|---|
| `measurement.py` | HE43 handoff | no caller outside its tests (HE44 now: `action_search.py`, `target_activity.py`) |
| `compound_identity.parent_form` | HE43 handoff | the view guard only; IT43 `dgidb_listing.py` kept its own regex (HE44 now: `dgidb_listing.py`) |
| `READ_INCOMPLETE`, `ID_NOT_RESOLVED` | HE43 | only inside the component; no consumer parses levels with a closed vocabulary; the new view guard reads `ID_NOT_RESOLVED` |
| Wikidata name source | HE43 | `repurposing_view.compound_public_names` and `repurposing_shareable_audit` (real build audited PASS) |
| `join_names` | HE42 | `consume_reader.py` (verified by grep) |
HE43 binding: the session never wrote `MANDATE_BOUND` for HE43, so the watch reports UNKNOWN for it (record complete, no consequence); HE44 is bound (watch state RUNNING).

## 2. Activities reached by target (H1) — `framework/scripts/target_activity.py`
Observed need (SCI43 consumer row 9): azetukalner (CHEMBL5095264) has no target row in the catalogue, so the by-symbol path misses it; ChEMBL holds a human EC50 on KCNQ2. Path studied before designing: the catalogue's target rows come from curated mechanisms, DGIdb and GtoPdb interactions; ChEMBL activities are not in it; the adapter already reads targets by accession and activities by target with a coverage state.
Component: gene symbol -> the one UniProt accession of the pinned GtoPdb target table -> adapter by accession (single protein and complex apart) -> activities per human target with the adapter's coverage -> molecules; each row a `measurement` (original type, value, unit, relation kept); no direction, selectivity or efficacy assigned; `reached_by_target_path`, `in_catalogue`; states UNRESOLVED_SYMBOL / NO_TARGET_FOR_ACCESSION / READ_ERROR / READ_INCOMPLETE / NO_ACTIVITY_ROWS. A salt record reaches its parent (a first run showed tiagabine hydrochloride reached and tiagabine not).
Pre-registered (`H1_preregistration.md`, committed before any result): KCNQ2 control and SLC6A1 as the different case. Result: (a) ezogabine reached by the target path; (b) azetukalner returned, `reached_by_target_path` no, EC50 = 98 nM, single protein, human, with its document; (c) no direction; (d) tiagabine returned (8 activity rows), its salt record is the one the by-symbol path reaches; (e) coverage COMPLETE 220 of 220; (g) and (h) by tests. All met.
Scale, stated plainly: KCNQ2 gives 352 molecules, 347 without a ChEMBL name (screening deposits), 7 in the catalogue, 5 of those not reached by the target path (azetukalner, flupirtine, quinidine and two unnamed); SLC6A1 gives 172 molecules, 3 in the catalogue. An activity is a pointer to a primary-source read, not a candidate (quinidine's KCNQ2 row is a `>` bound; GABA on SLC6A1 is the substrate).
**Reconciliation with IT44.** IT44 built its own by-target path (`activity_search.py`, `2216ce33`) in the same hours. Not rewritten. Defect reproduced in its target resolution: the cached index (targets linked to a curated mechanism) has no target for HCN1-3, PANX1, SLC12A2, SLC12A5 and misses 117 of the exact human targets of 37 relation genes (19 single protein; `symbol_coverage.tsv`); `for ... in idx.get(sym, [])` yields nothing, so S2 was read from HCN4 only and S4 was written as 0 molecules while PANX1 has a complete activity row. IT44 now records a state per symbol and will adopt `resolve_targets` and the adapter fetch after landing.

## 3. The quantity to the point of use (H2)
Where the value was lost: `action_search.py` reduced a registry row to "6.95 pIC50 (=)". Now `search_rows.tsv` keeps that column as it was and adds `affinity_type`, `affinity_nM_column` (with relation and range) and `affinity_check` (the internal agreement of the row); the old columns are identical row by row, `molecules.tsv` is byte-identical, the IT41/IT42 tests pass. `same_datum` now converts through `measurement` (one convention, not a parallel formula). Effect: the Cs+ rows on HCN1, HCN2 and HCN4 are `UNIT_CONFLICT_SUSPECT`; 126 rows agree, 342 are not checkable. The DQP-1105 rows are `AGREE` while two of them differ from the primary table by 1000: the test says so, and the internal check is not offered as if it would have found them. Pointers for the scientific work: `cs_hcn_pointers.md` (no column is chosen).
Real cases checked to the consumer (471 GtoPdb rows of the IT41 table; 607 ChEMBL activity rows of the KCNQ2 and SLC6A1 reads):
| Case | Real instance | What reaches the consumer |
|---|---|---|
| log value and concentration | 126 rows with both columns | both kept; `AGREE` |
| interval | 11 rows with a range | the range, written smallest to largest with its unit (a first version printed `[300000.0-130000.0]`, low and high affinity, found on these rows and corrected) |
| censored | 1 registry row with `<`; 106 of 607 activity rows | relation kept; `CENSORED` flag; the converted value is a bound, never compared as a value |
| unit missing | 1 activity row (no value, no unit) | `VALUE_MISSING` / `UNIT_MISSING`; no conversion invented |
| different systems | activity rows carry target type, organism, assay id and text | kept in `measurement`; no averaging anywhere |
| registry against source | DQP-1105 (two rows 1000 off the paper), Cs+ HCN (log and nM columns 1000 apart) | DQP-1105 is `AGREE` and stays unseen by the internal check; Cs+ is `UNIT_CONFLICT_SUSPECT` |
| republished through an intermediary | DGIdb rows whose claim source is ChEMBL | `claim_source` kept in the DGIdb listing; no potency exists there to be counted twice |

## 4. Identity and coverage (H3)
`dgidb_listing.py` now uses `parent_form` (salts merge, stereo stays apart) and its summary says `overlap_basis = name_key_estimate_not_identity`. Measured: one DGIdb-only record (clorazepate dipotassium, S5) moved from "new" to "already in the simple search" (a false new); no correct link was lost; the enantiomer pair of the IT43 names was already counted as two molecules and stays two. A comparison by catalogue parent id is not a better reference here: a DGIdb-only record has no parent until it is reconciled.

## 5. Retrieval errors to the output (H4)
The chain recovery -> `target_evidence` -> identity table -> join -> page keeps the states to the table (HE43); the page's identity label is about identity, not evidence level. Two gaps closed: the public-name loader no longer lets an `ID_NOT_RESOLVED` id carry a name from another source; and the canonical `repurposing_search.py need` printed 30 of 709 rows (default `--limit`) under a header saying "all rows listed=709", so GRIN2B (122 rows) did not appear at all. It now prints `# TRUNCATED ... rows per symbol ...` and `# SYMBOLS WITHOUT A CATALOGUE TARGET ROW ...` (synthetic tests).

## 6. Cost of a real package (H5) — the HE43 package, my own session
Perimeter: this coordinator transcript from the HE43 mandate (258 turns, one model, no context drop; start context 203,188 tokens, peak 603,198); delegates counted apart from the notifications' totals (which are not output tokens). `session_model_census.py --since` by phase:
| Phase | Turns | Cache read | Output |
|---|---:|---:|---:|
| production (code, tests, regeneration) | 164 | 58.2 M | 143.6 k |
| first battery, verdict failure, fix, second battery | 28 | 13.2 M | 10.3 k |
| merge and regeneration | 17 | 8.4 M | 11.3 k |
Dominant factor: re-reading a context that grows from 203 k to 603 k tokens: the start context alone is 49% of the cache read; output is 0.2%; tool-result text carried is about 11% and the ten longest-carried results are 36% of that (whole-file dumps where a key lookup sufficed). The waiting for the second battery (73 minutes) cost 14 turns and 6.5 M cache read.
Improvement applied: wait for a battery by event (`Monitor` on the battery PID), not by repeated 10-minute polls. Comparison on the same kind of wait (the HE43 merged battery, 17 minutes from the monitor start to its event, with no polling): 2 turns and 1.3 M cache read, against 14 turns and 6.5 M cache read for the 73-minute poll-waited second battery (about 0.12 against 0.19 turns per waiting minute; the 2 turns include writing this note). Exploratory, one wait of each kind, different context lengths: it supports the practice, it does not validate a saving. Not applied, and why: a fresh window cannot be forced by the runtime; the decisive premises and the originals are untouched.

## 7. DREAM, continuity, names (H6, H7, H8)
`DREAM.md`: four connections with controls and consumers; the reopen condition of the fly question is half met (public stock listing; no phenotype or rescue), recorded as a pointer on IT41-Q04; retrieval test 2 calls, 22,291 notification tokens, correct, limits stated.
Continuity: the existing watch and stop hook were checked, not changed: 20 events, all NONE (no resume delivered, no wake-up on a completed record), HE43 UNKNOWN for the missing binding, `test_mandate_watch` 27 and `test_mandate_continuity` 68 tests OK. No second monitor or cron was created.
Names: a compound whose name is not allowed now shows its ChEMBL id as a link to the source record (identifier only, audited PASS); `onfasprodil` and NP10679 are examples (no Wikidata item).

## 8. How to remove each upgrade
`target_activity.py` and its test (nothing calls it yet); the three columns of `search_rows.tsv` and `affinity_columns` in `action_search.py` (the `affinity` column is untouched); `overlap_basis` in the DGIdb summary and the `key()` swap; `listing_notes` in `repurposing_search.py`; `compound_public_links` and its rendering; the Monitor wait is a habit, not code.

## 9. Landing
HE43: release battery PASS WITH SKIPS (233 targets, 11 skipped) on the frozen merged candidate `19d09ce3`; the record commit after it is documentation only; gate PASS; pushed as `273c8b56` with `--expect-sha`, verified by ls-remote. The live page was read after the push: its generic statement that the edition omits all compound names was out of date once names appear; it is corrected in the page source and the five languages (HE44), pending the next push.
