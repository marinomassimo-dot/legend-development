# RS-R6 hypotheses (controllable perturbations only)

All entries are IPOTESI. Nothing here is medical advice; no dose, schedule or route is given. Row ids refer to `evidence_rs_r6.tsv`.

## H1 - T-type calcium channel block as a genotype-dependent seizure modifier in the null (IPOTESI)

* Perturbation: ethosuximide (approved T-type blocker) and, for a target control, genetic reduction of the T-type channel in the Wwox-null background.
* Premises (DATO): ethosuximide suppressed PTZ-provoked seizure in Wwox-null mice and had no effect in wild-type and heterozygous controls at the low PTZ dose used (M02, PMID 32000863, passage-level reading). The repository already carries the T-type axis in card H01.
* Counter-evidence: controls received a low PTZ dose, so a floor effect cannot be excluded (wild-type PTZ scores are about 0.5 to 1.3 stage); lithium in a separate cohort reduced wild-type scores significantly from a similarly low baseline, which argues the wild-type negative for ethosuximide may be real (census lines 609-610); provoked seizure only; no target-specific control; lithium suppressed in all genotypes (C01), showing that this assay can respond without WWOX involvement.
* Transfer conditions to the WWOX-DEE reference class: null/null class first (no residual protein needed, because the target lies downstream); a seizure endpoint in a young animal; matched provoking stimulus across genotypes.
* Transfer breakers: no genotype-by-drug interaction once the stimulus is matched; no effect on spontaneous seizures; effect absent in a missense or splice class with residual WWOX.
* Next discriminating experiment: a genotype-by-drug test at a PTZ dose giving matched seizure scores in all genotypes, with a second T-type blocker and a genetic T-type knockdown arm.

## H2 - HIF1-alpha restraint as a metabolic modifier of the null (IPOTESI)

* Perturbation: HIF1-alpha lowering (genetic Hif1a reduction in the Wwox-null, or a compound with a target control); digoxin is the only compound tested and is a cardiac glycoside, so it is the probe, not the proposal.
* Premises (DATO): digoxin raised blood glucose in the germline null (M04, repository census, not re-read) and delayed liver tumour formation with a larger effect in hepatocyte-specific Wwox-null mice than in controls (M03, PMID 29724996, passages read).
* Counter-evidence: small group, one time point, implausible printed dose for the glycaemia arm; tumour endpoint is liver, not brain; effect attributed to HIF1-alpha without a target-specific control in the source; WW1-dependent binding may be retained by missense alleles.
* Transfer conditions: null/null class; glycaemia or an energy-metabolism readout, not seizures; a genetic Hif1a arm to separate target from compound.
* Transfer breakers: Hif1a reduction does not move glycaemia or seizure susceptibility in the null; effect appears in wild type equally. The digoxin experiment itself had a wild-type arm in which glucose fell (about 108 to about 77 mg/dl, n = 3, no significance mark, read from the figure) and a placebo knockout arm without a rise; a rise in a near-hypoglycaemic pup within 40 minutes is compatible with a stress or toxicity effect that is not HIF1-alpha-borne (independent verification).
* Next discriminating experiment: conditional Hif1a reduction in the Wwox-null with glycaemia and seizure threshold as readouts, against digoxin and vehicle.

## H3 - Antioxidant relief of a ROS-dependent defect in WWOX-deficient neural cells (IPOTESI)

* Perturbation: N-acetyl-cysteine (real compound) as a probe of ROS dependence.
* Premises (DATO): N-acetyl-cysteine prevented microsatellite instability and restored senescence induction in Wwox-null fibroblasts (M07, PMID 37897534, passage-level reading); the fly respiratory-complex work states ROS, Akt, autophagy and HIF dependence in the interaction (I02, abstract only).
* Counter-evidence: fibroblast senescence is not a neural phenotype; ROS in null neurons is unmeasured in these sources; broad antioxidants fail often in vivo; the fly effect has Wwox as the modifier, not the defect.
* Transfer conditions: donor-derived or isogenic WWOX-null neurons show raised ROS; a viability or maturation endpoint that moves.
* Transfer breakers: no ROS increase in null neurons; N-acetyl-cysteine changes nothing in matched isogenic pairs.
* Next discriminating experiment: ROS measurement and a maturation endpoint in isogenic WWOX-null versus corrected neurons, with and without N-acetyl-cysteine.

## H4 - Ldh lowering (already carded as E02; no new arm) (IPOTESI)

Genetic Ldh reduction rescued locomotion in the Wwox-RNAi plus amyloid-beta 42 fly (M09). Restated for completeness: it depends on the amyloid background and on an Atf4-driven lactate axis; the next experiment stays the one in card E02 (lactate and LDH readouts in WWOX-deficient versus isogenic human neural cells).

## Not advanced

* p53 deletion (M08): rescued a bone defect but accelerates osteosarcoma (C04); not a controllable or safe intervention.
* Chk2 inhibition with DNA damage (O01) and any DepMap-conditional gene (O02): oncology viability signals; no argument for transfer to a developmental or neurological phenotype.
* Lithium (M01): non-specific in the repository census (C01); stays in card G01.
* A51 and D-APV (M05, M06): already carded; not re-read.
