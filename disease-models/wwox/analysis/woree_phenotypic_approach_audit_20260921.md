# WOREE "phenotypic-driven approach" audit — Riva 2022 (PMID 35573960)

**Source.** Riva A, Nobile G, Giacomini T, Ognibene M, Scala M, Balagura G, Madia F, Accogli A,
Romano F, Tortora D, Severino M, Scudieri P, Baldassari S, Musante I, Uva P, Salpietro V,
Torella A, Nigro V, Capra V, Nobili L, Striano P, Mancardi MM, Zara F, Iacomino M.
*A Phenotypic-Driven Approach for the Diagnosis of WOREE Syndrome.*
**Front Pediatr** 2022;10:847549. PMID **35573960**, PMCID **PMC9100683**,
DOI [10.3389/fped.2022.847549](https://doi.org/10.3389/fped.2022.847549).
Metadata retrieved from **PubMed**; full text retrieved from **PubMed Central**.
Identifiers verified against PubMed metadata before any file was written — all match,
including the full 23-author list.

**Artefact.** `files/fulltext/PMID35573960_PMC_MCPtext.txt` — 19,348 bytes,
sha256 `fbb3de8265ce128c53229985b993cf7cb3a17b2fc0d57b27db624444a66f4acc`.
Verbatim MCP body only; no abstract, no header, no edits.

**Licence.** `get_copyright_status` returned `license.type: null`, `license.url: null`,
`is_open_access: false`, with `checked_sources: ["pubmed"]` and `found_in_pmc: 0` — i.e.
**PMC was never consulted**, so that flag carries no information about PMC retrievability.
The copyright statement returned is "Copyright © 2022 Riva, Nobile, ... Zara and Iacomino."
Frontiers publishes under CC BY, but **this audit does not treat the licence as established**:
what is established is that the PMC body fetched non-empty on a single attempt.
Licence status therefore: **asserted-CC-BY-by-publisher-policy, not confirmed by the tool.**

---

## 0 · VERDICT

**This paper is a single-patient case report. It makes no claim that phenotype predicts WWOX
genotype class, and it explicitly reproduces the opposite — "A recent review did not highlight a
clear correlation between the extension of[WWOX] mutation and the onset or severity of epilepsy."
It therefore does not contradict Oliver 2023; the title's "phenotypic-driven approach" is a
narrative diagnostic heuristic for recognising the *disease*, never an algorithm for inferring the
*allele class*, and the paper's own conclusion subordinates it to genetics. Its load-bearing
contributions to LEGEND are elsewhere: a complete four-way therapeutic negative (vigabatrin, ACTH,
CBD oil, ketogenic diet all failed in one biallelic-null patient), explicit prose evidence of
cerebellar involvement (inferior vermis hypoplasia from day 7, dentate-nuclei signal change at
2y4m) that cuts against the cerebellar-sparing hypothesis, and a demonstration that a single-exon
WWOX deletion was invisible to exome CNV calling.**

---

## 1 · Study design and N

**Design: a single-patient case report with a narrative literature discussion. Not a cohort, not a
series, not a meta-summary. N = 1 of the authors' own.**

The paper says so in its own voice: "Here we report the case of a patient with a peculiar
clinic-radiological pattern suggestive for a WOREE syndrome, forcing us to further investigate the
underlying genetic etiology." (Introduction, final sentence.) The abstract: "We report a boy with
a peculiar clinic-radiological pattern supporting the diagnosis of WOREE syndrome."

The Results open "Our patient was the first child of non-consanguineous parents coming from the
same small Sicilian area, with unremarkable family history ()." Singular throughout. The trio
(proband + two unaffected parents) is the sequencing unit; only the proband is affected.

The only other patients in the paper are cited, not studied: "Previous studies (,), describe 54
patients with WOREE syndrome associated with biallelic[WWOX] pathogenic variants." Those 54 are
handled entirely by citation — no re-abstraction, no table, no pooled statistic.

String evidence for the design claim (roman-type words, so the zeros are informative):
`cohort` = 0, `prospective` = 0, `retrospective` = 0, `sensitivity` = 0, `specificity` = 0.

---

## 2 · What the "phenotypic-driven approach" concretely is

**It is a narrative, retrospectively stated heuristic. It is not a validated algorithm, there is no
score, no criteria set, no ordering, no operating characteristics, and it is never tested.**

The whole of the approach is one sentence, and it is *post hoc* — it says what led *these* clinicians
to *this* diagnosis, in the past tense, about a case they had already solved:

> "In the present case, the main characteristics that lead to the diagnosis of WOREE were the
> dysmorphic features, the severity of epilepsy, and mostly the neuroradiological pattern."

That sentence gives three features and one ranking word ("mostly" → neuroradiology first). It is
the entire content of the title.

**Grammatical-mood check (the failure mode named for this session).** The mood is narrative-past
and hedged, not declarative-general:

- Title: "A Phenotypic-Driven Approach **for** the Diagnosis" — a noun phrase, no verb, no claim.
- Abstract Background: "Clinicians **have become more confident** with the phenotypic picture of
  WOREE syndrome, **allowing** earlier clinical diagnosis." — a statement about clinicians'
  confidence, not about the phenotype's discriminative power.
- Discussion close: "Nowadays, clinicians have become much more confident with the phenotypic
  picture of WOREE syndrome, allowing early clinical diagnosis to be made. **Yet, genetics is
  pivotal to making the definitive diagnosis** and for parental counseling."
- Abstract Conclusions: "**Genetic testing remains crucial** in establishing the definitive
  diagnosis of WOREE syndrome."

So the paper's own conclusion **subordinates** the phenotypic approach to genetic testing. The
title is the strongest form of the claim that appears anywhere in the paper, and nothing in the
body raises the claim to that level. **Any downstream re-voicing of this as "phenotype is
sufficient / near-sufficient for WOREE diagnosis" would be an inflation of the source.**

**The paper undercuts its own first feature in the next sentence.** Having named dysmorphism as a
leading feature, it immediately writes: "Nevertheless, dysmorphic features are not a constant
feature of the whole WOREE phenotype since they may be absent in ∼52% of the patients () (,)."
A feature absent in roughly half of cases has near-zero diagnostic yield when absent.

**The index patient lacks the cardinal literature feature.** The paper states "The most-reported
clinical features are acquired microcephaly, severe and polymorphic seizures, and neurodevelopmental
delay." The word `microcephal*` occurs three times in the whole text and **not once refers to this
patient** — the three occurrences are SCAR12 ("non-progressive microcephaly"), the Mignot 2015
definition ("progressive microcephaly") and the 54-patient literature summary ("acquired
microcephaly"). The only two head-circumference values given for the patient are **OFC 33 cm
(50th centile) at birth** and **OFC 41 cm (25th centile) at 4 months** — neither microcephalic,
and the paper never reports a later measurement. This is an internal weakness of the
phenotypic-driven argument that the paper does not address.

**One Discussion feature has no Results antecedent.** The Discussion lists "round hypotonic face"
among the patient's dysmorphic features; the Results dysmorphism list is "OFC 41 cm (25°centile),
short neck, low anterior hairline, bushy eyebrows, long eyelashes, and broad nasal bridge (,)" —
"round hypotonic face" is not in it. Minor, but it is a Discussion addition, not a Results finding.

Corroborating string evidence: `algorithm` = 2 occurrences, both in the array-CGH Methods (the
"diploid peak centralization algorithm and the legacy centralization algorithm"); `score` = 1,
the Apgar score; `criteria` = 1, "genetic criteria for very rare variants". **There is no
diagnostic algorithm, score or criteria set anywhere in this paper.**

---

## 3 · Does it claim phenotype predicts genotype class?

**No. It makes no such claim, and it states the opposite of one, in prose, in its own Discussion.**

The decisive sentence:

> "A recent review did not highlight a clear correlation between the extension of[WWOX] mutation
> and the onset or severity of epilepsy ()."

(Discussion; the empty parenthesis is the deleted citation — see §9. The gene symbol is deleted by
the extractor, hence "extension ofmutation" in the raw body.)

That is Riva 2022 *importing* a negative finding, not asserting a positive one. It concerns exactly
the axis Oliver 2023 measured: onset and severity of epilepsy versus the genotype.

The one genotype-to-phenotype statement the paper does make is at **disease level, not allele
level**, and it is generic review framing, not a finding of this work:

> "There are two main neuropathological phenotypes correlated with[WWOX] bi-allelic pathogenic
> variants: SCAR12 spinocerebellar ataxia-12 (SCAR12 syndrome) and[WWOX]-related epileptic
> encephalopathy (WOREE) (,).[WWOX] missense mutations lead to hypomorphic alleles related to
> SCAR12 syndrome, an early-childhood onset cerebellar ataxia associated with non-progressive
> microcephaly, generalized tonic-clonic epilepsy, and developmental delay (,). On the other hand,
> a complete lack of[WWOX] expression correlates with WOREE."

This is the standard missense→SCAR12 / null→WOREE dichotomy, fully citation-supported and
contributing no new data. It is a **coarse two-bin statement between two named syndromes**. It says
nothing about predicting genotype class *within* the WOREE phenotype, which is Oliver's question.
It should not be cited as this paper's finding: the paper generated no genotype–phenotype data.

It is also worth recording that the paper's own patient is a **counter-example to the "typical
onset" expectation** while remaining inside the expected genotype class: "The average epilepsy onset
in WOREE is 2–3 months (range 1 day to 7 months) (,). Interestingly, our patient had the earliest
epilepsy onset, presenting on the first day of life" — a biallelic-null patient at the extreme tail
of the onset distribution, which widens rather than narrows the phenotype–genotype mapping.

---

## 4 · Seizure data

**Age at onset — first day of life, within hours of birth.** "A few hours after birth, he presented
hypoglycemia, respiratory distress associated to tonic-clonic seizures, and horizontal nystagmus."
And in the Discussion: "our patient had the earliest epilepsy onset, presenting on the first day of
life, and his multi-daily tonic seizures never responded to any pharmacological treatment."

**Semiology.** Neonatal: tonic-clonic. Established: "He presented multi-daily asymmetric tonic
seizures (with eye and head deviation to the left, left arm hyperextension and right arm flexion)".
Frequency at last report: "The multi-daily seizures, up to 50 attacks per day, strongly disturbed
his sleep."

**EEG, three time points, all quoted in full.**
1. Neonatal: "The electroencephalography (EEG) showed monomorphic delta activity with epileptiform
   discharges often accompanied by a sustained rhythmic jerking of the limbs."
2. At 4 months, interictal: "EEG during wakefulness was characterized by slow monomorphic activity
   and multifocal independent spikes and spikes and waves."
3. At 4 months, ictal correlate: "corresponding on EEG to a generalized high voltage slow wave with
   overlap of low amplitude fast activity and generalized voltage attenuation."
4. Evolution: "Over the years, the interictal epileptiform anomalies increased and the background
   activity became more disorganized."

**Two informative roman-word zeros on EEG.** `hypsarrhythmia` = 0, `burst` = 0, `West syndrome` = 0,
`spasms` = 0 in the entire extracted body. These are roman-type clinical words, not italicised
tokens, so **these zeros are evidence, not instrument artefact**: this patient is *not* described as
having hypsarrhythmia, epileptic spasms, West syndrome or burst-suppression. That matters, because
ACTH and vigabatrin — the two spasm-directed agents — were nevertheless used.

**Treatments, with the repository's four standing-interest interventions each addressed explicitly.**

| Standing-interest agent | Present? | What the paper says |
|---|---|---|
| **Vigabatrin** | **Yes** | Listed among drugs that "were ineffective", *and* retained in the current regimen: "Current ASMs include vigabatrin (70 mg/kg/day)" |
| **ACTH** | **Yes** | "Moreover, three cycles of ACTH had very poor results." |
| **Cannabidiol** | **Yes, as "CBD oil"** | Listed among the ineffective agents. The literal string `cannabidiol` = 0, but `CBD` = 1 — this is a **naming difference, not an absence**, and must not be recorded as a cannabidiol negative-by-zero |
| **Ketogenic diet** | **Yes** | "The ketogenic diet did not significantly improve seizures and was suspended." |

Full verbatim treatment sentence: "Several anti-seizure medications (ASM) were ineffective (i.e.,
valproate, vigabatrin, clonazepam, clobazam, levetiracetam, rufinamide, and CBD oil) or determined
adverse events such as extreme drowsiness or increased secretions (i.e., phenobarbital, nitrazepam).
Moreover, three cycles of ACTH had very poor results. The ketogenic diet did not significantly
improve seizures and was suspended. Current ASMs include vigabatrin (70 mg/kg/day), clobazam
(1 mg/kg/day) and clonazepam (0.9 mg/day)."

**Nothing worked.** "his multi-daily tonic seizures never responded to any pharmacological
treatment." Non-seizure pharmacology also failed: "His severe spasticity and dystonia responded
poorly to pharmacological treatment with baclofen."

**An internal tension worth flagging, not resolving.** Vigabatrin appears simultaneously in the
"ineffective" list and in the current regimen at 70 mg/kg/day. The paper offers no explanation. Two
readings are possible — partial benefit below the "effective" threshold, or inertia — and the text
does not distinguish them. No visual-field or MRI-toxicity monitoring is mentioned in connection
with the retained vigabatrin. **This is reported, not recommended; nothing here is medical advice.**

---

## 5 · Neuroimaging, and the cerebellum

**Four MRI time points are reported, all in Results prose, with figure legends as a second textual
source. The cerebellum is mentioned, repeatedly, and it is abnormal from day 7.**

**Day 7 and 2 months (Results prose):** "Brain magnetic resonance imaging (MRI) studies performed
at the age of 7 days and 2 months showed frontal bilateral periventricular cysts, enlargement of
cerebral subarachnoid spaces, especially in the frontal-temporal regions, **and a small inferior
vermis**."

**4 months (Results prose):** "Brain MRI at 4 months of age revealed delayed myelination, reduction
of the white matter volume, and reabsorption of the periventricular cysts ()." Plus "Brain MR
spectroscopy showed small lactate peaks."

**2 years 4 months (Results prose):** "Brain MRI performed at 2 years and 4 months revealed mild
progression of the brain atrophy and marked reduction with signal alterations of the periventricular
white matter, especially in the parietal-occipital regions, **thinned corpus callosum**, and squared
lateral ventricles. **Mild signal alterations were also noted at the level of the pons and dentate
nuclei ().**" Plus "Brain MR spectroscopy demonstrated mild NAA reduction and the absence of lactate
peaks ()."

**Discussion prose:** "Similarly, our patient showed mild progressive brain atrophy, delayed
myelination, and **inferior cerebellar vermis hypoplasia**."

**Discussion prose, the paper's own novelty claim:** "Interestingly, in the later phase of the
disease, we noticed a peculiar leukoencephalopathy pattern, characterized by marked volume reduction
and signal alterations of the periventricular white matter, especially in the posterior regions,
with squared lateral ventricles and thinned corpus callosum, like in the prematurity-related
periventricular leukomalacia. At the moment, there are no data on the evolution of neuroimaging
findings in the late phases of WOREE, and more studies are needed to verify if this periventricular
leukomalacia-like pattern is a typical feature of the disease." — note the mood: "we noticed",
"more studies are needed to verify". **An n=1 observation offered as a hypothesis, explicitly.**

**Prose versus figure — the D-14 question, answered.** Every neuroimaging finding above appears in
**Results or Discussion prose**. Uniquely for this extraction, the **figure legends also survived**
(see §9), and they corroborate rather than carry the claims:

- FIGURE 2 legend: "Sagittal T1-weighted image shows hypoplasia of the corpus callosum (thick arrow)
  **and inferior cerebellar vermis** (arrowhead)."
- FIGURE 3 legend: "There are mild T2/FLAIR hyperintensities also at the level of the pons (arrows)
  **and cerebellar dentate nuclei** (arrowheads). ... Sagittal T1-weighted image depicts marked
  thinning of the posterior sections of the corpus callosum (thick arrow), **and inferior cerebellar
  vermis hypoplasia** (arrowhead)."

**Therefore no neuroimaging claim in this audit rests on an uninspected figure image. D-14 does not
bite here.** The one thing that *is* figure-only and therefore not adjudicable is the visual
appearance itself — the grading of severity, the exact extent of the signal change, anything a
reader would have to measure off the image.

**Bearing on the cerebellar-sparing question, stated carefully.** The repository holds a standing
question arising from (a) a rat model with ~95% penetrant ataxia and a histologically intact
cerebellum, and (b) a human case-series abstract asserting a pattern "in which the cerebellum is
spared". **This paper is evidence against generalising that sparing to WOREE.** Its patient has
inferior vermis hypoplasia documented at 7 days — i.e. **present at birth, developmental, not
acquired** — persisting at 2y4m, plus dentate-nuclei signal abnormality appearing later. The
Discussion further reports vermis hypoplasia as a *literature-typical* WOREE feature: "structural
brain abnormalities including corpus callosum hypoplasia, progressive cerebral atrophy, **cerebellar
vermis hypoplasia**, and white matter hyperintensity representing delayed myelination have been
described in most cases."

Two cautions on that inference. First, **vermis hypoplasia is a midline structural finding and is
not the same claim as cerebellar-hemisphere or Purkinje-cell involvement** — a cerebellum can be
vermis-hypoplastic and otherwise unremarkable. Second, this is n=1, and the "described in most
cases" statement is a narrative literature assertion with a deleted citation, not a counted result.
What the paper licenses is: *cerebellar structural abnormality is reported in this WOREE patient,
in prose, from the first week of life* — enough to make an unqualified "cerebellum is spared in
WWOX disease" claim untenable as a universal, not enough to establish a rate.

**Thalamus: absent.** `thalam*` = 0. Roman-type word, so this is an informative zero — **no thalamic
involvement is reported in this patient.**

**Corpus callosum: present and progressive.** Hypoplasia in the 4-month figure legend, "thinned
corpus callosum" in Results prose at 2y4m, "marked thinning of the posterior sections" in the FIGURE
3 legend, and "corpus callosum hypoplasia" named as a literature-typical feature.

**White matter: the dominant abnormality.** Delayed myelination at 4 months, volume reduction, then
the posterior-predominant periventricular leukoencephalopathy at 2y4m. The paper's own framing is
the periventricular-leukomalacia analogy quoted above.

**Spectroscopy, a detail LEGEND should not lose:** lactate peaks present at 4 months, **absent** at
2y4m, with NAA reduction appearing. A transient lactate elevation that resolves is an atypical
metabolic trajectory; the paper records it without interpreting it, and the extensive metabolic
work-up was negative ("Specific tests for metabolic disorders ... resulting within normal limits").

---

## 6 · Variants

**Genotype: compound heterozygous, both alleles null. No missense, no splice-site allele.**

**Allele 1 — maternal, nonsense.** "Exome Sequencing detected the stop variant ():c.790C > T
(p.Arg264*) in one allele of[WWOX] in the proband and his unaffected mother." A stop codon at
residue 264 of a 414-residue protein; the paper does not discuss NMD or residual product.

**Allele 2 — paternal, single-exon genomic deletion.** "Q-PCR analysis showed both the proband and
his father had the same deletion of exon 6 (), which by means of trio-based array-CGH 180K proved to
be a 84,828-bp (g.chr16:78,360,803–78,445,630) deletion ()." Transcript consequence demonstrated at
RNA level: "The RT-PCR product () showed the proband and his father had the same deleted exon 6
fragment (), fusing exon 5 and 7 of[WWOX] ()."

**Splice-acceptor alleles: none.** `acceptor` = 0, `donor` = 0 — roman-type words, so these are
informative zeros. `splice` = 1, and its single occurrence is a Methods filter criterion ("splice
site (SS)"), not a patient allele.

**SDR-domain missense alleles: none.** `SDR` = 1, its single occurrence being the generic protein
description: "It encodes a 46 KD, 414-amino acid protein that contains two WW domains at the NH2
terminus and a central short-chain dehydrogenase/reductase (SDR) domain ()." `missense` = 1, in the
generic SCAR12 sentence quoted in §3. **This paper contributes no missense allele data.**

**The methodological finding, which is the paper's real contribution.** The exon-6 deletion was
**missed by exome sequencing, including its CNV caller**: "No other potentially pathogenic variants
were identified in the exome. **CNVs analysis was also unremarkable.** Due to the strong clinical
suspect, we performed additional analysis to reach genetic confirmation." It was recovered only by
RT-PCR on fibroblasts, Sanger of the fusion product, Q-PCR dosage, and 180K array-CGH. The abstract
generalises this: "our findings suggest that targeted Next Generation Sequencing-based testing may
occasionally show technical pitfalls, prompting further genetic investigation in selected cases with
high clinical suspicion."

Two consequences LEGEND should carry:
- **Single-exon WWOX CNVs are a known blind spot of standard exome CNV calling.** Published WOREE
  genotypes in which only one pathogenic allele was found may be under-ascertained rather than
  genuinely monoallelic. This is a reason to treat allele-class census figures as lower bounds.
- **This group has patient fibroblasts and runs RT-PCR on WWOX transcripts.** Methods: "The RT-PCR
  derived from fibroblast extracts of patient and unaffected parents and age-matched neurotypical
  control". That is precisely the assay type the repository has recorded as missing for a splice
  allele (no RNA data on variant-carrying cells). Capability observation only, not a claim.

---

## 7 · Natural history

**The patient is alive at last report; no death, no survival analysis.** `died` = 0, `survival` = 0,
`autopsy` = 0 — roman-type words, informative zeros. `death` = 2, both in generic disease-level
statements about WOREE, not about this patient: "leading to severe disability and death within the
first years of life" (Introduction) and Mignot's definition including "premature death".

**Latest ages anchored in the text:** brain MRI at 2 years 4 months; "At 3 years, gastrostomy was
placed due to failure to thrive and severe gastroesophageal reflux"; and the FIGURE 1 legend refers
to "Portraits of patient II-1 at 4 years." The narrative ends at "the last hospitalization" without
a stated age. **So: alive at approximately 4 years, with no upper bound given.**

**Developmental trajectory: no trajectory. A floor from the start.**
"No developmental milestones were achieved."
"At the last hospitalization, he showed profound intellectual disability, he was unable to follow
objects and he never acquired sitting position."

**Progressive systems involvement.** Movement disorder: "The multi-daily seizures progressed along
with a severe movement disorder characterized by spastic tetraparesis and dystonia of limbs and
trunk, worsening during periods of distress or discomfort." Respiratory and orthopaedic: "He
developed scoliosis, and airway secretion accumulation required cough machine use." Feeding:
gastrostomy at 3 years. Urogenital, a detail rarely recorded in WOREE reports: "He presented
bilateral ascending testis from the second month of life."

**Sensory systems intact.** "Ophthalmological examination and auditory brain stem response did not
show any pathological findings." This is a direct prose negative and a notable one — the Mignot
definition the paper itself quotes includes "ophthalmological involvement", and **this patient does
not have it**, while still being biallelic-null. Another phenotype-does-not-follow-genotype datum.

**Metabolic work-up negative.** "Specific tests for metabolic disorders (including neurotransmitters,
folate, pterins, amino and organic acids, carnitine profile, plasma very long-chain fatty acids) were
performed both on cerebrospinal fluid (CSF), blood and urine samples resulting within normal limits."

---

## 8 · Abstract versus results

**There is no softening and no inversion of a result. There is one genuine attribution error, one
direction-of-hedging anomaly, and substantial omission. Reporting each explicitly, including the
negative finding, as required.**

**8.1 — One real discrepancy: the abstract misattributes the exon-5/7 fusion to Q-PCR.**

Abstract: "The Q-PCR product showed that the proband and his father harbored the same deleted
fragment, **fusing exons 5 and 7** of[WWOX]."

Results: "**The RT-PCR product** () showed the proband and his father had the same deleted exon 6
fragment (), **fusing exon 5 and 7** of[WWOX] (). **Q-PCR analysis** showed both the proband and his
father had **the same deletion of exon 6** ()."

The Results assign the fusion to RT-PCR (with Sanger confirming it) and assign to Q-PCR only the
dosage demonstration of exon 6 loss. The abstract collapses the two assays into one and credits the
transcript-level finding to the DNA dosage assay. This is an **assay-attribution error, not a
result-strength error** — the underlying findings are both real and both reported. It matters only
for anyone citing this paper for *which technique recovers a transcript-level fusion*. Note also
that "Q-PCR product" is not a meaningful object in the Results' own usage.

**8.2 — The hedging runs the unusual direction: the body is harder than the abstract.**

Abstract Background: "The disease ... **usually** leads to severe disability **or** death within the
first years of life."
Introduction: "leading to severe disability **and** death within the first years of life (,)."

The Introduction states it absolutely and conjunctively; the abstract adds "usually" and changes
"and" to "or". This is the **inverse** of the standard failure mode — here the abstract is the more
careful text and the body overstates. Neither statement is about this patient, and neither is
supported by data generated here; both are citation-carried disease-level generalisations.

**8.3 — Omission is large but structural, and in one place it is load-bearing.**

The abstract omits entirely: the entire treatment history (all nine named drugs, ACTH, the ketogenic
diet), every neuroimaging finding, the EEG, the spectroscopy, the developmental outcome, and the
patient's current age. For a four-part structured abstract of a case report this is ordinary.

But one omission is not ordinary. **The abstract's Background and Conclusions both trade on the
phenotypic-diagnosis framing, and the abstract never states which phenotypic features were used.**
A reader of the abstract alone gets "Clinicians have become more confident with the phenotypic
picture of WOREE syndrome, allowing earlier clinical diagnosis" and "We report a boy with a peculiar
clinic-radiological pattern supporting the diagnosis" — the content that would let them evaluate the
claim (three features, one of them absent in ~52% of patients, one of them — microcephaly — absent
in this very patient) lives only in the Discussion. **The title plus abstract are more supportive of
a phenotype-first approach than the body is.** That is the finding of interest for §8, and it is a
title/abstract framing effect rather than a misreported result.

**8.4 — No inversion.** Every numerical and genetic result in the abstract matches the Results
**of the published case report `PMID 35573960` (Riva *et al.*, *Front Pediatr* 2022;10:847549)**,
whose single proband's alleles these are: c.790C>T (p.Arg264*) inherited from the unaffected mother;
the 84,828 bp deletion at g.chr16:78,360,803–78,445,630 removing exon 6, inherited from the
unaffected father. Checked one by one. No result is reversed, and no negative result is presented as positive.

---

## 9 · Extraction-defect report (instrument state)

**The italic-deletion defect is present and severe.** Direct evidence in the body: "biallelic
pathogenic variants in **thegene**", "this severe phenotype **asencodes** for a transcriptional
regulator", "the phenotype **in-null mice**", "**Thegene** is located at 16q23.3-q24", "the extension
**ofmutation**", "**().knockout** animal models". Every one of these is a deleted italicised *WWOX*.

**The literal string `WWOX` appears exactly twice in the extracted body**, and both occurrences are
the PCR primer names in Methods (`WWOX_ex4F`, `WWOX_ex7R`) — set in roman/monospace and therefore
spared. **A count of `WWOX` in this artefact is an instrument reading of the extractor's italic
handling, not a measure of how often the paper discusses the gene.** In every quotation in this
document I have restored the gene symbol as `[WWOX]` and flagged the restoration.

**Cross-reference deletion confirmed:** 23 empty `()` and 10 empty `(,)` in the body. All inline
citations and all figure call-outs are gone. This means every "(,)" in a quoted sentence marks
missing evidential support I cannot chase, and specifically that **I cannot identify which review is
meant by "A recent review did not highlight a clear correlation..."** — the citation is deleted. That
sentence's content is quotable; its provenance is not recoverable from this artefact.

**Italic-class zeros recorded but NOT offered as evidence anywhere above:** `in vitro` = 0,
`in vivo` = 0, `P <` = 0, `P =` = 0, `Wwox` = 0. These are instrument readings.

**Roman-class zeros, which ARE informative and are used as evidence above:** `hypsarrhythmia` = 0,
`burst` = 0, `West syndrome` = 0, `spasms` = 0, `thalam*` = 0, `acceptor` = 0, `donor` = 0,
`cohort` = 0, `prospective` = 0, `retrospective` = 0, `sensitivity` = 0, `specificity` = 0,
`died` = 0, `survival` = 0, `autopsy` = 0. One near-miss handled explicitly: `cannabidiol` = 0 but
`CBD` = 1 — **not a negative**, a naming difference (§4).

**Did a patient table survive? There is no table in the extracted text — `Table` = 0, and no TABLE
block — and on balance I judge that no patient table existed in the original.** The reasoning: this
extraction is **atypical in that all three figure legends survived in full** (FIGURE 1, 2 and 3
blocks are present at lines 31, 35 and 39 of the artefact), so the extractor was not stripping
float-object captions wholesale on this document; a TABLE caption would plausibly have survived the
same way. Combined with the design — a single-patient report whose entire clinical history is
narrated in continuous Results prose, with no "as shown in Table" construction anywhere — the most
likely state is that the paper has three figures and no table. **This is a reasoned judgement, not a
verified fact**, and it should be treated as the weakest assertion in this document. The practical
risk is low: because N = 1 and the phenotype is narrated exhaustively in prose, there is no
plausible patient table whose loss would hide phenotype data from this audit.

**Figures themselves: not inspected, and none needed.** No image was available. Per D-14 no negative
asserted only by a figure has been adjudicated here — and as established in §5, no neuroimaging
claim in this audit rests on figure-only evidence, because each has a prose antecedent in Results or
Discussion.

---

## 10 · What LEGEND may now infer

**10.1 — Riva 2022 and Oliver 2023 do not disagree. They answer different questions, and on the one
axis where they touch, Riva reproduces Oliver's negative.**

Oliver 2023 asks, within a WWOX cohort: *does genotype class predict age at seizure onset?* Its
Fig. 4B answers no, p = .65.

Riva 2022 asks: *can a clinician recognise WOREE syndrome — the disease — from phenotype before the
genetics returns?* That is a question about discriminating WWOX disease from the rest of the
early-infantile epileptic encephalopathy differential. It is **not** a question about discriminating
null from hypomorphic alleles within WWOX.

Two claims of the form "phenotype is informative" that operate at different levels are not in
conflict. A phenotype can be characteristic enough to point at a gene while carrying no information
about which allele class within that gene. **That is in fact the position both papers occupy**, and
Riva says so explicitly: "A recent review did not highlight a clear correlation between the extension
of[WWOX] mutation and the onset or severity of epilepsy ()."

**Consequence for the working model.** The apparent tension flagged in the full-text queue entry for
PMID 35573960 ("tocca direttamente la questione se il fenotipo predica la classe genotipica — che
Oliver Fig. 4B nega sull'asse dell'esordio") **resolves as a non-conflict.** No claim needs
re-opening on that basis. If anything, Riva is a weak *corroborator* of Oliver, because it is an
independent group importing the same negative.

**Two further Riva observations point the same way — biallelic null, atypical phenotype:**
- Onset at day 1 against a WOREE mean of 2–3 months: the extreme tail of the distribution, in a
  patient whose genotype is unambiguously null/null.
- Absent ophthalmological involvement, despite the disease definition the paper itself quotes
  including it, and despite no microcephaly being documented.

Both strengthen, rather than weaken, the proposition that **genotype class is a noisy proxy for
phenotype in WWOX disease** — which is the existing position recorded in the working model
(entry 033).

**10.2 — A four-way therapeutic negative in a single biallelic-null patient.** Vigabatrin, ACTH,
CBD oil and the ketogenic diet were each tried and each failed in the same child, alongside
valproate, clonazepam, clobazam, levetiracetam and rufinamide, with phenobarbital and nitrazepam
stopped for adverse effects. This is the repository's four standing-interest interventions, all in
one patient, all negative. n = 1, uncontrolled, no duration or dose given except for the current
regimen — so this is a **data point, not a trend**, and it neither supports nor contraindicates any
agent for any individual. **It is not medical advice and contains no recommendation.** Its value is
as a counterweight to any inference that a WOREE patient who failed conventional ASMs has an
untried ketogenic or ACTH route: here, those were tried.

The vigabatrin detail deserves separate recording because the repository holds a conflicting-evidence
status on vigabatrin in WWOX: this patient had vigabatrin listed as ineffective **and retained at
70 mg/kg/day**, and had **no hypsarrhythmia or epileptic spasms** — so this case is not comparable to
the Shaukat 2018 West-syndrome cases in which vigabatrin resolved spasms. The conflict is not
advanced by this paper; it is joined by a third, different scenario.

**10.3 — Cerebellar sparing cannot be stated as a general feature of WWOX disease in humans.** This
patient has inferior cerebellar vermis hypoplasia documented at 7 days of life and still present at
2y4m, plus dentate-nuclei signal abnormality at 2y4m, all in prose. The paper additionally asserts
that cerebellar vermis hypoplasia has "been described in most cases" of WOREE. The standing question
should be reframed: the sparing observation from the rat model concerns **histological integrity of
the cerebellar cortex** in the presence of ataxia, which is a different proposition from **midline
vermian developmental hypoplasia on MRI**. These can coexist. LEGEND should not let a
human-radiological finding and a rodent-histological finding be scored against each other as if they
measured the same thing.

**10.4 — Allele-class censuses drawn from exome data are lower bounds.** A pathogenic single-exon
WWOX deletion was invisible to exome CNV calling in an expert centre and required RT-PCR, Sanger,
Q-PCR and array-CGH to recover. Any published count of WWOX genotype classes assembled from
NGS-diagnosed patients will systematically under-count intragenic CNV alleles and over-count
apparently-monoallelic cases. This is a **methodological caution to attach to census-derived
numbers**, not a claim about any specific census.

**10.5 — What may NOT be inferred from this paper.** It generated no genotype–phenotype data, no
functional data, no protein data, no missense allele, no splice allele, and no survival endpoint.
Its title must not be re-voiced as a finding: **"A Phenotypic-Driven Approach" is the authors'
proposal and framing, never their result**, and the authors' own stated conclusion is that "Genetic
testing remains crucial in establishing the definitive diagnosis of WOREE syndrome." Any downstream
text that renders this paper as evidence that phenotype suffices for WOREE diagnosis, or that
phenotype indexes allele class, is inflating it.

---

## 11 · Declaration

**Author:** Scientist B.
**Date:** 2026-09-21.
**Mode:** READ-ONLY toward all canonical LEGEND files. **No canonical file was modified** — no
registry, no queue, no ledger, no current file, no commit candidate. No git command was run. Exactly
two files were written: the verbatim full-text artefact
`files/fulltext/PMID35573960_PMC_MCPtext.txt` and this analysis.

**Declared limits.**
1. **No figure image was inspected**, and none is inspectable in this environment. Per D-14, no
   negative asserted only by a figure has been adjudicated. All three figure *legends* survived
   extraction as text and are quoted as legend text, clearly labelled as such.
2. **Patient table:** none present in the extracted text (`Table` = 0, no TABLE block). On the
   evidence that all three figure legends survived, and that this is an N=1 report with the full
   clinical history in continuous prose, I judge that **no patient table existed in the original**.
   This is a reasoned judgement, not a verified fact, and is the weakest assertion in this document.
3. **Extraction defect: PRESENT and severe.** Every italicised token was deleted — the gene symbol
   *WWOX* throughout (surviving only twice, as roman primer names), and all inline citation and
   figure cross-references (23 empty `()`, 10 empty `(,)`). The reference list is absent.
   Consequently the provenance of the "recent review" negative quoted in §3 is not recoverable from
   this artefact. Every zero string-count used as evidence in this document is a **roman-type**
   word; italic-class zeros are recorded in §9 and are used nowhere as evidence.
4. **Licence: not confirmed.** `get_copyright_status` reported `license.type: null`,
   `is_open_access: false`, `checked_sources: ["pubmed"]`, `found_in_pmc: 0` — PMC was not consulted,
   so the flag is uninformative. Retrievability was established empirically by a single successful
   fetch returning a 19,348-byte body. Frontiers policy is CC BY; that is publisher policy, not a
   tool-verified fact for this article.
5. **Nothing in this document is medical advice.** All treatment content reports what was
   administered to one patient and what was observed. No statement is phrased as, or should be read
   as, a recommendation.
