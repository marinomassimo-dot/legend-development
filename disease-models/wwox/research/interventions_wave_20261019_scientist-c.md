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

