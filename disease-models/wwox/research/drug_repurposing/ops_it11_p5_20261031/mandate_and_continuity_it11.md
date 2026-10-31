# IT11 P5 (B) old-mandate reconciliation and (C) radar and hourly-check verification (2026-10-30/31 UTC, read-only)

Sources read: `ledger/tasks/orchestrator/ORCH-REPURPOSING-10H-20261021.json` (all steps, DECISIONS_TAKEN), `framework/scripts/mandate_watch.py` (classify, check, open_tasks, log_event),
`mandate_continuity.py status`, `~/.local/state/legend/mandate_watch/events.jsonl` (557 events), `scout_daily*.json|log|md`, `daily_push_check.log`, `crontab -l`,
session evaluation `session_evaluations/2026-10-22_orchestrator_repurposing_10h.md`, the audits under `page_adjudications/`. Reproduce C with `python3 -I continuity_it11.py` (output saved in `evidence/continuity_it11_output.txt`).
Tests: `test_mandate_watch.py` + `test_mandate_continuity.py`: 85 tests OK (1 skipped). The monitor was not modified (no defect reproduced).

## B1. Conclusion of the original objective

| item | finding |
|---|---|
| Objective | ten-hour batch, window 2026-10-21 21:45Z to 2026-10-22 07:45Z: P3 qualification and first P4 cards for both paths, four Scientists, hourly watch |
| Record state | `MANDATE_STATE COMPLETE`, 5 of 5 steps DONE, set 2026-10-30 12:34Z by the integrator (commit `168e9e36`, which is an ancestor of remote main); the hourly check has reported `COMPLETE (record verdict RELEASED)` since 2026-10-30 15:37Z |
| Before that | UNKNOWN 51 consecutive hourly checks ("no session transcript carries MANDATE_BOUND"): correct, nothing was started on a hypothesis |
| Verdict | the original objective is concluded. It is not widened: the later iterations IT1 to IT10 (all COMPLETE) carried the scientific line. **Nothing to propose to the operator for this record.** |

## B2. Residual scientific debts (kept, not deleted, not hidden by the closure)

The record itself names them (step evidence and DECISIONS_TAKEN revert note); I located where each lives now.

| debt named in the record / self-evaluation | where it lives now | state read |
|---|---|---|
| rerun of 53 unverifiable figure attestations | `page_adjudications/locator_audit_R2_figures_rerun_20261022.md`; later `locator_audit_R2h_repairs_20261022.md` (10 figure triples, all SUPPORTED) | the rerun table: 53 triples = 24 SUPPORTED, 1 adverse, 28 UNVERIFIABLE (image reader limit). **28 stay open** unless re-read in a session where images render; current per-manifest count not recomputed (`locator_audit.py --working-tree` not run; UNVERIFIED) |
| audits of the 3 R1d corrected entries and the R2f repairs | `locator_audit_R2f_R1d_repairs_20261022.md` | done 2026-10-22 (one OVERSHOOT, 32751129 entries 6/7, then covered by the R2h repair audit) |
| audits of the 21 narrowed R2 entries / entries with zero auditors | `locator_audit_narrowed_entries_20261024.md` (24 judged), `locator_audit_R1_repairs_20261024.md` (21 of 21 SUPPORTED) | done; the record's evidence text predates them |
| second blind pass on the P4 card repairs | `locator_audit_deep_cards_20261022.md`, `locator_audit_R4_cards_20261022.md` and the later card/needs audits of IT7 to IT9 | a pass exists; a dedicated second pass on exactly those repairs was not found (UNVERIFIED) |
| Mirror ex-post review of the batches | none found in the repository; not a precondition (LEGEND_CORE 21e) | open, optional |

Where they should live: the 28 UNVERIFIABLE figure triples belong in the locator-audit queue (`locator_audit.py --working-tree` is the gate); the Mirror review in the Mirror queue if the operator wants it. The mandate record was left untouched; closing it did not remove them.

## B3. Does the monitor behave as required? (code, logs, tests)

| property | evidence | verdict |
|---|---|---|
| live work vs stop vs concluded | `classify()`: RELEASED -> COMPLETE or PAUSED, never restarted (test `complete_paused_and_blocked_are_never_restarted`); busy session or quiet < 25 min -> RUNNING; CONTINUE + idle -> STOPPED_RESUMABLE | yes |
| job in progress | live job keeps RUNNING even silent (`jobs["alive"]`); finished-uncollected and dead jobs are reported in the request; 9 `job_started` events (IT5 to IT8 batteries) all ended with exit files | yes |
| does not restart completed mandates | 343 COMPLETE checks, action NONE every time; the only exception is by design: a COMPLETE record whose closing commit is not on the remote asks again (test `complete_record_without_the_push_is_not_complete`). The 10H closing commit is on remote main | yes |
| no repeated notification without change | only a RESUME is printed (cron output `mandate_watch.log` is 0 bytes); an accepted request is suppressed for 180 min for the same queue signature; the only repeated RESUMEs in 557 events are 3 on the probe task `WATCH-PROBE-20261028` within two minutes (18:58 to 18:59, 2 failed deliveries rc=1, which by design do not store the pending request) and one 56 minutes later after the probe was resumed by hand | yes; the repeats were a deliberate probe |
| cost | one event per mandate per hour is logged even when nothing changed (about 2 KB per hour; 109 KB now; rotated once at 256 KB) | trace by design (iteration 7), not a defect |
| still noisy | `INTAKE-OVERNIGHT-20261002` and `ORCH-METABOLIC-BATCH-20261019` stay OPEN with `ALL_BLOCKED` (unblock conditions recorded: operator PDFs or a new WWOX paper); they are logged BLOCKED hourly, silently | their closure is an Orchestrator decision; not done here, their debts are real |
| a possible weakness (not reproduced as a defect) | each COMPLETE record touched in the last 3 days triggers a `git fetch` per hour (about 10 fetches per run). No failure observed; no change made | observation |

## C1. Hourly check (cron `37 * * * *`)

First event 2026-10-28 18:58Z (probe), cron line live from 19:37Z. 52 hourly slots expected to 2026-10-30 22:37Z; **52 present**, no gap above 1.5 h between consecutive runs (64 run clusters; manual runs at 16:34 on 10-29 and the probe add extras). Failures: 2 failed deliveries, both on the probe task before the real mandates (rc=1); 0 since. Actions other than NONE: 6 (4 probe, IT4 once, IT5 once; the in-session path "the caller is the session"). IT10 was UNKNOWN once (20:37Z, before its binding) and COMPLETE at 21:37Z. Update at 06:37Z on 10-31: 60 of 60 slots present, still no gap above 1.5 h; the IT11 record is seen from the 23:37Z run (see the state in the output file).

## C2. Daily radar (`20 5 * * *`, 05:20 UTC)

| slot | evidence | status |
|---|---|---|
| 2026-10-27 | `scout_daily.log` line for SigCom-LINCS ETag change (IT9 attributes it to the cron slot) | evidenced |
| 2026-10-28 | the JSON of 07:21Z is a manual run (IT9/scout log); the 05:20 cron slot left no separate trace (state is overwritten, log silent when unchanged); syslog unreadable | **unprovable, not shown to have failed** |
| 2026-10-29 | pending-log entry dated 2026-10-29 (openFDA-NDC) and the scout-log statement "last real run 2026-10-29 05:20" | evidenced |
| 2026-10-30 | `scout_daily.json` `run_at 2026-10-30T05:20:01Z`, verdict NO_USEFUL_CHANGE, `errors []`; discovery cursor 3, 2 new items | evidenced |
| 2026-10-31 | `run_at 2026-10-31T05:20:01Z`, NO_USEFUL_CHANGE, `errors []`, discovery cursor 4; `--status`: "RADAR OK ... 2.2 h ago" at 07:3xZ | evidenced |

Result: 3 of 4 slots since the cron line existed are evidenced, 1 (10-28) is unprovable; no failure, no probe error. Radar run files are overwritten each day, so a run leaves no per-day trace except when something is selected; a per-day append line would make every slot provable (a small harness idea, not done).

Two entries wait in `scout_daily_pending_log.md` (TO_TRIAGE) for `scout_daily.py --append-log` on a task branch. `daily_push_check` ran at 18:45Z each day (hourly cron, acts once a day).

## C3. Finding that matters now: IT11 is not bound

`ORCH-ROADMAP-IT11-20261031` has been `UNKNOWN: no session transcript carries MANDATE_BOUND for this task` in all 8 hourly checks from 2026-10-30 23:37Z to 2026-10-31 06:37Z. With UNKNOWN the watch starts nothing, so the process restart that interrupted the Orchestrator session was NOT covered by the hourly control. Cause (code, `find_bound_transcript`): the marker `MANDATE_BOUND: <TASK_ID>` must start a line of the session's own text (measured 2026-10-29) and no such line exists for IT11. Action for the Orchestrator (not done here: the binding is written by the session itself): emit that line at the start of a line in the resumed session. Tool defect: none (same behaviour as IT6 and IT9 before their binding).
