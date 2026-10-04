# CC-20261003W5-A-DOSE-TWO-SIDED-01 — two phenotypes of one gene do not share one dose, and the harms of the high dose are reported where the abstract is not

- `context_policy: SOURCE_FIRST`
- Sources: PMID 41712282 (`FTR-20261003-41712282-01`), PMID 40988338 (`FTR-20261003-40988338-01`),
  PMID 39358605 (`FTR-20261003-39358605-01`), PMID 41314141 (`FTR-20261003-41314141-01`),
  PMID 41712149 (`FTR-20261003-41712149-01`). All manifests validate (VERDICT: PASS).
  **None mentions WWOX.**
- Change class: **MINOR** — one research-line record and one research-candidate record in the
  research layer. It **extends** wave 3's finding that "the highest dose was not the best dose" in
  two of three sources, and narrows no `consolidated baseline` claim.
- **Nothing here is medical advice.**

## The finding, in one sentence

In the one source that measured a metabolic endpoint and a seizure endpoint in the same animals at
the same two doses, **the two endpoints had different dose-response curves** — the metabolic endpoint
was dose-graded and the high dose drove it *below* the wild-type level, while the seizure endpoint
saturated at the low dose — which means a WWOX programme predicting rescue of both a metabolic axis
and a seizure axis cannot assume one dose serves both, and must choose which endpoint sets the dose.

## The measurement

PMID 41712282 dosed *Slc13a5*-knockout mice intrathecally at P10 at 2×10^11 vg (low) and 8×10^11 vg
(high) and read both axes:

- **Metabolic (plasma citrate):** dose-graded — 87 ± 7.7% of wild type at the low dose and
  **65 ± 8.0%** at the high dose. The knockout baseline is about 20% *above* wild type in blood, so
  the high dose did not normalise the analyte; it **overshot past normal by a third**.
- **Seizure (pentylenetetrazol kindling):** saturated — "low-dose AAV9/SLC13A5 administered at P10
  provided similar benefit as high dose". Spike trains, power spectra and sleep, by contrast, did
  improve more at the high dose.

The authors put the matching risk on the record themselves: a transgenic model overexpressing the
same gene in a neuronal subpopulation from embryonic development "was reported to cause autistic-like
and jumping behaviors, and altered white matter integrity and synaptic plasticity", and they note
that rodent expression of the gene is low at birth and rises afterwards. So the arm that best
corrects the chemistry is the arm closest to a published developmental harm, and the arm that
corrects the seizures is the lower one.

## Why this matters for a WWOX programme specifically, with the transfer limit

The repository's working expectation for WWOX includes a metabolic axis alongside the seizure
phenotype. If that expectation is right, then PMID 41712282 is the closest available model of the
*shape* of the dosing problem a WWOX programme faces: not "find the dose that rescues", but "find out
whether the two axes agree, and if they do not, decide which one the dose is for". **Transfer limit:**
the gene is a transporter whose analyte is directly measurable in blood and CSF, which is why the
mismatch is visible at all; WWOX has no such analyte in this repository, and a programme that cannot
measure its metabolic axis cannot discover a mismatch of this kind — it would simply dose to the
seizure endpoint and never learn that the other axis had overshot. The transfer is therefore to the
**experimental design**, not to the dose: *measure both axes at every dose level, in the same
animals*.

## The second pattern: where the high-dose harm is reported

In three of these sources the adverse consequence of the top dose is present in the paper but absent
from the sentence a reader would carry:

| Source | The headline | What the body or supplement holds |
|---|---|---|
| **PMID 40988338** | "well tolerated", dose-dependent rescue | A ceiling ("suggesting a ceiling effect that limits overexpression") and, in one methods clause plus Table S3, **5 of 10 high-dose mice with poor surgical recovery, only 5 recorded** — against 0 of 8 (low dose), 0 of 4 (mid dose), 1 of 11 (non-injected). The high-dose electrophysiology is therefore the surviving half of that group, and the Discussion's safety paragraph does not mention it |
| **PMID 39358605** | abstract: the primate study "revealed no significant adverse events associated with the therapeutic intervention" | Dose- and time-dependent treatment-related degeneration in dorsal root ganglia, spinal cord and sciatic nerve; a treatment-associated white-cell and lymphocyte rise at 28 days in the therapeutic arm; one unexplained death at 80 days in an animal that had received the therapeutic vector. "No significant adverse events" is a grading judgement, not an absence of findings |
| **PMID 41314141** | "well tolerated" at the highest intrathecal dose ever given | 2 of 57 events judged related, the lot was 42% genome-containing so the capsid burden was 2.38×10^15 particles, and the adverse-event table does not reconcile with itself (counts sum to 58 against a stated 57; two rows disagree with their own percentages, which imply 5 and 20 events where the counts say 7 and 18) |

PMID 41712149 states the general form of the risk for both gene-based routes — "dose-dependent
immune responses, vector-related toxicity, and uncertainties regarding long-term expression and
neurodevelopmental effects following early-life intervention" — and adds, for upregulation
strategies, "theoretical risks related to excessive or off-target transcriptional activation".

## Ops (provisional ids; re-measured at commit time)

### 1 · `disease-models/wwox/research/research_lines_current.md` — `append` (new record)

```
---

## RL-GT-004 — Two-sided dose: a gene's two phenotypes may not share one dose, and the high-dose harm is reported below the headline
**Status:** active
**Primary pathway:** P7 (gene therapy design), dose selection
**Evidence base:** PMID 41712282 (`FTR-20261003-41712282-01`), PMID 40988338 (`FTR-20261003-40988338-01`), PMID 39358605 (`FTR-20261003-39358605-01`), PMID 41314141 (`FTR-20261003-41314141-01`), PMID 41712149 (`FTR-20261003-41712149-01`) — none of which mentions WWOX
**Clinical relevance:** HIGH strategic / NOT clinically validated
**Reason active:** in the one source that read a metabolic and a seizure endpoint in the same animals at the same two doses, the two curves differed: plasma citrate fell dose-dependently to 65 ± 8.0% of wild type at the high dose — an overshoot past normal, from a baseline about 20% above wild type — while the chemoconvulsant endpoint saturated, the low dose giving the same benefit as the high. The same authors record that overexpressing that gene in development has been reported to cause autistic-like behaviour and altered white-matter integrity. For a disease model that predicts both a metabolic and a seizure axis, this is the shape of the dosing problem: the question is not which dose rescues, but whether the axes agree and which one the dose is for. TRANSFER LIMIT: the comparator gene is a transporter with a directly measurable analyte in blood and CSF, which is why the mismatch is visible; WWOX has no such analyte here, so a WWOX programme could dose to a seizure endpoint and never learn that another axis had overshot. The transfer is to experimental design — measure both axes at every dose level in the same animals — not to any dose. Separately, three of these sources report the high-dose harm below the headline: a dose-confined 50% surgical attrition visible only in a supplementary table; "no significant adverse events" covering dose- and time-dependent nerve and spinal-cord degeneration, a treatment-associated leucocytosis and one unexplained death; and a "well tolerated" highest-ever intrathecal dose whose adverse-event table does not reconcile with itself.
**Next action:** require of any WWOX dose-finding design that (i) every axis the working model predicts is measured at every dose level in the same animals, (ii) the per-group attrition and its cause are reported per dose arm, and (iii) a tolerability claim is read against the body and supplement rather than the abstract.
```

### 2 · `disease-models/wwox/research/research_candidates_current.md` — `append` (new record)

```
### RC-A-20261003w5-03 — Decide, before any WWOX dose-finding design, which endpoint sets the dose

**The question to settle on paper first:** if the WWOX working model predicts both a metabolic axis
and a seizure axis, and the two axes turn out to have different dose-responses — as they do for the
one comparator gene in which both were measured at two doses (PMID 41712282) — which one does the
dose serve?

**Why it cannot be deferred to the data:** the comparator could detect the mismatch only because its
metabolic axis has a directly measurable analyte in blood and CSF. A WWOX programme without an
equivalent pharmacodynamic readout would see one curve, not two, and would conclude it had found the
dose. This is the same conclusion the wave-3 restoration spec reached from a different direction
(`RC-C-20261003w3`, acquire a pharmacodynamic readout before specifying a dose) and it is reinforced
here by two further sources whose dose cannot be stated in protein units at all: PMID 41712282's
antibody does not recognise the endogenous mouse protein, so there is no wild-type reference for
expression level, and PMID 39358605's target antibody was unreliable and had to be proxied by a
partner subunit of the same complex.
```

## What would change the model if true, and what would falsify it

**Would change it:** a WWOX pharmacodynamic readout with a wild-type reference — which would make a
two-axis dose-response measurable at all. **Would falsify the central claim here:** a demonstration
in the comparator system that the apparent seizure-endpoint saturation is a power artefact (the
authors offer underpowering as one reading of a related null), in which case the two axes may share a
dose after all and the design requirement weakens to "measure both and check".

### LOCATOR TRIPLES FOR BLIND AUDIT

(The metabolic endpoint is dose-graded and the high dose drives it below the wild-type level. | high dose–treated mice were decreased to 65% | Results, functional NaCT, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(The seizure endpoint does not share that dose-response: the low dose did as well as the high dose. | low-dose AAV9/SLC13A5 administered at P10 provided similar benefit as high dose | Discussion, dose paragraph, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(The authors name a published developmental harm from overexpressing the same gene. | was reported to cause autistic-like and jumping behaviors, and altered white matter integrity and synaptic plasticity | Discussion, dose paragraph, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Long-term consequences of excess expression were not assessed in this study. | adverse effects related to prolonged or excessive NaCT expression were not evaluated in the present study | Discussion, safety paragraph, `files/fulltext/PMID41712282_Bailey2026_PMC.xml`)

(Raising the vector dose did not raise total protein, indicating a ceiling. | suggesting a ceiling effect that limits overexpression | Discussion, overexpression paragraph, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(A dose-associated surgical harm is reported only in the methods and never discussed. | half of the mice that received the high-dose | Methods, surgical protocol, `files/fulltext/PMID40988338_Quinlan2025_PMC.xml`)

(Treatment-related microscopic nerve and spinal-cord findings were dose- and time-dependent. | These treatment-related microscopic findings displayed a dose and time dependence in the severity and incidence of histopathological findings | Results, NHP toxicology, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(One animal that received the therapeutic vector died unexplained during the one-year study. | There was one unexplained death at 80 days post-treatment | Results, long-term safety, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(A treatment-associated white-cell rise occurred in the therapeutic arm and resolved by one year. | Elevation in white blood cell count (WBC) was observed in the ICM cohort treated with AAV9/CBh-hAP4B1 | Results, long-term safety, `files/fulltext/PMID39358605_Wiseman2024_PMC.xml`)

(The trial reports the highest intrathecal dose used in any gene therapy trial, as a total dose rather than per kilogram. | the highest intrathecal dose utilised in any gene therapy trial to date | Discussion, dose paragraph, `files/fulltext/PMID41314141_Greenberg2026_PMC.xml`)

(Both gene-based routes share a dose-dependent immune and vector toxicity risk and unknown developmental consequences. | including dose-dependent immune responses, vector-related toxicity, and uncertainties regarding long-term expression and neurodevelopmental effects following early-life intervention | Gene-based therapies, closing paragraph, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)

(Upregulation carries its own overshoot risk. | theoretical risks related to excessive or off-target transcriptional activation | Gene-based therapies, closing paragraph, `files/fulltext/PMID41712149_Balestrini2026_PMC.xml`)

---

## BATCH DISPOSITION — `BATCH_20261003_004` (2026-10-03, ACTOR_ID `scientist`, Scientist I), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED as `RL-GT-004` plus `RC-A-20261003w5-03` (both declared ids free). Class **MINOR**.

**Deduplication, measured rather than assumed:** this candidate and `CC-20261003W5-C-DOSE-SCALAR-01` were compared and are **not** the same finding — one is about two endpoints not sharing one dose-response and about high-dose harm reported below the headline, the other about three mutually non-convertible dose scalars; their source sets are disjoint (group A against group C) and they share no proposition. Both propagated, as separate records.

**Three integrator amendments (blind audit).** (1) The low-dose/high-dose equality holds for the **pentylenetetrazol-kindling paradigm only**; the same paragraph reports greater benefit at the high dose in all other metrics, epileptic discharges included. (2) The treatment-associated white-cell rise *«had diminished»* by one year rather than resolved. (3) The nerve and dorsal-root-ganglion findings are arm-level but single-animal (1 of 3, 1 of 3, 1 of 4), with one animal in the detargeted arm still affected.

**Not medical advice.**
