# IT42 P2 — what the added source did and what the reasoning did (evaluation of retrieval and qualification)

Non-canonical working note. Not medical advice. Protocol fixed before execution: `eval_protocol_it42.md` (with dated addenda on scorer and engine defects found by the first run and by the independent check; criteria and the meaning of "improvement" unchanged). Code `eval_it42.py`; inputs `generation_it41_20261109/search_rows.tsv` built from the catalogue (ChEMBL 37; the DGIdb 2024-06-10 claims are **not** read by any path), GtoPdb 2026.3.1 and the Harness identity table. **This is an evaluation of retrieval and qualification, not of prediction.** Two limits are structural: the error criteria E1–E5 are checked by a scorer that shares facts with the guided path, so "B has no unflagged error" is true by construction and only the independent sample check (below) is evidence about correctness; and the sources used to build the method are not independent validation. Agreement is not accuracy.

## Results (`eval_results.tsv`, run 4; units are distinct molecules after cross-source merging through the catalogue parent and with radiolabelled forms dropped in every path)

| Q | path | rows | units | clean | E1 dir | E2 site | E3 subunit | E5 id | units with unflagged error | ref. positives | UNKNOWN verdict | candidates with named unknown fields | excluded with reason |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | A0 | 28 | 24 | 4 | 3 | 20 | 0 | 0 | 20 | 4/6 | 0 | 0 | 0 |
| Q1 | A1 | 59 | 55 | 7 | 12 | 46 | 1 | 0 | 48 | 4/6 | 0 | 0 | 0 |
| Q1 | B | 8 | 7 | 7 | 0 | 0 | 0 | 0 | 0 | 4/6 | 1 | 3 | 47 |
| Q2 | A0 | 39 | 7 | 2 | 5 | 0 | 0 | 0 | 5 | n/a | 0 | 0 | 0 |
| Q2 | A1 | 84 | 29 | 18 | 11 | 0 | 0 | 0 | 11 | n/a | 0 | 0 | 0 |
| Q2 | B | 41 | 18 | 18 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 | 11 |
| Q3 | A0 | 488 | 71 | 68 | 3 | 0 | 0 | 0 | 3 | n/a | 0 | 0 | 0 |
| Q3 | A1 | 640 | 115 | 94 | 21 | 0 | 0 | 0 | 21 | n/a | 0 | 0 | 0 |
| Q3 | B | 541 | 91 | 91 | 0 | 0 | 0 | 0 | 0 | n/a | 3 | 0 | 26 |
| Q4 | A0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 | 0 |
| Q4 | A1 | 6 | 6 | 4 | 2 | 0 | 0 | 0 | 2 | n/a | 0 | 0 | 0 |
| Q4 | B | 4 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 | 2 |
| Q5 | A0 | 2 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 | 0 |
| Q5 | A1 | 15 | 14 | 14 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 | 0 |
| Q5 | B | 15 | 14 | 14 | 0 | 0 | 0 | 0 | 0 | n/a | 0 | 0 | 0 |
| Q6* | A0 | 74 | 15 | 9 | 6 | 0 | 0 | 0 | 6 | n/a | 0 | 0 | 0 |
| Q6* | A1 | 193 | 55 | 25 | 29 | 0 | 0 | 1 | 30 | n/a | 0 | 0 | 0 |
| Q6* | B | 84 | 25 | 25 | 0 | 0 | 0 | 0 | 0 | n/a | 1 | 0 | 29 |

Reference positives exist only for Q1 (six tools named by primary readings of earlier packages). "Units with unflagged error": a path returned an item with at least one of E1–E5 without saying so (A0 and A1 never say; B excludes it, or marks it UNKNOWN, or names the missing field). Q6\* is post hoc (addendum 2).

## A — the added source (A1 against A0)

Clean units: 4 → 7 (Q1), 2 → 18 (Q2), 68 → 94 (Q3), 0 → 4 (Q4), 2 → 14 (Q5); units with an unflagged error rise in step: 20 → 48 (Q1), 5 → 11 (Q2), 3 → 21 (Q3), 0 → 2 (Q4), 0 → 0 (Q5). Reference positives: **no gain** (4 of 6 in both; ifenprodil and Ro 25-6981 are in neither table). The second source is mostly coverage, and it brings its own misleading items with it: for Q1 a simple two-source search presents 55 units of which 48 carry an unflagged error.

## B — relational qualification on the same universe (B against A1)

Units with an unflagged error: 48 → 0 (Q1), 11 → 0 (Q2), 21 → 0 (Q3), 2 → 0 (Q4), 0 → 0 (Q5). **No clean unit is lost without a record**: the units that are clean for the scorer but not in B's shortlist (3 in Q3: flumazenil, an alpha-3 ligand, etazolate) are kept as UNKNOWN (direction unclear, or mixed rows) or EXCLUDED with their reason (`eval_lost_candidates.tsv`). Reference positives kept: 4 → 4. Unknowns kept with a reason: Q1 1 UNKNOWN verdict (the DQP-1105 row: assay text names GluN2C) and 3 candidates with a named missing field (receptor site); Q3 3 UNKNOWN verdicts. Excluded with a recorded reason: 47 (Q1), 11 (Q2), 26 (Q3), 2 (Q4). **Q5 is the case where reasoning adds nothing**: every returned row is an inhibitor of the right targets, so B equals A1; its value is the source (2 → 14 units) and the role assignment in the public list.

## Post hoc case Q6\* (identity), reported apart

Relation S8 (AMPA/kainate antagonism) was added for the P1 trace (addendum 2). A0 returns 15 units, A1 55 with 30 carrying an unflagged error including **one identity error** (the GtoPdb label GYKI53784, which the identity table flags as a label conflict); B returns 25 clean units, flags the GYKI53784 rows UNKNOWN (label conflict) and keeps the distinct structure GYKI53655 as a candidate. It is the only question in which E5 catches anything.

## Independent sample check (a reader with the originals; `verify/VERDICTS.md`)

41 rows sampled from the strata of the first run: 0 verdicts wrong against the relation's columns and the GtoPdb and catalogue originals; the one stratum the sample missed (76 ChEMBL rows excluded for direction) was read in full by the verifier: all correct. The check also found three defects that were then fixed (the engine returned CANDIDATE on a branch that should be UNKNOWN — 84 rows affected; units were not merged across sources — 0 of the GtoPdb rows had a catalogue id; radiolabelled forms were counted); the numbers above are after those fixes.

## Reading

* The added source gave the *coverage*; the qualification gave the *protection against misleading items*. Neither finds the two tools missing from both tables.
* "Clean" is not a nomination: Kv7 openers are clean units in Q2 (18) and the right output remains **abstention** (cases.md Case 4).
* Cost: catalogue load and index 4.0 s (shared), one-symbol ChEMBL lookup 0.01 ms, GtoPdb table read 0.12 s, qualification of the rows a few milliseconds. The guided path costs nothing material after the first load; what it changes is reading burden: for Q3, 640 rows / 115 units for a reader of A1 against 91 shortlisted units, 3 unknown and 26 excluded with a reason; for Q1, 59 rows / 55 units against 7 shortlisted units, 1 unknown, 3 with a named missing field and 47 exclusions with a reason.
* No graph propagation is used, so no graph baseline or specificity control applies.

## Limits

Five pre-fixed questions plus one post hoc, one reference list (Q1 only), no outcome independent of the construction of the sources; the guided rules are the relation's own columns plus the identity table, so a mis-specified relation row would be mis-applied uniformly; DGIdb claims for the S6/S7 genes are not read by any path (the statement "A1 returns every row a careful analyst would start from" in the protocol is withdrawn for them).
