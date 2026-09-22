# Has any cerebellum-resolved FUNCTIONAL measurement ever been made in a Wwox/WWOX model?

**Actor:** Scientist M · **Date:** 2026-09-22 · **Axis:** FUNCTION, not anatomy and not transduction
**Question class:** instrument census — *what can each published readout structurally see, before what its number says*

> **Not medical advice.** Nothing here is a treatment, dose, route or clinical-management recommendation.
> Therapeutic output supports discussion with a treating clinical team; it never substitutes for one.

**Sources retrieved today, first-hand, according to PubMed.** `PMID 32000863` / `PMC6990504`
([DOI](https://doi.org/10.1186/s40478-020-0883-3)) · `PMID 34634460` / `PMC8609180`
([DOI](https://doi.org/10.1016/j.nbd.2021.105529)) · `PMID 36828035` / `PMC10835625`
([DOI](https://doi.org/10.1016/j.pneurobio.2023.102425)) · `PMID 36779245` / `PMC10952634`
([DOI](https://doi.org/10.1111/epi.17542)). Metadata/abstract depth: `PMID 17823927`
([DOI](https://doi.org/10.1002/gcc.20497)) · `PMID 19500159` ([DOI](https://doi.org/10.1111/j.1601-183X.2009.00502.x))
· `PMID 31340538` ([DOI](https://doi.org/10.3390/ijms20143596)) · `PMID 33914858`
([DOI](https://doi.org/10.1093/brain/awab174)) · `PMID 38407561` ([DOI](https://doi.org/10.1002/ajmg.a.63575)).
Inherited (sibling- or repo-attested, tagged as such throughout): `PMID 34747138`
([DOI](https://doi.org/10.15252/emmm.202114599)) · `PMID 42422765` ([DOI](https://doi.org/10.1016/j.omta.2026.201791))
· `PMID 38161429` ([DOI](https://doi.org/10.3389/fped.2023.1301166)) · `PMID 17470496`
([DOI](https://doi.org/10.1093/brain/awm078)).

> **Scope, and what is deliberately NOT here.** The Purkinje-resolved **transduction stain** is Scientist J's
> node ([`purkinje_existing_material_experiment_20260922.md`](purkinje_existing_material_experiment_20260922.md))
> and is not re-derived. The seven-layer `VECTOR GENOME → … → FUNCTION` decomposition is Scientist C's
> ([`cerebellum_layer_localisation_20260922.md`](cerebellum_layer_localisation_20260922.md)); this file
> occupies its **layer 7 only**, which that file itself marks `CANNOT BE EVALUATED`. The dose
> non-monotonicity premise is CLOSED and is not reopened. `CLAIM 039`'s standing narrowing is not modified.

---

## 0 · The answer, stated before the evidence

> 🔴 **There is no cerebellum-resolved functional measurement in the Wwox/WWOX literature. Not one, in any
> species, in any allele, at any age.** Every functional readout that exists is one of four things: a
> whole-animal motor composite (rotarod, clasping, footprint, open field), a **forebrain** electrophysiological
> recording, a **corticospinal or peripheral** conduction measure, or a narrative clinical descriptor. The only
> cerebellum-resolved measurements that exist at all are **anatomical** (Purkinje counts, layer thickness,
> foliation) or **molecular** (regional western, vDNA, mRNA, RNA-seq).

And the sharpest single fact this census returned is not an absence but a **protocol step**, read first-hand
from Methods:

> 🎯 **The only slice-electrophysiology study in the entire Wwox literature discards the cerebellum at the
> dissection step.** `PMID 34634460`, Methods § 5.2, verbatim: *"Once the mice were deeply anesthetized, they
> were swiftly decapitated, and the brain was removed. **The cerebellum and olfactory bulbs were removed**, and
> the remainder of the tissue was placed caudal-side down onto a platform…"*

That is `NOT TESTED` **by protocol**, which is a stronger and more useful statement than `NOT REPORTED`. It also
means the tissue that would answer the question is currently being generated and thrown away by a running,
funded protocol — which is what § 4 is built on.

---

## 1 · THE CENSUS

**Allele discipline.** `Wwox`-null (Aqeilan line) ≠ `Wwox`-null (NCKU WD1/WD234 lines) ≠ `Wwox^gt/gt` ≠
`Wwox^P47T/P47T` ≠ Synapsin-Cre neuronal conditional (S-KO) ≠ rat `lde/lde` ≠ human WOREE ≠ human SCAR12.
**Nothing is pooled across rows and nothing transfers between them.**

**Statistical class key.** `MEASURED` = a number exists, no comparison · `FORMALLY COMPARED` = a stated test and
threshold · `DESCRIPTIVELY DIFFERENT` = asserted difference, no test reported on the surface read ·
`NOT TESTED` = the arm does not exist · `NOT RECONSTRUCTABLE` = the surface cannot yield it.

### 1.1 Rodent

| # | Model · allele | Age | Instrument | What was ACTUALLY measured | Purkinje resolved? | Cerebellum-**localising**? | Result · class |
|---|---|---|---|---|---|---|---|
| R1 | Mouse `Wwox^−/−`, **NCKU WD1 (exon 1) and WD234 (exon 2/3/4)**, two independent strains | **P18–20** | **Rotarod**, constant speed *and* accelerating (4→40 rpm/5 min), 3-day training, means used | Latency to fall | 🔴 **NO** | 🔴 **NO** — motor composite | KO latency *"much shorter"* than `+/+` and `+/−`; `+/−` vs `+/+` **ns**. **FORMALLY COMPARED** (one-way ANOVA, α = 0.05) |
| R2 | same | **P18–20** | **Ink-paw footprint gait kinematics**, ≥5 steps/animal | **stride length**, **hind-base width**, **hind/fore-base ratio** | 🔴 **NO** | 🔴 **NO** | All three *"significantly decreased"* in KO; `+/−` **ns**; body-size-normalised version *"data not shown"*. **FORMALLY COMPARED**. 🎯 **The only quantitative gait-kinematic dataset in the whole corpus** |
| R3 | same | P18–20 | Hindlimb clasping (tail suspension) | Presence/absence of clasp | 🔴 NO | 🔴 NO | KO abnormal, `+/+` and `+/−` normal. **DESCRIPTIVELY DIFFERENT** |
| R4 | same | **3 weeks** | **Tc-MEP** — scalp stimulation, needle electrodes in **bilateral forelimb intrinsic plantar muscles** | Peak-to-peak amplitude; onset latency | 🔴 NO | 🔴 **NO — corticospinal by the authors' own statement**: *"monitor the descending response that is propagated through the corticospinal tracts"* | `+/+` 59.2 ± 9.0 µV (n = 10) vs KO 11.8 ± 5.4 µV (n = 4), *p* < 0.05; latency 1.39 ± 0.13 vs 2.44 ± 0.37 ms, *p* < 0.01. `+/−` amplitude 59.6 ± 17.2 µV (n = 5) **ns**, latency 2.13 ± 0.22 ms *p* < 0.05. **FORMALLY COMPARED** |
| R5 | same | P19–20 | Cresyl violet / H&E / calbindin IF — **anatomy, listed only to bound it** | Vermian lobule VI–VII fusion, smaller lobule V; *"partial loss of the Purkinje cells and their diminished expression of calbindin"*; TUNEL⁺ granular layer | ✅ yes (anatomy) | ✅ yes (anatomy) | No counts in the running text. Repo-attested figure read ≈18 vs ≈7 per area. **DESCRIPTIVELY DIFFERENT** in text |
| R6 | **Mouse Synapsin-Cre × `Wwox^fl/fl` (S-KO)**, plus S-HT, S-WT littermates | **P13–17** | **Acute slice LFP + whole-cell** (the corpus's only slice electrophysiology) | Neocortex layer II/III and V; hippocampus CA1/CA3 | 🔴 **NO** | 🔴 **NO — and the exclusion is mechanical**: *"The cerebellum and olfactory bulbs were removed"* | Cerebellum: **NOT TESTED, BY PROTOCOL.** Neocortex: bursting 0/11 S-WT slices, 4/23 S-HT, 36/42 S-KO; δ–γ and θ–HFO coupling; L2/3→L5 at ≈11 mm/s; abolished by d-APV; CBX −87 % frequency; mEPSC amplitude ↑, sIPSC amplitude and frequency ↓; RMP depolarised, sag ↑, post-inhibitory rebound ↑. Hippocampus: CA1→CA3 population spike ↑, CA3→CA1 **ns** |
| R7 | **Mouse `Wwox^−/−` (Aqeilan line) + AAV9-hSynI-WWOX**, `PMID 34747138` | adult | **Cell-attached recording** | *"1.6–2 mm posterior to the bregma and 4 mm lateral to the midline"*, depth 300 µm; legend *"spontaneous **neocortical** activity"* | 🔴 NO | 🔴 **NO — neocortex by stated coordinates** | **No cerebellar physiology in the paper.** Repo-attested from this session's recursive re-read |
| R8 | same | adult | Rotarod · open field · EPM | Motor coordination, anxiety | 🔴 NO | 🔴 NO | 🔴 **rescued-vs-WT ONLY**: *"we could not assess behavior of Wwox-null mice due to their poor conditions and premature death"*. vs untreated null: **NOT TESTED**. vs WT: `DESCRIPTIVELY EQUIVALENT`, no pre-specified equivalence margin |
| R9 | same | P17/P19 | Hindlimb clasping, **Appendix Fig S3** | — | — | 🔴 NO | 🔴 **UNREAD** — Appendix not retrievable; queued as `FT-152`. May or may not carry a KO arm |
| R10 | **Mouse `Wwox^−/−` + AAV9-hSynI-hWWOX, TX-007**, `PMID 42422765` | **P18** | **Hindlimb clasping**, reported by the authors as *"ataxia scores"* | Clasping severity, LD and HD arms | 🔴 NO | 🔴 **NO — the label is cerebellar, the assay is not.** Clasping is routinely positive in corticospinal, basal-ganglia and diffuse neurodegenerative models | LD partial, HD *"near-complete rescue"*. **SIBLING-ATTESTED**; `n` and P-values absent from the served body |
| R11 | same | **3 months** | Rotarod · open field · EPM | Motor coordination, anxiety | 🔴 NO | 🔴 NO | **HD only**, comparator **WT + RI**, no LD arm, no untreated-KO arm. ⚠️ Rotarod reads ***supra*-WT** (*"significantly higher motor coordination and learning compared with WT mice"*) — uninterpretable in either direction. **SIBLING-ATTESTED** |
| R12 | same | from ~P14, 7 d | **ECoG**, single channel | *"the recording electrode was positioned above the **right dorsal cortex**"* | 🔴 NO | 🔴 **NO — no cerebellar electrode** | *"limited cohort"*. **SIBLING-ATTESTED** |
| R13 | **Mouse neuronal `Wwox` deletion**, `PMID 33914858` | — | *"impaired axonal conductivity"* (abstract, first-hand) | 🔴 **Recording site NOT STATED in the abstract** | 🔴 NO | 🔴 **NOT RECONSTRUCTABLE** | 🔴 **No PMCID; the local PDF carries the `P 5 0.05` text-layer defect and is `SUSPECT`; the reading is SUSPENDED in this repository (`FT-044`).** I do **not** assert the site was or was not cerebellar. `PREMISE: UNREAD_PRIMARY` + `SOURCE_BLOCKED` |
| R14 | **Mouse `Wwox^P47T/P47T`** knock-in (SCAR12 allele), `PMID 36828035` | 🔴 **age NOT STATED for the behavioural cohort** (n = 19 / 17 / 16) | **Rotarod**, 4 rpm + 20 rpm/min acceleration, 3 trials | Time to fall; distance travelled | 🔴 NO | 🔴 NO | Mutant falls sooner, shorter distance, than `+/+` and `+/−`. **FORMALLY COMPARED** |
| R15 | same | — | Hindlimb clasping; OFT; EPM; JSET; TCST | Clasp; centre time; open-arm time; social preference | 🔴 NO | 🔴 NO | Clasping **DESCRIPTIVELY DIFFERENT**; OFT/EPM anxiety-like ↑ and locomotion ↓ — **FORMALLY COMPARED**, cerebellum-mute |
| R16 | same | **> 6 weeks**, 21–53 h, n = 3 / 3 | **Video-EEG**, silver wire electrodes *"implanted bilaterally into the subdural space over **frontal and parietal cortex**"* | Interictal spikes, GTCS | 🔴 NO | 🔴 **NO cerebellar electrode** | >4 seizures / 24 h in all three mutants; WT 0–68 spikes/h, no seizures. **FORMALLY COMPARED** |
| R17 | same | **80 d and 250 d**, n = 3/group | **Calbindin⁺ Purkinje** and **Hcn1⁺ basket** counts in 1000 µm sections; ML thickness (calbindin) and GL thickness (calretinin/DAPI), 24 measurements per animal in preculminate + primary fissures | **Anatomy** — listed because it is the *only* cell-type-resolved cerebellar quantification in the corpus and it is **not** functional | ✅ yes | ✅ yes | PC number significantly reduced; **basket cells `ns` at both ages** — a genuine specificity control. ⚠️ 250-d cohort is survivor-selected. **FORMALLY COMPARED** |
| R18 | same | 150–280 d, n = 5/group | **Cerebellar RNA-seq** | Enrichment for *"cerebellar dysfunction"* and movement-disorder gene sets | 🔴 NO | 🟡 region-resolved transcriptome | 🔴 **An enrichment label is an annotation, not a measurement of cerebellar function.** The paper's *"severe cerebellar dysfunction"* rests on histology + transcriptome, **never** on a physiological or cerebellum-specific behavioural readout |
| R19 | **Mouse `Wwox^gt/gt` hypomorph**, `PMID 17823927` | lifespan | Lifespan, testis histology, fertility, B-cell lymphoma incidence | — | 🔴 NO | 🔴 **NO — no neurological or motor phenotyping is reported at all** | **NOT TESTED.** 🔴 See § 1.3 — the brief's hard constraint, verified |
| R20 | **Rat `lde/lde`** (exon-9 13-bp frameshift), `PMID 19500159` / `PMID 17803050` | 21–33 d | **EEG**, 8 channels (4 unipolar, 4 bipolar) | Interictal spikes on **bipolar occipital leads**; audiogenic seizures 19/20 = 95 % (females only) | 🔴 NO | 🔴 **NO — scalp/cortical montage, no cerebellar lead** | **FORMALLY COMPARED** for seizures (0/14 controls). Cerebellum: **NOT TESTED** |
| R21 | same | — | *"Ataxic gait"*, 95 % of mutants vs 0 % of controls | **Observational, unblinded**, scored inside the *"Observation of epilepsy"* section | 🔴 NO | 🔴 NO | 🔴 Repo audit, verbatim: *"non sono stati eseguiti test motori quantitativi (rotarod, footprint, analisi cinematica)"*. **DESCRIPTIVELY DIFFERENT** |
| R22 | same | perinatal / immature | `PMID 31340538` — **cerebral cortex** neurite growth, oligodendrocyte and glial counts | — | 🔴 NO | 🔴 **NO — cortex, and anatomical** | Not a functional measurement and not cerebellar |
| R23 | **Mouse `Wwox^+/−`** | 3 weeks / P13–17 | Rotarod, footprint, clasping (R1–R3); slice LFP (R6) | — | 🔴 NO | 🔴 NO | Motor battery **all ns**; Tc-MEP latency `p < 0.05` with normal amplitude; 4/23 S-HT slices burst vs 0/11 S-WT. A subclinical **forebrain** network phenotype. Cerebellum: **NOT TESTED** |

### 1.2 Human

| # | Pole · allele | n | Instrument | What was measured | Cerebellum-localising? | Class |
|---|---|---|---|---|---|---|
| H1 | **SCAR12**, `P47T` homozygous, `PMID 17470496` | 4 sibs | **Clinical narrative only** | *"Moderate to mild cerebellar ataxia and psychomotor retardation … severe dysarthria, nystagmus, diminished reflexes"*; walking delayed to 2–3 y | 🟡 the *signs* are, the *instrument* is not | 🔴 **NOT TESTED** — no scored scale of any kind |
| H2 | **SCAR12**, `G372R` homozygous | 2 sibs | Clinical narrative | *"spastic ataxia, and paraplegia"* | 🟡 confounded by spasticity | 🔴 **NOT TESTED** |
| H3 | **SCAR12**, both families | 6 | **SARA · ICARS · BARS · posturography · quantitative oculomotor or saccade recording · eyeblink conditioning** | — | — | 🔴 **NOT TESTED — zero, all six instruments, both families.** `PREMISE: NOBODY_LOOKED` |
| H4 | **SCAR12** | 6 | Cerebellar imaging | *"Mild cerebellar atrophy … in MRI of two affected children"* — 🔴 **secondary**; the primary's own abstract says *"MRI … of **one** patient revealed … **posterior white matter hyperintensities**"* | 🟡 | `PREMISE: SECONDARY_UNVERIFIED` (repo-held, `FT-149`). **No volumetry** |
| H5 | **WOREE / WWOX-DEE**, `PMID 36779245` | **13** (12 families) | Clinical examination; scalp EEG; brain MRI, all reviewed at cohort level | 🎯 *"**None achieved independent walking**"* (13/13) · *"All had poor or absent eye contact"* · 11/13 nonverbal · severe truncal hypotonia · spasticity 10/13 | — | See § 1.4 — **structurally untestable**, not merely untested |
| H6 | same | 13 | Movement-disorder phenotyping | **Dystonia 8** (3 with dyskinetic component), bradykinesia 2, parkinsonism 1, hyperekplexia 1 | 🔴 **NO** | 🎯 **Ataxia is not recorded as the movement disorder in any of the 13.** FORMALLY TABULATED per patient |
| H7 | same | 13 | **Brain MRI, qualitative radiological read** | Cohort pattern = severe frontotemporal atrophy (13/13), hippocampal atrophy, very thin corpus callosum, **severe optic atrophy in all**, white matter signal change. **Cerebellum is not part of the cohort pattern.** Per-patient cerebellar mentions: Pt 3 *"mild vermis atrophy"* (19 m), Pt 7 *"abn T2 BG, **cerebellum**, peduncles, brainstem"* (8 m), Pt 10 *"inc T2 brainstem **dentate nuclei**"* | 🟡 3/13, qualitative | 🔴 **NO VOLUMETRY anywhere.** `MEASURED` = no; `DESCRIPTIVELY DIFFERENT` at best |
| H8 | **WOREE**, `PMID 38161429` | **101 across 9 studies** | Systematic neuroimaging collation | *"Hypoplasia of the cerebellar vermis"* → **`2:2`**, one study; *"less specific"*; of Tabarki's five: *"**Of note, the cerebellum was not affected**"*; one fetal + high-resolution **post-mortem MRI at 21 GW**, *"mild hypoplasia of the cerebellar vermis"* | 🟡 imaging | **Imaging, not function. No volumetry, no histology.** SIBLING-ATTESTED |
| H9 | **WOREE**, any cohort | — | SARA · ICARS · posturography · eyeblink conditioning · VOR/optokinetic · quantitative gait | — | — | 🔴 **NOT TESTED, and see § 1.4: not testable in this population** |

### 1.3 🔴 The `gt/gt` hypomorph — the brief's hard constraint, verified at source

`PMID 17823927` abstract, first-hand, verbatim:

> *"Homozygous Wwox gene-trap mice (Wwox(gt/gt)) had **no detectable Wwox protein in most tissues examined**,
> although, **a low level could be detected in a minority of tissues**."*

Three things follow, and only these three:

1. **The tissues are not enumerated on the surface I read, and brain is not among any tissue named.** The named
   organs in the abstract are **testis** (atrophic seminiferous tubules, reduced fertility) and the lymphoid
   compartment (B-cell lymphoma). ⇒ **Residual WWOX in `gt/gt` brain or cerebellum is an ABSENCE OF
   MEASUREMENT.** `PREMISE: NOBODY_LOOKED`. It is **not** evidence of absent brain protein, and this file
   states nothing that implies otherwise.
2. **No neurological or motor phenotyping is reported for this allele at all** — not rotarod, not gait, not
   EEG, not clasping. So the `gt/gt` row of every functional census is `NOT TESTED`, which is a different thing
   from a negative result.
3. ⚠️ `abstract-depth` ⇒ `PREMISE: UNREAD_PRIMARY`. The body is already queued (`A10` of the acquisition
   packet). `REVIVAL_TRIGGER` in § 5.

### 1.4 🎯 NEW — the human cerebellar endpoint in WOREE is not unmeasured, it is **structurally unavailable**

This is the census's most consequential human finding and it is first-hand from `PMID 36779245`.

Every instrumented cerebellar functional test in clinical use requires at least one of: **stance and gait**
(SARA items 1–3, ICARS posture/gait subscale, all posturography), **voluntary limb targeting** (finger-chase,
nose-finger, fast alternating movements), **intelligible speech** (dysarthria scoring), or **visual fixation
and pursuit** (oculomotor subscales, optokinetic, VOR-cancellation).

The Oliver cohort, verbatim: *"None achieved independent walking"*; *"All had poor or absent eye contact,
consistent with visual impairment"*; 11/13 nonverbal; severe truncal hypotonia with peripheral spasticity in
10/13; 11/13 gastric-tube fed.

⇒ 🔴 **In WOREE, SARA, ICARS, posturography and quantitative oculomotor testing are not merely unperformed —
their prerequisites are absent in the population.** Recording a zero here as "nobody looked" would be
misleading; the correct record is **instrument/population mismatch**, and the consequence is that
*any* future WOREE trial that wants a cerebellar endpoint must build one from scratch for a non-ambulant,
visually-impaired, non-verbal cohort, or borrow one from the SCAR12 pole.

⇒ 🎯 **And the mirror statement is the actionable one. SCAR12 is the WWOX population where these instruments
ARE administrable** — those patients walk (delayed to 2–3 years), survive to 17–26 years, and carry ataxia,
dysarthria and nystagmus as their defining signs. **Nobody has ever administered a scored ataxia scale to a
SCAR12 patient.** That is a genuine `NOBODY_LOOKED`, on a population of six, at essentially zero cost, and it
is the cheapest human-side item this census produced.

### 1.5 🔴 A cross-model contradiction that must never be smoothed

Repo-attested verbatim from `PMID 19500159`'s Discussion: *"Although **neither abnormal behavior nor impaired
motor skill was observed in the Wwox KO mice** (Aqeilan et al. 2007), lde/lde rats show ataxic gait and
spontaneous epileptic [seizures]"*.

Against `PMID 32000863`, where two independent `Wwox`-null mouse strains show large, formally compared rotarod
and footprint deficits at P18–20.

⇒ **Two `Wwox`-null mouse reports, from two laboratories, disagree on whether the null mouse has a motor
phenotype at all.** Different targeting strategies, different backgrounds, different ages, different
laboratories. This is recorded as an unresolved divergence, **not** adjudicated here, and it is a standing
reason never to write "the Wwox-null mouse is ataxic" without naming the line.

---

## 2 · Prospective `DISCOVERY_TRACE`

**Predictions were written to `scratchpad/predictions_registered.md` at 13:13:54 UTC on 2026-09-22, before the
first PubMed call of this axis (13:16 UTC onward).** They are reproduced unchanged.

| # | Prediction, as registered | Falsifier fixed in advance | Outcome | What decided it |
|---|---|---|---|---|
| **M-1** | **No Purkinje-cell recording** (simple/complex spike, in vivo or slice, loose-patch or whole-cell) exists in ANY Wwox model of ANY species | one such paper | 🟢 **SUPPORTED** | `(WWOX OR Wwox) AND (Purkinje)` → **2**, both **counts**, neither a recording. `… AND ("cerebellar slice" OR "cerebellar slices" OR "parallel fiber/fibre" OR "climbing fiber/fibre" OR "long-term depression" OR "deep cerebellar nuclei" OR "inferior olive")` → **0**, all nine terms present and correctly expanded in the returned translation. Full-text semantic corpus (Scholar Gateway) → 15 passages, **14 of them contain no WWOX at all**. Bounded by `PREMISE: METHODS_INVISIBLE` (see § 2.1) |
| **M-2** | **No cerebellar slice work** of any kind, in every allele | any cerebellar slice recording | 🟢 **SUPPORTED — and upgraded from an absence to a positive statement.** The negative no longer rests on a query: `PMID 34634460` Methods says the cerebellum was **removed before slicing**. `NOT TESTED, BY PROTOCOL` |
| **M-3** | **No eyeblink conditioning, VOR, optokinetic or vestibular testing** in any Wwox model | any | 🟢 **SUPPORTED** | `… AND (eyeblink OR "vestibulo-ocular" OR optokinetic OR nystagmus OR vestibular OR oculomotor OR saccade)` → **1**, a human case report (`PMID 38407561`) in which *nystagmus* is a presenting **sign**, not a test. First-hand token census of `PMID 36828035`: `eyeblink` 0, `vestibul` 0 |
| **M-4** | **Quantitative gait kinematics exist only as ink-paw footprint in the `Wwox^+/−` heterozygote**, reported as no-difference, with **zero** in the null, `gt/gt`, `P47T`, conditional and rat alleles | a CatWalk/DigiGait/footprint dataset in any homozygous Wwox model | 🔴 **REFUTED** | `PMID 32000863` ran ink-paw footprint kinematics — **stride length, hind-base width, hind/fore-base ratio, ≥5 steps per animal** — in the **homozygous null**, in **two independent knockout strains**, at P18–20, with all three significantly decreased. The het half of my prediction was right (`ns`); the half that mattered was wrong. 🎯 **A quantitative gait dataset in a homozygous Wwox model DOES exist, and this census would have mis-stated the corpus had the prediction not been falsifiable.** It remains, however, **not cerebellum-localising** — see § 2.2 |
| **M-5** | **No human instrumented cerebellar functional measure** (SARA, ICARS, BARS, posturography, quantitative oculomotor) in SCAR12 or WOREE | any scored scale or instrumented test | 🟢 **SUPPORTED** | `… AND (posturography OR "Scale for the Assessment and Rating of Ataxia" OR SARA OR ICARS OR "ataxia rating scale" OR volumetry OR "cerebellar volume")` → **0**, complete and correct expansion of all seven terms (note `SARA[All Fields]` also matches the surname *Sara*, so the query is if anything **over**-inclusive and the zero is not a tokenisation artefact). First-hand read of `PMID 36779245` end to end: no scale anywhere. `PREMISE: METHODS_INVISIBLE` still attached — a scale buried in a supplement would not index |
| **M-6** | **No human cerebellar MRI volumetry** in SCAR12 or WOREE | any numeric cerebellar volume in a WWOX patient | 🟢 **SUPPORTED** | Same zero as M-5 on `volumetry` / `"cerebellar volume"`. `PMID 36779245`'s entire MRI reporting is qualitative radiological prose (*"mild vermis atrophy"*, *"severe frontotemporal atrophy"*); `PMID 38161429` tabulates presence/absence across 101 patients. Not one cubic millimetre |
| **M-7** | **`gt/gt`: no cerebellum-resolved functional readout**; whatever motor testing exists is a composite | any | 🟢 **SUPPORTED, and stronger than predicted** — the founding paper reports **no neurological phenotyping whatsoever** (§ 1.3). The binding note travels intact: absence of a brain WWOX quantification in `gt/gt` is a **missing experiment**, never evidence of absent brain protein |
| **M-8** | **No rodent Wwox paper reports a motor readout that is cerebellum-localising by construction** | any cerebellum-specific behavioural assay | 🟢 **SUPPORTED** | Rotarod, clasping, footprint, open field, EPM, Tc-MEP — every one is a composite or a non-cerebellar tract measure. § 2.2 |

**Score: 7 SUPPORTED · 1 REFUTED · 0 AMBIGUOUS.** One open boundary rather than a score: `PMID 33914858`'s
*"impaired axonal conductivity"* has **no stated recording site on any surface this repository may read** (no
PMCID; the local PDF is `SUSPECT` and its reading is suspended). It is the single place where a cerebellar
conduction measurement is not formally excluded, and I decline to guess. `REVIVAL_TRIGGER` in § 5.

### 2.1 🔴 Two PubMed failure modes demonstrated LIVE today — one of them new to the established list

**(i) NEW — a quoted phrase does not match its own plural.** `(WWOX OR Wwox) AND (… "motor evoked potential" …)`
returned **2** records and **did not include `PMID 32000863`**, whose abstract contains *"transcranial motor
evoked potential**s**"*. The quoted phrase is matched against the indexed token stream; the singular phrase does
not match the plural token. A known-positive was silently dropped. This joins the seven established modes as an
eighth: **quoted-phrase number agreement**.

**(ii) `METHODS_INVISIBLE`, quantified for the first time on this corpus.** Positive control
`(WWOX OR Wwox) AND (neocortex OR neocortical OR "hippocampal slice")` → **exactly 1** record (`34634460`).
At least **three** papers in this corpus contain neocortical electrophysiology (`34634460`, `34747138`,
`33914858`). ⇒ **Index recall for a physiology term on this corpus is ≈ 1/3.** A PubMed zero on a physiology
term therefore carries roughly **one third** of the power one would naively assign it — which is exactly why
M-2's negative was rebuilt on a Methods sentence rather than left resting on a query.

### 2.2 🎯 Why the refutation (M-4) does **not** create a cerebellar readout

Stride length, base width and base ratio are the classic cerebellar-ataxia gait signature — and in this animal
they are uninterpretable as a cerebellar measure, for four independent reasons, each first-hand from the same
paper:

1. **Severe peripheral neuropathy in the same animals**: *"a large number of abnormal-shaped and demyelinated
   axons in a compact mass were found in the sciatic nerves"*, with active caspase-3 in Schwann cells.
2. **A corticospinal deficit in the same animals**: Tc-MEP amplitude down ~5×, latency up ~75 % (R4).
3. **Body size**: the animals are severely dwarfed; the size-normalised gait analysis is reported only as
   *"data not shown"*, so the reader cannot separate a short stride from a short mouse.
4. **The authors' own attribution**: *"severe hypomyelination in the central and peripheral nervous systems
   **may cause** the behavioral deficits including poor balance, motor incoordination and gait ataxia"* — they
   do not attribute it to the cerebellum.

⇒ The corpus's one quantitative gait dataset is a **whole-organism motor composite measured in an animal with
at least three non-cerebellar motor lesions**. `gate_is_not_quantity`: the instrument is fine, its selectivity
is zero. This is the census's general finding in miniature.

---

## 3 · Seven mechanistically distinct explanations for how a neuron-restricted vector improves ataxia

All are `IPOTESI`. **No winner is selected and no probabilities are assigned**, because no discriminating
measurement exists. 🔴 **None of these asserts that Purkinje cells are poorly transduced — that is unmeasured,
and E1 is precisely the branch in which they are well transduced.**

### E1 · Purkinje cells **are** transduced and express WWOX, and nobody has looked
**Mechanism.** `hSynI` is active in Purkinje cells, AAV9 reaches them, WWOX is restored cell-autonomously, and
the ataxia improvement is exactly what it appears to be. The reason this is invisible is a reagent convention:
the programme's only cell-type-resolved cerebellar number is `NeuN⁺WWOX⁺`, and NeuN has not labelled Purkinje
cells since Mullen 1992.
**Discriminating readout.** Per-cell WWOX intensity in calbindin⁺ somata (Scientist J's stain) — **high**.
**What kills it.** Calbindin⁺ cells reading near-zero.

### E2 · Granule-cell rescue alone suffices
**Mechanism.** The transduced population is overwhelmingly granule cells (they dominate the NeuN⁺ compartment
and the homogenate). Restoring WWOX to the granule layer restores mossy-fibre → granule → parallel-fibre
throughput; Purkinje cells then fire normally on a normal input, with no Purkinje-autonomous WWOX at all.
**Discriminating readout.** 🎯 **The joint measurement**: per-cell WWOX in calbindin⁺ somata **near-zero**
*while* Purkinje simple-spike rate and regularity (CV2) normalise **in the same animal**. Neither channel alone
separates E2 from E1 — which is why § 4 puts both in one preparation.
**What kills it.** PC physiology still abnormal despite a fully rescued granule layer.

### E3 · The improvement is not cerebellar at all
**Mechanism.** The treated animal stops being a dying animal. CNS-only WWOX restoration is reported to
normalise **glucose**, Leydig cells, fertility and cortical bone; it restores **myelination** non-cell-
autonomously; and it rescues the forebrain network. A mouse that is no longer hypoglycaemic, cachectic,
hypomyelinated and seizing will clasp less and stay on a rod longer whatever its cerebellum is doing.
**Discriminating readout.** A **non-cerebellar motor axis measured in the same animals as a cerebellar one**:
Tc-MEP-style corticospinal conduction + grip strength + body weight + blood glucose, alongside Purkinje
physiology. E3 predicts the systemic and corticospinal axes normalise while the cerebellar one does not.
**What kills it.** Cerebellar physiology normalising while the systemic axes are still abnormal.

### E4 · Non-cell-autonomous support through presynaptic partners
**Mechanism.** `hSynI` reaches granule cells, and also pontine and **inferior-olivary** neurons. Purkinje
function is rescued *through its inputs* — parallel-fibre drive and climbing-fibre drive — without any
Purkinje-autonomous WWOX. Note the construction constraint already held by this repository: **`hSynI` cannot
reach Bergmann glia at all**, so any glial component of Purkinje support is untreatable by this vector by
design.
**Discriminating readout.** 🎯 **Input side versus output side, separately**: PF-PC EPSC amplitude and
paired-pulse ratio, and CF-evoked complex-spike waveform and CF mono-innervation, **versus** PC intrinsic
excitability (rheobase, input resistance, spontaneous rate in synaptic blockade). E4 predicts inputs normalise
while PC-intrinsic properties stay abnormal; E2 predicts both normalise; E1 predicts PC-intrinsic normalises.
**What kills it.** PC-intrinsic properties normalising with inputs unchanged.

### E5 · The ataxia endpoint is too coarse to have detected a residual deficit
**Mechanism.** Nothing cerebellar is fully rescued; the instruments simply cannot see what remains. Hindlimb
clasping is near-binary; rotarod is a composite with a ceiling and is confounded by motivation, weight and
learning — in the TX-007 arm it even reads **supra-WT**, which is not a possible true result for a
cerebellum-deficient animal and marks the assay as saturated.
**Discriminating readout.** A **high-resolution** endpoint in the **same treated animals**: interlimb
coordination variability and phase dispersion on CatWalk/DigiGait, or delay eyeblink-conditioning acquisition
slope. E5 predicts the coarse endpoints look rescued and the high-resolution ones do not.
**What kills it.** High-resolution kinematics and cerebellar learning both indistinguishable from WT.

### E6 · Timing, not targeting — the cerebellar window closed before P0
**Mechanism.** Purkinje cells are born E11–E13 and are post-mitotic before birth. A P0–P5 ICV intervention
arrives after Purkinje specification and initial dendritogenesis. WWOX may be delivered perfectly and simply
arrive too late for this cell type, while arriving in time for postnatally-generated granule cells and for
myelination.
**Discriminating readout.** Purkinje number and layer thickness in the **untreated KO at P0–P2** versus WT, and
in treated KO at P30; plus **flatness of every cerebellar readout across dose and across the existing D0–D5
window arms**. E6 uniquely predicts a cerebellar deficit that is **dose-insensitive and age-of-injection-
insensitive** — which is what the existing `0.1×–1.4×` cerebellar pattern already looks like.
**What kills it.** An untreated KO cerebellum that is normal at P0–P2, or a cerebellar endpoint that moves
with injection age.

### E7 · Survivor selection manufactures the appearance of cerebellar rescue
**Mechanism.** The untreated-null comparator is absent *because those animals died*, and every behavioural and
P240/P300 readout is taken on animals that lived. If treatment changes **which** animals reach the test day, the
treated cohort is enriched for the constitutionally mildest phenotypes. The cerebellar improvement would then be
a property of the cohort, not of the cerebellum — and no amount of cerebellar measurement in survivors detects
it.
**Discriminating readout.** 🎯 **An intention-to-treat cerebellar endpoint**: a per-animal early severity marker
(P10–P14 weight trajectory, seizure burden, clasping) linked to that same animal's P30 cerebellar readout, with
the **full treated cohort accounted for including deaths**. E7 predicts the early marker, not the treatment arm,
predicts the cerebellar outcome.
**What kills it.** Cerebellar outcome independent of early severity within the treated arm.

### 3.1 Distinctness check — no two explanations die on the same observation

| Falsifying observation | E1 | E2 | E3 | E4 | E5 | E6 | E7 |
|---|---|---|---|---|---|---|---|
| Calbindin⁺ PC WWOX reads **near-zero** | 🔴 **dies** | 🟢 supported | — | 🟢 supported | — | — | — |
| PC physiology normal **with** PC WWOX near-zero | — | 🟢 **confirmed** | — | 🟢 supported | — | — | — |
| Systemic/corticospinal axes normalise, cerebellar does not | — | — | 🟢 **confirmed** | — | 🟢 supported | 🟢 supported | — |
| PC-**intrinsic** properties normalise, inputs unchanged | 🟢 supported | — | — | 🔴 **dies** | — | — | — |
| High-resolution kinematics + eyeblink both WT-like | — | — | — | — | 🔴 **dies** | 🟡 weakened | — |
| Cerebellar endpoint **moves with dose or injection age** | — | — | — | — | — | 🔴 **dies** | — |
| Cerebellar outcome **independent of early severity** within the treated arm | — | — | — | — | — | — | 🔴 **dies** |

Seven explanations, seven distinct falsifiers. E1/E2/E4 are separated **only** by measuring per-cell WWOX and
Purkinje physiology in the same preparation — which is the whole argument of § 4.

---

## 4 · The ONE compressed experiment

> ## 🥇 **Delete one sentence from a running protocol: keep the cerebellum.**
>
> **Acute sagittal cerebellar-slice loose-patch recording of Purkinje simple and complex spikes — plus
> PF-PC and CF-PC evoked responses — at P13–P17, in `Wwox`-null, AAV9-hSynI-WWOX-treated null, heterozygote and
> wild-type littermates; with the contralateral hemicerebellum from the SAME animals post-fixed for calbindin +
> WWOX per-cell intensity.** One animal yields the functional readout and the transduction readout, on the same
> genotype, at the same age.

### 4.1 Why this and not something else

**1. The tissue already exists and is currently discarded.** `PMID 34634460` runs exactly this preparation, at
exactly this age, in exactly these genotypes, in the collaborating Toronto laboratory, and its Methods discard
the cerebellum before slicing. The experiment is not a new cohort; it is **a change to one line of a dissection
protocol** plus a vibratome plane.

**2. 🎯 It supplies the comparator the entire programme lacks — the untreated null — and viability is
DEMONSTRATED, not assumed.** Behaviour cannot be run on untreated nulls: *"we could not assess behavior of
Wwox-null mice due to their poor conditions and premature death"*. **Slice physiology can.** `PMID 34634460`
recorded **42 slices from 24 S-KO mice** at P13–P17. The barrier that has made every behavioural comparison in
this programme rescued-vs-WT **does not apply to a slice**. This is the single strongest argument for the
design and, so far as this census can tell, it has not been made.

**3. Its outcome is genuinely unpredicted, and that is what information gain means.** E1 predicts high PC WWOX;
E2 and E4 predict near-zero PC WWOX with normal PC firing; E3 and E6 predict abnormal PC firing regardless.
Three live hypotheses make **opposite** predictions from the same preparation.

**4. It is the only design that separates E1, E2 and E4**, because those three differ **only** in the joint
distribution of per-cell WWOX and per-cell physiology — a joint distribution no existing or planned experiment
measures.

**Cost class:** 🟡 **`PROTOCOL AMENDMENT TO A RUNNING EXPERIMENT`** for the untreated-null / het / WT arms —
no new vector, no new age, no new behaviour, no new animals beyond those already being killed. 🔴
`REQUIRES A TREATED COHORT` for the AAV arm, unless the existing window-arm animals (`S8`, D0–D5, HD, *"at
least three littermates per time point"*) are still being generated, in which case that arm is also an
amendment rather than a cohort.

**What is deliberately NOT added.** No in-vivo awake unit recording (new rig, new surgery, and the null does not
survive to an implantable age). No eyeblink conditioning (needs a behaving adult; the null dies at 3–4 weeks —
it is the right experiment for the **`P47T`** allele, which lives ~393 days, and is a separate proposal). No
zebrin/Aldolase-C module mapping — the parasagittal-banding question is already an
`NEW ANALYSIS ONLY` item on the archived whole-slide scans and belongs to the sibling node.

### 4.2 🔴 What this experiment CANNOT settle

1. **Necessity.** Presence of WWOX in a Purkinje cell is not a demonstration that a Purkinje cell needs it. Only
   a **`Pcp2`/`L7`-Cre × `Wwox^fl/fl`** cross tests necessity. The floxed exon-1 allele exists and its makers
   named this cross in print in 2020; it has never been reported. 🔴 `NEW ANIMAL COHORT REQUIRED`.
2. **Development versus deficit.** At P13–P19 the cerebellum is still maturing; a difference may be **delay**,
   not loss. Two ages are needed, and the second age is available **only in the treated arm**, which
   reintroduces survivor selection — i.e. it cannot by itself kill **E7**.
3. **Translation versus protein stability.** A steady-state per-cell WWOX intensity is the product of synthesis
   and degradation, and nothing here splits them.
4. **Cerebellar learning.** Eyeblink conditioning and VOR adaptation test what the cerebellum *learns*, not what
   it *does*. Slice physiology is mute on both, so it cannot fully kill **E5**.
5. **Humans.** Mouse, and a specific null line. It transfers to neither WOREE nor SCAR12, and to no dose, route
   or construct recommendation in any species. **Nothing here is medical advice.**
6. **The `gt/gt` allele.** This design says nothing about the hypomorph, whose brain WWOX remains unmeasured.

### 4.3 The cheapest companion item, at essentially zero cost

**Administer a scored ataxia scale (SARA or ICARS) to the living SCAR12 patients** (§ 1.4). Six individuals, two
families, alive at 17–26 years, ambulant, with ataxia as the defining sign — and not one scored assessment in
the literature. It is the only human cerebellar functional measurement in WWOX disease that is **both absent and
administrable**. 🟢 `NO NEW EXPERIMENT` — it is a clinical assessment, not research apparatus.
⚠️ Patient contact, recruitment and any clinical assessment are `HUMAN_REQUIRED` and outside every agent
mandate; this file records the gap and takes no action.

---

## 5 · `REVIVAL_TRIGGER`s and what I COULD NOT establish

### 5.1 `REVIVAL_TRIGGER`s

| # | What is currently recorded | What would reopen it |
|---|---|---|
| T1 | **No cerebellar physiology exists in any Wwox model** | Any Purkinje, deep-nuclei, PF-PC or CF-PC recording, in any species, any allele; or a cerebellar electrode in any in-vivo Wwox recording |
| T2 | `PMID 33914858`'s *"impaired axonal conductivity"* has **no reconstructable recording site** | A clean structured surface (PMC deposit, publisher XML, or an uncorrupted PDF passing the `P 5 0.05` sentinel) for `FT-044` |
| T3 | **`Wwox^gt/gt` brain WWOX is unmeasured**, and the allele has no reported neurological phenotyping | The `PMID 17823927` body (`A10`) naming brain among *"tissues examined"*, or any `gt/gt` CNS western, or any `gt/gt` motor/EEG phenotyping |
| T4 | Repudi 2021's clasping test may or may not carry an untreated-KO arm | **Appendix Fig S3** of `PMID 34747138` becoming retrievable (`FT-152`) |
| T5 | **No human instrumented cerebellar measure** in SCAR12 or WOREE | Any SARA/ICARS/BARS score, posturography, quantitative oculomotor recording or eyeblink conditioning in any WWOX patient, including in a supplement |
| T6 | **No cerebellar volumetry** in any WWOX patient | Any numeric cerebellar or vermian volume, normalised or raw, in SCAR12 or WOREE |
| T7 | `Wwox^P47T/P47T` behavioural cohort **age is NOT STATED** | The `PMID 36828035` supplement or a correction stating the age at rotarod/OFT/EPM |
| T8 | Two `Wwox`-null mouse lines **disagree** on whether a motor phenotype exists (§ 1.5) | A head-to-head, or the Aqeilan 2007 primary read first-hand with its motor methods |
| T9 | The eighth PubMed failure mode (**quoted-phrase number agreement**, § 2.1 i) is asserted from one instance | A second instance, or a counter-example where a quoted singular does match an indexed plural |

### 5.2 COULD NOT ESTABLISH

1. 🔴 **Where `PMID 33914858` recorded axonal conduction.** No PMCID; the local PDF is `SUSPECT`; the reading is
   suspended. Optic nerve and sciatic nerve are both plausible given the co-authorship, and **I decline to state
   either** — an inference about a recording site is exactly the kind of guess that becomes a citation.
2. 🔴 **Whether `Wwox^gt/gt` brain retains residual WWOX.** Unmeasured. Not a negative.
3. 🔴 **The age of the `Wwox^P47T/P47T` behavioural cohort.** Absent from the Methods I read in full.
4. 🔴 **Whether any Wwox paper's *supplement* contains a cerebellar functional measure.** Supplements are not
   indexed and I retrieved none for `32000863`, `36828035` or `34634460`. Every absence in § 1 is bounded to the
   surface I read and carries `PREMISE: METHODS_INVISIBLE`.
5. 🔴 **Whether the TX-007 figure panels carry `n` or P-values for the clasping "ataxia score".** The served body
   contains zero `n =` and zero P-value tokens; the values are `SIBLING-ATTESTED` from figure reads.
6. 🔴 **Whether the Aqeilan-line `Wwox`-null is ataxic at all**, given § 1.5.
7. 🔴 **Whether archived cerebellar material from either AAV study still exists.** Archive retention is
   `NOT STATED` in both papers, as the sibling nodes also record.
8. 🔴 **Any human cerebellar functional datum whatsoever.** Six SCAR12 patients, ~75 WOREE patients in the
   published literature, and not one scored cerebellar assessment. `PREMISE: NOBODY_LOOKED`.

---

## 6 · Self-grade

| Component | Grade | Reason |
|---|---|---|
| **§1 census completeness** | **A−** | Every rodent allele in the corpus is represented with its own row, no allele is pooled, and the three papers most likely to hold a cerebellar functional readout were read first-hand today rather than inherited. Held off an A by item 4 of § 5.2: **no supplement was retrieved for any of the three**, so every negative is bounded to the served body |
| **§1 instrument discipline** | **A** | Every row answers *what the instrument structurally excludes* before reporting its number: Tc-MEP is corticospinal by the authors' own sentence, clasping is not cerebellar, rotarod saturates and in one arm reads supra-WT, the slice study physically discards the cerebellum, and the human WOREE cohort cannot perform the prerequisites of any cerebellar scale |
| **§2 trace quality** | **B+** | Eight predictions, all registered with explicit falsifiers before the first query, **one genuinely refuted** — and refuted in the direction that would have made the census wrong. Not higher because M-1/M-2/M-3/M-8 were close to one another in content, so seven SUPPORTED overstates the number of independent bets: they are better read as three |
| **§2.1 method contribution** | **A−** | A new PubMed failure mode demonstrated on a live known-positive, plus the first **quantification** of `METHODS_INVISIBLE` on this corpus (≈1/3 recall for a physiology term), which converts a hand-waved caveat into a number that future sessions can use to size their own zeros |
| **§1.4 human finding** | **A** | The distinction between *unmeasured* and *structurally unavailable* is, I think, the most useful thing in this file, and it comes with its own mirror: the pole where the instruments **are** administrable is SCAR12, where nobody has administered them. Both halves are first-hand |
| **§3 explanation set** | **B+** | Seven mechanistically distinct explanations, seven distinct falsifiers, all five required ones present, and the Purkinje-poor-transduction claim never made. E6 overlaps a sibling's `C3` — I credit it rather than re-badge it, and kept it only because it carries a distinct **functional** prediction (dose- and age-insensitivity). Not higher for that overlap |
| **§4 experiment** | **A−** | The cost-class argument is the real content: the decisive tissue is being generated and discarded by a running protocol, and the untreated-null comparator that blocks every behavioural comparison in this programme is **demonstrably obtainable in slice** — 42 slices from 24 knockout mice, on the record. Held off an A because the treated arm may still need a cohort, which I state rather than hide |
| **§5 honesty of the boundary** | **A** | Eight COULD-NOT-ESTABLISH items, including one where the obvious inference (the `33914858` recording site) was available and declined |
| **Overall** | **B+ / A−** | The census's headline is a zero, and a zero is only worth reading if the instrument that produced it is trustworthy. Most of this file's effort went into that, not into the zero |

**Nothing graded F.** The weakest component is the supplement gap (§ 5.2 item 4): three first-hand body reads
with zero supplements retrieved is a real ceiling on every negative in § 1, and I would rather name it than
grade around it.

---

## 7 · Operating-mode record

**`DEFAULTS_TAKEN`**
- *TX-007 (`PMID 42422765`) and Repudi 2021 (`PMID 34747138`) panel values not re-derived first-hand* → carried
  as `SIBLING-ATTESTED` / repo-attested and tagged on every row. Safe: they are **anatomical and behavioural**
  rows in a **functional** census, and none of this file's conclusions turns on their magnitudes. Different if
  the census had needed a number from them.
- *`PMID 33914858` unreadable on every permitted surface* → recorded as `NOT RECONSTRUCTABLE` and continued,
  rather than stopping. Safe: `SOURCE_BLOCKED → REVIVAL_TRIGGER → CONTINUE` is the established route, and the
  item is already queued as `FT-044`.
- *No supplements retrieved* → declared as a bound on every negative rather than treated as read.

**`DECISIONS_TAKEN`**
- *Excluded the Purkinje transduction stain and the seven-layer decomposition from this file.* Alternatives
  rejected: re-deriving them for completeness. Reversible, and they are one link away. Consulted: the sibling
  files themselves.
- *Refused to infer the `33914858` recording site from author affiliation.* Alternative rejected: stating
  "optic nerve, probably". Reversible; the inference remains available to anyone who wants to make it explicitly.
- *Scored M-4 as REFUTED rather than partially supported.* The het half was right and the load-bearing half was
  wrong; a prediction that is graded on its easy half is not a prediction.

**`STOP_LOG`** — class 1: 0 · class 2: 0 · class 3: 0. No reserved act was required. No git command was run, no
`*_current.md`, registry, queue, ledger, receipt or state-manifest file was touched, no `BATCH_COMMIT` was run,
and no external contact was attempted. Exactly one file was written: this one.

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V0 · Declared deviation

One read-only `git status --porcelain`, self-declared. Nothing staged, committed or pushed —
confirmed against the working tree. **Accepted, recorded, not repeated.** Both of today's later
delegates declared the same deviation unprompted, which is the behaviour the rule is for.

## V1 · 🟢 The decisive sentence is VERIFIED VERBATIM — and it is stronger than reported

I re-pulled `PMC8609180` independently. According to PubMed,
[DOI](https://doi.org/10.1016/j.nbd.2021.105529). Methods §5.2, *slice preparation*:

> *"Once the mice were deeply anesthetized, they were swiftly decapitated, and the brain was
> removed. **The cerebellum and olfactory bulbs were removed**, and the remainder of the tissue was
> placed caudal-side down onto a platform in a solution of ice-cold sucrose…"*

🟢 **CONFIRMED.** And the repository's own manifest for this PMID contains **zero** occurrences of
`cerebell` — verified locally. So `NOT TESTED, BY PROTOCOL` is correct, and the corpus's only
slice-electrophysiology study has never been read for this.

🔴 **Three details that make it stronger than the report states:**
1. **The cerebellum is removed as the first step of the dissection**, before the block is mounted.
   This is not "the cerebellum was not studied". It is **the cerebellum was physically discarded at
   the bench, in every experiment in the paper.**
2. **The tissue is discarded *in order to* mount the forebrain.** The block is placed *"caudal-side
   down"* — removing the cerebellum is what creates that face. The removal is structural to the
   preparation, not an oversight.
3. **The sectioning is coronal** — *"The neocortex and hippocampus were sectioned coronally
   400–500 µm thick"*.

## V2 · 🔴 "Delete one sentence from a running protocol" UNDERSTATES the amendment — and the honest version is a better ask

Because the cerebellum is removed to create the mounting face, and because the forebrain is cut
coronally, **keeping the cerebellum requires a second block and a second cut plane**, not the
deletion of a sentence. Cerebellar slice physiology needs its own orientation; the two cannot come
off one block in one plane.

🟢 **The amendment survives, and reframed it is a stronger argument, not a weaker one:**

> **Stop discarding tissue you already have.** The cerebellum in this protocol is currently
> **binned**. The experiment therefore costs **zero additional animals** — it costs a second
> vibratome block, a second cut plane and additional rig-hours per animal, on tissue that is at
> present thrown away.

Cost class stays 🟡 `PROTOCOL AMENDMENT TO A RUNNING EXPERIMENT`, with the amendment's true content
stated. "Zero extra animals, because the tissue is already being discarded" is a better sentence to
put in front of a laboratory than "delete one sentence", and it is the one that is true.

## V3 · 🟢 The argument I consider the file's best is verified at source

> *"0 of n = 11 slices from 7 S-WT mice; 4 of n = 23 slices from 14 S-HT mice; **36 of n = 42
> slices from 24 S-KO mice**"*

🟢 **CONFIRMED.** So **24 untreated knockout animals were successfully recorded at P13–17** — the
exact comparator whose absence blocks every behavioural comparison in the gene-therapy programme
(*"we could not assess behavior of Wwox-null mice due to their poor conditions and premature
death"*). **The barrier is behavioural, not physiological**, and it is demonstrated rather than
argued. This is the single most useful thing in the file and it changes what can be asked for.

⚠️ **One allele bound the file should carry explicitly.** This is the **Synapsin-I-Cre conditional
S-KO**, not the systemic null. The authors say so themselves: *"it is not clear whether the
Wwox-null mice exhibit a similar electrophysiological phenotype."* The "24 knockouts recorded"
argument transfers as **feasibility of slice recording in a severely affected young animal**; it
does not transfer as a statement about the null.

## V4 · Endorsed, with the constraints kept

🟢 **The human finding is the file's second result and it is correctly bounded.** *In WOREE the
cerebellar endpoint is structurally unavailable, not merely unmeasured* — no independent walking,
no eye contact, mostly nonverbal, which removes the prerequisites of `SARA`/`ICARS` items and all
posturography; and the movement disorder recorded is **dystonia, not ataxia**. The mirror —
**SCAR12 patients are ambulant into their twenties and no scored ataxia scale has ever been
administered** — is the cheapest item in the file and correctly parked as `HUMAN_REQUIRED`.
🟢 **The `gt/gt` line is handled exactly as required**: no neurological phenotyping at all, brain
never among tissues examined, stated as a **missing measurement** and never as absent brain protein.
🟢 **Seven explanations, no winner, no probabilities, and Purkinje transduction never asserted to be
poor.** `E1`/`E2`/`E4` separable only by the joint distribution of per-cell WWOX and per-cell
physiology — correct, and it is why the contralateral-hemicerebellum arm belongs in the same animal.
🟢 **An eighth PubMed failure mode**, verified in kind: a quoted phrase not matching its own plural
(`"motor evoked potential"` missing an abstract reading *potentials*). 🟢 **And the first
quantification of `METHODS_INVISIBLE`** — index recall ≈1/3 for a physiology term — which is a
number this repository has needed for a long time and has never had.

## V5 · Grade

**B+ endorsed; I decline the A−.** The headline negative is real, verified and new, and the
feasibility argument is excellent. It is held at B+ because the one experiment was sold as smaller
than it is (V2), and because, as the file itself says, three first-hand body reads retrieved **zero
supplements**, so every negative in §1 is bounded to the served surface.

**No row is canonical; none is proposed for `BATCH_COMMIT`.** The `Pcp2`-Cre × `Wwox^fl/fl` cross
needed for necessity is correctly listed under what this experiment **cannot** settle.
