# Architecture

LEGEND is a cumulative, lossless knowledge system. The operator loads files into context, LEGEND processes them, and produces updated files as output. It works on **real files**, never on chat memory.

## Three layers

The public edition is organized into three layers. The layering is itself the privacy design: everything that could link to a single individual is kept in a **private N-of-1 overlay that is not part of this repository**.

| Layer | Path | Purpose |
|---|---|---|
| **1 — Framework** *(generic, patient-free)* | `framework/` | The reusable engine, with no disease specifics. |
| **2 — Disease model** *(WWOX, public literature only)* | `disease-models/wwox/` | The de-identified, disease-level WWOX model. |
| **— Overlay** *(excluded)* | *(private, not in repo)* | The individual N-of-1 content: the personal clinical record, a genotype tied to a persistent individual, family-relationship data, treatment schedule, donor cell provenance, and the live operational logs (inbox, commit queue, capability-scout log). |

### `framework/` — the engine

| Path | Purpose |
|---|---|
| `framework/instruction/LEGEND_CORE.md` | How LEGEND thinks: the operating core. |
| `framework/instruction/epistemic_discipline.md` | The four levels + the discipline for premises and negatives. |
| `framework/protocols/` | Executable procedures: ingest, batch-commit, LINT integrity, wikilink schema, file-generation rule, parallel protocol, navigation index. |
| `framework/eval/` | The failure-aware evaluation framework + failure taxonomy. |
| `framework/master/gold_is_in_the_details.md` | The "gold is in the details / parity of sources" superordinate principle. |
| `framework/state/state_manifest_current.md` | Disease-agnostic state fixture (single source of truth for system state). |
| `framework/manuals/` | The operating manuals: `operator_manual.md` (session types, modes, commit gates) and `deep_dive_manual.md` (how a paper becomes a claim — coverage discipline, epistemic tagging, transfer assessment). De-identified and generic; preserved in their original language. |

### `disease-models/wwox/` — the WWOX disease model (public literature)

| Path | Purpose |
|---|---|
| `disease_model.md` | Disease-level mechanistic synthesis + genotype-interpretation rules + decision framework. |
| `mission.md` | The mission / north-star and epistemic reset (disease-level). |
| `meta/` | Structured syntheses per biological axis (network/myelin/glia, metabolism, prenatal structure, human spectrum, GABA paradox), from public literature. |
| `research/` | Future-work research lines and candidates, full-text queue, the **dismissal ledger** (negatives are claims), the **discovery ledger** and the **therapeutic-hypotheses ledger** — the two compounding-memory files. |
| `biomarker_endpoint/` | Tier 1/2 gene-linked biomarker candidates vs Tier 3 distal clinical endpoints — kept strictly separate. |
| `therapeutics/` | Scored portfolio of candidate therapeutic strategies (read-only toward the model; promotion via pipeline). |
| `analysis/` | The in-silico variant-triage pipeline + data + the adversarial red-team of a worked variant example + the **proteostasis rationale** behind the chaperone lever (published with its later repair). Also the **DisMech export pipeline** — claims to Monarch-compatible disorder-mechanism entries, built to refuse rather than to produce plausible YAML; dry run only, nothing submitted ([status](disease-models/wwox/analysis/README.md#the-dismech-export-pipeline)). |
| `registries/` | De-identified disease-level registries — the four canonical "current" files the LINT engine requires: `working_model_current` (the canonical model + claim mirror + version changelog), `claim_registry_current` (canonical claims), `paper_registry_current` (integrated papers), `literature_tracking_log_current` (paper lifecycle). |

> **Registries — de-identified.** The registries carry public-literature bibliographic state with all individual-linking data removed: the persistent-individual relevance axis is neutralized (to "clinical relevance" and "directness to the reference genotype"), family-relationship data is decoupled, cell-line ownership is removed, and no dates or record identifiers remain. Specific variants appear only as decoupled disease-model worked examples. Some entries remain in their original language pending translation.

> **Compounding memory — the two ledgers.** `research/discovery_ledger_current.md` (the cumulative discovery capital: leads toward biomarkers, molecules and repurposing, never deleted, only re-statused) and `research/therapeutic_hypotheses_ledger_current.md` (the scored hypothesis portfolio from the co-scientist loop) are what make LEGEND a compounding engine rather than a bibliography. Both are de-identified to disease level: they reason about **the reference genotype** — a WWOX-DEE genotype class — not about a person, and links to private operational logs are rendered as plain text rather than broken links.

### Root — the bootstrap

| File | Purpose |
|---|---|
| `CLAUDE.md` | The normative operating bootstrap: modes, operational gates, batch-commit triggers, URGENT exception, working-model versioning, claim states, LINT severities, commit rules, recovery. |
| `AGENTS.md` | Thin entrypoint for Codex and other agentic tooling: read order + inviolable facts, then it delegates to `CLAUDE.md`. Deliberately duplicates nothing. |
| `.claude/agents/` | The 5 reusable subagent prompts the skills dispatch to (full-text dossier, deep dive, research-group analyst, intake triage, literature scout). |
| `.claude/settings.json.example` | Allow-list template for running the autopilot without a prompt on every step. Read its security note: it does **not** enable `bypassPermissions`, which belongs in an isolated container or VM. |

### `.claude/skills/` — the operational skills

> Full catalogue with maturity status, inputs, outputs and shipped code: **[`SKILLS.md`](SKILLS.md)**.

The operational capability set, genericized:

| Skill | Role |
|---|---|
| `legend` | Autopilot orchestrator |
| `legend-start` | Session boot + structural LINT |
| `legend-study-intake-triage` | Bibliographic dedup/disambiguation |
| `legend-batch-inferential-sweep` | Second-pass inferential scoring of a batch |
| `legend-proband-priority-matrix` | Case-specific priority scoring (configurable axes) |
| `legend-ingest` | Inbox-quarantine classification |
| `find-fulltext` | Tiered full-text/PDF retrieval cascade |
| `legend-deepdive` | Canonical-claim deep dive → commit candidate |
| `legend-discovery` | Discovery-oriented deep dive (biomarkers / molecules / repurposing) |
| `legend-hypothesis-forge` | Therapeutic-hypothesis generator (co-scientist loop) |
| `legend-aso-designer` | ASO / splice-correction hypothesis triage |
| `legend-safety-triage` | ADMET / druggability / CNS BBB triage for candidate molecules |
| `legend-paperqa` | Cited RAG over a local full-text corpus |
| `legend-session-self-eval` | Post-batch self-diagnosis: executable gate, then the written judgement, then the micro-upgrade |
| `legend-locator-audit` | Blind adversarial audit of a reading's quotes before it may touch a baseline claim |
| `legend-research-loop` | Controlled micro-experiments (baseline → one variable → KEEP/DISCARD) |
| `legend-capability-scout` | Post-session capability-growth radar |
| `legend-session-takeaways` | Compact end-of-session synthesis |
| `legend-commit` | Executes a batch commit end-to-end with LINT gate + snapshot/restore |
| `legend-lint-repair-plan` | Turns LINT output into a safe repair plan |
| `legend-dashboard` | Obsidian-friendly dashboard/status views |

## Workflow & modes

- `LEGEND_AUTOPILOT` — orchestrates the full chain when given a study list: intake → sweep + priority matrix → ingest → full-text → deep-dive/discovery → therapeutic fan-out → safety → commit gate → capability growth → takeaways.
- `DEEP_DIVE` — analyze a source; output is a **commit candidate** (queued, never touches current files).
- `INGEST` — bring a source through the inbox quarantine.
- `STUDY_INTAKE_TRIAGE` / `BATCH_INFERENTIAL_SWEEP` / `PRIORITY_MATRIX` — dedup, score, and rank a study list before deep work.
- `LINT` — integrity/consistency check over the `.md` files (fast every session; deep on demand).
- `BATCH_COMMIT` — the **only** moment current files change. 8-phase, all-or-nothing, with snapshot/restore.
- `PARALLEL_BRANCH` / `PARALLEL_MERGE` — parallel deep dives on disjoint scopes; merge before commit. *Parallel deep dive yes, parallel commit no.*
- `Q&A` — consultation layer, **non-canonical and READ-ONLY** toward the four current files. A Q&A answer is not a claim and changes nothing; if a promotable datum emerges it goes through the pipeline. Always carries the "not medical advice / discuss with the treating clinical team" disclaimer.

Modes are **declared explicitly** when a session enters them, written with the `MODE:` prefix —
`MODE: LEGEND_AUTOPILOT`, `MODE: DEEP_DIVE`, `MODE: INGEST`, `MODE: STUDY_INTAKE_TRIAGE`,
`MODE: BATCH_INFERENTIAL_SWEEP`, `MODE: DISEASE_PRIORITY_MATRIX`, `MODE: LINT_AUTOMATIC` /
`MODE: LINT_DEEP`, `MODE: BATCH_COMMIT`, `MODE: PARALLEL_BRANCH` / `MODE: PARALLEL_MERGE`,
`MODE: Q&A`. The priority-matrix mode is `DISEASE_PRIORITY_MATRIX`: it scores against the
disease model's own axes, so the disease is part of the mode, not a parameter of it.

## Core invariants

- **Lossless**: no information lost, partially reconstructed, or destructively compressed.
- **No rebuild**: never regenerate canonical files from chat memory.
- **Epistemic discipline**: every claim tagged `DATO` / `INFERENZA` / `IPOTESI` / `ESPANSIONE`; premises and rejections tagged too.
- **Provenance gates publication**: `PUBLIC` / `PRIVATE` / `MIXED`; a derivative inherits the most restrictive status.
- **Gold is in the details**: no tier/score authorizes not reading a source.
- **Privacy by layering**: individual-linking content stays in the private overlay, never in the public layers.
