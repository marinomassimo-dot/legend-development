# Strategic Advisor brief — Stage P (proactive evaluation)

## Snapshot
- Repository SHA: `dbf00b732691606ed046538c51f43e5df9feb8b4` (branch `main`)
- Dispatch time (UTC): 2026-11-13T21:15:02Z
- Uncommitted paths: none
- Dashboard: https://marinomassimo-dot.github.io/legend-development/ · source revision dbf00b732691606ed046538c51f43e5df9feb8b4 2026-11-13T20:53:38+00:00 · the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.

## Operator roadmap (authoritative; operator instructions prevail over any automatic plan)
**Mission.** Improve LEGEND's ability to turn verifiable scientific knowledge into more useful pharmacological hypotheses, comparisons and experiments for WWOX loss of function, keeping the
return from open questions to research active.

**Current priorities** (revisable; a reasoned proposal to change them is allowed, a silent change is not):
1. Finish consuming the scientific and Harness deliveries already available, including the SCI51 corrections, keeping results, limits and work actually done apart.
2. Find where knowledge already held can produce a better pharmacological comparison, conditional hypothesis or experiment.
3. Compare going deeper on the current thread with the other prioritised questions of the module, by marginal benefit, cost and concrete chance of progress. The newest thread earns no priority by being newest; the EBP connections from SCI51 are an opportunity to compare, not a direction already imposed.
4. Assess Harness micro-upgrades when they unblock a scientific capability, remove useless work or improve the use of the tools already available.
5. Keep the dashboard as the map of research opportunities, correct and readable.

**Exploration allowed.** Anything inside the mission that uses material already in the repository or public, free sources: reading, extraction, comparison, conditional hypotheses, experiment designs, tool and identity work.

**Exclusions.** Clinical recommendations, doses, gene-therapy development, individual or private data, external contacts, new paid services, infrastructure growth without a concrete need.

**Pilot campaign** (first Proactive Strategic Advisor pilot): 24 hours from its effective activation (`advisor_pilot_20261113/budget.json`), no automatic renewal; at most three real strategic
invocations in total (dialogue and failed attempts included), at most three new executive assignments across the three sessions, no recursive delegation, no external spend. These are ceilings,
not targets. Exhausting the Advisor's budget stops its evaluations only; the work already authorised to the sessions goes on.

**Recent operator instructions** (newest first; add a dated line to change direction, or write "stop" or "pause" to suspend the pilot):
- 2026-11-13: the roadmap above; the Advisor may act without being asked, the Orchestrator keeps operational coordination; the operator can intervene at any time by editing this section.

## Campaign limits
{"expires_utc": "2026-11-14T18:22:36Z", "max_assignments": 3, "max_invocations": 3, "turn_limit": 20}

## Observed state (mechanical, this tick)
{
 "events": [],
 "open_mandates": [
  "INTAKE-OVERNIGHT-20261002",
  "ORCH-ADVISOR-PILOT-20261113",
  "ORCH-METABOLIC-BATCH-20261019",
  "PLAN-HE47-USABLE-KNOWLEDGE-PRESERVED-MEANING-SUSTAINABLE-COST-20261112",
  "PLAN-PROACTIVE-ADVISOR-20261113"
 ],
 "sessions": {
  "q230p-tooluniverse-blind-38": "idle",
  "HE": "busy",
  "IT Orchestrator": "idle",
  "legend-development-e8": "idle",
  "SCI": "idle",
  "legend-development-d5": "idle",
  "legend-development-05": "idle"
 },
 "commits_since_last_tick": 0
}

## Assignments already drafted, with their evidence level (do not duplicate; follow what was taken in charge)
{
 "ADV-001": {
  "recipient": "Science",
  "key": "ebp-reannotation-it29",
  "highest": "EXECUTED"
 },
 "ADV-002": {
  "recipient": "Harness",
  "key": "blocked-artefact-route",
  "highest": "EXECUTED"
 }
}

## Previous assessment
P1: `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/P1/assessment.md` (read it; reuse it when nothing relevant changed)

## Neutral entry points
| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit | largest file |
|---|---|---|---|---|---|
| limits | Authorised mission and resource limits: the task record named in the brief, and its siblings | `ledger/tasks/*/*.json` | 210 | 2026-11-13 | `ledger/tasks/scientist-a/AQEILAN-FT-A-001.json` (35,910 bytes) |
| invariants | Canonical project invariants and the operating rules | `CLAUDE.md`<br>`ARCHITECTURE.md`<br>`framework/master/harness_development_principles.md`<br>`framework/master/designed_for_growth.md`<br>`framework/master/gold_is_in_the_details.md`<br>`framework/instruction/LEGEND_CORE.md`<br>`framework/instruction/epistemic_discipline.md`<br>`disease-models/wwox/mission.md` | 8 | 2026-11-13 | `framework/instruction/LEGEND_CORE.md` (35,123 bytes) |
| repurposing_method | Drug-repurposing roadmap and Standing method | `disease-models/wwox/research/drug_repurposing/roadmap_current.md`<br>`framework/protocols/repurposing_adapter_convention.md` | 2 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/roadmap_current.md` (47,529 bytes) |
| dashboard | Dashboard: source records of the public page (the page is a map, the records are the facts) | `disease-models/wwox/research/drug_repurposing/view/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/DEPLOY.md` | 4 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/view/README.md` (35,880 bytes) |
| investigations | Investigations (research investment, not efficacy), needs and cards | `disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv`<br>`disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json`<br>`disease-models/wwox/research/drug_repurposing/needs/needs.md`<br>`disease-models/wwox/research/drug_repurposing/cards/*` | 65 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json` (1,101,419 bytes) |
| open_questions | Open-question maps and rows | `disease-models/wwox/research/drug_repurposing/**/open_questions*` | 5 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv` (171,301 bytes) |
| candidates | Candidates, comparisons and hypothesis packages | `disease-models/wwox/research/drug_repurposing/generation_it*/`<br>`disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv`<br>`disease-models/wwox/research/drug_repurposing/**/hypotheses*` | 52 | 2026-11-13 |  |
| packages | Completed packages and their consumer notes | `disease-models/wwox/research/drug_repurposing/*/README.md`<br>`disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md` | 242 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/README.md` (65,530 bytes) |
| diagnoses | Diagnoses, evaluations and DREAM | `disease-models/wwox/research/session_evaluations/*`<br>`disease-models/wwox/research/drug_repurposing/diagnosis_*/*`<br>`disease-models/wwox/research/dream*/README.md` | 198 | 2026-11-13 | `disease-models/wwox/research/session_evaluations/2026-10-04_BATCH_20261004_001.md` (60,878 bytes) |
| memory_dismissals | Dismissal and discovery ledgers, memory index (outside the repository) | `disease-models/wwox/research/dismissal_ledger_current.md`<br>`disease-models/wwox/research/discovery_ledger_current.md`<br>`/home/desktop/.claude/projects/-home-desktop-legend-development/memory/MEMORY.md` | 3 | 2026-11-12 | `disease-models/wwox/research/discovery_ledger_current.md` (926,660 bytes) |
| radar | Radar findings and capability gaps | `governance/candidates/HARNESS-SCOUT-*.md`<br>`disease-models/wwox/research/capability_scout_log.md`<br>`SKILLS.md`<br>`CAPABILITIES.md` | 4 | 2026-11-13 | `disease-models/wwox/research/capability_scout_log.md` (184,962 bytes) |
| tools | Which tool answers which question (the advisor has no shell; this explains what the records came from) | `framework/scripts/README.md` | 1 | 2026-11-13 | `framework/scripts/README.md` (55,620 bytes) |

Memory directory (read-only): `/home/desktop/.claude/projects/-home-desktop-legend-development/memory`

## Output
Return one assessment with the headings given in your definition. Name every file or page you opened under 'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them. This brief is your prompt: the copy saved in the campaign folder is the same text, so do not open it. A file the table marks over 20,000 bytes is paid for again on every later turn: Grep for the heading or id you need and read that range, and open the whole file when the question needs all of it; never re-read a range you already hold.
Give the usual headings, then `## Assignments`: either `none: <reason>` (continuing the plan can be the best decision) or one `### ASSIGNMENT n` block per assignment with exactly these `field: value` lines: key, recipient, question, why_now, roadmap_link, related_work, sources, decision_changed_by_result, perimeter_and_budget, method_autonomy, deliver_to, duplicate_check. recipient is Orchestrator, Science or Harness. At most as many blocks as the campaign allows; none to show independence.
