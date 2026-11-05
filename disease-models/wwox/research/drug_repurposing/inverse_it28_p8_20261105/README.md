# IT28 P8 inverse test: tazemetostat and TMP269, reasons first, then what the generator did

Non-canonical research material, not medical advice. Forward rows were frozen BEFORE the reconstruction (`frozen/`, sha256 in `frozen_sha256.txt`; S8 and S9 rows). The reconstruction was made by a separate agent that was forbidden to open generation outputs, stage tables, alternatives, decomposition or verification files (`reconstruction/README.md`); it read at abstract level only and ChEMBL REST returned HTTP 500, so every anchor is abstract-level. A blind reconstruction by an agent in the same runtime and repository is not perfectly blind: it could have found these compounds elsewhere in the repo through search; it was told not to. The favourable-reason phase is diagnostic of capability; counter-evidence is kept, not cancelled.

Neither compound is a discovery test: both were already in the module. This is a diagnosis of what entered the calculation.

## Result
The agent found NO source linking either compound to a measured WWOX-deficient phenotype; every reason is inferred from another system, and several of the strongest literature signals are counter-reasons.

| # | Reason (agent) | Class | What the forward rows show |
|---|---|---|---|
| T1 | Potent, selective EZH2 inhibition (IC50 11 nM, PMID 23620515) | OMISSION until IT28, now CONSUMED | S8: attribution NOT_ASSESSABLE because GtoPdb ligand 7011 had no ChEMBL id and was never joined; S9: SINGLE_MEASURED_TARGET at 11 nM in both families (Q5, Q8) |
| T2, T3 | Oligodendrocyte and Schwann myelination need PRC2/EZH2 (counter-reasons) | CONSUMED as a carried limit (text), not as a computation | existing `class_limit target:EZH2` (IT22 dossier): dual EZH1/EZH2 blockers highest-risk for the myelin axis |
| T4 | Transient EZH2 inhibition after status epilepticus increased later seizure burden (rodent, PMID 31891591); a serious seizure event in one treated patient (PMID 33035459) | OMISSION (counter-reason) | absent from the row; closed in IT28 by a `class_limit target:EZH2` row (abstract level; direction for a developmental epilepsy unknown, not negative) |
| T6 | Brain exposure limited by P-gp (PMID 25868794) | DATA_MISSING | no exposure input exists; the existing limit names an efflux substrate only for the probe GSK343 |
| T7, T5 | Tumour-cell chromatin effects; zebrafish cerebellar progenitors | not applicable / REPRESENTATION_LIMIT | no cell-type or tumour context field |
| T8 | No WWOX-EZH2 link found by search | consistent | the chains are context-free regulatory edges (EZH2 to IL6, EZH2 to NFE2L2), both CONDITIONAL_H_HARM, qualified no |
| M1 | TMP269 class IIa selective (HDAC5 IC50 97 nM, PMID 23524983) | CONSUMED (ATTRIBUTABLE, 97 nM) | but hand-over blocked: `identity_not_resolved` (has_chembl 0); GtoPdb gives CHEMBL3110004 yet that record is absent from the local ChEMBL cache, so no route turns it into an identity |
| M2 | HDAC5 translocation, MEF2A and microglial hyperexcitability in mouse epilepsy models | REPRESENTATION_LIMIT | localisation is not a seed or edge type; direction for TMP269 unknown |
| M3, M4 | TMP269 acts on hippocampal HDAC5 and BDNF; neuroprotection in a rat model with peripheral dosing | DATA_MISSING | no exposure or pharmacodynamic input |
| M5 | HDAC4 and HDAC5 required for Schwann cell myelination (counter-reason) | OMISSION (counter-reason) | closed in IT28 by a `class_limit target:HDAC5` row |
| M6, M7 | HDAC4/5 up in human temporal lobe epilepsy tissue (association); HDAC5 inhibition causes iron-dependent ROS in cancer cells | OMISSION / not applicable | association and cancer context only; not carried |

## Reusable correction (kept because it works on a second case)
Counter-premises found by an independent reading can be carried through the existing decision-scope `class_limit` mechanism without a veto: EZH2 (T4) and HDAC5 (M5) are two different cases of the same omission class. Effect (`results_s9`): `carried_limits` change on proposals at EZH2 and HDAC5 (and the proposals whose chain passes the HDAC5 edge); eligibility 220 and the 15 hand-overs are unchanged. Nothing was promoted or removed. An explanation written after the compound was named is a retrospective reconstruction; the table says which reasons entered the calculation: T1 (since S9), T2/T3 (as text), M1.

## Open
The TMP269 identity (a GtoPdb-given ChEMBL id absent from the cache) needs a second-actor structure check before an R4-type row; that is held, not applied. Ordering of the hand-over is unchanged.
