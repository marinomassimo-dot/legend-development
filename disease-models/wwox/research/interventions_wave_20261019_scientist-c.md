# Interventions wave 2026-10-19 — scientist-c, group H4 (oxygen, hypoxia/hyperoxia, HIF)

Task INTERV-H4-C-20261019 · branch task/INTERV-H4-C-20261019 · lot: group H4 of
`interventions_batch_selection_20261019.md`, tier order. English. Nothing here is medical advice;
public, disease-level edition; class level only (WWOX-null/KO, hypomorph, biallelic LoF, heterozygous
loss). BLOCK-1 caution applies to every oxygen exposure named below.

## 0. Headline, stated plainly

**There is no WWOX-deficient evidence on oxygen as an intervention** (supplemental oxygen, nocturnal
helmet or CPAP, intermittent hypoxia, hyperbaric oxygen, hypoxia therapy) in anything read in this lot.
Every paper below is a substitute: hypoxia, hyperoxia or HIF biology in other genotypes, epilepsy
models, neonatal brain injury or a disease-class comparator. **None of them is WWOX evidence.** They are
read for what transfers and what does not, with the system gap stated per paper.

## 1. Reading discipline

First pass `SOURCE_FIRST`; the comparison phase opened only after the locators were captured. Receipts
are staged under `receipt_staging/scientist-c/` (not appended). PMID 36364214 (Liu 2022) was read in
wave 1 of this actor (receipt FTR-20261019-36364214-01) and is not re-read: no stated question
requires it.

---

## 2. PMID 42420651 — Garg 2026, Nat Metab (tier 1) — hypoxia as therapy in a complex I-destabilising disease

context_policy SOURCE_FIRST · receipt FTR-20261019-42420651-01 · manifest PASS · **not WWOX evidence: WWOX is never named.**

**Measures.** (system) K562 cells (CRISPR fitness, proteomics) and the Htra2 S276C protease-dead mouse (mnd2),
(readout) survival, weight, grid and rotarod, striatal Gfap/Iba1 lesion scores, complex I subunit proteomics and
blots, HIF-target transcripts, iron-sulfur protein abundance, plus recombinant HTRA2/CLPB biochemistry. Chronic 11 percent
inhaled oxygen from P11 about tripled median survival (Fig 1d, read by eye roughly 28 to 75 days; all mice still died
by about day 110), rescued striatal but not thalamic inflammation, and the later the start the smaller the gain
(Extended Data Fig 1a). Complex I subunit levels recovered under hypoxia but complex I enzymatic activity did not
(Fig 2e), and the proposed mechanism, tissue hyperoxia, was never measured directly: the authors use iron-sulfur
protein depletion and lower HIF-target transcripts as proxies and call them "simply suggestive".

**Does not support.** Any statement about WWOX, about humans breathing reduced oxygen, or about a safe dose: the
translation path named is a haemoglobin-affinity drug (see PMID 39965572), not hypoxic gas. Chronic hypoxia was tested
in a mouse with a secondary complex I defect; whether a WWOX-null brain has such a defect is unestablished in this
repository (the WWOX respiratory-complex paper is unavailable). One rescue per genotype is not a class rule: the same
authors note a frataxin-null model gained symptoms but not lifespan.

**Changes for the disease model.** Nothing in claims. It supplies one transferable negative and one prediction
to hold as a hypothesis (not a claim): oxygen therapy responses depend on a primary mitochondrial lesion that raises tissue
oxygen; in the WWOX/HIF1A axis HIF target genes go the opposite way (HIF1A up on WWOX loss), so a "hyperoxia" rationale
cannot be copied across without a tissue pO2 measurement in a WWOX-deficient brain. BLOCK-1: hypoxic exposure is not a
low-risk intervention; the cohort here is mice, n of 3 to 15 per arm, with an author-held patent interest.

---

## 3. PMID 39087877 — Zhao 2025, Sleep (tier 2) — OSA, inflammatory proteins and a WWOX gene-mapping hit

SOURCE_FIRST · receipt FTR-20261019-39087877-01 (partial depth: only Table S18 of the 514-page supplement was opened) · manifest PASS · **WWOX appears only as a list entry; not WWOX evidence on intermittent hypoxia.**

**Measures.** Two-sample Mendelian randomisation of 91 plasma inflammatory proteins on OSA and
oximetry phenotypes in European-ancestry cohorts, followed by a FUMA gene-mapping step. Odds ratios are small (1.06 to 1.16 for
IL-18R1, IL-10RA, SLAMF1, CD5, IL-5; Fig 2), and only IL-18R1 and SLAMF1 survive FDR in the primary analysis.
WWOX is one of seven genes from the FUMA overlap. Supplementary Table S18 (pages 513 and 514) shows the WWOX row built on
**1 positional SNP**, CADD 2.928, no chromatin-interaction tissue, minimum GWAS P 3.28E-06 (the paper's own
instrument threshold is 5E-06, justified because protein loci rarely reach 5E-08); it has no expression or direction column. The Results sentence
calling WWOX "upregulated" therefore has no support in the table it cites.

**Does not support.** That WWOX variation raises OSA risk, that WWOX is up- or down-regulated in OSA, or any inference
about nocturnal hypoxia in WWOX loss of function. WWOX spans a 1.1 Mb fragile-site locus, so a positional hit is expected noise
until fine-mapped; the authors themselves say its effect on OSA "remains uncertain". The PubMed record carries a CommentIn link (not read).

**Changes.** Nothing in the model. It settles the selection-file question 3 only in the negative: no oximetry or sleep-study data
in a WWOX encephalopathy cohort are provided here, and the gene is not a robust OSA locus on this evidence.

---

## 4. PMID 26578889 — Lopez-Ramos 2015, Front Cell Neurosci (tier 2) — brain glycogen, hypobaric hypoxia and seizure susceptibility

SOURCE_FIRST · FTR-20261019-26578889-01 · manifest PASS · **not WWOX evidence (glycogen-synthase knockout mouse).**

**Measures.** Awake five-month-old male mice lacking brain glycogen synthase versus littermates, hippocampal CA1 field
recordings at ground level and 405 mmHg (about 5000 m simulated) for 60 minutes, then kainate and train-stimulation seizure
tests. The knockout showed higher 6-10 Hz power under hypobaric exposure (8.6 and 9.2 against 6.8 and 7.0), a more excitable
CA3-CA1 synapse at baseline whose paired-pulse difference vanished at 60 minutes and returned, and more kainate and train seizures
(after-discharges 64.2 versus 25 percent after kainate).

**Does not support.** Any therapeutic oxygen statement: the hypoxia is a 60-minute hypobaric stressor, the glycogen status is
inferred from the allele (no glycogen assay, no rescue), and the mechanisms offered (astrocytic potassium and glutamate uptake, high-firing
inhibitory neurons) are untested. The text gives two recovery times (24 h and "2-4 h") for one result and different n between text and legends.

**Changes.** Nothing in claims. It supports only a stated gap: the model's GSK3B arm and the hypoglycaemia lethality of the null mouse
both point at energy buffering, and this paper shows energy-buffer loss lowers seizure thresholds in a non-WWOX genotype. Hypothesis grade.

---

## 5. PMID 38074156 — Ma 2023, Front Pharmacol (tier 2) — intermittent hypoxia as the OSAS-epilepsy link (narrative review)

SOURCE_FIRST · FTR-20261019-38074156-01 · manifest PASS · **not WWOX evidence; no data generated.**

**Measures.** Nothing: a review with a keyword search and no inclusion rule. It argues that intermittent hypoxia drives HIF-1 alpha, NF-kB,
IL-6, TNF-alpha, ROS and ER stress, and through them epilepsy. The clinical anchor for oxygen-pressure treatment is a 1994 CPAP series (the
text gives 7 patients then 4 of 5 improving) and a 2022 study; the authors concede hypoxia-epilepsy research is "insufficient" and
that neuroinflammation is a modulator, not a cause.

**Does not support.** That nocturnal CPAP or any oxygen route reduces seizures in a developmental and epileptic encephalopathy, or that
sleep apnoea occurs in WWOX loss of function. The review's own closing call, to first confirm hypoxia during sleep in epilepsy
patients and then test its correction, is the missing experiment; its pointer to the answer is empty.

**Changes.** Selection-file question 3 stays open: no oximetry or sleep-study data in a WWOX cohort are in this literature, and a review
cannot supply them. Discovery lead (hypothesis): ask whether any published WWOX encephalopathy case report states overnight oximetry or
polysomnography ("none stated" is itself the recordable result).

---

## 6. PMID 37726428 — Villa 2023, Sci Rep (tier 2) — repeated postictal hypoxia and interictal cognition

SOURCE_FIRST · FTR-20261019-37726428-01 · manifest PASS · **not WWOX evidence (rat kindling).**

**Measures.** Hippocampal tissue pO2 by implanted optode in 81 male rats over 20 kindled seizures. Vehicle rats' area under 10 mmHg grew from
about 37 to about 440 mmHg min; acetaminophen (before seizures) or nifedipine (after) held it near zero. Interictal pO2 fell with repeated
seizures and recovered about six days after the last one; novel object/context memory failed in vehicle rats and was preserved in drug-treated rats (severity
against performance R2 0.35); isolated mitochondria showed lower calcium retention and lower basal and ATP-linked respiration (n = 5).
Blocking hypoxia did not change seizure duration or Racine stage.

**Does not support.** That oxygen supplementation helps: **no oxygen was given in any arm**; the hypoxia was prevented by
blocking vasoconstriction. It does not show hypoxia drives epileptogenesis (kindling progressed unchanged). Mitochondrial dysfunction
is correlation in a group of five. One timing statement (deficit "3 days" after) conflicts with the Results (24 h, 2 weeks).

**Changes.** Why oxygen is discussed at all in DEE: seizure-linked tissue hypoxia is a measurable harm in this model, but the only
tested remedy was a drug. For the model it is a transferable negative: ictal hypoxia as a feature of a WWOX phenotype is
unmeasured. Class-level BLOCK-1 note: acetaminophen at 250 mg/kg and nifedipine at 15 mg/kg i.p. in DMSO are rat experimental doses, not guidance.

---

## 7. PMID 37876811 — Liang 2023, iScience (tier 2) — HIF-1 alpha/HO-1, ferroptosis markers and epilepsy

SOURCE_FIRST · FTR-20261019-37876811-01 (partial: supplement tables S1 and S3 not read) · manifest PASS · **not WWOX evidence; the only WWOX item is a row in a gene list.**

**Measures.** Plasma untargeted metabolomics (62 patients, 20 controls; free fatty acids, bilirubin up, glutamine, arginine down), a
DisGeNET epilepsy gene set (1215 genes, 73 hubs) with HIF-1 signalling enriched, and PTZ-kindled mice (HIF-1 alpha, HO-1, COX-2, Fe2+,
ferritin, transferrin, GPX4, MDA; n = 3 per bar). Supplementary Table S2 lists WWOX among the 1215 epilepsy genes (row 252); Table S4 puts
the HIF-1 pathway 22nd of the enriched pathways, behind lipid and atherosclerosis, IL-17, cancer and TNF pathways, with HIF1A itself one of the 15 member genes
drawn from a hub set picked by network connectivity (a circularity the paper does not discuss).

**Does not support.** Causation: no intervention on HIF-1 alpha or HO-1 was made (the authors' own limitation), the patient arm reports
no anti-seizure medication, the ROS panel has images without a quantification plot, and three animals per arm carry every mouse conclusion.

**Changes.** The WWOX/HIF1A axis (HIF1A up on WWOX loss, read in the metabolic batch) predicts a pseudo-hypoxic neural state; this paper
shows HIF-1 alpha up in an acquired epilepsy model, so a raised neural HIF-1 alpha is **not specific** to WWOX loss and cannot be a WWOX marker. Question 1 of the
selection file (is neural HIF1A measurable in existing mouse tissue) stays open. WWOX is on the DisGeNET epilepsy list (a database
fact, not a measurement).

---

## 8. PMID 41324728 — Kuang 2025, Mol Neurobiol (tier 2) — HIF-1 alpha/BNIP3 and autophagy in epilepsy

SOURCE_FIRST · FTR-20261019-41324728-01 · manifest PASS · **not WWOX evidence.**

**Measures.** A public blood expression set (34 medication-free cases, 50 controls) and machine-learning classifiers (AUC 0.77 to 0.81; external
check AUC 0.793, interval 0.587 to 0.953, in hippocampal tissue from a different population), then LiCl-pilocarpine rats with the HIF-1
alpha translation inhibitor KC7F2 given 24 h before induction. KC7F2 lengthened latency to the first stage-4 seizure (about 19 to 40 min), lowered LC3 II/I, raised p62
and BNIP3, and increased neuron counts and mitochondrial area; spontaneous seizure counts did not change.

**Does not support.** Treatment of established epilepsy (the drug is a pre-treatment) or reduced seizure number: the Discussion says
HIF-1 alpha inhibition "reduced the number of SRS" while the Results report no change. For the same LiCl-Pilo group, neuron counts in Figure 8 (about 30 HE) and Figure 11 (about 6 HE)
differ about five-fold. The count of DE-ATGs is eleven in the text, ten names listed.

**Changes.** Nothing for claims. Adds the second acquired-epilepsy paper in which HIF-1 alpha is up and pharmacological HIF-1 alpha lowering is neuroprotective in a rodent,
on small n; whether the same holds when HIF1A is already raised by WWOX loss is untested. Class-level BLOCK-1 note: KC7F2 is an experimental anticancer compound.

---

## 9. PMID 41039661 — Huang 2025, Epigenomics (tier 2) — MeCP2, hypoxia and oxidative stress in Rett syndrome (narrative review)

SOURCE_FIRST · FTR-20261019-41039661-01 · manifest PASS · **disease-class comparator, not WWOX evidence.**

**Measures.** Nothing new: it collates breathing abnormalities, oximetry (partial pressure as low as 50 mmHg in about half of patients), mouse
hypoxia responses and an oxidative-stress marker table (Table 1) for MECP2 loss. Two statements matter for the oxygen questions: female
patients' breathing defects are "generally present during awake periods but not during sleep", and hyperventilation in patients occurs "independently of
hypoxemia". The central MeCP2-PARP1-BDNF hypoxia mechanism is labelled speculative by the authors.

**Does not support.** Any benefit of nocturnal or supplemental oxygen or helmet/CPAP in a developmental encephalopathy: the review contains no oxygen-therapy
trial. It does not establish that hypoxia causes the oxidative stress (stated as unanswered) and its Table 1 shows tissue-dependent glutathione direction.

**Changes.** For WOREE/SCAR12/DEE28 the transferable negative is that even in the best-described encephalopathy with hypoxaemia, awake-versus-sleep timing
and the cause-versus-consequence of hypoxia are unresolved, so a "nocturnal" rationale cannot be assumed. Whether WWOX loss produces breathing abnormalities is
not addressed here (a WWOX case-report scan is a lead, below).

---

## 10. PMID 42428241 — Khaksari 2026, Front Neurosci (tier 2) — task-dependent cortical oxygenation in Glut1 deficiency (fNIRS)

SOURCE_FIRST · FTR-20261019-42428241-01 · manifest PASS · **disease-class comparator (brain-energy disorder), not WWOX evidence.**

**Measures.** Relative oxy- and deoxy-haemoglobin change over six cortical regions during auditory and visual N-back tasks in seven people with
Glut1 deficiency (four female) and six controls (all female) at a patient conference. The title and abstract say oxygenation responses were **reduced**.
The body shows otherwise: Figure 4 and the Figure 5 table give patients **higher** left-prefrontal HbO (patients minus controls 1.19 to 1.43,
audio 2-back 1.38 with an interval of 0.08 to 2.69, p = 0.001 unadjusted in the pooled table) and almost every other interval crosses zero; occipital
deoxygenated haemoglobin is lower in patients. The authors then concede the differences "were not consistently supported by statistically significant group
differences after correction for multiple comparisons". Figure 3 shows the patient prefrontal HbO line at a flat positive offset (one trace near 0.008 on a
scale where controls sit near zero) with no task-locked change, so the "increase" may be a baseline offset (a reading of the figure, not a stated analysis).
Two ethics boards are named in different places.

**Does not support.** Reduced task oxygenation in Glut1 deficiency, an adaptive-compensation account, or any use of fNIRS as a biomarker of energy
failure. It is a seven-versus-six exploratory pilot with a 0-back baseline, fixed pathlength and a 0.03 Hz low-pass.

**Changes.** For the selection-file question on a measurable oxygen readout in a DEE analogue: fNIRS is feasible at a conference in older, higher-functioning
patients, but this first dataset does not yet show a disease signal and cannot calibrate expectations for WWOX loss. The model is untouched.

---

## 11. PMID 28119904 — Perrone 2016, Front Pediatr (tier 3) — oxygen use in neonatal care (review)

SOURCE_FIRST · FTR-20261019-28119904-01 · manifest PASS · **preterm-infant safety background, not WWOX evidence.**

**Measures.** Nothing new. It summarises ROS biology (mitochondria, free iron, hypoxia-reoxygenation, hyperoxia), organ toxicity (lung, retina, red cells; rodent
long-term neurodevelopment) and saturation-target trials. The trial lesson that bears on any oxygen manipulation: the lower target reduced severe retinopathy but raised death
before discharge (SUPPORT) and death plus necrotising enterocolitis (BOOST II); guidelines suggest 90 to 95 percent for infants under 28 weeks. Its own alarm advice
is inconsistent (90-95, below 85 and above 93, and 91 and 96 percent in three places), and it concedes the optimum is unknown.

**Does not support.** Any recommendation for a WWOX-deficient child, who is neither preterm nor in this trial population; it has no figures, tables or
methods and does not discuss encephalopathy. BLOCK-1 at class level: both too little and too much oxygen carry harm in neonates, and the safe window in a genetic DEE is
unmeasured.

---

## 12. PMID 40022130 — Serdar 2025, J Neuroinflammation (tier 3) — prenatal inflammation plus hyperoxia in the neonatal rat brain

SOURCE_FIRST · FTR-20261019-40022130-01 (partial: supplementary figure panels not opened) · manifest PASS · **animal safety-direction paper, not WWOX evidence.**

**Measures.** Prenatal LPS (E20) and 80 percent oxygen for 48 h (P3 to P5) in rat pups, outcomes at P5 and P11 (94 pups, both sexes pooled). Hyperoxia alone
caused acute oligodendrocyte degeneration (TUNEL-positive about 15 against about 3 per mm2) and hypomyelination (MBP area about 9 falling to about 6); the double hit gave the
largest brain-volume loss (about 123 to about 103 mm3), deep-cortical thinning, microglial activation and brain IL-6. Supplementary Table S2 shows the MBP-area interaction is
not significant (p = 0.0868), so that effect is hyperoxia-dominated and additive; growth effects were prenatal-LPS-driven.

**Does not support.** Human thresholds (80 percent for 48 h in a rat pup), sex-specific effects (not analysed), long-term outcome (not studied) or synergy for the
myelin readout. The Figure 7 correlations use only two groups (control and double hit) so they largely re-express group separation; brain cytokines (mRNA) and serum cytokines (protein)
differ in method; the data statement says no datasets were generated.

**Changes.** A transferable negative for the oxygen group: hyperoxia is injurious to the developing brain's oligodendrocyte lineage even without a second hit, so "more oxygen"
cannot be assumed harmless in a hypomyelinating genotype. Whether WWOX-null oligodendrocytes are more or less vulnerable is unmeasured (WWOX myelin papers exist but none tests oxygen).

---

## 13. PMID 42763430 — Moore 2026, ASN Neuro (tier 3) — "hyperoxia" and mouse oligodendrocyte progenitors in culture

SOURCE_FIRST · FTR-20261019-42763430-01 · manifest PASS · **in-vitro culture-methods paper; not WWOX evidence and not an exposure model.**

**Measures.** Primary C57BL/6 neonatal mouse OPCs expanded in 2 percent versus 20 percent oxygen. The title's "hyperoxia" is 20 percent, ordinary room-air culture (the authors call it
superphysiological). At 2 percent the cells doubled faster and passaged every four days (Fig 2C, a single curve without error bars), apoptosis at 96 h was 7.2 versus 18.7 percent, and rat OPCs were
insensitive to oxygen (Fig 2F, rat growth higher at 20 percent). After T3, about 63 percent of passage-3 cells became MBP-positive in 20 percent oxygen; at passage 6 only about 19 percent did
(Fig 7). The HIF-1 alpha explanation is a stated suspicion (HIF-1 alpha was not measured), and Sox10 loss between P0 and P3 is "not associated" with failure to reach O4 or MBP, which falls only at P6.

**Does not support.** That clinical hyperoxia inhibits OPC growth but promotes differentiation, any in vivo oxygen effect, or a HIF-1 alpha mechanism. Fig 7 is one to two
experiments with technical replicates; one comparison is printed as p below 0.5.

**Changes.** For the hypomyelination link only a methods point: mouse progenitor biology is oxygen-sensitive in culture, so oxygen is a confound in any in-vitro WWOX-null
oligodendrocyte experiment (control for incubator oxygen). No exposure inference.

---

## 14. PMID 42652189 — Alekseeva 2026, Biomedicines (tier 3) — NMDA and AMPA receptors in hyperbaric-oxygen seizures

SOURCE_FIRST · FTR-20261019-42652189-01 · manifest PASS · **animal safety-direction paper; not WWOX evidence.**

**Measures.** Adult male rats at 6 ATA (100 percent oxygen) until generalised seizure or 90 min. Memantine accelerated every seizure stage; perampanel (1 and 5 mg/kg) delayed stage 4 (about 37 to
about 69 and 57 min) but did not prevent seizures (7 of 8 treated animals seized); methionine sulfoximine (at 5 ATA) accelerated seizures. NeuN counts fell about 19 percent in CA3 after exposure.

**Does not support.** AMPA receptors as the "definitive upstream trigger": the combination arm used monotherapy data re-used from earlier experiments, the abstract says perampanel prevented CA1/CA3
cell death and the combination mitigated it, while section 3.6 says the combination did not protect either field, and Figure 6D shows the CA1 perampanel bar below the HBO2 bar although a significance
bracket links them. The Methods list 94 monitoring animals (abstract: 86) and call Iba-1 an astrocyte marker. Mechanisms (GluN2A zinc, blood flow, disinhibition) are untested.

**Changes.** This is the safety anchor of the group: hyperbaric oxygen provokes generalised seizures within tens of minutes at 6 ATA in rats, clinical protocols use 1.5 to 2.5 ATA for 60 to 90 minutes, and drug
modification of the effect is unreliable (a standard antiseizure NMDA blocker made it worse). For an epilepsy genotype any hyperbaric exposure is BLOCK-1; no WWOX data exist. Doses are rat experimental doses, not guidance.

---

## 15. PMID 39965572 — Blume 2025, Cell (tier 3) — HypoxyStat, a haemoglobin left-shifter as drug-based hypoxia therapy

SOURCE_FIRST · FTR-20261019-39965572-01 · manifest PASS · **preclinical mitochondrial-disease paper with a declared sponsor interest; not WWOX evidence.**

**Measures.** An oral covalent haemoglobin modifier (p50 about 26 to 5.6 mmHg) in wild-type and Ndufs4 knockout mice. At 400 mg/kg daily it raised Epo (about 380 pg/mL against about 130 for 11 percent
inhaled oxygen) and haematocrit (about 52 against 48 percent; up to about 59 percent at 600 mg/kg), and extended knockout lifespan 3 to 4 fold (n = 6 vehicle, 9, 9); started late it extended survival
in n = 10 against n = 6. The comparator GBT-440 did not rescue. Authors state intermittent or sleep-only hypoxia would be insufficient, effect is not acutely reversible except by transfusion, and chronic hypoxia
risks pulmonary hypertension and right heart failure.

**Does not support.** Use in any child or any non-complex-I disease: one mouse model, safety studies in mice and in vitro (three weeks in wild type, a 25-target off-target panel), first-generation compound, no statistics section
in the Methods, and the start of the "late" experiment is given as P50, P55 and P80 in three places.

**Changes.** The one oxygen-lowering route with a mechanism: it works where tissue is hyperoxic because of an ETC lesion (see Garg 2026). WWOX null tissue has no demonstrated hyperoxia, so nothing transfers; the "nocturnal"
route is explicitly not supported by the authors' own statement. Class-level BLOCK-1: polycythaemia and irreversibility.

---

## 16. PMID 38206902 — June 2024, PLOS ONE (tier 3) — acute seizures in neonatal inflammation-sensitised hypoxia-ischaemia (mouse)

SOURCE_FIRST · FTR-20261019-38206902-01 (partial: supplementary not read) · manifest PASS · **animal model where hypoxia is the injury; not WWOX evidence.**

**Measures.** P10 mice, carotid ligation plus 1 h at 8 percent oxygen, with or without LPS 4 h before; continuous EEG (seizures began about 16 s into hypoxia) and DAPI lesion scores at P30 (about 8 against about 23 of 60). Seizure duration, burden
and score were equal; three of the LPS-sensitised mice died in hypoxia after convulsive seizures (none in hypoxia alone).

**Does not support.** That acute seizures play no role: survivors only, EEG and histology in different animals, the mortality difference not analysed, an ordinal score compared by t-test, and a first-time-point p of 0.05 on background suppression called not significant. The group sizes are swapped between the Methods and the Figure 3 legend, and
the three supplementary spreadsheets (seizure review, background EEG, neuropathology scores) are **byte-identical** (one SHA-256) and hold only the seizure table, so the data behind Figures 3C and 4 are not deposited despite the data statement.

**Changes.** A neonatal reference for hypoxic seizures with an inflammatory hit; it informs why oxygen delivery is discussed in neonatal seizure care but contains no oxygen intervention.

---

## 17. What the lot says as a whole (class level, not medical advice)

| Oxygen item | WWOX-deficient evidence | Best substitute read | What the substitute does not carry |
|---|---|---|---|
| supplemental oxygen, neonatal | none | Perrone 2016; Serdar 2025 | preterm and rat-pup populations; no genetic encephalopathy |
| nocturnal helmet, CPAP, intermittent hypoxia | none (OSA gene list has WWOX as one positional hit) | Ma 2023; Zhao 2025; Huang 2025 | review hypothesis; Rett breathing defects are described awake, not asleep |
| hypoxia or hyperoxia in seizures | none | Villa 2023; June 2024; Lopez-Ramos 2015 | rodent models; hypoxia is the injury, no oxygen arm |
| hyperbaric oxygen | none | Alekseeva 2026 | rat seizure model at 6 ATA; protocol differs from clinical 1.5-2.5 ATA |
| hypoxia therapy | none | Garg 2026; Blume 2025 | needs an electron-transport lesion that raises tissue oxygen; not shown for WWOX |
| HIF1A and ROS | WWOX-direct anchor (Liu 2022) read in wave 1 and not repeated | Liang 2023; Kuang 2025 | correlational; HIF-1 alpha is also raised in acquired epilepsy |
| measurable oxygen readout | none | Khaksari 2026 | title contradicts its own figures; n = 7 versus 6 |

**Answers to the three questions of the selection file.** (1) Whether a Wwox-null neuron responds differently to hypoxia or hyperoxia: untested here; neural HIF-1 alpha is raised in two acquired-epilepsy models, so it is not a WWOX marker. (2) Whether ROS is the intermediate between WWOX loss and mitochondrial stress: nothing new beyond the wave-1 reading of Liu 2022; the hypoxia-therapy precondition (a complex I lesion that raises tissue oxygen) is not shown. (3) Whether nocturnal or ictal hypoxia belongs to the DEE phenotype: no oximetry or sleep data on a WWOX cohort exist in anything read; the one encephalopathy comparator (Rett) places its breathing defects awake.

**Extra self-chosen search (lot exhausted).** Four PubMed queries (WWOX with brain or neuron and hypoxia, ischaemia or ROS; with stroke, hypoxic-ischaemic or reoxygenation; with oxygen consumption or respiration; with oxygen and epilepsy or encephalopathy) returned 5, 4, 3 and 0 records. Nothing new qualified: two records were already read (wave 1 and another actor), one has a receipt from another actor, two Alzheimer's-disease WOX1 reviews and the four WWOX/HIF-1 papers named in the commit candidate have no open body (Europe PMC and OpenAlex checked). They are parked with that cascade.

**Skills declined, with reasons.** `legend-discovery` and `legend-hypothesis-forge`: no lead matured beyond the staged IPOTESI items; `legend-safety-triage`: no molecule was triaged (memantine, perampanel and HypoxyStat appear as literature objects in rodents); `legend-locator-audit`: no consolidated baseline claim is narrowed or reversed; `legend-commit`: scientists do not touch the four current files.
