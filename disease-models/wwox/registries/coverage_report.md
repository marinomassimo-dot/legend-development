# Corpus coverage and reading debt — WWOX

> **Generated file — do not edit by hand.** Regenerate with:
> ```bash
> python3 framework/scripts/coverage_report.py --disease wwox \
>     --out disease-models/wwox/registries/coverage_report.md
> ```
> It is a *view* over the canonical registries plus the append-only receipt ledger,
> never a second source of truth. A regression
> test re-derives it and fails if this file has drifted.

## Why this page exists

LEGEND ranks sources to order reading, **never to justify not reading them**. A source
that has not been read yet is *reading debt* — tracked, not discarded. That principle is
only credible if the debt is countable, so here it is counted, including the part that
makes the project look incomplete. It is supposed to look incomplete: the denominator is
the whole known corpus, not the part already processed.

## Coverage

| Depth | Records | Share | What it means |
|---|---:|---:|---|
| **Full text depth** | 68 | 16% | complete receipt or legacy registry declaration; trace split below |
| Partial full text | 9 | 2% | some sections read; explicitly declared incomplete |
| Abstract / screened | 13 | 3% | classified from metadata and abstract; no full text read |
| Catalogued only | 333 | 78% | known, deduplicated, never analytically processed — **the debt** |
| Filtered / superseded | 3 | 1% | explicitly set aside, with the reason preserved |

- **70** promoted `PAPER` records · **356** `CORPUS` placeholders
- **390** lifecycle entries in the literature tracking log
- **381** unique PMIDs known across the registries

## Receipt trace

- Authoritative ledger: `disease-models/wwox/registries/fulltext_read_receipts.jsonl`
- **145** append-only events: **122** contemporaneous · **22** conservative legacy reconstructions
- **55** registry records have a persisted `complete_fulltext_read` receipt
- **13** records still rely on a historical registry full-text declaration without a surviving complete coverage receipt
- **17** receipt event(s) do not yet map to a registry record

A full-text marker in the registry is preserved as historical state, but it is not
retroactively converted into a complete receipt. Only a contemporaneous or adequately
evidenced legacy receipt with a complete coverage map closes the trace.

## ⚠️ Historical reading debt

The registry is known to
under-record. An audit on 2026-07-25 against the private working archive found **80**
distinct full texts that had actually been retrieved and worked; **43** of their PMIDs are
present in this registry, and only **5** of those carried a declared `Evidence depth`.
The remaining records were read but never had the field set — the work happened, but
a public receipt cannot be reconstructed without surviving evidence.

Back-filling them is evidence work: it requires checking each record against surviving
dossiers or the retrieved text, not flipping a field because a PDF exists. A
downloaded file is not a read paper, in the same way that protein abundance is not
function — see `PROTEIN_STATE_IDENTITY_GATE` in the learned-gates registry. Until that
back-fill is done, **treat the full-text figure here as a floor, not an estimate.**

The number is published in this direction on purpose. Understating your own coverage is
the safe error; the unsafe one is a metric that reads a filename as evidence of reading.

## How to read these numbers honestly

A high catalogued count is **not** a backlog failure — it is the anti-false-negative design
working. Every one of those records was deduplicated against the registries and kept with its
identifiers, so it can be retrieved the moment a new mechanism makes it relevant. The failure
mode this prevents is the opposite one: a paper screened out, forgotten, and never reconsidered.

It happened once, and it is why the reading-debt tooling exists: a paper sat in the corpus
marked high-relevance and unread while the same conclusion was reconstructed from scratch
in silico. Surface those first:

```bash
python3 framework/scripts/unread_gold.py .
```

## Bringing new studies in

Never start from a raw bibliography. Deduplicate it against the registries first — the intake
gate answers *known / in-pipeline / new / ambiguous* before any retrieval effort is spent:

```bash
python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \
    --workspace . --input your_pubmed_export.txt --out triage.md
```

Then the batch sweep and the priority matrix order what to read first. See [`SKILLS.md`](../../../SKILLS.md).

## Scope

Bibliographic metadata only — identifiers, titles, processing state. No full texts are
redistributed and no individual-level information appears here.
