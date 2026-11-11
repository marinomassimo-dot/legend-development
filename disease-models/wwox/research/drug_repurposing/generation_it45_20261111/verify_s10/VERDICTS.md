# IT45 independent reader: S10 (KEAP1/NRF2) primary documents, verdicts

Reader: one delegate (sonnet, high effort), 2026-11-11. Not medical advice. No compound is recommended here.
Forbidden inputs (generation_it43, pointers_it44.tsv, any verdict or engine output) were not opened.

## 0. What was actually reached (read this first)

Source tiers are stated in every cell: **[FT]** = full text read; **[AB]** = PubMed abstract only; **[CH]** = ChEMBL curated record of the paper (a secondary, human-curated transcription of the paper's tables and assay descriptions, obtained from the public ChEMBL API; it is a pointer, not the paper, and I did not see the paper's own words behind it).

| PMID | Reached | How | Not reached |
|---|---|---|---|
| 38116420 | [FT] main text, Table 1 and Figure 2 read from the published images | PMC10726478 HTML + the table/figure JPEGs | Supporting Information (the PMC SI download is a proof-of-work interstitial, not solved; the ACS SI link returned HTTP 403) |
| 31411465 | [FT] complete accepted-manuscript text (Table 1, Figs 1-7, Results, Discussion, Experimental), HAL Rennes deposit | `univ-rennes.hal.science/hal-02474013v1/document` (page numbers are the manuscript's, not the journal's; I cite section/Table/Figure) | its Supporting Information |
| 21964340 | [FT] PMC author-manuscript main text, figure legends, Methods summary | PMC efetch XML + PubMed MCP full text | all supplementary files (Suppl Info Doc, data set 1, tables 1-8): PMC download pages are proof-of-work gated; Europe PMC says "not open access" |
| 37187090 | [AB] + [CH] | PubMed abstract; ChEMBL document CHEMBL5370549 | full text (ScienceDirect HTTP 403; Elsevier API returned metadata only). Europe PMC/Unpaywall list it as CC BY but the page is not retrievable without spoofing a browser, so NOT_REACHED |
| 27031670 | [AB] + [CH] | PubMed abstract; ChEMBL document CHEMBL3817762 | full text (closed access; ACS 403) |
| 28753294 | [AB] + [CH] | PubMed abstract; ChEMBL document CHEMBL4190292 | full text |
| 37386884 | [AB] + [CH] | PubMed abstract; ChEMBL document CHEMBL5334942 ff. | full text |
| 39241669 (review) | reference list only | Europe PMC `references` endpoint (237 entries, bibliographic metadata) | the review's text, including the sentence that cites halofuginone |
| 28039084, 34628069, 35618180 (the halofuginone primaries cited by 39241669) | [AB] only | PubMed | full texts (all closed or 403) |

Anything marked [CH] must be re-checked against the paper before it is quoted as the paper's words.

---

## Q1. 37187090 and 38116420: the Nrf2 assays

### 37187090 (Kim et al., Eur J Med Chem 2023; pyridinyl vinyl sulfones)

| Item | Verdict | Words relied on (locator) |
|---|---|---|
| Cell system and readout of the Nrf2 assay | SUPPORTED as [CH] only; NOT_REACHED in the paper | ChEMBL assay CHEMBL5371746: "Activation of Nrf2 in human U2OS cells co-expressing Keap1 assessed as induction of Nrf2 nuclear translocation incubated for 6 hrs by PathHunter chemiluminescence based analysis". Abstract [AB]: "approximately 16-folds higher Nrf2 activating effects than VEDA-1209 (10e: EC = 37.9 nM vs VEDA-1209: EC = 625 nM) in functional cell-based assay" |
| Incubation time | SUPPORTED as [CH] only | "incubated for 6 hrs" (same ChEMBL assay line). Paper text NOT_REACHED |
| Concentration range tested | NOT_REACHED | neither the abstract nor the ChEMBL descriptions state it for the translocation assay |
| Sulforaphane | SUPPORTED as [CH] only | ChEMBL: SULFORAPHANE EC50 = 879 nM (published unit 0.879 uM) |
| Dimethyl fumarate | SUPPORTED as [CH] only | ChEMBL: DIMETHYL FUMARATE EC50 = 5114 nM (0.005114 mM; published 5.114 uM) |
| Monomethyl fumarate | SUPPORTED as [CH] only, with a relation sign | ChEMBL: MONOMETHYL FUMARATE EC50 > 10000 nM (published "> 10.0 uM"); i.e. no EC50 reached, a floor set by the top concentration |
| Cross-check of the abstract with the curated table | CORRECTED (small) | Abstract: 10e "EC = 37.9 nM"; ChEMBL row for the same structure (3-chloropyridin-2-yl, 3-methoxypyridin-2-yl sulfone) lists 37.0 nM. VEDA-1209 625 nM agrees. One of the two is a transcription difference; the paper's table was not reached |
| NRF2 dependence of the readout shown (knockdown, inhibitor, KEAP1 mutant) | NOT_STATED in what I reached | no abstract sentence and no ChEMBL assay line describes a knockdown, an inhibitor arm or a KEAP1 mutant. The assay is a reporter built on Nrf2/Keap1 (U2OS "co-expressing Keap1") so the readout is Nrf2-tagged by construction, but whether the authors also test dependence is NOT_REACHED |
| Cell viability remark | SUPPORTED as [CH] only | ChEMBL CHEMBL5371756: "Cytotoxicity against mouse BV-2 cells assessed as effect on cell viability upto 3 uM incubated for 24 hrs by WST assay". The Nrf2/inflammation assays in BV-2 (immunoblot 3 h to 48 h; LPS pretreatment 6 h then 6 or 24 h) are all at or below 3 uM in the curated lines |

### 38116420 (Markovtsov et al., ACS Med Chem Lett 2023; Rigel)

| Item | Verdict | Words relied on (locator) |
|---|---|---|
| Cell systems | SUPPORTED [FT] | Results para 5: "profiled in our cellular assay screening for inhibition of IL-23 in response to LPS ... The compounds were screened initially in both the reported dendritic cells and THP-1 monocytes ... the THP-1 cell line being more sensitive". "the analogues were profiled in an Nrf2 translocation assay, 15" (method details deferred to Supporting Information, NOT_REACHED). Mechanism: "investigate the mechanistic effects of compounds 9, 13, 17, and 1 in THP-1 cells, probing Nrf2 activation and expression of the antioxidant enzyme HO-1"; "three-way nuclei staining of HUVEC cells". ChEMBL [CH] names the translocation assay "human PathHunter U2OS Keap1-Nrf2 cells ... chemiluminescent assay" |
| Readout | SUPPORTED [FT] | Table 1 column "Nrf2 Translocation EC50 (uM)"; Figure 2a western blots of Nrf2 and HO-1 (THP-1); Figure 2b imaging of p65, Nrf2, DAPI (HUVEC) |
| Incubation time | NOT_STATED in the main text for the translocation assay and the THP-1 westerns | the Methods are in the SI (NOT_REACHED). [CH]: HUVEC "preincubated for 5 hrs followed by TNF-alpha stimulation and measured after 1 hr" |
| Concentration range | SUPPORTED [FT] (figure labels) | Figure 2a lanes: compound 13 at 10, 2.0, 0.4, 0.08 uM; 9 at 50, 10, 2.0, 0.4 uM; 17 at 10, 2.0, 0.4, 0.08 uM; DMF at 10, 2.0, 0.4, 0.08 uM. Figure 2b rows (Conc, uM): 10.0, 3.33, 1.11, 0.37, 0.12, 0.04 |
| Sulforaphane value | NOT_STATED | the only mention is introduction text: "the sulforaphanes found in cruciferous vegetables"; no number anywhere in the main text or tables. Do not attribute a sulforaphane value to this paper |
| DMF value | SUPPORTED [FT] (Table 1, read from the image; cross-checked with [CH]: 7930 nM) | DMF (compound 1): IL-23 IC50 10.60 uM; Nrf2 Translocation EC50 7.93 uM; Niacin IC50 130 nM. Printed without a relation sign |
| MMF value | SUPPORTED [FT] (Table 1; [CH] agrees: 127200 nM) | MMF (compound 2): IL-23 IC50 18.89 uM; Nrf2 Translocation EC50 127.2 uM; Niacin IC50 0.96 nM. Printed without a relation sign |
| Compare with 37187090 | CORRECTED (do not mix) | the same molecules in the same type of cell reporter give DMF 7.93 uM here and 5.114 uM [CH] there, MMF 127.2 uM here and "> 10 uM" [CH] there. Values from the two papers are not interchangeable |
| NRF2 dependence of the readout | NOT_STATED (only assumed) | no knockdown, knockout or KEAP1 mutant. The only control is an IKK inhibitor: "Analyzing for nuclear Nrf2 shows concentration dependent levels with the compounds and no nuclear Nrf2 with the IKK inhibitor". That shows the inhibitor does not give the nuclear signal; it does not show that the compounds' effect needs Nrf2. The Keap1 link is biochemical: "several cysteine residues of purified Keap1 were modified after incubation with 13 (see Supporting Information for details)". The introduction cites "Nrf2 -/- animals resulted in a more severe clinical course" for MS models (literature, not tested here). The paper itself states a separate route: "While cytokine inhibition may be linked to Nrf2, there appears to be an independent pathway for inhibition of TLR signaling through inhibition of the NFkB and ERK1/2 activation" (Introduction) |
| Cell-viability remark | SUPPORTED [FT] | "DAPI staining confirms the cells are viable (Figure 2b ...)"; "in our assay of cell toxicity, 17 was found to be inactive, while 13 showed weak activity in both cell lines (A549 = 8.81 uM, H1299 = 2.32 uM)"; abstract: 17 "is not cytotoxic to cells". Note: the cytotoxicity cell lines are two lung cancer lines, not the Nrf2 assay cells |

---

## Q2. 31411465 (Tran et al., J Med Chem 2019) and 27031670 (Davies et al., J Med Chem 2016)

### 31411465 [FT]

Identification: Figure 1 legend: "9: Davies et al.27" and reference 27 is 27031670. So the Davies/Astex-GSK compound is compound **9** in Tran.

| Item | Verdict | Words relied on (locator) |
|---|---|---|
| Compounds compared in one assay format | SUPPORTED | Results, "Selection and synthesis": "a total list of 21 compounds (Figure 1A)", all run in FP (Cy5-Nrf2 probe, "Keap1 (14 nM) / Cy5-Nrf2 ... (3 nM)", 4% DMSO, 8% for 12-21), TSA and SPR, and an NQO1 cell assay; abstract: "the first side-by-side assessment of all reported Keap1-Nrf2 PPI inhibitor classes" |
| KEAP1 binding values as printed | SUPPORTED | Table 1 columns FP Ki (uM), TSA EC50 (uM), TSA dTm-max (C), SPR Kd (uM). Peptides: 1 Ki 0.54, Kd 4.2; 2 Ki 0.051, Kd 0.74. Compound 3 Ki 0.56, Kd 2.4. 4 Ki 0.25, Kd 0.37. 5 Ki 0.0061, Kd 0.32. 6 Ki 0.053, Kd 0.19 (two measurements). 7 Ki 0.048, Kd 0.47. 8 Ki 0.0021, Kd 0.026 (one measurement, kinetic fit). **9 Ki ~0.001 (footnote b: "affinity was too high to calculate an exact Ki, but IC50 value was 0.008 uM"), TSA EC50 1.9, dTm 25 C, SPR Kd 0.0014 (one measurement, kinetic 1:1 fit)**. 10 Ki 0.013, Kd 0.019. 11 Ki 2.8, Kd 51. Compounds 12-21: "NA" (no activity) in FP/TSA/SPR, with 19 ~280 and 20 ~71 uM in FP and "> 120 to > 500" SPR flags |
| Any of them shows NRF2-pathway activation in cells; which cell type | SUPPORTED, with limits | Results, "Cell activity in NQO1 induction assay": "induce NQO1 enzyme activity at varying concentrations (1, 5, and 10 uM) in Hepa1c1c7 murine hepatoma cells using sulforaphane (SFN) as a positive control"; Experimental: cells "incubated for an additional 24 h". "Compounds 7-10 were among the strongest binding ligands ... and were also potent NQO1 inducers, comparable to or exceeding SFN". Compound 6 and 11 did not induce; peptides 1, 2 inactive. **Readout is NQO1 enzyme activity only, not Nrf2 translocation, not Nrf2 knockdown**: Discussion: "The NQO1 induction assay ... is prone to give positive readouts that are not a consequence of engagement with the target of interest; e.g. progesterone is known to upregulate NQO1 without activating the Nrf2 pathway". Three compounds induced NQO1 without any Kelch binding: "compounds able to induce NQO1 in the cell do not necessarily show binding to the Keap1 Kelch domain (as seen for 12, 13, and 16)"; 13 "reacted with the Keap1 Kelch domain, presumably at the cysteine side chains" |
| Permeability remark | SUPPORTED | "The peptide controls 1 and 2 were inactive, likely because of the inherently limited physicochemical properties of peptides for permeating biological membranes". For 6: "lower cLogP and higher polar surface area ... might decrease its passive diffusion across the cell membrane". Introduction: "bulky ligands featuring carboxylic acids ... generally result in poor cell permeability and might explain the discrepancy between binding affinity and cell activity observed for e.g. compound 5.22, 27"; "The CNS permeability has been experimentally tested on a few Keap1 inhibitors (3 and 13) but with discouraging results". No permeability measurement for 9 itself |
| Binding mode | SUPPORTED | Abstract "non-covalent"; Discussion: "Compounds 3-11 are all well-characterized ... we confirm that they are genuine reversible binders of the Keap1 Kelch domain". Counter-assays: "Compounds 5 and 7-10 are all high-affinity and cell active compounds without any apparent chemical liabilities, such as covalent binding, redox activity, or aggregation". Exceptions: 11 shows adducts "at 800 uM" only; 13 and 20 react with thiols. SFN (positive control for covalent reactivity) "was not active in the FP assay ... demonstrating that this assay is generally not sensitive to covalent modifiers" |
| Authors' view of the compound set | note | "Based on our data, we question the legitimacy of a substantial proportion of the compounds (12-21) described in the literature" |

### 27031670 [AB] + [CH]

| Item | Verdict | Words relied on |
|---|---|---|
| Binding mode (covalent or not) | SUPPORTED [AB] | Abstract: "Pharmacological intervention has focused on molecules that decrease NRF2-ubiquitination through covalent modification of KEAP1 cysteine residues, but such electrophilic compounds lack selectivity ... We report here the first use of a fragment-based approach to directly target the KEAP1 Kelch-NRF2 interaction". The lead is a monoacid (title). Not covalent per the abstract |
| KEAP1 binding values | SUPPORTED as [CH] only; paper NOT_REACHED | ChEMBL (lead CHEMBL3819587): "Binding affinity to human recombinant N-terminal His6 and Avi-tagged KEAP1 (321 to 609 residues) ... by isothermal titration calorimetry": Kd = 1.3 nM. Comparators in the same ITC assay: Kd 670 nM, 4000 nM, 59000 nM. FP displacement of "5'-TAMRA-NRF2 peptide" (1 h): IC50 270 nM, 3400 nM, 61000 nM, "> 1000000 nM" for four other compounds; the lead's own FP row is an "Inhibition = 95.0 %" entry (assay "at 15 nM ... relative to control"; I could not tell from the curated line whether 15 nM is probe, protein or compound). Tran (above) independently reports compound 9 SPR Kd 0.0014 uM, FP Ki ~0.001 uM |
| Pathway activation in cells and cell type | SUPPORTED as [CH] only | all human bronchial epithelial: "NHBE cells", "human BEAS2B cells", "human bronchial epithelial cells from COPD patient". mRNA (6 h, RT-PCR): NQO1 EC50 22 nM, HO-1 16 nM, GCLM 36 nM, TXNRD1 27 nM; BEAS2B NQO1 enzyme activity (48 h) EC50 12 nM. Abstract: "activates the NRF2 antioxidant response in cellular and in vivo models" (rat lung, iv, [CH]: GCLC, GSTA3, SRXN1, TXNRD1, HO-1, NQO1 mRNA fold changes 13, 15, 28, 9, 17, 37 at 50 umol/kg) |
| NRF2 dependence | PARTLY SUPPORTED as [CH] | ChEMBL lists NQO1/GCLM mRNA and NQO1 activity assays "in presence of non targeting siRNA" and "in presence of NRF2 siRNA" in NHBE cells (1 uM, 24 h or 48 h). The curated entry for the non-targeting-siRNA activity arm is FC = 6.0; the NRF2-siRNA arms are "Inhibition" entries without a retrievable number. So an NRF2 knockdown control exists in this paper; its result values were NOT_REACHED |
| Permeability remark | NOT_STATED in what I reached | the abstract says "high cell potency" in the title and "drug-like properties"; Tran's remark that acid-bearing Kelch binders raise permeability concerns cites this paper (ref 27) for compound 5-type behaviour, not for compound 9 |

---

## Q3. 28753294 (Del Prete et al., J Nat Prod 2017) and 37386884 (Qi et al., J Med Chem 2023)

| Item | Verdict | Words relied on |
|---|---|---|
| Bardoxolone methyl value in the thiol-trapping paper (assay, cell line, time) | SUPPORTED as [CH] only; paper NOT_REACHED | ChEMBL CHEMBL4193075: "Activation of Nrf2 (unknown origin) expressed in human HaCaT-ARE-luc cells after 6 hrs by luciferase reporter gene assay": BARDOXOLONE METHYL EC50 = 60.0 nM (0.06 uM). Same assay "relative to control tertbutylhydroquinone": Ratio = 40.94 (no unit printed). Parent oleanolic acid: EC50 >= 18.9 uM. Same compound, NF-kB (TNF-stimulated, mouse NIH/3T3, 6 h, luciferase): IC50 = 1.2 uM; STAT3 (IFN-gamma, human HeLa, 6 h): IC50 = 2.38 uM. Viability: "Cytotoxicity against human HaCaT cells ... at >5 to 10 uM" (numeric result not retrieved) |
| What the paper says about reactivity | SUPPORTED [AB] | "Bardoxolone methyl (1) is the quintessential member of triterpenoid cyanoacrylates, an emerging class of bioactive compounds capable of transient covalent binding to thiols. The mechanistic basis for this unusual 'pulsed reactivity' profile ... are unknown." "the triterpenoid scaffold sharply decreases the reactivity of the enone system by steric encumbrance and that only strongly electrophilic and sterically undemanding substituents such as a cyanide or a carboxylate group can re-establish Michael reactivity, albeit in a transient way for the cyanide group". "a substantial dissection between the thiol-trapping ability and the modulation of biological end-points sensitive to thiol alkylation was observed". Thiol-trapping rates themselves NOT_REACHED |
| Bardoxolone (acid) Kd on KEAP1 in 37386884: assay | SUPPORTED as [CH] only | ChEMBL CHEMBL5334951: "Binding affinity to Keap1 (unknown origin) assessed as dissociation constant incubated for 200 sec by sensor chip immobilization based surface plasmon resonance analysis": BARDOXOLONE Kd = 48720 nM (48.72 uM); the PROTAC (CHEMBL5414697) Kd = 11870 nM (11.87 uM) |
| What the molecule was used for there | SUPPORTED [AB] (+[CH]) | Abstract: "several PROTACs were designed and synthesized by harnessing CDDO as the Keap1 ligand"; "compared with CDDO, PROTAC ... displayed significant advantages ... lower toxicity than CDDO". [CH]: CDDO used as a competitor in AML12 cells ("preincubated with CDDO followed by compound addition") and as a comparator in a 1 uM Keap1-degradation panel. Cells: mouse AML12 hepatocytes; PROTAC Keap1 degradation DC50 = 0.21 uM (48 h, western) |
| Are the two structures treated as one compound by the authors | NOT_REACHED (authors' statements); structures are two compounds | ChEMBL registers "BARDOXOLONE" (CHEMBL1093059, free carboxylic acid, C31H41NO4) and "BARDOXOLONE METHYL" (CHEMBL1762621, methyl ester, C32H43NO4) as separate molecules; the two papers name them differently (the PROTAC paper "CDDO"; the thiol-trapping paper "bardoxolone methyl (1)"). Whether either paper equates them was not reached. Do not move a number from one structure to the other: 60 nM (methyl ester, HaCaT reporter, 6 h) and 48.72 uM (acid, isolated Keap1, SPR) differ by about 800-fold and come from different assay types |

---

## Q4. 21964340 (Dawson et al., Nature 2011; I-BET151)

| Item | Verdict | Words relied on |
|---|---|---|
| Any KEAP1 measurement in the paper | NOT_STATED in main text; NOT_REACHED in the supplement | [FT]: the PMC main text, four figure legends and Methods summary contain no occurrence of KEAP1, Kelch or NRF2 (case-insensitive search of the full XML, 66 kB, zero hits). Supplementary files (Suppl Info Doc, data set 1, tables 1-8) were not reachable |
| The "IC50 > 10000" statement | SUPPORTED as a curated entry, CORRECTED in meaning | ChEMBL (document CHEMBL5696440) holds six KEAP1 rows, all for **molibresib (I-BET762, CHEMBL1232461), not I-BET151**: assay "Inhibition of KEAP1 (unknown origin) assessed as fold change at 10 uM incubated for 1 hr by colloidal coomassie staining based LC-MS/MS analysis"; fold change = 0.722 (10 uM), 0.835 (2 uM), 0.856 (0.4 uM), 0.94 (0.08 uM), 1.072 (0.016 uM); and "IC50 > 10000.0 nM". This matches the paper's first proteomic approach: "bead-immobilized analogues of I-BET762 were incubated with HL60 nuclear extracts and bound proteins were analysed by quantitative mass spectrometry", "with subunits of protein complexes exhibiting closely matching IC50 values". So KEAP1 is one of hundreds of proteins in a chemoproteomic competition table (supplementary), the "> 10000 nM" is a floor set by the top concentration (10 uM) where the fold change had only fallen to 0.72, and it is not a KEAP1 binding or pathway experiment. The source supplementary table was not seen; this reading is an inference from ChEMBL's assay line plus the Methods sentence |

---

## Q5. Halofuginone and NRF2

| Item | Verdict | Words relied on |
|---|---|---|
| Primary paper(s) cited by 39241669 | SUPPORTED (identity), NOT_REACHED (the review's sentence) | Europe PMC reference list of 39241669 contains three halofuginone primaries: cited-order 152 Tsuchida et al. 2016/2017, Free Radic Biol Med 103:236-247 "Halofuginone enhances the chemo-sensitivity of cancer cells by suppressing NRF2 accumulation" (PubMed MeSH: A549 Cells); 191 Lv et al. 2021, Photodiagnosis Photodyn Ther 37:102572 (cutaneous SCC line SCL-1; "Overexpression of NRF2 conferred resistance to co-treatment's effects"); 193 Panda et al. 2022, Free Radic Biol Med 187:92-104 (halofuginone micelles, "Nrf2-activated lung adenocarcinoma"). Which two cancer lines the review names: NOT_REACHED. If the two lines are A549 and SCL-1, the sources are 152 and 191; this is a guess, not read |
| Mechanism: NRF2-specific or general protein synthesis | SUPPORTED [AB]: general | Tsuchida abstract: "Halofuginone induced a cellular amino acid starvation response that repressed global protein synthesis and rapidly depleted NRF2." The screen was "for NRF2 inhibitors" and "identified febrifugine derivatives"; "application of the less-toxic derivative halofuginone in a low dose range rapidly reduced NRF2 protein levels". So NRF2 falls because translation is repressed globally; NRF2-specificity is not claimed. Panda abstract: halofuginone "caused severe hematopoietic and immune cell suppression in a dose-dependent manner" |
| Concentrations | NOT_REACHED | the abstracts give only "low dose range"; no number was available in any reached source |

---

## Q6. Statements about neurons, astrocytes or brain-derived cells

| Document | Verdict | What it contains |
|---|---|---|
| 37187090 | SUPPORTED [AB] + [CH] | abstract: "antioxidant and anti-inflammatory effects in BV-2 microglial cells and significantly restored spatial memory deficits in lipopolysaccharide (LPS)-induced neuroinflammatory mouse models". [CH]: BV-2 (mouse microglia) Nrf2 immunoblots 3 h to 48 h at 3 uM; LPS-challenged mouse GFAP and IBA1 immunostaining in hippocampus (CA1, CA3, dentate gyrus) and cortex at 20 mg/kg/day. No cultured neurons or astrocytes in the curated assay list |
| 38116420 | SUPPORTED [FT] | no neural cell used (THP-1, HUVEC, A549, H1299, U2OS); EAE mouse model; Nrf2 measured in thymus [CH]; introduction only: "On top of the neuroprotective effects, DMF 1 has been known to show anti-inflammatory properties"; chalcone/vinyl sulfone 6 "alleviate motor deficits in an animal model of Parkinson's Disease" (literature citation) |
| 31411465 | SUPPORTED [FT] | CNS is the stated motive (abstract, "permeating the blood-brain barrier"; Introduction "Nrf2 activation ... has shown encouraging neuroprotective effects in animal models of cerebral ischemia ... neurodegenerative disorders"), but no neural cells were used (Hepa1c1c7 hepatoma). Only CNS-permeability experiments quoted are literature ones for 3 and 13, "discouraging" |
| 27031670 | SUPPORTED as [CH] | bronchial epithelial cells (NHBE, BEAS2B, COPD) and rat lung; no neural cell in the curated assays |
| 28753294 | SUPPORTED as [CH] | HaCaT keratinocytes, NIH/3T3 fibroblasts, HeLa; none neural |
| 37386884 | SUPPORTED [AB] + [CH] | mouse AML12 hepatocytes, mouse liver (MCD diet), zebrafish toxicity; none neural |
| 21964340 | SUPPORTED [FT] | leukaemia models only |
| 39241669 | NOT_REACHED | review text not reachable |

Net: the only brain-derived system in the set is BV-2 microglia plus whole-mouse brain stains in one paper (37187090), reached only through its abstract and ChEMBL. No document in the set tests an NRF2 activator or a KEAP1 binder in cultured neurons or astrocytes.

---

## Ranked list: what "raise NRF2 activity and separate NRF2-dependent from independent benefit" most needs to know

1. **The common cell readouts do not themselves prove NRF2 dependence, and the set contains direct evidence of independence.** NQO1 enzyme activity (31411465, Hepa1c1c7, 24 h), ARE-luciferase (28753294, HaCaT, 6 h), and PathHunter nuclear translocation (37187090, 38116420, U2OS with Keap1, per ChEMBL) are all NRF2-pathway proxies. 31411465 shows NQO1 induction by compounds with no Kelch binding (12, 13, 16) and says "progesterone is known to upregulate NQO1 without activating the Nrf2 pathway". 38116420 states a separate NFkB/ERK route for fumarate-type compounds. The one paper in the set with an NRF2-siRNA control arm is 27031670 (per ChEMBL descriptions; the arm's numbers were not reached). In a neural system, an NRF2 knockdown or knockout arm is what separates the two, and only the Davies compound's paper is documented here as having one.
2. **Binding mode divides the reagent classes.** Non-covalent Kelch-pocket binders (31411465 compounds 3-11; Davies compound = Tran 9, ITC Kd 1.3 nM [CH], SPR Kd 0.0014 uM) versus cysteine electrophiles (sulforaphane, DMF/MMF "irreversible Michael addition", bardoxolone methyl "transient covalent binding to thiols"). Tran's Kelch-domain assays cannot see cysteine modifiers: SFN "was not active in the FP assay". A compound that works in cells but not in a Kelch assay is not necessarily off-pathway (cysteine sensors in IVR/BTB), and a compound that works in a Kelch assay is not necessarily cell-permeable (peptides inactive; acids have permeability concerns).
3. **Cross-paper numbers do not transfer.** DMF 5.114 uM [CH] (37187090) versus 7.93 uM (38116420); MMF "> 10 uM" [CH] versus 127.2 uM; SFN 0.879 uM [CH] has no counterpart in 38116420; 10e 37.9 nM (abstract) versus 37.0 nM [CH]. Bardoxolone acid Kd 48.72 uM (SPR, isolated Keap1) and bardoxolone methyl EC50 60 nM (HaCaT reporter) are two different molecules and two different assay types. Any comparison needs a common assay run in the neural cell.
4. **No neural cell evidence for any reagent class in this set.** Reporter and NQO1 values are from hepatoma, osteosarcoma, keratinocyte, bronchial epithelial, monocyte and endothelial cells; the only brain-derived data are BV-2 and mouse brain stains in 37187090 (not read beyond abstract). Cell-type transfer is unsupported by these documents.
5. **An "NRF2-lowering control" in the halofuginone class lowers NRF2 by a general mechanism.** Per the Tsuchida abstract it "repressed global protein synthesis" through an "amino acid starvation response", and Panda reports dose-dependent hematopoietic and immune suppression. Specificity for NRF2 is not claimed. Concentrations and the two lines the review names are NOT_REACHED.
6. **The "IC50 > 10000" attached to 21964340 is a chemoproteomic floor for I-BET762 (fold change 0.72 at 10 uM), not a KEAP1 measurement of I-BET151**; it should not be quoted as a KEAP1 binding or pathway result. The supplementary table behind it was not seen.
7. **Viability controls are thin and drawn from other cells.** 38116420's toxicity numbers are in A549 and H1299 (13: 8.81 and 2.32 uM), DAPI "confirms the cells are viable" in HUVEC; 37187090's BV-2 viability is up to 3 uM for 24 h ([CH]); 31411465 gives no viability data for the NQO1 assay. For a neural system, the usable concentration window must be established in the neural cell.
8. **Reagent identity checks that the documents impose:** Davies compound = Tran compound 9 (Figure 1 legend); CDDO acid is not bardoxolone methyl; Tran compound 9's SPR Kd and Ki rest on single or limit-of-assay measurements ("affinity was too high to calculate an exact Ki"; "Based on only one measurement").

## What was not done / could not be reached

- Full texts of 37187090, 27031670, 28753294, 37386884, 39241669, 28039084, 34628069, 35618180 (publisher pages answer HTTP 403; I did not use browser-header spoofing and did not solve the proof-of-work download gate that PMC puts on supplement files).
- Supporting Information of 38116420, 31411465 and 21964340 (assay methods, incubation times, the I-BET supplementary proteomic table).
- Every cell marked [CH] is a ChEMBL transcription; I did not check ChEMBL against the paper.
- Operator contact details were not used, searched for or sent to any service.
