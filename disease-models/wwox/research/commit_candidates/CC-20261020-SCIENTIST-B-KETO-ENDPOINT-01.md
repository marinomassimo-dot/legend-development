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
- **Blind locator audit:** **RUN 2026-10-21** — blind auditor, all **12 of 12** triples, verdict file
  [`page_adjudications/locator_audit_PMID36537114_20261021.md`](../page_adjudications/locator_audit_PMID36537114_20261021.md).
  **8 SUPPORTED · 1 OVERSHOOT · 2 UNDERSHOOT · 1 UNVERIFIABLE · 0 NOT_IN_SOURCE.** **All four adverse
  verdicts are repaired at source** — in the manifest entry each concerns, every repair carrying its
  own `contradicts_locator` object, and in this candidate's § 2 below. One repair makes the boundary
  **stronger** than the first wording (triple 9), two make it **narrower** (triples 0 and 5) and one
  removes a one-sided reading of the authors (triple 1).
  🔴 **One of the four is not discharged by the repair:** triple 5 is an **artefact gap**, and the
  growth values stay `PENDING_RE_ACQUISITION` until a native surface exists.
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
> seizure control**: *«However, the institution of a ketogenic diet in patients 1, 2, and 4 notably
> improved seizure control.»* **On the surface this repository holds** there is no seizure count, no
> frequency, no severity scale, no EEG change, no latency from institution to response and no
> persistence criterion — not in that sentence and not in Table 1, whose Epilepsy row records only
> seizure types and the fact of a response — so **effect size, time to benefit and duration are
> `UNKNOWN`** here. ⚠️ **Scope of that absence, corrected 2026-10-21 after the blind audit (triple 0,
> `OVERSHOOT`): the per-patient narratives are NOT COVERED** — the held surface delivers 8 of the
> article's chunks and the narratives of patients 1, 2 and 4, which is the one place a seizure count
> would appear, are absent. The absence is therefore asserted **of the delivered surface**, never of
> the article.
> ⚠️ **The authors hedge AND recommend, and both halves are theirs (corrected 2026-10-21 after the
> blind audit, triple 1, `UNDERSHOOT` — the first wording kept only the hedge and so made the paper
> more cautious than it is).** They write *«It may be premature to assert the potential beneficial
> effects of a ketogenic diet as they need to be evaluated carefully in a larger cohort»* **and, in the
> next sentence of the same chunk**, *«However, these findings suggest that the implementation of a
> ketogenic diet may help to improve the control of epilepsy in certain patients with WOREE
> syndrome»*; the abstract reports *«epilepsy that responded to a ketogenic diet in three patients»*
> and the summary concludes *«The institution of a ketogenic diet should be considered for the
> treatment of epilepsy in these patients.»* **The asymmetry this claim must not reintroduce is making
> a source sound as though it supports the reader's conclusion — in either direction.** What the
> boundary below rests on is the **absent measurement**, not on the authors being more doubtful than
> they are.
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
> 🔴 **And two of the three responders are previously published individuals, named by the source
> (strengthened 2026-10-21 after the blind audit, triple 9, `UNDERSHOOT`; the first wording said the
> surface does not say which two, and it does).** The text declares *«…five patients with WOREE
> syndrome, including three new and two previously published patients whose data have been updated»*;
> **Table 1's last row**, *«CNVs or SNVs reported in other studies or ClinVar database»*, attributes
> **patients 2 and 4** to *«Piard et al. (2019)»* (patient 3 to *«Shaukat et al. (2018)»*, patient 5 to
> *«BenSalem et al. (2015)»*), and the patient-4 sentence of the same table's chunk adds *«(published
> in figure S2; Dharmadhikari et al., 2019)»* — while **patients 1, 2 and 4 are the three described as
> responding to the diet**. So the boundary is not *«we cannot tell, therefore do not pool»* but the
> stronger and more specific one: **two of the three diet responders are named prior individuals, any
> pooled count across WOREE series double-counts them, and such a count must name which individuals it
> is counting.** ⚠️ One scope qualifier the row's own header imposes: it reports whether a **variant**
> was reported elsewhere, so it names the candidates while the three-new/two-published split is the
> text's.
> 🔵 **What the series carries as a quantitative KIND of endpoint, with its values pending:** growth
> is reported as **occipitofrontal circumference, height and weight against SD scores and percentiles
> at a stated age** for the three surviving columns, with **failure to thrive in 5/5**. 🔴 **The VALUES
> are `PENDING_RE_ACQUISITION` and no signed or ranged number from this paper may be cited (corrected
> 2026-10-21 after the blind audit, triple 5, `UNVERIFIABLE` — the defect is wider than this candidate
> first declared).** The held extraction strips hyphens and minus signs from **prose and numeric tokens
> throughout the document**, not only from the SD scores — *«shortchain»*, *«lossoffunction»*,
> *«exons 68»* (6–8), *«34weeks»* (3–4 weeks), *«50th75th»* (50th–75th), *«< 3SD»* (< −3 SD) — and a
> scan for U+2000–U+21FF returns the empty set, so **no numeric token is reliable for its sign or for
> single-value-versus-range**. **No PDF, page render or figure render exists for this PMID anywhere
> under `files/`.** Re-acquisition of a native surface for DOI 10.1002/ajmg.a.63074 is on the
> operator's PDF list, and an access control is not to be circumvented for it. **EEG, by contrast, is a
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

- ✅ **Closed by the audit, not open:** which two patients were previously published. Table 1's last
  row and the chunk-18 patient-4 sentence name them, and they are **both diet responders** — so the
  item that remains is narrower: reading **Piard 2019** and **Dharmadhikari 2019** to confirm those two
  individuals are the same individuals, which is what a pooled count would need.
- **A native-resolution surface for this article** — the publisher PDF or a page render of the Table 1
  page. Until one exists, every signed or ranged value here stays `PENDING_RE_ACQUISITION`, and this is
  an artefact gap rather than a finding against the reading: the eleven other triples verified against
  the surface that is held.
- The exposure denominator: how many patients were placed on the diet. **Possibly already answerable**
  from the per-patient narratives (chunks 3–17), which are absent from the held surface — so this item
  and the one above are the same acquisition.
- **A seizure quantity in those same narratives**, which would convert the absence in § 2 from a
  statement about the delivered surface into a statement about the article, in either direction.
- Any WOREE dietary report with a counted seizure endpoint, a defined window and a pre-specified
  responder definition. `MH-36537114-03` names the three candidates (Johannsen 2018, Ko 2018,
  Riva 2022), none of them read for its diet arm.
- Any WOREE series pairing a symptomatic endpoint with a developmental instrument measured at two
  timepoints — which would turn the non-modification argument above from three rows read together
  into a tested comparison.
