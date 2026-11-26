# Packet R: card sentences to check (20). Card files: disease-models/wwox/research/drug_repurposing/cards/<card>.packet.json

## R-01 (card L01_nrf2_axis)
SENTENCE: NFE2L2 0.75x, KEAP1 0.93x, NQO1 0.73x, G6PD 0.75x, SLC7A11 0.65x, BACH1 0.73x;
printed at: /disease_assertions[2]/measured_result_note
  record id: "DA-L01-003"
  record target_id: "IL1B, IL6, TNF, NFE2L2, KEAP1 and NRF2 target transcripts, human KO organoid"
  record source: "GSE156243 (deposit of PMID 34268881); unplanned descriptive reading in this package"
  record locator: "axis_it10_p22_20261031/organoid_nrf2_rows.tsv; selfaudit_reread_output.txt C1-C3"
  record endpoint: "descriptive cpm ratio KO/WT (4 v 2 libraries), no test"
  record direction: "UNKNOWN"
  record context: {"disease_id": "WWOX-deficient human cerebral organoid (engineered knockout)", "genotype": "KO versus WT", "species": "human", "cell_type": "cerebral organoid, bulk RNA", "developmental_stage": "culture week 15"}
  record reading_depth: "queried_not_full_read"

## R-02 (card F04_nmdar_intervention_class)
SENTENCE: S810R, the variant of the mouse model, is one of five potency losses: the text prints 1.9-fold;
printed at: /drug_assertions[5]/measured_result_note
  record id: "DR-P9-006"
  record target_id: "GluN2B-selective negative allosteric modulator radiprodil"
  record source: "Banke et al 2026, Brain (PMID 40994429; partial full text read 2026-11-25, ADV-276, receipt FTR-20261125-40994429-01; supplements not held; NOT WWOX EVIDENCE)"
  record locator: "abstract (PMC12677382, publisher bars download of the body): effective at more than 80 percent of the 27 tested disease-associated GRIN1 and GRIN2B missense variants, equally or more effective than at wild-type receptors; blocks synaptic GluN2B receptors in GluN2B-Ser810Arg knock-in slices; delays pentylenetetrazole seizures ; full text (ADV-276): Table 2, Table 3 'Rescue: animals' and the Results paragraph on S810R mice"
  record endpoint: "inhibition of disease-associated GRIN variants, synaptic GluN2B current in a gain-of-function knock-in mouse, incidence of tonic-clonic seizures and latency among animals that seized after pentylenetetrazole"
  record direction: "DECREASE"
  record context: {"disease_id": "GRIN-related disorders and mouse models (not WWOX)", "genotype": "GRIN gain-of-function variants (and mixed comparators)", "species": "human and mouse", "cell_type": "individuals; knock-in mouse slices", "developmental_stage": "children (as reported)"}
  record reading_depth: "partial_fulltext_read"

## R-03 (card P11_magnesium_nmdar_gate)
SENTENCE: 64 of the 229 had failed a first adrenocorticotropic hormone course (50 not seizure-free at its end, 14 relapsed within 1 to 12 months) and all 229 received it with magnesium, so magnesium cannot be separated;
printed at: /drug_assertions[4]/measured_result_note
  record id: "DR-P11-005"
  record target_id: "intravenous magnesium sulfate with ACTH after first-line failure (single arm)"
  record source: "Wang 2023 Pediatr Investig (PMID 36967744, PMC open access); NOT WWOX EVIDENCE"
  record locator: "PMC10030695 Results and Discussion; locators.tsv L23 to L26; staged receipt dated 20261029 (see README)"
  record endpoint: "seizure-free state at the end of a two-week course (infantile spasms)"
  record direction: "UNKNOWN"
  record context: {"disease_id": "infantile spasms after first-line failure (not WWOX)", "genotype": "UNKNOWN", "species": "human", "cell_type": "infants and young children 2 to 24 months", "developmental_stage": "UNKNOWN"}
  record reading_depth: "partial_fulltext_read"

## R-04 (card L01_nrf2_axis)
SENTENCE: by the figure (read by eye, not digitised) IL1b is about 1.9x and TNF about 3.3x of the plotted means, overlap with WT is marginal for IL1b and absent for TNF;
printed at: /disease_assertions[1]/measured_result_note
  record id: "DA-L01-002"
  record target_id: "IL1B and TNF transcripts, P47T cerebellum"
  record source: "Hussain 2023 (PMID 36828035), Fig 9d,e"
  record locator: "PMID36828035 full text (PMC10835625), Results; premises.tsv PR2"
  record endpoint: "qRT-PCR fold change, mutant over WT (n 6 v 6)"
  record direction: "INCREASE"
  record context: {"disease_id": "Wwox P47T/P47T knock-in mouse", "genotype": "P47T homozygote versus WT", "species": "mouse", "cell_type": "cerebellar tissue", "developmental_stage": "adult"}
  record reading_depth: "partial_fulltext_read"

## R-05 (card F01_glutamate_receptor_node)
SENTENCE: Fisher test reported 14 of 19 versus 3 of 15
printed at: /drug_assertions[2]/locator
  record id: "DR-W2-003"
  record target_id: "NMDAR pore blocker memantine; GRIN loss-of-function, indeterminate or no-effect variants (the comparator group also holds five individuals whose variants the authors call non-pathogenic)"
  record source: "Karnstedt 2026, Epilepsia (PMID 41489401; NOT WWOX EVIDENCE; other disease)"
  record locator: "same reading as DR-W2-002; Fisher test reported 14 of 19 versus 3 of 15"
  record endpoint: "clinical improvement"
  record direction: "NO_CHANGE"
  record context: {"disease_id": "GRIN-related developmental and epileptic encephalopathy (not WWOX)", "genotype": "GRIN variants classified loss of function, indeterminate or no effect", "species": "human", "cell_type": "individuals, mostly children", "developmental_stage": "median age 9 years (as reported)"}
  record reading_depth: "partial_fulltext_read"

## R-06 (card A02_proteasome_inhibitor_class)
SENTENCE: ERAD inhibition raised the activity of T191M without any change in its half-life, whereas for I278T the ERAD inhibitor raised both half-life (about 1.6-fold) and activity (about 374 percent of vehicle), so the dissociation of activity from turnover rests on T191M alone;
printed at: /drug_assertions[7]/measured_result_note
  record id: "DR-A02-008"
  record target_id: "CBS p.T191M and p.I278T versus wild type"
  record source: "Mijatovic 2024, PMID 39041895 (Results 3.3 to 3.4, Figures 5 and 6; Discussion); NOT WWOX EVIDENCE"
  record locator: "disease-models/wwox/research/drug_repurposing/broad_recovery_it6_p6_20261029/README.md section 4 row P-5"
  record endpoint: "half-life by pulse-chase and live-cell hydrogen sulphide production after proteasome, lysosome or ERAD inhibition"
  record direction: "INCREASE"
  record context: {"disease_id": "CBS deficiency, homocystinuria (not WWOX)", "genotype": "stable lentiviral expression in a CBS-knockout line", "species": "human", "cell_type": "HEK293A kidney line", "developmental_stage": "culture, 24 h readout"}
  record reading_depth: "partial_fulltext_read"

## R-07 (card M01_neurogenic_output_myc_window)
SENTENCE: radial glia increased in WOREE-derived organoids according to the text, but Fig 2F shows WOREE radial-glia log2 fold change of about +0.05 against about +0.9 in the knockout (a text/figure mismatch, flagged, not resolved), wild-type-like in SCAR12;
printed at: /disease_assertions[2]/measured_result_note
  record id: "DA-M01-003"
  record target_id: "radial-glia and neuron fractions of the single-cell dataset"
  record source: "PMID 42397075, Results (Fig 2D-F); text: SCAR12 radial glia 'similar to WT'; neuron decrease 'not the case in our patient-derived organoids'"
  record locator: "disease-models/wwox/research/drug_repurposing/question_it11_p22_20261031/premises.tsv PR2 (text lines 577 and 585-586)"
  record endpoint: "relative number of radial-glia cells and of neurons by single-cell clustering"
  record direction: "INCREASE"
  record context: {"disease_id": "WWOX-deficient human cerebral organoid model (engineered knockout; NOT a patient allele)", "genotype": "WWOX knockout versus wild type", "species": "human", "cell_type": "cerebral organoid radial glia", "developmental_stage": "organoid, culture week 15 to 16"}
  record reading_depth: "partial_fulltext_read"

## R-08 (card D01_a51)
SENTENCE: for SATB2 the knockout plus A51 arm is also not significantly different from wild type (about 0.7 against about 1.4 % of cells by eye), so SATB2 recovery is neither shown nor excluded;
printed at: /drug_assertions[1]/measured_result_note
  record id: "DR-D01-002"
  record target_id: "SATB2+ and CTIP2+ layer-neuron fractions"
  record source: "DL-THER-089 (same experiment; PMID 42397075)"
  record locator: "discovery_ledger_current DL-THER-089; disease-models/wwox/research/repurposing_known_roads_20261020_scientist-a.md § 2.4a"
  record endpoint: "fraction of layer neurons (SATB2+, CTIP2+)"
  record direction: "NO_CHANGE"
  record context: {"disease_id": "WWOX-deficient human cerebral organoid model (engineered knockout; NOT a patient allele)", "genotype": "WWOX knockout (constitutive engineered null)", "species": "human", "cell_type": "cerebral organoid progenitors (SOX2+ MYC+)", "developmental_stage": "organoid, culture weeks 8 to 15"}
  record reading_depth: "complete_fulltext_read"

## R-09 (card E02_ldh_inhibition)
SENTENCE: the US label of 2026-04-27 states that the human mechanism is unknown and names GABA-A and cytochrome P450 inhibition as possible mechanisms, gives protein binding of 99 percent and no peak concentration).
printed at: /p4_card/pharmacology

## R-10 (card F04_nmdar_intervention_class)
SENTENCE: reversible cholestatic liver injury 77 percent against 27 percent
printed at: /drug_assertions[12]/locator
  record id: "DR-P9-013"
  record target_id: "NMDAR pore blocker ketamine with AMPAR antagonist perampanel"
  record source: "SUPER-CAT, Neurology 2026 (PMID 42837646; abstract only; NOT WWOX EVIDENCE)"
  record locator: "abstract: observational multicentre cohort of 95 adults; resolution 84 percent against 49 percent; reversible cholestatic liver injury 77 percent against 27 percent"
  record endpoint: "resolution of super-refractory status epilepticus after cardiac arrest"
  record direction: "DECREASE"
  record context: {"disease_id": "postanoxic super-refractory status epilepticus, adults (not WWOX)", "genotype": "not applicable", "species": "human", "cell_type": "adults, mean age 66", "developmental_stage": "adult"}
  record reading_depth: "abstract_only"

## R-11 (card P11_magnesium_nmdar_gate)
SENTENCE: The EEG p of 0.04 reproduces from Table 2 as an uncorrected chi-square (11/2 against 6/7: chi-square 4.25, p 0.039), while a Fisher exact test gives 0.097 and a Yates-corrected chi-square 0.099, with two of four expected counts at 4.5;
printed at: /drug_assertions[3]/measured_result_note
  record id: "DR-P11-004"
  record target_id: "magnesium sulfate by injection for three days then an oral magnesium preparation for three months, on top of ACTH and antiseizure drugs"
  record source: "Yadav 2022 Iran J Child Neurol (PMID 35222658, PMC open access); NOT WWOX EVIDENCE"
  record locator: "PMC8752995 Results; locators.tsv L17 to L22; staged receipt dated 20261029 for this paper (see README)"
  record endpoint: "seizure control (clinical response) at 3 months (West syndrome)"
  record direction: "NO_CHANGE"
  record context: {"disease_id": "West syndrome (mostly symptomatic, perinatal hypoxic-ischaemic injury commonest; not WWOX)", "genotype": "UNKNOWN", "species": "human", "cell_type": "children 3 months to 5 years", "developmental_stage": "UNKNOWN"}
  record reading_depth: "partial_fulltext_read"

## R-19 (card J01_glial_reactivity_modulation)
SENTENCE: WWOX knockout versus wild type (4 versus 2 libraries, one laboratory)
printed at: /disease_assertions[6]/context/genotype

## R-24 (card A02_proteasome_inhibitor_class)
SENTENCE: The gain applies to wild type too (CBS wild-type half-life up about 7.7-fold under proteasome inhibition): a boost multiplies residual function and does not repair it.
printed at: /p4_card/evidence_for_and_against/against[0]

## R-25 (card E01_isr_modulators)
SENTENCE: Without amyloid the fly Atf4 comparison was not significant (6 vs 6;
printed at: /p4_card/evidence_for_and_against/against[0]

## R-29 (card L01_nrf2_axis)
SENTENCE: human organoid NRF2 targets do not form a coherent signature (NFE2L2 0.75x, NQO1 0.73x).
printed at: /p4_card/evidence_for_and_against/against[1]

## R-33 (card F03_bumetanide_chloride_gradient)
SENTENCE: Human brain or CSF exposure of bumetanide (the mouse brain to plasma ratio is about 0.015 to 0.02, abstract level).
printed at: /not_known[2]

## R-34 (card A03_client_binding_chaperone)
SENTENCE: an approved active-site chaperone for a lysosomal enzyme: 'amenable' call differs for 12.9 percent of variants between two near-identical assays and no clinical correlation is established (Fabry GLA)
printed at: /abstention_card/adjacent_context_not_wwox_evidence[1]
printed at: /p4_card/sources/external_not_wwox_evidence[1]

## R-35 (card E04_ketogenic_lactate_axis)
SENTENCE: A ketogenic-diet response is reported in 3 of 5 WOREE individuals (lactate 2.4 to 3.3 mmol/L in one individual;
printed at: /not_known[2]

## R-37 (card D01_a51)
SENTENCE: transcript only, raw p, 2 WT versus 4 KO organoids;
printed at: /p4_fields/cellular_context/target_expression

## R-39 (card F03_bumetanide_chloride_gradient)
SENTENCE: Mouse primary pharmacokinetics (abstract level, PMID 25449033 and PMID 33279441): brain to plasma ratio about 0.015 to 0.02;
printed at: /translation/cns_exposure

