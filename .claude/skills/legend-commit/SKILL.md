---
name: legend-commit
description: Runs a LEGEND BATCH_COMMIT — propagates the queued commit candidates into the 4 current files, end-to-end, with a LINT gate and snapshot/restore. Use it when there are ≥5 candidates, on the weekly trigger, or on request. It stops for authorization only on URGENT cat-1 (case safety) or a MAJOR baseline-reversal.
---

# legend-commit — BATCH_COMMIT, 8 phases

Paths are relative to the repo root. Authoritative procedure: `framework/protocols/prompt_batch_commit.md`.

## Pre-gate
1. LINT: `python3 framework/scripts/legend_lint.py .`
   - `BLOCK_SYSTEM` or `BLOCK_BATCH_COMMIT` → STOP, resolve first (any BLOCK stops the commit; exit code 2 or 3).
   - `PASS`/`WARN` → proceed (exit 0; WARNs stay in the queue).
2. **Carve-out:** if the batch includes an URGENT cat-1 (a case-safety signal) or a MAJOR baseline-reversal → ask the operator for a one-line ok BEFORE writing. Otherwise proceed end-to-end.

## 8 phases
1. Inventory the commit candidates from the commit-candidate queue.
2. Conflict detection (duplicate or conflicting claims/papers).
3. Backup: snapshot the workspace (`backup/snap_<timestamp>`) via `framework/scripts/batch_commit.py`.
4. Lossless propagation into the 4 current files (full rewrite, unchanged sections copied verbatim).
5. Post-lint: re-run `legend_lint.py .` → if `BLOCK_*` (exit ≠ 0), `restore` from the snapshot and ABORT.
6. Update `framework/state/state_manifest_current.md` (WM version, last batch id).
7. Cleanup + mark the candidates as committed (append-only).
8. Append to the activity log.

## Output
The 4 mandatory blocks: FILES TO CREATE / TO UPDATE / UNCHANGED / CHANGE LOG.
