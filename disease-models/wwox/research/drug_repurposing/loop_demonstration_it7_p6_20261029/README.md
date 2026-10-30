# IT7 P6 (roadmap R6): a negative and inconclusive result carried through the complete research loop

Scientist-a, task `ORCH-ROADMAP-IT7-20261029`, 2026-10-29. Non-canonical research material. **Not medical advice. A computational result is not therapeutic efficacy.** The reference genotype class is a WWOX-DEE genotype class; no individual-level record is used. No registration, contact, spend or access request was made.

## 1. The new result (what enters the loop)

Source: the IT7 P3 result, `network_comparison_it7_p3_20261029/README.md` on branch `task/it7-p3`, commit `0d9d9879` (commit `ce89192d` on that branch is the independent verifier's report; P3 may not yet be on `main`), built on the IT7 P1 six-gene glycolysis / lactate module (`subnetwork_it7_p1_20261029/README.md`, integrated). **The P3 verifier reproduced every quoted number**; on its own draw it records a decile-matched null 95th percentile of 0.396 and an exact p of 0.0595 where the producer's draw (quoted here and in the needs) gives 0.389 and 0.060 - same conclusion.

| Item (P3 label) | Result as pre-registered | Character |
|---|---|---|
| E1, module transfer to an independent WWOX-loss contrast (P47T knock-in mouse, GSE215425, hippocampus, 5 v 5 animals; regions of one animal are not independent) | module contrast D +0.329 (positive = WWOX-loss-like), decile-matched null 95th percentile 0.389, exact one-sided p 0.060; five of six genes in the build direction (HK2 +0.66, LDHA +0.48, SLC2A1 +0.18, BNIP3 +0.03, PDK1 -0.08 as predicted; LDHB -0.10 against) | **INCONCLUSIVE** (not transfers; not does-not-transfer) |
| E2 primary, signed external network vs an unsigned reference, ranking 256 compound families by observed module opposition in held-out neuron-like LINCS contexts | network rho 0.047; reference rho -0.085 | **NO ADDED VALUE** (no detectable signal at rho 0.15) |
| E2 secondary S2, signature route | rho 0.143, 0.007 under the 0.15 threshold, 90 percent interval [0.039, 0.243] that spans it; minimum detectable effect about 0.157; under its own random-readout null | **effect not detected, not excluded** (the P3 verifier's wording; the registered label was no added value). Weak positive counter-evidence to "no added value" for this route: interval lower bound 0.039 and a top-decile hit rate of 15 percent |
| E2 secondary S3, network with four curated HIF1A edges (labelled 'WWOX-enriched' in IT7; all four were already in the external network, so this is no test of WWOX knowledge: IT8 P4) vs external-only | difference -0.0015, 90 percent interval [-0.004, +0.0002] | **NO ADDED VALUE** |

Limits carried with it: exploratory; minimum detectable effect about rho 0.15; 256 families chosen by input availability, not a catalogue screen; wild-type neural cells, not WWOX-deficient cells; transcript, not activity; one partial-loss missense genotype, not a null; the 0.25 concordance rule that chose the six genes passes about 4 of 24 network genes by chance (P1 repair note). The module is therefore **not shown to be a reproducible WWOX-loss feature**, and the compound results carry no demonstrated WWOX-loss relevance. Reopening condition named by P3: a compound-response measurement in a WWOX-deficient human neural system with replication and a matched readout.

## 2. The loop, one step per row, with the file that carries it

| Step | What happened here | Where it lives (consumer) |
|---|---|---|
| 1 Observation | The P3 outcome is recorded as observation class `COMPUTATIONAL_RESULT`, with its inconclusive / negative character in the statement and the limits field: `O5`, `O6` on `NEED-PDH-PYRUVATE-AXIS`; `O6`, `O7` on `NEED-LACTATE-LDH` | `needs/needs.json` (checked by `needs/check_needs.py`); locators point to this record |
| 2 Inference | Two inferred lines say what the result does not license: a PDH restraint cannot be inferred from a transcript module or from a compound ranking; a compound is not preferred by a model that showed no added value | `inferred[]` of the same two needs |
| 3 Hypothesis | The hypotheses the needs cite (HYP-20260709-01, HYP-20260709-05, HYP-20261026-11) are unchanged; status and ranking live only in the hypothesis ledger, which this package does not edit (section 6) | needs `sources.hypotheses` (ids only) |
| 4 Biological need | The two needs gain one counter-evidence item each. The direction of both stays `uncertain` | `counter_evidence[]`; coverage `need_counter_evidence_items`; the view's need panel |
| 5 Compound search | Unchanged by design. The target-to-compound reach of the two needs is read again from the regenerated coverage (section 4); the catalogue and the identity layer are not touched, and the P3 result is not used to filter, order or score any compound | `coverage/coverage_summary.json` `needs.per_need` |
| 6 Comparison | The P5 comparison (`pharmacological_comparison_it7_p5_20261029/`, records CMP-04 to CMP-06) states the model position of the three E-axis hypotheses as "none beyond the P3 negative", apart from research priority and observed evidence | that folder |
| 7 Next experiment | Cards `I01`, `E03` and `E02` keep their decisive measurement (PDH phosphorylation, activity and tracer with a genotype-by-inhibitor interaction; LDH activity and lactate in WWOX-deficient neural cells) and gain a first sentence: on I01 and E03, read PDK1, LDHA, LDHB, HK2, SLC2A1 and BNIP3 transcripts beside the decisive measurement in the same cells (so the replicated WWOX-deficient human neural contrast that P3 named as missing doubles as a second transfer test); on E02, read LDHA and LDHB activity separately; on all three, no computational ranking selects the compound arm. These are the same cells and two readouts of the module, not two experiments | `cards/*.packet.json` -> rebuilt `*.card.json`; `view/work_order.json` entries for the two needs |
| 8 Regenerated queue | Coverage, the full and shareable views, the package, the join and the module handoff were regenerated; the effects are listed in section 4 | `coverage/`, `view/`, `join/`, `../../repurposing_batch_selection_20261029_module.md` |

## 3. What the result changes and what it does not

**Changes (data-driven, now visible downstream):** two needs carry the result as COMPUTATIONAL_RESULT evidence with its character; each need's counter-evidence count rises by one, and so does the `need_counter_evidence_items` value in every priority row on that need; three cards state what the decisive measurement now also reads and that no model ranking selects the compound arm; the work-order entries of the two needs say the same and credit this record.

**Does not change, by the rules (checked in section 4):**
* F / C / P positions. A position is derived from the signed drug assertions of a card on a need; a module-transfer result and a method comparison add no such assertion, so every position stays: I01 C3 on the PDH axis and on seizure control, F3 on lactate/LDH; E03 F3 on the PDH axis; E02 F3 on lactate/LDH. A model negative does not demote a hypothesis, and a low model rank alone establishes neither inefficacy nor harm.
* The count of WWOX-experiment observations per need. The observation class is COMPUTATIONAL_RESULT, so `wwox_system_observations` (WWOX_EXPERIMENT_IN_DEE_SYSTEM only) does not move; the same observation relabelled as an experiment would move it (mutation test).
* Card status (`hypothesis` / `controversial`), the premise columns, the direction `uncertain`, the catalogue (44,211 source-level records, 40,268 families), L3 and L4 cells (zero observed), and the absence of any score, rank or probability.
* Card E04 (ketogenic diet) is deliberately untouched: a diet acts below PDH and has no compound target row, so a compound-ranking negative says nothing about it, and the module transfer result does not bear on its open question (a PDH-specific measurement).
* The ISR and NMDAR measurements proposed in iteration 6 stay PROPOSED; nothing here implies they were run.

## 4. How propagation was verified

Commands run from the worktree with `LEGEND_CATALOG_CACHE` set to the root checkout's cache. A baseline was fixed first so that the diff isolates this package: the join state had lagged the receipt ledger (140 evidence tables differed only in `receipt_events` counts), so it was refreshed and committed alone as "IT7 P6 step 0" before any edit.

| Consumer | Command | Measured effect of the P6 edits only |
|---|---|---|
| Needs checker | `needs/check_needs.py`; `needs/test_check_needs.py` | OK; 85 observations (four added), document locators resolve (this record is the locator target) |
| Cards checker | `cards/check_cards.py` | 27 packets, 0 problems; the three rebuilt cards equal the bridge output (re-written in their stored indent so the diff is the content) |
| Coverage | `repurposing_coverage.py run` | `priorities.json`: 710 rows, 59 changed (55 on `NEED-PDH-PYRUVATE-AXIS`, 4 on `NEED-LACTATE-LDH`) and in each of them only `criteria.counter_evidence.need_counter_evidence_items` moved (6 to 7 and 3 to 4); `coverage_summary.json` unchanged; `coverage_matrix.json` moved only its two provenance hashes; `wwox_system_observations` of both needs unchanged (the new observations are COMPUTATIONAL_RESULT) |
| Positions | `repurposing_view.py positions`, before and after | byte-identical (every card x need position as before) |
| Views | `repurposing_view.py run --source full`, `run --source shareable`, `package`, `check` | both pages and the shareable package regenerated; `check` reports both current; the new statements, the counter-evidence item, the three card sentences and the work-order entries are present in `index.html`, `index_shareable.html` and `shareable_package/index.html` |
| Join | `repurposing_join.py run` (after the baseline commit) | queries 0 changed, evidence 0 changed, cards 2 changed of 28: `Q-N-08` (E03 and I01) and `Q-R-11` (E02); `Q-R-05` (the ketogenic diet, E04, untouched by design) unchanged |
| Handoff | `repurposing_join.py handoff --date 2026-10-29 --write ...` | the module table rows `Q-N-08` and `Q-R-11` and the card-table rows of E03 and I01 begin with the new sentence; 28 rows as before; no row added, removed or re-sorted |
| Regressions | `test_repurposing_coverage.py` class `LoopPropagationIT7P6` (5 tests); `test_repurposing_join.py` class `LoopPropagationIT7P6` (5 tests) | positive checks by identifier on the needs, cards, derived cards, handoff, work order, three pages and coverage rows; mutation tests (a) remove the recorded counter-evidence from a copy of the needs: the count in the priority rows of that need falls by one and nothing else in any row moves; (b) relabel the lactate observation as an experiment in a copy: `wwox_system_observations` rises by one; (c) write a marker into a copy of card E02: it appears in the derived card `Q-R-11` and in its handoff row and in no other derived card |
| Guard | `scripts/test_no_closed_world_assertions_on_live_state.py` | passes: no absence or count pin on append-only state was added |

A further check (added after the independent verification) compares the work-order `data` text with the first sentence of the card it cites, so that drift between the hand-written work order and the card is flagged.

The regression was first run on a statement that lacked the character word the test requires (`NO ADDED VALUE` was missing from observation `O7`); it failed, the statement was corrected, and it passed. A regression that cannot fail was not accepted.


## 5. Next action created by the loop

The same act as before, with one added readout: PDHA1 Ser293 phosphorylation, total PDH, PDH activity and a glucose tracer, genotype by PDK-inhibitor, in WWOX-deficient human neural cells against matched controls (card I01), and LDH activity, lactate and LDHA / LDHB separately in the same cells (card E02), with PDK1, LDHA, LDHB, HK2, SLC2A1 and BNIP3 transcripts read beside them. **Proposed, not run**; the cells are not held and an access request for a public organoid deposit exists as a draft only and was not filed.

## 6. Ledger and registry edits that are NOT part of this package (for the batch path)

Not edited here, listed for the batch path: (a) discovery ledger: a lead recording "six-gene glycolysis / lactate module, independent transfer test inconclusive (P47T hippocampus p 0.060, LDHB discordant), method comparison: network routes no added value, signature route not detected and not excluded" with falsifier "a replicated WWOX-deficient human neural contrast with a matched protein or activity readout"; (b) therapeutic hypothesis ledger: a note on HYP-20260709-01 and HYP-20261026-11 that a computational comparison added no support (no status or score change proposed by this package); (c) the P3 numbers quoted in the two needs were verified (ce89192d); nothing is owed except re-reading them if P3 is revised; (d) the join, view and coverage outputs are derived and are regenerated by the integrator after the other IT7 packages land; (e) no receipt applies (no paper was newly read for a full-text receipt).

## 7. UNVERIFIED

That P47T is a fair independent test of a module built in two human neural systems (one partial-loss missense, animals as unit, regions not independent); whether LDHB discordance reflects biology, the missense genotype or noise; the mapping of the module genes to protein activity (none is measured).
