# COMMIT CANDIDATE — CC-20260922-MODEL-HORIZON-01

**Source:** Scientist M, `model_horizon_and_p47t_platform_20260922.md` Part 3. The agent died on a
**session rate limit at hand-back**, having written a complete file — classified **COMPLETE**, not
`PARTIAL` (the file terminates cleanly and its conclusions are self-contained).
**Verified by the Orchestrator** in `PMC8649866` (retrieved in full) and in the PubMed record for
PMID 17823927.
**Change class:** **MINOR** in edit size. 🔴 **It corrects two statements the Orchestrator wrote and
reported**, and it supplies the strongest available support for `D-31`.
**Target:** `discovery_ledger_current.md` (`DL-BIO-085`, `DL-MECH-011`) ·
`resilience_and_modifier_census_20260921.md` · the `gt/gt` lifespan wherever it appears.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2.**
**Proposes:** `D-34` — *"a platform that can answer a question is not a model of the disease."*
**BLOCK-1:** no molecule, no dose, no route, no safety claim. *"No gross tumour detected in a limited
number"* is not *"safe."*

---

## 1 · 🎯 `D-31` is now supported by the authors' own words, three times in one paper

This session established that `P1–P5` is **the set of ages tested, not a measured window**. The 2021
primary says so itself — all three verified by the Orchestrator in the retrieved body:

> *"**Since KO mice died within less than 4 weeks, we could not perform recordings in adult KO
> mice.**"*

> *"**Unfortunately, we could not assess behavior of [Wwox]-null mice due to their poor conditions
> and premature death.**"*

> *"**The limited life span and poor conditions of [Wwox]-null mice prompted us to treat these mice
> very early on in their life (P0).** Nevertheless, attempts to treat post-natal [Wwox]-null mice by
> different route of AAV administration **should and will be explored in the future**."*

🔴 **Three times, the authors state that the animal's death — not a biological boundary — set the
limit of what was measured.** The last sentence names the untried experiment explicitly. **This is
the strongest support the repository has for `D-31`, and it was in a paper we already held.**

---

## 2 · The horizon table: of twelve portfolio questions, nine do not transfer

Scientist M mapped every `TX-`/`DL-` question with a horizon beyond ~P30 against three animals.
**The null cannot test any of them** — for most, structurally: *the animal ends before the question
starts.* Summary of the transfer column, which is the one that matters:

| | verdict |
|---|---|
| **Transfers cleanly** | **1** — `H12`, longitudinal biomarker trajectory, **and only because it is a statement about an assay, not a genotype**: a WWOX-*abundance* biomarker misclassifies `P47T` as normal, which is a property of the biomarker |
| **Transfers partially** | **2** — durability (`H1`) and tumour latency (`H5`), **and only on their vector-biology or direction-of-effect half.** Cassette persistence and promoter silencing travel between genotypes; *durability of phenotypic rescue* does not, because the phenotype being held is not the same phenotype |
| 🔴 **Does not transfer** | **9** — including every seizure, myelination, window and mortality question |

> **`D-34`: a platform that can answer a question is not a model of the disease.**

🎯 **`H11` is the highest-value row, and it is blocked by one unmade Western blot.** `TX-002`
(CRISPRa) and `TX-003` (proteostatic boost of *residual* protein) need an animal that **has** residual
protein. The null has none by definition. **`P47T` is the wrong platform for the opposite reason** —
it carries **wild-type-level** protein, so there is nothing to upregulate and boosting it would
amplify a binding-dead protein. **`Wwox^gt/gt` is the only structurally correct animal in the
corpus** — and whether it qualifies has never been measured (see §3).

🔵 **And one row is only mislabelled as transfer:** `H7`, adult cerebellar degeneration as a
*treatable* endpoint, is **`P47T`'s home disease** — it *is* the SCAR12 allele. That is not a
transfer question at all.

---

## 3 · 🔴 Two things the Orchestrator wrote are wrong, and the primary says so

**(a) `Wwox^gt/gt` is NOT established as "a hypomorph with residual protein."** My own brief to
Scientist M used that framing. According to PubMed, Ludes-Meyers 2007
([DOI](https://doi.org/10.1002/gcc.20497)), verbatim:

> *"Homozygous Wwox gene-trap mice (Wwox(gt/gt)) had **no detectable Wwox protein in most tissues
> examined**, although, **a low level could be detected in a minority of tissues**."*

🔴 **The abstract names none of those tissues and does not name brain.** So the animal is a
hypomorph *by the authors' conclusion*, and **residual protein in the organ that matters is
unmeasured**. The repository already held this correction
(`CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01`); **my brief did not, and a delegate caught it.**

**(b) *"Viable to 2 years"* is a secondary panel reading, and the primary contradicts it.** I wrote
that in the recovery point and reported it. Its source is **Suzuki's Table 2 `Viability` row** — a
*secondary* source at `panel` depth. The primary's own abstract says:

> *"We observed that the Wwox(gt/gt) mice had a **significantly shorter lifespan**."*

⚠️ **Both are on file and have never been reconciled, and the *"viable to 2 years"* form is the one
in circulation — including in what I told the Operator.** Neither is a read of the primary's body.
**Proposed:** wherever the `gt/gt` lifespan appears, carry both with their depths, and stop using the
2-year figure unqualified.

🔵 **New detail the repository did not hold:** the lymphoma finding is **sex-specific** — *"**female**
hypomorphs had a higher incidence of spontaneous B-cell lymphomas."* `H5`'s tumour-latency row should
carry that.

**(c) ⛔ And the body was attempted, per this session's own corrected rule.** PubMed reports
**`PMC4143238`** for this paper — a PMCID the repository had recorded as absent.
`get_full_text_article(pmc_ids=["PMC4143238"])` → **`full_text: ""`**. **So the disposition is now
`unacquirable by attempt`, not by inference from a licence** — which is exactly the correction landed
earlier today, applied to itself. **A PMCID is still not a body.** `H11` stays blocked.

---

## 4 · 🔴 A third overshoot, and it is the observation-floor rule again

`DL-BIO-085`'s table cell and `resilience_and_modifier_census_20260921.md` describe `P47T` epilepsy
as **"adult-onset" / *"esordio adulto"***. The Hussain abstract says only that the mice *"displayed
epilepsy"* and that the **recordings** were made in adults.

> **"Recorded in adults" is not "onset in adulthood."**

`seizure_ascertainment_census_20260922.md` already logs this correctly as a **floor** — *"no juvenile
recording was performed"* — **but the stronger wording survives in two other files.** Same defect
class as *"first observed abnormal" ≠ "onset"*, which this repository has now hit four times.
**Flagged for repair.**

---

## 5 · What `P47T` is and is not — and why it is not a clean platform either

- **IS** a **SCAR12 missense knock-in** at the WW1 PPxY-binding site — **loss of function by failed
  interaction, not by lost protein**; WWOX protein is *"comparable to wild-type controls."*
- **IS** an adult animal: *"unlike KO models that survive only for 1 month, live beyond 1 year."*
- 🔴 **IS NOT a null and IS NOT a model of WOREE.** It models the *milder* allelic class, which
  `PMID 36779245` places on the **low**-mortality side of a log-rank-significant survival split —
  **the opposite end of the stratification from the null/null genotypes WOREE mortality is weighted
  toward.**
- 🔴 **IS NOT a clean long-horizon platform.** *"These deficits progressed with age and mice became
  practically immobile."* Any durability or late-intervention experiment runs against a
  **progressively degenerating cerebellar background that is itself a confounder** — an improvement
  could be rescue **or** slowed degeneration, and the two are not separable without a design that
  anticipates it.
- ⚠️ **Strain background is an unverified confound across all three animals.** The Aqeilan null is
  **FVB** (2021 Methods, `full-text`); the backgrounds of `P47T` and `gt/gt` are not stated in any
  surface read. **Cross-model comparison without that is not controlled.**

---

## 6 · Provenance

- **The three 2021 quotations and the Fig 1C/2C legends** were read by the Orchestrator in
  `PMC8649866`, retrieved in full this session.
- **The `gt/gt` abstract quotations** are verbatim from the PubMed record retrieved this session; the
  **body was attempted and is empty**.
- **`PMID 36828035` and `PMID 36779245` are `abstract-depth` here**, labelled as such at every use;
  the `P47T` full-text read is a prior session's, recorded in
  `seizure_ascertainment_census_20260922.md`.
- **Genotype classes kept rigidly separate throughout** — null ≠ `P47T` ≠ `gt/gt` ≠ rat `lde/lde` ≠
  human compound heterozygote — which is the whole point of §2.
- **`UNREAD_PREMISE`: measured at 0 before landing, not predicted.**
