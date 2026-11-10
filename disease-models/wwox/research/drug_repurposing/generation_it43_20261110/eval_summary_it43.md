# IT43 P4: what the evaluation shows (protocol `eval_protocol_it43.md`; figures `eval_results.tsv`)

Non-canonical working note. Not medical advice. No predictive validation. Questions not used in IT42: Q7 (S2 HCN), Q8 (S4 connexin/pannexin), Q9 (S9 PDK inhibition).

| Question | A0 units | A1 units (clean) | A2 adds (typed) | Unflagged-error units A1 -> B | B keeps | Clean lost without record |
|---|---|---|---|---|---|---|
| Q7 S2 | 2 | 16 (12) | 3 (1) | 4 -> 0 | 12 candidates, 4 excluded with reason | 0 |
| Q8 S4 | 0 | 5 (5) | 1 (1) | 0 -> 0 | 5 | 0 |
| Q9 S9 | 1 | 3 (3) | 6 (0) | 0 -> 0 | 3 conditional | 0 |

**Source value.** Large: 2 -> 16, 0 -> 5 and 1 -> 3 units from adding the curated interaction table; the DGIdb listing adds 10 more units, 2 with a typed action, all UNKNOWN by rule. Known compounds reached show path coverage, not prediction.
**Qualification value.** Small on these three questions: it removes the 4 wrong-direction units of S2 (the independent reader confirmed the four activators of its 30-row sample were opposite to a blocker) and nothing in S4 and S9, where the typed rows were already clean. It kept the unknowns and removed none of the clean ones.
**Generation value (S9).** The path reached a reference, a second chemotype and an isoform-bias tool, all kept conditional on an unmeasured premise (no abstention was needed and none was manufactured); it did not produce a favourable candidate, and it surfaced a safety flag and a symbol trap.

**Independent reader (`verify/VERDICTS.md`).** 4 of 4 activators in the 30-row sample are the engine's excluded rows (agreement). Disagreements with the engine's picture, kept as findings: (1) three inorganic ions (a monovalent cation and two divalent ions) are returned as candidates in S2 and count among its 12 clean units: not drug candidates; an implementable flag (`non_drug_entity`) is not yet in the engine; (2) the parent molecule and its salt of one drug appear as separate rows (merged by the catalogue parent in the unit count, listed twice as rows); (3) one HCN-blocker series is isoform-mismatched (the compound is HCN1-preferring, the rows are on other isoforms), which the relation did not specify; (4) species "human" for one S9 compound is not supported by its abstract. No clean unit was found wrongly excluded.
**Limits.** The scorer copies the IT42 rules and shares facts with the engine; the sample is 30 of the S2/S4 rows and every S9 row; no reference positives exist for these questions; no graph step was used, so no graph baseline applies.
