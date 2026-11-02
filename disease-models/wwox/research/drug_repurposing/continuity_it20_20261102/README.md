# IT20 P1 - resume after a controlled stop, observed (2026-11-02)

Non-canonical process record. CLI on the host: Claude Code 2.1.316 (`claude --help`, `claude stop|logs|attach|rm --help` read before use). The folder trust of /home/desktop/legend-development had been accepted by the operator. All times UTC. **Manual call of the monitor, not a scheduled event** (the quiet threshold was lowered to 1 minute for the test with `--quiet-minutes 1`; the production threshold is 25).

## The probe
A diagnostic background session (`claude --bg --permission-mode auto --name it20-resume-probe`, id `43d6be83-198c-4aca-a7a1-a0c07845ba86`, cwd the repository root) bound to its own record `ORCH-ROADMAP-IT20-RESUME-20261102` (two idempotent steps; checkpoint and outputs outside git in ~/.local/state/legend/probe_it20/; the final record is `probe_record_final.json`). R1: save the radar plan to `plan_gaps.txt` unless it exists, write `checkpoint.json`. R2: from that checkpoint derive the question ids about provenance, DGIdb, pharmacology, evaluation or view (`probe_gap_queries.txt`, 26 ids, used by P7).

## Sequence (monitor events from `mandate_watch.py events`)
| Time | Event |
|---|---|
| 22:26-22:27 | session started; first reply line `MANDATE_BOUND: ORCH-ROADMAP-IT20-RESUME-20261102`; R1 done, `checkpoint.json` = step R1, sha256 691e8d2d...; record 1 DONE, 1 TODO |
| 22:27:54-22:28:46 | five checks: `RUNNING`, session id = the probe (the resolver found it from its persisted text) |
| 22:27:58 | `claude stop 43d6be83` (only this session); `claude agents --json` no longer lists it |
| 22:28:58, 22:29:00 | `STOPPED_RESUMABLE`, action RESUME: "session absent from the live listing and silent, authorised work remains" (deliver none) |
| 22:29:09 | the same check with `--deliver resume`: `claude --bg --resume 43d6be83...` **sent**, output "backgrounded 43d6be83" - same session id, not a copy |
| 22:29 | resumed session read the checkpoint, did R2 only: `gap_queries.txt` sha256 f1de2ee4..., `checkpoint.json` = step R2, record 2 of 2 DONE |
| 22:30:01 | `COMPLETE`, "record verdict RELEASED" (an unattributed call of the watch, not mine) |

## No duplication
`plan_gaps.txt` sha256 unchanged (691e8d2d...) after the resume (R1 was not redone); no commit (HEAD unchanged), no branch, no acquisition; the record stayed untracked and was removed after copying.

## What this shows and does not show
- **Shown (manual path, real runtime):** correct binding, persisted checkpoint, controlled stop of the probe only, correct classification, the real `--bg --resume` path delivering under the same id, continuation from the checkpoint, no repeated work. The earlier blocker ("Workspace not trusted") is gone for the repository root.
- **Not shown:** a delivery by the scheduled hourly cron (`37 * * * *`, `mandate_watch.py check --all --deliver resume`) to a really dead session; a RESUME delivered to a live idle session (the in-session cron) is not a resume after a stop. A scheduled event is collected below when it happens.
- Another directory with its own trust limit was not met in this probe (worktrees were not tested again).
