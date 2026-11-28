# COMMIT CANDIDATE — CC-20261128-ORCHESTRATOR-CLAIM005-FIELD-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (repair of a red CI) · **Date:** 2026-11-28 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** CI of main red from run 2835 (`1c309be84`, BATCH_20261128_005): `test_trace_claim_foundation.py`, 2 failures. **Status:** PROPAGATED

> Public, disease-level, de-identified. Nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR, no version bump. Whitespace only.** CLAIM 005, `Genotype/model relevance`: BATCH_20261128_005 added a rat counter-observation inside the one-line field, so the field read as two species and the species-drift check lost CLAIM 005. The clause moves to a continuation line. No word changes.

## 2 · Where the text is
One `replace-within` operation on CLAIM 005 through `batch_commit.py propagate`: ", e nella corteccia del ratto" became ",\ne nella corteccia del ratto". Pathograph regenerated.

## 3 · Checks
`test_trace_claim_foundation.py` 22 OK (2 failures before), `test_pathograph.py` 32 OK, the four DisMech suites, `test_candidate_tree_freshness.py`, the two claim benchmark suites and `test_public_claims_contract.py` OK; structural LINT no BLOCK. No blind round: no sentence was composed.
Why it was not caught at landing: the publication gate and the landing suites did not run `test_trace_claim_foundation.py`.

## BATCH DISPOSITION — `BATCH_20261128_006`, append-only
**Status:** PROPAGATED (claim registry by `batch_commit.py propagate`). MINOR.
