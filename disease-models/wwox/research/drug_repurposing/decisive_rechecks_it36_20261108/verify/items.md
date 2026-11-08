# Items for a blind audit (IT36 P1)

Check every item against the source named (open routes only; held full text for PMID 34634460 is under files/fulltext/ of the repository root: PMID34634460_Wwox_osc2021_PMC_r2.xml and files/supplement/PMID34634460_r2/mmc1_text.txt). Verdicts per item: SUPPORTED / OVERSHOOT / UNDERSHOOT / NOT_IN_SOURCE / UNVERIFIABLE, with the verbatim locator you found and the depth you reached.

# Part 1: HDAC5 and HIF-1alpha rows

## A01
- role: support
- source_id: PMID 26061431
- system: Hep3B, HeLa, MCF7 human cancer lines; screen of HDAC1, 3, 5, 6 by siRNA
- species: human
- perturbation: knockdown (siRNA; HDAC1, 3, 5, 6 compared)
- what_changes_in_HIF1A: protein amount (hypoxic accumulation) and stability (proteasome-dependent loss; blocked by MG132)
- which_HDAC5_property_implicated: amount of HDAC5 (loss); catalytic activity not isolated in this row
- readout: HIF-1alpha protein by western blot
- controls: control siRNA; other HDAC siRNAs as comparators; MG132 rescue of the loss
- hypoxia_or_normoxia: hypoxia (HIF-1alpha measured as hypoxic accumulation)
- locator_quote: only HDAC5 knockdown remarkably impaired hypoxic accumulation of HIF-1α
- depth: full_text (Results; figure images not viewed)
- limits: HDAC4 siRNA was bought but the screen lists HDAC1, 3, 5, 6; cancer lines; replicate numbers not in the text read
- what_it_does_not_show: does not show HDAC5 acting on HIF-1alpha in neural cells, in normoxia or in a WWOX-deficient cell

## A02
- role: support
- source_id: PMID 26061431
- system: Hep3B, with HeLa and MCF7 (effect 'similar', data not shown); H9c2 rat cardiomyocytes
- species: human (Hep3B, HeLa, MCF7); rat (H9c2)
- perturbation: inhibitor (LMK235, called HDAC5-specific by the authors; TSA comparator)
- what_changes_in_HIF1A: amount and stability of protein; loss is ubiquitination-independent and hydroxylation-independent (still occurs with E1 inactivated or with DFX)
- which_HDAC5_property_implicated: catalytic activity (inhibitor)
- readout: HIF-1alpha protein
- controls: MG132; DFX; TS20 cells with temperature-sensitive E1; TSA as general inhibitor
- hypoxia_or_normoxia: hypoxia (and DFX, a hydroxylase inhibitor)
- locator_quote: LMK235 effectively induced HIF-1α degradation even E1 was inactivated
- depth: full_text (Results; figure images not viewed)
- limits: selectivity of LMK235 is taken from IC50 values quoted in the paper, not shown here; the paper elsewhere reports HDAC1 and HDAC6 IC50 values for it; a compound effect is not attributed to HDAC5 by a target-specific control in this row
- what_it_does_not_show: does not show that the inhibitor acts only through HDAC5; does not show a scaffold route

## A03
- role: support
- source_id: PMID 26061431
- system: Flag-HDAC5 constructs in cells (line not named in the passage read)
- species: human cells (line not named in the passage)
- perturbation: catalytic mutant (C698/H704A) against wild type; overexpression
- what_changes_in_HIF1A: protein amount (stabilisation)
- which_HDAC5_property_implicated: catalytic activity (mutant could not deacetylate alpha-tubulin and could not stabilise)
- readout: HIF-1alpha protein; mutant activity checked on alpha-tubulin
- controls: wild-type HDAC5 as comparator; tubulin deacetylation assay for the mutant
- hypoxia_or_normoxia: not stated for this experiment in the text read
- locator_quote: the HDAC5-C698/H704A mutant was unable to stabilize HIF-1α
- depth: full_text (Results; figure images not viewed)
- limits: the mutant is defined by analogy with HDAC4 C669/H675A; the paper itself notes class IIa enzymes act as scaffolds in the nucleus and still reads this arm as catalytic
- what_it_does_not_show: does not exclude loss of binding partners (HDAC3, MEF2) by the mutant; expression and stability of the mutant are not described in the text read

## A04
- role: support
- source_id: PMID 26061431
- system: overexpression of nuclear-locked and cytosol-locked HDAC5 mutants in cells (line not named in the passage)
- species: human cells (line not named in the passage)
- perturbation: domain or site mutants of localisation (S278/279A cytosolic; L1092A nuclear); AMPK-site mutant S259/498A
- what_changes_in_HIF1A: protein amount; also nuclear accumulation of co-expressed HA-HIF-1alpha (localisation)
- which_HDAC5_property_implicated: localisation (cytosolic HDAC5 acts; nuclear-locked HDAC5 barely does)
- readout: HIF-1alpha protein; subcellular fractions; immunofluorescence
- controls: wild-type HDAC5; localisation of each mutant confirmed by imaging
- hypoxia_or_normoxia: hypoxia and glucose deprivation for the AMPK arms; normoxia for the basal arms
- locator_quote: overexpression of the nuclearly localized HDAC5 mutant barely increased the HIF-1α levels
- depth: full_text (Results; figure images not viewed)
- limits: imaging done on overexpressed protein
- what_it_does_not_show: does not show endogenous HDAC5 localisation in any neural cell

## A05
- role: support
- source_id: PMID 26061431
- system: Hep3B cells; Flag-Hsp70 purified from cells; purified recombinant HDAC5
- species: human
- perturbation: overexpression, knockdown, catalytic mutant, in vitro deacetylation
- what_changes_in_HIF1A: binding partner (Hsp70 and Hsp90 content of the HIF-1alpha complex) and localisation (nuclear accumulation); HIF-1alpha acetylation not changed
- which_HDAC5_property_implicated: catalytic activity on Hsp70 (acetylated Hsp70 is the proposed substrate)
- readout: Hsp70 acetylation, co-immunoprecipitation of Hsp90 and Hsp70 with HIF-1alpha
- controls: K559/561R Hsp70 mutant; HDAC3 as comparator; inactive HDAC5 mutant
- hypoxia_or_normoxia: hypoxia for the complex experiments (stated per experiment in the paper)
- locator_quote: HIF-1α acetylation levels did not seem to be affected by HDAC5 knockdown either
- depth: full_text (Results; figure images not viewed)
- limits: the arrow from Hsp70 deacetylation to HIF-1alpha loss is supported by co-expression and K559/561R data, not by an Hsp70-deacetylation-dead rescue in the endogenous setting
- what_it_does_not_show: does not show HDAC5 deacetylating HIF-1alpha itself (the paper reports no change in HIF-1alpha acetylation)

## A06
- role: support
- source_id: PMID 26061431
- system: cells with HDAC knockdown (cell line not named in the passage read); HA-HIF-1alpha plus Flag-HDAC5 co-transfection
- species: human cells (line not named in the passage)
- perturbation: knockdown of HDAC5 under hypoxia; co-overexpression of HDAC5 with HIF-1alpha in normoxia
- what_changes_in_HIF1A: transactivation (target mRNA); not a separate HIF-1alpha activity assay
- which_HDAC5_property_implicated: amount of HDAC5
- readout: endogenous mRNA of CA9 (CA-IX) and SLC2A1 (GLUT1); lactate output
- controls: other HDAC siRNAs; HIF-1alpha overexpression alone
- hypoxia_or_normoxia: hypoxia (6 h) for knockdown; co-transfection experiment condition not stated in the text read
- locator_quote: only HDAC5 knockdown significantly blunted the hypoxic upregulation of CA-IX (p = 0.0035,) and GLUT1 (p = 0.0014,)
- depth: full_text (Results; figure images not viewed)
- limits: GLUT1 dependence on HIF-1 is stated as background (the paper calls CA-IX and GLUT1 well-known metabolic enzymes mainly regulated by HIF-1 transactivation activity) and no HIF1A knockdown control is described in the text read; t-test on 2^-ddCt, p < 0.01 threshold
- what_it_does_not_show: does not show that the GLUT1 fall is HIF-1-dependent in these cells; does not show SLC2A1 in neural cells

## A07
- role: support
- source_id: PMID 26061431
- system: same paper; AMPK, hypoxia, glucose depletion in cells; CRISPR HDAC5+/- Hep3B
- species: human
- perturbation: AMPK activation or inhibition; HDAC5 heterozygous knockout
- what_changes_in_HIF1A: localisation (hypoxia and AMPK send endogenous HDAC5 to the cytosol); amount (HDAC5 mRNA and protein rise in hypoxia)
- which_HDAC5_property_implicated: localisation and amount of HDAC5
- readout: HIF-1alpha nuclear accumulation; proliferation under hypoxia
- controls: compound C, AICAR, leptomycin B, S259/498A mutant
- hypoxia_or_normoxia: hypoxia and low glucose
- locator_quote: the cytosolic translocation of HDAC5 facilitates HIF-1α stabilization
- depth: full_text (Results; figure images not viewed)
- limits: the sentence quoted is the authors' own summary of the AMPK arms
- what_it_does_not_show: does not show that WWOX or any WWOX-deficient state changes HDAC5 localisation

## B01
- role: support
- source_id: PMID 34021541
- system: mouse hippocampal neurons (low-magnesium 'epilepsy' model) and a lithium-pilocarpine mouse model; HEK293 for the miRNA luciferase assay
- species: mouse (the abstract says rat, the Methods say mice; this inconsistency is in the paper)
- perturbation: knockdown (sh-HDAC5), overexpression (oe-HDAC5), miR-485 mimic or agomir upstream
- what_changes_in_HIF1A: protein amount (HIF1A protein and nuclear HIF1A fall with HDAC5 silencing; HIF1A overexpression does not change HDAC5)
- which_HDAC5_property_implicated: amount of HDAC5 (expression level); no catalytic mutant, no domain mutant
- readout: western blot, mRNA, immunofluorescence and immunohistochemistry of HIF1A and PFKFB3; ChIP of HIF1A at the PFKFB3 promoter; apoptosis, oxidative stress and cytokines
- controls: sh-NC and oe-NC; rescue by HIF1A or PFKFB3 overexpression; blank cells
- hypoxia_or_normoxia: not hypoxia: low-magnesium excitation and pilocarpine models; no hypoxia exposure described
- locator_quote: HDAC5 silencing reduced HIF1α and PFKFB3 expression in epileptic cells
- depth: full_text (Results, Methods, figure titles; figure images not viewed)
- limits: the read-outs are of the epileptic-model state; vendor-sourced neurons; a placeholder 'X of 90 mice died' is left in the Methods; replicate structure 'repeated three times' is not further defined; statistics t-test and ANOVA on groups
- what_it_does_not_show: does not show that HDAC5 acts on HIF1A in unstimulated neurons; does not show SLC2A1; does not separate catalytic from scaffold action

## B02
- role: support
- source_id: PMID 34021541
- system: same paper, co-immunoprecipitation in the neuron model
- species: mouse
- perturbation: overexpression of HDAC5
- what_changes_in_HIF1A: binding partner (HDAC5 co-precipitated with HIF1A)
- which_HDAC5_property_implicated: presence of HDAC5 protein in a complex with HIF1A (physical association)
- readout: HIF1A immunoprecipitation then blot for HDAC5
- controls: oe-NC comparator
- hypoxia_or_normoxia: not stated
- locator_quote: IP detected the binding of HDAC5 to HIF1α, and the results showed that oe-HDAC5 combined more HIF1α than oe-NC
- depth: full_text (Results; figure images not viewed)
- limits: overexpressed HDAC5; association does not state a domain or the effect on activity
- what_it_does_not_show: does not show direct binding, the binding domain, or that binding is needed for the HIF1A change

## C01
- role: support
- source_id: PMID 19071119
- system: human cell line (not named in the abstract; MeSH: Cell Line, Humans)
- species: human (MeSH)
- perturbation: presence of HDAC4 and HDAC5 (mode of expression not stated in the abstract)
- what_changes_in_HIF1A: transactivation of HIF-1alpha; protein amount not changed (no stabilisation); binding partner (less FIH-1, more p300)
- which_HDAC5_property_implicated: scaffold or domain: association through the inhibitory domain of HIF-1alpha (the FIH-1 binding site); catalytic requirement not reported in the abstract
- readout: transactivation assay (reporter type and target genes not stated in the abstract)
- controls: not stated in the abstract
- hypoxia_or_normoxia: not stated in the abstract
- locator_quote: HDAC4 and HDAC5 enhanced transactivation by HIF-1alpha without stabilizing HIF-1alpha.
- depth: abstract_only (PubMed record; no PMC record; full text not reached by an open route in this package)
- limits: every methodological item is unread; any statement on controls, cell line, hypoxia, reporter or mutants would be invented from the abstract
- what_it_does_not_show: does not tell whether deacetylase activity is required (abstract silent); does not tell if the effect is in hypoxia; does not name any endogenous target

## C02
- role: support
- source_id: PMID 19071119
- system: same abstract
- species: human (MeSH)
- perturbation: presence of HDAC4 and HDAC5
- what_changes_in_HIF1A: binding partner: HIF-1alpha binds FIH-1 less and p300 more in the presence of these HDACs
- which_HDAC5_property_implicated: scaffold or domain (inhibitory domain contact)
- readout: co-association and binding assays (formats not stated in the abstract)
- controls: not stated in the abstract
- hypoxia_or_normoxia: not stated in the abstract
- locator_quote: binding of HIF-1alpha to FIH-1 decreased, whereas binding to p300 increased
- depth: abstract_only
- limits: as C01
- what_it_does_not_show: does not show that this route operates for SLC2A1, in neural cells, or in WWOX deficiency; the abstract reports no stabilisation, which differs from PMID 26061431 where stability is the central finding

## D01
- role: counter
- source_id: PMID 42413489
- system: pancreatic ductal adenocarcinoma (PDAC) cells and models, including in vivo and in vitro (not specified in the abstract)
- species: not stated in the abstract
- perturbation: HDAC5 depletion (loss); pharmacological inhibition of HIF1alpha and LSD1 in HDAC5-deficient models
- what_changes_in_HIF1A: HIF1alpha transcriptional activation is potentiated by HDAC5 loss, through hyperacetylated FOXA1 acting at HIF1alpha-targeted genes (transactivation, chromatin access); HIF1alpha amount not stated in the abstract
- which_HDAC5_property_implicated: catalytic activity (FOXA1 K270 deacetylation) and amount
- readout: chromatin occupancy and HIF1alpha-targeted gene sets (target genes not named in the abstract)
- controls: not stated in the abstract
- hypoxia_or_normoxia: not stated in the abstract
- locator_quote: In HDAC5-loss PDAC, K270 hyper-acetylated FOXA1 is reprogrammed to the transcription start sites (TSSs) of HIF1α-targeted genes
- depth: abstract_only (PubMed record; Molecular Cell 2026; no PMC id)
- limits: abstract level; the relation is HDAC5 loss increasing HIF1alpha-target output through a third factor, in cancer cells
- what_it_does_not_show: does not show a direct HDAC5 to HIF1alpha-protein action; does not address neural cells, SLC2A1 or WWOX; does not say whether SLC2A1 is among the targets

## D02
- role: counter
- source_id: PMID 36124413
- system: ovary of the dehydroepiandrosterone-induced PCOS mouse model
- species: mouse
- perturbation: overexpression (adenovirus)
- what_changes_in_HIF1A: HIF-1alpha/VEGFA/VEGFR2 signalling suppressed by HDAC5 (activation level; the abstract does not say HIF-1alpha protein)
- which_HDAC5_property_implicated: catalytic activity on a substrate (VEGFR2 acetylation inhibited), amount
- readout: angiogenesis factors VEGFA, PDGFB/D, ANGPT1/2, CD31; HIF-1alpha/VEGFA/VEGFR2 signalling
- controls: not stated in the abstract
- hypoxia_or_normoxia: not stated (disease model, not an oxygen manipulation)
- locator_quote: HDAC5 suppressed activation of angiogenesis-related HIF-1α/VEGFA/VEGFR2 signaling in PCOS ovaries partly via inhibiting VEGFR2 acetylation.
- depth: abstract_only (PubMed record; no PMC id)
- limits: abstract level; the effect runs through VEGFR2 acetylation, 'partly'; the opposite sign to PMID 26061431 and 34021541 for the same pathway family
- what_it_does_not_show: does not show a HIF-1alpha protein change; neither neural nor SLC2A1; shows the sign is not universal

## D03
- role: counter
- source_id: PMID 35704695
- system: PC12 rat pheochromocytoma cells under intermittent hypoxia (and, earlier, rats)
- species: rat
- perturbation: exposure to intermittent hypoxia lowering HDAC5 protein by phosphatase- and ROS-dependent dephosphorylation; NIPP1 overexpression and calyculin A as tools
- what_changes_in_HIF1A: HIF-1alpha protein and transcriptional activity rise when HDAC5 is lost or dephosphorylated (stability)
- which_HDAC5_property_implicated: amount of HDAC5 (degradation) and phosphorylation state
- readout: HIF-1alpha protein and transcriptional activity (reporter or targets not named in the abstract)
- controls: antioxidant, NOX inhibitor, calyculin A, NIPP1 (as named in the abstract)
- hypoxia_or_normoxia: intermittent hypoxia
- locator_quote: HDAC5 dephosphorylation by IH lead to augmented hypoxia-inducible factor (HIF)-1α protein and an increase in its transcriptional activity.
- depth: abstract_only (PubMed record; the open PMC route returned an empty body in this session)
- limits: abstract level; the abstract calls HDAC5 an 'upstream activator' of HIF-1 signalling in the last sentence while the preceding results read as loss of HDAC5 going with more HIF-1alpha; the causal arrow is therefore undetermined at abstract level
- what_it_does_not_show: does not isolate HDAC5 as the cause of the HIF-1alpha rise (phosphatase and ROS act on other proteins); neural-like cells but a tumour line

# Part 2: electrophysiology statements about PMID 34634460 (source of record)

## E01
- statement (restated): The legend of Fig. 4H declares 14 cells from 7 animals for the pooled control group and 7 cells from 4 animals for each component; the animals of the components sum to 8. The discrepancy is real as printed; its origin is not determined, and it is a reporting inconsistency to flag, not a demonstrated error in the data.
- what the source declares (as quoted): Fig. 4 legend, panel H (one sentence): "S-CTLs n = 14 cells from 7 animals; S-KOs n = 9 cells from 5 animals" and "s-WT N = 7 cells, 4 animals; s-HET N = 7 cells, 4 animals". Methods 5.1: S-CTL is "a clustered group" of S-HT and S-WT.
- reconstructable from aggregate statistics: no. Cells add (7 + 7 = 14); animals do not (4 + 4 = 8, declared 7). Both numbers sit in the same legend sentence, so this is not an artefact of different panels. The cause (misprint, one animal counted twice, a different recording subset for the pooled group) cannot be decided from the paper; the supplement Table S1 lists bursts, slices and animals of the field recordings, not patch-clamp cells.

## E02
- statement (restated): The legend of Fig. 4F declares a pooled control group (18 cells, 10 animals) smaller than the sum of its two components (31 cells, 13 animals). Real as printed. It means the p values of the pooled and of the component comparisons were not necessarily computed on the same cells.
- what the source declares (as quoted): Fig. 4 legend, panel F (one sentence): "S-CTLs n = 18 cells from 10 animals, S-KOs n = 17 cells from 10 animals" and "s-WT: N = 14 cells, 5 animals; s-HET N = 17 cells, 8 animals".
- reconstructable from aggregate statistics: no. Components sum to 31 cells and 13 animals against 18 and 10 for the pooled group; same legend sentence. Either the pooled group and the components are different recording sets (not declared) or one of the numbers is a misprint; the paper does not say, and no per-cell listing exists.

## E03
- statement (restated): mEPSC numerosities are internally consistent. The inhibitory current has no action-potential-independent recording, so no pre- or postsynaptic split exists for inhibition.
- what the source declares (as quoted): Fig. 4 legend, panel C: "S-WT N = 10 cells, 4 animals; S-HT N = 10 cells, 5 animals; S-KO N = 10 cells, 5 animals". Panel D: "N = 10 cells, 5 animals". TTX appears only for the excitatory recording (Results 2.3; Methods 5.4).
- reconstructable from aggregate statistics: partly. Cells and animals are declared and self-consistent; the number of events per cell, which sets the KS result, is not declared.

## E04
- statement (restated): As declared. Cells per animal average 2.6 (WT), 2.5 (HT), 2.7 (KO) pyramidal and 1.3 and 1.2 for interneurons, so animal-level analysis would have 5, 6 and 15 units (4 and 5 for interneurons).
- what the source declares (as quoted): Table 1 row "N's (# cells/# animals)": 13/5, 15/6, 40/15 (pyramidal WT, HT, KO); 5/4 and 6/5 (interneurons, WT+HT and KO). Fig. 6 legend: "For n's, see Table 1."
- reconstructable from aggregate statistics: yes for the numbers, no for anything finer: no per-animal cell count, no per-cell values.

## E05
- statement (restated): The paper declares unpaired t-tests for the current-clamp table and KS tests for the cumulative distributions, a Bonferroni correction 'in each case', and it nowhere states the unit of analysis. 'Cells analysed as independent units' (physiology.tsv) is the reading of the N's row, not a declaration.
- what the source declares (as quoted): Table 1 footnote: "Unpaired t-test for N's indicated in the table." Methods 6.7: "An unpaired t-test was used when there were two groups and a normal distribution"; "A Bonferroni post-hoc correction was applied in each case for tests of multiple comparisons". Methods 6.7 does not name the KS test; Fig. 4 legends do ("KS test").
- reconstructable from aggregate statistics: partly. The test family is declared; the sampling unit (cell, animal, event) is not stated for any test; whether Bonferroni was applied to Table 1 asterisks is not stated; Table 1 does not say whether the dispersion is SD or SEM.

## E06
- statement (restated): The cumulative plots are empirical distribution functions of an input that is not described. That the compared samples are events (or inter-event intervals) is an inference from the size of the p values (E07), not a declaration of the paper.
- what the source declares (as quoted): Methods 6.5: "generated using ecdf.m function in Matlab, which computes the Kaplan-Meier estimate of the cumulative distribution function of the input". The input vector is not described; the number of events per cell is not stated anywhere in the text read.
- reconstructable from aggregate statistics: no. ecdf of itself does not pool anything: it describes whatever vector it is given. Pooling follows only if the authors fed it all events of all cells of a group, which the Methods do not say.

## E07
- statement (restated): If cells were the units, 10 of the 18 reported KS values (all six sIPSC, two mEPSC amplitude, two sEPSC amplitude) could not have been obtained, because each lies below the smallest p the exact two-sample KS test can return for the declared N's; the other 8 are compatible with cells. If events were the units, no inconsistency arises, but the inference is then about events pooled over few animals. The paper declares neither model, so no internal contradiction of the paper is asserted. Without the raw events or cell-level values the tests cannot be reconstructed, and in their absence the KS values describe event distributions and carry no animal-level inference.
- what the source declares (as quoted): Legends of Fig. 4 give p values with "KS test" and the cell and animal N's; the model 'one value per cell' is not declared by the authors.
- reconstructable from aggregate statistics: partly, arithmetic on the declared N's only. Exact smallest two-sided p of a two-sample KS test with n and m single values is 2/C(n+m,n). With cells as units: sIPSC (14 v 9: floor 2.5e-6; 7 v 9: 1.8e-4): all six reported values fall below the floor (6 of 6) (smallest 9.2e-135); mEPSC amplitude WT-KO 4.99e-7 and HT-KO 1.33e-6 (10 v 10: floor 1.1e-5) fall below, WT-HT 1.98e-4 and all three mEPSC frequency values do not; sEPSC amplitude WT-KO 3.5e-23 (14 v 17: floor 7.5e-9) and HT-KO 5.5e-26 (17 v 17: floor 8.6e-10) fall below, CTL-KO 1.5e-5 (18 v 17: floor 4.4e-10) and all sEPSC frequency values do not. Without the raw events or cell-level values no test can be reconstructed.

## E08
- statement (restated): Events within a cell, and cells within an animal, are not independent observations. A test that treats them as independent can return very small p values from a small number of animals; this is a limit on what the p values support, not an error attributed to the authors. Animal-level statistics are not reported for any key result of the paper (sIPSC amplitude, sEPSC amplitude, mEPSC amplitude, sag, rebound).
- what the source declares (as quoted): Methods 6.7: "Sample size represents at least the minimum number of samples needed to establish significance." No mixed model, no animal-level test and no correction for clustering is named. Fig. 4E and G legends: "Right graph shows total mean ± standard error of sEPSCs for all animals."
- reconstructable from aggregate statistics: partly. Table 1 N's give 5/6/15 pyramidal and 4/5 interneuron animals, enough to say what the independent replication is; whether any test was run on animal-level summaries is not stated (the right-hand graphs of Fig. 4E and G are described as 'for all animals').

## E09
- statement (restated): The direction and ordering of the Table 1 means are as printed; which group differences reach significance depends on a test whose unit and dispersion are not declared and whose printed p values cannot be reproduced from the printed means. The KO-only rebound contrast and the HT-versus-KO ordering are therefore undecided, not refuted.
- what the source declares (as quoted): Fig. 6B: "average ± SEM for all animals tested" (sag bar plot, p = 0.04761 and p = 0.00322, unpaired t-test); Fig. 6C rebound p = 0.24947 and 0.00393; Table 1 gives mean ± without naming SD or SEM and marks asterisks versus WT.
- reconstructable from aggregate statistics: partly. Read as SEM with the Table 1 N's, a pooled or Welch t-test gives: input resistance WT-KO 0.022 or 0.011 and WT-HT 0.053 or 0.048; resting potential WT-KO 0.038 or 0.028 and WT-HT 0.18; sag WT-HT 0.11 or 0.10 and WT-KO 0.071 or 0.006; rebound WT-HT 0.67 or 0.65 and WT-KO 0.26 or 0.066; interneuron AP amplitude 0.011 or 0.010. Read as SD every difference is far smaller than 0.001 and the asterisks would not distinguish groups, so the SEM reading is the only one near the printed marks. Several printed p values (sag in HT, rebound in KO, resting potential in HT) are not reproduced; Fig. 6 may be animal-level or a different subset. Not decidable without per-cell or per-animal values.

## E10
- statement (restated): (i) Fixed current step: this is what the paper did; groups with higher input resistance are driven further, so absolute sag at -200 pA is not a measure of Ih density. (ii) Matched membrane potential: not done; it is the comparison that would isolate a channel difference (experiment X1 of the HCN package). Ohm's law gives the first-order steady deflection (resistance times current) only; sag is non-linear and voltage-dependent (Ih activation, Kir and other K+ conductances, capacitance and time course, T-type recovery), so Y04's 'even if HCN density is unchanged' holds as a possibility, not as an estimate of how much of the sag rise is passive.
- what the source declares (as quoted): Methods 6.6: "The sag voltage was measured by subtracting the most negative membrane deflection from its return to steady state"; "a hyperpolarizing pulse of -200pA". Table 1: "Sag (at −200 pA)". The step is fixed in current for every cell; no protocol at a matched membrane potential is described.
- reconstructable from aggregate statistics: partly. The fixed-current design is declared; with a fixed current the deflection scales with each cell's input resistance, so the table compares cells driven to different potentials. A comparison at matched membrane potential does not exist in the paper and cannot be built from means.

## E11
- statement (restated): Y05 to Y07 are linear illustrations of scale, not estimates: they show that the same current drives high-resistance cells several mV further, not by how much, nor what fraction of the sag is passive (audit: about one third in KO and one half in HT with the sag fraction held fixed; the fraction rise is about 1.5 standard errors). The README sentence 'does not need extra HCN' should read 'need not require extra HCN; the linear part accounts for only a share; the non-linear share is undetermined'.
- what the source declares (as quoted): Methods 6.6: "Input resistance was measured by the slope of the computed I-V plot." The current range of the slope is not stated; the sag and the deflection are not reported per cell.
- reconstructable from aggregate statistics: no for any new number; the three rows are products of group means (resistance times 0.2 nA; resting potential minus deflection minus sag). They are linear, assume the I-V slope equals the steady response at -200 pA, treat ratios of means as means of ratios, and carry no variance. Where Ih or Kir is active the slope near rest may overestimate the steady deflection at -200 pA, so the deflections are upper-end illustrations.

## E12
- statement (restated): Lower implied capacitance is a hint that cells may be smaller, not a measured size; cell size is kept as a separate candidate from Ih and from K+/leak conductances.
- what the source declares (as quoted): Methods 6.6: "The time constant was measured by applying the first 50-60 ms of a small hyperpolarizing stimulus to an exponential, standard fit." Table 1 tau 18.55, 18.79, 21.25 ms (pyramidal).
- reconstructable from aggregate statistics: no. Ratio of group means; single-exponential tau of a non-uniform neuron is not a membrane time constant of a point cell; age P13-17 changes size; tau and resistance come from different protocols.

## E13
- statement (restated): Statements about Ih in this paper rest on a current-clamp sag at a fixed current. They are compatible with a larger Ih, with a larger passive deflection recruiting the same Ih, with changed K+ conductances, with smaller cells, or with T-type contributions to rebound; none of the four is separated by the data. Network-activity consequences are a fifth, separate question (bursting is a slice-level finding: 36 of 42 KO slices from 24 animals, 4 of 23 HT slices from 14 animals, 0 of 11 WT slices from 7 animals).
- what the source declares (as quoted): Results 2.6: "the hyperpolarization activated potassium current was elevated, as evidenced by a larger hyperpolarization in response to a negative current injection". Discussion 3.5 heading: "Pyramidal neurons of Wwox S-KO mice show increased sag current, stronger post-inhibitory rebound, depolarized neuronal membrane potential". No voltage-clamp Ih record and no blocker in the paper.
- reconstructable from aggregate statistics: not applicable (a wording matter). The authors' evidence for an elevated current is the larger deflection to the same step, which is the quantity that input resistance already changes.

## E14
- statement (restated): The heterozygote carries part of the intrinsic changes (input resistance, resting potential, sag are marked; rebound is not); the knockout and the heterozygote were never compared directly. 'The same intrinsic changes' overstates; 'several of the same intrinsic changes versus WT, rebound excepted' is what the table supports.
- what the source declares (as quoted): Table 1: resting potential and sag are starred in HT; rebound is not (1.24 ± 0.58 against 0.96 ± 0.19; Fig. 6C p = 0.24947); input resistance starred in HT and KO; HT versus KO is never tested. Results 1: "4 of n = 23 slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice".
- reconstructable from aggregate statistics: partly. The pattern is read from asterisks versus WT only; whether HT and KO differ from each other is not tested; the printed p values for sag in HT and rebound in KO are not reproducible (E09).

## E15
- statement (restated): The sIPSC mean amplitude is lower by about half in the declared summary, a large shift against its spread; the frequency difference (1.9 Hz) and the sEPSC amplitude difference (1.4 pA) are small against their spread, so 'frequency lower' and 'amplitude shifted' are descriptive of event distributions and do not carry an animal-level effect.
- what the source declares (as quoted): Results 2.5: "mean amplitude ± standard deviation: S-CTL 23.3 ± 12.0pA; S-KO 24.7 ± 13.6 pA"; sIPSC 57.3 ± 31.0 and 27.5 ± 19.4 pA; frequency 10.3 ± 11.5 and 8.4 ± 10.0 Hz. The text says standard deviation for these; the figures' right-hand graphs say standard error 'for all animals'.
- reconstructable from aggregate statistics: partly. From the printed means and SD the standardised differences are about 1.1 (sIPSC amplitude), 0.18 (sIPSC frequency) and 0.11 (sEPSC amplitude). What the SD describe (events, cells or animals) is not stated; SD larger than the mean for frequency (11.5 against 10.3 Hz) points to a distribution of per-event or per-interval values, not of cell means (INFERENZA).

# Part 3: computed statements to recompute independently
- K1. For a two-sample exact Kolmogorov-Smirnov test with one value per cell, the smallest attainable two-sided p is 2/C(n+m,n). Recompute for the sample sizes the legends declare for each KS comparison in the paper, compare to each reported p, and list how many reported p fall below the floor. The producer reports: 10 of 18 reported KS p values fall below the floor (all 6 sIPSC, 2 mEPSC amplitude, 2 sEPSC amplitude), the other 8 compatible. State your own count and the n,m you used for each.
- K2. The paper declares nowhere the unit (cell or event) of the KS tests; the Methods describe an empirical cumulative distribution construction (ecdf) and a t-test/rank-sum/Bonferroni framework. Check by string search of Methods and legends whether any sentence states the unit.
- K3. Table 1 dispersion is read as SEM by the producer; with that reading the printed significance marks are not reproduced for sag in HT, rebound in KO and resting potential in HT. Check what dispersion Table 1 declares and recompute an approximate two-sample test from the printed means, dispersions and N (cells) for those three cells; say whether the printed mark is reproduced, not reproduced, or whether it depends on the unstated test.
