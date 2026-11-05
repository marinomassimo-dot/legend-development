# Module inputs proposed by package B1 (sb-b1, 2026-11-05)

Nothing here was applied. Every item is a proposal for the consumer that owns the file named at
the head of each block; the owning files were not opened for writing by this package. Row ids
refer to `evidence_b1.tsv` in this directory. No administered-dose number appears in any
proposal, and no proposal carries an individual-level record.

---

## 1 · Card `H02_gabaat_inactivator_myelin_exposure.packet.json` — new `drug_assertions`

Vocabulary as in the packet: `id`, `target_id`, `endpoint`, `direction`, `source`, `locator`,
`epistemic_status`, `reading_depth`, `context` (`disease_id`, `genotype`, `species`,
`cell_type`, `developmental_stage`), `evidence_scope`, `note`. Every row below is
`NOT WWOX EVIDENCE` and `OTHER_DISEASE_PRECEDENT` unless stated.

| proposed id | target_id | endpoint | direction | source and depth | rests on |
|---|---|---|---|---|---|
| DR-H02-012 | brain_MRI_abnormality | rate of the MRI abnormality in children given vigabatrin for infantile spasms, by aetiology | INCREASE | PMID 36601084, `partial_fulltext_read`, receipt `FTR-20261105-36601084-23` | B1-01, B1-04 |
| DR-H02-013 | brain_MRI_abnormality | association of age at first exposure, peak amount, cumulative amount and duration with the MRI abnormality | UNDETERMINED | PMID 36601084, `partial_fulltext_read` | B1-02, B1-03 |
| DR-H02-014 | brain_MRI_abnormality | detectability of the MRI abnormality against an already abnormal baseline | UNDETERMINED | PMID 36601084 Discussion, `partial_fulltext_read` | B1-07 |
| DR-H02-015 | brain_MRI_abnormality | whether a delayed-myelination baseline predisposes to the MRI abnormality | NO_CHANGE | PMID 40527948, `abstract_only`, receipt `FTR-20261105-40527948-23` | B1-09 |
| DR-H02-016 | brain_MRI_abnormality | aetiology class of children with and without the MRI abnormality | INCREASE for genetic aetiology, hypothesis-generating | PMID 42735667, `abstract_only` | B1-11 |
| DR-H02-017 | brain_MRI_abnormality | peak against cumulative exposure for the asymptomatic and the symptomatic form | INCREASE for peak, UNDETERMINED for the symptomatic form | PMID 28230253, `abstract_only` | B1-12 |
| DR-H02-018 | brain_MRI_abnormality | cerebrospinal and spectroscopic GABA concentration in children with and without the MRI abnormality | INCREASE | PMID 35183975, `abstract_only` | B1-17 |
| DR-H02-019 | CNS_myelination | optic-nerve fractional anisotropy during exposure and after stopping | DECREASE during exposure, RECOVERY after stopping | PMID 40670421, `partial_fulltext_read` | B1-18 |
| DR-H02-020 | CNS_myelination | myelin staining, myelin and oligodendrocyte enzyme activity and myelin basic protein in the immature rat, with a drug-free period | DECREASE, partial recovery only | PMID 10840396, `abstract_only` | B1-23 |
| DR-H02-021 | CNS_myelination | myelin staining, axonal degeneration, glial death and astrogliosis in the immature rat at low exposure | DECREASE | PMID 9168839, `abstract_only` | B1-24 |
| DR-H02-022 | intramyelinic_edema_vacuolation | microvacuolation after a twelve-week drug-free period in the adult rat | INCREASE, not fully reversed | PMID 15150739, `abstract_only` | B1-25 |
| DR-H02-023 | intramyelinic_edema_vacuolation | neuropathological examination of 62 people on long-term exposure and five earlier human specimens | NO_CHANGE | PMID 1940119 and PMID 2767014, `abstract_only` | B1-22, B1-27 |
| DR-H02-024 | intramyelinic_edema_vacuolation | myelinated-fibre toxicity of vigabatrin and of GABA in a myelinating explant culture | INCREASE for both agents, no intramyelinic oedema | PMID 2757909, `abstract_only` | B1-28 |
| DR-H02-025 | CNS_myelination | clinical severity of an autoimmune demyelination model under GABA injection against vigabatrin | INCREASE for GABA, DECREASE for vigabatrin | PMID 23194644, `abstract_only` | B1-29 |
| DR-H02-026 | CNS_myelination | white-matter endpoint in the only juvenile exposure study of CPP-115 | NOT_MEASURED | PMID 24321005, `partial_fulltext_read` | B1-33 |
| DR-H02-027 | CNS_myelination | white-matter endpoint for OV329 in two full texts | NOT_MEASURED | PMID 34617595 and PMID 38937107, `queried_not_full_read` | B1-34 |
| DR-H02-028 | CNS_myelination | myelination score and myelin transcripts under a genetic block of GABA catabolism (not a drug exposure) | DECREASE | PMID 40741980, `partial_fulltext_read` | B1-30 |
| DR-H02-029 | CNS_myelination | myelination on imaging and post mortem under biallelic loss of the enzyme the drug inactivates (not a drug exposure) | DECREASE | PMID 27376954, `abstract_only` | B1-31 |

Two rows that already exist should gain a note rather than a new id:

* DR-H02-005 (the label row): add that the label's sections are consistent with the
  independent cohorts read here, whose rates in exposed infants run from 22.1 to 44.7 percent
  across four cohorts (B1-01, B1-08, B1-11, B1-13), and that one cohort found the pattern in
  7 of 52 children never exposed (B1-35).
* DR-H02-009 (the single sibling case): add that the sibling's juvenile animal study measured
  no white-matter endpoint (B1-33), so the sibling has no brain-myelin measurement in any
  species at any age (B1-32, B1-34).

## 2 · Card `H02` — text fields

* `mechanism`: append the GABA-axis paragraph. Proposed wording, DATO plus INFERENZA kept
  apart: two genetic conditions that raise brain GABA without any drug — a block of GABA
  catabolism downstream of the target, and biallelic loss of the target itself — are both
  associated with reduced myelination, the first in the same regions where the drug
  abnormality appears (B1-30, B1-31); GABA alone reproduced the mild myelinated-fibre
  toxicity of the drug in an explant culture (B1-28); and cerebrospinal free GABA was higher
  in the two children with the abnormality than in those without (B1-17). INFERENZA: the
  liability is better described as a property of raised GABA in a myelinating brain than as a
  property of the vigabatrin molecule, which makes it a class question for every inactivator
  and not a vigabatrin-only question. IPOTESI and its discriminator: if the axis is GABA, a
  sibling that reaches the same brain GABA elevation should reproduce the lesion at matched
  target engagement; the experiment that would discriminate is a matched-engagement
  comparison of two inactivators in the same juvenile model with the same white-matter
  readout. No source read measures it.
* `evidence_against`: add the three human negatives — no myelin microvacuolation or sheath
  splitting in 62 people examined after long-term exposure (B1-22), no vacuolation in five
  earlier human specimens with the animal lesion absent in primates (B1-27), and a negative
  autopsy in a term infant exposed from the neonatal period with a malformed brain (B1-21) —
  and the one model with pre-existing myelin pathology in which the drug was given, where it
  did not worsen the outcome (B1-29).
* `not_known`: replace "Whether a Wwox-deficient juvenile brain is more, equally or less
  susceptible" with the same sentence plus the one human test that exists: a cohort of 76 in
  which a delayed-myelination baseline did not appear to predispose (B1-09), abstract level,
  myelination graded from routine reports, no stated power.
* `status`: keep `controversial`. Harm tag at card level: the card should carry a harm tag for
  vigabatrin and an explicit `undetermined` for the siblings, never a shared tag. Reason: for
  vigabatrin the imaging liability is established in four independent cohorts and the immature
  animal myelin endpoint recovers only partially (B1-23, B1-25), while for CPP-115 and OV329
  the white-matter endpoint has never been measured (B1-32, B1-33, B1-34), and an unmeasured
  endpoint is not a clean one.
* `question_history`: add this package, its question and the two bounded nulls (B1-37, B1-38).

## 3 · `needs/needs.json`, need `NEED-MYELINATION`

* `counter_evidence`: add one entry. Proposed text: the drug-side white-matter question that
  this need carries is partly answered outside WWOX — in the immature rat the myelin content
  endpoint recovers only partially after a drug-free period while imaging and vacuolation
  resolve (B1-23, B1-25), and in the one human cohort that tested it a delayed-myelination
  baseline did not predispose to the imaging abnormality (B1-09); no study has given any
  inactivator of this class to a hypomyelinating or myelin-mutant animal (B1-37) or to any
  WWOX system (B1-38).
* `intervention_direction.do_not_assume`: add that an exposure that raises brain GABA during
  the myelination window is a candidate myelin stressor in its own right (B1-28, B1-30,
  B1-31), so a GABA-raising symptomatic lever and a pro-myelinating aim can pull against each
  other; the sign in a WWOX brain is undetermined in both directions.
* `observed`: no new observation is proposed. This package read no WWOX source and adds no
  WWOX observation.

## 4 · `view/work_order.json`, entry `NEED-MYELINATION`

Proposed replacement for `data`, stated qualitatively and with no amounts: card H02 next
measurement, with the exposure series written as windows rather than levels. Three start
windows in a juvenile model that survives them — before the onset of myelination, at its
steepest phase, and after its peak — each with a matched vehicle arm in both genotypes, one
exposure level carried unchanged across windows, a recovery arm at twice the exposure duration
after the last administration, and three readouts that the human literature shows separate:
imaging signal change, which resolves; vacuolation on electron microscopy, which resolves
incompletely in the adult rat; and myelin content by electron microscopy g-ratio with a myelin
protein, which recovered only partially in the immature rat. Confirmed brain exposure in both
genotypes, blinded reading, and a pre-planned genotype-by-window interaction test. The dog and
rat start-age evidence that motivates the windows is abstract level only, so the series tests
it rather than assuming it.

Proposed replacement for `would_change`: unchanged in substance, with one addition — a clean
absence of added injury moves H02 to a position without WWOX-specific harm rows but cannot
clear the class, because the human negative that matters most (a delayed-myelination baseline
not predisposing) is abstract level in a cohort of 76 and the siblings have no white-matter
measurement at all.

Proposed addition to `feasibility`: a human denominator route exists that needs no new
measurement: three cohorts now report aetiology class against the imaging abnormality
(B1-04, B1-11, B1-16), so a structured count of WWOX-DEE children exposed, imaged and
followed could be read against the published aetiology strata rather than against a single
pooled rate.

## 5 · `proposed_registry_changes` (plain statements; nothing was changed)

1. The working-model sentence on the vigabatrin imaging abnormality in WWOX-DEE (the position
   corrected in BATCH_20261019_025, carried through CLAIM 001) should gain one clause: the
   same imaging pattern is reported in other genetic encephalopathies, including one whose
   baseline MRI carries delayed myelination and callosal hypoplasia (B1-19) and one with a
   GABA-pathway gene (B1-20), so the co-occurrence of this pattern with a hypomyelinating
   baseline is not WWOX-specific.
2. CLAIM 001, efficacy and safety sides: no change of sign is proposed. A note is proposed
   recording that four independent exposed cohorts put the rate between 22.1 and 44.7 percent
   and that one cohort found the pattern in children never exposed, so a WWOX count without a
   denominator cannot be read as an excess.
3. The premise that "start age decides" (carried in the work order text for
   `NEED-MYELINATION` and in card H02) should be split by species and by depth: in animals it
   rests on abstract-level rat-window and dog start-age studies; in humans it is supported by
   one cohort and a pooled review and is not reproduced as an independent factor in either
   human cohort read here at full text. Proposed status: `premise_partially_supported,
   species-split`, with the human half flagged as contested rather than established.
4. No new claim id is proposed. Nothing read here is a WWOX measurement, so no row of this
   package is eligible for the claim registry as WWOX evidence.
5. `NEED-INHIBITORY-HYPOFUNCTION` keeps its uncertain direction; this package adds no
   evidence on whether raising GABA helps or harms seizure control in this disease.
