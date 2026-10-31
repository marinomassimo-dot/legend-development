# Proposals from IT12 P1-alt (not applied; for the batch path)

## 1. Card notes (text for the owner of the card; no card file was edited)

* **E03 (PDK inhibition, DCA).** Add to `limits` or `p4_fields.counter_evidence`: in the only genome-wide genetic-interaction screen of a WWOX-null line (HAP1, one clone, unreplicated; GSE298081, authors' Data S4), loss of PDHA1 (qGI +0.567, FDR 0.020), CS (+0.566, 0.036), LIPT1 (+0.345, 0.075) and NDUFAF1 (+0.318, 0.051) is better tolerated by the WWOX-null clone than expected, which is the opposite sign to a PDH-activation rationale. The four genes are common positive-interaction hubs (same-sign calls in 30 to 40 of 298 query screens), the system is a leukaemia-derived line and the endpoint is proliferation. Status: counter-evidence of low weight; does not change the assessment. Suggested probe: add a PDHA1 knockdown arm to the isogenic PDH-activity experiment already specified in E03.
* **E04 (ketogenic / lactate axis) and any 2-deoxyglucose-class idea.** Caution note: in the same screen SLC2A1 (qGI -0.593, FDR 0.050) and HK2 (-0.464, 0.040) loss is worse tolerated by the WWOX-null clone (an aggravator). Non-neural, unreplicated; a caution on direction, not evidence of harm in neurons.
* **K01 (HIF/glycolytic shift).** Sign-compatible only: the screen's glycolysis-dependence pattern (SLC2A1/HK2 aggravators; TCA-entry genes less needed) fits a glycolysis-weighted clone. HIF1A qGI +0.395, FDR 0.22 (not significant); EGLN1 +0.118, VHL -0.182 (not significant). No convergence is claimed: one clone cannot separate WWOX loss from clonal adaptation, and SLC2A1/HK2 are the IT7 seed rows (guard IT7_READOUT6).
* **L01 (NRF2), M01 (MYC), G01 (lithium/GSK3), E01 (ISR).** No support in the screen: NFE2L2 +0.101 (FDR 0.97), KEAP1 +0.018 (0.96), MYC +0.155 (0.81), GSK3A -0.059 (0.94), GSK3B -0.344 (0.75), EIF2AK1 +0.372 (0.48), EIF2AK3 -0.194 (0.86), ATF4 +0.033 (0.95), EIF2AK4 -0.355 (0.33), TP53 -0.326 (0.55) (Data S4; the clustered matrix S8 lacks ATF4, TP53, KEAP1, GSK3B). Absence of an interaction in a proliferation readout of a non-neural line does not weaken a neural premise.
* **E02 (LDH inhibition).** Unchanged. HAP1 shows no LDHA/LDHB interaction (+0.016 / -0.113, FDR 0.88 / 0.79); the fly rescue (PMID 42909904) remains the single genetic premise.

## 2. Needs (new entries proposed; wording for `needs/needs.json` owner)

* **N-P1B-1 (second clone / re-expression of the HAP1 WWOX screen).** Ask the data holders (Moffat/Myers/Boone groups, contacts are in the GEO record; do not send any operator address) whether a second WWOX-null clone or a WWOX re-expression screen exists. Decisive datum: reproduction of PDHA1/CS/LIPT1/NDUFAF1 (positive) and SLC2A1/HK2 (negative) in a second clone. Cost: one e-mail by the operator; zero spend.
* **N-P1B-2 (neural genetic-interaction readout).** Any CRISPR screen or targeted knockdown panel in WWOX-null versus corrected human neural cells (iPSC-neuron, NPC or organoid) with a proliferation, viability or activity endpoint; the panel to include LDHA, PDHA1, SLC2A1, HK2, HIF1A. Merge with the isogenic experiments already specified in K01/E02/E03 rather than a separate study.
* **N-P1B-3 (DepMap bulk).** If an operator-run bulk download of the DepMap release is made, test whether WWOX expression or copy number tracks any dependency among PDHA1, CS, SLC2A1, HK2 across lines. Hypothesis only (dependency is not rescue). Licence of the release to be read first; the portal cannot be used (human verification page).
* **N-P1B-4 (ChEMBL retry).** Re-run the lever identity and potency lookups (LDHA inhibitors, GLUT1 inhibitors, PDH/lipoylation inhibitors) when the ChEMBL REST returns 200; none was read at source in this package.

## 3. Receipts (not written)

* GEO series GSE298081/GSE298082 SOFT (sha256 of the merged text 8247b78e...), PMC13281610 full text (sha256 cbdc7dea...), Zenodo GIN-v1.0.4.zip (md5 e2e391f703cbf8245dbd417f6c673722, sha256 c380d079...) with Files S1, S4, S8 parsed. Proposed `source_kind` = public_dataset_derived; evidence_depth = partial_fulltext_read for the paper (design, qGI, replicate, suppression and data-availability passages; not the supplementary figures) and complete table read for S1/S4/S8 (the WWOX query column and the replicate-pair sheet).
* PMC13684411 (PMID 42909904): one sentence set re-read (Ldh rescue); already covered by FTR-20261026-42909904-01; no new receipt needed.
* PMC3016910 (21075834) and PMC4547717 (26302329): genetic-interaction passages read in XML; repository may record `partial_fulltext_read`.

## 4. Registry notes

* `ops_it11_p5_20261031/scouting_it11.md` WATCH on GSE298081: close as "authors' Data S4 read; no WWOX-specific suppressor/sensitiser claim possible; association table only". The IT11 crude check (6 genes z<-4, 1 z>4 versus 15 batch-unmatched WT screens) and the authors' scores agree that the profile is sparse (88 calls; rank 18 of 298 from the sparsest).
