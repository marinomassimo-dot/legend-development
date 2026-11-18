# Wake-up continuity: diagnosis, controlled demonstration and exact limits (2026-11-18)

Non-normative record. The operative rule lives in
[`framework/protocols/cross_session_transport.md`](../../framework/protocols/cross_session_transport.md)
("Wake-up durability: the presidio belongs to the ADV campaign, not to a chat"); this file
keeps the evidence behind it. Raw logs of the demonstration are in
[`wakeup_continuity_20261118_evidence/`](wakeup_continuity_20261118_evidence/) with
`SHA256SUMS.txt`; they are kept verbatim, including one heading that this record retracts
(see "Inferred, not observed").

## A. Diagnosis of 2026-11-18, re-checked on the present state

| Point of the mandate | Re-check | Verdict |
|---|---|---|
| Desktop environment stopped by an OOM event at 12:08:43 UTC, then restarted | `journalctl --user -u turbovnc-desktop.service`: "A process of this unit has been killed by the OOM killer" 12:08:43, "Failed with result 'oom-kill'" 12:08:52, "11.0G memory peak, 0B memory swap peak", restart job 12:08:57; unit has `OOMPolicy=stop`, `Restart=on-failure`, `MemoryMax=infinity` | confirmed |
| The VPS (this host) was not restarted | `uptime -s` = 2026-10-28 06:27:46: no reboot; only the user-level desktop service restarted | confirmed |
| External monitor recovered ADV and SCI | the monitor's event log (`~/.local/state/legend/mandate_watch/events.jsonl`) shows `RESUME` with `delivery: sent` at 12:37:51Z for `ORCH-ADV-FOLLOWTHROUGH-20261114` and 12:38:17Z for `ORCH-ADV004-20261113` (the two records the monitor could read); nothing for the HE and IT work held in messages | confirmed |
| HE and IT not recovered at first because the mandate check did not represent work held in messages | work accepted by message was not a step of any record the monitor reads; fixed by `mandate_continuity.py accept` / `step` and by steps that name a blocker still counting as executable | confirmed, fixed |
| ADV's internal recall depends on the session process | session crons are session-scoped; see "Runtime facts" for what survives a stop | confirmed, with a finding (crons are restored on resume) |
| ADV and IT share ACTOR_ID `orchestrator` but are different sessions | records carry `SESSION_NAME` / `SESSION_BINDING`; `MANDATE_BOUND` marker in the session's own transcript is the identity | confirmed |
| SCI resumed under another name broke a delivery registration | delivery refusal compared display names; now resolved through `mandate_watch.route` against live sessions by session id | confirmed, fixed |

The memory use is **not** attributed to one killed process: the journal names the cgroup that
the kernel chose (the desktop service) and the service policy stopped every process in it; it
does not say which process had grown. The measured facts are only: 16 GB RAM, no swap, one
cgroup holding browser, desktop and helper processes, and an OOM policy that widens the kill.

## B. Controlled demonstration (scratch session, no production session touched)

Probe session `HE-PROBE`, probe record `PROBE-HE-RECOVERY-20261118` in a scratch root, one
hourly-style recall (a 4-minute cron appending a timestamp to `fired.txt`), a detached probe
worktree. Session ids: `8ac2e368-8a7e-4656-ab57-4658e0724bb7` (original),
`3be20fd7-24ba-43e6-8515-5482aa93c4dc` (copy started by a flag, see finding 3),
`940511d5-863d-49c1-a533-3383038ec849` (second copy, authorised host at the end).

Proved with the real runtime (`claude --bg`, `claude stop`, `claude agents --json`):

1. **Dead session with an open mandate is recovered once.** After `claude stop`, the old watch
   said "not sent: the session is alive" because a stopped session stays in `claude agents
   --json` with no pid and no status. With `session_is_live` (pid > 0 and `/proc/<pid>` not
   zombie) the same check sends one `--resume` and the session comes back (`DEMO.txt`, 20:06:43).
2. **The recall comes back with the session.** The session cron is restored on resume under the
   same job id (`2c89b82e` in `cronlist.txt` before and after, one job after the second
   revival, `events.txt` "jobs=1"). The agent still calls `CronList` first and creates a recall
   only when none carries the mark (`recall_clause`).
3. **Flags on a session with saved options start a copy.** `--bg --name X --resume <sid>` for
   a session that has `~/.claude/jobs/<id8>/state.json` started a new session id with the
   transcript copied (marker included). The revival now passes no flags for such sessions and
   passes `--name` only for sessions without saved options.
4. **A second death is recovered again.** The "request already pending" guard held for 180
   minutes even for a session that had died again; it now applies only to a live session or
   within a 10-minute start-up grace (`DEMO.txt`, 20:26 vs 20:27).
5. **Two live sessions with the marker: no host is chosen.** `DUPLICATE_HOST` keys on the
   marker in each live session's own transcript, not on the display name: two sessions both
   called `HE-PROBE` were detected, none revived, no second recall (`DEMO.txt`, 20:29). Two
   sessions with the same name and only one marker are *not* a duplicate (fixture test).
6. **Authorised transfer.** `mandate_watch.py rebind --task … --to … --authorised-by <pointer>`
   refused while another live session carried the marker, accepted after that one was stopped,
   wrote `SESSION_BINDING` with `authorised_by` and `previous`, and logged a `rebind` event.
   The check afterwards pointed at the new session id (`DEMO.txt`, 20:30).

### Inferred, not observed

- The raw heading of the last block of `DEMO.txt` says "two live restored recalls fire twice per
  slot". That was written before the observation and is **retracted**: `fired.txt` shows one
  line per slot while one session was live, and the interval in which two sessions were live
  was too short to contain a slot. That two restored session crons in two live sessions would
  both fire is an **inference** from the documented session-scope of crons; it is the reason
  `DUPLICATE_HOST` refuses to arm or revive, not a measured fact.
- The 7-day expiry of session crons is the documented runtime behaviour; it was **not**
  waited out. The renewal bookkeeping (`recall_status`, `recall-armed`, "RECALL RENEWAL DUE")
  is fixture-tested only.

### Runtime facts used (Claude Code 2.1.327)

- The daemon auto-respawns background sessions it killed or that crashed, from
  `~/.claude/jobs/<id8>/state.json` (`respawnFlags`, `name`, `selfWake`); it does not run when
  the whole user session is gone, which is why the external hourly check exists.
- `claude agents --json` keeps stopped sessions listed; liveness must be read from the pid.

## C. Exact limits (what is NOT guaranteed)

- **Live idle session without a recall.** It is not dead, so the external check does not
  revive it (a second copy of a live session is forbidden). What the external check can do is
  request work from it only when a pending request is not already known; whether the session
  then re-arms its recall is the agent's act. A live session whose recall expired and that
  receives no message stays idle until something writes to it. The minimal supported tool is
  the hourly external check's request (it reaches a live session through its own queue) plus
  `recall-armed`/"RECALL RENEWAL DUE" in the tick: the renewal is announced, not forced.
- **Host loss with the whole user session gone** (desktop OOM stops the VNC service; cron
  service is a separate cgroup and keeps running): the external check runs, but a session can
  be resumed only if the user-level daemon is reachable. Not measured here; stated as a limit.
- **Swap.** `sudo` needs a password in this environment; nothing was changed. The exact block is
  handed to the operator through ADV (reserved decision), see the memory-containment notes.
- Transcripts were never edited and no message was simulated; every revival went through
  `claude --bg --resume`.

## D. Fixture versus real runtime

| Property | Fixture tests | Real runtime |
|---|---|---|
| dead-but-listed session revived once | `Continuity20261118` | demonstrated (B1) |
| recall restored on resume | – | demonstrated (B2) |
| no flags for saved-option sessions | `Continuity20261118` | demonstrated (B3) |
| re-revival after second death | `Continuity20261118` | demonstrated (B4) |
| `DUPLICATE_HOST` | `Continuity20261118` | demonstrated (B5) |
| authorised `rebind` | `Continuity20261118` | demonstrated (B6) |
| alias follows the marker after a rename | `Continuity20261118` | fixture only |
| accepted work visible to the monitor | `AcceptedWork` | fixture only |
| observed ref vs stale local `main` | `ObservedRef` (bare-remote fixtures) | reproduced on the real repo (local `main` 159 commits behind the verified `development/main`) |
| recall renewal due | `ObservedRef` | fixture only |

## E. Memory and recoverability (measured 2026-11-18, 16 GB, no swap, systemd 255)

**Where things live (cgroups).** `mandate_watch.py resources` lists, for every live session, the
unit that an OOM event would stop with it. At 20:38 UTC: ADV and the reconciliation session (both
revived by the hourly check) were in `cron.service`; HE, IT and five other sessions started from the desktop
were in `turbovnc-desktop.service`, which held 77 processes and about 9.2 GB RSS (an upper bound:
shared pages are counted per process) while its largest single process was 0.9 GB. The memory
peak of the killed service on 2026-11-18 was 11.0 GB with 0 B swap peak. Nothing in the journal
says which process had grown, so the loss is **not** attributed to one process.

**What the hourly check does and does not give.** The check runs from `cron.service`, a separate
unit from the desktop; a revived session lands in `cron.service`, so it survives the next desktop
OOM stop. Both units have `OOMPolicy=stop` and `Restart=on-failure`: an OOM kill *inside*
`cron.service` would stop the check and every revived session together, and systemd would restart
cron, with the next `:37` run reviving the sessions again. That worst case (up to one hour of
latency, no operator) was **reasoned from the unit settings, not provoked**, because provoking it
would stop production sessions. The desktop unit's policy was not changed: stopping a desktop
that has lost a process is a defensible policy and the change needs a measured reason.

**Containment, proven with the real kernel.** The `memory` controller is delegated under the user manager unit of uid 1000
(`cgroup.controllers` there: cpu memory pids).

- `systemd-run --user --scope -p MemoryMax=200M python3 alloc.py 600`: the process was killed by
  the OOM killer inside `run-r….scope` (exit 137, journal "A process of this unit has been killed
  by the OOM killer"); `turbovnc-desktop.service` kept `ActiveEnterTimestamp` 12:08:57 and
  `NRestarts=3`.
- `mandate_watch.py job run --task T --label capped --memory-max 300M -- python3 alloc.py 900`:
  `DONE`, exit file `137`; the same with 50 MB: exit 0. A value such as `3GB` is refused, and when
  `systemd-run` is missing the job is **not** started uncapped.
- The cap is opt-in and picks no figure: it is applied to jobs started through `job run`, not to
  processes already running or to browsers started by hand. Fixture tests: `MemoryContainment`.

**Coordination by observed load.** `mandate_watch.py resources` reports memory available, swap,
pressure-stall averages, load, the cgroups holding most RSS and the live jobs with their caps. It
states facts only; there is no threshold and nothing in the watch refuses a job because of it.

### Swap: exact limit, nothing changed

`sudo -n true` answers "a password is required"; the actor has no passwordless administrator
right, so no swap was created and nothing was bypassed. Prerequisites read without privileges:
root is ext4 on `/dev/sda1`, 41 GB available (79 % used), no `/swapfile`, no swap entry in
`/etc/fstab`, `vm.swappiness=60`, kvm guest. The change is a reserved administrator act; this is
the exact block for the operator to read and run (nothing here was run):

```
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
swapon --show && free -m
# undo: sudo swapoff /swapfile && sudo rm /swapfile && sudo sed -i '\|^/swapfile none swap|d' /etc/fstab
```

Swap lengthens the time before an OOM kill and turns some of them into slowness; it does not
remove the cause, and 4 GB is a quarter of the memory this host has.

## F. Selective cleanup (2026-11-18)

Criteria applied to each worktree before `git worktree remove` (no `--force`): HEAD is an ancestor
of the verified `development/main`; `git status --porcelain` clean; ignored files other than
`__pycache__`, `*.pyc` and the hard-linked `files/` tree absent; no process with its cwd inside;
no open mandate record names it; last activity two days old or more. Removed (15): `it41 it42
it47 it50 it51 it52 it53 p010 p010b p010v11 p013 p019 p020 p021 pushmine`; plus the probe worktree
after its evidence was on `development/main`. Kept and why: `p010c` (named as BASELINE in the
IN_PROGRESS record ORCH-P010-AEDMATRIX-20261116), `p022` (ignored run logs: unique data), `p022b`
(one commit not on `development/main`), `he86` (unmerged merge commit only; its content change,
the M101 reorder, landed from this worktree), `/tmp/it56_iso` (live processes, 32 tracked
changes), `adv`, `adv2`, `adv3` (ADV's, integrated and clean but used today).

**Space, counted by inode.** The files of the removal set were grouped by (device, inode); those
whose link count equals their occurrences inside the set are freed, the others stay linked from
the main corpus. Prediction 6.82 GB (apparent sum 202 GB, of which 65 GB is `files/` shared with
the corpus); `df` before/after 6.93 GB. The 71 GB "attributed to worktrees" is therefore not
recoverable by deleting them.

**Evaluated separately.** `uv cache prune` (the only safe form: it removes unreachable objects)
freed 0 MB of 8.4 GB, so nothing was removed from the uv cache. VS Code: the `anthropic.claude-code`
extension 2.1.326 is marked obsolete in `.obsolete`, but six processes still execute its native
binary, so its directory (367 MB) was kept; only its cached VSIX installer (176 MB, no open
handle) was removed. The Claude Code binaries under `~/.local/share/claude/versions` (2.1.317 is
run by ADV's session, 2.1.327 by the others) are the runtime's own and were not touched.

**A hazard found.** `claude purge <path>` was dry-run for the probe worktree: its plan contained
the project entry `projects["/home/desktop/legend-development"]` of `~/.claude.json` (trust,
history, MCP servers), that is the **production** project's, beside the probe's own transcripts.
It was not run. The probe sessions were unlisted with `claude rm` and only their three
transcripts and file-history directories were deleted, by exact path, after the evidence folder
was published.

## G. First production run of the new watcher (cron :37, 21:37 to 21:40 UTC) and one finding

The root checkout had been fast-forwarded to code containing d82868b75, so the hourly job ran
the new watcher for the first time. Read from the events log: 132 checks in about three minutes;
states COMPLETE 108, UNKNOWN 19, BLOCKED 3, RUNNING 2; **no `DUPLICATE_HOST`, no request sent to
a live session**; ADV's record RUNNING ("session busy; busy is not progress"). The UNKNOWN rows
are old records whose sessions no longer carry a `MANDATE_BOUND` marker (unchanged behaviour).

**Finding: a record that landed on `development/main` but is not yet in the root checkout is
UNKNOWN when two or more registered worktrees carry a copy.** `PLAN-HE-CONTINUITY-20261118` was
UNKNOWN ("multiple unmerged task records; no authoritative root copy") because the root lagged
the published ref and a second worktree had merged it. The rule that nothing is guessed is kept
(an existing test pins it). The row now says why: `published: true` and "advance the root with
`git merge --ff-only development/main`", after which the record is watched. Until then a mandate
registered by `accept --create-for` is not woken by the hourly check: the actor that creates a
standing record must make sure the root has it, or say so.

## H. ACTOR_ID `advisor`: demonstration under the new actor (2026-11-18, DEC-20261118-ADVISOR-ACTOR)

Real runtime, scratch root, probe session `HE-PROBE-ADV` (id `360e9a12-4667-4cad-804d-ba7396435027`, haiku), probe record under `ledger/tasks/advisor/` with `ACTOR_ID: advisor` and a `RECALL`
field; raw logs and digests in `wakeup_continuity_20261118_evidence/advisor_actor/`. Observed: the probe bound itself (`MANDATE_BOUND` as its own line) and armed ONE recall
(4-minute cron); `mandate_watch.py route --to advisor` resolved to it alone through "ACTOR_ID advisor: binding"; `check` RUNNING; after `claude stop`, `check --deliver resume`
sent one resume under the **same session id**; the resumed session reported `jobs=1` (the recall restored, no second one armed) and the first firing after the resume was observed
(22:12:22 UTC, `fired.txt`). Not demonstrated here, because the machinery is unchanged and was proven in section B: duplicate hosts, authorised `rebind`, flag-copy. Fixtures
(`ActorAlias`): before the passage `route --to orchestrator` is AMBIGUOUS (IT and ADV carry the same ACTOR_ID); after it, `advisor` resolves to the ADV session and `orchestrator` to IT; a
COMPLETE record of an actor bound to another live session does not count; an unreachable host reads UNRESOLVED. The probe session was unlisted with `claude rm`; its transcript was deleted by exact path.
