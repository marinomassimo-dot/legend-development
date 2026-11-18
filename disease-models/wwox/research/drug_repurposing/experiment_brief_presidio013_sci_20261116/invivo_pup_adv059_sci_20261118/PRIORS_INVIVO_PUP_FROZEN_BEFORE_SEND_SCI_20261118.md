# Priors for the in vivo pup brief (first provoked-seizure experiment in the Wwox-null pup), frozen before the brief is sent anywhere (SCI, 2026-11-18)

Non-canonical. Hypothesis level (IPOTESI): labels, not measurements. **Subjective weights fixed before any data so that a later score is literal; they are not validated predictive probabilities** (SCI's earlier scored forecasts are not distinguishable from chance on their own, see `adv046_review_sci_20261118/PART_A_INFERENCE_REVIEW_ADV046_SCI_20261118.md` point 3). Class labels only; no agent is named as a use; no dose; nothing here is a WWOX result; not medical advice. Reference genotype class only. The slice priors file `PRIORS_13_11_FROZEN_BEFORE_SEND_SCI_20261117.md` (sha256 `3c567acddf10244602c4536d3153f134cab4eba0690321290edd23772b7d8be0`) is a different experiment and is untouched. The brief that cites this file's sha256 is sent nowhere before this file is committed.

## Definitions fixed now
* **Assay age** = the postnatal age chosen by the laboratory for all genotypes in one session (the age of the PTZ test in Cheng 2020 is not stated; the paper says "preweaning"). **Older age** = the oldest age in the wild-type age series at which the vehicle stimulus still gives wild-type pups a non-floor response.
* **Stimulus** = the laboratory's own published standard provoked-seizure assay, at an exposure fixed in a pilot so that wild-type vehicle pups reach a mean per-animal stage above the floor (the held Cheng 2020 wild-type pups sit at stage about 1 on 0 to 6).
* **S (per-animal summary)** = area under the modified Racine stage against time over the laboratory's standard observation window. **Ratio R(genotype)** = mean S of treated animals divided by mean S of same-genotype, same-session vehicle animals; analysed on the log scale; unit of analysis = animal, litter as cluster (bootstrap over litters). **Interaction ratio** = R(knockout) divided by R(wild type). A ratio is an **effect** when it is at most 0.7 with an interval excluding 1; a **null** when its interval lies inside 0.85 to 1.15; otherwise **unresolved**.
* **Seizure type per animal:** minimal = stages 1 to 2; generalised = stages 4 to 5 with tonic phase; status = three or more tonic-clonic seizures in 1 hour (the Cheng 2020 definition). Incidences are reported per type.
* **Panel valid at an age** = the flat-profile panel agent (for example valproate) has an effect in wild-type vehicle-matched animals at that age in the same session. **A null for any test arm is read only when the panel is valid at that age.**
* **Floor** = wild-type vehicle S below the stage-1 equivalent of the laboratory's own detection limit (fixed in the pilot); arms at the floor are not interpretable.

## Predictions (weights; each class set sums to 1; scored as the natural-log of the weight given to the observed class, against a uniform weight over the classes of the same set, in nats; binary statements against ln 0.5)
**Set E, ethosuximide at the assay age and in the age series (panel valid, wild type above floor):**
| class | meaning | weight |
|---|---|---|
| E1 | knockout-selective: R(-/-) is an effect, R(+/+) a null, interaction ratio at most 0.7 | 0.20 |
| E2 | age-limited with a wild-type floor: R(+/+) a null at the assay age and an effect at the older age; knockout effect present or not | 0.30 |
| E3 | general: effects in all three genotypes with R values within a factor 1.2 of each other | 0.20 |
| E4 | no effect in any genotype at any age tested | 0.15 |
| E5 | not interpretable (panel not valid, or wild type at the floor) | 0.15 |
**Set C, a selective T-type blocker beside ethosuximide (class label; no engagement control exists in pups, none was found):**
| class | meaning | weight |
|---|---|---|
| C1 | same pattern as ethosuximide in the knockout | 0.30 |
| C2 | no effect in the knockout while ethosuximide has one | 0.25 |
| C3 | no effect anywhere (not interpretable without an engagement control) | 0.30 |
| C4 | effect in all genotypes | 0.15 |
**Binary statements:**
| # | statement | weight |
|---|---|---|
| P1 | vehicle knockout pups have S at least 1.5 times vehicle wild-type S at the assay age (replication of the susceptibility in Cheng 2020) | 0.80 |
| P2 | the flat-profile panel agent has an effect in wild type at the assay age | 0.65 |
| P3 | ethosuximide has an effect in wild type at the oldest age tested | 0.60 |
| P4 | lithium has an effect (R at most 0.7) in wild type at the assay age (Cheng 2020: yes) | 0.60 |
| P5 | lithium interaction ratio lies between 0.7 and 1.43 (no genotype specificity) | 0.65 |
| P6 | a second GSK-3 inhibitor of another class has an effect in the knockout | 0.45 |
| P7 | the general non-GSK-3 comparator has an effect in the knockout | 0.75 |
| P8 | at least one test or panel agent raises minimal-seizure incidence by at least 1.3 times vehicle while lowering generalised-seizure incidence | 0.45 |
| P9 | the knockout vehicle group needs a status-epilepticus stopping rule in at least a quarter of animals (Cheng 2020: about half of knockouts reached status on PTZ) | 0.60 |

## Rejecting observations (written now)
* E1 is rejected if R(+/+) is an effect while the panel is valid at the assay age; E2 is rejected if R(+/+) at the older age is a null with the panel valid there; E3 is rejected if the interaction ratio is at most 0.7 or at least 1.43.
* "Lithium acts through GSK-3 in the knockout" (a statement, not a prior) is not supported unless the second GSK-3 inhibitor of another class has an effect in the knockout and the non-GSK-3 comparator does not; P5 true with P6 true supports a general GSK-3-class effect without knockout selectivity.
* Any null from an arm at the floor, or at an age where the panel is not valid, is **unresolved**, not a rejection.
* The pore-blocker arm is not frozen here: its priors are written when that stage is reached, after the harms and stopping rules.
