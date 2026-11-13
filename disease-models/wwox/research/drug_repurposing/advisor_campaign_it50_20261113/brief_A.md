# Strategic Advisor brief — Stage A

## Snapshot
- Repository SHA: `d8baa78d780dbef74721ea1d232b05e3356946aa` (branch `task/it50`)
- Dispatch time (UTC): 2026-11-13T07:37:03Z
- Uncommitted paths (4; read as on disk):
  - `ledger/tasks/orchestrator/ORCH-ROADMAP-IT50-20261113.json` (M) sha256 `2a7baec71f0f3f76`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/advisor_sealed/INTENDED_ACTION_1.md` (??) sha256 `d418f3adf3e0904b`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/inputs/constraints.md` (??) sha256 `6a164c1699612fa8`
  - `disease-models/wwox/research/drug_repurposing/advisor_campaign_it50_20261113/inputs/mission.md` (??) sha256 `81f51156807c7f78`
- Deliveries the caller announces (announced ≠ in this snapshot ≠ reachable by your tools ≠ read; 'read' is recorded after the run):

  | announced | in this snapshot | reachable from your working directory |
  |---|---|---|
  | `387f6ae4:disease-models/wwox/research/drug_repurposing/kir2_drugname_sci49_20261112` | YES | YES |
  | `387f6ae4:disease-models/wwox/research/drug_repurposing/cell_context_verify_sci49_20261112` | YES | YES |
  | `387f6ae4:disease-models/wwox/research/drug_repurposing/advisor_followup_20261112` | YES | YES |
- Dashboard: https://marinomassimo-dot.github.io/legend-development/ · source revision 387f6ae49edb6e8aa8259703336fc7f25cd7bda9 2026-11-13T02:22:05+00:00 · the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.

## Mission and limits (verbatim from the caller)
Mission: improve the generative capacity of LEGEND for WWOX loss-of-function drug repurposing (gene therapy outside the pharmacological proposals): turn evidence, relations, experimental results and knowledge already held into pharmacological hypotheses, discriminating comparisons and useful experiments. Verification accompanies generation. A useful result may open a possibility that was invisible, recover a lost proposal, improve a comparison or delimit an unsupported path.
Strategic question: which next investment can most improve a drug-repurposing decision, comparing further depth in the current thread, another priority thread, unused knowledge and a small technical obstacle? Do not force a rotation of threads. The advisor should consider the dashboard (a map of opportunities), open questions, favourable and contrary results, DREAM, diagnoses, pertinent radar, cost and invariants. Source records are the factual reference.
Scope: current WWOX investigations, candidates, open questions and existing capabilities. No clinical recommendation, patient-level analysis, gene-therapy development, business activity, outreach, paid service or broad infrastructure redesign.

## Operational constraints
Constraints: zero new external spend; no contact with people; public edition; not medical advice; ranking means research investment, not efficacy; no change of rank, sign or qualification to show an effect; no predictive claim from better access to knowledge; one scientific delegate at a time with a distinct verifier; originals read in full when accessible.
Boundaries: the science session has a generative mission starting from myelination (do not duplicate or interrupt a package already under way); Harness builds a minimal link for design-only packages (no competing reader); SCI50 is an input when it arrives, not a constraint. Window: up to ten hours; one Stage A and one Stage B only for IT50 (a failed attempt counts). The IT48 pilot ceiling is separate and spent.
Dependencies: browser tests on this host need a working Chromium (the tool now selects an installed older Snap revision).

Task record carrying the mission: `ledger/tasks/orchestrator/ORCH-ROADMAP-IT50-20261113.json`

## Neutral entry points
| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit | largest file |
|---|---|---|---|---|---|
| limits | Authorised mission and resource limits: the task record named in the brief, and its siblings | `ledger/tasks/*/*.json` | 202 | 2026-11-13 | `ledger/tasks/scientist-a/AQEILAN-FT-A-001.json` (35,910 bytes) |
| invariants | Canonical project invariants and the operating rules | `CLAUDE.md`<br>`ARCHITECTURE.md`<br>`framework/master/harness_development_principles.md`<br>`framework/master/designed_for_growth.md`<br>`framework/master/gold_is_in_the_details.md`<br>`framework/instruction/LEGEND_CORE.md`<br>`framework/instruction/epistemic_discipline.md`<br>`disease-models/wwox/mission.md` | 8 | 2026-11-12 | `framework/instruction/LEGEND_CORE.md` (35,123 bytes) |
| repurposing_method | Drug-repurposing roadmap and Standing method | `disease-models/wwox/research/drug_repurposing/roadmap_current.md`<br>`framework/protocols/repurposing_adapter_convention.md` | 2 | 2026-11-12 | `disease-models/wwox/research/drug_repurposing/roadmap_current.md` (44,438 bytes) |
| dashboard | Dashboard: source records of the public page (the page is a map, the records are the facts) | `disease-models/wwox/research/drug_repurposing/view/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/DEPLOY.md` | 4 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/view/README.md` (34,905 bytes) |
| investigations | Investigations (research investment, not efficacy), needs and cards | `disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv`<br>`disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json`<br>`disease-models/wwox/research/drug_repurposing/needs/needs.md`<br>`disease-models/wwox/research/drug_repurposing/cards/*` | 65 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json` (1,097,886 bytes) |
| open_questions | Open-question maps and rows | `disease-models/wwox/research/drug_repurposing/**/open_questions*` | 4 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv` (160,144 bytes) |
| candidates | Candidates, comparisons and hypothesis packages | `disease-models/wwox/research/drug_repurposing/generation_it*/`<br>`disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv`<br>`disease-models/wwox/research/drug_repurposing/**/hypotheses*` | 49 | 2026-11-13 |  |
| packages | Completed packages and their consumer notes | `disease-models/wwox/research/drug_repurposing/*/README.md`<br>`disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md` | 234 | 2026-11-13 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/README.md` (65,530 bytes) |
| diagnoses | Diagnoses, evaluations and DREAM | `disease-models/wwox/research/session_evaluations/*`<br>`disease-models/wwox/research/drug_repurposing/diagnosis_*/*`<br>`disease-models/wwox/research/dream*/README.md` | 195 | 2026-11-13 | `disease-models/wwox/research/session_evaluations/2026-10-04_BATCH_20261004_001.md` (60,878 bytes) |
| memory_dismissals | Dismissal and discovery ledgers, memory index (outside the repository) | `disease-models/wwox/research/dismissal_ledger_current.md`<br>`disease-models/wwox/research/discovery_ledger_current.md`<br>`/home/desktop/.claude/projects/-home-desktop-legend-development/memory/MEMORY.md` | 3 | 2026-11-12 | `disease-models/wwox/research/discovery_ledger_current.md` (926,660 bytes) |
| radar | Radar findings and capability gaps | `governance/candidates/HARNESS-SCOUT-*.md`<br>`disease-models/wwox/research/capability_scout_log.md`<br>`SKILLS.md`<br>`CAPABILITIES.md` | 4 | 2026-11-13 | `disease-models/wwox/research/capability_scout_log.md` (183,245 bytes) |
| tools | Which tool answers which question (the advisor has no shell; this explains what the records came from) | `framework/scripts/README.md` | 1 | 2026-11-12 | `framework/scripts/README.md` (54,854 bytes) |

Memory directory (read-only): `/home/desktop/.claude/projects/-home-desktop-legend-development/memory`

## Output
Return one assessment with the headings given in your definition. Name every file or page you opened under 'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them. This brief is your prompt: the copy saved in the campaign folder is the same text, so do not open it. A file the table marks over 20,000 bytes is paid for again on every later turn: Grep for the heading or id you need and read that range, and open the whole file when the question needs all of it; never re-read a range you already hold.
