# IT checkpoint 4, 2026-11-21 (IT Orchestrator successor window N; ACTOR_ID orchestrator; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's request at a closed increment, context about 340k tokens)

Reply to the operator in Italian, write files in English. This file is read by the next window; nothing here is a result. Model and effort: this window ran on Sonnet 5.5 at its default effort; every delegate was dispatched as sonnet at effort high and the effort was stated in each dispatch (the delegates report that they cannot see it; the transcript is the source).

## 1. Landed in this window (all gate PASS, ls-remote verified)
`c0de3657d` NP4G2 retrieval comparison, ADV-124 row classes, N1 reconciliation, wording correction after SCI part A · `3b56f190d` and `53c570731` N4 route check and the painted-page read · `101cc9423` mandate steps N4, N5 · `48ec453d7` ADV-123 consumer_delta recorded as owed · `1e5fd6b3a` routing of the Wwox EM label through needs.json · `60c86d784` portfolio RP-011 parked. ADV-129 (painted Italian): branch `task/it59-adv129`, landed SHA in the report message that follows this file; its record is `adv129_painted_italian_it_20261121/RESULT_ADV129_IT_20261121.md`.

## 2. State of the mandate
22 steps, 21 DONE plus ADV-129 accepted and recorded DONE with evidence at landing; step 6 (operational continuation) stays IN_PROGRESS as the standing step. Reserved to the operator: items 17 and 18 (and item 9, the gate cache); nothing here decides them.

## 3. Open items, owner, named event
| Item | Owner | Event |
|---|---|---|
| Package and `package --check` on the final tip; card-text folds (EB-ETX-01 coherence-check wording; F02 and J01 OL-class line; thyromimetic row; the P17 EM label) | IT | operator's item 17 |
| Wwox EM label: `needs/needs.json` line 502 first, then regenerate ranking and the view in one pass (frozen `evaluation_it17_p3` copies untouched) | IT | item 17 (section 6 and 7 of `NIGHT_20261120_N1_RECONCILIATION_IT.md`) |
| WM103 part 2 and the coordinated CLAIM 011 Title and BLOCK 2 row | operator | item 18 |
| Seven matching-pilot cases in other languages: typed revival, batches of 25 passages with one blind check per batch | IT, only if the operator or the pilot owner asks | a request |
| Static guard extension for Italian authored text in embedded data; `--gene-anchor` default decision | HE | HE's list; a second row or a live Europe PMC rerun for the default |
| NP4G2 independent reproduction (an independent culture or OPC-intrinsic report) | open question, not a task | trigger unchanged |
| Portfolio RP-011 (parked: at least six compounds with a measured outcome in a WWOX-deficient system, listed before any cascade); RP-013 (waiting: HE's Italian-fragment follow-up is closed by ADV-127/128; keep the row as ADV records it); RP-029 (item 9, operator's) | ADV | their own events |

## 4. K_core test I read next
HE landed the opt-in flag `scout_daily.py --gene-anchor` (a393995ef). Its trial (`np4g2_retrieval_it_20261120/gene_anchor_trial_he_20261121/RESULT_GENE_ANCHOR_HE_20261121.md`) is already read and recorded as a dated line in my NP4G2 result file: my literal proposal returned 0 records; the gene plus the row's top subject word returned 7 in the scout window, 2 of them in K_core. The next reading is HE's Europe PMC rerun when Europe PMC answers again, and a second reopen row; neither is mine to run.

## 5. Facts and recipes learned (memory note `it-successor-n-20261120-pitfalls`)
* A commit or merge while `safe_push --serialize` waits moves HEAD and the push refuses; finish every edit and merge first, then touch nothing. Kill by exact PID.
* Painted-page reads: `repurposing_view.Cdp` with the page in a non-hidden directory under the home (the snap Chromium cannot read dot-directories; `--dump-dom` of the 5.6 MB page is empty); scan scripts are HE's in `adv128_painted_italian_he_20261121/`.
* The work-order 'next test' card is built by script from the embedded data (`assets/curated.js`); a server-side wrapper does not reach it. Localise the embedded-data copy only, not the object the server renderers read (a first version failed `test_a_translated_passage_is_never_shown_as_original_language_only`).
* The content inventory is collected from the shareable edition only; full-edition-only authored text is not in it and falls back to the original-language marker.
* A model verifier found a real mistranslation that pre-dated this window (German 'Herstellerextraktion' for the analyst who produced an extraction): translation checks must judge role words as a specialist would.

## 6. First steps for the successor
1. Read the router, the state manifest (`current_state: READY`), sections 21c, 21d, 21e, `roles/orchestrator.md`, this file.
2. Bind the mandate (`MANDATE_BOUND: ORCH-ROADMAP-IT59-20261119` as its own text block alone in its message, then a tool call; `handoff` is the proof, not the claim).
3. Wait on the named events of section 3; do nothing on the package before item 17; no frozen candidate is touched.
