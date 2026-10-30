# E-03 nirogacestat (Q6 expression, opposes; gamma-secretase -> NOTCH3 -> MYC)

Scientist-b4, 2026-10-30. Not medical advice. The Q6 MYC seed is WEAK-DIRECTION-ONLY (`../qualification_it9_p4b_c_20261030/seed_assessment_Q6_MYC.md`): direction of MYC (higher in WWOX-deficient radial glia) is supported, valence is not, so "opposes" and "mimics" stay conditional.

## Decision (first)

**DROP.** Decisive data: both records of the chain are family-level credits. (1) gamma-secretase -> NOTCH3 is a SIGNOR record on the four-subunit complex (APH1A_NCSTN_PSEN1_PSENEN) citing a review of gamma-secretase regulation in which the word NOTCH3 does not occur (0 occurrences in the full text). (2) NOTCH1_NOTCH3_RBPJ -> MYC cites Palomero 2006, a NOTCH1 paper in T-cell leukaemia that tests NOTCH1 only. In addition the drug is labelled for adults only, with epiphyseal disorder in paediatric patients with open growth plates, embryo-fetal toxicity, and no CNS datum. Biological promise LOW; depth MEDIUM-HIGH; feasibility MEDIUM-HIGH to obtain, LOW for a developing-brain system; priority none. This is "insufficient support", not "no activity": a gamma-secretase inhibitor does lower c-myc mRNA in Notch1-dependent T-ALL (another inhibitor, compound E).

## 1. Identity
ChEMBL CHEMBL1770916 (hydrobromide CHEMBL4298153), InChIKey VFCRKLWBYMDAED-REWPJTCUSA-N = PubChem by InChIKey and by names nirogacestat and PF-03084014. VERIFIED. First approval 2023.

## 2. Target, action, measures (ChEMBL 16 rows)
Curated mechanism: gamma-secretase inhibitor (CHEMBL2094135, complex APH1A/APH1B/NCSTN/PSEN1/PSEN2/PSENEN). IC50 1.2-6.2 nM (6 rows, 5 documents, binding assays), 19.15 nM (1 cell-based row); GSAP IC50 6.2 nM; HDAC6 % inhibition about 0 (2 rows). No row on a single presenilin, and no NOTCH3-specific datum: the compound inhibits the enzyme complex that cleaves all its substrates (APP, all Notch receptors, others).

## 3. Exposure and nervous-system data (openFDA label OGSIVEO, effective 2026-09-01; `exposure_E.tsv`)
Oral 150 mg twice daily; steady-state Cmax 508 ng/mL, AUC0-tau 3,370 ng.h/mL; bioavailability 19%; protein binding 99.6%; terminal half-life 23 hours; CYP3A4 85%. Indication: adults with progressing desmoid tumours. 8.4: safety and effectiveness not established in paediatric patients; epiphyseal disorder reported with open growth plates. No CSF or brain datum in the sections read.

## 4. Safety and counter-evidence
Label warnings: diarrhoea (84%), ovarian toxicity, hepatotoxicity, non-melanoma skin cancer, electrolyte abnormalities, hypersensitivity, embryo-fetal toxicity (rat embryo-fetal death below human exposure); headache 30% v 15%. openFDA: 838 reports, seizure terms 0 (404; counts, not incidence). Class evidence (abstract): the phase 3 trial of semagacestat, another gamma-secretase inhibitor, ended early with worse ADAS-cog and ADCS-ADL in the treated arms (23883379); a 2017 report calls semagacestat a pseudo-inhibitor, so it is a class signal, not a nirogacestat datum. Notch inhibition in neural progenitors promotes neuronal differentiation in the literature opened only as titles (Notch and neurogenesis review 2025), so for this seed it could be read either as favourable (fewer progenitors) or harmful (progenitor depletion): valence unknown.

## 5. Edge provenance (`edge_provenance_E.tsv`, rows 9-10)
* gamma-secretase complex -P(+)-> NOTCH3: reference 25610395 (review, full text fetched, passages searched): no NOTCH3; generic Notch cleavage; FAMILY_LEVEL_CREDIT. Q-a NO, Q-b not applicable.
* NOTCH1_NOTCH3_RBPJ -T(+)-> MYC: reference 16847353, **Palomero 2006, read from Abstract through Discussion (Methods and references not)**: Q-a NO (murine T6E T-ALL, five human Notch-dependent T-ALL lines, DN3 thymocytes; NOTCH1 only; NOTCH3 appears once, in a reference title); Q-b YES for NOTCH1 and the transcript seed (c-myc mRNA, nuclear run-on, ICN1 ChIP at a CSL site, cycloheximide-insensitive up-regulation); Q-c PARTLY (the gamma-secretase inhibitor compound E at 1 uM lowers c-myc mRNA in all five human T-ALL lines and T6E; nirogacestat not tested; not neural); Q-d PARTLY (organoid NOTCH1 1.28x, NOTCH3 1.29x, MYC 1.52x KO/WT; the paper shows c-myc is rescued in only 3 of 5 human lines: MYC is not the only target).
The MYC transcript edge therefore belongs to NOTCH1 in leukaemia, and NOTCH3's share is not tested anywhere in the chain.

## 6. Target expression
Organoid cpm (KO v WT): NOTCH1 369/483/405/394 v 307/339; NOTCH3 256-334 v 234/233; PSEN1 87-108 v 77/76; APH1A 155-186 v 186/184; NCSTN 160-203 v 147/141; RBPJ 58-88 v 97/83; HES1 63-81 v 60/50. hNPC (hNSC): NOTCH3 111, MYC 2.0 (WWOX-deleted hNSC: MYC 18.4, one library). HPA adult: PSEN1 enriched in oligodendrocytes (545 nCPM), NOTCH1 in astrocytes (77 nCPM); radial-glia class not given. Target and pathway are expressed.

## 7. Trials registry (2026-10-30)
Compound query 32 studies (30 listed); epilepsy/seizure 0, hypomyelination 0, neurodevelopment 0, WWOX 0, CNS tumour 0; paediatric terms 5 (desmoid tumours from 12 months in a phase 2; a compassionate-use protocol from 16 years). Two WWOX hits in Europe PMC are congress abstract books.

## 8. Experiment, readout, falsifier, transfer limits
No compound experiment. The class-level question (does Notch pathway inhibition lower MYC and raise NEUN+/SATB2+ fractions in KO radial glia?) is the MYC-specific-lever experiment of the seed assessment, and can be run with a genetic NOTCH1 or NOTCH3 or RBPJ reduction rather than a drug. Falsifier: MYC unchanged or neuronal fractions unchanged. Transfer limits: leukaemia records, adult-only drug, embryo-fetal toxicity, week-7-to-16 organoid phenotype versus postnatal treatment.

## UNVERIFIED
Nirogacestat CNS exposure; NOTCH3 protein in radial glia; the Notch-neurogenesis literature beyond titles; the sign of benefit of MYC reduction.
