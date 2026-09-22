# DISCOVERY PASS — why a 2.14× dose step changes survival categorically while protein barely moves

**Date:** 2026-09-22 · **Actor:** Orchestrator · **Mode:** `EVIDENCE → REPRESENT → DIVERGE → CONNECT → HYPOTHESIZE → PREDICT → DESIGN → VERIFY`
**Epistemic status:** every H below is 🟡 `IPOTESI` until discriminated. **No numerical probabilities.**
**Not medical advice. No dose, route or treatment recommendation for any person or animal.**

> 🔴 **§ 5 of this file — the PREDICTIONS — was written to disk and committed BEFORE the confirming
> searches were run.** That order is the point (§ 19: prediction-before-search prevents post-hoc
> storytelling). § 6 records the outcomes afterwards, with each prediction classified.

---

## 1 · EVIDENCE — the observation, stated without interpretation

| quantity | LD (`1.23E11`) | HD (`2.63E11`) |
|---|---|---|
| **survival** | reaches **0%**; *"LD-treated mice did not survive to P90"* | plateau **≈80% to 300 days** |
| regional WWOX protein | \| ← **"a trend toward"**, significance in **1 of 4** regions (hippocampus) → \| |
| regional WWOX **mRNA** | \| ← **no stated significance** → \| |
| dose ratio | \| ← **2.1382×, invariant under every unit reading** → \| |

**The mismatch:** a categorical survival outcome across a step that produces, at best, a graded and
mostly non-significant protein difference. Scientist A's verdict on reconstructing it from this paper
alone: **`NOT RECONSTRUCTABLE`**, and *"a mismatch between two differently-powered measurements — not
as biology."*

## 2 · REPRESENT — what kind of problem this is

Three quantities are being compared that are **not the same kind of thing**:
- **survival** — a whole-organism, time-integrated, threshold-crossing outcome;
- **regional protein fold-WT** — a spatial **mean over a homogenate**, at one or two ages;
- **dose** — an input, delivered once, neonatally.

🔴 **A mean over a homogenate at P30 is being used as a proxy for a time-integrated organismal
threshold.** Any mechanism that breaks that proxy — in *space*, in *time*, or in *distribution* —
produces this mismatch with no non-monotonicity and no artefact required. **That is the space to
diverge over**, and it partitions naturally into: wrong **place**, wrong **time**, wrong **statistic**,
wrong **cohort**, or a non-CNS mediator.

## 3 · DIVERGE — six mechanistically distinct explanations

### H1 · WRONG PLACE — a survival-critical population that no homogenate resolves
Survival depends on a small population (brainstem autonomic/respiratory, or hypothalamic
glucose-sensing) that **crosses a threshold** between LD and HD, while the four assayed regions dilute
it to a trend.
- **Expect if true:** the survival-critical region is one **not assayed**; per-cell WWOX there differs categorically.
- **Supports:** 🔴 **hypothalamus, brainstem, thalamus, striatum were NEVER assayed for WWOX** — while being assayed for myelin, so the omission is a selection; CNS-only restoration reverses a systemic phenotype.
- **Against:** no direct measurement anywhere.
- **Cheapest discriminator:** WWOX protein in hypothalamus + brainstem at LD and HD.

### H2 · WRONG COHORT — the plotted arm is not the treated arm
Scientist A: the HD survival denominator is **smaller than the HD experiments require** (≥35 floor to ≥61 nominal distinct HD-treated KO animals needed, against an attested `n=30`), **and the selection rule is ABSENT**.
- **Expect if true:** per-arm flow shows selection; "≈80%" is conditional on entering the plotted set.
- **Supports:** `censor*` = 0 occurrences; WT+RI at ≈72%; the fertility cohort (**20 breeding cages per group**) is never plotted.
- **Against:** selection struggles to manufacture LD reaching **0%**.
- **Discriminator:** the per-arm animal-flow and censoring table.

### H3 · WRONG TIME — protein is measured after the window that decides survival 🎯
Untreated KO dies at **~3 weeks**. Every protein measurement is **P30 or later**. So protein is read **after** the lethal window has closed, **in the animals that survived it**. A trend at P30 says little about protein at P10–P14, when the animal is dying.
- **Expect if true:** protein at **P7–P14** differs categorically between LD and HD, while P30 protein converges; late timepoints are survivor-biased by construction.
- **Supports:** ~3-week untreated lethality; IHC Methods **state** perfusion *"(WT, KO, and KO injected mice) at different ages (**P10**-P180)"* — so early material exists and was collected; P300 observations are survivor-selected.
- **Against:** no P10–P14 WWOX quantification is reported at either dose.
- **Discriminator:** WWOX protein at P10–P14, both doses. ⭐ **The material was already collected.**

### H4 · WRONG STATISTIC — a mean hides a fraction-above-threshold
If HD raises the **fraction of cells carrying enough genomes** rather than the mean per cell, a homogenate mean moves slightly while the **count of adequately rescued cells** doubles. Survival may depend on the count, not the mean.
- **Expect if true:** the per-cell distribution is **bimodal**; mean shifts little, fraction-above-threshold shifts a lot.
- **Supports:** 🔴 **per-region % transduced at LD and HD was NEVER measured** — the acknowledged hole; vDNA per tissue is not per-cell copy number; S3E's steep low-dose limb is consistent with a saturating per-cell curve.
- **Against:** not measured.
- **Discriminator:** per-cell WWOX **distribution** by quantitative IF — not a homogenate.

### H5 · A NON-CNS MEDIATOR — the metabolic axis carries the difference 🎯🎯
Hypoglycaemia is the paper's **central systemic phenotype** and is reversible by **CNS-only** restoration. If death is a metabolic crisis rather than a neurological burden, a **small** CNS protein difference in a glucose-regulating population yields a **categorical** survival difference **through blood glucose**.
- **Expect if true:** glucose diverges categorically and **early**; survival tracks glucose better than it tracks regional protein fold-change.
- **Supports:** 🎯 the repository already records that **at P20 the low dose had NOT corrected hypoglycaemia and the high dose HAD** — a categorical, early, non-protein difference on exactly the right axis.
- **Against:** the glucose→survival causal step is not itself demonstrated.
- **Discriminator:** per-arm glucose time-course against per-arm survival.

### H6 · MATERNAL CONFOUND — the breeding scheme changed
2021: *"Heterozygote mice were used for breeding."* 2026: *"Heterozygote **or KO rescued mice**…"* — **and the per-arm distribution is never stated.** Dam metabolic status could drive pup survival independently of the pup's own dose.
- **Expect if true:** dam-stratified survival differs; the effect attenuates within a dam stratum.
- **Supports:** the scheme demonstrably changed between the two papers; glucose is the central endpoint; a treated KO dam is metabolically unlike a Het dam.
- **Against:** no dam-stratified data exist.
- **Discriminator:** per-animal dam genotype and treatment status in the flow table.

## 4 · CONNECT — the two that compose

🎯 **H3 and H5 are not competitors; they compose into one mechanism**, and neither alone is as strong:

> **The lethal window is early (~3 weeks). The lethal proximate cause is metabolic (hypoglycaemia).
> The one categorical LD-vs-HD difference on record sits at P20 — inside that window, on that axis.
> And every protein measurement is taken later, in survivors.**

So the "modest protein difference" and the "categorical survival difference" are not measuring the
same animals at the same time: **the protein data describe the post-window survivors, and the
survival data are decided pre-window.** Under this composite, **no biological non-monotonicity, no
threshold in expression and no statistical artefact is required** — only a **timing-and-axis
mismatch between what was measured and what determined the outcome.**

⚠️ H2, H4 and H6 remain live and are **not** subsumed: H2 and H6 would make the survival numbers
themselves unreliable, and H4 would make the homogenate the wrong instrument regardless of timing.

## 5 · PREDICT — written and committed BEFORE the confirming searches

Persisted for the composite **H3+H5**. Each will be classified afterwards as `PREDICTION SUPPORTED` /
`PREDICTION REFUTED` / `NOT TESTED` / `AMBIGUOUS`.

| # | prediction |
|---|---|
| **P1** | A **categorical** (not graded) LD-vs-HD blood-glucose difference exists at an **early** age, and the repository's `P20` record is a true quotation of the primary, not a paraphrase. |
| **P2** | The **LD survival collapse FOLLOWS the glucose divergence in time** — glucose diverges at/near P20, LD deaths accumulate after it. If deaths substantially precede any glucose divergence, the mediation ordering fails. |
| **P3** | Survival ordering across **all** arms tracks **glucose correction** more closely than it tracks **regional WWOX protein fold-change**. |
| **P4** | **Hypothalamus** — the glucose-sensing region — is either **not assayed** for WWOX, or, if assayed, shows a **larger** LD-vs-HD difference than cortex or cerebellum. |
| **P5** | **No WWOX protein quantification exists at P7–P14 at either dose**, so the early-window protein state is unmeasured and H3 cannot be refuted from the existing record. |
| **P6** | If the authors ran a **glucose-rescue or feeding intervention** arm, survival would improve **without** a proportional change in regional WWOX protein. *(Expected to be `NOT TESTED` — recorded because a refutation here would be decisive against H5.)* |

## 6 · VERIFY — outcomes

*(to be appended after the searches; deliberately empty at the moment of writing)*
