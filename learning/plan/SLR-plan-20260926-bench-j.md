---
record_type: SESSION_LEARNING_REVIEW
date: 2026-09-26
actor_id: plan
role: Harness Engineering
runtime: Claude Code (subagent dispatched by the Orchestrator)
task: task/bench-j
classification: MEASURED_ARCHITECTURE_CHANGE
scope: BATCH_COMMIT propagation path (Harness roadmap v1.1, Wave 6, Benchmark J)
status: LOCAL
---

# Benchmark J: record-scoped editing replaces the full rewrite for three of four current files

## Work completed

Benchmark J asked whether a deterministic record-scoped editor can replace BATCH_COMMIT's
"full rewrite, unchanged sections copied verbatim" without losing legitimate edits, modelled on
Benchmark I and frozen phase by phase: J0 corpus + pre-registration (`32e91ad`), J1 editor
(`50d9d39`), J2 replay (`aa38a63`), J3 decision (`a687b30`), J4 adoption (`71900ae`). Everything
is under `framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/`.

- J0: 72 unique (commit, file) events, 708 hunks; INTENDED 614, LEGITIMATE_COLLATERAL 93,
  VERBATIM_COPY_DRIFT 1, ACCIDENTAL 0; 13 hunks hand-labelled (1.8 %).
- J2: 706 / 707 legitimate edits reproduced byte for byte, silent corruption 0, control 69 / 69.
- J3: PARTIALLY_SUPPORTED — working model, claim registry, literature log supported; the paper
  registry lost one edit to a duplicated `## Purpose` heading.
- J4: `batch_commit.py propagate` + `prompt_batch_commit.md` § 4.0 + `legend-commit` step 4.

## Learning and impact

1. **The rewrite, as practised, did not damage text** — the history contains no accidental
   collateral. The adoption case is a guarantee, not a repair; the benchmark says so rather than
   manufacturing a benefit.
2. **The failure that decided the fourth file was an address, not an edit.** Identity
   addressing is only as good as heading uniqueness; `record_scoped_edit.py blocks` names every
   duplicate, and today there is exactly one in the four files.
3. **Granularity matters per surface.** Record-level replace is the wrong unit for the working
   model (three `#` BLOCKs; BLOCK 3 holds the changelog — 88 % of the file); range edits fit it.
4. Deriving ground truth from companions (candidates, receipts, the state history) is what made
   the labelling cascade decisive; message-only attribution leaves 128 hunks to judgement. That
   generosity is disclosed in the pre-registration as a bias against detecting collateral.

`LEARNING_INDEX` is still absent (`ANNEX_INDEX.md` marks it pending); no `LEARNING_ID` or
promotion claim is made.

## Decisions taken

- A new tool, not an extension of `scoped_record_edit.py` (JSONL field edits under operator
  authorisation, a different object and contract). Revert: delete `record_scoped_edit.py`.
- `registry_records.partition` added to the existing parser instead of a second one; no existing
  output changed (107 `test_registry_records` tests green). Revert: remove the function.
- Paper registry kept on full rewrite by the pre-registered rule, although 327 / 328 of its
  edits replayed; reopen only with a new anchor and a new pre-registered replay.

No scientific current file, reading status or inference was changed; the replay ran on git
objects in a scratch clone.
