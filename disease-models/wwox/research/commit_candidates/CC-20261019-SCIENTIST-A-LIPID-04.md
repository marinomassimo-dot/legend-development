# CC-20261019-SCIENTIST-A-LIPID-04 — very-long-chain sphingolipid, VLCFA and peroxisome comparators of group G1

`context_policy: QUESTION_DRIVEN`. **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (identity records of non-WWOX comparators; no claim touched; one proposed method note for RL-003). `target_wm_version`: next MINOR after the integrator's current value.
**Nothing here is medical advice.** Numbering is provisional. Every paper in this candidate has the word WWOX zero times unless stated; records are comparators and must carry that fact.

## 1 · Landings (this file grows by section as the lot proceeds)

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 41715204 (Sun 2026, J Transl Med, CerS2 conditional knockout, very-long-chain sphingolipids and myelination) | `FTR-20261019-41715204-01` (partial: supplementary video not inspected) | New `PAPER` record (none exists), type murine mechanistic comparator, T3, relevance LOW (WWOX absent) |
| 2 | PMID 36583573 (Teo 2023, Glia, CerS2 deleted in myelinating cells: myelin lipid chain length, microglia, lethality) | `FTR-20261019-36583573-01` | New `PAPER` record (none exists), murine mechanistic comparator, T3, relevance LOW (WWOX absent) |
| 3 | PMID 40590574 (Wong 2025, Mov Disord, biallelic ELOVL1 variants: hypomyelinating leukodystrophy, movement disorder, ichthyosis) | `FTR-20261019-40590574-01` (partial: photographs and videos not inspected) | New `PAPER` record (none exists), human genetic comparator, T3, relevance LOW (WWOX absent) |
| 4 | PMID 32123819 (Isokawa 2019, FASEB BioAdv, Elovl1-deficient mice, myelin sphingolipid chain length, motor coordination) | `FTR-20261019-32123819-01` | New `PAPER` record (none exists), murine comparator, T3, relevance LOW (WWOX absent) |
| 5 | PMID 41815956 (Eberhart 2026, Front Mol Neurosci, Pex2 knockout Zellweger mice: lipid metabolism and hypomyelination) | `FTR-20261019-41815956-01` | New `PAPER` record (none exists), murine comparator, T3, relevance LOW (WWOX text-absent; WWOX protein is one unchanged row of the deposited proteome) |

## 2 · Record content (source 1)

What it measures: brain lipidomics, imaging, proteomics, EM and culture assays in CNS and oligodendrocyte-lineage CerS2 knockout mice. WWOX: zero occurrences.

Note text to carry:
🔴 **A comparator and a design template, not WWOX evidence.** Cell-of-origin differs from the recorded WWOX myelin defect: here the oligodendrocyte-lineage deletion suffices, whereas CLAIM 003 records WWOX hypomyelination as non-cell-autonomous after neuronal deletion and CLAIM 005's boundary records astrocyte and oligodendrocyte Wwox deletions as negative. The microdomain step rests on a cholesterol-depletion experiment (beta-cyclodextrin, about 40 percent, flat across 50 and 250 uM) that does not remove very-long-chain sphingolipids. P20 EM has two animals in one arm and the plotted group sizes are the reverse of the legend. Whole-brain proteomics (deposited table) shows GFAP about 3.2-fold up, undiscussed in the paper. Supplementary video not inspected.

## 3 · Method note proposed for the myelin line (no claim change)

If a Wwox-null or P47T brain lipidomics is ever run for question 1 of the metabolic batch, the species to read are C16-C18 versus C22-C24 ceramides, sphingomyelins, hexosylceramides and sulfatides, white-matter imaging, and raft-fraction lipids at P20; a neuron-OPC co-culture with independently genotyped partners separates cell-autonomous from non-cell-autonomous action. IPOTESI; no such measurement exists in the repository.

## 4 · What must NOT be written

- No statement that WWOX loss alters very-long-chain sphingolipids, ceramide chain length or cholesterol in brain or myelin.
- No claim link; no individual-level content.

## 5 · Registry statements to re-check at integration

None existing for this PMID. CLAIM 003 and CLAIM 005 are unchanged.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. Hypomyelination at P20 | EM images revealed significant reductions in both the number and thickness (g-ratio) of myelin sheaths in cKO-nestin mice as early as P20. | Results, section 2, `files/fulltext/PMID41715204_Sun2026_PMC.xml`
2. Beta-cyclodextrin effect described as severe | Addition of 50 μM β-CD to wild-type co-cultures severely impaired myelination (Fig. 6C), and a higher dose at 250 μM showed no additive effect (Fig. 6D). | Results, section 6, same artefact
3. Causal link incomplete | We acknowledge that a definitive causal link requires supplementation with purified individual VLC species, but this remains technically challenging due to difficulties in isolating specific VLC sphingolipids (e.g., distinct ceramides). | Results, section 7, same artefact
4. P20 sample sizes in the legend | (C) The g-ratio of myelin sheath in P20 mice corpus callosum, n = 4 for Ctrl, n = 2 for cKO-nestin mice. | Figure 2 legend, same artefact
5. GFAP up in the whole-brain proteome | Gfap coverage 74.4: LFQ CKO 18655000000 18549000000 14626000000 15183000000 \| WT 6816800000 4273900000 3985400000 5758200000 \| ratio CKO over WT 3.22 | `files/fulltext/PMID41715204_Sun2026_supplement/Table3_myelin_proteins_derivation.txt` (aggregate derivation of the deposited proteomics spreadsheet)

## 6 · Source 2 (PMID 36583573, Teo 2023): record content

What it measures: CNP-Cre CerS2 knockout: brain and purified-myelin lipidomics, EM, gliosis, whole-brain cytometry, motor tests, survival. WWOX: zero occurrences.

Note text to carry:
🔴 **A comparator with a measured cholesterol negative.** Even with severe hypomyelination and death, myelin cholesterol is unchanged (1577 versus 1616 nmol/mg protein) and total sphingomyelin is unchanged; the change is chain length (C22-C24 to C16-C18) with totals of HexCer, sulfatide and ceramide rising. A distinct microglial subset (TMEM119 and P2RY12 low; CD68, CD11c, CD45, MHC-II high) is about four-fold more abundant at 6 weeks and eight-fold at 10 weeks (3 mice per group); the trigger (TREM2, denatured MBP) is untested. The oligodendrocyte-lineage deletion suffices for myelin loss, whereas CLAIM 003 records WWOX hypomyelination as non-cell-autonomous. Deaths were not investigated. The deposited per-animal table reproduces Table 2 for four checked lipids.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 2)

6. Myelin cholesterol does not differ | Myelin cholesterol content did not differ between CerS2fl/fl and CerS2ΔO/ΔO mice (1577 ± 202 vs. 1616 ± 140 nmoles/mg protein), and sphingolipid levels in the liver did not differ between the two genotypes (Figure 3k–n). | Results, myelin lipid acyl chain length, `files/fulltext/PMID36583573_Teo2023_PMC.xml`
7. Totals rise while chain length shifts | Increased C16‐C18 variants produced an increase in total HexCer, ST and ceramide in myelin from CerS2ΔO/ΔO relative to CerS2fl/fl mice, despite reduced C22‐C24 variants (Figure 3f–h), whereas total SM was not significantly different (Figure 3i). | same
8. The microglial subset is about four- and eight-fold more abundant | and was approximately 4‐fold more abundant in 6‐week‐old CerS2ΔO/ΔO compared to CerS2fl/fl mice, increasing to 8‐fold in 10‐week‐old CerS2ΔO/ΔO mice | Results, phagocytic microglial population, same
9. The trigger is untested | Myelin phagocytosis by microglia can be initiated by interaction of the receptor TREM2 with myelin lipids such as ST and SM, when myelin or cellular debris is present | Discussion, paragraph 9, same
10. The cause of death was not determined | Death in CerS2ΔO/ΔO mice was sudden and unexpected. This necessitated modification of our ethics protocol such that CerS2ΔO/ΔO mice were only kept up to 4 months of age, and we were unable to determine the exact cause of death. | Discussion, paragraph 8, same

## 7 · Source 3 (PMID 40590574, Wong 2025): record content

What it is: seven patients from five consanguineous families with homozygous ELOVL1 variants (one nonsense, four missense VUS); MRI hypomyelination 6 of 6 and thin corpus callosum 5 of 6; biochemistry of one patient (plasma and fibroblasts). WWOX: zero occurrences. Class-level only.

Note text to carry:
🔴 **A comparator, and a conditional negative for the WOREE seizure phenotype.** The comparison table lists seizures as absent in recessive ELOVL1 disease and the clinical table has no seizure or EEG row, so hypomyelination with thin corpus callosum from a VLCFA lesion is recorded without epilepsy. The biochemistry is one patient and one variant; the antibody used to show absent protein targets residues 250-277, beyond the truncation at 154; the truncated protein retains about 57 percent of wild-type elongation in transfected cells; Supplementary Table 2 has an anomalous C22:0 cell and Supplementary Figure S1 a variant typo (c.284C>T for c.248C>T). Photographs and videos not inspected.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 3)

11. The antibody epitope lies beyond the truncation | As expected for a nonsense variant, Western blot analysis using a polyclonal antibody targeting the C‐terminal peptide sequence of ELOVL1 (amino acids 250–277, C‐ELOVL1) detected no signal in whole cell extracts from case 1 fibroblasts (Fig. 3A). | Results, expression in fibroblasts, `files/fulltext/PMID40590574_Wong2025_PMC.xml` (variant p.Trp154*, Results, molecular genetic data)
12. Seizures are absent for recessive ELOVL1 disease in the comparison table | Spasticity + + + − − − Seizures − − + − − − Movement disorder + − − − − − | Table 1, same artefact
13. Plasma VLCFA was measured in one patient | Analysis of VLCFAs in plasma was performed only in case 1 and demonstrated a decrease in C24:0 and C26:0 concentrations, consistent with the function of ELOVL1 in the synthesis of C22‐C26 VLCFAs (Supplementary Table S2). | Results, clinical review, same artefact
14. Only case 1 was studied in fibroblasts | Unfortunately, fibroblasts were unavailable from the other cases. | Discussion, paragraph 7, same artefact

## 8 · Source 4 (PMID 32123819, Isokawa 2019): record content

What it measures: brain sphingolipid lipidomics (3 versus 3), Ugt8a mRNA, EM at 13 months, survival and a behavioural battery in an epidermis-rescued whole-body Elovl1 knockout. WWOX: zero occurrences.

Note text to carry:
🔴 **A readout template, not WWOX evidence.** Chain-length shortening (C24 and C26 almost absent) with total GalCer down 39 percent and mild, late myelin thinning confined to the smallest and largest axons (EM at one age, 13 months; animals per group not stated). Two of 22 knockouts died of startle epilepsy and only 22 of 66 expected knockouts were present at three weeks. The text reports no wide-beam difference while Figure 4L prints P .0199 for wide-beam slips. The only VLC-lesion seizure phenotype in this lot is in this mouse; the human ELOVL1 series (PMID 40590574) records none.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 4)

15. Total GalCer down 39 percent | Consistent with the results of the TLC analysis, the total levels of GalCer and 2‐OH GalCer were reduced by 39% and 34%, respectively, in Elovl1 −/− Tg(IVL‐Elovl1) mice relative to control mice. | Results, section 1, `files/fulltext/PMID32123819_Isokawa2019_PMC.xml`
16. Startle epilepsy deaths | Three more of these mice were lost by the age of eight weeks, and two of them died from startle epilepsy. | Results, section 4, same
17. EM counts | Average diameters ± SD of myelinated axons: n = 96 [Elovl1 +/+ Tg(IVL‐Elovl1)] and n = 73 [Elovl1 −/− Tg(IVL‐Elovl1)] total axons counted in 13 different fields of view. | Figure 3 legend, same
18. Wide-beam text | On the wide beam, there were no significant differences between control and Elovl1 −/− Tg(IVL‐Elovl1) mice; however, on the narrow beam, Elovl1 −/− Tg(IVL‐Elovl1) mice moved significantly more slowly and exhibited more paw slips (Figure 4K, L). | Results, section 4, same (panel: `files/figures/PMID32123819/FBA2-1-747-g004.jpg`, Figure 4L wide-beam P .0199)

## 9 · Source 5 (PMID 41815956, Eberhart 2026): record content

Systemic Pex2 knockout at P10: CNP activity down 50-60 percent, myelin mRNAs and proteins down, cholesterol unchanged with desmosterol up, white-matter cholesterol-synthesis enzymes down and cortical up, CERS2/DEGS1/UGT8/FA2H proteins down, p-RPS6 down, Trem2 and cytokines up.

Note text to carry:
🔴 **A peroxisome-lesion comparator; WWOX is not studied.** Whole-region tissue, one age, knockouts n = 3 to 6, controls pooled from two genotypes; hypomyelination confounded by bile-acid-dependent fat malabsorption; sphingolipid chain length not measured. The deposited proteome lists WWOX protein in spinal cord, brainstem and cerebellum with no change (log2 fold change +0.14, -0.06, -0.26; P 0.40-0.73).

### LOCATOR TRIPLES FOR BLIND AUDIT (source 5)

16. Cholesterol similar, desmosterol up | While cholesterol levels were similar in the brains of control and Pex2−/− mice, desmosterol levels were significantly elevated in the brains of both untreated and BA-fed Pex2−/− mice compared to their control littermates (Figure 3A). | Results, sterol levels, `files/fulltext/PMID41815956_Eberhart2026_PMC.xml`
17. Nutritional confound named | Postnatal peroxisome-deficient Pex2−/− mice suffer from intestinal lipid malabsorption due to impaired bile acid synthesis (Keane et al., 2007), and the combination of inadequate dietary fat intake and impaired fatty acid processing can lead to severe energy deficits and developmental delays such as hypomyelination. | Discussion, paragraph 4, same
18. Whole-tissue limitation | A limitation of our study is that we analyzed the entire tissue of different regions of the CNS, so that observed changes in the activity of enzymes, or the expression of genes and proteins cannot be assigned to a specific cell type (neurons, astrocytes, oligodendrocytes, and microglia). | Discussion, paragraph 8, same
19. WWOX protein unchanged in cerebellum | CBL diff_exp_analysis: Wwox | header cells: ['Gene', 'log2 fold change', 'p.value', 'FDR'] | values: ['-0.26134379502771682', '0.67404861086198831', '0.87760320871459885'] | `files/fulltext/PMID41815956_Eberhart2026_supplement/Table3_wwox_derivation.txt`
