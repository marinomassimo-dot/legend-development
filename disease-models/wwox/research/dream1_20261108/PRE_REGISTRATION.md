# DREAM-1 pre-registration: does consolidated experience change what a fresh session retrieves and does? (2026-11-08)

Non-canonical research material. Not medical advice. Zero spend: no paid API, no Dreams service, no new account; delegates run inside the existing session quota. Written and committed before any test run.

## What is compared

* **Condition k1 (A, current organisation):** repository clone at b316b28d (remote main when work started). **Condition k2 (B, consolidated):** the same plus commit fce0c531 (`framework/scripts/README.md` section 13: six habits that existed only in one chat's private memory; one dated correction in `gsk3_eif2b_20261107/CONSUMER_NOTE.md`). Nothing else differs. Clone directories are named neutrally (repo_k1, repo_k2) so the agent cannot read the condition from its path.
* **What a run sees:** the clone only. The private memory folder, git history and other directories are excluded by instruction. This models a session on **another runtime**, which cannot read one chat's private memory; it does not model the chat that owns that memory.
* **Same for all runs:** agent type `legend-delegate`, model `sonnet`, effort `medium` (delegation_budget.md section 1, retrieval role), one delegate at a time, no recursive delegation, no file modification, same prompt template, output limited to 200 words. Order counterbalanced: odd cases run k1 first, even cases k2 first.
* **8 cases from real incidents** (`cases.json`, sha256 `7401531d61389594f8fe18fb53eb9717b126b189e853c8feec1af38ac95520d6`): D1 token figures later corrected, D2 receipts declared staged that are already recorded, D3 a retrieval route that failed, D4 a figure called unresolvable, D5 a battery copy, D6 a refused cleanup, D7 a qualified relation that could feed a consumer, D8 a function at risk of being rewritten. Kinds: 3 targeted at lessons that the consolidation moved (D4, D5, D6), 1 stale note (D2), 4 controls whose content the consolidation did not touch (D1, D3, D7, D8). Outcomes are hidden from the agent; the question gives the state, not the result.
* **Authorship limit, stated:** the cases, the rubric and the consolidation were written by the same actor. The rubric was written from the original sources and the lessons' own wording, not from the new section's text, and grading is done by a separate blind context that sees only the question, the rubric and the answer, with no condition label and no transcript.

## What is measured, separately

1. **Retrieval of the memory:** from the transcript of each run, whether the agent opened or ran any anchor path or command of the case (`anchors`), counted mechanically.
2. **Correctness of what it retrieved:** blind grader, per required fact: present and right / partial / absent or wrong.
3. **Use in the decision:** blind grader: the proposed action is acceptable and no forbidden action is proposed.
4. **Observable operational result:** blind grader: would a session following the answer reach the right outcome.
5. **Cost:** per run, from `session_model_census.py`: birth context, peak context, output, cache read, turns, wall time. Observed and estimated are kept apart; tokens are not converted to a share of a plan.
6. **Context consulted:** number of distinct repository files opened per run (from the transcript).

## How the result maps to a verdict (fixed now)

* **KEEP:** on the targeted cases B is better than A on use in the decision and on the operational result, with no loss on controls or on stale-note and qualification checks, and the cost of the consolidation and of its upkeep is small.
* **SIMPLIFY:** the benefit comes from a few links or from correcting existing notes. Keep only those and discard the rest.
* **INCONCLUSIVE:** with 8 cases per condition the difference cannot be told from noise or the cases sit at ceiling in both. Keep the cases and the reopening condition.
* **DISCARD:** no observable advantage, or B introduces a distortion, loses a qualification, or costs more than it saves.

No threshold is fixed beforehand beyond this; a difference of one case out of eight is reported as such. A shorter note that drops a decisive limit counts against B even if it is faster to read.

## Known limits of a retrospective replay

States are written after the incidents; the agent's tools can search the whole clone, so a good model may find an answer in either condition without a pointer. A run that finds the answer unaided in k1 shows that the memory was not needed for this model, not that it is useless for a weaker one. Eight cases and one model family. No real resumption of work on a new activity is part of this pilot unless it appears in the report.
