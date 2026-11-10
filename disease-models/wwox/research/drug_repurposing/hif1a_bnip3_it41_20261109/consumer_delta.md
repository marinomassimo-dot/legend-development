# Consumer delta — IT41 package B, HIF1A to BNIP3 (proposals only; nothing applied)

Task record `ORCH-IT41-20261109`. Every row names the consumer file and row, the proposed change, the source and the read depth. The integrating session (IT41) decides; this package edits none of these files, no ranking, no dashboard, no need, no new registry. Paths are relative to `disease-models/wwox/research/drug_repurposing/`.

**Point of the generative path that should use the result.** The step that links a chain to its premise (stage S16 of `generation_it39_20261109/`, mapping rows that tie `HIF1A -T(+)-> HK2` chains to the premise) should tie the three `HIF1A -T(+)-> BNIP3` chains (IT21P2-0001 to 0003) to a premise of their own, so that a reader of those proposals sees the abstention and the discriminating question instead of the HK2 premise; `output/explanations.tsv` is the five-row representation, `output/new_measurements.tsv` the list of conditions.

## What changes in the conclusions, and what does not

| Changes | Does not change |
|---|---|
| The BNIP3 chains get a premise of their own: transcript signal small and partly an artefact, no protein or flux, direction context dependent, abstention with a question | The three proposals' ids, ranks and `PARTIAL_EXAMPLE` status; no rank moves |
| The sign flip of the neuron library is a scale artefact, not a centring dependence | The HIF1A to HK2 premise chain and its rows |
| Neural sources read HIF inhibition and BNIP3 rise as protective (rat epilepsy, TBI abstract, HT22 OGD) | The statement that no WWOX neural protein measurement exists (a search result) |
| EGR1 is lower in the KO organoid (IPOTESI, cheap recompute) | Compound identities (Harness) |

## Proposals

| # | Consumer and row | Proposed change | Source and depth |
|---|---|---|---|
| 1 | `case_it9_p6_hif_axis_20261030/premises.tsv` (columns `premise_id, premise, where_to_rederive`) | Add rows for a BNIP3 premise: (a) the organoid transcript +0.46 log2, not robust; (b) the neuron-library sign is a scale artefact; mouse P17 flat; (c) no protein or flux measurement; (d) direction context dependent in HT22 (protein up in hypoxia with glucose, down in OGD; BNIP3 loss harmful in OGD); each with its re-derivation pointer | `output/decisive.tsv` D01-D03, D11-D12; GEO deposits (re-derived by the verifier) |
| 2 | `generation_it39_20261109/results_s16/proposals_it21.tsv` (a built surface of its stage; change the mapping source, do not edit the file) | Tie IT21P2-0001 to 0003 to the new BNIP3 premise (not to an HK2 premise) and carry the abstention text in the premise-decisive-test field; regenerate | `output/explanations.tsv` E5 |
| 3 | `ranking_it8_p9_20261029/investigations.tsv` | No HIF1A-to-BNIP3 investigation exists. Proposed decision for IT41: open one row only if the discriminating question below is judged worth a laboratory measurement; text: "In isogenic WWOX-deficient against add-back human neural cells at matched oxygen: does BNIP3 protein rise, does it fall on HIF1A and EPAS1 knockdown, and does BNIP3 knockdown make survival, ROS and membrane potential better or worse?" No rank proposed | `output/explanations.tsv`, `output/new_measurements.tsv` M1-M7 |
| 4 | `cards/K01_hif_axis_glycolytic_shift.card.json`, `p4_fields.counter_evidence` | Add: the one neural in-vivo HIF-inhibitor test (rat epilepsy, 41324728) lowered HIF-1alpha and raised BNIP3 with lower autophagy marker; HT22 data show BNIP3 loss harmful in OGD; both non-WWOX | D07, D11-D12 |
| 5 | `needs/needs.json`, the HIF-axis need | Add an observation for BNIP3 protein and mitophagy flux as unmeasured and the open-measurement list; the file cannot hold oxygen level, time or cell line as separate fields (format limit) | `output/new_measurements.tsv` |
| 6 | Harness identity delivery (`identity_it41_20261109/`) | PX-478, EZN-2968, nitroglycerin identities remain with Harness; KC7F2 and XMU-MP-1 appear as named by their papers and carry no catalogue check here | `output/explanations.tsv` E1-E2 |

## Not proposed (and why)

* No compound candidacy, no HIF-lowering lever, no mitophagy modulator: the direction is not sustainable.
* No change to the HIF1A to HK2 premise, to ranking or to the dashboard.
* No promotion of the EGR1 observation beyond an IPOTESI with a recompute check.

## Reads still open (none required for this delivery)

Full text of 42323821 (embargoed in PMC until June 2027); a primary source for FOXO3, p53, E2F1 and NF-kB on BNIP3 in neurons (leads 38043200, 34475505); supplements of 41972676 and 25012504; Fig 6-7 of 38443598 and Fig 11 of 41324728.
