# Blind report, ADV-283 sentences S1 to S5

Checker: independent blind reader (sonnet, high). Hypothesis-level reading of public deposited data; not medical advice.
Scripts: /home/desktop/.claude/jobs/ae0002e7/tmp/adv283/blind/ (pdk.py, chk.py, anchor.py, cage.py, cage2.py, sn.py, marker.py), run with python3 -I -P -E and file paths as arguments.

## Common recomputation (S1, S2, S4 inputs)

Mapping. Ensembl r92 cdna fasta: 113,193 transcripts, every header has a gene_symbol field. Both TPM tables have 111,083 rows each; 111,083 of 111,083 rows matched a fasta header by the versioned id directly; 0 rows had no mapping, 0 TPM unmapped. Every column sums to 1,000,000 TPM. Transcripts per gene in the tables: Pdk1 8, Pdk2 5, Pdk3 3, Pdk4 3 (the same counts exist in the fasta). Gene ids: Pdk1 ENSMUSG00000006494, Pdk2 ENSMUSG00000038967, Pdk3 ENSMUSG00000035232, Pdk4 ENSMUSG00000019577. Only the Pdk3 and Pdk1 protein_coding transcript is one each (Pdk3: 1 protein_coding + 2 processed_transcript), so gene TPM includes non-coding isoforms (for Pdk1 7 of 8 transcripts are processed_transcript).

Gene TPM, GSE158681 (hippocampus, 14 libraries; column order S_Ctrl_1, S_Ctrl_2, S_KO_1..3, N_Ctrl_1, N_Ctrl_2, N_KO_1, N_KO_2, KO_1, KO_2, WT_1..3):
- Pdk1: 20.75 23.93 | 12.02 15.51 16.75 | 13.06 16.23 | 15.22 15.46 | 13.08 19.24 | 15.04 20.76 15.63
- Pdk2: 76.64 89.90 | 119.53 97.48 111.85 | 88.09 74.53 | 121.48 97.40 | 52.68 40.04 | 66.59 53.38 58.79
- Pdk3: 28.04 25.70 | 33.33 25.24 29.25 | 29.36 28.45 | 24.82 27.95 | 14.87 15.38 | 23.83 21.37 20.66
- Pdk4: 3.87 3.59 | 2.17 4.97 5.06 | 3.12 3.31 | 2.65 1.29 | 2.73 3.68 | 7.98 7.23 6.67
GSE158682 (cortex, 7 libraries; CRTX_S_Ctrl_1..4, CRTX_S_KO_1..3):
- Pdk1: 9.98 11.65 4.30 5.74 | 8.91 3.81 6.40
- Pdk2: 134.58 120.53 136.88 145.78 | 125.60 187.67 197.30
- Pdk3: 19.14 21.90 17.27 17.31 | 13.83 18.65 25.38
- Pdk4: 3.06 2.62 1.65 3.08 | 1.49 1.44 1.87

Ratios of arm means (deficient / control) and "every deficient library below every control library" (ALL-BELOW):
| arm (KO n vs ctl n) | Pdk1 | Pdk2 | Pdk3 | Pdk4 |
|---|---|---|---|---|
| global null hippocampus (2 v 3) | 0.943, no | 0.778, yes | 0.689, yes | 0.440, yes |
| Synapsin-Cre hippocampus (3 v 2) | 0.661, yes | 1.316, no | 1.089, no | 1.090, no |
| Nestin-Cre hippocampus (2 v 2) | 1.047, no | 1.346, no | 0.913, yes | 0.613, yes |
| Synapsin-Cre cortex (3 v 4) | 0.805, no | 1.266, no | 1.020, no | 0.615, no |

Every ratio, every library value and every n quoted in S1 and S2 reproduces (to the rounding quoted).

Arm assignment and unit. Arms are assigned from column names only (KO/WT = global null; S_ = Synapsin-Cre; N_ = Nestin-Cre; CRTX_S_ = cortex Synapsin-Cre). No SOFT file for GSE158681/2 is held, so the deposit's own sample descriptions were not read. Supporting checks that I could do: (a) Wwox TPM is 8 to 40 fold lower in the columns called KO in every arm (global KO 0.3, 0.4 vs WT 3.5, 4.3, 3.9; S_KO 0.4, 0.3, 0.8 vs 3.3, 3.4; N_KO 0.1, 0.4 vs 3.5, 3.6; cortex S_KO 5.0, 3.8, 9.0 vs 8.0, 26.5, 25.7, 15.1, a weaker contrast), so the KO labels are consistent with genotype; (b) the paper (files/fulltext/PMID33914858 ... .txt, Fig. 3 legend) states cortex S-Control n=4, S-KO n=3 and hippocampus S-Control n=2, S-KO n=3 at P17, which equals the column counts for those two arms. The paper text I read gives NO n, age or genotype description for the Wwox-null or N-KO hippocampal RNA-seq (it says only that bulk RNA-seq on whole hippocampal tissues of Wwox-null and N-KO was done, Supplementary Table 2, not held). So the n of 2 v 3 (global) and 2 v 2 (Nestin) and the P17 age for those two arms are NOT verified from held text. The paper never states that a library is one animal; I could not verify that the unit is an animal rather than a pool or a technical replicate. Unit of n in every arm is the library; the animal equivalence is an unverified assumption.

Composition check I ran on the same tables (not in the sentences): oligodendrocyte genes fall to 0.17 to 0.49 of control in every deficient arm (Plp1 ratio global 0.25, Syn 0.17, Nes 0.28, cortex 0.49; Mbp 0.25, 0.23, 0.39, 0.44) and Gfap rises 1.6 to 4.3 fold (global 1.57, Syn 4.34, Nes 2.47, cortex 1.80). The paper itself reports hypomyelination and reduced mature oligodendrocytes. So every deficient arm differs in cell composition, and any Pdk ratio is a whole-tissue mixture ratio.

Human anchor GSE156243 (counts, 4 cko + 2 cwt libraries; 35,337 gene rows; library sums 38.7, 41.2, 38.2, 34.2, 37.3, 30.0 million): PDK3 raw counts cko 424.999 394 455 322 vs cwt 263.001 194. Ratio of raw-count means is 1.746; ratio of library-size-normalised (counts per million) means is 1.547, which is the quoted 1.55; all four cko CPM (11.0 9.6 11.9 9.4) are above both cwt (7.1 6.5). So "1.55 times" is a CPM ratio, not a ratio of counts, and is not stated as such. PDK1 CPM ratio 0.781 (all KO below both WT), PDK2 0.913, PDK4 1.365. Caveat: WWOX counts in the cko columns are HIGHER (raw 547 488 632 420 vs 359 302; CPM ratio 1.39), so the held count table does not by itself show WWOX loss in the arm called knockout; "human organoids" and the cko/cwt assignment are not verifiable from this one file (no SOFT named for it).

## S1

VERDICT: ADD

Checked and right: all four Pdk3 ratios and all library values; n per arm; the global-null "every knockout library below every wild-type library" (max 15.38 < min 20.66); the 1.55 in the anchor (as CPM, see above) and 4 v 2 libraries.

1. "Pdk3 is not higher in the Wwox-deficient arm" and "Pdk3 1.089" / "1.020": two arms have a ratio above 1 (Synapsin hippocampus 1.089, cortex 1.020). "Not higher" is only true if a threshold for "higher" is given. Add: "not higher by more than 9 percent in any arm (1.089 and 1.020 are nominal increases inside overlapping library ranges: Synapsin KO 25.24 to 33.33 vs control 25.70 and 28.04; cortex KO 13.83 to 25.38 vs control 17.27 to 21.90)". Alternatively "no arm shows the anchor-size increase (1.55 with every KO library above every control library)".
2. "two held mouse datasets from one study": the two deposits are not independent replications of each other; they share lab, mice, protocol and (for Synapsin) the same genotype contrast in two tissues. The non-replication therefore comes from one study, and the 1.55 anchor is a different species, different system (organoid or culture vs P17 whole tissue) and a different knockout design. Add: "one study (PMID 33914858, linked by identical n per arm; the deposits name no paper)".
3. "single-deposit observation": as a count of deposits it is right (only GSE156243 shows it among the deposits named). As a "therefore" from the mouse data it does not follow, because absence in mouse bulk P17 tissue (n 2 to 4 libraries, tissue composition shifted) does not test a human organoid finding. Replacement: "...is therefore not replicated in these mouse tissues and rests on one deposit".
4. Missing: (a) the 1.55 is a library-size-normalised (CPM) ratio of 4 v 2 libraries (raw count ratio 1.75) and WWOX counts are not lower in that deposit's knockout columns; (b) the global-null mice are on an FVB background and the conditional lines on C57BL6/J;129sv mixed (paper Methods), and the global-null/Nestin n, age and control definition are not stated in the held paper text; (c) Gene TPM sums 3 transcripts of which 2 are non-coding processed_transcripts; (d) the deficient arms have fewer oligodendrocytes and more Gfap (see above); (e) n is libraries, assumed animals; (f) the "Nestin-Cre arm" is hippocampus (GSE158681) but is written without tissue; (g) the human PDK3 vs mouse Pdk3 equivalence is by symbol only (see 4 below).
5. Mouse Pdk1 to Pdk4 map one to one to PDK1 to PDK4: in the held files each Pdk is a single Ensembl gene with a distinct id and I found no second gene with a Pdk-type symbol in the fasta (only Pdk1 to Pdk4 headers). One-to-one orthology is by symbol; it is not tested from a held orthology table. This is standard knowledge (four PDK paralogs in both species) and I found nothing contradicting it, but I did not verify it from a held file.

## S2

VERDICT: MUST CHANGE (final sentence), plus ADD on the cortex clause

Right as worded: all Pdk1 values, ratios (0.661, 0.943, 0.805), n per arm; Pdk1 meets both criteria (ratio at most 0.83 and every deficient library below every control) only in the Synapsin hippocampus arm (max KO 16.75 < min control 20.75). The Nestin arm is 1.047 (not stated in the sentence).

1. "it is not lower in ... the cortex (0.805; ...)": the ratio 0.805 is below 0.83, so the cortex PASSES the ratio threshold and fails only the library criterion (KO 8.91 above control 4.30 and 5.74; the ranges overlap throughout). The sentence quotes the ratio next to "not lower" without saying which criterion fails. Add: "(ratio 0.805 meets the 0.83 limit but KO libraries 8.91 and 6.40 lie above control libraries 4.30 and 5.74, so the all-below criterion fails)". The thresholds are applied as written to the four arms named; only the cortex needs this explanation. Note the Nestin arm and the global null are named in the sentence; no other arm exists.
2. "The isoform pattern PDK3 higher with PDK1 lower is therefore not seen together in any primary comparison": this has no stated criterion for "PDK3 higher" and does not follow from the preceding sentence, which only addresses PDK1. In the Synapsin hippocampus arm, the one arm where Pdk1 is lower by both criteria, Pdk3 is nominally higher (1.089; mean 29.27 vs 26.87 TPM). By a nominal reading the pattern IS present in that arm. It is absent only if "higher" is defined by a criterion that 1.089 with overlapping libraries (25.24 below 25.70) fails. This is a statement that says more than the sources support unless the criterion is added. Replacement: "Pdk3 is not higher by the anchor-size criterion (ratio at least 1.2 [or 1.55] with every deficient library above every control library) in any primary comparison; the nearest case is the Synapsin hippocampus arm, where Pdk1 is 0.661 and Pdk3 is 1.089 with overlapping libraries (n 3 against 2)." Also define "primary comparison" (the four arms listed); in the global null Pdk3 is lower (0.689) and Pdk1 not.
3. Missing: Pdk1 TPM in the cortex is only about 4 to 12 TPM and in all arms 4 to 24 TPM, so the quoted ratios are for low to moderate expression with 2 to 4 libraries per arm; the anchor's Pdk1 was 0.78 (CPM) with all four KO below both WT, so the cortex ratio 0.805 is anchor-sized but not anchor-consistent; the tissue composition and unit points of S1.

## S3

VERDICT: MUST CHANGE (the "lower in both cell types" and "WWOX depletion in both" readings); numbers reproduce

Recomputed from GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz (columns Gene, hNSC, Neurons, hNSC_WWOX_del, Neurons_WWOX_del; 9,427 rows, 0 duplicate symbols, one row each for PDK1, PDK2, PDK3 and WWOX; PDK4 not in the table):
- PDK1 5.156, 3.304 | 3.558, 1.571: ratios hNSC 0.690, neurons 0.476.
- PDK3 15.566, 12.972 | 14.164, 4.272: ratios hNSC 0.910, neurons 0.329.
- PDK2 32.82, 37.11 | 34.40, 7.19: 1.048 and 0.194.
- WWOX 2.902, 2.539 | 3.349, 0.516: ratios hNSC 1.154, neurons 0.203.
The sample-to-column assignment is confirmed by the held SOFT (GSM3590948 hNSC wild type undifferentiated; GSM3590949 hNSC_WWOX_del silenced; GSM3590950 neurons wild type; GSM3590951 neurons_WWOX_del silenced; one sample per condition, one series, lentiviral shRNA treatment). One sample per arm, as stated.

Problems:
1. Column totals of the table are not on a common TPM scale: 609,160 (hNSC), 264,496 (Neurons), 606,894 (hNSC_WWOX_del) and 89,582 (Neurons_WWOX_del), not 1,000,000. The Neurons_WWOX_del column carries only a third of the mass of the Neurons column. Consequently every gene is shifted in the neuron pair: median del/control ratio over the 9,026 genes nonzero in both is 0.357 (hNSC pair: 1.15); GAPDH 0.549, ACTB 0.377, TUBB3 0.064, MAP2 0.304. PDK3 0.329 and PDK1 0.476 in neurons are at or near that global shift. If each column is renormalised to its own table total, the neuron ratios become PDK3 0.972 and PDK1 1.404 (hNSC: 0.913 and 0.693). So "PDK1 is lower in both" is not robust in neurons; the direction changes with normalisation. I cannot say which scaling is right (the deposit's own normalisation is not described in held files; the table is smaller than "all genes" suggests and the bed tag counts file lists 31.7, 14.3, 32.7, 40.7 million tags in a different order).
2. "lower with WWOX depletion in both cell types": the held table shows WWOX 1.154 times HIGHER in hNSC_WWOX_del (3.349 vs 2.902), i.e. no depletion of WWOX CAGE signal in the stem cell pair; only neurons show a drop (0.203, or 0.60 after renormalisation). The SOFT labels both deficient samples "wwox expression: silenced" by shRNA, so the label is right, but the data in hand do not show silencing in hNSC. Replacement: "in the shRNA-silenced samples (WWOX CAGE TPM 1.15 times control in hNSC, 0.20 in neurons)".
3. The control is "wild type", with no scrambled-shRNA control described in the held SOFT; the deficiency is partial knockdown, not knockout; the differentiation is spontaneous.
Suggested replacement: "In GSE126075 (one shRNA-silenced and one untreated sample per cell type, merged TPM by gene symbol; the neuron-pair columns differ in total TPM, 89,582 against 264,496, so every gene is lower by a median 0.36 in the silenced neuron sample) PDK3 and PDK1 are not distinguishable from that library-wide shift; this is descriptive only and not counted."
"n of 1 per arm, descriptive, not counted" is correct and adequate; the unit is a sample/culture, not an animal.

## S4

VERDICT: ADD

Recomputed (matrix.mtx features x barcodes; feature id for Pdk3 is row 4700 in both libraries): ctrl 3,182 barcodes, 31,053 features, 18,482,731 total UMI, Pdk3 628 UMI in 515 nuclei; ko 2,920 barcodes, 6,262,462 non-zero entries, 16,657,433 total UMI, Pdk3 489 UMI in 415 nuclei. All numbers in the sentence reproduce. Other genes for context (UMI in nuclei): Pdk1 394 in 340 (ctrl) vs 409 in 350 (ko); Pdk2 261/249 vs 159/151; Pdk4 30/28 vs 15/15; Wwox 2,041 in 1,017 vs 204 in 141 (a 10-fold UMI drop in the knockout library, consistent with the labels).
1. "no cell-class labels held" is true of the held files; "one control and one knockout library" is true (paper: S-Control n=1, S-KO n=1 at P17).
2. Add what the reader needs: the libraries are the Synapsin-Cre neuron-targeted pair (paper Fig. 3F legend), not the global null; P17; fractions of nuclei with Pdk3 detected are 16.2 percent (ctrl) and 14.2 percent (ko), at about 1.2 UMI per detecting nucleus, i.e. sparse detection, so a "detected in both" statement says only that the gene is expressed in a minority of nuclei; per-nucleus total UMI are similar (about 5,800 and 5,700). The paper reports a 15 percent / 68 percent change in oligodendrocyte populations, so composition differs between the two libraries. "No direction is claimed" is a correct restraint; I confirm the data cannot give one (one library per arm, nuclei are not replicates).
Suggested clause: "the control and knockout libraries are the Synapsin-Cre neuron-targeted pair at P17; Pdk3 is detected in about 16 and 14 percent of nuclei".

## S5

VERDICT: ADD

Sheet lines read: 7, 25 and 26 (and the next lines containing "dichloroacetate"; line 32 on millimolar). Line 7 reads, verbatim: "One 2017 document (CHEMBL4007440, ELISA with full-length His6-PDHA1 as substrate, 30 minutes) gives IC50 PDK1 1.03 mM, PDK2 0.50 mM, PDK3 5.56 mM: an 11-fold range across isozymes in one assay." The document id, assay description, year, the three IC50 values and "one assay" match the sentence exactly; 5.56 / 0.50 = 11.1, 5.56 / 1.03 = 5.4.
1. "PDK3 is the isoform least inhibited in that assay": only PDK1 to PDK3 are in the sheet line; PDK4 is not reported (not "not measured", absent from the sheet). Say "among the three isozymes reported".
2. The inference "not read with PDK3 as the relevant target in this genotype class on this evidence" rests on two separate points: (a) lower enzymatic potency of dichloroacetate at PDK3 in a single 2017 ELISA of unstated species (but only 5-fold weaker than PDK1 and all values are millimolar; the sheet's own line 32 says the compound acts at millimolar concentrations and no brain concentration was found); (b) Pdk3 not higher in mouse tissue, which does not bear on whether PDK3 is a relevant target (an unchanged or lower Pdk3 does not make an inhibitor irrelevant; the anchor's human organoid result says the opposite). I could not find in the sheet lines I read that the sheet says anything about PDK3 as a target; the sentence is a repository inference. Add: "this is a prioritisation of weight, not exclusion; potency differences of 5 to 11 fold across isozymes are small against the millimolar scale and the mouse evidence is composition-confounded".
3. The sheet says a 1999 row gives IC50 above 2 mM for "PDK" in vitro and a different readout; "no order between the two documents is read" so "one assay" is the correct wording and stands.
Verdict ADD, not MUST CHANGE, because the quoted facts are accurate and "on this evidence" is hedged.

## Item 4 summary (answered above)

- "single-deposit observation": follows as a count (only GSE156243 shows it), not as a replication test (S1 point 3).
- Thresholds: ratio 0.83 or less and every-library-below are applied as written to the four mouse arms in S2. The cortex meets the ratio and fails the all-below rule; this is not stated (S2 point 1). In S1 no threshold is stated for "not higher" (S1 point 1). S3 to S5 quote no threshold. The anchor's own PDK3 meets ratio and all-above (CPM), the anchor's Pdk1 meets 0.83 and all-below.
- Mouse Pdk1 to Pdk4 to human PDK1 to PDK4: one per symbol in the held fasta; orthology by symbol only, not tested by a held ortholog table.

## Item 5, what readers need that is missing across the sentences

Detection level (TPM 4 to 33 for Pdk1/Pdk3 in tissue; 16 percent of nuclei in the snRNA libraries), tissue composition (oligodendrocyte genes down 2 to 6 fold, Gfap up 1.6 to 4.3 fold in every deficient arm), age (P17 stated by the paper only for the Synapsin arms; null and Nestin ages not found in held text), genotype definition (global null on FVB background vs floxed Cre lines on C57BL6/J;129sv; whole tissue, not neurons alone), unit (library; animal equivalence not stated in any held file), the human anchor is CPM from a deposit whose WWOX counts are not lower in the knockout columns, and the CAGE table's unequal column totals.

## Summary table

| id | verdict |
|---|---|
| S1 | ADD |
| S2 | MUST CHANGE |
| S3 | MUST CHANGE |
| S4 | ADD |
| S5 | ADD |

## Files opened

- /home/desktop/.claude/jobs/ae0002e7/tmp/adv283/BLIND_SENTENCES_ADV283_SCI_20261125.md
- /home/desktop/legend-development/files/geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz
- /home/desktop/legend-development/files/geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz
- /home/desktop/legend-development/files/reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz
- /home/desktop/legend-development/files/geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz, gse126075_soft_full.txt, GSM3590948.txt to GSM3590951.txt (sample headers), bed_streamed_tagcounts_and_sha256.tsv
- /home/desktop/legend-development/files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz
- /home/desktop/legend-development/files/geo/GSE158684/ (six ctrl/ko barcodes, features, matrix files; SHA256SUMS head)
- /home/desktop/legend-development/files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt (grep and excerpts: methods, Fig. 1 and 3 legends, RNA-seq results paragraph)
- /home/desktop/legend-development/.claude/worktrees/sci_am_20261125/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/adv098_agent_sheets_he_20261119/BATCH8_broad_ISRIB_trazodone_omaveloxolone_dichloroacetate_HE_20261120.md (grep of the dichloroacetate, PDK, CHEMBL4007440 and IC50 lines only; the grep output also showed the lines on trazodone and ISRIB that contain "IC50", which I did not use)
- Not opened: framework protocols, delegation_budget.md (the blind rules forbade other repository text), card files, PREREG, result or audit documents. No network.

## What I could not verify

Arm assignment beyond column names for GSE158681/2 (no SOFT held); n, age and control definition of the global-null and Nestin hippocampal arms from the paper; that one library equals one animal; the species and cell type behind the "human organoids" label and the cko/cwt assignment of GSE156243; the normalisation of the GSE126075 merged table; orthology from a held ortholog table.
