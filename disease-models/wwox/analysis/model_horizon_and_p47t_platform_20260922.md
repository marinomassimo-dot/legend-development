# Model horizon vs. therapeutic-portfolio horizon — and whether `Wwox^P47T/P47T` or `Wwox^gt/gt` is the better platform

**Actor:** Scientist M · **Date:** 2026-09-22 · **Reports to:** Orchestrator
**Read depth declared per line.** `full-text` = served body read in this act; `abstract-depth` = PubMed
metadata only; `panel` = a figure read by a prior wave, not re-read here.
**BLOCK-1.** No molecule, no dose, no route, no safety claim is recommended anywhere below. Doses and
titres appear only as what a paper reported. *"No overt toxicity observed"* is not *"safety established."*
**Nothing here is medical advice.** This file is non-canonical: it touches no registry, no receipt
ledger, no state manifest.

**Genotype classes are held apart throughout and never merged:**
`Wwox−/−` null (Aqeilan FVB; Aldaz null) · `Wwox^P47T/P47T` SCAR12 missense knock-in ·
`Wwox^gt/gt` gene-trap · `G372R` · rat `lde/lde` · human compound heterozygote.

---

## PART 1 — The 2021 censoring claim, verified number by number

**Source read in this act:** `PMID 34747138` · `PMC8649866` · Repudi *et al.* 2021, *EMBO Mol Med*
16(1):e14599 — [DOI](https://doi.org/10.15252/emmm.202114599). Retrieved via PubMed/PMC
(`get_full_text_article(["PMC8649866"])`), **served in full, `full-text` depth.**
According to PubMed, the body, both survival legends, the Discussion and the Materials and Methods
were served; **the Appendix (including `Appendix Fig 1`, the vector schematic) was not.**

### 1.1 The exact legend text

**Figure 1C legend, verbatim as served** (the extractor deletes every `n` token, so `total= 18`
reads for `total n = 18`; the numerals are intact and the deletion is stated, not repaired):

> "Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected with
> AAV9‐hSynI‐mWwox [total= 18, spontaneously dead= 6, mice taken out for electrophysiology/electron
> microscopy/analysis, are shown in yellow,= 12] compared to mice injected with AAV9‐hSynI‐GFP (= 6)
> or the non‐injected (= 8);< 0.0001, log‐rank Mantel–Cox test."

**Figure 2C legend, verbatim as served:**

> "Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected with
> AAV9‐hWWOX [total= 16, alive= 6, spontaneously dead= 6, 4 mice (shown in yellow) were taken out for
> analysis) compared to the non‐injected (= 8)] (< 0.0001, log‐rank Mantel–Cox test)."

### 1.2 Verdict per number

| Claimed (candidate §4a) | Legend says | Verdict |
|---|---|---|
| mWwox total **18** | `total= 18` | ✅ **verified**, `full-text` |
| mWwox spontaneously dead **6** | `spontaneously dead= 6` | ✅ **verified** |
| mWwox removed **12 (67%)** | `mice taken out for electrophysiology/electron microscopy/analysis … = 12` | ✅ **verified**; 12/18 = 66.7% |
| mWwox mortality among non-removed **6/6 = 100%** | not stated; **arithmetically forced** — 6 + 12 = 18 leaves no room for an `alive` category, and unlike Fig 2C this legend lists none | ✅ **verified as an arithmetic consequence**, ⚠️ **not as a reported statistic** |
| hWWOX total **16** | `total= 16` | ✅ **verified** |
| hWWOX spontaneously dead **6** | `spontaneously dead= 6` | ✅ **verified** |
| hWWOX removed **4** | `4 mice (shown in yellow) were taken out for analysis` | ✅ **verified** |
| hWWOX mortality among non-removed **6/12 = 50%** | `alive= 6` + `spontaneously dead= 6`; 16 − 4 = 12 | ✅ **verified** |
| *"These numbers are in a figure legend"* | both are figure legends (Fig 1C, Fig 2C) | ✅ **verified** |
| *"No difference was noted when using the murine or human WWOX vectors."* | Results, §*Restoration of neuronal WWOX rescues growth retardation and post‐natal lethality*, final sentence of the paragraph | ✅ **verified verbatim, word for word** |
| *"removed at scheduled times"* | Fig 1C says only *"taken out for electrophysiology/electron microscopy/analysis"*; **Fig 2C says only *"taken out for analysis"*** — no age, no schedule, no criterion is stated for any removal | 🔴 **NOT verified — this is the delegate's inference, not the paper's words** |
| *"no sensitivity analysis exists"* | the Statistical analysis section names only *"The two‐tailed unpaired Student's‐test or two‐way ANOVA with Bonferroni for post hoc comparisons"*; no sensitivity analysis, no competing-risks or informative-censoring treatment appears anywhere in the served body | ✅ **verified as an absence in the served body** (the Appendix was not served) |

**So: every arithmetic claim in the candidate's table is correct. The interpretation attached to it
overreaches in three separate ways, and one of them is the softener the brief asked me to look for.**

### 1.3 🔴 The softener: the paper *does* report a Kaplan–Meier, and it does mark the censoring

Both arms are **Kaplan–Meier curves with a log-rank Mantel–Cox test, `p < 0.0001`**, and both legends
state that the removed animals are **"shown in yellow"** on the curve. Kaplan–Meier *is* the standard
handling of animals withdrawn before the event: they are censored at withdrawal and marked.

- **The candidate's framing — *"the survival analysis conditioned on a non-random removal"* — must be
  corrected.** The analysis is not a naive proportion computed among the non-removed; it is a
  time-to-event estimate that censors the removed animals and displays them. ⚠️ *This materially
  softens the finding and is reported as the brief required.*
- **What remains true, and is the real defect:** the paper never states that censoring is
  non-informative, never gives the age or the selection criterion for a single removal, and runs no
  sensitivity analysis. **Kaplan–Meier is only unbiased if withdrawal is independent of prognosis, and
  that assumption is neither stated nor tested here.**
- **Answer to the brief's question, precisely:** the paper **adjusts for the removals mechanically**
  (censoring inside a KM estimator) and **nowhere acknowledges the non-randomness** of who was removed
  or when. Its Discussion limitations concern oligodendrocyte-autonomous function, tumour surveillance
  in *"the limited number of adult"* treated mice *"(age 8–11 months)"*, and the P0 treatment age —
  **not the survival cohort.**

### 1.4 🔴 The direction-of-bias claim is not established, and is partly contradicted by the paper

The candidate asserts the removal is *"non-random by construction, **in the direction that flatters
survival**."* **The 2021 body does not support that direction, and supplies evidence against it for the
mWwox arm**, where the removals are concentrated:

| Experiment using **KO + AAV9-hSynI-mWwox** animals | Age | n |
|---|---|---:|
| Adult cell-attached recordings, Fig 3C–D | **6 months** | 3 |
| Corpus-callosum electron microscopy, Fig 5D–F | **6 months** | 3 |
| Aged open-field, Fig 6L–O (females) | **8–9 months** | 3 |
| Tumour surveillance, Discussion, *"limited number of adult"* treated mice | **8–11 months** | not given |

An animal removed at 6–9 months is censored at long follow-up. **Late censoring does not inflate a
survival curve the way early censoring does.** `INFERENCE` — the paper does not state that these adult
cohorts were drawn from the Fig 1C 18, but Fig 1C is the only mWwox survival cohort it describes.
**Verdict: the direction of the bias is undetermined, and for a substantial share of the 12 it points
the other way.**

### 1.5 🔴 *"Mortality among non-removed"* is a statistic with no time axis, and that is why the two arms differ

- **All mice die.** A cumulative mortality of 100% is uninformative without a horizon, and **neither
  legend reports a single death time.** The comparator matters: the untreated `Wwox−/−` null dies at
  **3–4 weeks**, and this paper's own mWwox animals were being recorded at **6 months** and open-field
  tested at **8–9 months**. `6/6` deaths spread across that span is not a failure of rescue.
- **The 100%-vs-50% contrast is most cheaply explained by follow-up duration, not by vector species.**
  The hWWOX arm still had `alive= 6` at write-up; the mWwox arm is the one carried to 6–9 months. A
  cohort followed longer accrues more deaths. **`INFERENCE`, not measured** — the paper gives no
  enrolment or censoring dates.
- 🔴 **Both sides of the equivalence question are unsupported.** The paper asserts
  *"No difference was noted when using the murine or human WWOX vectors"* (Results) and
  *"our analyses did not reveal any difference between mWwox and hWWOX vectors"* (Discussion) — **while
  running no statistical comparison between the two arms.** Each arm is tested only against its own
  untreated controls. *An untested equivalence is not equivalence.* But the candidate's counter-evidence
  — 100% vs 50% — **is not a valid time-to-event comparison either.** ⚠️ **Correct statement: nobody
  compared the two vectors, in either direction.**

### 1.6 Recorded, not claimed as new — and one prior reading I could not re-verify

Repository check performed before writing (`grep -rn` under `disease-models/wwox/`):

- **The two legends are already in the repository at `full-text` depth**, from the delegate's own in-act
  fetch: `analysis/tx007_dose_challenge_20260922.md` lines 167–168 and 296–305. The candidate's §4a says
  the Orchestrator *"could not verify them from local artefacts"* — that is about the Orchestrator's
  surfaces, not about the repository, which holds the verbatim.
- 🔴 **The hWWOX censoring was landed a month ago, not today.**
  `CC-20260826-DOSE-DECISION-TABLE-01.md` row 13 and `CC-20260826-DOSE-TRANSFERABLE-QUANTITY-01.md`
  row 7 both record *"4 of 16 censored"*, *"censoring marked on the curve"* and the verdict
  ⚠️ *"CONFOUNDED — Repudi's terminal fraction cannot be taken at face value."*
  **What is genuinely new in the candidate is the mWwox arm (12 of 18), not the phenomenon.**
- ⚠️ **A prior panel reading I could not re-verify and must not discard.** Two 2026-08-26 candidates
  record that Fig 2C's *plotted* curve **reaches 0%** while its legend says `alive= 6` — an internal
  inconsistency in the paper. **I read the legend, not the panel; the served body carries no figure
  image.** If that panel reading holds, the `6/12 = 50%` figure is itself contested by the paper's own
  graphic, and the candidate should say so.
- `analysis/denominator_audit_therapeutic_portfolio_20260922.md` line 73 already quotes the Fig 1C
  legend and already flags the `n`/`p` deletions. The candidate's §4a prediction — that the
  denominator audit *"did not read the censoring inside it"* — is **correct as to the mWwox arm**.

### 1.7 What a corrected §4a should say

> The 2021 figure legends report, verbatim, `total= 18, spontaneously dead= 6, mice taken out for
> electrophysiology/electron microscopy/analysis … = 12` (Fig 1C) and `total= 16, alive= 6,
> spontaneously dead= 6, 4 mice … taken out for analysis` (Fig 2C) — **12 of 18 and 4 of 16 withdrawn.**
> Both arms are **Kaplan–Meier with log-rank Mantel–Cox, `p < 0.0001`, and the withdrawn animals are
> marked on the curve**, so the removals *are* censored by the standard method. What the paper never
> does is state the age or criterion of any removal, assert non-informative censoring, or run a
> sensitivity analysis — and the mWwox arm's withdrawals demonstrably include animals taken at 6–9
> months, so **the direction of any bias is undetermined.** The paper's claim that
> *"No difference was noted when using the murine or human WWOX vectors"* rests on **no between-arm
> test at all**; the 100%-vs-50% contrast is most cheaply explained by unequal follow-up. **Both the
> paper's equivalence and the challenge to it are unsupported.**

---

## PART 2 — Does the 2021 paper mention WPRE?

🔴 **No. `WPRE` does not occur anywhere in the served body** — not in the Abstract, *The paper
explained*, Introduction, Results, any of the six figure legends, the Discussion, or Materials and
Methods. `full-text` depth.

The whole of what 2021 says about its cassette, verbatim:

> "Murine or human cDNA was cloned under the promoter of human in pAAV, and this vector was packaged
> into AAV9 serotype (Vector Biolabs, Philadelphia, USA). Custom‐made AAV9‐hSynI‐mWwox‐IRES‐EGFP,
> AAV9‐hSynI‐hWWOX, and AAV9‐hSynI‐EGFP viral particles were obtained either from Vector Biolabs or
> from the Vector Core Facility at Hebrew University of Jerusalem. Viral titer was measured by qRT–PCR
> using bGH primers."

(Italic gene tokens — `Wwox`, `WWOX`, `SYN1` — are deleted by the extractor; the sentence structure is
intact. `bGH` names a bovine-growth-hormone polyadenylation signal, not WPRE.)

- The only element 2021 names between promoter and cDNA is **`IRES-EGFP`, in the mWwox vector only.**
- 🔴 **The one surface that could still carry a WPRE is `Appendix Fig 1`, the vector schematic — which
  is referenced in the Results and was NOT served.** I make no claim about what it shows.
- **This confirms the prior wave and is not new.** `analysis/tx007_dose_challenge_20260922.md` line 505
  already records it, verified in-act, with the same conclusion: the repository's phrase
  *"the configuration of the 2021 proof-of-concept"* (`analysis/tx007_genotype_class_ceiling_20260921.md`
  line 175) is **an inference from Obeid 2026's framing, not a 2021 statement.** My independent read
  reproduces that verdict exactly. The unread 2021 Appendix vector map remains the only way to close it.

---

## PART 3 — The horizon question: what the null cannot test, and what can

### 3.0 The three sentences in which the 2021 authors say it themselves

All three are in the served body at `full-text` depth, and **all three are already in the repository**
(`fulltext_dossiers/PMID34747138_locators.md` l.106; `PMID34747138_partial_locators.md` l.114;
`registries/paper_registry_current.md` l.137; `analysis/wwox_developmental_timing_audit_20260920.md` l.276):

> "Since KO mice died within less than 4 weeks, we could not perform recordings in adult KO mice."
> *(the italic "in vivo" is deleted by the extractor; the repository's locator records the fuller form)*

> "Unfortunately, we could not assess behavior of‐null mice due to their poor conditions and premature death."

> "The limited life span and poor conditions of‐null mice prompted us to treat these mice very early on
> in their life (P0). Nevertheless, attempts to treat post‐natal‐null mice by different route of AAV
> administration should and will be explored in the future."

**Three times in one paper, the authors state that the null's death, not a biological boundary, set the
limit of what was measured.** That is the premise of everything below.

### 3.1 The horizon table

Horizons are taken from the repository's own `TX-` and `DL-` records; no axis is invented. "Null"
= `Wwox−/−`, dead at 3–4 weeks. 🔴 The transfer column is the one that matters, and it is mostly **NO**.

| # | Portfolio question (record) | Horizon | Null can test? | `P47T` can test? | `gt/gt` can test? | 🔴 Would a `P47T` / `gt/gt` answer transfer to a null-null or compound-het WOREE genotype? |
|---|---|---|---|---|---|---|
| **H1** | **Durability of rescue** — `DL-MOL-005` *"durevole (fino a P300)"*; `TX-007` monitor **M4** (≥3/6/12-month follow-up) | ≥ P300 | 🔴 **NO** in the untreated null. Only a *rescued* null lives that long, and a rescued null is a **survivor-selected subset** (`CC-20260814-42422765-01`) | 🟡 partly — the animal lives >1 y, so cassette persistence and biodistribution are measurable on a normal lifespan | ⚠️ unknown — lifespan is contested (see §3.2) | 🟡 **PARTIAL, and only for the vector half.** Cassette persistence, promoter silencing and biodistribution are **vector biology** and travel between genotypes. **Durability of *phenotypic rescue* does not**: the phenotype being held is not the same phenotype |
| **H2** | **Upper bound of the treatment window / post-onset, post-diagnosis dosing** — `DL-MECH-011`; `CC-20260922-POSTDIAGNOSIS-WINDOW-01`; `TX-007` window caveat | > P30, ideally months | 🔴 **NO — structurally impossible.** The animal ends before the question starts | 🟢 **YES** — an adult animal with an established, recorded seizure phenotype is dosable at any age | ⚠️ only if it has a phenotype to reverse, which is unmeasured | 🔴 **NO.** `P47T` carries **wild-type-level WWOX protein all along**; its damage trajectory is a partial-LoF trajectory, not a null one. A late rescue in `P47T` answers *"is an established WWOX-pathway phenotype reversible in an adult brain?"* — a real and unasked question — **but not** *"does late dosing work in a null"* |
| **H3** | **Adult / late-onset network phenotype; adult video-EEG seizure burden** — `seizure_ascertainment_census_20260922.md`; `DL-BIO-085` | > 6 weeks | 🔴 **NO.** The 2021 paper says so in its own words (§3.0) | 🟢 **YES — and it is the only WWOX animal where this has been done.** Bilateral 4-channel video-EEG, 14-day post-surgical recovery, adult, n = 3 vs 3 | 🔴 **NO — never attempted.** `Epilepsy` cell **empty** in Suzuki's Table 2 (`panel`, via `CC-20260826-LOCATOR-PACKET-01` (a),(c)) | 🔴 **NO.** `P47T` seizures are a **SCAR12** phenotype on a WW1-binding lesion. WOREE is an early-infantile DEE with spasms and focal seizures (`PMID 36779245`, `abstract-depth`). Same gene, different electroclinical syndrome |
| **H4** | **Progressive neuroinflammation as a longitudinal endpoint** — `DL-MECH-012`; `TX-007` | months | 🔴 **NO** | 🟢 **YES.** *"progressive neuroinflammation with elevated astro-microgliosis that increased with age"*, *"reduced number of Purkinje cells"* (`PMID 36828035`, `abstract-depth`) | ⚠️ unmeasured | 🔴 **NO for magnitude or trajectory.** 🟡 **Direction may transfer** — `DL-MECH-012` already records the anti-inflammatory brake as convergent across ≥3 models. But `DL-MECH-012`'s own caveat applies: `P47T` is a **WW1-scaffold** lesion; whether the brake is WW- or SDR-dependent is `NS-022`, **open** |
| **H5** | **Long-term consequence of brain-restricted restoration in a body that stays WWOX-deficient** — 2021: *"we did not detect gross tumor formation in the limited number of adult … treated mice that we examined (age 8–11 months)"*; `DL-MECH-009` overexpression trade-off | 8–24 months | 🔴 **NO** untreated; in treated animals only in a survivor-selected subset | 🟡 partly | 🟡 partly — and **this is the only axis where `gt/gt` is the *published* platform**: *"a higher incidence of spontaneous B-cell lymphomas"*, *"a significantly shorter lifespan"* (`PMID 17823927`, `abstract-depth`) | 🟡 **PARTIAL.** Tumour latency in a residual-protein animal is not tumour latency in a null. ⚠️ **BLOCK-1: this row is an endpoint gap, not a safety statement about anything.** *"No gross tumour detected in a limited number"* is not *"safe"* |
| **H6** | **Durability of myelin repair; adult remyelination** — `DL-MECH-010`, `DL-MECH-031` | ≥ 6 months | 🔴 **NO** untreated | ⚠️ **unmeasured** — no myelin readout is reported for `P47T` at any age | 🔴 **NO — never looked** | 🔴 **NO.** `DL-MECH-031` makes hypomyelination **secondary to the neuron**; a partial-LoF neuron is not an absent-protein neuron |
| **H7** | **Adult cerebellar degeneration / ataxia as a *treatable* endpoint** — `TX-006`; `DL-MECH-012` | months | 🔴 **NO** | 🟢 **YES — the strongest fit of any row.** Ataxia + Purkinje loss + *"mice became practically immobile"* with age | 🔴 **NO — never looked** | 🔴 **NO for WOREE**, where ataxia is not the leading disability. 🟢 **YES for SCAR12** — because `P47T` **is** the SCAR12 allele. *This row is only mislabelled as transfer: it is the model's home disease* |
| **H8** | **`TX-006` window-protection endpoints needing long observation** (status/SUDEP prevention, survival-to-adulthood) | months–years | 🔴 **NO** | 🟡 partly — adult spontaneous convulsions exist to count | 🔴 **NO** | 🔴 **NO.** WOREE mortality risk is **genotype-stratified and null/null-weighted** — *"patients with two null variants are at higher mortality risk (p-value = .0085, log-rank test)"* (`PMID 36779245`, `abstract-depth`). `P47T` is the **opposite** end of that stratification |
| **H9** | **`TX-005` lithium / GSK3β chronic dosing beyond weaning** | weeks–months | 🔴 **NO** for chronic dosing; the acute PTZ result is a peri-weaning result | 🟢 **YES** — chronically dosable, with a spontaneous-seizure readout | ⚠️ no readout established | 🔴 **NO.** `DL-MOL-003` already flags lithium as ⚠️ **mechanism-contraindicated** in WWOX loss. A `P47T` result would not lift that, and **BLOCK-1 forbids reading this row as any dosing recommendation** |
| **H10** | **`TX-004` chronic Wnt/MYC modulation and its therapeutic window** | weeks–months | 🔴 **NO** | 🟡 possible; no Wnt/MYC readout published in `P47T` | 🔴 **NO** | 🔴 **NO.** The MYC node comes from **human WOREE organoids**; `P47T` keeps protein, so *"lower MYC = better"* is untested in it, and `TX-004` already warns that default is unsafe |
| **H11** | **`TX-002` CRISPRa / `TX-003` proteostatic boost of *residual* protein, chronically, in vivo** | weeks–months | 🔴 **NO — and also the wrong biology**: a null has no residual protein to boost | 🔴 **NO — the wrong platform for the opposite reason**: `P47T` has **wild-type-level** protein, so there is nothing to upregulate; boosting it amplifies a binding-dead protein | 🟢 **In principle the ONLY correct platform in the corpus** — a residual-protein animal is exactly what `TX-002` needs | 🔴 **NO to a null** (nothing to boost, by definition). 🟡 **Possibly to a hypomorphic compound het** — **but only if `gt/gt` has residual protein in brain, which nobody has measured** (§3.2). **This is the single highest-value row in the table and it is blocked by one unmade Western blot** |
| **H12** | **Longitudinal biomarker trajectory; abundance ≠ function** — `DL-BIO-085` | months | 🔴 **NO** | 🟢 **YES, and `P47T` *is* the proof of the point** — normal abundance, lost function | ⚠️ unmeasured | 🟢 **YES — and this is the one row that transfers cleanly**, because the finding is about the **assay**, not about the genotype. A WWOX-abundance biomarker misclassifies `P47T` as normal; that is a property of the biomarker |

**Read the transfer column as a whole: of twelve horizons, one transfers cleanly (H12, and only because
it is a statement about an assay), two transfer partially and only on their vector-biology or
direction-of-effect half (H1, H4/H5), and nine do not transfer.** A platform that can answer a question
is not a model of the disease.

### 3.2 🔴 What these animals are, and are NOT — stated flatly

**`Wwox^P47T/P47T` (`PMID 36828035`, Hussain 2023, *Prog Neurobiol* — [DOI](https://doi.org/10.1016/j.pneurobio.2023.102425), `abstract-depth` here; read at full text in a prior session per `seizure_ascertainment_census_20260922.md`):**
- **IS** a **SCAR12 missense knock-in** at the WW1 PPxY-binding domain, *"impair[ing] its interaction
  with canonical proline-proline-X-tyrosine motifs in partner proteins"*.
- **HAS** WWOX protein *"comparable to wild-type controls"* (`PMID 42128308` §10.1, quoted in
  `PMID42128308_partial_locators.md` l.136) — **loss of function by failed interaction, not by lost protein.**
- **IS** an adult animal: *"unlike KO models that survive only for 1 month, live beyond 1 year of age."*
- **IS NOT a null. IS NOT a model of WOREE.** It is a model of the *milder* allelic class, and
  `PMID 36779245` places that class on the **low**-mortality side of a log-rank-significant survival split.
- 🔴 **IS NOT a clean long-horizon platform either.** *"These deficits progressed with age and mice
  became practically immobile."* Any durability or late-intervention experiment in `P47T` runs against
  a **progressively degenerating cerebellar background** that is itself a confounder — an improvement
  could be rescue, or slowed degeneration, and the two are not separable without a design that
  anticipates it.
- ⚠️ **One repository phrase overshoots the primary.** `DL-BIO-085`'s table cell and
  `resilience_and_modifier_census_20260921.md` l.114 say **"epilessia ad esordio adulto" / "adult-onset"**.
  The Hussain abstract says only that the mice *"displayed epilepsy"* and that the recordings were made
  in adults. `seizure_ascertainment_census_20260922.md` l.234 already logs this correctly as a **floor**
  — *"no juvenile recording was performed"*. **"Recorded in adults" is not "onset in adulthood",** and the
  stronger wording survives in two other files. Flagged, not repaired (not my layer).

**`Wwox^gt/gt` (`PMID 17823927`, Ludes-Meyers 2007, *Genes Chromosomes Cancer* 46(12):1129–36 — [DOI](https://doi.org/10.1002/gcc.20497), `abstract-depth` ONLY; the primary is `EVIDENCE_BLOCKED` behind a licence wall, `FT-111` / packet item `A10`, no receipt of any depth):**
- **IS** a gene-trap allele the authors themselves call hypomorphic, and **IS** viable where the null is not:
  *"Wwox hypomorphic mice are viable in contrast to the recently reported postnatal lethality of Wwox knockout mice."*
- 🔴 **IS NOT established to be "a hypomorph with residual protein" in the organ that matters.** Verbatim:
  *"Homozygous Wwox gene-trap mice (Wwox(gt/gt)) had **no detectable Wwox protein in most tissues
  examined**, although, **a low level could be detected in a minority of tissues**."* **The abstract names
  none of those tissues and does not name brain.** This corrects the framing my own brief used. The
  repository already holds the correction (`CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` row 3;
  `hypomorph_threshold_premise_audit_20260921.md`).
- 🔴 **The lifespan figure is in tension with itself, and the repository holds both halves.** The
  *"2 years"* in the brief is **Suzuki's Table 2 `Viability` row** (`CC-20260826-LOCATOR-PACKET-01` (c),
  `panel` depth, secondary source), while Ludes-Meyers' own abstract reports
  *"a **significantly shorter lifespan**"*. **Both cannot be used at once, and neither is a read of the
  primary.**
- **HAS never been observed, EEG'd or provoked.** `Epilepsy` cell empty in the same Table 2.
- 🔴 **IS therefore a *candidate* platform whose qualifying measurement has never been made.** For
  **H11**, the highest-value row in §3.1, `gt/gt` is the only structurally correct animal in the corpus —
  and the one experiment that would qualify it, **a brain Western blot**, is behind an unread paper.
  `CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` already names exactly that as the `REVIVAL_TRIGGER`:
  *"il pannello western per tessuto di `PMID 17823927`, o un video-EEG + readout mielinico su `Wwox^gt/gt`."*
- ⚠️ **Strain background is a further unverified confound across all three animals.** The Aqeilan null is
  **FVB** (2021 Methods, `full-text`). The backgrounds of `P47T` and `gt/gt` are not stated in the surfaces
  I read. Cross-model comparison without that is not controlled.

### 3.3 🔴 What this implies for the published claim that the treatment window is early

**The claim and the confound cannot be separated in the null, and the 2021 authors wrote the reason
themselves.** *"The limited life span and poor conditions of‐null mice prompted us to treat these mice
very early on in their life (P0)."*

- Today's repository already established the first half:
  `CC-20260922-POSTDIAGNOSIS-WINDOW-01` §1 records, from the 2026 primary,
  *"the inability to assess later intervention likely reflects a combination of **model-specific
  biological constraints and technical limitations, rather than a definitive boundary for therapeutic
  responsiveness**"* — 🔴 **so `P1–P5` is the set of ages tested, not a window that was measured, and the
  primary says so.** `paper_registry_current.md` l.273 records the same correction from 2026-08-10.
  **I am not claiming this; I am building on it.**
- **What I add is the platform half.** *"The window closes"* and *"the animal ends"* are confounded in
  the null **and cannot be deconfounded inside it**, because the deconfounding experiment — dose late,
  measure outcome — requires an animal that is alive late. **The `Wwox−/−` null is not merely an
  inconvenient platform for the upper-bound question; it is a logically impossible one.** Five years
  after 2021 stated post-natal dosing as declared future work, it remains undone (§3.4), and the model
  is why.
- 🔴 **But the substitution does not rescue the claim.** A late-dosing success or failure in `P47T`
  would be **a statement about a partial-LoF adult brain that has had wild-type-level protein its whole
  life**. It cannot establish an upper bound for a null. **The honest position is unchanged from
  `CC-20260922-POSTDIAGNOSIS-WINDOW-01`: neither closed nor open. What §3.1 adds is that the
  experiment is not merely unrun — it has no valid platform in the current corpus, and building one
  (a null-background animal that survives past P30, e.g. by minimal early rescue, or a
  conditional/inducible null) is itself the missing prerequisite.**

### 3.4 Usage census — has anyone used `P47T` or `gt/gt` for a therapeutic or interventional experiment?

All queries run in this act. **`query_translation` inspected before believing any count**, per the
four zero-traps. According to PubMed:

| # | Query | `total_count` | `query_translation` — expansion check | Records |
|---|---|---:|---|---|
| Q1 | `WWOX AND P47T` | **2** | ✅ fully expanded — `("wwox protein human"[Supplementary Concept] OR … OR "wwox"[All Fields]) AND "P47T"[All Fields]`. Zero-trap ruled out | `36828035` (the model paper itself), `39868255` |
| Q2 | `WWOX AND P47T AND (treatment OR therapy OR treated OR drug OR administration)` | **1** | ✅ expanded; `therapeutics`/`therapy` MeSH fired | `39868255` |
| Q3 | `WWOX AND (P47T OR knock-in) AND (rescue OR gene therapy OR AAV OR antisense OR intervention)` | **1** | ✅ expanded; `genetic therapy`[MeSH] fired | `39868255` — and it matches on *"therapeutic **interventions**"* in its own Conclusions, i.e. **on an aspiration, not an experiment** |
| Q4 | `Wwox AND (hypomorphic OR gene-trap OR knock-in)` | **5** | ✅ expanded | `36828035`, `36779245`, `25411445`, `20074932`, `17823927` |
| Q5 | `Wwox AND (gene-trap OR hypomorphic) AND (treatment OR therapy OR treated OR drug)` | **2** | ✅ expanded | `36779245` (**human clinical cohort**, matched on *"hypomorphic missense"*), `20074932` (**human SNP association**, matched on *"hypomorphic and knockout mouse models"*). 🔴 **Neither is an experiment in a `gt/gt` animal** |
| Q6 | `Wwox gt/gt mice` | **1** | ⚠️ the slash was **normalised, not echoed** — `… AND "gt gt"[All Fields] AND ("mice"[MeSH Terms] OR "mice"[All Fields])`. A real measurement, but a weak query form | `17823927` only — **the model paper itself** |

**Positive controls, identical query form:**

| Control | `total_count` | Reads |
|---|---:|---|
| `Scn1a AND (knock-in OR hypomorphic) AND (treatment OR therapy OR treated OR drug)` | **20**, `has_more: true`, ✅ fully expanded (`scn1a protein human`[Supplementary Concept] fired) | ✅ **The Q5/Q3 form DOES find interventional work in an allele-specific mouse when it exists.** The WWOX zeros are not a query artefact |
| `WWOX AND AAV` | **2** — `42128308`, `34747138`, ✅ expanded | ✅ AAV work on WWOX is findable. So **Q3's zero for `(P47T OR knock-in) AND AAV` is attributable to the model term, not the AAV term** ⚠️ Note: the candidate §1 reports `WWOX AND (AAV9 OR AAV OR adeno-associated)` → **3**; the bare-`AAV` form gives **2**, i.e. `42422765` is reached only via `AAV9`/`adeno-associated`. Not a contradiction — a narrower query. Recorded so the two counts are not read as disagreeing |

**🔴 THE FINDING — and it is first-class:**

> **In the whole indexed WWOX literature there is not one therapeutic or gene-rescue experiment in
> `Wwox^P47T/P47T` or in `Wwox^gt/gt`.** Every AAV/rescue arm in the corpus sits in the `Wwox−/−` null.
> **Zero AAV, zero gene therapy, zero antisense, zero pharmacological rescue in either animal.**
>
> The *only* intervention ever performed in a partial-LoF `Wwox` animal is **`PMID 39868255`** —
> De La Cruz *et al.* 2025, *bioRxiv*, [DOI](https://doi.org/10.1101/2025.01.17.633677) — in which
> mice *"were treated with intraperitoneal PBS vs LPS (10mg/kg) and euthanized 12 hours post-injection."*
> 🔴 **That is a pro-inflammatory *challenge*, not a therapy** — a 12-hour endotoxin provocation, in the
> **opposite** direction from treatment, on a **12-hour** horizon rather than a long one. It is a
> **preprint**, not peer-reviewed. Its genotype tokens are deleted by the extractor, but the record is
> retrieved by `"P47T"[All Fields]`, so the allele is indexed in it. `abstract-depth`:
> `get_full_text_article(["PMC11761808"])` returned **`"full_text": ""`** — another metadata-only PMC
> stub, and another live instance of the rule that a valid PMCID is not retrievability.
> **Already in the repository** as `DL-MECH-012`'s third convergent tissue; **what is new here is the
> census framing: it is the sole intervention, and it is a challenge.**

**⚠️ The census's own ceiling, stated rather than hidden.** `[All Fields]` **does not index Methods.**
A paper that used `P47T` tissue without naming it in title, abstract or keywords is invisible to Q1–Q6 —
**and the repository contains a proven instance**: `PMID 41562193` (Druck *et al.* 2026,
*Genes Chromosomes Cancer*) whose Methods name `P47T` kidneys from the Aldaz lab and whose dossier
tabulates three `P47T` mutant samples (`fulltext_dossiers/PMID41562193.md` ll.179–188, 299–301) — **and
which Q1 does not return.** So these counts are an **abstract-level ascertainment floor, not a complete
census.** The conclusion survives the caveat in one direction only: an unindexed *therapeutic* arm in
either animal is unlikely to exist while no indexed one does, but **it is not excluded.**

### 3.5 The experiment this names

Stated as a design gap, not a recommendation. **BLOCK-1: no molecule, no dose, no route.**

1. 🔴 **The cheapest and highest-value move is a literature act, not a bench act:** obtain `PMID 17823927`
   and read its **per-tissue Western panel for brain**. That single figure decides whether `gt/gt` is the
   `TX-002`/H11 platform or nothing. It is already the declared `REVIVAL_TRIGGER` of
   `CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01`, and it is currently `EVIDENCE_BLOCKED`.
2. **Second: a video-EEG + myelin readout on `Wwox^gt/gt` in adulthood.** It turns an empty Table 2 cell
   into a measurement and tests whether survival-with-residual-protein is seizure-free — which is the
   hypomorph-threshold question `CLAIM 032` currently carries on an abstract.
3. **Third, and to be labelled honestly:** an adult-dosing gene-addition arm in `P47T` answers
   *"is an established WWOX-pathway phenotype reversible in an adult brain?"* — a question nobody has
   asked, on the only WWOX animal that can be asked it. 🔴 **It does not answer the WOREE window
   question, and must not be reported as though it did.**
4. **The prerequisite nobody has built:** a null-background animal that survives past P30. Until one
   exists, the upper bound of the window has **no valid platform**, and every *"the window is early"*
   sentence in the portfolio is carrying an untested model artefact.

---

## PART 4 — Delta, non-verifications, contradictions

### 4.1 Delta of this file
1. **Independent `full-text` verification of both 2021 survival legends**, verbatim, number by number.
2. 🔴 **A three-part correction to the candidate's §4a interpretation**: the paper *does* run
   Kaplan–Meier with log-rank and *does* mark the censored animals; *"at scheduled times"* is not in the
   paper; the direction of bias is undetermined and demonstrably late for part of the mWwox arm.
3. 🔴 **Neither the paper's equivalence claim nor the challenge to it is supported** — no between-arm
   test was ever run, and the 100%-vs-50% contrast lacks a time axis.
4. **WPRE independently confirmed absent from the 2021 body**, with the one unread surface named.
5. **A twelve-row horizon × platform × transfer matrix** built only from existing `TX-`/`DL-` records.
6. 🔴 **The usage census, with counts, translations and two passing positive controls: zero therapeutic
   or rescue experiments in `P47T` or `gt/gt`; one intervention total, and it is an LPS challenge in a preprint.**
7. 🔴 **H11 named as the highest-value blocked row**: `gt/gt` is the only structurally correct platform
   for the residual-protein-boost strategies, and one unread Western blot decides it.
8. 🔴 **A correction to my own brief's framing**: `gt/gt` is *not* established as "a hypomorph with
   residual protein" in brain; its own abstract says *no detectable protein in most tissues* and does
   not name brain.

### 4.2 Could not verify
- **Any 2021 figure panel.** The served body carries no images. The prior reading that Fig 2C's plotted
  curve reaches 0% while its legend says `alive= 6` is **held, not re-verified**.
- **`Appendix Fig 1`** (2021 vector schematic) — not served. The WPRE question is closed for the body and
  open for the appendix.
- **Death times, removal ages and removal criteria** for any 2021 animal — absent from both legends and
  from the body.
- **Whether the adult 6–9-month mWwox cohorts were drawn from the Fig 1C 18** — `INFERENCE`, plausible,
  not stated.
- **`PMID 17823927` beyond its abstract** — licence wall, `FT-111`/`A10`, no receipt. **Everything about
  `gt/gt` in this file is `abstract-depth` or secondary-panel depth.**
- **`PMID 39868255` beyond its abstract** — PMC stub, `full_text: ""`.
- **`PMID 36828035` in this act** — `abstract-depth` here; a prior session read it at full text.
- **Strain background** of `P47T` and `gt/gt`.

### 4.3 Contradicting a repository assertion
1. 🔴 **`DL-BIO-085`'s "epilessia ad esordio adulto"** and `resilience_and_modifier_census_20260921.md`
   l.114's **"adult-onset"** are **stronger than the primary's abstract**, which reports only that the
   mice *"displayed epilepsy"* and that recording was done in adults.
   `seizure_ascertainment_census_20260922.md` l.234 already has it right, as a **floor**. Two files still
   carry the overshoot.
2. ⚠️ **The `gt/gt` lifespan is held two incompatible ways**: *"2 years"* (Suzuki Table 2, `panel`,
   secondary) vs *"a significantly shorter lifespan"* (Ludes-Meyers' own abstract). Not a new discovery —
   both are on file — but the two are never reconciled, and the *"viable to 2 years"* form is the one in
   circulation.
3. ⚠️ **The candidate's §4a implication that the censoring is unhandled** is the one assertion this file
   directly contradicts: it is handled, by the standard estimator, and the legend says so.

---

**End.** Non-canonical. No registry, receipt ledger or state manifest was touched.
Nothing here is medical advice; therapeutic reasoning supports discussion with a treating clinical
team and never substitutes for one.
