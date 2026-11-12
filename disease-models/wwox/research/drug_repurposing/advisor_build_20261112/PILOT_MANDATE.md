# LEGEND — Strategic Advisor Pilot Mandate

Recipient: the active main Orchestrator

Delivery note:
If this brief is being read by Harness Engineering, complete the factual Implementation Handoff section and deliver it to the active main Orchestrator. Do not assume its role or execute this pilot yourself.

Repository: https://github.com/marinomassimo-dot/legend-development
Workspace: /home/desktop/legend-development

Start after the implementation handoff and at a safe boundary of ongoing work.

## IMPLEMENTATION HANDOFF — COMPLETED BY HARNESS

Written by Harness Engineering (ACTOR_ID `plan`), task `PLAN-STRATEGIC-ADVISOR-PHASE1-20261112`. Facts only; the build report with evidence is [`README.md`](README.md) in this folder.

* **Invocation procedure:** `.claude/skills/legend-strategic-advisor/SKILL.md`, with `framework/scripts/strategic_advisor.py` for snapshot, brief, launch, capture, attempt log and check.
* **Agent definition:** `.claude/agents/legend-strategic-advisor.md`.
* **Verified build SHA:** see the line `BUILD_SHA` at the end of this file. It is written after landing, because a file cannot name the commit that contains it. The smoke ran against an earlier commit of the same branch; the only later change to the agent is one added sentence.
* **Resolved model configuration.** Stage A: alias `opus`, effort `high`; resolved and read back as `claude-opus-5-5` on every assistant turn in the smoke, without new spend. Fallback if it ever stops resolving: `sonnet`, `high`, disclosed. Stage B: `sonnet`, effort `medium`; the alias and effort are passed the same way, **but this profile was not exercised**.
* **Smoke result.** Two attempts were made, both counted: S1 was refused at launch before any model call (`--restricted` hides the project agents; flag removed); S2 succeeded. S2 read one public file correctly, reported both sealed-folder access attempts as refused, and listed exactly the four tools. Cost: 868 output tokens and 14,282 first-turn context tokens on opus, plus a 1,640-token secondary haiku call. Records: `smoke/` in this folder.
* **Assessment capture method.** The headless run's own result event, saved verbatim as `A<n>/assessment.md` or `B<n>/assessment.md` with `meta.json` (digests, model per turn, tool calls). For S2 the saved text also equals the last assistant text of the persisted session transcript. The raw stream and transcript stay local and are not published. Not caller transcription.
* **Mechanically verified restrictions.** The advisor was born with exactly `Read, Glob, Grep, WebFetch` and no MCP server (runtime init event). A Read and a Grep on the sealed folder were refused by the runtime.
* **Procedural or unverified limits.**
  * Ceilings (2 Stage A, 2 Stage B) bind only runs launched through `strategic_advisor.py`; direct `claude` calls bypass them. One recorded extra attempt is allowed only after a failure.
  * Nothing prevents invoking on every heartbeat; the skill states when not to.
  * The advisor inherits the project instructions, the memory index and the account email; it has no parent conversation. It is not blind to the repository: the sealed folder hides only the text placed in it. Say what the advisor saw in its "Freshness and exposure" section; do not claim blindness.
  * The Agent-tool path (`subagent_type`) is invisible to an already-running session and was not exercised. Use the headless path in the skill.
  * That the advisor forms a view before a plan is known, reads complete originals, or reports truthfully what it opened is not enforced.
  * A fetch of the public dashboard returns rendered text (about 617,000 characters, 100,000 per call) with no build date; use the repository records for fact.
  * The Stage B profile and long-assessment capture have not been run.

## PILOT MANDATE

Do not alter the mandate below.

Objective:
Select and execute two bounded research increments that improve WWOX loss-of-function drug-repurposing generation or prioritization.

Compare further investment in a current branch with other existing investigations or open questions. Return results to actual research and drug-repurposing consumers.

Scope:
Current WWOX investigations, candidates, open questions and existing capabilities. Each increment has one principal question. Supporting harness work must address a concrete obstacle to that question.

Exclusions:
No clinical treatment recommendation, patient-level analysis, gene-therapy development, business activity, external outreach, paid service or broad infrastructure redesign.

Time boundary:
At most 24 hours from the first Stage A dispatch. Finish earlier when the two increments and their evidence report are complete. Do not renew the window automatically.

Advisory resource ceiling:
At most two Stage A assessments and two Stage B responses, in addition to the single smoke invocation already authorized to Harness.

Use the resolved model configuration from the handoff. No silent escalation, recursive delegation or new external spending.

Technical failures still consume resources. Do not create unlimited replacement attempts.

Scientific delegation follows existing discipline and budgets. Reuse valid work rather than launching agents automatically.

Reserved decisions:
Exactly those in the canonical authority rules. This pilot creates no additional approval requirement.

### BEFORE EACH STAGE A

Record in the existing task:
- campaign start and end boundary;
- owner session;
- repository SHA and dispatch time;
- relevant uncommitted inputs, if any;
- dashboard build date or source revision, when available;
- current scientific baseline;
- the next action you would take without the new assessment;
- material constraints and dependencies.

Do this before both Stage A assessments, not only the first.

Keep your preferred next action out of Stage A's initial brief.

Supply the neutral source entry points through the delivered procedure. The advisor chooses relevant material to inspect.

Verify mandate–session binding and use existing continuity mechanisms.

### EVALUATION CRITERIA — FIX BEFORE EXECUTION

Useful difference may include:
- avoiding duplicated work;
- selecting a more decisive question;
- improving a discriminating experiment;
- making unused knowledge act in a consumer;
- choosing another branch for an evidence-supported reason.

No demonstrated difference includes:
- the same action and result without an evidenced improvement;
- an assessment not consumed;
- additional explanation without a useful operational effect.

Harm may include:
- a false premise affecting the choice;
- duplicated or interrupted work;
- scope expansion;
- lost evidence;
- improper scientific or ranking changes;
- blocked ordinary work;
- disproportionate resource use.

A negative or inconclusive scientific result can be useful. A persuasive strategic report alone is not evidence of benefit.

For each criterion, preserve the observations and source pointers supporting the assessment. Do not use the engine's own labels as independent truth.

Record human interventions after the pilot starts, distinguishing optional steering from intervention required to continue.

### EXECUTION

1. Invoke Stage A and preserve the complete returned assessment through the supported capture path.
2. Invoke Stage B separately with Stage A, your previously recorded intended action and operational constraints.
3. Choose the bounded work and record why the recommendation was accepted, adapted or rejected.
4. Execute under existing scientific standards.
5. Consume the result into the affected investigation, question, comparison, generator or candidate record.
6. Before the second Stage A, record your updated intended next action independently.
7. Complete the second increment and its consumer update.

Continuing the same branch can be justified. Do not force redirection or manufacture a favorable candidate.

Do not generate three new assignments automatically.

An advisor assessment is not scientific validation. New scientific premises require the existing evidence and review process.

### BOUNDARIES AND STEERING

At the time or invocation boundary, do not open another increment.

Preserve unfinished work and open scientific questions accurately. Do not label them scientifically resolved because the pilot window ended.

The main Orchestrator session and current task record are the normal steering path. Explicit operator instructions received elsewhere remain valid under existing precedence and must be reconciled.

If the advisor is unavailable, continue useful authorized work where possible and record the missing contribution. Do not duplicate sessions or invent approval requirements.

If a reversible addition is causing operational harm, use existing authority to contain or disable it; do not wait for the periodic review to prevent further harm.

### FINAL CAMPAIGN EVIDENCE REPORT

Report in Italian:
- what changed;
- why directions were chosen;
- intended actions recorded before each assessment;
- alternatives not pursued;
- results that changed the plan;
- exact consumers updated;
- measured advisory and scientific resource use;
- human interventions;
- evidence for useful difference, no difference or harm;
- remaining directions;
- actual limits of autonomy demonstrated.

You may provide a clearly labeled provisional assessment. Do not present self-evaluation as independent validation.

Periodic operator and cross-model review may confirm or revise the assessment and judge whether to keep, revise or remove the addition.

That review is not an approval prerequisite for completing the evidence report or continuing other already authorized work.

Keep configured capability, successful invocation, consumed advice and improved outcome separate.

Do not launch a 72-hour campaign automatically.

BUILD_SHA: 4633abf7e18b65be0b51dde8c5dc47c89de6872e (integration and publication commit on the development repository's main; publication gate PASS, verified by ls-remote)
BUILD_VERIFICATION: release battery on candidate 2513fe1fb7552058681a64e4d535677a00e38776 gave FAIL on two suites, both red on the base main without this change (the ranking regeneration check, fixed on main by another session; four browser tests, because the host's Chromium snap refresh needs a newer C library). Targeted reruns passed: the view suite (221 tests) with the older Chromium revision, the ranking suite after merging the fix, the advisor suite (17 tests), and the quick pre-freeze suites. No full battery was rerun on the landed SHA.
