# ADV-262 pre-registration: the three unheld primaries behind the claims' n (SCI, 2026-11-25)

Written before any search for the three papers and before any of them is read. Actor `orchestrator` (SCI). Hypothesis level; no spend, no contact, no e-mail address in any request. Brief: `assignments/ADV-262.md`.

## Question
PMIDs 17803050 (CLAIM 038, rat phosphate and BUN), 34214506 (CLAIM 034, "n = 2" loss-of-function evidence, PAPER 054) and 40875931 (CLAIM 033, registry cohort, Table 2 mortality by genotype class) were "not checked" in ADV-261. For each: is the n independent, and what unit is stated?

## Routes, in order (a challenge page, 403, 429 or 500 is a result and ends that route)
1. Receipts ledger and `files/fulltext` by PMID, by title words and by SHA-256 of any stored artefact (`evidence_presence.py --search`).
2. Europe PMC `fullTextXML` and `supplementaryFiles`; the PMC article page; the PMC open-data bucket.
3. The publisher's open page; the PubMed full-text tool for an open article.
4. Not used: ResearchGate, any resolver that asks for an e-mail address, authors, paid services.
A paper no route reaches goes to `files/operator_inputs/PDF_REQUEST_LIST_ADV223_20261124.md` with its consumer claim.

## What counts
* **Unit stated:** the legend or Methods names what n counts (animals, cultures, wells, slices, individuals, families) in one place, and a second place agrees or does not conflict. One place = "one source".
* **Read:** Methods, the Results sentence carrying the n, the legend or table; supplement table if open. Coverage in the receipt is stated as read, not as intended; an abstract is not a read.

## Predictions (fixed now)
* 17803050 (Suzuki 2007, rat lde): the "4 normal, 5 mutant per sex" are animals, independent; litter of origin not stated. P(independent) 0.75.
* 34214506 (Saadane 2021): the "n = 2" counts independent experiments on one cell line or one culture, not separately derived units: not independent for derivation. P(non-independent) 0.6.
* 40875931 (registry cohort): the counts are individuals; families are not reported or include siblings, so the genotype-class comparison cannot be called family-independent. P(families not stated or clustered) 0.6.
* At least one of the three is not reached by any open route: P 0.5.

## Output
Per paper: verbatim locator for the n and the unit, receipt with honest coverage, effect on the ADV-261 table (stays non-independent / becomes independent / stays unknown), wording for IT. Two increments, about 90 minutes.
