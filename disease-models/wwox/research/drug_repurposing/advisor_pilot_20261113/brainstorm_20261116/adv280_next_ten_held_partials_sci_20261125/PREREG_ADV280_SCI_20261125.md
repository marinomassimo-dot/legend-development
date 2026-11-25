# ADV-280 pre-registration: the next ten readable held records (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Actor `orchestrator` (SCI, `claude-sonnet-5-5`, effort high). Brief: `assignments/ADV-280.md`. Held bytes only: no acquisition, no spend, no contact, no e-mail address to any service. Not the frozen RP-045 prediction; the sealed ADV-174 and ADV-175 folders are excluded from every scan. Written before any of the ten articles is opened. Seen so far: counts, held file names and whether each held file opens (file type, image size, PDF page count, archive member names), earlier receipts' coverage, and the repository sentences that cite each record (the thing under test).

## 1. Rule

The ADV-279 rule (`PREREG_ADV279_RULE_SCI_20261125.md`, wider rule, two routes) re-run on today's ledger, with two changes: ADV-279 receipts join the excluded set, and **defective held files are removed from the inventory first** (`content_check_adv280.py`, output `defective_held_files_adv280.tsv`: 9,921 held files checked, 60 defective: empty, an HTML or error page under a binary name, wrong magic bytes, broken archive). A defect in the file is not a read. Counts by `count_adv280.py`, output `count_adv280.tsv`.

| | studies |
|---|---|
| excluded as already read in ADV-265, 269, 272, 276 or 279 (receipts) | 75 |
| outside those, with consumers and an unread class | 99 |
| readable from held bytes, old rule | 3 |
| readable from held bytes, wider rule | 40 (route A 37, route B 37, both 34) |
| minus the standing ADV-279 exclusions still counted | 36 |

The brief's 41 is 51 minus the ten read; it still contained the five left out by amendment or order (28151481 retracted; 28045433 and 41948127 only held figure already read; 30362252 error pages; 33958783 false consumers). The remainder is 36.

## 2. Excluded for a defective held file

| record | defective held file | effect |
|---|---|---|
| 30362252 | both figure files and the supplement PDF are HTML pages, the supplement archive does not open | not readable; excluded |
| 19366691 | the held PDF is an HTML page | no readable class left; excluded |
| 29310447 | the held PDF is an HTML page | no readable class left; excluded |

No other ranked record has a defective file under its identifiers. All held files of the ten below open (images decode, PDFs report a page count, archives pass their CRC test, XML parses). A file that opens can still be the wrong article; that is checked when it is read.

## 3. Order

ADV-265 order: consumer units, then the number of readable results classes, then discussion, then identifier. The first ten after the exclusions:

| inc. | record | consumers | readable class | sentence under test |
|---|---|---|---|---|
| 1 | 36926521 (Colin 2023) | 2 | figures, supplementary | patient-fibroblast western read as "WWOX loss": strongly reduced band with a faint residual, one control, no quantification (CLAIM 033); exon 5 skipping amplicon, not quantified (DL-BIO-002) |
| 1 | 37804316 (AFG3L2 ISR) | 2 | figures, supplementary | HRI or DELE1 loss worsens and a GADD34-targeted compound improves patient-cell and mouse endpoints, survival gain about 6 to 7 days; kinase evidence is siRNA in fibroblasts, GCN2 and PERK not tested (card E01) |
| 1 | 41570991 (Bouchez 2026) | 2 | figures, supplementary | stiripentol non-competitive on LDH; effect on NADH-oxidising enzymes (card E02, DR-E02-005, -006) |
| 1 | 41706892 (PNAS 2026) | 2 | figures, supplementary | group I mGluR agonism raises phospho-eIF2 alpha and ATF4 protein within minutes without Atf4 mRNA change in normal mouse hippocampus (card E01) |
| 1 | 10.1101/2025.05.01.651195 (preprint) | 2 | supplementary | the preprint's statuses in CLAIM 025 and DL-META-088; the published version (PMID 42909904) was read completely, so a change must concern what is attributed to the preprint |
| 2 | 35883580 (Liu 2022 review) | 2 | figures | review model pY33 to pS14: no same-system kinetics, no mutants; videos qualitative (DL-MECH-057, -058). The ledger entry says the eight figures were read; the receipt says captions only |
| 2 | 38378758 (Clausen 2024) | 2 | supplementary | flow shift of a Parkin library; lysosome-inhibitor control did nothing; 29 degree effect; half of pathogenic variants wild-type abundant (card A02 DR-A02-002; R1 PA-3, PB-1, PB-2, premise 0) |
| 2 | 38443647 (Bacq 2024 review) | 2 | figures | LDH-inhibiting concentrations at or above total plasma and far above estimated free tissue level; brain to plasma near 1; liver to plasma about 35 once in rat; LDH ranked last (card E02 DR-E02-007) |
| 2 | 38731820 (Poliquin 2024) | 2 | supplementary | HRD1 and an antiseizure drug in a Gabrg2 knock-in: seizure endpoint six animals, one-tailed, drug did not act through HRD1 as shown (card A04, R1) |
| 2 | 38740822 (Gronbaek-Thygesen 2024) | 2 | supplementary | ASPA map: E1 and proteasome inhibition raise the low-abundance population, chloroquine does not; 50 of 61 pathogenic variants below 0.5 abundance; substrate no effect (card A02, R1) |

Reserve, in the same order, used only if one of the ten proves unreadable: 39216838, then 39923817.

## 4. What counts as completed, per record

As ADV-279 part 2 section 3: for supplementary, all held supplement text and tables and every held supplementary figure image looked at (audio-visual files are listed and said to be unwatched unless watched); for figures, every main figure opened as an image. Otherwise the class stays unread and the result says what is missing. For each rendered page the sha256 of the PNG and of its source file; for each held image the sha256 of the file. Values carried from a workbook or figure are labelled by sheet or figure, panel and row, with species and replicate unit. A workbook is read sheet by sheet; a data sheet too large to read row by row is declared as parsed and sampled, with what was computed. One receipt per record. A blind delegate (`legend-delegate`, sonnet, effort high) reads every pivotal item. One wording message to IT per increment. **Strict change** = the repository sentence must change. **Loose** = strict, or a window, dose, species, unit or evidence level must be added.

## 5. Predictions (fixed now), recalibrated on the last two batches

The last two batches gave strict 4 of 10 (ADV-276 step 2 batch 2) and 5 of 10 (ADV-279); loose 6 of 10 and 9 of 10. This batch has no text class, and its card sentences are shorter than ADV-279's, which lowers the chance that a supplement contradicts them; several of these records were read recently with figures opened as images.

* **P1:** strict changes 3 of 10 (range 1 to 6).
* **P2:** loose changes 7 of 10 (range 4 to 9).
* **P3, by class.** Supplementary-only records (10.1101, 38378758, 38731820, 38740822): strict 1 (0 to 3), loose 3 (1 to 4). Figures-only records (35883580, 38443647): strict 0 (0 to 1), loose 1 (0 to 2). Records with both (36926521, 37804316, 41570991, 41706892): strict 2 (0 to 3), loose 3 (1 to 4).
* **P4:** at least one supplement, sheet or panel disagrees with the paper's own text or legend: 0.8.
* **P5:** no direction reversed: 0.9.
* **P6:** at least one of the ten cannot be completed from held files: 0.4.
* **Rejecting observation (ADV):** strict below 2 of 10 would mean the wider-rule yield has fallen and ADV moves to another debt.
