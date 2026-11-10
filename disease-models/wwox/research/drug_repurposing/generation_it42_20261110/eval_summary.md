# IT42 P2 — what the added source did and what the reasoning did (evaluation of retrieval and qualification)

Non-canonical working note. Not medical advice. Protocol fixed before execution: `eval_protocol_it42.md` (with two dated addenda on scorer defects, both of which first made the paths look *different from what they were*; criteria unchanged). Code `eval_it42.py`; inputs `generation_it41_20261109/search_rows.tsv` built from the catalogue (ChEMBL 37, DGIdb 2024-06-10 download), GtoPdb 2026.3.1 and the Harness identity table at the commit of the run. **This is an evaluation of retrieval and qualification, not of prediction**: the sources used to build the method are not independent validation, the error criteria are checked from source fields by a scorer that shares facts with the guided path (see the independent sample check below), and agreement is not accuracy.

## Results (`eval_results.tsv`, run 3)

| Q | path | rows | units | clean | E1 dir | E2 site | E3 subunit | E5 id | units with unflagged error | ref. positives | UNKNOWN kept | excluded with reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | A0 | 28 | 24 | 4 | 3 | 20 | 0 | 0 | 20 | 4/6 | 0 | 0 |
| Q1 | A1 | 67 | 63 | 7 | 13 | 54 | 1 | 0 | 56 | 4/6 | 0 | 0 |
| Q1 | B | 8 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 4/6 | 1 | 55 |
| Q2 | A0 | 39 | 7 | 2 | 5 | 0 | 0 | 0 | 5 | n/a | 0 | 0 |
| Q2 | A1 | 84 | 29 | 18 | 11 | 0 | 0 | 0 | 11 | n/a | 0 | 0 |
| Q2 | B | 41 | 18 | 18 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 11 |
| Q3 | A0 | 488 | 71 | 68 | 3 | 0 | 0 | 0 | 3 | n/a | 0 | 0 |
| Q3 | A1 | 671 | 125 | 101 | 24 | 0 | 0 | 0 | 24 | n/a | 0 | 0 |
| Q3 | B | 567 | 101 | 101 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 30 |
| Q4 | A0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 |
| Q4 | A1 | 6 | 6 | 4 | 2 | 0 | 0 | 0 | 2 | n/a | 0 | 0 |
| Q4 | B | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 2 |
| Q5 | A0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 |
| Q5 | A1 | 16 | 15 | 15 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 |
| Q5 | B | 16 | 15 | 15 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 |

Reference positives exist only for Q1 (six tools named by primary readings of earlier packages); "units with unflagged error" counts units for which a path returned an item with at least one of E1–E5 without saying so (A0 and A1 never say; B excludes or marks UNKNOWN).

## A — the added source (A1 against A0)

Coverage: clean units 4 → 7 (Q1), 2 → 18 (Q2), 68 → 101 (Q3), 0 → 4 (Q4), 2 → 15 (Q5). The second source also brings errors with it, in larger absolute number than clean units in Q1 (+36 units with an unflagged error against +3 clean) and in Q3 (+21 against +33). Reference positives: **no gain** (4 of 6 in both; ifenprodil and Ro 25-6981 are in neither table). The source effect is mostly coverage, and a simple search on the two sources is not credible as an answer: for Q1 it presents 63 units of which 56 carry an unflagged error.

## B — relational qualification on the same universe (B against A1)

Units with an unflagged error: 56 → 0 (Q1), 11 → 0 (Q2), 24 → 0 (Q3), 2 → 0 (Q4), 0 → 0 (Q5). **Clean units lost: 0** (`eval_lost_candidates.tsv` is empty in run 3; run 1's six apparent losses were a scorer defect, kept in the addendum). Reference positives kept: 4 → 4. Unknowns kept with a reason: 1 in Q1 (the DQP-1105 row, assay text names GluN2C), not turned into a negative. Excluded with a recorded reason: 55 (Q1), 11 (Q2), 30 (Q3), 2 (Q4). **Q5 is the case where reasoning adds nothing**: every returned row is an inhibitor of the right targets, so B equals A1; the value of Q5 is the source (2 → 15 units) and the role assignment in the compound view, not the filter.

## Reading

* Most of the *coverage* gain comes from the added source; most of the *protection against misleading items* comes from the qualification. Neither finds the two tools that are missing from both tables.
* "Clean" means the unit passes E1–E5; it is not a nomination. Kv7 openers are clean units in Q2 (18) and the right output remains **abstention** (cases.md, Case 4): nomination is a separate state of the hypothesis.
* Cost: catalogue load and index 4.0 s (shared by all paths), one-symbol ChEMBL lookup 0.01 ms, GtoPdb table read 0.12 s, qualification of 892 rows 4 ms. Computing the guided path costs nothing material after the first load; what it changes is reading burden: for Q3, 671 rows / 125 units for a reader of A1 against 101 shortlisted units plus 30 excluded with a reason for B; for Q1, 67 rows / 63 units against 7 shortlisted units, 1 unknown and 55 exclusions with a reason.
* No graph propagation is used, so no graph baseline or specificity control applies.

## Limits

Five questions, one reference list, no outcome independent of the construction of the sources; the guided rules are the relation's own columns (`wanted_direction`, `site_policy`, `subunit_in`, `subunit_out`) plus the identity table, so a mis-specified relation row would be mis-applied uniformly. A sample check by a reader with the originals (below) is the independent part.
