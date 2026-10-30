# E-02 roxadustat (Q2 expression, mimics; EGLN2 -> FOXO3 -> SLC2A1/BNIP3)

Scientist-b4, 2026-10-30. Not medical advice. Q2 carries the IT7_READOUT6 guard; nothing here evaluates the compound by reversal of the six IT7 readout genes. "Mimics" means the compound pushes the seeds in the direction of the WWOX-deficient state; it is not a candidate treatment by construction.

## Decision (first)

**DROP (as a lever).** Decisive data: (a) the compound acts on the seed genes through HIF stabilisation (EGLN1 IC50 14-5740 nM in ChEMBL; no EGLN2 row at all), not through the proposed EGLN2 -> FOXO3 chain; (b) the chain's FOXO3 -> SLC2A1 reference states that FOXO3a REPRESSES HIF-1 activity at the Glut-1 promoter while the network sign is +; (c) EU label: seizures common (1.1% v 0.2% non-dialysis; 2.0% v 1.6% dialysis), caution in epilepsy, secondary hypothyroidism, paediatric use not established; ChEMBL EC50 12.9 nM (THRB) and 32.7 nM (THRA) and a 2025 report of thyroid-hormone-receptor activation at clinical concentrations; rat brain and hippocampal necrosis at about 3-6x the human AUC. Biological promise LOW; depth MEDIUM-HIGH; feasibility of obtaining the drug HIGH, safety-limited; priority of a next experiment on roxadustat: none. "Insufficient support" for the proposed chain, not "no activity": the drug is a potent prolyl hydroxylase inhibitor.

## 1. Identity
ChEMBL CHEMBL2338329 (first approval 2021), InChIKey YOZBGTLTNGAVFU-UHFFFAOYSA-N = PubChem by InChIKey and by the names roxadustat and FG-4592. VERIFIED.

## 2. Target, action, measures (ChEMBL, 62 activity rows, complete; `measures_by_target_type.tsv`)
Curated mechanism: HIF prolyl hydroxylase inhibitor (target record CHEMBL3831261, no name). Rows by target, assay type B, human: EGLN1 IC50 14-5,740 nM (16 rows, 15 documents), EGLN1 inhibition % 47-97 (4 rows with relation =), EGLN1 EC50 6,110 nM; EGLN3 inhibition % only (no relation = value); **EGLN2: no row**. Other 2-oxoglutarate oxygenases: FTO 9,800 nM; HIF1AN (FIH) IC50 greater than a limit (1 row, relation >); TET1-3 IC50 greater than limits and inhibition 25-44%; ASPH 19,400 nM; BBOX1 8,100 nM; KDM8 46,300 nM. Thyroid receptors: THRB EC50 12.9 nM, THRA EC50 32.7 nM (one document). Values are not pooled across types or units.

## 3. Exposure and nervous-system data
EU product information (EMA Evrenzo, PDF fetched 2026-10-30, sha256 88f6c6d4...; sections 4.2, 4.4, 4.6, 4.8, 5.2, 5.3 read): oral tablet; protein binding about 99%; volume of distribution 24 L; effective half-life about 15 hours; no brain-concentration datum; paediatric safety and efficacy not established ("no data are available"); contraindicated in the third trimester. Registry: paediatric CKD-anaemia studies from age 2 years exist (NCT05970172 active, NCT04925011 unknown status, NCT04621331 withdrawn); results not retrieved. Not FDA-approved: no openFDA label and no FAERS record (404; absent, not zero).

## 4. Safety and counter-evidence
Label: seizures reported as common in clinical studies (see Decision), "use with caution in patients with a history of seizures, epilepsy"; cerebral infarction, thromboembolic events, secondary hypothyroidism (reversible). Rat 26-week intermittent studies: brain necrosis and gliosis in one Sprague-Dawley animal at about 6x and brain/hippocampal necrosis in four Fischer rats at about 3-5x the human AUC; not in cynomolgus monkeys at up to about 2x. Thyromimetic action (Morita 2025, passages; molidustat, structurally dissimilar, did not activate the receptors in that report): thyroid hormone is central to brain development, so any neural-cell result with roxadustat has a confound. A single HIF-PH inhibitor class review hit, "HIF1 stabilization by roxadustat improves cognition and prevents neuron loss in Alzheimer's disease in vivo" (2026, title only), is not evidence for this question.

## 5. Edge provenance (`edge_provenance_E.tsv`, rows 5-8)
* **EGLN2 -P(-)-> FOXO3 (SIGNOR:24990963 = Zheng 2014; PMC full text, read from Abstract through Discussion; Methods partly; references not).** Q-a: the target is FOXO3a PROTEIN (hydroxylated at Pro426 and Pro437, USP9x binding blocked) in T47D and MCF-7 breast cancer cells, MEFs and mammary fat pad of Egln2-null mice; Foxo3a mRNA unchanged; no neural cell. Q-b: sign - and level protein match the edge as an edge; it says nothing about a seed transcript. Q-c: PARTLY: the prolyl hydroxylase inhibitors DMOG, DFO and CoCl2 raise FOXO3a; roxadustat not tested; the paper says the regulation is HIF-independent. Q-d: EGLN2 mRNA is expressed in the organoid (88-97 cpm KO, 103-104 WT, ratio 0.89); roxadustat has no EGLN2 potency row.
* **FOXO3 -T(+)-> SLC2A1 (CollecTRI, references 18268343 and 29301589).** Emerling 2008 (abstract): FOXO3a complexes with HIF-1alpha and p300 on the Glut-1 promoter and "negatively regulates HIF-1 transcriptional activity": **sign contradicted by the abstract**. The second reference is a forward genetic screen (title and abstract) with no SLC2A1 statement. Not read beyond abstracts.
* FOXO3 -T(+)-> BNIP3: muscle autophagy (2007) and cardiomyocyte atrophy (2013) abstracts; sign + non-neural.
* The direct route: **Bruick 2000 (full read)**: hypoxia mimetics (CoCl2, DFO) induce Nip3 and Glut-1 mRNA in CHO-K1; HIF-1alpha drives the Nip3 promoter. A prolyl hydroxylase inhibitor therefore reaches BNIP3 and SLC2A1 by HIF stabilisation: that is the disease direction in this system (organoid EPAS1 3.80x, HK2 4.73x, SLC2A1 2.67x KO/WT), so the "mimics" label is correct and the FOXO3 chain is not the mechanism.

## 6. Target expression
Organoid cpm KO v WT: EGLN1 0.87, EGLN2 0.89, EGLN3 1.82, FOXO3 1.19, EPAS1 3.80, THRA 0.74, THRB 1.00 (low, 2-4 cpm). hNPC CAGE: EGLN2 108 (hNSC), FOXO3 12. HPA class level: EGLN1-3, FOXO3 detected in all tissues; adult only.

## 7. Trials registry (ClinicalTrials.gov v2, 2026-10-30)
Compound query: 72 studies overall (30 listed); epilepsy/seizure 0, hypomyelination/leukodystrophy 0, neurodevelopment 0, WWOX 0, CNS tumour 0; paediatric terms 5 (renal anaemia, from 2 years). WWOX hits in Europe PMC for roxadustat are two congress abstract books (no relevant datum).

## 8. Experiment, readout, falsifier, transfer limits
No experiment on roxadustat. The question it stands for (does HIF stabilisation phenocopy the KO seed genes, and is HIF already saturated in KO?) is part of the E-01 experiment, using a prolyl hydroxylase inhibitor without thyromimetic action (molidustat per the 2025 report; to be verified before use) and genetic EGLN1/VHL loss. Valence discrimination there: if HIF stabilisation in WT reproduces the KO module and the effect is blunted in KO, the KO state is HIF-driven. Falsifier: no change of the module in WT cells. Transfer limits: roxadustat's thyromimetic and seizure signals, adult dosing, and the non-neural chain records.

## UNVERIFIED
Roxadustat EGLN2 potency; the second FOXO3 -> SLC2A1 reference; whether molidustat lacks thyromimetic action beyond the one report; brain exposure; paediatric trial results.
