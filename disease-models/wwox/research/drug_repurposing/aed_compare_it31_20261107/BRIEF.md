# Brief: antiseizure comparators for the seizure-control cards (P8, IT31)

Read `../batch_sci_20261105/BRIEF_COMMON.md` first; it binds (open routes only, no e-mail address to any service, no administered-dose numbers, depth honesty, write only in your folder, stage receipts and never record them, wording rules). `framework/protocols/delegation_budget.md` sections 2 and 7 bind you: you start no agents. Before opening any PMID check the receipt ledger depth (`framework/scripts/fulltext_receipts.py`, query by PMID) and do not reread a source already read beyond abstract unless you need a new detail.

**Question.** For the seizure-control thread, what separates the antiseizure agents a clinician already knows, and which of them has a WWOX-specific reason to be studied, as distinct from general antiseizure activity? Agents: ethosuximide, levetiracetam, perampanel (and any other agent named in WWOX-related DEE reports you find in the module's A1 table).

**Three separate columns, never merged.** (1) General antiseizure activity: one primary or review source for the mechanism and the seizure types it is used for. (2) WWOX-specific rationale: only what the module records already hold (cards, `needs/needs.json`, `batch_sci_20261105/a1_wwox_reports/`, investigations INV-03/04/05/09/10); name model, endpoint, limits and counter-evidence. If a record holds none, write NONE_HELD, not a negative. (3) Comparative advantage actually demonstrated head to head, in WWOX or in any model: expected NONE for most pairs; say what was searched.

**Mechanism contrast to state, from sources.** ethosuximide: T-type calcium channel; levetiracetam: synaptic vesicle protein SV2A, not the same mechanism; perampanel: non-competitive AMPA receptor antagonist, not an NMDA receptor modulator. A more potent or more selective analogue is not better without context, exposure and safety.

**Usage figures.** Any percentage of children with a WWOX-related DEE who receive an agent must carry its source and denominator or be dropped. Use the A1 `cases_a1.tsv` and `denominators_a1.tsv` first; do not extend them by new reading unless a named report is missing. Count children once across reports.

**Domains kept apart.** seizure control, development, network function, myelin, quality of life: one result on one is not carried to another. Track A (variant-independent) and Track B (variant- or lesion-dependent) stay separate; so do broad recovery and partial benefit.

**Work, bounded.** At most 8 full-text or abstract sources beyond what the module holds; stop when answered or exhausted; if a source is unreachable say so (not a negative).

**Deliverables in `aed_compare_it31_20261107/output/`:** `README.md` (answer first, at most one page, every statement DATO / INFERENZA / IPOTESI), `comparison.tsv` (agent, column, statement, source_pmid_or_record, locator_quote_max25words, source_depth, note), `queries.tsv`, `receipts/` with staged receipts (suffix `31`) and `INDEX.tsv`. No dose, schedule or preference between agents; no clinical recommendation.

**Consequences fixed before you read.** If a WWOX-specific rationale exists for an agent, it becomes a candidate row for the comparator field of the seizure card(s) with its endpoint and limits; if none, the card keeps general-activity wording only; any usage percentage without a source is removed from consumers.

Final message: what you completed, what you could not reach, and the setting you ran under as you can see it.
