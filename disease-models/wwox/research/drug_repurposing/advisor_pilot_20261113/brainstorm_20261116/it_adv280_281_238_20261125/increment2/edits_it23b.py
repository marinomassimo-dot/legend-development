"""IT 2026-11-25 (IT23, increment 2; verifier C's replacements folded by IT24 the same day): wording for SCI's ADV-282 null-note audit
(13 disease-assertion notes in eight cards). Same schema as edits_it23.py. Data only; applied by apply_it24.py. Hypothesis level; nothing here is medical advice."""
EDITS = []
def e(i, card, mode, old, new): EDITS.append(dict(id=i, card=card, mode=mode, old=old, new=new, sources=[]))

# Revised by IT24 after blind verifier B (narrow recheck of composed wording): T06, T10, T17, T19, T19c, T21, T24, T25, T28, T31.

e("T01", "E03_pdk_inhibition_dca", "replace",
  "PDK1 -0.34, lower in sign only (the IT5 same-sets re-analysis gives -0.39, inside the single-gene null, p about 0.30;",
  "PDK1 -0.34 (mean of log2(CPM+1), knockout minus wild type; log2 of the ratio of mean CPM is -0.36) and -0.39 (log2 of the ratio of mean median-of-ratios counts, which is the IT5 same-sets re-analysis), the same six libraries; PDK1 is in neither deposited list and is lower in sign only (lower in all four knockout libraries than in both wild-type libraries, a pattern that is common in this deposit: of 2,804 genes with mean CPM within 1.5-fold of PDK1's, 663, 24 percent, are lower in all four knockout libraries than in both wild-type libraries and 570, 20 percent, higher, against about 6.7 percent each way expected for exchangeable 4 against 2 libraries; inside the single-gene null, p about 0.30, where the null is not defined in the held files, an empirical version gives 0.27 to 0.39, and a recompute of the share of expression-matched genes with an equal or larger shift gave 0.33 to 0.35; with 4 against 2 libraries no rank test can reach a two-sided P below 0.13, and a Welch t-test on log2(CPM+1) would give about 0.03 and is not meaningful with 2 wild-type libraries;")

e("T02", "E03_pdk_inhibition_dca", "replace",
  "the PDK/PDH set +0.17 (P 0.22, not different from chance);",
  "the PDK/PDH set +0.17 (P 0.22 from the repository's own set test, rerun at 0.2265; the set is not defined in the held files and the +0.17 is not reproduced: plausible memberships tried gave +0.15 to +0.24, and a second reader's random sets of plausible membership gave P 0.33 to 0.81; the set mean averages away PDHA1, PDPR and LDHA, which are in the authors' up list at adjusted P 5.8E-10, 1.3E-04 and 4.9E-06, and PDK3, higher in all four knockout libraries at 1.55 times, nominal P 7.39E-03, adjusted P 5.65E-02);")

e("T03", "E03_pdk_inhibition_dca", "replace",
  "LDH-to-PDH ratio not shifted (inside the spread of the two wild-type libraries).",
  "the LDH-to-PDH transcript ratio depends on the pairing (log2 of (LDHA+LDHB) over (PDHA1+PDHB+DLAT+DLD), knockout minus wild type, -0.14; LDHA over PDHA1 0.72 against 0.86, three of four knockout libraries below both wild-type libraries; LDHA over (PDHA1+PDHB) 0.54 against 0.56), and no pairing was fixed in advance in the held sources.")

e("T04", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "PDK1 -0.39, LOWER IN SIGN ONLY: inside the single-gene null (p about 0.30)",
  "PDK1 -0.39 (log2 of the ratio of mean median-of-ratios counts; -0.34 is the mean of the log2(CPM+1) difference, -0.36 the log2 of the ratio of mean CPM; the same six libraries; lower in all four knockout libraries than in both wild-type libraries), LOWER IN SIGN ONLY: inside the single-gene null (p about 0.30) (null not defined in the held files; an expression-matched empirical null gave 0.33 to 0.35 on recompute; a Welch t-test on log2(CPM+1) would give about 0.03 and is not meaningful with 2 wild-type libraries)")

e("T05", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "(the earlier card E03 prints -0.34 for the same comparison; the two runs differ in method and the difference is not reconciled here)",
  "(the earlier card E03 prints -0.34 for the same comparison: the two values differ by normalisation and by the statistic; with 4 against 2 libraries no rank test can reach a two-sided P below 0.13, so 'inside the null' reflects the size of the shift and the small n)")

e("T06", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "The PDK set as a whole is indistinguishable from chance.",
  "The PDK set as a whole is indistinguishable from chance (the set is not defined in the held files; PDK1 to PDK4 unweighted mean of the four printed log2 shifts +0.11, +0.15 on the ratio of mean CPM; random 4-gene sets of similar expression give a mean shift as large in absolute value in about 55 to 65 percent of draws, depending on the statistic), but it hides opposite signs (log2, median-of-ratios): PDK1 -0.39, PDK2 -0.17, PDK3 +0.59 (higher in all four knockout libraries, in the authors' up list, nominal P 7.39E-03, adjusted P 5.65E-02, above 0.05), PDK4 +0.40; a statement of no support for a raised PDK is not a statement about PDK3.")

e("T07", "L01_nrf2_axis", "replace",
  "P2RY12 0: no cytokine-expressing compartment.",
  "P2RY12 0: IL6 and P2RY12 not detected, IL1B and TNF at or near zero (0 to 11 and 0 to 1 counts per library), while other cytokines (TGFB1, MIF, IL33, CSF1) are expressed and weak AIF1 and CD68 signal is present, so a cytokine-expressing or myeloid-like compartment is not excluded.")

e("T08", "L01_nrf2_axis", "replace",
  "HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x: no coherent NRF2 signature.",
  "HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x (higher on group means, and above both wild-type libraries in 3 of 4 knockout libraries, not 4): mixed direction in the named panel, so no coherent NRF2 signature by that criterion; outside the named genes GSTP1, PRDX1, TXNRD1, PGD, FTH1 and GCLM are also lower in all four knockout libraries than in both wild-type libraries, and FTL in 3 of 4 (ratios 0.76 to 0.91; FTL 0.81) and GCLC is 1.14 times. The ratios here are of mean CPM; with median-of-ratios normalisation NFE2L2, KEAP1, NQO1, G6PD, SLC7A11 and BACH1 are 0.73, 0.90, 0.71, 0.73, 0.64 and 0.72, and HMOX1, SRXN1 and GSR are 1.61, 1.29 and 1.17; the authors' list value for NFE2L2, log2FC -0.58, differs from the mean-ratio value -0.41 because it is a DESeq2 estimate.")

e("T09", "L01_nrf2_axis", "replace",
  "only NFE2L2 is in the authors' DE list (padj 1.43E-02, log2FC -0.58, above the stated alpha 0.01); NQO1 0.73x and HMOX1 1.67x are in neither list.",
  "NFE2L2 (adjusted P 1.43E-02, log2FC -0.58) and G6PD (adjusted P 7.15E-03, log2FC -0.42) are in the authors' DE list, as are GSTP1 (4.38E-03) and PRDX1 (2.44E-02), both lower; the lists are cut at nominal P below 0.01 and fold change above 1.2 (adjusted P up to 0.068), which is why NFE2L2 is in them above the stated alpha 0.01; NQO1 0.73x, HMOX1 1.67x and the other genes named in this note are in neither list.")

e("T10", "L01_nrf2_axis", "replace",
  "the figure shows Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark.",
  "the figure was read by eye as Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark; the figure image is no longer held (the figure folders are empty on 2026-11-25), so the two readings cannot be re-checked; the Il6 reading sits slightly below the text's more than 1.5 fold; no significance is claimed for Tnf-a.")

e("T11", "L01_nrf2_axis", "replace",
  "2-week-old KO versus Cre-positive littermates, n 4 v 4;",
  "2-week-old KO versus Cre-positive littermates, n 4 v 4 mice (hippocampal tissue; the qRT-PCR wells are technical triplicates and the biological unit is the mouse);")

e("T12", "L01_nrf2_axis", "append",
  "absence of a significance mark is not absence of an effect.",
  " Loss of Wwox mRNA or protein is not shown in this paper for these animals; the same assay (qRT-PCR on hippocampal tissue, 2-week-old knockout against wild type) does detect changes in Grin2c, Grm3 and Kcna2 (n 4 v 4, Fig 6D legend, from hippocampi 'freshly dissected from a separate set' of mice, separate from the neurosphere donors); whether these are the same four animals as Fig 4E is not stated.")

e("T13", "F02_myelination_activity_sign", "replace",
  "PDGFRA and OLIG1 are nominally higher in knockouts, SOX10, MOG and OLIG2 are not; counts are very low and composition differs; a week-15 organoid has no compact myelin. Not myelin evidence.",
  "PDGFRA is higher in all four knockout libraries (about 8.8 times mean CPM, 2.6 against 0.3; in the authors' up list, adjusted P 6.55E-03) and OLIG1 is higher from very low counts (4 to 33 against 1 to 2; in neither list); SOX10, MOG and OLIG2 show no clear difference (ratios 1.13, 1.03, 1.25; none in either list; SOX10 has 2 to 7 raw counts per library, so no power); counts are very low for these five and composition differs; PLP1 and MBP, not in this panel, are also higher on group means (1.88 and 1.79 times; PLP1 above both wild-type libraries in 4 of 4 knockout libraries but not in either list, with one knockout library at 198 CPM; MBP above both wild-type libraries in 3 of 4 and in the authors' up list, adjusted P 4.46E-02) and are not low (PLP1 49 to 198 CPM). That a week-15 organoid has no compact myelin is background knowledge, not stated in a held source. Not myelin evidence.")

e("T14", "J01_glial_reactivity_modulation", "replace",
  "(P2RY12, CX3CR1, PTPRC, TREM2) so the tissue cannot test a microglial arm;",
  "(P2RY12, CX3CR1, PTPRC, TREM2; these are microglial or myeloid markers, PTPRC being a pan-leukocyte marker, which is general knowledge and not settled by a held source; AIF1 and CD68 are detectable at 3.8 to 14.6 and 8.8 to 38 CPM) so the tissue cannot test a microglial arm;")

e("T15", "J01_glial_reactivity_modulation", "replace",
  "of seven reactive-pan genes above 5 CPM only VIM and CD44 are raised (both radial-glia or progenitor associated), SERPINA3, TIMP1 and SOCS3 are lower, C3 and STAT3 not separated;",
  "of seven reactive-pan genes above 5 counts (the unit is counts; SERPINA3 is 0.4 to 3 CPM and C3 1.5 to 7.6 CPM) only VIM and CD44 are raised (a radial-glia or progenitor association of the two is not stated in a held source; one reader's check of an unperturbed cortical spheroid time course from another laboratory, GSE150123, found CD44 rising with culture age, rho +0.92, recomputed by a second blind reader), SERPINA3, TIMP1 and SOCS3 are lower, C3 is not separated, and STAT3 is higher in all four knockout libraries (1.46 times, in the authors' up list, adjusted P 5.74E-03) but below the 1.5-fold cut of the declared rule;")

e("T16", "J01_glial_reactivity_modulation", "replace",
  "Not a gliosis measurement and not myelin or seizure evidence.",
  "GFAP RNA is not raised (ratio 0.88; median-of-ratios 0.84; in neither list) and the article's week-15 qPCR for GFAP is flat (by eye about 1.1 against 1.0, no mark, n 4 v 4, one batch), while S100B and AQP4 are higher at week 15 (by eye about 2.7 and 2.4, one asterisk). The week-15 GFAP immunofluorescence (Fig 3A) is one unquantified representative field per genotype, by eye somewhat brighter in the knockout, and S100beta is the clearer difference. The authors write that GFAP also marks radial glia at week 15; GFAP rises clearly only later (week-24 qPCR, by eye about 26-fold; immunoblot at week 20 or 24). So at week 15 RNA and the qPCR are flat for GFAP and the protein evidence is weak, not clearly higher. Not a gliosis measurement and not myelin or seizure evidence.")

e("T17", "J01_glial_reactivity_modulation", "replace",
  "No Wwox signal was seen in Iba1-positive microglia by that assay; astrocyte-specific deletion was scored for delay, weight and survival (control 8, knockout 9) with no abnormality, and the paper does not report GFAP or Iba1 immunoreactivity, EEG or seizures for it; the authors say a cell-autonomous astroglial function is not excluded.",
  "In the wild-type rat (postnatal day 21; one double-staining panel, Fig 6D, two fields (cortex layer V and corpus callosum), representative of three independent experiments, no count) no Wwox signal was seen in Iba1-positive microglia by that assay, while Wwox signal was seen in neurons, oligodendrocytes and astrocytes in sibling panels A to C of the same figure (same age and sex, postnatal day 21 male wild-type rats; the legend does not say they are the same sections) (no Wwox-null section control in that figure; elsewhere in the paper the antibody was run on Wwox-mutant lde/lde rats: no immunoblot band at the wild-type position, though an extremely weak band of slightly different mobility remains (Fig 2A and B), and no intense signal in lde/lde cortex layer V and corpus callosum (Fig 2C), where the authors also describe a slight residual immunofluorescence); in the mouse, astrocyte-specific (GFAP-Cre) deletion was scored for delay, weight and survival (control 8, knockout 9, the n of the weight and appearance panels; survival n not separately stated; log-rank P 1.0 is reported) with no abnormality; GFAP staining is shown only to mark astrocytes for the WWOX-loss validation (Supplementary Fig 1F, one representative field, day 18), and no GFAP or Iba1 reactivity measure, EEG or seizure record is reported for it; the authors write that they cannot exclude cell-autonomous functions of WWOX in oligodendrocytes or astrocytes in other neurological disorders.")

e("T18", "J01_glial_reactivity_modulation", "replace",
  "Area fraction, not cell number; dentate gyrus unmarked;",
  "Area fraction, not cell number (IBA1 n 6 against 6, GFAP n 8 knockout against 6 wild type, mice; whole hippocampus IBA1 p below .005 and GFAP +30 percent, p below .05; CA1 and CA3 GFAP +36 and +53 percent); dentate gyrus 'marginal' in the text and not marked as significant;")

e("T19", "J01_glial_reactivity_modulation", "replace",
  "and Fig 4E shows Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark;",
  "and Fig 4E was read by eye on 2026-10-31 as Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark (the figure image is no longer held, so the two readings cannot be re-checked; the Il6 reading sits slightly below the text's more than 1.5 fold; no significance is claimed for Tnf-a; loss of Wwox mRNA or protein is not shown for these animals in this paper);")

e("T20", "K01_hif_axis_glycolytic_shift", "replace",
  "HIF1A mRNA 0.84 times (flat, as expected for a protein-level axis); PDK1 0.78 times.",
  "HIF1A mRNA 0.84 times (not in the authors' list and lower in 3 of 4 knockout libraries, so 'flat' here means not in the list; as expected for a protein-level axis); PDK1 0.78 times (lower in all four knockout libraries; not in the list). All printed ratios are ratios of mean CPM; with median-of-ratios normalisation they are 3.70, 4.60, 2.59 and 1.42 for EPAS1, HK2, SLC2A1 and ARNT.")

e("T21", "K01_hif_axis_glycolytic_shift", "replace",
  "the glycolytic genes also fall with elapsed culture time in unperturbed spheroids,",
  "HK2, SLC2A1, LDHA and DDIT4 also fall with elapsed culture time in unperturbed human cortical spheroids (GSE150123, another laboratory, 62 libraries, day 25 to 652; one reader's computation: median CPM from day 220 on is 0.37 to 0.42 of that up to day 80, Spearman rho -0.46 to -0.60), but ADM (rho -0.08), BHLHE40 (-0.00) and EGLN3 (+0.38, rises) do not, and P4HA1 (-0.23, median ratio 0.71) and ANKRD37 (-0.40, median ratio 0.62) fall less than the four above; among genes not raised in the knockout, checked against culture age by a second reader, PGK1 has rho -0.01, ALDOA -0.22, ENO1 -0.26, PKM +0.01, PFKP +0.23, NDRG1 +0.14, CA9 +0.25 and HIF1A -0.06, while PDK1 falls with culture age (rho -0.45, median ratio 0.62, much as ANKRD37), and EPAS1 itself rises with culture age (rho +0.44, median ratio 3.9),")

e("T22", "K01_hif_axis_glycolytic_shift", "replace",
  "(MYC +0.56 log2)",
  "(MYC +0.56 log2 of the ratio of mean median-of-ratios counts, +0.61 with CPM; not in the authors' list)")

e("T23", "K01_hif_axis_glycolytic_shift", "replace",
  "against the observed +2.18, +1.40 and +0.75,",
  "against the observed +2.18, +1.40 and +0.75 (mean log2 of CPM plus 1; a recompute gives +2.17, +1.38 and +0.74, the printed values differing by up to 0.02; the authors' list gives log2 fold changes of 2.46, 1.44 and 0.91),")

e("T24", "K01_hif_axis_glycolytic_shift", "replace",
  "(a driver-expressed transgene, whose level reports protein stability and not transcription), and the stock table lists a GFP-tagged sima PBac line (BDSC 42672)",
  "(read as a driver-expressed transgene, whose level would report protein stability and not transcription, if the Methods' UAS name is meant; the genotype table of the supplement shows no UAS element for this reporter and the stock is PBac{sima-GFP.AC.FPTB}VK00037 (BDSC 42672), a PBac-inserted GFP-tagged sima transgene at a landing site on chromosome 2, carried in one copy (sima:GFP/+) in addition to the endogenous sima (by the stock name; the paper's 'endogenously tagged' is not substantiated by the stock table), so the Methods' UAS name is not matched and this reading is one of two)")

e("T25", "K01_hif_axis_glycolytic_shift", "replace",
  "Sima is the single fly HIF-alpha, so no HIF-1 versus HIF-2 split is possible. The authors attribute the lactate rise to Atf4, not to sima. The only neural HIF-alpha protein readout in a WWOX-loss model, invertebrate, and not evidence of absence in mammals.",
  "The paper calls sima the fly HIF1-alpha orthologue; whether it is the single fly HIF-alpha, and so whether a HIF-1 versus HIF-2 split is possible, is not stated in the held paper. The authors suggest Atf4, not sima, as the likely route to the Ldh and lactate rise (hedged in the Results, 'could be the mechanism'; the Discussion is stronger: 'our data suggest that Atf4, rather than the HIF1alpha orthologue sima, is primarily responsible'). Invertebrate, and not evidence of absence in mammals; that it is the only neural HIF-alpha protein readout in a WWOX-loss model is a literature-scope statement that no held file supports. Readout: fluorescence averaged over four regions of 415.1 square micrometres per unfixed brain (as the Methods describe it, not whole-brain fluorescence), day-14 females; the replicate unit is the brain (P 0.5185 fits 7 and 9 brains, 14 degrees of freedom). Knockdown check: Wwox mRNA in fly heads by qPCR (Supplementary Fig 1; three replicates of 15 heads, newly eclosed, no amyloid, so not matched in age or background), and an effect of the same manipulation at day 14 (Atf4 immunostain higher in the same tissue, P 0.0022; lactate in pooled heads). No control shows that the reporter can move (no hypoxia and no sima manipulation; searched hypox and sima over the main text and the supplement text, 2026-11-25).")

e("T26", "M01_neurogenic_output_myc_window", "replace",
  "SCAR12 overlaps the wild-type lower tail. Protein-level, small organoid numbers, one laboratory.",
  "SCAR12's lower whisker overlaps the wild-type interquartile range (by eye). A second by-eye reading of the Fig 3K medians gave about 67 for knockout and 47 for SCAR12. Protein-level; n 7, 5, 8 and 11 organoids for wild type, knockout, SCAR12 and WOREE, with more plotted points than organoids and the unit of the points not stated; one laboratory (not checked).")

e("T27", "M01_neurogenic_output_myc_window", "replace",
  "In SCAR12 the radial-glia fraction is wild-type-like and the single-cell neuron-cluster fraction is not reduced (DA-M01-003; WOREE shows reduced CTIP2 and SATB2, Fig 6B, so SCAR12 is the clean dissociation case), so the MYC rise is present without that composition phenotype.",
  "In SCAR12 the week-16 single-cell radial-glia and neuron-cluster fractions are wild-type-like (DA-M01-003) and CTIP2 and SATB2 are wild-type-like (Fig 6B; WOREE shows reduced CTIP2 and SATB2), but the week-7 immunostaining shows SOX2-positive cells increased (median about 47 against about 13 percent) and SATB2-positive cells decreased against wild type (Fig 1F, by eye); MYC (Fig 3K, week 16) is raised in all three lines, so SCAR12 is a partial dissociation, not a clean one (the readouts and weeks differ: week-7 immunostaining and week-16 single-cell RNA sequencing and CTIP2 and SATB2 immunostaining; whether it is time-dependent is not shown).")

e("T28", "M01_neurogenic_output_myc_window", "replace",
  "(death by four weeks is stated for nestin-Cre; the Synapsin-Cre survival age is not stated); that progenitors are largely WWOX-intact under Synapsin-Cre is an inference, not a measurement; oligodendrocyte and astrocyte deletion do not.",
  "(death by 3 to 4 weeks is stated for nestin-Cre, 100 percent, n 14, and for Synapsin-Cre, n 15, Fig 1I); that progenitors are largely WWOX-intact under Synapsin-Cre is an inference, not a measurement (WWOX loss was measured in NeuN-positive neurons and WWOX was intact in CC1-positive oligodendrocytes of Synapsin-Cre mice; progenitors were not stained); oligodendrocyte and astrocyte deletion do not reproduce growth retardation or premature death (measured: delay, weight and survival for both lines; for the oligodendrocyte deletion only, hind-limb clasping at postnatal day 18 and MBP staining at postnatal day 17, 'no major changes' in the latter, Supplementary Figs 2D and 8), seizures were not recorded for them and the authors state no phenotypic abnormalities; their WWOX loss is shown in one representative field each at day 18 (Supplementary Fig 1E, 1F; by eye, WWOX signal in the astrocyte-control field is itself faint and some WWOX-positive cells remain in the oligodendrocyte-knockout field, so deletion efficiency is not quantified), while the survival curves of the oligodendrocyte-deletion and astrocyte-deletion lines run to about 120 days (by eye, Fig 1L and 1O).")

e("T29", "F01_glutamate_receptor_node", "replace",
  "(cumulative distributions, KS test on pooled events;",
  "(cumulative distributions, KS test, taken here as on pooled events: the paper says only KS test on cumulative plots and the very small P values imply events as the unit;")

e("T30", "F01_glutamate_receptor_node", "replace",
  "frequency is not different from the heterozygote but does differ from wild type (KS P about 2.4e-4; direction not stated in the text);",
  "frequency is not different from the heterozygote but does differ from wild type (KS P about 2.4e-4; direction not stated in the text and not readable by eye from the curves); the heterozygote itself also differs from wild type in amplitude (P about 2.0e-4) and in frequency (P about 0.0018), so the frequency difference between knockout and wild type is shared with the heterozygote and cannot be assigned to complete loss specifically (with 4 wild-type animals, animal or litter differences are also possible);")

e("T31", "F01_glutamate_receptor_node", "append",
  "a residual NMDAR component is not excluded and no NMDAR current was measured.",
  " The incubation ACSF contains 1.3 millimolar MgSO4; the recording perfusate is not described separately. An NMDAR-dependent component is shown elsewhere in the paper (the delayed evoked field response is suppressed by d-APV, Supplementary Fig S3C, 6 slices from 3 animals); spontaneous excitatory currents are said to be 'isolated by voltage-clamping pyramidal neurons' at minus 70 millivolts with a K-gluconate pipette solution, and the miniature currents were recorded at the same potential with TTX added; for these whole-cell recordings no GABA-A, AMPA or NMDA antagonist is named (searched picrotoxin, bicuculline, gabazine, CNQX, NBQX, DNQX: none; d-APV appears only in the field-potential experiments). Loss of the target protein is not shown in this paper (the floxed allele and Cre line are cited; the knockout characterisation is in another paper), but an effect of the same manipulation in the same preparation is shown (the amplitude shift itself; sIPSC reduction in amplitude and frequency, Fig 4G-H, recorded in other cells: S-KO n 9 cells from 5 animals, with a high-chloride pipette solution). The text cites Fig 4C for amplitude where the legend assigns amplitude to 4B and frequency to 4C.")

e("T10b", "L01_nrf2_axis", "replace",
  "Il6 is the only significant cytokine; Tnf-a is a non-significant increase.",
  "The text marks only Il6 as significant; Tnf-a carried no mark in the earlier by-eye reading, which cannot be redone now.")

e("T19b", "J01_glial_reactivity_modulation", "replace",
  "which their significance mark does not support;",
  "which the text's own significance statement (Il6 only) does not support for Tnf-a (n 4 v 4 gives little power, so absence of significance is not absence of effect);")

e("T19c", "J01_glial_reactivity_modulation", "append",
  "leaves cause versus consequence open.",
  " Its Discussion nevertheless writes of 'the epileptic phenotype observed in these mice', with no measurement in this paper (its Introduction cites earlier reports for epileptogenesis in Wwox-deleted mice).")

e("T25b", "K01_hif_axis_glycolytic_shift", "replace",
  "normoxia, not measured without the transgene or under hypoxia",
  "oxygen conditions not stated (flies at 25 degrees Celsius, 12 hours light and 12 dark), not measured without the transgene or under hypoxia")
