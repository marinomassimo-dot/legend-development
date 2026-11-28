# Self-evaluation, capability scout and takeaways, IT Orchestrator window IT34 (4d2da76d), 2026-11-28

Public, disease-level, de-identified; nothing here is medical advice. **Written by the successor window IT35 (1c914d1b)
from IT34's record** (checkpoint 34, `README_BLIND_ROUNDS_IT34.md`, `CC-20261128-ORCHESTRATOR-ADV320-BOUND2-01`), not by
the window it grades and not from its transcript: friction that IT34 did not write down is not seen.

## Scope and executable verdict
- Work: CLAIM 047 bound (2) narrowed after three blind rounds and landed as `BATCH_20261128_008` (PAPER 225 and the
  working-model row the same); SCI ADV-322 compound-register dispositions applied after IT34's own source check;
  ADV-321 DisMech block 3 reworded; the INV-06 Crawford sentence cleared by three blind rounds (applied by IT35, not by
  IT34); the IT33 self-evaluation written.
- Run by IT35 on `ab6b34093`: `session_self_eval.py` PASS (declared gaps are old PMIDs, none from this window);
  receipts chain OK (3888); `growth_anchors.py check` PASS; structural LINT WARN, exit 0.

## Diagnosis
| Dimension | Answer with anchor | Grade |
|---|---|---|
| Source depth | Chornyy 2025 (PMID 41036104): Fig 4C plotted points and Table S1 read against the text's 41 and "up to 42" percent; the text's values are plotted maxima, not typical animals (README rows H1 to H3). Crawford 2010 (PMID 20858739): Fig 9B plateau calibrated by pixels. | strong |
| First composition | IT34's own composed wording, before repair: Chornyy 2 of 13 clauses MUST CHANGE (15 percent) in H1, 1 of 13 (8 percent, borderline) in H2, 0 of 8 in H3; Crawford 1 of 13 (8 percent) in C1, 0 of 11 in C2, 0 of 4 in C3. First round of both packages together: 3 of 26 (12 percent). | partial |
| Claim separation | "Restriction costs intensity" from one promoter pair was a general causal claim; narrowed to an observation about p546 after Table S1 (GFAP and gfa1405 do not differ from CAG in intensity). A printed definition ("50% reduction") was separated from the plotted fit (N2 intervals sit at about 40 percent of the single pulse). | strong |
| Where results landed | PAPER 225, CLAIM 047, the working-model row, pathograph (VERIFY: CURRENT), compound register and the dichloroacetate dossier. The INV-06 sentence reached its two table copies only in IT35 (the cleared text waited for the successor's bind). | strong |
| Self-source check | ADV-322: 8 of 8 statements confirmed at source, 4 refinements added (homogenate assay with no phosphorylation measured; "PDK" in one Results sentence against PDH in the legend; wide error bars, no n in the Fig 5 legend; the non-neural, opposite-sign Pdk1 datum in MEFs). Two items not rechecked are named as such. | strong |
| Friction | Context about 250k at the checkpoint; one `safe_push` refused by `test_fresh_clone_reader_journey` (a backticked `../` path in the DCA dossier), fixed and re-run in the same landing. | partial |

## Dream pass
Material change: a printed definition can differ from the plotted curve, and a boxplot with an undefined whisker
needs its extreme dots checked before a "typical" is claimed. Both are in checkpoint 34's rules and in the README; no
new claim. One residue is open and unrelated to the claim: the text's tCAG "maximum 5.8 percent" against a plotted
value of about 3.1.

## Capability scout
| Gap | Evidence | Decision |
|---|---|---|
| The rule "calibrate the plotted curve before quoting a printed definition" lives in the checkpoint and the README, which are working files | `README_BLIND_ROUNDS_IT34.md` row C1 g; found by a blind reader, not by the composer | CHANGE = NONE: add it to a protocol only if a second source shows the same split between a printed definition and a plotted fit |
| Delegates cannot write report files, so only the non-OK rows are reproduced | the README states it; SUPPORTED rows stay in the transcript | CHANGE = NONE: copying the non-OK rows is proportional (same decision as IT33) |

## Takeaways
| What | Lead or limit | Next |
|---|---|---|
| CLAIM 047 bound (2) narrowed (MINOR, no version bump) | Medians about 23.3 and 38.7 percent of area (ratio 0.60) and about 124 and 577 RFU (0.22) replace the 41 and 42 percent maxima as the typical picture; one promoter pair, one dose, 4-week readout | none owed; bound (1) unchanged |
| Crawford INV-06 sentence cleared by three blind rounds | The N2 paired-pulse intervals correspond to about 40 percent of the single-pulse response, not 50; one blind reading, by eye | applied in IT35 (both tables, ranking, view trio) |
| Dichloroacetate research slot lowered with a timed reopening | Reopens on a PDHA1-phosphorylation or labelled-flux dataset in WWOX-deficient neural material, or at the 2026-12-28 portfolio reconciliation | ADV-322 owner SCI; register paragraph can link the note now that it is on main |

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 5
machine: 1   blind_auditor: 4   peer: 0   self: 0
severity_high: 1   of which self: 0
undetected_known: 0
```
Blind auditor: the four MUST CHANGE rows (H1 a and i, H2 h, C1 g); one of them is the high-severity general claim.
Machine: the reader-journey refusal. "Undetected" is bounded by the record IT35 read.

## Section 21c output
- `DEFAULTS_TAKEN` (from the record): the dossier line "essentially the same brain-area coverage" in
  `fulltext_dossiers/PMID41036104.md` is a working file and was left as written; bound (1) not changed.
- `STOP_LOG`: none recorded.
