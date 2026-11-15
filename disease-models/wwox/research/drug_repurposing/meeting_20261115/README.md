# MEETING — implementation and observation, 15 November 2026

Actor: `plan` (Harness Engineering); runtime: Codex; profile: HARNESS.

## Problem and implementation

The operator requested a periodic team round table to surface pending work, priority-ordered
TO-DOs and prospects across ADV, Orchestrator, Science, Harness and Mirror. The permanent
practice lives once in [cross-session transport section 13](../../../../../framework/protocols/cross_session_transport.md#13--meeting).
The shared router, persistent-session bootstrap, Advisor procedure/definition and tool index
point to it. The operator's authorisation is in the existing roadmap instruction log.

The existing Advisor command now exposes `meeting`: status, a source-backed request, an
idempotent open and verbatim closing notes. The hourly `tick` includes independent meeting
status even when no strategic evaluation is due. Continuous campaigns default to six hours
between starts; material event requests can anticipate that. One existing recall, one host,
no new service, approval or required model invocation. An open round is resumed, not multiplied.

The derived agenda points at existing records and portfolio. It claims no participant has
spoken. Actual replies, unavailable participants, disagreements, decisions and transport/task
pointers belong in the closing notes. Existing task records retain execution status; a
meeting's closure neither delivers an assignment nor completes its research. Strategic choices
and operational coordination retain their current boundaries and the recipients' autonomy.

## Verification scope

The Advisor suite passed 136 tests, including eleven new meeting controls: exact timing and
start-to-start cadence, event anticipation and deduplication, late-event retention, concurrent
requests separated from evaluation saves, absent participant handling without invented replies,
actual pauses/resources/running evaluations, unchanged pilot budget, minute-based recovery,
same-second recovery, honest error handling, and a due meeting beside an ordinary NONE.
Section references (13), link targets (5), skill packages (6), tool routing (7), documented
commands (3) and release surface (11) passed. Structural LINT is WARN without a block.
The first Advisor test run failed three inherited text-count assertions because the recall
now carries a third command. The tests now verify the actual tick/meeting/evaluate routes to
one campaign and linked-worktree refusal rather than a fixed number of command mentions.

The first full inventory on a8b7b6696 was interrupted without verdict after 55 green
completed targets (56 started); its retained log is not a PASS. After integration of HE60,
138 Advisor tests and 13 section-reference tests passed. Later full-inventory verification,
exact final publication and native meeting follow-through are recorded in `ledger/tasks/plan/PLAN-MEETING-20261115.json` as observed. No live meeting,
scientific benefit or final CI success is claimed by these fixture results.

## Boundaries and reversibility

Meeting cache and pending requests survive a process restart in the existing host-state
folder. Committed minutes recover cadence and an open round on a new host; unsaved request
signals still need source/transport reconciliation. The recall retains the existing
session-lifetime/restart limitations. A broken meeting cache is reported independently and
does not stop ordinary research. No guarantee of model compliance, delivery or uptime is added.

Disable with `meeting_enabled: false` in the campaign's CONTINUOUS.json; optionally change
`meeting_interval_hours`. Removing the meeting command/tick field and their references leaves
the ordinary Advisor evaluation and research paths. No external spending, installation or
scientific promotion was performed. Runtime decision quality and total coordination cost
require observation; number of meetings is not a success measure.
