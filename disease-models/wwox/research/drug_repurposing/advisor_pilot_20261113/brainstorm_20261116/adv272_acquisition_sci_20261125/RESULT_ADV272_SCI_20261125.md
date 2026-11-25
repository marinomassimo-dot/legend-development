# ADV-272 result: acquisition of the not-held partials with consumers (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. Pre-registration `PREREG_ADV272_SCI_20261125.md` (digest and time in the companion files, 09:01:18Z), written before the 421 were listed and before any request. Permitted routes only: Europe PMC REST and fullTextXML, the PMC article page, doi.org and a publisher page by plain requests from a declared generic client (no browser identity, no e-mail address, no contact-address resolver, no author contact), one request at a time, at least 2 s apart, no bursts; every challenge page, 403, 500, 502, 503 and timeout is recorded as a route result and was never bypassed. No spend. No delegate. PMIDs appear in this research file only.

## 1. Answer first

* Population confirmed: 421 not-held partials (HE's `held_studies.py`; it now prints 1,085 latest partials, ADV had 1,091). **Only 55 of the 421 feed any consumer unit**; 366 feed none.
* **24 of the top 25 were acquired and verified** (20 as Europe PMC full-text XML, 4 as the PMC article page); the 25th (rank 1, 40875931) returned a challenge page. `held_studies.py` now counts 688 held and 397 not held (from 664 and 421).
* Ranked by consumer units, the programme leans on papers it holds only in part most through **discovery-ledger leads (23 units), research-portfolio rows (21), cards (24 files, about 12 cards: a card and its packet file each count) and ranking rows (14)**; claims (4 units, two papers) and hypothesis records (1) least.
* One acquired paper (rank 2, 34021541) was read: Tables 1 and 2 sum correctly, but two tables disagree on a comparable arm, the stated inclusion rule contradicts the tables, and a number in the Methods was never filled in (section 5).
* ADV's three IT targets (16818616, 25720522, 18460020) were not obtained: Europe PMC flags all three not open access and not in PMC; two doi.org requests returned a 403 challenge page and the Springer page delivered the abstract only. They are on the new operator list.

## 2. Predictions scored (PREREG)

| | Prediction | Observed | Scored |
|---|---|---|---|
| P1 | 9 of the top 25 open access (range 5 to 14) | 20 of 25 `isOpenAccess = Y` (24 answered at first pass or after one slow retry for the 11 that returned 502, 503 or a timeout; the 25th answered on a second request); 5 N | **rejected** (too low). ADV noted it was trending that way after the first 14 answered |
| P2 | 7 acquired and verified (3 to 11), at most the number flagged open | **24** acquired (20 flagged open, plus 4 flagged not open that are in PMC and were obtained as the PMC article page) | **rejected** on both clauses |
| P3 | at least three non-open papers return a route result on one plain request | all 5 did: Europe PMC fullTextXML timeout (20810895) and HTTP 500 (23141539, 24321005, 40994429); doi.org 403 challenge page (40875931). Four were then fetched as the PMC article page, one request each, 10 s apart | met |
| P4 | at least one acquired paper holds a class its latest receipt lists as unread | yes (for example 34021541: supplementary, figures; all of the top 25 are partials by construction) | met |
| P5 | at least one acquired artefact fails verification | none failed: each carries its own PMID, the paper's own title agrees (two matcher misses, 36530994 and 36601084, were checked by hand: markup and an empty flag title), none is a challenge page | **rejected** |

Calibration: my guess of the open-access share was low by a factor of two (the unheld partials with consumers are mostly recent or PMC-deposited papers), and I did not foresee that a paper Europe PMC flags not open can still be on PMC as a readable article page.

## 3. The ranking and the lean

Rule as frozen: distinct consumer units found by route 2 (unit text, by PMID, PAPER id and DOI), ties by route 1 (files naming the id), then PMID. The 12 route-disagreements are listed by the script. Top five: 40875931 (5 units: card B01, CLAIM 001, 013, 033), 34021541 (4: card K01, INV-7, INV-16), 23435430 (3 lead rows), 41066510 (3: RP-012, RP-036, RP-039), 20810895 (2: card F03); then a flat tail of 2s.

Unit classes over the 55 papers with any consumer (route 2): cards 24 files, leads 23, portfolio 21, ranking rows 14, claims 4, hypotheses 1; papers per class: portfolio 19, leads 17, cards 12, ranking 7, claims 2, hypotheses 1. Where a lead sentence can sit on a paper nobody has opened, that is the lean; the programme's claims rest almost entirely on held papers. Files: `ranking_adv272.tsv`, `rank_not_held_adv272.py`.

## 4. Acquisition record (`acquisition_table_adv272.tsv`)

Stored under `files/fulltext/PMID<pmid>_ADV272_<PMCID>_epmc_20261125.xml` (or `_pmcpage_20261125.html`) in the root checkout (gitignored), SHA-256, section/figure/table counts and the PMID found in the artefact are in the table. Not acquired in the top 25: 40875931 only. Open-access papers of ranks 26 to 55 (of 30: 20 flagged Y, 5 N, 5 route results) were flagged, not acquired (outside the frozen scope); they are listed in section B of the operator list for the next round. Note on provenance: Europe PMC's own `fullTextUrlList` names an Unpaywall link for 16818616 (a supplementary figure on figshare, HTTP 202, empty body); no e-mail address went to any service.

HE's report that `PMID24932569/NIHMS618643-supplement-01.xls` is a saved reCAPTCHA page was the verification precedent: every artefact above was opened and carries the paper's own PMID.

## 5. One paper read: 34021541 (rank 2; card K01, INV-7, INV-16)

Source: Europe PMC fullTextXML (PMC8202868), sha256 `27e14928f361225fa0b7f62bf8b9e61f56706377e16e7e4327f3afe09da05d92`; miR-485 acting on HDAC5, HIF1α and PFKFB3 in a lithium-pilocarpine model and a low-magnesium neuron model. Read: abstract, Results 1 to 5, Tables 1 and 2, Methods on the mouse model, seizure scoring and statistics, the limitations paragraph; figures captions only; supplementary figures not held. No WWOX, SLC2A1 or class IIa tool compound appears in the text (searches by two routes: text and tables).

* **Tables 1 and 2 (Racine grade counts, n = 10 per arm):** every row sums to 10. Table 1: control 10 at grade 0; epilepsy 1 (III), 2 (IV), 7 (V); agomir-NC 2, 2, 6; miR-485 agomir **6 at grade 0**, 3 at I, 1 at II. Table 2: agomir-NC + oe-NC 1, 1, 8; **miR-485 agomir + oe-NC 6 at I, 4 at II, none at 0**; plus oe-HDAC5 3, 2, 5; plus oe-HIF1α 2, 2, 6; plus oe-PFKFB3 1, 1, 8 (III, IV, V).
* **Irregularities (printed, not interpreted):** (1) the miR-485 agomir arm (with empty vector in Table 2) is 6 of 10 seizure-free in Table 1 and 0 of 10 seizure-free in Table 2; the text describes it as "grade IV-V down to I-II". (2) The Methods say mice with grade IV or V were used in subsequent experiments, yet the epilepsy arms of Tables 1 and 2 hold ten grade III animals (1, 2, 1, 3, 2, 1). (3) The Methods read "X of 90 mice died during status epilepticus": the number was never filled in, and all nine arms are n = 10 (90 in all). (4) The abstract calls the in-vivo model a rat model; the Methods use male ICR mice. (5) Table 2 carries the title of Table 1. (6) No test is printed for the ordinal grade tables; cell experiments "repeated three times", the unit (wells or independent cultures) is not stated; mouse panels say n = 10.
* **What the paper supports (hypothesis level; mouse; one group):** lowering HDAC5 or HIF1α through miR-485 reduced seizure grade, apoptosis and oxidative and inflammatory markers in this model, and overexpressing HIF1α in the agomir arm returned seizure grades to IV and V in 8 of 10 (Table 2). It is a precedent for the K01 HIF-axis direction only and says nothing about WWOX.
* **Wording for IT (not applied):** K01 packet DR-K01-006 lists 34021541 at abstract level (`reading_depth: abstract_only`, direction UNKNOWN): add "read at partial full text 2026-11-25 (FTR-20261125-34021541-01): lithium-pilocarpine ICR mice, n 10 per arm, Racine counts; miR-485 agomir lowers grade and HIF1α overexpression reverses it; two tables disagree on the agomir arm, inclusion rule and tables conflict, mortality never reported; no WWOX datum". Whether the direction changes from UNKNOWN is IT's and ADV's decision. INV-16 (HDAC5 to SLC2A1): this paper does not touch SLC2A1.
* Receipt: `FTR-20261125-34021541-01`, `partial_fulltext_read` (no section beyond those read is claimed).

## 6. Not acquired and the operator list

New file `files/operator_inputs/PDF_REQUEST_LIST_ADV272_20261125.md` (root checkout, gitignored, next to the ADV-223 list, which is not edited): section A (one unacquired top-25 paper and the three ADV-273 targets, with route results; for 18460020 the specific need is Supplementary Fig S1B) and section B (ranks 26 to 55 with open-access flag and consumer classes: 20 open, 5 not, 5 route results). Journal-site attempt (ADV's pattern): doi.org for 40875931, 16818616 and 18460020 returned the same challenge page; the Springer page for 25720522 returned the abstract page; none bypassed.

## 7. Limits

Figure images and supplements of the 24 acquired papers are unopened (only 34021541 was read, in part); the 12 route disagreements of the ranking were not hand-resolved; the OA flag is Europe PMC's, a second source was not queried; unit counts include a card and its packet file as two; ranks 26 to 55 were not acquired; the Europe PMC fullTextXML route answered 502, 503, 500 and timeouts on a share of requests (service load; route results, not retried in a burst), so a rerun may differ.

## 8. DREAM line

Changed: the programme's lean on unread sources is concentrated in leads, portfolio rows and cards, not claims; a closed-access flag is not the end (four PMC article pages); a table the lead rests on can contradict its own methods (34021541). Consumer: IT (K01 source line), ADV (acquisition round for ranks 26 to 55, 20 of them open access). Rule: score a prediction on what was asked, say so when the range was missed by a factor, and verify every acquired artefact for its own PMID.

## Update 2026-11-25 (SCI, after ADV's reading of this result)

Lesson, at ADV's request: the Europe PMC flags and our own expectations (ADV's and mine: 9 of 25 open, 7 acquired) understated what plain, declared, permitted routes reach. 20 of 25 were flagged open and 24 were acquired, because a paper flagged not open can still be on PMC as a readable article page, and because fullTextXML failing with 500 or a timeout is a route result for that route, not for the paper. Rule for the next round: try the PMC article page and the journal's own page by one plain request each at a human rate before listing a paper for the operator. ADV also verified at the abstract that 34021541 says 'cellular and rat models' and 'ICR mice' in the same abstract; the Table 1 against Table 2 arm is not yet independently checked by a second reader.
