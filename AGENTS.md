# AGENTS.md — agent entrypoint (thin pointer)

This file is only the **entry point** for Codex and compatible agentic tooling.
**The single normative source is [`CLAUDE.md`](CLAUDE.md)** (plus [`framework/instruction/LEGEND_CORE.md`](framework/instruction/LEGEND_CORE.md)).
No content is duplicated here: read `CLAUDE.md` and operate from it. That is deliberate — two parallel normative files drift.

## Read order (mandatory, in this order)

1. [`framework/state/state_manifest_current.md`](framework/state/state_manifest_current.md) — the live state, **always first**; confirm `current_state: READY`.
2. [`CLAUDE.md`](CLAUDE.md) — **the complete normative source**: layer architecture, modes, operational gates, writing rules, epistemic discipline, skill bootstraps.
3. The bootstrap skills named in `CLAUDE.md`: [`legend-capability-scout`](.claude/skills/legend-capability-scout/SKILL.md), [`legend-session-takeaways`](.claude/skills/legend-session-takeaways/SKILL.md), and [`legend`](.claude/skills/legend/SKILL.md) as the autopilot when a study list is supplied.
4. The 4 canonical current files in [`disease-models/wwox/registries/`](disease-models/wwox/registries/) (plus [`meta_index_current.md`](disease-models/wwox/meta/meta_index_current.md) for Standard sessions).

## Inviolable facts (valid before you have finished reading `CLAUDE.md`)

- The **4 scientific current files** change **only** via `BATCH_COMMIT`. Never reconstruct them from chat memory.
- LINT gate: `python3 framework/scripts/legend_lint.py .` → exit `0` ok · exit `2` = only `BATCH_COMMIT` blocked (read-only deep dive / ingest may continue) · exit `3` = `BLOCK_SYSTEM`, recovery mandatory.
- Publication gate: `python3 scripts/public_release_gate.py` must return `PASS` before anything leaves this repository. `python3 scripts/run_release_regressions.py` runs every release suite.
- In a deep dive the full text must be read **in full**; `grep`/keyword is **forbidden** as a method of analysing a study (allowed only for file-finding, dedup, post-reading audit).
- Every full-text analysis, regardless of route, must emit and persist a `FULLTEXT_READ_RECEIPT`; retrieval, indexing or RAG queries never count as a complete read. Check existing receipts before rereading.
- Append-only files never lose entries — only status changes.
- **Nothing is medical advice**: every clinical-strategic output exists to support discussion with a treating clinical team.
- The public edition contains **no individual-level record**. Where the private edition reasons about one person, this edition reasons about **the reference genotype**, a disease-level genotype class. Do not reintroduce individual linkage, family-relationship data, institutions, dates or record identifiers.

## Sync rule

If this file and `CLAUDE.md` diverge, **`CLAUDE.md` + the state manifest win**. This file is deliberately minimal: update it **only** if the read order or the inviolable facts above change — **never** re-duplicate `CLAUDE.md`.
