# PREREG ADV-287 step 2: the card statements that carry a superlative or count word (SCI, 2026-11-25; hypothesis level; reference genotype class only; not medical advice)

Frozen before any source of a NEW statement is opened. Authority: ADV decision of 2026-11-25 after the ADV-287 result (checkpoint AO section 1): this pass only; the full H02 (40) and A01 (20) passes and the second random 20 stay HELD until IT reports the ADV-282 and ADV-287 sentences applied. Held bytes only; no search, no acquisition, no spend, no contact.

## Universe (a census, not a sample)

`list_adv287_step2.py` -> `list_adv287_step2.tsv` (sha256 first 16: 9084a56cd461145c): the pattern "the one", "the only", "largest", "three independent", "none", "at least", "every", "independent" over the 239-statement universe of `../adv287_card_statements_sci_20261125/universe_adv287.tsv` returns 22 statements, the count ADV named (the first six words alone return 14; "every" and "independent" are the two further words that reproduce the per-card counts printed in RESULT section 4). Of the 22: 5 were audited in step 1 (n=1, 3, 9, 15, 17: classes carried, not re-read), 1 is stopped by the Obeid rule (k=5, card C04: its only source is PMID 42422765; neither the article nor its manifest or receipts are opened), **16 are new**.

## Word role (judged on the sentence alone, before any source)

LOAD_BEARING (the word asserts a count, uniqueness, extremum or universality that the source can falsify): 12 of the 16 new (k=2, 7, 8, 9, 10, 11, 12, 13, 17, 18, 20, 22). INCIDENTAL: 4 (k=3 hedge, 6 pronoun, 16 interval, 21 proposed design).

## Classes

As in step 1: CORRECT, INCOMPLETE (comparator, row or document left out), WRONG (number, count or unit), NOT ASSESSABLE (source not held, or a proposed design with no source claim; reason named). A negative or uniqueness claim ("the one", "none", "no ... in X") is judged over the whole set it names: the producer states that set (which rows, documents or database entries, with the date of the pull) before judging. For every non-CORRECT statement a second field says whether the error is carried by the marked WORD or sits elsewhere in the sentence (OTHER).

## Comparator (computed from step 1, before this pass)

Step 1, assessable statements, both-reader errors: marked sentences 3 of 5 (errors n=1, 3, 15); unmarked 3 of 12 = 25 percent (errors n=2, 14, 20). The unmarked rate is the comparator.

## Predictions

1. Assessable among the 16 new: 13 to 15.
2. INCOMPLETE-or-WRONG among the assessable LOAD_BEARING statements: central **33 percent, range 15 to 55**.
3. INCOMPLETE-or-WRONG among the assessable INCIDENTAL statements: central 20 percent, range 0 to 50 (three or fewer statements; not interpreted alone).
4. At least half of the errors in LOAD_BEARING statements are carried by the marked word.

## Rejecting observation

The both-reader INCOMPLETE-or-WRONG rate over the new assessable LOAD_BEARING statements is **at or below 25 percent** (the unmarked step-1 rate): the words do not concentrate errors. Then no further pass is scheduled by word; the wording rule in IT's recipe stays as a cheap habit resting on step 1 only, and this is said. With 11 or 12 assessable one statement is 8 or 9 points, so the decision is fragile within one statement either way; the leave-one-card-out rate is reported beside it and a decision that flips under it is called UNDECIDED.

## Protocol

Producer (legend-delegate, model sonnet, effort high, stated in the dispatch and read back): for each new statement writes `producer/src_KK.md` containing ONLY the source pointer, the whole source table or verbatim passages with their locators (sheet or figure, panel and row; species and replicate unit beside each value) and no verdict or commentary; and one row per statement in `producer/STEP2_TABLE.tsv` (k, card, sentence, source set, recomputation, class, carrier WORD or OTHER, affected span, corrected sentence, reading depth). Blind reader (a second legend-delegate, sonnet, effort high): receives only the sentences and the src files, never the producer's table. SCI verifies every non-CORRECT on the held bytes. The rate is reported over both-reader agreement; disagreements are listed and counted as a sensitivity range.
