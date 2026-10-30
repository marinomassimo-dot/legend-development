# P3-04 ceperognastat: DROP of the generated proposal (edge defect), with class safety counter-evidence

Scientist-a3, 2026-10-30. Not medical advice.

**Proposal as generated.** Seed PFKP transcript up (S025, member of the glycolysis/lactate set, weight 1/sqrt n). Path OGA -> PFKP (+1); action "opposes" (Z total 6.42, in-degree 4.75, the highest of the group; seed-specific in both nulls). Identity was name-matched only (UNVERIFIED) in P3.

## 1 Identity (now verified by structure)
ChEMBL CHEMBL5095251 (preferred name CEPEROGNASTAT), InChIKey FRVXHWNHGWUTQO-CABZTGNLSA-N, C16H22FN5O3S. PubChem CID 135260636 is returned for that InChIKey, and for the names "ceperognastat" and "LY3372689"; the PubChem synonym list holds LY3372689 and LY-3372689. ChEMBL's molecule search returns the same record for "ceperognastat" and "LY3372689". The published discovery paper (PMID 39748851 abstract) states "ceperognastat (LY3372689)". Not independently checked: the WHO INN list structure (the name-to-structure link rests on the databases' depositors). Parent, no salt.

## 2 Target, action, measures
OGA (CHEMBL5921) IC50 2.36 nM, "=", human full-length N-terminal His-tagged enzyme expressed in baculovirus, preincubation 30 min (document CHEMBL5576136, 2024). This is the **only** ChEMBL row (1 of 1, complete); no curated mechanism, no selectivity row: selectivity UNKNOWN here (not "selective"). The catalogue's sign for OGA came from GtoPdb (-1).

## 3 Exposure and nervous system
Abstract of the discovery paper: oral, CNS-penetrant, more than 95 percent OGA enzyme occupancy in animal and human brain in phase 1 (PET ligand study NCT03944031 and NCT04392271 in healthy adults). Phase 1 safety in healthy adults: no serious adverse events after single and multiple doses (abstract). No paediatric datum; no label (investigational): the openFDA label query returned 404 (state recorded).

## 4 Safety and counter-evidence
* Phase 2 in early symptomatic Alzheimer disease (NCT05063539, JAMA 2026 abstract; 327 randomised): 3 mg arm progression ratio versus placebo 1.32 (credible interval 1.10-1.58), i.e. 32 percent greater; serious adverse events 26.4 percent (3 mg), 12.0 percent (0.75 mg), 15.7 percent (placebo).
* Acute synaptic effects: three structurally distinct OGA inhibitors, ceperognastat included, suppressed short- and long-term plasticity in mouse hippocampal slices (J Prev Alzheimers Dis 2026 abstract).
* Neurodevelopment: O-GlcNAc dyshomeostasis from a pathogenic OGT variant causes microcephaly, cortical dysplasia and hyperactivity in mouse (eLife 2026 abstract); partial rescue of homeostasis by reduced OGA activity in a second OGT model (eNeuro 2026 abstract). So O-GlcNAc balance matters for brain development in both directions; it does not make the WWOX-derived edge valid.
* Seizure-specific reports: none found.

## 5 Edge provenance (decisive)
OGA -> PFKP: SIGNOR, type post_translational, sign +1, reference PMID 26399441 (Nat Commun 2015). Full text (Europe PMC XML, PMC4598839) read at passage level: O-GlcNAcylation of PFK1 inhibits PFK1 enzyme activity and reroutes glucose to the pentose phosphate pathway; studied in A549 lung cancer cells with glycosylation-deficient PFKL/PFKP/PFKM mutants; the primary study (Science 2012, serine 529, hypoxia, cancer cells; abstract read) is cited there. The OGT -> PFKP (-1) record has the same reference; the OGA sign is its inversion. The record is about enzyme ACTIVITY after a protein modification; the seed is PFKP TRANSCRIPT, flat in the organoid (KO/WT CPM ratio 1.00; 98.6-104.3 in KO, 100.0-101.5 in WT). OGA's complete outgoing edge list in the network: G6PD, PFKM, PFKP, PFKL, all O-GlcNAc-on-enzyme. Under the pre-registered rule 2 (non-transcriptional record applied to a transcript seed and no alternative edge) this drops the proposal. It does not show that OGA inhibition cannot change glycolysis.

## 6 Expression
OGA (MGEA5): HPA adult brain snRNA low cell-type specificity, detected in all; organoid 120-210 CPM (KO 141-210, WT 120-133); hNPC TPM 14.7 (hNSC control), 11.0 (hNSC WWOX-del). OGT 69-119 CPM. PFKP broad.

## 7 Trials registry
2026-10-30: "ceperognastat" 0; "LY3372689" 6 studies (5 phase 1 healthy volunteers: NCT03819270, NCT03944031, NCT04106206, NCT04392271, NCT05749848; 1 phase 2 Alzheimer disease NCT05063539; all completed); 0 in epilepsy, seizure, DEE, hypomyelination, neurodevelopmental disorder, intellectual disability, cerebral palsy.

## 8 Decision
DROP of the WWOX-derived proposal: promise LOW; depth MEDIUM; feasibility LOW (investigational, programme reported negative, research supply UNVERIFIED); priority NONE. "Insufficient support", not "no activity": the compound is a potent, CNS-penetrant OGA inhibitor, and its counter-evidence (synaptic plasticity suppression, excess serious adverse events at 3 mg, neurodevelopmental sensitivity to O-GlcNAc balance) would in any case weigh against a paediatric DEE use. If O-GlcNAc balance is ever tested in a WWOX-deficient system, the premise must come from measured O-GlcNAc or OGT/OGA changes there, not from this edge.
UNVERIFIED: programme status; research availability; the JAMA, J Prev Alzheimers Dis and eLife papers were read at abstract level; the INN structure check above.
