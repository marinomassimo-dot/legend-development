# Consumers: what to change, where, in which order (for the IT30 Orchestrator, the single integrator)

Non-canonical research note. Not medical advice. Nothing named below was edited by this batch except files inside `batch_sci_20261105/`, the task record `ledger/tasks/orchestrator/ORCH-SCIBATCH-DR-20261105.json` and the staged receipt copies under `receipt_staging/scibatch/`. All proposals are text and rows for you to apply, renumber and regenerate. Challenge ids carried here: `CH-SB-CONCORDANCE`, `CH-SB-VGB-WHITEMATTER`, `CH-SB-POSTONSET-RESTORATION` (the task record's `returned` field names this file and the package README).

## 1 · Suggested order

1. Merge this branch (or `main` after it lands). It adds only new files plus the task record.
2. Receipts first (section 2), then regenerate the surfaces the ledger feeds, then the consumer edits (section 3), then validators, then the registry proposals (section 4) through the normal `BATCH_COMMIT` path.
3. Do not apply the vocabulary additions that appear in some first-round drafts (a human `model_type` value, a fifth window state, a card-level harm tag): two independent checks rejected them; the existing vocabulary suffices (section 5).

## 2 · Receipts (109 staged, none recorded)

* Where: `disease-models/wwox/research/receipt_staging/scibatch/` (copies; the originals with their `INDEX.tsv` are in each package's `receipts/`). Counts by package: A1 16 (suffix 21), A2 24 (22), B1 37 (23), R1 22 (24), R2 10 (25).
* Trial already done on a throwaway clone of this branch (`record_staged_receipts.py`, dry run): **TRIAL OK**. Re-run it on your tip before `--apply`: another session may have added receipts for the same PMIDs, which would make a `prior_receipt` stale (the trial is the only check that catches it).
* Order matters and is handled by event-id order: A1's receipt `FTR-20261106-42735667-21` names B1's abstract receipt `FTR-20261105-42735667-23` as `prior_receipt`.
* Depths: no receipt is a `complete_fulltext_read`; most are `partial_fulltext_read` or `abstract_only`. So no PAPER record is owed for the `test_batch_queue` identity check, and none is proposed as a completed reading (all R sources are other-disease precedents).
* After `--apply` the tool prints the regeneration commands (coverage report, reading state, batch queue, pathograph); run them, then `candidate_tree_freshness.py --candidate HEAD --base main`.

## 3 · Consumer edits

Row ids and identifiers in the source files are proposals; renumber against your tip (`needs.json` observation ids, `DR-H02-0nn` ids, work-order text may have moved).

| Consumer (file, record, field) | Change | Source file in this batch | Validator or regeneration |
|---|---|---|---|
| `needs/needs.json` need `NEED-WWOX-GENE-ADDITION`: `observed`, `inferred`, `counter_evidence`, `notes`, `intervention_direction.do_not_assume` | add the consolidated observations and text lines (replaces both R packages' own proposals, whose identifiers collide) | `integration/NEED-WWOX-GENE-ADDITION_consolidated.md` and `.json` | `needs/check_needs.py`; `model_type` is free text, use `other_animal_model` and the existing `human_clinical_report` |
| `view/work_order.json` entry `NEED-WWOX-GENE-ADDITION`: `data`, `would_change`, `feasibility` (`window_state` unchanged) | append the per-endpoint wording and the level-achieved requirement | same file, section "Work order and INV-01" | regenerate the view; the entry also carries Italian summary fields |
| `ranking_it8_p9_20261029/investigations_it20.tsv` row `INV-01` (`next_test`, `novelty_perimeter`) | append the per-endpoint wording; rank unchanged | same | `test_investigations.py`, `ranking_it8.py run` |
| `ranking_it8_p9_20261029/unit_caveats.tsv` unit `U07` | one `limit` row: external precedent split on seizure endpoints; sheath structure after onset in a neuron-driven lesion unmeasured | same | regenerate |
| cards `C01_aav9_wwox`, `C04_aav9_endpoint_families` `p4_fields.temporal_or_model_limit` (and C01 `endpoint_pursued`) | text appends; there is no `next_measurement` field on C04 | same | `cards/check_cards.py` (forbidden-text regex: no number next to mM, mg, kg, no ellipsis) |
| `cards/H02_gabaat_inactivator_myelin_exposure.packet.json`: `drug_assertions`, `mechanism`, `evidence_against`, `not_known`, `question_history`; notes on `DR-H02-005` and `-009` | add the corrected assertions (card vocabulary INCREASE, DECREASE, UNKNOWN, NO_CHANGE only) and the text; **no harm tag** (no such field; the module computes the position; a card-level C3 for vigabatrin stays conditional on injury demonstrated in a Wwox-deficient model, as the work order registers) | `b1_whitematter/module_inputs.md` sections 1 to 2 | `cards/check_cards.py` after regenerating the card with the bridge |
| `needs/needs.json` need `NEED-MYELINATION`: `counter_evidence`, `intervention_direction.do_not_assume` | add the lines of B1 section 3 | `b1_whitematter/module_inputs.md` section 3 | `check_needs.py` |
| `view/work_order.json` entry `NEED-MYELINATION`: `data`, `feasibility`; **`would_change` amendment** | adopt the window-series wording; the `would_change` edit changes a pre-registered sentence: accept or refuse it explicitly (B1 flagged it) | `b1_whitematter/module_inputs.md` section 4 | regenerate the view |
| `ranking_it8_p9_20261029/investigations_it20.tsv` row `INV-10` (`evidence_available`, `decisive_uncertainty`, `next_test`, `novelty_perimeter`) | use the combined sentence below; keep the next test about a dated developmental instrument before and after a sustained response | `a1_wwox_reports/module_inputs.md` section 1, `a2_baseline/module_inputs.md` section 1 | `test_investigations.py` |
| `ranking_it8_p9_20261029/unit_caveats.tsv` unit `U20` | caveat rows: counts in children not independent exposures; no instrumented sustained response; hormonal co-therapy measured as a risk factor in the sibling cohort | A1 sections 1 and 4; B1 section 2 | regenerate |
| `needs/needs.json` need `NEED-SEIZURE-CONTROL-SYMPTOMATIC`: `observed` O1 text, new observation (all 16 fields; `locator_status` from MANIFEST, DOCUMENT, REGISTRY_ONLY, GAP), `counter_evidence` | per A1 section 2, with the double-counting clause kept and genotype at class level | `a1_wwox_reports/module_inputs.md` section 2 | `check_needs.py` |
| `view/work_order.json` entry `NEED-SEIZURE-CONTROL-SYMPTOMATIC` | denominators sentence (diet: minimum 3 exposed, still not stated; vigabatrin MRI children: 2 of 2 at abstract level, probably inside an 18-of-64 cohort) | A1 section 3 | regenerate |
| `catalogue_funnel_it18_p2_20261101/vigabatrin_sources_resolved.tsv` | append the assertion rows in the file's 12 columns and its own value sets | A1 section 5 | the funnel's tests |
| `cards_early/EB-VGB-01`, `EB-KD-01` | caveat text per A1 section 6; do not add instrumented-response language | A1 section 6 | `cards_early/check_cards.py` |

### Combined sentence for `INV-10` and CLAIM 031 (settled by review A, point (a))

*No WWOX child is recorded with a developmental gain after a symptomatic improvement. Four children in three reports (two of them in one report) had a partial, transient or clinically-defined improvement with development not progressing; two had neither. That is what the baseline in other genetic and structural early-onset encephalopathies predicts (a responder with poor development is the majority outcome in infantile spasms and near-universal in genetic strata), so it is not by itself a WWOX-specific feature. The comparison holds only as a binary: the baseline uses standardised scores with a cut, every WWOX developmental statement is a clinician narrative, and no WWOX child had a sustained, instrumented response.*

## 4 · Registry proposals

`PROPOSED_REGISTRY_CHANGES.md` (this folder) lists the claim, paper and ledger changes in the repository's candidate vocabulary. None is applied. The two that matter most: CLAIM 031's genotype-independence line is wider than its sources (decoupling holds in genetic and structural strata, not in unknown aetiology); CLAIM 042's revival trigger (a Q230P diet exposure) is met by documented exposure alone, for the homozygous configuration, while the claim's own compound-heterozygous carrier is untouched.

## 5 · What was rejected on independent checking (do not reintroduce)

* A human `model_type` value and a fifth window state: `model_type` is free text and `human_clinical_report` already exists (nine observations use it); window states attach to WWOX evidence only.
* A card-level harm tag for vigabatrin: no such field exists.
* "Start age decides" as a settled premise, and also its rejection: the human record supports an age band in infants, the animal half rests on abstracts, the one full-text cohort cannot test a within-infancy window.
* "Myelin after onset has never been tested": the class is not empty outside the gene families first searched; what is unmeasured is sheath morphometry after onset in a neuron-driven lesion.

## 6 · Dependencies and open items

* Engine: `scout_daily.py` `TABLE_LIMIT` and the diagnosis parser (`FROM_THE_MAP.md`).
* `CQ-IT30-05` (vigabatrin across seizure models) should read the B and A conclusions above first.
* Not executed in this batch: map rows `WO-06` (integrated stress response and seizures) and `RS-R6` (suppressors of WWOX loss); see `FROM_THE_MAP.md`.
* Residual unverified evidence is listed in `VERIFICATION.md`.
