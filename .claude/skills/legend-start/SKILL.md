---
name: legend-start
description: Starts a LEGEND session — loads the state manifest + the 4 current files (+ meta_index for Standard sessions), runs the structural LINT and declares whether the system is READY or BLOCK. Use it at session start or when consistency must be checked before a commit.
---

# legend-start — LEGEND session bootstrap

Paths are relative to the repo root.

## What it does
1. Reads `framework/state/state_manifest_current.md` and confirms `current_state: READY`.
2. Reads `.claude/skills/legend-capability-scout/SKILL.md` (mandatory capability growth).
3. Reads `.claude/skills/legend-session-takeaways/SKILL.md` for the final closing.
   For an assigned `plan` or `junior-harness` actor, also run
   `python3 framework/scripts/harness_session_start.py --actor <ACTOR_ID>`.
   This reports the current ISO week's scout status and, for Plan, branch hygiene.
   `SCOUT_DUE` invokes `legend-harness-scout` for Junior; `TRIAGE_DUE` sends Plan to
   the named weekly report. Missing or invalid reports stay visible; they are not gates.
   Codex's `runtime_parity.py --bootstrap --actor <ACTOR_ID>` runs the same check.
4. If the operator provided studies/papers/PMIDs/DOIs/titles:
   - if they want to start the process, use `.claude/skills/legend/SKILL.md` as autopilot;
   - if they ask only for dedup/screening, activate `.claude/skills/legend-study-intake-triage/SKILL.md`.
   In any case, do not start ingest/deep-dive until dedup is done.
5. Loads the 4 canonical current files (and the meta index if Standard).
6. Runs the structural LINT:
   `python3 framework/scripts/legend_lint.py .`
7. Reports the verdict (4 levels, aligned with CLAUDE.md §LINT Severity; CLI exit code: 0=PASS/WARN, 2=BLOCK_BATCH_COMMIT, 3=BLOCK_SYSTEM):
   - `PASS` / `WARN` → **READY** for everything (deep-dive and commit; WARNs stay in the queue).
   - `BLOCK_BATCH_COMMIT` → **READY-for-DEEP_DIVE, NOT-for-commit**. A DEEP_DIVE is read-only and may proceed; the BATCH_COMMIT stays blocked until the findings are resolved. The CLI prints `GATE: only BATCH_COMMIT blocked`.
   - `BLOCK_SYSTEM` → **total BLOCK**: 4 current files missing or manifest corrupt. Do NOT proceed with anything, go to recovery (CLAUDE.md §Recovery). The CLI prints `GATE: BLOCK_SYSTEM`.

> Rule: only `BLOCK_SYSTEM` stops a deep-dive. `BLOCK_BATCH_COMMIT` stops **only** the commit. Do not confuse the two levels.

## Expected output
A concise block: framework/WM version, status of the 4 files, LINT verdict (one of the 4 levels), the GATE, and "READY (deep-dive) / READY (commit) / BLOCK".
