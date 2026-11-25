"""IT 2026-11-25 (IT23): proposed sentences for the checkpoint-22 queue (ADV-280, ADV-281, ADV-238/239 remainder).
Each entry: (id, file group, target, mode, old, new). mode: 'replace' (old substring -> new), 'append' (new appended to the end of the string that contains old) or 'after' (new inserted right after old).
Data only; applied by apply_it23.py after the blind check. Hypothesis level; nothing here is medical advice."""

M281 = "[IT 2026-11-25, ADV-281: "
M280 = "[IT 2026-11-25, ADV-280: "
M239 = "[IT 2026-11-25, ADV-239: "
EDITS = []


def e(i, card, mode, old, new, sources):
    EDITS.append(dict(id=i, card=card, mode=mode, old=old, new=new, sources=sources))


F = "/home/desktop/legend-development/files/"
DR = "disease-models/wwox/research/drug_repurposing/"

# ---- ADV-281 (null notes) -------------------------------------------------
SHAH = [F + "fulltext/PMID40485335_Shah2025_PMC12146831.xml", F + "figures/PMID40485335/"]
e("S01", "A01_pba_class", "replace", "the partly trafficked branch was outside the reach of this class, not of every chemical chaperone.",
  "the partly trafficked branch was outside the reach of 4-PBA, not of every chemical chaperone. " + M281 +
  "the null arm is 4-PBA 1 mM for 48 h in G443D flies (Fig 6G, seizure behaviour unaltered); in G443D flies the transporter already shows a wild-type-like expression pattern (Fig 6C legend, Fig 6E, Supp Fig 4C), so the fly arm does not test a trafficking defect; 10 % glycerol was also not significant in G443D flies, so no tested chaperone rescued G443D in vivo; "
  "the same 4-PBA dose reduced seizures in G443V flies (Fig 6H); 4-PBA 10 mM also did not rescue G443D uptake in HEK293 cells (Fig 3B).]", SHAH)
CLA = [F + "fulltext/PMID38378758_Clausen2024_PMC10879094.xml", F + "supplement/PMID38378758/", F + "fulltext/PMID38740822_Gronbaek2024_PMC11091098.xml", F + "supplement/PMID38740822/"]
e("S02", "A02_proteasome_inhibitor_class", "replace", "a lysosome-inhibitor control did nothing, placing the loss on the proteasome.",
  "chloroquine (20 uM, 16 h) gave little shift ('no substantial changes', Clausen Fig 3C; 'little effect', Gronbaek-Thygesen Fig 4F) and no readout in either paper shows that it blocked lysosomal degradation in these cells; "
  "proteasome-pathway perturbations shift part of the low-abundance population and the authors attribute most low-abundance variants, not all, to proteasomal degradation; the ASPA authors write that they cannot exclude a role for autophagy where expression persists longer. " + M281 + "no activity check for chloroquine; searched 2026-11-25.]", CLA)
COL = [F + "fulltext/PMID38051092_Collard2023_PMC10761163_epmc_2026-10-29.xml"]
e("S03", "A02_proteasome_inhibitor_class", "replace",
  "while I278T activity did not rise at all although the same allele is rescued by proteasome inhibition in mice and in the kidney line.",
  "while I278T activity was not rescued (text statement; the figure bars were not viewed), although the paper cites rescue of I278T by proteasome inhibitor treatment in yeast, human patient fibroblasts and transgenic mice (its refs 15, 25, 28); proteasome inhibitors were tested in this paper on R125Q only; the Discussion adds that blocking proteasomal degradation of all cellular proteins was by itself insufficient to restore I278T activity and that induction of the unfolded protein response and specifically of HSP70 was required for the bortezomib rescue (its ref 15), and that short-term high-dose proteasome inhibitor treatment is accompanied with substantial toxicity while long-term low-dose treatment was ineffective (its ref 28).", COL)
CHE = [DR + "lucas_clarke_followup_20261026/chembl_named_activities.tsv", DR + "lucas_clarke_followup_20261026/chembl_mechanisms.tsv"]
e("S04", "E03_pdk_inhibition_dca", "replace", "In the measurements retrieved the enzyme assay shows no half-maximal inhibition at the highest concentration tested and",
  "Among the measurements retrieved, three enzyme rows record no half-maximal inhibition (IC50 above 1 mM; CHEMBL1133665, CHEMBL1132309, CHEMBL1133733, which carry identical companion values and record no top concentration), other enzyme-level rows differ (EC50 180 uM, CHEMBL5370584; EC50 5.7 mM with 64.2 % inhibition at 10 mM, CHEMBL4308888; Kd above 1 mM, CHEMBL3813671; EC50 above 100 mM, CHEMBL4732185) and", CHE)
KES = [F + "fulltext/adv051_it_20261118/A/PMID40165594_europepmc_core.json"]
e("S05", "H01_apinocaltamide_ttype", "append", "A measured null in a seizure type that is not the WWOX provoked-seizure phenotype",
  " " + M281 + "one model only (rat amygdala kindling), known from the abstract, which gives no dose or exposure for that arm; the same abstract reports suppression of spike-wave discharges in two rat strains and reduced severity of generalized convulsive seizures in two mouse tests, the latter at higher concentration.]", KES)
STE = [F + "fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf", F + "fulltext/PMID42397075_Steinberg2026_OUP-AM_fitz.txt", F + "fulltext/PMID42397075_Steinberg2026_OUP-Supplement/"]
e("S06", "M01_neurogenic_output_myc_window", "replace", "the upper-layer marker mildly rises (main text).",
  "the upper-layer marker mildly rises according to the main text, while the panel marks SATB2 in knockout against knockout plus A51 as not significant (Supplementary Fig 7F).", STE)
e("S07", "M01_neurogenic_output_myc_window", "replace", "no randomisation or blinding is stated for the whole study (not specific to this arm);",
  "the article states that no randomisation or blinding was applied (whole study, not specific to this arm); the Supplementary Fig 7 legend gives organoid numbers of 4, 4, 6 and 7 for one experiment while the panels plot more points;", STE)
e("S08", "M01_neurogenic_output_myc_window", "replace", "(panel values are prior-session attestations; the supplement is not available locally)",
  "(the supplementary figures PDF is held since 2026-11-21 and Supplementary Fig 7F-G was viewed on 2026-11-25; other panel values remain prior-session attestations)", STE)
e("S09", "D01_a51", "replace", "The panel values are NO LONGER RE-AUDITABLE: the published supplement exists in no checkout and the preprint does not contain the A51 experiment.",
  "The published supplementary figures are held since 2026-11-21, so the panel values can be re-read (this row's values were not re-audited on 2026-11-25); the preprint does not contain the A51 experiment.", STE)
e("S10", "D01_a51", "append", "MEASURED NO RECOVERY: knockout-versus-treated not significant for both markers",
  " " + M281 + "the two markers are CTIP2 (Supplementary Fig 7G) and SATB2 (Supplementary Fig 7F); NEUN does rise; CTIP2 is near zero in both knockout arms (about 0.1 and 0.7 % of cells by eye), so a floor limits the test; for SATB2 the knockout plus A51 arm is also not significantly different from wild type (about 0.7 against about 1.4 % of cells by eye), so SATB2 recovery is neither shown nor excluded; in wild type DMSO lowers CTIP2 (about 12.6 to about 5.6 % of cells by eye) and the knockout comparator is not labelled as vehicle; one knockout clone, one experiment, week-15 harvest.]", STE)
LUC = [F + "fulltext/PMID42909904_PMC13684411.xml", F + "fulltext/PMID42909904_LucasClarke2026_BrainComms_fcag385.pdf", F + "fulltext/PMID42909904_supplement/"]
e("S11", "E01_isr_modulators", "append", "Not significant without amyloid (t 0.0894",
  " " + M281 + "knockdown was verified by head qPCR in newly eclosed females only (about 0.55 of control, 3 pools; Supplementary Fig 1), not at day 14; Atf4 staining in the LacZ background is near blank in both genotypes (Supplementary Fig 5D), so the null may sit at the detection floor; the two backgrounds were tested with different tests.]", LUC)
OBE = [F + "fulltext/PMID42422765_Obeid2026_PMC_r2.xml", F + "figures/PMID42422765_r2/"]
e("S12", "C04_aav9_endpoint_families", "append", "High dose about 113: not significant against wild type",
  " " + M281 + "Fig 3E, postnatal day 10, Student t tests without multiplicity correction; the reference-item knockout arm (about 95 mg/dL) differs from wild type (about 129 mg/dL) at one star only; about 11 high-dose and 8 knockout points counted on the plot (no n in the legend): 'not significant against the untreated knockout' is not evidence of no effect.]", OBE)
e("S13", "C04_aav9_endpoint_families", "append", "Low dose about 105: not significant against wild type",
  " " + M281 + "Fig 3E; about 7 low-dose and 8 knockout points counted on the plot (no n in the legend); in Fig 3C (no statistics, no n) the low-dose mean weight at day 10 is about 4.8 g against about 4.4 g for the untreated knockout, and the low-dose curve is already above the knockout curve at day 5 (about 3.5 against 2.3 g) and day 15 (about 6.4 against 4.7 g), read by eye; the text reports partial low-dose improvement of hindlimb clasping at P18 and an intermediate glucose improvement at P20, while low-dose WWOX expression is shown in the main figures at P30; so the day-10 null is a single time point at which the low dose has only begun to separate from the knockout, and it is not evidence of no effect.]", OBE)
YAD = [F + "fulltext/PMID35222658_ADV272_PMC8752995_epmc_20261125.xml"]
e("S14", "P11_magnesium_nmdar_gate", "replace", "The EEG p value is not reproducible from Table 2 (about 0.10 by a Fisher test), EEG denominators differ (26 and 22), and Table 3's margins agree",
  "The EEG p of 0.04 reproduces from Table 2 as an uncorrected chi-square (11/2 against 6/7: chi-square 4.25, p 0.039), while a Fisher exact test gives 0.097 and a Yates-corrected chi-square 0.099, with two of four expected counts at 4.5; the DQ/SQ p of 0.09 (only the 'Normal' row is printed, 4 against 0) is not reproduced and depends on the assumed group sizes (0.055 uncorrected chi-square and 0.114 Fisher for 26 and 22; 0.030 to 0.075 and 0.096 to 0.128 for the other sizes tried); the EEG row is labelled 'n=26' although its counts total 13 in each group, while the group sizes are 26 and 22; and Table 3's margins agree", YAD)
e("S15", "P11_magnesium_nmdar_gate", "replace", "Table 4's 0.004 and the seizure-control 0.69 also reproduce, and only the EEG p value of Table 2 does not.",
  "Table 4's 0.004 and the seizure-control 0.69 also reproduce. [IT 2026-11-25, ADV-281: this corrects the ADV-276 statement that the EEG p of Table 2 does not reproduce.]", YAD)
HU = [F + "fulltext/PMID40670421_ADV272_PMC12267420_epmc_20261125.xml"]
e("S16", "H02_gabaat_inactivator_myelin_exposure", "replace", "the diffusion coefficient was unchanged.",
  "the diffusion coefficient did not differ significantly (right median 1209 in the finding group against 1280 in controls, left 1427 against 1366; the authors call the differences not consistent between the two optic nerves).", HU)
e("S17", "H02_gabaat_inactivator_myelin_exposure", "append", "Medians with quartiles are reported while the test named is a one-way analysis of variance.",
  " " + M281 + "groups of 11, 11 and 13 children, the exposed groups defined by the imaging finding; no drug-level or GABA measure in the children with normal imaging; the follow-up is six of the 11 'owing to patient partial compliance'.]", HU)
KOB = [F + "fulltext/PMID27211851_Kobayashi2016_PMC4879264_epmc_20261125.xml"]
e("S18", "L01_nrf2_axis", "replace", "the NRF2-knockout control was a pharmacological activation (DEM, 15d-PGJ2; 6 h M1 stimulation, n 3-4 mice) that removed the inhibition of IL6, IL1b and IL1a;",
  "NRF2-knockout macrophages were the control for the pharmacological activation arms (DEM, 15d-PGJ2; 6 h M1 stimulation, n 3 mice), and the knockout removed their inhibition of IL6, IL1b and IL1a;", KOB)

# ---- ADV-280 ---------------------------------------------------------------
LDH = [F + "fulltext/PMID42035940_GBM2026_PMC_r2.xml", F + "fulltext/PMID41570991_Bouchez2026_PMC_r2.xml", F + "supplement/PMID41570991_r2/", F + "figures/PMID41570991_r2/"]
e("S19", "E02_ldh_inhibition", "replace", "Cell viability and extracellular acidification fall at tens of micromolar.",
  "In U87 glioblastoma cells (PMID 42035940) viability falls at 10 to 60 uM stiripentol over 48 h and extracellular acidification falls at 25 to 50 uM over 24 h; in the two mouse small-cell lung cancer lines of the complex I paper (mSCLC 2405 and 1578; PMID 41570991) viability by annexin V and propidium iodide was not significantly changed at 250 uM and was lower at 500 uM (Supplementary Fig 1B, n 3).", LDH)
e("S20", "E02_ldh_inhibition", "replace",
  "NADH-driven oxygen consumption of isolated mouse heart and liver mitochondrial preparations, with complex I as the entry point (a flux readout of the organelle preparation, not an isolated-enzyme activity; the same paper's NADH-activity assays are dye-reduction measures), is inhibited from tens of micromolar (plot readings, auditor-confirmed, about 3 points of uncertainty: heart about 48, 5 and 1 percent remaining across the three lowest-to-highest concentrations tested; liver about 67, 36 and 23);",
  "NADH-driven oxygen consumption of permeabilised mouse mitochondria, with complex I as the entry point (six concentrations, 25 to 150 uM), falls in heart to about 48 percent remaining at 25 uM and about 5 percent at 100 uM (n 4), and in liver to about 67, 38 and 24 percent at 25, 100 and 150 uM (n 3; first marked significant at 100 uM); plot readings, about 3 points of uncertainty. The same paper also measures NADH-dependent activity two ways in permeabilised mouse heart mitochondria: INT dye reduction (inhibited by stiripentol, not by rotenone) and duroquinone NADH oxidation followed at 340 nm (inhibited by both stiripentol and rotenone) (Fig 6B, 6D); a Q2-based NADH-oxidation assay was run on yeast mitochondria, where stiripentol did not inhibit the Nde or Ndi activity (Fig 6E, 6F);", LDH)
e("S21", "E02_ldh_inhibition", "replace", "The text figure of about 70 percent inhibition at the middle concentration is 51 to 53 percent raw in Supplementary Fig 2.",
  "The text figure of about 70 percent inhibition at 100 uM refers to intact uncoupled mouse small-cell lung cancer cells, not mitochondria (Supplementary Fig 2, where the plot reads 51 to 53 percent raw; 100 uM is the second of four concentrations).", LDH)
BAC = [F + "fulltext/PMID38443647_Bacq2024_PMC_r2.xml"]
e("S22", "E02_ldh_inhibition", "append", "it ranks LDH inhibition last in sensitivity among stiripentol's mechanisms.",
  " " + M280 + "that ranking covers the direct mechanisms, with LDH tied with the attenuation of energy metabolism; the CYP-inhibition route is outside it; the liver-to-plasma ratio was measured 1 h after an intravenous injection.]", BAC)
AFG = [F + "fulltext/PMC10907083_PMID37804316_europepmc_fulltext_2026-10-29.xml", F + "supplement/PMID37804316/"]
e("S23", "E01_isr_modulators", "replace", "HRI or DELE1 loss worsens, and a GADD34-targeted compound improves, patient-cell and mouse endpoints (survival gain about 6 to 7 days at the median by plot reading), a different direction from",
  "DELE1 or HRI siRNA slows the growth of patient fibroblasts in low-glucose culture (neither was removed in mice), and a GADD34-targeted compound slightly improves patient-fibroblast growth in low-glucose culture and, given to the dams around birth and then daily to the pups, extends survival of the knockout mice (about 6 days at the median by plot reading, 5 treated knockouts or a multiple; the authors write 'only 10 days'; eIF2alpha phosphorylation and ATF4 not measured in treated mice), a different direction from", AFG)
DHP = [F + "fulltext/PMC12933080_PMID41706892_europepmc_fulltext_2026-10-29.xml", F + "supplement/PMID41706892/"]
e("S24", "E01_isr_modulators", "replace", "group I mGluR agonism raises both in minutes without an Atf4 mRNA change in normal mouse hippocampus",
  "a 5-minute pulse of a group I mGluR agonist raises both, measured 30 minutes later (n 3, P about 0.045), without an Atf4 mRNA change, in normal mouse hippocampal slices", DHP)

# ---- ADV-238 / ADV-239 remainder ------------------------------------------
P47 = [DR + "advisor_pilot_20261113/brainstorm_20261116/adv239_influence_audit_sci_20261125/out/influence_adv239.tsv",
       DR + "advisor_pilot_20261113/brainstorm_20261116/adv239_influence_audit_sci_20261125/out/gsea_loo_adv239.tsv",
       DR + "advisor_pilot_20261113/brainstorm_20261116/adv239_influence_audit_sci_20261125/out/unit_values_adv239.tsv"]
e("S25", "J01_glial_reactivity_modulation", "after", "the regulator-level inflammatory inference there does not rest on those canonical transcripts (absence from a thresholded list is not a measurement).",
  " " + M239 + "in the repository re-run, the hallmark TNFA/NF-kB gene-set enrichment rests on one or two animals: without mutants M6 and F8 it meets positive-direction q < 0.05 in no forebrain region, and in cortex removing M6 alone reverses its enrichment score.]", P47)
e("S26", "J01_glial_reactivity_modulation", "append", "IL6/JAK/STAT3 loses the q threshold but keeps a positive score in all three (ADV-233).",
  " " + M239 + "removing M6 alone also removes more than half of the TNFA set-mean rise in all three forebrain regions (left: hippocampus 0.49, cortex 0.12, prefrontal cortex 0.45 of it).]", P47)
e("S27", "K01_hif_axis_glycolytic_shift", "after", "HYPOXIA keeps q < 0.05 only in hippocampus but keeps a positive score in all three (ADV-239).",
  " " + M239 + "set means of HYPOXIA, GLYCOLYSIS and APOPTOSIS: hippocampus and prefrontal cortex keep the sign and at least 60 percent of the rise without any one animal, while in cortex removing M6 leaves about 0.21, 0.38 and 0.22 of it; in the repository re-run cortical APOPTOSIS does not reach q 0.05 even with all animals; the cortical rise of the six-gene control set (five glycolytic enzymes and Ndrg1) holds without M6.]", P47)
e("S28", "L01_nrf2_axis", "after", "the NRF2 target transcripts Hmox1 and Srxn1 are modestly higher in all four regions (+0.3 to +0.7 log2), Nqo1 is mixed, Gclm and Txnrd1 flat",
  " " + M239 + "Srxn1 keeps at least 70 percent of its rise without any one animal in every region; the cortical rise of Hmox1 and of the five-gene NRF2 set rests more than half on mutant M6]", P47)
ORG = [DR + "w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv", DR + "advisor_pilot_20261113/brainstorm_20261116/adv239_influence_audit_sci_20261125/out/unit_values_adv239.tsv"]
e("S29", "F02_myelination_activity_sign", "replace", "Oligodendrocyte-lineage transcripts are barely detectable in the week-15 organoid.",
  "Oligodendrocyte-lineage markers SOX10 and OLIG1 are below 1 CPM in all six libraries of the week-15 organoid (4 knockout, 2 control), while PLP1 is 49 to 198 CPM (isoforms not resolved) and MBP about 1 to 4 CPM.", ORG)
e("S30", "F03_bumetanide_chloride_gradient", "append", "IT13 P3a (2026-10-31): also no transcript support in the P17 Wwox-deletion mouse deposits",
  " " + M239 + "in the cortex deposit of the neuron-targeted deletion (4 control, 3 knockout libraries) the Slc12a2/Slc12a5 ratio is higher by 0.24 log2 with overlapping libraries, and this falls to 0.085 when one control library is removed; Slc12a5 itself is lower in all three knockout libraries than in all four controls (log2 -0.65); among the hippocampal contrasts Slc12a5 is higher only in the Nestin-Cre one (+0.28, overlapping) and lower in the Syn-Cre and germline-null ones (-0.55, -0.41).]", P47)

# investigations (evidence_available clauses)
INV = {
    "INV-06": " " + M239 + "in the mouse cortex deposit of the neuron-targeted deletion the CTGF change is not stable: log2 +0.19 with all libraries, from -0.37 to +0.46 when one library is removed.]",
    "INV-15": " " + M239 + "in the neuron-targeted (Syn-Cre) deletion the hippocampal Pvalb fall comes from 2 control against 3 knockout libraries (all three below both controls); in cortex of the same deletion, 4 against 3, the fall is smaller (log2 -0.59 against -1.70) and the libraries overlap. The two other hippocampal contrasts also fall, with every knockout library below every control (Nestin-Cre log2 -0.86, 2 against 2; germline null -1.16, 3 against 2).]",
    "INV-16": " " + M239 + "in the P47T mouse the higher SLC2A1 transcript is a forebrain reading (log2 +0.19 to +0.27, 5 against 5); cerebellum goes the other way (-0.17, 3 P47T against 4 wild type); the genotypes overlap in all four regions, and in cortex removing one wild-type animal (F5) leaves less than half of the rise.]",
}
INV_SOURCES = P47

# non-card texts
DL058_OLD = "figure e video sono dati adattati/ripubblicati."
DL058_NEW = ("[corrected 2026-11-25, ADV-280: only Figures 5 and 6 are declared adaptations of earlier data (refs [44] and [54]); Figures 1 to 3, 7 and 8 are schematics and Figure 4 a STRING output run for the review; the origin of the three videos is not stated.]")
DL058_SOURCES = [F + "fulltext/PMID35883580_Liu2022_PMC_r2.xml", F + "figures/PMID35883580_r2/"]
DOSSIER_OLD = "neuronal, not glial, Wwox is the relevant pool"
CLAIM_NOTES = {
    "S34 (CLAIM 033 reserve, PMID 36926521)": ("The RT-PCR and its sequencing used blood RNA and the western used fibroblasts (two samples, one lane each: control and proband); the loading control is drawn as actin (43 kDa) although the supplementary methods also state that vinculin was used as the cytoplasmic loading control; the supplementary methods name fibroblasts from a healthy donor and from individual 13, not individual 11, so the source of the blotted individual 11 fibroblasts is not listed.",
        [F + "fulltext/PMID36926521_Colin2023_PMC.xml", F + "supplements/PMID36926521/", F + "figures/PMID36926521/"]),
    "S35 (CLAIM 005, GAD2 in the week-15 organoid)": ("GAD2 transcript is higher on average in knockout organoids than in controls; the libraries overlap (4 knockout against 2 control).", ORG),
    "S36 (preprint dossier doi 10.1101/2025.05.01.651195, PPR1015434)": ("Neuronal more than glial Wwox may be the relevant pool (the preprint's own wording is 'may be more important'): glial knockdown with neuronal amyloid also shortened lifespan slightly (median 22 against 24 days, p 0.0095, N 100-115 flies per genotype, Supplementary Fig S3A, curve read by eye) although the Discussion says glial knockdown had no effect on the toxicity of neuron-derived Abeta42; startle-induced locomotion was not changed (p 0.3491).",
        [F + "fulltext/PPR1015434_LucasClarke2025_EPMC.xml", F + "supplements/PPR1015434/", F + "figures/PPR1015434/"]),
    "S39 (research note R1, Premise 0 row)": ("[ADV-280, 2026-11-25: loss of function in those wild-type-abundant pathogenic variants is not measured in this paper; function (mt-Keima mitophagy, Supplementary Fig 1B, 1C) was tested for wild type, C431A (inactive) and R42P only, and R42P, a low-abundance pathogenic variant, appeared functional when overexpressed; for the wild-type-abundant ones the paper infers a mechanism from clustering around the active site, predicted functional-site and conservation scores (four of six) and literature structural data (T415N, G430D, K161N, G284R), and says the mechanisms behind R33Q, M434T and P437L remain unclear.]", []),
    "S40 (research note R1, PMID 38731820)": ("[ADV-280, 2026-11-25: in wild type the BiP rise with zonisamide is significant in two of four brain regions (cerebellum 1.35-fold, p 0.023; thalamus 1.68-fold, p 0.023), a trend in hippocampus (1.50-fold, p 0.064) and not significant in cortex (1.39-fold, p 0.149, a rise of similar size to the cerebellar one); in the Gabrg2+/Q390X mice none of the four regions changed; the drug was given at 20 mg/kg daily intraperitoneally for 7 days to Gabrg2+/Q390X mice and wild-type littermates aged 1 to 1.5 months (N 6 to 8 animals).]", []),
}
