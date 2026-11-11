# Blind design review, IT46 P4: two causal comparisons

Reviewer: independent design reviewer (sonnet, high, no sub-agents). Public sources only, zero spend, no contact, no e-mail address sent anywhere, no header spoofing. I did not open `generation_it46_20261111/p4_audit_it46.md`. Non-canonical working note; not medical advice. Labels: DATO (read in a source), INFERENZA (my reasoning), NON VERIFICATO (from my background knowledge; my PubMed queries for it returned nothing or were not opened).

Sources actually read: the brief; `generation_it45_20261111/p3_lever_it45.md`; `generation_it45_20261111/s10_dose/result_it45.md` and one line of its `selection_it45.md`; `ranking_it8_p9_20261029/investigations_it20.tsv` (INV-18 row, cut at about 2.5k characters, so its tail was not seen); `generation_it46_20261111/cell_context_it46.tsv`; the full text of PMID 34634460 (PMC8609180, through PubMed; Table 1 and the figures were not in the text returned, so the three resting potentials and the sag values are **not** verified by me); PubMed abstracts for the other items cited.

---

## Comparison A: opener in the bath against current injected in one cell (R5, IT45-Q01)

### Facts I rely on (DATO, PMID 34634460 full text)
* Mouse is a neuron-specific (Synapsin-Cre) Wwox knockout, P13-17. Bursts were counted as **field (LFP) events in slices**: 0/11 wild type (7 mice), 4/23 heterozygote (14 mice), 36/42 knockout (24 mice). So the biological unit of the phenotype is the slice, and slices are nested in animals.
* Bursts are abolished by D-APV (50 uM, reversibly), reduced 87 percent in rate by carbenoxolone (not reversible on washout); onset is dominated by an excitatory (reversal about 6 mV) current. Median rate 2.29 bursts/min, inter-burst interval 26.2 s. The authors ran drug tests in slices that had shown at least three bursts.
* Recorded cells were layer II/III pyramidal neurons, "not spiking spontaneously" only, K-gluconate pipette with 0.5 mM EGTA and 2 mM Na2ATP. Interneurons were also recorded: spontaneous IPSCs were reduced in the knockout (amplitude 57.3 to 27.5 pA).
* Frequency-current slope did not differ once curves were shifted to rheobase. The authors say the animals die at 3-4 weeks, so P13-17 may be "late-stage".
* Held RNA (`cell_context_it46.tsv`, class means, not current or share): mouse KCNQ2 neurons P7 30.68 against OPC P17 10.68 (SHARED, "partly" attributable to neurons); KCNQ3 4.27 against newly formed oligodendrocytes 4.57 (SHARED); KCNQ4 and KCNQ5 NOT_IN_TABLE ("unknown, not low"). Human, n=1: KCNQ2 neuron 0.10 against fetal astrocyte 4.30 (OTHER_ENRICHED); KCNQ3 SHARED. The mouse and human KCNQ2 neuron values differ by about 300-fold and the file does not explain it; I could not check why (dataset, age and class definitions not opened).

### Check 1, same biological unit
**My answer first.** The outcome (bursts) belongs to a slice network. A bath opener acts on the slice; an injected current acts on one cell among thousands. They are not the same unit. A single hyperpolarised pyramidal cell cannot be expected to lower a field burst, so the burst endpoint does not exist for the injection arm.
**Verdict: DISAGREE (does not hold as written).** Also, slices are nested in mice (42 slices from 24 knockouts), so the statistical unit should be the animal, or a mixed model with animal as random effect, not the slice.
**Corrected design.** Both arms at slice level, the animal as the independent unit; cell-level recordings are a nested secondary reading in the same slices.

### Check 2, same level of observation
**My answer first.** R5 says "lowers bursts" for one arm and "hyperpolarisation of equal size" for the other. Burst rate is a field/network reading; hyperpolarisation size is a single-cell membrane reading. "The same endpoints" cannot be met by one injected cell.
**Verdict: DISAGREE.**
**Corrected design.** Read both arms on both levels in the same slice: (i) LFP burst rate in layer II/III, within-slice, before against during the manipulation, with a vehicle time-control arm (burst rate can drift, and the paper's own washouts were not all reversible, so a crossover alone is unsafe); (ii) whole-cell resting potential, input resistance, sag, rheobase, rebound in one or two pyramidal cells and, if feasible, one interneuron per slice. Use a continuous rate, not incidence: 36/42 is already near ceiling.

### Check 3, intervention local or on the whole preparation
**My answer first.** Bath: the whole preparation, including pyramidal cells, interneurons (already weakened in inhibition), terminals, and non-neuronal cells that carry some KCNQ2/3 RNA (OPC, oligodendrocyte lineage; the model also has hypomyelination per the authors). Pipette: one cell, and a DC current is an offset, not a conductance: it leaves input resistance unchanged and is not voltage- or state-dependent, whereas a Kv7 opener adds a voltage-dependent conductance that is largest when the cell depolarises, i.e. at burst onset. Even at equal steady-state shift, the two interventions differ in what they do to the dynamics that matter for bursts.
**Verdict: DISAGREE.**
**Corrected design.** Two clean pairings, each local-to-local or global-to-global:
* Single cell: dynamic clamp adding a Kv7-like (M-type) conductance against a leak/K conductance giving the same steady-state shift, read on cell-level endpoints only (rheobase, EPSP summation, rebound, firing to a fixed synaptic-like input). This keeps the conductance-against-offset question without claiming a burst result.
* Slice: bath opener against a bath-applied non-Kv7 hyperpolarising manipulation, read on bursts (see check 6 for the limits of any such comparator).

### Check 4, intensity and exposure comparable
**My answer first.** "Equal size" taken as equal steady-state shift is not equal exposure. The opener's tissue concentration in a 400-500 um slice is unknown; its effect on Vm depends on each cell's Kv7 availability and resting potential (which differs by genotype here: -79.25/-75.51/-73.62 mV as carried, not verified by me); the injected current is chosen by the experimenter. The opener also lowers input resistance; the DC does not. Whole-cell dialysis can run down M-current (NON VERIFICATO: my query returned nothing), which would make the Vm shift to a given dose smaller in the recorded cell than in the unrecorded network.
**Verdict: DISAGREE.**
**Corrected design.** Show that the drug acts in the recorded tissue before reading any burst result: a measured Vm and input-resistance change in cells of the same slice, and an XE991-sensitive component. Then match on mean Vm shift and on input-resistance change, over at least three levels (a dose-response in both arms), not one point. A "no effect" (the "inert" row) is only interpretable if that drug-action check passed.

### Check 5, cellular reading kept apart from the network outcome
**My answer first.** The wording merges them: the comparison outcome is bursts but the "equal size" matching variable is cellular. The paper itself shows why they must be separate: the heterozygote shares several cellular features with the knockout (depolarised, more sag) yet bursts in only 4/23 slices, and bursts are NMDAR- and gap-junction-dependent network events. A cellular shift does not by itself predict a burst change, and the reverse.
**Verdict: PARTLY (the plan separates them in section 4 but R5 as worded does not).**
**Corrected design.** Pre-specify the two readings as separate endpoints with separate decision rules; report the cell-level shift as the exposure check, the burst rate as the outcome; never infer one from the other.

### Check 6, alternative explanations still compatible
**My answer first.** Yes, several remain, and one is structural.
* **Structural.** In the original design the injection arm cannot lower slice bursts by construction, so "more than injection" is nearly guaranteed and the "generic" outcome cannot occur. R5 cannot discriminate.
* **"More than equal-size injection" does not mean Kv7-specific.** It also follows from generic conductance shunting (any added K conductance lowers input resistance) or from an off-target action. Retigabine/flupirtine-class compounds are reported to enhance GABA-A receptor function (review, PMID 33580520, doi 10.1111/epi.16832; a retigabine analogue is a delta-GABA-A positive modulator, PMID 34727270, doi 10.1007/s11064-021-03475-y). The knockout has weakened inhibition, so a GABA-A route to a benefit is a live, Kv7-independent explanation. Kv7 specificity is shown by block or occlusion (an XE991- or linopirdine-sensitive benefit; a second opener chemotype with a different off-target profile), not by comparison with current injection.
* **Cancellation.** Kv7 channels sit on interneurons and axon initial segments as well as pyramidal cells (NON VERIFICATO; my interneuron query gave only culture work, e.g. PMID 38577639). A bath opener can weaken inhibition in a preparation whose IPSCs are already reduced, hiding a pyramidal benefit.
* **Substrate not shown at the right age.** The RNA is P7 whole-cortex class means; KCNQ4 and KCNQ5 are unknown, not low; human KCNQ2 in neurons is low in a single sample. The expression of Kv7 in P13-17 layer II/III pyramidal cells is not held.
* **Time and washout.** Spontaneous burst rate may drift; a drug that is slow to wash out cannot be used as its own control.
**Verdict: DISAGREE.**
**Corrected R5 (keeps the question "Kv7-specific or generic hyperpolarisation").** Split into two:
* **R5a, mediation.** An opener lowers burst rate (paired within slice, against a vehicle time control) and the effect on bursts and on Vm is reversed or occluded by XE991 (or linopirdine); optionally reproduced by a second opener of a different chemotype.
* **R5b, specificity against generic.** In slices, at matched mean Vm shift and matched input-resistance change (measured in sampled cells), a bath-applied non-Kv7 hyperpolarising manipulation gives a burst reduction equal to the opener's (generic), smaller (Kv7-specific, with the voltage-dependence argument), or larger. State the limit: every non-Kv7 comparator (a GIRK or K2P activator, a KATP opener, lowered extracellular K+) has its own cell distribution and off-targets, so a perfect match is not available and the conclusion is "not distinguishable from generic hyperpolarisation at matched shift", not proof of either.
In the single cell, use the dynamic-clamp pairing of check 3 for cell-level endpoints only.

### Question (a): if the Kv7-blocker-sensitive difference current is NOT smaller in the knockout, does that refute a Kv7-opener lever?
**My answer first.** No. R2 tests a cause (mechanism (d), a Kv7 deficit near rest). The lever's premise is different: that a Kv7 conductance is present and can be increased, and that increasing it lowers bursts. A current that is not smaller shows the target is present (which, if anything, supports availability) and removes explanation (d); it does not test whether an opener changes bursts, which only R5a/R5b do.
**Verdict: AGREE with the IT45 logic that R2 and R5 are separate; DISAGREE with any reading of a normal R2 as refuting the lever.**
**Conditions for reading R2 at all.** Normalise to capacitance (branch (c), smaller cells, would otherwise masquerade as a smaller current); report an activation curve (V1/2 and slope), not only amplitude at one voltage, because a shifted voltage dependence or altered PIP2 coupling can matter with equal peak current; mind whole-cell rundown and the unclamped axon-initial-segment portion; XE991 is not perfectly selective (NON VERIFICATO). What would refute the lever: no burst effect despite a verified drug action in the same slices (check 4), or no XE991-sensitive current in P13-17 pyramidal cells.

### Question (b): "useful in general" against "specific to the Wwox lesion"
**My answer first.** They are two claims needing two tests. Burst reduction by an opener in knockout slices alone shows only the first, and only for this assay (bursts, not cognition or motor function, which nothing here measures). A "specific to the lesion" claim needs a genotype-by-drug interaction.
**Verdict: the IT45 text states the caveat in words but the design has no arm for it.**
**Corrected design.**
1. Knockout slices: dose-response of burst rate, paired within slice, with vehicle time control and XE991 reversal (the "general, Kv7-mediated" claim).
2. A non-Wwox hyperexcitable comparator run in the same sessions: wild-type littermate slices cannot serve at baseline (0/11 burst), so bursts must be induced, with the induction mechanism stated and the baseline burst rate matched to the knockout's. Test the genotype-by-drug interaction on potency and on effect size at matched baseline. Say that the induced bursts may have a different mechanism, which limits the inference.
3. Heterozygote slices (partial dose, 4/23 with bursts) as a gradient, not as a control.
4. Link to the mechanism measurement (R2 in the same cells): a lesion-specific benefit is easier to claim if it tracks a Wwox-dependent change (for example larger effect where Kv7 current is smaller); absent that, state "general symptomatic lever".
Even a perfect set cannot prove "specific to Wwox" with a pharmacological arm alone; a rescue arm (restoration of Wwox) would be needed and none is available in these slices.

### What I could not check (A)
Table 1 and the figures of PMID 34634460 (the resting potentials, sag, input resistance values, the supplement); whether whole-cell and LFP were recorded in the same slices throughout (the reversal-potential experiment did record both together); M-current rundown, Kv7 interneuron and AIS literature, XE991 selectivity, retigabine's GABA-A effects in cortical slices (only the review and an analogue paper were reached; my searches for the other items returned no records); the cell-class and age of the human RNA values; Kv7 expression at P13-17 in layer II/III pyramidal cells.

---

## Comparison B: covalent KEAP1 electrophile against non-covalent KEAP1 binder, each with and without NFE2L2 knockdown, "on the same cell readout that depends on NRF2, not on binding potency" (S10)

### Facts I rely on (from `result_it45.md`, DATO as stated there, and PubMed)
* Every NFE2L2 value held is a reporter or translocation EC50 in a human cell line; the binder's cell data are in bronchial epithelial cells; no neuron or astrocyte (`result_it45.md`). Two documents disagree on the same compounds (5.114 against 7.93; "greater than 10" against 127.2), so across-document potencies are not interchangeable (the file's own rule).
* The Kelch-domain assay is blind to cysteine modifiers (sulforaphane inactive); NQO1 induction alone cannot separate an NRF2-independent benefit; halofuginone is not an NRF2-selective control.
* `cell_context_it46.tsv`: NFE2L2 and KEAP1, mouse and human, NOT_IN_TABLE (unknown, not low).
* Covalent fumarate esters adduct thousands of proteins in cells (click-chemistry proteomics, about 2,970 targets for the diester, KEAP1 itself found only at lower level; PMID 36493513, doi 10.1016/j.redox.2022.102560) and inactivate GAPDH (PMID 29599194, doi 10.1126/science.aan4665). NRF2 activators, including sulforaphane, show NRF2-independent effects in cells where NFE2L2 is inactivated or knocked out (PMID 37459366, doi 10.1371/journal.ppat.1011506, effect on a nuclear-export protein; PMID 38930573, doi 10.3390/microorganisms12061191, macrophages from NRF2-null mice).

### Check 1, same biological unit
**My answer first.** Within one cell type the unit is the independent culture (not the well). The across-cell-type claim is where it breaks: neurons and astrocytes differ in the NRF2/KEAP1 axis (NON VERIFICATO from literature I could not search; the held table is silent), so exposure and knockdown efficiency are cell-type properties, not constants. Neuronal cultures commonly contain some astrocytes; a small astrocyte fraction could dominate an NRF2 target-gene signal if astrocytes respond more strongly (NON VERIFICATO). The design as written has no WWOX genotype factor, so the unit that matters for the project (a WWOX-deficient neural cell against its control) is absent.
**Verdict: PARTLY.**
**Corrected design.** Genotype (WWOX-deficient against isogenic or littermate control) as a factor in each cell type; report culture purity (neuron and astrocyte markers) for every culture; use independent cultures as replicates.

### Check 2, same level of observation
**My answer first.** A target-gene transcript set is one level for both compounds and is the right choice over NQO1 alone. But it sits downstream of two distinct things: how much KEAP1 is engaged (proximal) and whether the cell is protected (distal). "Same readout that depends on NRF2" fixes only the middle level.
**Verdict: PARTLY.**
**Corrected design.** Three levels, each reported on its own: proximal (NRF2 protein and nuclear NRF2 at fixed times); the pre-specified target-gene set (several NRF2-dependent genes, fixed before the experiment, plus an NRF2-independent control set, with NRF2-dependence of the set shown by NFE2L2 knockdown in vehicle); distal (survival or oxidative-damage readout under the challenge, defined in advance; the document does not define "benefit").

### Check 3, intervention local or on the whole preparation
**My answer first.** In dissociated cultures both compounds reach every cell; there is no regional question. The locality problem is molecular: the electrophile is not local to KEAP1 (thousands of cysteine adducts; the reactive proteome includes GAPDH, per the sources above), whereas the non-covalent binder is directed at the Kelch pocket and spares cysteines (but may also release other Kelch-domain partners, NON VERIFICATO). NFE2L2 knockdown removes only the NRF2-dependent part of an electrophile's action; the remainder is not subtracted by it, and the cited NRF2-independent effects show the remainder is not small in some systems.
**Verdict: PARTLY (the knockdown is the right control, but it does not make the covalent arm KEAP1-local).**
**Corrected design.** Keep the knockdown arm; add a KEAP1-route control for the covalent arm (a KEAP1 cysteine-sensor mutant, where available) and a genetic ceiling arm (KEAP1 lowering) to calibrate what a pure KEAP1 route gives. Where a covalent effect survives NFE2L2 loss, label it NRF2-independent rather than "lost".

### Check 4, intensity and exposure comparable
**My answer first.** This does not hold. A covalent, thiol-reactive compound acts by concentration times time (rate of adduct formation against turnover of the modified protein), is consumed by intracellular glutathione and by medium thiols, and its effect persists after washout. A reversible binder acts at equilibrium occupancy, depends on cell permeability, and the effect vanishes when it is removed. A single concentration of each, in one pre-treatment, will measure different things; "not on binding potency" is right as a rule but leaves exposure unspecified. The oxidative challenge adds a second exposure problem: it can itself activate NRF2 (a ceiling or interaction), and it consumes the electrophile and glutathione, so the challenge can change the covalent arm's effective dose and not the binder's. Glutathione level and electrophile handling may differ between neurons and astrocytes (NON VERIFICATO). The held potency values are from other cells and other assays and, per the engine's own rule, are NOT_COMPARABLE.
**Verdict: DISAGREE.**
**Corrected design.**
* Phase 0, exposure matching, per cell type: a concentration-response (at least five points) and a time-course (at least three times) for each compound on the proximal reading and on the gene set; a cytotoxicity reading in the same wells to exclude concentrations where the electrophile injures cells; intracellular glutathione; a washout arm for both compounds.
* Choose the working exposure for each compound as the one giving a matched submaximal level of the proximal NRF2 reading (for example, matched on the response, using the genetic KEAP1-lowering arm as ceiling), not matched on Kd or EC50 from elsewhere.
* Fix, in advance, the timing against the challenge (pretreat then challenge with compound present; and pretreat then wash out), and run both for both compounds.
* Include a challenge-only arm and a compound-plus-challenge arm so the interaction with the challenge can be separated from the compound's own effect.

### Check 5, cellular reading kept apart from the network outcome
**My answer first.** The plan puts "the network outcome last", but in separate neuron and astrocyte cultures there is no network to read; the reading that can be made is cell-autonomous (transcript, possibly survival). A transcript is not protein or enzyme activity; NQO1 activity alone was already flagged as unable to separate NRF2-independent benefit. A compartment question (does the benefit in astrocytes act through neurons) needs a co-culture, conditioned-medium or slice arm.
**Verdict: PARTLY.**
**Corrected design.** State that the single-cell-type phase answers only cell-autonomous questions; move the compartment and network question to a defined second phase (co-culture or conditioned-medium transfer, then slice or organoid), with its own endpoint; never carry a transcript result forward as a network result.

### Check 6, alternative explanations still compatible
**My answer first.** Several.
* An NRF2-independent covalent benefit (NF-kB, GAPDH, metabolic, nuclear-export targets) that knockdown does not remove completely or that the readout does not see.
* Incomplete knockdown: residual NRF2 can still be amplified, giving "partial dependence"; neurons are hard to knock down by siRNA, so efficiency and the method (viral shRNA or genome editing) must be reported per cell type, with at least two independent reagents, to exclude off-target or transfection-induced stress responses that move ARE genes.
* Floor effects: a knockdown cell is already more sensitive to the challenge, so a "benefit lost" may be only a floor; judge the knockdown-by-compound interaction on a fold-over-own-vehicle scale and on absolute survival.
* The covalent arm may worsen outcome (consumption of glutathione under the challenge), which the "benefit lost" criterion would not separate from "no benefit".
* Non-cell-autonomous leakage (astrocyte products in neuron cultures); species and cell-line carry-over from the held values (human lines only).
* Without a WWOX-deficient arm, any result applies to the NRF2 pathway in these cells, not to H1-H6 about WWOX (the premise that NRF2 protein, nuclear NRF2 and target-gene activity in a WWOX-deficient neural system are measured is still missing, as the file itself says).
**Verdict: DISAGREE (compatible alternatives remain).**

### Corrected design for B, in one place
Factors: WWOX-deficient against control, per cell type (neurons, astrocytes, purity reported) x compound (covalent, non-covalent, genetic KEAP1-lowering ceiling, vehicle) x NFE2L2 (non-targeting against at least two independent knockdown or knockout reagents, efficiency measured) x challenge (none against one defined). Phase 0 matches exposure as above. Endpoints at three levels reported separately (proximal NRF2, pre-specified gene set with an NRF2-independent control set, distal survival or damage). Decision rules written before the run: a benefit lost under knockdown for both compounds supports NRF2 dependence only if knockdown efficiency, the interaction on a fold scale, and the challenge-only arm are all in hand; a benefit surviving knockdown is labelled NRF2-independent; worsening is labelled as such. The network or compartment question is a second phase.

### What I could not check (B)
The primary papers behind the two compounds (I read no source for them; I rely on `result_it45.md` as written); the knockdown results of the non-covalent binder's source; any neuron or astrocyte NRF2 data (my PubMed queries for neuron/astrocyte NRF2 and for non-covalent KEAP1 inhibitors returned no usable records, so the claims about astrocyte versus neuron NRF2 activity, glutathione, cell permeability of Kelch-pocket binders and Kelch-partner release are NON VERIFICATO).

---

## Summary table

| Check | A (opener in bath against injected current) | B (covalent against non-covalent KEAP1) |
|---|---|---|
| 1 unit | does not hold (slice against cell; animal is the unit) | partly (unit is culture; no WWOX genotype arm) |
| 2 level | does not hold (field burst against single-cell Vm) | partly (middle level only) |
| 3 local or whole | does not hold (bath against pipette; offset against conductance) | partly (covalent not KEAP1-local) |
| 4 exposure | does not hold | does not hold (time-dependent covalent against equilibrium binder; challenge interaction) |
| 5 cell against network | partly | partly (no network in separate cultures) |
| 6 alternatives | does not hold (generic or off-target explanations stay; design cannot yield "generic") | does not hold (NRF2-independent action, incomplete knockdown, floor, worsening) |

## Tool calls and tokens (approximate)
About 24 tool calls: 1 file read, 5 shell reads of repository files, 14 PubMed calls (search, metadata, one full text), 1 write. Approximately 130k tokens in total, dominated by PubMed payloads (the full text and the metadata returns).
