# IT29 P2: two cases chosen before any compound was looked for (2026-11-05)

Non-canonical research material, not medical advice. Public edition: the subject is the WWOX-DEE reference genotype class.
Baseline `main` = `8c7c46cf`. Stage consumed by the current method: IT28 `generation_it28_p6_20261105/results_s9/` (994 rows; named by
the Standing method pointer and checked by file digest in `frozen_current/README.md`, not assumed from file dates).

## What the current method does on these two endpoints (frozen, `frozen_current/`)

| | Search layer (need to target to catalogue) | Generator (expression seeds to engine) |
|---|---|---|
| Oligodendrocyte maturation / myelination (`NEED-MYELINATION`, direction `restore`) | 546 associations over 202 families, **every row abstains at `no_coupling_row`**: the record holds no target-to-myelin coupling. Muscarinic antagonists (benztropine among them) are listed but cannot be signed. | No myelin or oligodendrocyte-lineage seed exists in the six seed sets (Q2 to Q8), so no proposal is reached through this endpoint. |
| Network hyperexcitability / provoked bursting (`NEED-SEIZURE-CONTROL-SYMPTOMATIC`, `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR`) | 91 and 709 associations; rows abstain at `action_not_stated`, `coupling_not_measured`, `not_an_intervention_target`. | Seeds are transcripts (Pvalb, Gad1, Npy); IT13 P3a already found the engine returns proteasome/HDAC inhibitors by transcription chains and no ion-channel agent. |

These are **rows 3 and 4 of the six-way distinction**: the data may exist and not be represented (a signed target-to-endpoint
coupling), and a representation (the `coupling` column) exists but is empty for these needs. They are not, as yet, a biological
limit and not a request for more catalogue.

## Case 1 (principal): maturation of the oligodendrocyte lineage, endpoint = oligodendrocyte differentiation and myelin formation

* **Endpoint.** Progression from precursor to MBP-positive / myelinating oligodendrocyte (marker counts, myelin segments in a co-culture, ultrastructure in vivo). Measured *as a function*, kept apart from a single marker transcript.
* **Relation to an observed WWOX problem.** Neuron-deleted Wwox mice are hypomyelinated; add-back in neurons in the neonatal window partly prevents it; in the knockout the oligodendrocyte transcript share is low (Mbp UMI share ratio 0.30, `snrna_it13b_pv_20261031`). IT14 P4 (`glia_maturation_it14_p4_20261101`) reached **RESTRICT**: the driver is upstream of the oligodendrocyte, and no compound was entered.
* **Why this is not a repeat of IT14 P4.** That package was a reconnaissance and stopped at the role question. The new question is narrower and executable: *which interventions move this endpoint in a seizure-free, cell-autonomous system, in which direction, and how many of them are catalogue compounds whose sign the search layer currently cannot assign?* The output is a signed coupling table the existing search layer can consume, and a comparison with the abstaining frozen result.
* **Why not ISR or HDAC5.** Both were taken only as far as the IT28 questions; HDAC4/5 and EZH2 reappear here only as **possible opposed** evidence (IT28 carried them as myelin counter-premises at abstract level; IT29 P10 narrowed HDAC4/5 to a transient peripheral delay with no CNS datum, CH-IT29-CLASSIIA-CNS-MYELIN), which is exactly what a phenotype-first table must keep visible.
* **Result the comparison could change.** If signed perturbation evidence turns the 546 abstentions into a small set of signed, context-conditioned levers (or shows that direction depends on the neuronal signal, INV-06), the INV-06 "orderable or not" decision moves; if the signed evidence is all neuron-dependent or in-vitro only, the class stays a role question and the abstention is confirmed as correct.

## Case 2 (contrasting): network hyperexcitability in a developmental epilepsy setting

* **Endpoint.** Network-level discharge: burst incidence or frequency in culture, slice or organoid; seizure-like locomotion or electrographic events in a larval fish; provoked-seizure threshold in a pup.
* **What differs from Case 1.** Another cell type (neurons, inhibitory/excitatory balance); another level of measurement (electrophysiology and behaviour, not differentiation counts); a **possible compensatory role** (bursts may counterbalance, not cause, a deficit; IT14 P3 left repair against counterbalance open); and a different data situation (phenotypic screens exist in other epilepsy models, while WWOX has no deposited numeric source data, IT13 P3a).
* **Current manual reference.** IT14 P3 (`function_pharm_it14_p3_20261101`: clobazam/NDMC, ladder, experiment table) and IT13 P3a (Kv7 opener) are the *manual phenotype-first baseline*; the comparison asks whether the computable path reproduces, narrows or contradicts them, with the caveat that they came from the same repository (retrospective, declared).
* **Result the comparison could change.** Whether the signed-coupling route generalises to a lesion where the endpoint is a circuit property, and whether any agent class is separated by *direction in a developmental model* from the T-type and NMDAR thread (INV-03/INV-04) already prioritised.

## Selection rule (fixed before searching)
Both cases were chosen from the ranking's needs and the IT28 residuals, using the frozen abstention pattern and the existence of a manual baseline. No compound name was used to choose either case.
