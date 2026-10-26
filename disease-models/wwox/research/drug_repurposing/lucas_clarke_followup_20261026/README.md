# Lucas-Clarke 2026 follow-up: from the paper's biology to target -> compounds -> cards -> research queue

Scientist `scientist-c`, 2026-10-26, task branch `task/sci-c-lc-repurposing`. Operator-approved mandate. Exploratory, non-canonical, class level,
not medical advice, no dose, no wet-lab claim. Every external database or fly statement is NOT WWOX EVIDENCE. Direct evidence, inference,
hypothesis and speculation are labelled apart (DATO / INFERENZA / IPOTESI / ESPANSIONE).

| Step of the mandate | File | One-line result |
|---|---|---|
| 1 Biological needs, per experimental contrast | [`biological_needs.md`](biological_needs.md) | seven contrasts, five strands (ISR, LDH/lactate, PDH/PDK kept separate, Wwox dose and glycolytic genes, methionine), each with direction, context, status, what to verify; no Wnt/TCF7L2/mitochondrial/GSK3 beta premise |
| 2 Target identity, then compounds | [`target_resolution.tsv`](target_resolution.tsv), [`compounds_and_sources.md`](compounds_and_sources.md), raw outputs and scripts in this folder | PDK1 is a measured PDPK1 collision; DGIdb and Open Targets are empty for eIF2B activators; ChEMBL curated mechanisms: 6 rows; Open Targets count and list both obtained |
| 3-4 Two dimensions, cards, HYP drafts | [`../cards/E01..E04`](../cards/) (`build_cards.py` here writes them), [`../../commit_candidates/CC-20261026-SCIENTIST-C-LCFOLLOWUP-01.md`](../../commit_candidates/CC-20261026-SCIENTIST-C-LCFOLLOWUP-01.md) | four cards, each with Track (A/B) and route (RECUPERO_PROFONDO / BENEFICIO_PRECOCE) as separate fields; two HYP drafts and a consequence note staged for the integrator |
| 5 MTBLS12344 | [`mtbls12344.md`](mtbls12344.md) | not publicly retrievable today (folder 404, absent from the public listing, API 401); recorded; reopening condition stated |
| 6 ToolUniverse | [`tooluniverse_trial.md`](tooluniverse_trial.md), `tu_results.json`, `tu_compare.json` | one question (PDK2); same compounds, actions and sources as the direct routes, fewer fields, silent 1000-row cap; WATCH |
| 7 Queue and regeneration proof | [`regeneration_proof.md`](regeneration_proof.md), [`../../repurposing_batch_selection_20261026_module.md`](../../repurposing_batch_selection_20261026_module.md) | the join and handoff were regenerated; staged leads were applied in a scratch worktree to show the new rows |
| 8 Closing | the cards carry limits and next experiments; E04 is a reasoned abstention | see the CC |

## What `repurposing_join.py` covers, and what it does not (declared)
The join asks ChEMBL and openFDA by the **candidate name** a mechanism-map heading gives, PubTator 3 by the first two gene-looking tokens of a query,
and Open Targets only for WWOX itself on claim-derived queries. It **never** queries DGIdb, iLINCS or Orphadata, and it never asks a source for the
compounds of a target. Its derived cards for dichloroacetate (`Q-N-08`) and lactate (`Q-N-06`) therefore carry no drug assertion at all; the hand-made E-series
cards carry them. `repurposing_join.py diff` shows that gap field by field (`regeneration_proof.md`). The six adapters were used here by direct call, and
DGIdb through `kg_thin_slice.drug_packet`; coverage per source is the table in `compounds_and_sources.md` section 1.

## Reproduce
```
python3 disease-models/wwox/research/drug_repurposing/lucas_clarke_followup_20261026/dgidb_query.py
python3 .../chembl_target_mechanisms.py ; python3 .../chembl_activities.py ; python3 .../chembl_named_compound_activities.py
python3 .../opentargets_lists.py ; python3 .../adapters_run.py
python3 .../build_cards.py && python3 disease-models/wwox/research/drug_repurposing/cards/check_cards.py
```
The scripts need the network and write dated retrievals; rerunning them changes the retrieval date and may change counts. No call sent any personal
address, credential or registration; the ChEMBL, DGIdb, Open Targets, openFDA, PubTator 3, iLINCS and Orphadata calls are key-less.
