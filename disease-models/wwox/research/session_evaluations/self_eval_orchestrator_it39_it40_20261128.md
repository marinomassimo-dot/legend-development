# Self-evaluation, capability scout and takeaways, IT Orchestrator windows IT39 (c817e528) and IT40 (8424b293), 2026-11-28

Public, disease-level, de-identified; nothing here is medical advice. Written by IT40 for the ADV-337 work (IT39 produced the PREREG, producer and blind reader; IT40 composed the result) and as IT39's owed grading, from the committed PREREG, RESULT, receipt and checkpoint 39; it is not IT39's own account.

## Scope and executable verdict
Work: ADV-337, complete read of PMID 33914858 (Repudi 2021, Brain) and the blind comparison of 38 consuming sentences. Receipt `FTR-20261128-33914858-41` (complete_fulltext_read; the two mp4 supplements named unviewed), work manifest locators 40 to 50, `RESULT_ADV337_IT_20261128.md`. `fulltext_receipts.py verify` OK (3964 chained), manifest validator PASS, `growth_anchors.py check` PASS, `legend_lint.py` no block, view, shareable view, package and ranking regenerated. Effort high (read back from the transcript). One MINOR BATCH_COMMIT, `BATCH_20261128_010` (PAPER 004 carries the complete-read marker; the landing suite `test_batch_queue` refused the receipt until it did); no claim edit, because no decision changed. `test_batch_queue.py` 52 tests OK.

## Diagnosis
| Dimension | Answer with anchor | Grade |
|---|---|---|
| Frozen question | PREREG and sentences hashed before the producer ran; E1 and E2, a counterexample and a decision-effect line stated; IT39's expectation (15 to 33 percent) recorded and failed | strong |
| Independent check | The composition was checked by a second reader: 13 of 25 assessed rows changed class (52 percent), 15 of 25 with basis-only changes. The headline rate moved from 77 to 30 percent (IT40 adjudication 37.5 percent) | strong as a check; the rate itself is not robust |
| What the check found | The first reader counted a qualifier anywhere as Q, including clauses taken from other papers and sentences that already state their limit. The class boundary, not the facts, drove the gap; both readers agree on every quoted figure | process lesson |
| S32 (candidate finding) | Confirmed on rendered panels (Suppl Fig 5G, 7F) by a reader who did not find it; no decision changes, so a dated pointer, not a CLAIM edit | strong |
| S45 | The first reader's N was an attribution slip (the sentence's "same paper" is the Tc-MEP paper). The second reader's check of the unit was stopped by a safeguard; IT40 judged from the sentence text only and said so | partial, declared |
| Orchestrator adjudication | IT40's third look at 13 contested rows is not blind and not a third rate; it is labelled as such and the verdict on E2 is left undecided | declared |
| Provenance of the read | Producer is a delegate; the receipt's coverage rests on its page-by-page read plus the second reader's panels; mp4 files not viewed | partial, declared |
| Friction | The landing gate refused the first push: a complete-read receipt on a record with no full-text marker fails `test_coverage_is_not_overstated_against_the_registry`; the batch commit closed it. Two merges of main also brought new receipts into the chained ledger, so the receipt was recorded again on a branch restarted from main each time | process |

## Dream pass
Material change: a headline rate from a single blind reader can reverse on a second reader because the W/Q line moves, not the facts; the PREREG fixed classes but not the Q test ("narrows what the sentence takes from this paper, not already stated in it, and a reader would act differently"). Connection queued as a proposal to ADV, not a claim: a PREREG that freezes a class rule needs a tested edge case (one row of each side) before the reader runs. Rejecting observation: a second batch where first and second reader agree within two rows.

## Capability scout
| Gap | Evidence | Decision |
|---|---|---|
| The two mp4 supplements of PMID 33914858 cannot be decoded here; a temporary decoder fetch was refused by the auto-mode classifier, not retried | Receipt names them unavailable; any claim resting on them is bounded to legend and text | CHANGE = NONE for the harness; a decoder is a standing operator item (ADV listed it as a stop) |
| Merging main into a branch that already recorded a receipt conflicts on the ledger, the state anchor, ranking, coverage and reading state | Five conflicting generated files on 2026-11-28 | CHANGE = NONE: restart from main and re-record; the pointer is in the checkpoint. A proposal to HE: `fulltext_receipts.py record --dry-run` could also run the registry-marker test, since only the push gate found it |

## Takeaways
| What | Lead or limit | Next |
|---|---|---|
| Neuronal deletion of Wwox (S-KO) reduces WWOX, it does not remove it: bulk RNA-seq hippocampus 0.184 (n 3 v 2), cortex 0.360 (n 3 v 4), File012; N-KO 0.068, null 0.101 (File013, n 2 v 2 and 2 v 3) | Any treated-arm design on this model needs the residual signal as a covariate | RP-019 design, ADV |
| N-KO and null also carry quantified myelin counts (Suppl Fig 5G and 7F, legend n = 3 per genotype each; points are fields in 5G, unit ambiguous in 7F) | CLAIM 003's evidence-boundary line is too narrow; direction unchanged | correction proposed in the RESULT for the next BATCH_COMMIT |
| Share of consuming sentences going beyond the paper: floor 7 of 23 to 26 (27 to 30 percent), up to 20 of 26 (77 percent) under a looser rule | E1 rejected under every reading; E2 not decided | ADV decides whether the Q test needs a fixed form |

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 4
machine: 2   blind_auditor: 1   peer: 0   self: 1
severity_high: 0   of which self: 0
undetected_known: 0
```
Machine: two classifier or safeguard stops (decoder fetch; a consuming-sentence unit lookup), neither retried. Blind auditor: the first reader's Q overcount, counted once. Self: IT40 first wrote ADV-336's WWOX-signal figure as a myelin figure in the draft RESULT; corrected before landing.

## Section 21c output
- `DEFAULTS_TAKEN`: S45 classed from the sentence text alone; the unit not opened.
- `STOP_LOG`: two refusals recorded above; none blocked the receipt.
