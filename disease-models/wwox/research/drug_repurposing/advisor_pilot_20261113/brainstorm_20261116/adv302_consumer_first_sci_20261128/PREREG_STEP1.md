# ADV-302 step 1: frozen prediction and counting rule (SCI, window 64fc909a)

Frozen 2026-11-28T07:04:41Z, before any consumer count of the unread tail was run. Hypothesis level; not medical advice.

## Prediction (ADV's, copied from assignments/ADV-302.md)

At least 6 catalogued-only records without a receipt carry a consumer; strict at least 1 of the three read.
Rejecting: 0 consumer-bearing records (park the tail, resume when a consumer appears); 3 or more read and 0 strict (park by consumer rule).

## Population

The records of `coverage_report.py --json` `reading_debt` that carry no receipt (`reading_debt_split.no_receipt`, 185 at this tip; 194 when the assignment was written).

## Counting rule (fixed before the first count)

* A record is identified by every PMID, DOI, PMCID and `PAPER NNN` id on the identifier lines of its registry entry (and of any other entry sharing one of them).
* Count A (script): `framework/scripts/consumer_count.py` as on this tip (surfaces: claims, models, discovery and hypothesis ledgers, cards, portfolio, investigation rows).
* Count B (independent): my own fixed-string search of the same identifiers over every tracked text file under `disease-models/wwox/`, registries of papers and tracking, receipts, coverage report and generated views excluded; no code shared with count A.
* A record is **consumer-bearing** only if both counts hit it. A hit by one count only is listed and read by hand, with the reason.
* **Consumer** means a unit that uses the study (a claim, section, lead, hypothesis, card, portfolio or investigation row). A queue line, census line, search log or session report that only lists the study is not a consumer; each reported unit is opened before it is counted.
* Unit order for step 2: number of distinct consumer units from count A after hand check; ties by number of units that state a result of the study, then by PMID ascending.
