# COMMIT CANDIDATE — CC-20261124-ORCHESTRATOR-ADV215-CORPUS-STUBS-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-215, PubMed delta intake) · **Date:** 2026-11-24 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/it_adv215_20261124/RESULT_ADV215_PUBMED_DELTA_IT_20261124.md` and its triage table (PubMed metadata and abstracts read 2026-11-24; three free PMC texts read for targeted contexts, no receipt written).
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. Neither registry is edited by this act, and no standalone batch is run for it.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS (stated before any apply)
**MINOR.** Nine new CORPUS stubs (class-level placeholders, `not_processed`, no claim link, no grade above the placeholder default) and one identifier line on an existing record (`LIT-0538`). No claim, working-model sentence, ranking row or compound card changes; no existing record's status, receipt or grade changes.

## 2 · What and why
The WWOX PubMed count is 708 today (standing term of RESULT section 1, point 5). Seven of these records carry no registry record (six are named only in research notes, one appears nowhere), and two human `WOX1` records are cited only in the reference lists of held full texts. A census that is not a record cannot be counted as reading debt (gold_is_in_the_details); a stub makes the debt countable and costs nothing else. The 37 plant WOX1 records of ADV's list are **not** registered (not WWOX).

## 3 · Proposed records (corpus numbers are assigned at propagation, the next free numbers after the last `CORPUS-STUB`)
Common fields for all nine: `Status: not_processed` · `Registry role: corpus placeholder only` · `Claim links: none` · `Note: Added by CC-20261124-ORCHESTRATOR-ADV215-CORPUS-STUBS-01 (ADV-215 intake). Triaged at abstract level; where a free PMC text exists it was retrieved and the WWOX contexts read, with no receipt. Preserve until processed, filtered out, or upgraded to a full PAPER record. Not medical advice.`

| # | Identifier | Full title (PubMed) | Next action |
|---:|---|---|---|
| 1 | PMID 43036373 / DOI 10.1177/15357597261496145 | A Window Into WOREE: WWOX, Organoids, and Epilepsy (Epilepsy Currents 2026, commentary on the held Brain 2026 organoid study; secondary source) | none owed; secondary commentary on `PAPER 094`; its WOREE-over-SCAR12 sentence is a review-level compression and is not imported over the pooled-only reading |
| 2 | PMID 42991897 / DOI 10.3389/fgene.2026.1973684 | Population-specific differences in ClinVar pathogenic and likely pathogenic variants of epilepsy-associated genes between East Asian and non-Finnish European populations: a nucleotide-resolved gnomAD v4.1.1 analysis (Front Genet 2026) | screening only; four WWOX alleles among 17 enriched variants (reference-population counts, small East Asian denominator); transferability T4 for the model (population frequency) |
| 3 | PMID 31829254 / DOI 10.1186/s13041-019-0530-8 | Systematic analysis of expression signatures of neuronal subpopulations in the VTA (Mol Brain 2019) | screening only; wild-type mouse expression map (WWOX co-expressed with TH and VGLUT2 in medial VTA); T3 |
| 4 | PMID 42790938 | WWOX Suppresses Gastric Cancer Cell Proliferation, Migration, and EMT by Negatively Regulating the Wnt/β-Catenin Signaling Pathway (Ann Clin Lab Sci 2026) | screening only; abstract level, not open access; cancer cell lines and xenografts; T3 |
| 5 | PMID 43048821 / DOI 10.2174/0115672026523581261106063859 | Multi-omic Insight into the Causal Relationship Between Programmed Cell Death and Cognitive Function (Curr Neurovasc Res 2026) | screening only; abstract level, not open access; population Mendelian randomisation; T3 |
| 6 | PMID 42635858 / DOI 10.1007/s10126-026-10697-0 | Correlation of Long Non-Coding RNAs and Gene Expression in Response to Reverse Development of Turritopsis dohrnii (Mar Biotechnol 2026) | none; Wwox only a listed gene; T4 |
| 7 | PMID 43004178 / DOI 10.1186/s12711-026-01104-2 | Genetic and regulatory architecture of meat yield traits in commercial pig populations (Genet Sel Evol 2026) | none; WWOX only a GWAS candidate gene in pigs; T4 |
| 8 | PMID 19365417 / DOI 10.1364/oe.17.005987 | Surface plasmon-enhanced two-photon fluorescence microscopy for live cell membrane imaging (Opt Express 2009) | none; `WOX1` (WWOX) only as an EGFP construct used as a membrane label; cited in two held WWOX full texts; T4 |
| 9 | PMID 16140946 / DOI 10.1158/0008-5472.CAN-05-1022 | HYAL1 hyaluronidase in prostate cancer: a tumor promoter and suppressor (Cancer Res 2005) | none; `WOX1` (WWOX) activation read as an apoptosis marker in prostate cancer cells; cited in held WWOX full texts; T3 |

### `LIT-0538` — field `Identifier value` (metadata upgrade, not a new paper)
Old (verbatim): `DOI 10.21203/rs.3.rs-9950101/v1 / PPR1316475`
New: `DOI 10.21203/rs.3.rs-9950101/v1 / PPR1316475 / PMID 42818975 (assigned after 2026-10-04; PubMed preprint record, PMC13622852)`
Also the field `Identifier type` text `DOI / preprint id (no PMID exists)` becomes `DOI / preprint id (PMID assigned later: see Identifier value)`. Every other byte of the record is unchanged; the receipt `FTR-20261004-PPR1316475-01`, the dossier and the Status stay as they are.

## 4 · What this does NOT do
* No `PAPER` record, claim, grade, ranking row, compound card or portfolio row. No receipt. No full-text read is claimed.
* The 37 plant WOX1 records are not registered. `42721537` stays `FT-110`.
* The derived coverage and reading-state surfaces change only by the new rows; regenerate them after the batch.

## 5 · Statements for the blind check at propagation time
1. Each of the nine PMIDs and DOIs in the table matches PubMed (identifier, journal, year, title) — surface: PubMed record.
2. None of the nine is already a `PAPER`, `CORPUS-STUB` or `LIT` record (PMID, DOI and a 70-character title prefix searched in the paper registry, the literature log and the full-text queue on 2026-11-24).
3. The LIT-0538 PMID 42818975 belongs to the same Research Square preprint as DOI 10.21203/rs.3.rs-9950101/v1 — surface: PubMed record (preprint) and the PMC record PMC13622852.
