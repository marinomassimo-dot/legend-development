# IT16 P2 pre-registration: does the module's intervention priority predict anything that can be checked outside the module?

Written 2026-11-01 before `predictive_it16_p2.py` was run. Non-canonical research material; not medical advice; a computational result is not therapeutic benefit. Public edition, WWOX-DEE genotype class, no individual-level record.

Disclosed before registration: I had already seen (a) the member_evidence table (7 of 64 members flagged tested_in_wwox_system = yes), (b) the general selection (8 units), (c) one PubMed query (2023-2026, WWOX with neural and treatment words: 25 hits) and the metadata of seven papers. Nothing below was tuned to a computed number; the numbers are not known.

## Question
Task type: hypothesis generation / probe selection ("which interventions should be tested next in a WWOX-deficient system"). The module's output for it is the general selection of `ranking_it8_p9_20261029/selections.tsv` (8 of 69 units). Does that selection (a) differ from what a WWOX-agnostic or trivial rule gives, and (b) have any outcome, independent of the module and later than the selection, against which it can be scored?

## Baselines (fixed)
- B0 random: 8 units drawn from the 69 (exact hypergeometric).
- B1 "known results first": order units by the number of WWOX-system assertions attributed to them (member_evidence.tsv, summed by unit), ties broken by unit id. This is the trivial rule "list what has already been tested".
- B2 "outside-WWOX only": the same pool ordered by outside-WWOX assertions, to show what a context-blind retrieval would pick.

## Data and split
Pool: the 69 units of `units.tsv` (file SHA-256 recorded by the script). Outcomes: the dated third-party WWOX-system results behind the units flagged tested = yes (`outcomes_it16.tsv`: PMID, publication date from PubMed metadata, system, kind of result). Split by publication date: freeze date 2026-10-29 (first snapshot of the ranking). Retrospective split (secondary, expected to be invalid and reported as such): dev = results up to 2021, eval = 2022 and later.

## Measures
1. Overlap: |module top-8 intersect tested|; |B1 top-8 intersect module top-8|; Kendall tau of module order against B1 order on shared items; module top-8 members that B1 would not select, with the module's stated reason.
2. Independence of outcomes: distinct origins (papers) behind the tested interventions (one origin counts once); results dated after the freeze date; kind of result (controlled perturbation vs case report); PubMed re-census 2026-10-29 to 2026-11-01 for new WWOX-system perturbation papers.
3. Circularity: is the candidate pool defined by the outcomes (a unit exists because its paper was read)? Count of tested units whose only WWOX-system evidence is the outcome paper itself.
4. Unknown handling: units with no WWOX-system result are 'no result', not 'negative' (count of untested units carrying a WWOX-system null/harm assertion); units whose evidence is class-level only.
5. Cost: curation rows, run time, network calls inside the script (none).

## Decision rules (stated before running)
- If independent post-freeze outcomes number fewer than 5, no accuracy, enrichment or benefit claim is made for the selection; the result is 'not measurable', with the denominator.
- If the pool is defined by the outcomes (measure 3 equals the number of tested units), the retrospective split is declared invalid for prediction and reported descriptively only.
- 'WWOX contribution' is reported as the choices in which the module's top-8 differs from B1 and B2 (inclusion, exclusion, order), each with the stated reason, and nothing else.
- 'No added value over B1 for the part that can be measured' is an acceptable outcome and will be written as such.
- Not counted as benefit prediction: recovery of known relations, identifier fixes, sign compatibility, agreement between copies of one source or between language models.

## Reopening
A third-party WWOX-system perturbation result for a unit dated after 2026-10-29, or at least 5 such results: `predictive_it16_p2.py evaluate --outcomes <tsv>` scores the frozen selection against B0/B1 without edits.
