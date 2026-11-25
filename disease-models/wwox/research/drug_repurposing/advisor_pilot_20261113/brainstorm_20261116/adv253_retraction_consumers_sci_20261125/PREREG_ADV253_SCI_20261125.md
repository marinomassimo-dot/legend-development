# ADV-253 pre-registration: who depends on retracted material behind review PMID 28045433 (SCI; hypothesis level; not medical advice)

Frozen before this window opens the review, the retracted article, the retraction notice or any figure image.

## What is already known to the writer (not a prediction)

* The repository records that PMID 28151481 (*Cell Death Dis*) is retracted (notice PMID 35680840) and that review PMID 28045433 "reuses its data/dependencies". ADV-249 did not open the review.
* A repository search made while scoping showed that `analysis/wwox_expression_boost_census_20260922.md` row A10 (decitabine) cites only PMIDs 28151481 and 28045433.
* The discovery ledger lead DL-MECH-025 states that the review reuses a Figure 3B (per checkpoint AF; the lead text is re-read after this file is frozen).

## Questions

1. What does the review's Figure 3 (text citation and legend) show, and does it come from the retracted article?
2. Which other statements of the review rest on the retracted article?
3. Which cards, lead rows, portfolio rows, hypothesis records, claims, paper records, model files and analysis rows lean on either?

## Material

* Retracted material: **the whole article** PMID 28151481 (the notice retracts the article, not single panels). Panels the notice names are listed separately, so both levels are reported.
* Review material that counts as retracted: any figure, panel, value or sentence of PMID 28045433 whose cited source is PMID 28151481.

## Listing rule (two routes, both run; a row counts if either finds it)

* Route 1, line search (`git grep`) over tracked files for: PMIDs 28045433, 28151481; DOIs 10.3390/ijms18010075, 10.1038/cddis.2016.403; PMC5297710, PMC5386451; DL-MECH-025; the registry ids of the two papers (PAPER, LIT and CORPUS-STUB numbers found by the first search); "Bendinelli" and "Maroni" near 2016 or 2017.
* Route 2, record-aware split of the canonical registries, ledgers, cards, TSV tables and analysis files (one unit per record, row or card), with the same identifiers, plus a **value route** without identifiers: decitabine together with WWOX; 1833; HGF, TAZ or Met together with WWOX; HIF-1 together with bone metastasis.
* The review's reference list is screened with `dependency_integrity.py screen` for other retracted or noticed items (a screen, not a verdict).
* Listed but not classed as consumers: bibliographic census files, receipts, locator audits, session evaluations, assignment and checkpoint files, history files.

## Dispositions (one per consumer row)

* **depends**: the statement or value has no cited support other than PMID 28151481, or the part of PMID 28045433 that restates it.
* **independent**: another primary, not a restatement of the retracted one, is named for the same statement. The depth at which that primary was read is written beside it.
* **mixed**: the row carries two or more statements, at least one dependent and at least one independent; each is named.
* **describes the retraction**: the row is about the retraction itself; nothing leans on it.
* **unclear**: the row does not say which source carries the statement.

A citation of the retracted article in support of nothing (a bibliography line, a census row) is "no statement".

## Figure comparison

If the figure images of both articles are retrievable by an open route (Europe PMC, PMC open-data bucket; no challenge page is passed), compare review Figure 3 panel by panel with every figure of the retracted article. "Same content" needs the same visible image or the same plotted values with the same labels; it is reported as a visual observation by one reader, not as a finding about conduct. If the images are not retrievable, the answer to question 1 rests on legend and text and says so.

## Expectations (scored in the result)

* E1: no card and no claim record depends on the retracted material.
* E2: the review's Figure 3 restates retracted-article data at least in part (the repository says so, unchecked).
* E3: at most five consumer rows are classed "depends" or "mixed".

## Limits

One reader; no delegate; no edit of any registry, card or claim (wording for IT only); no spend; no contact; spaced requests; no e-mail address to any service.
