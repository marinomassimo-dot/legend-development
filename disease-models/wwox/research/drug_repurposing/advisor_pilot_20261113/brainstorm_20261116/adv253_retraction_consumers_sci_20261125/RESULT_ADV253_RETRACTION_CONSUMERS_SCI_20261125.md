# ADV-253 result: who depends on retracted material behind review PMID 28045433 (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; nothing here is medical advice. Open copies only; no spend, no contact, no delegate. One reader. Pre-registration: `PREREG_ADV253_SCI_20261125.md` (frozen before the review, the retracted article, the notice or any image was opened). No registry, card or claim is edited here.

## 1. Answer

* **No card, claim, portfolio row or hypothesis record depends on the review or on the retracted articles** (two routes; E1 met). The canonical text that names them does so to exclude them.
* **Two analysis rows lean on it:** the decitabine row A10 of the expression-boost census (depends; it states no direction) and the autophagy census, where the review is one of the two papers on the "WWOX raises autophagy" side (mixed). Neither has a canonical consumer.
* **The review's dependency is wider than recorded:** it cites **five** retracted articles, not one. Two of those retractions (August and September 2026) are not in the Retraction Watch snapshot of 2026-10-21, and one of them (PMID 19357348, a WWOX paper) is not flagged in `batch_queue.md`.
* **"Reuses its data" holds for one value, not for the figure.** Review Fig 3B cites the retracted paper's protocol and gives Wwox under decitabine as 0.2x, the value of retracted Fig 6a. The blot images, the Beclin-1 and p62 lanes and the cell-line comparison of Fig 3A do not appear in any figure of PMID 28151481.

## 2. The sources, quoted

**Retraction notice** (PMID 35680840, retracting PMID 28151481): "The Editors are retracting this article because of concerns with a number of figures. An investigation by the University of Milan confirmed that:" followed by a list of vinculin loading-control bands reused between panels and between publications, then "The Editors therefore no longer have confidence in the data." and "Maria Alfonsina Desiderio disagrees with this retraction." The notice names panels "Fig. 3b" and "3d" for vinculin; in the open XML and figure files of the article, Figure 3 is immunohistochemistry without a loading control. The mismatch is recorded, not interpreted.

**Review Figure 3 legend** (PMID 28045433): "Wwox protein levels in breast carcinoma cell lines, and role of decitabine and Wwox in the expression of autophagy players. [...] (B) the 1833 cells were exposed to decitabine or the vehicle alone for 30 days; WWOX expression vector (e.v.) was transfected for 24 or 48 h [64]." Reference 64 is PMID 28151481.

**Review text:** "As shown in Figure 3B, the transfection of WWOX expression vector increased strongly Beclin-1 and less p62 protein levels in 1833 cells (quantification of the data is included in the graphic)." Its one other citation of reference 64: "Oppositely, hepatocyte growth factor (HGF)/Met receptor, one of the principal bone-metastatic regulatory axis, is downregulated [64]."

## 3. Figure comparison

Open routes: PMC open-data bucket (review Fig 3 image, sha256 `b0e06977880def00d3cf8deb67655cb66a2a7e97a78097dd4b5c1e216fdfb86a`); Europe PMC `supplementaryFiles` for PMC5386451 (all eight main figures and the supplement, zip sha256 `ac17fa01680dc9bec5b9f5ad2ac023b8b60786c67510fe76b7f6cca5586538d4`). A direct Europe PMC figure URL returned 403 and was not retried. Copies: `files/fulltext/adv253_sci_20261125/` (root checkout, ignored by git).

| Review Fig 3 content | In PMID 28151481? |
|---|---|
| 3A: Wwox blot, 1833 / MDA-MB231 / MCF7 | not found |
| 3B: Wwox, vehicle and decitabine (1.1x, 0.2x) | Fig 6a is a bar chart with Wwox about 0.2 under 30 days of decitabine in 1833 cells: **same value, no blot shown there** |
| 3B: Wwox after the expression vector (45x, 41x) | not found (Fig 6c gives 3.2x cytosol, 2.8x nuclei, a different preparation) |
| 3B: Beclin-1 and p62 blots and graph | not found; the article's text and supplement text contain neither word |

These are visual observations by one reader of the published files. They say nothing about conduct, and they do not show where the review's unpublished-elsewhere panels come from.

## 4. The review's retracted references

Reference list screened with `dependency_integrity.py screen` (snapshot 2026-10-21) and, as a second route, all 79 references with a PMID queried in Europe PMC.

| Ref | PMID | Notice | In the 10-21 snapshot | What the review hangs on it |
|---|---|---|---|---|
| 41 | 25447306 | 32746981 (2020) | yes | several mechanism sentences: ectopic WWOX stabilising HIF-1α in 1833 cells, HDM2 sequestration, E-cadherin induction |
| 42 | 19357348 | 42583763 (2026-08) | **no** | not traced sentence by sentence |
| 58 | 26041563 | 32799870 (2020) | yes | HGF / TGFβ1 / Twist programme |
| 64 | 28151481 | 35680840 (2022) | yes | Fig 3B protocol; HGF/Met down-regulation |
| 78 | 15240510 | 42713750 (2026-09) | **no** | not traced sentence by sentence |

PubMed marks 19357348, 15240510, 27023526 and 16840440 as retracted publications (second route). A Europe PMC author search returns **11 retracted publications** by the review's senior author; the six not cited by the review are 29337876, 27023526, 24434513, 23660387, 16840440 and 9683527. Same-group papers without a notice (23566416, 22717556, 27187355, 31121879) are not impugned by this; none is cited by a claim, the working model, a card or a ledger lead.

## 5. Consumers

Full table: `consumers_adv253.tsv` (14 rows). Route 1: `git grep` for the identifiers. Route 2: `scan_records_adv253.py` (959 files, 16,178 units; 64 hit, 30 by identifier; output `route2_units.tsv`). The value-only hits (decitabine, HIF-1α) were opened: they rest on other sources (Stewart 2014; the Wwox-loss HIF-1α line), not on this cluster.

Dispositions: depends 1, mixed 1, describes the retraction 8, no statement 4.

**Working model, line 81.** "The WWOX/HIF1α axis stands only on the independent sources already registered" and "No baseline claim depended on the invalidated line" are consistent with what was found: no claim cites this cluster. The part "the review reuses its data and dependencies" should be narrowed.

## 6. Wording for IT (not applied)

1. **DL-MECH-025, working model line 81, `disease_model.md` line 33, CORPUS-STUB-061, LIT-0085/0401:** "Review PMID 28045433 cites five retracted articles of its own group (25447306, 19357348, 26041563, 28151481, 15240510). Its Fig 3B cites the protocol of retracted PMID 28151481 and gives the same decitabine value for Wwox (0.2x); its blot images, Beclin-1 and p62 were not found in that article. Not usable as support for any of it." Check the date field "retracted in 2022": correct for 28151481 only.
2. **Autophagy census (C2), dated line:** "28045433 is not counted: the Beclin-1 observation exists only as a panel in a review whose group has 11 retractions. Without it this census holds one paper on the up side (36621327, abstract) and two on the down side; the later sign audit and the full read of 33300063 govern the direction statement."
3. **Expression-boost census row A10:** "sources retracted or restating a retracted article; no usable observation."
4. **`batch_queue` / corpus:** mark PMID 19357348 retracted (notice 42583763).
5. **CC-20261019-SCIENTIST-C-H4-01:** PMID 25447306 is retracted; it should not be requested as a manual PDF.

## 7. Expectations scored

* E1 (no card or claim depends): **met.**
* E2 (Fig 3 restates retracted-article data at least in part): **met narrowly**, one value; the images and the autophagy lanes were not found there.
* E3 (at most five rows "depends" or "mixed"): **met** (two).

## 8. Deviations and limits

* The pre-registration defined retracted material as PMID 28151481 only. The other four retracted references and the group's retractions were found afterwards and added to the identifier list.
* The HIF-1α value patterns were added to route 2 after the review's sentences had been read.
* The record scan covers registries, research notes, commit candidates, analysis, meta, cards and ranking tables; it skips census files, receipts, audits, evaluations, assignment and checkpoint files, history files and generated join outputs.
* The two retracted references 42 and 78 were not traced to individual sentences.
* The review was not re-read in full here (it already has receipt FTR-20261124-28045433-01 with figures at caption depth); this pass opened Figure 3, the sentences citing retracted references and the reference list. No new receipt is recorded.
* Authors were not contacted. Nothing here is a statement about any person's conduct.

## 9. New question

Which other WWOX-corpus records have gained a retraction or expression of concern that neither the snapshot nor the receipt-based sweep reaches? `epmc_notice_sweep.py` covers only papers with a receipt; the 700-odd catalogued PMIDs could be queried in Europe PMC in about 20 spaced requests. Rejecting observation: no unflagged notice beyond 19357348. Consumers: `batch_queue.md`, claim support, request lists.
