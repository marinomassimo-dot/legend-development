# IT22 P4 batch 1: qualification of four conditional proposals handed over by IT21 P2 (2026-11-03)

Non-canonical research material. Public edition: the reference genotype is a WWOX-DEE genotype class; no individual-level record; no e-mail address, operator identity or contact string was sent to any service; zero spend, no registration.
**Not medical advice.** No scientific current file, registry, card, need, ranking or ledger was edited and no receipt was recorded (the 17 receipt files in `receipts/` are prepared for the integrator). A generated conditional proposal cannot be QUALIFIED here: a qualified hypothesis needs a sourced role of the observed change and a measured link in a WWOX system, and none of the four has either.

## 1. Decisions (first)

| Proposal | Compound | Q / arm | Disposition | Deciding reason (one line) | Novelty |
|---|---|---|---|---|---|
| IT21P2-0005 | pracinostat (SB939), pan-HDAC | Q2 H_HARM, HDAC5 -> SLC2A1 | **INCONCLUSIVE** | HDAC5 IC50 is 47 nM in one source and 5113 nM in another (109-fold), class I and IIb values sit within 1-2x of HDAC5 in the first, so attribution to HDAC5 cannot be decided; the one edge reference is a muscle knockdown | known thread re-emitted |
| IT21P2-0043 | desidustat (ZYAN1), pan-PHD | Q2 H_PROTECT, EGLN2 -> FOXO3 -> BNIP3 | **INCONCLUSIVE** | no EGLN2/PHD1 potency exists for the compound and the only EGLN2 -> FOXO3 evidence used non-selective PHD inhibitors, while the seed genes also respond to the direct HIF route; role unknown | known thread re-emitted |
| IT21P2-0052 | AT-13148, dual ROCK/AKT | Q4 H_HARM, MAPKAPK2 -> CDC25A -> FOXO1 -> NPY | **INCONCLUSIVE** | the premise that it inhibits MAPKAPK2 has no positive measurement (curated mechanism row without an activity row; the one MK2 value, Kd > 30000 nM, is uninformative because the same assay also reads AKT > 30000 nM); measured profile is ROCK/AKT/PKA at 4-50 nM | known thread re-emitted (via ROCK2 in IT9/IT10); the Q4 MK2 relation is new for this molecule |
| IT21P2-0380 | rineterkib (LTT462), ERK1/2 | Q5 H_PROTECT, MAPK1 -> BCL3 -> TNF | **INCONCLUSIVE** | the chain predicts TNF/IL6 up, the direct ERK requirement for TNF predicts down in the same cell type, nothing measured in a Wwox system decides, and the molecule has one potency number and no selectivity | known thread re-emitted |

Counts: INCONCLUSIVE 4, KEPT_CONDITIONAL 0, REJECTED_INFORMATIVE 0, QUALIFIED 0. All four keep `status_after = status_before`. None is rejected because in each case the datum that would decide is missing, not contradicted, and unknown is not negative. Each record names the missing datum.
Table: `qualification_it22_p4_b1.tsv` (the 22 columns of the IT21 P4a records, in the same order, plus `why_not_proposed_before` and `novelty_class`).

## 2. How the carried context was used

* **Carried limits.** Every row keeps its hand-over limit: for the two Q2 rows the second-system limit SECOND_SYSTEM_GATE_FAILED (the hNPC library of GSE126075 did not show WWOX lower, `hnpc_gse126075_it5_20261029/RESULTS.md` section 1, so the human second system is not independent); for 0052 NPY_SIGN_CONTESTED and the gamcemetinib premise (MK2-CDC25A-FOXO1 in postmitotic NPY neurons, not shown); for 0380 the Bcl3-derepression v direct-ERK competition from the tizaterkib record. One origin counts once (the two human deposits behind the Q2 seeds are one shared derivation).
* **Same-type potency only.** `typed_potency_it22_p4_b1.tsv` lists every ChEMBL value by target, measure type, unit and document; `class_alternatives_it22.py` (with the shared catalogue cache) gave the GtoPdb typed values (pracinostat HDAC5/1/3/10 IC50 47/49/43/40 nM; rineterkib MAPK1 IC50 0.026 nM with no other target; no ligand at EGLN2 or MAPKAPK2). IC50, Ki and Kd are never compared with each other. Where two sources disagree for one target the disagreement is reported, not averaged. Nothing in this package says "more potent" or "less toxic" from similarity.
* **Decision scope.** `decision_scope_it22.tsv` was applied as written. Nanatinostat's rejection (a statement about its own potency profile) is not applied to pracinostat, which was assessed on its own data; only its edge-level limit (HDAC5 -> SLC2A1 rests on one muscle reference) transfers. Roxadustat's DROP (EU-label properties; a FOXO3 -> SLC2A1 repression edge the desidustat chain does not contain) does not transfer. Gamcemetinib's and tizaterkib's edge-level premises transfer to 0052 and 0380, their molecule-level data do not.

## 3. What was retrieved (denominators)

* ChEMBL REST (`ChEMBL_37` as served 2026-11-03): 4 molecules, 4 mechanism queries (curated rows: AT-13148 two, none for the others), 4 activity sets (81 + 6 + 316 + 1 rows), 83 typed rows kept. Raw files are not in git; digests in `raw_hashes_it22_p4_b1.tsv`.
* OmniPath: 8 edge pairs, filtered locally by gene symbol (the service ignores part of its filters): 8 of 8 found; reference lists as served.
* Expression: the two local WWOX-deficient human datasets, descriptive only (`organoid_gene_rows_p4_b1.tsv`, GSE156243, 4 KO v 2 WT libraries; `hnpc_gene_rows_p4_b1.tsv`, GSE126075, one library per arm; a gene missing from the hNPC table is ABSENT, never zero). The mouse Wwox deposits that carry the Q5 seeds were not extracted here.
* PubMed (MCP): metadata and abstracts for about 30 records, open full text for 5 (PMC XML saved, hashed, quotes matched by exact string search).
* Europe PMC returned HTTP 500 for three of the five article XML fetches (NCBI PMC served them instead); NCBI E-utilities rate-limited several count queries (not used for any figure here).

## 4. Reading depth (`reading_depth_it22_p4_b1.tsv`)

| Depth | Papers |
|---|---|
| partial full-text read (receipt prepared) | PMID 32616501 (AT13148 first-in-human; text read end to end, figures/tables/supplement/references not read), PMID 39914641 (desidustat, stroke, CKD mice; same coverage) |
| queried, not read section by section (receipt prepared) | PMID 28689659 (Bcl3 phosphorylation; keyword passages) |
| existing ledger reading re-inspected, no new receipt | PMID 24990963 (EglN2/FOXO3a, earlier partial reading FTR-20261030-24990963-01), PMID 22991226 (abstract) |
| abstract only (receipt prepared) | 20181828, 15629715, 17292828, 21670150, 16783365, 15465827, 22798670, 22781553, 25840982, 29360358, 39383771, 38759372, 30841499, 42415186 |
| abstract only, no new receipt | the seed papers 30290271, 36828035, 34268881 (existing ledger events) |
| not read; value taken from a ChEMBL row | 29191878 (kinobead Kd), 25637120 (Ki panel), 40263713 (desidustat enzyme panel), 32791404 |

`locators_it22_p4_b1.tsv`: 15 verbatim quotes (L1-L15) matched against the saved article text, plus three absence locators (N1: no MK2/MAPKAP/CDC25 string in the AT13148 article; N2: no FOXO/BNIP3/EGLN string in the desidustat stroke article; N3: no TNF measurement in the Bcl3 article).

## 5. Findings the generator should hear

1. **A curated mechanism row can stand with no activity row** (AT-13148 -> MAPKAPK2): the curated MK2 target rests on references whose abstracts, and in one case full text, do not name MK2. The engine took it as the compound's main target.
2. **A kinobead non-detection is not a negative**: the same table gives AKT1/2/3 Kd > 30000 nM for a compound with AKT IC50 38-402 nM. Any rule that treats "> 30000 nM" as inactivity would have rejected the true target.
3. **Two IC50 sources for one compound-target pair can differ 109-fold** (pracinostat HDAC5 47 v 5113 nM), and the engine's "ATTRIBUTABLE, 1.2-fold" reads only one of them. A check for a second typed source per pair would have flagged it.
4. **Isoform naming trap**: EGLN2 is PHD1, the paper and the label say "PHD2" for EGLN1; the only desidustat PHD value is at EGLN1. A potency joined by compound name at "PHD" would have been credited to the wrong gene.
5. The BBOX value for desidustat (420 nM) is lower than its PHD2 value (1300 nM) inside the same document: a measured off-target axis nobody had listed.
6. The IT21 rerun table already labelled the 0052 Q4 row "GAINED_BY_RERUN_NULL_OR_SIGN_CHANGE_NOT_A_FINDING" while the hand-over still carried it as a proposal.

## 6. Limits and UNVERIFIED (consolidated)

Abstract-level reading carries every literature sign except the L-locators; the bodies of PMIDs 20181828, 15629715, 17292828, 21670150, 16783365, 15465827, 22798670 and 22991226 could qualify a sign (21670150 returned an empty body from the full-text route). The direct ERK -> TNF route and Tpl2 are carried at title level from the tizaterkib record, not re-read. The HIF-responsiveness of BNIP3/SLC2A1 in neural cells is background knowledge, not verified here. Not checked: brain exposure of any compound; EGLN2/PHD1 potency of desidustat; a cell-free MAPKAPK2 IC50 for AT-13148; selectivity and cellular potency of rineterkib; mouse Mapk1/Bcl3/Tnf values in the Wwox mouse deposits; which pracinostat HDAC5 value reflects cellular engagement; a desidustat approval statement (taken from a 2025 paper, not from a label). ChEMBL and PubMed are moving services (counts as served 2026-11-03). Expression comparisons are descriptive (4 v 2 libraries, one library per hNPC arm, no test).

## 7. Files

`qualification_it22_p4_b1.tsv`, `edge_provenance_it22_p4_b1.tsv` (12 edges: sign, level, system, transfer, local check, grade), `typed_potency_it22_p4_b1.tsv`, `locators_it22_p4_b1.tsv`, `reading_depth_it22_p4_b1.tsv`, `raw_hashes_it22_p4_b1.tsv`, `organoid_gene_rows_p4_b1.tsv`, `hnpc_gene_rows_p4_b1.tsv`, `receipts/` (17 JSON files, event IDs `FTR-20261103-<pmid>-NN`; the Bcl3 one is `-02` with `prior_receipt` `FTR-20261103-28689659-01`), `rows_it22_p4_b1.py` (the four records as data) and `build_batch1.py` (writes the tables and receipts from the served raw files; `--help` is safe).
