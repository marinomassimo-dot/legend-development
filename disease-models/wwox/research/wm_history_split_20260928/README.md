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

**Second known limit — the rule class A was assigned by.** `census_brief.md` defines "a place a
current reader still sees" as the working model's live sections **or** the claim record the
statement qualifies, on the stated ground that *every route that loads the working model loads the
claim registry whole beside it*. That ground is a premise about **routing**, and it was
asserted in the brief rather than verified route by route before the classification. Measured
afterwards, on 2026-09-28, it is **false for one documented route**:

> `.claude/skills/legend-aso-designer/SKILL.md:35` (step 0, *Load the context*) names *"the working
> model, the discovery ledger, the therapeutic strategy portfolio (to avoid duplication), the
> hypothesis ledger"* — and no claim registry. `grep -c claim_registry` over that file returns
> **0**; the only occurrence of the word `claim` in it is inside the not-medical-advice disclaimer
> at line 60, so no later step picks it up.

Every other documented route checked supports the premise, so this is one exception and not a
pattern: `framework/manuals/operator_manual.md` § 1.1 / § 1.2 load both *per intero* for MINIMAL,
STANDARD and FULL, and `legend-hypothesis-forge` step 0 (`:56`) loads *"the working model and claim
registry whole"*.

So for every A unit whose `represented_at.where` is `C` (the claim registry) rather than `L` (the
working model), the unit is safe to leave cold on every route **except** the ASO-design route,
where the carrying surface is not loaded. That exception matters out of proportion to its count:
it is the route whose output is candidate sequences against a splice allele, and a therapeutic
bound, safety caveat or genotype limit classed A on a claim-registry representation does not reach
a reader designing there. Those units are the first the review should sample, ahead of a uniform
sample of the `C`-carried population.

**The route list the premise was checked against** — recorded so the next split does not re-assert
it from memory. `legend-start` · `legend` · `legend-deepdive` (skill and agent) ·
`legend-discovery` · `legend-hypothesis-forge` · `legend-aso-designer` — the six skills whose prose
names the working model — plus `framework/manuals/operator_manual.md` § 1.1 / § 1.2 / § 2. Of those
six, `legend-aso-designer` was the sole exception; the ex-post review re-derived the survey by
prose rather than by path token and found no second. The premise therefore held in practice, but
only by the accident of another step's mandate (`legend-start` loads the claim registry whole in
every profile, and `CLAUDE.md` § 2 makes that row apply without being asked), which left the
direct-invocation case exposed. A rule that holds by accident is one nobody can rely on next time:
**the brief asserted the premise and never checked it, and class A rests on it.**
`census_brief.md` is deliberately **not** annotated — it is evidence and stays byte-identical to
what the reviewers worked from; this README is where its limits are recorded.

**Third known limit — enumeration is not completeness.** Both checks above are only as complete as
the two reviewers' `live_elements` lists. `migration_check.py` verifies the elements they
nominated; nothing measures whether they nominated everything a unit asserts. Density is not
coverage: one element per ≈180 B of unit text, and no A unit without a quote, still leaves a
sentence nobody listed unjudged. Measured instance, found by the ex-post review: the unit-misprint
assertion that `BATCH_20260928_005` later had to retract was nominated by **neither** reviewer, so
`H005` and `H021` were classed A without the census ever judging that sentence. (That retraction
composes anyway — the hot file asserts no unit token at all, so no hot-file reader can meet the
unretracted statement — but the class was reached without the judgement, which is the limit.)

Found by the Orchestrator session, which checked the skill files rather than citing a remembered
census, and reproduced here before this paragraph was written; the enumeration limit and the route
list are the ex-post review's findings `X2` and `A14`.

Raised by the Orchestrator session on 2026-09-28 while dispatching the ex-post Mirror review, and
recorded here rather than acted on: the A units whose carrier is the claim registry are the
population that review samples, and a producer re-grading its own census after seeing the objection
is the weaker of the two available answers. If the rider bites, the repair may be a promotion (a
Scientist's, through `BATCH_COMMIT`), a pointer from the carrying claim record, or a correction to
what a route's documentation says it loads (Harness Engineering's) — which of the three is for the
review to say, not for this file to assume.

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
