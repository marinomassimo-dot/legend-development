# E-06 sulfopin (Q6 expression, opposes; PIN1 -> MYC), mechanism probe

Scientist-b4, 2026-10-30. Not medical advice. Q6 MYC seed: WEAK-DIRECTION-ONLY; the seed assessment's first experiment is a MYC-specific graded lever, before any compound. Selected under amendment E1 as a `mechanism_probe`; AG-17724, BJP-06-005-3 and AG-122018 (same PIN1 cluster) are comparators and were not qualified.

## Decision (first)

**KEEP-AS-PROPOSAL (mechanistic experiment; conditional on the seed-valence experiment; not a treatment).** Biological promise (given only the WWOX-seed link and target action): LOW-MODERATE - PIN1 acts on MYC protein stability and activity and sulfopin lowers Myc target genes, but the MYC valence in the seed is unknown and the network's "transcriptional" PIN1 -> MYC label is a mode mislabel for the transcript seed. Depth MEDIUM; feasibility MEDIUM in vitro (a validated probe with an inactive control; supply UNVERIFIED), LOW clinically (no human exposure); priority LOW-MEDIUM (after the MYC-specific lever). The compound qualifies better than the other five as a probe because its target is selective, its engagement can be measured and a matched inactive analogue exists; this is a statement about probe quality, not about benefit.

## 1. Identity
ChEMBL CHEMBL5397880 (no preferred name), InChIKey NMHVAHHYKGXBMY-UHFFFAOYSA-N = PubChem CID 155804394 by InChIKey and by the name sulfopin; 2-chloro-N-(2,2-dimethylpropyl)-N-(1,1-dioxothiolan-3-yl)acetamide, C11H20ClNO3S (a chloroacetamide covalent warhead on a sulfolane). VERIFIED.

## 2. Target, action, measures (ChEMBL 12 rows, complete)
PIN1 (human, type B): Ki 17, and values up to 700 nM (3 rows, 3 documents; relation =), IC50 120 nM (2 rows, 1 document). No curated mechanism row. Primary paper (Dubiella 2021, PMC HTML, passages read): covalent on Cys113; fluorescence-polarisation apparent Ki 17 nM after 14 h; 1.4 A co-crystal structure; selectivity for Pin1 Cys113 by two chemoproteomic methods in two cell lines; cellular and in vivo target engagement by a competition pulldown (spleen, oral gavage 10-20 mg/kg); phenocopies Pin1 genetic knockout in cells. Alternative targets: none reported as dose-dependent in the chemoproteomic screens (as stated by the paper; the datasets were not opened).

## 3. Exposure and nervous-system data
Mouse: oral 10 mg/kg Cmax 11.5 uM, bioavailability 30% (3 mice); microsomal half-life 41 minutes; daily intraperitoneal 10-40 mg/kg for two weeks without adverse effects or weight loss (paper statement). **Brain or CSF concentration: not reported** in the passages read. No human exposure, no label, no registry entry.

## 4. Safety and counter-evidence
Negligible cytotoxicity across 275 cancer lines in 5 days (PRISM), growth effects only after 6-8 days; covalent chloroacetamides carry an off-target reactivity risk that the paper tests by chemoproteomics (low intrinsic reactivity). PIN1 is also a regulator of tau and other proteins; its role in radial glia is not established by anything read here. Seizure-provoking reports: none found. Neurodevelopmental toxicity: no datum.

## 5. Edge provenance (`edge_provenance_E.tsv`, rows 17-18)
* **PIN1 -T(+)-> MYC (CollecTRI/ExTRI2/GOA; ten references)**: titles and abstracts of all ten read; the full text of 32300594 read at passage level. They concern: MYC protein isomerisation at Pro63 after Ser62 phosphorylation and its effects on stability, DNA binding and nuclear-pore localisation (26655473 NMR, 32300594 review/perspective, 23318434 MYC and Abl); PIN1 and beta-catenin/FoxM1 (11533658, 26820938, 16428447); correlations of PIN1 with cyclin D1 in oral and lung cancer tissue (12792768, 12579289, 17275947); a genome-wide mRNA-level study (24416409). **None of the ten abstracts reports MYC mRNA after PIN1 manipulation.** Q-a NO for the transcript seed; Q-b NO (the quantity is MYC protein stability or activity); the v3 mode filter could not see this because the resource labels the record "transcriptional". A post-translational SIGNOR record PIN1 -> MYC (23716601) exists in live OmniPath but not in the committed SIGNOR export, so the protein-seed arm of the engine does not carry it.
* **Compound to readout (Dubiella 2021)**: in Mino B lymphoma cells sulfopin (1 uM, 6 h) lowers 206 genes enriched for Myc targets (RNA-seq); in MYCN-driven neuroblastoma (zebrafish, allografts, Th-MYCN mice) it reduces tumour progression and prolongs survival. Q-c PARTLY: Myc target genes, not MYC level, and MYCN not MYC, in neural-crest-derived tumours, not radial glia.

## 6. Target expression
Organoid KO/WT: PIN1 62.7/58.9/68.0/69.8 v 78.4/73.1 cpm (0.86); MYC 1.52; hNPC: PIN1 83.3 (hNSC), 93.1 (WWOX-deleted), neurons 53.6 and 22.8. HPA adult: PIN1 detected in all tissues and cell types at class level. The target is expressed in the relevant human neural systems.

## 7. Trials registry (2026-10-30)
sulfopin: 0 studies in every slice. Europe PMC "sulfopin AND (WWOX OR WOREE)": 0 hits (title/abstract/full-text index as served).

## 8. Experiment, readout, falsifier, transfer limits
In KO and patient-derived organoids at the window of the A51 test (week 8 to 15): sulfopin versus the matched inactive analogue Sulfopin-AcA (described in the paper) at concentrations that engage PIN1 in these cells (competition pulldown with the desthiobiotin probe), run beside the MYC-specific lever of the seed assessment (graded degron or OmoMYC) so that PIN1 is read as a second modality. Readouts: MYC+/SOX2+ fraction, MYC target signature by pseudobulk (not cell-level tests), pH3+ fraction of SOX2+, NEUN+ and SATB2+ fractions, PIN1 engagement. Adaptive versus harmful valence: if MYC+ cells and the MYC signature fall and neuronal fractions rise, the MYC rise is harmful; if neuronal output falls, the rise is compensatory. Falsifier: no change of the MYC+ fraction and signature at engaged concentrations (PIN1 is not a MYC lever here), or the specific lever shows no neuronal gain (the opposes reading itself drops). Transfer limits: PIN1 has many substrates, the readout is MYC activity rather than level, prenatal-equivalent window, no CNS exposure.

## UNVERIFIED
Sulfopin supply and the AcA control availability; PIN1 engagement concentration in neural cells; brain exposure; the chemoproteomic datasets; PIN1 in radial glia.
