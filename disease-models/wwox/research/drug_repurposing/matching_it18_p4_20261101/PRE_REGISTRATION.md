# IT18 P4 pre-registration: does the WWOX need context improve compound matching over a target-only search?

Written 2026-11-01 before any compound label of this task was produced. Non-canonical research material; not medical advice; computational, pharmacological compatibility only, no benefit claim. Public edition, WWOX-DEE genotype class.

## Decision under test
A need in `needs/needs.json` names intervention targets and, for some needs, a direction (`intervention_direction.direction` = down/up/uncertain, WWOX-derived, with its stated certainty). Which catalogue compounds should the module put forward for that need? Three equivalent paths over the same universe:

| Path | Information used | Output per compound |
|---|---|---|
| T target-only | the need's intervention-target genes; any catalogue compound with a direct human ChEMBL curated mechanism on them | "candidate" (no label) |
| X external-only | T plus the compound's ChEMBL action direction, and a direction chosen **without WWOX**: the majority GtoPdb direction of the target among DEV compounds (as B1 in IT17) | compatible / opposite / indeterminable |
| L LEGEND contextual | T plus ChEMBL action direction, plus the need's WWOX direction; indeterminable when the need direction is uncertain, or the action is partial/mixed/unknown, or the compound has opposite directions on target genes of the same need | compatible / opposite / indeterminable |

Universe: catalogue parent compounds (human, direct mechanism rows only, as in `evaluation_it17_p3_20261101/direction_task.py`) with a mechanism on at least one intervention-target gene of a need. Two need groups: **directed** (direction down or up on a target gene: today EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, SEIZURE-CONTROL-SYMPTOMATIC, T-TYPE-CALCIUM, all "down") and **uncertain** (the other needs with intervention targets).

## What is measured (and what is not)
Reference: GtoPdb release 2026.3.1 curated interaction action for the same compound and target gene, mapped to DECREASE / INCREASE as in IT17 (partial agonist = ambiguous, excluded from the determinate set). For a directed need, a compound is **truly compatible** when its GtoPdb direction on at least one need target equals the need direction and it has no determinate opposite direction on another target of the same need; **truly opposite** when determinate and reversed. This measures *pharmacological compatibility with a stated direction*. It is not prediction of benefit, safety or efficacy, and the need direction itself is a WWOX-derived hypothesis the reference cannot judge.

Principal measure: on directed needs, **precision of the compatible label among compounds with a determinate reference**, compound-level (a compound counted once per need), Wilson 95% interval, against T's base rate (fraction of the T set that is truly compatible: what recommending everything returned achieves). Complementary: opposite compounds wrongly labelled compatible (count and list), coverage of the reference (share of compounds with no GtoPdb counterpart), abstention rate and reasons, errors. Split by compound hash as IT17 (first hex digit of sha256 of the parent ChEMBL id: 0-7 DEV, 8-f EVAL); the rule tables and the X prior are fixed on DEV only; EVAL is read once after the lock.

WWOX contribution is stated in two separate parts and not summed: (a) **on directed needs**: do X and L produce different labels? If the target prior already equals the WWOX direction, L = X and the WWOX contribution to accuracy is zero, which is an acceptable result; (b) **on uncertain needs**: the number of compounds X labels compatible or opposite that L declares indeterminable because the WWOX record states the direction is uncertain or conflicting (cite the need's counter-evidence). The reference cannot score (b); it is an information effect, listed per need, not an accuracy gain.

## Contrasting cases (chosen before scoring, justified by the contrast)
The scorer reports a case table beside the aggregate. Cases are selected by rule from the universe, not by outcome, from at least these contrasts when the data hold them, with the count of each contrast available:
1. same target, opposite action (inhibitor vs positive modulator at one NMDAR/AMPAR/T-type subunit gene);
2. same compound, different targets with opposite or different actions inside one need;
3. same target family, different pharmacology (subunit-selective vs pan-blocker; voltage- or use-dependent channel blockers; irreversible enzyme inhibitor vs reversible);
4. partial/ambiguous action versus clean action;
5. compounds whose only evidence for the target is a ChEMBL record without GtoPdb counterpart (reference unknown: kept as unknown, never as negative);
6. compounds with a documented WWOX-system result (cards) versus without.
Minimum: 8 cases, and at least one for each contrast that has data; the absence of data for a contrast is reported.

## Decision rules (stated before running)
- "L improves matching over T" only if the lower Wilson bound of L's compatible-label precision exceeds T's base rate by at least 5 points on at least 40 determinate compounds in EVAL. Otherwise "no advantage over target-only measured" is the result.
- "WWOX knowledge improves accuracy over X" only if L and X differ on directed needs and L is right where X is wrong on a paired exact sign test (p below 0.05); if L = X on directed needs, write "no measured WWOX contribution to accuracy on directed needs".
- Conservation: an unknown reference is not negative; one curated origin counts once; ChEMBL and GtoPdb share part of their literature, so agreement is not independent confirmation (state it); unresolved compounds are not counted as errors.
- If fewer than 40 determinate EVAL compounds exist, report the figure with its interval and no improvement statement; this is an acceptable outcome and is not rescued by widening the universe after the lock.

## Declared prior knowledge (retrospective, not prospective)
IT17 already compared ChEMBL and GtoPdb directions on 926 pairs (0.997 agreement) and saw six discordant pairs; the author of this registration knows that the covered space is easy. Hiding the answer table does not make this prospective. The task is retrospective on pre-existing curated data; the sealed IT17 freeze is untouched, and no prospective outcome is claimed or invented.

## Staging (order is part of the design; commits show it)
1. Executor writes `answers_lock.json` (sha256 of the code, of the DEV rule tables and of `answers.tsv` with T/X/L labels for every universe compound) and commits it **before** the GtoPdb reference for the universe is read for EVAL.
2. Reference is read and joined; EVAL scored once; the results file records the digest of the lock.
3. A different actor verifies from the files only.
