## Assessment (Stage P, P17)

**1. Principal decision.** The deepening round of 16:35Z is in progress. It now holds 18 ideas, all marked ADVANCE. Its 21:21Z closing round sets no step that carries those ideas into the drug-repurposing loop. The decision is whether to queue that step now, or to add more deepening work, or to wait.

**2. Leading recommendation.** Queue one consumption pass for the Orchestrator (IT), to start after the 21:21Z closing round:
- link each prediction in the idea-by-arm table to the existing candidates, investigations and open questions;
- say whether each one strengthens, weakens or leaves them unchanged;
- list the mechanism classes the ideas imply that the current ranking lacks (labels only, BLOCK-1 pending);
- freeze the table by digest before any pilot data exists.

Science and Harness keep their own dossiers; I am not adding deepening tasks for them.

**3. Relevant alternatives.**
- *(a) More held-data deepening, assigned by me:* excluded. Science is visibly running many frozen-before-run tests in `deepening_sci_20261116/` (I13, I15, I16, I19, rivals, heterozygote sizes, PAM against chloride). Harness has I8, I18 and I4 in `deepening_he_20261116/`. The owners already hold that work.
- *(b) The wet-lab pilot:* the highest value, but it needs the operator to provide a laboratory (MEETING 13:21Z, decision 3). That branch is parked, not a reason to idle.
- *(c) Tool authorisation for ADMET-AI / RDKit:* an operator item. The BLOCK-1 flags stay "not run" until it is given.
- *(d) RP-003 open-question draw and RP-021 symbol trial:* earlier threads. The operator's 16:35Z instruction makes developed ideas the current product, so they are not the next marginal step.
- *(e) The ROCK2 and ISR items in the daily radar:* the radar's own closing text says the ROCK2 residual is pharmacology qualification, not generation. The ISR hits are keyword noise (repositories named "Israr", an HSC kinetics repository). Neither is worth forwarding.

**4. Why now.**
- *Facts:* `ideas_arm_table.tsv` on remote main has 58 rows over 17 arms. It contains no freeze or hash, no INV- reference, no candidate and no open-question id. Yet `UNIFIED_MODEL_U1_AND_IDEA_ARM_TABLE.md` says the table "is frozen by hash before the pilot's results exist". Several arms fall outside the antiseizure set (substrate/ketone, remyelination, Y2/NPY, glycine-site, K2P/Kv7 leak opener). Priority B of the roadmap and the operator's 07:05Z item 1 ("reach an experiment and a drug-repurposing step") both need this connection.
- *Precedent:* IT did the same kind of consumption for the morning programme (rows IT56-Q01 and IT56-Q02 in `open_questions_map.tsv`, lines 195–196).

**5. Evidence and uncertainty.**
- *Facts:* `ideas_portfolio.tsv` (remote) shows depths of seed (I1, I3, I4, I6, I8, I16), chain (I2, I5, I9, I10, I11a/b, I14, I17) and model (I7, I13, I15). None is experiment-ready or repurposing-ready.
- *Interpretation:* the gap between ideas and repurposing is one of representation and consumption, not missing biology.
- *Uncertainty:* I saw remote main only through WebFetch. Listings may be truncated, and I read summaries rather than the TSV byte for byte. The closing round may already plan this step; the assignment's `obsolete_if` covers that case.
- *Activity at dispatch:* Harness, Science and legend-development-39 busy; IT idle; Mirror has no live session. IT being idle fits its I2 addendum being "running", probably a delegate. That is my inference, not verified. I see no stuck session to unblock.

**6. Next bounded action, expected result and decision changed.**
- *Action:* IT's consumption pass, as specified in Assignment 1.
- *Expected result:*
  - a frozen arm table;
  - a short consumption note with one line per arm × candidate or investigation (strengthen / weaken / unchanged);
  - zero or more new open-question rows, each naming the decision it changes and marked in-silico or wet-lab;
  - a list of mechanism classes absent from the ranking, flagged BLOCK-1 pending.
- *Decisions it can change:* which arms the experiment brief must keep, for example the GABA-A PAM row that separates rebound from restored inhibition; and whether INV-03/04 (efonidipine/flunarizine), INV-05 (GABA-A subtype), WO-11 (GluN2B) or IT56-Q01 (tonic current) change status or wording. It promotes no candidate.

**7. What would change my view.**
- The closing round already assigns this pass, or IT says the table is still changing tonight. Then the freeze moves later.
- A Science result that kills a central idea (for example I1's rebound reading). Then the table is consumed after that revision.
- An operator item arriving (a laboratory, or the tool authorisation). Then the pilot or BLOCK-1 work comes first.

**8. Resource implications.** One IT pass of a few hours, with at most one delegate, at no cost. It does not touch Science's or Harness's frozen predictions or their scripts. The weekly quota is unknown and I assume none.

**9. Inspected.**
- *Opened:*
  - `P16/assessment.md`
  - `brainstorm_20261116/DEEPENING_ROUND.md`
  - `deepening_adv_20261116/UNIFIED_MODEL_U1_AND_IDEA_ARM_TABLE.md`
  - `deepening_adv_20261116/I9_PNN_PV_MATURATION.md`
  - `meetings/MEETING-20261116T132146Z-ctit3nmc.md`
  - `research_portfolio.tsv`, lines 1–6
  - `open_questions_map.tsv`, lines 195–196
- *Fetched from remote main:* the `brainstorm_20261116/` listing, `ideas_portfolio.tsv` (summarised by the fetch tool), `ideas_arm_table.tsv` (summary), and the listings of `deepening_attacks_it`, `deepening_he` and `deepening_sci`.
- *Not reached:* the content of the Science, Harness and IT dossiers; `EXPERIMENT_BRIEF_V1_1.md`; the investigations TSV; the live dashboard; the 19:21Z meeting, if one was held.
- *Host duties carried over from P16, not verified:* reconciling the recall text and the stale P11 effect.

**10. Freshness and exposure.**
- *Snapshot:* local snapshot 015b9b5 is 127 commits behind; the remote was read at about 20:40Z.
- *Exposure:* this is Stage P, so there is no Orchestrator preference to be blind to. I read my own earlier ADV dossiers, which are history, not corroboration.

## Assignments

### ASSIGNMENT 1
key: deepening-round-repurposing-consumption
recipient: Orchestrator
question: After the 21:21Z closing round, carry the deepening round into the repurposing loop. (1) Freeze `ideas_arm_table.tsv` by digest before any pilot data exists, as U1 states. (2) For each arm × idea prediction, name the existing candidate, investigation, comparison or open question it bears on: at least INV-03/INV-04 (Cav3: efonidipine/flunarizine), INV-05 (GABA-A subtype), INV-02 (ISR), WO-11 (GluN2B window), IT56-Q01 (tonic current). Say whether it strengthens, weakens or leaves it unchanged, and why. (3) List the mechanism classes the ideas imply that are absent from the current ranking, as labels with BLOCK-1 marked "not run". (4) Write an open-question row only where a named decision changes, marked in-silico or wet-lab. Otherwise record a reasoned non-row.
why_now: 18 ideas are ADVANCE but none is repurposing-ready. The arm table has no freeze and no link to INV, candidates or questions. Roadmap priority B and the operator's 07:05Z item 1 need this step, and IT was idle at 20:35Z.
roadmap_link: Priorities 1–2; strategic direction B and C; operator instructions of 2026-11-16 at 07:05Z (item 1) and 16:35Z (ideas pushed forward)
related_work: DEEPENING_ROUND.md; UNIFIED_MODEL_U1_AND_IDEA_ARM_TABLE.md; ideas_portfolio.tsv; the earlier IT consumption pass (IT56-Q01/Q02); EXPERIMENT_BRIEF_V1_1.md
sources: disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/{ideas_arm_table.tsv,ideas_portfolio.tsv,deepening_*_20261116/}; batch_sci_20261105/map/open_questions_map.tsv; ranking_it8_p9_20261029/investigations.tsv; experiment_brief_presidio013_sci_20261116/EXPERIMENT_BRIEF_V1_1.md
decision_changed_by_result: Which arms the slice brief must keep (the GABA-A PAM row separates rebound from restored inhibition); whether INV-03/04/05, WO-11 or IT56-Q01 change status or wording; which classes outside the antiseizure set enter the ranking's reading list. No candidate is promoted.
perimeter_and_budget: Mechanism level only. Hypotheses labelled as such. No dose and no recommendation. Reference genotype class only. Lawful free sources and zero spend. A reCAPTCHA or interstitial page is a stop. At most one delegate. Do not edit Science's or Harness's frozen prediction files or their scripts. One isolated landing worktree; run the structured-data and release-surface tests before pushing.
method_autonomy: IT chooses the format, the order and whether a line becomes a row. It may correct the premise or declare the pass superseded, giving the reason in its own record.
deliver_to: ADV host and Science (second reader for any changed INV wording); consumers are open_questions_map.tsv and the investigation cards
duplicate_check: Not in ADV-001 to ADV-015 (ADV-013/014/015 belong to the morning AED programme). DEEPENING_ROUND.md assigns no consumption into the map. P16 drafted nothing.
mode: queued
start_condition: The closing round of 21:21Z has ended, or IT says the arm table is stable for tonight
interferes_with: Science's and Harness's active deepening tests, if the table changes while being frozen; freeze a dated version and add later rows as a dated update
obsolete_if: The closing round has already assigned the same consumption and freeze to someone, or a test has killed the central U1 reading before the pass starts

## Portfolio updates
```json
[
  {"id": "RP-005", "status": "assigned", "next_action": "The AED programme is closed (CLOSING_SYNTHESIS.md, blind audit, IT56-Q01/Q02 consumed). The current prospective generative case is the deepening round of 2026-11-16 at 16:35Z (DEEPENING_ROUND.md): 18 ideas marked ADVANCE, depth seed/chain/model, none repurposing-ready; judge and fate metrics retired as gates. Next: freeze the idea-by-arm table and consume it into the repurposing loop (P17 Assignment 1, queued for IT after the 21:21Z close).", "updated_utc": "2026-11-16T20:45:00Z"}
]
```

## Outcome
outcome: queue
excluded: No new deepening tasks for Science or Harness, because both are busy with frozen held-data tests on their own ideas. The wet-lab pilot and the tool authorisation are operator items. The RP-003 draw and RP-021 have lower marginal value than consuming today's ideas. The ROCK2 and ISR radar leads are pharmacology qualification or keyword noise.
reason: The deepening round produces ideas but has no step that links its arm predictions to the candidates and open questions or freezes them before pilot data. A queued IT pass after the 21:21Z close fills that gap without touching work in progress.
resume_when: event