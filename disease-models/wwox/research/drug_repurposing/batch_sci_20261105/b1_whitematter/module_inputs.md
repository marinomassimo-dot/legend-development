# Module inputs proposed by package B1 (sb-b1; first pass 2026-11-05, corrected 2026-11-06)

Nothing here was applied. Every item is a proposal for the consumer that owns the file named at
the head of each block; the owning files were not opened for writing by this package. Row ids
refer to `evidence_b1.tsv` in this directory. No administered-dose number appears in any
proposal, and no proposal carries an individual-level record.

Corrected after the adversarial review (`verify/review_B/`): `direction` now uses only the card
vocabulary INCREASE, DECREASE, UNKNOWN, NO_CHANGE with no compound strings; needs `direction`
uses only up, down, restore, modulate, uncertain; the request for a card-level harm tag is
withdrawn (no such field exists and the module computes the position); the two drug-free genetic
conditions have been moved out of `drug_assertions`; and the sign inversion in the
autoimmune-model row is repaired.

---

## 1 · Card `H02_gabaat_inactivator_myelin_exposure.packet.json` — new `drug_assertions`

Vocabulary as in the packet: `id`, `target_id`, `endpoint`, `direction`, `source`, `locator`,
`epistemic_status`, `reading_depth`, `context`, `evidence_scope`, `note`. Every row is
`NOT WWOX EVIDENCE` and `OTHER_DISEASE_PRECEDENT` unless stated. `direction` is one of
INCREASE, DECREASE, UNKNOWN, NO_CHANGE; every qualification belongs in `note`, never in the
direction field.

| proposed id | target_id | endpoint | direction | source and depth | rests on |
|---|---|---|---|---|---|
| DR-H02-012 | brain_MRI_abnormality | rate of the abnormality among children imaged during exposure, by aetiology | INCREASE | PMID 36601084, `partial_fulltext_read`, receipt `FTR-20261105-36601084-23` | B1-01, B1-04 |
| DR-H02-013 | brain_MRI_abnormality | association of age at first exposure, peak amount, cumulative amount and duration with the abnormality, in a cohort whose exposure began almost entirely under 12 months | UNKNOWN | PMID 36601084, `partial_fulltext_read` | B1-02, B1-03 |
| DR-H02-014 | brain_MRI_abnormality | detectability of the abnormality against an already abnormal baseline | UNKNOWN | PMID 36601084 Discussion, `partial_fulltext_read` | B1-07 |
| DR-H02-015 | brain_MRI_abnormality | whether a delayed-myelination baseline predisposes to the abnormality | UNKNOWN | PMID 40527948, `abstract_only`, receipt `FTR-20261105-40527948-23` | B1-09 |
| DR-H02-016 | brain_MRI_abnormality | aetiology class of children with and without the abnormality | UNKNOWN | PMID 42735667, `abstract_only` | B1-11 |
| DR-H02-017 | brain_MRI_abnormality | peak against cumulative exposure for the asymptomatic form | INCREASE | PMID 28230253, `abstract_only` | B1-12 |
| DR-H02-018 | brain_MRI_abnormality | cerebrospinal and spectroscopic GABA concentration in children with and without the abnormality | INCREASE | PMID 35183975, `abstract_only`; the spectroscopic ratio did not differ significantly between children with and without the abnormality (p = 0.31, two against eleven children); only the cerebrospinal free GABA difference (p = 0.03) and the higher ratio under the drug than in controls (p = 0.02) were significant | B1-17 |
| DR-H02-019 | optic_nerve_diffusion_metric | optic-nerve fractional anisotropy during exposure and after stopping | DECREASE | PMID 40670421, `partial_fulltext_read` | B1-18 |
| DR-H02-020 | CNS_myelination | myelin staining, myelin and oligodendrocyte enzyme activity and myelin basic protein in the immature rat, with a drug-free period | DECREASE | PMID 10840396, `abstract_only` | B1-23 |
| DR-H02-021 | CNS_myelination | myelin staining, axonal degeneration, glial death and astrogliosis in the immature rat at low exposure | DECREASE | PMID 9168839, `abstract_only` | B1-24 |
| DR-H02-022 | intramyelinic_edema_vacuolation | microvacuolation after a twelve-week drug-free period in the rat | INCREASE | PMID 15150739, `abstract_only` | B1-25 |
| DR-H02-023 | intramyelinic_edema_vacuolation | neuropathological examination of 62 people on long-term exposure and five earlier human specimens | NO_CHANGE | PMID 1940119 and PMID 2767014, `abstract_only` | B1-22, B1-27 |
| DR-H02-024 | intramyelinic_edema_vacuolation | myelinated-fibre toxicity of vigabatrin and of GABA in a myelinating explant culture | INCREASE | PMID 2757909, `abstract_only` | B1-28 |
| DR-H02-025a | clinical_disease_severity_autoimmune_demyelination | clinical severity score of an autoimmune demyelination model under exogenous GABA | INCREASE | PMID 23194644, `abstract_only` | B1-29 |
| DR-H02-025b | clinical_disease_severity_autoimmune_demyelination | clinical severity score of the same model under vigabatrin | DECREASE | PMID 23194644, `abstract_only` | B1-29 |
| DR-H02-026 | CNS_myelination | white-matter endpoint in the only juvenile exposure study of CPP-115 | UNKNOWN | PMID 24321005, `partial_fulltext_read` | B1-33 |
| DR-H02-027 | CNS_myelination | white-matter endpoint for OV329 in the two reachable articles | UNKNOWN | PMID 34617595 and PMID 38937107, `queried_not_full_read` | B1-34 |
| DR-H02-030 | brain_MRI_abnormality | prevalence of the abnormality in exposed against naive infants, and in exposed against naive children aged 2 to 16 and adults | INCREASE in infants, NO_CHANGE in the older bands | PMID 19054414, `abstract_only`, receipt `FTR-20261106-19054414-23` | B1-39 |
| DR-H02-031 | brain_MRI_abnormality | age at examination, therapy duration and peak amount in children with and without the abnormality | INCREASE | PMID 18783433, `abstract_only` | B1-40 |
| DR-H02-032 | brain_MRI_abnormality | rate and risk factors with an unexposed comparison group | INCREASE | PMID 20384718, `abstract_only` | B1-41 |
| DR-H02-033 | brain_MRI_abnormality | time course of the abnormality after the start of exposure | INCREASE | PMID 19258289, `abstract_only` | B1-42 |
| DR-H02-034 | sibling_tissue_accumulation | concentrations of OV329 and vigabatrin in plasma, brain, eyeball and retina after a two-day mouse infusion, and the location of the sibling toxicology record | UNKNOWN | PMID 42470358, `partial_fulltext_read`, receipt `FTR-20261106-42470358-23` | B1-43 |
| DR-H02-035 | CNS_myelination | oligodendrocyte lineage cell number and myelination under endogenous GABA acting on GABA-A receptors | DECREASE | PMID 27796063, `abstract_only` | B1-44 |
| DR-H02-036 | CNS_myelination | precursor differentiation, myelin protein and remyelination under GABA-B engagement | INCREASE | PMID 35980256 and PMID 31349008, `abstract_only` | B1-45, B1-46 |
| DR-H02-037 | retinal_function_ERG | retinal lesion components, plasma taurine, and the effect of darkness and of taurine supplementation | DECREASE in plasma taurine | PMID 19194884, `abstract_only` | B1-47 |
| DR-H02-038 | taurine_transport | taurine uptake in intestinal and renal cell models under vigabatrin | DECREASE | PMID 25062867, `abstract_only` | B1-48 |

Notes required on three of these rows:

* DR-H02-016 must carry the caveat that the two children of the WWOX imaging report cannot be
  excluded from that same cohort on the published record, so this row is **not** independent
  corroboration of the WWOX observation; the question belongs to package A1.
* DR-H02-019 must state that a diffusion metric of the optic nerve is not a myelination
  measurement and that the tract is also the retinotoxicity target. Its `target_id` is therefore
  the metric, not `CNS_myelination`.
* DR-H02-034 must state that the sibling was below the assay's limit of quantitation in brain as
  well as in the eye, so the comparison supports no brain inference in either direction, and that
  the toxicology package itself was not read.

Two rows that already exist should gain a note rather than a new id:

* DR-H02-005 (the label row): add that three independent centres put the rate among imaged
  children between 22.1 and 44.7 percent, that the one cohort reporting its exposed denominator
  gives about 26 percent per exposed child, and that unexposed comparators exist (7 of 52 in one
  cohort; 4 percent of naive infants in the controlled study).
* DR-H02-009 (the single sibling case): add that the sibling's juvenile animal study measured no
  white-matter endpoint and that the OV329 toxicology package is described only in
  subscription-only reports, so the sibling endpoint is unmeasured by any reachable route.

## 2 · Card `H02` — text fields

* `mechanism`: append a paragraph that leaves the GABA direction **unsigned**. DATO: GABA alone
  reproduced a mild myelinated-fibre toxicity in culture without producing intramyelinic oedema;
  cerebrospinal GABA was higher in two cases, both preterm with post-haemorrhagic hydrocephalus;
  two genetic conditions that raise GABA show reduced myelination, with gamma-hydroxybutyrate
  correlating almost as strongly in one; endogenous GABA acting on GABA-A receptors reduces
  oligodendrocyte lineage number and myelination, while GABA-B engagement accelerates precursor
  differentiation and promotes remyelination; and vigabatrin depletes taurine and inhibits taurine
  transport, with taurine deficiency reported as the cause of its retinal lesion. INFERENZA: the
  liability may be a property of raised GABA in a myelinating brain, but the axis has opposite
  signs by receptor class and a molecule-specific rival exists, so neither a class reading nor a
  molecule reading is established. IPOTESI and its discriminator: a matched-engagement comparison
  of two inactivators in one juvenile model with one white-matter readout, plus receptor-subtype
  arms. No source read measures it.
* `evidence_against`: add only what the card does not already hold — the three human negatives
  (62 examined after long-term exposure; five earlier specimens with the animal lesion reported
  absent in primates; a negative autopsy in a term infant exposed from the neonatal period), the
  autoimmune-model dissociation, and the GABA-B rows. The hormonal rival, the caution against
  reading retinal gentleness as myelin gentleness and the lethal highest arm of the rat spasm
  model are already on the card and are cited, not repeated.
* `not_known`: replace "Whether a Wwox-deficient juvenile brain is more, equally or less
  susceptible" with the same sentence plus: in the one cohort that compared it, a
  delayed-myelination baseline **did not demonstrate** an excess (76 children, abstract level,
  myelination graded from routine reports, no stated power), while one case report describes delayed
  myelination reported in the same examination as the pattern, on a normal initial MRI. Add that the OV329 toxicology package exists and is
  unread.
* `status`: keep `controversial`. **No card-level harm tag is proposed**: no such field exists in
  any packet card, and the module carries this through `p4_card.status`, the counter-evidence rows
  and the computed positions. The work order already registers that demonstrated added injury in a
  Wwox-deficient model is what would make a card-level C3 for vigabatrin; this package does not
  pre-empt it. The siblings stay UNKNOWN on the white-matter endpoint and never share vigabatrin's
  rows.
* `question_history`: add this package, its question, the two bounded-null attestations and the
  correction round with its audit and review verdicts.

## 3 · `needs/needs.json`, need `NEED-MYELINATION`

* `counter_evidence`: add one entry. Proposed text: the drug-side white-matter question is partly
  addressed outside WWOX — in the immature rat the myelin content endpoint recovers only partially
  after a drug-free period while the qualitative images and the vacuolation resolve and regional
  T2 stays elevated (B1-23, B1-25); in the one cohort that compared it, a delayed-myelination
  baseline did not demonstrate an excess (B1-09, abstract level, graded from routine reports, no
  stated power); and no study has given any inactivator of this class to a hypomyelinating or
  myelin-mutant animal (B1-37) or to any WWOX system (B1-38).
* `intervention_direction.do_not_assume`: add that an exposure raising brain GABA during the
  myelination window is a candidate myelin stressor **whose sign is unresolved**, since GABA-A
  signalling reduces oligodendrocyte lineage number and myelination while GABA-B signalling
  promotes differentiation and remyelination (B1-44, B1-45, B1-46).
* `intervention_direction.direction` is unchanged: `restore`. No new value is proposed, and
  `observed` is untouched because no WWOX source was read.

## 4 · `view/work_order.json`, entry `NEED-MYELINATION`

Proposed replacement for `data`, stated qualitatively and with no amounts: card H02 next
measurement with the exposure series written as windows rather than levels. Three start windows in
a juvenile model that survives them — before the onset of myelination, at its steepest phase, and
after its peak — each with a matched vehicle arm in both genotypes, one exposure level carried
unchanged across windows, a recovery arm at twice the exposure duration after the last
administration, and three readouts that **the two rat studies** show separate: imaging signal
change including a quantitative measure, since the qualitative images normalised in the immature
rat while regional T2 did not; vacuolation on electron microscopy, which resolved incompletely in
the adult rat; and myelin content by g-ratio with a myelin protein, which recovered only partially
in the immature rat. The human record covers imaging alone. Confirmed brain exposure in both
genotypes, blinded reading, and a pre-planned genotype-by-window interaction test. A
receptor-subtype arm is worth adding, because GABA-A and GABA-B engagement move myelination in
opposite directions. The dog and rat start-age evidence that motivates the windows is abstract
level only, so the series tests it rather than assuming it.

**Flagged as an explicit amendment to a pre-registered sentence, not as a non-change:**
`would_change` currently reads that a clean absence of added injury would move H02 "to a position
without harm rows". The proposed amendment is to read "without WWOX-specific harm rows", because a
clean absence in a Wwox-deficient model would not clear the class: the cohort-level human negative
is abstract level in 76 children and the siblings have no reachable white-matter measurement. The
owner of the file should treat this as an amendment and accept or refuse it as such.

Proposed addition to `feasibility` (kept as written in the first pass, and the most useful item
here): a human denominator route exists that needs no new measurement — four cohorts now report
aetiology class against the imaging abnormality (B1-04, B1-11, B1-16, B1-41), so a structured
count of WWOX-DEE children exposed, imaged and followed could be read against the published
aetiology strata and against the unexposed comparators (B1-35, B1-39) rather than against a single
pooled rate.

## 5 · `proposed_registry_changes` (plain statements; nothing was changed)

1. The working-model sentence on the vigabatrin imaging abnormality in WWOX-DEE (the position
   corrected in BATCH_20261019_025, carried through CLAIM 001) should gain one clause: the same
   imaging pattern is reported in other genetic encephalopathies, including one whose baseline MRI
   carries delayed myelination and callosal hypoplasia (B1-19) and one in which a concurrent
   systemic metabolic deficiency was proposed as a co-factor (B1-20), so the co-occurrence of this
   pattern with a hypomyelinating baseline is not WWOX-specific. Separately, one cohort reports
   GABA-receptor subunit variants in both its groups (B1-11); that cohort may contain the two
   children of the WWOX report and is not independent corroboration of it.
2. CLAIM 001, efficacy and safety sides: no change of sign is proposed. A note is proposed
   recording that three independent centres put the rate among imaged children between 22.1 and
   44.7 percent, that the one cohort reporting its exposed denominator gives about 26 percent per
   exposed child, and that the same pattern occurs in children never exposed (7 of 52 in one
   cohort; 4 percent of naive infants in a controlled study), so a WWOX count without a
   denominator cannot be read as an excess.
3. The premise "start age decides" should be split by species and by depth, with **both halves
   supported and neither confirmed at full text here**: in animals it rests on abstract-level
   rat-window and dog start-age studies whose full texts were unreachable; in humans it is
   supported by a controlled, blinded cross-age study and three further cohorts, and is not
   reproduced in one cohort whose exposure began almost entirely under 12 months and therefore
   cannot test a within-infancy window. Proposed status: `premise_supported_species_split`, human
   half supported at cohort level, animal half abstract-level only.
4. No new claim id is proposed. Nothing read here is a WWOX measurement, so no row of this package
   is eligible for the claim registry as WWOX evidence.
5. `NEED-INHIBITORY-HYPOFUNCTION` keeps its uncertain direction; this package adds no evidence on
   whether raising GABA helps or harms seizure control in this disease.
