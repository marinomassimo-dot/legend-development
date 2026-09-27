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

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `development`, branch `task/wave2-development`.
**`context_policy`: `QUESTION_DRIVEN`**, declared before either source was opened, and declared honestly rather than as `SOURCE_FIRST`: this session already held this candidate's own conclusions. Held going in — this candidate and its two package siblings, the manifests for `PMID 36828035` (56 locators) and `PMID 34747138` (20), and `CLAIM 032` / `DL-BIO-085` retrieved with `registry_records.py` (the two large registries were never grepped wholesale). Questions, stated as narrowly as the facts required: *does Hussain 2023 state an age of onset for the P47T homozygote anywhere in its body; does it state the strain background; and are §1's three 2021 quotations verbatim?*

**Verdict: `READY_MINOR`** — and the one operation left for the batch is the `D-34` row. Everything else in this candidate is now either **applied outside batch** (below) or **already propagated** by an earlier batch.

### 1 · What was done — the work itself, not a note about it

1. 🔴 **§4's defect is confirmed at the source and repaired in both files that carried it.** Hussain 2023 (`PMID 36828035`, complete read `FTR-20260913-36828035-03`) states **no age of onset at all**. The only age attached to seizure ascertainment is the EEG cohort's — *"was performed during 24-hour sessions in adult (aged >6 weeks)"*, Methods 4.4, n = 3 per genotype — while Results 2.3 introduces the phenotype as *"displayed signs of spontaneous seizures, occasionally beginning with wild running and jumping"*, with no age, and the Introduction says only *"these mice reached adulthood and displayed intense seizure activity"*. **Three locators added** to `deepdive_manifests/PMID36828035.json` (**entries 59–61**); manifest still **STRICT PASS, 0 gaps**, artefact digest reproduced.
2. ✅ **§1's three quotations were checked against the primary body, and one is not verbatim.** The 2021 paper reads *"Since KO mice died within less than 4 weeks, we could not perform **in vivo** recordings in adult KO mice"* — the words *in vivo* were dropped without an ellipsis. The candidate's point is unaffected and the quotation is corrected. **Two locators added** to `deepdive_manifests/PMID34747138.json` (**entries 20–21**), the second being the behaviour limb — *"Unfortunately, we could not assess behavior of Wwox-null mice due to their poor conditions and premature death"*, which is why every behavioural comparison in that paper is rescued-versus-wild-type and never rescued-versus-untreated. §1's two Discussion sentences were **already persisted** (entries 6–7) and were re-matched rather than duplicated.
3. 🔴 **§5's strain-background bullet is wrong in the safe direction and is corrected: the `P47T` background IS stated in the primary.** Methods, *Development of Wwox P47T mouse model*: *"FVB/6 N female mice were used as embryo donors and ICR females were used as the surrogates"*, with the line maintained by heterozygous crosses and **littermate** controls. **Two locators added** (`PMID36828035.json` **entries 62–63**). What remains unstated is any later backcrossing; the `gt/gt` background stays unnamed in its own primary (`PMID17823927.json` entry 41).
4. 🔵 **§3(b)'s lifespan reconciliation is settled by a reading this candidate did not have.** `FTR-20260914-17823927-01` is a **complete** read of Ludes-Meyers 2007: survival is *"significantly decreased"* (**P = 0.0188, Breslow**) over a study **censored at 104 weeks** (*"Mice were allowed to live out their life span or until 104 weeks of age"*), with the tumour excess **female-only** (9/14 vs 3/15; males *"similar between the two genotypes"*, 5/14 vs 5/18, footnote `P = 0.23` which is the χ² statistic and not its P). **So *"viable to 2 years"* is an end of observation, not a lifespan** — which is stronger than the candidate's *"carry both with their depths"*, and it means §3(b) is closed rather than pending.
5. ⛔ **§3(c) stands unchanged and is not re-attempted**: `PMC4143238` serves an empty body, so `H11` stays blocked by an unmade Western and not by a licence.

### 2 · Applied outside batch (non-canonical targets, `MINOR`)

| file | what changed | how |
|---|---|---|
| `research/discovery_ledger_current.md` `DL-BIO-085` | append-only rectification: the table cell reads as *"crisi spontanee registrate in adulti (>6 settimane); età d'esordio non riportata"*, with the two verbatim sentences and the locator entries named | append-only bullet; **no earlier text rewritten** |
| `analysis/resilience_and_modifier_census_20260921.md` l.114 | *"adult-onset"* → *"epilepsy **recorded in adults (>6 weeks), onset age not reported**"*, with a dated in-line marker | single-clause replacement, rest of the row byte-identical |
| `analysis/model_horizon_and_p47t_platform_20260922.md` | the `H5` cell gains the sex-specific tumour figures, the Breslow result and the 104-week censoring; a dated append-only *Rectification* section records the non-verbatim quotation, the FVB background and the onset repair | one cell edited with its own marker + append at end of file |
| `analysis/seizure_ascertainment_census_20260922.md` | the two *"2 years"* sites are qualified as an observation cut-off with the Breslow result | in-line dated markers |

**The four scientific current files and `disease_model.md` were not touched.** `fulltext_receipts.py record` was **not** run.

### 3 · Exact operation list for `batch_commit.py propagate`

One operation only, and it is the one this package deliberately does not apply itself, because two earlier batches recorded that the optional `D-` rows are operator directives and skipped them:

| # | file | record | op | old (verbatim from the current file) | new |
|---|---|---|---|---|---|
| **M1** | `research/dismissal_ledger_current.md` | `DEFAULTS THAT BIT US` table, after the `D-06` row | `insert-after` | `| **D-06** | *(meta)* *the tool built for a problem is immune to that problem* |` *(anchor line only; nothing in it is replaced)* | a new row, **number allocated by the batch** (`D-34` proposed; `D-35`/`D-36` are claimed by `CC-20260922-SEIZURE-ASCERTAINMENT-01` and `CC-20260922-GTGT-CNS-QUALIFICATION-01`): `| **D-34** | *a platform that can answer a question is a model of the disease* | 🔴 **False, and the horizon table measures it**: of twelve portfolio questions with a horizon beyond ~P30, **nine do not transfer** to any animal in this corpus — for most, structurally, because *the animal ends before the question starts*. `Wwox`-null dies at 3–4 weeks; `Wwox^P47T/P47T` reaches adulthood but is **the mild allelic class** and carries a **progressively degenerating cerebellar background** that confounds any durability read; `Wwox^gt/gt` is the only structurally correct animal for a residual-protein question and **its brain has never been assayed**. | Four therapeutic arms were pruned on a window that was never measured (`D-31`), and `H11` is blocked by one unmade Western rather than by biology |` |

⚠️ **Nothing else is owed to the batch by this candidate.** §2's horizon table, §5's platform bullets and §6's provenance are analysis-layer statements already on disk; §1 is now locators; §3 is propagated or closed; §4 is applied above.

### 4 · Receipts and pending

Two pending receipt JSONs, **`fulltext_receipts.py record` deliberately NOT run** (the ledger is a hash chain and sibling packages are appending in parallel): `receipts_pending/development_36828035_1.json` (`FTR-20260927-36828035-04`, `partial_fulltext_read`) and `receipts_pending/development_34747138_1.json` (`FTR-20260927-34747138-03`, `partial_fulltext_read`).

🔴 **Evidence-locality finding worth more than this candidate.** `files/fulltext/PMID34747138_Repudi2021_PMC.xml` — the artefact behind twenty persisted locators — was **absent from this deployment**. It was re-acquired free from Europe PMC (`.../PMC8649866/fullTextXML`) and **reproduced the declared digest `7da156e8…` byte for byte**; NCBI efetch of the same article returns a different serialisation (`c430d5d2…`), so the route is part of the recipe. Nine figure artefacts that manifest declares are still absent and no locator added here rests on an image.

**DEFAULTS_TAKEN.** (1) *A quotation in §1 was not verbatim* → corrected and persisted as a locator instead of being left as a candidate-only sentence; safe because the meaning is unchanged and the source is now bound to a digest. (2) *§5 asserted a missing fact that the primary states* → read the Methods and recorded the fact rather than leaving a false gap; the gap that survives (backcrossing) is narrower and named. (3) *The `D-34` row is `MINOR` and non-canonical but the `D-`row lane is claimed by two sibling candidates and was skipped by two batches as an operator directive* → specified as an op with the number left to the batch, rather than minting a number that could collide. **STOP_LOG: empty.**
