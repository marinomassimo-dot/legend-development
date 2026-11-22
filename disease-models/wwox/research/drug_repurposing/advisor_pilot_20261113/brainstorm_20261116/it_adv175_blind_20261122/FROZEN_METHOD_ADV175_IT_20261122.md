# ADV-175 frozen method (IT, 2026-11-22), written BEFORE any compound was scored

Hypothesis level; no dose; not medical advice; no WWOX evidence. Question: does the current mechanism-based selection rank compounds by normalisation of calcium-oscillation features toward control (1 uM, one CDKL5-deficiency patient line, technical-replicate aggregate) beyond a declared simple baseline built from the same inputs, against a fixed null?

## What was read, and what was not
* Read for this task: the permitted file `files/adv175_predictor_for_it/predictor_input.tsv` (SHA-256 7d63de87e42ea9f8aa2ed5f28790bf61cbad078485e27514e05338badf66f127, verified; 175 rows, 173 distinct SMILES groups, 175 distinct CAS), the ADV-175 assignment text, and HE's earlier engine-evaluation design and freeze recipe (other targets). Before this freeze I looked at the column list and at the counts of the `vendor_pathway` and `form` fields only; no compound row was inspected.
* NOT read: the source paper, its supplement or workbook, the custodian folder, the outcome key, the sealed note, HE's ADV-174 result file (read only after the score file is committed), any search for the screen's results.
* **Memory record (leakage).** I know that a Muotri-laboratory study of CDKL5 deficiency in iPSC-derived neural cultures exists and that a compound screen on calcium activity is its subject, because the assignment says so; I recall NO compound-level result and hold no drug-response pair. If a compound row triggers a recalled response pair during scoring, its id goes in the `recognised` column of the score file with the pair named in one phrase, and the score is still assigned by the rubric below (no adjustment). Absence of recall is not proof of absence of contamination.

## Engine procedure (the mechanism-based selection, applied to this file)
Fixed order, one pass, fields used: product_name, vendor_target, vendor_pathway, SMILES, descriptors, synonyms. No outside lookup, no network, no tool. Score = expected strength of an acute effect on neuronal-network calcium oscillation at 1 uM in a spheroid, **direction-agnostic** (the file gives no direction of the genotype deviation; a score cannot say whether a compound normalises or worsens). Rubric (integer 0 to 5, applied to the compound's best-supported main action):
* 5: main action is a direct modulator of neuronal excitability machinery at nanomolar to low-micromolar potency (voltage-gated Na, K, Ca or HCN channel; NMDA, AMPA or kainate receptor; GABA-A receptor or GABA/glutamate transporter; mGluR).
* 4: same classes with weaker, mixed or off-target-dominated action; or high-potency neuromodulatory GPCR ligands whose receptors drive network rhythm (muscarinic, serotonergic, adrenergic, dopaminergic, histaminergic, opioid, cannabinoid, adenosine).
* 3: pathway-proximal kinase or signalling modulators from the held mechanism set that plausibly alter network activity on a slower scale (mTOR/PI3K/AKT, GSK3, MAPK/ERK, microtubule dynamics, TrkB/BDNF, HDAC, cAMP/PKA, calcium handling stores such as SERCA, ryanodine or IP3 receptor).
* 2: indirect neuroactive routes (neurotransmitter synthesis, uptake or metabolism enzymes; Na/K-ATPase; general transporters; low-potency channel blockers).
* 1: general cytotoxic, antiproliferative, DNA-damage or apoptosis agents (a viability filter of undefined unit may remove them, direction unknown); or a plausible but weak effect.
* 0: no plausible acute neuronal-activity route (antimicrobial, vitamin, peripheral hormone, metabolic reagent, dye).
Modifier: -1 if the compound's main target class normally needs more than 10 uM for effect; +0 otherwise (no upward bonus). Floor 0, cap 5. Compounds sharing an identical SMILES receive the same engine score (alias group). Ties are allowed and kept.

## Declared baselines (same inputs only; not tuned on any outcome, none is available to me)
* **B1 (class prior)**: 2 if `vendor_pathway` is "Neuronal Signaling"; 1 if "GPCR & G Protein" or "Transmembrane Transporters" or "transporter" or "Neurological Disease"; 0 otherwise. Reason: the simplest pharmacology prior that a reader with no mechanism reasoning would use; vocabulary counts only were seen before freezing.
* **B2 (descriptor prior)**: the compound's `alogp` value (higher lipophilicity first), missing values scored as the file median. Reason: lipophilicity is a common proxy for promiscuous activity in cell assays.
Both baselines are computed by script from the file with no judgement.

## Exclusions
None by outcome. No row is dropped; the 173 SMILES groups are the units HE may bootstrap by. Rows with a missing field are scored on the fields present.

## Metric and null (HE computes; stated for the record)
Primary: AUC of the engine score against HE's label with an alias-group bootstrap; secondary: engine-minus-B1 AUC gap with the same bootstrap; recognition stratum scored apart and a sensitivity without its pharmacological classes (HE). Null: chance (AUC 0.5) by label permutation. Power per HE: about 15 usable positives, SE about 0.07, a gap under about 0.15 is invisible. The result must be worded "no lift detectable at a gap of about 0.15" if the gap is below that; a tie or no lift is a result. Not a rescue, efficacy or WWOX statement; broad suppression cannot be told from a genotype effect.

## Deliverable
`SCORES_ADV175_IT_20261122.tsv`: id, engine_score, baseline_b1, baseline_b2, recognised (blank unless a pair was recalled), committed and landed before HE reveals or scores anything; its SHA-256 is sent to ADV with this file's digest.
