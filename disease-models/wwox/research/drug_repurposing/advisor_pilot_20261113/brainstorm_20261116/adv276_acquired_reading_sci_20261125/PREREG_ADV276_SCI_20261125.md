# PREREG ADV-276 (SCI, 2026-11-25): read the newly acquired papers that cards and leads lean on

Written before any of the 16 papers below was opened in this assignment. Hypothesis level; nothing here is medical advice. Reference-genotype class only.

## Order (the lean, from the ADV-272 acquisition table; cards first, then leads)

Cards (10 papers): 20810895 (F03), 24321005 (H02), 28447936 (E01), 35222658 (P11), 36601084 (H02), 36967744 (P11), 38605177 (H01), 40670421 (H02), 40994429 (F04), 42470358 (H02). Leads (6 papers): 23435430, 22479346, 36530994, 24086726, 40500435, 30202070. Portfolio, ranking rows and claims only if time remains after these 16.
Within each group: papers whose latest receipt lists the most unread classes first (20810895, 28447936, 42470358 list methods, tables and results unread), so the largest chance of a changed sentence comes first.

## What counts as read, per paper

The classes the replaced receipt lists as not read, now read in the acquired bytes (Europe PMC XML or PMC article page): methods, results, tables, discussion, limitations as applicable. Figures stay `captions_only` (images are not opened unless I say so); supplementary stays `not_read` (not held). A receipt records only what was read; a paper where only abstract-level checks were made is recorded `queried_not_full_read`.

## Predictions (fixed now)

1. Papers read in increment 1 (about 60 minutes): 7 (range 4 to 10); in the two increments, all 16 is not expected (expected 12, range 8 to 16).
2. Papers whose reading changes a consumer's wording, among those read: 4 (range 2 to 7). A consumer's wording changes when a table, a legend or a methods statement contradicts, narrows or adds a unit/species/n limit to the exact sentence the card or lead uses.
3. At least one paper fails the check in the strong sense (a table, legend or methods statement contradicts the consumer's sentence): 60 percent.
4. The card rows that say "abstract level" or "no receipt" (38605177 H01, 40994429 F04) have the highest share of changed wording; the P11 rows that say "text read" (35222658, 36967744) the lowest.
5. At least one paper has an internal inconsistency of the kind found in 34021541 (two tables disagree, a stated rule contradicts a table, an unfilled placeholder): 50 percent.

## Rules (ADV-269, carried)

Every number carried from a table, workbook, figure or panel names the table, row, figure and panel; replicate unit and species beside every value; every printed ratio or sum recomputed; a negative carries its date and query; the consumer's whole row is read before a finding is called new; `held_studies.py` is the test of "held"; wording goes to IT as wording only. No delegate, no spend, no contact. PMIDs only in research files.

## Failure rule

A paper fails the check when a table, a legend or a methods statement contradicts the sentence the consumer uses. A paper that merely adds detail passes with a note.
