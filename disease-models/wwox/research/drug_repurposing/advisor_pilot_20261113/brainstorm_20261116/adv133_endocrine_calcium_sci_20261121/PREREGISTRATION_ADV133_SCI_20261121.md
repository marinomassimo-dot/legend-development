# ADV-133 strand 1, pre-registration: early endocrine-calcium axis of the Wwox-null pup (SCI, 2026-11-21; written and committed before any source of this strand is read; hypothesis level; no dose; reference genotype class only; not medical advice)

Assignment: `assignments/ADV-133.md` (owner SCI, method autonomy SCI). Strand 2 (ErbB4/NRG1 handle question) does not start before this strand closes with its sentence.

## 1. What is fixed before reading
**Question.** Is a systemic endocrine, calcium or nutritional deficit present in Wwox-null pups before the first spike (about P9), and if so does a lever class with pup exposure facts (hormone-axis, supplement or dietary classes) enter the pharmacological comparison, or does it only accompany the seizures?

**Discriminating observation (the one that decides).** Serum total calcium, ionised calcium, and any steroid or hormone measure (corticosterone, growth hormone, IGF-1, parathyroid hormone, vitamin D metabolites, thyroid axis), in Wwox-null pups against wild type, measured at P7 to P14, set against the seizure timeline (first spikes about P9 in the neuron-targeted line; ECoG in the germline null begins about P14; death about P20 to P25).

**Outcome rules (written now):**
| Reading | Sentence this strand will carry |
|---|---|
| Normal calcium (and hormone measures) at ages that already have seizures or the growth lag | The strand is closed for this lever class; the sentence says so and names the ages and the n. |
| Low or abnormal BEFORE onset (P7 to P8, or before the first measured spike) and not explained by undernutrition | A hormone-axis or supplement lever class enters the comparison with exposure facts and harms. |
| Abnormal only AFTER onset | A consequence of the seizure or feeding state, not a driver, not a lever. |
| Abnormal at P7 to P14 but undernutrition not excluded | A named confound: the sign is carried as "not separable from feeding", with the cheapest separating measurement. |
| Not measured at those ages in any held or reachable source | A MISSING MEASURE, named, with the cheapest measurement that would settle it (serum calcium and albumin with body weight and milk-spot at P7, P9, P11 in a line that already exists). |

**Rejecting observation for the lever class.** Normal serum calcium and hormone values at P7 to P14 in a primary that states n, age, genotype and units. One such row closes the strand for the measured axis only; it does not close the axes it did not measure.

## 2. The rival declared in advance: undernutrition (the D4 feeding artefact)
Sicker pups suckle less, so a low calcium, low glucose or low hormone value can be a consequence of intake, not a primary endocrine sign (DISCOVERY_TRACE D4; ADV pointer 1). I will tell a primary sign from an undernutrition consequence only by what the sources show:
1. **Age of the sign against the growth lag and the seizure timeline.** The germline null's weight lag is reported from day 4 (ADV-101 table); a calcium sign no earlier than the weight lag is not separable from feeding.
2. **Albumin.** Total calcium follows albumin; the reported hypoalbuminemia (Aqeilan 2008 as quoted by one producer) would lower total calcium without a change in ionised calcium. Total calcium alone cannot carry a lever claim; ionised or albumin-corrected calcium is required, or the row is downgraded.
3. **Pattern.** Undernutrition predicts low glucose, low insulin, low IGF-1, raised GH and raised corticosterone together; a primary hormone-axis defect predicts a different pattern (for example low PTH or low vitamin D metabolites with preserved weight-for-age). Only a pattern read from the same animals counts.
4. **Rescue evidence.** Neuronal restoration normalising the sign together with weight and feeding supports "downstream of CNS state"; it does not separate feeding from endocrine control (same reasoning as ADV-101: all arms move together).
Any held source that has a cross-fostering, pair-fed or milk-spot arm is the only one that can separate these; absence of such an arm is recorded, not filled.

## 3. Counters carried, not discarded
* lde/lde rat serum constituents normal at 28 days (Suzuki 2009 as quoted in a dossier): later age, other species, other allele, and cited to an earlier paper that is not held, whose abstract reports raised urea nitrogen, creatinine and phosphate and lower GH (ADV-074, ADV-101). It cannot carry a dissociation until the earlier paper is read; it also does not support a normal-at-P7-to-P14 sentence.
* A hypocalcaemia relay in the harm-against-phenotype note (ADV-079) has its primary (Aqeilan 2008) absent; that note's wording stays "relay, primary absent" until reconciled below.
* Calcium is, in ADV-079, a HARM axis (lithium and others). A finding of low calcium would therefore both open a lever class and weaken some comparators; the note will state both directions.

## 4. Reconciliation of Aqeilan 2008 first (ADV-133 step 1)
One producer quotes the paper (hypoproteinemia, hypoalbuminemia, hypoglycemia, hypocalcemia, hypotriglyceridemia, hypocholesterolemia, no liver, pancreas, gut or kidney lesions); another lists it absent by two routes. Rule fixed now: an absence claim needs two routes; a challenge page is a STOP for that route and is recorded as the route result, never as a finding; a quote carried second-hand is marked second-hand until read in the source. Age of the animals and n in that paper are read before any number is used.

## 5. Comparisons this could change (stated before the result)
* **Bridge group:** a lever class no antiseizure agent represents; and, if calcium is low before onset, a confound for seizure-suppressant readouts (hypocalcaemia is itself a seizure provoker).
* **Harm-against-phenotype (ADV-079):** calcium as a harm axis for lithium and others.
* **By-endpoint survival comparison:** a systemic non-seizure contribution to death would separate survival from seizure control; DISCOVERY_TRACE 7.4 noted that calcium, acidosis, haematology and bone were never measured in treated animals.
If the strand closes with the normal-calcium sentence, none of these changes and the sentence is the deliverable.

## 6. Method, effort and perimeter
Held files first (counted grep, then read the closest notes whole): ADV-074 R4 report, ADV-079 note, ADV-101 note; Wwox primaries on the axis: Aqeilan 2008, Suzuki 2009 (abstract level so far), Repudi 2021 appendix tables on bone, Obeid 2026 supplementary S5 and S6, Hussain 2023 supplementary S2. Complete reads with FULLTEXT_READ_RECEIPT and verbatim locators for every number used; ages, denominators, significance and marker-versus-function stated at the first pass (ADV-123 verifier corrections). One delegate at a time, model and effort stated in every dispatch and read back; one blind verifier on the deciding rows with legend statistics and n in each triple's questions. Reading and analysis at effort high; plain clients only; no spend; no external contact; no operator e-mail to any service; no individual-level information.
