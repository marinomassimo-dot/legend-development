# Intake wave 5 — 2026-10-03 — Scientist C (group C)

`context_policy: SOURCE_FIRST`
`branch: task/sci-C-20261003w5`
`theme: AAV9 / intrathecal / neonatal delivery safety as a human and NHP evidence base`

> **Nothing in this note is medical advice.** It supports discussion with a treating clinical team
> and does not substitute for one.
>
> **WWOX occurs zero times in all six sources.** Every one is an earned null for the gene. They are
> read as transferable delivery-safety evidence, and every transfer limit is stated.

---

## 0 · The assigned question

> *What does each source add to, or limit in, the claim that the safety of an intrathecal or
> intracisternal AAV9 dose in an infant can be bounded before the first patient — specifically which
> toxicity is dose-driven, which is immune-driven and therefore modifiable, how much of the dose
> actually reaches the target as opposed to being governed by CSF dynamics, and which of these can be
> measured in a patient rather than only at necropsy — and for each, does the source measure it in a
> human, an NHP, or a mouse?*

## 1 · The six, and what each actually is

| # | PMID | What the selection card said | What the source is | Species | Verdict |
|---|---|---|---|---|---|
| C1 | 41966056 | "first-in-human cohort", MPS I | **single patient, n = 1**, intra-cisterna magna, >5.5 y follow-up | human, second year of life | INGEST |
| C2 | 41210171 | pre-existing immunity, safety and biodistribution | 15 female macaques, **one dose level**, no immunosuppression, 4 weeks, terminal | NHP, ~41 months | INGEST |
| C3 | 41257285 | transcriptional changes after IT AAV9 | 40 female macaques, **empty-capsid and promoterless arms**, RNA-seq at 28 days | NHP, 12–50 months | INGEST |
| C4 | 41948127 | safety/efficacy/biodistribution in mice and NHPs | CMT1A RNAi programme; 20 macaques, **sex-balanced**, 6 and 12 weeks | mouse + NHP | INGEST |
| C5 | 42205472 | "clinical implications for **intrathecal** delivery" | review of **intraventricular** delivery | human physiology, review | INGEST |
| C6 | 42134074 | "deliberately the weakest member; drop it first" | **the only source carrying the human clinical record** | human, review | INGEST |

Nothing was DEFERRED; all six were acquired lawfully, free, as PMC JATS re-fetched by this reader.

## 2 · The answer

### 2.1 Which toxicity is dose-driven

**The honest answer is that this evidence base does not establish a dose–response for the toxicity
everyone is worried about, and three of the four primary studies cannot in principle do so.**

- **C2 cannot**: Figure 6C, read at panel level, prints one dose — 1.2 × 10¹³ vg/animal — identical
  across all three treated groups. Only pre-existing immunity varies.
- **C1 cannot**: n = 1, one dose.
- **C3 can, partly**: 1.0 × 10¹³ versus 3.0 × 10¹³ vg/NHP in study A; the high dose produced
  bilirubin and liver-enzyme elevation with transient tremor, the low dose did not.
- **C4 can, but in mice**: 1E11/2E11/5E11 reduced inflammation in the diseased model while
  **1E12 increased it** — a ≤2-fold step flipping the sign. This is the only explicit threshold in
  the group and it is murine, cargo-specific and confounded by the vector correcting the disease.
- **C6, in humans, points the other way**: DRG signals appeared at 1.2 × 10¹⁴ vg (STEER, two sensory
  cases) while CLN7 at 5 × 10¹⁴–1 × 10¹⁵ and SPG50 at 1 × 10¹⁵ assessed DRG by MRI *and* nerve
  conduction and found nothing. **The human record does not scale monotonically with dose.**

### 2.2 Which toxicity is immune-driven and therefore modifiable

Here the group gives a genuinely clean answer, and it comes from the arms C3 has and nobody else does:

> **Hepatic and DRG toxicities were only detected after administration of full AAV9 viral particles,
> but not empty capsids or Promoterless test articles.** (C3)

At a comparable capsid load, **capsid alone is not sufficient**, and **a genome without a working
promoter is not sufficient**. The injury requires a transcriptionally productive cassette. C6 reaches
the same mitigation independently — weaker or cell-restricted promoters — and a dog row in its
Table 1 reports *"Encephalitis associated with a T-cell response to the transgene product"* after IT
AAV9 carrying GFP: transgene-directed, immune-mediated, and therefore modifiable.

Within C2, immunity and the lesion separate cleanly in opposite directions:

| Finding | Tracks pre-existing immunity? | Evidence |
|---|---|---|
| DRG / nerve-root / spinal-cord axonal degeneration | **No** — the figure caption says so explicitly | C2 Fig 6A |
| Brain meningeal mononuclear infiltrate | **Weakly** — one animal of four graded moderate | C2 Fig 6C panel |
| Perivascular neuropil infiltrate | **No — non-monotonic**: 0/4 low, 2/4 medium, 1/4 high | C2 Fig 6C panel |
| Systemic interferon response, splenic T-cell response, CSF antibody kinetics | **Yes** | C2 Figs 3–5 |
| ALT / GLDH elevation | **No** — "without impact of pre-existing immunity" | C2 |

**So pre-existing immunity drives the systemic and meningeal immune response, not the axonopathy.**

The modifiable axis identified mechanistically is **interferon / JAK-STAT, not NF-κB** (C3), which
is why the authors suggest glucocorticoids may be weaker prophylaxis than assumed. That is a
hypothesis — no immunosuppressed arm was run in any NHP study in this group.

### 2.3 How much of the dose reaches the target

**Not determined by any source here, and C5 explains why the question has no single-number answer.**
Delivered dose at a CSF route is governed by CSF production, pathway anatomy and **age** — C5's own
top three drivers. Particle size is not limiting (the foramina of Luschka are ~40,000× an AAV
capsid). What is limiting is flow, surface adhesion and arachnoid membranes.

Two concrete consequences:

1. **The group uses three mutually non-convertible dose scalars.** Fixed total vg per animal or per
   patient (C2, C3, C6 — every human trial), per gram of brain mass (C1), and per CSF volume
   (C4, scaled 371-fold mouse→macaque, which C5's Table 4 independently reproduces at ≈375).
2. **Only brain-mass scaling adapts to an infant.** The approved human intrathecal product is a
   fixed 1.2 × 10¹⁴ vg for everyone from 2 to 18 years. C5 says plainly that this is current
   practice and is inadequate for a CSF route. **And C5's Table 4 has a single, adult, undated
   "human" row — so the only cross-species scaling table in the group cannot set an infant dose.**

One measured delivery fact does transfer: **pre-existing serum antibody left CNS vector-genome
biodistribution intact while reducing it to DRG, liver and heart and increasing it to spleen** (C2).

### 2.4 Which of these can be measured in a patient rather than only at necropsy

| Readout | Measures | Species it was shown in | Status |
|---|---|---|---|
| **NCV + CMAP, serial** (baseline / 6 wk / 12 wk) | DRG and peripheral nerve **function** | NHP (C4); used in humans in CLN7, SPG50, ALS (C6) | **the strongest item in the group** |
| Spine/brain MRI, serial | structural CNS, DRG signal | human (C1, C6) | routine |
| Plasma NfL | axonal injury, any cause | NHP (C3, cited); mouse (C4) | **bidirectional — see below** |
| CSF IL-12p40 | local inflammation | NHP (C2) | candidate; authors call it inconclusive |
| Serum ALT / GLDH, troponin I, ECG | hepatic / cardiac | NHP (C2, C4); human (C1, C6) | routine |
| Serum + CSF anti-capsid titre | immune exposure and response | NHP (C2); human (C6) | routine; note C1's 320:1–1,280:1 plasma:CSF gradient |
| PET-labelled AAV9 capsid (¹¹C, ¹⁸F, ⁸⁹Zr) | **how much vector reaches where** | cited, not demonstrated here (C5) | the only route to §2.3 in a living patient |

> **The NfL trap, and it matters specifically for WWOX-DEE.** C3 uses rising NfL as a marker of
> vector-induced DRG injury; C4 uses falling NfL as a marker of therapeutic benefit. NfL reports
> axonal injury from any cause. In a disease that itself destroys axons, a rise cannot be assigned to
> the vector and a fall cannot be assigned to rescue without an independent anchor.
> **WWOX-DEE is exactly such a disease**, so NfL alone cannot serve as the DRG-safety readout there.
> NCV/CMAP, which are anatomically specific, can.

### 2.5 §13 boundary — none of this is a WWOX biomarker

Every patient-measurable item above reports **vector–host interaction or generic axonal injury**, not
the functional state of WWOX. Under LEGEND_CORE §13 they are Tier 3 / out of gene-biomarker scope and
belong in the safety-monitoring file, never in the biomarker registry. C1 is the clean illustration:
MPS I has a Tier-1 CSF readout (IDUA enzyme activity) and an accumulating substrate (heparan
sulfate). **WWOX has neither** — no secreted product, no accumulating substrate. What transfers from
C1 is the *architecture* (serial CSF sampling at the dosing route), not the analyte.

### 2.6 The direct answer to the headline question

**No — the safety of an intrathecal or intracisternal AAV9 dose in an infant cannot be bounded
before the first patient on this evidence base, and the reason is not that the data are reassuring or
alarming but that they are mismatched to the recipient.** Specifically:

- not one of the four primary studies dosed an infant, a neonate, or an animal younger than
  12 months (C2 ~41 months, C3 12–50 months, C4 age unreported, C1 is the only paediatric datum and
  is n = 1 at ~20 months);
- three of the four are female-only (C2, C3; C4 is the exception);
- the dose cannot be converted across the group because three incompatible scalars are in use, and
  the one physiological table that would convert them has no paediatric row;
- the DRG lesion that governs the whole field has **no incidence count** in C2 (zero tables in the
  article; the supplement, which I fetched and read, holds only titre tables) and, where it *is*
  counted (C4), **occurs in 50% of concurrent vehicle controls**.

What *can* be bounded before the first patient: the **immunosuppression regimen** (§3), the
**monitoring schedule** (§2.4), the **promoter choice** (§2.2), and the **eligibility criterion**
(serostatus should not alone exclude — C2's conclusion, corroborated by the GAN trial actually
enrolling seropositive participants, C6).

## 3 · The most transferable finding in the group

**Four independent programmes converge on triple immunosuppression where the recipient is predicted
null for the transgene product**, versus a steroid alone where endogenous protein is present:

| Programme | Regimen | Rationale as stated |
|---|---|---|
| GAN (C6) | prednisolone + sirolimus + tacrolimus | CRIM-negative participants "at higher risk of developing an immune response to transgene-expressed gigaxonin protein" |
| CLN7 (C6) | prednisone + sirolimus ± tacrolimus | modelled on GAN |
| SPG50 (C6) | prednisolone + sirolimus + tacrolimus | "given the predicted absence of endogenous expression for this patient" |
| MPS I (C1) | methylprednisolone/prednisone + tacrolimus + sirolimus, 48 weeks | prior anti-IDUA antibody from ERT |
| SMA (C6) | **prednisone alone**, ~2 months | endogenous SMN present via SMN2 |

**A WWOX-DEE recipient with a biallelic loss-of-function genotype falls in the predicted-null class
by construction.** The relevant precedent for a WWOX restoration programme is therefore the
GAN/CLN7/SPG50 regimen, not SMA's prednisone alone.

**Transfer limits, stated exactly.** This is an inference from genotype class to immunological class.
It is not measured for WWOX. No controlled comparison of triple versus single immunosuppression
exists in any of these programmes. The regimens differ in agent, dose and duration. A WWOX missense
allele that produces a stable but non-functional protein would **not** be predicted-null and would
not inherit this precedent — P47T, Q230P, G372R, A141T and P252A are not interchangeable with each
other or with a null, and a heterozygote is neither a demonstrated negative nor a positive.

**The nearest disease precedent** is CLN7 (C6): paediatric, neurodegenerative, seizure-bearing,
intrathecal scAAV9, triple immunosuppression, DRG assessed by MRI and nerve conduction, >2 years
follow-up, "relative stability in their seizures". The transfer limit is the gene: MFSD8 ≠ WWOX,
n = 4, and the efficacy comparison is uncontrolled against historical natural history.

## 4 · The contested DRG question — what this wave settles and what it does not

Waves 3–4 left DRG toxicity contested. This group moves it, in both directions.

**Weakening the case that intrathecal AAV9 injures the DRG:**

1. **Background lesions in controls.** C4: minimal-to-mild DRG lesions in **2 of 4 saline animals**.
   C2 panel C: meningeal mononuclear infiltrate in **2 of 3 vehicle animals**, a lesion the text
   nonetheless classes among "test-article–related microscopic findings". Two independent studies.
2. **No incidence anywhere in C2.** Zero `<table-wrap>` elements in the article; Figure 6C tabulates
   brain only; the fetched supplement holds only titre tables. Methods confirm DRG at four levels
   were sectioned and stained — the data exist and are not reported.
3. **"Representative" is doing real work.** C4's Figure 5A caption says treated DRG show "no
   significant histological abnormalities"; its body says 40% of animals had lesions.
4. **Human negatives at the top of the dose range.** CLN7 and SPG50, assessed by MRI and nerve
   conduction (C6).

**Strengthening it:**

1. **A regulatory hold.** NHP DRG findings stopped enrolment in a human paediatric intrathecal
   programme, which was then terminated early (C6).
2. **Human positives exist.** Two sensory cases in STEER; one ALS patient with MRI and
   electrophysiological signs plus pain, improved but not resolved (C6).
3. **Dose is not the shield.** C6's Table 1 reports NHP DRG toxicity at 1.2 × 10¹³–6 × 10¹³ vg —
   *below* the human IT dose — in juvenile macaques.
4. **A mechanism with a lever.** The lesion needs a productive cassette (C3); promoter strength is
   the proposed mitigation (C6).

**Net position.** The DRG lesion is real, is not driven by pre-existing immunity, is mild and
largely reversible where it has appeared in humans, has a substantial background rate in control
macaques that most reports do not subtract, and has a plausible modifiable driver in the expression
cassette. **The single most useful corrective this wave supplies is procedural: no DRG claim from an
NHP study should be accepted without a concurrent-control incidence, and most of this literature does
not report one.**

**An unresolved tension, recorded rather than harmonised.** C6 attributes DRG toxicity to
"supraphysiological gene expression levels with strong ubiquitous promoters". C3 found transgene
transcript **highest in heart and skeletal muscle — the tissues without pathology** — while injury
tracked vector-genome load in liver and DRG. Both agree a promoter is necessary; they disagree on
whether expression magnitude is the graded driver. The shared mitigation survives either way.

**A hypothesis this wave generates, flagged as such.** At a fixed intrathecal dose, pre-existing
immunity *reduced* DRG vector load (C2). An infant is typically seronegative. It follows, as an
untested HYPOTHESIS, that **a seronegative infant receives higher DRG exposure than a seropositive
adult at the same absolute dose** — for the CNS target immunity is irrelevant, but for the DRG the
seronegative recipient is the more exposed one. This inverts the selection card's framing. It is
untested: no infant was dosed, DRG injury was never quantified in C2, and vector load is not injury.

## 5 · What would change the model if true, and what would falsify it

| Proposition | What would confirm it | What would falsify it |
|---|---|---|
| The modifiable driver of CSF-route AAV9 organ toxicity is the expression cassette, not capsid load | a cell-restricted or weak-promoter construct at matched capsid dose producing the C3 transcriptional signature at reduced amplitude and no DRG lesion | a promoterless or empty-capsid arm producing DRG lesions at a higher capsid dose; or a weak-promoter construct producing the same lesion |
| The relevant prophylaxis for a predicted-null recipient is triple immunosuppression | a controlled comparison of triple vs steroid-alone in a CRIM-negative cohort showing fewer anti-transgene responses and better durability | equivalent outcomes on steroid alone, or triple immunosuppression failing to prevent anti-transgene T-cell responses |
| Steroids are insufficient because the axis is JAK/STAT | a JAK-inhibited arm suppressing the C3 interferon signature where steroids do not | steroid prophylaxis abolishing the interferon signature in an NHP arm |
| NHP DRG lesions over-report vector attribution | concurrent-control incidence reported across several studies showing control rates near the treated rates | properly controlled studies showing treated-only lesions with a clear dose gradient |
| A seronegative infant is the more DRG-exposed recipient | DRG vector load measured across a seropositivity gradient *and* an age gradient at matched dose | DRG load invariant to serostatus in young animals |
| NfL cannot serve as the WWOX-DEE vector-safety readout | baseline NfL in WWOX-DEE shown to be elevated and drifting, with no separable vector-attributable component | stable disease-baseline NfL with a distinguishable post-dose excursion |

## 6 · What in the brief and the selection record was wrong

1. **C5's route.** The selection card titles PMID 42205472 as being about **intrathecal** delivery;
   the paper is about **intraventricular** delivery. Route is the variable the group exists to
   separate from dose, so this is material.
2. **C1's design.** Described as "a small, open-label first-in-human cohort". It is **n = 1**, a
   single-patient IND.
3. **C1's readout.** Described as "generates measurable enzyme activity"; the article's own title
   leads on sustained neurodevelopment without transplant, and the enzyme activity has since fallen
   to 6.8% of control.
4. **C2's question.** The card frames it as deciding "whether an *infant* is an easier or harder
   recipient than an adult". The study has no infant, no juvenile, no male and no dose arm, and its
   measured result points the opposite way from the card's framing (see §4).
5. **C6's worth.** Called "deliberately the weakest member; drop it first if the group needs only
   five." It is the only source in the group carrying the human clinical record, the regulatory
   history and the immunosuppression pattern. Dropping it would have removed the human layer
   entirely.
6. **C4's framing.** The card asks "whether DRG and Schwann-cell findings are reported on the same
   animals" — they are, but the card does not anticipate that the DRG finding's load-bearing number
   is in the **control** arm.

## 7 · Reading-debt discharged, and opened

**Discharged:** none. No registry statement in this repository rests on any of these six PMIDs —
all six had no registry record, no prior receipt and no manifest before this pass
(`paper_packet.py packet --pmid N`, six times: "this is a first reading", "no route recorded").

**Opened — the primaries these six lean on and that LEGEND has not read:**

| Source | Debt |
|---|---|
| C1 | ref 10, the CNS tumour with vector genome integration after the same route and vector; ref 9, the NHP ICM neuropathology study reporting no DRG lesions |
| C3 | ref 10, the authors' own prior study — the primary behind the NfL correlation, the histopathology and the in-life toxicity, none of which is measured in C3 |
| C4 | Figure S23, the contract laboratory's NHP pathology report behind every safety statement; Figure S18, the mouse toxicology report |
| C5 | Supplementary Material 2, the paediatric CSF-flow section — the part of that paper most relevant to this question; and the primaries behind Table 4 |
| C6 | every programme reference, in particular ref 81, the NHP study that triggered the regulatory hold, and refs 33/107 (STRONG/STEER), 34 (GAN), 38 (CLN7), 85 (ALS), 86 (SPG50) |

## 8 · Patient-overlap check

Required by the brief for case series. **C1 is the only source reporting an identifiable patient
course**, and it is a single patient. I checked it against the other five: none reports an
individual patient. Within C6's tables, the SMA, GAN, CLN7, SPG50 and ALS cohorts are distinct
programmes with distinct registrations. C1's subject is **not** the child described in C1's own
citation of the phase 1/2 tumour case: C1's subject was dosed in the second year of life and is
reported tumour-free at >5.5 years, while the cited case was dosed at ~1 year in a different,
registered study. No double-counting found. All description here is at class level.

## 9 · Method notes from this pass

- **Numeric tables must be read cell-wise.** Reading C5's Table 4 from flattened JATS running text,
  where adjacent numeric cells concatenate without a delimiter, produced a plausible but wrong table
  and led me to draft a false criticism of the source. Re-extraction by cell boundary showed the
  source is correct and self-consistent. The defect was mine. Recorded in the C5 dossier §3 and in
  candidate `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`.
- **Panels changed the reading in both papers where I rendered them**, as wave 4 predicted — C2's
  panel C overturned three sentences, C4's panel A contradicted its own caption and corrected a dose
  literal. Both figures are declared artefacts in their manifests.
- **The PMC `instance/<pmcaid>/bin/<file>` path serves figure and supplement binaries where the
  `articles/<PMCID>/bin/` path returns 404**; `pmc_pow_fetch.py` solved the proof-of-work page for
  the one supplement that needed it.

## 10 · Outputs

Dossiers: `fulltext_dossiers/PMID{41966056,41210171,41257285,41948127,42205472,42134074}.md`
Manifests: `deepdive_manifests/PMID{…}.json` — all six **PASS** `--verify-artifacts`
Receipts (prepared, not recorded): `scratchpad/receipts_pending_w5/sciC_<pmid>_1.json`, six files
Candidates: `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01`, `-DRG-ATTRIBUTION-01`,
`-TRANSGENE-NULL-IMMUNOSUPPRESSION-01`, `-DOSE-SCALAR-01`, `-REGISTRY-01`
