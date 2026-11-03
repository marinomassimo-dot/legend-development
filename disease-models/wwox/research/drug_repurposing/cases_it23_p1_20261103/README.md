# IT23 P1: which gap is worth closing, on which cases (frozen before any new capability)

Non-canonical. Not medical advice. Baseline: `main` `03ac7b8c` (IT22 closed: release gate green, served page equals the package). The current method is frozen in `frozen_current_method.tsv`
(862 rows of the IT22 final stage table for the three cases) and `frozen_inputs.tsv` (digests of every input and code file it used); both are committed before any IT23 capability exists.

## Where the useful chain breaks today (read from the frozen tables)

| Break | Evidence in the frozen table | Capability that could address it |
|---|---|---|
| Knowledge present, not consumed | Q5 has 282 rows in 55 mechanism clusters, but the biggest cluster sizes are targets with many same-mechanism family members (Q6: NR3C1 80 rows, JAK2 43, BRD4 38): rows are not independent hypotheses | relation provenance (one origin counts once): P2 |
| Direction or role uncertain | every question has role `unknown`: both arms (`H_HARM`, `H_PROTECT`) are generated, the engine cannot say what separates one intervention from another on consequence | consequence simulation under explicit scenarios: P3 |
| Profiles on several targets cannot be compared | a compound is credited through ONE chain from ONE listed target; BRD4 appears in 43 Q5 rows, each scored on its own chain | multi-protein profile comparison: P4 |
| Insufficient data to separate rival hypotheses | for Q8 one usable seed (organoid transcript, second system failed its control) | name the measurement; do not simulate (P3 rule) |

## Cases (contrasting; chosen from current data, not because a gene is differentially expressed or central in the graph)

| Case | Why | What it tests |
|---|---|---|
| Q5 cytokines (IL6 significant in the null hippocampus; IL1B and TNF up in P47T cerebellum; organoid below the floor) | the direction is the best sustained one: two independent mouse preparations agree in sign, at transcript level only | an intervention space with a sustained direction and an unknown role (damaging, protective, consequence of seizures) |
| Q6 MYC in radial glia | one within-cell-type contrast; the rise could be a driver, a marker of retained progenitor state or a compensatory response; IT21 P3 and IT22 records already show one DOT1L, AURKB and CDK4 thread each | an alteration that may be COMPENSATORY: an inhibitor of the node and an inhibitor of its upstream driver can have opposite consequences |
| Q8 NFE2L2 | lower in one organoid contrast; the second system failed its control; adjusted p above the deposit's own alpha | the case where inputs are NOT sufficient: the correct output may be an abstention that names the measurement |

Vorinostat stays a known diagnostic case (IT21), not a blind test. Cases used to BUILD a method are listed in P6; predictions for the unseen cases are frozen before verification.

## What is frozen

`frozen_inputs.tsv`: seeds, the Q5/Q6/Q8 engine seed sets, roles, annotations, the family action table, the IT22 stage tables, the decision scope table and the engine code. `frozen_current_method.tsv`: for the three questions every proposal row with its chain, z-scores, status, eligibility, blocker, attribution state, carried limits and hand-over flag.
Re-run `python3 freeze_current_method.py` to check that nothing frozen has changed (the digests must equal).
