# Self-evaluation - repurposing batch P4 early-benefit cards, scientist-d (2026-10-21)

## Scope and executable verdict
- Task `REPURP-10H-P4-EARLY-D-20261022`, branch `task/repurp-p4-early-d`. No paper read, no receipt, no manifest touched: the batch is a synthesis of qualified material.
- `session_self_eval.py`: VERDICT FAIL, all blocking lines are `ORPHAN_COMPLETE_READ` for the R3 and R4 receipts of other and earlier tasks (22 PMIDs), not caused by this task and not fixable by it; no line concerns cards_early. `fulltext_receipts.py verify`: OK, 743 chained receipts. `check_cards.py`: PASS (9 packets, every card rebuilds byte for byte, every quote found verbatim). LINT: run at landing by `task_close.py` (result in the task JSON).
- Local verdict: PASS for this task's mechanics. Global: the registry-record debt for the R3/R4 complete reads stands.

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Does each card make the unknown visible? | Every card has `not_known`, UNKNOWN time fields, and assertions placed so that the unmeasured cells sit beside the measured one | strong | Blind audit owed |
| Symptomatic versus disease modification | Carried in each card's expected-contribution row, in `evaluation_frame` and on the development abstention | strong | None |
| Source parity / labelling | Non-WWOX sources labelled and enforced mechanically; but the cards rest on registry and note surfaces, not on new reads, and the WWOX VABAM anchor and the diet series have no complete native surface | partial | Native surface of the series; anchor receipt |
| Use of an unaudited reading | The T-type card carries R2's narrowing of a lead that R2 itself declares owed an audit | partial | Audit by a third actor |
| Quote discipline | 20 quoted passages (14 distinct), all found verbatim by the checker; none stitched | strong | None |
| What a card could still hide | `OPPOSES_DISEASE_CHANGE` on a single-source comparison can be read as a result; handled by the README, not by the bridge | partial | Bridge gap 5 |

## Process and capability diagnosis
- Skills used: none of the reading skills (no reading). `legend-discovery-method` declined: no novelty claim made. `legend-hypothesis-forge` and `legend-safety-triage` declined: no prediction and no molecule triage was in scope.
- Friction: the bridge cannot sign a null effect, cannot fill its own `translation` block and has no abstention state; the checker was written to enforce from outside what the bridge cannot.
- Self-caught: three counts in my first draft (the vigabatrin report count, a genotype count and a mis-numbered R2 section) were corrected by re-reading the source before the checker ran; the checker caught none of them, it cannot.
- Micro-upgrade: `cards_early/check_cards.py`, shipped, with its own run as the test. It checks the one thing that bit earlier batches, verbatim quotation, against the repository sources. Candidate for promotion into `framework/scripts` if the deep-recovery cards want the same check.
- Residual risk: the cards are well formed, not verified; every card is IPOTESI or ASTENSIONE.

ATTRIBUTION_CENSUS
incidents: 3
machine: 0   blind_auditor: 0   peer: 0   self: 3
severity_high: 0   of which self: 0
undetected_known: 0
