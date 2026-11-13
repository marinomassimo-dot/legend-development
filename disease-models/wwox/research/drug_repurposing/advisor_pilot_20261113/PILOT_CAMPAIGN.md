# Proactive Strategic Advisor: pilot campaign (handoff to the Orchestrator)

Non-canonical working note. Task record `ledger/tasks/plan/PLAN-PROACTIVE-ADVISOR-20261113.json`. The campaign is authorised by the operator's prompt of 2026-11-13; Harness delivers it here and the Orchestrator owns its operational coordination.

## What is authorised
24 hours from the effective activation recorded in `budget.json`, no automatic renewal. At most **three** real strategic invocations in total (dialogue and failed attempts included) and at most **three** new executive assignments across the three sessions; no recursive delegation; no external spend and no new service. These are ceilings, not targets: a continuation of the current plan, with its reason, is a valid decision, and nothing is to be invented to complete a sequence. Exhausting the Advisor's budget stops its evaluations only; your work already authorised goes on.

**Amendment 2026-11-13 (operator, night mission; current limits).** The totals are now **five** real strategic invocations and **six** executive assignments, counting everything already used (2 invocations and 3 assignments before the amendment), failed attempts included; at most 20 turns per invocation; no new service, purchase or external spend; the original expiry is unchanged and there is no renewal; the ten-hour autonomy window (to 2026-11-14T09:33Z) is procedural. The record is `budget.json` `amendments`; the "three" above and the 3/3 of the first period are historical. The campaign was not reactivated and no counter was reset.

## The mission it works from
The operator's roadmap: the marked section at the top of `disease-models/wwox/research/drug_repurposing/roadmap_current.md` (mission, five priorities, exploration allowed, exclusions, pilot budget, a dated log of the operator's instructions). A new line there prevails over any automatic plan and triggers a re-evaluation; "stop" or "pause" suspends the pilot. The dashboard, the open questions, DREAM and the radar are tools the Advisor uses to choose how to pursue those priorities; they are not a second plan.

## What reaches you and how
* An hourly mechanical check (`strategic_advisor.py tick`, no model call) reads the roadmap digest, the commits of `main`, the task records (through the continuity module), the mandate watch's event log and the list of sessions. About every four hours, earlier when a delivery, a closed or stalled mandate or a roadmap edit anticipates it, it runs one strategic evaluation (Stage P, opus, effort high, at most 20 turns, read-only). When nothing decision-relevant changed it reuses the previous assessment.
* An evaluation may draft assignments (`ADV-001`..) in `advisor_pilot_20261113/assignments/`, each with: the question, why now, the roadmap link, related active work, the original sources to read, the decision a result would change, perimeter and budget, your methodological autonomy (rival explanations, better methods and negative results welcome), who receives the result and which consumers to update, and what was searched to avoid duplicating assigned or consumed work.
* The session that runs the schedule (Harness) delivers a pointer with the supported cross-session message and records it (`deliver --state SENT`). Sent is not taken in charge.
* **You record taking each in charge in your own task record, with its id (`ADV-nnn`)**: that is the evidence the Advisor looks for. You may adapt its order or method for dependencies, resources or overlap, writing the reason; no further approval is needed inside the campaign. You may also defer it with a reason and a revival condition. An operator instruction to stop or suspend keeps its precedence.
* `strategic_advisor.py status --campaign advisor_pilot_20261113` keeps apart: drafted, sent, taken in charge, executed. None of them says the result was useful.

## What stays unchanged
No recommendation changes a scientific conclusion, ranking, need direction or candidate state by itself; a candidate under verification is not modified by an assignment; the Advisor reads complete originals for any substantive assessment and keeps announced, in-snapshot and actually-read material apart.

## What you owe back
The pilot report (yours): which decisions and research cycles advanced without a new operator prompt, and with what observable benefit; the usefulness of each decision against the continuation that would have happened anyway; duplicated or superfluous work avoided; any interference or slowdown introduced; ordinary interventions asked of the operator; the actual cost (model, effort, turns, output and cache from `meta.json`; subscription use, not money). The success criterion is a strategic choice derived from the roadmap, an assignment actually taken in charge, a returned and consumed result, and a later autonomous re-evaluation: if there are no new inputs or opportunities, say so.

## Turning it off
`python3 framework/scripts/strategic_advisor.py disable --campaign disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113` (or CronDelete the hourly job, or write "stop" in the roadmap log). Ordinary scheduling, the mandate watch and your work are untouched.
