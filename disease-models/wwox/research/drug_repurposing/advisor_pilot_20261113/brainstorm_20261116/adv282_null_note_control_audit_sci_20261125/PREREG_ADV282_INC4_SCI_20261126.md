# PREREG, ADV-282 increment 4: null-note audit, queue ranks 25 to 32 (SCI, 2026-11-26)

Hypothesis level; reference genotype class; nothing is medical advice. Written and hashed before any source of these rows was opened. What I knew before: the queue table (`queue_ordered_adv282.tsv`, ranks 25 to 32, notes unchanged on today's cards, checked by script), each row's source label, which source files are held (names only), and the results of increments 1 to 3 (`RESULT_ADV282_SCI_20261125.md`).

## 1. Rows

DA-L01-005 (Cheng 2023, PMID 37897534, held article, figures, supplement), DR-A02-010, DR-A02-006, DR-A02-007 (Gupta 2023, PMID 37319242, held article XML; figures not held), DR-A01-007 (Guiberson 2018, PMID 30266908, held article XML and supplement), DR-B01-002 (Hristodor 2025, PMID 40544182, held article), DR-P9-009 (Wang 2026, PMID 41288262, labelled abstract only; a full-text XML of that PMID is held in `files/fulltext/ketamine_kds_it_20261117/` and is used), DR-E01-002 (PMID 42771346, abstract only, not held: see 4). None rests on the Obeid 2026 article.

## 2. The ONE matching rule (frozen in increment 3, repeated unchanged)

* **CHECK PRESENT** = the held source itself shows **target loss or target engagement of the same manipulation** in the **same preparation** (species, cell type or tissue), at the **same or lower dose and the same or shorter exposure**, in the same paper: for a knockout, knockdown or deletion the loss of the target protein or transcript (or reporter) in that preparation; for a compound, a direct readout of engagement or activity of that compound on its target (dose-response or positive control of the same compound, same preparation); for a variant or clinical exposure, a direct measurement of the variant's functional effect or of the drug's level or target effect in the same patients or system.
* **CHECK PRESENT BUT NOT MATCHED** = such a check exists but differs in dose (higher), time, cell type, species, assay or preparation, or is a citation of another paper.
* **CHECK ABSENT** = no such check in the held bytes (query and date recorded).
* **NOT ASSESSABLE** = source bytes missing or not what their name says.
* An effect of the same manipulation on another endpoint in the same preparation is **not** the class; it goes in a separate column "other effect of the same manipulation: yes/no, locator". An assay control (the readout can move) is neither.
* **Strict** = CHECK ABSENT; **loose** = CHECK ABSENT or NOT MATCHED. Counts for both readers under this rule only.

**One added clause (abstract-level rows only):** when the only source is an abstract, its silence is not absence: the class is NOT ASSESSABLE (abstract) unless the abstract itself reports an engagement readout (then PRESENT or NOT MATCHED). The sentence verdict (MUST CHANGE / ADD / STANDS) is still given against the abstract.

## 3. Prediction and rejecting observation

Calibration: increment 3 under this rule gave strict 1 of 8, loose 3 of 8, blind MUST CHANGE 3 of 8; increments 1 and 2 blind loose 5 of 14, MUST CHANGE 6 of 14. These rows are mostly compound rows in non-neural or non-WWOX systems.

* Assessable rows: 6 to 7 of 8 (DR-E01-002 abstract only).
* **Strict: 1 of the assessable, range 0 to 3. Loose: 3, range 1 to 5.** Rejecting observation: loose 0 or 1 (the engagement checks are mostly present).
* **Blind MUST CHANGE (the yield): 2 of 8, range 0 to 4.** Rejecting observation: 0 (the null-note wording class stops paying in compound rows).

## 4. Method

First reading from the held bytes (article text, the figure images or supplement tables where the class or a quoted number depends on them; sha256 of every file opened in the files-viewed table; negative findings carry date and query). A row labelled abstract-only whose abstract is not held: the PubMed abstract is fetched once through NCBI efetch (plain request, no e-mail address, no key), saved under `files/fulltext/adv282_abstracts_sci_20261126/` with its sha256 and marked abstract-level; a refusal or challenge is a route result. A figure whose number a sentence quotes and which is not held may be fetched once from the PMC open-data bucket on the same terms. Blind reader: `legend-delegate`, model sonnet, effort high (stated in the dispatch, read back from the census), receives the verbatim card sentence built by script and the **whole source** paths, never my class or facts, and answers MUST CHANGE / ADD / STANDS plus its own class under section 2. Recomputed numbers and replicate unit and species beside every value; every table or figure value labelled by sheet or figure, panel and row. Receipts are not written (targeted checks, not completed reads). Consumers named for every changed sentence; card edits belong to IT.
