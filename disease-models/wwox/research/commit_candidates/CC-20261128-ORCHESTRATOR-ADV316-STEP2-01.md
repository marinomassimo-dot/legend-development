# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-ADV316-STEP2-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (SCI ADV-316 step 2, first-composition sentences for PMIDs 41744777, 42395553 and 27339895) · **Date:** 2026-11-28 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI's `SENTENCES_TO_IT32_ADV316_STEP2_SCI_20261128.md` (receipts `FTR-20261128-41744777-01`, `FTR-20261128-42395553-01`). **Checks:** three blind rounds by `legend-delegate` (sonnet, effort high stated), packets and rates in `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv316_step2_it33_second_read_20261128/`. **Status:** PROPAGATED in `BATCH_20261128_007`.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR, no version bump.** Wording narrowed to what the held sources print: PAPER 228 (`AAV9-DM` is "five point mutations", not "double-mutant"; the 127-fold unit; the 126-fold peak is text-stated from a ventral-side image and in no panel; brain vg about 60-fold lower against wild-type AAV9; brain RNA not different), PAPER 362 and CLAIM 009 (PMA 0.55 nM with A23187 0.30 µM; the mitochondrial data are endogenous protein; the fractionation markers sit on separate blots and cytochrome C is not constant; Fig 4E percentages; the "under stress" leg), CLAIM 011 (no significant treatment x genotype interaction, not "not disease-specific"; replicate unit undefined), CLAIM 047 and its working-model row (the ~8-fold is packaging only, AAV9-DM named), DL-MECH-159 (the marker rows as they are).

## 2 · Where the full text is
`make_ops_it33.py` (builds `ops_paper_it33.json`, `ops_claims_it33.json`, `ops_working_model_it33.json`: 8 + 5 + 1 record-scoped `replace-within` ops through `batch_commit.py propagate`), `apply_ledger_it33.py` (one exact-once fragment, DL-MECH-159), all in `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv316_step2_it33_second_read_20261128/`.

## 3 · Checks and what they changed
Round 1 (SCI's 21 statements, 75 clauses): 0 MUST CHANGE, 6 ADD, 4 UNSETTLED. Round 2 (my composed fragments, 48 clauses): 3 MUST CHANGE (6 percent), all repaired, 10 ADD, 1 UNSETTLED. Round 3 (repaired fragments, 53 clauses): 0 MUST CHANGE, 2 ADD applied, 1 UNSETTLED (Jurkat paper not held). Full table and what was not carried: `README_BLIND_ROUNDS_IT33.md`. Suites after the edit: `test_trace_claim_foundation` OK, `test_batch_queue` 52 OK, `test_candidate_tree_freshness` 37 OK, `test_public_claims_contract` 2 OK, the four DisMech suites OK, structural LINT no BLOCK; `test_pathograph` failed on drift until `pathograph.py` regenerated the inventory and export (VERIFY: CURRENT).

## BATCH DISPOSITION — `BATCH_20261128_007`, append-only
**Status:** PROPAGATED (paper registry, claim registry and working model by `batch_commit.py propagate`; the discovery ledger by one exact-once fragment). MINOR.
