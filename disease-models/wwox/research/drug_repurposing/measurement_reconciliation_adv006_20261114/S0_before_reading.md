# ADV-006 S0 — frame fixed before the tables were read (2026-11-14)

Non-canonical. Not medical advice; no dose, schedule, route or preference for any drug; nothing phrased as advice for a child. Written before the source tables were opened beyond their summaries; what I had seen is only the assignment text, `open_questions_map.tsv` lines 121-123 (truncated) and the folder survey (nine `new_measurements.tsv` files, no folder named for a consolidation).

## What I had and had not checked
* Own unlanded work on this axis: none (worktrees `adv`, `adv004` detached and integrated; `it*` are other actors').
* Receipts ledger: no source of this package is a new full-text read; if one is opened it gets a staged receipt.
* A consolidation artefact: a folder survey found none by name. **Not searched by content:** the August commit candidates `CC-20260826-EGABA-ANALYSIS-PLAN-01`, `-EGABA-EXPERIMENT-01` and `-EGABA-CLOSURE-01` (they name "perforated" and may already specify an E_GABA recording; the producer reads them as sources, and if one is a full specification the result is "a specification already exists", stated and stopped).
* A name collision seen before reading: `open_questions_map.tsv` IT42-Q01 points at `glun2b_comparators_sci42_20261110/output/new_measurements.tsv#M01` (tissue pH) while SCI42's own chloride table also has an `M01` (E_GABA). Two measurements share an id.

## Definitions (fixed now)
* **Request:** one row (or one stated step) in a source that asks for a recording, comparison or readout not yet in hand. A source row that only describes a recording already published is not a request.
* **Same measurement:** two requests whose answer one recording session could give without changing any of: preparation (species, region, layer/cell type, age bin, genotype arms), recording mode and configuration (e.g. whole-cell/perforated, pipette chloride), the quantity read, the condition that changes that quantity (antagonists and their identity, temperature, pH, agonist level), the unit of analysis and the cohort structure. Different names, labels, ids or wording do not make a difference.
* **Partly overlapping:** one session could give both if one named cell were changed or added; the cell is named.
* **Distinct:** at least one of those cells cannot be satisfied together with the other request's cell in one session (a different preparation, a different quantity, an incompatible condition).
* **Genuine conflict:** two specifications of what is the same measurement in every other cell, but differing in one cell so that both cannot be met in one recording. Quoted verbatim with file, row id and column, never paraphrased. A wording difference with the same content is a **synonym**, not a conflict.
* **Indispensable / substitutable:** indispensable when the source itself says reading cannot replace it or no in silico route exists; substitutable only when a named existing dataset or paper already answers it and a locator is given.
* **Order of interpretability:** measurement B is interpretable only after A when B's own source says a result of A conditions it; otherwise unordered. No invented dependency.

## Priors written before reading (to be scored by the verifier)
* G1: SCI47 Phase 0's perforated-patch E_GABA, sIPSC with antagonist-defined identity and mIPSC are SCI42's M01 and M03 specified again, with at least one genuine conflict in the antagonist identity, unit of analysis or age bin.
* G2: IT42-Q01 (tissue pH, `glun2b_comparators...#M01`) is distinct from SCI42's M01 (E_GABA) though they share an id; the assignment's "M01 E_GABA" must not be merged with it.
* G3: NP3P3 as re-scoped by ADV-004 (matched-beta same-laboratory recombinant series) is a different preparation from every slice recording and is closed by none of them; NP3P2 is probably a wet trigger whose specification is already given in the SCI42/SCI47 recordings.
* G4: no single slice preparation closes more than about four distinct rows, and it does not decide L2 (the subtype question), the pH question or the heterologous series.
* G5: the per-table field mapping needed for a `DESIGN_MAP` registration differs between SCI42, SCI47 and the IT14 table so that one generic mapping cannot cover them; each package needs its own entry (`DESIGN_MAP` holds two packages today, neither from this thread).
* G6 (against the brief): fragmentation may be partly correct because the arms test different biology (supply, postsynaptic, chloride handling).

## Outcome space (all complete results)
Consolidation possible with named conflicts; "they are distinct"; "conflicts cannot be adjudicated from the packages"; "a specification already exists (where)"; "fragmentation is correct"; "suspend the thread with a revival condition". I commit to none.

## Perimeter and stop rule
One folder, zero spend, no contact, no personal data, no edit to a source package or shared file, no new register or gate, no rank/sign/direction/state change, no wet work commissioned or urgent, ADV-004's "may" sentence for L2 unchanged (never "alpha2-preferring", never "a subtype-discriminating pair"). Producer then blind verifier, one at a time, sonnet, producer effort medium, verifier high, no escalation. If reading and the blind check are not done by 06:30Z I send the presidio the partial table (distinct measurements and the crosswalk) before anything else.
