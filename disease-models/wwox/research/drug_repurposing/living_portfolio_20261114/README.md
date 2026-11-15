# Living Research Portfolio

Implemented by Harness Engineering (ACTOR_ID plan), on the operator's explicit request of 2026-11-14.

## Permanent source and purpose

[research_portfolio.tsv](../research_portfolio.tsv) is the one operational opportunity portfolio. The [operator roadmap](../roadmap_current.md) retains mission authority, the open-question and candidate records retain scientific meaning, and linked task records retain execution status. The twenty initial rows are research opportunities, not new findings, assignments or predicted therapeutic effects.

The portfolio covers generation, the first-five-unit review, prioritised open questions, new science batches, EVAL, batch diagnosis, old and new radars, PubMed updates, memory/DREAM, tool use, predictive graphs, public datasets, dashboard clarity, variant mechanisms, antiseizure comparisons, myelination, ISR, cell context and harness simplicity. Some are ready to assess, others are backlog or wait for a new premise. Readiness is not an instruction to launch every row.

## Read and feed

From the primary checkout:

```bash
python3 framework/scripts/strategic_advisor.py portfolio
python3 framework/scripts/strategic_advisor.py portfolio --id RP-003
python3 framework/scripts/strategic_advisor.py portfolio --json
```

A partial update is a JSON object, for example:

```json
{"id":"RP-003","mandate_id":"ACTUAL-RECIPIENT-TASK-ID","outcome":"Result and consumer pointer; next question if one remains"}
```

Save that object to a local file, then use:

```bash
python3 framework/scripts/strategic_advisor.py portfolio --upsert /tmp/opportunity.json
```

Other fields and rows survive. Writers share a host-local lock; replacement is atomic. Direct TSV edits remain possible. Git preserves the history. A linked mandate owns execution; its release requests a consumption review rather than automatically closing the opportunity. An unresolvable task is UNKNOWN, never silently treated as available work. Mark `done` or `retired` only with the actual disposition in `outcome`; a future question gets its own row or an explicitly revised action.

The read-only analyst may return an optional section:

````markdown
## Portfolio updates
```json
[{"id":"RP-NEW","opportunity":"Question raised by the result","status":"backlog","sources":"path/to/original-package.md"}]
```
````

The existing evaluation procedure saves the assessment verbatim and applies these advisory updates. No section is required when nothing changed. Invalid updates are reported, not an approval gate. SCI, IT, HE and the hosting ADV session feed pertinent rows at material handoffs, following transport section 12.

## Consultation and recall

ADV finds the stable path in its agent definition, skill, entry points, roadmap and every Stage P brief. It consults the index on startup/resume, after compaction, before assignments, after material results, when the queue ends and before a portfolio-wide wait; the selected complete sources support substantive decisions.

The existing recall observes semantic changes, linked mandate outcomes and resolved dependencies even without a new radar. A deferred portfolio event remains visible until an evaluation consumes it. Timestamps and row order do not themselves wake a model. Operator pause, disable, resource checks and the existing evaluation rhythm still prevail. No new scheduler or service is installed.

## Verification and limits

The tests use the repository's stand-in runtime: a new row reaches a saved Stage P brief, an assessment patch feeds a new follow-up back into the portfolio without rewriting the assessment, a deferred change is not lost, and a time-dependent opportunity becomes actionable without a radar. They also verify source-preserving updates and that task release is not mistaken for consumption.

This proves the mechanical path, not that a future model selects the best scientific work or updates every row. Real delivery, uptake and scientific usefulness remain observed outcomes of the continuing trial. The implementation uses the existing evaluation runtime and recall; it adds no service, external spend or estimate of subscription quota.

## First live use

The existing ADV recall started [assessment P9](../advisor_pilot_20261113/P9/assessment.md) at 2026-11-14 22:23:29 UTC and completed it at 22:25:55 UTC. Its [metadata](../advisor_pilot_20261113/P9/meta.json) records a read of the complete portfolio. The optional assessment updates were applied to RP-005, RP-008 and RP-017, demonstrating both input consumption and the return path.

P9 drafted a literature census for RP-008. The hosting ADV session then checked the original scout implementation, declined the draft as duplicative on its stated premises, and revised RP-008 with the reason and a narrower reopening condition. The draft remains visible in the assignment history; it was not dispatched or taken in charge. This is evidence of actual use and correction, not evidence of improved scientific prediction or a new literature finding. The original 24-hour trial window remains unchanged.

Removal: delete the portfolio branches, its entry point, TSV and routing paragraphs; existing consultation and proactive campaign modes remain usable. The original trial window and counters are untouched.

## Session learning record

Session: PLAN-LIVING-RESEARCH-PORTFOLIO-20261114 · Date: 2026-11-14 · ACTOR_ID: plan · Role: Harness Engineering · Task: same id, version 1, generation 1.

| Field | Observed result |
|---|---|
| WORK COMPLETED | One persisted opportunity portfolio, update command, recall input and assessment return path, routed through the existing Advisor. |
| PROBLEMS | The first targeted checks caught an oversized agent definition; the first live proposal relied on a mistaken duplicate-check premise. My temporary-directory choices also caused a browser visibility failure and then ignored privacy fixtures. |
| SOLUTION | Shortened the definition without relaxing the limit. The hosting ADV checked the originals, declined the proposal and corrected the portfolio. Checked both browser access and privacy/inventory fixtures before repeating with a non-ignored temporary directory outside repositories. |
| LEARNING | A durable pointer and a tested consumer are necessary; successful consultation still does not establish good strategic selection. |
| MICRO-UPGRADE | Reused the existing evaluation and recall rather than creating another scheduler or task authority. |
| IMPACT | Twenty initial opportunities became retrievable inputs; three were fed back by a real assessment. No scientific claim or ranking change is attributed to this implementation. |
| CLASSIFICATION | Harness capability and observed procedural use. |
| SCOPE | ADV consultation and material SCI/IT/HE handoffs; scientific evidence and execution remain in their existing records. |
| EVIDENCE | Implementation 614db32d7, new LivingPortfolio tests, P9 assessment and metadata, and the corrected RP-008 outcome. Verification scope is recorded in the task record. |
| LEARNING_ID | PLAN-LIVING-RESEARCH-PORTFOLIO-20261114-L1 |
| CONFIRMATION_CLASS | Mechanical tests plus one live use; scientific decision benefit unmeasured. |

## Verification environment incident

The first complete-inventory attempt on 614db32d7 completed 226 suites without a nonzero suite exit, then accumulated browser waits. The page file existed on the host but not under the running Snap Chromium process's filesystem root. A separate synthetic HTML fixture loaded successfully with the same installed browser from the project's ignored `tmp/` directory. Browser startup and a working DevTools endpoint had not established access to the workload's files.

Only this actor's runner and its checked descendant identities were stopped. That attempt is **INTERRUPTED WITHOUT VERDICT**, not PASS. Its original log and interruption receipt remain local.

The second attempt on b6270eab80d7d14894573768fc351975cceb3253 ran the browser suite first: 225 tests PASS. My choice of an ignored temporary directory inside the project then caused fixture discovery failures in `test_public_release_gate.py` and `test_release_runner_verdict.py`. Those failed suite results remain recorded; the attempt was interrupted, not relabelled PASS.

A dedicated, non-ignored temporary directory outside all repositories passed the synthetic browser-file probe, 62 privacy tests and 20 runner tests. The standard complete inventory is repeated in a fresh clone of f5cba5948fa8e241811c79c141c8236bf5838a46 with that `TMPDIR`. No sandbox-bypass flag, new browser installation or weakened assertion is used. RP-020 records the small workload-probe opportunity for ADV to assess; no additional gate or service was implemented.

## Final verification

On 2026-11-15 the standard complete inventory on **f5cba5948fa8e241811c79c141c8236bf5838a46** finished **PASS WITH SKIPS: 251 targets, 43 skipped tests**, with every suite exit 0. This includes 109 Advisor tests, 225 dashboard tests and 14 language tests. The skips concern absent local corpus, caches, inputs or host-specific conditions; the [task record](../../../../../ledger/tasks/plan/PLAN-LIVING-RESEARCH-PORTFOLIO-20261114.json) retains the exact reasons, log digest and earlier attempts. LINT is WARN without BLOCK; the current privacy scan found no BLOCK and no findings in changed files.

The runner returned 0 and removed its PID file. The hosting command transport nevertheless reported 143 after printing `BATTERY_EXIT=0`; that distinct observation is retained in the task record. It does not replace any suite result.

The full-inventory verdict belongs to the named candidate. Subsequent changes concern this guide, the task record and portfolio follow-through; the publication uses targeted closure checks and the public release gate on its exact commit. The completed mechanical and live-use checks do not establish improved scientific prediction or strategic decision quality.
