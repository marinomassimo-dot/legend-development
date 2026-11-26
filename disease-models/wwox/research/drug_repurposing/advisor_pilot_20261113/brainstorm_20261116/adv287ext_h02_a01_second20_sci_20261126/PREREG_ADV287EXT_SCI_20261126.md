# PREREG, ADV-287 extension: card families H02 and A01 in full, and a second random 20 (SCI, 2026-11-26; hypothesis level; not medical advice)

Frozen at 2026-11-26T02:07:51Z, before any source of any listed statement was opened by SCI or a delegate of this window. Session c6d4dd83 (claude-sonnet-5-5, effort high). Authorisation: ADV-287 section 4 extension (items 1 and 3 of its RESULT), hold lifted by IT's apply 49b7ac71a; mandate step accepted 2026-11-26T02:04:49Z.

## Population and draw (files in this folder)

* Eligible: sentences of the frozen ADV-287 universe still printed verbatim in the same card packet and not audited before (step 1 sample, step 2 list). Counts in `counts_ext.tsv`: H02 30, A01 16, other families 146. Sentences rewritten since 2026-11-25 (IT's corrections, blind-checked by IT when applied) drop out by the verbatim test. Excluded cards and Obeid mentions stay excluded; rows whose enclosing record names only the Obeid article as source are removed from the record's own source field, nothing opened (13 rows, cards C04 and J01), leaving 133 in the other families.
* Draw: ADV-287 rule (strata route1 and route2-only, largest remainder: 11 and 9; `random.Random(287)` over rows sorted by card and sentence; reserves in draw order). `sample_ext.py`, `list_ext.tsv`.
* Screen on the sentence alone (`screen_ext.py`, `screened_out.tsv`): no computed or comparative quantity (label, design description, proposal, "ratio", "range" or "versus" without a value) is out; a sentence with text identical to one already drawn counts once (R-19 stands for four). Result in `sample_final.tsv`: H02 25, A01 14, random 20 (13 card families).
* A01: IT is landing changes to card A01 (drug_assertions [0], [1], [3]). A01 sentences are re-tested for verbatim presence on the main that carries IT's sha, before their first reading; a changed sentence drops out and is counted. A sentence under a pending ADV-282 correction (DR-H02-036 clause, DR-A01-007) is not part of the draw or is reported apart.

## One matching rule (first reader, blind reader and SCI alike; no phrase added for one reader)

Judge the sentence as printed in its card record (target, endpoint and context fields of that record may be read to know what the sentence is about) against the WHOLE cited source (every table, row, figure and the whole answer), not the quoted row.

* **CORRECT**: every number, count, unit, direction, attribution and absolute word (the only, the one, none, all, largest, not stated, not measured) holds.
* **ADD**: holds, but the same source carries a fact worth adding. Not an error; counted apart.
* **WRONG**: a number, count, unit, direction or attribution is not what the source gives.
* **INCOMPLETE**: the numbers match, but a left-out comparator, row, document or condition makes the stated number, ratio, range, superlative or negative untrue or misleading **as stated**. An omission that only adds context is ADD.
* **NOT ASSESSABLE**: source not held or not readable (named), or the sentence states no fact of any source (a proposal). A partly assessable sentence is judged on the assessable part and the rest is named.
* A negative ("not held", "no measurement", "never read") is verified only with a search carried out now, its date and query written; otherwise **UNSETTLED**.
* Numbers are labelled by sheet, figure, panel and row, never by position; replicate unit and species beside each value; every printed ratio, fold, range and sum is recomputed from ALL rows. A lower-bound or upper-bound value cannot carry a claim beyond its bound.

## Readers

First reader: legend-delegate, sonnet, effort high stated in the dispatch and read back. Blind reader: a second legend-delegate, same setting, given the card id, the verbatim sentence, the record's source and locator fields, and nothing of the first reading; it opens the whole held source itself. One delegate at a time. SCI checks every non-CORRECT and every disagreement on the original. **Only an error that the blind reader also calls WRONG or INCOMPLETE and that SCI verifies on the original is counted as MUST CHANGE**; first-reading counts are not results. Held bytes and repository files only; no web, no acquisition, no contact; the Obeid 2026 article, its manifest and receipts are not opened.

## Predictions (assessable statements; verified MUST CHANGE)

| set | statements | central | range |
|---|---|---|---|
| H02 | 25 | 15 percent | 5 to 35 |
| A01 | at most 14 | 20 percent | 5 to 40 |
| random 20 | 20 | 20 percent | 5 to 40 |

Calibration: ADV-287 step 1 6 of 17 (35 percent), step 2 5 of 12 load-bearing; ADV-282 verified 5 of 22 (23 percent); lower here because sentences with absolute words were mostly audited already and rewritten ones are excluded. NOT ASSESSABLE among all: 5 to 18. ADD: more frequent than MUST CHANGE.

## Rejecting observation

Verified MUST CHANGE at or below 10 percent of the assessable statements of the pooled 59 (or fewer after A01 changes): the statement audit of the cards stops after this pass and no third sample is drawn; the next held-source work is then the one-consumer reading batch. H02 plus A01 and the random 20 are also reported separately, with exact binomial intervals.

## Consumers

Corrected sentences to IT (card owner), verified MUST CHANGE and ADD listed apart; the result to ADV.
