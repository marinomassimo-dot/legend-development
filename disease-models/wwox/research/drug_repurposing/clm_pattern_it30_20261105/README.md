# CLM-pattern evaluation set: 30 real decisions of the repurposing work (IT30, 2026-11-05)

Non-canonical research material, public edition (WWOX-DEE reference genotype class). Not medical advice. Zero spend, no contact. No model was run to build this set.

## Answer first

* **30 cases** in `cases.tsv` (tab-separated, UTF-8, 9 equal columns): **7 easy, 12 ambiguous, 11 deceptive**.
* Purpose: test the pattern "state, compare alternative actions, choose next work" (the pattern of the CLM project, which scores candidate actions against a state). A CLM-style score is not generation of hypotheses and not a probability of biological truth; neither is any verdict on this set.
* **Sources** (all inside the repository): Orchestrator task records `ledger/tasks/orchestrator/ORCH-ROADMAP-IT2..IT29` and `ORCH-FRESH-IT29-P10` (DECISIONS_TAKEN, STOP_LOG, and the structured `challenge` objects of IT28 and IT29); package READMEs under `disease-models/wwox/research/drug_repurposing/` for IT4 to IT29; the P10 working files `cycle_it29_p10_20261105/` (QUESTION, ROUTING, LOG, RETURN); pre-registrations and deviation logs of IT7 and IT18. Iterations covered: IT4, IT5, IT7, IT8, IT13, IT14, IT17 to IT20, IT23 to IT26, IT28, IT29.
* **Decision types covered:** targeted reading versus thematic batch (CLM-22, 23, 28, 30); new search versus reuse of an available result (CLM-13, 15, 20, 21); more compounds versus clarifying biological direction (CLM-03, 06, 23, 26); identity check versus pharmacological evaluation (CLM-01, 15, 17, 18, 19); new analysis versus abstention with a reopening condition (CLM-04, 06, 10, 14); consumption of a returned result (CLM-21, 25, 29); process or authority choices (CLM-02, 09, 11).
* **Poor and mixed cases are included on purpose:** 1 poor (CLM-13), 8 mixed (CLM-03, 05, 06, 16, 20, 23, 25, 26), 21 good. Outcome quality describes the decision's consequence, not the biology. Cases where a step was repeated or a result was not consumed carry `yes` in the last column (CLM-05, 08, 12, 13, 16, 20, 21, 28).

## How the state at decision time was reconstructed

1. For each case the decision moment was fixed first (date, package, step), then `state_text` was written only from the records that existed at that moment: the task record of that iteration, the mandate or brief, the pre-registration, the frozen tables, and for IT28 and IT29 the `available_knowledge` and `decisive_uncertainty` fields written when each challenge was opened (they predate the returns).
2. Package READMEs are usually written at the end of the work. Where a README states both the question and the result, only the question-side facts were used for `state_text` and the result-side sentence went to `outcome_known_later`. Numbers that were computed by the decision itself (for example the gap counts found by a diagnosis step) were treated as state only when the decision was taken after them.
3. Options are the alternatives named in the record (CLM-01, 03, 27 and the "set aside" lists) or the evident alternatives at that point, including plausible low-value ones (an untested promising signal, a name-based join, waiting). The taken option is placed at a seeded random position (A to E); `action_taken` uses the same letters. Option text for the taken action is often the most detailed.
4. `outcome_quality` and `duplicate_search_or_wasted_step` were judged from later records only; "weakly evidenced" is written where no counterfactual exists.

## What could not be reconstructed, and what was dropped

* The ledger DECISIONS_TAKEN entries of IT2 to IT12 are one or two lines; the deliberation is in package files that were not always dated inside the day. Cases there were kept only where a package README or pre-registration shows the question side (CLM-03, 04, 05, 06).
* Dropped (not in the set): (a) IT7 fly-factorial firewall breach: the record says only "a firewall breach found and removed", the before-state could not be separated from the after-state; (b) IT24 P1 source check of five suspect sign pairs: why those pairs were suspect (which resource disagreed) is not stated in the files read, so the state could not be built without inventing it; (c) IT28 P8 inverse test as a design decision: the compounds were already in the module and the README says it is not a discovery test, which made the option set depend on later knowledge; (d) operator-integration decisions (IT22 research-yield priority, IT24 readability, IT23 new resources): these are operator choices, not Orchestrator choices.
* Not reconstructed: the Orchestrator's private reasoning where only the action is recorded; whether CLM-05's carried statements existed in the exact words implied (inferred from the list of files the correcting commit changed); the exact clock order within one day for IT7 to IT8.
* The packages mix several actors (Scientist, verifier, Orchestrator). Where the record shows the Orchestrator briefing or accepting the work (verification in CLM-07, a package design in CLM-24), the case is the Orchestrator's choice to commission or accept that design.

## Known leak risks (for whoever reads results)

* Length and detail bias: the option actually taken is usually the longest and most specific one.
* Vocabulary bias: the repository's own vocabulary ("carried limit", "abstain", "not detected, not excluded", "second actor") appears in the taken option more often than in the others.
* Pattern bias: in this repository the conservative option (verify first, abstain, report as pending) was taken in most cases; a chooser that always picks "verify first" will score well and show nothing. Deceptive cases CLM-05, 08, 13, 20, 25 are where the plain verify-first rule is not enough.
* Some state texts contain facts that already carry a hint (CLM-17 states that a handed-over row rests on a single listing claim; CLM-27 lists that two files disagree).
* Overlap: CLM-27, 28, 29, 30 are four consecutive steps of one cycle (P10), and CLM-18 and 19 two consecutive steps; a model that read the earlier case has seen state for the next one.
* Public repository: a model with access to this repository may have seen the records; no "novelty" can be claimed for a score.
* Outcome column and `duplicate_search_or_wasted_step` must be hidden from the chooser; `source_paths` should also be hidden because the paths name the iteration and the folders hold outcomes.

## Protocol for the separate verifier (reads state and options only)

1. Input: file `cases.tsv` with columns `case_id`, `state_text`, `options` only. Hide `difficulty`, `source_paths`, `action_taken`, `outcome_known_later`, `outcome_quality`, `duplicate_search_or_wasted_step`.
2. For each case, output a set: every option the verifier considers reasonable next work (several allowed; ranking inside the set is optional), and `NONE_SUFFICIENT` if none is adequate. Add a one-line reason and any fact the verifier would want that the state does not give. The verifier must not search the repository, and must be a different run, context and model instance from anything that wrote or read this set.
3. A model under test is run in the same way, separately; its output may be a score per option, but a score is a ranking of actions against a state, not a probability that the action is biologically right.
4. Scoring (done by a third party after step 2): (a) hit rate of the taken option inside the verifier set; (b) size of the verifier set (a model that marks everything reasonable is uninformative); (c) separately for easy, ambiguous and deceptive; (d) for deceptive cases, whether the verifier avoided the option flagged in the case's `outcome_known_later` or `duplicate_search_or_wasted_step`; (e) NONE_SUFFICIENT rate, which is expected to be low.
5. Do not read the result as agreement with scientific truth: the taken action is the Orchestrator's choice, and several cases are marked mixed or poor. A disagreement with the taken action is not an error until the outcome column has been read.
6. Report the per-difficulty counts and the leak risks above next to any figure.

## Result of the retrospective comparison (IT30, 2026-11-05) and verdict

What was run: two fresh model contexts of the current model family, each given only `case_id`, `state_text` and the options shortened to their first 22 words (so length does not carry the answer). The **chooser** scored every option 0 to 3 against the state and chose, with `NONE` allowed (`chooser_blind.tsv`). The **verifier**, separately, marked every option REASONABLE, WEAK or UNREASONABLE with several allowed and `none_sufficient` possible (`verifier_blind.tsv`). Neither saw the action taken or the outcome. This tests the *pattern* (state, compare alternatives, choose) with a current model. It is not a test of the CLM checkpoint (see below) and not a hand-written classifier standing in for it.

| Measure | Result |
|---|---|
| Chooser pick equals the action taken | 28 of 30 (easy 7/7, ambiguous 11/12, deceptive 10/11); the two differences are cases where the Orchestrator took an action outside the listed options |
| Taken action judged by the verifier | REASONABLE in 28; WEAK in 1 (CLM-13, the one case with a poor outcome); 2 not scorable (action outside the options) |
| Chooser pick judged by the verifier | REASONABLE in 30 of 30 |
| Options marked UNREASONABLE by the verifier, taken or chosen | 0 |
| `none_sufficient` raised | 0 of 30 |
| Steps the history repeated or wasted (8 cases) that the chooser avoided | 0 demonstrable. It repeated the taken option in 7; in the 8th (CLM-20) it chose a listed option while the history took an unlisted one, so whether it would have avoided the waste cannot be read from the options |
| Cost | about 30 s and 60k tokens for 30 cases per reader; no extra step added to any decision |

**What this does and does not show.** The comparison produced no change of decision that the verifier judged an improvement: the chooser agreed with history, and history was almost always reasonable by the verifier. That is the expected result when (a) the alternatives were reconstructed *after* the action was known (the taken option was longer and more specific in 27 of 30 cases before shortening, and the alternatives are plausible-but-weak by construction) and (b) the deterministic challenge routing and the Orchestrator's own checks had already removed the obviously bad paths. So the set can show that the pattern does no harm and costs almost nothing; it cannot show that it improves choices, because it contains no real decision where the right option was not already the visible one. The one poor case (CLM-13) was repeated by the chooser, so a generic model comparison did not catch it either; what would have caught it was a fact the state did not state (the data bucket was dead).

**Checkpoint.** CLM-v0.1-8B needs a Qwen3-8B embedding endpoint (vLLM, one GPU); this host has 4 CPUs, 15 GB of RAM and no GPU. It was not run and no mock stands in for it. The project reports its own benchmark results on small held-out sets (38 and 30 tasks); revision examined: the repository front page and API documentation on 2026-11-05 (the page shows no commit date; the documented model release is 2026-09-19), Apache 2.0 code and weights.

**Verdict: WATCH for the checkpoint, TRIAL for the pattern in one place.** The pattern is adopted only where it costs nothing and a real fork exists: before a new cycle, write the state in a few lines, list the alternatives including "reuse what exists" and "none is sufficient", and score them before acting (done once, before acting, for the IT30 cycle: `S8_CHOICE.md`). No new agent, no harness, no gate. Re-open for the checkpoint if a GPU becomes available at no cost; re-open for the pattern if a forward test (choices made before their outcome is known, on open questions) shows a decision it changed.
