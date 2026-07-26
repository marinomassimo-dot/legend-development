# CAPABILITIES — What LEGEND Actually Is

> **LEGEND is not a bibliography.** It is an attempt to develop **evolutionary, self-improving patterns with an automatic compounding effect** — a new way to grow *knowledge and capability together, in lockstep*.
>
> Every batch does not merely add data — it **increases the system's power to discover**. Every session leaves at least one **micro-upgrade of capability**. Every real error becomes a **reusable gate** that prevents its whole class. The machine that manages the knowledge grows *with* the knowledge — through surgical, targeted improvements, never rewrites.

This document is a census of the distinctive patterns that make that claim concrete. It exists so that a reader can see, explicitly, that the value here is **method and self-improving capability**, not a literature dump.

---

## The compounding flywheel

```
read a full text line-by-line  →  extract mechanism + tag epistemics
        │                                      │
        ▼                                      ▼
 a lead is found (or a lead is discarded — with a REVIVAL_TRIGGER)
        │                                      │
        ▼                                      ▼
 a NEW mechanistic datum arrives  →  re-audit: re-scan every past rejection
        │                                      │
        ▼                                      ▼
 an error is made  →  it becomes a named GATE that prevents its class forever
        │                                      │
        ▼                                      ▼
 end of session  →  capability-scout leaves ≥1 proportional capability micro-upgrade
        │
        ▼
 next batch starts MORE capable than the last  ── compounding ──┐
        ▲                                                        │
        └────────────────────────────────────────────────────────┘
```

The key inversion: most systems **accumulate knowledge**. LEGEND accumulates knowledge **and** the capability to handle it — so the two never fall out of step.

---

## The distinctive patterns

### A — Epistemic discipline (the honesty machine)
1. Four-level classification of every claim: `DATO` (data) / `INFERENZA` (inference) / `IPOTESI` (hypothesis) / `ESPANSIONE` (extension).
2. The discipline extends to **premises** (`PREMISE_TAG`, including `DEFAULT_FROM_TEXTBOOK` = a research target, not a foundation) and to **negatives** (rejections).
3. The **false-negative doctrine**: a false positive is tested and dies; a false negative is silent, permanent, and compounding.
4. The **"defaults that bit us"** table — textbook defaults that proved false in this domain.

### B — Never lose a lead (anti-false-negative loop)
5. `dismissal_ledger` — nothing dies in silence; every rejection is recorded.
6. `REVIVAL_TRIGGER` — every rejection declares what evidence would reopen it.
7. **Re-audit loop** — every new mechanistic `DATO` re-scans the dismissal ledger. *This is what makes it self-improving, not merely self-correcting.*
8. `PUBLICATION_BOUNDARY` / provenance-taint — `source_scope: PUBLIC/PRIVATE/MIXED`; a derivative inherits the most restrictive status.

### C — Reusable failure-mode gates (learned from real errors)
9. A growing library of named gates, each born from a real, documented error:
`DEGRADATION_DIRECTION_GATE` · `REPORTER_IDENTITY_GATE` · `MECHANISM_DIRECTNESS_GATE` · `TARGET_ATTRIBUTION_GATE` · `PROTEIN_STATE_IDENTITY_GATE` · `KG_EDGE_HAS_NO_SIGN` · `EXTERNAL_DOSSIER_CANONICAL_DRIFT_GATE` · `NMD_LAST_EXON` · `MECHANISTIC_OVERTRANSFER` · `DISMECH_DELTA_GATE` · `PRE_EXTERNAL_CLAIM_VERIFICATION_GATE` · `ALLELIC_ARCHITECTURE_RESOLUTION_GATE` · `READING_DEBT_PARTITION_GATE` · …
Each gate turns a one-time mistake into a permanent immunity. (This library is the seed of the failure-aware benchmark in `framework/eval/`.)

### D — Gold is in the details / parity of sources
10. No tier, score, or category authorizes *not reading* a source; the decisive detail can live anywhere, especially where the title promises nothing.
11. `grep`/keyword is forbidden as a *method of analysis* (allowed only for file search, dedup, audit).
12. Every new full-text processing route writes a validated, hash-chained `FULLTEXT_READ_RECEIPT` through an anchored, locked writer; LINT and the coverage/queue views consume it fail-closed. Historical prose-only claims remain explicitly legacy/unknown and are grandfathered by exact identity, so they cannot be exchanged for new unsupported declarations. An already-complete paper is reused unless a new `reread_reason` justifies another pass.

### E — The compounding discovery engine
13. `discovery_ledger` — cumulative discovery capital (biomarker / molecule / repurposing / mechanism leads) that grows across sessions.
14. **Discovery Power Principle** — every batch must *increase the system's power to discover* (new bridges, hypotheses, tools, priorities), not just add or sort knowledge.
15. **Auto-research** — the discovery skill autonomously generates and pursues the next searches a lead implies.

### F — Self-improvement / evolutionary capability
16. `capability-scout` — every session must leave at least one proportional **capability** micro-upgrade (a gate, a procedure, a tool, an import), not only knowledge.
17. The **knowledge↑ ⇒ capability↑ lockstep** principle.
18. `research-loop` — controlled micro-experiments (baseline → one variable → `KEEP` / `DISCARD` / `INCONCLUSIVE` / `CRASH`): procedures are *validated*, not adopted on plausibility.

### G — Failure-aware evaluation
19. Controlled cumulative arms (base → +schema → +guardrails), a **temporal T0→T1 test** (does the system reopen the right conclusion when evidence changes?), a run/cost ledger, and no-tuning-on-test. See `framework/eval/`.
20. It measures *where the reasoning fails* — the thing that silently corrupts long-running synthesis.

### H — Lossless cumulative architecture + safety
21. Lossless / no-rebuild / no-masquerade. 22. `DEEP_DIVE → COMMIT CANDIDATE → BATCH_COMMIT` — canonical files change only inside a batch commit, all-or-nothing, with snapshot/restore. 23. **LINT** integrity (four severities; wikilink integrity; biomarker-scope enforcement). 24. State manifest as single source of truth. 25. `URGENT_COMMIT` exception (five categories, operator-authorized only). 26. Parallel deep-dive yes, parallel commit no.

### I — Interoperability + disciplined separations
27. Biomarker (Tier 1/2 functional readout) vs Endpoint (Tier 3 distal clinical) — a **hard** separation, LINT-enforced. 28. Data/inference and literature/claims/strategies/biomarkers kept separate. 29. A **semantic wiki** of path-independent basename wikilinks. 30. Ontology crosswalk (MONDO/HP/GO/MAXO/CL/UBERON/ClinVar) and **DisMech interoperability**.

### J — Therapeutic fan-out (knowledge → action)
31. `hypothesis-forge` — a co-scientist loop (generate → critique → rank → evolve) producing a scored portfolio of candidate levers. 32. `aso-designer`, `safety-triage` (ADMET / BBB / safety gate), `proband-priority-matrix`. 33. The **in-silico variant-triage pipeline** (mechanism → chaperone-vs-ASO lever; see `disease-models/wwox/analysis/`). 34. **Actionability contract** — every finding declares its lever, its next decisive experiment, and what changes if it is true.

### K — Autopilot orchestration
35. An autopilot that runs the full chain: intake → inferential sweep → priority matrix → ingest → full-text → deep-dive / discovery → therapeutic fan-out → safety → commit gate → **capability growth** → takeaways. 36. Conditional skill fan-out + routing to an external computational workshop.

### L — Adversarial rigor (red-team)
37. Falsification matrices, discriminating-experiment design, and provenance data-vs-inference tables (see the red-team package in `disease-models/wwox/analysis/data/redteam/`). 38. Hostile review before anything is declared "external-ready."

---

## Why this matters for rare disease

Rare-disease knowledge is scarce, scattered, and slow to grow. A system that only *accumulates* eventually drowns in what it has collected. A system that grows its *capability* in lockstep — that turns every error into an immunity and every session into a capability gain — can keep pace with, and eventually outrun, the growth of the knowledge itself. That is the bet.

## What the public edition excludes (and why it loses no pattern)
- **Patient clinical record** — excluded; the *disease-level* science it referenced is synthesized in `disease-models/wwox/meta/`, `disease-models/wwox/analysis/`, and the therapeutic files.
- **Operational audit logs** — excluded as process records; the reusable capabilities they document are abstracted here and in `framework/eval/`.
- **Third-party researcher assessments** — excluded (subjective judgements about named people).
- **The external computational workshop** — third-party repositories are not redistributed; a licence-aware manifest stands in their place.

**What is *not* excluded:** the executable runtime **ships**. The framework scripts (`framework/scripts/`), the skill scripts (`.claude/skills/*/scripts/`), the analysis pipeline (`disease-models/wwox/analysis/scripts/`) and the release tooling (`scripts/`) are present and covered by regression suites, de-identified rather than dropped.

### Honest status of this claim

The patterns A–L are all represented publicly. **The edition is not yet certified lossless in every dimension**, and the outstanding items are tracked, by name and status, in [`release/losslessness_manifest.json`](release/losslessness_manifest.json) — the same file the release suites check this page against. The 234-link Obsidian migration is complete and protected by exact-heading regression tests; its completion record is [`release/LINK_MIGRATION_HANDOFF.md`](release/LINK_MIGRATION_HANDOFF.md). Read every `PARTIAL`, `LEGACY_UNREPRODUCIBLE` and `PENDING_CONTENT_REWRITE` entry before treating any capability claim on this page as complete. This edition is public-evidence-only.
