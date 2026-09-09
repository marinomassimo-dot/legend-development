---
name: legend-start
description: Starts a LEGEND session with task-specific context, structural LINT and a READY/BLOCK verdict. Use at session start or before a consistency check; harness maintenance does not preload scientific registries.
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
4. If the operator provided studies/papers/PMIDs/DOIs/titles:
   - if they want to start the process, use `.claude/skills/legend/SKILL.md` as autopilot;
   - if they ask only for dedup/screening, activate `.claude/skills/legend-study-intake-triage/SKILL.md`.
   In any case, do not start ingest/deep-dive until dedup is done.
5. Selects and declares `SESSION_PROFILE` from the task, using
   [operator manual §1](../../../framework/manuals/operator_manual.md#1-modalità-di-sessione):
   `HARNESS`, `MINIMAL`, `STANDARD` or `FULL`. Loads that profile's context; role alone does
   not choose a profile. If the task changes, applies the new profile before the new work.
6. Runs the structural LINT:
   `python3 framework/scripts/legend_lint.py .`
   LINT reads the canonical files from disk in every profile; its checks do not require
   copying those files into model context. A PASS verifies structure, not scientific reading.
6b. For scientific work, extraction-tool maintenance, or environment/toolchain diagnosis,
   runs the toolchain preflight:
   `python3 framework/scripts/tool_preflight.py`
   Reports, in one line, which external extractors this deployment actually has. It never blocks
   (a fresh container legitimately lacks optional tools), but a session that will need figure
   extraction, page adjudication or PDF text must know BEFORE it plans, not mid-reading. On
   2026-09-09 an actor discovered only after re-acquiring a PDF that `fitz` was absent, which makes
   `regenerate_adjudications.py` — rule 5e's own remedy for a SUSPECT PDF surface — unrunnable, and
   leaves every xref-extracted figure artifact in the corpus unrestorable in that environment.
7. Reports the verdict (4 levels, aligned with CLAUDE.md §LINT Severity; CLI exit code: 0=PASS/WARN, 2=BLOCK_BATCH_COMMIT, 3=BLOCK_SYSTEM):
   - `PASS` / `WARN` → **READY** for everything (deep-dive and commit; WARNs stay in the queue).
   - `BLOCK_BATCH_COMMIT` → **READY-for-DEEP_DIVE, NOT-for-commit**. A DEEP_DIVE is read-only and may proceed; the BATCH_COMMIT stays blocked until the findings are resolved. The CLI prints `GATE: only BATCH_COMMIT blocked`.
   - `BLOCK_SYSTEM` → **total BLOCK**: 4 current files missing or manifest corrupt. Do NOT proceed with anything, go to recovery (CLAUDE.md §Recovery). The CLI prints `GATE: BLOCK_SYSTEM`.

> Rule: only `BLOCK_SYSTEM` stops a deep-dive. `BLOCK_BATCH_COMMIT` stops **only** the commit. Do not confuse the two levels.

## Expected output
A concise block: `SESSION_PROFILE`, framework/WM version, status of the 4 files from LINT,
LINT verdict (one of the 4 levels), the GATE, and "READY (deep-dive) / READY (commit) / BLOCK".
Distinguish files inspected by a validator from files actually read into context.
