# Receipt-ledger notice sweep (ADV-044, step 1; HE; 2026-11-18)

Written for: ADV, then whoever reads receipts before building on a paper. Zero spend; no ledger write; not medical advice.

## Answer
**No PMID behind a receipt has gained a Correction, Expression of Concern or Retraction notice after it was read.** Of 1,435 distinct PMIDs in `fulltext_read_receipts.jsonl` (2,035 rows, read 2026-11-18), Europe PMC links 44 notices to 42 of them: 41 `Erratum in`, 2 `Expression of concern in`, 1 `Retraction in`. All 44 are dated before the first receipt for that paper (`notice_sweep.tsv`, column `vs_receipt` = PRE; nine old errata are listed by citation only and dated from the citation year, 2006 to 2015). Post-dating: 0. The cut is the date of the notice's first publication against the ledger's `event_at`, at the precision the notice date has.

## Is there a later sweep already
No ledger-wide one. What exists: the per-reading `retraction_check` in each deep-dive manifest (at reading time), `erratum_scope_check.py` (manifests only: 594 examined, 387 with an erratum recorded, 107 SCOPE_UNDECLARED), and `dependency_integrity.py` (Retraction Watch snapshot of 2026-10-21, DOI-keyed, retraction and expression of concern, plus a corpus mode over reference lists). The new `epmc_notice_sweep.py` is the first that walks the receipt ledger, and it is the only one that asks the post-dating question.

## Second route (absence needs two)
Retraction Watch join over the 1,389 receipt DOIs: one hit, `16223882` (expression of concern, 2017-04-03), the same paper the 2026-09-09 sweep found. Europe PMC found two more integrity notices (below) that the snapshot does not list. Not seen by either route: a notice PubMed never linked to the paper, and any notice dated after 2026-10-21 for the Retraction Watch route.

## The three integrity hits and who consumes them
| PMID | Notice | Receipts | State |
|---|---|---|---|
| 16223882 | Expression of concern, PMC 28373548, 2017-04-03 | 1, complete read, 2026-09-09 | already known: flagged by `dependency_integrity.py` in the 2026-09-09 sweep |
| 23446842 | Retraction, notice 42464650, 2026-07-17 | the legacy receipt was invalidated by the identity audit of 2026-08-06 (the registry's PAPER 032 owns another PMID); no live reading | already handled: `PUBLICATION_INTEGRITY_HOLD` on the registry record, no claim rests on it, status `not_processed` |
| 39083422 | Editorial Expression of Concern 40512803 (2025-06-13); the paper also has the Correction 39432800 (2024-10-21) | 3 receipts, partial reads, 2026-11-13 | the SCI50 producer and verifier missed both; the SCI51 verifier found them and `m1_ebp_reagents_sci51_20261113/consumer_delta.md` row 4 records the update as APPLIED (SCI50 claims carry a dated update line) |

So the sweep adds no new integrity case. It confirms that one of the three was caught only by a second blind reader.

## What the sweep does show: the erratum question is open outside the manifests
30 of the 42 PMIDs have receipt text that never mentions the notice (the other 12 do). Of those 30, 2 are the integrity cases above and 28 are errata. Twelve of the 28 carry verbatim locators in a partial or complete read, and **none of the twelve has a deep-dive manifest**, so `erratum_scope_check.py` has never seen them (`--pmid` returns 0 manifests). The notice was out before the reading in every case, so nothing here is a later discovery; it is a question the reading did not record. Most errata are cosmetic; whether any of these corrects a panel a locator stands on is not known.

| PMID | receipt events | depth | erratum | erratum date |
|---|---|---|---|---|
| 19503085 | 1 | partial_fulltext_read | 40670687 | 2025-08-01 |
| 21822218 | 2 | partial_fulltext_read | citation only | 2011 Nov 2 |
| 22622579 | 1 | partial_fulltext_read | citation only | 2014 Jul 17 |
| 23536761 | 1 | partial_fulltext_read | citation only | 2013 |
| 24209626 | 1 | partial_fulltext_read | citation only | 2015 Apr 23 |
| 24997607 | 1 | partial_fulltext_read | 38997609 | 2024-09-01 |
| 25186741 | 3 | partial_fulltext_read | citation only | 2015 Jan 14 |
| 29533123 | 2 | partial_fulltext_read | 30507342 | 2018-12-03 |
| 30919030 | 2 | partial_fulltext_read | 31482207 | 2019-09-03 |
| 35655584 | 1 | partial_fulltext_read | 36176337 | 2022-09-26 |
| 36594817 | 1 | partial_fulltext_read | 39404600 | 2024-10-15 |
| 37006625 | 1 | partial_fulltext_read | 37152903 | 2023-04-20 |

Suggested re-reading order: by the erratum's own scope text once fetched (author-name corrections `21822218`, `23536761` can be cleared from the erratum note in the Europe PMC record; the others need the erratum read). I did not read any erratum.

## Limits
* 6 PMIDs are not in the Europe PMC `MED` source (`not_indexed.txt`): all PubMed-indexed preprints (2025 to 2026). A published version, if any, is not followed.
* A notice date is its first publication date; Europe PMC may link it later. A later link of an old notice would read PRE here.
* `Erratum in` is a PubMed link type; a publisher correction PubMed never linked is invisible.
* The check does not read any notice: a PRE hit says the notice existed at reading time, not that the reading saw it.
* 12 of 42 receipt texts mention a notice; the regex (erratum, correction, concern, retract) can miss other words.

## Repeat it
`python3 framework/scripts/epmc_notice_sweep.py --out <folder>` (about 2 minutes, one request at a time, 1 s pause, no key, no contact parameter; a non-JSON or challenge reply stops the run with exit 2). Cadence: after every batch that adds receipts for papers not yet in the ledger, or monthly; it needs no scheduler. Exit text prints the count of POST-DATING hits; any non-zero count is the re-reading list. Offline checks: `python3 framework/scripts/test_epmc_notice_sweep.py`.
