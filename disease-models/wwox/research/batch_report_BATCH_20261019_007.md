# BATCH COMMIT REPORT — BATCH_20261019_007

> Follow-ups of the Mirror review of `BATCH_20261019_006` (`mirror_review_BATCH_20261019_006_and_harness.md`, findings A1 to A5). Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation, operator away. **Not medical advice.**

## Summary

- Type: MANUAL. Pre-flight LINT `WARN` (0 BLOCK); post-propagation LINT `WARN`, 0 BLOCK (the standing `UNLINKED_SUPPORT` / `POSSIBLE_CONTRAST` set).
- WM version: `WM_v7.25` -> `WM_v7.26` (MINOR; one bump per batch).
- Commit candidates: none. The scope is the Mirror's follow-ups, each verified against its source before any edit. No record was added; no claim created or reversed; **no `Status`, `Type` or `Summary` changed anywhere**.
- Snapshot `backup/20261020_batch007` (not committed); pre-batch commit `72f1487a` (the harness commit of the same session). No restore used. `FULL_FALLBACK`: none; every op list (paper registry 8 ops, working model 2, working-model history 2, discovery ledger 5) was accepted on the first dry run after one anchor fix in my own list (the `PAPER 426` anchor, a typo of mine).
- Harness items B2, B3 and the semantics sentence of B4 are not batch work: committed separately as `72f1487a` with `legend_commit.sh`; `test_manifest_receipt_repoint.py` 23 OK, `test_manifest_receipt_provenance.py` 20 OK, `test_manifest_scaffold.py` OK, release gate PASS.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_007.md` (this report); `backup/20261020_batch007/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `registries/paper_registry_current.md` | header: one sentence in the transferability scale (A2, rows against counts) and the earliest-producer sentence (B4); `PAPER 400` and `PAPER 414` transferability text (A1); `PAPER 425` overlap paragraph (A3); depth lines of `PAPER 140`, `148`, `426` name the receipt the manifest cites and the one that extended it (B4) |
| `research/discovery_ledger_current.md` | `DL-MECH-117` (A5), `166` and `167` (A3), `168` title and statement (A4) |
| `registries/working_model_current.md`, `working_model_history.md` | version, `Last update`; history note and changelog row |
| `framework/state/state_manifest_current.md`, `state_history.md` | WM version, last-batch fields; `batch_20261019_007_scope` / `_candidates` |
| derived surfaces | `pathograph` (inventory and export) regenerated; `coverage_report`, `batch_queue`, `reading_state` regenerated and byte-identical |

## FILES UNCHANGED

Claim registry, literature log, full-text queue (no op: `FT-201` already states the overlap question), the other three scientific current files, biomarker, endpoint and therapeutic files, the receipt ledger (680, untouched), `growth_anchors.jsonl` (no structural growth, so no `record`; the scale acknowledgement was **not renewed**), the deep-dive manifests, the Mirror's own review file (not edited).

## CHANGE LOG — each finding checked first

1. **A1 — Mirror right, and incomplete.** `PAPER 400` said "WWOX not measured" while recording four WWOX cases: now "appears as a count only (four cases among 261; no case-level datum ...)". The same boilerplate was also inaccurate for `PAPER 414` (Rushing: a copy-number marker set and a transcript correlation are printed for WWOX); reworded, grade unchanged (T4 by the list-entry rule). `PAPER 326` and `406` do not carry a false statement; left.
2. **A2 — applied.** One sentence in the scale: a record that tabulates WWOX cases as rows with onset and genotype is T2 (Agarwala), one that only counts cases or lists the gene is T4 (Kilic), because a count has no case-level datum to transfer.
3. **A3 — Mirror right in substance, wrong in detail.** Checked in the Agarwala XML: Tables 1 and 4 carry an earlier-report entry in the Literature column for all three WWOX rows. The two same-variant rows (onset 4 and 21 days, both male) cite the Piard cohort (`PAPER 117`); the deletion row (27 days, female) cites Surana 2020 (`FT-201`). Checked in the on-disk supplement of `PAPER 117` (an integrator check, not a receipted reading): its only homozygous patient for that variant is female with onset at 7 weeks, so **neither same-variant row is that patient**; the deletion row cannot be checked (Surana not read). Result written in `PAPER 425`, `DL-MECH-166`, `DL-MECH-167`: "overlap not excluded" (with a patient reported elsewhere, and for the deletion row), the 3 of 80 stays this cohort's own proportion, and the rows are not to be added to a pooled count until traced. Nothing pooled elsewhere was found to double-count (the rows were never entered in a genotype-phenotype corpus).
4. **A4 — applied.** `DL-MECH-168` title now "A normal neuroimaging entry is listed for one early-onset WWOX case in one series (a single table entry)".
5. **A5 — applied.** `DL-MECH-117`: dominated by the denominator "only when the denominator's variance is the larger"; the paper prints case-control fold changes (HIF1A 3.8, WWOX 1.4), no variances, so the condition is inferred from the ratio tracking HIF1A, not measured.
6. **B2, B3 (harness).** The provenance docstring and the receipt protocol now say the ceiling fell from 21 to 9 by reclassification, not repair; "exactly one naming event" replaced by the code's rule (one or more, earliest coherent by append order and `event_at`) in the protocol, the repoint docstring and the test docstring.
7. **B4.** The semantics (the manifest's `receipt` is the earliest producer; a depth line may cite the later reading it reports and then says which produced and which extended) is stated once in the paper-registry header, the provenance docstring and the protocol. `PAPER 140`, `148` and `426` fixed. A sweep of all `PAPER` depth lines against their manifest found eight older records (`PAPER 005`, `011`, `018`, `054`, `061`, `063`, `071`, `094`) where the manifest cites a different receipt (mostly a later re-read, i.e. SUPERSEDED or `-02`/`-04` ordering cases). **Not edited here**: their depth lines are long legacy text and each needs a per-record reading; listed for the operator or the next batch.

## DEFAULTS_TAKEN

1. No `CC-*` candidate was authored; the Mirror review is the scope, so the manifest records `commit_candidates_propagated: 0`.
2. A3 stated as "overlap not excluded" rather than "possible overlap with PAPER 117", because the Piard check narrowed it.
3. `PAPER 414`'s grade left T4 although a literal reading of the scale could make it T3; the grade is not a finding of the Mirror and a regrade is a separate decision.
4. No `growth_anchors.py record`: no structural count changed. Registry size grew by a few KB (papers about 1.54 MB, far below the +25 percent re-raise point, 1.92 MB); **no scale acknowledgement was renewed or needed**.

## DECISIONS_TAKEN

- Harness text committed separately (`72f1487a`) before the batch, as asked.
- The eight legacy depth-line mismatches in item 7 are parked, not edited.
- The Mirror's file was not touched (A6).

## Verification

`legend_lint.py`: `WARN`, 0 BLOCK. `fulltext_receipts.py verify`: OK, 680 chained. `growth_anchors.py check`: PASS (papers 416, literature 679, unread premises 0). `public_release_gate.py`: PASS, 0 BLOCKS. `test_batch_queue.py` 51 OK, `test_pathograph.py` 32 OK. No e-mail string, truncated digest or study-identifier literal in the added text outside identifier lines already present. The full release battery was not run.
