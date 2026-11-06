# From the open-question map: items for the integrator

Non-canonical research note, not medical advice. Source: `map/README.md` and `map/open_questions_map.tsv` (115 rows, built from 160 source items, pinned to commits; `main` moved to 0845ed06 while the map was built, IT29 now being on `main`). This note lists only what needs an integrator decision. Everything else in the map is a reading aid.

## Counts

By kind: wet-lab measurement 28, engine or infrastructure 28, monitor 23, literature-executable 17, data-access blocked 11, decision 8. By status: OPEN 92, CONCLUDED 14, IN_PROGRESS 5, CLAIMED_THIS_BATCH 3, SUPERSEDED 1. Most open questions need a measurement the repository cannot make; a minority is executable at zero spend on public sources.

## The five executable and unclaimed questions, and what became of them in this batch

| Map row | Question | State at the end of this batch |
|---|---|---|
| `WO-06` | Mammalian study of integrated-stress-response modulation on seizures; the paper that rebuts the Sephin1 mechanism (PMID 29618508); five abstract-only glial papers | Dispatched, stopped by the account usage limit before any file was written; **not executed**. Still open, still unclaimed. |
| `RS-R6` | Suppressors or modifiers of WWOX deficiency (Alliance of Genome Resources, BioGRID ORCS, DepMap lookups never run) | Same: dispatched, stopped, **not executed**. The Alliance API answers key-less. |
| `IT29-P12` | Methods of the oligodendrocyte-differentiation screen (PMID 27592856) behind two signed rows | Not started; possible overlap with IT30 step S2. |
| `TS-01` | Re-check of 21 reopen conditions that no record shows probed | Not started. Better solved by the engine fix `EN-01` below, so the radar probes them every day. |
| `TS-02` | Trial-registry census re-run | **Done**: `integration/TS02_trial_registry_rerun.md`. Same 84 identifiers, same per-query states as on 2026-10-20. |

## Engine defects found while running the daily plan (for IT30, not touched here)

* `EN-01`: `framework/scripts/scout_daily.py` reads at most 12 reopen/decision tables (`TABLE_LIMIT = 12`, newest by iteration number); `main` holds 13, so `recovery_it10_p23_20261031/reopen_searches.tsv` (R1 to R9: Q230P protein fate, ACK1, albendazole, ITCH, suppressors) never enters the plan. Raising the limit, or selecting by openness, makes `TS-01` unnecessary.
* `EN-02`: the plan's diagnosis parser needs a six-column table; `diagnosis_it28_20261105/README.md` has four, so no diagnosis-derived question has reached the plan since IT28.
* `EN-03`: derived search terms are generic for several needs (about 40 percent noise, measured in IT18).

## Contradictions between records (stale text to correct; map rows `DC-01` to `DC-05`)

1. The module README names iteration 19 as CURRENT although iterations 20 to 28 exist (the IT29 banner calls the lower sections a historical index).
2. The roadmap's "Current stage" pointer lags the newest generation stage.
3. `view/DEPLOY.md` says the view is served nowhere; the public site answers HTTP 200 and the repository README links it.
4. Reopen rows still say NEEDS-DATUM although a later record served them (`R3`, `NP5A3`, `NP1B4`); `uncarded_items.tsv` N12 and `triggers.tsv` still say "above all R3" although both R3 sources were read and the datum is absent.
5. `needs/needs.json` calls the autophagy registry stubs unread; two of the three have since been read as full records.
6. Header dates: `view/work_order.json` `research_update` is 2026-10-29 while two entries are dated 2026-11-01.

## Interaction with IT30's own queue

The IT30 conditional question on vigabatrin (`CQ-IT30-05`, sign across seizure models) shares the compound, not the question, with the vigabatrin packages of this batch. Package A and B conclusions (symptomatic response and development; white-matter safety) are inputs to that question: read `integration/CONSUMERS.md` rows for `INV-10`, `NEED-SEIZURE-CONTROL-SYMPTOMATIC`, `NEED-MYELINATION` and card H02 before answering it.
