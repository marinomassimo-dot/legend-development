# Brief — Package A: membrane physiology to pharmacological hypotheses (producer)

Read `BRIEF_COMMON.md` first. Your folder: `disease-models/wwox/research/drug_repurposing/membrane_hypotheses_20261108/` (outputs in `output/`). Claim actor label `mh-a`. Receipt event ids end in `-51`.

## Starting state (qualified in the IT38 repeat; do not re-derive, complete it)

WWOX observations from the neuron-specific (Synapsin-Cre) deletion slice paper PMID 34634460, layer II/III pyramidal neurons, P13–P17: resting potential depolarised, input resistance about 40 percent higher in both mutants (102.88 / 143.26 / 143.03 MΩ), sag and rebound changes whose printed p values are not reproducible under assumed Welch/SEM (no contradiction of the paper is asserted: the unit of the tests is undeclared). Sag was not matched or normalised for input resistance. A review (PMID 37982354) states open HCN depolarises RMP but lowers Rin, whereas the mutants show depolarisation with Rin up, the pattern of fewer open conductances; sag is not shown anywhere to be HCN-exclusive (Kv7 and other channels shape sag-like relaxations). GAERS Ih (PMID 24953239): the authors do not read the increase as seizure-restraining. Ivabradine (PMID 34018186): sag block and hyperpolarisation in normal cortical L5/6 slices, injection into somatosensory cortex cut absence-seizure time much more than thalamic VB injection, effective orally only with the efflux inhibitor elacridar.

## Questions

1. Which explanations of "depolarised RMP, higher Rin, altered sag/rebound" fit the data and which do not: more HCN function; fewer open potassium/leak conductances (K2P/Kir/Kv7 and their regulation); passive properties (capacitance, cell size, space clamp, age and maturation, cell-type mix in layer II/III); recording or solution artefacts; a composite. State for each what it predicts for RMP, Rin, sag, rebound and for a blocker/opener effect, and what the paper's own numbers allow.
2. **Complete the primary reading** of 34634460: Methods (internal and external solutions, junction potential, protocols, how sag/rebound/Rin were computed, analysis unit, genotype pooling), Table 1, the figures that carry sag/rebound/RMP, and the supplementary parts that bear on membrane properties. Complete 34018186 (Methods, figures on sag, resting potential, dose, the elacridar experiment, the cortical injection design; what rats, what age, what slices) and 24953239 as far as the decisive Ih/Rin/RMP numbers go; the review 37982354 only where it carries a number you use.
3. For **alternative probes**, read only the primary papers that actually establish a mechanism you would use: a leak/K2P modulator, a Kv7 opener (retigabine/XE991/SCR2682), an Ih blocker of a different chemotype (e.g. ZD7288 and its known off-target actions), and, if one is genuinely useful, a Kir or K2P tool. Keep age, preparation, concentration, selectivity and endpoint with the number. Do not read a probe paper only to add a name.
4. Produce **at most three** distinct hypotheses (or an abstention row naming the datum that would change the decision) in the format of the common brief. A hypothesis must name which result would weaken it and the single most discriminating experiment (for example matched-potential, matched-Rin comparison; voltage clamp isolation of Ih; K-leak reversal; blocker order and a second chemotype; a Rin-normalised sag measure). Include the cell-context axis (is the effect cell-autonomous, layer-specific, maturation-stage specific).

## Source budget

At most **8 sources newly read**, of which at least the three named in item 2 must be read at the depth stated (Methods + figures + supplement where present). Fewer is fine. Reuse earlier receipts where the earlier read already covers the exact numbers you use; say which.

## Phase 1 only now

Write `observations.tsv`, `alternatives.tsv`, `probes.tsv`, `evidence.tsv`, `queries.tsv`, the receipts, then stop and report (sources with depth, figures and supplements actually viewed, anything unreachable). Phase 2 comes by message.
