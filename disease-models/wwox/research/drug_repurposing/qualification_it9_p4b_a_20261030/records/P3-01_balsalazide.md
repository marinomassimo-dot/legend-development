# P3-01 balsalazide: DROP (insufficient support at the declared target)

Scientist-a3, 2026-10-30. Not medical advice. A compatible action of a context-free network is not a predicted benefit.

**Proposal as generated (IT9 P3).** Q2 seed SLC2A1 transcript up (S017, two human neural systems, one method). Network path PPARG -> SLC2A1 (+1); compound action "mimics" (Z total -3.30, in-degree -3.03), conditional on the uncertain PDK1/PDHA1 seeds. PPARG is a hub (degree 209).

## 1 Identity
ChEMBL CHEMBL1201346, parent record, InChIKey IPOKCKJONYRRHP-FMQUCBEESA-N (E-azo; the marketed substance is the disodium salt). PubChem CID 54585 holds the stereo-free key IPOKCKJONYRRHP-UHFFFAOYSA-N: the first block (connectivity) is identical; the exact-key lookup returned 404, an expected consequence of the stereo block, logged in `service_log.tsv`. Active moiety: mesalamine (CHEMBL704), named as `active_chembl_id` in ChEMBL's hierarchy.

## 2 Target, action, measures
* Balsalazide: curated mechanism rows 0; activity rows 678 of 678 (complete). **PPARG: no row** (state NO_ROWS_FOR_THIS_TARGET, not a negative result). SIRT5 IC50 "=" 3,900 and 5,300 nM (human recombinant, fluorometric or HPLC assays, five documents CHEMBL4765439, CHEMBL4828753, CHEMBL5113501, CHEMBL5137064, CHEMBL5360531), 83 and 89 percent inhibition at 50 uM; a cell-lysate pull-down EC50 8,800 nM. COX-1 and COX-2 are DrugMatrix single-condition screens without a reported value (one COX-2 AC50 "> 30,000 nM").
* Mesalamine: three curated mechanisms (ALOX5 inhibitor, PPARG agonist, COX inhibitor) from references; 428 of 428 rows, **0 on PPARG**. The PPARG reference read at passage level (Rousseaux 2005, PMC2213148, open access): reporter activation and PPARG induction in HT-29 colonic epithelial cells with **5-ASA 30 mM**.
* Selectivity: the signed targets in the catalogue (ALOX5, PPARG, PTGS1, PTGS2, all from the mesalamine mechanism) are not properties of the dosed molecule.

## 3 Exposure and nervous system
Label (openFDA, effective 2025-02-18): prodrug released as 5-ASA by colonic azoreductases; fasting 2.25 g, n=17: balsalazide Cmax 0.51 ug/mL, 5-ASA 0.22 ug/mL, N-acetyl-5-ASA 0.88 ug/mL; protein binding of balsalazide at least 99 percent; urinary recovery of parent 0.1-0.2 percent. Paediatric: established 5-17 y for ulcerative colitis (PK study in 68 patients, abstract). No CSF or brain measurement found. Arithmetic (assumptions stated): 5-ASA 0.22 ug/mL / 153.1 g/mol = 1.4 uM total plasma, against 30 mM in the cited PPARG experiment, a ratio of about 2e4. For the parent: 0.51 ug/mL / 357.3 g/mol = 1.4 uM total, about 14 nM free at 99 percent binding, about 280 fold below the 3.9 uM SIRT5 IC50. This is arithmetic on different experiments, not a prediction.

## 4 Safety and counter-evidence
Label: seizures only under overdose (salicylate toxicity list). PubMed "balsalazide AND (seizure OR convulsion OR epilepsy)": 0 hits. openFDA spontaneous reports (counts, never rates, not comparable between drugs): 505 matched; seizure 5, convulsion 1, generalised tonic-clonic seizure 1. Neurodevelopmental toxicity: no source found.

## 5 Edge provenance
`edge_provenance_judged.tsv`: PPARG -> SLC2A1 is a CollecTRI (ExTRI text-mining) transcriptional record with ten itemised references from stem cells, adipocytes, endothelium, kidney, bone, mesothelium; none neural. The same network has PPARG -> PFKP with sign -1 (VSMC paper), so the hub points both ways within the glycolysis set. Defect that decides: the compound-to-target step belongs to the metabolite.

## 6 Expression
HPA adult brain snRNA: PPARG low cell-type specificity, detected in many (adult only, no developmental value claimed). WWOX-KO organoid bulk: PPARG 1.8-4.9 CPM (4 KO, 2 WT, descriptive); absent from the hNPC CAGE table (absent from a table is not zero expression).

## 7 Trials registry
ClinicalTrials.gov, 2026-10-30, intervention "balsalazide": 9 studies (ulcerative colitis and healthy volunteers); with each of epilepsy, seizure, developmental and epileptic encephalopathy, hypomyelination, neurodevelopmental disorder, intellectual disability, cerebral palsy: 0 (`trials_registry_search.tsv`).

## 8 Feasibility and decision
No verification experiment is recommended: the dosed molecule has no PPARG measure, the active species acts at millimolar in the one cited system, and systemic exposure is micromolar. Biological promise LOW; depth of evidence MEDIUM; feasibility LOW; priority NONE. This is "insufficient support", not "no activity". Limits on transfer: one transcript seed, two systems, one method, maturity confound (P1), organoid n=4 v 2.

UNVERIFIED: PPARG potency of 5-ASA beyond one paper (no activity row exists); brain 5-ASA concentration; the Rousseaux paper was read at passage level, not in full (no receipt staged).
