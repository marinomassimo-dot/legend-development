# ADV-254 pre-registration: ledger leads with no primary PMID that consumers lean on (SCI; hypothesis level; not medical advice)

Frozen before the count of this assignment is run. Identification only: no primary is read in this increment.

## Already seen by the writer (not a prediction)

* ADV-249: 239 lead ids, 153 with a primary PMID by its rule, 86 with none.
* A quick count while scoping found that only DL-BIO-009 (cards E02, E04) and DL-MECH-153 (card L01) among the 86 are named by a card, claim, model, investigation or trigger. DL-BIO-009's text was printed.

## Rules

* **No PMID:** the lead's blocks in `research/discovery_ledger_current.md` contain no PubMed identifier (ADV-249's `primaries()`; second route: any `PMID`, `pubmed.ncbi` or bare 8-digit number after "PMID" in the block).
* **Consumer:** the lead id is named by a card or packet, a claim, the working model or disease model, a portfolio, investigation or trigger row, a hypothesis record, the mechanism-intervention map or another analysis file. Cross-references between ledger leads are counted separately and are not consumers. Two routes: (1) `git grep` per lead id; (2) the record-aware split of ADV-249's script, extended to the same surfaces. Generated files (join output, rankings built from the ledger) and census, receipt, audit, assignment and history files are not consumers.
* **Identifiers inside a lead:** PAPER, CLAIM, DOI, PMC, GEO ids and "Author year" strings. A PAPER id resolves to a PMID through `paper_registry_current.md`; a DOI or "Author year" through the registry first, then Europe PMC search (spaced requests).
* **Outcome per lead with a consumer:** **found** (every primary the lead's statement rests on has a PMID or a stable identifier), **partly found**, **not found** (what is missing), or **inference** (the lead is a model inference that names no primary of its own; then say how its consumers word it).
* Leads without a consumer are only counted by identifier class (registry id, DOI or accession, author-year only, nothing).

## Expectations (scored in the result)

* E1: at most five of the 86 have a consumer.
* E2: at least half of the 86 name a registry id, DOI or accession, so "no PMID" is mostly not "no source".
