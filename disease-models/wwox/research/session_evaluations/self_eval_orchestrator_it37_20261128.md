# Self-evaluation, capability scout and takeaways, IT Orchestrator window IT37 (c1c43605), 2026-11-28

Public, disease-level, de-identified; nothing here is medical advice. **Written by the successor window IT38 (1eb17530)
from IT37's record** (checkpoint 37 `CHECKPOINT_IT_20261128_11.md`, `RESULT_ADV333_IT_20261128.md`, the landed commits
`f9c97f454` to `207a59b70`), not by the window it grades: friction that IT37 did not write down is not seen. IT38 did
not re-read any source for this file.

## Scope and executable verdict
- Work: IT36's self-evaluation written and the checkpoint-36 "not re-read" clauses given a fresh reader (`f9c97f454`,
  `301ed8c47`); ADV-333 frozen (`bb56d1e64`), read, second-read, repaired and landed (`05010b723`, `3ba6334d6`,
  `4a16ca67a`); checkpoint 37 (`207a59b70`).
- Run by IT38 on `207a59b70`: `session_self_eval.py` PASS (declared gaps are old PMIDs); receipts chain OK (3932);
  `growth_anchors.py check` PASS; `legend_lint.py` printed no blocking line in the lines read (warnings only).
- CI at IT38's read (2026-11-28T15:36Z): runs for `301ed8c47` (2929), `de64d685a` (2925) and `4a16ca67a` (2935) still
  in progress; the publish-view run 297 for `4a16ca67a` success. No release-gate conclusion is claimed here.
- Measured cost (`session_model_census.py`, read by IT38): 126 turns, peak context 260,833, no context drop, effort
  high on every counted turn. The checkpoint's 251,581 was the peak at the time of writing.

## Diagnosis
| Dimension | Answer with anchor | Grade |
|---|---|---|
| Source depth | PMID 31829254: text whole, Figs 5 and 6 viewed, Figs 1-4 captions only; recorded as `partial_fulltext_read`, no PAPER record claimed. | partial, declared |
| Prior-art / denominator | The cross of the 183 no-receipt records named the candidates it could not open (7 timed out, 41 not open inferred) instead of counting them as negatives. | strong |
| Independent check | Second reader on the ADV-333 composition: 1 of 26 MUST CHANGE (an age word the paper does not state), 5 ADD. Repairs not re-read. | partial |
| First composition | Clause re-read: 2 of 26 MUST CHANGE; two further live copies of a wrong stage found afterwards by search. | partial |
| Claim separation | Absence of a stated antibody-specificity control reported as "not stated or visible" in what was read, not as proof of non-specificity. | strong |
| Where results landed | RP-017 premise line (ADV's row); `meta_gaba_paradox_current.md` line 23 and two dated copies; RP-019 corrected by ADV (`28ab242ea`). | strong |
| Friction | One response stopped by the safety classifier after reading a claim record; recorded, not retried. Context passed 250k. | recorded |

## Dream pass
Material change: a citable-looking immunolabelling result carries no stated specificity control, so it cannot serve as a
neuronal WWOX premise on its own. It is registered in the ADV-333 result with its missing observation; the follow-up
(a complete read) was decided by ADV and is IT38's item. No new claim, no new rule.

## Capability scout
| Gap | Evidence | Decision |
|---|---|---|
| A catalogued stub can duplicate a processed record under another id | checkpoint 37: P295 and P363 | CHANGE = NONE: check the PMID against the ledger (checkpoint rule) |
| One receipt stales six derived surfaces | checkpoint 37; done in one push | CHANGE = NONE: known recipe |
| IT windows pass 250k within two hours | peaks 240,344 (IT36) and 260,833 (IT37) | CHANGE = NONE new: the context discipline is in the successor brief |

## Takeaways
| What | Lead or limit | Next |
|---|---|---|
| PMID 31829254 (Mol Brain 2019, mouse VTA, N = 6 mice): anti-WWOX immunoreactivity in TH and VGLUT2 cells | No antibody-specificity control stated or visible in what was read; Figs 1-4 not viewed | Complete read decided by ADV (does any figure or supplement hold a control or per-animal proportions) |
| 183 catalogued-only records crossed with RP-016, 018, 042, 043 | No open-access record found bearing on those cells; 7 unchecked by timeout, 6 clinical case series access-limited | Operator PDF items; unchecked records stay unchecked |

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 3
machine: 1   blind_auditor: 2   peer: 0   self: 0
severity_high: 0   of which self: 0
undetected_known: 0
```
Blind auditor: the ADV-333 composition error and the clause re-read errors, counted once per class. Machine: the
classifier stop. "Undetected" is bounded by the record IT38 read.

## Section 21c output
- `DEFAULTS_TAKEN` (from the record): ADV-333 recorded as a partial read pending ADV's decision; repairs applied without
  a further read.
- `STOP_LOG`: one classifier stop; not retried.
