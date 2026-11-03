# IT21 P6 targeted scouting for six named generative-pharmacology gaps (2026-11-03)

Non-canonical research material; not medical advice. No WWOX-deficient neural system and no patient data are involved; every number below is about public resources. Zero spend, no registration, no e-mail sent to any service, nothing installed, no third-party raw table committed (probe outputs hold counts, gene symbols and 6 module rows only). Searches: WebSearch/WebFetch on GitHub, Hugging Face, Nature-portfolio/bioRxiv/PMC; metadata was read, full texts were not. Machine-readable table: `decisions.tsv`.

## Already compared, not reopened
- Signed TF/kinase edges: SIGNOR + CollecTRI via OmniPath were compared in IT7 P3 (`../network_comparison_it7_p3_20261029/`): NO ADDED VALUE at the registered threshold. Compound-target potency: IT14 P6 and IT15 P5 (DrugCentral, Pharos, BindingDB, PDSP, Papyrus, UniChem) added no pair; a search for a 2026 successor to ChEMBL/BindingDB found only ChEMBL 37 (May 2026) and Guide to Pharmacology 2026.1, both already the module's sources. Chem-PerturBridge, EuTxGNN, DrugClaw, CLAMP, DeepPurpose: IT18. These are not re-asked.
- A directory `scout_it20_*` does not exist; the latest scouting records are IT18 (`../scout_it18_20261101/`) and the IT20 diagnosis.

## Verdicts
| Candidate | Gap | Version / date | Licence (read) | Code / data / weights / service | Test | Verdict | Cost h |
|---|---|---|---|---|---|---|---|
| LINCS L1000 shRNA knockdown, library LIB_6, via iLINCS | b | service undated; 10 WWOX signatures, 986 NPC signatures | iLINCS CC BY | data and service free, key-less; no weights | yes, below | WATCH | 0 to wire (existing `ilincs` adapter takes `libraryid: LIB_6`); 2 to score |
| Curated human genetic-suppression table (Unlu 2023) | c | 2023, 932 rows, 484 genes | supplement terms not read | data only (xlsx 142 KB inside a 26 MB zip) | yes, below | WATCH | 1 |
| PerturbAI whole-brain in vivo Perturb-seq (HF) | b | v1.0, 2026-03-20, mouse, 1,947 genes | card cc-by-4.0; gated on institutional e-mail | data (tens of GB per file), no code in the repo | not possible (gate asks for an e-mail) | WATCH | 3 once the gene list is public |
| Perturb Sapiens (HF) | b | 2026-01-09, 1.34 TB | CC BY 4.0 | model-predicted responses | none (predictions, not data) | REJECT | - |
| GLOW26 negative sampling for biomedical KG | f | Zenodo 2025-12-28, 744 MB + 197 MB | data CC BY 4.0; GitHub repo shows no licence | code and data | none (size; no KG predictor in the module) | WATCH | 4 |
| KGE leakage benchmark (Briere et al.) | f | bioRxiv v2 2025-11-14 | preprint CC BY-NC 4.0; no code licence seen | no code link on page read | none (abstract page only) | TRIAL, reading only | 1 |
| ChEA-KG signed TF edges | a | 2025 | not read | data | none | WATCH | - |
| HPA single-cell JSON / Allen human brain taxonomy | e | live / Allen CC BY-NC | HPA terms not re-read | service | one call | REJECT (covered) | 0 |

A licence not read is not a prohibition and not a permission; terms must be read before any reuse. Redistribution: nothing from these sources is redistributed here beyond gene symbols, counts and 6 LINCS log-fold values.

## Test 1 (gap b): LINCS shRNA knockdown in neural progenitors
Question fixed before running (`lincs_kd_probe.py`): do WWOX knockdown signatures exist, is the knockdown visible, do the six module genes of IT7 P3 appear in the NPC signature, and is the NPC signature related to the other cell lines. Outputs: `lincs_kd_output.txt`, `lincs_kd_module.tsv`, `lincs_kd_control_output.txt`, `lincs_kd_coverage_output.txt`.
- Exist: yes, 10 signatures (LIB_6; HA1E, HCC515, HEPG2, MCF7, NPC, PC3 x2, A375, A549, ASC; 96 or 144 h). NPC = `LINCSKD_25575`, 96 h. This is the first neural-progenitor gene-knockdown readout the module can query; it had used compound signatures only.
- Knockdown visible: no. Each signature holds the 978 L1000 landmark genes; WWOX is not one, so the knockdown cannot be verified from the signature.
- Module genes: 1 of 6 present (BNIP3 -1.34, p 0.002, the opposite sign to the WWOX-loss build direction); the other five are not landmarks. No module test is possible.
- Specificity control (`lincs_kd_control.py`, first 40 other-gene NPC signatures by id, no choice by outcome): WWOX-NPC against WWOX in the 9 other cell lines has Spearman rho median 0.30 (-0.07 to 0.49); against other-gene NPC signatures median 0.24 (-0.51 to 0.75). 0 of 9 cross-cell values exceed the control maximum, 5 of 9 the control median. The similarity is a shared shRNA/cell-state axis, not a WWOX effect.
- Coverage (`lincs_kd_coverage.py`): of 23 panel genes (WWOX, module, axis and DEE genes) only 4 have an NPC knockdown signature: WWOX, NFE2L2, SLC2A1, BNIP3. No DEE channel gene (GRIN2A/B, KCNQ2, SCN1A/2A/8A, STXBP1, CDKL5, CACNA1G) is present.
- Observable value for the module today: none. Limits: one shRNA consensus per line, a control of 40 of 985 signatures, no replicates; phase II or a larger control could differ. Remove: delete this directory; nothing else was touched.

## Test 2 (gap c): literature-curated suppression table
`suppression_probe.py` on Data S2 (932 rows: 347 cell, 585 patient; 58 with a neural tissue label). Panel of 25 genes declared before the lookup (WWOX, its interactors, module/axis genes, DEE and channel genes). Result: 1 of 25 present, GRIN2A as a suppressor of HTT (3 patient rows). WWOX, GRIN2B, KCNQ2, SCN1A and the rest are absent. Observable value for this module: none. Remove: delete the directory (the 26 MB source zip stayed in the scratch area, sha256 6b96f580cdeb90aa8805075ed1baaa728f1e896a985a044eedf2a9468772fa67).

## Test 3 (gap e): one HPA call
WWOX is "cell type enhanced" (choroid plexus, ependymal cells, podocytes) and low-specificity in brain nuclei: the same picture as the existing cell-type census. Nothing new.

## Not tested, and why
PerturbAI: the gate needs an institutional e-mail, which this module never sends to a service, so the perturbed-gene list could not be read and WWOX membership is unknown. GLOW26 and the leakage benchmark: no link predictor is in use, so a test would measure nothing a decision rests on.

## Radar question list (implemented as a data edit of THEMES in `framework/scripts/scout_daily.py`, with a test)
THEMES is the fallback used when no plan can be derived; the derived plan (from the latest diagnosis directory) is unchanged.
- ADD `gene-knockdown-neural` (gap b): single-gene knockdown in human neural cells, Perturb-seq/CRISPRi; the measured coverage (4 of 23) is in the gap text so a later run can tell whether it improved.
- ADD `genetic-suppression-rescue` (gap c): suppressors and synthetic rescue of loss-of-function neurodevelopmental genes.
- REWORD `neuron-perturbation-signatures`: says LINCS phase I compound signatures are used and phase II is not.
- WIDEN `repurposing-benchmarks`: keyword now covers knowledge-graph link prediction, leakage and negative sampling (gap f); `repurposing-negative-results` stays as the counter-evidence slot.
- RETIRE `open-compound-resources`: three scouts (IT14, IT15, IT21) found nothing beyond ChEMBL/DGIdb/GtoPdb; the reopen conditions live in the IT15 and IT18 decision tables.
Balance: 11 questions before, 12 after. Known-project follow-up (isr-atf4-epilepsy, residual-function-chaperone, pdh-assay, sdr-enzyme-assay, dee-drug-response-data) is untouched. The test class `FallbackThemeList` (3 tests: shape and unique ids, the IT21 changes, at least 5 categories with negative results and experiments kept) was added to `test_scout_daily.py`; 74 tests pass.
