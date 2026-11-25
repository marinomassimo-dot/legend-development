# PREREG, ADV-282 increment 2: ranks 9 to 16 of the ordered queue (SCI, frozen 2026-11-25T19:51:19Z)

Hypothesis level; reference genotype class; nothing here is medical advice. Same actor, brief, classes, comparator rules and blind check as `PREREG_ADV282_INC1_SCI_20261125.md`. Written before any source of these rows was opened by this window.

## Rows

DA-J01-006, DA-K01-008, DA-M01-002, DA-W2-002, DA-J01-008, DA-J01-002, DA-M01-007, DA-L01-001 (`queue_ordered_adv282.tsv`). Seen when this was written: the note, `source`, `direction` and `reading_depth` of each, and the increment-1 first reading.

## Increment 1 deviation, recorded here

Ranks 7 and 8 (DA-W2-011, DA-I01-006) were NOT audited: a safety classifier stopped the session's response as the extraction of their source article was starting. The step is not retried or rephrased. They stay queued by id, and the increment-1 predictions are scored on six rows.

## Predictions

Calibration: ADV-281 loose 4 of 9 and strict 1 to 2 of 9; increment 1 first reading loose 0 of 6, MUST CHANGE 2 of 6 (blind check not yet returned).

* P1 strict: 1 of 8, range 0 to 2.
* P2 loose: 2 of 8, range 1 to 4.
* P3 blind MUST CHANGE: 2 of 8, range 0 to 4.
* P4 blind MUST CHANGE or ADD: 6 of 8, range 4 to 8.
* P5 rows where the held bytes cannot be assessed: 0, range 0 to 1.

The rejecting observation of increment 1 now applies to the 14 audited rows of the two increments: loose 3 of 14 or fewer means the genetic and transcript nulls are mostly checked and a positive-control field, if proposed, is limited to compound and delivery rows.
