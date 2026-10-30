# Continuity verification (P7, read 2026-10-30 07:55 UTC, read-only)

Sources: `crontab -l`, `~/.local/state/legend/` (`scout_daily*.json|log|md`, `mandate_watch/events.jsonl`, `mandate_watch.log`,
`daily_push_check.log`), `git reflog` of `development/main`. `/var/log/syslog` is not readable by this user, so a cron start that left no
state cannot be proven or excluded from the system log.

## Crontab (three lines, none added or changed here)

| minute | job |
|---|---|
| `45 * * * *` | `daily_push_check.py --scheduled` (acts at 19:45 Europe/Rome only; logs one line per day) |
| `20 5 * * *` | `scout_daily.py` (05:20 UTC) |
| `37 * * * *` | `mandate_watch.py check --all --deliver resume` |

## Hourly control (`mandate_watch`)

| measure | value |
|---|---|
| first event | 2026-10-28 18:58 UTC (a probe task); the cron line appeared in the crontab backup of 2026-10-28 19:00 and `mandate_watch.log` was created 19:37 |
| last 7 days | the control has existed for 38 hours, not 7 days: 38 distinct hourly runs between 2026-10-28T18 and 2026-10-30T07, no gap longer than 1.5 h (319 of 383 check events at minute :37) |
| events | 383 check events, 8 job_started events (battery jobs of IT5 to IT8, all with exit files) |
| silent when unchanged | yes: 377 of 383 checks have action NONE and no delivery; `mandate_watch.log` is 0 bytes (nothing is printed unless the action is RESUME) |
| actions other than NONE | 6: 4 on the probe task `WATCH-PROBE-20261028` (2 of them deliveries that FAILED with rc=1 at 18:58:39 and 18:59:34 on 2026-10-28, before the real mandates; the probe was a deliberate test of an absent session) and 1 each on IT4 (20:31 on 2026-10-28) and IT5 (02:26 on 2026-10-29), answered "the caller is the session: continue now", which is the in-session path, not a delivery |
| failed deliveries since the probe | 0 |
| IT9 | the IT9 record was opened at 07:46 UTC, after the 07:37 run; the next hourly run (08:37) is the first that can include it |

Observations, not defects of the tool: 3 old orchestrator records keep a stale OPEN block and are re-checked every hour with no effect:
`ORCH-METABOLIC-BATCH-20261019` and `ORCH-REPURPOSING-10H-20261021` (state UNKNOWN, "no session transcript carries MANDATE_BOUND", 44 events each) and
`INTAKE-OVERNIGHT-20261002` (BLOCKED, 44 events); IT6 was UNKNOWN 11 times during its run for the same reason. The cost is about 2 KB of
`events.jsonl` per hour (76,945 bytes in 38 h). Closing those three records through the batch path (marking them with a final verdict) would
remove the noise; it is the Orchestrator's act and not a fix to `mandate_watch.py`.

## Daily radar (`scout_daily`)

| measure | value |
|---|---|
| scheduled runs since the line exists (crontab backup of 2026-10-28 19:00) | 2 possible (2026-10-29, 2026-10-30 at 05:20 UTC); both evidenced: `scout_daily.json` `run_at` 2026-10-30T05:20:01+00:00 (not a baseline, verdict NO_USEFUL_CHANGE), and a pending-log entry dated 2026-10-29. Earlier state (discovery `seen` dates 2026-10-27) comes from manual runs |
| after the last IT8 push | yes: the last push to `development/main` was 2026-10-30 01:50:44 UTC (`90f26804`); the radar ran at 05:20:01 |
| unchanged checks silent | yes: 3 lines in `scout_daily.log` in total; in the last report the watched entries not listed below were UNCHANGED and printed nothing |
| what it printed | 2026-10-29: SigCom-LINCS (ETag changed) and openFDA-NDC (version 2026-10-27 -> 2026-10-28); 2026-10-30: one Discovery hit for the residual-function theme (a paper on another gene's variant, a Rosetta repository). All "TO_TRIAGE: a detected change is not a reading" |
| anomaly | the SigCom-LINCS line was printed on 2026-10-29 but `scout_daily_pending_log.md` holds no entry for it (only openFDA and the 2026-10-30 hit). Either a triage consumed it or the entry was lost; UNVERIFIED, and an ETag of a service endpoint changes with every deployment, so it is a noisy fingerprint (a change of the service build, not of data). No code was changed |
| failed deliveries | none recorded (the radar only prints and writes files) |

## Push check

`daily_push_check.log`: one line per day since 2026-09-30. 2026-10-29 18:45 UTC reported UNPUBLISHED (101 commits on `main`), and the three pushes
that followed (reflog: 20:35 on 2026-10-29, 00:24 and 01:50 on 2026-10-30) brought `development/main` to `90f26804`. At 07:55 UTC local `main` is 2
commits ahead (the IT9 mandate records), expected; the next scheduled check is 18:45 UTC.

## Defects

No defect small enough to fix with a test was found. Not changed: crontab, scheduler, monitors.
