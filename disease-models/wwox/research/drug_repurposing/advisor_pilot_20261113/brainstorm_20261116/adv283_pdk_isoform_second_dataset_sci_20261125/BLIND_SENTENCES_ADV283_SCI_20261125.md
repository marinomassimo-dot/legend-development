# Blind sentences, ADV-283 (verbatim repository sentences built by script; verdicts MUST CHANGE / ADD / STANDS; do not assume right or wrong)

Held sources for S1 and S2: /home/desktop/legend-development/files/geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz ; /home/desktop/legend-development/files/geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz ; transcript to gene mapping: /home/desktop/legend-development/files/reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz (headers). The deposits state no paper; the paper the repository links them to is PMID 33914858 (Repudi 2021, files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt) by identical n per arm.
Held sources for S3: /home/desktop/legend-development/files/geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz and gse126075_soft_full.txt (same folder).
Held sources for S4: /home/desktop/legend-development/files/geo/GSE158684/ (the six GSE158684_ctrl_ and GSE158684_ko_ filtered files).
Held source for S5 (read only the lines on dichloroacetate and PDK isozymes): disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/adv098_agent_sheets_he_20261119/BATCH8_broad_ISRIB_trazodone_omaveloxolone_dichloroacetate_HE_20261120.md under /home/desktop/legend-development/.claude/worktrees/sci_am_20261125/ ; the anchor deposit for the 1.55 times in S1 is files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz (counts, one library per column cko1-4, cwt1-2).

## S1

In two held mouse datasets from one study (GSE158681 hippocampus and GSE158682 cortex, postnatal day 17, transcript TPM summed to gene) Pdk3 is not higher in the Wwox-deficient arm. Hippocampus, global null KO against wild type: Pdk3 ratio of arm means 0.689 (14.87 15.38 against 23.83 21.37 20.66 TPM, n 2 against 3), every knockout library below every wild-type library. Hippocampus, neuron-targeted (Synapsin-Cre) KO against control: Pdk3 1.089 (33.33 25.24 29.25 against 28.04 25.70 TPM, n 3 against 2). Nestin-Cre arm: Pdk3 0.913 (24.82 27.95 against 29.36 28.45 TPM, n 2 against 2). Cortex, neuron-targeted KO against control: Pdk3 1.020 (13.83 18.65 25.38 against 19.14 21.90 17.27 17.31 TPM, n 3 against 4). The anchor's higher Pdk3 (1.55 times in human organoids, 4 knockout libraries against 2 wild-type) is therefore a single-deposit observation.

## S2

Pdk1 is lower (ratio 0.83 or less with every deficient library below every control library) only in the neuron-targeted hippocampal arm (0.661; 12.02 15.51 16.75 against 20.75 23.93 TPM, n 3 against 2); it is not lower in the global null hippocampus (0.943; 13.08 19.24 against 15.04 20.76 15.63 TPM, n 2 against 3), the nestin-Cre arm, or the cortex (0.805; 8.91 3.81 6.40 against 9.98 11.65 4.30 5.74 TPM, n 3 against 4). The isoform pattern PDK3 higher with PDK1 lower is therefore not seen together in any primary comparison.

## S3

In the human neural stem cell and neuron CAGE deposit GSE126075 (one sample per arm, no replicate, merged TPM by gene symbol), PDK3 is lower with WWOX depletion in both cell types (hNSC 0.910, neurons 0.329) and PDK1 is lower in both (hNSC 0.690, neurons 0.476); with n of 1 per arm this is descriptive and is not counted toward support or failure.

## S4

In the mouse hippocampal snRNA-seq deposit GSE158684 (one control and one knockout library, no cell-class labels held) Pdk3 is detected in both libraries (control: 628 UMI in 515 of 3182 nuclei; knockout: 489 UMI in 415 of 2920 nuclei); this is a coverage statement and no direction is claimed.

## S5

One 2017 document (CHEMBL4007440; ELISA, full-length His6-PDHA1 substrate, 30 minutes) gives dichloroacetate IC50 PDK1 1.03 mM, PDK2 0.50 mM, PDK3 5.56 mM in one assay. Because PDK3 is the isoform least inhibited in that assay and is not higher in the two held mouse Wwox-deficient tissues, the sheet is not read with PDK3 as the relevant target in this genotype class on this evidence.

