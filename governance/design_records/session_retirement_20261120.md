# Background predecessor retirement — 2026-11-20

Actor: `plan` (Harness Engineering), Codex runtime.
Task: `PLAN-SESSION-RETIREMENT-20261120`.
Scope: harness only; no scientific claims, patient material, paid calls or new agents.

## Observed failure and cause

Released SCI windows accumulated as live, idle background sessions. They retained RAM
and remained reachable through native messaging, exposing the team to accidental
context reload. They were not observed making model calls merely by being idle.

The native HE transcript at 15:56:34Z records an automatic security refusal of a
compound command combining `claude stop`, pipes, waiting and worktree inspection.
The supplied reason was “Destructive or Unwanted Actions”. The evidence does not
establish which component caused rejection. Subsequent team messages treated retirement
as an operator-only duty. This generalized one runtime refusal into a standing authority
restriction. It was also possible to report handoff RUNNING while the predecessor
remained live; there was no mechanical recovery for that omitted final step.

A scoped supported stop was allowed in this Codex runtime after examining release,
activity and job evidence. That difference does not establish that a future native
Claude approval decision will allow it. No permissions were weakened, no refused
command was disguised and no kill fallback was used.

## Existing capabilities reused

`mandate_watch.py` already reads release/bind markers, runtime inventory, PID start times,
jobs and persistent local events. Its hourly host entry already runs at minute 37.
The normal `handoff` stays read-only; `--retire-old` opts into the protected action.
The existing `check --all --deliver resume` also recovers missed background retirements
for monitored, executable mandates. No extra scheduler, actor, model invocation or
repository registry was added. Normative procedure: cross-session transport section 12,
“Retire the released predecessor at a session handoff”.

The runtime listing distinguishes full `sessionId` from runtime `id`. In the live
probe, stopping by full UUID returned “No session matching”; the exact listed runtime
id succeeded. Neither display names nor guessed prefixes identify an action target.
The current `claude rm --help` includes deletion of a worktree. It is excluded; the
scripts README's earlier broader extrapolation from a scratch probe was corrected.

## Actual probes and corrections

- Earlier manual retirement of two released SCI windows preserved their transcripts
  and worktrees. The supported stop removed both live processes and their sockets.
- During this implementation, two more SCI predecessors accumulated. Both met the
  protected preconditions and were stopped by the new path; only their acting successor
  remained. A further released IT predecessor was retired through the same path.
- The first protected stop returned success before teardown completed. The initial
  immediate verification honestly returned STOP_UNVERIFIED. A later observation proved
  the process gone. The implementation now observes for up to ten half-second intervals
  after the initial observation; it never issues a second stop to achieve that result.
  Each runtime inventory call has its own existing timeout, so total elapsed time is not
  guaranteed to be five seconds.
- IT had bound its successor before its predecessor's final release. That historical
  overlap is reported, not erased. The new successor had subsequently acted after the
  release and was the unique bound host, so the old idle process could safely retire;
  the earlier mistake is not converted into an indefinite cleanup block.
- Active interactive sessions are outside automatic retirement. Unknown observations,
  active descendants, task jobs, competing hosts and a changed PID/start identity keep
  the target. Task-level job ownership deliberately prevents a claim of session-specific
  ownership which the current job metadata cannot support.

## Validation and limits

The targeted watcher suite covers dry run, exact runtime address, idempotency, retained
files, other active mandates, missing and competing successors, missing release,
interactive/busy sessions, descendants, live/corrupt jobs, changed and reused PIDs,
failed inventory, unwritable attempt state, crash after recording intent, explicit
refusal, false success and delayed teardown. It also checks the existing hourly call
path, read-only delivery, paused/closed mandates and the CLI's separate retirement result.

A failed, interrupted or unverified attempt is persisted by the existing machine-local
watcher state helpers before any automatic repeat. Only the supported stop is called;
no transcript, job-store entry or worktree is removed. A prior unverified stop that is
later independently observed absent can be reconciled without a second command.

Residuals: the runtime exposes no atomic compare-idle-and-stop operation, so a newly
arriving message can race the final observation. Linux process inspection, runtime
permission, a readable state directory and the host's scheduler remain dependencies.
No claim is made that a model will always follow the recipe. Mechanical catch-up works
only after the checkout used by host cron carries this change and for eligible monitored
mandates. There is no mechanical ban on an explicit future human resume of old history.

## Session learning and self-evaluation

DECISIONS_TAKEN: reuse the handoff and hourly watch, protect identities and active work,
keep history, and distinguish a runtime refusal from repository authority. Reversible by
removing the opt-in retirement branch and hourly catch-up call; historical evidence stays.
DEFAULTS_TAKEN: kept interactive actors and every uncertain target; no global permission
edit or deletion. A blocked retirement does not stop unrelated research.
STOP_LOG: no request for routine operator approval; temporary verification and publication
states are reported literally rather than claimed complete.
ATTRIBUTION_CENSUS: the operator identified the recurrence; native HE's refusal and runtime
help supplied the diagnosis; this actor implemented and tested the correction. No blind
independent review or prospective token-saving result is claimed.

DREAM connection: a handoff's operational consumer includes retirement, just as scientific
integration includes consumption rather than delivery alone. The useful micro-upgrade is
an observable final step and recovery in an existing mechanism, not another instruction
copy. Consumers: launcher recipe and hourly mandate watch. Counterexample: an idle
interactive actor or active task job must not be swept away to satisfy a session count.
Scientific full-text evaluation is inapplicable to this code-only task; LINT and receipt
verification are still run. Exact test/landing evidence is in the task record.
