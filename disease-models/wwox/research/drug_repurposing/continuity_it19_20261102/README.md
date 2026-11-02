# IT19 P1 - why IT18 continuity failed, and what was and was not shown (2026-11-02)

Non-canonical process record. Times are UTC from the session transcript, the watch event log and the user journal.

## What happened (verified)
| Time | Fact | Source |
|---|---|---|
| 2026-11-01 20:50 | IT18 started; **no `MANDATE_BOUND` line was ever written at the start** | session transcript |
| 2026-11-01 23:10:51 | last transcript entry before an 8.3 h silence | transcript gap |
| 2026-11-01 23:11:56 | `turbovnc-desktop.service` (the desktop session that hosts the sessions) killed by the **kernel OOM killer**, restarted 23:12:06; the BioPathNet explanation step had reached 11.27 GB against a threshold that was only checked afterwards | user journal; IT19 P4 |
| host uptime | since 2026-10-28 06:27: **no reboot, no VPS restart** that night | `uptime -s`, `last reboot` |
| 2026-11-02 05:37, 06:37 | hourly check on the IT18 record: `UNKNOWN`, no action (no line was bound) | `mandate_watch.py events` |
| 2026-11-02 07:32 | I wrote the line in a narration message; **that message is not in the persisted transcript** (the transcript holds the narrations at 07:32:26 and 07:33 but not this one) | transcript scan |
| 2026-11-02 08:37 | still `UNKNOWN` | events |
| 2026-11-02 09:03:50 | first persisted line (end of the final report); 09:37 the record was COMPLETE | transcript, events |

## Causes, separated
- **Binding emitted too late / never:** at IT18 start. Verified. Cause of the first `UNKNOWN` checks.
- **Line in an unpersisted message:** verified for the 07:32 line; why that narration was not persisted is not known (other narrations of the same minutes were). Consequence: writing the line is not enough, it must be *verified* against the resolver.
- **Process death:** the sessions died at about 23:11 because the desktop service hosting them was OOM-killed - the overshoot of a trial job, not a VPS update and not a reboot. Only one overnight event is shown; the other interruptions of the day are not attributed.
- **Revival route:** even with a bound dead session, `claude --bg --resume` from cron needs CLI workspace trust of the directory; `claude --bg` in the repository root and in a worktree both answered "Workspace not trusted. Run `claude` in <dir> once and accept the trust prompt" (reproduced 2026-11-02 ~10:40). The watch had been logging only "failed rc=N"; it now logs the reason (`delivery_output`, test `test_a_failed_revival_logs_why_it_failed`).
- **Not the cause:** runtime delivery for a live idle session (in-session cron) was not tested as failing; it is armed again for this mandate.

## Fixes
1. Binding verification step in the Standing method (emit first, then `mandate_watch.py check --task <id> --deliver none --json` must return this session's id). Done this mandate: emitted before the first tool call, resolver returned session `4325d70d-...`, state RUNNING, record identity ORCH-ROADMAP-IT19-20261102.
2. `UNKNOWN` now says how to fix itself; failed revival logs its reason.
3. Cause removal: P4 now documents a kernel-enforced per-job memory cap (`systemd-run --user --scope -p MemoryMax=... -p MemorySwapMax=0`), tested on a harmless load, so a trial cannot take the desktop service down again.

## Resume: what was and was not observed
- **Not observed:** a resume after a stop. A controlled probe (a small real package with a record, a bound background session, an orderly stop, a watch check and a resume) could not start: `claude --bg` refused for lack of workspace trust, which only the operator can give by running `claude` once in the directory. The probe record was removed; no job, commit or acquisition was duplicated.
- **Observed:** correct classification on the real record (`RUNNING`, "session busy", this session's id); `COMPLETE` is never restarted (IT18 record, 09:37 event); `UNKNOWN` took no action. The failing-delivery logging is a unit test, not a live event.
- **Residual technical operation (not an authorisation matter):** run `claude` once in /home/desktop/legend-development and accept the workspace trust prompt; afterwards a dead bound session is revivable by the hourly watch. Until then only the in-session cron (live idle session) can deliver.
