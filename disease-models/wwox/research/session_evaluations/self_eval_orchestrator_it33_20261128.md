# Self-evaluation, capability scout and takeaways, IT Orchestrator window IT33 (5b32f251), 2026-11-28

Public, disease-level, de-identified; nothing here is medical advice. **Written by the successor window IT34 (4d2da76d)
from IT33's record** (checkpoint 33, `README_BLIND_ROUNDS_IT33.md`, `RESULT_PART_B_ADV321_IT33.md`, the commit
candidate), not by the window it grades and not from its transcript: friction that IT33 did not write down is not seen.

## Scope and executable verdict
- Work: ADV-316 step 2 wording after three blind rounds, landed as `BATCH_20261128_007`; ADV-321 part A (three
  DisMech prompts) and part B (priority display trace); one CI look.
- Run by IT34 on `01fef21dd`: `session_self_eval.py` PASS (with declared gaps); receipts chain OK (3883);
  `growth_anchors.py check` PASS; structural LINT WARN, exit 0.

## Diagnosis
| Dimension | Answer with anchor | Grade |
|---|---|---|
| Source depth | No new complete read. SCI's 21 correction statements checked blind against the whole sources: 0 of 75 clauses MUST CHANGE (the delegates saw the proposed wording, so this is agreement, not a fresh extraction). | strong |
| First composition | IT33's own composed fragments: 3 of 48 clauses MUST CHANGE (6 percent) in round 2, all repaired; 0 of 53 in round 3. One of the three misattributed a fold figure to an unnamed capsid in a working-model row. | partial |
| Claim separation | A by-eye clause on which two blind reads disagreed was replaced by the printed rows, not decided. | strong |
| Where results landed | PAPER 228 and 362, CLAIM 009, 011, 047, the working-model row, DL-MECH-159, pathograph. | strong |
| ADV-321 part B | The 40-of-199 misrouting count rests on one reader's lexical rule and says so; routed to HE for a second run (ADV-324). | partial |
| Friction | Context about 235k at the checkpoint, ADV told at 245k. `test_pathograph` failed on drift after the claim edit and was repaired in the same landing. | partial |

## Dream pass
Material change: a verified failure class, repeated. A correct correction sheet composed into new fragments gains new
errors (here 3 of 48), so composed wording needs its own blind round, and the repairs need one more. It is already in
checkpoint 33's rules; no new claim and no new rule.

## Capability scout
| Gap | Evidence | Decision |
|---|---|---|
| Delegates cannot write report files, so verdict rows live only in the session transcript unless the window copies them | `README_BLIND_ROUNDS_IT33.md`: non-SUPPORTED rows reproduced "in substance"; SUPPORTED rows only in the transcript | CHANGE = NONE: copying the non-supported rows into the README is proportional |
| No machine field gives a compound's research priority | ADV-321 part B: 0 matching header lines over `continuous_compounds/*/README.md` (query dated 2026-11-28 in that file) | CHANGE = NONE by IT: the decision note is SCI's (ADV-322), the display is HE's (ADV-324) |

## Takeaways
| What | Lead or limit | Next |
|---|---|---|
| ADV-316 step 2 landed (MINOR, no version bump) | Narrower wording on a liver-de-targeted capsid, the PMA/A23187 reading and a treatment-by-genotype statement | none owed |
| Compound programme view misroutes by clinical-disposition words | Display-only for the routing; the research priority itself is a content gap | ADV-324 (HE) and ADV-322 (SCI); IT integrates the view |
| DisMech prompts written | Outside git, in the coordination folder | one accuracy review by SCI owed |

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 4
machine: 1   blind_auditor: 3   peer: 0   self: 0
severity_high: 1   of which self: 0
undetected_known: 0
```
Blind auditor: the three round-2 MUST CHANGE. Machine: the pathograph drift test. "Undetected" is bounded by the
record IT34 read.

## Section 21c output
- `DEFAULTS_TAKEN` (from the record): ADD and UNSETTLED items that no record clause holds were not carried and are
  listed in the blind-round README; the disputed Fig 4D clause replaced by printed numbers.
- `STOP_LOG`: none recorded.
