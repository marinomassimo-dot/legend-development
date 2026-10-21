# Early benefit in WOREE — which endpoints are measurable, and what this repository already holds on each

> **Actor** `scientist-b` · **Task** `REPURP-P3-EARLYBENEFIT-B-20261020` · written 2026-10-20,
> completed 2026-10-21 · the `BENEFICIO_PRECOCE` axis of the operator's roadmap v4 r14.
> **Non-canonical research record.** It touches none of the four scientific current files and none of
> `disease-models/wwox/disease_model.md`. One commit candidate accompanies it
> (`CC-20261020-SCIENTIST-B-KETO-ENDPOINT-01`), and nothing here reaches a current file except through
> `BATCH_COMMIT`.
>
> **Public, disease-level, de-identified.** Patients are described at class level only. **Nothing here
> is medical advice.** No dose, no schedule, no administration route and no recommendation appears
> below; **paediatric suitability is not presumed for anything, supplements and food-based
> interventions included** — a diet is not safe because it is food, and an authorisation for another
> use is not an authorisation for this one.
>
> **The rescue reference is not written here.** `WOREE_RESCUE_REFERENCE` is owned by Harness
> Engineering at
> [`drug_repurposing/woree_rescue_reference_scaffold.md`](drug_repurposing/woree_rescue_reference_scaffold.md),
> which this note **read and references** rather than duplicating. Where a value for one of the five
> families appears below, it is cited **from the claim registry**, which is also what that scaffold's
> § 5 instructs its filler to do. No rival per-measure card exists in this file.

---

## 0 · The answer in one page

**Measurable, today, in a human child with WOREE:** growth (occipitofrontal circumference, height,
weight against SD scores at a stated age) and seizure occurrence by clinical description. That is
approximately all, and only the first is quantitative **as a kind of measurement** — the published
values this repository can reach are `PENDING_RE_ACQUISITION` (§ 1.4).

> 🔴 **Corrected 2026-10-21 after a blind locator audit** of the reading behind §§ 1.4, 1.5 and row 14
> ([`page_adjudications/locator_audit_PMID36537114_20261021.md`](page_adjudications/locator_audit_PMID36537114_20261021.md);
> 12 of 12 triples, **8 SUPPORTED · 1 OVERSHOOT · 2 UNDERSHOOT · 1 UNVERIFIABLE · 0 NOT_IN_SOURCE**).
> Four corrections travel through this note and each is marked where it lands: the **surface defect is
> global**, not confined to the growth minus signs, so no signed or ranged value from that paper is
> citable; the **absence of a counted seizure endpoint** is asserted of the delivered surface only; the
> **authors hedge *and* recommend**, and carrying only the hedge made them sound more doubtful than
> they are; and the independence boundary is **stronger**, not vaguer, than the first draft said —
> the source **names** the previously published patients and **two of them are diet responders**.
> A correction that strengthens a boundary is the outcome an audit is for, and it is recorded here in
> the same breath as the three that narrow one.

**Everything else in the five endpoint families is either qualitative, preclinical, or absent.**
The two endpoint files this repository keeps for exactly this purpose —
[`biomarker_endpoint/biomarker_candidates_current.md`](../biomarker_endpoint/biomarker_candidates_current.md)
and
[`biomarker_endpoint/clinical_monitoring_endpoints_current.md`](../biomarker_endpoint/clinical_monitoring_endpoints_current.md)
— are **structure-only**: both declare *«STRUCTURE READY — no candidate/endpoint populated yet»*, and
their populated sections read *«Currently empty.»* So the scorecard, the responder-definition
discipline and the Tier-1/Tier-3 separation all exist as machinery with **zero rows through them**.
That is the first finding of this note, and it is not a literature gap: it is a structural debt
visible in the repository's own files.

**The single most consequential statement the roadmap asks me to keep is already measured here, and
twice.** A symptomatic benefit does not demonstrate a slowing of the disease:

- in a WOREE child, vigabatrin **resolved** the spasms and at two years the child was **profoundly
  delayed anyway**, and the cognitive deficit **precedes** the seizures
  ([`discovery_ledger_current#DL-MECH-039`](discovery_ledger_current.md), Shaukat 2018, carried at
  `HYP-20260709-07`);
- in the only WOREE series reporting a therapeutic response of any kind, the *«Developmental delay»*
  row is **identical in all five columns** — the three diet responders included — and **two of the
  three responders had died**, at two years and at two years four months (PMID 36537114, read for this
  task, `FTR-20261020-36537114-01`; both rows **SUPPORTED** by the blind audit, triples 2 and 3).

So in this disease the non-equivalence is not a methodological caution imported from the roadmap. It
is printed in two independent sources, and any early-benefit candidate scored on a seizure endpoint
must carry it.

⚠️ **And it must be carried without the mirror-image error.** The authors of that series **hedge and
recommend in the same breath** — *«It may be premature to assert the potential beneficial effects»*
and *«The institution of a ketogenic diet should be considered for the treatment of epilepsy in these
patients»*. The first draft of this note quoted only the hedge, which the blind audit returned as
`UNDERSHOOT` (triple 1): it made the source sound as if it supported this note's conclusion. **The
non-modification argument rests on the absent measurement and on the two rows above, never on the
authors being more doubtful than they are** — and nothing in it is a reason for or against a dietary
intervention for any child.

**The word *protection* is not available on any endpoint in this corpus.** Nothing has been measured
as preserving a function that would otherwise have been lost — the one intervention that improves
multiple domains does so by restoring the missing gene in a mouse before postnatal day five, and even
there the comparator against wild type is either untracked or significant **against** the rescue on
the endpoint where it is drawn (`CLAIM 004`).

---

## 1 · The five families, qualified for model, genotype, age window and control

The roadmap lists these five as **revisable qualitative references, not a coverage requirement**, and
states that a single useful endpoint is a legitimate early benefit. I keep that: the table below is
not a scorecard and assigns no weights.

### 1.1 Excitability / EEG

| | |
|---|---|
| **Human, measurable now** | Seizure type and EEG **pattern**, qualitatively. In the one series read for this task, EEG is a descriptive string in every column — hypsarrhythmia, background slowing, multifocal discharges — with **no density, no background score, no repeat interval**. Seizure occurrence and drug resistance are recorded in the two large cohorts; neither reports a counted seizure endpoint. |
| **Quantitative human** | **None.** A dated PubMed probe (2026-10-21) for `WWOX AND (qEEG OR "quantitative EEG" OR …)` returns **0**. The repository's own lead for a WWOX-specific burst-suppression qEEG signature, [`DL-MECH-003`](discovery_ledger_current.md), is `IPOTESI` with belief **low**, resting on an **abstract**; its primary is unread and **parked** by this task (§ 4). |
| **Preclinical, measured** | ECoG spike-wave discharges in the `Wwox`-null mouse, reduced by neuronal AAV9-hSynI-WWOX to a level **statistically indistinguishable from wild type** (`****` WT-vs-KO, `****` KO-vs-HD, **`ns` WT-vs-HD**) — `CLAIM 040`. **Model** `Wwox`-null full KO, **age window** implant P14, recording P14→P21, **control** WT and untreated KO, **n = 5 per group**, single epidural channel, acquisition beginning with no post-surgical recovery interval. |
| **What it does not support** | SWD is an **absence-type electrographic signature** and is not a surrogate for the convulsive types that compose human WOREE (tonic, clonic, tonic-clonic, myoclonic, spasms). The **interictal-spike** endpoint of the same figure prints `0.2000`, which is **exactly the two-tailed Mann-Whitney floor** at those group sizes — it means *not tested*, in either direction. Recording starts at P14, so onset below P14 is unconstrained. |
| **Assay that would produce a human measurement** | A pre-specified qEEG parameter on routine clinical EEG — epileptiform-discharge density per hour and a background-organisation score — read **blind, by two readers, with the inter-rater agreement reported**, at a fixed interval, with a responder definition fixed **before** the observation window (`clinical_monitoring_endpoints_current.md` § 4). The repository already names this as Tier 3 and insists it is not a WWOX read-out. |

### 1.2 Myelination

| | |
|---|---|
| **Human, measurable now** | MRI **impression** only: *«delayed myelination pattern for age»* in one column of the series read here; the comparator cohort reports delayed myelination as *occasionally* reported. |
| **Quantitative human** | **None.** The same dated probe for `WWOX AND (DTI OR "diffusion tensor" OR "magnetic resonance spectroscopy" OR volumetry OR "myelin water" …)` returns **0** — and the working model nevertheless lists *«MRI + DTI as a structured baseline»* under SURVEILLANCE. That is a reasonable clinical posture with **no WWOX source behind the instrument**, and it should be read as such. |
| **Preclinical, measured** | The quantitative myelin endpoints exist and are good ones: electron-microscopy **g-ratio**, myelinated and unmyelinated **axon counts**, **conduction latency**, CNP/MBP intensity, CC1⁺/PDGFRα⁺ counts — and `CLAIM 003` records that **every one of them belongs to the neuronal (`S-KO`) line**, not to the oligodendrocyte-conditional line, whose only quantified endpoints are weight and survival (n = 11 vs 10, log-rank **P = 1.0**). |
| **Under rescue** | **Divided, and this is the family where *improved* and *normalised* come apart.** In the 2021 companion (`CLAIM 004`) the **g-ratio normalises** — the treated cloud overlaps wild type — while **unmyelinated axons per field is significant *against* the rescue** (~26 per field in WT against ~52 in treated, `**`); myelinated axons per field and CC1⁺/PDGFRα⁺ have **no treated-vs-WT bracket drawn at all**. In the 2026 dose study the family is **`UNRESOLVED`: no treated arm is quantified** (`CLAIM 011`). |
| **What it does not support** | No statement of the form *«the phenotype is rescued»*. The oligodendrocyte-targeted construct produced no benefit **under the conditions tested**, which does not show oligodendrocytes are useless as a target — expression and configuration differ, and an Olig2-Cre deletion shows **no baseline hypomyelination** (117.6 ± 12.5 against 125.1 ± 9 myelinated axons per field, **P = 0.22**), with a phenotype emerging **only under challenge** (ageing to 18 months; remyelination after cuprizone). ⚠️ That last source is a **bioRxiv preprint, not peer reviewed, from the same laboratory** — it raises no status. |
| **Assay that would produce a human measurement** | Myelin-sensitive quantitative MRI — DTI scalars or a myelin-water fraction in named tracts, same sequence, same scanner, two timepoints, with the **age-expected trajectory** as the comparator rather than a single normal range. In the animal, `CLAIM 003`'s decisive experiment is explicitly **not a new mouse**: it is g-ratio, axon counts and a conduction measurement at P10/P17/P60 **in a line that already breeds**, with the animal as the statistical unit and a challenge arm. |

### 1.3 Neuroinflammation / gliosis

| | |
|---|---|
| **Human** | **Nothing.** No gliosis, GFAP, Iba1 or cytokine measurement exists in any human WWOX record this repository holds, and no fluid marker of any kind (§ 2). |
| **Preclinical, measured** | GFAP⁺ and Iba1⁺ counts and area fractions in hippocampal subfields of the `P47T` knock-in at 80 and 250 days (`CLAIM 006`); reduced GFAP/Iba1 after neuronal rescue in the `Wwox`-null mouse (`CLAIM 004`); gliosis `RESCUE` at high dose and **`NO_RESCUE` at low dose** in the dose study (`CLAIM 011`). |
| **What it does not support** | **Astrogliosis** rises with age; **microglial abundance progression is untested** — no 80-versus-250-day bracket is drawn for it, which is not an absence. The statistics are **pseudoreplicated**: each point is a subfield or a single cell from **n = 3 mice**, with no multiplicity correction, no power analysis, no declared blinding or randomisation. The model is `P47T`, a **different domain** from the SDR missense worked example, and transfer to it is prohibited by the claim. And a glial effect observed **after a neuronal rescue does not identify a glial target** — that is the inference the roadmap forbids and `CLAIM 011` already carries. |
| **Assay that would produce a human measurement** | A blood or CSF glial-activation marker with a stated limit of detection and a paediatric reference interval, measured longitudinally. **None has ever been measured in a WWOX carrier** — see § 2, which is the sharpest negative in this note. |

### 1.4 Growth / metabolism — **the one family with a quantitative human endpoint**

| | |
|---|---|
| **Human, measurable now** | **Occipitofrontal circumference, height and weight against SD scores or percentiles at a stated age**, plus failure to thrive. In the series read for this task the **kind** of measurement is established — printed for the three surviving columns, with **failure to thrive in 5/5** and an age of onset given for one. 🔴 **The VALUES are `PENDING_RE_ACQUISITION`, and this is wider than the first draft of this note declared (corrected 2026-10-21, blind audit triple 5, `UNVERIFIABLE`).** The held extraction strips hyphens and minus signs from **prose and numeric tokens throughout the document** — `shortchain`, `lossoffunction`, `exons 68` (6–8), `34weeks` (3–4 weeks), `50th75th` (50th–75th), `< 3SD` (< −3 SD) — and a scan for U+2000–U+21FF returns the empty set, so **no numeric token from that paper is reliable for its sign or for single-value-versus-range**, and reading them as signed magnitudes (as the first draft did) is not available either. **No PDF, page render or figure render exists for this PMID anywhere under `files/`**; re-acquisition of a native surface for DOI 10.1002/ajmg.a.63074 is on the operator's PDF list, and an access control is not to be circumvented for it. *(The audit wrote «every hyphen in the document»; this reading's own qualification is that hyphens survive inside citation-anchor fragments such as `#ajmga63074-bib-0010` — which reaches no prose or numeric token, so the consequence is unchanged.)* ⚠️ The clause the first draft attached here — that this is *«the only human WOREE endpoint of that kind in the records this repository holds»* — is **withdrawn from the locator** as a statement about this repository that no quote from the paper can support; it survives only as this note's own reading, in the row below. |
| **Why it matters** | It is **standardised, repeatable, clinically obtainable without a specialised laboratory, has an age-expected trajectory as its comparator, and is already being collected in routine care** — the four properties `clinical_monitoring_endpoints_current.md` scores highest. It is the first plausible row that file could ever carry, and this note deliberately **does not write that row**: population is a `BATCH_COMMIT` act. |
| **Preclinical, measured** | Growth and glycaemia rescued by neuronal AAV9-hSynI-WWOX — **at high dose only**: at P20 the low dose **had not** corrected hypoglycaemia and the high dose had (`CLAIM 011`). CNS-only restoration reversing hypoglycaemia is the striking result of the family (`CLAIM 004`). |
| **What it does not support** | A systemic read-out after a brain-directed intervention needs its own mechanism statement, and none is measured. Separately, a systemic `Wwox`-null mouse at **P18 is metabolically decompensated**, so **any** brain phenotype in that window carries a quantified systemic confounder (`CLAIM 036`) — which means a growth or glycaemia endpoint in that model measures the animal's whole condition, not a neural effect. Elevated BUN recurs across rodent models with **two competing explanations, renal insufficiency or seizure-driven hypercatabolism, neither ever tested**; creatinine recurrence is `UNDETERMINED` (`CLAIM 038`). |
| **The caution that must travel with it** | Growth is the endpoint most likely to move for reasons that have nothing to do with WWOX — feeding route, intercurrent infection, dietary intervention, seizure burden. It is a **good early-benefit endpoint and a bad specificity argument**, and the repository's own non-confusion rule says exactly this: a distal endpoint can change with no WWOX-linked biological modification. |

### 1.5 Survival / function

| | |
|---|---|
| **Human, measurable now** | Survival, and the series read here prints it per column (*«Died at 2years 4months … Alive at 8years»*). Function is recorded as **a clinical label** — *«profound developmental delay»*, uniform across five columns. |
| **Quantitative human function** | **None.** The dated probe for `WWOX AND (Bayley OR Vineland OR "Gross Motor Function" OR actigraphy OR "Hague seizure severity")` returns **0**, and a record-level query across every registry surface returns **zero** records for `GMFM`, `Bayley`, `Vineland` and `wearable`. **No standardised developmental, motor or seizure-severity instrument has ever been applied in a WWOX cohort.** The largest cohort reports *«global disability»* as not differing significantly between genotype classes — from a **parental survey with documented survival bias** (`CLAIM 013`), which is a statement about that instrument as much as about the biology. |
| **Preclinical, measured** | Survival in the `Wwox`-null mouse: at high dose a plateau near 80 % to 300 days; at low dose **survival is not rescued at all** — death moves from about 20 to about 90 days and the curve then reaches zero (`CLAIM 011`). 🔴 That is a **threshold, not a continuum**, between 1.23 and 2.63 × 10¹¹ vg **as printed**, with the **unit convention never declared** by the primary (bilateral ICV, 2.0 µL per hemisphere), so the absolute dose is uncertain by a factor of exactly two while the ratio is invariant. No dose is transferred by this note and none is recommended. |
| **Function under rescue** | **Mixed, and read as a triple of endpoint × dose × window.** The source states *«Locomotor activity parameters … showed no significant differences between groups»* **and**, in the same record, *«Treated KO mice exhibited significantly higher motor coordination and learning compared with WT mice»*. **No cognitive endpoint was measured.** And **there is no untreated disease arm at P90 by construction**: untreated nulls and low-dose animals do not survive to be tested. |
| **Assay that would produce a human measurement** | A caregiver- or clinician-rated instrument with published reliability in a profoundly impaired paediatric population, scored at two or more timepoints, with a responder definition fixed in advance; paired with a seizure diary whose definition of an event is written before the window opens. **`PREMISE: DEFAULT_FROM_TEXTBOOK`** on my part that such an instrument exists and is suitable for this severity band — I did not source one, and the one search I ran for a validated DEE outcome-measure set returned nothing. That is a research target, not a foundation. |

---

## 2 · The negative that is the product

Three absences, each measured rather than assumed, and each bounded.

**(a) There is no validated WWOX biomarker, and the ceiling is measured, not guessed.** The three
direct read-outs a published protocol demonstrates end to end — transcript by comparative Ct, protein
by immunoblot densitometry, protein in tissue by immunohistochemistry — are **Tier 1 modalities and
none is validated**: no limit of detection, linear range, calibrator, sensitivity, specificity or
cut-off anywhere, and the tissue read-out reaches only **fair** inter-rater agreement (weighted
κ 0.264 and 0.273) **with unlimited tissue and two boarded pathologists**. Enzymatic activity is not
measured at all. The matrix is canine tumour tissue — **no WWOX variant, no CNS tissue, no body
fluid** (`CLAIM 046`). A protocol that could not exceed *fair* agreement under those conditions does
not become more precise in a harder matrix. **So no pharmacodynamic endpoint exists for any WWOX-
directed intervention**, and any candidate claiming one must clear this measured bar.

**(b) No fluid marker has ever been measured in a WWOX carrier.** `WWOX AND ("neurofilament light"
OR NfL)` returns **exactly one** record, and it is an Alzheimer's-disease plasma-biomarker
genome-wide study in which WWOX appears as a **locus associated with the plasma Aβ42/Aβ40 ratio** —
no WWOX measurement, no WOREE patient, no paediatric arm (According to PubMed,
[DOI](https://doi.org/10.1093/brain/awac128)). It is not a WOREE endpoint and is recorded here only so
the zero is not mistaken for a gap in searching.

**(c) The instrument absences are absences of *indexing*, and the difference is not cosmetic.** Both
probes above are title-and-abstract queries. The reading done for this task found, in the **body** of
a case series, a **visual evoked potential** performed in a WOREE patient (*undetectable bilaterally*)
and a **sleep study** that detected sleep apnoea with hypopnoea — while the dated probe for VEP and
ERG against WWOX returns **0**. So the correct statement is *«no WWOX paper is indexed for these
instruments»*, not *«these instruments have never been used in WOREE»*. The unbounded version would
have been false, and a false negative in this repository is the error that compounds
([`epistemic_discipline.md`](../../../framework/instruction/epistemic_discipline.md) § 2). Both
findings are **n = 1, one timepoint, no parameter, no comparator**: endpoint *existence*, not endpoint
*validation*.

**What would retire each:** (a) a WWOX assay reporting a concentration against a recombinant
calibrator with a stated limit of detection, in a matrix obtainable from a living patient, or any
published inter-rater agreement above κ 0.6; (b) any fluid marker measured in a WWOX-genotype cohort;
(c) a full-text sweep of the WOREE case literature for instrument mentions in bodies and tables —
cheap, and it would convert three indexing negatives into measured ones.

---

## 3 · Twenty relations from the current records, qualified

Each row: **entity → effect**, direction or `UNKNOWN`, context (model · genotype · age · control),
source, epistemic state, and the outcome class the task contract requires — *relevant negative ·
partial · inconclusive · exposure-or-toxicity limit · not verified · UNKNOWN*. No row is a
recommendation and no dose below is transferred.

| # | Entity → effect | Direction | Context (model · genotype · age · control) | Source | Epistemic state | Outcome class |
|---|---|---|---|---|---|---|
| 1 | Neuronal AAV9-hSynI-WWOX → survival | ↑ **above a threshold only**; below it, none | mouse · `Wwox`-null full KO · ICV P1–P5 · untreated KO and WT | `CLAIM 011` | `DATO` preclinical, claim **flagged for review** over the word *dose-dependent* | **partial** |
| 2 | Same → ECoG spike-wave discharges | ↓ to `ns` versus WT | mouse · `Wwox`-null · implant P14, record P14→P21 · WT + untreated KO, n = 5/group, single channel | `CLAIM 040` | `DATO` | **partial** (absence-type signature, not a convulsive surrogate) |
| 3 | Same → interictal spike rate | `UNKNOWN` | same figure, same cohort | `CLAIM 040` | `DATO` that the test is at its floor (`p = 0.2000` = Mann-Whitney minimum) | **inconclusive** — *not tested*, in either direction |
| 4 | Same → myelination | `UNKNOWN` | mouse · `Wwox`-null · dose study · **no treated arm quantified** | `CLAIM 011` | `UNRESOLVED` by the claim's own word | **inconclusive** |
| 5 | Same → gliosis (GFAP/Iba1) | ↓ at high dose; **no rescue at low dose** | mouse · `Wwox`-null · ICV neonatal · untreated KO | `CLAIM 011`, `CLAIM 004` | `DATO` | **partial** + **exposure limit** |
| 6 | Same → glycaemia / growth | ↑ at high dose; **not corrected at low dose at P20** | mouse · `Wwox`-null · P20 · untreated KO | `CLAIM 011` | `DATO` | **partial** |
| 7 | Same → locomotor activity | **no difference between groups** (source's own words); motor coordination/learning **above WT**; cognition **not measured** | mouse · `Wwox`-null · P90 · **WT only — no untreated disease arm survives** | `CLAIM 011` | `DATO` + a declared unresolved panel conflict | **relevant negative** (locomotor) + **inconclusive** (the excess) |
| 8 | AAV9-hSynI-WWOX (2021 companion) → myelin ultrastructure | **g-ratio normalises**; **unmyelinated axons per field significant *against* the rescue** (~26 WT vs ~52 treated) | mouse · `Wwox`-null · single ICV at P0 · WT, KO+GFP, rescued; n = 3/genotype for EM | `CLAIM 004` | `DATO` | **partial** + **relevant negative** |
| 9 | Neuronal WWOX deletion → myelination | ↓, **non-cell-autonomously** (oligodendrocytes never transduced; WWOX intact in CC1⁺ cells) | mouse · Synapsin-Cre conditional · P10–P60 · littermate control | `CLAIM 003` (`consolidated baseline`) | `DATO` for the endpoints; `INFERENZA` for the step to *non-cell-autonomous* | **partial** — recovery is **incomplete** and the residual gap is untested |
| 10 | Oligodendrocyte WWOX deletion → baseline myelination | **no difference** (117.6 ± 12.5 vs 125.1 ± 9, **P = 0.22**); phenotype only under ageing or cuprizone challenge | mouse · Olig2-Cre conditional · 18 months / post-cuprizone · littermate | `CLAIM 003` boundary | ⚠️ **bioRxiv preprint, not peer reviewed, same laboratory** | **not verified** + **relevant negative** at baseline |
| 11 | `P47T` → hippocampal astrogliosis | ↑, and rising with age; **microglial abundance progression untested** | mouse · `P47T` knock-in · 80 and 250 days · WT; **n = 3 mice, subfields/cells as the unit** | `CLAIM 006` | `DATO` + prudent `INFERENZA`; **T3, genotype caution mandatory** | **partial** |
| 12 | Systemic WWOX loss → whole-animal metabolic state | decompensated at P18 | mouse · systemic `Wwox`-null · P18 · WT | `CLAIM 036` | `DATO` (measures) + `INFERENZA` (scope as confounder) | **exposure limit** — it bounds every brain endpoint read in that window |
| 13 | WWOX loss → renal/catabolic markers (BUN, creatinine) | BUN ↑ across models; creatinine ↑ **in the rat only**, recurrence `UNDETERMINED` | rat `lde/lde` and mouse null · juvenile/adult · WT | `CLAIM 038` | `DATO` (the measures) + `IPOTESI` (**both** explanations) | **inconclusive** — renal insufficiency vs seizure-driven hypercatabolism, never tested |
| 14 | Ketogenic diet → seizure control | ↑ (clinician-reported) in 3 patients; **development unchanged in 5/5; 2 of the 3 responders died by 2 y 4 m**; exposure denominator **absent**; no count, score, latency or duration **on the delivered surface** (the per-patient narratives are **not covered**); **2 of the 3 responders are prior published individuals named by the source** (Table 1's last row → Piard 2019 for patients 2 and 4; chunk 18 → Dharmadhikari 2019 for patient 4), so a pooled count double-counts them and must name which | **human** · biallelic predicted-null WOREE · paediatric · **uncontrolled, no comparator** | PMID 36537114 / `CLAIM 042` + this reading (`FTR-20261020-36537114-01`), **audited 2026-10-21**, triples 0, 1, 5, 9 repaired at source | `DATO` (uncontrolled case series) + `INFERENZA`; ⚠️ the authors **hedge and recommend** — they call it *«premature to assert»* **and** write that the diet *«should be considered»* | **partial, symptomatic only** — explicitly **not** disease modification |
| 15 | Lithium → PTZ-induced seizures | ↓ **in all three genotypes, wild type included** | mouse · `Wwox` +/+, +/−, −/− · acute pretreatment · WT comparator present | `CLAIM 016` / `TX-005` | `DATO`; `EVID` carried on the **failed specificity test**, not the rationale | **relevant negative** — specificity was testable in that assay and was not found |
| 16 | Vigabatrin → spasms / brain MRI | spasms ↓ in some reports; **VABAM documented** in WWOX-DEE | **human** · WWOX-DEE · infancy · conflicting reports | `CLAIM 001` | `DATO`, **conflicting evidence** | **exposure-or-toxicity limit** |
| 17 | Seizure control → developmental outcome | **no effect demonstrated**; deficit **precedes** seizures and did not improve when spasms resolved | **human** · WOREE · two years of follow-up · within-patient | `DL-MECH-039` (Shaukat 2018) via `HYP-20260709-07` | `INFERENZA`, strongly supported | **relevant negative** — the axis-defining one |
| 18 | Direct WWOX read-outs (transcript, immunoblot, IHC) → a validated biomarker | **no**; IHC inter-rater κ 0.264 / 0.273 (*fair*) | canine tumour tissue and cell lines · **no WWOX variant, no CNS, no body fluid** | `CLAIM 046` | `DATO` (the measurement properties) + `INFERENZA` (the tier assignment) | **relevant negative** — the measured floor every future endpoint must clear |
| 19 | Raising neuronal WWOX above the measured high dose → toxicity | `UNKNOWN` | **no source has a vector, a delivered dose or an in vivo endpoint above it**; the dose study contains **no tumour surveillance** (`neoplas`, `carcinog`, `histopatholog`, `necropsy` = 0 on the fingerprinted main-text surface) | `CLAIM 011`, `PREMISE: NOBODY_LOOKED` | absence of evidence, **not** evidence of absence; not carried as a hazard | **exposure-or-toxicity limit** — an unmeasured ceiling on an irreversible exposure |
| 20 | WWOX loss → sleep / network state | day–night **redistribution** in a strong hypomorph; the human arm moves with **time in bed**, not sleep physiology | *Drosophila* hypomorph (mRNA ≈ 8 % of control), males, one background, **no rescue arm**; human intronic GWAS below genome-wide significance, **no WWOX expression measured** | `DL-MECH-013` | `INFERENZA`; the human leg explicitly **suggestive only** | **inconclusive** — plus one human WOREE polysomnogram, n = 1, from this reading |

Four further relations sit outside the table because they are about measurement rather than biology:
the qEEG burst-suppression signature (`DL-MECH-003`, `IPOTESI`, belief low, **abstract-only and its
primary unread — parked, § 4**); the scotopic ERG b-wave as a translatable endpoint (`DL-BIO-010`,
`ESPANSIONE`, with the warning that the **a-wave is invariant**, so an ERG endpoint must name its
component or it measures something else — and **no ERG has ever been recorded in a WWOX model**); the
exon-8→9 junction assay as the enabling endpoint for a splice-correcting strategy
(`HYP-20260709-06`, `IPOTESI`, and `TX-001` records that **its efficacy endpoint has no baseline
denominator in any WWOX allele in any tissue**); and growth as the first plausible human row (§ 1.4).

---

## 4 · Time to access and time to benefit — two dimensions, both qualified

The roadmap insists these are separate and that either may be `UNKNOWN`. They are, and here they are
unequal.

**Time to access.** On the public ClinicalTrials.gov v2 API, read 2026-10-20 by Harness Engineering
and **not re-run here**, there is **no registered WOREE interventional study**. WOREE, the
spelled-out name and EIEE28 all resolve to **one identifier**, an observational rare-disease registry
and natural-history study — not an interventional study of a WWOX-directed therapy. `DEE28` and
`MZ-9138` return nothing. The one record under the relevant sponsor is a different candidate for a
different indication. Full evidence and raw responses:
[`drug_repurposing/clinical_census_20261020.md`](drug_repurposing/clinical_census_20261020.md).
**Its own cautions bind this note**: a missing hit does not prove absence — a study may be
unregistered, worded beyond those synonyms, registered elsewhere or registered later — and **an NCT
number proves neither recruitment nor first dosing**, nor an IND authorisation, nor an approval. The
six programme events are kept separate there and four of them are `UNKNOWN` **by design**.
Separately, a compassionate-use administration is reported at **institutional-press-release level
only** — not a peer-reviewed case report and not an independent replication (carried in the working
model as *not a datum*, and in `TX-007` as news-level n = 1).

**Time to benefit.** `UNKNOWN` for **every** candidate in this repository, with no exception, and for
a reason that is structural rather than incidental: the only human observation of a therapeutic
response in WOREE reports **no latency and no duration** (§ 3 row 14), and the preclinical rescue's
own window is an **interval tested and an exterior untested** — treatment from P0 to P5 in an animal
that dies at about three weeks, with the authors themselves declining the biological reading of the
boundary (`TX-007`). **`NOT_MEASURED ≠ SMALLER`**: no experiment in any WWOX model varies age at
treatment beyond mouse P5, and **no human age-at-treatment datum of any kind exists**.

**What follows for scoring, and it is a negative result about the method.** For the one accessible
intervention in the corpus, access is immediate and the benefit is symptomatic, unquantified and
demonstrably compatible with death inside two years. For the one intervention with multi-domain
preclinical benefit, access is `UNKNOWN` and irreversible once taken. **Neither dominates the other**,
and a single blended score would hide exactly that. The roadmap's instruction to keep benefit,
evidence, risk and time separately visible is not conservatism here — it is the only presentation the
evidence supports.

---

## 5 · One paper parked, with the cascade I ran

**PMID 42190144** (Riccardi 2026, *Neurology* 106(12), DOI 10.1212/WNL.0000000000218013) — the
burst-suppression cohort in which WWOX appears among the novel associations, and the primary behind
`DL-MECH-001` and `DL-MECH-003`, the repository's only lead toward a WWOX-specific qEEG endpoint. It
carries **zero receipts**: the lead stands on an **abstract**, which is never an evidentiary surface.
Claimed for `scientist-b`, then **parked**. Cascade run 2026-10-20:

| Route | Result |
|---|---|
| PMC id conversion | *Identifier not found in PMC* |
| Europe PMC (core) | `Subscription required`, no PMCID |
| Unpaywall | `is_oa: true`, `green`; **one** OA location, a repository deposit |
| OpenAlex | same single OA location; publisher and PubMed locations not OA |
| Semantic Scholar | same URL, status `GREEN`, licence CC-BY |
| The repository deposit, direct (two domains, three paths, three User-Agent policies) | **anti-bot proof-of-work challenge** on every request; 12 KB of challenge HTML instead of the PDF |
| Repository search API → the named file path | same challenge |
| Sanctioned fetcher | *«blocked by a bot challenge … Protected by Anubis»* |

**DEFAULT TAKEN:** the challenge is an access control, and solving a proof-of-work to get around one
is not a route this actor takes on its own authority. The paper is parked as a **declared debt**, not
read, and `DL-MECH-003` keeps its `IPOTESI` tag and its low belief. The deposit is CC-BY and the
record is a genuine one, so the debt is **cheap to clear by a different hand**: an interactive session
or an operator-supplied PDF closes it in minutes. Until then, **the WWOX-specific qEEG endpoint is a
hypothesis resting on an abstract**, and this note states it as nothing more.

---

## 6 · What this note does not do

- **It writes no rescue card.** `WOREE_RESCUE_REFERENCE` is Harness Engineering's, and its § 3 names
  three divergences a filler must resolve against `CLAIM 011`'s locators rather than against the
  roadmap's prose. Every value this note cites for the five families is cited **from the claim
  registry**, which is what that scaffold instructs. Nothing here is a rival table.
- **It populates no endpoint file.** `biomarker_candidates_current.md` and
  `clinical_monitoring_endpoints_current.md` are structure-only and are populated through
  `BATCH_COMMIT` with a scorecard, an evidence status and a responder definition fixed in advance.
  § 1.4 argues that growth is the first row either file could carry; it does not write the row, and
  the commit candidate explicitly proposes none.
- **It assigns no weights to the five families** — the roadmap forbids deriving them from the single
  rescue study, and nothing else in the corpus could supply them.
- **It recommends nothing, for anyone.** No dose, no schedule, no route, no dietary course, no
  supplement, and **no paediatric suitability presumed for anything**. Every output is class-level and
  supports discussion with a treating clinical team; it never substitutes for one.

## 7 · Where this leaves the axis, in four lines

1. A legitimate early benefit on **one** endpoint is available in principle, and the endpoint most
   nearly ready is **growth**, because it is quantitative *as a kind of measurement*, repeatable,
   already collected, and has an age-expected trajectory to be compared against. 🔴 **It is not yet
   usable as a baseline:** the only values this repository can reach are on a surface that strips every
   sign and range, so they are `PENDING_RE_ACQUISITION`, and **a native surface for that article is
   therefore the single cheapest unblocking acquisition on this axis** (§ 1.4).
2. The endpoint everyone reaches for first — **seizures** — is the one this disease has twice shown to
   be **uncoupled from developmental outcome**. It remains worth pursuing for quality of life, status
   epilepticus and SUDEP, and it must never be scored as disease modification.
3. **No pharmacodynamic endpoint exists**, so no candidate can currently demonstrate that it is acting
   on WWOX at all; the measured floor for one is `CLAIM 046`.
4. The cheapest decisive moves are four, and none needs a new model: **acquire a native surface for
   DOI 10.1002/ajmg.a.63074** (it unblocks the growth values, the exposure denominator and the
   seizure-count question in one acquisition, since all three live in the chunks the held surface is
   missing); clear the parked qEEG primary; read the three cited dietary reports for their endpoints
   (`MH-36537114-03`); and sweep the WOREE case literature's **bodies and tables** for instrument
   mentions, which would convert three indexing negatives into measured ones.
5. **And one methodological result worth keeping.** The blind audit of this axis's single reading
   returned **4 adverse verdicts in 12 triples after every other gate had passed** — one of which
   *strengthened* the boundary it corrected, and one of which widened a declared artefact defect into
   a standing acquisition debt. An owed audit is a debt, not a discharge; this one paid for itself.
