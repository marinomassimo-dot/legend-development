# P4CD-04 dimethyl fumarate (Q5 expression, KEAP1 -P-> RBX1 -P-> NFKBIB -T-> TNF, mimics): DROP of the generated proposal (artefact chain; direction contradicted by the literature)

Scientist-a4, 2026-10-30. Not medical advice. This is a DROP of the proposal chain, not a statement about dimethyl fumarate in general.

**Proposal as generated.** Seeds TNF and IL6 transcripts up (S085, S086; Wwox-null hippocampus). Chain KEAP1 -P(+)-> RBX1 [SIGNOR] -P(-)-> NFKBIB [SIGNOR] -T(+)-> TNF [CollecTRI]; the engine reads DMF as a KEAP1 inhibitor whose net action on TNF has the same direction as the seed (arm 'mimics', TNF up); z -9.3 / -11.0 / -8.9. Selected by the ordering rule (tie with diroximel fumarate resolved by the written tie-break; see SELECTION_NOTE 2.4).

## 1 Identity and active moiety
Dimethyl fumarate CHEMBL2107333, InChIKey LDCRTTXIJACKKU-ONEGZZNKSA-N (PubChem by name, BG-12 and key agree), VERIFIED. Label: after oral dosing DMF is not quantifiable in plasma; the active species is monomethyl fumarate (CHEMBL589586, NKHAVTQWNUWKEO-NSCUHMNNSA-N, verified); ChEMBL's prodrug flag is not set for DMF, so the v3 prodrug filter did not catch it (a gap for the engine's F3).

## 2 Target, action, measures
Curated: KEAP1 inhibitor (DMF and MMF). ChEMBL human measures (not pooled): KEAP1/NRF2 cell assay EC50 5,110 nM (1 row, 1 document, DMF); HCAR2 (GPR109A, the other known MMF receptor) functional IC50 130 nM (DMF, 1 row) and 0.96 nM (MMF, functional) with MMF Ki 180 nM (binding). KEAP1 covalent modification is not captured by IC50 rows.

## 3 Exposure and nervous system
openFDA label (set of 10 labels, most complete used, 2021-07): MMF median Tmax 2 to 2.5 h; Cmax 1.87 mg/L (about 14 uM from the molecular mass) and AUC 8.21 mg h/L at 240 mg twice daily with food; Vd 53 to 73 L; protein binding 27 to 45 percent; paediatric use 'not established' in the label, but paediatric studies in ages 10 to 17 years are registered (NCT02283853 phase 3 completed, NCT02410200 phase 2 completed, NCT02555215 extension, a recent phase 3 not yet recruiting). CSF/brain concentration: not retrieved (a nose-to-brain formulation paper exists; no human CSF datum found): UNVERIFIED.

## 4 Safety and counter-evidence
Label warnings: anaphylaxis/angioedema, progressive multifocal leukoencephalopathy, herpes zoster and opportunistic infections, lymphopenia, liver injury; the 13 sections fetched contain no 'seizure/convulsion/epilepsy' string. Seizure literature: DMF is reported antiepileptogenic and disease-modifying in a kainate rat model (37940957, abstract) and anti-seizure/antioxidant in PTZ-kindled mice (38583440, title only); Europe PMC DMF x seizure 15 hits (not all opened). Direction contradicted by literature: DMF lowered IL-1b and TNF and microglial/astrocytic activation in two mouse neuroinflammation models (38897132, 35665831, abstracts); NRF2 is a repressor of IL1B/IL6 transcription in the network itself (NFE2L2 -T(-)-> IL1B/IL6; 63 and 76 curation-effort records).

## 5 Edge provenance (decisive; see edge_provenance_judged.tsv and edge_records_complex.tsv)
The two P edges are SIGNOR complex-level records: KEAP1 -> CUL3_RBX1_SKP1 (SIGNOR:17046835, PGAM5 as a KEAP1-CUL3 substrate; the node includes SKP1, which is not a CRL3 subunit) and CUL1_RBX1_SKP1 -> NFKBIB (SIGNOR:10514424, beta-TrCP ubiquitination of IkBb by SCF). The engine splits complexes into members and the two records meet only at the shared members RBX1 (and SKP1): two different E3 ligases joined by member sharing. The chain KEAP1 -> RBX1 -> NFKBIB therefore does not describe a mechanism (a new defect type for the v3 filters, the complex-join artefact). The terminal edge NFKBIB -> TNF is a valid macrophage record (IkBb-null mice lose LPS-induced TNF; 20740013, keyword check of the PMC text: no brain or microglia; sign +). Edge reading is abstract level for the P edges (neither paper in PMC).

## 6 Expression (adult HPA)
KEAP1 6 to 28 nCPM (oligodendrocyte 28); NFE2L2 25 to 260 (CNS macrophage 260, astrocyte 153); NFKBIB 4 to 17; HCAR2 about 0 in all brain cell types and microglia (0.0), 10 in macrophages, 19.5 in monocytes. TNF/IL6/IL1B in CNS macrophage only. Organoid: KEAP1 about 60 to 70 CPM, 0.93 x. HCAR2 was not in the local datasets queried.

## 7 Trials registry
DMF x 7 slices: 0 in epilepsy, hypomyelination, neurodevelopment, WWOX; 109 in the multiple sclerosis/neuroinflammation slice (30 listed); 14 paediatric-term records.

## 8 Feasibility and limits
No experiment is proposed for this chain. DMF's real mechanism (KEAP1/NRF2 and HCAR2) belongs to a separate, class-level question: NRF2 activators in neuroinflammation (omaveloxolone is the approved neurological member, first not-taken eligible cluster of this round) and is not derived from the WWOX seeds through this chain.

## Decision and scores
**DROP** of the generated proposal. Decisive datum: the chain is joined across two different E3 ligase complexes through RBX1/SKP1 member sharing (SIGNOR:17046835 vs SIGNOR:10514424), and the 'mimics' direction (DMF raises TNF) is contradicted by published in-vivo microglia/astrocyte data. Basis note: the complex-join defect was not in the pre-registered N2 list; I applied it as a defect of mode type (a record that does not exist as a connected path) and disclose it as an addition. Promise (WWOX seed + target action): LOW; depth MEDIUM; feasibility HIGH (approved oral drug) but not applicable; priority none.
