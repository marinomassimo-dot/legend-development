# Pilot decision dossier: the shared slice assay (template v1 of IT; SCI, ADV-091 item 1, 2026-11-19; hypothesis level)

Hypothesis level. Reference genotype class only. No dose, schedule or recommendation for any agent in any person. Not medical advice. No personal or individual-level information is used or recorded. Costs appear only as ranges the operator supplies: none is supplied, so every cost cell says `not supplied`. This page ranks nothing: funding order is not research order.

**Correction in force (ADV, 2026-11-19, dated line in the meeting record).** The shared slice assay serves the NMDAR pore blocker against d-APV, the Kv7 opener (cell against slice) and the E_GABA add-on. **Ethosuximide does not belong to it**: it is ordering row 3, the in vivo pup series (stage 2). I checked it in the held files: the slice package v2 (S2, parts 1 to 3 and 6) contains no ethosuximide arm, and no Kv7 arm either (the Kv7 slice design is in the brief sections that S2 says it never folded, and in the IT46 P4 audit). So two of the three readouts below are in S2 (pore blocker against d-APV; E_GABA) and one is an **addition to S2** (the Kv7 opener, from the IT46 audit); a slice ethosuximide arm would be a further addition, and none is proposed here.

**Wording rule.** Where a sentence below says what a source shows, it gives the verbatim anchor with its locator, or says INFERENCE. Anchors are from the held full text of Breton et al. 2021 (Neurobiol Dis 160:105529; held file `PMID34634460_Breton2021_PMC.xml`, Results) unless another source is named.

## 0. Header
`candidate_id` SHARED-SLICE-PREP (three readout blocks: OPP-02, OPP-01, OPP-05 of IT's map) · `portfolio` ambitious (OPP-02, OPP-01) and conservative (OPP-05), per IT's map · `cluster` the shared-assay opportunity of the brainstorm · `dossier_date` 2026-11-19 · `author` SCI · `package_sources` `experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/SLICE_PACKAGE_V2_CONSOLIDATED.md` (S2) and `ORDERING_PAGE.md` with its dated lines (ADV-088, ADV-090); `generation_it46_20261111/README.md` (P4 audit); `expression_timecourse_adv088_sci_20261119/`; the frozen priors file (sha256 `3c567acddf10244602c4536d3153f134cab4eba0690321290edd23772b7d8be0`, untouched) · `cost_ranges_item` not supplied.

**The preparation, named once.** Neuron-specific (Synapsin-Cre) Wwox-knockout neocortical slices, P13 to P17, spontaneous bursting recorded as a field potential in the superficial layer, evoked delayed NMDAR response (layer V stimulus, layer II/III field) as the block-matching readout, whole-cell recordings in the same slices for sag voltage (paired, in mV). The preparation is the one reported by Breton et al. 2021. Whether any laboratory still runs it, and whether it has capacity, is unknown.

---

# Block A. NMDAR pore blocker against d-APV in matched fractional block (IT's OPP-02)

## A1. Chain
| Link | Statement | Evidence class | Source and locator | Weakest? |
|---|---|---|---|---|
| L1 Target engaged | In this preparation the NMDAR-mediated delayed evoked response is measurable and d-APV suppresses it, so, by INFERENCE (the package's design reasoning, not a sentence of the paper), engagement of an NMDAR antagonist can be read (that d-APV is competitive is S2's statement, not the paper's); engagement of a pore blocker has not been measured. | INFERENZA | Breton 2021, Results: "This delayed response was NMDA receptor mediated, as addition of d-APV reversibly suppressed the response". Pore blocker: its choice, trapping, off-rate and Mg2+ competition are not read in any held source (S2 part 6, item 4); abstract-level and primary-text reading of ketamine-like and memantine-like agents exists, but no slice measurement. | |
| L2 Direction | d-APV removes the bursts; a pore blocker has not been tested. | DATO-adjacent | Breton 2021, Results: "Blocking glutamatergic neurotransmission with d-APV (50 μM) eliminated the spontaneous bursting events, as recorded from an LFP placed in the superficial neocortical layer." Counts: 5 slices from 3 animals (figure legend). | |
| L3 Phenotype relevance | Slice bursts bear on seizures in the animal. | IPOTESI | The authors state it as open: "future studies may look at how the prolongation of the bursts could initiate seizures in Wwox S-KO mice" (Breton 2021, Discussion). | |
| L4 Transfer | To a variant of the reference genotype class and to the age that matters. | unknown | The held preparation is a neuron-specific deletion read at P13 to P17 (S2 part 2). Whether a missense or splice variant was ever recorded is **not addressed by the held sources**: the words missense, splice and variant do not occur in Breton 2021, S2 or the ordering page (a word search of those three texts, not of the whole repository). | **yes** (lowest class), then L3 |

## A2. What we know
(1) d-APV 50 μM eliminated bursts and they returned on washout (Breton 2021, Results: "Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal"); limit: 5 slices from 3 animals, one laboratory. (2) The same paper reports increased sag current in the knockout neurons, and discusses that "the use of an Ih blocker is controversial as an anti-epileptic, and in some cases could make the pathology worse"; so a pore blocker with an Ih action is not interchangeable with d-APV (INFERENCE for the pore blocker: its trapping, off-rate and Mg2+ competition are not read in any held source). (3) Five antiseizure mechanism classes tie in the repository's ranking and all three contributing threads come from one network of laboratories (S2 part 2; IT56-Q02): the tie is broken only by measurement.

## A3. The decisive uncertainty, and the decision it changes
**Uncertainty:** does a use-dependent pore blocker, matched to d-APV for fractional block of the evoked delayed response, change the spontaneous burst rate the same way, and what does the rate do 5 to 120 minutes after washout? **Decision it changes:** whether the pore-blocker class is carried to an in vivo arm (the pup brief's stage 4, which by its own rule does not start before the slice arm has run) and by which route it is read (NMDAR dependence, sag or trapping, or disinhibition).
| Result | What we conclude (link moved) | Decision that changes | Next step | Cost range |
|---|---|---|---|---|
| Positive: at matched depth the pore blocker lowers the burst rate like d-APV, with the evoked response suppressed to the target depth and the paired sag unchanged | In this preparation, use-dependent block lowers bursting through NMDAR dependence (moves L1 and L2 for the class; L3 and L4 not moved) | The class stays eligible for stage 4, with harms and stopping rules written first | Stage-4 design written; agent chosen by the laboratory before data | not supplied |
| Negative, control passed: no fall in bursts at matched depth, while d-APV in the same slices eliminates them and the evoked response shows the target depth was reached | The burst suppression by d-APV is not reproduced by pore block at matched depth: class-specific action or competitive-site dependence (moves L2 for the class) | The class is not carried to stage 4 on an NMDAR rationale; a rise in burst rate at intermediate depth would be recorded as the first sign of a disinhibition route and a harm flag | Class parked with the slice record as its reason | not supplied |
| Ambiguous or null, control failed: d-APV does not eliminate bursts in this laboratory's hands, or the target depth is not reached, or vehicle slices do not keep stable bursting | No link moves: UNRESOLVED | None | Repeat after the laboratory fixes the assay condition (bath Mg2+, temperature, burst rule) | not supplied |
**Interpretable-null control (named).** All three must hold in the same slices for a null to count as a negative: (i) the laboratory's own d-APV positive control reproduces elimination of the bursts; (ii) the fractional block of the evoked delayed response is verified per slice at the stated depth for every agent; (iii) time-matched vehicle slices keep stable bursting over the washout period. Failing any one, the row is the ambiguous one.
**The "would we do anything different" check.** The decision changes in two of three rows (carry or park the class). Not yet put to a person who could say "we would not do anything different": that ask is ADV's or the operator's; recorded as **not asked**.

## A4. Why no cheaper analysis reduces it (perimeter of "tried")
In silico: a model of the burst network says the agents can be told apart at intermediate block depths (a hypothesis generator, not evidence; ADV-046 part B and the ADV-063 rerun, as summarised in S2 part 2; not re-read here). Held literature: a two-route check (Europe PMC and PubMed, 2026-11-17) found no second origin of neuron-level slice recordings from a Wwox-deficient neuron; supplements and figures not examined; the check cannot see an unindexed report (S2 part 2; IT56-Q02). **A cheaper route exists and has not been tried: a check of what is already held.** S2 part 2 says that the per-slice values of the washout overshoot (about 1.8 times baseline, read from the published figure by image, error bar including 1.0) "are not recoverable from the held supplement, which is raster". A Breton 2021 supplement is on disk (`files/supplement/PMID34634460_r2/`: `mmc1.docx` with summary tables for baseline, carbenoxolone and brilliant blue FCF, and four raster tiff images). The ordering page, in its supply list, names "the Breton supplement" among the items not held. **S2 and the ordering page disagree on whether it is held, and I have not opened the held images to see whether they contain Supplementary Fig. S3C (the evoked-response figure S2 cites) or any per-slice burst values**; the conflict is open. Block A's engagement readout (A1 L1) leans on that supplementary figure, which the paper's text sentence cites but which I have not seen. If the held files lack them, a request to the group is the operator's act.
**The dossier is therefore not ready in the template's sense for L1 and L2**, and the first step is to read the held supplement, not to wait for a supply.

## A5. What a study of this class can and cannot resolve
Resolves L1 (engagement of the class in the preparation, by the evoked-response match) and L2 (direction at the burst readout). **Cannot resolve L3** (a slice burst is not a seizure) **or L4** (one neuron-specific deletion line at P13 to P17; no variant, no age that matters). After the best outcome L4 stays unknown and L3 stays a hypothesis: the study resolves no weakest link, and says so.

---

# Block B. E_GABA, perforated patch, null against age-matched control (IT's OPP-01), an add-on in the same slices

## B1. Chain
| Link | Statement | Evidence class | Source and locator | Weakest? |
|---|---|---|---|---|
| L1 Target engaged | The chloride gradient of the null neurons at the assay age is unmeasured, so whether a chloride lever has anything to act on is unknown. | unknown | S2 part 3.1: "No Wwox system has a measured E_GABA." (a bare absence statement; the ordering page row 4 says "no Wwox E_GABA exists"; I ran no separate search of the held sources for it; `adv065c_transfer_sci_20261118`). | **yes** |
| L2 Direction | Which way E_GABA differs, if it does. | unknown | Same. | **yes** |
| L3 Phenotype relevance | A depolarised E_GABA would bear on bursting. | IPOTESI | IT46 P8 ledger line: GABA enrichment is not functional inhibition (DIS-017 revival trigger "E_GABA or electrophysiology in the same model and stage" not fired). INFERENCE for the bursting link. | |
| L4 Transfer | To the reference genotype class and the age that matters. | INFERENZA | Unaffected mouse whole-brain bulk RNA-seq (one dataset; ages sampled P0, P3, P14, P28, P63; four samples per age; transcript level; not the knockout): Slc12a5 / Slc12a2 ratio 3.12 at P3, 5.65 at P14, 5.28 at P28; it is at plateau at P14, the first age sampled after P3 (`expression_timecourse_adv088_sci_20261119/`, result note section 1 and finding 3). | |

## B2. What we know
(1) The Wwox slice paper measures a fall of spontaneous inhibition but in a high-chloride pipette with no evoked IPSC, so it cannot report E_GABA (IT46 README, errors disclosed). (2) In unaffected mouse whole-brain bulk RNA the ratio is at plateau at P14; where the rise ends within P3 to P14 is not measured, and P13 and P17 are not sampled, so whether a null-against-control difference in the primary window would read as persistent is an inference (one dataset, transcript, no protein or current). (3) The mouse bumetanide datum was withdrawn as evidence (INV-04 D10, per IT's map; not re-read here).

## B3. The decisive uncertainty, and the decision it changes
**Uncertainty:** is E_GABA of null neocortical neurons different from age-matched control at P13 to P17, and in which direction? **Decision:** whether a chloride lever (an NKCC1 blocker or a KCC2 enhancer, with a GABA-A modulator in a factorial layout) deserves an arm, and in which direction.
| Result | What we conclude (link moved) | Decision that changes | Next step | Cost range |
|---|---|---|---|---|
| Positive: null E_GABA depolarised against control (fraction of depolarised cells reported, bursting against non-bursting slices from the same animal) | A persistent chloride-gradient shift at this age, primary or secondary to bursts (moves L1 and L2) | A chloride arm becomes eligible; the NKCC1-blocker arm is conditional and second (S2 3.1) | Factorial layout with an engagement readout, a wild-type-on-agent group, bath without bumetanide as the primary condition | not supplied |
| Negative, control passed: E_GABA equal to control at P13 to P17 and the laboratory shows the readout detects a known shift | No chloride-gradient abnormality at this age (L1 and L2 closed for P13 to P17 only) | No chloride arm at this age; an earlier window (P9 to P10, a suggestion for the laboratory, burst status unknown) stays unmeasured | Earlier-age arm only if the laboratory takes it | not supplied |
| Ambiguous or null, control failed: bimodal or unstable recordings, or the sensitivity control does not show the known shift | UNRESOLVED | None | Repeat with the control fixed first | not supplied |
A hyperpolarised E_GABA in the null would be a positive row with the opposite lever direction: neither chloride lever as drawn is supported.
**Interpretable-null control (named).** In wild-type slices of the same age and preparation, the perforated-patch readout shows a depolarising shift of E_GABA when a chloride-transport manipulation is applied (a class label, no agent or dose named here), and the wild-type control E_GABA is in the range expected after the switch. Without it the null is UNRESOLVED.
**The "would we do anything different" check.** Two rows change the decision about a chloride arm. Not asked of a person.

## B4. Why no cheaper analysis reduces it
Public transcript data (one whole-brain mouse dataset, ages P0, P3, P14, P28, P63) shows the transcript ratio at plateau at P14 in unaffected brain; it does not say when within P3 to P14 it rises, and does not say what E_GABA is in the knockout and cannot (RNA is not protein or current). No cheaper route is untried here: a Wwox E_GABA does not exist in any held source (ordering row 4; absence stated with that perimeter, second route: the IT46 revival-trigger check on the dismissal ledger).

## B5. Resolves and cannot resolve
Resolves L1 and L2 for the chloride lever at the measured age. Cannot resolve L3 (whether the gradient drives bursts needs a manipulation with a readout) or L4. After the best outcome L3 stays a hypothesis.

---

# Block C. Kv7 opener, cell against slice, with a Kv7-blocker mediation arm (IT's OPP-05; an addition to S2)

## C1. Chain
| Link | Statement | Evidence class | Source and locator | Weakest? |
|---|---|---|---|---|
| L1 Target engaged | The Kv7 channel is expressed in the neurons and an opener reaches it in a bath-applied slice. | INFERENZA | One whole-brain bulk dataset: Kcnq2 transcript rises by about half between P14 and P28 (post hoc look, `expression_timecourse_adv088_sci_20261119/POSTHOC_TARGET_FAMILIES_ADDENDUM_SCI_20261119.md`; transcript, whole brain). IT47's update (IT46 README, 2026-11-12): "An OPC contribution to a bath-applied Kv7 opener is a plausible alternative to control (IT47-Q04), not an established action. RNA is not protein or current. The inferences were not independently verified by SCI47." | |
| L2 Direction | The opener lowers burst incidence in the null. | unknown | No held source tests a Kv7 opener against bursts in this preparation (IT46 P4 audit: the injection arm "has no burst endpoint"). | **yes** |
| L3 Phenotype relevance | Reducing bursts bears on seizures. | unknown | As block A. | **yes** |
| L4 Transfer | To the reference genotype class and the age that matters. | unknown | As block A. | **yes** |

## C2. What we know
(1) The IT46 P4 audit recorded that "the Kv7 opener against injected current does not hold on burst incidence (the injection arm has no burst endpoint)" and corrected the design into R5a (mediation, with a Kv7 blocker or a second chemotype), R5b (a non-Kv7 hyperpolarisation matched on membrane-potential shift and input-resistance change), dynamic clamp for single cells, the animal as the unit and a separate genotype-by-drug test (README, section P4; the audit file itself was not re-read here). (2) The apparent mouse-against-human KCNQ2 difference is not a species difference (technical cause open; IT47 update). (3) Kcnq2 transcript is on a rising phase between P14 and P28 in the one dataset, so a Kv7 series across ages sits on that phase (ADV-088 post hoc look).

## C3. The decisive uncertainty, and the decision it changes
**Uncertainty:** is a Kv7-opener effect on bursting neuron-mediated, Kv7-specific and larger in the null than in wild type? **Decision:** whether a Kv7 route is a conservative-cluster candidate worth an arm.
| Result | What we conclude (link moved) | Decision that changes | Next step | Cost range |
|---|---|---|---|---|
| Positive: the opener lowers bursts, a Kv7 blocker reverses it (R5a), a matched non-Kv7 hyperpolarisation does not reproduce it (R5b), and the effect is larger in the null than in wild type | A Kv7-mediated, genotype-enhanced effect on bursts in neurons (moves L2) | The Kv7 route becomes a candidate with an arm | Cell-level confirmation by dynamic clamp, animal as the unit | not supplied |
| Negative, control passed: no effect although the opener shifts membrane potential or input resistance in the recorded neurons and the blocker reverses that shift | The opener does not lower bursts here despite engagement (moves L2) | The Kv7 route drops for this readout | Parked with the record | not supplied |
| Ambiguous or null, control failed: effect seen but reproduced by the matched hyperpolarisation, or no engagement shown | UNRESOLVED as to Kv7 specificity | None | Redesign with the engagement readout first | not supplied |
**Interpretable-null control (partial).** The engagement readout (a measurable membrane-potential or input-resistance shift by the opener, reversed by the blocker) is named; whether it distinguishes a neuronal from an oligodendrocyte-lineage action in a bath is not settled. A null is therefore counted as a negative only where the engagement shift is seen in the recorded neurons.
**The "would we do anything different" check.** Two rows change the decision; not asked of a person.

## C4. Why no cheaper analysis reduces it
The route was audited in silico by IT (P4, blind reviewer verdicts) and returned a redesign, not an answer; the transcript time course says a rising phase exists, not that the channel acts on bursts. No cheaper route is untried here except re-reading the P4 audit file, which I did not do.

## C5. Resolves and cannot resolve
Resolves L2 (direction at the burst readout, with mediation). Cannot resolve L3 or L4. After the best outcome L3 and L4 stay unknown.

---

# Shared-assay sections (apply to the three blocks)

## 6. Shared assay
One preparation serves OPP-02 (core), OPP-01 (same cells, perforated patch) and OPP-05 (added arms R5a and R5b), and the optional PV measurement OPP-07 on slice-animal tissue (an assay, not a candidate). **Ethosuximide is not served** (pup series, OPP-03). Sharing changes the design: extra arms for block B and block C; an extra age for block B (P9 to P10 as a separate arm, a suggestion for the laboratory); same-day littermate controls at each age with exact age in days per animal (ADV-090 design line, which holds without the dataset); deletion completeness per animal and per region at protein level (S2 3.2); sex, litter and cage recorded (S2 3.6). Animals and slices for three readouts are drawn from the same animals where the laboratory can: a sizing statement per readout is not made here (no SD exists for any of them; the paired-sag arithmetic of S2 part 6 item 7 is illustrative and assumed).

## 7. Blind-check status
`checked by a fresh delegate for IT (sonnet, effort high), 2026-11-19, scope: 19 statements of fields 1 to 3 (chain, what we know, anchors) given as statement plus anchor only`: SUPPORTED 8, SUPPORTED_WITH_LIMIT 9, OVERSHOOT 2, none unsupported or unverifiable (IT's report, `adv094_it_20261119/V_REPORT_VERBATIM_ADV094_IT_20261119.md`, lands with IT's next push). **Second check (a different fresh delegate for IT, same day, 9 repaired statements): SUPPORTED 2, SUPPORTED_WITH_LIMIT 5, OVERSHOOT 1, UNVERIFIABLE 1, none unsupported** (`adv094_it_20261119/V2_REPORT_VERBATIM_ADV094_IT_20261119.md`, lands with IT's next push). **Third round of repairs, 2026-11-19, unaudited:** A4 rewritten (the raster sentence restricted to the overshoot's per-slice values; the S2 and ordering-page conflict on the Breton supplement stated as open; no claim that S3C is not held), A1 L4 ('not addressed by the held sources', word-search perimeter stated), B1 L1 and L2 (no borrowed perimeter), C1 L1 (the OPC sentence with its adjacent limits), A1 L1 (the engagement reading marked INFERENCE). **First-round repairs (checked once, the second check above):** the two overshoots (the transcript-ratio sentence in B1 L4 and B2 (2); the pore-blocker 'no held source' narrowed to four properties in A1 L1), the exact Kv7 quotation (C2 (1)), the OPC sentence quoted (C1 L1), the locator of the raster sentence (A4), perimeter words for the two absences (A1 L4, B1 L1 and L2) and 'competitive' attributed to S2 (A1 L1). Sentences marked INFERENCE or "not re-read" are not anchored.

## What the panel as a whole could change (no ranking, no recommendation)
A funder deciding whether the first costly study is a shared-assay slice panel would learn, from a positive or a negative row, one mid-chain fact per readout (engagement and direction for the pore-blocker class, the chloride gradient at one age, Kv7 mediation), and from no row anything about phenotype relevance or transfer to a variant and age: those two links stay open after the best outcome of every block. The preparation, the animals and the burst readout are shared; the three readouts are separable and each is optional for the laboratory (S2 part 3).

## Filling checklist (reviewer's first look)
1. Four links with a class per block: present; `unknown` printed as unknown. 2. Three outcome rows and a named control per block: present (block C: control partial, stated). 3. A decision named per block; the "anything different" question: recorded as not asked. 4. Perimeter in field 4: given; one cheaper route untried and named (a check of the held Breton 2021 supplement for Supplementary Fig. S3C and per-slice values, with the S2 against ordering-page conflict on what is held; the P4 audit file not re-read). 5. Field 5 says which link stays open: L3 and L4 in every block. 6. Field 7 honest: not checked.
