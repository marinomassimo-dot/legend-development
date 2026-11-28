# ADV-302 step 2: addendum, availability and reduced set (SCI, window 64fc909a)

Written 2026-11-28T07:12:02Z, before any section of 26041563 or 25703206 was read and before any delegate dispatch. Read before writing: PubMed and Europe PMC metadata, graphic file names, and the body of the retraction note (PMID 32799870). The rule of `PREREG_STEP2.md` is unchanged.

## Routes tried for each consumer-bearing record (2026-11-28; no address given to any service; refusals are results)

| PMID | full text | routes and results |
|---|---|---|
| 26041563 (R1) | yes | Europe PMC fullTextXML 200; supplementaryFiles 200 (7 figures, 3 supplements); retraction note PMC7429703 200 |
| 19465938 (R2) | no | Europe PMC: no PMC copy; nature.com article page 200, subscription preview only; OpenAlex closed; HAL 0 records; CORE record without a file; Semantic Scholar 429 (queued as FT-180) |
| 14695174 (R3) | no | Europe PMC: no PMC copy; aacrjournals.org 403 challenge page; OpenAlex closed; CORE no match; Semantic Scholar 429 (queued as FT-206) |
| 16818616 | no | Europe PMC: no PMC copy (only a supplementary figure on figshare); OpenAlex closed; the institutional handle returned 500 |
| 25703206 (R4) | yes | NCBI efetch pmc 200 (PMC4376589, author manuscript); PMC article page 200, 26 figure and table images |
| 25720522 | no | Europe PMC: subscription link only |
| 34015398 | no | Europe PMC: subscription link only |
| 25411445 | no | known: waits for the operator's supply |

**2 of the 8 consumer-bearing records can be read.** The set of step 2 is R1 and R4. Consumer text of R4: `CONSUMER_TEXT_STEP2_R4.md`.

## What this does to the prediction

Strict at least 1 can still be met by two records. The rejecting observation (three read, 0 strict) **cannot** be met: with 0 strict of 2 the result is "not decidable, availability", never a rejection.

## Held files (root checkout, under `files/`)

`fulltext/PMID26041563_Bendinelli2015_PMC.xml`, `fulltext/PMID32799870_RetractionNote_PMC.xml`, `figures/PMID26041563_adv302/`, `supplement/PMID26041563_adv302/`, `fulltext/PMID28045433_Maroni2017_PMC.xml` (the review named by the consumer lines); `fulltext/PMID25703206_Schuchardt2015_PMC.xml`, `figures/PMID25703206_adv302/`.
