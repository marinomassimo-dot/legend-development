# K1 · A record that cites a paper by its record link cites the paper

> Design record, harness only (non-normative about science). Nothing here changes a claim, the
> working model, an evidence grade or a disease-model conclusion. Date: 2026-09-26.
> Evidence: Benchmark I ([`I1_RESULTS.md`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/I1_RESULTS.md),
> fixture I03; [`i1_posthoc_backlink_mention.json`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/i1_posthoc_backlink_mention.json)).

## The semantic change

`registry_records.py get --pmid P` (and `--doi D`) now also returns, as a `mention`, every
record whose text **wikilinks to an identity record of the query**. The hit is labelled with the
link it rests on: `mention (links to paper_registry_current#PAPER 021)`.

- **The alias set** is the query's identity records only — records whose declared identifier
  fields (`Identifier`, DOI, PMID) name P or D — computed over the corpus the command already
  loaded, by the same test the `identity` branch uses. A record that only *mentions* P in prose
  is not an alias, so a link to it is not read as a citation of P.
- **Unchanged:** `identity` hits; plain prose `mention` hits; the outward `--hops` walk (a record
  a hit links **to** is still reached only by `--hops`, and labelled `linked from … (hop n)`);
  sections are still named, never carried; no ranking, stemming, synonyms, embeddings or index.

## Why `CaseEReachableOnlyByExpansion` changes

It pinned that, for PMID 33914858, **no** claim is returned at hop 0 and claims appear only at
hop 1. Two of the claims it pinned as "reachable only by expansion" — CLAIM 003 and CLAIM 015 —
reach the paper only because they carry `[[paper_registry_current#PAPER 004]]`, PAPER 004 being
that PMID's identity record. That is exactly Benchmark I's I03 miss (CLAIM 015 → PAPER 021 →
PMID 31340538): a claim that cites the paper was invisible to the command meant to find what
rests on it. Benchmark I reverted the repair because it changed approved semantics; K1 changes
them deliberately.

What the test pinned and still holds, and is still pinned: a claim the paper record links
**out** to, and which does not itself cite the paper (here CLAIM 002, 004, 016), is reached only
by `--hops`, and the expansion stays explicit in the rendered limits.

## Expected effect (from the post-hoc file) and measured effect

| Benchmark I, STRONG (29 targets) | before K1 | post-hoc prediction | measured after K1 |
|---|---:|---:|---:|
| CURRENT targets retrieved | 13 | 17 | **17** |
| CURRENT median registry fraction | 2.6 % | 3.5 % | **3.5 %** |
| PROGRESSIVE targets retrieved | 25 | 26 | **26** |

All 78 fixture × strategy rows are identical to the post-hoc file. Size guard and the full
numbers: [`I3_DECISION.md`](../../framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/I3_DECISION.md) § K1.
