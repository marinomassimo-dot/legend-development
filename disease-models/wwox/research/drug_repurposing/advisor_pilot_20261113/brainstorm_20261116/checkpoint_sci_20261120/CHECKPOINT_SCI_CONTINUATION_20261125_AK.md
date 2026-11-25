# Checkpoint AK: SCI continuation of 2026-11-25 after ADV-279, for the successor that takes ADV-280 (resume from AI + AI addendum + AJ + AJ addendum + this file; hypothesis level; not medical advice; not edited once hashed)

Why: ADV asked for it (the tick read context at 316k). Written by session `8ee4045d-dc8b-4fb7-bcc6-f0a9721f8ead` (claude-sonnet-5-5; the opening brief required effort high). Standing rules unchanged: AH sections 0 and 5, AI section 0 (release and bind procedure, no e-mail address to any service or into a public file, challenge pages are results, no spend, no contact, Codex paused, frozen RP-045, sealed ADV-174 and ADV-175, no renames, reply to the operator in Italian, files in English, state model and effort in every dispatch). Peers on the roster at writing: ADV - CURRENT a5e6f2ad, IT Orchestrator - CURRENT 61513c04 (past its restart line: look for its successor), HE - CURRENT 02915fa6; run `ListAgents` first. Commit trailers: the lines the session's own reminder gives.

## 1. State

* **ADV-279 is closed**, both increments, on development/main `449e8c300`; consumed by ADV; mandate step `OBJ_ACCEPTED[121]` DONE (121 done, 1 blocked on the operator's papers, 0 to do). **Nothing of it is left to read.**
* Folder, under `brainstorm_20261116/`: `adv279_next_ten_held_partials_sci_20261125/`: `PREREG_ADV279_RULE_...` (the rule), `..._ORDER_...` (counts, order, predictions), `..._AMENDMENT1_...`, `count_adv279.py` with its TSVs, `BLIND_STATEMENTS_INC1/2`, `BLIND_REPORT_INC1/2`, `RESULT_ADV279_INC1/INC2`, `FILES_VIEWED_ADV279_SCI_20261125.tsv`, ten receipts and the two receipt scripts.
* Counts: of 109 ranked partials with consumers and an unread class outside earlier batches, **3** are readable from held bytes under the old rule and **51** under the wider rule (routes A 47, B 47, both 43).
* Read: increment 1 = 33914734 (strict), 37781246 (loose), 39769031 (no change), 42875792 (strict), 28749468 (loose); increment 2 = 30266908 (strict), 34359949 (strict), 37248434 (loose), 37275776 (strict), 36278433 (loose). Batch: strict 5 of 10, loose 9 of 10; supplement class 4 of 7 and 6 of 7; figure class 1 of 3 and 3 of 3; text class none; reversals 0. Predictions P1 (strict 2, 0 to 4) and P2 (loose 4, 2 to 7) both missed high.
* IT has the wording (two messages, nine items), has not applied it, and queued it for its successor (CLAIM 011 and CLAIM 043 by BATCH_COMMIT). IT also re-derives the five strict findings as owner (ADV).
* `36278433`: supplement not read whole (receipt marks figures only).

## 2. Open work, in order

1. **Accept ADV-280** into the mandate (`mandate_continuity.py accept`), brief `advisor_pilot_20261113/assignments/ADV-280.md` (in the root checkout at writing; it lands with ADV's next push). The mandate record reads ALL_BLOCKED until you do.
2. ADV-280 in short (the brief governs): the next ten of the remaining readable records in the same consumer-count order; PREREG first, predicting from the last two batches (strict 4 of 10 and 5 of 10); list error-page, empty or otherwise unreadable held files before any delegate reads; two increments of five; blind second reading of every pivotal item; supplement and figure class with two counts each; wording to IT; report to ADV, who then rotates SCI off this strand.
3. Session end skills and a final report in Italian.

Of the 51: ten read, and left out by amendment or order with a reason: 28151481 (retracted), 28045433 (only held figure already read), 30362252 (error pages), 33958783 (false consumers), 41948127 (only held figure already read). Re-run `count_adv279.py` against today's ledger and apply these exclusions; do not take the remainder from memory.

## 3. Method for figure and supplement receipts

Open every held figure of the class as an image, or render every page (`pdftoppm -r <dpi> -png`; `pdfimages` for a single embedded raster), and look at each; say where only a thumbnail was looked at. Mark `figures` or `supplementary` as `read` only if every held item of the class was looked at; otherwise leave it `not_read` and say what is missing. ADV-280 asks for the PNG hash of the rendered page: record the sha256 of each rendered PNG **and** of its source file. ADV-279 recorded source-file hashes only (`FILES_VIEWED_...tsv`); its rendered PNGs were scratch and are not hashed. Receipt pattern: `make_receipts_adv279.py OUTDIR` (event id, `prior_receipt`, fingerprint of the XML, basis sentence); record one by one, `verify`.

## 4. Checklist

`adv276b_lead_receipts_sci_20261125/PRE_READ_CHECKLIST_ADV276_SCI_20261125.md`, four lines added: a table printed as an image; the sibling panel; every arrowhead in every enlarged panel; held bytes must match the file name.

## 5. Landing facts and lessons

* After receipts, in order: commit the receipts; `coverage_report.py`, `reading_state.py`, `ranking_it8.py run`; commit; **then** `repurposing_view.py run`, `run --source shareable`, `package`, `i18n --what collect`; commit; `candidate_tree_freshness.py --candidate HEAD --base development/main --all` must say FRESH; then `safe_push`. Skipping the views cost two refused pushes.
* No `#` comment lines in a `.tsv` (landing suite red).
* Push as in AJ section 3; the lock queue was 2 deep, 7 to 15 minutes per try.
* One image-location reading of ADV-276 (27845895 Figure 10) was wrong and is corrected by an appended section in that RESULT.
* Self-evaluation: `research/session_evaluations/2026-11-25_sci_adv279.md`. Capability gap recorded: held-file content check (routed to HE through ADV).
