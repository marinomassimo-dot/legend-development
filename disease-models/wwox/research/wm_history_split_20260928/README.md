# Evidence for `BATCH_20260928_004` — the working-model history split

The per-unit evidence behind
[`CC-20260928-WM-HISTORY-SPLIT-01`](../commit_candidates/CC-20260928-WM-HISTORY-SPLIT-01.md)'s
99-unit map, persisted after the batch landed so the classification is re-derivable from the
repository and not only from a session scratchpad. Byte-identical to the files the batch used;
`SHA256SUMS` fixes them.

| File | What |
|---|---|
| `census_brief.md` | the one brief both reviewers worked from (classes A/B/C/D, what "represented" means) |
| `history_units.json` | the 99 units cut deterministically from `working_model_current.md` at `a923e10` (uid, lines, verbatim text) |
| `census_producer.json` · `census_verifier.json` | the two independent classifications, with every `represented_at` quote and every B proposal |
| `promotion_sources.json` · `promotion_verdicts.json` | the six promoted units and the third agent's verdicts on the restatements (three fixes, applied as recorded in the batch report) |
| `ops.json` | the seven record-scoped operations `batch_commit.py propagate` applied |
| `migration_check.py` | the deterministic check, as run |

**Known limit, stated so no one over-reads it.** `migration_check.py` verifies **presence**: each
unit verbatim in the cold file, each quoted string still in the live working model or the claim
registry, each promoted phrase live. It cannot see a qualification that survives only in a weaker
form, or only by combining two present sentences. That is the question put to the ex-post Mirror
review (four self-nominated weak points, dispatched by the Orchestrator on 2026-09-28).

Re-run from the repository root, **pinned to the batch's own commit** `1e130f0` (0 failures):

```bash
D=disease-models/wwox/research/wm_history_split_20260928; R=disease-models/wwox/registries
python3 $D/migration_check.py $D/history_units.json $D/census_producer.json $D/census_verifier.json \
  <(git show 1e130f0:$R/working_model_current.md) <(git show 1e130f0:$R/working_model_history.md) \
  <(git show 1e130f0:$R/claim_registry_current.md) <(git show a923e10:$R/working_model_current.md)
```

Against a later tree it reports every later edit of the moved text, by design. Measured on the
tree after `BATCH_20260928_005` (`c8827a4`): units **H001, H005, H017, H021** are no longer
verbatim because that batch corrected them in place under `prompt_batch_commit.md` § 7.2 — each
correction names `CC-20260928-A1-RESIDUE-01`, the date and the wording it replaced — and the hot
file's header changed with its version bump to `WM_v7.4`. Those five findings are expected; any
other one is not.
