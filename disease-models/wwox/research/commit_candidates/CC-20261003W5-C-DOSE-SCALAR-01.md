# CC-20261003W5-C-DOSE-SCALAR-01 — "dose" is not one quantity in this evidence base, and none of the three scalars in use can set an infant dose

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-03 · **Author:** Scientist C, intake wave 5 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead)

> **MINOR.** No canonical claim is edited. This candidate records a measurement-hygiene finding about
> the delivery literature and names the gap that blocks any pre-first-patient dose bound for an
> infant. **Nothing here is medical advice.**

---

## 1 · Three mutually non-convertible scalars, in six sources

| Scalar | Used by | Example values |
|---|---|---|
| **Fixed total vector genomes per animal or per patient** | PMID 41210171, PMID 41257285, and **every human trial** indexed by PMID 42134074 | 1.2 × 10¹³ vg/animal; 1.0–3.0 × 10¹³ vg/NHP; human intrathecal 6 × 10¹³ – 1 × 10¹⁵ vg |
| **Per gram of brain mass** | PMID 41966056 (human intracisternal) | printed with a corrupted sign; see `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01` |
| **Per CSF volume** | PMID 41948127 | murine doses "scaled 371-fold for the increased CSF volume in monkeys compared to mice" |

A number expressed in one of these cannot be converted into another without the species- and
age-specific brain mass and CSF volume that would make the conversion. **Only one source in the
group supplies those**, and that is the finding below.

## 2 · The conversion table exists, is internally sound, and still cannot do the job

PMID 42205472 Table 4, read **cell-wise** from the XML table structure:

| Species | Brain volume (cm³) | External brain surface area (cm²) | CSF volume (cm³) | Ventricular surface area (cm²) | Total surface area/brain volume (cm⁻¹) |
|---|---:|---:|---:|---:|---:|
| Mouse | 0.3 | 3 | 0.04 | 0.5 | 11.7 |
| Rat | 2.2 | 20 | 0.15 | 1 | 9.5 |
| Macaque | 90 | 200 | 15 | 8 | 6.8 |
| Human | 1400 | 1850 | 140 | 32 | 1.3 |

**It is coherent.** CSF volume rises monotonically across the four species and the
surface-area-to-volume ratio falls monotonically, as it must. And its mouse and macaque CSF volumes
independently reproduce the scaling factor an actual programme used: 15 / 0.04 ≈ **375**, against the
**371-fold** stated by PMID 41948127 — agreement to about one percent between two independent
compilations.

**And it still cannot set an infant dose, for one reason: there is a single "human" row and it
carries no age.** 1400 cm³ of brain and 140 cm³ of CSF are adult values. The review says in prose
that paediatric CSF dynamics "change rapidly with age, primarily due to skull growth" and then
**defers the detail to Supplementary Material 2**, which is not in the body and which this reading
did not retrieve. So the one cross-species scaling table available to this wave stops exactly where
the question starts.

## 3 · Why this is not a pedantic point

PMID 42205472 states plainly that fixed dosing is current practice and is inadequate for a CSF route:

> "In the case of intraventricular therapies, dosing considerations may need to include factors such
> as the patency of the pathways and estimated ventricular volume (at a minimum), much as a pediatric
> dosing schedule is adjusted according to weight."

And the approved human intrathecal product is dosed as **a fixed total**, 1.2 × 10¹⁴ vg, for
everyone from 2 to under 18 years — ages across which brain mass and CSF volume differ substantially.
The review names **age** among the top three drivers of variability in delivered dose at a CSF route.

Two further facts make the per-animal total the least informative of the three scalars:

1. **Infused volume matters and is itself inconsistently reported.** PMID 41948127 infused over
   approximately six hours via an implanted catheter *"to avoid increasing intracranial pressure"* —
   and states that volume as 4 mL in Results and 3 mL in Methods.
2. **Primate DRG toxicity is tabulated at 1.2 × 10¹³ – 6 × 10¹³ vg per animal**, i.e. *below* the
   human intrathecal total of 1.2 × 10¹⁴ vg. Expressed as totals the primate dose looks smaller than
   the human one; expressed per CSF volume (macaque 15 cm³ against adult human 140 cm³) it is
   roughly an order of magnitude larger. **The same two numbers invert their order depending on the
   scalar.** This is the clearest demonstration in the wave that the scalar is not a presentational
   choice.

## 4 · Op — discovery_ledger_current.md

`op: APPEND` one lead at the end of the lead list of
`disease-models/wwox/research/discovery_ledger_current.md`. No `old` text; this is an append.

```
### DIS-xxx (provisional) — A CSF-route dose carried without its scalar is not a dose, and no published scalar yet converts an adult or primate dose to an infant one

**Tag:** INFERENZA
**Status:** open
**Created:** 2026-10-03 · intake wave 5, Scientist C (group C)
**Causal statement:** The CSF-route AAV9 literature expresses dose in three mutually non-convertible
ways - fixed total vector genomes per subject, vector genomes per gram of brain mass, and vector
genomes scaled by CSF volume - and comparisons across sources silently assume they are the same
quantity. They are not: a primate and a human dose can invert their rank order depending on which
scalar is used. The one published cross-species table of brain and CSF volumes available to this
wave is internally sound but carries a single, undated, adult human row, so it cannot convert any
of these into an infant dose.
**Reasoning chain:**
1. Two primate studies and every human trial indexed in this wave dose by fixed total vector genomes
   per subject; one human report doses per gram of brain mass; one preclinical programme scales by
   CSF volume.
2. The cross-species table's mouse and macaque CSF volumes independently reproduce that programme's
   stated 371-fold scaling factor to about one percent, so the table is usable between species.
3. The same table has one human row, with adult values and no age qualifier; the review's prose says
   paediatric CSF dynamics change rapidly with age and defers the detail to a supplement outside the
   body.
4. The approved human intrathecal product is a fixed total dose across ages two to under eighteen,
   while the same review names age among the top three drivers of variability in delivered dose at a
   CSF route.
5. Primate dorsal-root-ganglion toxicity is tabulated at per-animal totals below the human
   per-patient total, yet is far larger per unit CSF volume - the rank order inverts with the scalar.
**Counter-evidence / what would refute this lead:** if delivered dose at target turned out to be
governed by something that fixed totals capture adequately - for instance if the transduced
compartment saturates well below any dose in clinical use - then the choice of scalar would not
affect exposure where it matters. No source in this wave measures delivered dose at target in any
species, so this possibility is open.
**Falsifying experiment:** measure delivered vector at a defined CNS target across a range of
subject sizes at a fixed total dose. If target exposure is flat across sizes, fixed dosing is
defensible and this lead is refuted; if it scales inversely with CSF volume, it is confirmed.
Isotope-labelled capsid PET, which one source names as feasible, is the non-terminal route to this
measurement.
**Operational consequence (proposed, not a gate):** a dose carried into this repository from a
delivery source must carry its scalar in the same field, and a comparison between two doses on
different scalars must state the conversion used or decline to compare.
**Transfer limit to WWOX:** none of the six sources mentions WWOX; all are earned nulls for the gene.
This lead constrains how a dose could be set for a hypothetical CSF-route WWOX programme and asserts
nothing about what that dose should be.
**Links:** `research/intake_wave_20261003w5_C.md` §2.3; dossiers `PMID42205472.md` §3,
`PMID41948127.md` §7, `PMID42134074.md` §2.
**Not medical advice.**
```

## 5 · Verification note for the integrator

Table 4 above was extracted **by cell boundary** from the JATS table structure, not from flattened
running text. A first pass of this reading took it from flattened text, in which adjacent numeric
cells concatenate without a delimiter, and produced a wrong table plus a false criticism of the
source. That correction is recorded in `CC-20261003W5-C-CARRIED-NUMBER-INTEGRITY-01` and in the
PMID 42205472 dossier §3. **If this table is re-derived, re-derive it cell-wise.**

## 6 · LOCATOR TRIPLES FOR BLIND AUDIT

```
(A preclinical programme scaled its dose between species by cerebrospinal fluid volume | We chose low and high doses in NHPs based on the minimally effective dose (MED) and fully efficacious doses (FED) identified in CMT1A mice (2E11 total vg and 5E11 total vg, respectively) and scaled 371-fold for the increased CSF volume in monkeys compared to mice (Figures 2 and 3; Table S3). | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Results, 'Intrathecal delivery of AAV9.U6.miR871 to non-human primates')

(The infusion was deliberately slow because infused volume bears on intracranial pressure | Vector or formulation buffers were administered via catheter, implanted pre-study, as a single 4-mL intrathecal infusion over a 6-h period to avoid increasing intracranial pressure. | files/fulltext/PMID41948127_Stavrou2026_PMC.xml — Results, 'Intrathecal delivery of AAV9.U6.miR871 to non-human primates')

(A human intracisternal dose was expressed per gram of brain mass rather than as a total | Following successful computed tomography (CT)-guided access to the cisterna magna with a 25-gauge neonatal spinal needle, 1E−10 vector genome copies/g brain mass (1.265E−13 genome copies) of RGX-111 in 5 mL of Elliotts B artificial CSF was injected over 5 min without adverse effects. | files/fulltext/PMID41966056_Wang2026_PMC.xml — Results, 'Clinical outcomes', dosing paragraph)

(A review states that fixed dosing is current practice and that a cerebrospinal-fluid route requires individualised consideration of pathway patency and ventricular volume instead | In the case of intraventricular therapies, dosing considerations may need to include factors such as the patency of the pathways and estimated ventricular volume (at a minimum), much as a pediatric dosing schedule is adjusted according to weight. | files/fulltext/PMID42205472_Engelhard2026_PMC.xml — Additional factors in physiological CSF flow variability, 'Effects of age and sex on CSF flow')

(The same review names age among the three largest drivers of variability in cerebrospinal-fluid circulation and therefore in delivered dose | According to a synthesis of the currently available literature, the most significant factors expected to cause variability of CSF macrocirculation would be overall CSF production, anatomical pathway variation, and age. | files/fulltext/PMID42205472_Engelhard2026_PMC.xml — Additional factors in physiological CSF flow variability, synthesis)

(The paediatric detail of that review is deferred to a supplement outside the body of the article | A more detailed consideration of CSF flow dynamics in the pediatric population is provided in Supplementary Material 2. | files/fulltext/PMID42205472_Engelhard2026_PMC.xml — Additional factors in physiological CSF flow variability, 'Effects of age and sex on CSF flow')

(Isotope-labelled capsid imaging is named as a non-terminal route to quantifying biodistribution in a living subject | More recently, antibodies and AAV9 capsids (as examples) can be labeled with PET isotopes such as carbon-11, fluorine-18, and zirconium-89, enabling noninvasive tracking and quantitative biodistribution studies in vivo, including after intraventricular administration (Pandit-Taskar et al., 2019; Allen et al., 2022; Bansal et al., 2025). | files/fulltext/PMID42205472_Engelhard2026_PMC.xml — Diseases affecting CSF flow, 'Direct assessment of the movement of therapeutic agents through the CSF')
```

**Artefacts confirmed on disk before writing these triples:**
`files/fulltext/PMID41948127_Stavrou2026_PMC.xml`,
`files/fulltext/PMID41966056_Wang2026_PMC.xml`,
`files/fulltext/PMID42205472_Engelhard2026_PMC.xml`. Digests are recorded in full in the
corresponding deep-dive manifests, each of which passes
`deepdive_manifest.py --pmid N --verify-artifacts`.

> Note for the auditor: the table in §2 is **not** offered as a locator triple, because it is a
> table and not a sentence. If it is to be audited, it should be re-extracted cell-wise from
> `files/fulltext/PMID42205472_Engelhard2026_PMC.xml`, table-wrap index 3, and compared.

---

## BATCH DISPOSITION — `BATCH_20261003_004` (2026-10-03, ACTOR_ID `scientist`, Scientist I), append-only

**Nothing above this line was rewritten.** Operator standing authorisation, verbatim: *«procedi sempre»*.

**Verdict:** PROPAGATED as **`DL-METH-117`** · class **MINOR**.

**Renumbered:** the op declared a provisional `DIS-xxx` in the discovery ledger, whose sequence runs `DL-<CATEGORY>-NNN` and stood at **116**; the integrator assigned the next free number in that sequence.

**Not a duplicate of `CC-20261003W5-A-DOSE-TWO-SIDED-01`** — measured, not assumed: disjoint source sets and no shared proposition. Both landed.

**Two integrator amendments (blind audit).** (1) The human intracisternal dose is printed per gram of brain mass **with an absolute total in parentheses**, so per-gram is the primary expression rather than the only one. (2) The review's inadequacy-of-fixed-dosing statement is about **intraventricular** therapies, is hedged, and draws on non-paediatric trials — the lead's claim is about what a carried number means, not about what the review prescribes.

The Table 4 figures were carried **as the candidate re-derived them cell-wise** from the JATS table structure (`Rat | 2.2 | 20 | 0.15 | 1 | 9.5`), not from flattened text.

**Not medical advice.**
