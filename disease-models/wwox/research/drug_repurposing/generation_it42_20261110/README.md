# IT42: separating the added source from the reasoning, and following the results to the decisions

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. **Evaluation of retrieval and qualification and of consumption; no predictive validation exists.**

| Piece | File | What it shows |
|---|---|---|
| P0 | `ledger/tasks/orchestrator/ORCH-ROADMAP-IT42-20261110.json` | record of the whole queue; IT41 reconciled (local main = remote = f7305230; CI of e2dbe391 success; IT41 batteries by SHA in its record) |
| P1 | `trace_it42.md`, `test_trace_it42.py` | three cases from relation to public page; which output was only exported and what now reads it; a consistency gate between the engine's verdicts and the kinds shown |
| P2 | `eval_protocol_it42.md` (fixed first), `eval_it42.py`, `eval_results.tsv`, `eval_summary.md`, `eval_table.md` | A (added source) against B (relational qualification) on the same universe; two scorer defects found and recorded as addenda |
| P3 | `provenance_it42.md` | onfasprodil and NP10679: provenance, roles, what moves them; two reconstruction corrections (one datum in three representations; a reference field that is not a PMID) |
| P4 | `apply_p4.py`, `test_stage_it42.py` | the IT41 corrections propagated to INV-05 and the comparator table; the smallest regressions |
| P5 | `second_relation_it42.md` (before the search), relation S7 | supply-side GABA lever; the relation ran through the same table and code, with the qualification columns as data |
| P6 | `compound_view.tsv` (12 items, new fields moves/where/identity), view code and five-language strings | public list of compounds and hypotheses in research order |
| P7 | `../next_batch_it42_20261110/BRIEF.md` | the next scientific brief: supply, response or chloride gradient |

Key results are in `eval_summary.md`. In one line: the added source gave the coverage (clean units 4 → 7, 2 → 18, 68 → 101, 0 → 4, 2 → 15 over five questions); the qualification removed every misleading item without losing a clean unit (units with an unflagged error 56, 11, 24, 2, 0 → 0) and kept the unknowns with a reason; it recovered no reference positive that the tables do not hold (ifenprodil and Ro 25-6981 are in neither), and for the unambiguous S7 it changed nothing.
