# CLAUDE.md — LEGEND router

**This file routes. It does not legislate.** Every operating rule lives in a named normative file
and is reproduced nowhere else; if this file and a normative file ever disagree, the normative
file wins. It became a router on 2026-08-16, when the operating law it had accumulated was moved
to canonical homes — the map of that migration is in
[`governance/design_records/claude_md_migration_map.md`](governance/design_records/claude_md_migration_map.md).

---

## 0 · Before anything else

```
Your ACTOR_ID is assigned by the operator — never inferred from your directory (AGENTS.md § 4).
No lease gates your work: root and `main` are writable by every actor (LEGEND_CORE §21e).
Work on a task branch in your worktree; land it on `main` yourself at task end; delete it.
First run with no laboratory at all (no roles registered, no worktrees): read /BOOTSTRAP.md.
```

Read [`framework/state/state_manifest_current.md`](framework/state/state_manifest_current.md)
**first, every session**, and confirm `current_state: READY`.

Then open, by name and before your first act,
[§21c STOP POLICY](framework/instruction/LEGEND_CORE.md#21c-stop-policy),
[§21d DECISION AUTHORITY](framework/instruction/LEGEND_CORE.md#21d-decision-authority) and
[§21e AGILE OPERATING MODE](framework/instruction/LEGEND_CORE.md#21e-agile-operating-mode).
They govern when you may **not** stop, what you may decide without the operator, and how work
moves from a worktree to `main` in hours — so an actor who has not loaded them falls back to
asking or to waiting, which are the failures they exist to remove. This router names the
sections rather than the file alone because naming the file was not enough: on 2026-09-04 a
session read this router end to end and reached neither §21c nor §21d, and it was the
operator who noticed.

Three facts bind before you have finished reading anything else:

- **Nothing here is medical advice.** Therapeutic output supports discussion with a treating
  clinical team; it never substitutes for one.
- **The four scientific current files change only through `BATCH_COMMIT`**, and are never
  reconstructed from chat memory.
- **This is the public edition and contains no individual-level record.** Where the private
  edition reasons about one person, this one reasons about the reference genotype — a WWOX-DEE
  genotype class. Do not reintroduce individual linkage.

---

## 1 · Where the law is

| You need | Read |
|---|---|
| How LEGEND thinks; gates, blocking strings, commit rules, recovery order | [`framework/instruction/LEGEND_CORE.md`](framework/instruction/LEGEND_CORE.md) |
| Claim classification, premises and negatives, revival triggers | [`framework/instruction/epistemic_discipline.md`](framework/instruction/epistemic_discipline.md) |
| Parity of sources; what counts as having read something (rules 1–8, 5b–5e) | [`framework/master/gold_is_in_the_details.md`](framework/master/gold_is_in_the_details.md) |
| Designing for a system that never stops growing | [`framework/master/designed_for_growth.md`](framework/master/designed_for_growth.md) |
| `FULLTEXT_READ_RECEIPT` on every full-text route; `verbatim_locators` and persistence | [`framework/protocols/fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md) |
| `pubmed_corpus_harvest` produces a census, not evidence; an abstract is not a read | [`framework/master/gold_is_in_the_details.md`](framework/master/gold_is_in_the_details.md) and [`framework/scripts/pubmed_corpus_harvest.py`](framework/scripts/pubmed_corpus_harvest.py) |
| The state-control exception and append-only carve-out | [`framework/state/state_manifest_current.md`](framework/state/state_manifest_current.md) |
| Self-diagnosis before growth and takeaways | [`framework/protocols/session_self_evaluation.md`](framework/protocols/session_self_evaluation.md) |
| Batch commit, LINT, ingest, parallelism and worktree isolation, wikilinks, file generation, read receipts | [`framework/protocols/`](framework/protocols/) → [`index.md`](framework/protocols/index.md) |
| Layers, modes, core invariants | [`ARCHITECTURE.md`](ARCHITECTURE.md) |
| How to actually run a session; session types | [`framework/manuals/operator_manual.md`](framework/manuals/operator_manual.md) |
| What the system can do, with maturity status | [`SKILLS.md`](SKILLS.md) · [`CAPABILITIES.md`](CAPABILITIES.md) · [`FAQ.md`](FAQ.md) |
| The disease-level model | [`disease-models/wwox/registries/working_model_current.md`](disease-models/wwox/registries/working_model_current.md) |

### The multi-agent laboratory

| You need | Read |
|---|---|
| First run, chats to open, qualification, lease | [`BOOTSTRAP.md`](BOOTSTRAP.md) |
| The constitution: body + annexes A–J | [`governance/`](governance/) → [`ANNEX_INDEX.md`](governance/ANNEX_INDEX.md) |
| Your own role contract | [`roles/`](roles/) |
| What the system does **not** guarantee | [`governance/annex_j_runtime_control_plane.md`](governance/annex_j_runtime_control_plane.md) § J.0 |
| Why the governance is shaped this way (non-normative) | [`governance/design_records/`](governance/design_records/) |
| Active lessons for your role, once operative | `active_lessons/` — **not yet materialized** |

---

## 2 · Skill bootstraps — apply without being asked

| Trigger | Invoke |
|---|---|
| A new reader asks what this is, how to start, or why it matters | Answer from [`FAQ.md`](FAQ.md); never improvise a capability [`SKILLS.md`](SKILLS.md) does not claim |
| Session start | [`legend-start`](.claude/skills/legend-start/SKILL.md) |
| Session start for `plan` / `junior-harness`; weekly scout due or report awaiting triage | [`legend-harness-scout`](.claude/skills/legend-harness-scout/SKILL.md), dispatched by `framework/scripts/harness_session_start.py` |
| A list of studies / PMIDs / DOIs arrives with "start / process / analyze" | [`legend`](.claude/skills/legend/SKILL.md) — the autopilot |
| Any study list, before ingest or deep dive | [`legend-study-intake-triage`](.claude/skills/legend-study-intake-triage/SKILL.md) |
| After intake, over the whole batch | [`legend-batch-inferential-sweep`](.claude/skills/legend-batch-inferential-sweep/SKILL.md) |
| Whenever the sweep runs | [`legend-proband-priority-matrix`](.claude/skills/legend-proband-priority-matrix/SKILL.md) |
| Every analytical batch or completed full-text read, **before** takeaways | [`legend-session-self-eval`](.claude/skills/legend-session-self-eval/SKILL.md) — the upgrade is the answer, not the promise of one |
| Every session, before closing | [`legend-capability-scout`](.claude/skills/legend-capability-scout/SKILL.md) |
| Every session, final response | [`legend-session-takeaways`](.claude/skills/legend-session-takeaways/SKILL.md) |

---

## 3 · Runnable checks

```bash
python3 framework/scripts/legend_lint.py .              # structural LINT over the canonical state
python3 framework/scripts/fulltext_receipts.py verify   # ledger chain + state-manifest tail anchor
python3 framework/scripts/growth_anchors.py check       # registry cardinality + both debt ratchets
python3 framework/scripts/unread_gold.py --help         # the unread-gold sweep
python3 scripts/public_release_gate.py                  # the publication gate
python3 scripts/run_release_regressions.py              # every release suite at once
python3 governance/scripts/governance_fingerprint.py compose --all   # per-role governance fingerprint
```

Persist receipts with `fulltext_receipts.py record`. Hand-editing the ledger breaks its hash chain
and halts LEGEND until the edit is undone or authorized and re-anchored.

---

## 4 · Read order for a first-time reader

[`README.md`](README.md) → [`FAQ.md`](FAQ.md) → [`CAPABILITIES.md`](CAPABILITIES.md) →
[`ARCHITECTURE.md`](ARCHITECTURE.md) → [`framework/instruction/LEGEND_CORE.md`](framework/instruction/LEGEND_CORE.md) →
[`framework/instruction/epistemic_discipline.md`](framework/instruction/epistemic_discipline.md) →
[`framework/master/gold_is_in_the_details.md`](framework/master/gold_is_in_the_details.md) →
[`framework/manuals/operator_manual.md`](framework/manuals/operator_manual.md) →
[`disease-models/wwox/registries/working_model_current.md`](disease-models/wwox/registries/working_model_current.md)

> **Public edition.** Three layers: `framework/` is the generic engine, `disease-models/wwox/` is
> the de-identified disease model from public literature, and the private N-of-1 overlay is
> excluded by design and is not part of this repository. That layering *is* the privacy design.
