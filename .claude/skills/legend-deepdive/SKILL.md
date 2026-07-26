---
name: legend-deepdive
description: Runs the LEGEND analysis pipeline on the papers the operator provides (group credibility → full-text → dossier → deep-dive) with multi-hop expansion to relevant related/cited papers, and produces a COMMIT CANDIDATE. Use it after the operator has indicated the papers to analyze. It does not start analysis on its own initiative.
---

# legend-deepdive — Analysis pipeline

Paths are relative to root.

> **Full method manual: [`framework/manuals/deep_dive_manual.md`](../../../framework/manuals/deep_dive_manual.md).**
> This skill is the executable summary. The manual is the normative procedure — coverage discipline, the epistemic tag required on every extracted statement, transfer assessment across genotype / model / endpoint, the deep biological mechanism output, cross-domain research expansion, the strategy space (repurposing and biomarkers), limits and uncertainty, commit impact and change log, and the methodology log. When the two disagree, the manual wins.

## Human gate
Starts ONLY from the papers the operator provides. From there it expands.

## Pipeline (per paper)
1. `research-group-analyst` (subagent) → group credibility + author disambiguation.
2. `find-fulltext` (skill) → PDF/full-text retrieval.
3. `fulltext-dossier` (subagent) → neutral extraction into `staging/`.
4. `legend-deepdive` (subagent) → COMMIT CANDIDATE + inbox proposal (read-only toward the current files).

## Full-text rule: the details of every study
The gold is in the details of every full text, not only in papers already labelled important.
- `grep`/keyword search is forbidden as a *method of study analysis*. It may be used only to find files, dedup, or do technical audit after reading; never to decide what a paper says.
- For each available full text, `fulltext-dossier` and text parsing are readability/anchoring tools, not substitutes for reading.
- The output must include a section-by-section coverage map: Abstract, Intro, Methods, Results, figures, tables, Discussion, Supplementary if available.
- Methods, secondary results, figures/tables, limits and supplementary materials must be checked for assays, reagents, models, pathways, biomarkers, safety, failure modes and repurposing leads.
- `Evidence depth: full text reviewed` is admissible only with `coverage_status: complete_fulltext_read`.
- If the text is large, read in sequential chunks and declare `FULL TEXT LARGE — COMPLETE READING IN PROGRESS` until coverage is complete.
- For WWOX-direct, `CANONICAL_CANDIDATE`, `P0_FAST_TRACK`/`P1_HIGH`, safety-relevant, therapy/GT/ASO-relevant, model-shifting papers, or ones the operator explicitly calls important, the full reading must be completed before the final analysis.
- Before reading, check prior receipts by PMID/DOI. Every completed or partial analysis returns a `FULLTEXT_READ_RECEIPT` conforming to `framework/protocols/fulltext_read_receipt.md`; the caller must persist it. A second complete read is forbidden without `reread_reason`.

## Canonical files to pass/read
- State: `framework/state/state_manifest_current.md`
- The 4 canonical scientific current files (working model, claim registry, paper registry, literature tracking log).
- Operational: the inbox and the commit-candidate queue.
- Protocols: `framework/protocols/ingest_protocol.md`, `framework/protocols/wikilink_schema.md`
- The research-group knowledge base.

## Multi-hop expansion
Follow related/cited papers while WWOX-relevant (even several hops); stop when relevance drops. Each expanded paper re-runs the whole pipeline.

## Output
COMMIT CANDIDATEs queued in the commit-candidate log (append-only), plus one `FULLTEXT_READ_RECEIPT` per paper actually analysed. If candidates ≥5 → suggest `legend-commit`.
