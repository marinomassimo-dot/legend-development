# IT49 P5: result of the generalisation case INV-02 (ISR modulators), against the pre-registration

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Nothing here nominates a compound; no rank, sign or qualification changed. Pre-registration: `prereg_it49.md` (committed in 9cba43c8 before any row of the case was read). The decisive propositions of the ISR package were independently audited earlier (`isrib_discrim_20261108/verify/audit_a.md`, units U1-U4 supported); no new decisive scientific proposition was made here, so no new verifier was run.

## What was run (same inputs for each arm)
1. **Simple target search** (existing `action_search.py` with the case-local relations I1-I3, `relations_inv02_it49.tsv`; gtopdb pinned input, ChEMBL curated mechanisms): 12 rows. I1 (raising eIF2B activity): **0 rows** (an eIF2B activator is not a catalogued target action; the card and the package name it as a research probe). I2 (PERK): 3 rows, all inhibitors. I3 (the other eIF2alpha kinases): 9 rows, of which 2 activators are excluded by direction (correct) and 7 inhibitor rows. `primary_target` is false in GtoPdb for 6 of the 12 rows (two of them named for other kinases: a RIPK1 and a Cdk2 inhibitor): kinase-panel or secondary-target rows, flagged here as likely false links, not read at the primary.
2. **Previous path**: the INV-02 row. It already states the decisive uncertainty (the sign of the ISR at protein level in a WWOX-deficient human neural cell is unmeasured; an attenuating and a potentiating compound are equally defensible) and a first test with no compound: ATF4 protein, total and phosphorylated eIF2alpha and per-cell translation, against an isogenic control, then a pre-registered panel only if the sign is high.
3. **Path with hypotheses, context and premises**: `hypotheses_for(INV-02)` returns no row (no ISR package is registered with a hypotheses role); the cell-class join answers "no held table carries these genes: cell-class attribution is an open question, not an answer" for all 11 ISR genes; the unregistered package `isrib_discrim_20261108` holds a design (steps, controls, decision branches) rather than hypothesis rows.

## Against the predictions
* P1 (no rows from `hypotheses_for`): **held**. The generalisation question then answers itself: a package of **design-only** layout (steps, controls, branches; no relation, observation, rival and measure cells per hypothesis) **cannot** be consumed by a manifest row and a mapping entry. The capability generalises across hypothesis layouts (five layouts now), not to design packages. A design reader would be new code, which the pre-registration counted as failure to generalise for this layout.
* P2 (unknown, not low): **held** (all 11 genes unknown).
* P3 (premises or controls the card lacks): **held, in a small amount**. The package adds, with sources: step 0 (qualify the readouts, the antibody site and the engagement control in one plate before any arm); an engagement control by eIF2B assembly shift in the same plate; the antibody-site ambiguity (human residue 539 of eIF2B epsilon is Asp, so "S539" is not a human serine); the four evidence levels (binding, biochemical effect, translation in the preparation, function in a pathological system); the probe-not-candidate role of the eIF2B activator. Most of the sign-first design was already on the card.
* P4 (no molecule, no direction): **held**.

## Failure outcomes, checked
* A mapping beyond a manifest row and a mapping entry: **met for design-only packages** (above).
* A false link: **found by the check** in arm 1 (6 of 12 rows not primary-target); none carried into arm 3.
* A premise the package does not state: none carried.
* Arm 3 equal to arm 2 in the next experiment: **largely yes**: the first experiment is the same (protein-level sign, no compound); the difference is the step 0 qualification and the engagement control, which change what the plate must contain, not the order.

## What this shows and does not show
Shows: the hypothesis-layout consumption is not the limit for INV-02; the limit is that the knowledge sits as a design, which the generator does not read, and that the held tables do not carry the ISR genes (RNA class means of the ISR genes would be the next input, a zero-spend extraction like IT47-B1, not a measurement). The simple target search is poor here in a specific way (0 rows for the node the card cares about) and noisy in another (6 of 12 not primary). Does not show: a better pharmacological prediction, a favourable compound, novelty, or that this behaviour would hold for a case chosen by someone else. One retrospective case, chosen by a rule fixed beforehand, scored by the session that built the method; independent reference absent.

## Cost
Software: seconds for the search and the join. Orchestrator time: about 30 minutes of the session (not measured by a tool). No delegate used.

## Limits
The case relations I1-I3 are case-local (not added to the production relation tables). The panel-row flag uses GtoPdb's primary-target field, not a reading of the primary papers. The package was not changed.
