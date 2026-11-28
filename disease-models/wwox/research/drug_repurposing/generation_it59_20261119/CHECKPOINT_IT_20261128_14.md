# Checkpoint IT39 (window c817e528), 2026-11-28, written at about 250k context

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119. Read this file only (`_13` holds IT38's close; its "Traps" are in `_12`). Codex is never contacted. Worktree `it_39_20261128`; main at `e046d4808` when this was written.

## Done
* Bound (marker verified), main merged, effort high. IT38's owed ADV-335 self-evaluation addendum written (`self_eval_orchestrator_it38_20261128.md`).
* ADV-335 composition read again by a fresh reader: 0 of 9 class changes; two basis clauses qualified; "figure not held" negative withdrawn (PMID 22193544 Fig 1d is in the PMC open-data bucket: WWOX band lost with siRNA in SH-SY5Y, antibody unidentified); E2 "below one third without U6 or U7". Compared cell by cell with HE ADV-336: only the band the authors label 46 kDa (about 41.6 kDa on the printed ladder) is lost in knockouts; ~48 and ~50 kDa persist. ADV accepted: no registry edit. Dated notes on ADV-246/251 results. Details: `adv335_antibody_it_20261128/RESULT_ADV335_IT_20261128.md` (two addenda).
* Mandate rows closed as already consumed (IT28 queue, ADV-321, ADV-333); ADV-286 dates kept as one BLOCKED calendar row (C1 re-check 2026-12-05, C2 not before 2026-12-06, UNRESOLVED 2026-12-12). CI: all completed gate runs green; Pages run #301 red only in the smoke step (CDN served run #300's page; live equals a local build; HE records a retry patch as a proposal, the workflow is operator-reserved).
* Memory note `it39-antibody-composition-pitfalls.md`.

## ADV-337 (accepted by ADV): complete read of PMID 33914858 and blind comparison
Folder: `advisor_pilot_20261113/brainstorm_20261116/adv337_repudi_it_20261128/`.
* PREREG `PREREG_ADV337_IT_20261128.md` sha256 `9f18ec01e078ec3371400f72207c4dd1c247e37e59bb8ae04ca5990472e867c9`; sentences `SENTENCES_ADV337.tsv` (38) sha256 `16379cd157c7333ea47831822c5337e38dc2a6551999aa04e21d31cf7015e3fa`. Hashes taken 2026-11-28T16:34:56Z before the producer was dispatched; committed after (`a3b244e6a`, on main `e046d4808`). Denominator is a screen (sentences naming the paper); E1 beyond at most 10 percent of assessed, E2 at least one third, IT's expectation 15 to 33 percent.
* Producer (sonnet 5.5, effort high) returned the complete read; receipt draft `receipt_draft_producer_ADV337.json` (passes `staged_receipt_check.py`; placeholder event id `FTR-20261128-33914858-37` to reassign; no v2 work manifest yet; the two mp4 supplementary movies were NOT viewed, no decoder, so `supplementary` should be recorded as read with the movies named unavailable, or the depth weighed as partial). Producer facts: S-KO WWOX recounts from the authors' count sheets 0.19 (hippocampus, n 3 v 2), 0.18 and 0.36 (File012 hippocampus, cortex; n 3 v 4), so loss is incomplete; no rescue or re-expression experiment in the paper; interneurons not studied (snRNA n = 1 v 1); myelin, latency and organoid units are sections, FOVs or slices; text says "~6-fold" unmyelinated while the printed means give 4.9; Suppl Fig 6B legend says reduced while the bars show the reverse.
* Blind reader (sonnet 5.5, effort high; paper and the 38 sentences only, classes W/Q/N/O/U given in the brief) was dispatched after the producer: its reply reaches only the orchestrator. Its text goes to `BLIND_READER_AS_DELIVERED_ADV337_IT39.md` in the folder (written before IT39 stops).

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | Blind reader's table | if the file above is absent, the reader never returned: dispatch again with the brief in the PREREG classes and the same two inputs |
| 2 | Compose `RESULT_ADV337_IT_20261128.md` | shares W/Q/N/O/U with denominators, beyond = Q + N of assessed against the frozen E1/E2; say which of IT's expectation held; producer numbers labelled by panel and unit |
| 3 | Second reader on the composition | resume the producer (SendMessage to it) or use a fresh delegate; MUST CHANGE rate with denominator; one active delegate at a time |
| 4 | Receipt and PAPER record | PAPER 004 exists; reassign the event id, add the schema-v2 work manifest with the 8 to 12 locators, `fulltext_receipts.py record`, derived surfaces after one receipt (ranking, coverage, reading state, view) |
| 5 | Edits | claim edits only through BATCH_COMMIT after `test_batch_queue.py`, only where a decision changes (sentences narrowed, RP-017 premise wording, RP-019 conditional-arm design); otherwise a dated pointer; report to ADV |
| 6 | IT39 self-evaluation, capability scout, takeaways | owed; the ADV-335 findings above are the material |

## Traps met
* The consuming-sentence screen needs the CLAIM 003 core fields added by hand: its Title, Summary and Clinical meaning do not name the paper.
* `safe_push` merges main under the lock and moves HEAD; read the packet "at commit" line after a push, not before.
* A delegate slicing the claim registry with its own script is refused by the classifier; name `registry_records.py get --id`.
* Disk 8.4 GB at this point (floor 1.5 GB); copies of the paper artefacts (61 MB) sit in this worktree's ignored `files/fulltext/`; remove nothing yourself.
