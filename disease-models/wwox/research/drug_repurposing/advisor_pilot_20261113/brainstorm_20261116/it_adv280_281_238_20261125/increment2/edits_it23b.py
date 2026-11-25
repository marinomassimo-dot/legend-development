"""IT 2026-11-25 (IT23, increment 2): proposed wording for SCI's ADV-282 null-note audit (13 disease-assertion notes in eight cards).
Same schema as edits_it23.py. Data only; applied by apply_it23b.py after the blind check. Hypothesis level; nothing here is medical advice."""
EDITS = []
def e(i, card, mode, old, new): EDITS.append(dict(id=i, card=card, mode=mode, old=old, new=new, sources=[]))

# ---- DA-GSE-PDK-003 (E03)
e("T01", "E03_pdk_inhibition_dca", "replace",
  "PDK1 -0.34, lower in sign only (the IT5 same-sets re-analysis gives -0.39, inside the single-gene null, p about 0.30;",
  "PDK1 -0.34 with CPM normalisation (-0.39 with median-of-ratios normalisation, which is the IT5 same-sets re-analysis, same six libraries; lower in all four knockout libraries than in both wild-type libraries but lower in sign only, inside the single-gene null, p about 0.30, where the null is not defined in the held files, an empirical version gives 0.27 to 0.39, and with 4 against 2 libraries no rank test can reach a two-sided P below 0.13;")
e("T02", "E03_pdk_inhibition_dca", "replace",
  "the PDK/PDH set +0.17 (P 0.22, not different from chance);",
  "the PDK/PDH set +0.17 (P 0.22 from the repository's own set test, rerun at 0.2265; the set is not named in the held files and a second reader's random sets of plausible membership gave P 0.33 to 0.81; the set mean averages away PDHA1, PDPR and LDHA, which are in the authors' up list at adjusted P 5.8E-10, 1.3E-04 and 4.9E-06, and PDK3, higher in all four knockout libraries at 1.55 times, nominal P 7.39E-03, adjusted P 5.65E-02);")
e("T03", "E03_pdk_inhibition_dca", "replace",
  "LDH-to-PDH ratio not shifted (inside the spread of the two wild-type libraries).",
  "the LDH-to-PDH transcript ratio depends on the pairing (log2 of (LDHA+LDHB) over (PDHA1+PDHB+DLAT+DLD), knockout minus wild type, -0.14; LDHA over PDHA1 0.72 against 0.86, three of four knockout libraries below both wild-type libraries; LDHA over (PDHA1+PDHB) 0.54 against 0.56), and no pairing was fixed in advance in the held sources.")

# ---- DA-I01-001 (I01)
e("T04", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "PDK1 -0.39, LOWER IN SIGN ONLY:",
  "PDK1 -0.39 (median-of-ratios normalisation; -0.34 with CPM normalisation, the same six libraries; lower in all four knockout libraries than in both wild-type libraries), LOWER IN SIGN ONLY:")
e("T05", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "(the earlier card E03 prints -0.34 for the same comparison; the two runs differ in method and the difference is not reconciled here)",
  "(the earlier card E03 prints -0.34 for the same comparison: the two values differ by normalisation, CPM against median-of-ratios, not by result; with 4 against 2 libraries no rank test can reach a two-sided P below 0.13, so 'inside the null' reflects the size of the shift and the small n)")
e("T06", "I01_pdk_inhibition_dca_premise_seizure_glycaemia", "replace",
  "The PDK set as a whole is indistinguishable from chance.",
  "The PDK set as a whole is indistinguishable from chance (the set is not defined in the held files; PDK1 to PDK4 mean shift +0.10), but it hides opposite signs (log2, median-of-ratios): PDK1 -0.39, PDK2 -0.17, PDK3 +0.59 (higher in all four knockout libraries, nominal P 7.39E-03, adjusted P 5.65E-02), PDK4 +0.40; a statement of no support for a raised PDK is not a statement about PDK3.")

# ---- DA-L01-003 (L01)
e("T07", "L01_nrf2_axis", "replace",
  "P2RY12 0: no cytokine-expressing compartment.",
  "P2RY12 0: no detectable IL1B, IL6 or TNF transcript and no P2RY12, while other cytokines (TGFB1, MIF, IL33, CSF1) are expressed and weak AIF1 and CD68 signal is present, so a cytokine-expressing or myeloid-like compartment is not excluded.")
e("T08", "L01_nrf2_axis", "replace",
  "HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x: no coherent NRF2 signature.",
  "HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x (higher on group means, and above both wild-type libraries in 3 of 4 knockout libraries, not 4): mixed direction in the named panel, so no coherent NRF2 signature by that criterion; outside the named genes GSTP1, PRDX1, TXNRD1, PGD, FTH1, FTL and GCLM are also lower in all four knockout libraries (ratios 0.76 to 0.91) and GCLC is 1.14 times.")
e("T09", "L01_nrf2_axis", "replace",
  "only NFE2L2 is in the authors' DE list (padj 1.43E-02, log2FC -0.58, above the stated alpha 0.01); NQO1 0.73x and HMOX1 1.67x are in neither list.",
  "NFE2L2 (adjusted P 1.43E-02, log2FC -0.58) and G6PD (adjusted P 7.15E-03, log2FC -0.42) are in the authors' DE list, as are GSTP1 (4.38E-03) and PRDX1 (2.44E-02), both lower; the lists are cut at nominal P below 0.01 and fold change above 1.2 (adjusted P up to 0.068), which is why NFE2L2 is in them above the stated alpha 0.01; NQO1 0.73x, HMOX1 1.67x and the other genes named in this note are in neither list.")

# ---- DA-L01-001 (L01)
e("T10", "L01_nrf2_axis", "replace",
  "the figure shows Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark.",
  "the figure was read by eye as Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark; the figure image is no longer held (the figure folders are empty on 2026-11-25), so the two readings cannot be re-checked and sit slightly against the text's more than 1.5 fold for both; no significance is claimed for Tnf-a.")
e("T11", "L01_nrf2_axis", "replace",
  "2-week-old KO versus Cre-positive littermates, n 4 v 4;",
  "2-week-old KO versus Cre-positive littermates, n 4 v 4 mice (hippocampal tissue, triplicate wells);")
e("T12", "L01_nrf2_axis", "append",
  "absence of a significance mark is not absence of an effect.",
  " Loss of Wwox mRNA or protein is not shown in this paper for these animals; the same assay and animal group does detect changes in Grin2c, Grm3 and Kcna2 (n 4 v 4, Fig 6D legend), whether in the same four animals is not stated.")

# ---- DA-W2-012 (F02)
e("T13", "F02_myelination_activity_sign", "replace",
  "PDGFRA and OLIG1 are nominally higher in knockouts, SOX10, MOG and OLIG2 are not; counts are very low and composition differs; a week-15 organoid has no compact myelin. Not myelin evidence.",
  "PDGFRA is higher in all four knockout libraries (about 8.8 times mean CPM, 2.6 against 0.3; in the authors' up list, adjusted P 6.55E-03) and OLIG1 is higher from very low counts (4 to 33 against 1 to 2; in neither list); SOX10, MOG and OLIG2 are not different (ratios 1.13, 1.03, 1.25); counts are very low for these five and composition differs; PLP1 and MBP, not in this panel, are also higher (1.88 and 1.79 times; MBP in the authors' up list, adjusted P 4.46E-02) and are not low (PLP1 49 to 198 CPM). That a week-15 organoid has no compact myelin is background knowledge, not stated in a held source. Not myelin evidence.")

# ---- DA-J01-007 (J01)
e("T14", "J01_glial_reactivity_modulation", "replace",
  "(P2RY12, CX3CR1, PTPRC, TREM2) so the tissue cannot test a microglial arm;",
  "(P2RY12, CX3CR1, PTPRC, TREM2; these are microglia-specific markers, and AIF1 and CD68 are detectable at 3.8 to 14.6 and 8.8 to 38 CPM) so the tissue cannot test a microglial arm;")
e("T15", "J01_glial_reactivity_modulation", "replace",
  "of seven reactive-pan genes above 5 CPM only VIM and CD44 are raised (both radial-glia or progenitor associated), SERPINA3, TIMP1 and SOCS3 are lower, C3 and STAT3 not separated;",
  "of seven reactive-pan genes above 5 counts (the unit is counts; SERPINA3 is 0.4 to 3 CPM and C3 1.5 to 7.6 CPM) only VIM and CD44 are raised (a radial-glia or progenitor association of the two is not stated in a held source; one reader's check of an unperturbed cortical spheroid time course from another laboratory, GSE150123, found CD44 rising with culture age, rho +0.92, not recomputed), SERPINA3, TIMP1 and SOCS3 are lower, C3 is not separated, and STAT3 is higher in all four knockout libraries (1.46 times, in the authors' up list, adjusted P 5.74E-03) but below the 1.5-fold cut of the declared rule;")
e("T16", "J01_glial_reactivity_modulation", "replace",
  "Not a gliosis measurement and not myelin or seizure evidence.",
  "GFAP RNA is not raised (ratio 0.88, in neither list) although the article's own GFAP immunofluorescence at week 15 is higher (Fig 3A) and its week-15 qPCR for GFAP is flat, so RNA is silent on GFAP while protein is not. Not a gliosis measurement and not myelin or seizure evidence.")

# ---- DA-J01-006 (J01)
e("T17", "J01_glial_reactivity_modulation", "replace",
  "No Wwox signal was seen in Iba1-positive microglia by that assay; astrocyte-specific deletion was scored for delay, weight and survival (control 8, knockout 9) with no abnormality, and the paper does not report GFAP or Iba1 immunoreactivity, EEG or seizures for it; the authors say a cell-autonomous astroglial function is not excluded.",
  "In the wild-type rat (postnatal day 21; one double-staining image, representative of three independent experiments, no count) no Wwox signal was seen in Iba1-positive microglia by that assay, while Wwox signal was seen in neurons, oligodendrocytes and astrocytes of the same sections (no Wwox-null section control in that figure); in the mouse, astrocyte-specific (GFAP-Cre) deletion was scored for delay, weight and survival (control 8, knockout 9, the n of the weight and appearance panels; survival n not separately stated) with no abnormality; GFAP staining is shown only to mark astrocytes for the WWOX-loss validation (Supplementary Fig 1F, one representative field, day 18), and no GFAP or Iba1 reactivity measure, EEG or seizure record is reported for it; the authors write that they cannot exclude cell-autonomous functions of WWOX in oligodendrocytes or astrocytes in other neurological disorders.")

# ---- DA-J01-002 (J01)
e("T18", "J01_glial_reactivity_modulation", "replace",
  "Area fraction, not cell number; dentate gyrus unmarked;",
  "Area fraction, not cell number (IBA1 n 6 against 6, GFAP n 8 knockout against 6 wild type, mice); dentate gyrus 'marginal' in the text and not marked as significant;")
e("T19", "J01_glial_reactivity_modulation", "replace",
  "and Fig 4E shows Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark;",
  "and Fig 4E was read by eye on 2026-10-31 as Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark (the figure image is no longer held, so the two readings cannot be re-checked and sit slightly against the text's more than 1.5 fold for both; no significance is claimed for Tnf-a; loss of Wwox mRNA or protein is not shown for these animals in this paper);")

# ---- DA-K01-002 (K01)
e("T20", "K01_hif_axis_glycolytic_shift", "replace",
  "HIF1A mRNA 0.84 times (flat, as expected for a protein-level axis); PDK1 0.78 times.",
  "HIF1A mRNA 0.84 times (not in the authors' list and lower in 3 of 4 knockout libraries, so 'flat' here means not in the list; as expected for a protein-level axis); PDK1 0.78 times (lower in all four knockout libraries; not in the list). All printed ratios are ratios of mean CPM; with median-of-ratios normalisation they are 3.70, 4.60, 2.59 and 1.42 for EPAS1, HK2, SLC2A1 and ARNT.")
e("T21", "K01_hif_axis_glycolytic_shift", "replace",
  "the glycolytic genes also fall with elapsed culture time in unperturbed spheroids,",
  "HK2, SLC2A1, LDHA and DDIT4 also fall with elapsed culture time in unperturbed human cortical spheroids (GSE150123, another laboratory, 62 libraries, day 25 to 652; one reader's computation: median CPM from day 220 on is 0.37 to 0.42 of that up to day 80, Spearman rho -0.46 to -0.60), but ADM, BHLHE40, P4HA1, ANKRD37 and EGLN3 do not (rho -0.40 to +0.38; EGLN3 rises) and the flat genes were not checked there,")
e("T22", "K01_hif_axis_glycolytic_shift", "replace",
  "(MYC +0.56 log2)",
  "(MYC +0.56 log2 of the ratio of mean median-of-ratios counts, +0.61 with CPM; not in the authors' list)")
e("T23", "K01_hif_axis_glycolytic_shift", "replace",
  "against the observed +2.18, +1.40 and +0.75,",
  "against the observed +2.18, +1.40 and +0.75 (mean log2 of CPM plus 1; the authors' list gives log2 fold changes of 2.46, 1.44 and 0.91),")

# ---- DA-K01-008 (K01)
e("T24", "K01_hif_axis_glycolytic_shift", "replace",
  "(a driver-expressed transgene, whose level reports protein stability and not transcription)",
  "(read as a driver-expressed transgene, whose level would report protein stability and not transcription, if the Methods' UAS name is meant; the genotype table of the supplement shows no UAS element and the stock is a genomic-tagged insertion, so this reading is one of two)")
e("T25", "K01_hif_axis_glycolytic_shift", "replace",
  "Sima is the single fly HIF-alpha, so no HIF-1 versus HIF-2 split is possible. The authors attribute the lactate rise to Atf4, not to sima. The only neural HIF-alpha protein readout in a WWOX-loss model, invertebrate, and not evidence of absence in mammals.",
  "The paper calls sima the fly HIF1-alpha orthologue; whether it is the single fly HIF-alpha, and so whether a HIF-1 versus HIF-2 split is possible, is not stated in the held paper. The authors suggest Atf4, not sima, as the likely route to the Ldh and lactate rise (hedged: 'could be the mechanism'). Invertebrate, and not evidence of absence in mammals; that it is the only neural HIF-alpha protein readout in a WWOX-loss model is a literature-scope statement that no held file supports. Readout: fluorescence averaged over four regions of about 415 square micrometres per unfixed brain, day-14 females; the replicate unit is the brain (P 0.5185 fits 7 and 9 brains, 14 degrees of freedom). Knockdown check: Wwox mRNA in fly heads by qPCR (Supplementary Fig 1; three replicates of 15 heads, newly eclosed, no amyloid, so not matched in age or background), and an effect of the same manipulation at day 14 in the same tissue (Atf4 immunostain higher, P 0.0022; lactate). No control shows that the reporter can move (no hypoxia and no sima manipulation; searched hypox and sima over the main text and the supplement text, 2026-11-25).")

# ---- DA-M01-002 (M01)
e("T26", "M01_neurogenic_output_myc_window", "replace",
  "SCAR12 overlaps the wild-type lower tail. Protein-level, small organoid numbers, one laboratory.",
  "SCAR12's lower whisker overlaps the wild-type interquartile range (by eye). Protein-level; n 7, 5, 8 and 11 organoids for wild type, knockout, SCAR12 and WOREE, with more plotted points than organoids and the unit of the points not stated; one laboratory (not checked).")
e("T27", "M01_neurogenic_output_myc_window", "replace",
  "In SCAR12 the radial-glia fraction is wild-type-like and the single-cell neuron-cluster fraction is not reduced (DA-M01-003; WOREE shows reduced CTIP2 and SATB2, Fig 6B, so SCAR12 is the clean dissociation case), so the MYC rise is present without that composition phenotype.",
  "In SCAR12 the week-16 single-cell radial-glia and neuron-cluster fractions are wild-type-like (DA-M01-003) and CTIP2 and SATB2 are wild-type-like (Fig 6B; WOREE shows reduced CTIP2 and SATB2), but the week-7 immunostaining shows SOX2-positive cells increased (median about 47 against about 13 percent) and SATB2-positive cells decreased against wild type (Fig 1F, by eye); MYC (Fig 3K, week 16) is raised in all three lines, so SCAR12 is a partial, time-dependent dissociation, not a clean one.")

# ---- DA-M01-007 (M01)
e("T28", "M01_neurogenic_output_myc_window", "replace",
  "(death by four weeks is stated for nestin-Cre; the Synapsin-Cre survival age is not stated); that progenitors are largely WWOX-intact under Synapsin-Cre is an inference, not a measurement; oligodendrocyte and astrocyte deletion do not.",
  "(death by 3 to 4 weeks is stated for nestin-Cre, 100 percent, n 14, and for Synapsin-Cre, n 15, Fig 1I); that progenitors are largely WWOX-intact under Synapsin-Cre is an inference, not a measurement (WWOX loss was measured in NeuN-positive neurons and WWOX was intact in CC1-positive oligodendrocytes of Synapsin-Cre mice; progenitors were not stained); oligodendrocyte and astrocyte deletion do not reproduce growth retardation or premature death (measured: delay, weight and survival, and hind-limb clasping for the oligodendrocyte deletion), seizures were not recorded for them and the authors state no phenotypic abnormalities; their WWOX loss is shown in one representative field each at day 18 (Supplementary Fig 1E, 1F), while the survival of the null lines runs to about 120 days.")

# ---- DA-W2-002 (F01)
e("T29", "F01_glutamate_receptor_node", "replace",
  "(cumulative distributions, KS test on pooled events;",
  "(cumulative distributions, KS test, taken here as on pooled events: the paper says only KS test on cumulative plots and the very small P values imply events as the unit;")
e("T30", "F01_glutamate_receptor_node", "replace",
  "frequency is not different from the heterozygote but does differ from wild type (KS P about 2.4e-4; direction not stated in the text);",
  "frequency is not different from the heterozygote but does differ from wild type (KS P about 2.4e-4; direction not stated in the text and not readable by eye from the curves); the heterozygote itself also differs from wild type in amplitude (P about 2.0e-4) and in frequency (P about 0.0018), so the frequency difference between knockout and wild type is not a knockout effect;")
e("T31", "F01_glutamate_receptor_node", "append",
  "a residual NMDAR component is not excluded and no NMDAR current was measured.",
  " An NMDAR-dependent component is shown elsewhere in the paper (the delayed evoked field response is suppressed by d-APV, Supplementary Fig S3C, 6 slices from 3 animals); isolation from miniature inhibitory currents is not described (TTX only). Loss of the target protein is not shown in this paper (the floxed allele and Cre line are cited; the knockout characterisation is in another paper), but an effect of the same manipulation in the same cells is (amplitude shift; sIPSC changes, Fig 4H). The text cites Fig 4C for amplitude where the legend assigns amplitude to 4B and frequency to 4C.")
