# Overclaim Closure, the Frozen Negative, Three Protocol Seeds, and the Revival-Trigger Ledger

**Four closures over the existing portfolio.** No molecule is added, none is proposed, and no
canonical file is edited. The routable candidates are the seven `CC-20260826-*` objects in
`../research/commit_candidates/`; this file carries the work that does not belong inside them.

> **Status:** non-canonical analysis artefact. **READ-ONLY toward every canonical file.**
> **Nothing here is medical advice, and no clinical recommendation is made or withdrawn.**

---

## 1 · PHASE 3 — `therapy_levers.md`: eight overclaims, classified, with minimum edits

`therapy_levers.md` carries **eight of the twelve** overclaims found across the therapeutic surfaces.
It is the most reader-facing document in the chain and the furthest from the locators, which is
almost certainly why.

| # | Location | Current text | Class | Minimum edit |
|---|---|---|---|---|
| **O-1** | Practical priority **2** | *"lithium as a preclinically-grounded **disease modifier** (GSK3β)"* | 🔴 `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` | *"lithium — a general anticonvulsant with a WWOX-adjacent mechanistic rationale **that has not been demonstrated**; **no developmental endpoint has ever been measured under lithium in any WWOX system**"* |
| **O-2** | **A2** | *"GSK3β is **elevated** in cortex, hippocampus and cerebellum"* | `UNMEASURED_TARGET_DIRECTION` | *"GSK3β **Ser9 phosphorylation falls** in cortex, hippocampus and cerebellum — a **densitometry with no statistical test reported**; neither cited source claims elevated abundance"* |
| **O-3** | **A2** | *"the **strongest repurposing signal**"* | 🔴 `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` | delete the superlative. *"a real anticonvulsant effect, **not WWOX-specific**: it suppressed seizures in **all three genotypes including wild type**, in an assay that detected genotype specificity for ethosuximide in the same figure"* |
| **O-4** | **C2** heading | *"**Proof** that restoring WWOX **reverses the phenotype**"* | 🔴 `GLOBAL_RESCUE` | *"WWOX re-expression **corrects several cellular and electrophysiological readouts** in WOREE-derived organoids. The rescue is **ubiquitous, supraphysiological and partial**, and no developmental or cognitive endpoint was measured"* |
| **O-5** | **C1** | *"rescued Wwox-null mouse phenotypes — epilepsy, **hypomyelination**, lethality"* | `GLOBAL_RESCUE` *(ignores a non-rescued endpoint)* | *"…improved survival and epileptiform activity, and **partially** restored myelination — on the one panel where treated animals are compared with wild type, the comparison is **significant against the rescue**"* |
| **O-6** | line 12 | *"…all **time-dependent** processes where **early intervention protects development**"* | 🔴 `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` | *"…all time-dependent processes. ⚠️ **That early intervention protects development has not been demonstrated for any WWOX intervention** — see `CLAIM 031`, where cognitive impairment precedes the epilepsy and does not improve when seizures are controlled"* |
| **O-7** | Practical priority **4** | *"AAV9-WWOX gene therapy (**already effective in mouse**)"* | `GLOBAL_RESCUE` | *"AAV9-WWOX gene therapy — effective in mouse **on survival, spike-wave discharges and gliosis, at high dose, in the P0–P5 window**; cognition and developmental trajectory were not measured"* |
| **O-8** | **B1** | *"WWOX loss **activates** GSK3β"* stated as fact | `UNMEASURED_TARGET_DIRECTION` | *"WWOX loss is **associated with reduced GSK3β Ser9 phosphorylation**, read as activation by the authors. ⚠️ `CLAIM 035` holds the WWOX brake to be **S9-independent** and predicts that a pS9 western returns a false negative — the two readings **exclude each other** on this axis"* |

**Class totals for this file:** `SYMPTOM_CONTROL_AS_DISEASE_MODIFICATION` **3** (O-1, O-3, O-6) ·
`GLOBAL_RESCUE` **3** (O-4, O-5, O-7) · `UNMEASURED_TARGET_DIRECTION` **2** (O-2, O-8) ·
`TRANSFERRED_AS_DIRECT` **0** *(the one instance of that class, O-11, is in the map's `R-01`, not
here)* · `OTHER` **0**.

### 1.1 The two that most deserve the scrutiny they were asked to get

🔴 **O-1 — *"disease modifier"*, in a section headed *"for clinical discussion"*.** This is the
sharpest overclaim in the portfolio and the classification is not close. Lithium was tested on **one
endpoint, once, acutely, as a pre-treatment within one hour of PTZ**, in **all three genotypes**,
with **zero** developmental endpoints — and the authors write that whether lithium rescues the
developmental deficits *"remains to be studied"*. *Disease modifier* asserts the exact proposition
`CLAIM 031` denies (`T1`, human, direct) and `N-15` forbids. Its placement under *"for clinical
discussion"* is what makes it worth fixing first: it is the sentence most likely to be carried out of
the repository by a reader who reads nothing else.

⚠️ **O-4 — *"Proof"*.** The word appears once in the therapeutic chain and it appears here. The
underlying result is real and useful; the noun is not available for it. The paper registry's own
record already calls the same rescue *"ubiquitario, sovrafisiologico e **parziale**"* — the
correction is therefore not new evidence but **propagation of a bound that already exists one layer
down**.

### 1.2 What is correctly bounded in the same file, reported so the sweep is not one-sided

| Location | Why it passes |
|---|---|
| **A1** vigabatrin | *"Symptomatic, **does not modify WWOX**; the most solid 'buy-time' base"* |
| **B4** Zfra | *"evidence is Alzheimer/cancer, **none in epilepsy/WOREE**. Experimental, indirect"* |
| **C3** splice-switching ASO | *"an ASO **does not repair the sequence** and cannot recreate an abolished acceptor site"*, with the Milasen precedent explicitly labelled **regulatory, not proof of amenability** |
| Header | *"**Not medical advice** — every molecule named must be evaluated solely by a treating clinical team"*, and *"Preclinical evidence does not guarantee human efficacy or safety"* |
| Line 10 | *"**No WWOX-specific clinical trial exists**… No approved therapy for WOREE"* |

**None of the eight edits adds, removes or reorders a molecule. None changes a clinical
recommendation, because the file makes none.**

---

## 2 · PHASE 7 — the disease-modification negative, stress-tested and frozen

The negative was re-attacked rather than re-stated. **Three adversarial moves**, each designed to
*find* a counterexample rather than confirm the null.

| Move | Change from the previous sweep | Result |
|---|---|---|
| **1** | **drop the improvement-verb requirement entirely** — any developmental/cognitive endpoint co-occurring with any intervention, regardless of outcome | **137 co-occurrences across 18 files**, against 15 before |
| **2** | widen the window from ±300 to **±600 characters** | included in the above |
| **3** | add assay-name probes absent from the first lexicon — `three-chamber`, `T-maze`, `radial arm`, `puzzle box`, `social interaction`, `habituation`, `operant` | no new file surfaced by these tokens |

Move 1 surfaced **seven files the earlier sweep never reached**, including `working_model_current.md`,
`clinical_monitoring_endpoints_current.md`, the dose-study dossier and the lithium paper's
supplementary. **Every one was read.**

### 2.1 The near-miss, named — because the next sweep will hit it too

🔴 **The dose study's own text contains the word *"learning"*.**

> *"Treated KO mice exhibited significantly higher motor coordination and **learning** compared with
> WT mice (Figure 4K)"*

**It is not a counterexample, and the paper itself says why.** Figure 4K is the **rotarod**
(latency to fall), so the "learning" is **motor learning across trials**. The same paragraph's
concluding sentence enumerates the battery:

> *"…neurobehavioral and motor outcomes indistinguishable from those of WT controls, encompassing
> **locomotor activity, anxiety-related behavior, and motor coordination**"*

— three domains, **none cognitive**. ⇒ the negative survives, and it now survives **against a named
near-miss rather than against silence**, which is a stronger position than the one it held before.

**Other candidates examined and rejected as counterexamples:** `clinical_monitoring_endpoints_current.md`
lists Bayley and Vineland as **endpoints that ought to be collected**, prospectively, for monitoring —
not results under an intervention. `working_model_current.md`'s hit is `CLAIM 031` itself plus
`CLAIM 039`. `PMID25012504.md` uses *"developmental trajectory"* in a **relevance-scoring** section.
`PMID42128308.json`'s hit is the word **"Milestones"** in a figure title — a historical timeline of
WWOX research.

### 2.2 The frozen negative

> ## `DISEASE_MODIFICATION_EVIDENCE_STATUS: ABSENT ON THE EXAMINED CORPUS — FROZEN`
>
> **Corpus:** 210 files — 133 `disease-models/wwox/**/*.md`, 64 deepdive manifests, 10 top-level
> `files/fulltext/` artefacts, enumerated with `Path.glob` **before** any pattern ran.
> **Interventions included:** 27 named agents/modalities plus the generic tokens `treated`,
> `treatment`, `rescue`.
> **Endpoints searched:** 24 cognitive/developmental terms and assay names.
> **Positive controls:** survival **68** triples / 22 files · motor **12** triples / 4 files — the
> instrument finds rescued endpoints that exist.
> **Exclusion rules:** `IQ`/`DQ` word-boundary anchored (unanchored, `IQ` fires inside
> *ub**iq**uitination*); developmental improvement **inferred from** seizure improvement does not
> count; growth and metabolic endpoints (weight, glucose) are not developmental endpoints.
>
> **Result: 0 counterexamples.** Across the corpus there is **no record of any WWOX intervention —
> pharmacological, dietary, genetic or gene-addition — for which a seizure or electrographic
> endpoint improved AND a developmental or cognitive endpoint independently improved.**
>
> ⚠️ **Bounded, and not universal.** No external search was authorized this session; **356 catalogued
> `CORPUS` records are unread**; the negative is a statement about **what this repository can
> currently support**, and nothing beyond it. It must not be carried out of the corpus that produced
> it.

---

## 3 · PHASE 8 — three protocol seeds

Written as arms and endpoints, not as narrative. Each states what a null buys.

### `E-1` — occlusion + memantine dose–response

| | |
|---|---|
| **MINIMAL_ARMS** | vehicle · **sub-maximal d-APV** (concentration taken from the memantine dose–response, **not** the maximal 50 µM) · memantine ≥4 concentrations · carbenoxolone 100 µM · **sub-maximal d-APV + CBX co-application** · selective connexin blocker (or Cx36/Cx43 genetic arm) · BB-FCF **powered and tested**. `Wwox` S-KO neocortical slices P13–P17; **isogenic parental and W-AAV-rescue lines** as internal comparators in the organoid/MEA replicate |
| **PRIMARY_ENDPOINT** | normalized burst frequency; secondary duration, amplitude, phase–amplitude coupling. **Washout reported for every arm** |
| **MECHANISTIC_ENDPOINT** | the **occlusion term** — co-application vs CBX alone |
| **POSITIVE_PATTERN** | CBX reduces bursting **further** in the presence of sub-maximal d-APV ⇒ gap junctions are independent. Memantine dose-dependent ⇒ the clinical compound reproduces the tool |
| **NULL_PATTERN** | no further reduction ⇒ the gap-junction node **collapses into NMDAR**; memantine flat ⇒ `R-02` does not advance and the T1 conjunction stays with a tool compound |
| **CONFOUND** | 🔴 **d-APV at full block drives frequency to zero — no headroom for occlusion.** Sub-maximal dosing is not an optimisation, it is the precondition for the experiment being able to fail. Second: the **~1.85× washout overshoot** must be reported per arm. Third: slice-to-slice variance at n≈10 |
| **DECISION_CONSEQUENCE** | settles `CC-20260826-NMDAR-CONJUNCTION-01`, `CC-20260826-GAPJUNCTION-ATTRIBUTION-01` and `CC-20260826-PANNEXIN-N16-01` **in one preparation** |

### `E-2` — gramicidin perforated-patch `E_GABA`

| | |
|---|---|
| **MINIMAL_ARMS** | WWOX-KO · **isogenic parental** · W-AAV-rescued KO · **and a developmental series** across ≥3 timepoints anchored to a **measured maturation landmark**, not to days in culture |
| **PRIMARY_ENDPOINT** | **`E_GABA` by gramicidin perforated patch** — the recording that does not dialyse intracellular chloride, which whole-cell destroys |
| **MECHANISTIC_ENDPOINT** | NKCC1 and KCC2 **protein** (not transcript); direction of the GABA response; **sIPSC amplitude in the same cells** |
| **POSITIVE_PATTERN** | `E_GABA` depolarized vs parental, NKCC1/KCC2 shifted immature, rescued by W-AAV ⇒ the `M3` axis moves **T6 → T2** and bumetanide becomes **rankable** |
| **NULL_PATTERN** | 🔴 `E_GABA` indistinguishable from parental ⇒ **the chloride axis closes** and bumetanide moves from *unrankable* to *closed*. *"Depolarizing GABA"* is a **hypothesis** in this repository — the published organoid work measures GABAergic markers, receptor components and hyperexcitability, **not** chloride reversal — and a null removes it |
| **CONFOUND** | 🔴 **cell composition** — an organoid with declared regionalization defects is not composition-matched to its control, so a population-level difference may be *which cells were recorded*. Mitigate with cell-type-resolved recording. Second: the chloride switch is itself developmental, so **one timepoint cannot distinguish *inverted* from *delayed***. Third: `MARKER_TO_FUNCTION_GATE` — NKCC1/KCC2 abundance is **not** `E_GABA` |
| **DECISION_CONSEQUENCE** | **converts an axis or closes one.** The only seed here whose null is as decision-relevant as its positive |
| **HOW IT SEPARATES POLARITY FROM AMPLITUDE** | `E_GABA` is indifferent to amplitude; sIPSC amplitude is indifferent to reversal. **Run both in the same cells:** depolarized `E_GABA` + preserved amplitude = chloride defect · normal `E_GABA` + reduced amplitude = synaptic/receptor defect · both = two lesions, not one |

### `E-3` — delayed dosing with a seizure-matched ASM comparator

| | |
|---|---|
| **MINIMAL_ARMS** | AAV9-hSynI-WWOX at **three timepoints** (P0–P5 · post-onset early · post-onset late) · AAV9-hSynI-GFP at each · untreated hypomorph · wild type · 🔴 **ASM titrated to equivalent SWD suppression** · **vehicle-ASM**. Model: a **hypomorph** (`Wwox^gt/gt` or `Wwox^P47T`, >1 year), **not** the systemic null, which dies before any learning assay and is metabolically decompensated in the only window it offers |
| **PRIMARY_ENDPOINT** | a **cognitive/learning** measure — pre-specified, blinded, powered. **Not rotarod:** rotarod latency is motor learning and is the exact conflation this design exists to break |
| **MECHANISTIC_ENDPOINT** | regional WWOX protein (cortex · hippocampus · midbrain · **cerebellum**) · SWD burden · **myelin quantified with the WT-vs-treated bracket drawn** · sIPSC amplitude in L2/3 pyramidal neurons |
| **POSITIVE_PATTERN** | cognitive endpoint improves in the gene-therapy arms and **not** in the seizure-matched ASM arm ⇒ **disease-modifying**. This is the only result in the whole package that would license that word for anything |
| **NULL_PATTERN** | both arms suppress SWD equally, **neither** moves cognition ⇒ gene addition past the window is **symptomatic**, and `N-15` extends from symptomatic levers **to the causal lever itself** |
| **CONFOUND** | 🔴 **matching SWD is not matching seizure burden** — SWD is an electrographic surrogate; arms matched on it may differ in behavioural seizures, sleep architecture or subclinical burden. And **ASMs have direct cognitive effects of their own, in both directions**, which is a second uncontrolled variable — hence the vehicle-ASM arm and a cognitive-side-effect readout. Second: **a hypomorph is not a null**. Third: timepoints anchored to a measured landmark or the "window" is a species artefact |
| **DECISION_CONSEQUENCE** | the only seed that addresses the empty column the whole portfolio is ranked on. **Run after `E-1` and `E-2`, whose results define its arms** |

---

## 4 · PHASE 9 — the revival-trigger ledger

**A negative without a revival trigger becomes permanent dogma.** Coverage measured over the full
candidate population.

**Population: 25** — 9 promoted (`R-01`…`R-09`) + 15 negative (`N-01`…`N-15`) + `N-16`.

| Where the trigger lives | Count | Which |
|---|---|---|
| Second-pass §6 tables | **20** | all 9 `R` · `N-01` · `N-03` · `N-07`…`N-14` · `N-16` |
| The candidate's own map block only | **4** | `N-02` · `N-04` · `N-05` · `N-06` |
| **Nowhere under its own name** | **1** | 🔴 **`N-15`** |

**Plus seven new triggers written into the `CC-20260826-*` objects**, one per candidate, so each
routable candidate carries its own reopening condition rather than inheriting one.

### 4.1 The single gap, and it is the one that matters

**`N-15` — *"counting seizure control as developmental protection"*** — the map's own *"most
consequential negative in the whole portfolio"* — carries **no `REVIVAL_TRIGGER` in its map block**
and appears **nowhere** in the second pass's revival-trigger tables, though it is named five times
elsewhere in that file.

**The condition exists; it is filed under a different object.** Second-pass §6 item 19, written for
`R-01-B`: *"Any endpoint in the `DEVELOPMENTAL_TRAJECTORY` or `COGNITION` column, in any WWOX model,
under any intervention, **with a seizure-matched comparator arm**."*

⇒ **a filing defect with the failure mode of one.** A reader consulting `N-15` — the negative most
likely to be quoted downstream, because it constrains every other candidate — finds a closed door,
and the key is under `R-01-B`.

**Proposed minimum edit**, `CHANGE_CLASS: MINOR`:

> **`N-15` `REVIVAL_TRIGGER`:** *Reopen if any WWOX intervention reports an endpoint in the
> `DEVELOPMENTAL_TRAJECTORY` or `COGNITION` column that improves **with a seizure-matched comparator
> arm holding seizure burden constant** — the design of `E-3`. Absent that arm, a cognitive
> improvement alongside a seizure improvement is **not** evidence against `N-15`, and this trigger
> is not satisfied by it. Cross-referenced to `R-01-B` and `E-3`.*

### 4.2 Coverage after the proposed edit

> ### `REVIVAL_TRIGGER_COVERAGE: 25 / 25` once the `N-15` edit lands · **24 / 25 today**

---

## 5 · Corrections against my own prior files

| # | Where | What I wrote | What re-derivation shows |
|---|---|---|---|
| **1** | `therapeutic_repair_candidates.md` §3 · `therapeutic_canonical_repair_package.md` §4 | **MOTOR = `RESCUE` at HD**, on S4A's `ns` against wild type | 🔴 **Incomplete, in the direction favourable to the therapy.** `fulltext_dossiers/PMID42422765_partial_locators.md` — on my own branch, unconsulted — records that Figure 4 draws the **WT-vs-treated comparison in all eight panels**, that **three are significant**, and that in all three the treated animals **exceed** wild type (velocity ≈9.5→≈11.5 · distance ≈3 400→≈4 300 · rotarod ≈85 s→≈145 s), unadjusted across eight comparisons. **A significant difference from wild type is not normalisation, and its direction does not change that.** MOTOR → **`PARTIAL / NOT_NORMALISED`**; the `RESCUE` count falls from **4 to 3**. Carried into `CC-20260826-AAV9-ENDPOINT-SPLIT-01` |
| **2** | `therapeutic_repair_candidates.md` §2 | *"Cheng's westerns are taken at **P20**"* | The paper does not settle it: Methods say **P14**, the Fig. 7c legend says **P20**, Fig. 6a says *"P14 **or** 20"*. Verified in the JATS. The `CLAIM 036` confounder **holds under either reading**, so the argument no longer depends on a date I asserted |
| **3** | `PILOT_PMID32000863…SCIB_v1` §3.4 *(my own prior adjudication)* | het *"sits at or above `+/+` in every one of the three regions"* | **0.1 too strong in two of three** (hippocampus 3.5 vs 3.6; cortex 3.8 vs 3.9). The correct statement — **the heterozygote is indistinguishable from wild type and is not intermediate** — is unaffected and is the decisive one |
| **4** | `therapeutic_canonical_repair_package.md` §7 | overclaim patterns summed **3+1+4+4** with one item double-counted, and *"nine in `therapy_levers.md`"* | Corrected in place to **3+1+5+3 = 12** and **eight** in `therapy_levers.md` |
| **5** | `therapeutic_repair_candidates.md` §3 | cerebellar argument citing `CLAIM 039`'s rat penetrance | Corrected in the prior session: `CLAIM 039` is the **rat** model and its own title ends *"and it is **not cerebellar**"*. The argument holds **inside the mouse**, where the lesion is locatored |

---

**Layer discipline.** This file modified no canonical file, promoted no hypothesis, named no new
molecule, formulated no clinical indication, dose, schedule or sequence of care, and designed no
sequence or construct. Every count states its population and can be re-run. Every molecule named
anywhere in this chain is **material for discussion with a treating clinical team**, and nothing here
substitutes for one. **Not medical advice.**
