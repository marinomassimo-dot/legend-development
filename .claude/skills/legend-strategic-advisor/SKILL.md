---
name: legend-strategic-advisor
description: 'Strategic perspective for LEGEND, consulted or proactive. Consulted by the Orchestrator: Stage A (independent assessment, no preferred plan) then Stage B (dialogue on its intended action). Proactive pilot (Stage P): an hourly bounded check and a roughly four-hourly evaluation, driven by the operator''s roadmap, that drafts assignments for the Orchestrator, Science and Harness and follows them to a result. Saves every complete assessment. Use when a material result changes a premise or opportunity, a queue ends, or the operator edits the roadmap. Read-only analysis; gates nothing.'
---

# legend-strategic-advisor — a second, separate view on what to invest in next

A strategic perspective that is **consulted** (the Orchestrator asks: Stages A and B, optional, never a precondition) or **proactive** (Stage P, on a schedule, inside a campaign the
operator authorised: see "Proactive pilot" below). It gates nothing and approves nothing, its analysis is read-only, and the ordinary research loop runs the same without it. The Orchestrator keeps
operational coordination and decides how and in what order an assignment is run, recording why when it adapts one. The reasoning is in
the agent definition ([`.claude/agents/legend-strategic-advisor.md`](../../agents/legend-strategic-advisor.md));
this file owns discovery, invocation, persistence and handoff. Principles stay in their canonical homes
([harness principles](../../../framework/master/harness_development_principles.md),
[delegation budget](../../../framework/protocols/delegation_budget.md),
[transport §12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity)).

## When

* Campaign start; completion of an operational increment; a material result that changes a candidate,
  premise or research decision. Coalesce triggers that overlap. Not on a heartbeat, a commit or a test run.
* Reuse a saved assessment when the inputs it listed have not changed (`strategic_advisor.py snapshot`
  against the SHA and uncommitted list in its brief).
* A bounded campaign states its own ceilings in its task record; this procedure never renews them.

## Chain

```
scientific work → repurposing results → candidates, counter-evidence, open questions
→ Stage A → Stage B → Orchestrator decision → bounded work → consumer updated → (next trigger)
```

## Stage A — independent assessment

1. In the existing task record write: campaign boundary, owner session, SHA and dispatch time, the
   baseline, constraints and dependencies, and the action you would take without the advisor. Put the
   **text of that action** in the campaign's sealed folder, not in a file the advisor is pointed to:
   `strategic_advisor.py seal --campaign <DIR> --index <N> --text-file <F>`; the task record carries
   its path and sha256. The launch denies `Read` on `advisor_sealed/`; Grep and Glob over it are
   best-effort (see limits).
2. Write the mission and the constraints as two plain files (mission, scope, exclusions, time, ceilings;
   no preferred plan). Then:
   `python3 framework/scripts/strategic_advisor.py brief --stage A --campaign <DIR> --mission-file <F> --constraints-file <F> --task-record <PATH> [--expect <SHA>:<folder> ...]`
   For every delivery the mission text announces ("X is on main"), pass `--expect` with its SHA and, when it adds a folder, that folder. A date or a SHA in a record does not put the
   material in the advisor's checkout: the brief states four things apart, **announced ≠ in this snapshot ≠ reachable by the advisor's tools ≠ read** (the last is filled in `meta.json`
   after the run). The brief also lists, unasked, the commits `main` holds that this branch lacks and the folders they add, and `brief` prints a WARNING when something announced is missing.
   If it is missing, merge `development/main` into the task branch at a safe boundary (clean tree, the usual merge) and rebuild the brief — rebuilding costs nothing, only `run` counts.
   If the merge is not safe now, run anyway: the limitation is in the brief and the advisor must say it did not read that material. Never point the advisor at a sibling checkout:
   it is outside its tools, and widening them is not the remedy.
3. Run it in the background (it can take tens of minutes):
   `python3 framework/scripts/strategic_advisor.py run --stage A --campaign <DIR> --brief <DIR>/brief_A.md --model opus --effort high`
   Use `opus` only if the account serves it without new spend; otherwise `sonnet` + `high`, and say it was
   a fallback. A model flag is a request: read the model back from `A<n>/meta.json`, which keeps four things apart: the alias asked, `init_model` (the model the run started on),
   the model of every turn (`census.models`) and `final_turn_model` (the model that wrote the answer). The runtime may change model mid-run and records why
   (`refusal_fallbacks`: original and fallback model, trigger, category — never the withheld text). Both Stage A runs of the first campaign did so (2026-11-12, category `bio`);
   one ran 18 of 25 turns, and wrote its answer, on the fallback model. Say which model wrote an assessment from `final_turn_model`, never from the alias, and do not call a run
   single-model when `check` prints a NOTE about a fallback. A silent change with no recorded reason is still a PROBLEM.
4. The complete assessment is `A<n>/assessment.md`: the runtime result event, saved verbatim, with
   `meta.json` (tools the advisor was born with, model per turn, files it opened, usage, digests).
   Persist it **before** summarising or acting. Never retype it. If the run fails, the attempt still counts.

## Stage B — dialogue

`brief --stage B --campaign <DIR> --assessment <DIR>/A<n>/assessment.md --sealed-intended <DIR>/advisor_sealed/INTENDED_ACTION_<N>.md --constraints-file <F>`, then
`run --stage B … --model sonnet --effort medium`. It is a second, fresh invocation that reads the saved Stage A
in full; no live continuation is assumed. Decide, and record why the advice was accepted, adapted or rejected.
Consensus is not required. A Stage B that agrees after reading the plan shows agreement, not independence: independence is claimed for Stage A only, and only as far as its
`Freshness and exposure` section says. The advisor's inherited memory and the earlier assessments a later Stage A reads are exposure to declare, not something to strip to earn a "blind" label.

## Capture methods, in order of preference

1. The runtime's own result event of a headless run (what `run` does). `check` compares it with the persisted
   session transcript.
2. Mechanical extraction from an identified transcript: `strategic_advisor.py extract --transcript <jsonl> --out <F>`
   (a subagent transcript under `~/.claude/projects/<project>/<session>/subagents/` for the Agent-tool path).
3. Caller transcription, only if nothing above exists: label it "transcribed by caller", keep the original,
   and say that fidelity was not checked. A hash of a transcription proves only that transcription.

The raw stream and the session transcript stay local and are not published; the package keeps
`assessment.md`, `meta.json`, the briefs and the attempt log.

## Limits (what is mechanical and what is procedural)

* **Mechanical:** the tool list (`--tools`, an agent definition, `--restricted`, no MCP, `dontAsk`), read back in
  `meta.json` from the runtime's init event; the deny rule on `advisor_sealed/`; the saved assessment equal to the
  result event; the model read back per turn; a count of every launch made through this tool.
* **Procedural:** the ceilings bind only runs launched through this tool; direct `claude` calls bypass them. That
  the advisor follows its brief, opens what it should, or reports truthfully what it opened is not enforced.
  The advisor inherits project instructions and the memory index; do not call it isolated from them.
  Whether the runtime falls back to another model mid-run is not controllable from here; it is read back and disclosed.
* **Cost:** the entry-point table marks files over 20,000 bytes, and the contract tells the advisor to Grep for a range before opening a large file whole. That is a nudge, not a limit, and the
  saving it may bring is expected, not measured: no extra invocation was made to prove it. The first-turn context (about 17k tokens: instructions, memory index, tools) is paid on every turn.
* **Dashboard:** a plain page fetch returns the rendered text in 100,000-character pages, with no build stamp. Use
  the repository records for fact and the page for presentation.
* The Agent-tool path (`subagent_type: legend-strategic-advisor`) works only in a session started after the
  agent file landed; an already-running session does not see it.

## Disable or remove

Disable: stop calling it; nothing depends on it. Remove: delete `.claude/agents/legend-strategic-advisor.md`, this
folder, `framework/scripts/strategic_advisor.py` and its test, the row in `framework/scripts/README.md`, the
`run_release_regressions.py` entry, the route-registry lines, and the router rows in `CLAUDE.md` §2 and `SKILLS.md`.

## Proactive pilot (Stage P)

**Accountable host, optional consultant.** The current rule is **Laboratory ownership** in
[cross-session transport section 12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity).
The ADV host owns overall performance and the continuing programme. The read-only invocation
supplies a second perspective; it is not a required approval or the only way to choose work.
At a delivery, closure or recall, the host reconciles the originals, the current recipient
state and the consumer, chooses what next deserves investment, and follows it through.

For a host decision inside the already-authorised continuous campaign, write the ordinary
`## Assignments` / `### ASSIGNMENT n` blocks and run:
`python3 framework/scripts/strategic_advisor.py assign --campaign <DIR> --text-file <FILE>`.
This reuses the existing assignment log, keys, duplicate checks and delivery route, labels
the origin `host`, updates the last choice and launches no model. It does **not** send or
claim acceptance: resolve the live recipient, SendMessage the saved assignment pointer,
record the actual receipt with `deliver`, and verify take-in-charge and consumption.
Existing operator controls, shared resource limits and an in-flight consultant remain
visible; the bounded pilot gains no alternative route around its ceilings. Do not call
model-mediated reading or coordination "token-free" just because no delegate was launched.

When a separate perspective can change the direction, use `evaluate` as below. Its brief
now includes actual session activity and changed original-result paths at pinned revisions,
including edits to existing files. `DIFFERS OR UNAVAILABLE` requires host reconciliation at
a safe boundary, not a checkout reset, a new gate or a conclusion from an unread source.
The source index is not a shortlist or a reading receipt. A future MEETING is not permission
to defer the next useful choice. Technical completion and strategic effectiveness remain
separate: use the behavioural work in the implementation handoff, not a keyword test.

At strategic decision boundaries, the hosting session and analyst use **Direction before
status** in [cross-session transport section 12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity).
The generated brief puts that canonical paragraph and the source map ahead of the mechanical
queue and previous decision. The host applies the same reasoning at a delivery or MEETING
without commissioning another evaluation merely to fill a form. A technical test can check
that these inputs reach the analyst; useful strategic initiative still needs observed work.

**What it is.** The operator's roadmap (the marked section at the top of `disease-models/wwox/research/drug_repurposing/roadmap_current.md`) defines the mission and the priorities; the
dashboard, the open questions, DREAM and the radar help the Advisor choose how to pursue them. Without waiting to be asked it observes the laboratory, compares directions, and may draft
assignments (`### ASSIGNMENT` blocks) for the Orchestrator, Science or Harness. A new operator line in the roadmap prevails over any automatic plan and triggers a re-evaluation. The Advisor
cannot change a conclusion, ranking or qualification, and has no new mission or budget of its own.

**The two levels, one schedule.** An hourly in-session cron (the one scheduling mechanism a live session can use and the one that can also *deliver*: the host crontab already runs the mandate watch
and is not repeated) runs `python3 framework/scripts/strategic_advisor.py tick --campaign <DIR>`. `tick` is mechanical and makes no model call: it reads the roadmap digest, the commits of `main`
since the last tick, the task records, the mandate watch's own event log and the runtime's list of sessions, and answers `NONE` (nothing new: the previous assessment stands; an answer about events, not about opportunities: its line names the ready portfolio rows, and a statement that remaining work depends on the operator names them too), `EVALUATE`,
or why not (`RUNNING`, `DEFERRED`, `BUDGET`, `EXPIRED`, `DISABLED`). On `EVALUATE` choose an effective host decision through `assign`, reuse a still-valid choice with current evidence, or consult in the background with `strategic_advisor.py evaluate --campaign <DIR>` (opus, effort `high`, the existing
fallback if the account does not serve it, declared in `meta.json`). Evaluations are about four hours apart, earlier when a delivery, a closed mandate, a stalled mandate or a roadmap edit
anticipates one; the same events are never evaluated twice (a digest), an evaluation that is still running is not overlapped (process identity), and a session waiting for a CI run, a battery or
a delegate is not "stalled": only the mandate watch calls a mandate resumable, and recovery stays with it.

**A hold is not an evaluation (HE64, 2026-11-15).** The pending digest is consumed only when an evaluation completes, so a hold decided by hand re-fired `EVALUATE` at every recall. When the right choice is to wait, record it without a model run: `strategic_advisor.py hold --campaign <DIR> --reason "<why waiting is right>" --resume-when record:<TASK>=<STATE>` (or `path:<file>~<text>`; a time or `event` alone is refused, so a hold cannot become a timer for silence). It lists the events and commits it clears in `<DIR>/holds.jsonl` and `status`, spends no invocation and no budget, and ends at its `resume_when`, a roadmap change or the first NEW event. The tick then reports `HELD by host at <utc>: <reason>`.

**Assignments and their evidence.** `evaluate` saves the assessment verbatim and registers each complete draft as `<DIR>/assignments/ADV-nnn.md` (a block missing a required field, a key already
drafted or already named in a task record, and anything over the campaign's assignment budget are logged and refused). Then the session that holds the cron delivers: check the recipient is a live
named session (`claude agents --json`), send the pointer with the supported cross-session message (SendMessage), and record `strategic_advisor.py deliver --id ADV-nnn --state SENT --evidence <message id>`;
an unreachable recipient is recorded `UNREACHABLE` and stays an explicit residual (the assignment file is in the repository, and the hourly mandate watch and the recipients' own checks are the
existing retry). `status --campaign <DIR>` keeps four things apart: **drafted** (saved), **sent** (the channel accepted a message), **taken in charge** (its id is in a recipient's task record),
**executed** (a DONE step carries its id). None of them says the result was useful; that is judged against the continuation that would have happened anyway. Never write into a transcript to
simulate a message and never start a copy of a live session to make it resume.

**Budget, and what enforces it.** `activate` writes `<DIR>/budget.json` (24 hours, no renewal, at most three real strategic invocations in total, failed attempts and dialogue included, at most
three assignments, a turn limit of 20). *Code-enforced for runs launched through this tool:* the invocation total, the expiry, the assignment count, the disable flag, the turn limit (`claude -p` has
no turn-limit flag on this host, so the launcher stops the child it started and the attempt counts). *Procedural:* that the cron keeps running (it is session-only, fires only while the session is idle,
and expires after seven days) and that deliveries are made; the account's total consumption is not controlled by any of this. Exhausting this budget stops the Advisor's evaluations only; the
sessions' already authorised work continues.

**Who holds the presidio, and what survives.** The operator may host the recall in a dedicated session (`ADV`, ACTOR_ID `orchestrator`, a mandate of its own distinct from the IT Orchestrator's);
the evaluations are still run by `legend-strategic-advisor` in a separate read-only context, and the hosting session runs `tick`, starts `evaluate`, critically judges incoming signals and decisive premises, delivers scoped work and follows its result. Operational execution remains with the recipients; ADV is not an approval step. One campaign, one
state: run every command from the **primary checkout** (the campaign folder, `budget.json` and the counters are files there; the state directory is keyed by the campaign name; a linked worktree
holds its own copy, so `tick`, `evaluate`, `deliver`, `activate`, `disable` and `recall` refuse to run from one). Transfer = the new host reads the campaign and the state, the old host
`CronDelete`s only its Advisor recall (never another mandate's job), the new host creates its own with the text `strategic_advisor.py recall --campaign <DIR>` prints, and verifies its first fire.
**Restore on restart:** the recall lives in the session process's memory (CronCreate is session-only, `durable` has no effect, a recurring job expires after seven days). A compaction keeps the
process; a termination, a resume in a new process (the mandate watch's `claude --bg --resume` included) or the seven days drop it, and nothing restores it by itself. So the hosting session's
mandate record carries a standing first step: `CronList`; if no job's text contains `Proactive Strategic Advisor pilot, hourly mechanical check`, create it from `recall`; if one exists, create
nothing. Not verified here: that a compaction leaves the job in place (the campaign's first recall was created after one); this is an unresolved limit, not a guarantee.

**Strategic inputs.** `entrypoints` is the one index (no second registry). Its rows separate the operator roadmap, the dashboard and its source data, investigations and cards, open questions,
candidates, packages, diagnoses and DREAM (a connection DREAM proposes is a question, not evidence), the scientific radars, harness scouting, the capability surface, and the tools and cost
protocol. The harness-scouting weekly tables stop at their last week; the live feed is the daily scout's briefing in the host cache, which the advisor cannot reach, so the Stage P brief embeds
it (dated, shortened, addresses removed) as a feed of opportunities. Costs and unused-capability diagnoses exist as tools and per-invocation `meta.json`, not as a standing report: say so rather
than infer. A pointer that finds nothing or only old material is a visible limit in the assessment.

**Disable.** `strategic_advisor.py disable --campaign <DIR>` (or delete the cron with CronDelete, or write "stop" in the roadmap's instruction log): later ticks and runs refuse, and ordinary
scheduling, the mandate watch and the sessions' work are untouched. Remove the capability: delete the Stage P code paths, the roadmap section markers and the campaign folder; Stages A and B are independent of them.

## MEETING

**MEETING is part of the existing recall**, with its one rule in
[cross-session transport §13](../../../framework/protocols/cross_session_transport.md#13--meeting).
Inspect `tick.meeting` independently of the ordinary evaluation verdict. When actionable,
the hosting session opens/resumes `strategic_advisor.py meeting --campaign <DIR> --open`,
asks the live relevant participants for their prioritised deltas via SendMessage, and makes
source-backed decisions with Orchestrator at safe boundaries. An ordinary `NONE` does not
swallow a due alignment; a headless evaluation or a second cron is unnecessary. Record
actual replies, unavailable participants and assignments in closing notes, then
`meeting --campaign <DIR> --close <NOTES.md>`. Follow through with existing delivery/task
records; closing minutes alone is not delivery. A significant incoming request is registered
with `meeting --request <reason> --source <original pointer> --actor <participant role>`.
The agenda ADV brings is derived from the closing comparison of cross-session transport section 12 ("A local wait is not exhaustion"): consumed results and the decision they change, marginal value of the current thread against other roadmap opportunities, then an executable question for the effective recipient; blocked sources, a laboratory-dependent experiment or a benchmark that cannot be evaluated stop their own path only. It opens the first message to the participants and the closing notes.
Continuous mode defaults to six hours between meeting starts. Set `meeting_enabled: false`
in its existing CONTINUOUS.json to remove the periodic/event meeting path; ordinary research,
the portfolio and the Advisor's evaluations keep their existing behaviour.

## Living Research Portfolio

The permanent operational source is
[`research_portfolio.tsv`](../../../disease-models/wwox/research/drug_repurposing/research_portfolio.tsv),
linked from the roadmap's Work order. The canonical feeding/consultation habit lives in
[cross-session transport §12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity).
`strategic_advisor.py portfolio` prints its index; `portfolio --id RP-003` reads a whole row;
`portfolio --upsert /tmp/opportunity.json` merges a partial text-valued object by stable id,
preserving the other fields and rows. Writes use a host-local lock and atomic replacement;
use the primary checkout so writers share one file. No new service or approval is required.

`observe` reads the rows and derives execution from linked mandate records. A changed
opportunity/priority, released mandate needing consumption review or met dependency is a
portfolio event even without a radar; it survives a DEFERRED tick until evaluated. Editorial
timestamps and row ordering do not trigger an evaluation. The brief contains a compact index,
the permanent path and the update route. An optional `## Portfolio updates` fenced JSON list
in a saved assessment is applied by `evaluate`; malformed patches are reported and never
become a gate on scientific work. The read-only advisor itself still writes nothing.

An assignment is linked by `mandate_id` once taken in charge. Its execution status is derived,
not copied into this file. `done` records actual disposition/consumption; a released mandate
requests review rather than automatically marking an opportunity complete. New sources,
follow-up questions and priority changes keep feeding the same file. The supplied rows are
operator-requested research opportunities, not findings or proof that work has begun.

## Continuous operation (HE52, 2026-11-14)

A pilot is bounded by its own limits; continuous operation is the operator's persistent, revocable authorisation to continue inside the roadmap. They are two modes of one campaign, never two campaigns.

* **The mode is a small file**, `<campaign>/CONTINUOUS.json`, written by `strategic_advisor.py authorise-continuous --campaign <c> --source <where the operator's line is recorded>`. It keeps `budget.json`, the counters, the results and the failures exactly as they were (`pilot_at_authorisation` records them) and does not renew, reset or enlarge anything. `end-continuous --reason ...` (or deleting the file) returns to the bounded rules. `status` shows both: the pilot's ceilings against what was executed, and the continuous evaluations since the authorisation.
* **What binds in continuous mode:** the disable flag; an operator `PAUSE:`/`STOP:` line in the roadmap section whose scope is `all` or `advisor` (`RESUME:` lifts it; other scopes are shown to the evaluation and applied by their sessions); the Advisor's slice of the shared weekly allocation when the operator has stated the limit (`delegation_budget.md` section 10); the turn limit of one run; the tick's own rhythm (`min_hours_between`, `min_hours_anticipating`). A roadmap change evaluates at once; `URGENT:` and `INTEGRATION:` lines are carried to the evaluation.
* **What does not bind:** the pilot's expiry, its total of invocations, its per-stage ceilings, its assignment cap. An assignment that ends does not end the presidio.
* **`queue.exhausted` means no written executable step, not that the portfolio is exhausted.** A `hold` or a left-unrun `EVALUATE` names the excluded paths with their actual cause and a resume condition, and lapses at the ordinary cadence (cross-session transport section 12, "A local wait is not exhaustion").
* **Tick verdicts are observations, not proof that a wait is justified.** The `presidio` field shows the saved choice, its reason and resumption condition. Apply the canonical portfolio-selection rule before a whole-laboratory wait; an empty queue does not imply that useful work is exhausted. `PAUSED` (operator), `RESOURCES` (allocation), `DISABLED` and `EXPIRED`/`BUDGET` (bounded pilot) retain their meaning.
* **The presidio's own mandate record** keeps the standing objective open until the operator ends it. Choosing and preparing the next useful work is an executable step, not a `BLOCKED` wait for an operator line or an unowned delivery. A genuine whole-portfolio wait is `BLOCKED` with its actual cause and resumption condition. A future trial report is a separate step; its date does not block other objectives. Update obsolete blockers when results arrive rather than carrying closed dependencies forward.
* **After compaction, a restart or a lost recall:** the campaign, its state and the mode are on disk in the primary checkout, so nothing is lost with a session. The recall (a session-bound cron) is lost with the process; compaction keeps the process. Restore with `CronList` first and `strategic_advisor.py recall` only when no job carries the recall mark: one copy. A switched-off machine or a killed process cannot be recovered by any prompt: the next session that loads the mandate restores the recall. When this procedure or `recall_prompt` changes, compare the existing Advisor job with the current `strategic_advisor.py recall` text and replace only that job if it differs, preserving the hourly cadence and verifying one copy. Do not leave an older in-memory prompt as a second operating rule; campaign state, counters and history are not reset.
* **Radar items are opportunities, not orders:** compare each with the current thread, the other open questions, the promising comparisons, knowledge already held and concrete obstacles; read the originals for a substantial decision; adopt a principle in a few lines before installing a capability. "Already covered", "not useful" and "no difference" are valid outcomes.

* **Wake-up durability (operator, 2026-11-18, permanent):** the presidio's scheduling and recovery belong to this campaign and to the ADV **host** session, never to the read-only analyst and never to a new
  operator prompt. The operating rule (the chain cron -> revival -> one restored recall -> day-5 renewal, work registered with `mandate_continuity.py accept`, authorised `rebind`, `DUPLICATE_HOST`, the exact
  limits) lives once in [cross-session transport §12](../../../framework/protocols/cross_session_transport.md#wake-up-durability-the-presidio-belongs-to-the-adv-campaign-not-to-a-chat-operator-2026-11-18-permanent); after a revival or a substitution run CronList first and create the recall only if no job carries its mark, then `strategic_advisor.py recall-armed`.

## Follow-through during waits (HE54, 2026-11-14)

The rule lives once, in [cross-session transport §12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity) ("A wait is a moment to anticipate useful work"). Here: `tick` returns `waiting_on` (the blockers named in the open records, one cheap read) and a NEW wait is an event, evaluated at the ordinary rhythm and grouped; a standing wait is not re-evaluated. The evaluation brief carries `waits` and the follow-through paragraph; an assignment may add the optional lines `mode` (independent | queued | conditional), `start_condition`, `interferes_with`, `obsolete_if`. The presidio delivers an authorised draft in the turn that reads it. A queued assignment is a `BLOCKED` step with `unblock_when` in the recipient's record; superseding it is a `DONE` step whose evidence says why. The pilot's assignment cap does not apply in continuous operation.

## What comes next when the queue is empty (HE57, 2026-11-14)

The rule lives once, in [cross-session transport §12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity) ("Continuity is a choice of what comes next"). Here: the evaluation ends with an `## Outcome` block (`outcome`, `excluded`, `reason`, `resume_when`) that `evaluate` stores in the host state as `last_outcome`, with `unstated_streak` counting consecutive evaluations that left none. In continuous mode `tick` (a) resumes a stated wait when its `resume_when` is met (`record:<TASK_ID>=<STATE>`, `path:<file>[~<text>]`, `after:<UTC>`, read by the continuity module's own `unblock_met`); (b) asks for ONE evaluation when the last one left no outcome, nothing executable remains (`queue.exhausted`: no non-sender record in CONTINUE) and `min_hours_between` has passed, and not again until an outcome is stated; (c) leaves a stated wait or choice alone, and shows it in `presidio` (`WAITING (motivated)` with the excluded alternatives, the reason and the resume condition). A wait already over when it is stated, a `resume_when` the tool cannot read, or a `record:` id that does not exist (P8 wrote one the recipient had not created yet), is stored as `event` with the problem named, so it cannot loop or strand the wait; `resume_when` is read only for a wait. A run the runtime cut short by a refusal fallback after fewer than `MIN_CALLS_AFTER_FALLBACK` (8) tool calls is INCOMPLETE (`incomplete_run`; P11, 4 calls, believed a delivered result was still in flight): `evaluate` takes no assignment, portfolio update or outcome from it, keeps the triggers pending, stores `last_incomplete` and `tick` shows it; P10 had the same fallback with 17 calls and is used. The advisor's own writes (P<n>/, assignments, invocation log) and the sender records are not events (`_own_updates`; a recipient's result file in the campaign folder still is). Limit: the tick shows the plumbing; that a model writes the block and ranks the portfolio well is not demonstrated by it. Remove: delete the `last_outcome` branch of `tick`, `parse_outcome`/`resume_met` and the brief's `## Portfolio selection`; the pilot's behaviour does not depend on them.


**Host follow-through (operator correction, 2026-11-15).** Apply the source rule in
cross-session transport section 12, "Strategic synthesis is executable work". On `EVALUATE`,
run the pending evaluation or record a current, source-backed reason it is already superseded;
"no new radar" or a review hours away is not that reason. If a useful direction remains broad,
prepare a scoped planning/research assignment to the Orchestrator rather than requiring a
ready-made task from the operator. Keep a pipeline of questions, not a fixed count of launches.
Read relevant current recipient records; the brief now carries their verdicts and paths beside
the historical transport levels and chooses the previous assessment by numeric invocation order.
A tick detects an outcome left by a historically incomplete run, preserves it as
`last_invalidated_outcome`, removes its scheduling effect and requests a replacement evaluation
within existing permissions. Assessments and failures remain intact. This also repairs P11's
old wait after deployment; no manual edit of a transcript or second scheduler is involved.


A clinical-coverage audit does not dispose of mechanistic discovery. If a result leaves
unread oncology/structural sources or PMC identifiers, reconcile actual access and reading
state, then select a mechanism-first discovery case or ask Orchestrator to select it. An
existing INV/open-question citation is not a prerequisite for a new question. The full rule
and source-parity reference live in cross-session transport section 12; no new screening gate,
reading quota or mandatory adoption is added.


**Incoming signals are work to judge, not mail to file.** Apply cross-session transport section 12,
"Route useful signals" to both the hosting session and the read-only assessment. A radar's Plan
addressee or lack of an imperative to ADV does not dispose of it. Read relevant originals, compare
with existing assignments, and make a reasoned disposition. A useful Harness question goes to the
live Harness recipient; a research question goes to Orchestrator/Science under existing ownership.
Notify with a durable pointer and the bounded question, record transport using the existing route,
and follow the response; do not claim an archive or RP link is a send. Use the existing source
entry points, including full operator radar reports beside their audit notes, not only their README.
Producers' handoff text is helpful; the standing rule does not depend on that text being present.


**Evaluation cadence (2026-11-15).** The interval is measured from the evaluation start,
not its completion: a run's duration must not make the next hourly recall miss eligibility by
seconds and defer it for another hour. `last_evaluation_utc` keeps the historical completion;
`last_evaluation_started_utc` is recorded separately. Legacy start time is recovered only from
matching runtime metadata; if unavailable, the tool declares its completion-time fallback.
`DEFERRED` names the actual next eligible time rather than claiming an anticipating event is absent.
No new timer, overlapping evaluation, budget renewal or periodic model call is added.

Deferred observations remain in the existing `pending_events`/`pending_commits` until an
evaluation consumes them, even when no new radar or commit arrives. A tick during a running
evaluation leaves its observation baseline unchanged, so later deliveries reach the next run.
This reuses the existing state and digest; it adds no queue, scheduler or forced model launch.


**A completed choice is not perpetual activity (continuous mode).** With no executable recipient
work, pending delivery/mandate/portfolio signals can request a strategic evaluation without the
ordinary coalescing interval. The single recall, duplicate digest, running check, real allocation
and operator controls still apply; the tick itself launches no model. With no new signal, a
previous `continue`, `switch`, `assign` or `queue` is revisited at the configured ordinary cadence
when its executable queue is empty. A supported stated `wait` retains its real resumption
condition. Thus next-work selection does not depend on a new radar, delivery or operator prompt,
and the bounded pilot does not acquire these continuous-mode launches. Reassessment is a choice
of useful work or a supported wait, never a duty to invent work.

The evaluation consumes its own advisory portfolio patches; they are not new evidence for
another evaluation. If the shared portfolio changed during the read, keep the old observation
digest so the external change remains a signal. This protects continuity from self-generated
busy work while preserving real recipient results and external inputs.

## Autonomous scientific leadership and urgency (operator, 2026-11-18, permanent)

The rule lives once, in [cross-session transport §12](../../../framework/protocols/cross_session_transport.md#12--autonomous-mandate-continuity) ("Autonomous scientific leadership and urgency"), and its source is the 2026-11-18 entry of `roadmap_current.md`. Here only what changes the consultation: the operator is a boost, not a dependency, so a report to the operator is never a reason to wait; at a consumed delivery or a weakened candidate the host runs the candidate-to-candidate loop; and a recommendation that one candidate is "more promising" than another must say for which endpoint, model, phase of development, mechanism and level of evidence (acute, chronic seizure control and development are different; tolerability or an elegant rationale is not efficacy). The analyst is asked for that comparison when the host cannot judge it alone.

## Monitor and help (operator, 2026-11-15, permanent)

The rule lives once, in cross-session transport section 12 ("Monitor and help; do not only direct"). Here: at every recall and every delivery read `tick`'s `activity` block (session status, minutes quiet, idle share, minutes since the last commit on `main`) with the open records and their awaited events, not the verdict alone. An idle share above half without a written reason is a prompt to send. Help a stuck session by finding what blocks it and supplying or routing the input; correct your own premise first; never take over the recipient's method. Address a role only after `mandate_watch.py route --to <role>` resolves it; for an unresolved role (Mirror today) say so and keep a conditional request in the portfolio.
