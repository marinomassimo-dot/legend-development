# COMMIT CANDIDATE — adversarial falsification pass over the WWOX mechanistic model

**Candidate ID:** CC-20260825-ADVERSARIAL-FALSIFICATION-01
**Date:** 2026-08-25
**Status:** queued; **no canonical scientific file modified**, no meta modified, no ledger appended
**Mode:** adversarial falsification of claims already at registry. Not an ingest, not a deep dive
on a new paper, not a batch commit.
**Target WM:** current at BATCH_COMMIT time; rebase required
**Batch gate:** intentionally untouched

---

## 🔴 APPEND-ONLY CORRECTION — 2026-08-26. One of this candidate's own headline statements is false.

This candidate asserted, twice, that **"nobody has ever performed continuous video-EEG on a
Wwox-null mouse."** That is **wrong**, and the falsifier was inside the repository the whole
time, in a paper this candidate itself cites.

**PMID 42422765 (Obeid 2026) — `PAPER 011`, integrated since `BATCH_20260710_A`, the source of
`CLAIM 011` — performed continuous 24/7 wireless ECoG on `Wwox`-null pups**, transmitter
implanted at P14, recorded for **7 consecutive days**, screened for interictal spikes and SWDs
by a **blinded** investigator, n = 5 per group. Verified here against the structured PMC surface
(`PMID42422765_Obeid2026_PMC.html`, Methods, *"Surgery and ECoG data acquisition"*).

**Why the error happened, stated plainly because the shape matters more than the fact.** I
enumerated four papers — Suzuki 2009, Aqeilan 2007, Aqeilan 2008, Repudi 2021 — found no EEG in
any of them, and asserted a **universal negative over the whole corpus**. That is a negative
without its denominator: the correct procedure was to enumerate every WWOX paper with an
electrophysiology method *before* claiming absence. Worse, the counter-evidence was not obscure:
`CLAIM 011`'s own title in the working model contains the string **"ECoG/SWD"**, and I had read
that line earlier the same session. I checked what I remembered and not what the registry said.

**Everything downstream of that sentence is superseded by
[`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md)**, which re-derives the CLAIM 037
adjudication from the ECoG evidence. The direction of the repair does not soften: `CLAIM 037`'s
headline is not merely over-broad, it is **false**, and the falsifier is canonical.

Two statements in §2 below are retracted in place and marked `[RETRACTED 2026-08-26]`.

---

## 0. Reading provenance — what this pass may and may not claim

This pass produced **no `complete_fulltext_read`** and **no `FULLTEXT_READ_RECEIPT`**. Every
reading below is a **targeted adjudication** of named propositions against a fingerprinted
artifact. It clears no reading debt. `FT-044` stays open.

### 0.1 First-hand adjudications performed here

| Source | Artifact | SHA-256 | Surface adjudicated |
|---|---|---|---|
| PMID 33914858 — Repudi et al. 2021, *Brain* 144:3061–3077 | `files/fulltext/PMID33914858_Aqeilan2021.pdf` | `960569a9c0d4e7634a53e3b829fc29145767f9df0ce620cf827b891c6708d559` | **rendered pages 1, 4, 5, 6 at 200–220 dpi** (PyMuPDF), read as images |
| PMID 18487609 — Aqeilan et al. 2008, *JBC* 283:21629 | `files/fulltext/PMID18487609_Aqeilan2008_PMC.html` | `4e8d70eaa9eeb4290edc014b642433d91f3ffa81f1cd6908cadb821033ecc5df` | structured PMC text |
| PMID 17360458 — Aqeilan et al. 2007, *PNAS* 104:3949 | `files/fulltext/PMID17360458_Aqeilan2007_PMC.html` | `89b96fefd93cddba72eeb5774ca889bb3e2a9ba0dd2000ec0aed2031aac403fd` | structured PMC text (targeted absence check) |
| PMID 34268881 — Steinberg et al. 2021, *EMBO Mol Med* 13:e13610 | `files/fulltext/PMID34268881_Steinberg2021_PMC.xml` | `de340289bc6704c9b9ec752f81afed64a02211a83d95d675a1d46f40be6304f6` | JATS XML (targeted absence check + Discussion) |
| PMID 25331887 — Abu-Odeh et al. 2014, *PNAS* | `files/fulltext/PMID25331887_AbuOdeh2014_PMC.html` | `8c629a545f7cc6961dfe349148a2878709f046e6892d33328eda7dbbf3c008f2` | structured PMC text (authorship check) |
| PMID 32581702 — Iacomino et al. 2020, *Front Neurosci* | `files/fulltext/PMID32581702_Repudi2020_PMC.xml` | `369100251faee767e1002188cb63f78622df88c1b2b8dde09f71c5dc89855e1f` | JATS front matter (attribution check) |

🔴 **Rule 5d applies and was applied.** PMID 33914858 is `pdf_only` with a `SUSPECT` text layer
(`FT-044`: the extractor returns `P 5 0.05` where the page prints `P < 0.05`). Every proposition
attributed to it below was read **off the rendered page**, never off the text layer. The text
layer was used only to locate which page to render. Two positive controls held on the rendered
pages: `Results were considered significant when P < 0.05` (p. 3065) and `delta (< 5 Hz)`
(p. 3065) — both of which the extractor corrupts.

🔴 **Rule 5e applies.** No crop, page image or figure is written into the repository. The
regeneration recipe is the table above plus the page numbers and dpi; the images live only in a
session scratchpad outside the repo.

### 0.2 Second-hand adjudications reused, and attributed

Where a number below comes from a **prior LEGEND figure adjudication** rather than from this
pass, it is marked `[manifest]` with its manifest and entry number. Those are:
`deepdive_manifests/PMID18487609.json` (Aqeilan 2008 figures),
`deepdive_manifests/PMID34634460.json` (Breton 2021),
`deepdive_manifests/PMID42397075.json` (Steinberg 2026 *Brain*),
`deepdive_manifests/PMID42128308.json` (Aqeilan 2026 review),
`deepdive_manifests/PMID32581702.json`, `PMID31543760.json`, `PMID31340538.json`,
`PMID19936220.json`.

### 0.3 The structural observation that frames everything below

**Most of what falsifies the canonical layer is already inside this repository, in the manifest
and ledger layers, and has not propagated to the claims.** Of the fourteen adjudications below,
eight rest on locators captured by previous readings. The failure mode is not ignorance — it is
the uneven application CLAUDE.md names: a finding recorded where it was found, not carried to
where it bites.

---

## 1. Current model inventory — axes and load-bearing claims

Derived from `claim_registry_current.md` (39 claims) and `working_model_current.md` (WM_v4.2).

| Axis | Claims | Weight in the model |
|---|---|---|
| Network hyperexcitability / E-I (P1) | 002, 021, 015 | **core** — "primary disturbance of neocortical network stability"; drives BLOCK-1 ACTIVE 1 |
| GABAergic vulnerability / safety (P2) | 001, 005, 037 | **core safety** — drives the vigabatrin position |
| Prenatal / developmental architecture (P3) | 014, 015, 022 | core — drives "EEG > early MRI" and the DEE framing |
| Myelin / white matter (P4) | 003, 004, 011 | surveillance — drives MRI+DTI logic |
| Metabolism / mitochondria / redox (P5) | 009, 010, 025, 026, 034, 036, 038 | supporting, with counter-direction recorded |
| Neuroinflammation / glia (P6) | 005, 006 | modifier, declared downstream |
| Gene-therapy readiness / threshold (P7) | 004, 011, 030, 032, 033 | **core therapeutic** — sets the dose-threshold logic |
| Wnt / MYC | 002 (via PMID 42397075) | emerging |
| GSK3β node | 016, 035 | emerging, residue-resolved |
| DNA damage / canonical WWOX | 029 | structural, non-operational |
| Domain / routing / interpretive | 007, 019, 023, 024, 028, 030, 033 | interpretive scaffolding |
| Clinical spectrum / natural history | 008, 012, 013, 017, 018, 020, 031 | contextual |

**Axes with no claim at all**, noted because absence is a finding: no claim covers
**ion-channel biophysics** (the model's only intrinsic-excitability datum, a depolarised resting
potential, sits inside CLAIM 021 without being named), and no claim covers **mouse epilepsy** —
see CLAIM 037 below.

---

## 2. Claim-by-claim adjudication

### CLAIM 032 — "WWOX haploinsufficiency is not deleterious: the therapeutic threshold is well below full restoration"

**CURRENT_STATUS:** `in observation` · DATO · T1/T2 · clinical relevance **VERY HIGH**

**BEST_SUPPORTING_EVIDENCE:** every published human family has healthy heterozygous carrier
parents; the `Wwox^gt/gt` hypomorph is viable while the null dies at 3–4 weeks; Tochigi 2019
`+/lde` rats express ~half the protein with normal cortical IHC. In this pass, one further
independent support: in the synapsin-Cre conditional the heterozygote *"did not show any
abnormal phenotypes and was behaviourally indistinguishable from control mice"* (PMID 33914858,
p. 3065, rendered page).

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — three independent measured heterozygote phenotypes, all
already in this repository, none of them in the claim:**

1. **Bone morphology.** PMID 18487609, verified here against the structured PMC surface:
   *"The three-dimensional μCT images of femur metaphysis in mice at day 15 (Fig. 3B) show
   **reduced trabecular member connectivity and bone surface area in both the HET and KO**."*
   Sizes from the figure `[manifest PMID18487609 entry 14]`: trabecular number −19 %,
   connectivity density **−50 %**, bone surface **−54 %**, with no error bars overlapping;
   tissue density −2.6 % and explicitly unchanged. The **same paper**, ~2000 words earlier:
   *"Wwox heterozygous (HET) pups were indistinguishable from wild-type (WT) animals at all
   stages of development and postnatal life."*
2. **Neuronal intrinsic properties.** `[manifest PMID34634460 entries 10, 16]` Breton 2021
   Table 1 marks the heterozygote significantly different from wild type on **four** properties —
   action-potential amplitude, input resistance, resting membrane potential, sag. **Input
   resistance saturates at one allele**: WT 102.88, HET 143.26, KO 143.03 MΩ — the heterozygote
   is indistinguishable from the *knockout*. Resting potential grades monotonically
   (−79.25 / −75.51 / −73.62 mV), and the paper attributes the hyperexcitability precisely to
   the depolarised resting potential.
3. **Network readout.** `[manifest PMID34634460 entry 1]` Spontaneous neocortical bursting:
   0/11 WT slices, **4/23 HET (17 %)**, 36/42 KO (86 %). Computed here: HET-vs-WT Fisher exact
   two-sided **p = 0.28** (not significant, underpowered); KO-vs-WT p = 1.6 × 10⁻⁷.

**MODEL_CONTEXT:** mouse — constitutive `Wwox^+/−` (bone) and synapsin-Cre `Wwox^+/flox` (CNS).
**DIRECT_WWOX.** **CAUSAL** for the allele-dose relation, **ASSOCIATIVE** for the therapeutic
inference built on it.

**SURVIVES_FALSIFICATION: QUALIFIED** — and this is the most consequential qualification in the
pass.

**REASON:** the claim is true at the level it was built on — organism survival, lifespan, human
carrier clinical status — and false as the general statement it is written as
(*"la perdita di un solo allele di WWOX non produce fenotipo"*). Its own list of limits says the
threshold *"è nota per sopravvivenza e **morfologia**"*; morphology is exactly where the
heterozygote is not normal. Worse for the therapeutic argument: the two CNS heterozygote
findings sit on **P1**, the pathway the therapy exists to fix, and on the **same readout**
(neocortical bursting) that defines the disease model. `DL-META-097` recorded the bone half
correctly and declared it `ESPANSIONE`, refusing transfer to human carriers — that refusal is
right for the bone tissue and does not license the claim's general sentence about the mouse.
The CNS half has never been connected to the claim at all.

The consequence is not cosmetic. CLAIM 032 licenses *"correggere o compensare un solo allele
basta, in linea di principio: the reference genotype diventerebbe l'equivalente funzionale di un
portatore sano"*. If the carrier already carries a measurable network phenotype, "functional
equivalent of a healthy carrier" is a statement about **clinic**, not about **network
physiology** — and it silently sets the therapeutic target at a level that has never been shown
to normalise the readout the therapy is aimed at.

🔴 **And it collides with CLAIM 011.** CLAIM 011 established from Obeid 2026 Fig 3B that the
AAV9 dose-response for survival is a **threshold, not a continuum** — below 2.63 × 10¹¹ vg
survival is not rescued at all. CLAIM 032 argues the threshold is *low* because the het is fine.
Those two claims point in opposite directions and neither cites the other.

**MISSING_DECISIVE_EXPERIMENT:** in AAV9-hSynI-WWOX-rescued S-KO mice at graded dose, measure the
three heterozygote-sensitive readouts (slice bursting incidence, sIPSC amplitude, resting
membrane potential) against **both** WT and HET. If the rescue plateaus at the heterozygote
rather than at wild type, the therapeutic threshold is above 50 % and the portfolio's dose logic
inverts. Powered comparison: bursting incidence needs ≳60 slices/genotype to separate 17 % from
0 % at 80 % power.

---

### CLAIM 037 — "The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype … explicitly absent in Wwox-null mice"

**CURRENT_STATUS:** `in observation` · DATO · T2 vulnerability / **T3 for any transfer of the
epileptic phenotype to a murine model**

**BEST_SUPPORTING_EVIDENCE — and it is *strengthened* by this pass.** The claim's negative about
the constitutive null now has a third and a fourth independent support, both found here:

- PMID 17360458 (Aqeilan 2007 *PNAS*, the paper that made the null): the words *seizure*,
  *ataxi*, *behavi* and *motor* occur **zero times** in the whole article.
- PMID 18487609 (Aqeilan 2008 *JBC*), verified against the structured PMC surface:
  *"Although homozygous mice were runted, **they did not exhibit any abnormal behavior or
  impaired motor skills**."*

🔴 **And that turns a positive assertion in the literature into a fifth instance of the
"citation firms up its source" pattern.** PMID 33914858 p. 3065 states, on the rendered page:
*"Wwox-null mice are born at a Mendelian ratio and are indistinguishable from wild-type
littermates.^19,20 Within a few days after birth, mice begin to show signs of growth retardation
**and seizures** until they succumb by 3–4 weeks of age (Fig. 1A–C)."* Adjudicated here:
**Fig. 1A–C contains no seizure measurement** — A is a photograph of WT vs KO at P18, B a weight
curve, C a Kaplan-Meier survival curve. References 19 and 20 are Aqeilan 2007 and Aqeilan 2008,
i.e. the two sources quoted above, one silent and one explicitly negative. The assertion is
unsupported by every source it names.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — the *second clause* of the claim is falsified.** The
same paper's first-hand data, read on the rendered page:

- **S-KO** (`Wwox^flox/flox; Synapsin-Cre⁺`): *"uncontrolled spontaneous tonic-clonic seizures
  beginning at P9 and ranging from several seconds to a few minutes (68.5 ± 13.4 s; n = 6 of
  P14–18)"* (p. 3065, Supplementary Video 2).
- **N-KO** (nestin-Cre): *"N-KO mice showed tremors/seizures (Supplementary Video 1)"*.
- Slice-level correlate: 86 % of S-KO slices show epileptiform bursting vs 0 % of controls.

So **the epileptic phenotype does transfer to a murine model** — two of them — and the
transferability tag `T3 for any transfer … to a murine model` is wrong as written.

🔴 **The claim's stated explanation for the mouse negative is also falsified.** Its evidence
boundary says the mice *"potrebbero morire prima di convulsionare"* and calls the survival
difference the testable ground (2–3 weeks mouse vs 3–12 weeks rat, earliest rat onset day 16).
The S-KO **has the same 3–4-week lifespan** (Fig. 1I, premature death by 3–4 weeks, S-Control
n = 13, S-KO n = 15, P = 0.0001) and seizes **from P9**. Lifespan therefore cannot be the
explanation: a mouse with that lifespan does seize.

**MODEL_CONTEXT:** rat `lde/lde` (positive, EEG-documented) vs mouse constitutive null
(negative, two labs, no EEG ever performed) vs mouse conditional neuronal deletion (positive,
behavioural video only). **DIRECT_WWOX. CAUSAL** for the conditional, **ASSOCIATIVE** for the
species contrast.

**SURVIVES_FALSIFICATION: QUALIFIED — split required.**

**REASON:** the two clauses have opposite fates and must be separated. Clause A (the seizure
phenotype of the *published rat* is real, EEG-documented, and the constitutive-null mouse
negative is not contradicted by any first-hand measurement) **survives and is strengthened**.
Clause B (`T3` for transfer to a murine model) **is falsified**. The residual honest statement
is sharper than either: ~~nobody has ever performed continuous video-EEG on a Wwox-null mouse.~~
🔴 **[RETRACTED 2026-08-26 — FALSE.** Continuous 24/7 ECoG over 7 days was performed on
`Wwox`-null pups in PMID 42422765 (`PAPER 011`). See the correction block at the top of this
file and [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md).**]**
The negative in Suzuki 2009 is an empty table row; the positives in Repudi 2021 rest on
*"a mobile camera, when monitoring the mice at the animal facility"* (PMID 33914858 p. 3064,
Methods, rendered page). Two opportunistically-observed positives and one unmeasured negative do
not constitute a species difference; they constitute an unmeasured axis.

**MISSING_DECISIVE_EXPERIMENT:** continuous video-EEG, P7–P21, one design, five arms:
`Wwox^−/−` (Aqeilan allele), `Wwox^ΔCre/ΔCre` (Aldaz/EIIA allele), `Nes-Cre`, `Syn-Cre`,
`Wwox^+/−`. This single experiment closes CLAIM 037's species question, closes the open question
CLAIM 005 declared testable, and supplies the heterozygote arm CLAIM 032 needs.

---

### CLAIM 003 — "Neuronal WWOX deletion induces non-cell-autonomous hypomyelination"

**CURRENT_STATUS:** `consolidated baseline` · DATO · T2

**BEST_SUPPORTING_EVIDENCE:** PMID 34747138 — oligodendrocytes are never transduced by the
neuron-specific vector (CC1/anti-WWOX co-staining) and myelination improves regardless. That is
direct.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — the experiment the claim declares missing has already
been done, in the claim's own primary source.** CLAIM 003's evidence boundary (written
2026-08-10) states: *"Non promuovibile senza una delezione o un rescue Olig2/CNP-specifici."*
PMID 33914858 — **PAPER 004, the claim's own Source** — contains the Olig2-Cre deletion.
Adjudicated here from the rendered Figure 1 caption (p. 3066): *"(J–L) Conditional ablation of
Wwox either in oligodendrocytes (O-KO) or in astrocytes (G-KO) does not cause phenotypic
abnormalities, such as developmental delay (J and M, shown at P17), weight loss (K and N) and
postnatal lethality (L and O) … (O-Control, n = 11 and O-KO, n = 10, P-value 1.0, no
significance, log-rank Mantel-Cox test)"*. Panels L and O show 100 % survival out to ~120 days.

**But the deletion as performed cannot settle the question**, and that is the useful half:
Figure 1J–O measures **gross appearance, body weight and survival only**. No g-ratio, no EM, no
CC1⁺ count, no MBP. The residual myelin gap the authors attribute to *"an oligodendrocyte-
specific WWOX function"* is therefore neither confirmed nor excluded by it.

Converging, from the same repository: `[manifest PMID42128308 entry 9]` the 2026 Aqeilan review
gives the Olig2-Cre line *"No major defects"* at baseline and a defective-remyelination phenotype
**under cuprizone** — a **conditional requirement**, i.e. an unchallenged oligodendroglial
readout is a *designed* false negative. `[manifest PMID42128308 entry 24]` qualifies that
finding as `IPOTESI` because its sole source, Abudiab 2025, is an unrefereed preprint the review
never labels as one — while `meta_network_myelin_glia_current.md:92` states the cell-autonomous
oligodendroglial role without that qualification.

**MODEL_CONTEXT:** mouse conditional deletions, four Cre drivers. **DIRECT_WWOX. CAUSAL.**

**SURVIVES_FALSIFICATION: QUALIFIED.**

**REASON:** the mechanism is unaffected; the *decisive experiment named in the claim* is wrong
and must be replaced with a narrower and far cheaper one. This is the `PATTERN_ALREADY_SOLVED`
failure applied to evidence rather than to code: the model asked the literature for something
the literature had already delivered, and therefore asked for the wrong thing.

**MISSING_DECISIVE_EXPERIMENT:** myelin quantification — EM g-ratio, unmyelinated axon count,
CC1⁺ and MBP — in the **existing** `Olig2-Cre; Wwox^flox/flox` line at P17 and at 120 days, at
baseline **and** under cuprizone. The line exists and is viable to 120 days; the experiment is a
histology run, not a new mouse.

---

### CLAIM 002 — "WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype"

**CURRENT_STATUS:** `consolidated baseline` · DATO + INFERENZA prudente · T2 · clinical
relevance HIGH

🔴 **Provenance defect first.** The claim's core Source is `PAPER 001`, whose registry record
reads `Identifier: preprint`, `Journal/source: bioRxiv`, `Authors: Steinberg et al.`, with a
**paraphrased title and no DOI**. The refereed version exists, has been read in this repository,
and carries **30 verified locators** — PMID 42397075, *Brain*, DOI 10.1093/brain/awag239 — and
**has no PAPER record at all** (`grep` over `paper_registry_current.md` returns nothing). A
`consolidated baseline` claim is sourced to an unversioned preprint placeholder while its
refereed version sits read and unregistered.

**BEST_SUPPORTING_EVIDENCE:** hyperexcitability and its normalisation by WWOX re-expression are
reproduced across two organoid papers, and SCAR12 patient-derived organoids also show
hyperexcitability `[manifest PMID42397075 entry 17]`.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — four, all from the refereed version:**

1. 🔴 **The rescue's comparator is missing, exactly as in CLAIM 004.**
   `[manifest PMID42397075 entries 11–12]` The text says the treatment restored hyperexcitability
   *"to a level similar to the WT organoids"*; Figure 6A(ii) carries brackets for WT-vs-EGFP and
   EGFP-vs-treated only — **no WT-vs-treated bracket exists**. The same defect the model already
   corrected for the mouse arm is uncorrected in the organoid arm.
2. 🔴 **The rescue does not set an expression level.** `[entries 23, 29]` WWOX protein after
   AAV9 ranges **0.4× to 7× wild type across lines with the same vector** — a 17-fold spread;
   SATB2 in treated WOREE runs from wild-type level to ~11×; TCF-4 falls to 0.3×. Against
   CLAIM 028 (*"more WWOX = better" is not a safe default*) and against CLAIM 035's
   "stable-but-inert" design constraint, an uncontrolled 17-fold spread is a **safety and design
   finding**, not a detail.
3. 🔴 **The neurogenesis phenotype is largely the engineered knockout's.** `[entry 3]` Cell-
   fraction log2FC vs WT: WWOX-KO neurons ≈ −2.6, while SCAR12 and WOREE both sit within ±0.2.
   `[entry 22]` The direct WOREE-vs-SCAR12 neuronal volcano carries essentially nothing past
   threshold — the clinical severity gradient does not appear transcriptionally. `[entry 26]`
   corrects this in the right direction: MYC activation *is* shared by the patient lines in
   radial glia; what the KO carries disproportionately is the downstream consequence.
4. **Method limits** `[entries 18–20]`: the MYC-inhibition pillar uses A51, *"established to
   suppress Wnt **and** MYC"* — the causal attribution to MYC inherits that ambiguity; the three
   experiments carrying the thesis (scRNA-seq, MYC inhibition, ChIP-seq) are the three without
   independent differentiations; *"No randomization or blinding was applied in this study."*

🔴 **And the "immature GABAergic signature / depolarizing GABA" component is not a measurement.**
Adjudicated here against the Steinberg 2021 JATS XML: the article contains **zero** occurrences
of `KCC2`, `NKCC1`, `SLC12A`, `gramicidin`, `perforated` and `bicuculline`. All four occurrences
of *depolariz* sit in **one Discussion paragraph** and are entirely citation-based (Obata 1978;
Ben-Ari 2007; Murata & Colonnese 2020; Khalilov 2005). The paper's own chain is:
*"a marked increase in GABAergic markers … even more surprising when considering the decrease in
GABA receptor components seen by RNA-seq"* → *"several lines of evidence implicate that during
development, GABAergic synapses have a depolarizing effect"* → the spectral-power result
*"further strengthens **the idea** that depolarizing GABA plays a key role"*. No chloride, no
reversal potential, no GABA-evoked response is measured anywhere.

`PREMISE_TAG: DEFAULT_FROM_TEXTBOOK` — *"during development GABA is depolarizing"*. It is doing
real work: the same paragraph uses it to explain *"the lack of efficacy of common anticonvulsant
therapies on immature neurons"*. And the marker pattern it explains (GAD up, GABA-A subunits
down) reads at least as naturally as **reduced** GABAergic signalling.

**MODEL_CONTEXT:** human hESC-derived and patient-iPSC organoids. **DIRECT_WWOX.**
Hyperexcitability **CAUSAL**; depolarizing-GABA **HYPOTHETICAL**.

**SURVIVES_FALSIFICATION: QUALIFIED — split required.**

**REASON:** "WWOX-LoF causes network hyperexcitability" survives, including in patient lines.
"AAV-WWOX rescues the organoid phenotype" survives **only as improvement, not normalisation**,
is silent on radial glia by the authors' own statement (*"rescued neuronal functional phenotypes
without correcting RG abnormalities"*), and comes with no expression-level control. "WWOX-LoF
impairs neurogenesis" transfers poorly to patient genotypes. The GABAergic sub-clause is
`IPOTESI` presented in the working model as a signature.

**MISSING_DECISIVE_EXPERIMENT:** gramicidin-perforated-patch E_GABA (or KCC2/NKCC1 protein plus
Cl⁻ imaging) in WWOX-KO and WOREE organoid neurons and in S-KO cortex, at matched developmental
stage against isogenic control. This is the only measurement that converts the model's GABA axis
from textbook default to datum, and it is the measurement on which the P2 safety position — the
one clinically consequential thing the model says — implicitly rests.

---

### CLAIM 021 — "WWOX loss directly destabilizes neocortical network physiology through combined synaptic and intrinsic mechanisms"

**CURRENT_STATUS:** `consolidated baseline` · DATO · T2 · clinical relevance HIGH

**BEST_SUPPORTING_EVIDENCE:** `[manifest PMID34634460 entries 1, 8, 15]` 86 % of S-KO slices
burst vs 0 % of WT (p = 1.6 × 10⁻⁷, computed here); sIPSC amplitude halved (57.3 ± 31.0 pA →
27.5 ± 19.4 pA); resting potential depolarised with a monotonic genotype gradient. Robust.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — three limits, all altering how the claim should be
worded:**

1. **The excitatory half is negligible.** `[entry 7]` sEPSC amplitude: control 23.3 ± 12.0 pA vs
   KO 24.7 ± 13.6 pA — a **1.4 pA separation inside a 12 pA spread**. The paper's own Results
   say it plainly `[entry 9]`: *"favors excitation over inhibition, **primarily through an
   impairment in the amplitude of the inhibitory currents**"*. The working model's narrative
   lists "increased excitatory drive" beside "reduced spontaneous inhibition" as co-equal
   mechanisms; they differ by a factor of ~9 in effect size.
2. 🔴 **Heterozygotes are pooled into the control arm.** `[entry 10]` The S-CTL pooling rule is
   conditional on no HT-vs-WT difference, and Table 1 marks the heterozygote significantly
   different from WT on four intrinsic properties. The entire spontaneous-current analysis of
   Figure 4E–H uses that pooled control. So the reported "control" values are not wild-type
   values.
3. **The measurement window is late-stage, by the authors' own statement.** `[entry 17]`
   Recordings at P13–P17 in animals dying at 3–4 weeks; *"the chosen age group may mimic a
   late-stage disorder of WWOX"*.

**MODEL_CONTEXT:** mouse `Wwox^flox/flox; Synapsin-Cre⁺`, acute slices and anaesthetised in-vivo
LFP under **ketamine-xylazine** (PMID 33914858 Methods, rendered p. 3064 — ketamine is an NMDA
antagonist and an anticonvulsant). **DIRECT_WWOX. CAUSAL.**

**SURVIVES_FALSIFICATION: QUALIFIED.**

**REASON:** the finding is solid; three descriptors around it are not. Most consequentially, the
working model elevates this to *"a **primary** disturbance of neocortical network stability"* —
**primacy cannot be established by a measurement the authors themselves call late-stage.** The
word "primary" is an inference about ordering that no experiment in the claim's source addresses.

**MISSING_DECISIVE_EXPERIMENT:** the same slice panel at P5–P8, before the seizure onset the
conditional shows at P9. If bursting and the sIPSC deficit are already present pre-onset, the
"primary" framing earns its word; if they emerge with the seizures, network instability is a
consequence and the pathway ordering in the working model changes.

---

### CLAIM 036 — "A systemic constitutive Wwox-null mouse at P18 is metabolically decompensated …"

**CURRENT_STATUS:** `in observation` · DATO + INFERENZA · T3 methodological

**BEST_SUPPORTING_EVIDENCE:** unchanged and strong — glucose, bicarbonate, BUN, calcium, WBC,
splenic atrophy, all quantified with p-values in PMID 19936220.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — one sentence inside the claim is falsified.** The claim
states the confounder *"è esattamente il divario che l'allele condizionale `Wwox^flox` …
è stato costruito per chiudere e **che nessuno ha usato in questa direzione**."* PMID 33914858
uses a conditional allele in exactly that direction, with four Cre drivers, and includes the
control that matters: `Olig2-Cre` and `GFAP-Cre` deletions produce **no growth, weight or
survival phenotype out to ~120 days** (Fig. 1J–O, rendered p. 3066) — so the floxed allele
itself is not deleterious, and the phenotype tracks the *neuronal* deletion.

**Second limiting finding, new: the constitutive null is not one phenotype.** Ludes-Meyers 2009
(Aldaz allele, EIIA-Cre) `[manifest PMID19936220 entry 3]`: *"As early as 72 h after birth 43 %
(15 of 35) of Wwox KOs had died and 77 % had died by 17 days"*. PMID 33914858 Fig. 1C (Aqeilan
allele, rendered p. 3066): survival is **100 % to ~day 19**, then falls to zero by day 25
(WT n = 10; KO n = 11; P = 0.0023). Two "Wwox-null mice" with materially different survival
curves.

**MODEL_CONTEXT:** two distinct null alleles and colonies. **DIRECT_WWOX. ASSOCIATIVE** for the
confounder's scope.

**SURVIVES_FALSIFICATION: QUALIFIED.**

**REASON:** the design warning is correct and should stay. Two things around it are not: the
separation *has* been performed, and the confounder's magnitude is a property of the Aldaz
colony, not of "the Wwox-null mouse". Any canonical text saying "the Wwox-null mouse" without
naming allele, Cre driver and colony is aggregating two different animals.

**MISSING_DECISIVE_EXPERIMENT:** the P18 blood-chemistry panel repeated in the Aqeilan-allele
null and in `Syn-Cre` conditionals. If the neuronal conditional is metabolically normal at P14
while seizing from P9, the confounder is excluded for every CNS phenotype measured in that line —
which retrospectively cleans up CLAIM 005, CLAIM 021 and the whole P2/P6 axis.

---

### CLAIM 039 — "Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95 % versus 0 % — and it is not cerebellar"

**CURRENT_STATUS:** `in observation` · DATO · **T3 — fenotipo di ratto, allele non umano**

**BEST_SUPPORTING_EVIDENCE:** unchanged — 95 % vs 0 %, cerebellum histologically unremarkable.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE:** the claim's `Clinical meaning` asserts *"la letteratura
a valle non lo porta affatto"*. PMID 33914858 carries it, first-hand, in two mouse models
(rendered p. 3065): *"N-KO mice showed tremors/seizures … and **ataxia (lack of coordination in
hind limb clasping test)** as observed in Wwox-null mice (Supplementary Fig. 2A and B)"*; and for
the neuronal deletion, *"these mice displayed lack of coordination and **ataxic phenotype**
(Supplementary Fig. 2C)"*. The abstract of that paper lists ataxia among the four cardinal
phenotypes.

**MODEL_CONTEXT:** rat `lde/lde` plus two mouse conditional deletions. **DIRECT_WWOX. CAUSAL.**

**SURVIVES_FALSIFICATION: QUALIFIED** — the datum survives intact; **two sub-assertions are
falsified**: the `T3 / rat-only` transferability tag, and the statement that the downstream
literature does not carry the phenotype.

**REASON:** ataxia is now a **cross-species, cross-allele** phenotype — rat frameshift null,
mouse nestin-Cre, mouse synapsin-Cre — which makes it *more* interesting than the claim allows,
not less. It is also the one WWOX-DEE phenotype with a documented conserved animal correlate and
**no structural explanation in any species**.

**MISSING_DECISIVE_EXPERIMENT:** quantitative motor phenotyping (rotarod, footprint, kinematics),
blinded, in `Syn-Cre` and `Nes-Cre` conditionals with cerebellar and spinal histology — the rat
work was observational and unblinded, and the mouse work is a clasping test. If ataxia is
non-cerebellar in both species, the lesion localisation becomes a tractable question and a
candidate non-seizure endpoint.

---

### CLAIM 005 — "Reduced GABAergic interneurons and glial activation in WWOX-KO"

**CURRENT_STATUS:** `consolidated baseline` · DATO · T2

**SURVIVES_FALSIFICATION: YES**, unchanged — this claim is already carefully bounded (marker
abundance, not cell loss; NPY DG-only; no medication implication).

**What changes is its declared open question.** Its boundary states: *"Whether the mouse lacks
the phenotype or dies before expressing it is open and testable: the earliest rat seizure onset
(day 16) already exceeds the entire lifespan of the mouse null."* As adjudicated under
CLAIM 037, a mouse with that same lifespan seizes from **P9**. The lifespan explanation is
closed; the question is now *why the neuron-restricted deletion seizes and the systemic null
apparently does not* — or whether the difference is an artefact of nobody having looked with EEG.

**MISSING_DECISIVE_EXPERIMENT:** the same video-EEG panel named under CLAIM 037.

---

### CLAIM 004 — "AAV9-WWOX neuron-targeted rescue shows multi-domain in vivo improvement"

**CURRENT_STATUS:** `consolidated baseline`, flag resolved 2026-08-10 with the comparator written
into the claim.

**SURVIVES_FALSIFICATION: YES**, as currently qualified. No new falsifier found.

**One finding worth carrying:** the comparator defect this claim was flagged for is **not
isolated** — it recurs in the organoid arm (CLAIM 002, Figure 6A(ii), no WT-vs-treated bracket)
and in the Obeid 2026 supplementary (CLAIM 011, S8, no treated-vs-KO comparison). Three papers,
one laboratory group, the same omission: **the bracket that would test whether the rescue reaches
normal is the bracket that is not drawn.** That is a pattern about the evidence base, not about
any single claim, and it belongs in the working model's P7 reading rules.

---

### CLAIM 014 / CLAIM 015 — prenatal cortical development and the "misassembled prenatal substrate"

**CURRENT_STATUS:** both `consolidated baseline`; 015 typed **INFERENZA strongly supported**

**BEST_SUPPORTING_EVIDENCE:** Iacomino 2020's rat BrdU birth-dating shows a clean migration
arrest — `[manifest PMID32581702 entry 4]` eight of ten cortical zones significant, direction
consistent — with cortical wall thickness unchanged `[entry 20]`, which is what makes it a
migration phenotype rather than a growth one. That negative is load-bearing and it is a *tested*
negative.

**BEST_FALSIFYING_OR_LIMITING_EVIDENCE — the *prenatal mammalian* evidence is thinner than
"strongly supported" implies:**

1. `[manifest PMID32581702 entries 1–2]` The sole human neuropathological comparison rests on
   **one affected fetus against one control fetus** — Methods say one, Results say three, and the
   Figure 2A caption says *"compared to a normal fetus"*, singular. `[entry 15]` Figure 2A
   labels cortical layers **only on the control**, so the layer identification in the patient
   section is asserted, not shown — and that identification is the whole claim of the panel.
2. `[entry 18]` The rat experiments are **n = 3 per genotype**, Student's t-test, **ten zones
   per panel with no multiplicity correction**.
3. `[entry 14]` The paper's central molecular claim was tested at protein level in the
   WWOX-deficient human brain and **the result was negative** — *"revealed a slight reduction of
   tubulin-1-alpha protein, although not significant"* — in one half-sentence the Discussion
   never repeats.
4. `[manifest PMID31543760 entries 1–4]` Kośla 2019's dramatic hNPC phenotype is **3D-only**:
   *"No such phenomenon was observed when the cells were cultured in 2D as a monolayer"*, and the
   seeding-density control that would exclude the obvious artefact is *"data not shown"*.
5. 🔴 **A counter-directional developmental fact, currently nowhere in the model.**
   `[manifest PMID31543760 entry 10]` WWOX expression in whole human brain is **higher in adults
   than in 20–33-week fetuses** — 17.7 vs 9.2 TPM RLE.
6. CLAIM 014's own boundary already removes Tochigi 2019 from the prenatal column (PND5–21).

**MODEL_CONTEXT:** one human fetus, rat `lde/lde`, shRNA in human NPCs. **DIRECT_WWOX** for the
rat and the fetus, **INDIRECT** for the knockdown. **ASSOCIATIVE** for the human histology
(n = 1 vs n = 1), **CAUSAL** for the rat birth-dating.

**SURVIVES_FALSIFICATION: QUALIFIED.**

**REASON:** the direction is supported; the strength is not. `INFERENZA strongly supported` on
CLAIM 015 should read `INFERENZA supported on thin and partly uncontrolled n`, with the human
arm marked n = 1 vs n = 1 and the layer identification marked unannotated. Point 5 does not
refute a prenatal role — expression level is not requirement — but it sits directly against the
implicit premise that the prenatal window is where WWOX matters most, which is also the premise
under the P0 gene-therapy window. It deserves to be a stated tension rather than an unstated one.

**MISSING_DECISIVE_EXPERIMENT:** cortical layer markers and birth-dating in `Nes-Cre;Wwox^fl/fl`
embryos (E14.5 injection → P1), n ≥ 6, with the analysis pre-registered on a fixed zone count.
The nestin driver acts from E10.5 and the line already exists; it would give the prenatal
mammalian dataset the model currently borrows from a rat and a single fetus.

---

### CLAIM 006 and CLAIM 007 — the P47T model

**CURRENT_STATUS:** both `consolidated baseline` · CLAIM 006 DATO + INFERENZA, CLAIM 007 DATO

🔴 **SURVIVES_FALSIFICATION: UNRESOLVED — the claims cannot be adjudicated, because their source
record names no paper.**

`PAPER 007` reads: `Authors: Hussain et al.` · `Year: 2023` · `Journal/source: pending
normalization` · **`Identifier: pending normalization`** · `Status: integrated` ·
`Claim links: 006, 007`. Its `Full title` — *"P47T model shows progressive neuroinflammation and
altered PPxY binding"* — is **a restatement of the two claims, not a published title.**

The paper it must be is in the same registry, as an unprocessed placeholder:
`CORPUS-STUB-053`, **PMID 36828035 / DOI 10.1016/j.pneurobio.2023.102425**, real title:
***"WWOX P47T partial loss-of-function mutation induces epilepsy, progressive neuroinflammation,
and cerebellar degeneration in mice"***, `Status: not_processed`, `Claim links: none`.

**Three consequences, in ascending order of importance:**

1. Two `consolidated baseline` claims rest on a PAPER record with no identifier and an invented
   title. This is the **PAPER 021 (Tochigi/Kumada) defect, uncorrected at a second site** — and
   the 2026-08-06 correction of PAPER 021 showed exactly how much an invented title can steer:
   it had been pulling that record toward a lissencephaly reading the study never makes.
2. **The claim keeps the least actionable third of its source.** The published title names
   *epilepsy*, *progressive neuroinflammation* and *cerebellar degeneration*. CLAIM 006 renders
   only the middle one; CLAIM 007 renders a binding assay. Epilepsy and cerebellar degeneration
   reach no claim in the registry.
3. 🔴 **`meta_gaba_paradox_current.md` contradicts itself inside seven lines (17–23).** The
   provenance correction sits at **line 19**: *"Seizures are a RAT phenotype in this literature,
   and they are explicitly ABSENT in Wwox-null mice"*. It is **surrounded** by its own two
   counter-examples: **line 17**, *"Paper 87 (PMID 33914858) — Repudi 2021 Brain: neuronal Wwox
   deletion → hyperexcitability + myelin defects"*, a paper whose published title is
   *"…causes **epilepsy** and myelin defects"* — the same word dropped here as in CLAIM 003 —
   and **line 23**, *"Paper 53 (PMID 36828035) — Hussain 2023 Prog Neurobiol: P47T partial LoF →
   **epilepsy**, progressive neuroinflammation, cerebellar degeneration"*. A canonical meta
   asserts a species restriction that its own evidence list refutes on the lines immediately
   above and below it.

**Why this is the highest-value unread paper in the corpus.** `[manifest PMID42128308 entry 8]`
records from the 2026 review that in the P47T knock-in *"WWOX protein levels … remained
comparable to wild-type"* while the mutation disrupts WW1 PPxY binding — an animal with
**normal WWOX abundance and adult-onset seizures, cerebellar neurodegeneration and ataxia**. That
is the *in vivo* demonstration of CLAIM 030 (severity tracks residual **function**, not
abundance), and a direct warning that any Tier 1/2 biomarker built on WWOX abundance scores this
allele as normal. That entry is explicitly `IPOTESI`, because its source is the review, and the
review's rows cite the unrefereed Abudiab preprint. **The primary has never been opened.**

It is also, on the same evidence, the **only long-lived mouse model** in the WWOX corpus — every
other mouse here dies at 3–4 weeks, which is why the whole murine literature measures a
peri-weaning window and why nothing in the model speaks to adult-onset or progressive disease.

**MISSING_DECISIVE_EXPERIMENT / GAP:** acquire and read PMID 36828035 in full; repair PAPER 007
(identifier, journal, authors, published title) and resolve it against CORPUS-STUB-053; then
re-derive CLAIM 006 and CLAIM 007 from the source rather than from each other.

---

### CLAIM 029 — "WWOX contributes to ATM-linked DDR competence and genome-stability maintenance"

**CURRENT_STATUS:** `in observation` · DATO + INFERENZA prudente · T2 conceptual

🔴 **SURVIVES_FALSIFICATION: UNRESOLVED — registry defect, not evidence defect.**

The same PMID carries **two PAPER records, both linked to CLAIM 029, disagreeing with each
other**:

| | `PAPER 027` | `PAPER 030` |
|---|---|---|
| Identifier | PMID 25331887 / DOI 10.1073/pnas.1409252111 | PMID 25331887 · PMCID PMC4226089 · same DOI |
| Authors | **Schrock et al.** | **Abu-Odeh 2014** |
| Evidence depth | *(integrated)* | **abstract reviewed — full text not yet extracted** |
| Claim links | 029 | 029 |

Adjudicated here against `PMID25331887_AbuOdeh2014_PMC.html`: the article is
*"WWOX, the common fragile site FRA16D gene product, regulates ATM activation and the DNA damage
response"*, and the string **`Schrock` does not occur anywhere in it**. So `PAPER 027` carries a
**wrong author attribution** — the third instance of the invented-metadata class after PAPER 021
and PAPER 007. Meanwhile the full text **is** present locally (`PDF` + `PMC HTML` + `assets`) and
a manifest exists, while the registry still declares the claim's source as abstract-only.

**MISSING_DECISIVE_EXPERIMENT / GAP:** merge PAPER 027 and PAPER 030, correct the authorship to
Abu-Odeh et al., and set the evidence depth from the artifact that is already on disk. Only then
is the claim adjudicable.

---

## 3. Cross-cutting contradiction — the P6 glial direction

Not a single claim, so recorded separately.

- **Mouse hippocampus, systemic KO** (PMID 30290271, CLAIM 005): IBA1 and GFAP **area fraction
  higher** in CA1, CA3 and whole hippocampus.
- **Rat cortex, `lde/lde`** (PMID 31340538) `[manifest entries 5, 8]`: *"the expression level of
  Iba1 in cerebral cortices were significantly **lower** in lde/lde than in +/+ rats at the all
  ages examined"*, GFAP likewise reduced — and the authors state the discordance themselves:
  *"These results are apparently **in contrast** to our present data showing significant
  reductions in dendrite growth of wide-ranging neurons and GFAP- and Iba1-positive areas in the
  cerebral cortex."*
- **Mouse, neuron-specific rescue** (PMID 34747138 / PMID 42422765): ↓GFAP/Iba1 after rescue,
  read by the model as gliosis downstream of neuronal dysfunction.

`meta_network_myelin_glia_current.md` records Tochigi only as *"rat lde/lde: cerebral cortex
hypomyelination"* — the reversed glial sign is nowhere in the canonical layer, and the meta's
Core Findings assert *"gliosis as a downstream response"* as though the direction were settled.

**Classification: CONTRADICTION_TO_RESOLVE.** Species, region and age all differ, so this may be
a real biological dissociation rather than a conflict — but the model currently states one
direction and holds evidence for both.

---

## 4. Model revision candidates

Nothing here is applied. Each line is a proposal for a lawful `BATCH_COMMIT`.

| # | Target | Class | Proposal |
|---|---|---|---|
| 1 | **CLAIM 032** | **QUALIFY** (major) | Replace *"la perdita di un solo allele non produce fenotipo"* with the organism-level statement, and write in the three measured heterozygote phenotypes (bone μCT; four intrinsic properties with input resistance saturating at one allele; 17 % vs 0 % slice bursting, Fisher p = 0.28, underpowered). Add the explicit boundary: **clinically silent ≠ physiologically silent**, and the therapeutic corollary that "partial restoration suffices" cannot be inferred from carrier health on the P1 readout. Cross-link to CLAIM 011 and CLAIM 021 as an open tension. |
| 2 | **CLAIM 037** | **SPLIT** | Clause A (rat phenotype real; constitutive-null mouse negative uncontradicted by any first-hand measurement) → keep, **strengthen** with PMID 17360458 (zero mentions) and PMID 18487609 (*"did not exhibit any abnormal behavior or impaired motor skills"*). Clause B (`T3` for murine transfer) → **retract**: two mouse conditionals seize, one from P9 with n = 6 quantification. Delete the "may die before seizing" explanation — falsified by a same-lifespan mouse. ~~Add the residual statement: no Wwox-null mouse has ever had continuous video-EEG.~~ 🔴 **[RETRACTED 2026-08-26 — FALSE. Superseded by `CC-20260826-CLAIM037-01`, which repairs CLAIM 037 as a *false headline*, not an over-broad one.]** |
| 3 | **CLAIM 003** | **QUALIFY** | Replace the missing-experiment clause: the `Olig2-Cre` deletion **exists** in PAPER 004 and shows no gross/weight/survival phenotype to ~120 days, but **measures no myelin endpoint**. The decisive experiment is myelin quantification in that existing line ± cuprizone. Record the conditional-requirement caveat and its `IPOTESI` status (sole source unrefereed). |
| 4 | **CLAIM 002** | **SPLIT + QUALIFY** | Separate hyperexcitability (survives, incl. patient lines) from rescue (improvement, not tested normalisation; radial glia uncorrected by the authors' own statement; **0.4×–7× WWOX protein across lines with the same vector**) from neurogenesis (largely engineered-KO-specific). Demote the "immature/depolarizing GABA signature" to `IPOTESI` with `PREMISE: DEFAULT_FROM_TEXTBOOK`. |
| 5 | **PAPER 001 / PMID 42397075** | **UPGRADE** (provenance) | Create the PAPER record for PMID 42397075 (*Brain*, DOI 10.1093/brain/awag239, 30 verified locators) and demote PAPER 001 to a superseded preprint pointer, preserved append-only. A `consolidated baseline` must not be sourced to `Identifier: preprint`. |
| 6 | **PAPER 007 / CLAIM 006 / CLAIM 007** | **CONTRADICTION_TO_RESOLVE** | Repair PAPER 007 from CORPUS-STUB-053 (PMID 36828035, *Prog Neurobiol*, real title). Until the primary is read, both claims are **UNRESOLVED**, not `consolidated baseline`. Fix the internal contradiction in `meta_gaba_paradox_current.md`. |
| 7 | **PAPER 027 / PAPER 030** | **CONTRADICTION_TO_RESOLVE** | Merge the duplicate PMID 25331887 records; correct the authorship (Abu-Odeh, not Schrock); set evidence depth from the local artifact. |
| 8 | **CLAIM 021** | **QUALIFY** | Record the ~9× asymmetry between the inhibitory (−52 %) and excitatory (+6 %, inside a 12 pA SD) effects; record the heterozygote pooling into the control arm; record the authors' own late-stage caveat. **Remove "primary" from the working model's network paragraph** or mark it `INFERENZA` — a late-stage measurement cannot establish primacy. |
| 9 | **CLAIM 036** | **QUALIFY** | Retract *"nessuno ha usato [l'allele condizionale] in questa direzione"*. Add: the two null alleles have materially different survival curves (43 % dead by 72 h vs 100 % alive to day 19), so the confounder's magnitude is colony-specific. Require allele + Cre driver + colony wherever a canonical text says "Wwox-null mouse". |
| 10 | **CLAIM 039** | **QUALIFY** | Retract the `T3 / rat-only` tag and the "downstream literature does not carry it" statement; ataxia is cross-species and cross-allele. Keep the "no structural explanation" finding, which is now stronger. |
| 11 | **CLAIM 014 / 015** | **DOWNGRADE** (strength, not direction) | 015: `INFERENZA strongly supported` → `INFERENZA supported`, with the human arm marked n = 1 vs n = 1 and layers unannotated on the patient section; the rat arm n = 3 with 10 uncorrected comparisons; the hNPC arm 3D-only. Add the fetal-vs-adult WWOX expression datum as a stated tension with the early-window premise. |
| 12 | **meta_network_myelin_glia** | **CONTRADICTION_TO_RESOLVE** | Record the reversed glial sign in rat cortex and the authors' own statement of the discordance. |
| 13 | **P7 reading rule** (working model) | **NO_CHANGE to claims, ADD to model** | Record the recurring comparator omission across three papers from one group (CLAIM 004 EM panels, CLAIM 002 Fig 6A(ii), CLAIM 011 Fig S8): where a rescue is reported as reaching normal, check whether the WT-vs-treated bracket exists before importing "normalises". |

---

## 5. Top falsification gaps, ranked by how much resolving them would move the model

1. **Continuous video-EEG across the Wwox allelic/Cre panel, P7–P21.** Five arms:
   `Wwox^−/−` (Aqeilan), `Wwox^ΔCre/ΔCre` (Aldaz/EIIA), `Nes-Cre`, `Syn-Cre`, `Wwox^+/−`. One
   experiment closes CLAIM 037's species question, closes CLAIM 005's declared open question,
   supplies CLAIM 032's heterozygote arm, and would tell the field whether the "mouse has no
   epilepsy" statement it has repeated since 2009 was ever measured. *Changes: disease mechanism,
   model selection for every future preclinical study.*
2. **Does the AAV9 rescue reach wild type, or plateau at the heterozygote?** Graded-dose
   AAV9-hSynI-WWOX in S-KO, measuring slice bursting incidence, sIPSC amplitude and resting
   membrane potential against **both** WT and HET. *Changes: therapeutic prioritisation, directly.
   It is the experiment that decides whether the low-threshold argument of CLAIM 032 survives
   contact with the threshold finding of CLAIM 011.*
3. **The expression window — floor and ceiling — for WWOX restoration.** Per-line, per-cell WWOX
   protein after AAV9 against phenotype rescue. The refereed organoid data show **0.4×–7×** WT
   from one vector, SATB2 to ~11×, TCF-4 to 0.3×. With CLAIM 028 ("more WWOX = better" is unsafe)
   and CLAIM 035 (the ERLIQ 402–406 "stable-but-inert" trap), nobody has established that a
   *ceiling* exists or where it is. *Changes: therapeutic design and BLOCK-1 safety.*
4. **Measure E_GABA in a WWOX-deficient human neuron.** Gramicidin-perforated patch, or
   KCC2/NKCC1 protein plus Cl⁻ imaging, in WWOX-KO and WOREE organoids and in S-KO cortex. The
   model's entire GABA axis — and the mechanistic half of its only clinically consequential
   position, the vigabatrin caution — currently rests on a Discussion paragraph citing 1978, 2005,
   2007 and 2020 general developmental neuroscience, in a paper with zero measurements of
   chloride. *Changes: biomarker selection and the P2 safety rationale.*
5. **Read PMID 36828035 (P47T, *Prog Neurobiol* 2023) in full, and repair PAPER 007.** The only
   long-lived mouse in the WWOX corpus; the only *in vivo* dissociation of normal WWOX abundance
   from severe neurological phenotype; the source of two `consolidated baseline` claims that
   currently cite no paper; and the reason a canonical meta contradicts itself. *Changes: the
   abundance-vs-function biomarker logic (CLAIM 030), the mouse-epilepsy question, and the
   registry's integrity on the P2/P6 axis.* Not descriptive literature — it is the missing
   control for a claim the model already makes.

---

## 6. Tallies

```
CLAIMS_TESTED                     14   (002, 003, 004, 005, 006, 007, 014, 015, 021,
                                        029, 032, 036, 037, 039)
CLAIMS_SURVIVING                   2   (004, 005 — unchanged; 005's open question now closed)
CLAIMS_QUALIFIED                   9   (002, 003, 014, 015, 021, 032, 036, 037, 039)
CLAIMS_FALSIFIED (whole claim)     0
SUB-ASSERTIONS FALSIFIED           5   CLAIM 037 "T3 for murine transfer";
                                       CLAIM 037 "the mice may die before seizing";
                                       CLAIM 003 "not promotable without an Olig2/CNP deletion";
                                       CLAIM 036 "nobody has used the conditional in this direction";
                                       CLAIM 039 "the downstream literature does not carry it"
CLAIMS_UNRESOLVED                  3   (006, 007, 029 — provenance, not evidence)
UNRESOLVED_CONTRADICTIONS          6
```

**The six contradictions:**

1. **Heterozygote bone.** Ludes-Meyers 2009 Discussion (*"heterozygous mice did not show any
   abnormalities … as well as blood or **bone** parameters"*) vs Aqeilan 2008 Results
   (*"reduced trabecular member connectivity and bone surface area in both the HET and KO"*).
   Two labs, both papers fully read here, contradiction recorded nowhere.
2. **Wwox-null mouse seizures.** Asserted in PMID 33914858; denied three times plus an empty
   Table 2 row in PMID 19500159; denied by PMID 18487609, which is one of the two references the
   assertion cites; unmentioned in PMID 17360458, the other.
3. **Null-mouse survival.** 43 % dead by 72 h (Aldaz allele) vs 100 % alive to ~day 19
   (Aqeilan allele). Same nominal genotype, different animal.
4. **Glial direction.** Reduced GFAP/Iba1 in rat `lde/lde` cortex vs increased in mouse KO
   hippocampus vs gliosis-reduced-by-rescue in mouse. Flagged by the rat's own authors, absent
   from the canonical layer.
5. **CLAIM 032 × CLAIM 021.** Haploinsufficiency "not deleterious" vs a heterozygote that is
   intermediate on four intrinsic properties and indistinguishable from the knockout on input
   resistance.
6. **`meta_gaba_paradox_current.md` internal.** "Seizures are explicitly absent in Wwox-null
   mice / are a rat phenotype" vs its own evidence list naming two mouse models with epilepsy in
   their titles.

---

## 7. Therapeutic implications

- **The dose logic of P7 is not settled, and the model currently reads it as settled.**
  CLAIM 032 lowers the target ("partial restoration suffices"); CLAIM 011 shows a threshold, not
  a slope; the heterozygote carries a network phenotype on the pathway the therapy targets; and
  the vector does not control expression level within a 17-fold spread. Four facts, one
  direction each, no synthesis. Until experiment 2 above is done, **"a lower, safer dose would
  still help" and "the threshold sits well below full restoration" are both hypotheses**, and
  the working model should say so where it currently states a design principle.
- **The safety ceiling is unaddressed.** Every P7 statement in the model concerns whether there
  is *enough* WWOX. `[manifest PMID42397075 entries 23, 29]` show a rescue that overshoots by an
  order of magnitude in one direction and undershoots to a third in another. CLAIM 028 and
  CLAIM 035 both predict that this matters. Nothing in the portfolio names a ceiling.
- **The GABAergic caution keeps its clinical position and loses its mechanistic backing.** The
  model already states that the depolarizing-GABA rationale does not predict clinical response
  (CLAIM 001). This pass shows the rationale is not merely non-predictive but **unmeasured** in
  every WWOX system. The vigabatrin position should continue to rest on the human safety signal
  and the conflicting efficacy evidence — not on a mechanism.
- **A non-seizure endpoint is available and unused.** Ataxia is now documented across rat and two
  mouse conditionals, is more penetrant than seizures in the rat (95 % vs ~34 %), and has no
  structural explanation. CLAIM 031 argues that seizure control does not rescue development;
  a quantitative motor endpoint is exactly the kind of readout that argument calls for.

---

## 8. Benchmark candidates discovered

Each is machine-checkable from state that already exists, and each is derived from a defect found
in this pass rather than proposed in the abstract.

| ID | Rule | What it would have caught today |
|---|---|---|
| `CLAIM_SOURCE_IDENTIFIER_GATE` | No claim at `consolidated baseline` may cite a PAPER record whose `Identifier` is a placeholder (`preprint`, `pending normalization`, `multiple`, `PENDING`). | CLAIM 002 → PAPER 001; CLAIM 006/007 → PAPER 007; CLAIM 008 → PAPER 008; CLAIM 023 → CORPUS P206 (already found by a prior reading, by hand) |
| `DUPLICATE_IDENTIFIER_GATE` | Two PAPER records with the same PMID/DOI → `BLOCK_BATCH_COMMIT`. | PAPER 027 / PAPER 030 (PMID 25331887), both linked to CLAIM 029 with different authors and different evidence depth |
| `TITLE_FIDELITY_GATE` | A PAPER record's `Full title` must match the title the corpus seed carries for its identifier. Derived from the harvest, never hand-declared. | PAPER 007's invented title; PAPER 027's wrong author; historically PAPER 021 (Tochigi/Kumada) |
| `PHENOTYPE_DROP_CHECK` | If a source title names a phenotype term (`epilepsy`, `ataxia`, `degeneration`, `lethality`) that appears in **no** claim linked to that paper → `INFO`. | PAPER 004 (*"causes epilepsy and myelin defects"* → CLAIM 003 says only myelination); CORPUS-STUB-053 |
| `MODEL_IDENTITY_GATE` | Any canonical sentence naming a rodent genotype must resolve to (allele, Cre driver, colony/source). | "the Wwox-null mouse" aggregating two alleles with 43 %-by-72 h vs 0 %-by-day-18 survival |
| `PLACEHOLDER_SHADOW_CHECK` | A `not_processed` CORPUS stub whose identifier or title matches an `integrated` PAPER record with a placeholder identifier → the stub is that paper. | CORPUS-STUB-053 shadowing PAPER 007. 🔴 **The existing detector already half-sees this and cannot close it:** `session_self_eval.py` reports `[UNREAD PREMISE] PMID 36828035 cited in meta_gaba_paradox_current.md` — it fires on the meta's explicit citation and is **blind to the same paper reaching two `consolidated baseline` claims through a record that names no identifier.** The unread premise is detected where it is cheap and missed where it is load-bearing. |
| `LOCATOR_TO_CLAIM_PROPAGATION` | A manifest locator whose proposition is marked 🔴 and names a claim ID must be reachable from that claim, or be listed as declared debt. | eight of the fourteen adjudications above |

The last one is the general form of §0.3 and is the one worth building first: **this repository's
manifests are consistently sharper than its claims, and nothing measures the gap.**

---

## 9. What this candidate does not do

- No canonical file is modified. No meta is modified. No ledger is appended. No receipt is issued.
- No reading debt is cleared; `FT-044` (PMID 33914858) stays open and still owes road 2 — the
  text surface rebuilt from the rendering with its own declared extraction method. The pages read
  here were read as images and support **no text locator**.
- PMID 36828035 has **not** been read; every statement about the P47T mouse above is
  bibliographic (its published title) or second-hand through a review whose rows cite an
  unrefereed preprint, and is labelled as such.
- The adjudication of PMID 33914858 covers pages 1, 4, 5 and 6 only. The remaining thirteen
  pages — including the myelin quantification, the organoid arm and the full Discussion — were
  not read.
