# SCI47 package A — S0: frame, explanations and priors, written before the source is reopened (2026-11-12)

Non-canonical research material. Not medical advice; no dose, schedule, route or clinical preference; no claim on WWOX beyond the cited records; no compound is promoted. Reference genotype class only. Task record `ledger/tasks/orchestrator/ORCH-SCI47-20261112.json`. A later change to this file is a dated addendum. Paths relative to `disease-models/wwox/research/drug_repurposing/`.

## State found (no new reading yet)
* `main` 940182af. The IT46 package (`generation_it46_20261111`) is **not on main**; its files used here are copies in `inputs_it46/` taken from the IT46 worktree at commit cfac505c (`SOURCE_SHA.txt`), read-only.
* PMID 34634460 (Breton 2021): full-text receipts exist (FTR-20260810-34634460-02, PMC text, figures marked read, supplementary unavailable). IT45/IT46 readers worked on the text only, without figure legends, n or the supplement (`inputs_it46/s5_verify_VERDICTS.md`, end). Existing printed values (from those readers): sIPSC amplitude S-CTL 57.3 ± 31.0 pA, S-KO 27.5 ± 19.4 pA; frequency 10.3 ± 11.5 Hz and 8.4 ± 10.0 Hz; 140 mM KCl pipette; no mIPSC; no evoked IPSC; no antagonist named; Synapsin-Cre conditional line, P13-17, layer II/III pyramidal cells.
* **The suspected inversion.** IT46's README line 26 says "amplitude about half, frequency about a fifth", line 27 says "the amplitude falling more than the frequency". Read as "frequency reduced *to* a fifth", the two sentences contradict each other; read as "reduced *by* about a fifth" they agree (52% and 18%). The printed means favour the second reading. The package must check the **source** (text, Figure 4G-H, legend, statistics), not this arithmetic, and correct the meaning in every place the repository states it.

## Competing explanations kept apart (the protocol must say which it can and cannot separate)
| Code | Explanation | What it would predict that others do not |
|---|---|---|
| E1 | fewer or less active inhibitory inputs (number of synapses/cells, firing) | frequency of sIPSC and mIPSC fall; amplitude per event unchanged |
| E2 | less GABA per vesicle or release probability (presynaptic supply) | mIPSC amplitude may fall with fewer receptors saturated; paired-pulse ratio changes |
| E3 | postsynaptic receptor response (number, subunit, trafficking) | mIPSC amplitude falls, frequency unchanged; response to a puffed agonist falls |
| E4 | chloride gradient / shunting (driving force and conductance) | amplitude depends on E_GABA relative to holding potential; with a 140 mM pipette it is set by the pipette, so this explanation is not tested by those recordings |
| E5 | network state and maturation (age, activity-dependent changes, myelination/AP properties of interneurons) | changes with age window; reversible with network manipulation; AP amplitude of interneurons |
| E6 | passive properties and geometry (input resistance, capacitance, space clamp) | amplitude differences scale with cell size or access resistance |

## Priors fixed before reading (recollection or inference from the held records; unverified; scored afterwards)
* **P1.** The source supports a *fall by about a fifth* in sIPSC frequency, not a fall to a fifth, and the source's own statistics do not make that frequency change firm; the amplitude fall (about half) is the firmer one.
* **P2.** No recording in the paper separates E1-E4: sIPSCs are spontaneous only, in a high-chloride pipette, no TTX-insensitive miniature IPSCs, no evoked IPSCs, no named antagonist, no E_GABA.
* **P3.** The unit of analysis is the cell (and slices), animals are few and not tabulated per measure; at least one number decisive for the matrix has no animal-level n.
* **P4.** The model for the synaptic data is the neuron-targeted Synapsin-Cre conditional line, not the global knockout; no glial or interneuron-class specificity is shown.
* **P5.** Two arms of unrelated drugs "of equal measured effect" are not enough for the two-lever design: equal cellular effect measured in one recorded cell is not equal network effect in a slice; occlusion needs a shown ceiling and the same cell population; a bath application acts on cells that a single-cell injection does not.
* **P6.** For benzodiazepine-site modulation, a rationale beyond general anticonvulsant action exists only if the receptor/amplitude deficit is confirmed in physiological chloride; otherwise it is the same general rationale.
* **P7.** At least one lever worth keeping is not among GABA availability, receptor modulation and chloride transport (an excitability lever or a target tied to the measured passive properties); this is checked, not assumed, and a lever is dropped if the data do not make it useful.

## What the package cannot settle by reading (stated now)
Which of E1-E6 holds in the knockout. That needs a recording programme (miniature and evoked IPSCs in physiological chloride, E_GABA by perforated patch, paired-pulse ratio, passive properties of the same cells); this package states which measurement separates which pair and what each result would change.
