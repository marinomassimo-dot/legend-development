# P4CD-05 gamcemetinib (Q4 expression, MAPKAPK2 -P-> CDC25A -P-> FOXO1 -T-> NPY, opposes): INCONCLUSIVE (leaning DROP; one local datum disfavours the chain)

Scientist-a4, 2026-10-30. Not medical advice. The Q4 list rests on 10 transcriptional edges and 2 seed genes in the network (weakest base, v3 README).

**Proposal as generated.** Seed NPY transcript down (S116: WWOX-knockout cerebral organoids weeks 8-15, deposited table, log2 -6.24, tier A human; mouse NPY-positive interneuron counts down in dentate gyrus, S066). Chain MAPKAPK2 -P(-)-> CDC25A [SIGNOR/SPIKE] -P(+)-> FOXO1 [SIGNOR] -T(+)-> NPY [CollecTRI/DoRothEA]; MK2 inhibition would raise NPY (opposes); z 5.0/4.0/3.4.

## 1 Identity
CHEMBL5314585, InChIKey PYOQIOLRFIRRSO-LLVKDONJSA-N; PubChem returns the same key by gamcemetinib and by CC-99677 and by key (synonym BMS-986371). The catalogue family was DGIdb-only (name-matched in the selection); now VERIFIED by structure (ChEMBL = PubChem key).

## 2 Target, action, measures
ChEMBL has no curated mechanism row (absent datum). Human MAPKAPK2 biochemical IC50: 4 rows, 156 to 300 nM, 3 documents (a covalent inhibitor; IC50 depends on incubation time, so the numbers are not potency constants). Published (35982464, open access, abstract): selective covalent MK2 inhibitor, reduces cytokine production in PBMC and macrophages; first-in-human in 37 healthy volunteers (details beyond the abstract not read).

## 3 Exposure and nervous system
Registered: 7 phase 1 studies in healthy adults (PK, 14C mass balance, DDI) and a phase 2 in ankylosing spondylitis (NCT04947579; published 2026, 147 subjects, abstract 42167889). No paediatric records; no CSF/brain datum (absent). Tolerability details beyond the abstracts were not extracted.

## 4 Safety and counter-evidence
Not extracted (no label). Seizure: Europe PMC 'CC-99677/MK2 inhibitor x seizure/epilepsy' 0 hits. Compound x WWOX: 0. MK2 inhibition in microglia lowers cytokines (PF-3644022 in N9 cells, abstract 39013758) and MK2 stabilises TNF mRNA by a post-transcriptional route (general mechanism; the network holds no MAPKAPK2 -> TNF record): an anti-inflammatory action unrelated to NPY.

## 5 Edge provenance (see edge_provenance_judged.tsv)
MAPKAPK2 -> CDC25A (15629715, 17292828: G2/M checkpoint phosphorylation in transformed cells, abstract); CDC25A -> FOXO1 (21670150: CDC25A stabilises FOXO1 through CDK2 in breast cancer cells, abstract); FOXO1 -> NPY (10 references, all hypothalamic: food intake, arcuate Foxo1, astrocytic Foxo1; abstracts): (a) YES at the terminal edge, (b) hypothalamic neurons and astrocytes, not hippocampal/cortical interneurons, (c) sign matches, (d) no report of MK2 inhibition changing NPY. The two P edges are cell-cycle/cancer records.

## 6 Expression and a local datum
Adult HPA (nCPM): NPY 212 in MGE interneurons (3 or less elsewhere in the brain table; 66 in inhibitory neurons in the single-cell table); in MGE interneurons MAPKAPK2 18, CDC25A 1.4, FOXO1 5.7, ETV1 36. Local WWOX-deficient organoid GSE156243 (4 KO, 2 WT; descriptive, library-size scaled): NPY 0.05 to 0.12 CPM in KO vs 3.2 and 7.7 in WT; CDC25A 13.5 to 19.4 in KO vs 10.3 and 11.7 in WT; FOXO1 3.1 to 5.4 in KO vs 1.4 and 2.5 in WT; MAPKAPK2 136 to 147 vs 149 and 157. hNPC (one library per arm): NPY and MAPKAPK2 ABSENT, CDC25A 22.6/5.9 TPM (NSC/neuron) and 40.0/3.3 (after WWOX deletion), FOXO1 14.8/0.5 and 23.6/0.8. Observation: in the KO organoid the two intermediates the chain would raise (CDC25A, FOXO1) are already higher than wild type while NPY is lower; with FOXO1 -> NPY positive, the chain's mediators do not explain the NPY loss (n 4 v 2 bulk libraries; no test).

## 7 Trials registry
Done: 7 hits all conditions, 0 in neuro slices, 0 paediatric.

## 8 Feasibility and limits
Experiment (if pursued): WWOX-deficient organoids or iPSC-derived MGE interneurons treated with gamcemetinib (covalent: washout control) and a reversible MK2 inhibitor; readouts CDC25A and FOXO1 protein, NPY transcript and peptide, interneuron count; control FOXO1 knockdown/overexpression. Falsifier: no rise of FOXO1 protein or NPY with MK2 inhibition, or NPY unaffected by FOXO1 manipulation in this system. Limits: five of the chain's nodes are low in postmitotic interneurons; seed is organoid transcript plus a mouse cell count.

## Decision and scores
**INCONCLUSIVE, leaning DROP.** Missing datum: any evidence that MK2 -> CDC25A -> FOXO1 operates in postmitotic NPY neurons or that FOXO1 drives NPY in this WWOX-deficient system; the KO organoid pattern (FOXO1 and CDC25A up, NPY down) would turn this into a DROP if reproduced in an independent dataset. Not a DROP now: no pre-registered DROP condition (R1, R3, N2) is met. Promise LOW; depth LOW-MEDIUM; feasibility MEDIUM (human PK exists, access UNVERIFIED); priority LOW.
