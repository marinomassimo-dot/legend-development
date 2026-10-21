# CC-20261020-SCIENTIST-B-KETO-ENDPOINT-01 — the WOREE dietary observation, bound to its endpoints

- **Actor:** `scientist-b` · **Task:** `REPURP-P3-EARLYBENEFIT-B-20261020`
- **Target records:** `claim_registry_current#CLAIM 042` (evidence boundary only)
- **target_wm_version:** `WM_v7.27`
- **Change class:** **MINOR** — no claim created, none reversed, no `consolidated baseline` touched,
  no `Status`, `Type`, `Summary`, `Transferability` or `Source` moved. `CLAIM 042` gains an evidence
  boundary and nothing else.
- **Source:** PMID 36537114 (DOI 10.1002/ajmg.a.63074), `partial_fulltext_read`,
  receipt **staged** `FTR-20261020-36537114-01`, manifest `deepdive_manifests/PMID36537114.json`
  STRICT PASS, 12 verbatim locators.
- **Blind locator audit:** **OWED**, not run. Two of the propositions below bear on an
  already-propagated claim and one of the locators carries a declared surface defect (absent minus
  signs). `legend-locator-audit` on entries 1–6 and 10 before propagation.
- **Not medical advice. No dose, no schedule, no dietary recommendation, class level only.**

## 1 · What `CLAIM 042` says today

> *One WOREE series: three of five patients reported to improve on a ketogenic diet; number exposed
> not stated; the Q230P carrier has no diet entry.* `DATO (uncontrolled case series) + INFERENZA`,
> `in observation`, `T2, not for the Q230P class`.

Every clause of that is confirmed by the reading. Nothing is narrowed and nothing is withdrawn. What
the claim lacks is the **endpoint** behind the word *improve* — and in a repository whose roadmap
separates symptomatic benefit from disease modification, that is the load-bearing omission.

## 2 · Proposed addition — one evidence-boundary block, verbatim

> **Evidence boundary — which endpoint moved, and which did not (2026-10-20,
> `CC-20261020-SCIENTIST-B-KETO-ENDPOINT-01`, read on the surface this repository holds;
> `FTR-20261020-36537114-01`).** The benefit in this series is a **clinician-reported improvement in
> seizure control** and nothing more: *«However, the institution of a ketogenic diet in patients 1, 2,
> and 4 notably improved seizure control.»* There is **no seizure count, no frequency, no severity
> scale, no EEG change, no latency from institution to response and no persistence criterion**
> anywhere on the surface, so **effect size, time to benefit and duration are `UNKNOWN`**. The authors
> decline to assert the effect themselves: *«It may be premature to assert the potential beneficial
> effects of a ketogenic diet as they need to be evaluated carefully in a larger cohort.»*
> 🔴 **And the same table refuses a disease-modifying reading of it.** The *«Developmental delay»* row
> is **identical in all five columns** — *«Profound developmental delay»* five times, the three
> responders included — and the *«Recent status»* row reads *«Died at 2years 4months |Died at 2years
> |Alive at 8years |Alive at 6years |Alive at 7years»*, i.e. **two of the three patients described as
> responding had died**, within roughly two years. The symptomatic endpoint moved; the developmental
> endpoint did not move in any column; and survival in the responders is not what a disease-modifying
> reading would predict. **A symptomatic benefit in WOREE does not demonstrate a slowing of the
> disease**, and here that is printed rather than inferred (`PREMISE: DATO` for each row;
> `PREMISE: INFERENZA` for reading the three rows together as a non-modification argument — the paper
> draws no such comparison and reports no statistical test of any kind).
> ⚠️ **The exposure denominator is absent, measured on the delivered chunks:** the surface states that
> three patients responded and **never states how many were placed on the diet**, so *«three of five»*
> is a count of responders against cohort size, not a response rate.
> ⚠️ **Nor are the three observations necessarily independent:** *«…five patients with WOREE syndrome,
> including three new and two previously published patients whose data have been updated»* — and the
> delivered surface **does not say which two**. Until that is resolved, no response in this series may
> enter a pooled count across WOREE series, and none of the three may be asserted as a new observation.
> 🔵 **What the series does carry as quantitative endpoints, which is why it is read at all:** growth
> is reported as **occipitofrontal circumference, height and weight in SD scores and percentiles at a
> stated age** for the three surviving columns (*«OFC: 2 SD / Weight: 1.5 SD / Height: 3.0 SD (at
> 8years)»* — ⚠️ **the minus signs are absent from the extracted surface and the values are read as
> magnitudes only**, direction supplied by the same table calling that patient microcephalic from two
> months, never by the characters quoted), with **failure to thrive in 5/5**. **EEG, by contrast, is a
> qualitative pattern description in every column** — hypsarrhythmia, background slowing, multifocal
> discharges — with no density, no background score and no repeat interval. 🔵 **Two measurements
> nobody had recorded exist here at n = 1:** a **visual evoked potential**, *«Patient 4 demonstrated
> undetected visual evoked potentials suggesting central involvement»*, and a **sleep study**,
> *«Sleep apnea with hypopnea detected by sleep study»*. Both are single patients, single timepoints,
> no parameter and no comparator — endpoint *existence*, not endpoint *validation*. They also bound a
> negative: a dated PubMed probe for VEP, ERG, DTI, MRS and volumetry against WWOX returns **zero**,
> so that absence is an **indexing** absence and not an absence of measurement. 🔴 **And no WWOX
> read-out of any kind exists in this paper** — no protein, no transcript, no activity — so whatever
> changed in those three children, **nothing measured the gene**, and the observation is not evidence
> about WWOX functional state. **Not medical advice; no dose, schedule or dietary course is implied,
> and paediatric suitability is not presumed for anything.**

## 3 · What is NOT proposed

- No change to `Status`, `Type`, `Pathway`, `Transferability`, `clinical relevance`, `Summary` or
  `Source` of `CLAIM 042`.
- **No new claim.** The VEP and the sleep study are endpoint existence at n = 1; promoting either to a
  claim would be exactly the overstatement this candidate exists to prevent.
- **No population of `biomarker_endpoint/`.** Both files there are structure-only by design and are
  populated through `BATCH_COMMIT`; this candidate proposes no row in either, and the note that
  accompanies it says why the growth endpoint is the first plausible row rather than writing one.
- No touch of the four scientific current files by this actor, and no touch of
  `research/drug_repurposing/`, which a Harness agent owns.

## 4 · `REVIVAL_TRIGGER` / what would change this block

- Which two of the five patients were previously published — one sentence from the typeset paper, and
  it decides whether any of the three responses is a new observation.
- The exposure denominator: how many patients were placed on the diet.
- Any WOREE dietary report with a counted seizure endpoint, a defined window and a pre-specified
  responder definition. `MH-36537114-03` names the three candidates (Johannsen 2018, Ko 2018,
  Riva 2022), none of them read for its diet arm.
- Any WOREE series pairing a symptomatic endpoint with a developmental instrument measured at two
  timepoints — which would turn the non-modification argument above from three rows read together
  into a tested comparison.
