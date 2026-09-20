# WWOX developmental timing audit — does this corpus contain evidence about the life stage WWOX-DEE actually occupies?

**Date:** 2026-09-20 · Scientist A, batch `SCIENTIST_CHANG_NS_WWOX_NEUROPROTEOSTASIS_AND_PEPTIDE_INTERVENTION`
**Status:** non-canonical analysis. No canonical file modified, no commit candidate produced,
no therapeutic proposal made.
**Sources:** all retrieved from **PubMed / PMC open access** via the PubMed MCP server. Per-article
DOIs are given inline at first citation.

---

## 0 · Why this audit exists

WOREE / WWOX-DEE is neonatal-onset. Seizures start in the first weeks of life; the encephalopathy
is *developmental*. Everything wave 1 and wave 2 of this batch read from the Chang/NCKU corpus is
about a different life stage: cancer xenografts, 10–12-month 3xTg-AD mice, 10–11-month aged
heterozygotes, post-mortem AD hippocampi at mean age 80, and a cascade the lab itself times to
"middle age" and "20 to 30 years". This audit asks whether the corpus says anything at all about
the developing nervous system, and if so what it constrains.

---

## 1 · Read-depth declaration — honest, per paper

| PMID | Paper | Depth | Note |
|---|---|---|---|
| **15026124** | Chen S-T, Chuang J-I, Wang J-P, Tsai M-S, Li H, **Chang N-S**. *Neuroscience* 2004;124(4):831-9. "Expression of WW domain-containing oxidoreductase WOX1 in the developing murine nervous system." | **ACQUISITION-BLOCKED — abstract + PubMed metadata only** | `convert_article_ids` returns **no PMCID** for this PMID (record: `{"pmid":"15026124","requested-id":"15026124"}` — no `pmcid`, no `doi` field beyond the metadata record). It is a 2004 Elsevier *Neuroscience* paper with no PMC deposit. It is **unobtainable on this surface.** I did not attempt publisher retrieval; `sciencedirect.com` is EGRESS_BLOCKED per the batch's verified acquisition constraints. DOI [10.1016/j.neuroscience.2003.12.036](https://doi.org/10.1016/j.neuroscience.2003.12.036) |
| **22193544** | Wang H-Y, …, **Chang N-S**, Yang C-N, Lu P-J. *Cell Death Differ* 2012;19(6):1049-59. | **FULL TEXT** (PMC3354054) | Read end to end incl. all Results and Discussion. DOI [10.1038/cdd.2011.188](https://doi.org/10.1038/cdd.2011.188) |
| **30158849** | Liu C-C, …, Sze C-I, **Chang N-S**. *Front Neurosci* 2018;12:563. "WWOX Phosphorylation, Signaling, and Role in Neurodegeneration." | **FULL TEXT** (PMC6104168) | Chang-lab review. DOI [10.3389/fnins.2018.00563](https://doi.org/10.3389/fnins.2018.00563) |
| **34359949** | Hsu C-Y, …, Hsu L-J, **Chang N-S**. *Cells* 2021;10(7):1781. "WWOX and Its Binding Proteins in Neurodegeneration." | **FULL TEXT** (PMC8304785) | Chang-lab review. DOI [10.3390/cells10071781](https://doi.org/10.3390/cells10071781) |
| **34747138** | Repudi S, Kustanovich I, Abu-Swai S, Stern S, **Aqeilan RI**. *EMBO Mol Med* 2021;13(12):e14599. "Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes." | **FULL TEXT** (PMC8649866) | Not Chang lab — directly adjacent, and the only paper in reach that bears on a treatment window. DOI [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| **32581702** | Iacomino M, …, Tochigi Y, …, Suzuki H, Salpietro V. *Front Neurosci* 2020;14:644. "Loss of Wwox Perturbs Neuronal Migration and Impairs Early Cortical Development." | **FULL TEXT** (PMC7300205) | Not Chang lab. Human 21-GW fetal neuropathology + `lde` rat. DOI [10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644) |
| **31340538** | Tochigi Y, …, Suzuki H. *Int J Mol Sci* 2019;20(14):3596. "Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination in a Rat Model of Lethal Dwarfism with Epilepsy." | **FULL TEXT** (PMC6678113) | Not Chang lab. The only paper with a measured postnatal WWOX **protein** time course. DOI [10.3390/ijms20143596](https://doi.org/10.3390/ijms20143596) |
| 31543760 · 34268881 · 34634460 · 38161429 · 42190144 | Kośla/Bednarek hNPC differentiation; Aqeilan organoid review; Breton/Carlen in-vitro KO oscillations; Battaglia WOREE neuroimaging mini-review; Riccardi burst-suppression DEE cohort | **METADATA / ABSTRACT ONLY** | Identified by search, triaged, not read. No finding below rests on them. |

### What I could not obtain, and therefore do not claim

- **No figure panel, blot, micrograph or quantification image was inspected in any paper.** The PMC
  extraction strips figure images, figure callouts and reference markers. Where a claim depends on
  a panel I say so. I make no statement about band intensity, staining pattern or layer morphology
  beyond what the authors state in running text or legend text.
- **PMID 15026124 — the one true developmental paper in the Chang corpus — was never read.** Every
  statement attributed to it below is a *secondary restatement by a later paper*, or its own
  abstract. That is a first-order limit on this entire audit and is carried through §2 and §6.
- Supplementary material was empty or absent in every deposit retrieved. No claim rests on it.

---

## 2 · Question 1 — When is WWOX expressed in the developing nervous system?

### 2.1 What the primary source's own abstract says (and only the abstract)

From the PubMed abstract of **PMID 15026124** (Chen/Chang 2004), verbatim:

> "Immunohistochemical analysis revealed that WOX1 was differentially expressed in early dividing
> cells from all three germ layers from embryonic to perinatal stages. In murine fetuses, WOX1 was
> present prevalently in the brainstem, spinal cord and peripheral nerve bundles, but its expression
> decreased after birth."
> — PMID 15026124, abstract

> "Notably, high levels of WOX1 immunoreactivity was observed in the neural crest-derived structures
> such as cranial and spinal ganglia and cranial mesenchyme during the late fetal stage. In the
> adult brain, WOX1 is abundant in the epithelial cells of the choroids plexus and ependymal cells,
> while a low to moderate level of WOX1 is observed within white matter tracts, such as axonal
> profiles of the corpus callosum, striatum, optic tract, and cerebral peduncle."
> — PMID 15026124, abstract

**No E-day or P-day is stated anywhere in the abstract or the PubMed record.** The staging
vocabulary is entirely qualitative: "embryonic", "perinatal", "late fetal stage", "after birth",
"adult". The task asked me to quote the actual stages rather than a summary. **I cannot, because the
paper that contains them is unobtainable on this surface.** Any E-day figure quoted from this paper
in this batch would be fabricated.

### 2.2 Four secondary restatements of PMID 15026124 — and they do not agree

This is the substantive finding of §2. Four separate papers restate the same inaccessible primary,
and each emphasises something different:

| Restating paper | Verbatim restatement | What it implies about early embryonic expression |
|---|---|---|
| **22193544** (Chang co-author) | "WWOX expression in the developing brain is **low during the early embryonic stage** when organogenesis is most rapid; however, moderate-to-high WWOX immunoreactivity is detected in the brain and spinal cord during the middle and late fetal stages." | LOW early, rising to mid/late fetal |
| **30158849** (Chang senior) | "In the developing mouse brain, WWOX protein expression is **essentially present in every brain region** and the expression level is reduced in the newborns." | Ubiquitous, then falls at birth |
| **34747138** (Aqeilan, citing Chen) | "WWOX is **ubiquitously expressed in all brain regions** (Chen, …)." | Ubiquitous; no developmental regulation mentioned at all |
| **31340538** (Suzuki, citing Chen) | "Wwox protein is **highly expressed in the developing nervous system of mouse embryos**, with the level of expression and localization of this protein in mouse CNS **drastically changing from late embryonic- to postnatal-stage**." | High in embryos; direction of change unspecified |

"Low during the early embryonic stage" (22193544) and "highly expressed in the developing nervous
system of mouse embryos" (31340538) are not the same claim. Neither is "reduced in the newborns"
(30158849) the same as "ubiquitously expressed in all brain regions" with no time term (34747138).
**The corpus's own account of when WWOX turns on in the developing brain is unstable across
restatements, and the primary that would settle it cannot be opened here.** I flag this as an
unresolved provenance defect, not as a contradiction I have proven.

### 2.3 The one measured expression time course anyone in reach actually ran

**PMID 31340538** (Tochigi/Suzuki 2019, rat, PND 5 / 10 / 15 / 21, Western blot + IHC) is the only
paper obtained here that measures WWOX protein across defined postnatal days. From **Results**:

> "Additionally, we found that the expression of Wwox protein increased with age in whole brains and
> cerebral cortices of +/+ rats (D,E). These findings suggest that Wwox protein might have important
> roles in normal brain development during early postnatal period."
> — PMID 31340538, Results §2.1

and from the **Discussion**:

> "Our data clearly showed age-related increases in Wwox expression in the normal rat brain during
> early postnatal development, indicating that Wwox may play an important role for establishing
> normal brain networks."
> — PMID 31340538, Discussion

Regions and cell types, same paper, **Results**:

> "Immunohistochemical analysis showed that Wwox protein was widely expressed in the forebrain,
> especially in layers II-III and V of the cerebral cortex, as well as the white matter, corpus
> callosum (CC), hilus in the hippocampus, habenular nuclei (HN), thalamus, hypothalamus, and
> internal capsule (IC)."
> — PMID 31340538, Results §2.1

> "Because neurons, oligodendrocytes, and astrocytes all derive from neural stem cells, these
> findings suggest that Wwox may be expressed in all neural stem cell-lineages."
> — PMID 31340538, Results §2.3

Microglia are the exception — the same section reports Iba1-positive microglia were **not**
immunostained for Wwox, and the Discussion attributes the microglial reduction in mutants to a
secondary effect.

Note this paper also **corrects** an earlier cell-type claim: "Although previous immunohistochemistry
found that Wwox protein was present in neurons and astrocytes but not in oligodendrocytes, our
double immunofluorescence using specific markers clearly showed that Wwox protein was present in
oligodendrocytes… To our knowledge, this study is the first to show that Wwox is expressed in
oligodendrocytes" (PMID 31340538, Discussion).

### 2.4 Human data — mRNA, prenatal to teenage

The Chang lab itself pulled the Human Brain Transcriptome and reported, in **PMID 34359949** §8.1:

> "In the IκBα/WWOX/ERK survival signaling, **no reduction of gene expression for IκBα, WWOX, and
> ERK is shown from prenatal to the teenage period.** … No downregulation of TRAPPC6A, SH3GLB2 and
> tau is shown up to the teenage period."
> — PMID 34359949, §8.1

And in **PMID 30158849**:

> "However, WWOX protein expression levels are significantly increased in the human fetal brains
> (GeneCard database shown above). This is in agreement with our observations using mouse fetal
> brains."
> — PMID 30158849, "Gene Expression in the Brain"

The same review is explicit that mRNA and protein dissociate for this gene — "There is no positive
correlation between WWOX mRNA expression and protein expression" (PMID 30158849) — so the flat human
mRNA trajectory does **not** license a claim that human WWOX protein is flat prenatal→teenage.

---

## 3 · Question 2 — Is expression developmentally regulated, or constitutive?

**Developmentally regulated — but the corpus gives two opposite directions, in different regions and
different species, and never reconciles them.**

| Claim | Direction | Source | Region / species | Measured or restated? |
|---|---|---|---|---|
| "its expression decreased after birth… significantly reduced in the brain stem and spinal cord of adult mice" | **DOWN** after birth | PMID 15026124 abstract | mouse **brainstem, spinal cord** | primary, but **abstract only — Results unread** |
| "expression of Wwox protein **increased with age** in whole brains and cerebral cortices" PND5→21 | **UP** postnatally | PMID 31340538 Results | rat **whole brain, cerebral cortex** | **measured**, Western blot + IHC, 4 timepoints |
| "low during the early embryonic stage… moderate-to-high… during the middle and late fetal stages" | **UP** across gestation | PMID 22193544 Discussion | mouse brain, spinal cord | restatement of 15026124 |
| "no reduction … from prenatal to the teenage period" | **FLAT** | PMID 34359949 §8.1 | human, mRNA, HBT | database readout |

These are not necessarily in conflict — mouse brainstem/spinal cord falling while rat forebrain/cortex
rises is biologically coherent, and caudal CNS matures earlier than cortex. **But the corpus's
summary sentences flatten the regional split.** "The expression level is reduced in the newborns"
(PMID 30158849) is stated of "the developing mouse brain" without restriction to brainstem and cord,
and it is the sentence a reader carries away.

**Is there a peak?** No paper in reach reports a peak with a stage attached. PMID 31340538 stops at
PND 21 — the age at which `lde` rats are dying — so its "increases with age" curve is truncated and
cannot be read as reaching or passing a maximum. **A treatment-window argument built on a WWOX
expression peak has no anchor in anything obtainable here.**

---

## 4 · Question 3 — Does the aggregation cascade connect to development at all?

**No — but it is not ageing-*only* either. It is ageing-framed with one explicit postnatal
exception, and that exception is asserted, not demonstrated on any surface I could inspect.**

### 4.1 The ageing framing, in the lab's own words

> "Aggregate formation of tau and Aβ levels in the brains are very low in middle-aged healthy humans
> of 40 to 70 years old."
> — PMID 34359949, §1 (section heading: "Brain Protein Aggregation Starts from Middle Age")

> "We reported that when WWOX protein is downregulated in the hippocampi of middle-aged individuals,
> brain protein aggregation may start to occur. **The aggregation process is slow and may take 20 to
> 30 years.** Ultimately, extracellular amyloid β plaques and intracellular tau tangles are built up
> in the brain of AD patients approximately at 70-years old or older."
> — PMID 34359949, §7.2

> "If our observations hold true, TPC6AΔ/TIAF1 starts polymerization in the middle age, and takes at
> least 10–40 years to generate significant amounts of tau and amyloid β protein aggregates for
> clinically defined AD symptoms."
> — PMID 30158849, "TRAPPC6AΔ Protein Aggregation Is Upstream of TIAF1"

### 4.2 The postnatal exception — and it is a large one

> "**In Wwox knockout mouse, it only takes less than 15 days after birth to let the brain proteins
> polymerize and aggregate in a cascade-like manner.** The sequential protein aggregation starts
> from TPC6AΔ, then TIAF1 and SH3GLB2, and ultimately amyloid-beta (Aβ) and tau."
> — PMID 34359949, §7.2

> "Further, evidence revealed that when Wwox gene is knocked out in mice, aggregation of TIAF1,
> TPC6AΔ, amyloid β, Tau, and many other proteins occurs in the brains **in less than 3 weeks**."
> — PMID 30158849, "WWOX Controls TRAPPC6AΔ, TIAF1, and Tau Aggregation"

> "Presence of pS35-TPC6AΔ and pT181-Tau aggregates is shown in the cortex and hippocampus of
> **3-week-old Wwox knockout mice**."
> — PMID 30158849, Figure 4 legend (panel D)

> "Wwox gene knockout mice rapidly exhibit aggregation of many proteins in the brains **just in 15
> days after birth.** These proteins include TPC6AD, TIAF1, and SH3GLB2, tau and Aβ. Notably, human
> newborns with WWOX deficiency rapidly develop severe neural diseases, metabolic disorders,
> retarded growth and early death."
> — PMID 30158849, Perspectives, §"A Focus on WWOX and Protein Aggregation in Middle Age"

### 4.3 What that exception does and does not establish

**Does establish (as an authorial claim):** the same cascade the lab times at 20–40 years in sporadic
human ageing is claimed to run to completion — through Aβ and tau — in a genetically WWOX-null mouse
brain within 15 days to 3 weeks of birth. If true, that is a ~500-fold compression of the timeline
and it lands squarely inside the life stage WWOX-DEE occupies.

**Does not establish, and must be stated plainly:**

1. **This is postnatal, not developmental.** P15 and P21 mouse are juvenile, not embryonic. **No
   paper in this corpus, Chang or otherwise, reports any node of the aggregation cascade at any
   embryonic timepoint.** TRAPPC6AΔ, TIAF1, SH3GLB2 aggregation in an E-stage brain: not measured,
   not claimed, not available.
2. **The window is bounded by lethality, not by biology.** `Wwox`-null mice "died within less than 4
   weeks" (PMID 34747138, Results). "Since KO mice died within less than 4 weeks, we could not
   perform recordings in adult KO mice" (PMID 34747138, Results). "<15 days" and "<3 weeks" are
   therefore *the entire observable lifespan of the animal*, not a demonstrated rate. The statement
   "it only takes less than 15 days" is a ceiling imposed by the model, not a measured latency.
3. **It rests on the reagent this batch already found underdetermined.** The P21 result is
   `pS35-TPC6AΔ` immunostaining — the same isoform-specific antibody whose epitope this batch's
   TRAPPC6AΔ node audit found to be largely shared with wild-type TPC6A and never validated against
   a genetic null. The neonatal claim inherits that defect in full. I did not see the panel.
4. **Both statements are review-level self-citation.** Both PMID 30158849 and PMID 34359949 are
   reviews; the citation markers are stripped by the PMC extraction, so I cannot identify which
   primary paper reports the P15 mouse data, and I could not verify it at source.

**Verdict on Q3:** the cascade is not *exclusively* ageing in this corpus — but its only non-ageing
foothold is a juvenile-postnatal assertion in two reviews, bounded by lethality, resting on a
contested antibody, with **no embryonic data at any node**. It does not transfer to a
prenatal-onset encephalopathy on this evidence.

---

## 5 · Question 4 — Is there a stated or implied critical window?

**There is a demonstrated *sufficient* intervention point (P0, mouse). There is no demonstrated
closing point. And there is direct evidence that damage begins before P0.**

### 5.1 The intervention that worked, and exactly when it was given

**PMID 34747138** (Aqeilan lab), Results:

> "Viral particles (2 × 10^n/hemisphere) of AAV9-hSynI-mWwox, AAV9-hSynI-hWWOX, or AAV9-hSynI-EGFP
> were injected into the ICV region of Wwox-null mice **at birth (P0)**, to achieve widespread
> transduction of neurons throughout the brain."
> — PMID 34747138, Results

> "A single intracerebroventricular (ICV) injection of AAV9-Synapsin I-WWOX rescued the growth
> retardation, hypoglycemia, epileptic seizures, ataxia, and premature death of Wwox-null mice. In
> addition, WWOX restoration improved myelination and reversed the abnormal behavioral changes of
> Wwox-null mice."
> — PMID 34747138, Introduction (result summary; the individual claims are each supported in Results)

### 5.2 The author's own statement that the window was never probed

> "**The limited life span and poor conditions of Wwox-null mice prompted us to treat these mice very
> early on in their life (P0). Nevertheless, attempts to treat post-natal Wwox-null mice by different
> route of AAV administration should and will be explored in the future.**"
> — PMID 34747138, Discussion

This is decisive and must not be softened. **No later-than-P0 treatment arm exists.** The study
establishes that P0 is early enough. It says nothing whatever about whether P7, P14 or the
equivalent human age would also be early enough — and the authors say so themselves.

### 5.3 The construct restores WWOX only in mature neurons — an informative negative

> "Successful delivery of AAV9-hSynI-mWwox-IRES-EGFP (AAV-mWwox) or AAV9-hSynI-hWWOX (AAV-hWWOX)
> should lead to expression of intact WWOX protein in **Synapsin-I-positive non-dividing/matured
> neurons**."
> — PMID 34747138, Results

> "Importantly, WWOX expression was lacking in non-neuronal cells of the brain such as
> oligodendrocytes of KO mice injected with either AAV-mWwox or AAV-hWWOX."
> — PMID 34747138, Results

> "As presented in Appendix Fig, **no WWOX expression was detected in Wwox-null tissues in P17 and
> 9-month-old rescued mice**" (liver, pancreas, kidney, testis, ovary).
> — PMID 34747138, Results

So a rescue that reaches **only post-mitotic neurons, only in brain, only from P0** was sufficient
for survival, seizure control, myelination and behaviour. WWOX was **not** restored in dividing
progenitors, in radial glia, in oligodendrocytes, or anywhere peripherally. That argues the
requirement served by this rescue is substantially *postnatal and neuronal* — which is the single
most encouraging structural fact in this audit.

### 5.4 But damage demonstrably begins before birth

**PMID 32581702** — human fetal neuropathology at 21 gestational weeks, homozygous `WWOX`
c.790C>T p.Arg264Ter. From **Results**:

> "In the histological HE staining of Wwox-deficient developing human brain we observed anomalous
> migration of the external granular layer within the molecular layer and also the latter appeared
> as not homogeneous."
> — PMID 32581702, Results

> "Disorganization of irregularly distributed glial trajectories was also observed with GFAP staining."
> — PMID 32581702, Results

Rat birth-dating in the same paper — BrdU at **E16.5**, read out at **P1**:

> "Since these results clearly indicated that migration of late-born neuron was impaired in lde
> cortical plate, BrdU was injected fetus at **E16.5** when the late-born neuron actively
> proliferate. When BrdU-incorporated cells were traced to **P1**, we found altered distribution of
> BrdU-positive cells in lde cerebral walls, revealing delayed migration of late-born neurons.
> **These results indicate that Wwox deficiency impairs prenatal neuronal migration which is required
> for normal cortical layer formation at birth in rats.**"
> — PMID 32581702, Results

> "the density of Satb2-positive cells was significantly decreased in the surface layer of lde
> cortical plate (area number 1 corresponding to cortical layer II). This defect was accompanied by
> increase in Satb2-positive cells of the bottom layer in lde cerebral wall (area number 7
> corresponding to intermediate zone (IZ))."
> — PMID 32581702, Results

So: by P0 — the moment the successful gene therapy was administered — a `Wwox`-null cortex already
carries a mislaminated cortical plate built from neurons that migrated abnormally between E16.5 and
P1, and a human `WWOX`-null cortex already shows disordered granular/molecular layering at 21 GW.

### 5.5 A within-group refinement worth recording

The `lde` rat group's own earlier paper concluded the opposite about migration:

> "the normal density and distribution of NeuN-positive neurons and the normal level of expression
> of NeuN in the cerebral cortices of lde rats during early postnatal period indicated that **Wwox is
> not required for proliferation and migration of immature neurons**."
> — PMID 31340538 (2019), Discussion

One year later, with layer-specific markers (Satb2/Tbr1) and E16.5 BrdU birth-dating instead of bulk
NeuN counts, the same investigators (Tochigi, Suzuki are authors on both) reported impaired prenatal
migration (PMID 32581702, quoted above). **Total neuron number is normal; their laminar placement is
not.** A NeuN count was the wrong instrument. This is the fourth abstract/summary-versus-results
divergence this batch has logged, and it argues again for reading Results.

---

## 6 · Developmental stage vs WWOX expression — can a table be built?

**Partly, and only with the species, region and evidence-grade columns attached.** A clean
stage-by-stage table cannot be built, because the only paper that staged mouse CNS expression
systematically is unobtainable and no obtainable paper reports an E-day for WWOX expression itself.

| Stage | Species / region | What is claimed | Source | Grade |
|---|---|---|---|---|
| Early embryonic ("organogenesis most rapid") | mouse, brain | **LOW** | PMID 22193544 Discussion | restatement of unread 15026124 — **contradicted** by PMID 31340538's restatement of the same primary |
| Embryonic → perinatal, all three germ layers | mouse, early dividing cells | "differentially expressed" | PMID 15026124 abstract | abstract only |
| Mid/late fetal | mouse, brain + spinal cord | **MODERATE–HIGH** | PMID 22193544 Discussion | restatement |
| Late fetal | mouse, cranial + spinal ganglia, cranial mesenchyme (neural-crest-derived) | **HIGH** | PMID 15026124 abstract; restated PMID 34359949 §7.1 | abstract only |
| Fetal (unstaged) | mouse fetal brain; human fetal brain | **INCREASED** vs other | PMID 30158849 ("significantly increased in the human fetal brains"; "in agreement with our observations using mouse fetal brains") | narrative + GeneCard database |
| Fetal → newborn | mouse **brainstem, spinal cord** | **DECREASES after birth** | PMID 15026124 abstract | abstract only |
| Prenatal → teenage | **human**, mRNA, HBT | **NO REDUCTION** | PMID 34359949 §8.1 | database; mRNA, and the same corpus says mRNA ≠ protein for WWOX |
| **PND 5 → 21** | **rat**, whole brain + cerebral cortex | **INCREASES with age** | PMID 31340538 Results §2.1 | **measured — Western blot + IHC, 4 timepoints. Strongest datum in the table.** |
| PND 21 | rat forebrain | cortical layers II-III and V, white matter, CC, hippocampal hilus, habenular nuclei, thalamus, hypothalamus, internal capsule; in neurons, astrocytes, oligodendrocytes; **not** microglia | PMID 31340538 Results §2.1, §2.3 | measured |
| Adult | mouse brain | choroid plexus epithelium, ependyma high; white-matter tracts low-to-moderate | PMID 15026124 abstract; restated PMID 30158849 | abstract only |

**No cell in this table carries an E-day.** That is the honest state of the evidence reachable here.

---

## 7 · Verdict

### `MIXED — stated with the split`

**The split, precisely:**

**(a) The wider WWOX field has real, primary, developmental evidence — and almost none of it is
Chang/NCKU.** Human `WWOX`-null fetal cortex at 21 GW with disordered granular/molecular layering
(PMID 32581702); `lde` rat prenatal migration failure birth-dated at E16.5 and read at P1 (PMID
32581702); a measured postnatal WWOX protein rise across PND 5–21 in rat cortex (PMID 31340538);
neonatal P0 neuronal gene therapy that rescues survival, seizures and myelination (PMID 34747138).
None of these four papers is from the Chang laboratory.

**(b) The Chang/NCKU corpus proper contributes one unobtainable expression paper, one in-vitro
differentiation paper, and narrative.** PMID 15026124 is the only developmental primary and it has
no PMC deposit. PMID 22193544 is a genuine differentiation result — but in RA-treated SH-SY5Y
neuroblastoma cells, not an embryo, and its own Discussion is careful: "we present a novel mechanism
for the regulation of neuronal differentiation by WWOX" (PMID 22193544, Discussion), with the
developmental inference imported wholesale from the unread Chen 2004. The lab's developmental
statements in its reviews are restatements of that one inaccessible paper, and **they do not agree
with one another** (§2.2).

**(c) The proteostasis cascade — the part of this corpus a therapy would be built on — is
ageing-framed, with a single juvenile-postnatal assertion and zero embryonic data.** "20 to 30
years", "middle age", "70-years old or older" for the human timeline; "less than 15 days after
birth" in the `Wwox`-null mouse, bounded by that animal's <4-week lifespan and resting on the
`pS35-TPC6AΔ` antibody this batch already found underdetermined.

---

## 8 · What this means for a treatment window in a neonatal-onset disease

Be conservative. The strongest developmental facts in reach point in two directions at once. On the
encouraging side, a single P0 intracerebroventricular AAV9 restoring WWOX **only in post-mitotic
Synapsin-I neurons** — not in progenitors, not in glia, not peripherally — was enough to rescue
survival, seizures, myelination, glucose and behaviour in `Wwox`-null mice; that is the most
informative result in this audit, and it suggests a substantial part of the requirement is served by
mature neurons after birth. On the restraining side, by the moment that injection was given, the
cortex was already built wrong: `lde` rat neurons born at E16.5 were still mislaminated at P1, and a
human `WWOX`-null fetus already showed disordered cortical layering at 21 gestational weeks. Those
prenatal migration events were not corrected by the P0 rescue and were not assessed in the rescued
animals. Three things therefore cannot be said on this evidence: that a window *closes* anywhere
(the Aqeilan study ran no post-P0 arm and says so explicitly); that mouse P0 maps to any human age
(no cross-species staging, no human dosing data, and human cortical migration is largely complete by
mid-gestation while mouse cortex is still maturing at birth); and that the proteostasis cascade is a
developmental target at all (no node of it has ever been measured at an embryonic timepoint, and its
one neonatal readout is an assertion in two reviews resting on a contested antibody). Mouse
developmental expression is not a human treatment window. The honest position is that a postnatal
neuronal intervention is *not excluded* by the developmental biology, that some developmental damage
is already done at birth, and that the size of the irreducible prenatal component is unmeasured.

---

## 9 · What I could not obtain

| Not obtained | Consequence |
|---|---|
| **PMID 15026124 full text** — no PMCID exists; Elsevier *Neuroscience* 2004; publisher egress blocked | The only developmental primary in the Chang corpus was never read. All E-day / P-day staging, all regional time courses, all immunohistochemistry, and the p53-wild-type-vs-knockout comparison are **unverified**. Four secondary restatements of it disagree (§2.2) and I cannot adjudicate them. |
| Any figure panel, blot or micrograph in any paper | No claim here rests on inspecting an image. The P21 `pS35-TPC6AΔ` result, the rat Wwox-vs-age Westerns, the Satb2/BrdU distributions and the AAV rescue quantifications are all taken from authors' running text or legend text only. |
| Reference markers / citation targets (stripped by PMC extraction) | For the two Chang reviews I cannot identify which primary paper reports the "<15 days after birth" mouse cascade data. It is cited but untraceable from this surface. |
| Supplementary material in every deposit | Empty or absent throughout. Nothing above depends on it. |
| PMIDs 31543760, 34268881, 34634460, 38161429, 42190144 | Triaged from metadata only, not read. Kośla/Bednarek 2019 (hNPC differentiation transcriptome, PMC6730490) is the highest-value unread item — its dataset is the one reanalysed in PMID 32581702 §"Transcriptomic Analyses" and a direct read would test that reanalysis. Recommended for a follow-on wave. |
