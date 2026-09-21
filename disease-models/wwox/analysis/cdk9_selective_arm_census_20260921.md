# Selective CDK9 as the mechanistically exact arm — a census

**Date:** 2026-09-21 · **Actor:** Scientist B · **Node:** `SELECTIVE_CDK9_AS_THE_MECHANISTICALLY_EXACT_ARM`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and every
> ledger. Nothing promoted, nothing committed.
>
> 🔴 **BLOCK-1 observed. No safety triage was run and no druggability score is assigned anywhere in this file.**
> Everything below is a census of what is *published*, with the point where the evidence stops named each time.
> No compound here is proposed for use in any person.
>
> **Nothing here is medical advice.** No dose, route, schedule or indication is formulated for any patient.

---

## 0. Read depth declared up front

| PMID | Identity | Depth **this session** | Returned body length | Figure access |
|---|---|---|---|---|
| **34523672** | Kaveh *et al.* 2021, *Development* — selective Cdk9 inhibition in **larval zebrafish**, with a `cdk9` knockout selectivity assay | 🟢 **full body read in-act** (Intro → Results → Discussion → Methods) | non-empty, **≈28 000 characters (approximate; not instrumented)** | none — no figure-panel claim is made from this environment |
| **38159337** | Le Rhun *et al.* 2023, *Eur J Cancer* — **zotiraciclib (TG02) EORTC 1608 STEAM trial in glioblastoma** | abstract read in-act | abstract only | none |
| **38658199** | **Corrigendum** to the above | metadata read in-act; abstract not available | n/a | none |
| **31699827** · **33306391** | AZD4573 — discovery and characterisation | abstracts read in-act | abstract only | none |
| **31892980** | LDC000067 in chordoma, incl. 3D culture | abstract read in-act | abstract only | none |
| **31872348** | JSH-009 — selectivity across 468 kinases/mutants | abstract read in-act | abstract only | none |
| **38689623** | glioma treatment review naming zotiraciclib | abstract read in-act | abstract only | none |
| **42397075** | the organoid A51 experiment | 🔴 **not fetchable — no PMCID.** Prior-session locators only | 0 bytes | none |
| — | PubMed `"selective CDK9 inhibitor"` | executed | **`total_count: 44`** | n/a |
| — | PubMed `CDK9 inhibitor AND (brain OR glioma OR CNS OR BBB OR neuron OR neurodevelopment)` | executed | **`total_count: 46`** | n/a |
| — | PubMed `zotiraciclib glioblastoma` | executed | **`total_count: 3`** | n/a |

🔴 **Declared gap, and it is the main one.** The **numerical CDK7 fold-selectivity** for AZD4573, JSH-009 and
LDC000067 lives in kinase-panel tables inside full texts I did **not** read; the abstracts assert selectivity
without giving the CDK7 number. **§2 reports what the abstracts state and refuses to supply figures they do not.**
⚠️ Two earlier over-conjoined queries returned `total_count: 0` and are **not** reported as absences; the counts
above come from simple queries that behaved.

---

## 1. The direct answer

**The class exists, it is procurable, and the census returns something the node did not anticipate: the one
CDK9-directed agent that has reached the human brain is not selective either, and its dose-limiting toxicity
was a seizure.** Genuinely selective CDK9 inhibitors are real — **AZD4573** (AstraZeneca, Phase I,
`NCT03263637`), **JSH-009** (*"great selectivity over 468 kinases/mutants"*, explicitly *"a useful
pharmacological tool"*), **LDC000067** (an ordinary research chemical, already used in 3D culture), and
**AT7519**, which is the only one of these whose CDK9-selectivity has been demonstrated **genetically, in a
living vertebrate, against a `cdk9` knockout**. So the arm is procurable for a dish experiment today.
🔴 **But two findings reverse the tone.** **First**, the only CDK9-targeting agent with human CNS data is
**zotiraciclib (TG02)**, and it is *"an oral **multi-cyclin dependent kinase (CDK) inhibitor**"* — the same
non-selectivity trap as A51 — with *"low single agent clinical activity"* (PFS-6 = **6.7 %**), toxicities of
*"neutropenia, gastrointestinal disorders and hepatotoxicity"*, and **two dose-limiting toxicities at 150 mg, one
of which was a grade 3 seizure.** In a disease defined by seizures, that is not a footnote.
**Second, and this is the finding that matters most:** in a developing vertebrate, **continuous** CDK9 inhibition
produced *"developmental and injury-associated adverse effects, including **reduced cardiomyocyte number
expansion**"*, while a **two-hour pulse avoided all of them** — and the authors name the reason: *"The majority of
CDK9 inhibitors act by competitively inhibiting the ATP-binding domain, which is **conserved between all CDKs**."*
🔴 **The A51 organoid experiment used continuous exposure from week 8 to week 15 — seven weeks — which is the
exposure regimen this literature identifies as the harmful one.** ⇒ **A selective CDK9 arm makes the
deconvolution *better* and simultaneously makes the original A51 experiment look worse: it was one dose, one
genotype, no treated wild-type arm, **and** a continuous schedule. The arm to add is AT7519 or AZD4573; the
variable to add alongside it is **duration**, not only dose.**

---

## 2. Task 1 and 2 — the agent table, with CDK7 stated

| Agent | Mechanism / class | Selectivity — **and what is said about CDK7** | Stage | Procurable for a dish experiment? | CNS data? |
|---|---|---|---|---|---|
| **AZD4573** | ATP-competitive CDK9 inhibitor; MCL-1 depletion, ↓pSer2-RNAP2 | *"a novel, potent, and **highly selective** CDK9 inhibitor"*; *"a potent and selective CDK9 inhibitor with suitable predicted human pharmacokinetic properties to deliver **transient** inhibition of CDK9"*. 🔴 **No CDK7 figure is given in either abstract.** The selectivity claim is asserted at abstract level; the kinase panel is in the full texts, unread here | **Phase I**, haematological malignancies, `NCT03263637`; **intravenous**, designed for *short target engagement* | 🟡 likely as a research chemical; not confirmed here | 🔴 **none found** |
| **AT7519** | ATP-competitive CDK inhibitor used as a CDK9 inhibitor | 🟢 **the only genetically demonstrated selectivity in this census.** *"Using cdk9−/− knockout mutants, we showed that **AT7519 is a selective CDK9 inhibitor**"*; and against flavopiridol, *"FVP displaying significant off-target effects from 2 hpt"*. ⚠️ **Still ATP-competitive**, and the same paper says the ATP pocket is *"conserved between all CDKs"* — so **CDK7 sparing is not claimed**, only relative CDK9 selectivity versus FVP | described by the authors as *"clinically approved"* (their word — regulatory status **not verified here**); used in oncology trials | 🟢 **Yes** — sourced in that study from **Astex Pharmaceuticals** | 🔴 no CNS use found; the in-vivo work is **cardiac**, in a **developing** organism |
| **Flavopiridol (FVP / alvocidib)** | first-generation, non-selective | 🔴 **Fails the genetic selectivity test**: *"FVP showed marked off-target effects in the selectivity assay"*. Not a CDK9-isolating arm | long clinical history in oncology | 🟢 Yes | 🔴 none found |
| **LDC000067** | *"selective CDK9 inhibitor"* | Asserted selective; the chordoma study shows the expected PD — *"lowered levels of Mcl-1 and RNA polymerase II (RNAP II) phosphorylation"*. 🔴 **No CDK7 figure in the abstract** | research chemical | 🟢 **Yes**, and it has already been used in **3D spheroid culture** — the closest existing precedent to an organoid arm | 🟡 **CNS-adjacent only**: chordomas *"commonly affect vital neurological structures"*. Not CNS pharmacology |
| **JSH-009** | *"novel highly selective CDK9 inhibitor"* | 🟢 **the broadest selectivity claim in the census**: *"displayed great selectivity over 468 kinases/mutants"*. 🔴 The CDK7 value is inside that panel and **the abstract does not state it**. The authors position it as *"a useful **pharmacological tool** for elucidating CDK9-mediated transcription"* | preclinical, AML | 🟡 research compound; supply route not established here | 🔴 none found |
| **Zotiraciclib (TG02)** | 🔴 *"an oral **multi-cyclin dependent kinase (CDK) inhibitor** thought to inhibit tumor growth via **CDK-9-dependent depletion of survival proteins such as c-MYC and MCL-1**"* | 🔴 **NOT selective — multi-CDK by its own description.** Same trap as A51 | 🟢 **Phase Ib in glioblastoma**, EORTC 1608 STEAM, `NCT03224104` | n/a for this purpose | 🟢 **YES — the only human CNS data in the class.** See §3 |
| **A51 / BTX-A51** *(for comparison)* | CK1α + **CDK7** + CDK9 | 🔴 **explicitly hits CDK7**, which is exactly why it cannot isolate the CDK9 contribution | Phase I, AML/MDS | 🟡 by collaboration | 🔴 none (Wave 6: 6/6 records, zero CNS mentions) |

### 2.1 🔴 The CDK7 problem, stated as the mechanism rather than as a caveat

> "The majority of CDK9 inhibitors act by competitively inhibiting the ATP-binding domain, which is conserved between all CDKs (). Consequently, long-term exposure to CDK9 inhibitor compounds can cause undesirable effects as a result of inhibition of other CDKs, many of which are cell-cycle regulators, such as CDK2 (;)."

`surface: body` · Discussion · `PMID 34523672`, read in-act.

**This is the structural reason a "selective CDK9 arm" is a matter of degree, not of kind.** CDK7 is a
transcription-**initiation** kinase (and a CDK-activating kinase); CDK9 is a transcription-**elongation** kinase.
An ATP-competitive agent that hits both does not separate initiation from elongation — **which is the precise
error `TX-004` already made in a different register**, and the node brief is right that repeating it would be
unforgivable. ⇒ **The honest formulation is not "use a selective CDK9 inhibitor" but "use the most
CDK9-selective agent available and demonstrate the selectivity in the assay system itself."**

🟢 **And one group has shown how to do exactly that.** The zebrafish study built a `cdk9` knockout selectivity
assay — *"a truly selective CDK9 inhibitor would not have any effect on knockout zebrafish larvae"* — and
generalises it: *"this larval zebrafish knockout screening approach could be applied to other druggable targets
and used to identify uniquely selective inhibitors in a high-throughput manner and across short time scales
(≤2 h)."* **That is a transferable method, and it is the only genetic demonstration of CDK9 selectivity in this
census.**

---

## 3. Task 3 — is there any CNS use of a CDK9 inhibitor at all? **Yes, and it is a warning**

`zotiraciclib glioblastoma` → **`total_count: 3`**: the trial report, its **corrigendum**, and a review. Verbatim
from the trial, read in-act:

> "Zotiraciclib (TG02) is an oral multi-cyclin dependent kinase (CDK) inhibitor thought to inhibit tumor growth via CDK-9-dependent depletion of survival proteins such as c-MYC and MCL-1 which are frequently overexpressed in glioblastoma."

> "The MTD was 150 mg twice weekly in combination with radiotherapy alone (group A) or temozolomide alone (group B). **Two dose-limiting toxicities were observed at 150 mg: one in group A (grade 3 seizure), one in group B (multiple grade 1 events). Main toxicities included neutropenia, gastrointestinal disorders and hepatotoxicity.** PFS-6 in group C was 6.7%."

> "TG02 exhibits overlapping toxicity with alkylating agents and low single agent clinical activity in recurrent glioblastoma. The role of CDK-9 and its down-stream effectors as prognostic factors and therapeutic targets in glioblastoma warrants further study."

`surface: abstract` · `PMID 38159337`, EORTC 1608 STEAM, `NCT03224104`.

**Three things follow, and the first two are negatives.**

1. 🔴 **A grade 3 seizure was a dose-limiting toxicity of a CDK9-directed agent in a brain-tumour population.**
   In a disease whose defining feature is pharmacoresistant epilepsy, this is the single most decision-relevant
   fact in the node. ⚠️ **Bounded honestly**: a seizure in a glioblastoma cohort has an obvious competing
   explanation — the tumour — and the abstract does not attribute causality beyond calling it a DLT. **It is not
   evidence that CDK9 inhibition is proconvulsant.** It is evidence that this class has been observed to have a
   seizure DLT in a CNS population, which is enough to require the question be asked and not enough to answer it.
2. 🔴 **The agent that got there is multi-CDK.** The class's CNS beachhead was won by exactly the kind of
   non-selective compound this node was convened to replace. **There is no selective CDK9 inhibitor with human
   CNS data.**
3. ⚠️ **Integrity note**: the trial report carries a published **corrigendum** (`PMID 38658199`), whose abstract
   is not available. **Any use of the numbers above should check what the corrigendum amended** — this node did
   not, and says so.

⇒ **The measured answer to task 3: CNS use of the class exists (`total_count: 3`), CNS use of a *selective*
member does not.**

---

## 4. Task 4 — what a selective CDK9 inhibitor would be expected to do to a progenitor pool

**The discouraging part first, as instructed.**

CDK9 inhibition does not target MYC. **It suppresses transcriptional elongation, and short-half-life transcripts
fall first** — MYC is simply the most famous of them. In a **proliferating radial-glia compartment in a
developing brain**, that is a general transcriptional brake applied to the cells whose job is to divide and
differentiate on a schedule.

🔴 **And this is not speculation: it has been measured in a developing vertebrate.** Verbatim, in-act:

> "We showed that continuous AT7519 or FVP treatments result in developmental and injury-associated adverse effects, including reduced cardiomyocyte number expansion, cardiac function and macrophage wound retention, in addition to neutropenia"

> "Continuous FVP treatment has previously been shown to inhibit cardiomyocyte proliferation in larval zebrafish (), suggesting that the same anti-proliferative effect could be occurring, although cardiomyocyte apoptosis may also contribute to the reduction in cardiomyocyte numbers."

`surface: body` · Results and Discussion · `PMID 34523672`.

**Read directly onto the WWOX question:** continuous CDK9 inhibition in a developing organism **reduced the
number expansion of a proliferating cell population**. That is the same class of effect a radial-glia pool would
be exposed to — and in the A51 organoid experiment, **SOX2⁺ fell from ≈60 % to ≈33 % while SATB2⁺ and CTIP2⁺ did
not move** (`figure-attestation-from-prior-session`). **A progenitor reduction that does not become neurons is
exactly what an anti-proliferative effect looks like**, and it is also exactly what "normalisation" looks like.
**The A51 data as published cannot distinguish the two.**

🔴 **The schedule finding, which is the actionable part.**

> "By limiting the CDK9i treatment period to a 2-h window, we were able to enhance the resolution of neutrophilic inflammation while avoiding all adverse effects."

> "we have shown that the timing, duration and selectivity of CDK9 inhibitor treatment is imperative when targeting the acute inflammatory response to promote tissue repair/regeneration"

`surface: body` · Results and Discussion · `PMID 34523672`.

**Set that against the organoid experiment: A51 was given at 125 nM continuously from week 8 to week 15 — seven
weeks of uninterrupted exposure.** The zebrafish work identifies *continuous* exposure as the harmful regimen and
a **two-hour pulse** as the one that retains benefit. **The A51 experiment used the regimen this literature
flags, and nobody has tested a pulsed schedule in a WWOX organoid.** Independently, AZD4573 was engineered
*"to deliver **transient** inhibition of CDK9"* — the same design principle, arrived at by a different route.

**Two further risk terms that must travel with any encouraging sentence.**
- **p53.** A51 *"activat[es] p53"* — and this literature shows WWOX-deficient progenitors already carrying DNA
  damage and a compromised apoptotic checkpoint. A pro-apoptotic push into that compartment is not obviously
  corrective.
- **`CLAIM 028` and `TX-004`'s own rule.** *"lower MYC/Wnt = better" is NOT a safe default*, and *"more WWOX =
  better"* is not either. **A general elongation blockade in a developing brain is the least targeted
  intervention in this portfolio, and it should be described that way.**
- **`DL-THER-089`'s BLOCK-1 question stays open and now has a second half.** It asked where the window lies
  between reducing excess progenitors and preventing normal corticogenesis. **This node adds that the window may
  be in *duration* as much as in *dose*, and neither axis has been tested in a WWOX system.**

---

## 5. Task 5 — better experiment, or different experiment?

**Better — and the improvement is not the arm I named in Wave 6. It is a second axis.**

Wave 6 proposed four arms differing in **mechanism**. This census shows that a CDK9 arm which differs only in
mechanism would still be confounded, because the harm and the benefit in this class separate along **duration**.
⇒ **The design gains a dimension and loses nothing.**

| Arm | Compound | Procurable today? | What it isolates |
|---|---|---|---|
| Vehicle | — | 🟢 | baseline |
| Reference | **A51 / BTX-A51**, 125 nM, the published schedule | 🟡 **by collaboration only** | reproduces the published result |
| **CDK9 arm** | **AT7519** (Astex) or **AZD4573** | 🟢 **AT7519 yes** — and it is the only agent in the census with **genetically demonstrated** CDK9 selectivity | the elongation contribution |
| Wnt arm | **XAV939** | 🟢 **yes** — already LEGEND's named comparator in `E-10` | the β-catenin contribution |
| **Schedule axis** *(new)* | each arm run **continuously** *and* **pulsed** | 🟢 free — it is a scheduling variable, not a reagent | **separates transcriptional rescue from anti-proliferative toxicity** |
| Controls | treated **wild-type** arm at every dose and schedule; ≥3 independent differentiations; ≥2 clones; blinded and randomised | 🟢 | the three method defects the original experiment declared |
| Readouts | SOX2⁺, SOX2⁺MYC⁺, NEUN⁺, **SATB2⁺, CTIP2⁺**, plus **nuclear β-catenin** (Wave 6) and now **a proliferation index and a cell-death readout** | 🟢 | tells normalisation apart from anti-proliferative suppression |

**Which arms are procurable today: the CDK9 arm and the Wnt arm. The reference arm is not.** That is a workable
position — the two mechanistic arms are the informative ones, and a failure to reproduce A51's effect with either
is itself the answer.

**What each outcome decides.**
- **AT7519 reproduces the SOX2⁺ normalisation, pulsed, without suppressing SATB2⁺/CTIP2⁺ further** ⇒ the effect
  is CDK9-mediated and separable from the anti-proliferative liability. **That would be the first genuinely
  encouraging result this axis has produced**, and only then would CNS exposure become the next question.
- **AT7519 reproduces it only continuously, with a proliferation-index fall** ⇒ **the "rescue" is an
  anti-proliferative effect**, and `TX-004` should be closed rather than refined.
- **XAV939 reproduces it** ⇒ the lever is `R-03`, with `R-03`'s paediatric liabilities.
- **Neither reproduces it** ⇒ A51's effect is off-target and the only pharmacological rescue in human
  WWOX-deficient neural tissue dissolves. **Cheapest possible way to learn it.**

---

## 6. What LEGEND already knew · what is new

### 6.1 Already held

- Wave 6: A51 ≈ BTX-A51 (CK1α + CDK7 + CDK9, `INFERENZA`, recorded in `FT-123`); its zero CNS data; its contested
  Wnt direction; the framing inversion that **the BBB is not the gate because the experiment is in organoids**.
- `DL-THER-089`: A51 at **125 nM, weeks 8 → 15**; the SOX2⁺/SOX2⁺MYC⁺/NEUN⁺ recovery against the SATB2⁺/CTIP2⁺
  null; the three declared method defects; the open BLOCK-1 question; `IPOTESI`, not a candidate.
- `TX-004` / `R-03` / `CLAIM 028`: *"lower MYC/Wnt = better" is NOT a safe default*; XAV939 as the comparator in
  `E-10`; tankyrase intestinal and bone toxicity.
- 🔴 **`CDK9` appears nowhere in LEGEND except in my own Wave-6 file and one queue line.** This class was entirely
  absent from the model before today.

### 6.2 New in this node

1. ✅ **The class is real and procurable**: AZD4573 (Phase I, `NCT03263637`), **AT7519** (Astex — the only one
   with **genetically demonstrated** CDK9 selectivity, via `cdk9−/−` zebrafish), LDC000067 (research chemical,
   already used in **3D culture**), JSH-009 (*"selectivity over 468 kinases/mutants"*, self-described as a tool).
2. 🔴 **CDK7 cannot be assumed spared**, and the reason is structural: *"the ATP-binding domain … is conserved
   between all CDKs."* **No abstract in this census states a CDK7 fold-selectivity figure** — declared gap.
3. 🔴 **The only CDK9-directed agent with human CNS data is zotiraciclib, and it is multi-CDK** — with
   PFS-6 **6.7 %**, neutropenia/GI/hepatotoxicity, and **a grade 3 seizure as one of two DLTs at 150 mg**.
   Bounded: a seizure DLT in a glioblastoma cohort is not evidence of proconvulsant pharmacology. ⚠️ A
   **corrigendum** exists and was not read.
4. 🔴 **Continuous CDK9 inhibition causes developmental adverse effects in a developing vertebrate**, including
   *"reduced cardiomyocyte number expansion"* — a **proliferating-population** effect, read directly onto the
   radial-glia question.
5. 🔴 **The schedule finding, and it indicts the A51 experiment**: a **2-hour pulse** avoided all adverse effects
   while retaining benefit, and AZD4573 was independently engineered for *"transient"* engagement — **while A51
   was given to the organoids continuously for seven weeks.** **Duration is an untested variable in the only
   pharmacological rescue this corpus has.**
6. ✅ **A transferable method LEGEND does not have**: the `cdk9` knockout selectivity assay — *"a truly selective
   CDK9 inhibitor would not have any effect on knockout zebrafish larvae"* — which the authors explicitly
   generalise to other targets at ≤2 h throughput.
7. 🔴 **A51's SOX2⁺ fall cannot be told apart from an anti-proliferative effect** with the published data, and
   the experiment lacks the proliferation and cell-death readouts that would separate them.

---

## 7. Corrections, with exact file and line coordinates

**W7-C1 — `DL-THER-089` should carry the schedule risk, which is new and specific.**
- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · `DL-THER-089` begins **line 2331**; the
  *"Cosa è A51"* bullet is **line 2334**; the BLOCK-1 bullet follows the panel table.
- **Issue:** the BLOCK-1 bullet frames the untested window as **dose**. This census shows the class separates
  benefit from harm along **duration**, and that A51 was given on the regimen the literature flags.
- **Proposed addition:** `🔴 **AGGIORNAMENTO 2026-09-21 — la finestra non è solo di DOSE, è di DURATA, e lo schema usato è quello segnalato come dannoso.** In zebrafish larvale, l'inibizione **continua** di CDK9 produce *"developmental and injury-associated adverse effects, **including reduced cardiomyocyte number expansion**"*, mentre un **impulso di 2 ore** *"avoid[s] all adverse effects"* (`PMID 34523672`, letto integralmente). Gli autori nominano la causa strutturale: *"The majority of CDK9 inhibitors act by competitively inhibiting the ATP-binding domain, **which is conserved between all CDKs**"*. **A51 negli organoidi è stato somministrato in continuo dalla settimana 8 alla 15 — sette settimane.** ⇒ la caduta di SOX2⁺ da ≈60 % a ≈33 % **non è distinguibile, con i dati pubblicati, da un effetto antiproliferativo**, e mancano sia un indice di proliferazione sia un readout di morte cellulare. **La durata è una variabile mai testata in nessun sistema WWOX.**`

**W7-C2 — the CDK9 class should be registered, with the seizure DLT attached.**
- **File:** `disease-models/wwox/analysis/mechanism_intervention_map.md` · §5 (negative translation) or as a new
  `R-` record — **placement is the map owner's call, not mine.**
- **Proposed content:** a class entry for **selective CDK9 inhibition** recording: the procurable agents
  (AT7519, AZD4573, LDC000067, JSH-009); that **CDK7 sparing is not established for any of them at abstract
  level**; that the **only CNS-exposed member is multi-CDK** (zotiraciclib) with *"low single agent clinical
  activity"* and **a grade 3 seizure among its two DLTs**; and the **developmental anti-proliferative signal**
  from `PMID 34523672`. **Class verdict: `TRANSFER_HYPOTHESIS` at best, and the seizure DLT must travel with it
  wherever it is cited.**

**W7-C3 — `E-10`'s comparator design can absorb the new arm at no cost.**
- **File:** `disease-models/wwox/analysis/mechanism_intervention_map.md` · `DECISIVE_PRECLINICAL_EXPERIMENTS`,
  row **`E-10`** (*"Nuclear β-catenin state first, then XAV939 vs CHIR99021 on organoid cortical layering"*)
- **Proposed:** extend `E-10` to carry the **AT7519 arm** and the **continuous-versus-pulsed axis**, since the
  organoid platform, the β-catenin readout and the layering endpoints are already specified there. **This makes
  `E-10` the single experiment that settles `TX-004` rather than two separate ones.**

**W7-C4 — a transferable method worth importing.**
- **File:** `disease-models/wwox/research/discovery_ledger_current.md` · a new `DL-METH-` entry
- **Content:** the **`cdk9` knockout selectivity assay** — treat a homozygous knockout of the nominal target with
  the candidate inhibitor and read a health surrogate; any effect is off-target. The authors generalise it
  explicitly. 🔴 **LEGEND has no in-system selectivity control of any kind for any candidate compound**, and this
  is the cheapest one in the literature.

---

## 8. Source attribution

Retrieved from **PubMed / PubMed Central**. DOIs are taken from the authoritative `identifiers.doi` field of
in-act `get_article_metadata` / `get_full_text_article` responses — **none reconstructed**.

| PMID | Citation | DOI |
|---|---|---|
| **34523672** | Kaveh A *et al.* Selective Cdk9 inhibition resolves neutrophilic inflammation and enhances cardiac regeneration in larval zebrafish. *Development* 2021 · **read in full in-act** | [10.1242/dev.199636](https://doi.org/10.1242/dev.199636) |
| **38159337** | Le Rhun E *et al.* Zotiraciclib (TG02) for newly diagnosed glioblastoma in the elderly or for recurrent glioblastoma: the EORTC 1608 STEAM trial. *Eur J Cancer* 2023 | [10.1016/j.ejca.2023.113475](https://doi.org/10.1016/j.ejca.2023.113475) |
| 38658199 | **Corrigendum** to the above. *Eur J Cancer* 2024 — ⚠️ **not read** | [10.1016/j.ejca.2024.114066](https://doi.org/10.1016/j.ejca.2024.114066) |
| 31699827 | Cidado J *et al.* AZD4573 Is a Highly Selective CDK9 Inhibitor That Suppresses MCL-1 and Induces Apoptosis in Hematologic Cancer Cells. *Clin Cancer Res* 2019 | [10.1158/1078-0432.CCR-19-1853](https://doi.org/10.1158/1078-0432.CCR-19-1853) |
| 33306391 | Barlaam B *et al.* Discovery of AZD4573… *J Med Chem* 2020 | [10.1021/acs.jmedchem.0c01754](https://doi.org/10.1021/acs.jmedchem.0c01754) |
| 31892980 | Shen S *et al.* Aberrant CDK9 expression within chordoma tissues and the therapeutic potential of a selective CDK9 inhibitor LDC000067. *J Cancer* 2020 | [10.7150/jca.35426](https://doi.org/10.7150/jca.35426) |
| 31872348 | Wang L *et al.* Discovery of a novel and highly selective CDK9 kinase inhibitor (JSH-009)… *Invest New Drugs* 2019 | [10.1007/s10637-019-00868-3](https://doi.org/10.1007/s10637-019-00868-3) |
| 38689623 | Lucke-Wold B *et al.* Focus on current and emerging treatment options for glioma: a comprehensive review. *World J Clin Oncol* 2024 | [10.5306/wjco.v15.i4.482](https://doi.org/10.5306/wjco.v15.i4.482) |
| 40665325 | Ball BJ *et al.* Phase I first-in-human dose escalation study of BTX A51… *J Hematol Oncol* 2025 | [10.1186/s13045-025-01724-z](https://doi.org/10.1186/s13045-025-01724-z) |
| 42397075 | Steinberg DJ *et al.* Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026 | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |

---

**End.** Not medical advice. No safety triage was run and no druggability score assigned. Read-only toward every
canonical file; nothing promoted, nothing committed.
