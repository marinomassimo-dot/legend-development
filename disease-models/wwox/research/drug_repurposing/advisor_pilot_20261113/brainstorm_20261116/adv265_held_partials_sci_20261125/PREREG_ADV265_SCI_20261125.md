# ADV-265 pre-registration: close the unread section classes of the held partials that carry the most consumers (SCI, 2026-11-25)

Written before any consumer count. Actor `orchestrator` (SCI). Hypothesis level; no spend, no contact, no e-mail address in any request; held bytes first, spaced requests only if a route is needed. Brief: `/home/desktop/.claude/jobs/a5e6f2ad/tmp/adv265.txt`. Not the sealed ADV-174 or ADV-175 material.

## Population
The 670 held partials of ADV-264: studies whose latest receipt is `partial_fulltext_read` and whose bytes are held (591 by ADV-219's name rule plus 79 by receipt digest; `population_adv264.tsv` and `held_under_other_names_adv264.tsv`, with the held-by-name set re-derived by the same code path as `recount_adv264.py`). The Tanna 2018 restoration (PMID 30370248, ADV-264) is recorded in the RESULT.

## Ranking rule (fixed now)
1. **Consumers.** Count the units that name the study by PMID, DOI or a registry id (PAPER, CORPUS, LIT) in: the claim registry, the card JSONs, the research-portfolio rows, the investigation rows of the rankings, the therapeutic-hypothesis ledger and the discovery-ledger leads, and the working model. Two routes per count: route 1 a `git grep` over the surfaces by identifier (file level), route 2 a record-aware split (unit level, as in ADV-256's `consumers_adv256.py`). The rank uses the route-2 unit count; a study with route 1 > 0 and route 2 = 0 or the reverse is flagged and resolved by reading the hits.
2. **Unread classes.** From the union of the study's receipts (best state per section): `discussion`, `figures`, `tables`, `supplementary` and `limitations` are "unread" when the best state is `not_read` or `captions_only`; `not_present` and `unavailable` are not counted. A study needs at least one unread class that the held bytes contain (ADV-219's scan rules) to enter the ranking.
3. **Order.** Consumers (descending), then number of unread classes among results-bearing ones (tables, figures, supplementary), then discussion; ties by PMID. The cut is the **top six**.

## What counts as completed
For each of the six: the unread classes read in the held bytes, each with a verbatim locator (page or section and a quote); a receipt (`FULLTEXT_READ_RECEIPT`) with honest coverage; a PAPER record candidate only if the coverage becomes complete; and, for each consumer unit, whether the newly read text **adds, narrows, contradicts or leaves unchanged** its wording.

## Prediction (fixed now)
* **3 of the 6 change at least one consumer's wording** (range 1 to 5). Basis: ADV-222's batch of held data sections narrowed or added in 4 of 7; ADV-216's three partials changed their maps.
* **The top six are not the six with the most unread classes** (the consumer count and the unread count are only weakly related): 0.7.
* **At least one of the six cannot be completed from held bytes** (a figure image or a supplement not in the held file): 0.5; it is then reported as partial with the section named, not extended by another route in this assignment.

## Out of scope
No claim, card or registry file is edited (wording is proposed to IT). No new acquisition unless a held byte is a stub (then one open route, spaced, recorded as a result). Two increments, about 120 minutes.
