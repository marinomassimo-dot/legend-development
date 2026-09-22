# There is no non-monotonicity to explain. The real anomaly is an effect-size mismatch

**Date:** 2026-09-22 · **Actor:** Orchestrator, from Scientist U's regional census
**Epistemic tag:** 🟡 `IPOTESI` for §3. §1 and §2 are repository facts, verified here.
**Not medical advice. No dose recommendation for any human or animal.**

🔴 **Provenance ceiling, stated first.** `files/` is gitignored and **absent from this worktree**, and
sequence/publisher egress is **403 at CONNECT**. So **every panel number below is a REPO ATTESTATION**
inherited from a prior actor's read — *not* first-hand in this session. The strongest backing is
`FTR-20260814-42422765-06`, a **`complete_fulltext_read` with `supplementary: read`**. Nothing here is
laundered as a fresh measurement.

---

## 0 · 🔴 PREMISE CORRECTION — the question this node was dispatched to answer was already retired

**Written after Scientist T returned, against the rest of this file, which was drafted before it.**

The apparent dose inversion — Fig 2's `8E10` arm described as *"rescue of lethality"* while Fig 3's
larger `1.23E11` LD produced only a modest extension ending in total mortality — **is a follow-up
artefact, and this repository adjudicated it at pixel level on 2026-08-26.**

`CC-20260826-DOSE-ADJUDICATION-01` § 6, verbatim heading: *"a second finding: Obeid 2026 contains an
apparent internal dose inversion, **and it is a follow-up artifact**."* **Figure 2B's x-axis ends at
50 days.** The `8E10` arm is flat at 100% to ~31 d. At 31 d the LD arm is still substantially alive,
so on Fig 2's axis LD would read as "rescued" too. *"Rescue of lethality"* means **alive at ~31 days**
in Fig 2 and **alive at 300 days** in Fig 3 — **one word, two windows, `NOMENCLATURE_CONFLICT`.**

> 🔴 **Three consequences, and the first is mine.**
> 1. **My `tx007_dose_unit_forensics_20260922.md` § 8 listed the Fig 2 horizon as unverified**, and I
>    reported to the Operator that non-monotonicity *"survives the audit"* with follow-up-horizon
>    mismatch as the *leading alternative*. **The repository already held the resolved answer, with a
>    reproducible crop recipe, for four weeks.** Same defect class as this session's `O-4` and S8
>    episodes: **a later node re-opened as unknown a question the repository had closed.**
> 2. **The LD → HD step is MONOTONIC.** There is no dose inversion between the two arms of Fig 3.
> 3. **The horizon-mismatch alternative is DEAD for LD vs HD** — they are two arms of one
>    Kaplan–Meier panel, and **the LD curve reaches 0%, which censoring makes impossible**, so the arm
>    is fully observed. Corroborated in running text: *"LD-treated mice did not survive to P90."*

**Cheap remedy, adopted:** before declaring any figure-level question open, **search the commit-
candidate queue for that figure number.** The answer may already be there at higher resolution.

---

## 1 · A panel conflation inside LEGEND — `DL-MECH-009` attributes S3E's numbers to S3F's variable

The four values **3.0 / 3.0 / 5.5 / 16.7** (cortex / hippocampus / midbrain / cerebellum) appear twice
in this repository, cited to the **same panel, S3E**, with **mutually exclusive** attributions:

| locus | says the 3–16.7× is… | arms it names |
|---|---|---|
| `discovery_ledger_current.md` `DL-MECH-009` | the **WPRE** effect — *"la rimozione del WPRE riduce l'espressione"* | +WPRE vs −WPRE |
| `CC-20260826-DOSE-DECISION-TABLE-01.md` § 4 | the **DOSE** effect, *"densitometry relative to the `4 × 10¹⁰` WPRE-free arm"* | `4E10` **WPRE-free** → `8E10` **WPRE-free** |

**The candidate's reading is internally consistent and the ledger's is not**, on the candidate's own
evidence: it keeps **S3E** and **S3F** as *different panels answering different questions* —

- **S3E** = the **dose** pair, both arms labelled WPRE-free → `3.0 / 3.0 / 5.5 / 16.7`
- **S3F** = the **WPRE** pair, `KO+W-WPRE (6E10 vg)` vs `KO+W (2.63E11 vg)` → an implied **≈44×
  dose-equivalence for one cassette element**

`DL-MECH-009` takes S3E's numbers and assigns them S3F's variable. Independently, Scientist U derived
WPRE multipliers from **Fig 2E** as **3.8×–24×, cerebellum highest** — a *different panel* with a
similar shape, which is exactly how two cerebellum-highest results get conflated.

> 🔴 **Prohibition, effective now: `3–16.7×` must NOT be cited as a WPRE effect** — not in
> `DL-MECH-009`, and not in `paper_registry_current.md`'s PAPER 011 note, which carries the same
> attribution (*"WPRE aumenta WWOX 3–16.7×/regione"*).
> **One read of the S3E caption in `mmc1.pdf` closes this.** It requires a worktree with `files/`.

⚠️ I cannot fully confirm from here. What I can say is that the two readings are incompatible, that
the candidate's is the better-provenanced and the self-consistent one, and that the ledger's is the
one that should not be relied on until the caption is read.

## 2 · What the dose reading implies — a steep limb, then a plateau

| step | dose pair | fold dose | cerebellar WWOX protein | source |
|---|---|---|---|---|
| **low regime** | `4E10` → `8E10` | **2.0×** | 🟢 **16.7×** — the **most** responsive region | S3E (per § 1's reading) |
| **high regime** | `1.23E11` → `2.63E11` | **2.14×** | 🔴 **no increase**; HD's lowest lane (`0.2`) sits **below** LD's lowest (`0.5`) | Fig 5L lanes, LD `0.7/0.5/0.7` vs HD `0.7/0.5/0.2` |

Same gene, same vector, same cassette, same region, **two nearly identical fold-dose steps** —
separated only by where they sit on the absolute axis. ⚠️ **This is NOT a non-monotonicity** (§ 0);
both steps are non-decreasing. It is a **steep limb followed by a plateau**.

🎯 **And Scientist T supplies the plateau independently, from the Methods.** Across the LD → HD step
the authors' own words for the expression difference are *"statistical significance in the
hippocampus"* — **1 of 4 regions** — **no stated significance on mRNA**, and **"a trend toward"** on
protein. Meanwhile **survival differs categorically**.

> 🔴 **THAT is the real anomaly, and it is sharper than the one we were sent to explain:
> survival changes categorically across a dose step that barely changes protein.**

**And the regional context makes it sharper.** Cerebellar WWOX protein sits at **0.1×–1.4× WT** in
every WPRE-free arm, dose and timepoint, while at P300 the forebrain/midbrain reach **cortex 8.2×,
hippocampus 10.7×, midbrain 5.6×, cerebellum 1.4×** (S5J).

🎯 **And it is not a delivery failure.** Cerebellar transduction is **not** deficient — S3C gives
cerebellum ≈**61% NeuN⁺WWOX⁺, the highest of three regions** (cortex ≈53%, hippocampus ≈52%); the 2021
paper gives cerebellum ≈57% vs cortex ≈61.5%, hippocampus ≈70.5%. **The neurons are reached.**

## 3 · 🟡 `IPOTESI` — the response saturates, and the two figures sample opposite sides of the knee

> **The variable that differs between LD and HD beyond nominal vg may be NOTHING.** The *expression*
> dose–response may have **saturated** somewhere between `8E10` and `1.23E11` — the low-regime panel
> measures the steep limb, the high-regime panel the plateau — while **survival is governed by a
> THRESHOLD that LD fails and HD crosses.** A saturating expression curve and a step-like survival
> curve are exactly what produces T's effect-size mismatch.

If so, the effect-size mismatch is **not an artefact and not a confound** — it is a **ceiling**,
and the cerebellum reaches its ceiling **lowest and earliest** (plateauing near 1× WT while forebrain
climbs to 5–11×). That would make the cerebellum the region where *more capsids buy least*, which is
precisely the therapeutically load-bearing fact for an ataxic disease.

**Standing alternatives, updated after T.** ~~follow-up-horizon mismatch between arms~~ — **DEAD**
(§ 0.3). Still live: **vector-prep identity** (see § 7 — it could account for all of it); survivor
selection at P300; per-cell output versus per-tissue vDNA load (≈9–12× below cortex); an **unmeasured
wild-type denominator**; and the **maternal metabolic confound** of § 7.

### What would test it, cheapest first

1. **Read the S3E caption** — resolves § 1 and tells us whether the low-regime point exists at all.
2. **An intermediate dose arm**, specified as a **fraction of HD, never in absolute vg** — the absolute
   axis is uncertain by exactly 2×, which does not touch the ratio but **does move where the knee
   sits**. *(Per `CC-20260922-CLAIM011-DOSE-ENDPOINTS-01`.)*
3. **Per-region % transduced at LD and HD.** 🔴 **Never measured** — S3C exists only in the `4E10`
   WPRE arm, and Fig 5 is tissue-level, so it cannot separate *more cells* from *more protein per
   cell*. This is the single measurement that would decide between saturation and coverage.
4. **Purkinje cells resolved.** 🔴 The cerebellum is treated throughout as **one homogenised
   compartment** — Purkinje cells are **never resolved**, so no cerebellar number here describes them.

## 4 · 🔴 The weakest link in the regional argument, named rather than buried

The P30 forebrain-versus-cerebellum contrast **rests on the hippocampal blot alone** — cortex and
midbrain individual lane values at P30 (Fig 5I, 5K) were **never recorded by anyone**. And that blot
is the one whose **KO lane reads `1.1`** — wild-type intensity **in a null animal** — where the other
three regions' KO lanes read **0.02–0.08**.

> **A null animal cannot express wild-type levels of the deleted protein.** That lane is a loading,
> normalisation, labelling or specificity failure, and until it is explained **the P30 contrast should
> carry a QC flag**, not a conclusion. Recovering Fig 5I/5K lane values is a ~5-minute task **for an
> actor whose worktree has `files/`**.

## 5 · Also resolved: the WPRE "contradiction" was a scope error, not a contradiction

The primary's Discussion states verbatim *"we removed WPRE as a proactive risk-mitigation step"*, and
its Methods map the arms: *"Constructs driven by EF1α, CMV, and MBP included WPRE, whereas the
hSynI-driven vector was generated both with and without WPRE."*

So the review describes the **final construct**; the supplement describes the **arm run to justify
removing it**. They are not in conflict. 🟢 **Consequence that matters: Figs 3–7 — dose, survival,
behaviour, all regional expression, myelin and ECoG — are WPRE-free on both sides and are therefore
NOT confounded by WPRE.** `DL-MECH-009` should be downgraded from *contradiction* to *scope
difference*. **Not edited here** — it is canonical and this is a proposal.

## 6 · Region inventory — what was never assayed, which is a choice

**Not assayed for WWOX expression in the 2026 paper:** striatum, corpus callosum, anterior commissure
(⚠️ **all three ARE quantified for MBP myelin in Fig 6**, so the omission is a selection, not a tissue
limitation), thalamus, brainstem, **hypothalamus** (⚠️ notable — **hypoglycaemia is the paper's central
systemic phenotype**), olfactory bulb, amygdala.

The 2021 paper reports **no fold-of-WT value for any region by any method**, and its widely-quoted
*"60–70% transduced"* is the **envelope across cortex + hippocampus + cerebellum over two figures** —
**not a per-region value**, and it should stop being cited as one.

---

## 7 · The delivery chain, reconstructed — everything STATED is matched, everything that could carry the effect is UNSTATED

From Scientist T, which **re-acquired `PMC13343157` this session** (48,780-char body **including the
complete Materials and methods**, read verbatim — so this section is **first-hand**, unlike §§ 2–6).

### 7.1 🔴 "HD spread further" is REFUSED by the text, not merely unsupported

> Methods, verbatim: *"delivering **2.0 μL/hemisphere**"* + *"The procedure was repeated for the
> contralateral hemisphere"*, in the single paragraph covering AAV9-hWWOX delivery.

**Volume is a constant across every arm.** Therefore **HD was a more concentrated prep, not a larger
one**, and the spread-further mechanism is excluded. Derived titres — **never printed anywhere in the
paper** — are `LD 3.075E10 ‖ 6.15E10` and `HD 6.575E10 ‖ 1.315E11` vg/µL (total ‖ per-hemisphere
reading).

### 7.2 Confound verdicts

**REFUSED — stated matched:** volume · injection count · rate · needle · coordinates · route ·
anaesthesia · **WPRE (both arms −WPRE, one sentence)** · FVB strain · titration method · housing.
*(The WPRE verdict independently confirms § 5.)*

🔴 **CONFIRMED live but entirely UNSTATED — the vector-prep chain:** lot · manufacturer (four sources
named, only two constructs assigned) · **empty:full capsid ratio (0 occurrences)** · purification (0)
· formulation buffer (0) · endotoxin (0) · titration CV (0) · and **whether LD is a dilution of HD or
an independent prep**.

**Ranked for the LD → HD step:** (1) **prep identity — could account for all of it**; (2) allocation
(20:30, no randomisation, no litter structure stated); (3) censoring/harvest — direction established,
**can only compress the gap, never create it**; (4) titration error — resizes, does not reverse;
(5) age spread — small. Age is `P0–P1` **stated for all arms**; per-arm distribution **ABSENT**.
⚠️ **S8's injection-window result is HD-only and must not be transferred to LD.**

### 7.3 🔴 A maternal metabolic confound nobody has recorded

> Methods, verbatim: *"Heterozygote **or KO rescued mice (KO injected with AAV9-hSynI-hWWOX)** were
> used for breeding."*

**Some KO pups have an AAV-treated KO dam, others a Het dam, and the per-arm distribution is never
stated.** In a study whose **principal systemic endpoint is blood glucose**, maternal metabolic status
is a live confound on the headline phenotype.

### 7.4 `censor*` appears **0 times**, yet animals are harvested at P30 / 3 mo / P180 / P240 / P300

The predecessor paper carries a documented **censored-as-event** Kaplan–Meier inconsistency
(`CC-20260826` § 7), and **vehicle-injected WT+RI sits at ≈72% at 300 days** — a wild-type arm should
not lose a quarter of its animals.

🔴 **CORRECTED 2026-09-22 by Scientist A's animal-flow reconstruction. My "this likely explains it"
was too strong, and harvest-plotted-as-death is now the LESS favoured reading.** The argument needs
no new data:

- HD's curve is **flat from ~85 d to 300 d** while HD tissue was demonstrably taken **terminally** at
  ~P90/P180/P240/P300 ⇒ **harvest-as-event is refused** (each harvest would step the curve down).
- LD's curve **reaches 0%** while LD tissue was taken at P30 ⇒ **harvest-as-censored is refused**
  (a censored animal holds a KM estimate above zero permanently).

⇒ **Under a single uniform convention, the harvested animals were never in the Fig 3B denominators at
all.** Conditional on one inherited pixel attestation, and stated as conditional.

**The space is now exactly two readings**, not one:
| | reading | support |
|---|---|---|
| **R1** | the ≈72% are **real events** (~5–6 of 20) | shape-consistent with **neonatal ICV procedure attrition** — both drops early, then ~250 flat days, which is **not** an aging hazard; and favoured by the argument above |
| **R2** | an **internally inconsistent** convention | has **precedent in this very lab** (`CC-20260826` § 7) |

🎯 **And there is a free discriminator that needs no new data.** With no censoring a KM estimate can
only take **multiples of 1/n**. Verified arithmetic: `14/20 = 70%`, `15/20 = 75%` — so **≈72% is
unreachable with n = 20**; `23/30 = 76.67%`, `24/30 = 80%` — so **≈78% is unreachable with n = 30**.
**Reading either plateau against the panel's gridlines therefore tests for censoring directly.**
⚠️ Pixel-read error is a live alternative and this is recorded as a **discriminant, not a result**.

⚠️ **And the paper runs the control that would settle it** — *"WT littermates received identical
injections to control for procedural effects"* — **and never reports its survival result.**

### 7.5 🟢 `VG_DOSE_ALONE_IS_NOT_TRANSFERABLE` extends to **vg/µL**

T tested whether **concentration** is the transferable quantity: **Obeid LD exceeds Repudi 2021 on
BOTH total vg AND vg/µL, under BOTH unit readings — and performs far worse** (0% by ~80 d versus
≈93% at 270 d). **Neither total dose nor concentration transfers between these two studies.**

### 7.6 The single record that would supply the most

**The per-arm animal-flow and censoring table** — n enrolled / dead / harvested / censored by date,
litter, dam, sex, exact injection day. It **outranks the vector CoA**, because it decides whether the
survival observation is an observation at all, and *establishing a mechanism for an artefact is wasted
work*.

Second: **the CoA for LD and HD material** — which would also settle the closed unit question for
free. Required stock titres are `3.075E13`/`6.575E13` (total reading) versus
`6.15E13`/`1.315E14` vg/mL (per-hemisphere), so **a single printed stock titre fixes `u`.**
