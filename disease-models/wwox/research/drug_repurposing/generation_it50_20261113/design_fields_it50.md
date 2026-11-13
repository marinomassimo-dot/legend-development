# Design-only knowledge: what the fields mean scientifically, and one real case (for Harness)

Non-canonical working note. Not medical advice. This note gives the scientific meaning of the fields of a design package and one real case; it builds no reader (Harness owns the minimal link) and makes no design retroactively a result or a prediction.

## Real case
`isrib_discrim_20261108/output/design.tsv` (steps 0-4) and `cards.tsv` (CARD-A1 ISRIB probe, CARD-A2 abstention). The IT49 case INV-02 showed it is not read by the generator; IT50 restated its hypotheses in the hypotheses layout (`isr_inv02_it50_20261113`) so they act now. What a design reader would add on top is **only** the part the hypotheses layout cannot hold: the branching.

## Fields of `design.tsv` and what each means
| Field | Scientific meaning | Becomes, in a conditional proposal |
|---|---|---|
| step | one experiment in an ordered programme; "0" qualifies readouts before any arm | the step label, never a result |
| condition_on | the earlier step and the outcome that must hold before this step is worth running | the **precondition** (unmet until that step has been run); never "assumed true" |
| question | what this step asks | the question of the discriminating measure |
| arms | the comparisons run in the step (cells, controls, compounds as arms) | the arms of the discriminating measure; compounds named here are arms, not candidates |
| readouts | what is measured | the readouts; a readout is not an engagement control unless the field says so |
| controls_already_qualified_in_module | controls whose behaviour the module already documents | **controls previously ignored by a simple search** (the engagement control, the mTOR-branch arm) |
| decision_it_changes | which research decision depends on the step | the decision at stake of the open question |
| if_result_X_then | the branch table: each possible outcome and the next step | the **discriminating results**, one per outcome; they are outcomes of an experiment, never expected results |

## What a design must never become
An expected result (the branch table lists what each outcome would mean, not what will happen); an observed result (a design has none); a direction (the branch for "benefit seen" is conditional on the data); an approved plan.

## What would be usable once the link exists
(1) A control the generator ignored: the engagement control (eIF2B assembly shift by sedimentation) in every ISRIB arm. (2) A comparison now representable: the node comparison of ISR2 with its branches. (3) A conditional hypothesis that was lost: ISR1 through ISR3 (done here by restatement). (4) A changed question or experiment: the plate content of the first experiment (step 0 before step 1).
