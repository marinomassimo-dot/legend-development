# Strategic Advisor — Phase 1 build report

Harness Engineering (ACTOR_ID `plan`). Mandate record `ledger/tasks/plan/PLAN-STRATEGIC-ADVISOR-PHASE1-20261112.json`.
Phase 2 (the bounded research pilot) belongs to the active main Orchestrator and is not run here; its brief is `PILOT_MANDATE.md` in this folder.
Four things are kept apart throughout: **configured** (the files exist and route), **invoked** (a run returned an assessment), **consumed** (the Orchestrator acted on it) and **beneficial** (the outcome was better). Phase 1 shows the first two for a trivial task. It shows nothing about the last two.

## 1 · What was built

| Component | Path | Owns |
|---|---|---|
| Agent definition | `.claude/agents/legend-strategic-advisor.md` | the advisory reasoning (Appendix A distilled, about 870 words including the header); tools `Read, Glob, Grep, WebFetch` |
| Procedure | `.claude/skills/legend-strategic-advisor/SKILL.md` | triggers, Stage A / Stage B steps, capture order, limits, removal |
| Plumbing | `framework/scripts/strategic_advisor.py` (+ `test_strategic_advisor.py`, 17 tests) | the entry map (one home), snapshot, neutral brief, read-only launch, capture, attempt log, check |
| Build evidence | this folder: `smoke/` (brief, `S1/`, `S2/`, `invocations.jsonl`, a sealed canary) | the smoke record |

No ACTOR_ID, scheduler, hook, gate or approval was added, and `LEGEND_CORE`, the canonical invariants and the settings files are unchanged.

**Routing changes (all of them).** `CLAUDE.md` section 2 (one optional row and the note under the table); `SKILLS.md` (one row, the count); `ARCHITECTURE.md` (one row); `FAQ.md`, `CITATION.cff` and `framework/ADOPTING.md` (the skill count, which `scripts/test_skill_packages.py` pins; its `EXPECTED_COUNT` is 25); `framework/config/fulltext_route_registry.json` (two lines); `framework/scripts/README.md` (one tool row); `roles/orchestrator.md` (one paragraph, "An optional second view"). The orchestrator governance fingerprint changes with that paragraph; `governance/scripts/test_governance_fingerprint.py` passes.

## 2 · Mechanisms reused

The per-turn model and effort read-back is `session_model_census.census`, applied to the advisor's own persisted session transcript. Test discovery, the route registry, the tool-routing and skill-package suites, the mandate record schema and the release battery are the existing ones. Transport is the existing cross-session transport; nothing new was added for delivery. One small function is new, `extract_transcript`, for a demonstrated gap: no existing script extracts a run's final answer from a transcript (delegate reports "live only in transcripts" in the memory note on subagent transcripts), and it also supplies the fidelity cross-check.

## 3 · Mechanical guarantees and procedural limits

| Claim | Status | How known |
|---|---|---|
| The advisor was born with exactly `Read, Glob, Grep, WebFetch`, no MCP server | mechanical, read back | the runtime init event of the smoke: `tools` and `mcp_servers` |
| A read of the sealed folder is refused | mechanical, measured once | deny rule `Read(**/advisor_sealed/**)`: both the Read and the Grep on the canary returned a permission refusal in the smoke |
| Reads outside the working directory and the added memory directory | runtime default under `dontAsk`, **not tested** | no allow rule covers them; not exercised |
| The saved assessment is the runtime's result event, verbatim | mechanical | `meta.json` digest; `check` re-verifies; for S2 it also equals the last assistant text of the persisted session transcript |
| Model and effort | read back, per turn | S2: every assistant turn ran `claude-opus-5-5`; the transcript rows carry effort `high` |
| Attempt ceilings (2 Stage A, 2 Stage B, 1 smoke) | **procedural**: enforced only for runs launched through this tool, which counts failed attempts too | `claude` called directly bypasses it; one recorded extra attempt is allowed after a failure |
| Duplicate avoidance, "do not invoke on every commit" | **procedural**: the skill says when; `snapshot` lets a caller compare | nothing prevents an invocation |
| The advisor follows its brief, reports truthfully what it read, forms a view before seeing a plan | **not enforced, not shown** | `check` compares its own list of inspected files with the recorded tool calls only for the sealed path |
| Isolation | partial, see section 5 | a fresh process has no parent chat; it does inherit project instructions and the memory index |

## 4 · The smoke record

Two attempts, both counted (ceiling: one smoke, so S2 is a recorded extra attempt).

* **S1** (16:50 UTC): refused at launch, before any model call, with `--agent 'legend-strategic-advisor' not found`. Cause, measured afterwards with a deliberately nonexistent agent name (which costs no model call): `--restricted` removes the project agents from the available list; with each other flag the agent is listed. The flag was removed. No tokens were spent.
* **S2** (16:51 UTC, about 10 s): Stage A profile, `--model opus --effort high`. Read `framework/protocols/delegation_budget.md`, quoted its heading and the concurrency sentence correctly, reported both sealed-folder attempts as refused, listed exactly the four tools. Read back: model `claude-opus-5-5` on both assistant turns (the alias `opus` resolved without new spend, `apiKeySource` none); output 868 tokens, cache creation 18,695, cache read 14,280, first-turn context 14,282 tokens; a secondary `claude-haiku-5-5` call of 1,461 input and 179 output tokens appears in the usage block and was not requested by the advisor. The runtime reports a list-price figure of about 0.17 for the run; that is an estimate on the existing logged-in account, not an invoice.
* **Capture:** method "runtime result event (stream-json), saved verbatim"; `transcript_cross_check` true; raw stream kept locally and not published; `check` passes.

The Stage A profile was exercised. **The Stage B profile (`sonnet`, `medium`) was not**: the same command line with another alias, never run. The final agent definition differs from the one the smoke ran against by one added sentence (do not put identifiers in a fetch); no tool or flag changed.

## 5 · Runtime findings that bind the use

1. **A new agent file is seen only by a new process.** A fresh `claude -p` lists it; an already-running session does not. The primary path is therefore the headless run in `strategic_advisor.py run`, which works from a running Orchestrator session. The in-session Agent-tool path (`subagent_type`) needs a session started after this lands and **was not exercised**.
2. **Inherited context.** The smoke transcript shows the advisor received the user-level instructions (238 characters), the project `CLAUDE.md` (about 12,000) and the memory index (about 8,500), plus the account email in the session context. It had no parent conversation. Treat it as informed by the project's rules and by the operator's memory index, and as not blind to either. The definition forbids putting identifiers in a fetch.
3. **Dashboard access.** A fetch of the public page returns the rendered text, not a shell: 617,476 characters, readable in pages of 100,000, with no build date on the page. The source revision comes from the repository (`snapshot` reports the package manifest digest and last commit). The live page's publication date was not checked.
4. **No shell means no registry tool.** The advisor cannot run `registry_records.py`; its definition tells it to find a record by line with Grep and read the whole block with Read.
5. The headless call does not use `--bare` (that needs an API key and would be new spend).

## 6 · Using it

`.claude/skills/legend-strategic-advisor/SKILL.md` is the procedure. The Orchestrator seals its intended action, builds the Stage A brief from a mission file and a constraints file (no preferred plan), runs it in the background, reads `A<n>/assessment.md`, builds the Stage B brief from the saved Stage A and the sealed action, runs it, decides, and records why. Output lands in the campaign folder the caller chooses under its own task or research package.

## 7 · Disable or remove

Stop calling it: nothing depends on it, and `test_no_other_script_imports_the_advisor_tool` pins that. To remove it, delete the agent file, the skill folder, `strategic_advisor.py` and its test, this folder, then revert the routing lines listed in section 1 (the skill count goes back to 24). Landing and removal were each checked against the quick suites that pin counts and routing.

## 8 · Not shown

That the advisor improves strategy; that Stage A is formed before a plan is known when the Orchestrator's preferences are readable elsewhere in the repository (the sealed folder covers only the text placed there); that Grep and Glob refusals hold for every path form (one Grep was tested); that the Stage B profile runs; that the Agent-tool path runs; that a long assessment is captured as faithfully as a short one (the code path is the same). A negative control for obedience does not exist.
