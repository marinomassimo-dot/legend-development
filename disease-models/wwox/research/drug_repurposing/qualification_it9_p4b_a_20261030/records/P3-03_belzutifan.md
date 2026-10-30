# P3-03 belzutifan: INCONCLUSIVE (exact missing datum named; go/no-go experiment defined)

Scientist-a3, 2026-10-30. Not medical advice; no dose or schedule is recommended.

**Proposal as generated.** Seed LDHA transcript up (S019; organoid and hNPC; falls with culture time in an unrelated spheroid series). Path EPAS1 -> LDHA (+1); action "opposes" (Z total 3.51, in-degree 3.06); conditional on the uncertain PDK1/PDHA1 seeds. EPAS1 is a hub (degree 73).

## 1 Identity
CHEMBL4585668, InChIKey LOMMPXLFBTZENJ-ZACQAIPSSA-N; PubChem CID 117947097 by key and by name; synonyms PT2977, MK-6482, Welireg. Parent, no salt.

## 2 Target, action, measures
Curated mechanism: HIF-2alpha inhibitor (references: NCT04586231 and a conference abstract). Human EPAS1 rows (complete pull 238 of 238): binding IC50 9 nM (PAS-B displacement, document CHEMBL4311943), 10 nM (scintillation proximity, CHEMBL5727638), 9 nM (CHEMBL6071589, 2024); reporter EC50 11 nM and VEGFA-reduction EC50 17 nM in 786-O cells (VHL-null renal carcinoma line; HIF-2alpha-driven); ratio EC50 versus PT2385 = 2.0. Safety screens: hERG IC50 above 50,000 nM; CYP3A4 inhibition rows in human liver microsomes (midazolam and testosterone substrates, up to 50 uM; no value stored in the row). Selectivity versus HIF-1alpha is not given as a ChEMBL row (ARNT dimerisation is the mechanism; HIF-1alpha selectivity row: UNKNOWN here).

## 3 Exposure and nervous system
DailyMed label (set 13e15ee0..., version 13, 09/2026): median Tmax 1-2 h; Vd 119 L; protein binding 45 percent; half-life 14 h; excretion urine 49.6 and faeces 51.7 percent (metabolites); metabolism UGT2B17 and CYP2C19. Paediatric: established from 12 years for locally advanced or metastatic pheochromocytoma or paraganglioma only. The label gives no CSF or brain concentration; VHL CNS hemangioblastoma response is an indication but a tumour response is not a measurement of free neural exposure.

## 4 Safety and counter-evidence
Boxed warning embryo-fetal toxicity (can render hormonal contraceptives ineffective); severe anaemia (haemoglobin decrease 93 percent, grade 3 in 7 percent, VHL study); severe hypoxia; dizziness 38 percent. No "seizure" or "convuls" string in the label text (searched). PubMed "belzutifan AND (seizure OR convulsion OR epilepsy OR neurotoxicity)": 0 hits. openFDA spontaneous reports: 618, epilepsy 3 (counts only). Counter-evidence on the target's neural role: HIF-2alpha conditional knockout (Emx1 and Nestin drivers) did not alter newborn or layer-specific cortical neurons or NSC maintenance at E16.5 in mouse (PLoS One 2026, abstract). Anaemia and hypoxia in a child with a developmental and epileptic encephalopathy is a mechanistic concern with no source tying it to seizures (UNVERIFIED).

## 5 Edge provenance
EPAS1 -> LDHA is a CollecTRI transcriptional record, nine reference tags, seven itemised titles from heart, hepatocellular carcinoma, endothelium, uveal melanoma, gut and pancreatic cancer; none neural. Mode (transcriptional) and sign (+) are consistent with the transcript seed. LDHA is mainly a HIF-1alpha target in the same network (HIF1A -> LDHA, many sources), and belzutifan does not act on HIF-1alpha. Verdict: usable as a hypothesis to test, not as a prediction for neural cells.

## 6 Expression
HPA adult brain snRNA: EPAS1 group-enriched in endothelial cells (1,673 nCPM), pericytes (727) and vascular smooth muscle (610), not in neurons or glia; ARNT broad. WWOX-KO organoid (CPM): EPAS1 1.18-9.06 (KO mean 5.5, WT 1.5, ratio 3.8, n=4 v 2, descriptive, untested), HIF1A ratio 0.84, ARNT ratio 1.46; EPAS1 and ARNT absent from the hNPC CAGE table.

## 7 Trials registry
2026-10-30: belzutifan 47 studies (33 under MK-6482, 25 under PT2977 for the same agent); epilepsy, seizure, DEE, hypomyelination, neurodevelopmental disorder, intellectual disability, cerebral palsy: 0 each.

## 8 Decision and experiment
INCONCLUSIVE under the pre-registered rule 4 (target not shown in a neural cell type). **Missing datum:** HIF-2alpha protein (stabilised, nuclear) in WWOX-deficient neural cells and its causal share in the glycolysis transcripts. **Go/no-go design:** in WWOX-deficient and isogenic control hNPC, neurons and organoids, measure EPAS1 protein at normoxia and 1-3 percent O2; if detected, a belzutifan concentration series bracketing its reported cell EC50 (11 nM, reporter line) with EPAS1 and HIF1A knock-down arms; readouts LDHA, SLC2A1, BNIP3 transcripts, an HRE/ARNT reporter, lactate output and 13C-glucose label into lactate versus TCA; valence readout viability and neurite or network activity under normoxia and low O2, tested as genotype-by-compound interaction (if the glycolytic shift is adaptive, HIF-2alpha blockade should worsen low-O2 survival; if harmful, improve it). Falsifier: no EPAS1 protein, or no change in LDHA/SLC2A1 beyond replicate variation at a concentration well above the EC50 with the knock-down arm also flat. Pre-register the effect-size threshold first.
Scores: promise LOW-MEDIUM (selective probe, transcript-only seed, vascular target in adult brain); depth MEDIUM; feasibility MEDIUM-HIGH in vitro (research supply UNVERIFIED); priority MEDIUM-LOW (cheap and decisive about HIF-2alpha involvement, not a therapy path).
Transfer limits: VHL-null cell lines define the compound's cell potency, not neural cells; LDHA seed maturity confound.
UNVERIFIED: research-use availability; HIF-1alpha selectivity row; ChEMBL transcription of the cited potency documents (not opened).
