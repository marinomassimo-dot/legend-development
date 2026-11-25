# ADV-279 pre-registration, part 2: counts, order, completion and predictions (SCI, 2026-11-25, 2026-11-25T16:18Z)

Hypothesis level; reference genotype class; nothing here is medical advice. Part 1 (`PREREG_ADV279_RULE_SCI_20261125.md`, the rule) was committed first. Written before any paper of this batch is opened. Seen so far: the counts, the held file names, the earlier receipts' coverage and the consumer sentences (the thing under test).

## 1. Counts (`count_adv279.py`, output `count_adv279.tsv`; input ranking `ranking_adv279_run.tsv` from the ADV-265 script on today's ledger)

| | studies |
|---|---|
| excluded as already read in ADV-265, 269, 272 or 276 (receipts) | 65 |
| outside those, with consumers and an unread class | 109 |
| readable from held bytes, **old rule** (ADV-265) | **3** |
| readable from held bytes, **wider rule** | **51** |
| route A (identifier path scan) finds | 47 |
| route B (names the article's XML declares) finds | 47 |
| both routes | 43 |
| no held XML, so no route B | 12 |

By class, wider rule (A, B; old rule): supplementary 35 (33, 34; 0); figures 24 (18, 20; 0); discussion 2 (2, 2; 2); tables 1 (1, 1; 1); limitations 0. **The old rule's blind spot is figures and supplements held as separate files**: it found none of either class outside the earlier batches. The ten asked for exist; there is no shortfall. A first run counted a generic `Data_Sheet_1` of another article (PMID 41822170) for PMID 37275776; the script now requires the identifier for generic names.

## 2. Order and exclusions
ADV-265 order: consumer units (route 2), then the number of readable results classes, then discussion, then PMID. Two exclusions, made after seeing the order and before opening any paper:
* **28151481** (c=3): a retracted article (working model integrity exclusion; ADV-249, ADV-253). No consumer should carry its wording.
* **28045433** (c=3): the only held figure image is Figure 3, already opened for ADV-253 (no new reading without padding).

| Increment | PMID | consumers | readable class | figures declared | what the consumer says (the sentence under test) |
|---|---|---|---|---|---|
| 1 | 30362252 (Davids 2019) | 6 | figures | 2 | brain lactate "extremely low" in one WWOX patient with a second candidate variant (card I01 DA-I01-008; HYP-20260709-01; DL-BIO-008) |
| 1 | 33914734 (ASPA C152W) | 5 | supplementary | 7 | blocking the Hsp70/Hsp110 route accumulated insoluble protein with no measurable activity, yeast and U2OS (cards A02, A05; HYP-20260709-08) |
| 1 | 33958783 (Liu 2021) | 4 | supplementary | 9 | WW1-WW2 tandem cooperativity (CLAIM 024; working model domain cooperativity) |
| 1 | 37781246 (Kałuzińska-Kołat 2023) | 4 | figures | 5 | lentiviral WWOX raised proliferation in 1 of 4 glioblastoma lines, phenotype cited from an earlier paper (CLAIM 011); high WWOX expression alone does not identify a state (DL-MECH-054, -053) |
| 1 | 39769031 (Rico-Molina 2024) | 4 | supplementary | 8 | stiripentol inhibits LDHA weakly in vitro (about a tenth racemate, a third enantiomers, at one high level; IC50 a bound) (card E02; DL-REPO-004; HYP-20261026-11) |
| 2 | 42875792 (Rathan-Kumar 2026) | 4 | supplementary | 5 | recovery of a recessive missense protein (HIKESHI V54L) in patient iPSC oligodendrocytes (cards A02, A05) |
| 2 | 28749468 (Janczar 2017) | 3 | supplementary | 8 | GRP78, phospho-IRE-1 and the PERK band shift never quantified; PERK activation unchanged by WWOX (DL-METH-114); restoration direction across systems (DL-THER-115); UPR adaptive against terminal (DL-MECH-023) |
| 2 | 30266908 (Guiberson 2018) | 3 | supplementary | 8 | 4-phenylbutyrate raises variant and wild-type Munc18-1; class-I HDAC comparator unchanged; osmolytes raise (card A01) |
| 2 | 34359949 (Hsu 2021 review) | 3 | figures | 3 | provenance of one link of the WWOX/TIAF1/tau cascade and the two-phospho-state proposal (CLAIM 043, 044) |
| 2 | 37248434 (Taouis 2023) | 3 | figures | 6 | the SDR region carries a measured protein interaction (DL-MECH-115); a nominal SNP association is not functional (DL-MECH-056) |

Reserve, used only if one of the ten proves a stub or not readable: 37275776 (supplementary), then 41948127 (figures).

## 3. What counts as completed, per paper
Every listed class read in the held files: for supplementary, all held supplement text and tables, and every held supplementary figure image looked at; for figures, every main figure opened as an image and looked at (sha256 listed). Otherwise the class stays unread in the receipt and the result says which part is missing. Verbatim locators for each statement that bears on a consumer; printed ratios and totals recomputed; every number carried from a workbook or figure labelled by sheet or figure, panel and row, with species and replicate unit; the five checklist classes (window; unit under n; species, preparation and age; the test behind the p; "all/none/absent") asked of each consumer sentence; variance from all eligible rows, never the called ones. One receipt per paper. A blind delegate (`legend-delegate`, sonnet, effort high) reads every pivotal item. One wording message to IT per increment.
**Strict change** = the consumer sentence must change. **Loose** = strict, or a window, dose, species, unit or evidence level must be added.

## 4. Predictions (fixed now)
* **P1:** strict changes 2 of 10 (range 0 to 4). Lower than ADV-276 (17 of 43): most of these are supplements and figures of papers whose Results were already read.
* **P2:** loose changes 4 of 10 (range 2 to 7).
* **P3, by class:** supplementary-class papers (6): loose 3 (range 1 to 5). Figure-class papers (4): loose 1 (range 0 to 3).
* **P4:** at least one figure, supplementary image or spreadsheet disagrees with the text or legend: 0.6.
* **P5:** no direction reversed: 0.9.
* **P6:** at least one of the ten cannot be completed from held files (a figure or supplement missing): 0.6.
**Rejecting observation:** if none of the ten changes any consumer's wording (loose), the claim that held figure and supplement files still move what the repository says is not supported, and ADV should move the reading effort to another debt.
