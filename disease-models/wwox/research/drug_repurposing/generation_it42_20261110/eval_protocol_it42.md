# IT42 P2 — protocol: separating the effect of an added source from the effect of relational qualification

Non-canonical working note. Not medical advice. **Fixed before execution (2026-11-10).** Any change after the first run is a dated addendum; results are not used to rewrite the questions, the criteria or the meaning of "improvement".

## Inputs and versions (frozen)

Catalogue `catalog/catalog.jsonl.gz` (ChEMBL_37 2026-05-01, DGIdb 2024-06-10 download in the catalogue); GtoPdb 2026.3.1 `interactions.csv` (cache); `generation_it41_20261109/relations_it41.tsv` rows S1–S7; the identity table `identity_it41_20261109/identity_table.tsv` at the commit of the run; code `action_search.py` at the commit of the run. No new network call is made by the evaluation.

## Questions (small, contrasting)

| Q | Relation | Why it is in the set |
|---|---|---|
| Q1 | S1 GluN2B-directed negative modulation | the main case; symbol lookups mix site classes and subunit assays |
| Q2 | S3 Kv7 opening | a case where the right output is mostly abstention |
| Q3 | S5 GABA-A positive modulation | a large family where direction is the main trap |
| Q4 | S6 chloride-gradient control (NKCC1 block, KCC2 enhancement) | a case where the wanted action has no record |
| Q5 | S7 raising GABA availability (GAT-1, GABA transaminase) | the new relation of P5, chosen before search |

## Paths

* **A0 — previous-source simple search:** all ChEMBL curated-mechanism rows for the target symbols of the relation (the IT40/IT41 baseline). No filtering.
* **A1 — two-source simple search:** A0 plus all GtoPdb interaction rows for the same symbols. No filtering.
* **B — action- and context-guided search on the same two sources:** A1 passed through the relation's wanted direction, the site/granularity class of the record, the subunit named by the assay text, cross-source merging by catalogue parent and the identity label-conflict flag, with every excluded row kept with its reason and every row that cannot be classified kept as UNKNOWN (not as negative).

The simple baselines are credible: A1 returns every row a careful analyst would start from. They are not scored zero for lacking a narrative; they are scored on the same objective criteria.

## Units and criteria (checkable from the source rows, not from the path's own rules)

Unit = one distinct parent molecule returned for a question (cross-source merged for scoring; the paths differ in whether they merge, which is itself measured as duplicate counting).

Error types, defined from source fields:
* **E1 direction error** — the recorded action is the opposite of the wanted one (agonist or positive modulator for a blocking question, and the reverse). Inverse agonists count as reducing.
* **E2 site-class error** — for a question about allosteric or subunit-directed modulation, the record is an orthosteric ligand, a channel blocker, or a family record whose subunit is unresolved, presented as if it were subunit-directed.
* **E3 subunit-transfer error** — the assay text of the row names a subunit different from the one the row sits under.
* **E4 duplicate** — the same parent molecule counted more than once (salts, stereoisomers, radiolabelled forms, cross-source copies).
* **E5 identity error** — the name resolves to a record that carries a label conflict in the identity table, or to no record carrying the intended target.
A returned unit is **clean** if it has none of E1–E5; **flagged** if it has at least one and the path says so; **unflagged error** if it has one and the path does not say so.

Reference positives (fixed list, from primary readings of earlier packages, not from the two tables): for Q1 radiprodil, traxoprodil, rislenemdaz, EVT-101 (ChEMBL assembly record), ifenprodil, Ro 25-6981 (primary-paper tools of the INV-05 packages). For the other questions no reference positive list exists, so recall is **not scored** there.

Unknowns: a unit for which a criterion cannot be evaluated (no assay text, no site recorded, no identity row). Preserved = listed as UNKNOWN with the missing field named; lost = dropped or silently classed as clean or as negative.

## Measures

1. Per path and question: units returned; clean; flagged; unflagged errors by type (E1–E5); reference positives returned.
2. **A (source effect)** = A1 − A0 on the same measures.
3. **B (qualification effect)** = B − A1 on the same measures, same universe.
4. Candidates lost by B = reference positives or clean units present in A1 and absent from B's shortlist without an UNKNOWN or exclusion record.
5. Unknowns preserved / lost.
6. Useful experimental comparisons: the number of units entering a comparison with a stated role (candidate, mechanism comparator, condition probe, control) that satisfy the necessary conditions fixed in `cases.md`.
7. Cost: wall-clock seconds to a usable shortlist per path (measured by running the code), rows a reader must open (A0/A1: all returned; B: shortlist + exclusion records counted separately), and the human/agent interventions needed.

## Meaning of "improvement"

B improves on A1 if, on the same universe, unflagged errors are lower, no reference positive or clean unit is lost without a record, and unknowns are preserved. A1 improves on A0 if it returns more reference positives or clean units without more unflagged errors per unit. Neither is a statement about prediction: the sources used to build the method are not independent validation; the result is an **evaluation of retrieval and qualification**. Agreement between paths or between agents is not accuracy.

## Not done on purpose

No graph propagation is used here, so no graph baseline or specificity control applies; if graph propagation is introduced later, the existing controls (simple baselines, specificity) apply then.

## Addendum 1 (2026-11-10, after the first run; the criteria and the meaning of "improvement" are unchanged)

The first run of `eval_it42.py` (kept as `eval_results_run1.tsv`, `eval_lost_candidates_run1.tsv`) listed six units as "clean but lost by B" in Q3: etifoxine, flumazenil, CGS8216, ZK93426, bicuculline, gabazine. All six are antagonists or inverse agonists in a question about positive modulation and B excluded them correctly; the evaluator's own E1 test had treated them as clean because its pattern for an agonist matched inside the word "antagonist". This is a defect of the scorer, not a change of criterion. The pattern was fixed (a word is an agonist only if not preceded by "ant" or "inverse "); `eval_results.tsv` is run 2. Neither path was tuned: the fix lowers the apparent quality of A0 and A1 and removes a false loss of B.

Addendum 1b (same day): a second scorer defect surfaced by the one remaining "lost" unit (CGS8216, GtoPdb type "Agonist", action "Inverse agonist"): the scorer read the type and the action together. The scorer now reads the action part of the field (after the slash) and falls back to the type part only when the action part is empty or 'None' (a channel blocker has action 'None'). Criteria unchanged; `eval_results.tsv` is run 3, runs 1 and 2 outputs are kept in this folder's history.

Addendum 2 (2026-11-10): relation S8 (AMPA/kainate antagonism) was added to the relations table for the P1 identity trace (the ambiguous-identity case). It is scored as **Q6\*, post hoc**, outside the pre-fixed set of five questions, and reported apart: it is the only question in which criterion E5 (identity) has anything to catch.

Addendum 3 (2026-11-10, after the independent sample check): (a) the engine's `qualify()` returned CANDIDATE on a branch that its docstring assigns to UNKNOWN (84 rows, mainly unknown direction); fixed: an unevaluable direction is now UNKNOWN (direction_unclear); a missing field that a check needs is named in `unknown_fields` and the row stays CANDIDATE; the `assay_text` flag is raised only when the relation fixes a subunit check. (b) Units were not merged across sources (no GtoPdb row carried a catalogue id); the GtoPdb ligand is now joined to the catalogue parent through its name when the name reaches exactly one parent, and radiolabelled forms are dropped in every path; the numbers of run 4 are after this. (c) The sentence in this protocol that A1 "returns every row a careful analyst would start from" is withdrawn: the DGIdb claims are in the catalogue but are read by no path. (d) "Unknowns preserved" is reported in two columns: UNKNOWN verdicts and candidates with a named missing field. Criteria and the meaning of improvement are unchanged; runs 1–3 are superseded and were not tuned to either path.
