---
name: legend-strategic-advisor
description: Optional strategic perspective for the Orchestrator. Calls the read-only legend-strategic-advisor twice, Stage A (independent assessment, no preferred plan) then Stage B (dialogue on the Orchestrator's intended action), saves each complete assessment, and returns it to the planning loop. Use at campaign start, after an operational increment, or when a material result changes a candidate, premise or research decision. Advisory only; gates nothing.
---

# legend-strategic-advisor — a second, separate view on what to invest in next

An **optional** consultation. It gates nothing, approves nothing and assigns nothing; the Orchestrator
decides after reading it, and the ordinary research loop runs the same without it. The reasoning is in
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
   `python3 framework/scripts/strategic_advisor.py brief --stage A --campaign <DIR> --mission-file <F> --constraints-file <F> --task-record <PATH>`
3. Run it in the background (it can take tens of minutes):
   `python3 framework/scripts/strategic_advisor.py run --stage A --campaign <DIR> --brief <DIR>/brief_A.md --model opus --effort high`
   Use `opus` only if the account serves it without new spend; otherwise `sonnet` + `high`, and say it was
   a fallback. A model flag is a request: read the model back from `A<n>/meta.json`.
4. The complete assessment is `A<n>/assessment.md`: the runtime result event, saved verbatim, with
   `meta.json` (tools the advisor was born with, model per turn, files it opened, usage, digests).
   Persist it **before** summarising or acting. Never retype it. If the run fails, the attempt still counts.

## Stage B — dialogue

`brief --stage B --campaign <DIR> --assessment <DIR>/A<n>/assessment.md --sealed-intended <DIR>/advisor_sealed/INTENDED_ACTION_<N>.md --constraints-file <F>`, then
`run --stage B … --model sonnet --effort medium`. It is a second, fresh invocation that reads the saved Stage A
in full; no live continuation is assumed. Decide, and record why the advice was accepted, adapted or rejected.
Consensus is not required.

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
* **Dashboard:** a plain page fetch returns the rendered text in 100,000-character pages, with no build stamp. Use
  the repository records for fact and the page for presentation.
* The Agent-tool path (`subagent_type: legend-strategic-advisor`) works only in a session started after the
  agent file landed; an already-running session does not see it.

## Disable or remove

Disable: stop calling it; nothing depends on it. Remove: delete `.claude/agents/legend-strategic-advisor.md`, this
folder, `framework/scripts/strategic_advisor.py` and its test, the row in `framework/scripts/README.md`, the
`run_release_regressions.py` entry, the route-registry lines, and the router rows in `CLAUDE.md` §2 and `SKILLS.md`.
