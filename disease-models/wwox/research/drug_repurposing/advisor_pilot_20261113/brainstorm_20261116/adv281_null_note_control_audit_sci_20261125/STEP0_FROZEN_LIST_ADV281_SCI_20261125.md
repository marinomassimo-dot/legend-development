# STEP 0, ADV-281: the frozen list (2026-11-25T18:59:07Z, before any source was opened)

Hypothesis level; not medical advice. Rule: `PREREG_ADV281_SCI_20261125.md` (sha256 `0946c595fcfc3964f9ed10b1590aeed446f2cd98a3e399acd2ef67611cfa6d04`).

| File | sha256 |
|---|---|
| `list_adv281.py` (phrases, both routes) | `845288812c5ab08828bcd5ca9e1ec94894231dc5f28db9b52a878f840534736e` |
| `route_hits_adv281.tsv` (130 rows found by either route) | `4ef1802339d05bda3ff869c6fd5a137a276aeacd0a54e78437f9830fa1af03c7` |
| `screen_adv281.py` (one decision per row) | `264e29234e6ee1cfea494ffc5a3c35f20a0b0d9f792cc7f6cf3123dae3c58d89` |
| `screen_adv281.tsv` (decisions, consumers) | `7434d8f1f7af480d569e090abee505c84df67201402cd4187c150bdb5819d921` |

## Counts

* 246 distinct assertion ids. Route S (`direction` = `NO_CHANGE`): 31. Route T (phrases): 125. Both 26, S only 5, T only 99, union 130.
* After screening the card text: **63 NULL rows** (26 both routes, 5 S only, 32 T only), 37 X-EVIDENCE, 25 X-OTHER, 5 X-NOMANIP.
* **Why the routes differ.** S misses every null written as a side arm of a row whose direction is something else (a control arm that did nothing inside an INCREASE row), and the transcript and genetic nulls coded UNKNOWN or by sign. T over-matches: "does not say", "was not read", "no effect size", and "null" used for a knockout genotype.
* Of the 63, 40 are drug assertions and 23 disease assertions (genetic or delivery manipulations). SCI's scan of ten was therefore an under-count by a wide margin.

## The ten of the brief

* Supported by both routes (5): DR-A01-003, DR-A01-004, DR-A02-009, DR-H01-003, DR-P11-006.
* Text route only (5 found): DR-A02-002, DR-E03-001, DR-H01-001, DR-L01-001, DR-M01-001. DR-E03-001 was matched by an incidental phrase ("is unchanged by this card"); its real null ("no half-maximal inhibition") is not in the phrase list, which is a recall limit of route T.
* **Dropped: DR-H01-001.** Its only match is "no effect size or n read"; the note records a suppression, not a null.

## Audit order (PREREG)

* Increment 1: DR-A01-003, DR-A01-004, DR-A02-002, DR-A02-009, DR-E03-001.
* Increment 2: DR-H01-003, DR-L01-001, DR-M01-001, DR-P11-006, DR-D01-002 (first addition by consumer-file count, 13).
* Queued additions, in consumer order: the other 53 NULL rows of `screen_adv281.tsv`, sorted by `n_consumer_files`.
* The predictions P1 to P3 were written for ten; nine of SCI's ten survive and are scored on nine. DR-D01-002 is counted apart.

## Set aside, reported to ADV

Six rows read "not different from wild type" as restoration (DR-AAV-GFAP-P5HD, DR-AAV-GFAPAREA-HD, DR-AAV-GLU20-HD, DR-AAV-MOTOR-HD, DR-C01-001, DR-D01-001). That is an equivalence-by-non-significance question, not an activity check, so it is not audited here.

## Limit

The screening is one reader's judgement of card text; it was not blind-checked. Consumer counts are tracked files naming the id, with card, view, join, checkpoint and audit files left out; they are a proxy for reach.
