# IT42: separating the added source from the reasoning, and following the results to the decisions

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. **Evaluation of retrieval and qualification and of consumption; no predictive validation exists.**

| Piece | File | What it shows |
|---|---|---|
| P0 | `ledger/tasks/orchestrator/ORCH-ROADMAP-IT42-20261110.json` | record of the whole queue; IT41 reconciled (local main = remote = f7305230; CI of e2dbe391 success; IT41 batteries by SHA in its record) |
| P1 | `trace_it42.md`, `test_trace_it42.py` | three cases from relation to public page; which output was only exported and what now reads it; a consistency gate between the engine's verdicts and the kinds shown |
| P2 | `eval_protocol_it42.md` (fixed first), `eval_it42.py`, `eval_results.tsv`, `eval_summary.md`, `eval_table.md` | A (added source) against B (relational qualification) on the same universe; two scorer defects found and recorded as addenda |
| P3 | `provenance_it42.md` | onfasprodil and NP10679: provenance, roles, what moves them; two reconstruction corrections (one datum in three representations; an activity id that is not a PMID) |
| P4 | `apply_p4.py`, `test_stage_it42.py` | the IT41 corrections propagated to INV-05 and the comparator table; the smallest regressions |
| P5 | `second_relation_it42.md` (before the search), relation S7 | supply-side GABA lever; the relation ran through the same table and code, with the qualification columns as data |
| P6 | `compound_view.tsv` (12 items, new fields moves/where/identity), view code and five-language strings | public list of compounds and hypotheses in research order |
| P7 | `../next_batch_it42_20261110/BRIEF.md` | the next scientific brief: supply, response or chloride gradient |

Key results are in `eval_summary.md`. In one line: the added source gave the coverage (clean units 4 → 7, 2 → 18, 68 → 101, 0 → 4, 2 → 15 over five questions); the qualification removed every misleading item without losing a clean unit (units with an unflagged error 56, 11, 24, 2, 0 → 0) and kept the unknowns with a reason; it recovered no reference positive that the tables do not hold (ifenprodil and Ro 25-6981 are in neither), and for the unambiguous S7 it changed nothing.

## Added after the science deliveries (SCI42), 2026-11-10

* **Onfasprodil and NP10679** (primary sources, d3a57a65): onfasprodil weakened from "emerged" to **unresolved** (no site, maximum, triheteromer result or measured selectivity in any source reached); NP10679 **probe**, subordinate to a measured tissue pH. The tissue pH joins the measured conditions (map row IT42-Q01). No entry of the public list is "emerged" any more; no choice of the first INV-05 experiment changed.
* **DQP-1105** (f84ee77b): resolved at source: the registry GluN2B and GluN2C rows are micromolar numbers stored as nanomolar; excluded from the GluN2B comparison. The IT41 reading ("a subunit transfer avoided") was the symptom, not the cause: **a registry value under a target can fail by unit as well as by subunit**.
* **Chloride gradient** (f84ee77b): **undetermined**; the only inhibitory recording used a 140 mM KCl pipette at −70 mV and cannot report the native gradient; order of the inhibitory minimum experiment M03 → M01 → M02 (INV-15 `next_test`; entry V11 follows it); map rows IT42-Q02 and Q03.
* **Identity** (Harness 871f7ffa): the identity table covers the names of the public list; the join uses `compound_identity.join_names` (no substring fallback); NOT_FOUND_BY_NAME counts as unverified; badges: 4 verified-by-name families, 1 label conflict (GYKI), 5 unverified (d-APV by name, DQP-1105, the GABA tools), 1 partial.
