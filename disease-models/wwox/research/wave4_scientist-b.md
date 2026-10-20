# Wave 4 — Scientist B — group W1 (older never-read WWOX-direct background and transferable rows)

Actor `scientist-b`, task `W4-W1-B-20261019`, branch `task/W4-W1-B-20261019` (worktree `.claude/worktrees/w4-b`, from main e956fe1e). Mode `PRIMARY_EVIDENCE_READ`, `context_policy` SOURCE_FIRST for every paper (all first reads; the queue and registry were opened only after the locators were captured). Receipts are staged, not recorded. Public disease-level record; nothing here is medical advice. Every substitute row is labelled NOT WWOX evidence.

## 1 · Result in one table

| PMID | Paper (tier) | Depth (staged receipt) | Manifest | Main finding |
|---|---|---|---|---|
| 41510857 | Kilic 2026 DRE genetics cohort (1) | complete | PASS | FT-115 negative confirmed: counts only (WWOX 4, CACNA1H 6 of 261), no patient-level data, no T-type text, Figure 1 does not match text counts |
| 40327201 | Hammouz 2025 cancer review (1) | partial (organ-cancer sections not read) | PASS | cancer-cell glycolysis-up sign for WWOX loss unremarked against null-mouse hypoglycemia; vermis and migration statement sits next to a case-report citation that contains neither |
| 35883580 | Liu 2022 pY33 to pS14 review (1) | partial (figures captions only) | PASS | originating-laboratory model; no measurement in any WWOX loss-of-function tissue; heterotopia in newborns cited to mouse papers; one retracted WWOX-direct citation |
| 27075929 | Chang 2016 bubbling cell death (1) | PARKED | n/a | PMC author manuscript only, no lawful body reachable |
| 29581896 | Kuo 2018 FRET method (2) | partial | PASS | n = 2 to 4 per trace, no statistics, ectopic overexpression, dominant-negative control still peaks |
| 27773744 | Schrock 2017 Fhit and Wwox (2) | partial (no figures obtainable) | PASS | thymidine rescue is in Fhit-null cells only; Wwox survival data rest on five lines, one passage comparison, one unadjusted database split |
| 25802472 | Chang 2015 thematic-issue editorial (2) | PARKED | n/a | PMC author manuscript only |
| 35107375 | Liang 2022 WWOX and AMOTp130 (2) | PARKED | n/a | published version closed; bioRxiv version rate-limited (429) |
| 36979157 | Kaluzinska-Kolat 2023 GBM lines (2) | partial | PASS | WWOX gain 2.6- to 15-fold raises apoptosis in 3 of 4 lines and lowers a resazurin readout in all four; non-neuronal |
| 42720877 | Schatz 2026 epilepsy-genetics review (3, class level) | partial | PASS | WWOX table row "MedPath Trial of gene replacement" is unsourced; no WWOX trial registered by condition search |
| 42738851 | Pozhitnova 2026 iPSC fragile sites (3) | partial | PASS | FRA16D minor and line-specific in three iPSC lines; WWOX not recurrently rearranged in culture |
| 42650175 | Delahanty 2026 PBA with SLC6A1 (3, NOT WWOX evidence) | partial | PASS | ER-retained transporter rescued in cells; 4 mM PBA reduced viability; trial feedback stated without data |
| 42587736 | Song 2026 PBA with GABRA1 (3, NOT WWOX evidence) | partial | PASS | PBA raises wild-type and variant alike; mouse data expression-only in 3-4 animals; human arm one uncontrolled child |
| 42846717 | Samanta 2026 ketogenic review (3, NOT WWOX evidence) | partial | PASS | WWOX absent; KD evidence in the relevant syndromes is small series; hypoglycemia at induction is a listed class risk |

Eleven readings, three parked: 14 of 14. Dossiers: `fulltext_dossiers/PMID<PMID>.md`; manifests: `deepdive_manifests/`; receipts: `receipt_staging/scientist-b/FTR-20261019-<PMID>-01.json`; commit candidate `CC-20261019-SCIENTIST-B-W4-NEGATIVES-01`. `owed_sections.py --staging` reports exactly the partial sections named in the table (for example 42738851 owes figures, introduction, methods, results, supplementary and tables; 41510857 owes none).

## 2 · What the lot says as a set

1. **The T-type negative stands and is cleaner.** The only PubMed record joining WWOX to a T-type channel gene has no patient-level data and no calcium-channel text (FT-115). The queue wording "across different patients" is not supportable and should read "no patient-level data".
2. **Several secondary sources in this lot carry claims their citations do not hold**: the WWOX "trial of gene replacement" line (Schatz), the vermis and migration statement (Hammouz), newborn heterotopia (Liu), the cancer-cell glycolysis-up sign presented without the null-mouse hypoglycemia (Hammouz). The repository should cite primaries.
3. **The pY33 to pS14 model and the FRET method are one laboratory's, with weak statistics** (n = 2 to 4, no tests, ectopic overexpression, a dominant-negative that still peaks); they are not independent support for each other.
4. **There is still no cofactor, nutrient or supplement report for WOREE, SCAR12 or Wwox loss in this lot.** The only supplementation experiment is thymidine in Fhit-null cells (27773744). Class-level rows (ketogenic review, two phenylbutyrate papers) are substitutes: they supply base rates (anecdotal KD evidence in the syndrome classes that contain WWOX-DEE; hypoglycemia at induction), a dose caution (4 mM PBA reduced cell viability; PBA raises wild-type protein too), and the system-gap statement (membrane transporters and receptors versus a cytosolic WWOX).
5. **WWOX gain of function is not inert in glial-tumour cells** (36979157): a non-neuronal caution for the dose-control census; nothing about neurons.

## 3 · Effect on the disease model

No claim is reversed (MINOR). Proposed: retire FT-115 as a confirmed negative with the wording refinement; annotate the Schatz table line and the Hammouz paragraph as unsourced or mis-attached; keep every class-level row labelled SUBSTITUTE.

## 4 · Parked and the cascade run

- **27075929 (Chang 2016), 25802472 (Chang 2015) and 35107375 (Liang 2022).** Each has a PMCID and a green-OA label (OpenAlex), but the PMC efetch XML is a 6 to 13 kB stub, PMC HTML and PDF paths serve the reCAPTCHA page or an interstitial under no User-Agent, Europe PMC `fullTextXML` returns HTTP 500 and the render and `ptpmcrender` routes return 403; the PMC open-data bucket holds no key for them. For 35107375 the preprint DOI exists (a bioRxiv version) but the publisher site returned HTTP 429 (backed off, not retried in a loop) and Europe PMC holds no full text for the preprint record. Operator wishlist: the three author-manuscript PDFs (the first two are Exp Biol Med 2015 and 2016 items, the third a J Virol 2022 paper).

## 5 · Blind locator audit (voluntary; no mandatory trigger met)

Seven load-bearing triples went to a blind auditor (sources only): six SUPPORTS and one PARTIAL (Hammouz vermis and migration). The PARTIAL was my overstatement: the sentence has no citation of its own; the Feng citation sits on the preceding sentence, so the attribution is by adjacency. It is corrected and declared (`contradicts_locator` with the audit object) in the manifest, dossier, commit candidate and receipt. One numeric correction (Kuo Figure 2 level after the early peak: about 2,000 to 4,000, not 2,500) was declared likewise. Two auditor side-observations kept: the Kilic figure uses two x-axes (ADGRV1 reaches about 14 on the top axis against 6 in the text); in Kaluzinska-Kolat Figure 2B the proliferation difference runs opposite ways in T98G and U87MG against DBTRG-05MG.

## 6 · Method deviations and DEFAULTS_TAKEN

See the task contract `ledger/tasks/scientist-b/W4-W1-B-20261019.json`. In brief: all first reads are partial where only the passages relevant to the stated question were read (declared per receipt); gene-direct references of reviews are listed as queued strings in each manifest (this actor does not edit the queue); commits under `LEGEND_STALE_SURFACES_BECAUSE`; the ClinicalTrials.gov condition queries of 2026-10-20 are recorded as `external_provenance` on the Schatz locator.
