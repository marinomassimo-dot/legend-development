# ADV-292 pre-registration: ten held partial records (SCI, window 9bb60ab5, frozen 2026-11-26T00:33Z)

Hypothesis level; reference genotype class only; nothing here is medical advice. Actor `orchestrator` (SCI, `claude-sonnet-5-5`, effort high). Brief: `assignments/ADV-292.md` with ADV's correction note and decision of 2026-11-26. Held bytes only: no acquisition, no spend, no contact, no e-mail address to any service. The frozen RP-045 prediction and the sealed ADV-174 and ADV-175 material are not touched. The Obeid 2026 article is not among the records and stays unopened. The reading is done by the successor window; this window opens none of the ten.

## 1. What had been seen when this was frozen

Counts from the receipt ledger; held file names and types; member names and CRC of the two supplement zips; receipts' coverage state for 42807679; the identifiers of the consumer units. No article text, figure, table or supplement of the ten was opened for this unit, and the consumer sentences were not read for it.

## 2. A wrong first list, and the correction

SCI's first proposal (and the registered row) named 30362252, 33958783, 28151481 and 42807679 among the ten. It used the ADV-265 matching and did not apply the ADV-279/280 exclusions. 30362252: the held figure and supplement files are HTML error pages. 33958783: false consumers (ADV-279 amendment 1). 28151481: retracted. 42807679: 5 of 7 declared figures held. The threshold ADV had stated for preferring this batch (more than ten partials with two or more consumers) is **not** met: after the corrections 7 eligible readable records have 2 consumer units and none has more; one of the seven (40301740) holds one main figure of seven; for the card records "2 units" is one card and its packet. ADV decided to keep the batch with the corrected ten.

Count commands, all read-only, run on this ledger: `rank_held_partials_adv265.py`, `containment_adv265.py`, `content_check_adv280.py`, `count_adv280.py` (excludes receipts of ADV-265, 269, 272, 276, 279), then `framework/scripts/consumer_count.py` on the readable keys. Standing exclusions: 28151481, 28045433, 41948127, 33958783.

## 3. The ten, in reading order

| inc. | record | consumer units | class to read | held files (under `files/` in the root checkout) |
|---|---|---|---|---|
| 1 | 39216838 | card A03 (card and packet) | supplementary | `supplement/PMID39216838_r2/` (docx, pdf, three xlsx, article pdf) |
| 1 | 40485335 | card A01 (card and packet) | supplementary | `figures/PMID40485335/` (four supplement TIFF) |
| 1 | 41178115 | card A04 (card and packet) | supplementary | `supplement/PMID41178115/` (SI pdf, 18 pages) |
| 1 | 42268630 | card A01 (card and packet) | supplementary | `supplement/PMID42268630/` (xlsx) |
| 1 | 41664646 | investigations.tsv:3; investigations_it20.tsv INV-06 | figures | `fulltext/PMID41664646_Ahuja2026_imec_VoR.pdf` (render the pages) |
| 2 | 39923817 | investigations.tsv:7; investigations_it20.tsv INV-16 | tables only (figures, supplementary and limitations stay unread) | `fulltext/PMID39923817_ADV272_PMC13078857_epmc_20261125.xml` |
| 2 | 37946251 | CLAIM 033 | supplementary | `supplements/PMID37946251/` (xlsx, `s.zip`) |
| 2 | 40858643 | CLAIM 033 | supplementary | `supplements/PMID40858643/` (xlsx, `s.zip`) |
| 2 | 26419537 | DL-MECH-170 | figures, supplementary | `figures/PMID26419537_r2/`, `supplement/PMID26419537_r2/` |
| 2 | 31781019 | DL-MECH-170 | figures, supplementary | `figures/PMID31781019_r2/` |

Reserve, used only if one of the ten proves unreadable: 36282524, then 42807679 (partial: figures 3 to 7 only).

Order inside the choice: the six complete-class records with two units; then the one-unit records that a CLAIM cites; then ADV-265 order. This ordering is SCI's choice, not the ADV-265 rule alone.

## 4. What counts as completed, per record

As ADV-280 section 4. All held supplement text, tables and supplementary figure images looked at (audio-visual files listed and declared unwatched unless watched); every main figure opened as an image for the figures class. A class that cannot be completed from held files stays unread and the result says what is missing. Before saying "not held", list `files/supplement*`, `files/figures` and `files/fulltext` for the identifier. sha256 for each image or rendered page. Values carried from a workbook or figure are labelled by sheet or figure, panel and row, with species and replicate unit; folds and ranges are computed over all source rows. One receipt per record. For CLAIM 033 papers, report at variant or genotype-class level and copy no patient-level row into the repository. Apply the ADV-276 pre-read checklist and the ADV-287 wording rule to SCI's own sentences. A blind delegate (`legend-delegate`, sonnet, effort high stated in the dispatch) reads every pivotal item.

## 5. Matching rule (one rule)

A record counts as **one strict change** only if both hold for at least one consumer sentence that names or rests on it: (a) the reader verifies on a held file of the class read that the sentence as written is false or unsupported; (b) a blind sentence-level reader, given the repository sentence verbatim and the held sources and none of the reader's verdicts, returns MUST CHANGE for that sentence. If only one of (a) and (b) holds, the record does not count as strict and is listed separately with both readings. **Loose** = strict, or a window, dose, species, unit or evidence level must be added. Figure-class and supplement-class yields are reported separately.

## 6. Predictions and stopping

* **P1 (ADV, fixed):** strict changes 3 of 10, range 1 to 5.
* **Rejecting observation (ADV):** at most 1 of 10 strict: held partials at this consumer level are exhausted, and the debt moves elsewhere.
* **Increment stop (ADV):** if the first five give 0 strict changes, stop and tell ADV before the second five.
* No other prediction is registered here.
