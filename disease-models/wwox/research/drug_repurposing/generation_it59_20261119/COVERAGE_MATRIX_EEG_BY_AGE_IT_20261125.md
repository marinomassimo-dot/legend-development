# Held seizure and electrophysiology readouts in WWOX-deficient systems, by model and age (IT, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Built from the card assertions only (`cards/*.card.json`, `input.disease_assertions` and `input.drug_assertions`, rows whose `endpoint` or `target_id` names an EEG, electrophysiology or seizure term); no new reading, no age inferred. Asked by ADV (checkpoint 20, section 1, item 6). **Consumer:** the PREREG of the next compound comparison.

## Denominator (two routes, 2026-11-25)
| Count | Route 1: card assertion fields (`endpoint`, `target_id`, `context.cell_type`) | Route 2: text search over the whole card file |
|---|---|---|
| Card files scanned (`cards/*.card.json`; 30 packets also) | 30 | 30 |
| Cards with an EEG or electrophysiology term | 7 (C01, E02, F01, F04, H01, H02, P11), 18 rows | 16 (the 7 plus A01, C04, D01, F02, F03, I01, J01, K01, L01) |
| of which on a WWOX-deficient system | 4 cards (C01, F01, F04, P11), 13 rows | no further held readout found in the 9 text-only cards: where their sentences name a WWOX system they are planned arms, stated absences or the C01 data again (sentence filter, not a full reading) |

Terms: EEG, electrocorticography/ECoG, electrophysiology, patch, whole-cell, field potential, LFP, s/m E/IPSC, membrane potential, action potential, MEA, spike, burst. A first scan keyed on seizure words had missed three of the 13 rows (`DA-W2-003`, `DA-P9-004`, `DA-P11-002`). Behavioural and clinical seizure rows below are **not** in these counts; each says it is not EEG.

## Choices, stated before the table
* **Ages** are the card's own words (`context.developmental_stage`).
* **Seizure and EEG classes listed in the claim registry** (query on `claim_registry_current.md`, 2026-11-25: myoclon, clonic, tonic seizure, focal, spasm, status epilepticus, hypsarr, spike-wave, multifocal, and their Italian forms): **five seizure classes** — epileptic spasms (`CLAIM 001`, `011`, `031`, `040`), myoclonic (`001`, `011`, `040`), clonic or tonic-clonic including audiogenic (`001`, `005`, `011`, `037`, `040`), focal (`001`, `009`, `032`, `040`), status epilepticus (`031`) — and **three electrographic patterns** — spike-wave discharges (`011`, `032`, `040`), multifocal EEG (`012`, `042`), hypsarrhythmia (`032`, `042`). No tonic-only seizure term was found by that query (2026-11-25). A mention in a claim is not a count of patients, and several mentions concern non-WWOX comparators.
* **Phenotype class** is a column only where a card names one.

## 1. WWOX-deficient systems
| Model (card's genotype) | Age (card) | Readout | Phenotype class named by the card | Card rows (no compound) | Card rows with a compound or vector |
|---|---|---|---|---|---|
| Mouse, Synapsin-Cre Wwox knockout, neocortex slice | juvenile, about two weeks | fraction of slices with bursts; burst frequency | none | F01 `DA-W2-001`, P11 `DA-P11-001` | F01 `DR-W2-001` and P11 `DR-P11-001` (both d-APV) |
| same | juvenile, about two weeks | mEPSC amplitude; sIPSC amplitude | none | F01 `DA-W2-002`, P11 `DA-P11-003` | none |
| same | juvenile, about two weeks | delayed evoked response (layer V stimulation); resting membrane potential | none | F01 `DA-W2-003` (its note says d-APV suppresses it), P11 `DA-P11-002` | none |
| Mouse, Synapsin-Cre Wwox knockout, neocortex slice | postnatal day 13 to 17 | resting membrane potential; sIPSC amplitude and frequency | none | F04 `DA-P9-001`, `DA-P9-002` | none |
| Mouse, Synapsin-Cre Wwox knockout, hippocampal slice | postnatal day 13 to 17 | presence of spontaneous bursts | none | F04 `DA-P9-003` | none |
| Mouse, Synapsin-Cre Wwox knockout, neocortex slice | postnatal day 13 to 17 | suppression of the delayed evoked response across stimulus strengths | none | none | F04 `DA-P9-004` (d-APV) |
| Mouse, constitutive Wwox deletion (FVB), cortical electrocorticography | about two to three weeks after birth | spike-wave discharge rate | spike-wave discharges | none | C01 `DR-C01-001` (vector) |
| Mouse, Wwox-/- constitutive null, whole animal | preweaning (no day given) | provoked behavioural seizure stage (not EEG) | provoked, behavioural | G01 `DA-LI-PTZ-001`, H01 `DA-H01-001` | G01 `DR-LI-001` (lithium; `-002` wild-type and `-003` heterozygote arms) |
| Mouse, conditional lines (card M01) | postnatal pups to four weeks | seizures reported with survival and growth (not EEG) | none | M01 `DA-M01-007` | none |
| Human, WWOX-null class (predicted) | infancy | epileptic spasm burden (clinical report) | epileptic spasms | H02 `DA-H02-003` | none |
| Human, WWOX-DEE, one individual | adult | seizure response (clinical) | none | none | F01 `DR-W2-007` (perampanel among seven antiseizure drugs, not isolated; n = 1) |

## 2. What is missing, read against the compound windows above
1. **No EEG or electrophysiology row in a WWOX-deficient system before postnatal day 13**, and none in an adult or chronic animal, among the card assertions.
2. **The lithium window (preweaning, provoked behavioural stage) has no EEG or slice readout in the same row set.** The nearest is the constitutive-null electrocorticography at about two to three weeks, a different card, preparation and endpoint.
3. **The only compound on a slice readout is d-APV** (burst frequency, rows `DR-W2-001` and `DR-P11-001` of one experiment; delayed evoked response, `DA-P9-004`), acute and ex vivo; no row measures it by EEG in the animal.
4. **No row records EEG or electrophysiology classed as** myoclonic, clonic or tonic-clonic, focal or status epilepticus in a WWOX-deficient system (the provoked behavioural stage is not a recording). Epileptic spasms appear only as a clinical report.

## 3. Limits
* Card assertions only: a held measurement that no card carries is not here (the human organoid recordings and the P47T animal observations are examples to check before the PREREG uses an absence). "None in the cards" is not "none held" and not "none published".
* Rows on non-WWOX systems (clinical trials in infantile spasms, wild-type rodents) are left out of the table.
