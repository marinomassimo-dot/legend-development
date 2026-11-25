# Sentences to check against their sources (blind check, IT, 2026-11-25)

Repository root for relative paths: /home/desktop/legend-development/.claude/worktrees/it_23_20261125

## S01

Where: card A01_pba_class

Part under test (new wording):

> the partly trafficked branch was outside the reach of 4-PBA, not of every chemical chaperone. [IT 2026-11-25, ADV-281: the null arm is 4-PBA 1 mM for 48 h in G443D flies (Fig 6G, seizure behaviour unaltered); 10 % glycerol was also not significant in G443D flies, so no tested chaperone rescued G443D in vivo; the same 4-PBA dose reduced seizures in G443V flies (Fig 6H); 4-PBA 10 mM also did not rescue G443D uptake in HEK293 cells (Fig 3B).]

Whole field as it will read:

> MEASURED NO RESCUE (behaviour unchanged). Encoded NO_CHANGE: a reported null, not an unmeasured cell. In the same paper glycerol, an osmolyte-type chemical chaperone, did rescue G443D in vitro: the partly trafficked branch was outside the reach of 4-PBA, not of every chemical chaperone. [IT 2026-11-25, ADV-281: the null arm is 4-PBA 1 mM for 48 h in G443D flies (Fig 6G, seizure behaviour unaltered); 10 % glycerol was also not significant in G443D flies, so no tested chaperone rescued G443D in vivo; the same 4-PBA dose reduced seizures in G443V flies (Fig 6H); 4-PBA 10 mM also did not rescue G443D uptake in HEK293 cells (Fig 3B).]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID40485335_Shah2025_PMC12146831.xml
- /home/desktop/legend-development/files/figures/PMID40485335/

## S02

Where: card A02_proteasome_inhibitor_class

Part under test (new wording):

> chloroquine (20 uM, 16 h) gave little shift ('no substantial changes', Clausen Fig 3C; 'little effect', Gronbaek-Thygesen Fig 4F) and no readout in either paper shows that it blocked lysosomal degradation in these cells; proteasome-pathway perturbations shift part of the low-abundance population and the authors attribute most low-abundance variants, not all, to proteasomal degradation; the ASPA authors write that they cannot exclude a role for autophagy where expression persists longer. [IT 2026-11-25, ADV-281: no activity check for chloroquine; searched 2026-11-25.]

Whole field as it will read:

> Flow shift of a library, not a protein recovery measure; chloroquine (20 uM, 16 h) gave little shift ('no substantial changes', Clausen Fig 3C; 'little effect', Gronbaek-Thygesen Fig 4F) and no readout in either paper shows that it blocked lysosomal degradation in these cells; proteasome-pathway perturbations shift part of the low-abundance population and the authors attribute most low-abundance variants, not all, to proteasomal degradation; the ASPA authors write that they cannot exclude a role for autophagy where expression persists longer. [IT 2026-11-25, ADV-281: no activity check for chloroquine; searched 2026-11-25.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID38378758_Clausen2024_PMC10879094.xml
- /home/desktop/legend-development/files/supplement/PMID38378758/
- /home/desktop/legend-development/files/fulltext/PMID38740822_Gronbaek2024_PMC11091098.xml
- /home/desktop/legend-development/files/supplement/PMID38740822/

## S03

Where: card A02_proteasome_inhibitor_class

Part under test (new wording):

> while I278T activity was not rescued (text statement; the figure bars were not viewed), although the paper cites rescue of I278T by proteasome inhibitor treatment in yeast, human patient fibroblasts and transgenic mice (its refs 15, 25, 28); proteasome inhibitors were tested in this paper on R125Q only.

Whole field as it will read:

> Soluble protein of both alleles rose; activity of R125Q rose 5 to 7-fold to about a tenth of wild type, while I278T activity was not rescued (text statement; the figure bars were not viewed), although the paper cites rescue of I278T by proteasome inhibitor treatment in yeast, human patient fibroblasts and transgenic mice (its refs 15, 25, 28); proteasome inhibitors were tested in this paper on R125Q only. Endpoint recorded for I278T: protein up, activity unchanged (NO_CHANGE for activity). Different intervention and a cell line with strong baseline ER stress, so this is not a clean test of expression context, but it is a measured protein-up activity-flat case for a cytosolic enzyme.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID38051092_Collard2023_PMC10761163_epmc_2026-10-29.xml

## S04

Where: card E03_pdk_inhibition_dca

Part under test (new wording):

> Among the measurements retrieved, three enzyme rows record no half-maximal inhibition (IC50 above 1 mM; CHEMBL1133665, CHEMBL1132309, CHEMBL1133733, which carry identical companion values and record no top concentration), other enzyme-level rows differ (EC50 180 uM, CHEMBL5370584; EC50 5.7 mM with 64.2 % inhibition at 10 mM, CHEMBL4308888; Kd above 1 mM, CHEMBL3813671; EC50 above 100 mM, CHEMBL4732185) and

Whole field as it will read:

> Curated PDK inhibitor. Among the measurements retrieved, three enzyme rows record no half-maximal inhibition (IC50 above 1 mM; CHEMBL1133665, CHEMBL1132309, CHEMBL1133733, which carry identical companion values and record no top concentration), other enzyme-level rows differ (EC50 180 uM, CHEMBL5370584; EC50 5.7 mM with 64.2 % inhibition at 10 mM, CHEMBL4308888; Kd above 1 mM, CHEMBL3813671; EC50 above 100 mM, CHEMBL4732185) and a fibroblast lactate-oxidation effect appears at a high micromolar concentration: weak in vitro. The repository's existing safety position (peripheral neuropathy, BLOCK-1) is unchanged by this card.

Held sources:
- disease-models/wwox/research/drug_repurposing/lucas_clarke_followup_20261026/chembl_named_activities.tsv
- disease-models/wwox/research/drug_repurposing/lucas_clarke_followup_20261026/chembl_mechanisms.tsv

## S05

Where: card H01_apinocaltamide_ttype

Part under test (new wording):

> [IT 2026-11-25, ADV-281: one model only (rat amygdala kindling), known from the abstract, which gives no dose or exposure for that arm; the same abstract reports suppression of spike-wave discharges in two rat strains and reduced severity of generalized convulsive seizures in two mouse tests, the latter at higher concentration.]

Whole field as it will read:

> 'No effect on focal onset seizures' (abstract). A measured null in a seizure type that is not the WWOX provoked-seizure phenotype; shown so that the class is not read as broad-spectrum. [IT 2026-11-25, ADV-281: one model only (rat amygdala kindling), known from the abstract, which gives no dose or exposure for that arm; the same abstract reports suppression of spike-wave discharges in two rat strains and reduced severity of generalized convulsive seizures in two mouse tests, the latter at higher concentration.]

Held sources:
- /home/desktop/legend-development/files/fulltext/adv051_it_20261118/A/PMID40165594_europepmc_core.json

## S06

Where: card M01_neurogenic_output_myc_window

Part under test (new wording):

> the upper-layer marker mildly rises according to the main text, while the panel marks SATB2 in knockout against knockout plus A51 as not significant (Supplementary Fig 7F).

Whole field as it will read:

> Progenitor fractions fall, the pan-neuron fraction rises, the deep-layer marker is unchanged and the upper-layer marker mildly rises according to the main text, while the panel marks SATB2 in knockout against knockout plus A51 as not significant (Supplementary Fig 7F). The compound lowers two pathways and is not MYC-selective; percentages carry no denominators; one of three experiments without independent differentiations; no randomisation or blinding is stated for the whole study (not specific to this arm); the authors' clause is 'using multiple biological replicates' for the experiments without independent differentiations.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/

## S07

Where: card M01_neurogenic_output_myc_window

Part under test (new wording):

> the article states that no randomisation or blinding was applied (whole study, not specific to this arm); the Supplementary Fig 7 legend gives organoid numbers of 4, 4, 6 and 7 for one experiment while the panels plot more points;

Whole field as it will read:

> Progenitor fractions fall, the pan-neuron fraction rises, the deep-layer marker is unchanged and the upper-layer marker mildly rises (main text). The compound lowers two pathways and is not MYC-selective; percentages carry no denominators; one of three experiments without independent differentiations; the article states that no randomisation or blinding was applied (whole study, not specific to this arm); the Supplementary Fig 7 legend gives organoid numbers of 4, 4, 6 and 7 for one experiment while the panels plot more points; the authors' clause is 'using multiple biological replicates' for the experiments without independent differentiations.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/

## S08

Where: card M01_neurogenic_output_myc_window

Part under test (new wording):

> (the supplementary figures PDF is held since 2026-11-21 and Supplementary Fig 7F-G was viewed on 2026-11-25; other panel values remain prior-session attestations)

Whole field as it will read:

> PMID 42397075, Results and Supplementary Fig 7F-G (the supplementary figures PDF is held since 2026-11-21 and Supplementary Fig 7F-G was viewed on 2026-11-25; other panel values remain prior-session attestations); the compound arm was run in the knockout line only

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/

## S09

Where: card D01_a51

Part under test (new wording):

> The published supplementary figures are held since 2026-11-21, so the panel values can be re-read (this row's values were not re-audited on 2026-11-25); the preprint does not contain the A51 experiment.

Whole field as it will read:

> Knockout above wild type. The published supplementary figures are held since 2026-11-21, so the panel values can be re-read (this row's values were not re-audited on 2026-11-25); the preprint does not contain the A51 experiment.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/

## S10

Where: card D01_a51

Part under test (new wording):

> [IT 2026-11-25, ADV-281: the two markers are CTIP2 (Supplementary Fig 7G) and SATB2 (Fig 7F); NEUN does rise; CTIP2 is near zero in both knockout arms (about 0.1 and 0.7 % of cells by eye), so a floor limits the test; one knockout clone, one experiment, week-15 harvest.]

Whole field as it will read:

> MEASURED NO RECOVERY: knockout-versus-treated not significant for both markers, CTIP2 remaining far below wild type. Encoded NO_CHANGE; it stays UNRESOLVED because the single disease assertion is on a different endpoint (gap G-2). This row is the split that the first row hides. [IT 2026-11-25, ADV-281: the two markers are CTIP2 (Supplementary Fig 7G) and SATB2 (Fig 7F); NEUN does rise; CTIP2 is near zero in both knockout arms (about 0.1 and 0.7 % of cells by eye), so a floor limits the test; one knockout clone, one experiment, week-15 harvest.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/

## S11

Where: card E01_isr_modulators

Part under test (new wording):

> [IT 2026-11-25, ADV-281: knockdown was verified by head qPCR in newly eclosed females only (about 0.55 of control, 3 pools; Supplementary Fig 1), not at day 14; Atf4 staining in the LacZ background is near blank in both genotypes (Supplementary Fig 5D), so the null may sit at the detection floor; the two backgrounds were tested with different tests.]

Whole field as it will read:

> Not significant without amyloid (t 0.0894, P 0.9305, n 6 brains; 95% interval about plus or minus 1.3 pooled SD). A measured non-significant result in a different contrast, not an unmeasured cell and not a demonstrated absence; no interaction test between the two backgrounds is reported (re-read 2026-10-28). [IT 2026-11-25, ADV-281: knockdown was verified by head qPCR in newly eclosed females only (about 0.55 of control, 3 pools; Supplementary Fig 1), not at day 14; Atf4 staining in the LacZ background is near blank in both genotypes (Supplementary Fig 5D), so the null may sit at the detection floor; the two backgrounds were tested with different tests.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42909904_PMC13684411.xml
- /home/desktop/legend-development/files/fulltext/PMID42909904_LucasClarke2026_BrainComms_fcag385.pdf
- /home/desktop/legend-development/files/fulltext/PMID42909904_supplement/

## S12

Where: card C04_aav9_endpoint_families

Part under test (new wording):

> [IT 2026-11-25, ADV-281: Fig 3E, postnatal day 10, Student t tests without multiplicity correction; the reference-item knockout arm (about 95 mg/dL) differs from wild type (about 129 mg/dL) at one star only; about 11 high-dose and 8 knockout points counted on the plot (no n in the legend): 'not significant against the untreated knockout' is not evidence of no effect.]

Whole field as it will read:

> High dose about 113: not significant against wild type and not significant against the untreated knockout. The text says both doses partially corrected hypoglycaemia; the panel qualifies the text (entries 36, 37). [IT 2026-11-25, ADV-281: Fig 3E, postnatal day 10, Student t tests without multiplicity correction; the reference-item knockout arm (about 95 mg/dL) differs from wild type (about 129 mg/dL) at one star only; about 11 high-dose and 8 knockout points counted on the plot (no n in the legend): 'not significant against the untreated knockout' is not evidence of no effect.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42422765_Obeid2026_PMC_r2.xml
- /home/desktop/legend-development/files/figures/PMID42422765_r2/

## S13

Where: card C04_aav9_endpoint_families

Part under test (new wording):

> [IT 2026-11-25, ADV-281: Fig 3E; about 7 low-dose and 8 knockout points counted on the plot; at day 10 the low dose shows no visible body-weight difference either (Fig 3C) and its WWOX expression is shown at day 30 only, so this null precedes any demonstration that the dose acts at that age.]

Whole field as it will read:

> Low dose about 105: not significant against wild type and not significant against the untreated knockout. [IT 2026-11-25, ADV-281: Fig 3E; about 7 low-dose and 8 knockout points counted on the plot; at day 10 the low dose shows no visible body-weight difference either (Fig 3C) and its WWOX expression is shown at day 30 only, so this null precedes any demonstration that the dose acts at that age.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42422765_Obeid2026_PMC_r2.xml
- /home/desktop/legend-development/files/figures/PMID42422765_r2/

## S14

Where: card P11_magnesium_nmdar_gate

Part under test (new wording):

> The EEG p of 0.04 reproduces from Table 2 as an uncorrected chi-square (11/2 against 6/7: chi-square 4.25, p 0.039), while a Fisher exact test gives 0.097 and a Yates-corrected chi-square 0.099, with two of four expected counts at 4.5; the DQ/SQ p of 0.09 (only the 'Normal' row is printed, 4 against 0) is not reproduced (0.055 uncorrected chi-square, 0.114 Fisher); EEG denominators differ

Whole field as it will read:

> Open-label randomised, 52 recruited and 48 analysed per protocol, comparator syrup held calcium and vitamin D without magnesium, no blinding. Seizure control p 0.69 and development p 0.09 (no difference); EEG improvement p 0.04 in the Results and p 0.003 in the Discussion (internal inconsistency). No post-treatment serum magnesium is reported in the text read although the Discussion says supplementation raised it. The EEG p of 0.04 reproduces from Table 2 as an uncorrected chi-square (11/2 against 6/7: chi-square 4.25, p 0.039), while a Fisher exact test gives 0.097 and a Yates-corrected chi-square 0.099, with two of four expected counts at 4.5; the DQ/SQ p of 0.09 (only the 'Normal' row is printed, 4 against 0) is not reproduced (0.055 uncorrected chi-square, 0.114 Fisher); EEG denominators differ (26 and 22), and Table 3's margins agree with Table 2 once its unlabelled 'Low' row (4/2/3, printed in the table footer of the XML) is assigned to the non-intervention group by the group totals (an earlier reading that they disagreed assigned that row to the intervention group; corrected 2026-11-25, ADV-276, after a blind check). Table 3's printed p values (0.003 intervention, 0.42 non-intervention) reproduce by chi-square from the counts (0.0029 and 0.418; intervention Low 4/4/0 and Normal 2/3/13, non-intervention Low 4/2/3 and Normal 3/2/8); Table 4's 0.004 and the seizure-control 0.69 also reproduce, and only the EEG p value of Table 2 does not.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID35222658_ADV272_PMC8752995_epmc_20261125.xml

## S15

Where: card P11_magnesium_nmdar_gate

Part under test (new wording):

> Table 4's 0.004 and the seizure-control 0.69 also reproduce. [IT 2026-11-25, ADV-281: this corrects the ADV-276 statement that the EEG p of Table 2 does not reproduce.]

Whole field as it will read:

> Open-label randomised, 52 recruited and 48 analysed per protocol, comparator syrup held calcium and vitamin D without magnesium, no blinding. Seizure control p 0.69 and development p 0.09 (no difference); EEG improvement p 0.04 in the Results and p 0.003 in the Discussion (internal inconsistency). No post-treatment serum magnesium is reported in the text read although the Discussion says supplementation raised it. The EEG p value is not reproducible from Table 2 (about 0.10 by a Fisher test), EEG denominators differ (26 and 22), and Table 3's margins agree with Table 2 once its unlabelled 'Low' row (4/2/3, printed in the table footer of the XML) is assigned to the non-intervention group by the group totals (an earlier reading that they disagreed assigned that row to the intervention group; corrected 2026-11-25, ADV-276, after a blind check). Table 3's printed p values (0.003 intervention, 0.42 non-intervention) reproduce by chi-square from the counts (0.0029 and 0.418; intervention Low 4/4/0 and Normal 2/3/13, non-intervention Low 4/2/3 and Normal 3/2/8); Table 4's 0.004 and the seizure-control 0.69 also reproduce. [IT 2026-11-25, ADV-281: this corrects the ADV-276 statement that the EEG p of Table 2 does not reproduce.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID35222658_ADV272_PMC8752995_epmc_20261125.xml

## S16

Where: card H02_gabaat_inactivator_myelin_exposure

Part under test (new wording):

> the diffusion coefficient did not differ significantly (right median 1209 in the finding group against 1280 in controls, left 1427 against 1366; the authors call the differences not consistent between the two optic nerves).

Whole field as it will read:

> A diffusion metric of the optic nerve is not a myelination measurement, and the tract is also the retinotoxicity target; the target here is therefore the metric, not CNS_myelination. Fractional anisotropy was lower in the group with the deep-grey finding than in unexposed controls and rose after stopping; the diffusion coefficient did not differ significantly (right median 1209 in the finding group against 1280 in controls, left 1427 against 1366; the authors call the differences not consistent between the two optic nerves). Full text (ADV-276, 2026-11-25, receipt FTR-20261125-40670421-01): the rise after stopping is Table 3, six of the 11 children of the imaging-finding group (left 0.273 to 0.367, p = 0.044; right 0.286 to 0.437, p = 0.050, which is not below 0.05 although the text says P < 0.05), with no unexposed time control. In Table 2 the exposed group with normal imaging is not significantly below controls (right median 0.463 against 0.427; left 0.390 against 0.410); the starred difference is the imaging-finding group against controls. Medians with quartiles are reported while the test named is a one-way analysis of variance.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID40670421_ADV272_PMC12267420_epmc_20261125.xml

## S17

Where: card H02_gabaat_inactivator_myelin_exposure

Part under test (new wording):

> [IT 2026-11-25, ADV-281: groups of 11, 11 and 13 children, the exposed groups defined by the imaging finding; no drug-level or GABA measure in the children with normal imaging; the follow-up is six of the 11 'owing to patient partial compliance'.]

Whole field as it will read:

> A diffusion metric of the optic nerve is not a myelination measurement, and the tract is also the retinotoxicity target; the target here is therefore the metric, not CNS_myelination. Fractional anisotropy was lower in the group with the deep-grey finding than in unexposed controls and rose after stopping; the diffusion coefficient was unchanged. Full text (ADV-276, 2026-11-25, receipt FTR-20261125-40670421-01): the rise after stopping is Table 3, six of the 11 children of the imaging-finding group (left 0.273 to 0.367, p = 0.044; right 0.286 to 0.437, p = 0.050, which is not below 0.05 although the text says P < 0.05), with no unexposed time control. In Table 2 the exposed group with normal imaging is not significantly below controls (right median 0.463 against 0.427; left 0.390 against 0.410); the starred difference is the imaging-finding group against controls. Medians with quartiles are reported while the test named is a one-way analysis of variance. [IT 2026-11-25, ADV-281: groups of 11, 11 and 13 children, the exposed groups defined by the imaging finding; no drug-level or GABA measure in the children with normal imaging; the follow-up is six of the 11 'owing to patient partial compliance'.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID40670421_ADV272_PMC12267420_epmc_20261125.xml

## S18

Where: card L01_nrf2_axis

Part under test (new wording):

> NRF2-knockout macrophages were the control for the pharmacological activation arms (DEM, 15d-PGJ2; 6 h M1 stimulation, n 3-4 mice), and the knockout removed their inhibition of IL6, IL1b and IL1a;

Whole field as it will read:

> NRF2 binds near Il6/Il1b and blocks Pol II recruitment, independently of ROS and the NRF2 motif; Tnf is not changed. Macrophages, not microglia. NOT WWOX EVIDENCE. Which experiment used which: the Keap1-cKO genetics gave the Tnf-unchanged result; NRF2-knockout macrophages were the control for the pharmacological activation arms (DEM, 15d-PGJ2; 6 h M1 stimulation, n 3-4 mice), and the knockout removed their inhibition of IL6, IL1b and IL1a; THP-1 (human) DEM lowered IL6, IL1B and IL1A. No NRF2-loss control exists in that paper for omaveloxolone, dimethyl fumarate or monomethyl fumarate.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID27211851_Kobayashi2016_PMC4879264_epmc_20261125.xml

## S19

Where: card E02_ldh_inhibition

Part under test (new wording):

> In U87 glioblastoma cells (PMID 42035940) viability falls at 10 to 60 uM stiripentol over 48 h and extracellular acidification falls at 25 to 50 uM over 24 h; in the cells of the complex I paper (PMID 41570991) viability by annexin V and propidium iodide was not significantly changed at 250 uM and was lower at 500 uM (Supplementary Fig 1B, n 3).

Whole field as it will read:

> In U87 glioblastoma cells (PMID 42035940) viability falls at 10 to 60 uM stiripentol over 48 h and extracellular acidification falls at 25 to 50 uM over 24 h; in the cells of the complex I paper (PMID 41570991) viability by annexin V and propidium iodide was not significantly changed at 250 uM and was lower at 500 uM (Supplementary Fig 1B, n 3). LDH activity in a lysate of treated cells and on recombinant enzyme falls only at hundreds of micromolar (the size of the lysate inhibition is not in the text and no LDH IC50 exists). NADH-driven oxygen consumption of isolated mouse heart and liver mitochondrial preparations, with complex I as the entry point (a flux readout of the organelle preparation, not an isolated-enzyme activity; the same paper's NADH-activity assays are dye-reduction measures), is inhibited from tens of micromolar (plot readings, auditor-confirmed, about 3 points of uncertainty: heart about 48, 5 and 1 percent remaining across the three lowest-to-highest concentrations tested; liver about 67, 36 and 23); no assay compares the two, so potencies are not comparable (INFERENZA: the effective concentrations are ordered complex I below LDH). The text figure of about 70 percent inhibition at the middle concentration is 51 to 53 percent raw in Supplementary Fig 2. The complex I paper reports no inhibition of malate dehydrogenase. Genetic LDHA/B double knockout raises respiratory capacity whereas stiripentol lowers it, so the drug does not phenocopy LDH ablation on respiration (INFERENZA). Cellular effects of stiripentol are therefore not attributable to LDH alone on the available data (the 2026 glioblastoma paper itself reports 'at least a partial role' of LDH). In a mouse glioblastoma xenograft stiripentol prolonged survival (log-rank P 0.002; median survival 80 days for control and 97 for treated as printed, while the study's source data (published Figure 6F; 16 control and 15 treated animals) give 95 for the treated arm; human stem-like cells in immunodeficient mice. Results and legend state one dose and the Methods another, which the authors' peer-review reply identifies as an earlier experiment replaced by the published one; direction and test unchanged; 2026-11-25, ADV-279, SCI reading). None of the sources states which stereoisomer was used. Tumour models: no seizure, neurodevelopment or WWOX meaning.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42035940_GBM2026_PMC_r2.xml
- /home/desktop/legend-development/files/fulltext/PMID41570991_Bouchez2026_PMC_r2.xml
- /home/desktop/legend-development/files/supplement/PMID41570991_r2/
- /home/desktop/legend-development/files/figures/PMID41570991_r2/

## S20

Where: card E02_ldh_inhibition

Part under test (new wording):

> NADH-driven oxygen consumption of permeabilised mouse mitochondria, with complex I as the entry point (six concentrations, 25 to 150 uM), falls in heart to about 48 percent remaining at 25 uM and about 5 percent at 100 uM (n 4), and in liver to about 67, 38 and 24 percent at 25, 100 and 150 uM (n 3; first marked significant at 100 uM); plot readings, about 3 points of uncertainty. The same paper also measures NADH-dependent activity three ways in permeabilised mitochondria: INT dye reduction (inhibited by stiripentol, not by rotenone) and duroquinone and Q2 NADH oxidation followed at 340 nm (both inhibited by stiripentol);

Whole field as it will read:

> Cell viability and extracellular acidification fall at tens of micromolar. LDH activity in a lysate of treated cells and on recombinant enzyme falls only at hundreds of micromolar (the size of the lysate inhibition is not in the text and no LDH IC50 exists). NADH-driven oxygen consumption of permeabilised mouse mitochondria, with complex I as the entry point (six concentrations, 25 to 150 uM), falls in heart to about 48 percent remaining at 25 uM and about 5 percent at 100 uM (n 4), and in liver to about 67, 38 and 24 percent at 25, 100 and 150 uM (n 3; first marked significant at 100 uM); plot readings, about 3 points of uncertainty. The same paper also measures NADH-dependent activity three ways in permeabilised mitochondria: INT dye reduction (inhibited by stiripentol, not by rotenone) and duroquinone and Q2 NADH oxidation followed at 340 nm (both inhibited by stiripentol); no assay compares the two, so potencies are not comparable (INFERENZA: the effective concentrations are ordered complex I below LDH). The text figure of about 70 percent inhibition at the middle concentration is 51 to 53 percent raw in Supplementary Fig 2. The complex I paper reports no inhibition of malate dehydrogenase. Genetic LDHA/B double knockout raises respiratory capacity whereas stiripentol lowers it, so the drug does not phenocopy LDH ablation on respiration (INFERENZA). Cellular effects of stiripentol are therefore not attributable to LDH alone on the available data (the 2026 glioblastoma paper itself reports 'at least a partial role' of LDH). In a mouse glioblastoma xenograft stiripentol prolonged survival (log-rank P 0.002; median survival 80 days for control and 97 for treated as printed, while the study's source data (published Figure 6F; 16 control and 15 treated animals) give 95 for the treated arm; human stem-like cells in immunodeficient mice. Results and legend state one dose and the Methods another, which the authors' peer-review reply identifies as an earlier experiment replaced by the published one; direction and test unchanged; 2026-11-25, ADV-279, SCI reading). None of the sources states which stereoisomer was used. Tumour models: no seizure, neurodevelopment or WWOX meaning.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42035940_GBM2026_PMC_r2.xml
- /home/desktop/legend-development/files/fulltext/PMID41570991_Bouchez2026_PMC_r2.xml
- /home/desktop/legend-development/files/supplement/PMID41570991_r2/
- /home/desktop/legend-development/files/figures/PMID41570991_r2/

## S21

Where: card E02_ldh_inhibition

Part under test (new wording):

> The text figure of about 70 percent inhibition at 100 uM refers to intact uncoupled mouse small-cell lung cancer cells, not mitochondria (Supplementary Fig 2, where the plot reads 51 to 53 percent raw; 100 uM is the second of four concentrations).

Whole field as it will read:

> Cell viability and extracellular acidification fall at tens of micromolar. LDH activity in a lysate of treated cells and on recombinant enzyme falls only at hundreds of micromolar (the size of the lysate inhibition is not in the text and no LDH IC50 exists). NADH-driven oxygen consumption of isolated mouse heart and liver mitochondrial preparations, with complex I as the entry point (a flux readout of the organelle preparation, not an isolated-enzyme activity; the same paper's NADH-activity assays are dye-reduction measures), is inhibited from tens of micromolar (plot readings, auditor-confirmed, about 3 points of uncertainty: heart about 48, 5 and 1 percent remaining across the three lowest-to-highest concentrations tested; liver about 67, 36 and 23); no assay compares the two, so potencies are not comparable (INFERENZA: the effective concentrations are ordered complex I below LDH). The text figure of about 70 percent inhibition at 100 uM refers to intact uncoupled mouse small-cell lung cancer cells, not mitochondria (Supplementary Fig 2, where the plot reads 51 to 53 percent raw; 100 uM is the second of four concentrations). The complex I paper reports no inhibition of malate dehydrogenase. Genetic LDHA/B double knockout raises respiratory capacity whereas stiripentol lowers it, so the drug does not phenocopy LDH ablation on respiration (INFERENZA). Cellular effects of stiripentol are therefore not attributable to LDH alone on the available data (the 2026 glioblastoma paper itself reports 'at least a partial role' of LDH). In a mouse glioblastoma xenograft stiripentol prolonged survival (log-rank P 0.002; median survival 80 days for control and 97 for treated as printed, while the study's source data (published Figure 6F; 16 control and 15 treated animals) give 95 for the treated arm; human stem-like cells in immunodeficient mice. Results and legend state one dose and the Methods another, which the authors' peer-review reply identifies as an earlier experiment replaced by the published one; direction and test unchanged; 2026-11-25, ADV-279, SCI reading). None of the sources states which stereoisomer was used. Tumour models: no seizure, neurodevelopment or WWOX meaning.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID42035940_GBM2026_PMC_r2.xml
- /home/desktop/legend-development/files/fulltext/PMID41570991_Bouchez2026_PMC_r2.xml
- /home/desktop/legend-development/files/supplement/PMID41570991_r2/
- /home/desktop/legend-development/files/figures/PMID41570991_r2/

## S22

Where: card E02_ldh_inhibition

Part under test (new wording):

> [IT 2026-11-25, ADV-280: that ranking covers the direct mechanisms, with LDH tied with the attenuation of energy metabolism; the CYP-inhibition route is outside it; the liver-to-plasma ratio was measured 1 h after an intravenous injection.]

Whole field as it will read:

> The review states that concentrations inhibiting LDH in vitro (tens to hundreds of micromolar) lie at or above total plasma levels at effective antiseizure doses and well above the estimated free tissue level, that brain to plasma ratio in the rat is near one, and that a liver to plasma ratio of about thirty-five was measured once in the rat; it ranks LDH inhibition last in sensitivity among stiripentol's mechanisms. Secondary statement of other people's measurements by a manufacturer-authored review; its Table 2 LDH range rests on three rows (the 2015 report and Guyon 2022 at hundreds of micromolar, the first second-hand; Le Dudal 2019 from tens to hundreds of micromolar, indirect oxalate); not re-derived. [IT 2026-11-25, ADV-280: that ranking covers the direct mechanisms, with LDH tied with the attenuation of energy metabolism; the CYP-inhibition route is outside it; the liver-to-plasma ratio was measured 1 h after an intravenous injection.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID38443647_Bacq2024_PMC_r2.xml

## S23

Where: card E01_isr_modulators

Part under test (new wording):

> DELE1 or HRI siRNA slows the growth of patient fibroblasts (neither was removed in mice), and a GADD34-targeted compound slightly improves patient-fibroblast growth and, given to the dams around birth and then daily to the pups, extends survival of the knockout mice (about 6 days at the median by plot reading, 5 treated knockouts or a multiple; the authors write 'only 10 days'; eIF2alpha phosphorylation and ATF4 not measured in treated mice), a different direction from

Whole field as it will read:

> Whether the ISR in a WWOX-deficient system is compensatory rather than harmful: in the AFG3L2 precedent (PMID 37804316) DELE1 or HRI siRNA slows the growth of patient fibroblasts (neither was removed in mice), and a GADD34-targeted compound slightly improves patient-fibroblast growth and, given to the dams around birth and then daily to the pups, extends survival of the knockout mice (about 6 days at the median by plot reading, 5 treated knockouts or a multiple; the authors write 'only 10 days'; eIF2alpha phosphorylation and ATF4 not measured in treated mice), a different direction from the PARS2 fly, with different species, endpoint and manipulation; the AFG3L2 kinase evidence is siRNA in fibroblasts, GCN2 and PERK were not tested, and the compound's target is disputed: an in vitro study with purified PPP1R15A fragments found Sephin1 at the tested concentration without effect on complex association or dissociation (biolayer interferometry) and Sephin1 at escalating concentrations (top concentration not stated in the text or legend) without effect on eIF2alpha-P dephosphorylation, and guanabenz inert at the high concentration tested in the enzymatic assay (PMID 28447936, Figures 7 and 8; ADV-276, 2026-11-25); the authors limit the statement of no direct interference with complex assembly or stability to that experimental system. Attenuators and potentiators are therefore two arms of one open question, not one direction.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMC10907083_PMID37804316_europepmc_fulltext_2026-10-29.xml
- /home/desktop/legend-development/files/supplement/PMID37804316/

## S24

Where: card E01_isr_modulators

Part under test (new wording):

> a 5-minute pulse of a group I mGluR agonist raises both, measured 30 minutes later (n 3, P about 0.045), without an Atf4 mRNA change, in normal mouse hippocampal slices

Whole field as it will read:

> Whether an ATF4 protein or P-eIF2a rise in a WWOX-deficient neural system survives silencing of network activity (tetrodotoxin or an mGluR5 antagonist): a 5-minute pulse of a group I mGluR agonist raises both, measured 30 minutes later (n 3, P about 0.045), without an Atf4 mRNA change, in normal mouse hippocampal slices (PMID 41706892; that network activity does so is an inference), and WWOX-deficient systems are hyperexcitable (IT8 P5 loop 1).

Held sources:
- /home/desktop/legend-development/files/fulltext/PMC12933080_PMID41706892_europepmc_fulltext_2026-10-29.xml
- /home/desktop/legend-development/files/supplement/PMID41706892/

## S37

Where: discovery ledger DL-MECH-058, lineage line (replaces the words 'figure e video sono dati adattati/ripubblicati')

Part under test (new wording):

> [corrected 2026-11-25, ADV-280: only Figures 5 and 6 are declared adaptations of earlier data (refs [44] and [54]); Figures 1 to 3, 7 and 8 are schematics and Figure 4 a STRING output run for the review; the origin of the three videos is not stated.]

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID35883580_Liu2022_PMC_r2.xml
- /home/desktop/legend-development/files/figures/PMID35883580_r2/

## S34

Where: S34 (CLAIM 033 reserve, PMID 36926521)

Part under test (new wording):

> The RT-PCR and its sequencing used blood RNA and the western used fibroblasts (two samples); the loading control is drawn as actin although the supplementary methods also name vinculin, and the methods do not list the source of the blotted fibroblasts.

Held sources:
- /home/desktop/legend-development/files/fulltext/PMID36926521_Colin2023_PMC.xml
- /home/desktop/legend-development/files/supplements/PMID36926521/
- /home/desktop/legend-development/files/figures/PMID36926521/

## S36

Where: S36 (preprint dossier doi 10.1101/2025.05.01.651195, PPR1015434)

Part under test (new wording):

> Neuronal more than glial Wwox is the relevant pool: glial knockdown with neuronal amyloid also shortened lifespan slightly (22 against 24 days, p 0.0095), although the Discussion says there was no effect.

Held sources:
- /home/desktop/legend-development/files/fulltext/PPR1015434_LucasClarke2025_EPMC.xml
- /home/desktop/legend-development/files/supplements/PPR1015434/
- /home/desktop/legend-development/files/figures/PPR1015434/

