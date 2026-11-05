# IT30 resume trial (read at 2026-11-05 23:23 UTC; no repo file touched)

Start: `mandate_continuity.py status --task ORCH-ROADMAP-IT30-20261105` ->
"CONTINUE, 15 steps, TODO 8, IN_PROGRESS 4, DONE 3, BLOCKED 0, unreconciled 0; next OBJ_S0[0]".
Record: ledger/tasks/orchestrator/ORCH-ROADMAP-IT30-20261105.json (HEAD 286ac2a1, tree clean).

## 1. Steps (15)
DONE (3): S5 (fa5eb2d2; results_s11; test_stage_it30), S6 (clm_pattern_it30_20261105: README, S8_CHOICE.md, cases.tsv, chooser_blind.tsv, verifier_blind.tsv), S8 (bumetanide into card F03, S8_CHOICE.md).
IN_PROGRESS (4): S0 (IT29 landed; only the CI gate is open), S2 (two sub-items DONE: 1,600 cap, stage reproducibility; manual table v raw converter, hyperexcitability case, independence by origin open), S3 (context_it30_20261105 adapter, 5 tests; hyperexcitability class table still descriptive, two contrast cases not run), S11 (legend above the fold in 5 languages, commit 0672016e; priority reasons, premise distinction, comparator display, browser check not done).
TODO (8): S1, S4, S7, S9, S10, S12, S13, S14. S7 is the step this trial is the proof for.
Disagreements record v files:
- S7 note says "TODO 12, IN_PROGRESS 2, DONE 1" (an older count); the status command now says TODO 8 / IN_PROGRESS 4 / DONE 3. The note is stale, not the statuses.
- RESUME.worktree says "HEAD 0672016e at this write"; HEAD is 286ac2a1 (the record commit itself). Harmless.
- S0 note and IT29 record (ORCH-ROADMAP-IT29-20261105.json: MANDATE_STATE OPEN, P16 IN_PROGRESS at OBJ_P17, D0-D9 at OBJ_P18 IN_PROGRESS) agree with each other; no file/record conflict found there. The "dashboard step" in RESUME next_action is OBJ_P18 (D0-D9), not P13.

## 2. Pending verification
Workflow "Public release gate" on 0845ed06e8d0bc39d94b6d65351ec6f938b1c5e9, run 42126538327
(https://github.com/marinomassimo-dot/legend-development/actions/runs/42126538327):
API `status: in_progress`, `conclusion: null`, started 2026-11-05T23:03:06Z (about 20 min before the read).
Job release-gate: step "Regression tests" in_progress; "Structural framework lint", "Public release gate", "Upload gate report" pending.
"Publish the shareable view" run 42126538332: completed / success.
No other verification is running (no local battery named by the record; battery_it29 clone was removed).

## 3. Complete, do not redo
1. CLM pattern, 30 cases, blind chooser plus blind verifier, verdict WATCH (checkpoint) / TRIAL (pattern): disease-models/wwox/research/drug_repurposing/clm_pattern_it30_20261105/README.md, S8_CHOICE.md, cases.tsv.
2. Carried-limits fix and S11 tables (994 proposals, 220 eligible, 15 hand-overs), engine-dir recipe: generation_it30_p5_20261105/README.md, results_s11/, test_stage_it30.py (commit fa5eb2d2).
3. Bumetanide neonatal record consumed into card F03 (cards rebuilt, check_cards 30 packets 0 problems, package regenerated c26b3c6f): S8_CHOICE.md. (Also done: compound-level adapter, context_it30_20261105/README.md + results/; and the IT29 battery PASS WITH SKIPS on d099a5be and the served-site check.)

## 4. Single next action
The record's own next_action step 1: read the Public release gate state for 0845ed06. Executed above: still in_progress,
so IT29 P16 and D0-D9 must stay IN_PROGRESS and MANDATE_STATE stays OPEN; the correct update is to the IT30 S0 note only
(and S7 note). Do not poll in a loop; re-read the run (id 42126538327) later and, only if conclusion=success, update the IT29
record on main. Meanwhile the unblocked work is S3 (hyperexcitability class table to compounds, run the two contrast cases).
Not touched: ORCH-SCIBATCH-DR-20261105 / dr-parallel-20261105 (other actor).

## 5. Record update (JSON fragment, NOT applied)
```json
"OBJ_S0": {"order": 1, "steps": [{"step": "S0 Close IT29: ...", "status": "IN_PROGRESS", "owner": "orchestrator",
 "note": "... Open: workflow 'Public release gate' run 42126538327 on 0845ed06 read at 2026-11-05T23:23Z via API: status in_progress, conclusion null, job step 'Regression tests' running since 23:03:06Z. When conclusion=success: set IT29 P16 (OBJ_P17) and D0-D9 (OBJ_P18) DONE and MANDATE_STATE COMPLETE in ORCH-ROADMAP-IT29-20261105.json; if failure, read the failed step log and fix on main first"}]},
"OBJ_S7": {"order": 8, "steps": [{"step": "S7 ...", "status": "IN_PROGRESS", "owner": "orchestrator",
 "note": "resume trial 2026-11-05 from status + this record only: counts TODO 8 / IN_PROGRESS 4 / DONE 3 reproduced, pending CI identified with run id, three complete results found; gaps: old counts in this note replaced; run id and 'dashboard step = OBJ_P18' were not in RESUME and are now"}]}
```

## Needed but not in the persistent references (guessed)
Nothing guessed to proceed; two items had to be derived: the workflow run id (found via API head_sha filter, full 40-char SHA required) and that "dashboard step" means OBJ_P18 in the IT29 record.
