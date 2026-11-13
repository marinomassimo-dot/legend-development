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

**What it is.** The operator's roadmap (the marked section at the top of `disease-models/wwox/research/drug_repurposing/roadmap_current.md`) defines the mission and the priorities; the
dashboard, the open questions, DREAM and the radar help the Advisor choose how to pursue them. Without waiting to be asked it observes the laboratory, compares directions, and may draft
assignments (`### ASSIGNMENT` blocks) for the Orchestrator, Science or Harness. A new operator line in the roadmap prevails over any automatic plan and triggers a re-evaluation. The Advisor
cannot change a conclusion, ranking or qualification, and has no new mission or budget of its own.

**The two levels, one schedule.** An hourly in-session cron (the one scheduling mechanism a live session can use and the one that can also *deliver*: the host crontab already runs the mandate watch
and is not repeated) runs `python3 framework/scripts/strategic_advisor.py tick --campaign <DIR>`. `tick` is mechanical and makes no model call: it reads the roadmap digest, the commits of `main`
since the last tick, the task records, the mandate watch's own event log and the runtime's list of sessions, and answers `NONE` (nothing new: the previous assessment stands), `EVALUATE`,
or why not (`RUNNING`, `DEFERRED`, `BUDGET`, `EXPIRED`, `DISABLED`). On `EVALUATE` run, in the background, `strategic_advisor.py evaluate --campaign <DIR>` (opus, effort `high`, the existing
fallback if the account does not serve it, declared in `meta.json`). Evaluations are about four hours apart, earlier when a delivery, a closed mandate, a stalled mandate or a roadmap edit
anticipates one; the same events are never evaluated twice (a digest), an evaluation that is still running is not overlapped (process identity), and a session waiting for a CI run, a battery or
a delegate is not "stalled": only the mandate watch calls a mandate resumable, and recovery stays with it.

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
the evaluations are still run by `legend-strategic-advisor` in a separate read-only context, and the hosting session only runs `tick`, starts `evaluate`, delivers and records. One campaign, one
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
