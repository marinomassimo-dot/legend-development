# PREREG, ADV-282 increment 3: null-note audit, queue ranks 17 to 24 (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing is medical advice. Written and hashed before any source of these rows was opened. What I knew before: the queue table (`queue_ordered_adv282.tsv`, ranks 17 to 24), each row's card note and source label, which source files are held (names only), and the results of increments 1 and 2 (ADV-282 RESULT).

## 1. Rows

Ranks 17 to 24, none of which has the Obeid 2026 article as a source (checked from the `source` column; the classifier stop stands and nothing from that article is opened): DA-I01-002 (GSE126075, PMID 31543760), DA-K01-005 and DA-K01-006 and DA-I01-004 (Baryla 2022, PMID 35328751), DR-W2-002 and DR-W2-003 (Karnstedt 2026, PMID 41489401), DR-W2-007 (Teplyshova 2024, PMID 39507621), DR-K01-006 (four PMIDs: 24889205 and 36655171 and 42276303 not held, 34021541 held as an ADV-272 fetch). A row whose every source is missing, or in which every named source is missing, is NOT ASSESSABLE; a row with several sources is assessed per held source. No acquisition, no spend, no contact.

## 2. The ONE matching rule (frozen; ADV's instruction after ADV-282)

The two readers diverged in ADV-282 over whether an effect of the same manipulation on another endpoint counts as the check. Under this rule it does not:

* **CHECK PRESENT** = the held source itself shows **target loss or target engagement of the same manipulation** in the **same preparation** (species, cell type or tissue), at the **same or lower dose and the same or shorter exposure**, in the same paper: for a knockout, knockdown or deletion the loss of the target protein or transcript (or reporter) in that preparation; for a compound, a direct readout of engagement or activity of that compound on its target (dose-response or positive control of the same compound, same preparation); for a variant or clinical exposure, a direct measurement of the variant's functional effect or of the drug's level or target effect in the same patients or system.
* **CHECK PRESENT BUT NOT MATCHED** = such a check exists but differs in dose (higher), time, cell type, species, assay or preparation, or is a citation of another paper.
* **CHECK ABSENT** = no such check in the held bytes (query and date recorded).
* **NOT ASSESSABLE** = source bytes missing or not what their name says.
* An effect of the same manipulation on another endpoint (phenotype, transcript, a different protein) in the same preparation is **not** the class; it is recorded in a separate column "other effect of the same manipulation: yes/no, locator" and never changes the class. An assay control (the readout can move) is neither.
* **Strict** = CHECK ABSENT; **loose** = CHECK ABSENT or NOT MATCHED. Counts for the first reader and the blind reader are given **under this rule only**, with the "other effect" column beside, never merged.

## 3. Prediction and rejecting observation

Calibration: under the stricter reading the blind readers found loose 4 of 9 (ADV-281, of the ten) and 5 of 14 (ADV-282); strict 1 to 2 of 9 and 1 of 14. These eight rows are mostly clinical, drug-in-other-disease or non-neural and carry no engagement readout by construction, so the rates should be higher.

* Rows assessable: 6 to 8 of 8 (DR-K01-006 NOT ASSESSABLE or one held source only).
* **Strict (ABSENT): 3 of the assessable, range 1 to 5. Loose (ABSENT or NOT MATCHED): 5 of the assessable, range 3 to 7.** Rejecting observation: loose 2 of the assessable or fewer (the checks are mostly present, as in the deposit rows).
* Blind reader MUST CHANGE (the yield, as ADV set it): 2 of 8, range 0 to 4. "MUST CHANGE or ADD" is reported but is not the yield.
* A row that is a repository table or a label (not a measurement) is NOT ASSESSABLE by construction; none is expected here.

## 4. Method and blind packet

First reading from the held bytes (XML extraction for article text, figure images or supplement tables where the class depends on them; hash of every rendered PNG and source file in the files-viewed table; negative findings carry date and query). Blind reader: legend-delegate, sonnet, effort high (stated, read back from the census), receives the verbatim card sentence built by script and the **whole source** (the full article text, every panel of any figure whose number the sentence quotes, whole supplement tables, not only the quoted row: HE's rule after its bexarotene error), never my class or facts, and answers MUST CHANGE / ADD / STANDS plus its own class under the rule of section 2. Recomputed numbers and replicate unit and species beside every value. Receipts are not written. Consumers named per changed sentence.
