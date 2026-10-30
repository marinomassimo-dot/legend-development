# P4CD-06 ceralasertib (Q4 expression, ATR -P-> ETV1 -T-> GRIN2C, mimics): DROP (safety-genetics and cancer-line edge; judgment beyond the pre-registered conditions)

Scientist-a4, 2026-10-30. Not medical advice. The 'mimics' arm means ATR inhibition would push GRIN2C in the direction of the Wwox-deficient datum (down).

**Proposal as generated.** Seed GRIN2C transcript down (S129: Wwox-null hippocampus and hippocampal neurosphere NSCs, tier B). Chain ATR -P(+)-> ETV1 [SIGNOR] -T(+)-> GRIN2C [CollecTRI/NTNU]; z -15.8/-4.8/-4.6.

## 1 Identity
CHEMBL4285417, InChIKey OHUHVTCQTUDPIJ-JYCIKRDWSA-N; PubChem 'ceralasertib' returns the same connectivity (CID 54761306). NOTE: PubChem name search for the code name 'AZD6738' returns a different record (CID 121596701, InChIKey DTTJKLNXNZAVSM-JYCIKRDWSA-N, IUPAC with a pyrrolo[2,3-c]pyridine ring instead of the [2,3-b] ring): a name-resolved identity is unsafe for this alias; the ChEMBL structure and the PubChem InChIKey lookup agree, so the compound itself is VERIFIED by key and the alias collision is recorded.

## 2 Target, action, measures
Curated: ATR kinase inhibitor. Human biochemical IC50 for ATR: 9 rows, 1 to 180 nM (6 documents), Ki 0.06 nM (1 row), ATR/ATRIP 14 nM; selectivity rows: MTOR 370 to 5,700 nM, PRKDC 7,400 nM, ATM and PIK3CA '>' values. The oral compound is a cell-cycle (checkpoint) kinase inhibitor.

## 3 Exposure and nervous system
Oncology trials only (48 registered; the paediatric-term slice returns osteosarcoma 12-40 y, a paediatric cancer platform, a gemcitabine combination). No label. Mouse tissue distribution study exists (35066692, abstract: dose-dependent bioavailability, tissue distribution in tumour-bearing mice; brain not extracted); a brain-penetrant ATR inhibitor was developed because AZD6738 permeates less (39053006, abstract, a competitor's claim). No CSF datum.

## 4 Safety and counter-evidence
Neurodevelopment: hypomorphic ATR (and ATRIP) mutations cause Seckel syndrome with severe microcephaly; in human iPSC-derived neural progenitors the ATR splice defect impairs the replication-stress response (30846821, abstract) and Atrip deficiency in retinal progenitors causes lamination defects and degeneration (32994318, abstract). ATR inhibition is cytostatic/cytotoxic to dividing cells (ATR inhibitor trials in haematologic malignancy, abstracts); haematologic toxicity is general knowledge, UNVERIFIED here. Europe PMC 'ATR inhibitor x seizure/epilepsy' 1 hit (not opened). Compound x WWOX 0.

## 5 Edge provenance (see edge_provenance_judged.tsv)
ATR -> ETV1: ATR phosphorylates and stabilises ETV1 in p53-deficient human cancer lines (23284306, abstract; PMC text downloaded, not read): (a) not transcriptional (protein stability), (b) cancer lines, (c) consistent sign, (d) not shown in any neural cell. ETV1 -> GRIN2C (22586091, 21746923, abstracts): Etv1 binds the NR2C promoter and is required for BDNF- and activity-induced NR2C expression in cultured mouse cerebellar granule neurons: (a) YES, (b) a neuron type, (c) sign matches, (d) no ATR link. So the terminal edge is neural and valid; the first edge is a cancer-line record.

## 6 Expression (adult HPA, nCPM; local)
ATR 66 to 196 everywhere (ubiquitous). ETV1: excitatory neurons 321 (upper layer), 258 (single-cell excitatory), astrocyte 91, MGE interneuron 36. GRIN2C: astrocyte 133, Bergmann glia 61, excitatory neurons 1 to 3 (hippocampal dentate gyrus 1.0). Organoid: GRIN2C 1.1 to 6.3 CPM (KO ratio 1.84, low counts), ETV1 KO 0.67 x WT; hNPC GRIN2C ABSENT. The mouse seed (down) is not reproduced in the human organoid (GRIN2C if anything higher). Developmental expression not retrieved.

## 7 Trials registry
Done: 48 oncology records; 0 in epilepsy, hypomyelination, neurodevelopment, neuroinflammation, WWOX.

## 8 Feasibility and limits
No experiment is recommended. A mimic of GRIN2C loss is not a rescue lever, the compound is an antiproliferative oncology agent, and the genetics of ATR hypofunction is itself a neurodevelopmental disorder.

## Decision and scores
**DROP** (decisive datum: ATR hypofunction causes microcephaly in humans (Seckel), so ATR inhibition during neurodevelopment is the phenocopy of a neurodevelopmental disease, while the proposal's first edge is a cancer-line stability record and the seed (GRIN2C down) is not reproduced in the human organoid). Basis note: this DROP rests on safety genetics plus edge provenance, not on a pre-registered DROP condition (R1, R3, N2 were not met); I label it as a judgment. Promise LOW; depth MEDIUM-LOW; feasibility LOW for any neural use; priority none.
