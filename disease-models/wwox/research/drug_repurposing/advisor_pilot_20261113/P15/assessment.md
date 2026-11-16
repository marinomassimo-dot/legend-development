I'm recommending three linked assignments for today's eight-hour MEETING programme. Mechanism matching for antiseizure drugs (item 3) is the new research batch (item 2), run as a prediction frozen before its outcome is gathered and then scored (item 1).

## 1 · Principal decision
How should the eight-hour programme the operator ordered on 2026-11-16 be spread across its three agenda items? Facts that frame it:
- The operator's line ends the host hold, so the previous HOLD (`record:INTAKE-OVERNIGHT-20261002=CONTINUE`) no longer applies.
- Every session except `legend-development-39` is idle. The executable queue is empty.
- ADV-012 is COMPLETE (`ORCH-ADV012-RP003-WO11-20261115.json`, `MANDATE_STATE: COMPLETE`).
- The MEETING file is open. No participant has been consulted yet (`MEETING-20261116T070702Z-f4lqagml.md`, "Round table and decisions").

## 2 · Leading recommendation
**Strategic judgment:** treat items 2 and 3 as the same batch, and use item 1 as the way that batch is run.
- **Item 3 becomes the new batch.** It is a mechanism-matching exercise across all antiseizure mechanism classes. It is built from the repository's WWOX threads (T1–T11 in `ADV_SEED.md`).
- **It is run as a prospective test.** The class-level predictions and the scoring rule are frozen by commit before an independent Scientist extracts the case-level exposure and outcome statements for the classes A1 never coded.
- **The work splits three ways:**
  - IT freezes the rule and the predictions, then integrates.
  - SCI builds the held-out outcome table, without seeing the predictions.
  - HE measures the starting rate at which frozen predictions held. It also checks whether the existing generation and consumer path can carry an "aggravation" hypothesis as its own sign, rather than netting it into "no match".

## 3 · Relevant alternatives
- **Choose the item-2 thread by the seed rubric (scores 0–3) before doing anything.** This adds a ceremony. The rubric also already favours AED matching:
  - it consumes held threads;
  - it has assay readouts (the slice burst for INV-05, PTZ for INV-04);
  - its agents are approved.
  
  Let the round object instead of scoring first.
- **Go deeper on Cav3, ethosuximide or NX1.** NX1 showed that the Fig 7 extraction cannot size the wild-type question (16–26× spread between bounds, `nx1_sizing_sci_20261115/README.md`). RP-016 is limited to missing values. Its marginal value is low. It enters the matrix as one row (T3/T5) and is not a batch on its own.
- **Repeat the RP-003 open-question draw.** Still valid, but it is the third in a row and does not answer the operator's agenda. Keep it queued.
- **RP-017, RP-018, ISR (INV-02).** These wait on measurements; the radar's ISR item is noise (unrelated repositories named ISR).
- **The radar's ROCK2 lead.** Two papers on new ROCK2 inhibitor chemistry. The diagnosis row already says the residual is pharmacology qualification, so nothing is waiting on this lead. No action; record it as triaged.
- **Mirror (RP-022).** No live session. The request stays conditional.

## 4 · Why now
- The operator has given an explicit agenda and asked for at least eight hours of directed work.
- All sessions are idle.
- The two blocked intake mandates are not dependencies of this work.
- **Interpretation:** a prospective case is exactly what RP-005 still lacks. Its only completed held-out case (`ORCH-RP005-HELDOUT-20261115`, the Fig 7 quantification) tested what a paper contains, not mechanism-level generation. P14 §3 already judged that the RP-004 F-predictions concerned paper content and were not a prospective EVAL case.

## 5 · Evidence and uncertainty
**Facts:**
- **The existing AED comparison is a literature table of three agents** (`aed_compare_it31_20261107/output/README.md`):
  - only ethosuximide has a WWOX experiment;
  - there is no drug-by-genotype test and no head-to-head in WWOX;
  - levetiracetam has no denominator.
- **A1 coded only four classes** (`batch_sci_20261105/a1_wwox_reports/denominators_a1.tsv`): vigabatrin, hormonal, ketogenic diet and cannabidiol.
  - 36 children were exposed after de-duplication; 6 have both endpoints.
  - Sodium-channel blockers, valproate, levetiracetam, topiramate and benzodiazepines appear only incidentally (`other_context`, 2 rows).
  - `cases_a1.tsv` holds 42 mentions of other agents that were never tabulated by class.
  - So a per-class outcome table, including worsening statements, does not yet exist in the repository. That makes it usable as a held-out outcome.
- **The ethosuximide effect is not shown to be WWOX-specific.** NX1 states the absolute-scale interaction test cannot separate a WWOX-specific effect from a proportional effect.

**Interpretations:**
- **Leap L1 ("PTZ is the wrong ruler") is right and binding.** A thread counts as WWOX-specific only with a genotype contrast.
- **Leap L5 is circular with the held-out outcome.** It infers the WWOX drivers from reported resistance to sodium-channel blockers and SV2A ligands, which is clinical outcome knowledge. It must be declared an input and excluded from scoring, or the test scores itself.
- **The predictor is contaminated.** IT sessions have read these case reports before. Blindness can only be partial: declare it, and freeze predictions from the thread records only.

**Uncertainty:** the case literature is small, selected for interest and drug-resistant across classes. The held-out table can mainly reject a prediction (for example, several stated improvements on sodium-channel blockers would reject L2's aggravation hypothesis). It can rarely confirm one. That is still a valid result.

## 6 · Next bounded action, expected result, decision changed
**Actions:**
- IT writes the matching rule and the class-level predictions with an explicit "WWOX-specific vs generic" column, age stratification (L4) and the aggravation hypotheses kept separate (L2). It commits them before seeing SCI's table.
- SCI builds the all-class exposure and outcome table from the held, receipted full texts.
- IT scores the predictions and writes the discriminating slice experiment (L7): one representative per top class, Wwox-null versus wild type, same-day controls, read on a ratio scale.

**Expected result:** a scored set of class predictions, a ranked list of what the case record cannot answer, and one experiment design.

**Decisions it changes:**
- the wording of the seizure cards for INV-03, INV-04, INV-05 and INV-10;
- whether any class gains or loses research priority;
- whether an aggravation question enters the open-question map;
- RP-005's first true prospective score.

No candidate row without BLOCK-1.

## 7 · What would change my view
- The round produces a stronger item-2 thread with a closer assay, or SCI reports that the held full texts state per-drug outcomes too rarely (fewer than about 5 informative statements outside the four classes). In that case item 3 becomes a matrix only, and the scoring step is dropped.
- An operator PAUSE line.
- HE finds the aggravation sign already represented. Its part (b) then closes as "no change".

## 8 · Resource implications
- IT: one integrating thread over about 8 hours.
- SCI: one producer pass plus a blind second reader on a sample.
- HE: one bounded measurement and code check.
- Free lawful routes only, zero spend, no contact parameter. No new registry, gate or tool unless HE shows a format gap. Nothing frozen is touched.

## 9 · Inspected
**Opened:**
- the MEETING file `MEETING-20261116T070702Z-f4lqagml.md`
- `brainstorm_20261116/ADV_SEED.md`
- `P14/assessment.md`
- `aed_compare_it31_20261107/output/README.md`
- `nx1_sizing_sci_20261115/README.md`
- `meeting_20261115/README.md`
- `a1_wwox_reports/denominators_a1.tsv`

**Grep only:** `ORCH-ADV012-RP003-WO11-20261115.json` (state), `ORCH-RP005-HELDOUT-20261115.json` (objective and state), INV titles in `investigations.tsv`, a count of other-agent mentions in `cases_a1.tsv`, and a Glob of ledger tasks dated 2026-11-15 and 2026-11-16.

**Not reached:**
- the portfolio file itself (I relied on the brief's excerpt);
- `comparison.tsv`, `cases_a1.tsv` rows and the INV-05 and WO-11 packages;
- the dashboard page, DREAM and the earlier meeting minutes.

## 10 · Freshness and exposure
- Snapshot fa81fd50a. The MEETING file was read uncommitted as on disk.
- The radar dated 05:20Z was treated as a lead only.
- No Orchestrator intended action was seen. I was exposed to ADV's own seed, which I partly disagree with: L5 is circular, and the 0–3 rubric is unnecessary.
- Host duty still open: reconcile the Advisor recall with the canonical `strategic_advisor.py recall` text.

## Assignments

### ASSIGNMENT 1
key: aed-mechanism-matching-prospective
recipient: Orchestrator
question: Across antiseizure mechanism classes (sodium-channel, T-type, SV2A, AMPA, GluN2B/NMDAR, GABA-A PAM, GABA-AT/GAT, Kv7, carbonic anhydrase/multi-target, valproate-type, hormonal, diet, cannabidiol/fenfluramine-type), which classes do the repository's WWOX threads (T1–T11) predict as a better match, which as an aggravation hypothesis (kept separate, never netted), and which as generic only? Answer under a rule fixed and committed before scoring, with age strata (P6–P8 vs P13–P15, the GluN2B share) and only genotype-contrast threads counting as WWOX-specific. Then, after SCI's held-out table arrives, how many frozen predictions does it support or reject, which agent-level distinction (if any) survives inside the top class, and which slice-panel experiment (Wwox-null vs wild type, one representative per top class, same-day control, ratio scale) would change the ranking?
why_now: The operator's 2026-11-16 MEETING agenda (items 2 and 3) ends the hold. All sessions are idle. IT31 is only a three-agent literature table and NX1 shows ethosuximide's specificity is unsized. RP-005 lacks a mechanism-level prospective case.
roadmap_link: Operator line 2026-11-16 (items 1–3); priorities 2–3; directions A, B, C, G; portfolio RP-005, RP-001, RP-016.
related_work: aed_compare_it31_20261107; nx1_sizing_sci_20261115; fig7_quant_ethosuximide_lithium_sci_20261115; cav3_pair_gaps_rp016_sci_20261115; wo11_mierau_it55_20261115; seizure_function_inv10_20261107; ORCH-RP005-HELDOUT-20261115 (paper-content case, COMPLETE). The current work keeps priority. Queue this assignment; you may anticipate its independent parts if resources and dependencies allow. Before starting it, check that results that arrived since have not changed its usefulness.
sources: advisor_pilot_20261113/brainstorm_20261116/ADV_SEED.md; ranking_it8_p9_20261029/investigations.tsv (INV-03, 04, 05, 09, 10); the WWOX thread packages above; needs/needs.json.
decision_changed_by_result: the wording of the seizure cards and the INV-03, 04, 05 and 10 next-experiment fields; the research priority of mechanism classes; a possible aggravation open-question row; RP-005's first prospective mechanism-level score.
perimeter_and_budget: One integrating thread of about 8 hours. Commit the predictions before reading SCI's table, and declare prior exposure to the case reports. L5 (reported resistance) is an input, not a scored prediction. No dose, route, schedule or recommendation to use any agent. BLOCK-1 applies before any candidate row. Reference genotype class only. Lawful free routes, zero spend, no contact parameter. Frozen packages untouched.
method_autonomy: IT chooses the scoring rule, the predictor (itself or a delegate), the thread tiers and whether agent-level comparison is warranted. It may merge, narrow or decline parts with a reason, and may correct this premise.
deliver_to: ADV presidio (MEETING closing notes; portfolio RP-005, RP-016); consumers: seizure cards, investigations, open-question map.
duplicate_check: No ledger task dated 2026-11-15 or 2026-11-16 covers all-class AED matching (Glob of both dates). IT31 covered three agents as a literature table. ADV-001 to ADV-012 contain no AED matching. Not checked: chat-only messages.

### ASSIGNMENT 2
key: a1-all-class-exposure-outcome-heldout
recipient: Science
question: From the WWOX case reports already held with full-text receipts (the 14 reports pooled in a1_wwox_reports, plus the seven-child series PMID 42721537 only if a lawful free full text exists), which statements tie a named antiseizure agent outside the four A1 classes to an outcome? The outcome can be response, no response, worsening or a new seizure type, recorded with age band at exposure, co-therapy and genotype class. Apply A1's per-child de-duplication rule; give counts only, with no percentage below 10. Which classes have no informative statement at all?
why_now: This is the held-out outcome for Assignment 1. A1 coded only vigabatrin, hormonal, ketogenic diet and cannabidiol, leaving 42 other-agent mentions in cases_a1.tsv untabulated. The extraction is independent and can start at once.
roadmap_link: Operator line 2026-11-16, item 3 ("not relying only on literature": here the literature is the test, not the source of the match); priorities 1–2; directions C, G.
related_work: batch_sci_20261105/a1_wwox_reports (cases_a1.tsv, denominators_a1.tsv, audits A1 and A1b); aed_compare_it31 levetiracetam and perampanel counts; INV-10 evidence. The current work keeps priority. Queue this assignment; you may anticipate its independent parts if resources and dependencies allow. Before starting it, check that results that arrived since have not changed its usefulness.
sources: a1_wwox_reports/*; the receipts in fulltext_read_receipts for those reports; batch_sci_20261105/verify/audit_A1*.
decision_changed_by_result: whether IT's frozen class predictions (including the sodium-channel aggravation hypothesis, L2) are supported, rejected or untestable; which classes need a new measurement rather than reading.
perimeter_and_budget: One producer pass plus a blind second reader on a sample of rows. Do not read or receive IT's prediction file until IT reports its freeze commit; do not send your table to the predictor before then. Held full texts and lawful free routes only (an abstract is census only), zero spend, no contact parameter, no identifiers beyond the published report and patient numbers.
method_autonomy: SCI chooses the extraction scheme, outcome categories and verification sampling, and may declare the table uninformative with a reason.
deliver_to: IT Orchestrator (scoring); ADV presidio informed.
duplicate_check: A1 covered four classes plus 2 other_context rows. IT31 counted only levetiracetam and perampanel mentions. No 2026-11-15 or 2026-11-16 ledger task extends A1.

### ASSIGNMENT 3
key: generative-baseline-and-aggravation-sign
recipient: Harness
question: (a) How many predictions frozen before their outcome exist in the repository (F1–F7 RP-004, WO-32, IT49-Q11, H1–H5, bets P-a and P-b, the RP-005 Fig 7 held-out case), split by whether they predict paper content or a generative mechanism? For each, what is the scored status, and what are the cost and verification route where recorded? (b) Can the existing generation and consumer path (conditional_proposals.py, hypothesis_package.py, consumer_links.tsv, the IT52 rows) carry an aggravation or "avoid" hypothesis as a sign of its own, distinct from no match and never netted? Check this against the code, not by assertion. If not, what is the smallest reversible change, and what is the cost of removing it again?
why_now: MEETING item 1 asks how to raise predictive generative capacity. Without a baseline, no later change can be measured. Assignment 1 will produce aggravation hypotheses that need a consumer path.
roadmap_link: Operator line 2026-11-16, item 1; priority 4; directions F, G; portfolio RP-005, RP-010.
related_work: ORCH-RP005-HELDOUT-20261115; generation_it52_20261114; mechanism_lens_it55_20261115/prediction_frozen.md. The current work keeps priority. Queue this assignment; you may anticipate its independent parts if resources and dependencies allow. Before starting it, check that results that arrived since have not changed its usefulness.
sources: the folders above; generation_it40_20261109/conditional_proposals.py; framework/scripts (hypothesis_package.py); ADV_SEED.md G1–G6.
decision_changed_by_result: whether item 1 needs a harness change or only a practice; the reference hit rate for RP-005; whether Assignment 1's aggravation output reaches a consumer.
perimeter_and_budget: A one-off table in a dated folder, not a new registry, gate or service. Any code change must be minimal, tested and reversible. Do not touch frozen candidates or other actors' verification clones. Zero spend.
method_autonomy: HE chooses the census method and may conclude that no change is needed.
deliver_to: ADV presidio and IT Orchestrator (for Assignment 1's consumer path).
duplicate_check: No 2026-11-15 or 2026-11-16 plan task covers a prediction baseline or an aggravation sign (Glob). HE47 and PLAN-HE-VALUE-CONTINUITY concern cost and continuity, not this.

## Portfolio updates

```json
[
  {"id": "RP-005", "status": "assigned", "next_action": "P15: AED mechanism-matching run as a prospective case (IT freezes class predictions, SCI builds the held-out all-class exposure/outcome table from A1 sources, HE measures the baseline of frozen predictions)", "updated_utc": "2026-11-16"},
  {"id": "RP-016", "next_action": "Folded into the AED mechanism-matching matrix (T5 row) at P15; no separate retrieval; operator qualifications stand", "updated_utc": "2026-11-16"}
]
```

## Outcome
outcome: assign
excluded: rubric scoring before work (ceremony; the round may object instead); further Cav3/NX1 depth (low marginal value, folded in as a row); a third RP-003 draw (valid but off-agenda, kept queued); RP-017/018/INV-02 (measurement-bound); ROCK2 and ISR radar items (no waiting obstacle; ISR hits are noise); Mirror review (no live session)
reason: The operator's 2026-11-16 agenda ends the hold. All-class AED matching, run as a prospective test with an independent held-out case table and a harness baseline, serves items 1–3 at once, consumes held threads and reaches a discriminating slice experiment.
resume_when: event