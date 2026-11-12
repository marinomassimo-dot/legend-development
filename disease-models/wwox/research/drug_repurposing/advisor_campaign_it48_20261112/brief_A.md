# Strategic Advisor brief — Stage A

## Snapshot
- Repository SHA: `eb424cd06bc63439be5f26a8de6ccba171e3cbda` (branch `task/it48`)
- Dispatch time (UTC): 2026-11-12T20:42:10Z
- Uncommitted paths (4; read as on disk):
  - `edger/tasks/orchestrator/ORCH-ROADMAP-IT48-20261112.json` (M) sha256 ``
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/advisor_sealed/INTENDED_ACTION_1.md` (??) sha256 `cf739080b3d5d7d5`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/inputs/constraints.md` (??) sha256 `0d3795727a1378ff`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it48_20261112/inputs/mission.md` (??) sha256 `add4e65fbf47183d`
- Dashboard: https://marinomassimo-dot.github.io/legend-development/ · source revision 3870f5457705917940530f9fa896b4697af9793a 2026-11-12T20:36:16+00:00 · the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.

## Mission and limits (verbatim from the caller)
Mission: improve WWOX loss-of-function drug-repurposing generation and prioritisation (gene therapy outside the pharmacological proposals). Success is when prior inactive knowledge changes a search, proposal, comparison or the next experiment; not molecule counts. Uncertain hypotheses stay explorable with premises, alternatives and a falsifier.
Campaign: choose and execute two bounded research increments, each with one principal question, returned to actual consumers (investigations, open questions, comparisons, generator, candidate records). Compare further investment in the current branch with other existing investigations or open questions, with a premise shared by several candidates, with knowledge already held but unused, and with a small technical obstacle that blocks a scientific decision. Continuing the current branch is allowed; so is changing it; neither is required.
Source entry points: use the entry map of strategic_advisor.py. The dashboard is a map of opportunities; the repository records are the factual reference.

## Operational constraints
Constraints: zero new external spend; no contact with external people, no operator e-mail to any service; no clinical treatment recommendation, patient-level analysis, gene-therapy development, business activity or broad infrastructure redesign; public edition (no individual-level record); not medical advice; ranking means research investment, not expected efficacy in a child; no change of rank, sign or qualification to show an effect; AED evidence kept separate (clinical / preclinical / untested); one scientific delegate at a time, producer and verifier distinct; originals read in full when accessible.
Time: at most 24 hours from the first Stage A dispatch (2026-11-12). Ceilings: two Stage A, two Stage B. Owner session: orchestrator (legend-development-4e).
Dependencies: SCI48 science delivery is available when it arrives and is not a constraint. Public view and CI of the last delivered main commit may still be completing. The browser test host has a Snap Chromium fault (CHROME_BIN workaround).

Task record carrying the mission: `ledger/tasks/orchestrator/ORCH-ROADMAP-IT48-20261112.json`

## Neutral entry points
| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit |
|---|---|---|---|---|
| limits | Authorised mission and resource limits: the task record named in the brief, and its siblings | `ledger/tasks/*/*.json` | 197 | 2026-11-12 |
| invariants | Canonical project invariants and the operating rules | `CLAUDE.md`<br>`ARCHITECTURE.md`<br>`framework/master/harness_development_principles.md`<br>`framework/master/designed_for_growth.md`<br>`framework/master/gold_is_in_the_details.md`<br>`framework/instruction/LEGEND_CORE.md`<br>`framework/instruction/epistemic_discipline.md`<br>`disease-models/wwox/mission.md` | 8 | 2026-11-12 |
| repurposing_method | Drug-repurposing roadmap and Standing method | `disease-models/wwox/research/drug_repurposing/roadmap_current.md`<br>`framework/protocols/repurposing_adapter_convention.md` | 2 | 2026-11-07 |
| dashboard | Dashboard: source records of the public page (the page is a map, the records are the facts) | `disease-models/wwox/research/drug_repurposing/view/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/DEPLOY.md` | 4 | 2026-11-12 |
| investigations | Investigations (research investment, not efficacy), needs and cards | `disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv`<br>`disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json`<br>`disease-models/wwox/research/drug_repurposing/needs/needs.md`<br>`disease-models/wwox/research/drug_repurposing/cards/*` | 65 | 2026-11-12 |
| open_questions | Open-question maps and rows | `disease-models/wwox/research/drug_repurposing/**/open_questions*` | 3 | 2026-11-12 |
| candidates | Candidates, comparisons and hypothesis packages | `disease-models/wwox/research/drug_repurposing/generation_it*/`<br>`disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv`<br>`disease-models/wwox/research/drug_repurposing/**/hypotheses*` | 46 | 2026-11-12 |
| packages | Completed packages and their consumer notes | `disease-models/wwox/research/drug_repurposing/*/README.md`<br>`disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md` | 227 | 2026-11-12 |
| diagnoses | Diagnoses, evaluations and DREAM | `disease-models/wwox/research/session_evaluations/*`<br>`disease-models/wwox/research/drug_repurposing/diagnosis_*/*`<br>`disease-models/wwox/research/dream*/README.md` | 192 | 2026-11-12 |
| memory_dismissals | Dismissal and discovery ledgers, memory index (outside the repository) | `disease-models/wwox/research/dismissal_ledger_current.md`<br>`disease-models/wwox/research/discovery_ledger_current.md`<br>`/home/desktop/.claude/projects/-home-desktop-legend-development/memory/MEMORY.md` | 3 | 2026-11-12 |
| radar | Radar findings and capability gaps | `governance/candidates/HARNESS-SCOUT-*.md`<br>`disease-models/wwox/research/capability_scout_log.md`<br>`SKILLS.md`<br>`CAPABILITIES.md` | 4 | 2026-11-12 |
| tools | Which tool answers which question (the advisor has no shell; this explains what the records came from) | `framework/scripts/README.md` | 1 | 2026-11-12 |

Memory directory (read-only): `/home/desktop/.claude/projects/-home-desktop-legend-development/memory`

## Output
Return one assessment with the headings given in your definition. Name every file or page you opened under 'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them.
