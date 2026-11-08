# DREAM-2 pre-registration (written 2026-11-08 before any comparison was run)

Non-canonical working note. Not medical advice. Public edition, reference genotype class. Zero spend; the Dreams service was not used.

## What is being tested

A light Dream pass (skill `legend-dream`, helper `framework/scripts/dream_pass.py`) run inside the session close. Four real cases and three synthetic controls. Retrospective replays and observations on current work are labelled apart in the result.

## Questions fixed in advance, and what would count as improvement

| Case | Kind | Question | Counts as improvement | Counts as no change |
|---|---|---|---|---|
| D3 (E-MTAB-14792 draft) | replay of DREAM-1 | Does a searcher who starts from the access question now reach the unsent draft and the hand-off to the operator? | The draft path appears in the first file a searcher is sent to by the places where the 403 is recorded, and `dream_pass.py pointers` reports zero files that name the accession without a route to the draft in those places | The draft is still reachable only by grepping its own file name |
| D7 (HDAC5 to SLC2A1 bridge) | control | Is the correct answer still produced unchanged: `--bridges` flag, bridged rows labelled hypothesised, no sign, other cell context, off by default? | Same four points present, nothing added to the answer | Anything lost is a regression |
| Current science (NB-1, MYC) | observation on current work | Did the verified NB-1 result reach what it should influence (need, card, investigation, generator)? | Each consumer named, with the sentence that shows it; unconsumed pieces named | A defect invented where the result is already consumed |
| Generative | observation on current work | Do available pieces combine into a question or test that is not already in the repository? | A named test, with what was already there (rows) separated from what is new (the combination), and the decisive limit | Restating INV-17 or the levers in other words |

## Synthetic controls (fixtures, declared synthetic)

1. Misleading association: two entities co-cited in many files must not receive a direction or a "consistent" label from the helper.
2. Lost qualifier: a context qualifier (cell type, species) present in a source row must still be present after the helper selects it.
3. Repeated work: a question already answered in the repository must be reported as answered, not re-proposed.

## Cost

Measured: token census of this session's Dream-pass turns with `session_model_census.py` and of any delegate, setting read back. Estimated: nothing converted to a share of a plan. Not observable: the saving in later sessions.

## Not claimed

No statistical validation; four cases and three fixtures. The author of cases, helper and rubric is one. A new connection is exploratory and not a claim.
