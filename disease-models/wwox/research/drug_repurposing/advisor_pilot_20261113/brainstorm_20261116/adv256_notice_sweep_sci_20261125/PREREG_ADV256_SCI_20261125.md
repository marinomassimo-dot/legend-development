# ADV-256 pre-registration: retraction and correction notices over the catalogued WWOX PMIDs (SCI; hypothesis level; not medical advice)

Frozen before any catalogue list is built or queried for this assignment.

## Already seen by the writer (not a prediction)

From ADV-253 and its searches: PMIDs 28151481, 25447306 and 26041563 are retracted and flagged; 19357348 is retracted (notice 42583763) and unflagged in `batch_queue.md`; 23446842 and 37156116 are recorded as retracted.

## PMID source list (two routes, counts reported)

* Route A: the PMID column of `corpus_seed_pubmed_20260806.tsv` plus every PMID in `paper_registry_current.md` identifier lines.
* Route B: every PMID in `batch_queue.md` and in `literature_tracking_log_current.md` identifier lines.
* The sweep runs over the union; the set differences are reported. A PMID that is itself a notice stays in the list and is marked as a notice.

## Notice rule (Europe PMC REST, `resultType=core`, source MED, no key, no contact parameter, spaced requests)

* **Retracted:** `pubTypeList` contains "Retracted Publication", or `commentCorrectionList` has "Retraction in" or "Partial retraction in".
* **Expression of concern:** a link "Expression of concern in".
* **Corrected:** a link "Erratum in", "Corrected and republished in", "Retracted and republished in" or any other type naming a correction.
* Each hit: the notice PMID (or citation text) and the notice's first publication date.
* A PMID not returned is "not indexed", never clean. A 429, a challenge or a non-JSON answer stops the run; no retry within the minute.

## Comparisons

* The Retraction Watch snapshot of 2026-10-21 held under `files/retraction_watch/`: which hits it lists (by PMID or DOI) and which it misses; and snapshot-listed catalogue records that Europe PMC does not mark.
* Repository note per hit: whether `batch_queue.md`, the paper registry or the literature log says retracted, concern or erratum for that PMID (or names the notice).

## Consumers

For every retracted or concern hit that the repository does not already flag, and for every flagged retraction: two routes (`git grep` by PMID and DOI; the record-aware split of the ADV-253 script), with the same dispositions as ADV-253. Corrections: consumers counted only for records a claim, card or ledger lead names.

## Expectations (scored in the result)

* E1: between 5 and 25 catalogued records are retracted.
* E2: between 1 and 3 retracted records carry no repository flag (19357348 counted).
* E3: at least one retraction notice dated August 2026 or later is absent from the snapshot.
* E4: no claim record leans on an unflagged retraction.
