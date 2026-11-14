# Strategic Advisor brief — Stage P (proactive evaluation)

## Snapshot
- Repository SHA: `8756c6e0540c9b1a98b5cd96d5cd82a7ce2bf588` (branch `main`)
- Dispatch time (UTC): 2026-11-14T02:09:11Z
- Uncommitted paths (31; read as on disk):
  - `disease-models/wwox/registries/coverage_report.md` (M) sha256 `e54bb8671897f808`
  - `disease-models/wwox/registries/fulltext_read_receipts.jsonl` (M) sha256 `3d2208d555c2876d`
  - `disease-models/wwox/registries/reading_state.md` (M) sha256 `331a22281d96c344`
  - `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv` (M) sha256 `585b272cb8c06da4`
  - `disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/README.md` (M) sha256 `7f328d2339edb488`
  - `disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/ladder_it14_p3.tsv` (M) sha256 `1748930d6f87c8bc`
  - `disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv` (M) sha256 `43b2d931e6525dcc`
  - `disease-models/wwox/research/drug_repurposing/inhibitory_defect_sci47_20261112/output/levers.tsv` (M) sha256 `b01dcaa921c6b226`
  - `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/investigations.tsv` (M) sha256 `4185a9aaef66ada9`
  - `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/investigations_it20.tsv` (M) sha256 `2bb195765bb67445`
  - `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json` (M) sha256 `f30108986066e5e0`
  - `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/selections.tsv` (M) sha256 `8ada0fb4a6b77be3`
  - `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/triggers.tsv` (M) sha256 `927a03b4e3ce2bd9`
  - `disease-models/wwox/research/drug_repurposing/view/i18n/content_de.json` (M) sha256 `9574668aacf0ff32`
  - `disease-models/wwox/research/drug_repurposing/view/i18n/content_es.json` (M) sha256 `3b049be34120eb57`
  - `disease-models/wwox/research/drug_repurposing/view/i18n/content_fr.json` (M) sha256 `8ef1615b400078ca`
  - `disease-models/wwox/research/drug_repurposing/view/i18n/content_it.json` (M) sha256 `c54d4fb701cfda26`
  - `disease-models/wwox/research/drug_repurposing/view/i18n/content_source.json` (M) sha256 `719a2fdaf77a2a2f`
  - `disease-models/wwox/research/drug_repurposing/view/index.en.html` (M) sha256 `d0ff27ae24e80090`
  - `disease-models/wwox/research/drug_repurposing/view/index.es.html` (M) sha256 `f185b3f20619d9d6`
  - `disease-models/wwox/research/drug_repurposing/view/index.fr.html` (M) sha256 `a3c75ee14a5d25a0`
  - `disease-models/wwox/research/drug_repurposing/view/index.html` (M) sha256 `92b26f55f71f1187`
  - `framework/state/state_manifest_current.md` (M) sha256 `f030b2a6f823db7a`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261113-24533090-62.json` (??) sha256 `c201527cb5eca3dd`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261113-25798598-62.json` (??) sha256 `5e491fb17d9b4682`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261113-27392635-62.json` (??) sha256 `8705bab89f550369`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261114-21237147-60.json` (??) sha256 `96c5eb8730850d75`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261114-24533090-60.json` (??) sha256 `5efff1a384692a87`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261114-25798598-60.json` (??) sha256 `94803625faa810a1`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261114-27392635-60.json` (??) sha256 `fd2ddb506ac1a9d6`
  - `disease-models/wwox/research/receipt_staging/adv004/FTR-20261114-42886059-60.json` (??) sha256 `6b1e8563b7ffefd6`
- Dashboard: https://marinomassimo-dot.github.io/legend-development/ · source revision 17fd1bcda4229737c391c1f1c3235a19547e99e6 2026-11-14T00:36:54+00:00 · the public page shows no build stamp; the package commit above is the source revision it is generated from. Publication date of the live page was not checked.

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

**Strategic direction** (operator, 2026-11-13, given with the ADV session mandate; it supplements the priorities above and changes none of them; the operator may be absent for the whole campaign and new instructions simply update the direction when given):
- A. *Raise generative capacity.* Find knowledge LEGEND holds but does not combine or use; find pharmacological levers, competing explanations, comparisons and experiments the current path misses. Keep apart novelty for LEGEND, novelty against the literature, and predictive capacity actually demonstrated.
- B. *Carry science through to drug repurposing.* Assess every substantial result for what it implies: does it strengthen, weaken or leave unchanged the candidates, comparisons, premises and open questions? A conditional proposal is useful when it states the conditions to verify; no favourable candidates and no quantity of hypotheses are imposed.
- C. *Return questions to research.* Promising, contrary and inconclusive results alike orient further work. A question says which decision a given answer would change and separates in silico work from measurements that are indispensable in vitro or in vivo.
- D. *Compare depth with a change of direction.* Weigh the marginal benefit of one more batch on the current thread against the other prioritised opportunities. Keep suspended branches, with the conditions that would make them interesting again. The most recent thread is not automatically the most important.
- E. *Look beyond the WWOX keyword when pertinent.* Use adjacent systems and literatures for transferable methods, perturbations and explanations; keep species, cell type, development, genotype, endpoint and the limits of the transfer.
- F. *Improve the Harness in the service of the science.* Prefer small interventions that unblock a capability, improve the use of the tools already available, remove duplication or make a change of direction easier. Assess scouting and mining by licence, cost, real availability and ease of removal; the reputation of a repository does not show that its pattern is useful.
- G. *Measure the benefit.* Look for observable differences: a better comparison, a more discriminating experiment, a useful connection, a recovered proposal, a resolved question, or useless work avoided. The number of prompts, agents, nodes or open activities is not progress by itself.

**Pilot campaign** (first Proactive Strategic Advisor pilot): 24 hours from its effective activation (`advisor_pilot_20261113/budget.json`), no automatic renewal of that expiry; no recursive delegation, no external spend. **Current limits** (amended 2026-11-13, see the dated line below and `budget.json` `amendments`): at most **five** real strategic invocations and at most **six** executive assignments in total, each invocation at most 20 turns, counting everything already used, failed attempts included (2 invocations and 3 assignments were used before the amendment; the "3/3" in the first-period evidence is historical, not the current limit). These are ceilings, not targets. Exhausting the Advisor's budget stops its evaluations only; the work already authorised to the sessions goes on.

**Recent operator instructions** (newest first; add a dated line to change direction, or write "stop" or "pause" to suspend the pilot):
- 2026-11-13 (night mission, ten hours, ends 2026-11-14T09:33Z and never past the campaign expiry): the operator is away. The ADV session coordinates IT, SCI and HE on its own and aims to close at least one useful cycle between research and drug repurposing: roadmap -> strategic choice -> assignment -> result -> consumption in drug repurposing -> new decision. The campaign limits above were raised (5 invocations, 6 assignments in total, no new service or spend). Before choosing, reconcile the real state (running, delivered and consumed, waiting with a resume condition, technical blocks, available sessions) and compare at least four real alternatives: go deeper on the thread just followed; change to another prioritised question; use knowledge already present that the generator does not exploit; fix a small Harness problem that blocks a scientific result. Prefer one principal, bounded and deep scientific assignment; one independent Harness assignment only if a concrete obstacle exists; any follow-up chosen after results, not reserved to fill the night. Recipients keep methodological autonomy (they may correct the premise and propose competing explanations). Keep generation and adversarial verification apart; a wet-lab experiment is described (measurement, comparison, decision it changes), never commissioned or turned into an urgent request. A negative or unchanged result is valid. The IT CI diagnosis stays first for publication and must not freeze independent SCI and HE work. Quiet periodic checks. No new registers, hierarchies, contracts, gates or schedulers.
- 2026-11-13 (later): the operator assigned the session "ADV — Strategic Advisor" (ACTOR_ID `orchestrator`) as the standing strategic presidio of this pilot, with no new budget and no renewal: it talks with the operator, keeps this section, hosts the recall and forwards assignments to IT, SCI and HE. The strategic direction A-G above was added from that mandate; priorities 1-5 are unchanged. No instruction to stop or pause.
- 2026-11-13: the roadmap above; the Advisor may act without being asked, the Orchestrator keeps operational coordination; the operator can intervene at any time by editing this section.

## Campaign limits
{"expires_utc": "2026-11-14T18:22:36Z", "max_assignments": 6, "max_invocations": 5, "turn_limit": 20}

## Observed state (mechanical, this tick)
{
 "events": [],
 "open_mandates": [
  "INTAKE-OVERNIGHT-20261002",
  "ORCH-ADV-PRESIDIO-20261113",
  "ORCH-ADVISOR-PILOT-20261113",
  "ORCH-METABOLIC-BATCH-20261019",
  "PLAN-HE47-USABLE-KNOWLEDGE-PRESERVED-MEANING-SUSTAINABLE-COST-20261112",
  "PLAN-PROACTIVE-ADVISOR-20261113"
 ],
 "sessions": {
  "q230p-tooluniverse-blind-38": "idle",
  "HE": "idle",
  "IT Orchestrator": "busy",
  "legend-development-e8": "idle",
  "SCI": "idle",
  "legend-development-d5": "idle",
  "legend-development-05": "idle",
  "legend-development-38": "idle",
  "legend-development-39": "busy"
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
 },
 "ADV-003": {
  "recipient": "Science",
  "key": "isr-target-route-retest",
  "highest": "EXECUTED"
 },
 "ADV-004": {
  "recipient": "Science",
  "key": "gabaa-subtype-same-system",
  "highest": "EXECUTED"
 },
 "ADV-005": {
  "recipient": "Harness",
  "key": "activity-route-usable",
  "highest": "EXECUTED"
 }
}

## Previous assessment
P3: `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/P3/assessment.md` (read it; reuse it when nothing relevant changed)

## Live harness scouting (daily scout briefing, read by the caller: a feed of opportunities, not of evidence; the weekly candidate tables are stale)
file time 2026-11-13T05:21Z; complete

RADAR BRIEFING 2026-11-13T05:20:04+00:00 | remote main 387f6ae49edb (context refreshed)
NEXT STEP: examine Discovery:reopen:function_pharm_it14_p3_20261101/NP3P2: Locus of the lost sIPSC current (receptor-limited or release-limited), with a physiological-chloride internal . Minimal test: read the source; reproduce one stated result on public inputs before any adoption
PLAN derived at main 387f6ae49edb from 20 surfaces (re-derived, 2 re-read), 72 priority question(s), digest 27ef08de451e
PLAN PROVISIONAL: 1 older reopen/decision table(s) not read this run (TABLE_LIMIT 12, 2 slots rotate by ISO week): disease-models/wwox/research/drug_repurposing/modifiers_it12_p1b_20261031/reopen_searches_it12_p1b.tsv
PLAN PROVISIONAL: surface disease-models/wwox/research/drug_repurposing/diagnosis_it28_20261105/README.md parsed 0 items (format changed or table emptied?)
Team explored: braincircuitsbehaviorlab (github; owner of discovered BrainCircuitsBehaviorLab/NMDAR_paper): 0 lead(s) of 7 scanned
CONTEXT: roadmap_current is dated 2026-11-01; later dated evidence in README.md (2026-11-02), capability_scout_log.md (2026-11-12) outranks its CURRENT heading: read that first.
Channels: github delta (6 new) | huggingface delta (3 new) | nature delta (2 new) | europepmc delta (6 new)
  question [scientific inputs] Locus of the lost sIPSC current (receptor-limited or release-limited), with a physiological-chloride internal solution an electrophysiology  -> if confirmed: reopen condition met? an electrophysiology report with the same-cell triad (isolated NMDAR current, sIPSC charge, resting potential and input resistance) and mini
    because: reopen function_pharm_it14_p3_20261101 table row NP3P2 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv @ blob abb8c8031e, main 387f6ae49edb]: "Locus of the lost sIPSC current (receptor-limited or release-limited), with a physiological-chloride internal "
  question [matching/pharmacology] Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to-head in one system with diaze -> if confirmed: reopen condition met? a head-to-head in one system with diazepam as comparator
    because: reopen function_pharm_it14_p3_20261101 table row NP3P3 [NEEDS-DATUM] [disease-models/wwox/research/drug_repurposing/function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv @ blob abb8c8031e, main 387f6ae49edb]: "Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to"
  question [unexpected] unplanned find: no gap assumed -> if confirmed: whether it reveals a question we did not know to ask
    because: open slot: no priority assumed
Delta 1: Discovery:reopen:function_pharm_it14_p3_20261101/NP3P2
  source / version+date / fact+limit: [paper/europepmc] MAPT-A152T mutation drives neuronal hyperactivity through Fyn-NMDAR signaling in human iPSC-Derived neurons: Insights into Alzheimer's patho (2024-12-24, published record) https://europepmc.org/article/MED/39811068; [paper/europepmc] Effects of esketamine on electrophysiology and metabolic reprogramming in brain organoids: insights into antidepressant mechanisms. (2025-08-30, published record) https://europepmc.org/article/MED/40885845; [paper/europepmc] Response of iPSC-derived neurons from individuals with treatment-resistant depression to (2 R,6 R)-hydroxynorketamine and r
  question + decision: Locus of the lost sIPSC current (receptor-limited or release-limited), with a physiological-chloride internal solution an electrophysiology  -> reopen condition met? an electrophysiology report with the same-cell triad (isolated NMDAR current, sIPSC charge, resting potential and input resistance) and mini
  roadmap placement: R1/R8; proposed use: none proposed until a claim is examined
  minimal test: read the source; reproduce one stated result on public inputs before any adoption
  cost + terms: screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated
  outcome / reopen: TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)
Delta 2: Discovery:reopen:function_pharm_it14_p3_20261101/NP3P3
  source / version+date / fact+limit: [preprint/europepmc] Systemic diazepam alters local hippocampal CA1 circuits and differentially affects entorhinal and CA3 inputs (2026-08-23, preprint (not peer reviewed)) https://europepmc.org/article/PPR/PPR1304123; [paper/europepmc] Chronic Chrysin, but Not Diazepam, Induces Anxiolytic-like Effects Without Behavioral Tolerance. (2026-09-10, published record) https://europepmc.org/article/MED/42796464; [paper/europepmc] Female ddY mice show a weaker diazepam-induced reduction in aggressive biting behavior toward inanimate objects and lower hypothalamic KCC2  (2026-11-05, published record) h
  question + decision: Same-system comparison of the subtype selectivity of the GABA-A positive modulators under discussion a head-to-head in one system with diaze -> reopen condition met? a head-to-head in one system with diazepam as comparator
  roadmap placement: R5; proposed use: none proposed until a claim is examined
  minimal test: read the source; reproduce one stated result on public inputs before any adoption
  cost + terms: screening: minutes; adoption: unestimated until read (licence, version, provenance); per item and per part (code / data / weights / service / article), shown where stated
  outcome / reopen: TO_TRIAGE (a search hit is discovery, not a reading; 'no useful opportunity' is valid)
Saved: state
Saved: report
Saved: pending log


## Neutral entry points
| id | what | patterns (relative to the repository root unless absolute) | matches now | last commit | largest file |
|---|---|---|---|---|---|
| limits | Authorised mission and resource limits: the task record named in the brief, and its siblings | `ledger/tasks/*/*.json` | 214 | 2026-11-14T01:53:40+00:00 | `ledger/tasks/scientist-a/AQEILAN-FT-A-001.json` (35,910 bytes) |
| invariants | Canonical project invariants and the operating rules | `CLAUDE.md`<br>`ARCHITECTURE.md`<br>`framework/master/harness_development_principles.md`<br>`framework/master/designed_for_growth.md`<br>`framework/master/gold_is_in_the_details.md`<br>`framework/instruction/LEGEND_CORE.md`<br>`framework/instruction/epistemic_discipline.md`<br>`disease-models/wwox/mission.md` | 8 | 2026-11-13T18:17:16+00:00 | `framework/instruction/LEGEND_CORE.md` (35,123 bytes) |
| repurposing_method | Drug-repurposing roadmap and Standing method | `disease-models/wwox/research/drug_repurposing/roadmap_current.md`<br>`framework/protocols/repurposing_adapter_convention.md` | 2 | 2026-11-13T23:33:43+00:00 | `disease-models/wwox/research/drug_repurposing/roadmap_current.md` (52,212 bytes) |
| dashboard | Dashboard: source records of the public page (the page is a map, the records are the facts) | `disease-models/wwox/research/drug_repurposing/view/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/manifest.json`<br>`disease-models/wwox/research/drug_repurposing/view/shareable_package/README.md`<br>`disease-models/wwox/research/drug_repurposing/view/DEPLOY.md`<br>`disease-models/wwox/research/drug_repurposing/view/evidence_graph.json`<br>`disease-models/wwox/research/drug_repurposing/view/work_order.json`<br>`disease-models/wwox/research/drug_repurposing/view/context_verdicts.json`<br>`disease-models/wwox/research/drug_repurposing/view/i18n/content_en.json` | 8 | 2026-11-14T00:36:54+00:00 | `disease-models/wwox/research/drug_repurposing/view/work_order.json` (51,423 bytes) |
| investigations | Investigations (research investment, not efficacy), needs and cards | `disease-models/wwox/research/drug_repurposing/ranking_it*/investigations.tsv`<br>`disease-models/wwox/research/drug_repurposing/ranking_it*/ranking.json`<br>`disease-models/wwox/research/drug_repurposing/needs/needs.md`<br>`disease-models/wwox/research/drug_repurposing/cards/*` | 65 | 2026-11-13T21:57:04+00:00 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json` (1,101,944 bytes) |
| open_questions | Open-question maps and rows | `disease-models/wwox/research/drug_repurposing/**/open_questions*` | 5 | 2026-11-14T00:10:09+00:00 | `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/open_questions_map.tsv` (173,392 bytes) |
| candidates | Candidates, comparisons and hypothesis packages | `disease-models/wwox/research/drug_repurposing/generation_it*/`<br>`disease-models/wwox/research/drug_repurposing/**/compound_decisions*.tsv`<br>`disease-models/wwox/research/drug_repurposing/**/hypotheses*` | 52 | 2026-11-14T00:01:50+00:00 |  |
| packages | Completed packages and their consumer notes | `disease-models/wwox/research/drug_repurposing/*/README.md`<br>`disease-models/wwox/research/drug_repurposing/**/CONSUMER_NOTE.md` | 244 | 2026-11-14T00:11:13+00:00 | `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/README.md` (65,530 bytes) |
| diagnoses | Diagnoses, evaluations and DREAM (a connection DREAM proposes is a question, not biological evidence) | `disease-models/wwox/research/session_evaluations/*`<br>`disease-models/wwox/research/drug_repurposing/diagnosis_*/*`<br>`disease-models/wwox/research/dream*/README.md`<br>`disease-models/wwox/research/drug_repurposing/dream*/README.md` | 200 | 2026-11-14T00:12:06+00:00 | `disease-models/wwox/research/session_evaluations/2026-10-04_BATCH_20261004_001.md` (60,878 bytes) |
| memory_dismissals | Dismissal and discovery ledgers, memory index (outside the repository) | `disease-models/wwox/research/dismissal_ledger_current.md`<br>`disease-models/wwox/research/discovery_ledger_current.md`<br>`/home/desktop/.claude/projects/-home-desktop-legend-development/memory/MEMORY.md` | 3 | 2026-11-12; 2026-11-14 (file time, outside the r | `disease-models/wwox/research/discovery_ledger_current.md` (926,660 bytes) |
| radar_science | Scientific, pharmacological, data and method radars (opportunities, not evidence) | `disease-models/wwox/research/drug_repurposing/radar_*/README.md`<br>`disease-models/wwox/research/capability_scout_log.md` | 5 | 2026-11-13T15:35:45+00:00 | `disease-models/wwox/research/capability_scout_log.md` (184,962 bytes) |
| harness_scouting | Harness scouting and repository mining. The weekly candidate tables stop at their last week (see `last commit`); the live feed is the daily scout, whose host cache is outside the repository and is embedded in the Stage P brief by the caller | `governance/candidates/HARNESS-SCOUT-*.md`<br>`/home/desktop/.local/state/legend/scout_daily_briefing.md` | 2 | 2026-09-28; 2026-11-13 (file time, outside the r | `governance/candidates/HARNESS-SCOUT-2026-W40.md` (34,158 bytes) |
| capability_surface | What the system claims it can do, with maturity | `SKILLS.md`<br>`CAPABILITIES.md` | 2 | 2026-11-13T18:17:16+00:00 |  |
| tools | Which tool answers which question, and what the shipped censuses and cost tools measure (the advisor has no shell; this explains what the records came from) | `framework/scripts/README.md`<br>`framework/protocols/delegation_budget.md` | 2 | 2026-11-14T00:01:50+00:00 | `framework/scripts/README.md` (56,803 bytes) |

Memory directory (read-only): `/home/desktop/.claude/projects/-home-desktop-legend-development/memory`

## Output
Return one assessment with the headings given in your definition. Name every file or page you opened under 'Inspected'. You cannot write, run commands or start agents. The entry points are starting places; follow references past them. This brief is your prompt: the copy saved in the campaign folder is the same text, so do not open it. A file the table marks over 20,000 bytes is paid for again on every later turn: Grep for the heading or id you need and read that range, and open the whole file when the question needs all of it; never re-read a range you already hold.
Give the usual headings, then `## Assignments`: either `none: <reason>` (continuing the plan can be the best decision) or one `### ASSIGNMENT n` block per assignment with exactly these `field: value` lines: key, recipient, question, why_now, roadmap_link, related_work, sources, decision_changed_by_result, perimeter_and_budget, method_autonomy, deliver_to, duplicate_check. recipient is Orchestrator, Science or Harness. At most as many blocks as the campaign allows; none to show independence.
