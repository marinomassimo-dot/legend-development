# SCI47 selective tail — what was done, and what was deliberately not

Non-canonical research material. Not medical advice. Reference genotype class only. Paths relative to `disease-models/wwox/research/drug_repurposing/`.

## Chosen (only items that change a consumer)
1. **Reading debt IT45 S10 for 38116420 and 21964340 (items named by the mandate): two targeted readings, two staged receipts of the coverage actually reached** (`receipts/`, ids -75, validated, not recorded; both `first_read`, `partial_fulltext_read`, bytes preserved by HE46 with SHA-256 in the receipts). They are **not** a complete reading of either article and must not be converted into one.
   * **38116420** (Markovtsov et al., ACS Med Chem Lett 2023): read Abstract, Introduction, Results and Discussion in the preserved text; figure images 1, 2, 3, 4 and Scheme 1 opened; **Table 1 cell values not in the preserved text and not obtained** (tables not_read); Supporting Information gated (unavailable). Findings relevant to the S10 pointer premise: the paper contains **no sulforaphane Nrf2 value** (sulforaphane is named once, in the Introduction, as a natural activator); the Nrf2 readouts are an Nrf2 translocation assay and IL-23 inhibition after LPS (THP-1 and dendritic cells), Nrf2 and HO-1 protein by blot in THP-1 cells (Figure 2a: Nrf2 and HO-1 rise with concentration for compounds 13 and 9, weakly for 17 and DMF), nuclear Nrf2 and p65 staining in HUVEC, and Nrf2 in thymus in the EAE study; no neural cell is used; DMF/MMF are comparators; EAE efficacy of the compounds is a clinical-score readout in mouse; Nrf2 loss is not tested in this paper (there is no Nrf2-null or knockdown arm in the text read). The statement "the NRF2 translocation EC50 of 17 is 32.4 µM and of 13 0.30 µM" is in Results (read).
   * **21964340** (Dawson et al., Nature 2011): main text only; no figure image opened; supplements not downloaded. The pull-down passage: bead-immobilised acetylated histone peptides captured 27 bromodomain proteins from HL60 nuclear extracts; excess I-BET151 or I-BET762 blocked capture of Brd2, Brd3, Brd4 and Brd9 and had no effect on 23 other bromodomain proteins including MLL; the Brd9 effect is said to be likely indirect. I-BET762 is the bead-ligand analogue of the first chemoproteomic approach. That is a BET-selective capture result in a leukaemia nuclear extract; the main text carries no data on other target classes, so it neither supports nor refutes a row that assigns the compound to another target.
2. **Winkel 2015 full text (an open NRF2 question, SCI46 D20):** the one retry, made with a new reason (the earlier HTTP 500 was hours old), returned HTTP 500 again from the same Europe PMC endpoint (2026-11-12 09:15 UTC). Recorded as a technical block, **not** a negative result and not retried by another route; the abstract-level status of D20 stands.

## Deliberately not done
* Criterion of adequacy of an NFE2L2 loss: already written in SCI46 (D19, outcome matrix O1-O10); repeating it would not change a consumer.
* A compensatory lever other than signature reversal: package A (levers.tsv L4, L5) carries it.
* Davies 2016 text or supplement: ACS and PMC routes are closed (no PMC id; ACS blocked earlier); not retried.

## Consumer delta (proposals; nothing applied)
| # | Recipient | Proposal |
|---|---|---|
| 1 | Reading-debt tracker (`he46_20261111/reading_debt_s10.tsv` and the IT46 P6 note) | after the integrator records the two receipts (-75), mark 38116420 and 21964340 as targeted partial readings with the coverage above; do not count either as a complete reading |
| 2 | IT45 S10 premise on 38116420 | the pointer premise "an ester/metabolite assay with a sulforaphane value" is confirmed absent in the text read |
| 3 | `keap1_nrf2_sci46_20261111` D12-D15 notes (fumarate class) | 38116420 adds no Nrf2-loss arm and no neural cell; it stays context, not mechanism |
