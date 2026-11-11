# IT46 P4: targeted audit of the decisive causal comparisons

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Two comparisons, not a campaign: the Kv7 opener against a current-injection hyperpolarisation (IT45 R5, question IT45-Q01), and the covalent against the non-covalent KEAP1 reagent (IT45 S10). Labels DATO / INFERENZA / IPOTESI. This is a design audit by logic and by the held facts; it reads no new paper. Independent check: see the last section.

## Checklist (applied to each comparison)
Same biological unit · same level of observation · local or whole-preparation intervention · comparable intensity and exposure · cellular reading kept apart from the network outcome · alternatives still compatible.

## 1. Kv7 opener applied to the slice against current injected in one cell (R5)

What IT45 wrote: "an opener lowers bursts by more than a current-injection hyperpolarisation of equal size → a Kv7-specific benefit; by the same amount → a generic one; not at all → inert".

| Check | Finding | Holds? |
|---|---|---|
| Unit | The opener acts on every cell and terminal in the slice that carries Kv7 channels (neurons of several types, axon initial segments, presynaptic terminals; the held RNA also shows Kcnq2 in OPC at 10.7 FPKM against 30.7 in P7 neurons). Injected current acts on the one recorded cell. | **No**: different units (population against one cell) |
| Level of observation | The endpoint was burst incidence (36 of 42 knockout slices, 4 of 23 heterozygote, 0 of 11 wild type, PMID 34634460 as carried in INV-18). Incidence is a slice-level, network outcome. Hyperpolarising one cell by injection does not change the incidence of a network event. | **No**: the equal-injection arm cannot be read on burst incidence |
| Local or whole | Opener: whole slice. Injection: one cell. | No |
| Intensity and exposure | The opener has concentration, wash-in and temperature dependence (slice penetration is slow and unmeasured); injected current has an amplitude. Matching "equal size" is only meaningful if size means the measured shift of the recorded cell's membrane potential. | Only if matched on the **measured shift**, not on the dose |
| Cell reading against network | Single-cell readings that both manipulations can be compared on: resting potential, input resistance, rheobase, first-spike threshold, firing-frequency adaptation, sag, in the same cell. | Yes, at this level |
| Alternatives | A Kv7 opener can lower excitability through the axon initial segment (threshold, spike afterhyperpolarisation) with little change at rest, and current injection reproduces neither. A difference between opener and injection at matched potential then **is** the interesting result (a Kv7-specific action beyond hyperpolarisation), but it is not a benefit in burst incidence. | yes, kept |

**Verdict:** the comparison as written does not hold for the burst endpoint; it holds at the single-cell level.

**Corrected design (same question).**
* **R5a, same cells.** In each recorded cell, an opener wash-in and, in the same or sister cells, a current injection matched on the measured shift of the resting potential; read rheobase, threshold, input resistance, firing adaptation and sag. Opener better than injection at matched potential → an action beyond hyperpolarisation (Kv7-specific); equal → generic hyperpolarisation; neither → inert at the cell level. A dynamic-clamp Kv7-like or leak conductance in a single cell is the sufficiency counterpart (SCI43 step 5).
* **R5b, slice level.** Burst incidence under the opener against an unrelated manipulation that hyperpolarises the recorded cells by the same measured amount (a second mechanism, not injection), with a concentration series so that incidence is read against the measured cellular effect. Incidence falling only at a cellular effect larger than the unrelated manipulation needs is the Kv7-specific network reading.
* **Genotype interaction.** An opener effect on bursts or excitability that is the same in wild type and knockout is a useful, generic, symptomatic action; it is **not** a WWOX-specific result. The question that bears on WWOX is a larger effect in the knockout than in wild type or heterozygote at matched baseline excitability (a drug-by-genotype interaction). Keep the two questions apart: useful in general, and specific to this lesion.
* **A normal Kv7-blocker-sensitive current in the knockout (R2) is not a refutation of the lever.** A compensatory action does not need a defect in its own target. R2 normal says the lever is compensatory, not corrective; the lever is dropped only by the conjunction already written (R2 normal **and** an opener no better than the matched alternative) or by absence of the channels in the recorded cell class.
* **Cell class.** The held RNA does not support "Kv7 is neuronal" cleanly (cell_context: KCNQ2 mouse shared, human enriched elsewhere in one neuron sample; KCNQ3 shared; KCNQ4/5 not queried): the slice opener arm needs a cell-specific control, as the Ba2+ arm does.

## 2. Covalent KEAP1 modifier against the non-covalent binder on one NRF2-dependent readout (IT45 S10)

| Check | Finding | Holds? |
|---|---|---|
| Unit and level | Both are applied to the same cell culture and read on the same target-gene set; cell-level readings, no network outcome claimed. | Yes |
| Exposure | A covalent electrophile acts in a time- and concentration-dependent, irreversible way and also modifies other thiols; a reversible binder acts at equilibrium. Equal concentration and time are not comparable exposures. | **Partly**: match on a reference response (equal induction of a reference target gene), not on concentration |
| Attribution | The electrophile's effect can be thiol stress independent of NRF2 (H5); NFE2L2 knockdown separates NRF2-dependent from -independent effects for **both** compounds. | Yes, if both arms have the knockdown |
| Alternatives | NQO1 alone is a poor readout (it can rise without NRF2 and without Kelch binding, as the reader found); a target-gene set is required. | kept |
| Cell types | Neurons and astrocytes separately; no neural datum exists. | open measurement |

**Verdict:** the S10 comparison holds with one design correction: exposure is matched on a reference response, not on concentration. No change of the question; consumed by SCI46 (the comparison is its axis).

## Propagation (consumers)
Investigations INV-18 `next_test` and compound view V10 `next_test` (clause generated by `apply_it46_audit.py`); open question IT45-Q01 text; a dated update line at the foot of `generation_it45_20261111/p3_lever_it45.md` and of `next_batch_it45_20261111/BRIEFS.md` (B2). The S10 exposure rule goes to the SCI46 delivery as a note for the comparison rows (no edit of its files).

## Independent check (blind design reviewer, sonnet/high; `verify_p4/VERDICTS.md`; about 24 tool calls, 130k tokens)
The reviewer wrote its own answers before seeing any agreement and did not open this file. **Agreement:** the equal-injection arm has no burst endpoint, so the comparison cannot return "generic" and almost guarantees "opener more than injection"; a non-smaller Kv7-blocker-sensitive current does not refute an opener lever (it tests the deficit hypothesis, not the lever); "useful in general" and "specific to the Wwox lesion" need separate tests. **Additions I had not made and now carry:**
* A DC offset is not a voltage-dependent conductance: it leaves input resistance unchanged while an opener lowers it, so "equal size" must match the **input-resistance change** as well as the shift of the membrane potential.
* "Opener better than injection" does not prove Kv7 specificity (generic conductance shunting; GABA-A potentiation reported for the retigabine class; cancellation through interneurons): specificity needs reversal or occlusion by a Kv7 blocker, or a second opener of a different chemotype.
* Bursts are slice-level events with slices nested in animals: the **animal is the statistical unit**; first show that the drug acts in the recorded tissue (a vehicle time control).
* Wwox specificity needs a genotype-by-drug interaction against a non-Wwox hyperexcitable preparation matched on baseline burst rate; wild-type slices do not burst at baseline (0 of 11), so bursts would have to be induced, which limits the inference; the heterozygote serves as a gradient; a drug arm alone cannot prove Wwox specificity (no rescue arm exists).
* S10 (comparison B): no WWOX genotype factor (the design speaks to the NRF2 pathway, not to the WWOX hypotheses); the covalent compound is consumed by thiols and persists after washout, so exposure is matched in a **phase 0** (concentration-response, time-course, cytotoxicity, glutathione, washout on a proximal NRF2 reading) before any comparison; an NRF2-independent control gene set and at least two independent NFE2L2-knockdown reagents with measured efficiency; fumarate esters are not local to KEAP1 (many protein adducts; NRF2-independent effects persist in NRF2-null cells, PMIDs given by the reviewer; I did not re-read them); separate neuron and astrocyte cultures have no network, so "network last" is a second phase.
**Not checked by the reviewer (kept as unverified):** neuron against astrocyte NRF2 and glutathione levels, Kv7 on interneurons, M-current rundown, XE991 selectivity, permeability of Kelch-pocket binders; no primary source for the two S10 compounds was read. The mouse against human KCNQ2 neuron discrepancy is still unexplained.
