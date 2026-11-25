# Held seizure and electrophysiology readouts in WWOX-deficient systems, by model and age (IT, 2026-11-25)

**2026-11-25, dated correction (read before citing).** The first version of this file had two denominators that disagreed (7 cards by field scan, 16 by text). Both are replaced by one count under a stated rule: **10 of 30 cards, 25 assertion rows; on WWOX-deficient systems 5 cards, 15 rows**. The field scan had missed one WWOX row (`DA-KO-SWD-001`) and the term list had missed one organoid readout (`DA-M01-005`). "None before postnatal day 13" now holds for the 15 reconciled WWOX rows, with the age limit stated in section 2.

Hypothesis level; reference genotype class; nothing here is medical advice. Built from the card assertions only (`cards/*.card.json`, `input.disease_assertions` and `input.drug_assertions`, rows whose `endpoint` or `target_id` names an EEG, electrophysiology or seizure term); no new reading, no age inferred. Asked by ADV (checkpoint 20, section 1, item 6). **Consumer:** the PREREG of the next compound comparison. [2026-11-25, IT, on ADV's instruction: no such comparison has been chosen yet, so until a PREREG names this file it is an unconsumed map; whoever opens that PREREG names it here.]

## Denominator (reconciled, 2026-11-25)
**Rule.** A card is counted when at least one of its assertion rows (`disease_assertion`, `disease_assertions`, `drug_assertion`, `drug_assertions`) reports a measured result of an electrical readout (EEG, electrocorticography, field potential, patch or whole-cell recording, synaptic or evoked current, membrane or action potential, firing, spikes or bursts, multielectrode array) in `endpoint`, `target_id`, `context.cell_type` or `measured_result_note`. Plans, predictions, next measurements, stated absences and restatements elsewhere in the card do not count. Calcium imaging is not counted.

| | Cards | Rows |
|---|---|---|
| Card files scanned (`cards/*.card.json`) | 30 | |
| Counted under the rule | 10: A01, C01, E02, F01, F04, H01, H02, K01, M01, P11 | 25 |
| of which on a WWOX-deficient system | 5: C01, F01, F04, M01, P11 | 15 |
| of which on other systems only | 5: A01, E02, H01, H02, K01 | |

WWOX rows (15): `DA-KO-SWD-001`, `DR-C01-001`; `DA-W2-001`, `-002`, `-003`, `DR-W2-001`; `DA-P9-001` to `-004`; `DA-P11-001`, `-002`, `-003`, `DR-P11-001`; `DA-M01-005`. Other rows (10): `DR-A01-005`, `DR-E02-005`, `DR-H01-001`, `DR-H02-008`, `-009`, `DR-K01-006`, `DR-P9-001` (the row itself calls its figures UNVERIFIED and unused), `DR-P9-006`, `DR-P11-002`, `DR-P11-004`. Rows of depth "abstract" or "partial read" keep that depth: this is a count of card rows, not of verified results.

**Why the first version gave 7 and 16** (both reproduced on 2026-11-25 with the same term list):
1. The field route read only the plural keys; 12 cards also carry a singular `disease_assertion`. Of those 12 rows one is electrical: C01 `DA-KO-SWD-001` (19 field rows, not 18; that table row below said "none").
2. It did not read `measured_result_note`: `DR-A01-005` (an EEG count in mouse knock-in lines), `DR-P9-001`, `DR-P11-004`, `DA-M01-005`.
3. The term list had no "firing" and no "synaptic current": `DR-K01-006`, `DR-P9-006`, `DA-M01-005` (M01 was in neither route).
4. The text route's nine extra cards: A01 (a real row, point 2), K01 (a real row, point 3; its only text hit was a planned array); C04 (restates the C01 spike-wave row and plans an arm), D01 (states an absence), F02 and F03 (restate the d-APV re-reading; F03 also plans patch recordings), I01 (planned EEG), J01 (planned recordings and one stated absence, `DA-J01-006`), L01 (planned array). So 16 counted mentions, not readouts.

Terms of the original two routes: EEG, electrocorticography/ECoG, electrophysiology, patch, whole-cell, field potential, LFP, s/m E/IPSC, membrane potential, action potential, MEA, spike, burst. A first scan keyed on seizure words had missed `DA-W2-003`, `DA-P9-004`, `DA-P11-002`. Behavioural and clinical seizure rows below are **not** in these counts; each says it is not EEG.

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
| Mouse, constitutive Wwox deletion (FVB), cortical electrocorticography | about two to three weeks after birth | spike-wave discharge rate | spike-wave discharges | C01 `DA-KO-SWD-001` | C01 `DR-C01-001` (vector) |
| Human, WOREE-derived cerebral organoid, neuron-promoter WWOX add-back versus control vector | organoid, add-back week 10 to 16 (no postnatal age) | firing, said to fall toward wild type (assay and panel not named in the row) | none | M01 `DA-M01-005` | none (gene add-back, held out from compound evaluation by the card) |
| Mouse, Wwox-/- constitutive null, whole animal | preweaning (no day given) | provoked behavioural seizure stage (not EEG) | provoked, behavioural | G01 `DA-LI-PTZ-001`, H01 `DA-H01-001` | G01 `DR-LI-001` (lithium; `-002` wild-type and `-003` heterozygote arms) |
| Mouse, conditional lines (card M01) | postnatal pups to four weeks | seizures reported with survival and growth (not EEG) | none | M01 `DA-M01-007` | none |
| Human, WWOX-null class (predicted) | infancy | epileptic spasm burden (clinical report) | epileptic spasms | H02 `DA-H02-003` | none |
| Human, WWOX-DEE, one individual | adult | seizure response (clinical) | none | none | F01 `DR-W2-007` (perampanel among seven antiseizure drugs, not isolated; n = 1) |

## 2. What is missing, read against the compound windows above
1. **No electrical readout in a WWOX-deficient animal preparation at a stated day before postnatal day 13**, and none in an adult or chronic animal, among the 15 rows. Limit of the statement: the Synapsin-Cre rows of F01 and P11 print only "about two weeks" and the electrocorticography row "about two to three weeks"; the organoid row has no postnatal age.
2. **The lithium window (preweaning, provoked behavioural stage) has no EEG or slice readout in the same row set.** The nearest is the constitutive-null electrocorticography at about two to three weeks, a different card, preparation and endpoint.
3. **The only compound on a slice readout is d-APV** (burst frequency, rows `DR-W2-001` and `DR-P11-001` of one experiment; delayed evoked response, `DA-P9-004`), acute and ex vivo; no row measures it by EEG in the animal.
4. **No row records EEG or electrophysiology classed as** myoclonic, clonic or tonic-clonic, focal or status epilepticus in a WWOX-deficient system (the provoked behavioural stage is not a recording). Epileptic spasms appear only as a clinical report.

## 3. Limits
* Card assertions only: a held measurement that no card carries is not here (organoid recordings beyond the one sentence of `DA-M01-005`, and the P47T animal observations, are examples to check before the PREREG uses an absence). "None in the cards" is not "none held" and not "none published".
* Rows on non-WWOX systems (clinical trials in infantile spasms, wild-type rodents) are left out of the table.
