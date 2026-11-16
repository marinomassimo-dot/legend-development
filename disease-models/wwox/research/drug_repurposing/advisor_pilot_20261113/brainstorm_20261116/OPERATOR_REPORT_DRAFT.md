# Running synthesis for the operator (ADV; updated at each checkpoint; non-canonical; not medical advice)

State as of 2026-11-16 08:0xZ (programme started 07:10Z; closing synthesis not before 15:10Z). Mechanism matching only: no dose, no recommendation to use any agent; BLOCK-1 not yet applied to any agent.

## Item 3, antiseizure agents: what the matrix says and does not say
* Classes, seizure endpoint, P13-P15 (frozen at f5b71a3f4345, rule.json sha256 679a6089..., 244 cells, 16 threads): a five-way top tie at 9 (NMDAR pore blockers, GABA-A positive modulators other than benzodiazepines, benzodiazepines, sodium-channel blockers, valproate-type). With the single origin collapsed the top set is three classes (NMDAR pore blockers, GABA-A PAM, benzodiazepines). Informativeness 0.67 (weak) and 0.80.
* Why it is weak, and the result in itself: every scoring thread comes from ONE origin (Breton 2021, neocortical bursts, absent in hippocampus). The origin hunt (SCI, 12 of 12 quotes checked) found NO independent origin for T1, T2, T13; the only independent origin on the inhibition axis is Aldaz 2019 (hippocampal PV+ loss), a different region. The GABA-axis conclusion is region-confounded as well as single-origin.
* A specific agent: NOT supported. No cell discriminates two agents inside a class, the generator therefore prints no agent ranking. The only agent with a WWOX experiment is ethosuximide and its WWOX specificity is not shown (no drug-by-genotype test; the extraction cannot exclude a proportional effect; lithium acts in all genotypes).
* Mismatch (aggravation) is kept apart: sodium-channel aggravation (AH1) is `unknown`; one rodent-premise hypothesis (NMDAR pore blockers, development, P6-P8) is recorded as such. No held statement supports or refutes it.
* Robustness: a post-hoc correction of 32 cells after an independent second read of 25 cells (21 say it, 1 locator wrong, 2 tiers and 1 directness proposed) leaves the top set unchanged (stable in 28 of 36 perturbations, size 4-5).
* The decisive step is an experiment, not more reading: a head-to-head of an NMDAR pore blocker against a GABA-A positive modulator on the same burst readout, in both regions and both genotypes, with a wild-type trigger or evoked-current control, and a sodium-channel arm for AH1. SCI's EXPERIMENT_BRIEF.md is due 10:30Z; IT triages the arms through BLOCK-1 afterwards.

## Item 1, predictive-generative capacity: measured, not claimed
* Starting reference (IT's baseline table, 137 predictions in 34 files): generative predictions held 16 of 33 scored (48%, mixed counted as not held); paper-content 37 of 56 (66%); predictor = scorer in 45 of 89 scored rows. Any claimed improvement is set against 48% with its interval and with predictor != scorer.
* Built today: a prediction ledger with four git-checkable guards (HE, prediction_ledger.py), a reproducible matrix generator with a pinned rule hash, tie sets, origin collapse, a degenerate-null report and a bounded stability enumeration (aed_matrix.py), a path for an aggravation hypothesis to reach a consumer without becoming a proposal to use a compound (cf41376f3), role separation (SCI predicts, a memory-free delegate is the baseline arm, IT keeps the ledger and scores, a blind extractor codes outcomes after both freezes).
* Declared in advance: the held-out A1 table covers four classes (seizure endpoint n = 11, 8, 8, 4; development 5 and 3), so at most 6 class pairs: the A1-only test is pre-declared UNINFORMATIVE for any 'beats baseline' claim (at least 10 class pairs needed); only the blind extraction of other-agent statements can lift it. The prospective registry (at least 10 predictions with dated outcome sources) carries the test of generative gain.

## Item 2, the new batch
Chosen: AED mechanism matching with a genotype contrast ending in a discriminating experiment design, with NMDAR/GluN2B by age as the experiment arm (aggregate 57 against 53 and 45). First packages delivered: matrix and freeze, second read, origin hunt, corrections. Next: experiment brief, BLOCK-1 triage, blind extraction and scoring, prospective registry.

## Cost so far (units, from the sessions' own readings; not a quota)
Baseline-arm delegate 6 turns, 40,573 output tokens; second-read delegate 30 turns, 32,907 output; main sessions not yet tabulated for this programme (trial_window_table.py at the close).
