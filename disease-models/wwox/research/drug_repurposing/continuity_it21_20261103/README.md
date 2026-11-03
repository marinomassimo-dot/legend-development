# IT21 P9 - resume of a really stopped session by the SCHEDULED cron (observed, 2026-11-03)

Non-canonical process record. All times UTC. Production configuration: root crontab `37 * * * * mandate_watch.py check --all --deliver resume`, quiet threshold 25 minutes (default; no flag lowered, scheduler untouched).

| Time | Event |
|---|---|
| 07:44-07:45 | probe session `it21-resume-probe` (id 0997aa07..., `claude --bg --permission-mode auto`) started; first reply line `MANDATE_BOUND: ORCH-ROADMAP-IT21-RESUME-20261103`; R1 done (r1.txt 07:45:19, checkpoint step R1), record step 1 DONE |
| 07:45:27-31 | monitor checks: RUNNING (session busy / activity 0 min) |
| 07:45:31 | `claude stop 0997aa07` (only that session; main session untouched) with R2 pending |
| 08:37:47 | **scheduled cron** run: STOPPED_RESUMABLE, action RESUME, delivery **sent** ("session absent from the live listing and silent, authorised work remains") |
| 08:38:04 | resumed session (same id 0997aa07) read checkpoint, wrote r2.txt and checkpoint step R2; record 2 of 2 DONE, MANDATE_STATE COMPLETE |

## Checks
- No duplication: r1.txt unchanged (07:45:19, one line, r1_line_count=1 in r2.txt); the plan/checkpoint was not redone; no commit, no branch, no network use by the probe.
- Delivery vs acceptance vs completion kept apart: delivery = monitor event `sent` (08:37:47); acceptance = same session id back in the live listing; completion = r2.txt + record COMPLETE (08:38:04).
- Other open mandates were classified in the same run and not revived because their session was alive (`[not sent: the session is alive]`), as designed.

## Raw monitor events for the probe
```
{"action": "RESUME", "at": "2026-11-03T08:37:47Z", "delivery": "sent", "kind": "check", "state": "STOPPED_RESUMABLE", "task": "ORCH-ROADMAP-IT21-RESUME-20261103", "why": "session absent from the live listing and silent, authorised work remains (1 executable step(s) remain; next: OBJ_R2[0] R2: only if checkpoint.json says R1 and r2.txt is absent, write r2.txt with)"}
{"action": "NONE", "at": "2026-11-03T08:39:27Z", "delivery": null, "kind": "check", "state": "COMPLETE", "task": "ORCH-ROADMAP-IT21-RESUME-20261103", "why": "record verdict RELEASED"}
```
## Limit
One observation on one host with a background (`--bg`) session; it does not show behaviour for an interactive terminal session killed by OOM or power loss.
