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

This proves the mechanical path, not that a future model selects the best scientific work or updates every row. Real delivery, uptake and scientific usefulness remain observed outcomes of the continuing trial. No new model invocation, subscription quota estimate or external spend is required by this implementation.

Removal: delete the portfolio branches, its entry point, TSV and routing paragraphs; existing consultation and proactive campaign modes remain usable. The original trial window and counters are untouched.
