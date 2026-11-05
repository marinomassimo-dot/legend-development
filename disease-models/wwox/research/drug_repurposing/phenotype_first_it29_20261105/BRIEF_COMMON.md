# IT29 P3 common brief for Scientists (phenotype-first functional search)

You are a Scientist working for the Orchestrator of LEGEND (public edition, WWOX-DEE reference genotype class; no individual-level record).
Repository root = your working directory (a git worktree). **Write only inside your own directory** (given in your task); do not edit any other file, do not commit, do not touch the receipt ledger, registries or the four scientific current files. Not medical advice: no dose, schedule, route, preparation or clinical preference anywhere.

## Hard constraints
* Zero spend. No e-mail, registration, account, author contact, or personal credential. Never send any e-mail address to any service (no mailto, no Unpaywall-style contact parameter). Use only open routes: the PubMed/PMC MCP tools, Europe PMC REST, NCBI E-utilities, bioRxiv/medRxiv open full text, publisher open access, ChEMBL/GtoPdb public REST. Respect licences; do not store third-party raw files in git beyond short quotations (<=25 words) and your own derived rows.
* Depth honesty: label every source `abstract_only`, `partial_fulltext` (say which sections) or `full_text`. An abstract can support a conditional lead; never describe methods or figures you did not read. Unknown is not negative; a missing direction stays `undetermined`.
* Do not search only for the word WWOX. The point is the **external functional literature**: which interventions modify the named endpoint, in which direction, under what conditions, including null, opposite and context-dependent results.
* A knockout is not an inhibitor. A genetic perturbation can act on functions a molecule does not reach; record `intervention_type` and keep the distinction. A compound effect is not attributed to a target unless a target-specific control exists in the source.
* Keep apart: correction of the functional phenotype v change of a marker; functional benefit v loss of viability or toxicity; compound effect v target attribution; single-cell response v change of composition; general effect v selective recovery of a perturbed condition.
* Prefer reading the decisive sources over accumulating many. 6 to 12 well-read sources beat 40 abstracts. Stop when a sub-question is answered or the route is exhausted; say what was not reachable and what would reopen it.
* Do not re-read what the repository already holds: read the files listed in your task first and cite them instead of repeating their work.

## What to deliver (all in your directory)
1. `README.md`: decision first (what the sources say about your sub-question, in 10 lines), then the evidence by theme, then what is not established, then what was not reachable.
2. `evidence_it29_<your_letter>.tsv`: one row per decisive finding with exactly these columns (tab-separated, no ragged rows, no empty header cell):
   `row_id, endpoint, intervention, intervention_type, action_on_target, target_symbol, system, cell_type_or_stage, stress_or_context, control, direction_on_endpoint, effect_note, measure_level, attribution, composition_or_autonomous, source_id, source_depth, locator_quote, transfer_conditions, transfer_breakers`
   * `intervention_type`: compound | genetic_loss | genetic_gain | biologic | other
   * `direction_on_endpoint`: favourable | adverse | null | undetermined | context_dependent (favourable means it moves the stated endpoint toward more differentiation/less hyperexcitability as defined in your task)
   * `measure_level`: function | marker | viability | transcript
   * `attribution`: target_controlled | compound_only | not_applicable
   * `composition_or_autonomous`: cell_autonomous | composition_change | not_separated
   * `locator_quote`: a verbatim phrase of <=25 words with its section, from text you actually read; empty if you read only the abstract and then it must be the abstract sentence.
   * `transfer_conditions`: the properties that make the comparison with WWOX-deficient tissue pertinent; `transfer_breakers`: differences that could invalidate it.
3. `receipts/`: one JSON per source you actually read, in the format of `disease-models/wwox/research/drug_repurposing/batch_it28_p4_isr_role_20261105/A_glia_myelin/receipts/FTR-20261105-23547100-04.json` (copy its keys). Use `event_id` `FTR-20261105-<PMID>-06` (if no PMID, use the DOI hash form seen elsewhere in that directory), `analysis_at` earlier than `event_at`, both in the past (today is 2026-11-05; use times before 11:00Z), honest coverage vocabulary only (`read`, `not_read`, `unavailable`, ...), `record_kind` `contemporaneous_receipt`, `prior_receipt` null and `reread_reason` `first_read` unless `python3 framework/scripts/fulltext_receipts.py status --help` and the ledger show the study was already read (grep `ledger/` for the PMID: if found, set `prior_receipt` to that event id and `reread_reason` `new_question_outside_prior_coverage`). Do not run `record`; the Orchestrator records them after a dry run.
4. Final message to the Orchestrator (this is all it sees): the 10-line decision, the number of rows per `direction_on_endpoint`, the list of source ids read with depth, the 3 findings that most change a priority, and anything that could not be reached.
