# The smallest experiments that DECIDE the cerebellar mechanism — existing-material first

**Date:** 2026-09-22 · **Actor:** Scientist G · **Class:** experiment design + method-discipline experiment
**Canonical main at start:** `e8ed228` · **No git run. No registry, queue, ledger, receipt or canonical file touched. No `BATCH_COMMIT`.**
**Nothing here is medical advice.** Therapeutic reasoning supports discussion with a treating clinical team; it never substitutes for one.

**Builds on, and does not re-derive:** `cerebellum_layer_localisation_20260922.md` (Scientist C) ·
`purkinje_cerebellar_celltype_wwox_census_20260922.md` · `fold_of_wt_is_undefined_for_vdna_20260922.md` ·
`tx007_per_arm_delivery_reconstruction_20260922.md` · `tx007_animal_flow_survival_validity_20260922.md`.

**Provenance ceiling, declared once.** I read **no primary body in this session**. Every Methods sentence quoted below
is quoted **as the sibling files attest it, first-hand from the served 2026 and 2021 bodies** — my use of it is
**second-hand** and is marked `SIBLING-ATTESTED`. `files/` is absent in this worktree, so the 2026 supplement and every
figure caption remain `SOURCE_BLOCKED`; the standing triggers are inherited unchanged and were **not retried**.

**Prior-art sequence, run before anything below is declared new** (`FIND ISSUE → SEARCH CLAIMS → SEARCH CANDIDATES →
SEARCH DISCOVERY LEDGER`), with `git grep … HEAD` and never over my own output:
- `claim_registry_current.md` — `host reference` · `single-copy` · `genome-equivalent` · `nuclei per` · `per nucleus` → **0**
- `governance/candidates/` and `disease-models/wwox/research/commit_candidates/` → **0** for all five
- `discovery_ledger_current.md` → **0** for the normalisation terms; **4** `Purkinje` hits, all phenotype/inflammation, none a WWOX measurement
- `COMMUNITY_FOLLOWUP` → **0 occurrences repo-wide.** This file is the first instance of the artefact.
⇒ The **normalisation-arithmetic** content below is not held by any registry, candidate or ledger. It **is** partly held
by the two sibling analysis files (§ 3.2, `P4`, `P5`), and every such overlap is graded `REDISCOVERY` in § 1. That grading
is the point of the exercise, not a formality.

---

# 1 · The prospective DISCOVERY_TRACEs

🔴 **Written and persisted BEFORE any confirmatory search.** The `EX-ANTE PREDICTION` fields below were committed to
this file before a single external query was issued in this session; the `RESULT` fields were empty at that moment and
were filled afterwards. Where a prediction failed, it is left standing and marked failed rather than rewritten.

---

## TRACE 1 — Does the missing host reference amplicon matter, and what is it structurally incapable of seeing?

**OBSERVATION.**
The strongest established result in this problem — a cerebellar vector-genome deficit of ≈**9–12×** below cortex that is
already *per host nucleus* — rests on a conversion that is **arithmetic, not measured**: *"For qPCR, **50 ng of DNA
template was used per reaction**"* (`SIBLING-ATTESTED`, 2026 Methods), one primer pair, **no host reference amplicon, no
standard curve**. The step *"50 ng ⇒ a fixed number of nuclei"* is an **estimate inherited as a measurement**. At the
same time the cerebellar transduced-neuron fraction is the **highest** of three regions (≈61%) while excluding Purkinje
cells from its own denominator by reagent construction (`MAB377` = NeuN clone A60).

**DIVERGE — six mechanistically distinct ways the mass→genome-equivalent conversion can be wrong, and they are not
paraphrases of each other.**

| | Mechanism | Acts on | Region-specific? | Detectable by a host reference amplicon in the same well? |
|---|---|---|---|---|
| **D1** | **Co-purified RNA inflates the apparent DNA mass.** If concentration was read by **A260 absorbance** rather than a dsDNA-specific fluorophore, "50 ng of DNA" is *50 ng of nucleic acid*. Cerebellar granule tissue is the most rRNA-dense brain compartment per unit mass, so the inflation is **largest exactly where the deficit is reported** | the conversion factor | 🔴 **YES, and in the direction that inflates the deficit** | 🟢 **YES — exactly and completely.** The host amplicon counts genome-equivalents actually present, whatever else carries the mass |
| **D2** | **Mitochondrial DNA occupies mass without contributing a nuclear genome**, and mitochondrial content per unit tissue differs between a granule-cell compartment and a pyramidal-arbour compartment | the conversion factor | 🟡 yes, magnitude unknown *a priori* | 🟢 YES |
| **D3** | 🔴 **Differential nuclear recovery — a COMPOSITION bias, not a conversion bias.** If small heterochromatin-dense granule nuclei lyse with different efficiency from large pyramidal or glial nuclei, then the nuclei **represented** in the recovered DNA do not match the tissue. The mass→genome conversion stays perfect; the *population* shifts | **which cells** the genome-equivalents came from | 🔴 YES | 🔴 **NO — STRUCTURALLY BLIND.** A host amplicon measures genome-equivalents present, not their cell-type provenance |
| **D4** | **PCR inhibitor carryover** (myelin lipid; haem, since RNA at least came from *"non-perfused tissue"*) suppresses the vector amplicon region-specifically | amplification efficiency | 🔴 YES | 🟢 **YES — this is precisely what an internal amplification control is for** |
| **D5** | **Ploidy / aneuploidy differences** between regions change DNA mass per nucleus | the conversion factor | 🟡 in principle | 🟢 YES |
| **D6** | **Cell-size scaling of per-nucleus vector load** — the carried `P5`: no cerebellum-specific biology at all, a size rule plus a compartment where the small-cell type dominates the nuclear count | the biology of layer 2 | ⛔ not a bias — a real effect | 🔴 NO |

**CONNECT — which outside domains supply the magnitudes and the instruments.**
- **Clinical AAV biodistribution and its regulatory practice.** The unit of record in that tradition is **vector genomes
  per diploid genome (`vg/dg`)**, and it is *enforced* by a **single-copy host autosomal amplicon multiplexed in the same
  reaction** — canonically `Tfrc` in mouse. The control this assay lacks is not an exotic refinement; it is the field's
  default unit definition. **This is the cross-domain import that reframes the question.**
- **Forensic quantitative genomics.** The `pg-per-diploid-genome` conversion and its failure modes are a *solved*
  problem there: modern forensic quantitation kits multiplex an **internal PCR control** and a **degradation-index
  target** precisely because mass is an unreliable proxy for amplifiable genome-equivalents.
- **Mitochondrial genetics.** mtDNA copy number is *routinely* assayed as an **mtDNA : nuclear-single-copy ratio** — the
  tradition that supplies `D2`'s magnitude, and it supplies it as an arithmetic bound rather than a measurement.
- **Stereology / isotropic fractionator (cell-number cytometry).** The tradition that measures **nuclei per unit tissue
  by region** — the only instrument that could ever have answered "does nuclei-per-ng differ by region", and the one
  whose logic shows why that question **does not enter a fixed-DNA-mass assay at all**.
- **Nucleic-acid quantitation instrumentation.** The named instrument, **DeNovix DS-11FX+**, is a **combined
  spectrophotometer *and* fluorometer** — so the Methods sentence naming it **does not decide** whether `D1` is live.

**HYPOTHESIS.**
> Every mechanism that a host reference amplicon *can* see (`D1`, `D2`, `D4`, `D5`) is **bounded to a small integer
> factor**, so the host reference **refines and cannot reverse** the cerebellar deficit. The mechanism that could carry
> a 9–12× effect on the measurement side is `D3`, and the host reference is **structurally blind to it**. ⇒ The host
> reference is the right first experiment, but for a **different reason than the repository holds**: not because it might
> overturn the number, but because it **partitions** the deficit into a normalisation component it can measure and a
> composition component it provably cannot — and that partition is what licenses the calbindin experiment as the only
> remaining route.

**EX-ANTE PREDICTIONS — committed before searching.**
- **P-a.** mtDNA contributes **< 3%** of total DNA mass in brain tissue, so `D2` cannot shift the ratio by more than a
  few percent. Pre-computed here, not searched: mouse mtDNA ≈ `1.63E4` bp; mouse diploid nuclear ≈ `5.4E9` bp; at even
  `5E3` mtDNA copies per cell the mass share is `1.63E4 × 5E3 / 5.4E9` ≈ **1.5%**.
- **P-b.** `D1` (RNA carryover) is the **largest** of the conversion terms, and whether it is live turns on a fact the
  Methods **do not state**: absorbance versus fluorimetric quantitation, and whether an **RNase A** step exists. I
  predict the held Methods quote **cannot** decide it, because the sentence carries an ellipsis exactly where an RNase
  step would sit.
- **P-c.** Nuclei **per mg of tissue** differ between mouse cerebellum and cortex by a **large factor (> 5×)** — and
  this is a **prediction that the quantity is IRRELEVANT here**, because DNA mass per diploid nucleus is a
  species-constant. ⇒ The "cerebellum is cell-dense" escape is closed for a **second, independent** reason, and
  Scientist C's § 3.2a conclusion is right **for the right reason**.
- **P-d.** A single-copy host amplicon in the same wells will shift the cerebellum/cortex ratio by **less than 3×** and
  will **not abolish** it. The deficit survives.
- **P-e.** If `D3` is real, **DNA yield per mg of tissue** will diverge between regions — and the host amplicon will
  read **normal anyway**, because it measures genome-equivalents present, not their provenance. ⇒ 🔴 **A host amplicon
  that leaves the ratio unchanged does NOT kill the denominator hypothesis.**
- **P-f.** `vg/dg` with a single-copy host reference is **standard practice** in AAV biodistribution, so this is a
  `CROSS-DOMAIN-DERIVED` import and **not** an agent-novel idea.

**DISCRIMINATOR.** One plate on the archived DNA, four readouts: **(i)** the existing vector amplicon; **(ii)** a
**single-copy autosomal host amplicon** in the same well; **(iii)** an **mtDNA** amplicon, to measure `D2` instead of
bounding it; **(iv)** a **plasmid standard curve**, to put both on an absolute `vg/dg` axis. Plus, off-plate,
**fluorimetric re-quantitation** of the same archived DNA against the recorded A260 value — which measures `D1`
retrospectively — and **DNA yield per mg of input tissue** per region, which is the only cheap handle on `D3`.

**RESULT.** `PENDING — filled after searching; see § 1.3.`

**EXPERIMENT (smallest, highest information gain for this trace).** The four-readout plate above. It is one primer pair
beyond what the laboratory already runs, on samples the Methods imply exist, and it retro-fits **every published vDNA
number in this literature** onto the field's standard unit.

**NOVELTY ORIGIN.**
- *"The assay has no host reference amplicon and the input is fixed mass"* → 🔴 **REDISCOVERY.** Held first-hand in
  `cerebellum_layer_localisation_20260922.md` § 3.2 and as hypothesis `P4`.
- *"'50 ng ⇒ per nucleus' is estimated, never measured"* → 🔴 **REDISCOVERY.** Held as `P4`, and the brief says so.
- *"Run a single-copy host amplicon on the archived DNA"* → 🔴 **REDISCOVERY.** Named as `P4`'s cheapest discriminator.
- *The arithmetic bounding of each conversion term* (`D1`, `D2`, `D5` given magnitudes rather than listed) → 🟢
  **AGENT-NOVEL.** `P4` names mtDNA and lysis as mechanisms and asserts without arithmetic that they are *"not plausible"*
  at 9–12×; no file in this repository bounds them.
- *`D3` is a composition bias and the host amplicon is structurally blind to it* → 🟢 **AGENT-NOVEL**, and it is a
  **correction to `P4`'s own distinctness table**, which records that `P4` *"DIES if a host reference amplicon leaves the
  ratio unchanged"*. That is true for `P4`'s mechanism (b) and **false for its mechanism (a)**. FLAGGED in § 2.4.
- *`D1` / A260-versus-fluorimetric and the DS-11FX+ dual-mode point* → 🟢 **AGENT-NOVEL**, and `CROSS-DOMAIN-DERIVED`
  from nucleic-acid quantitation practice.
- *`vg/dg` as the field's standard unit* → 🔵 **CROSS-DOMAIN-DERIVED.**
- *`D6`* → 🔴 **REDISCOVERY** (`P5`, carried verbatim in substance).

**CANONICAL STATUS.** 🔴 **`HYPOTHESIS ONLY`** for every mechanism `D1`–`D6`. The arithmetic bounds in `P-a` and `P-c`
are **`DERIVED`** from species constants and are not claims about this paper. **Nothing here is a `CANDIDATE` and
nothing is `CANONICAL`.** No registry was touched.

---

## TRACE 2 — Why are Purkinje cells vulnerable, and what single existing-material measurement splits the classes?

**OBSERVATION.**
Three facts sit together and are jointly strange. **(1)** The cerebellum has the **highest** transduced-neuron fraction
of three regions (≈61%) and the **lowest** genome load (≈9–12× below cortex), which forces **7–14× fewer genomes per
transduced cell** — positivity is a threshold, load is a quantity. **(2)** That ≈61% **cannot include a single Purkinje
cell**, because `MAB377` is NeuN clone A60. **(3)** In the one WWOX model where cerebellar cell types *were* resolved
with a Purkinje marker — `Wwox^P47T/P47T`, calbindin, `n = 3` — **total protein level is normal and Purkinje cells are
lost anyway** (median ≈82 → ≈25 at 80 d; ≈100 → ≈42 at 250 d; basket cells `ns` at both ages).

🔴 **The one legitimate framing of that third datum, and it is not widened here.** The permitted statement is **only**:
*for at least one WWOX missense model, normal total protein abundance is insufficient to preserve Purkinje cells.* It is
**not** evidence that abundance rescue never works — that would transfer across **allele** (`P47T` ≠ null), **mechanism**
(`P47T` abolishes PPxY binding at normal abundance; a null has no protein at all), **species**, and
**number-versus-function**. Four independent firewalls, any one of which breaks the transfer. The ≈25 → ≈42 rise is
**survivor selection** on the 250-day cohort and must never be read as recovery.

**DIVERGE — eight classes, kept as classes and not resolved.** Full specification, predictions and discriminators in § 4.
`C1` insufficient vector delivery to Purkinje cells · `C2` insufficient WWOX **per** Purkinje cell at adequate delivery ·
`C3` developmental timing — the Purkinje window closes before P0–P5 · `C4` cell-autonomous functional requirement ·
`C5` non-cell-autonomous support (Bergmann glia, granule-cell trophic input, climbing-fibre drive) · `C6` **function
rather than abundance** · `C7` regional metabolic vulnerability · `C8` circuit/network effect.

**CONNECT.**
- **Cerebellar developmental neuroanatomy.** Purkinje cells are born prenatally (≈E11–E13 in mouse) and are
  post-mitotic long before P0, whereas granule precursors proliferate in the external granular layer through ≈P21. That
  single asymmetry is what makes `C1`, `C3` and `D6`/`P5` *predict opposite things about the same cell* — Purkinje cells
  should be **good** episomal carriers (no mitotic dilution, large soma) and **bad** rescue targets (window already shut).
- **The `WW`-domain / `PPxY` interaction tradition.** `P47T` abolishes PPxY binding at normal protein level — so `C6`
  has a *specific*, falsifiable form: Purkinje cells depend on a PPxY-ligand partner more than granule cells do.
- **Selective neuronal vulnerability in the ataxias (SCA/ARSACS/Npc1 traditions).** Purkinje cells are the field's
  canonical metabolically-exposed neuron — huge dendritic arbour, high tonic firing rate, high per-cell ATP and
  calcium-buffering demand. That tradition supplies `C7`'s mechanism and its standard readouts.
- **Gene-therapy cell-type targeting.** Promoter and capsid engineering for Purkinje cells is an established sub-field
  (`Pcp2`/`L7` promoters; capsids selected for cerebellar tropism) — the tradition that makes the therapeutic
  consequence of `C1` versus `C6` **actionable rather than academic**.
- **Conditional-allele genetics.** A `Wwox` floxed exon-1 allele **exists**, and its own makers named the missing
  cerebellar/cell-type Cre cross in print in 2020. That is the only route to **necessity** rather than presence.

**HYPOTHESIS.**
> 🎯 **A "scissors" hypothesis, and it is the reason to run one stain rather than four.** Two independent systems are
> about to converge on the same partition. In `Wwox^P47T/P47T`, **abundance is normal and Purkinje cells die** — so
> abundance is not sufficient *in that allele*. If, in the AAV-treated null, Purkinje cells turn out to be **well
> supplied** with WWOX and are **still** lost, then abundance is not the limiting variable **in the null either**, and
> the therapeutic target moves from *delivery* to *function*. If instead Purkinje cells turn out to be **unsupplied**,
> then delivery **is** the limiting step for the cell type the ataxia phenotype is about, and the target is capsid,
> promoter or route. **The same single measurement returns whichever answer is true, and the two answers redirect the
> programme in opposite directions.** No published measurement can currently tell them apart.

**EX-ANTE PREDICTIONS — committed before searching.**
- **P-g.** No published WWOX measurement exists in a Purkinje cell in **any** WWOX-deficient or AAV-treated system, in
  any species. (Inherited as `PREMISE: NOBODY_LOOKED`; I predict the searches confirm it and add nothing.)
- **P-h.** Purkinje cells are **post-mitotic before birth** in mouse, whereas granule precursors divide postnatally ⇒
  `C1` and `D6`/`P5` predict Purkinje cells are **good** carriers; only an **arrival-geometry** account (`P3`) predicts
  them poor. So the stain discriminates *arrival* from *cell-size* directly.
- **P-i.** An `AAV9-hSynI-EGFP` reporter **exists in both papers** — `SIBLING-ATTESTED` 2026 Methods, and the 2021
  control virus. But I predict its **dose and arm do not match LD/HD**, so a reporter answer is a **promoter-layer**
  answer and **not** a delivery-at-therapeutic-dose answer. That bound must travel with it.
- **P-j.** `C7` (metabolic vulnerability) and `C4` (cell-autonomous requirement) are **NOT DISCRIMINABLE** by any
  existing-material experiment, because both predict identical per-cell WWOX distributions. They require the
  conditional allele, i.e. a new cohort. I predict no existing material separates them, and I will say so rather than
  invent a cheap proxy.
- **P-k.** Whole-slide scanning (*"imaged using a 3DHISTECH panoramic scanner"*, `SIBLING-ATTESTED`) means the **entire**
  sagittal section is in the archived image file at scanner resolution, **including the cerebellum and including the
  Purkinje cell layer, whether or not the authors analysed it** ⇒ a **layer-resolved cerebellar WWOX intensity
  distribution already exists as unanalysed data**. I predict this is true and that it is the cheapest class in the
  whole problem — `NEW ANALYSIS ONLY`.

**DISCRIMINATOR.** **Calbindin + WWOX double-label on existing perfused sections**, reporting the **full per-cell
intensity distribution** for Purkinje versus granule cells **in the same field**, with the **positive fraction reported
separately from the intensity**, plus the **calbindin count** in treated-KO / untreated-KO / WT. One antibody. Existing
material. Opposite predictions from two live hypotheses.

**RESULT.** `PENDING — filled after searching; see § 1.3.`

**EXPERIMENT.** As the discriminator; specified in full, with its channel chemistry and its bounds, in § 5.

**NOVELTY ORIGIN.**
- The **eight classes** → 🔴 **PROMPT-SEEDED.** The brief enumerates them; I specified them, I did not find them.
- The **SCAR12 framing and its four firewalls** → 🔴 **PROMPT-SEEDED** (the brief supplies the permitted statement and
  the prohibition) and 🔴 **REDISCOVERY** (the census § 4.3 holds the same three boundaries).
- *"Calbindin + WWOX on existing sections"* → 🔴 **REDISCOVERY.** Named as the cheapest discriminator of `H6` and `P5`
  in both sibling files.
- *"The ≈61% excludes Purkinje cells by reagent construction"* → 🔴 **REDISCOVERY** (§ 6.2) and **PROMPT-SEEDED**.
- 🟢 **AGENT-NOVEL — the "scissors":** that `P47T`-normal-abundance-with-loss and an AAV-treated-null Purkinje
  measurement are **two independent routes to the same partition**, so one stain converts a single-allele observation
  into a cross-allele inference *without* the abundance-transfer the brief forbids. No sibling file joins these two.
- 🟢 **AGENT-NOVEL — `P-k`:** that a *panoramic whole-slide scan* makes a layer-resolved cerebellar WWOX distribution
  an already-existing, never-analysed dataset. The siblings treat the cerebellar cell-type gap as needing a new stain;
  `NEW ANALYSIS ONLY` is a strictly cheaper class and no file names it.
- 🟢 **AGENT-NOVEL — the co-product argument:** the calbindin channel yields **Purkinje number in treated KO**, which is
  `NOT ASSAYED` and is the missing arm of the scissors, at **zero marginal cost** on the same section.
- 🔵 **CROSS-DOMAIN-DERIVED** — `C7` from the selective-vulnerability ataxia tradition; `C6`'s specific PPxY form from the
  WW-domain interaction tradition; the channel chemistry (mouse anti-calbindin freeing the rabbit channel) from
  routine multiplex-IF practice.
- 🔴 **REDISCOVERY** — `C3` is sibling `H7`; `C1` is sibling `P1`/`P3`; `C2` is the `V ≈ F × C` arithmetic already held;
  `C6` is `CLAIM 030`'s standing position that severity tracks residual **function**, not abundance.

**CANONICAL STATUS.** 🔴 **`HYPOTHESIS ONLY`** for `C1`–`C8` and for the scissors. `NOT ASSAYED` is recorded throughout
as neither `NORMAL` nor `ABSENT`. **Not a `CANDIDATE`, not `CANONICAL`.** The closed dose non-monotonicity premise is
**not reopened**, including from expression data.

---

## 1.3 · RESULT fields — filled after searching, with the failures left standing

**Surface used:** `Scholar_Gateway semanticSearch`, four queries, all returning passages with full metadata. **Every quotation
below is FIRST-HAND from the returned passage text.** 🔴 The gateway's `ai_generated` summary is **not** evidence and was
not used; the passage text is. ⚠️ Passage retrieval is **not** a whole-body fetch and **not** a read — none of these
papers is claimed as read, none is a receipt, and none is a `CANDIDATE`.

| Prediction | `RESULT` | What decided it |
|---|---|---|
| **P-a** mtDNA < 3% of DNA mass | 🟢 **SUPPORTED, and by a wider margin than predicted** | Lichter *et al.* 2023, *Advanced Biology* 7(8), [DOI](https://doi.org/10.1002/adbi.202300154), Methods, verbatim: *"in a given DNA sample from tissues, the fraction of mtDNA was approximately **only 0.1%**"*. My pre-computed bound was `< 3%`; the measured value is **~0.1%**, i.e. **30× tighter** |
| **P-a**, regional refinement I did **not** predict | 🟡 **A regional mtDNA difference EXISTS and runs in the deficit-inflating direction — and is three orders of magnitude too small to matter** | Clay, Daws & Konradi 2010, *Int J Dev Neurosci* 29(3):311–324, [DOI](https://doi.org/10.1016/j.ijdevneu.2010.08.007), verbatim: *"The spinal cord, striatum, and cortex have mtDNA copy numbers of **10,000 or more per cell**, the medulla possesses roughly 8000 copies per cell, and the **midbrain and cerebellum each have 4000 copies or less** per cell"*; and *"The volume fraction of mitochondria in neurons was found to be **lowest in cerebellar granule cells**, which correlates with the observed lower cerebellar mtDNA copy number"*. ⇒ **Arithmetic:** cerebellum carries **less** non-nuclear mass, so 50 ng of cerebellar DNA holds **slightly more** true genome-equivalents ⇒ the true cerebellar `vg/dg` is **marginally lower** than the mass-based estimate ⇒ the deficit is **inflated, by ≈0.06 percentage points**. **`D2` is dead on magnitude, and its direction is now known rather than guessed** |
| **P-b** the Methods cannot decide absorbance-vs-fluorimetric, and `D1` is the largest conversion term | 🟢 **SUPPORTED on both halves — and the field's correction is named explicitly** | Rasmussen, Daenzer & Fridovich-Keil 2020, *J Inherit Metab Dis* 44(1):272–281, [DOI](https://doi.org/10.1002/jimd.12311) — **a neonatal AAV9 rodent brain gene-replacement study**, Methods, verbatim: *"Of the two biological replicates, **one was treated with RNase during isolation, the other was not**"* and *"Initial DNA concentration readings were **measured by nanodrop, and final values were normalized to DNA concentrations measured by Qubit**"*. ⇒ RNase carryover and absorbance-versus-fluorimetric are **named, routinely-controlled variables in exactly this experiment type**, not an invented concern. 🔴 The 2026 Methods quote held by the repository carries an **ellipsis** precisely where an RNase step would sit (*"lysed in ATL buffer **…** DNA integrity and concentration were assessed"*) and names an instrument, the **DeNovix DS-11FX+**, that is **both** a spectrophotometer and a fluorometer ⇒ `NOT READABLE` from any surface this repository holds |
| **P-c** neurons per unit mass differ hugely by region, **and it is irrelevant to a fixed-DNA-mass assay** | 🟢 **SUPPORTED** | Herculano-Houzel *et al.* 2020, *J Comp Neurol* 528(17):2978–2993, [DOI](https://doi.org/10.1002/cne.24985), verbatim: *"all species retain a relative distribution of **10–25% of all neurons in the cerebral cortex, and 75–85% of neurons are found in the cerebellum**—regardless of the absolute or relative mass of these structures"*. ⇒ Nuclei-per-mg **does** differ enormously. ⇒ And it **does not enter** the assay, because DNA mass per diploid nucleus is a species-constant: the conversion `50 ng ÷ ~6 pg` is blind to how many nuclei a **milligram of tissue** held. 🎯 **Scientist C's § 3.2a is right, and now for a measured reason rather than an asserted one** |
| **P-d** a host amplicon shifts the ratio by < 3× and does not abolish it | 🟡 **NOT TESTED — untestable without running the experiment.** Left standing as the trace's central falsifiable prediction. The *bounds* on its components are now measured (`D2` ≈ 0.1%, `D5` ≈ 0.03% by arithmetic below), so only `D1` and `D4` remain unbounded, and both are of the size a nanodrop-to-Qubit correction absorbs | — |
| **P-e** a null host-amplicon result does **not** kill the denominator hypothesis | 🟢 **SUPPORTED by construction**, and it **corrects a sibling file** — see § 2.4 | Entailment, not a search result: an amplicon that counts genome-equivalents *present* cannot report their cell-type *provenance* |
| **P-f** `vg/dg` with a single-copy host reference is field-standard ⇒ `CROSS-DOMAIN-DERIVED`, not agent-novel | 🟢 **SUPPORTED — and it forces an honest downgrade of my own framing** | Sun & Liao 2022, *J Clin Pharmacol* 62(S2):S79–S94, [DOI](https://doi.org/10.1002/jcph.2141), verbatim: *"The concentration unit is typically **vector genome per microgram (VG/µg) total DNA** or **vg per diploid genome (vg/dg)** in solid tissues"*. 🔴 **Both are standard.** ⇒ The 2026 assay's fixed-mass design is **one of the two field-standard units**, not a deviation. Ai *et al.* 2017, *The Prostate* 77(12):1265–1270, [DOI](https://doi.org/10.1002/pros.23386), verbatim: *"targeting EGFP … and **the reference gene transferrin receptor (Tfrc)** … genome copy numbers per diploid genome were calculated through **dividing EGFP transgene copy numbers by two times of Tfrc gene copies**"* — the exact design proposed, already routine |
| **P-g** no WWOX measurement exists in a Purkinje cell in any WWOX-deficient or treated system | 🟢 **SUPPORTED — nothing found, and nothing added.** Inherited, unchanged | — |
| **P-h** Purkinje cells post-mitotic before birth; granule precursors divide postnatally | 🟢 **SUPPORTED, first-hand, in mouse** | Inouye & Murakami 1980, *J Comp Neurol* 194(3):499–503, [DOI](https://doi.org/10.1002/cne.901940302), verbatim: *"the majority of the Purkinje cell population was formed on **day 12 of gestation** and a few on day 13"*. Beierbach *et al.* 2001, *J Comp Neurol* 436(1):42–51, [DOI](https://doi.org/10.1002/cne.1052), verbatim: *"Mouse Purkinje cells are born in the ventricular zone of the fourth ventricle **between E11 and E13**"*. Weyer & Schilling 2003, *J Neurosci Res* 73(3):400–409, [DOI](https://doi.org/10.1002/jnr.10655), verbatim: *"cerebellar Purkinje cells are derived from precursors that undergo their **last mitosis in the ventricular zone** and migrate outward **postmitotically**"* … granule precursors *"**continue to divide until about postnatal Day 14**"*. 🎯 ⇒ The `PREMISE: DEFAULT_FROM_TEXTBOOK` behind sibling `H2`/`P2` is now **sourced in mouse**, and the asymmetry it needs is **first-hand** |
| **P-i** an `AAV9-hSynI-EGFP` reporter exists but at a non-matching dose/arm | 🟡 **HALF SUPPORTED, half `NOT ESTABLISHED`** | Existence is `SIBLING-ATTESTED` first-hand from 2026 Methods (*"Custom-made AAV9-CBA-hWWOX and **AAV9-hSynI-EGFP** viral particles were obtained from the Vector ELSC Core Facility"*) and the 2021 control virus. 🔴 **Whether EGFP animals were injected, perfused and sectioned in the 2026 study is `NOT STATED` on any surface this repository holds** — the sentence records *procurement*, not an arm. Dose and arm assignment: `ABSENT` |
| **P-j** `C4` and `C7` are not separable on existing material | 🟢 **SUPPORTED** — stated as a limit in § 4, not worked around with a proxy | — |
| **P-k** whole-slide scanning makes a layer-resolved cerebellar WWOX distribution already-existing unanalysed data | 🟢 **SUPPORTED on the instrument; conditional on coverage** | `SIBLING-ATTESTED` 2026 Methods: *"Sagittal brain sections (14 μm) … imaged using a **3DHISTECH panoramic scanner**"* — a whole-slide scanner digitises the entire section, so cerebellum and the Purkinje cell layer are inside the file whether or not they were analysed. 🔴 **Bound:** whether such scans exist **for the LD and HD arms** is `NOT STATED`; the one cerebellar transduced-fraction figure sits in the **`4E10` +WPRE** arm (S3C) |

### 1.4 🔴 An unpredicted find, flagged and not acted on — it STRENGTHENS and NARROWS a held repository position

The `P-h` search returned a paper the repository does not hold, and it speaks directly to the clone-A60 finding **in the
right species**.

**Weyer & Schilling 2003**, *Developmental and cell type-specific expression of the neuronal marker NeuN in the murine
cerebellum*, *J Neurosci Res* 73(3):400–409, [DOI](https://doi.org/10.1002/jnr.10655). Abstract, **verbatim**:

> "expression of this antigen in the cerebellum was **restricted to granule neurons and a small population of cells
> present in the lower molecular layer** of the adult cerebellum … In contrast to postmitotic granule neurons, **NeuN was
> not expressed by any other immunocytochemically identified cerebellar interneurons, which comprised basket and stellate
> cells, Golgi neurons, unipolar brush cells, and Lugaro cells.**"

| | Repository's held position (sibling § 6.2) | What this adds |
|---|---|---|
| Species of the supporting source | `PMID 17291468`, **abstract depth**, general/rat framing | 🟢 **Mouse**, and the 2026 model is mouse |
| What the cerebellar `%NeuN⁺WWOX⁺` denominator contains | *"granule cells, **molecular-layer and Golgi interneurons**, and **deep-nuclei neurons**"* | 🔴 **NARROWER.** Basket, stellate, Golgi, unipolar brush and Lugaro cells are **explicitly NeuN-negative** in murine cerebellum ⇒ the denominator is **essentially pure granule neurons**, plus an unidentified small molecular-layer population |

🎯 **Consequence, and it cuts both ways.** The ≈**61%** is an even **more granule-specific** number than the repository
records — which **strengthens** the sibling conclusion that *"the average cerebellar nucleus … is the average granule-cell
nucleus"* — and it **narrows** the repository's own enumeration of what that denominator covers. ⚠️ **Bounds, stated:**
**(a)** the passage names *"NeuN"* and **not the clone**; that it is `MAB377`/A60 is an `INFERENZA` from the antigen's
origin, strong but unread; **(b)** **deep cerebellar nuclei are not addressed** in the passage I read, so their NeuN status
stays `NOT ESTABLISHED` here; **(c)** this is a returned passage, **not a read body**, and carries no receipt.
🔴 **FLAGGED, NOT EDITED.** No registry, ledger, receipt or candidate was touched. `REVIVAL_TRIGGER` in § 7.

**Also returned, and it puts a number on a repository premise that was carrying none.** Andersen, Gundersen & Pakkenberg
2003, *J Comp Neurol* 466(3):356–365, [DOI](https://doi.org/10.1002/cne.10884), verbatim: *"the global cell density for
**Purkinje cells was 0.75 × 10³ mm⁻³**"* and *"the global cell density for **granule cells was 2,880 × 10³ mm⁻³**"*
⇒ ≈**3,840 : 1** by density. ⚠️ **Human, adult, stereological, neurons only** — it does **not** transfer to mouse and is
**not** a nuclear-fraction (glia are outside it). Recorded only because the repository's *"orders of magnitude"* statement
was `PREMISE: DEFAULT_FROM_TEXTBOOK` with no figure attached, and now has one, with its species firewall.

---

# 2 · QUESTION 1 — the qPCR denominator verdict

# 🎯 **`HOST REFERENCE WOULD REFINE`**

**Not** `CURRENT NORMALIZATION ADEQUATE`, because the conversion is unvalidated in two named, live ways and the panel's
absolute axis is unrecoverable. **Not** `HOST REFERENCE COULD CHANGE CONCLUSION`, because every mechanism a host
reference can see is now **arithmetically bounded far below** the 9–12× it would need to overturn. **Not** `UNRESOLVED`,
because the bounding is decidable from species constants plus two measured literature values and does not need the paper.

## 2.1 · The evaluation, term by term, as the brief requires

| Term | Status | Magnitude it can contribute to the **cerebellum/cortex vDNA ratio** | Visible to a host reference? |
|---|---|---|---|
| **DNA input mass** | *"50 ng of DNA template was used per reaction"* — a **fixed mass**, and `VG/µg total DNA` is one of the **two field-standard units** (Sun & Liao 2022) | Pipetting/quantitation error only. **Unbounded in principle, small in practice, and uncontrolled here** — there is no internal check that 50 ng was loaded **or amplifiable** | 🟢 **YES — this is the primary thing it buys** |
| **Ploidy assumptions** | Mouse brain nuclei are overwhelmingly diploid; the one candidate polyploid cerebellar type is the Purkinje cell | 🔴 **Negligible by arithmetic.** Even granting Purkinje tetraploidy outright, Purkinje cells are ≈**1 : 3,840** of cerebellar neurons by density (Andersen 2003, human) ⇒ a doubling of their DNA shifts total cerebellar DNA mass by ≈**0.03%** | 🟢 YES, and it has nothing to see |
| **Extraction quality / yield differences between regions** | 🔴 **`NOT STATED`.** *"DNA integrity and concentration were assessed … by using DeNovix (DS-11FX+)"* — an instrument that is **both** spectrophotometer and fluorometer; **which mode** is `NOT READABLE`. **No RNase step is visible**, but the held quote's **ellipsis sits exactly where one would be**, so this is `NOT READABLE`, **not a validated zero** | 🟡 **THE LARGEST CONVERSION TERM, and the only one left unbounded.** RNA carryover inflates apparent DNA mass most where rRNA density is highest, i.e. the granule-dense cerebellum ⇒ **inflates the deficit**. The field's own correction is explicit (nanodrop → Qubit; ±RNase replicates — Rasmussen 2020). Plausible scale: **a small integer factor**, not an order of magnitude | 🟢 **YES — completely.** A host amplicon counts genome-equivalents regardless of what carries the mass |
| **Genomic-equivalent normalisation** | 🔴 **ABSENT.** No host amplicon, no standard curve ⇒ no `vg/dg` axis, and the Fig 5A–5D caption *"normalized to WT levels"* is **undefined** for vDNA because `RI` is the **vehicle** (*"KO mice injected with the reference item (RI)"*, PBS/5% sorbitol/0.001% pluronic F-68) and **no vector-injected WT arm exists** | Removes the **absolute** axis entirely. **Within-panel regional ratios survive** | 🟢 **YES — this is what it restores** |
| **Choice of host reference gene** | Not a live risk. `Tfrc` is the routine single-copy autosomal choice (Ai 2017). Any single-copy autosomal locus **not inside a known copy-number-variable or fragile region** serves | 🟡 One caution specific to this gene family: **avoid a reference inside a common fragile site.** `WWOX` itself spans `FRA16D` — so the reference must be chosen away from fragile-site loci, which is a one-line design constraint, not an obstacle | — |
| **Regional composition differences — does nuclei-per-ng differ by region?** | 🎯 **NO, and this is the decisive line.** **Nuclei per *milligram of tissue* differs enormously** (75–85% of all brain neurons sit in cerebellum regardless of mass; Herculano-Houzel 2020). **Nuclei per *nanogram of DNA* does not**, because DNA mass per diploid nucleus is a species-constant. **Is it measured anywhere? 🔴 NO — not in either paper, and not for these tissues in anything I retrieved** | 🔴 **Zero, on the conversion.** But composition **does** act on the **biology** (`D3`, `D6`/`P5`): *which* nuclei the recovered DNA represents, and how vector load distributes across cell types of very different size | 🔴 **NO — STRUCTURALLY BLIND** |
| **Non-nuclear DNA (mtDNA)** | 🟢 **MEASURED AND BOUNDED.** ≈**0.1%** of tissue DNA mass (Lichter 2023); cerebellum ≈**≤4,000** copies/cell vs cortex **≥10,000** (Clay 2010) | ≈**0.06 percentage points**, in the deficit-**inflating** direction. **Three orders of magnitude too small** | 🟢 YES, and it has nothing material to see |
| **PCR inhibitor carryover** | 🔴 `NOT STATED`. RNA came from *"non-perfused tissue"*; whether DNA did is `NOT STATED` ⇒ haem and myelin lipid carryover cannot be excluded region-specifically | 🟡 Unbounded from published text, but the field's standard control is a **vector spike-in per sample** (Rasmussen 2020), which is cheap and was not run here | 🟢 **YES — an internal amplification control is exactly this** |

## 2.2 · Why the verdict is the middle class and not the strong one

> Sum of everything a host reference amplicon can see: **mtDNA ≈ 0.1% · ploidy ≈ 0.03% · loading error, RNA carryover
> and inhibitor carryover, jointly a small integer factor at the outside.** The deficit to be explained is **8.75×–12.05×**.
> **A plausible worst case removes perhaps 1.5–3× and leaves ≈3–8×.** The direction of the cerebellar conclusion does not
> move. ⇒ **`HOST REFERENCE WOULD REFINE`.**

🔴 **And the specific thing it refines is not the number — it is the number's licence.** Three defects are repaired at once
and none of them is the ratio: **(1)** the readout acquires the field's standard `vg/dg` axis, so it becomes comparable to
every other AAV study instead of to itself only; **(2)** the undefined *"fold of WT"* y-axis stops mattering, because
`vg/dg` needs **no wild-type arm** — which is the precise repair for a quantity whose WT value is **zero**; **(3)** the
per-nucleus reading stops being an inference from a fixed mass and becomes a **measurement**. 🎯 **The third is the point:
the repository's strongest cerebellar result currently cannot be cited without carrying an estimate in its denominator.**

## 2.3 · Two conditions under which the verdict would escalate — named so they are testable, not hedged

Both are `NOT READABLE`, and either, if it went the wrong way, moves the class to `HOST REFERENCE COULD CHANGE CONCLUSION`:
1. 🔴 **If the DeNovix was used in A260 mode AND no RNase step exists**, and cerebellar preps carry substantially more RNA
   than cortical ones, `D1` is no longer a small integer. **Cheapest check: re-quantify the archived DNA fluorimetrically
   and compare with the recorded value, per region.** No PCR required.
2. 🔴 **If DNA also came from non-perfused tissue**, regional inhibitor carryover is unbounded from the text. **Cheapest
   check: the spike-in control, one extra well per sample.**

## 2.4 · 🔴 FLAG — this corrects the sibling file's own distinctness table, and the correction matters

`purkinje_cerebellar_celltype_wwox_census_20260922.md` § 7.1 records that hypothesis `P4` **"DIES if a host reference
amplicon leaves the ratio unchanged"**. `P4` has two mechanisms: **(a) recovery** — *"homogenisation and lysis efficiency
is not uniform across nuclear types, so the nuclei actually represented in 50 ng need not match the tissue's nuclear
composition"* — and **(b) non-nuclear DNA**.

> 🎯 **The falsifier is valid for (b) and INVALID for (a).** A host reference amplicon counts the genome-equivalents
> **present in the well**. If granule nuclei lysed poorly, the surviving nuclei are still nuclei, the host amplicon still
> reads them correctly, and the ratio is unchanged — while the **population** the number describes has silently shifted.
> **An unchanged ratio would therefore be misread as killing `P4`(a) when it does not touch it.**

⇒ `P4`(a) is not a normalisation hypothesis at all; it is a **composition** hypothesis, and it belongs beside `P5`/`D6`
rather than beside `P4`(b). 🔴 **FLAGGED ONLY.** Prior-art sequence run (§ 0); no file edited; the sibling file is not
modified by me. **The cheap handle `P4`(a) actually needs is `DNA yield per mg of input tissue, by region`** — a number
the laboratory can read off its own extraction records without running anything.

---

# 3 · QUESTION 2 — existing-material feasibility

**Classes:** `NO NEW ANIMALS` (archived biomaterial, new bench work) · `NEW ANALYSIS ONLY` (no bench work at all) ·
`NEW STAINING` (existing sections, new reagent) · `NEW ANIMAL COHORT REQUIRED`.

**The two Methods sentences that make the whole table possible**, both `SIBLING-ATTESTED` first-hand:
> *"tissue samples (**up to 25 mg**) were lysed in ATL buffer … For qPCR, **50 ng of DNA template was used per reaction**."*
> *"Sagittal brain sections (**14 μm**) … rabbit polyclonal anti-WWOX 1:5,000 … mouse anti-NeuN, (MAB377) … imaged using a
> **3DHISTECH panoramic scanner**"*, with terminal perfusion of *"(**WT, KO, and KO injected mice**) at different ages
> (**P10-P180**)"*, and RNA taken separately from *"**non-perfused tissue**"* ⇒ **IHC animals are distinct from RNA animals,
> so perfused, sectioned tissue exists as a separate resource.**

| # | Experiment | 🎯 Class | Why the material exists — the Methods sentence that implies it | 🔴 What could break it |
|---|---|---|---|---|
| **1** | **Single-copy host-reference qPCR on existing DNA** (+ mtDNA amplicon, plasmid standard curve, spike-in, fluorimetric re-quantitation) | 🟢 **`NO NEW ANIMALS`** | *"tissue samples (up to 25 mg) were lysed in ATL buffer"* + *"50 ng of DNA template … per reaction"*. A 25 mg brain-tissue prep yields DNA in the **micrograms**; at 50 ng/reaction the published panels consumed a **small percentage** of it. ⇒ **Archived DNA in the microgram range is implied by the extraction scale itself.** The **vehicle arms (`KO+RI`, `WT+RI`) supply the matrix-matched vector-free blank** a standard curve needs — exactly the design Rasmussen 2020 used (*"standards were prepared by diluting purified AAV9-hGALT plasmid into rat genomic DNA … from PBS-injected control animals"*) | 🔴 **Archive retention is `NOT STATED`** — no biobank, storage-temperature or aliquot statement on any held surface. If the DNA is exhausted or degraded, this falls to `NEW ANIMAL COHORT REQUIRED`. **Stated as a conditional, not assumed away** |
| **2** | **Calbindin + WWOX on existing sections** | 🟡 **`NEW STAINING`** | *"Sagittal brain sections (14 μm)"* from perfused *"(WT, KO, and KO injected mice) at different ages (P10-P180)"*, already carrying **rabbit polyclonal anti-WWOX 1:5,000** as a validated channel in this exact tissue. 14 µm sagittal sections come in **series**, so unstained neighbours of already-imaged slides are the expected residue. 🎯 **Channel chemistry is free:** anti-WWOX is **rabbit**, so a **mouse monoclonal anti-calbindin** occupies the mouse channel that `MAB377` currently uses — and NeuN is not needed for this question | 🔴 The anti-WWOX polyclonal is **unidentified** (no vendor, catalogue or clone) ⇒ the intensity axis is **relative**, never absolute (magnitude-only, § 6.4 of the sibling). 🔴 Whether sections exist **for the LD and HD arms specifically** is `NOT STATED` |
| **3** | **Calbindin + reporter/EGFP on existing sections** | 🟡 **`NEW STAINING`** *(best case)* → 🔴 **`NEW ANIMAL COHORT REQUIRED`** *(if no reporter animal was sectioned)* | 🟢 **The reporter exists in BOTH papers, first-hand:** *"Custom-made AAV9-CBA-hWWOX and **AAV9-hSynI-EGFP** viral particles were obtained from the Vector ELSC Core Facility"* (2026), and **`AAV9-hSynI-EGFP` was the 2021 control virus**. EGFP is **natively fluorescent** ⇒ only calbindin needs staining, making this the cheapest possible two-channel readout | 🔴 **The 2026 sentence records PROCUREMENT, not an arm** — whether EGFP animals were injected, perfused and sectioned is `NOT STATED`. 🔴 The 2021 reporter arm is a **different study, a different vector, free-hand ~1 µL/hemisphere 33G versus stereotactic 2.0 µL 32G, and 5 years old** ⇒ **no 2021↔2026 transfer**, and tissue availability is unknown. 🔴 A reporter answers the **promoter** layer at the **reporter's** dose — **not delivery at `1.23E11`/`2.63E11`** |
| **4a** | **Region-specific protein re-analysis — re-blot archived lysates with total-protein normalisation** (Ponceau/REVERT) instead of GAPDH/HSP90 alone | 🟢 **`NO NEW ANIMALS`** | The immunoblot Methods list **two** loading controls (GAPDH CB-1001; HSP90 4874S) and *"which one normalises Fig 5 … is `NOT READABLE`"*. Lysates from the same *"up to 25 mg"* dissections are implied. One gel series retro-fits **every** fold-WT number and tests sibling `H5` directly | 🔴 Lysate retention `NOT STATED`. 🔴 Does **not** repair the missing **WT regional baseline**, which needs a recombinant-WWOX standard curve |
| **4b** | **Region-specific protein re-analysis — densitometry re-analysis of existing blot images** | 🟢 **`NEW ANALYSIS ONLY`** | *"No densitometry method"* is stated anywhere (`densitom` 0) ⇒ re-deriving band intensities from archived scans with a stated method costs nothing | 🔴 **Total-protein re-normalisation is NOT recoverable from an image** unless a Ponceau/REVERT scan was captured — usually it was not. So 4b answers *"what was the densitometry?"*, **not** `H5` |
| **5** | 🎯 **Cell-type-resolved re-quantification of existing raw images** — per-cell WWOX intensity distributions resolved by **cerebellar layer** (granular / Purkinje / molecular / deep nuclei) from the archived whole-slide scans | 🟢 **`NEW ANALYSIS ONLY` — the cheapest class in the whole problem** | 🎯 *"imaged using a **3DHISTECH panoramic scanner**"*. A panoramic scanner digitises the **entire** section at objective resolution. ⇒ **The cerebellum, its three cortical layers, and the Purkinje cell layer are already inside the archived image files — with WWOX already in one channel — whether or not the authors analysed them.** No animal, no reagent, no licence, no new bench step. **This is unanalysed data, not an unrun experiment** | 🔴 **Layer is not cell identity.** The Purkinje cell layer also holds **Bergmann glia and candelabrum interneurons**, so a marker-free layer read reproduces the known limit of the human `PMID 16941225` observation. 🔴 Requires the scans to **cover cerebellum in the arms of interest** — `NOT STATED`; S3C sits in the **`4E10` +WPRE** arm |

**Preference order among the brief's first three, on cost:** **#1** (`NO NEW ANIMALS`, one primer pair) → **#2**
(`NEW STAINING`, one antibody) → **#3** (`NEW STAINING` but with a `NOT STATED` precondition and a dose mismatch that
bounds its answer to the promoter layer). 🎯 **And #5 undercuts all three on cost** at the price of marker-free cell
identity — which is why § 5 pairs it with #2 rather than choosing between them.

---

# 4 · QUESTION 3 — the Purkinje divergent pass

**Rules honoured throughout.** Competing hypotheses are **preserved**; no winner is selected; **no numerical
probabilities**. Each class is `IPOTESI`. `NOT ASSAYED` is neither `NORMAL` nor `ABSENT`. No cross-region averaging, no
2021↔2026 transfer, survivor selection named on every P250/P300 row, doses in E-notation.

## 4.0 · The SCAR12 datum, in the one permitted framing, restated once and not widened

> **For at least one WWOX missense model, normal total protein abundance is insufficient to preserve Purkinje cells.**

`Wwox^P47T/P47T`, `PMID 36828035`, calbindin⁺ Purkinje counts in cerebellar vermis, `n = 3`/group: median ≈**82 → ≈25**
at 80 d; ≈**100 → ≈42** at 250 d; **basket cells (`Hcn1`⁺) `ns` at both ages** — a specificity control that makes the
Purkinje result mean something. ⚠️ The ≈25 → ≈42 rise is **survivor selection** on the 250-day cohort; the 80-day mutant
box's lower whisker reaches **0**. 🔴 **The statement is NOT widened to "abundance rescue never works."** Four
independent firewalls block that transfer, any one of which is sufficient: **allele** (`P47T` ≠ null), **mechanism**
(`P47T` abolishes PPxY binding *at normal abundance*; a null has no protein to bind with), **species/system**, and
**number versus function** (a cell count is not a protein measurement).

## 4.1 · Eight classes, each with an ex-ante prediction and a discriminator

| | Class | Mechanism, stated so it can be wrong | **If true, what else should we observe?** | 🎯 Discriminator | Cost class |
|---|---|---|---|---|---|
| **C1** | **Insufficient vector DELIVERY to Purkinje cells** | Purkinje somata sit deep to the molecular layer; a CSF-surface-entry gradient reaches them last and least. Delivery, not requirement, is the limiting step | Calbindin⁺ cells carry a **low or near-zero** vector/WWOX signal while granule cells in the same field do not; a **pial-inward gradient** is visible within the molecular layer; **intracisternal** delivery narrows the gap | Calbindin + WWOX (or + EGFP) with **per-cell intensity and depth position** recorded | 🟡 `NEW STAINING` |
| **C2** | **Insufficient WWOX PER Purkinje cell at adequate delivery** | Purkinje cells are transduced but each receives too few genomes to reach a functional threshold — the `V ≈ F × C` arithmetic applied to one cell type | Purkinje **positive fraction is high** while the **modal intensity is low**; the intensity distribution is **unimodal and shifted**, not bimodal; the gap **narrows with dose** between `1.23E11` and `2.63E11` | The same stain, reporting **positive fraction SEPARATELY from intensity**, at both doses. 🔴 This separation has **never been measured in any region at LD/HD** | 🟡 `NEW STAINING` |
| **C3** | **Developmental timing — the Purkinje window shut before P0** | Purkinje cells are born **E11–E13** and are post-mitotic before birth (Inouye 1980; Beierbach 2001; Weyer 2003, all first-hand passages). A P0–P5 intervention arrives after their specification and initial dendritogenesis | Cerebellar structural deficit is measurable in the untreated KO **at or before P0–P2**; treated-KO cerebellar layer thickness and Purkinje number at P30 stay below WT **even where forebrain endpoints normalise**; the cerebellar value is **flat across dose, across timepoint and across ±WPRE** — which is what the `0.1×–1.4×` pattern already looks like; **no injection age in P0–P5 narrows it** | Purkinje counts + layer thickness in **untreated KO at P0–P2** vs WT, and in **treated KO at P30**. The `S8` window arms (**D0–D5**, HD `2.63E11`, *"at least three littermates per time point"*) are an **existing** age series that was never read out on cerebellum | 🟡 `NEW STAINING` on existing S8 material; 🔴 `NEW ANIMAL COHORT` for P0–P2 |
| **C4** | **Cell-autonomous functional requirement** | A Purkinje cell needs WWOX **in itself**, for something no amount supplied elsewhere replaces | Purkinje-restricted ablation in an otherwise wild-type cerebellum **reproduces** the loss; restoring WWOX to granule cells alone does **not** rescue Purkinje number | 🎯 **`Pcp2`/`L7`-Cre × `Wwox^fl/fl`.** The floxed exon-1 allele **exists** and its own makers named this cross in print in 2020 — it has never been reported. **The only design that tests NECESSITY rather than presence** | 🔴 `NEW ANIMAL COHORT REQUIRED` |
| **C5** | **Non-cell-autonomous support fails** | Purkinje survival depends on Bergmann glia, granule-cell parallel-fibre input and climbing-fibre drive. A neuron-restricted promoter (`hSynI`) **cannot reach Bergmann glia at all**, so a glial contribution is untreatable by this vector **by construction** | Purkinje loss tracks **granule-layer or Bergmann-glia** status rather than Purkinje WWOX; a **ubiquitous** promoter (CBA) outperforms `hSynI` on cerebellar endpoints at matched dose; GFAP/Iba1 burden in cerebellum predicts Purkinje number | Glial marker + calbindin + WWOX on the **same** existing sections; and the **`A3` CBA arm at `4E10`** is an existing ubiquitous-promoter comparator. 🔴 **Bounded:** `A3`'s WPRE status and manufacturer are both `ABSENT`, so it differs from its comparators on **two unstated links** | 🟡 `NEW STAINING` |
| **C6** | 🎯 **FUNCTION rather than ABUNDANCE** | What a Purkinje cell needs is WWOX **doing something** — specifically, in the `P47T` allele, **PPxY-ligand binding through WW1**, which fails at normal protein level. Abundance is the wrong axis | Purkinje cells in the AAV-treated null are **well supplied** with WWOX and are **still lost**; the transgene's per-molecule activity, not its level, predicts the endpoint; a Purkinje-enriched PPxY-containing partner is identifiable and its loss phenocopies | 🎯 **The same stain, read jointly with the calbindin COUNT in treated KO** — see the scissors, § 5. `CLAIM 030` already holds that severity tracks **residual function, not abundance**; this is the cerebellar test of it | 🟡 `NEW STAINING` |
| **C7** | **Regional metabolic vulnerability** | Purkinje cells carry an enormous dendritic arbour, high tonic firing and correspondingly high ATP and Ca²⁺-buffering load — the canonical selectively-vulnerable neuron of the ataxia field. WWOX loss is tolerated where demand is low and not where it is high | Vulnerability rank across cell types tracks **metabolic load**, not WWOX level; other high-load neurons (deep cerebellar nuclei, spinal motor neurons) are affected before low-load ones; mitochondrial or oxidative markers diverge in Purkinje cells **before** they are lost | 🔴 **NOT DISCRIMINABLE on existing material** — `C4` and `C7` predict **identical** per-cell WWOX distributions. Needs a cell-type-resolved metabolic readout in a new cohort. **Stated as a limit; no cheap proxy invented** | 🔴 `NEW ANIMAL COHORT REQUIRED` |
| **C8** | **Circuit / network effect** | Loss is driven by aberrant activity — seizure burden, olivary drive or excitotoxic climbing-fibre input — rather than by anything local to the Purkinje cell | Purkinje loss correlates with **seizure burden** rather than with cerebellar WWOX; seizure control (or olivary silencing) spares Purkinje cells independent of WWOX; loss is **patchy by parasagittal band**, following circuit topography rather than a delivery gradient | **Spatial pattern on the existing scans** — parasagittal banding versus a smooth pial-inward gradient — is readable from archived whole-slide images at **`NEW ANALYSIS ONLY`** cost, and the two patterns are visually distinct. 🔴 The paper's ECoG is **single-channel over right dorsal cortex**, so the seizure–cerebellum correlation itself needs a new recording | 🟢 pattern: `NEW ANALYSIS ONLY`; 🔴 correlation: `NEW ANIMAL COHORT` |

### 4.2 · Distinctness check — no two classes collapse onto the same measurement

| Falsifier | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
|---|---|---|---|---|---|---|---|---|
| Dies if calbindin⁺ Purkinje WWOX is **HIGH** | 🔴 **dies** | 🔴 **dies** | no | no | no | 🟢 **confirmed** | no | no |
| Dies if calbindin⁺ Purkinje WWOX is **near-ZERO** | 🟢 confirmed | 🟡 weakened | no | no | no | 🔴 **not tested** | no | no |
| Dies if **positive fraction high but intensity low** | 🟡 weakened | 🟢 **confirmed** | no | no | no | no | no | no |
| Dies if untreated KO cerebellum is **NORMAL at P0–P2** | no | no | 🔴 **dies** | no | no | no | no | no |
| Dies if `Pcp2`-Cre ablation **fails to reproduce loss** | no | no | no | 🔴 **dies** | 🟡 supported | no | no | no |
| Dies if a **ubiquitous promoter does not outperform** `hSynI` in cerebellum | no | no | no | no | 🔴 **dies** | no | no | no |
| Dies if loss **follows a pial-inward gradient** rather than bands | 🟢 supported | no | no | no | no | no | no | 🔴 **dies** |
| Dies if vulnerability rank does **not** track metabolic load | no | no | no | no | no | no | 🔴 **dies** | no |

**Eight classes, eight distinct falsifiers.** 🔴 `C4` and `C7` share the "no" column on every existing-material row —
which is exactly `P-j`, and is why both are listed as needing a cohort rather than being folded into a cheaper proxy.

### 4.3 · What the SCAR12 datum teaches, on the three axes the brief names

| Axis | What it licenses | 🔴 What it does NOT license |
|---|---|---|
| **Function vs abundance** | That **abundance is not automatically the right endpoint** in this gene. `P47T` has normal total protein and loses Purkinje cells, so a gene-therapy programme reporting *"WWOX protein restored to X% of WT"* has **not thereby shown Purkinje protection** — the two are separate measurements and one has never been made | That abundance is **irrelevant**, or that raising abundance cannot help a **null**. A null has **no protein at all**; `P47T` has normal protein with a broken interaction. These are different starting points and the transfer fails on mechanism |
| **Cell-type vulnerability** | That Purkinje vulnerability in WWOX disease is **real, cell-type-selective and measurable**, with a `ns` interneuron control in the same sections — i.e. it is not a generalised cerebellar shrinkage | That the **same** cell type fails for the **same reason** in the null, the rat `lde/lde`, human WOREE or human SCAR12. `Wwox^P47T/P47T` ≠ `Wwox`-null ≠ `Wwox^gt/gt` ≠ rat `lde/lde` ≠ human WOREE ≠ human SCAR12; nothing transfers between those rows |
| **Gene-replacement targeting** | 🎯 **That the therapeutic question has two branches and the field has tested neither.** If Purkinje cells are **unsupplied**, the levers are **capsid, promoter and route**. If they are **well supplied and still lost**, the levers are **function-per-molecule and timing**, and more capsid is the wrong investment. 🔴 **`hSynI` cannot reach Bergmann glia at all** (`C5`), which is a targeting fact independent of how the branch resolves | Any dose, route or construct recommendation for any species. **Nothing here is medical advice** |

---

# 5 · 🎯 The single best existing-material experiment

> ## 🥇 **Calbindin + WWOX double-label on the existing perfused sections — reporting, in the SAME field: (i) the per-cell WWOX intensity DISTRIBUTION for Purkinje cells and for granule cells separately, (ii) the positive FRACTION separately from the intensity, and (iii) the calbindin COUNT in treated-KO, untreated-KO and WT.**
>
> **Cost class:** 🟡 `NEW STAINING` — **one antibody**, on material the Methods state exists, with the WWOX channel
> already validated in this exact tissue. **Channel chemistry is free:** anti-WWOX is a **rabbit** polyclonal, so a
> **mouse monoclonal anti-calbindin** takes the mouse channel `MAB377` currently occupies, and NeuN is not needed.
> **Report at both `1.23E11` and `2.63E11` if sections for both arms exist; report the arms that do exist if not.**

## 5.1 · Why it has the highest information gain — four independent reasons

**1. 🎯 It is the only experiment here whose outcome is genuinely UNPREDICTED, and that is what information gain means.**
Two live hypotheses make **opposite** predictions from the **same** section. A delivery-limited account (`C1`) predicts
calbindin⁺ cells read **near-zero**. The carried cell-size hypothesis (`P5`/`D6`) predicts Purkinje cells — among the
largest neurons in the brain, post-mitotic since **E11–E13** and therefore immune to the episomal dilution that empties
the granule lineage — read **near-cortical or higher**. 🔴 **Contrast with the host-reference qPCR (§ 2): I can already
predict its answer**, because every term it can see is bounded below the effect it would need to move. A measurement
whose result is foreseeable is a validation, not a discriminator.

**2. 🎯 It closes the gap that invalidates the single observation arguing hardest against delivery-limitation.**
The ≈**61%** cerebellar transduced fraction — the highest of three regions — **cannot contain a Purkinje cell**, because
`MAB377` is NeuN clone A60, and § 1.4 narrows that denominator further to **essentially pure granule neurons** in mouse.
Until a Purkinje-marker measurement exists, the number is not wrong; it is **inapplicable to the ataxia question**.

**3. 🎯 The calbindin channel yields a second, never-measured datum at ZERO marginal cost — and that co-product builds the scissors.**
Purkinje **number in the AAV-treated KO** is `NOT ASSAYED` by anyone. Counting it costs nothing once the channel is in
the section, and it is the missing arm of the inference:

| Purkinje WWOX in treated KO | Purkinje number in treated KO | 🎯 What it means | Where the programme goes |
|---|---|---|---|
| **HIGH** | **still reduced** | Two independent systems — `P47T` (normal abundance, cells lost) and an AAV-treated **null** — reach the same partition **by different routes**. Abundance is not the limiting variable in either | 🎯 **Function-per-molecule and timing.** More capsid is the wrong investment |
| **HIGH** | **preserved** | Delivery **and** abundance are sufficient in the null; the `P47T` loss is an **allele-specific functional lesion** and does not generalise | Protect the window; abundance rescue is on-target for the null |
| **near-ZERO** | **reduced** | 🎯 Delivery **is** the limiting step for the cell type the ataxia phenotype is about | **Capsid, promoter, route.** `hSynI` + AAV9 + ICV is the thing to change |
| **near-ZERO** | **preserved** | Purkinje cells do not need cell-autonomous WWOX at this timepoint ⇒ the deficit is **non-cell-autonomous** (`C5`) or absent | Look at Bergmann glia and granule-cell support, which `hSynI` cannot reach |

🔴 **Every one of the four cells redirects the programme, and they redirect it differently.** That is the definition of a
decisive experiment, and **no published measurement can currently distinguish any of them from any other.**
⚠️ **The inference is a CONVERGENCE, not a transfer.** It does **not** carry the `P47T` abundance conclusion across the
allele firewall — it asks the **null** the same question independently and compares the two answers afterwards.

**4. It is the cheapest thing that answers a question nobody has answered in any species.**
Per the census, **no WWOX measurement in a Purkinje cell exists in ANY WWOX-deficient or AAV-treated system**. The one
Purkinje-layer observation in the whole literature is **human, wild-type, marker-free, qualitative**, and its primary body
is licence-blocked.

## 5.2 · The two things to run beside it, and why neither displaces it

- **Run § 3 #5 FIRST, because it is free.** Re-quantifying the **existing whole-slide scans** by cerebellar layer is
  `NEW ANALYSIS ONLY` — **no animal, no reagent, no licence, no bench step**. It returns a layer-resolved WWOX
  distribution **today**, tells you immediately whether cerebellar scans for the arms of interest exist at all, and
  reads out `C8`'s parasagittal-versus-gradient spatial pattern at no extra cost. 🔴 **It does not displace the stain**,
  because the Purkinje cell layer also holds **Bergmann glia and candelabrum interneurons** — marker-free layer occupancy
  is **not** cell identity, which is precisely the limitation of the one human observation that already exists.
- **Run § 3 #1 in parallel, because it is orthogonal.** The four-readout plate on archived DNA costs one primer pair,
  needs no imaging, and is the only thing that puts the vDNA axis on the field's standard `vg/dg` unit and **removes the
  undefined *"fold of WT"* denominator entirely.

🔴 **What NONE of these settles, stated plainly:** `C4` versus `C7`; **TRANSLATION versus PROTEIN STABILITY**, which are
`NOT ASSAYED by anyone` and cannot be separated because a steady-state per-cell amount is their **product**; and the
**absolute** scale of every WWOX number, which needs the unidentified antibody, a recombinant standard curve and a
measured human-versus-mouse affinity ratio.

---

# 6 · `COMMUNITY_FOLLOWUP` candidates

⚠️ **Framing rule, applied to every row: "their existing work creates a natural next experiment that could resolve X."**
Never *"the authors were wrong."* The framing governs **phrasing only** — the internal epistemic record in §§ 1–5 is
unchanged and fully intact. 🔴 **No one was contacted. No correspondence was drafted, sent or prepared. These are
candidates in this file and nothing else.** This is the **first** `COMMUNITY_FOLLOWUP` artefact in the repository
(verified: **0** occurrences repo-wide before this file).

| # | **LAB** | **EXISTING CAPABILITY** | **OPEN QUESTION** | **MINIMAL EXPERIMENT** | **POTENTIAL VALUE** | **COST CLASS** |
|---|---|---|---|---|---|---|
| **F1** | The 2026 AAV gene-therapy group (`PMID 42422765`) | Archived brain DNA from *"up to 25 mg"* dissections; a running vector qPCR; **vehicle arms (`KO+RI`, `WT+RI`) that are a perfect matrix-matched vector-free blank** | Their regional vDNA comparison is the field's first for WWOX. Expressing it as `vg/dg` would place it on the unit other AAV programmes report — and would make the y-axis independent of a wild-type arm, which for a vector quantity does not exist by construction | **One extra primer pair** (single-copy autosomal host reference) in the same wells, plus a plasmid standard curve diluted into their own `RI` genomic DNA | 🎯 Retro-fits **every published WWOX vDNA number** onto the field's standard axis and makes the cerebellar result citable without an estimated denominator | 🟢 `NO NEW ANIMALS` |
| **F2** | Same group | **Perfused sagittal 14 µm sections** from *"(WT, KO, and KO injected mice) at different ages (P10-P180)"*; a validated **rabbit** anti-WWOX IF channel; a 3DHISTECH whole-slide scanner | Their transduced-fraction measurement used NeuN, which in murine cerebellum labels granule neurons; adding a Purkinje marker would extend the same measurement to the cell type the ataxia phenotype concerns | 🎯 **One stain: mouse anti-calbindin + their existing anti-WWOX**, reporting per-cell intensity **distributions** and positive fraction **separately**, plus Purkinje counts per genotype | 🎯 **The single highest-value experiment in this problem** (§ 5). First Purkinje-resolved WWOX value in any WWOX system, and it redirects the programme whichever way it lands | 🟡 `NEW STAINING` |
| **F3** | Same group | 🎯 **Whole-slide scans already on disk** — the cerebellum is inside every sagittal scan at objective resolution, with WWOX already in one channel | Their scans contain a cerebellar layer-resolved WWOX distribution that the published analysis did not need to report | **One re-analysis, no bench work**: per-cell WWOX intensity by granular / Purkinje / molecular layer, plus the spatial pattern (parasagittal bands vs pial-inward gradient) | First layer-resolved cerebellar WWOX in a treated animal; also reads out `C8`'s spatial signature | 🟢 **`NEW ANALYSIS ONLY`** |
| **F4** | Same group | Archived immunoblot **lysates**; two loading controls already in the antibody list (GAPDH CB-1001, HSP90 4874S) | Their immunoblot series could additionally report WWOX per µg **total protein**, which is robust to the genotype-dependent astrogliosis, microgliosis and hypomyelination the same paper documents | **One gel series** re-normalised to Ponceau/REVERT alongside the housekeeping value | Tests sibling `H5` (composition drift) directly and retro-fits every fold-WT number | 🟢 `NO NEW ANIMALS` |
| **F5** | Same group | The **`AAV9-hSynI-EGFP`** reporter, already procured from the Vector ELSC Core Facility and used as the 2021 control virus | Promoter activity per cerebellar cell type is not separable from delivery in a WWOX-channel readout; a reporter separates them because GFP has **no endogenous counterpart and needs no wild-type denominator** | **Calbindin + native EGFP** on reporter-injected sections, per cerebellar layer | Isolates the promoter layer from every layer beneath it with **no anti-WWOX antibody and no baseline assumption**. ⚠️ Answers at the **reporter's** dose, not at `1.23E11`/`2.63E11` | 🟡 `NEW STAINING` (🔴 → `NEW COHORT` if no reporter animal was sectioned) |
| **F6** | The `Wwox^P47T/P47T` / floxed-allele laboratory (`PMID 36828035`, `PMID 33255508`) | **Calbindin and `Hcn1` IF already established** in their cerebellar vermis sections, with counts published at 80 d and 250 d; a **`Wwox` floxed exon-1 allele in hand since the knockout was built** | Their calbindin sections count Purkinje cells; adding a WWOX channel to the **same** sections would say how much WWOX a Purkinje cell contains — which no measurement in any species currently reports | 🎯 **One extra channel on existing sections** (WWOX + their existing calbindin), in `P47T` and wild-type | Converts a **cell count** into a **protein measurement** in the exact cell type, in the one model with a published `ns` interneuron control | 🟡 `NEW STAINING` |
| **F7** | Same laboratory | The floxed allele, plus their own 2020 statement in print that *"targeted CNS ablation using promoters driving Cre recombinase to specific mouse brain regions such as the cerebellum … or specific cell types … will be highly informative"* | Whether a Purkinje cell **needs** WWOX cell-autonomously — the only question in this set that tests **necessity** rather than presence | **`Pcp2`/`L7`-Cre × `Wwox^fl/fl`** — a cross, no new construct, no new reagent | The only design that separates `C4` from `C5`; the gap the allele's own makers named six years ago | 🔴 `NEW ANIMAL COHORT REQUIRED` |
| **F8** | The neonatal AAV9 rodent CNS group (Rasmussen/Daenzer/Fridovich-Keil, [DOI](https://doi.org/10.1002/jimd.12311)) | A **published, working** neonatal-AAV9 rodent brain vector-genome protocol carrying **all three** controls at issue: paired ±RNase replicates, **nanodrop→Qubit** normalisation, and a **per-sample vector spike-in** for PCR inhibition, with `vg/dg` reported | Whether those controls materially change regional vector-genome ratios in **neonatally-injected brain**, where the WWOX question sits | **Publish (or share) the paired ±RNase and nanodrop-versus-Qubit deltas per brain region** from data they already generated | 🎯 Would convert this file's largest unbounded term (`D1`) from an argument into a **measured** correction factor, for the whole neonatal-AAV CNS field | 🟢 `NEW ANALYSIS ONLY` |
| **F9** | The human cerebellar single-nucleus multiome group (Cheng/Cummings, [DOI](https://doi.org/10.1002/alz70855_105855)) | **103,861 post-mortem human cerebellar + frontal-cortex nuclei, snRNA-seq + snATAC-seq, with Purkinje and granule clusters already separated** | Whether `WWOX` is transcribed in a human Purkinje nucleus, and whether its locus is accessible there | **One query of a matrix that already exists** | Converts `PREMISE: NOBODY_LOOKED` to a measured yes/no in a **human** Purkinje nucleus, plus per-cell-type chromatin accessibility no other dataset can give. ⚠️ **Conference abstract**: accession and data terms `NOT STATED`; AD/ADRD + control tissue, **not** WWOX disease | 🟢 `NEW ANALYSIS ONLY` |
| **F10** | The human WWOX tissue-IHC group (`PMID 16941225` / `PMID 33255508`) | The **only** cerebellar WWOX observation in the literature that names the **Purkinje cell layer**, with *"a very specific anti-WWOX polyclonal antibody"* | Whether any panel of that work shows a Purkinje soma at magnification, and with what antibody identity | **Retrieval and inspection of the existing cerebellar figure** — a reading step, not an experiment | The cheapest route to the field's only Purkinje-layer datum. 🔴 `SOURCE_BLOCKED` by **licence** (`is_open_access: false`, © Springer), third confirmation. Parked `HUMAN_REQUIRED`; **no external action taken** | 🟢 `NEW ANALYSIS ONLY` (blocked) |

---

# 7 · `REVIVAL_TRIGGER`s

**Inherited unchanged and NOT retried here** (`files/` absent; network is an allowlist; `SOURCE_BLOCKED → set trigger →
CONTINUE`): the 2026 supplement and all figure captions; **S3E/S3F** — 🔴 **`3–16.7×` is NOT cited as a WPRE effect
anywhere above**, and on any route opening, record **caption, arm labels, dose, WPRE status, region, timepoint,
normalisation denominator, values and statistics** immediately; Fig 5I/5K cortex and midbrain P30 lanes; `PMID 16941225`;
`PMID 17470496`; `PMID 24369382`; HPA; DropViz/Allen; the Cheng 2025 multiome; the Purkinje-restricted conditional;
`CLAIM 039`'s cerebellar endpoint; the mouse wild-type regional WWOX protein baseline; anti-WWOX antibody identity;
regional WWOX turnover; the WOREE *"most cases"* vermis line.

**New, added by this file:**

| # | Item | Status | `REVIVAL_TRIGGER` — and what to record on arrival |
|---|---|---|---|
| **R1** | 🎯 **Weyer & Schilling 2003 narrows the repository's `%NeuN⁺` denominator** (§ 1.4) | 🟡 **FLAGGED, NOT EDITED.** Passage-level, mouse, clone not named in what I read | Read the body of [DOI 10.1002/jnr.10655](https://doi.org/10.1002/jnr.10655). Record: **which NeuN clone**, whether **deep cerebellar nuclei** were examined, and the identity of the *"small population of cells present in the lower molecular layer"*. Any actor authorised to touch the registries should reconcile the sibling § 6.2 enumeration against it. **Recording rule, standing:** every cerebellar `%NeuN⁺WWOX⁺` figure is **granule-lineage, Purkinje-EXCLUDED**, and in mouse is **essentially granule-only** |
| **R2** | **DNA quantitation mode and RNase status in the 2026 extraction** | 🔴 `NOT READABLE` — the held Methods quote carries an **ellipsis** exactly where an RNase step would sit, and the **DeNovix DS-11FX+ is dual-mode** | Any route to the **unelided** DNA-extraction paragraph, or a Key Resources / Reporting Summary. Record: **absorbance or fluorimetric**, **RNase A yes/no**, **DNA yield per mg tissue by region**, and **whether DNA came from perfused or non-perfused tissue**. 🎯 **This is the only remaining unbounded term in § 2 and the one thing that could escalate the verdict class** |
| **R3** | **Archive retention of DNA, lysates and unstained sections** | 🔴 `NOT STATED` anywhere | Any biobank, storage or aliquot statement. **Every `NO NEW ANIMALS` and `NEW STAINING` row in § 3 is conditional on this**, and the conditionality is stated rather than assumed away |
| **R4** | **Whether whole-slide scans cover cerebellum in the `1.23E11` and `2.63E11` arms** | 🔴 `NOT STATED`; the one cerebellar transduced-fraction figure sits in the **`4E10` +WPRE** arm (S3C) | Any image-availability, data-availability or supplementary-figure statement. Decides whether § 3 #5 is `NEW ANALYSIS ONLY` or needs new material |
| **R5** | **Whether `AAV9-hSynI-EGFP` animals were injected, perfused and sectioned in 2026** | 🔴 `NOT STATED` — the Methods sentence records **procurement**, not an arm | Any figure, legend or methods statement naming an EGFP arm. Record **dose, WPRE status, age, region and n**. ⚠️ **No 2021↔2026 transfer** — different vector, free-hand ~1 µL/hemisphere 33G versus stereotactic 2.0 µL 32G |
| **R6** | **Paired ±RNase and nanodrop-versus-Qubit deltas in neonatal AAV9 rodent brain** | 🟡 Generated by Rasmussen 2020 and **not reported per region** | Any publication or dataset reporting them. Would convert `D1` from bounded-by-argument to **measured** |
| **R7** | **Purkinje ploidy in mouse cerebellum** | 🟡 Bounded to ≈**0.03%** by arithmetic here; **not searched**, because the arithmetic makes the answer irrelevant to § 2 | If any actor needs the absolute `vg/dg` of a **single Purkinje nucleus** (as opposed to the regional ratio), ploidy becomes load-bearing and must be measured, not bounded |

---

# 8 · What I could not establish

1. 🔴 **Whether a host reference amplicon would actually move the cerebellum/cortex ratio, and by how much.** `P-d` is
   `NOT TESTED` and untestable without running the plate. What is established is a **bound on its components**, not the
   result.
2. 🔴 **The magnitude of `D1` (RNA carryover).** The single largest unbounded term in § 2, and the one that decides
   whether the verdict stays at `HOST REFERENCE WOULD REFINE`. Blocked by `R2`.
3. 🔴 **Whether archived DNA, lysates or unstained sections still exist.** Every cost class in § 3 is **conditional** on
   this, and no held surface states it. `R3`.
4. 🔴 **Whether whole-slide scans cover cerebellum in the LD and HD arms** — which decides the cost class of the
   cheapest experiment in the file. `R4`.
5. 🔴 **Whether an EGFP reporter arm was injected, perfused and sectioned in 2026.** Procurement is first-hand; an arm is
   not. `R5`.
6. 🔴 **`C4` versus `C7`** — cell-autonomous requirement versus metabolic vulnerability. They predict **identical**
   per-cell WWOX distributions, so **no existing-material experiment separates them.** `P-j` held; no proxy invented.
7. 🔴 **TRANSLATION versus PROTEIN STABILITY.** `NOT ASSAYED by anyone`, in these papers or anywhere in this corpus, and
   **not separable** — a steady-state per-cell amount is their product. Inherited unchanged.
8. 🔴 **Any absolute WWOX scale.** The anti-WWOX antibody has **no vendor, catalogue or clone**; the human-versus-mouse
   affinity ratio is unmeasured; the mouse wild-type regional protein baseline was never measured. All three are
   **magnitude-only** — they do not create a regional divergence — but **no fold-WT number in this literature is on an
   absolute axis.**
9. 🔴 **Whether Fig 5A–5D plots raw copies per reaction.** The y-axis definition of the strongest result in the problem
   remains `NOT READABLE`, and *"fold of WT"* is **undefined** for it because no vector-injected WT arm exists — `RI` is
   the **vehicle** (*"KO mice injected with the reference item (RI)"*, PBS/5% sorbitol/0.001% pluronic F-68).
10. 🔴 **Any Purkinje-resolved WWOX value, in any species, in any WWOX-deficient or treated system.** `P-g` confirmed and
    **nothing added**. The nearest thing remains human, wild-type, marker-free, qualitative, licence-blocked.
11. 🔴 **The `3–16.7×` attribution.** Inherited `UNRESOLVED`, left `UNRESOLVED`, **not cited as a WPRE effect** anywhere
    above.
12. ⚠️ **Whether the Weyer & Schilling narrowing holds for deep cerebellar nuclei**, and **which NeuN clone** that paper
    used. Both `NOT ESTABLISHED` from a returned passage. `R1`.
13. ⚠️ **Whether any of §§ 4–5's mechanisms is correct.** Eight classes are **preserved**; none is selected; none is a
    `CANDIDATE` and none is `CANONICAL`.

---

## Closing declarations

- 🔴 **No git was run** — nothing committed, staged or pushed. **No registry, queue, ledger, receipt, manifest, dossier or
  canonical file was created or modified.** **No `BATCH_COMMIT`.** This one analysis file is the only write.
- 🔴 **The dose non-monotonicity premise is CLOSED and was not reopened**, including from expression data.
- 🔴 **Everything here is `HYPOTHESIS ONLY` or a flag.** A `DISCOVERY` hypothesis is **not** a `CANDIDATE` and **not**
  `CANONICAL`.
- 🔴 **No one was contacted.** § 6 contains candidates and nothing else.
- 🔴 **Nothing here is medical advice.** No dose, route or construct is recommended for any species, and therapeutic
  reasoning supports discussion with a treating clinical team rather than substituting for one.

*Scholar Gateway · 4 queries · 28 passages · 27 articles · 1980–2026. Passages are first-hand; the tool's
`ai_generated` summary was not used and is not evidence. Passage retrieval is not a read and carries no receipt.*

---

## 13 · ORCHESTRATOR VERIFICATION — added 2026-09-22 after hand-back

### 13.1 🟢 Flag 2 VERIFIED first-hand — and the primary says something stronger than was quoted

Retrieved independently. Weyer & Schilling 2003, *J Neurosci Res* 73(3):400–409,
[DOI](https://doi.org/10.1002/jnr.10655) — *"Developmental and cell type-specific expression of the
neuronal marker NeuN in the murine cerebellum"*. Verbatim from the abstract:

> *"expression of this antigen in the cerebellum was **restricted to granule neurons** and a small
> population of cells present in the lower molecular layer… NeuN was **not expressed by any other
> immunocytochemically identified cerebellar interneurons, which comprised basket and stellate cells,
> Golgi neurons, unipolar brush cells, and Lugaro cells**."*

🎯 **And from the Discussion, which was not quoted and is the stronger statement:**

> *"this cellular phenotype must be added to the list of neurons that fail to express NeuN, **which
> prominently includes cerebellar Purkinje cells** (Mullen et al., 1992; Wolf et al., 1996; Sarnat et
> al., 1998)."*

⇒ **Purkinje NeuN-negativity is NOT a clone-A60 quirk.** It is an established baseline property of the
**NeuN antigen itself**, on record since **Mullen 1992 — the original NeuN paper**. A sibling file
framed it as a property of clone A60; **the correct framing is more general and more damaging.**

Methodological quality of the primary is high: parvalbumin double-labelling with **two independent
antisera**, Pax2 for immature basket/stellate and Golgi, mGluR2 for mature Golgi, calretinin for
Lugaro and unipolar brush, GABA-A α6 as a granule marker. **Only candelabrum cells could not be
analysed**, for want of a specific marker — stated by the authors.

### 13.2 🎯 THE SYNTHESIS — the transduction datum excludes BOTH cell types that matter

Combining two independently verified sources that had not been put together:

| source | statement |
|---|---|
| Aldaz & Hussain 2020 abstract ([DOI](https://doi.org/10.3390/ijms21238922)), verified first-hand | the highest-WWOX cerebellar subtypes are *"**GABAergic basket cells and granule cells**"* |
| Weyer & Schilling 2003, verified first-hand | NeuN labels **granule cells only** — **not basket cells**, and **not Purkinje cells** |

> 🔴 **So the ≈61% `NeuN⁺WWOX⁺` cerebellar fraction excludes BOTH: the cell type relevant to ataxia
> (Purkinje) AND one of the two cell types the same field reports as having the highest cerebellar
> WWOX (basket).** It is, to a good approximation, **a granule-cell measurement**.

**Why this matters beyond bookkeeping.** That ≈61% is the single datum carrying the conclusion
*"cerebellar transduction is not deficient — it is the highest of three regions."* That conclusion is
now bounded to **granule cells**, which are also the cells that **numerically dominate the
homogenate**. So the transduction measurement and the protein homogenate are reporting on **the same
dominant population**, and **neither can speak to the two populations of interest.**

⚠️ **What this does NOT license.** It does **not** show that Purkinje or basket cells are poorly
transduced — **nobody has looked**, `PREMISE: NOBODY_LOOKED`. It removes a datum from one side of the
argument; it does not supply one to the other.

⚠️ **Species bound:** Weyer & Schilling is **murine**, which is the right species for the AAV
experiments, and Mullen 1992's Purkinje statement is broader. The Aldaz scRNA-seq is **mouse
transcript** (DropViz); its own human protein IHC reports all three layers. **Do not merge them.**

### 13.3 🔴 G corrected MY run-order endorsement, and I accept the correction

After the previous wave I endorsed **host-reference qPCR first**. G ranks **calbindin + WWOX first**,
and its argument is better than mine:

> **the qPCR's answer is now arithmetically bounded** — mtDNA contributes ≈**0.06 percentage points**
> and ploidy ≈**0.03%**, against the **8.75–12.05×** a host amplicon would need to overturn — so
> **a foreseeable result is a validation, not a discriminator.**

**I ranked an experiment by how load-bearing its target was, not by how much its outcome could still
move.** That is the right correction, and it generalises: **an experiment's value is the width of its
outcome distribution, not the importance of the quantity it measures.**

🟢 G's Q1 verdict — **`HOST REFERENCE WOULD REFINE`**, deliberately *not* the strongest class — is
consistent with that arithmetic and with the brief's instruction not to assume the strongest outcome.
⚠️ **One term remains unbounded: RNA carryover.** The DeNovix DS-11FX+ is **dual-mode**
(spectrophotometer *and* fluorometer) and the held Methods quote carries **an ellipsis exactly where
an RNase step would sit** ⇒ `NOT READABLE`, **not** a validated zero. That is the only route by which
the Q1 class could still escalate.

### 13.4 The cheapest item in this wave, and it is a cost-class change

🟢 *"imaged using a **3DHISTECH panoramic scanner**"* — a **whole-slide** scanner digitises the entire
section. So a **layer-resolved cerebellar WWOX distribution already exists as unanalysed data**,
moving that question from `NEW STAINING` to **`NEW ANALYSIS ONLY`**. ⚠️ Marked `SIBLING-ATTESTED` in
§ 3 and **not** independently verified here; and every such row remains conditional on **archive
retention, which is `NOT STATED`**.
