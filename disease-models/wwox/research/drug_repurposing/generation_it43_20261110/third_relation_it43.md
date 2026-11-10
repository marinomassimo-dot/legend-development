# IT43 P3: a metabolic relation, framed before any compound name is looked at

Non-canonical working note. Not medical advice; no dose, schedule or route. Written 2026-11-10 before the search; a later change is a dated addendum, not an edit. SCI43 works on resting K+ conductances of INV-18; this note touches no channel and re-reads nothing SCI43 reads.

## Choice and why it adds information over IT42
**S9: lowering the activity of the pyruvate dehydrogenase kinases (PDK1-4) to release PDH (need NEED-PDH-PYRUVATE-AXIS, INV-07).** IT41/IT42 relations were all receptor or transporter actions on a measured circuit. This one is an enzyme-regulation action on an axis whose sign is unresolved in the repository, so it tests whether the path can hold a relation with conflicting premises without inventing a direction. The carded chain (dichloroacetate and PDK inhibition) is old; the generative question is what the path does with it now.

## Frame
| Item | Statement |
|---|---|
| WWOX observation and context | A glycolytic signature (WWOX-system data, non-neural and organoid); the kinase transcript lower in an organoid; one PDH activity measurement with no difference in a non-neural fibroblast pool with partial WWOX depletion; a ketogenic-diet response reported in 3 of 5 WOREE individuals; lactate 2.4 to 3.3 mmol/L in one individual (INV-07 evidence_available). DATO as stated there; no neuronal PDH flux measurement exists. |
| Action that could give benefit | Less PDK activity, so less inhibitory phosphorylation of PDH and more pyruvate entering the mitochondrion. IPOTESI, and only if PDH is actually phosphorylated more in the affected cell. |
| Causal explanation | PDH is held down in WWOX-deficient neural cells (HIF1A-linked kinase induction) and the glycolytic shift is its consequence. |
| Compensatory explanation | The glycolytic shift is an adaptation to supply or redox conditions and PDH is already adequate or high; the kinase transcript fall is the cell's own correction. Releasing PDH further would add load. |
| Consequential explanation | Lactate and glycolytic markers follow seizures, hypoxia of the preparation or the ketogenic state, not the genotype. |
| Opposite or inert conditions | PDH already unrestrained (the kinase transcript is lower: the available sign points this way); a cell type that depends on glycolytic lactate export (an astrocyte-to-neuron or oligodendrocyte supply role); acidosis or lactate-sensitive states; a molecule whose action is on a different kinase isoform than the one expressed in the cell. |
| Functional outcome to modify | PDH activity and flux with lactate, pyruvate and redox state measured directly; then a functional readout (burst incidence or myelin-lineage readout) only if the premise holds. |
| Development and exposure | Neuron versus oligodendrocyte lineage and developmental age are not separated in the data; central exposure of a small molecule is a separate question, not assumed. |

## Relation row
`relations_it41.tsv` gains S9 with target_symbols `PDK1;PDK2;PDK3;PDK4`, wanted direction down (inhibition), site_policy `any`; no special code. Expected readout: molecules with typed PDK-inhibiting actions, those with only a listing, those whose action concerns another kinase or is an activator, and the identity state of dichloroacetate (a small molecule with many names).

## What the output may be
A conditional comparison, an abstention that keeps the exploratory possibility, or a circumscribed generative question. The first selection criterion is the premise (is PDH reduced at all), not the molecule. A compound found is classified as: known in WWOX, new combination for LEGEND, transferred hypothesis, or novelty verified within a stated search; nothing is claimed new from a name alone.

## Addendum (2026-11-10, after reading the INV-07 package `metabolic_inv07_20261107`, which the frame above had not consumed)
The earlier package answers INV-07 as **unresolved** and corrects two statements the frame repeated: the one human PDH activity measurement is a non-neural fibroblast line with partial depletion, where the kinase transcript and lactate are **up**, so the signs conflict between systems (organoid transcript lower, fibroblast higher) rather than pointing one way; and the only randomised human trial of the reference, in a mitochondrial lactic-acidosis disease (abstract level), was stopped early with all treated participants off study drug, mostly for peripheral nerve toxicity, efficacy not judgeable. It also states that the PDK1 of this axis is not PDPK1 (the symbol trap noted in `s9/result_it43.md` was therefore known but not applied to listing rows) and that PDH phosphorylation at one site gives neither activity nor the responsible kinase. Consequences: the premise measurement (amount, phosphorylation at all three sites, activity before and after dephosphorylation) precedes any compound arm; a safety flag is attached to the reference; the frame's "cause" explanation is one of seven compatible explanations in `explanations.tsv`, not the default.
