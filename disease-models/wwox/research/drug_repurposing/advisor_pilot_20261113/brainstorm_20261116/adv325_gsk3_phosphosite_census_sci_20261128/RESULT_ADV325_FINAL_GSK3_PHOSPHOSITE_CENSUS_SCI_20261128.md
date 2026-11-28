# ADV-325 final result: GSK3-substrate phosphosite census over held WWOX texts (SCI, 2026-11-28)

Hypothesis level; not medical advice. No register is edited. Rule: `PREREG_ADV325_GSK3_PHOSPHOSITE_CENSUS_SCI_20261128.md` (sha256 0983cfd7e3660537d9f43f7d28878d885d2d3fba860aad89448308098bf3585d, frozen 2026-11-28T12:48:22Z). It supersedes the interim of the same day where they differ; the cell-by-cell comparison with HE's blind table is in `COMPARISON_ADV326_ADV325_SCI_20261128.md`.

**Second reader: done** (`SECOND_READER_ADV325_SCI_20261128.md`, beside this file; its five changes are applied below).

## Answer

In the held files examined, **no readout meets the frozen rule as quantified (Q or Q-cell) on the reading of Cheng Fig 7c taken here (R; see the boundary below)**. Two meet it only as class R:

| Source | Material | Readout (listed site) | Class | Why not Q |
|---|---|---|---|---|
| Cheng 2020, PMID 32000863, Fig 7c | Wwox +/+, +/-, -/- mouse cerebellum, hippocampus, cortex; age **P20 in the legend, P14 in the Western blotting Methods (open premise)** | GSK3B pSer9 and total GSK3B immunoblot; ratios to beta-actin printed under one representative blot | **R** | "four independent experiments", unit not defined; animals per genotype not printed; no per-experiment value, spread or test; anti-GSK3B and anti-pSer9 antibodies not named |
| Wang 2012, PMID 22193544, Fig 1d | SH-SY5Y, WWOX siRNA (Results text); control lane labelled mock (HE's figure read) | Tau pS396 blot | **R** (cell material) | blot only; no number, no n |

Cheng Fig 7c values (+/+, +/-, -/-), pSer9 / beta-actin: cerebellum 2.7, 3.1, 1.3; hippocampus 3.6, 3.5, 2.0; cortex 3.9, 3.8, 2.5. Total GSK3B / beta-actin: cerebellum 2.2, 2.4, 2.4; hippocampus 2.3, 2.4, 2.6; cortex 2.2, 2.4, 2.6. Read from the figure by HE (ADV-326) and by an SCI delegate.

Wang Fig 1e is a differentiation count, not a phosphosite; Fig 4b adds GST-WWOX protein in vitro (not WWOX-deficient material): both N.

**No listed GSK3-substrate site (beta-catenin Ser33/37/Thr41, CRMP2 Thr514, glycogen synthase Ser641, the listed Tau sites) was found read in any Wwox-deficient brain** in the files examined. The only listed-site brain readout is on GSK3B itself.

## The boundary, stated

Cheng Fig 7c is R on this reading: the printed number belongs to one representative blot, and "four independent experiments" does not say that four animals per genotype were quantified. A literal reading that takes "four independent experiments" as n = 4 per arm makes it **Q in Wwox-null brain inside P14 to P21 under either printed age**, which is the pre-registered strong counterexample to H2. **The one printed item that would decide it:** a table of the four experiments' pSer9 densitometry per genotype and region, naming the animal (or pool) behind each value. Under either reading the panel gives one representative blot's ratios only: there is no held baseline with per-animal values or spread, so it cannot size an experiment.

## Outside the frozen list (adjacent; none counts as a pass)

* **Chang 2015, PMID 25650666, Fig 5D:** Tau **pT181** aggregates counted by immunohistochemistry in brain sections of 3-week-old Wwox +/+, -/+, -/- mice, n = 5, p = 0.0176; the paper states an increase in -/-. Already in the paper registry (PAPER 137), which adds that the heterozygote mean sits below wild type (no gene dosage) and that this is a section count, not tau biochemistry.
* **Lin 2022, PMID 36498839, Fig 6F:** pT181 plaque counts, cortex, 11-month Wwox +/- against +/+: no significant increase. Fig 1B of the same paper is an "NFT" antibody blot in MEF cells, epitope unstated, +/- against -/- with no wild-type lane, no n.
* **Wang 2012, retinoic-acid differentiation (not WWOX-deficient):** phospho-GSK3B S9 and phospho-beta-catenin "remained normal" while WWOX rose and Tau pS396/S404 fell. CLAIM 016 and CLAIM 035 carry the caution that pSer9 alone is not established as a readout of GSK3B activity here (nor shown to be a false negative).

## Outside the held perimeter

Sze 2004, PMID 15126504: **abstract only** (ledger lookup 2026-11-28; blocker FT-024). Its abstract reports, on WOX1 siRNA in neuroblastoma SK-N-SH cells, Tau phosphorylation at Thr212/Thr231 (**Thr231 is a listed site**) and Ser515/Ser516, and "enhanced phosphorylation of glycogen synthase kinase 3beta (GSK-3beta) and ERK" (GSK-3beta residue not stated); no number or n. It is a cell-material lead, not a pass and not a negative; no new access request was made.

## Against the pre-registration

| Predicted | Observed |
|---|---|
| passes (Q or Q-cell): 3, range 1 to 6 | **0** on the R reading of Cheng (below the range, a miss); 1 on the literal n = 4 reading (inside it) |
| class Q in Wwox-null brain at P7 to P28: 0 (30 percent for 1 or more) | 0 on the R reading of Cheng; 1 on the literal n = 4 reading |
| H2 favoured, 70 percent | H2 stands on the R reading. The lean was informed by an earlier figure audit of Cheng, so it is not an independent test |
| direction of a shared GSK3 site comparable across two papers | not testable: no site is read quantitatively in two sources |

## What it changes

* **GSK3 same-animal panel:** remains a new laboratory observation; there is no held baseline with per-animal values or spread. CLAIM 035 already asks such a readout to take Tau S396/S404, Tyr216 and Ser9 together with total GSK-3. Proposal for IT and ADV, not a decision: consider Tau pT181 beside total Tau as a pointer site, since it is the one Tau phosphosite with a count in null brain (weak: aggregates counted, no dosage).
* **Lithium-also-lowers-WT confound:** unchanged; the census did not search for lithium and supports no statement about lithium-treated tissue. ADV-327 asks the public literature.
* **RP-026:** no change of order from this census; the laboratory dependency stays.
* **Interim corrected:** the interim's "13 PMIDs with a hit, 2 with data" understated the search gap (below) and misattributed Wang's panels and class.

## Method and limits

1. Strict site regex (`census_strict.py`) over `files/fulltext` texts that mention WWOX or WOX1 (508 files, 394 ids). As run for the interim it read **only the largest file per id**; rerun on every file, plus the text types of `files/supplement` and `files/supplements`.
2. **Post-freeze screen amendment (search recall only; the inclusion rule is unchanged).** The strict regex missed "pT181-Tau" and "phosphorylated tau", and with them Chang 2015. A broader phrase screen ("phosphorylation of ...", "...-phosphorylation", "p-"/"pT"/"pS" forms for GSK3, Tau, beta-catenin, CRMP2, glycogen synthase) over XML, text, HTML, PDF, DOCX and Markdown files of the three folders (2671 files read) found 64 WWOX-mentioning id groups (copies and PMC ids not all merged).
3. Reading: Cheng and Wang by SCI text reading and HE's blind figure reading; seven Tau-term texts read to the end by one delegate (receipts, `partial_fulltext_read`: figures and references mostly not read); of the 64 groups, 14 had been examined in the steps above, one was not triaged (below), and the other 49 were triaged by a second delegate on matched passages, with rendered figures for the three positives: 1 R (Cheng again), 2 adjacent, 46 N, none undecided. PMID 42422765 matched the broad screen and was not triaged (held back by standing instruction).
4. **Not covered:** labels that exist only in images; supplements of most N papers beyond the strict screen; image, video, archive and legacy `.xls`/`.doc` files; phosphoproteomic tables that give sites in separate columns. A negative here is dated 2026-11-28 and bounded by these queries; it is not a statement about the literature.
