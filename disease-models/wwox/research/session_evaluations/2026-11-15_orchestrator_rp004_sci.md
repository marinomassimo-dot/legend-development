# Session self-evaluation: RP-004 reading of PMID 18620777 (orchestrator as SCI, 2026-11-15)

Non-canonical. Process diagnosis. Not medical advice.

## Executable verdict
`session_self_eval.py --workspace . --disease wwox`: PASS (declared gaps listed there are earlier debts, none from this reading). Task record `ledger/tasks/orchestrator/ORCH-RP004-SCI-20261115.json`; battery evidence is recorded there at landing.

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Predictions before the body | F1 to F7 were IT's, committed at 45fadb00f before anyone read the body; I scored them first, wording untouched, and checked by string match that the scored text equals the frozen text. 5 HELD, 2 NOT DETERMINABLE, 0 MISSED. | sound | none |
| Reading | Article page, one request, body read from Abstract to Discussion; 26 verbatim rows checked mechanically against the saved page (PASS); absence claims have a second route (string search, hits read one by one). Figure images not viewed, so the receipt is `partial_fulltext_read`. | sound, bounded | five figure panels (n, bars, vehicle against inhibitor) could move F5 and F7 |
| Verdict | carried with limits; the limits (two lines with different p53, baseline apoptosis not separated, selected clones, partial knockdown with one shRNA, one chemotype, no genetic JNK control, no phospho-JNK or c-Jun) are each quoted. | sound | "same direction" and "not separated" are my reading of the text (INFERENZA) |
| Verification | no blind verifier, my call; the decisive propositions are quotations | weak for the two inferential statements | an independent read if the case proceeds |
| Consumption | `consumer_delta.md` (six rows); receipt JSON left for the integrator to append | pending | benefit unproven until IT consumes it |

## Process diagnosis
* The mechanical check caught a real defect in my own tool, not in the reading: 11 of 26 quotes missed because the page puts link markup inside citation parentheses ("( 48 )"). The normaliser was fixed on both sides and the rerun passed; the words were identical in all 11.
* One wording of mine would have overstated the paper (SP600129 "cut proliferation of the knockdown line to 25%"): the text does not say which cells. Caught on a read-through before delivery and corrected in three files.
* Nobody outside this session has checked the reading yet.

## Micro-upgrades (the answers)
`verify_quotes.py` now tolerates link markup in citation parentheses and carries an absence-search section (six features) so that "the paper has no X" has a second route; reusable for any PMC-page reading.

## Residual debt
The figure panels; the receipt append (integrator); IT's scoring of the case predictions.
