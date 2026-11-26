# PREREG, ADV-282 increment 5: null-note audit, queue ranks 33 to 40 (SCI, 2026-11-26)

Hypothesis level; reference genotype class; nothing is medical advice. Written and hashed before any source of these rows was opened. What I knew before: the queue table (ranks 33 to 40, notes unchanged on today's cards), each row's source label, which source files are held (names only), and increments 1 to 3 plus my own frozen first reading of increment 4 (strict 2, loose 5 of 8, 3 sentences MUST CHANGE; its blind reader was still running).

## 1. Rows

DR-E01-003 (PMID 42179084, abstract), DR-W2-004 (Alekseeva 2026, PMID 42652189, held, complete read receipt), DR-H02-008 (PMID 24321005, PMC page held), DR-H02-023 (PMIDs 1940119, 2767014, abstracts), DR-H02-024 (PMID 2757909, abstract), DR-H02-036 (PMIDs 31349008, 35980256, abstracts), DR-L01-003 (Sheeni 2026, PMID 42939870), DR-H02-030 (PMID 19054414, abstract). None rests on the Obeid 2026 article.

## 2. Matching rule

Section 2 of `PREREG_ADV282_INC4_SCI_20261126.md`, unchanged, including the abstract-level clause. Sentence verdicts: MUST CHANGE = a statement of the note is false, contradicted by, or not supported by the source (including a wrong object of an attribution); ADD = true but a qualification a reader needs is missing; STANDS.

## 3. Prediction and rejecting observation

Six of the eight rows are abstract-level or exposure rows, so many classes will be NOT ASSESSABLE.

* Assessable rows (class other than NOT ASSESSABLE): 3, range 2 to 5.
* Strict: 1 of the assessable, range 0 to 3. Loose: 2, range 1 to 4.
* **MUST CHANGE (first reading and blind separately): 1 of 8, range 0 to 3.** Rejecting observation: 0 by the blind reader (abstract-level null notes are faithful to their abstracts).

## 4. Method

As increment 4. Abstract-only sources not already held are fetched once through NCBI efetch (no e-mail, no key) into `files/fulltext/adv282_abstracts_sci_20261126/` with sha256.

## Addendum before any source was opened (2026-11-26)

Sheeni 2026 (PMID 42939870, PMC13701765) is not held in `files/` (name and content search, 2026-11-26). One plain Europe PMC `fullTextXML` request is allowed for it (no e-mail, no key); a refusal, challenge or non-XML reply makes the row NOT ASSESSABLE and is recorded as a route result.
