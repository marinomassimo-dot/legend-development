---
artifact: CLAUDE.md MIGRATION MAP
governance_version: 3.1.1
status: PROPOSED — part of INTEGRATION_CANDIDATE v3.1.1, subject to Mirror hostile review
normative: no — this is the evidence of a migration; the destinations are normative
authored_by: plan
authored_on: 2026-08-16
---

# CLAUDE.md MIGRATION MAP

Governance v3.1.1 requires the root `CLAUDE.md` to be a minimal router (§0.3). It was not one: it
carried the load-bearing scientific and operational law. This map is the evidence that the
transformation lost nothing.

**Method.** Three independent read-only inventories mapped every rule in the old file against
`framework/`, `ARCHITECTURE.md`, the protocols, the manuals and the disease-model layer, quoting
rather than paraphrasing when claiming that content already existed elsewhere. Similar
terminology was not accepted as equivalence. Where the inventory found a rule only in
`CLAUDE.md`, it was **moved in full**; where it found it stated more strongly elsewhere, the
destination was left as the canonical home; where doubt remained, the rule was `PRESERVED`.

**Ordering deviation.** The base alignment (instruction step 4) was executed **before** this
migration (step 2). `main` commit `f2b9067` had added an *Observable-stop gate for long readings*
that the pre-rebase base did not contain, so inventorying the stale file would have silently
dropped a live operating rule. Recorded in MAT-006.

`STATUS` legend: `PRESERVED` — moved and now canonical elsewhere · `REPLACED_BY_EQUIVALENT` —
already stated at the destination, at equal or greater strength · `UNRESOLVED` — not settled.

---

## A · Parity of sources

| Old section | New canonical location | Status |
|---|---|---|
| Opening principle ("overrides every gate, score, tier and matrix") | `framework/master/gold_is_in_the_details.md` §opening | REPLACED_BY_EQUIVALENT |
| 2026-07-12 worked example — date, `Tier C`, **P252A and not Q230P**, the Q230P→CMA over-transfer | same file, §"The worked example" — date and allele pair **added** | PRESERVED |
| Inverted hierarchy: oncology / adult neurology / WOREE / the noise | same file, §"Why the intuitive hierarchy is inverted" | REPLACED_BY_EQUIVALENT |
| Rules 1–4 (no tier authorizes not reading; ranking orders, never replaces; disease context never downgrades; grep forbidden as method) | same file, §"Binding operational rules" 1–4 | REPLACED_BY_EQUIVALENT |
| Rule 5 — coverage map **+ the `coverage_status: complete_fulltext_read` gate** | same file, rule 5 — second half **added** | PRESERVED |
| Rule 5b — verbatim locators, the 2026-08-04 export, waiving with an argument | same file §5b; operational form in `framework/protocols/fulltext_read_receipt.md` | PRESERVED |
| Rule 5c — deterministic extraction, **ML converters are reading aids and never the declared artifact**, `extraction_method` declaration, figures at original resolution | same file §5c | PRESERVED |
| Rule 5d — rendered page as reference surface, `PMID 33914858`, 33/51, SUSPECT refused not normalised, **queue must record the different class** | same file §5d; screening in `deepdive_manifest.py` | PRESERVED |
| Rule 5e — adjudication as recipe, **standing policy for 33 of 51**, and the copyright paragraph: the privacy gate does not cover copyright, read the diff yourself before a public push | same file §5e | PRESERVED |
| Rule 6 — reading debt | `gold_is_in_the_details.md` rule 6 | REPLACED_BY_EQUIVALENT |
| Rule 7 — universal full-text trace | `gold_is_in_the_details.md` rule 7 **added**; contract in `framework/protocols/fulltext_read_receipt.md`; hard rule in `LEGEND_CORE.md` §5.1 | PRESERVED |
| Rule 8 — abstract corpus is not evidence, incl. the cross-link to rule 4 | `gold_is_in_the_details.md` rule 8 **added**; near-verbatim in `AGENTS.md`; enforced by `scripts/test_abstract_corpus_is_not_evidence.py` | PRESERVED |

## B · The system is alive and always growing

The whole section was absent from `LEGEND_CORE.md`, `epistemic_discipline.md`,
`gold_is_in_the_details.md` and every protocol. It now has a canonical home as a companion master
principle: **`framework/master/designed_for_growth.md`**.

| Old rule | New canonical location | Status |
|---|---|---|
| "LEGEND is never finished… correction is the product" | `designed_for_growth.md` §opening | PRESERVED |
| Calibration figures + "hundreds of thousands of full texts" + starting point never a design target | same file; machine counterpart `framework/state/growth_anchors.jsonl` named as authoritative | PRESERVED |
| "Will this still be informative at the thousandth batch?" | same file | PRESERVED |
| 1 — never pin a number a human must update; updating must cost as much as complying | same file, consequence 1; enforced in `growth_anchors.py` | PRESERVED |
| 2 — a freeze over living state reports drift | same file, consequence 2; `FREEZE_SCOPE_GATE` in `framework/eval/learned_gates_registry.md` | PRESERVED |
| 3 — external-database facts derived and cached, never hand-declared | same file, consequence 3 — **had no second home anywhere** | PRESERVED |
| 4 — state scale assumptions out loud; write the size down | same file, consequence 4 | PRESERVED |
| 5 — before building a guard, look for it; uneven application | same file, consequence 5; `PATTERN_ALREADY_SOLVED_GATE` carries the fuller incident list | PRESERVED |
| "Why this section exists" — append_only_prefix applied unevenly, twice | same file §"Why this principle exists" | PRESERVED |
| `mission.md` delegated the consequences to CLAUDE.md by anchor | link repointed to `designed_for_growth.md` | PRESERVED |

## C · Epistemic discipline

| Old rule | New canonical location | Status |
|---|---|---|
| Four levels DATO / INFERENZA / IPOTESI / ESPANSIONE + "never inferences as data" | `framework/instruction/epistemic_discipline.md` §1–2 (superset: adds L1/L2/L3 mapping) | REPLACED_BY_EQUIVALENT |
| Premises and negatives; the false-negative asymmetry; the `P → C` error shape | same file §3–4; table form in `dismissal_ledger_current.md` | REPLACED_BY_EQUIVALENT |
| "The most dangerous premises are too obvious to write down" + polyUb→proteasome | same file | REPLACED_BY_EQUIVALENT |
| `PREMISE_TAG`, incl. `DEFAULT_FROM_TEXTBOOK` as a research target | same file; per-session enforcement in `framework/protocols/session_self_evaluation.md` | REPLACED_BY_EQUIVALENT |
| `REVIVAL_TRIGGER` — **bound to `dismissal_ledger_current.md` by name** | same file §5 **added** (the destination path existed only in CLAUDE.md) | PRESERVED |
| Re-audit rule on every new mechanistic DATO | same file; `dismissal_ledger_current.md` | REPLACED_BY_EQUIVALENT |
| `DEFAULTS THAT BIT US` | same file (6 rows) and `dismissal_ledger_current.md` (16 rows, canonical) | REPLACED_BY_EQUIVALENT |
| "Until 2026-07-12 there was no discipline for premises or rejections" | same file §5 **added** | PRESERVED |

## D · Operational and commit rules

| Old section | New canonical location | Status |
|---|---|---|
| Workflow & modes (8 of 10) | `ARCHITECTURE.md` §Workflow & modes | REPLACED_BY_EQUIVALENT |
| `MODE: Q&A` — non-canonical, READ-ONLY, "not a claim", disclaimer | `ARCHITECTURE.md` **added** (absent everywhere) | PRESERVED |
| `DISEASE_PRIORITY_MATRIX` literal + the `MODE:` prefixes | `ARCHITECTURE.md` **added** | PRESERVED |
| One actor / one worktree / one branch — three 2026-08-09/10 failures, rules 1–5, rule 6 evidence locality, the `staging/` closing paragraph | `framework/protocols/parallel_legend_protocol.md` §"One actor, one worktree" **added**; rule 6's operational half remains in `fulltext_read_receipt.md` | PRESERVED |
| Operational gates — semantics of READY vs the three gate fields | `LEGEND_CORE.md` §21b **added**; the fields themselves live in the state manifest; BLOCK levels in `prompt_lint_integrity_check.md` | PRESERVED |
| BATCH_COMMIT triple trigger | `LEGEND_CORE.md` §BATCH triggers | REPLACED_BY_EQUIVALENT |
| URGENT_COMMIT_REQUEST, five categories, operator-authorized only | `LEGEND_CORE.md`; procedure in `prompt_batch_commit.md` | REPLACED_BY_EQUIVALENT |
| Working-model versioning | `prompt_batch_commit.md` §Format (superset) + `LEGEND_CORE.md` | REPLACED_BY_EQUIVALENT |
| Session types Minimal / Standard / Full | `framework/manuals/operator_manual.md` §1.1–1.3 (Italian) | REPLACED_BY_EQUIVALENT |
| Session types — autopilot-era additions (state manifest first; scout + takeaways; autopilot by default; Full's trigger list) | `operator_manual.md` §"Session types — autopilot-era additions" **added** | PRESERVED |
| Claim states — the six exact strings | `LEGEND_CORE.md` + `prompt_lint_integrity_check.md`, both literal | REPLACED_BY_EQUIVALENT |
| LINT severity scale + biomarker discipline | `LEGEND_CORE.md` + `prompt_lint_integrity_check.md` §3.10 | REPLACED_BY_EQUIVALENT |
| Commit block conditions; 8-phase procedure; all-or-nothing | `prompt_batch_commit.md`; `LEGEND_CORE.md` R0–R8 | REPLACED_BY_EQUIVALENT |
| `FULL STATE NOT AVAILABLE — COMMIT BLOCKED` (literal) | `LEGEND_CORE.md` §21b **added** — the string existed nowhere else | PRESERVED |
| `FILES TO CREATE` / `FILES TO UPDATE` / `FILES UNCHANGED`, "rewritten in full", "Removed must be empty" | `LEGEND_CORE.md` §21b **added** | PRESERVED |
| `PARTIAL FILE — NOT SAFE FOR REPLACEMENT` (literal) | `LEGEND_CORE.md` §21b **added**; the protocol's own token `FILE NOT GENERATED — RISK OF INCOMPLETE OUTPUT` remains in `file_generation_rule.md` | PRESERVED |
| `_current` suffix rule; append-only files never lose entries | `LEGEND_CORE.md` §21b **added**; echoed in `AGENTS.md` | PRESERVED |
| Minimal change and verification contract, incl. INCONCLUSIVE / CRASH and the scope caveat | `LEGEND_CORE.md` §21b **added** | PRESERVED |
| Observable-stop gate for long readings *(arrived from main in `f2b9067`)* | `LEGEND_CORE.md` §21b **added** | PRESERVED |
| No rebuild · Lossless · Loss aversion · Supplementary commit · Wikilink discipline · File protocol | `LEGEND_CORE.md` R0–R8, `ARCHITECTURE.md` §Core invariants, `file_generation_rule.md`, `wikilink_schema.md` | REPLACED_BY_EQUIVALENT |
| Recovery priority order (the seven-step chain) | `LEGEND_CORE.md` §21b **added** — the chain existed nowhere else | PRESERVED |
| Layer architecture table | `ARCHITECTURE.md` §Three layers | REPLACED_BY_EQUIVALENT |
| Skill bootstrap triggers | retained in the router — a trigger table *is* routing | PRESERVED (in router) |
| Runnable checks | retained in the router | PRESERVED (in router) |

## E · Inbound pointers

| Pointer | Action | Status |
|---|---|---|
| `mission.md` → CLAUDE.md growth anchor | repointed to `designed_for_growth.md` | PRESERVED |
| `AGENTS.md` — "the single/complete normative source is CLAUDE.md" | rewritten: CLAUDE.md routes, the named files legislate; sync rule updated | PRESERVED |
| Skills citing "parity of sources in `CLAUDE.md`" (`legend`, `legend-batch-inferential-sweep` + rubric, `legend-proband-priority-matrix`) | left as-is: the router names `gold_is_in_the_details.md`, so the reference resolves in two hops | PRESERVED |
| `legend-locator-audit` → "premise/negative discipline in CLAUDE.md" | same, resolves via router to `epistemic_discipline.md` | PRESERVED |
| `legend-start` → "CLAUDE.md §LINT Severity", "§Recovery" | **section anchors no longer exist**; both now live in `LEGEND_CORE.md` §21b and §LINT | UNRESOLVED |
| `ARCHITECTURE.md:48`, `README.md:319` — describe CLAUDE.md as the normative bootstrap | descriptions now inaccurate | UNRESOLVED |
| Dated orchestration reviews citing CLAUDE.md rules | left untouched: they are historical records of what was true when written | PRESERVED |

## F · UNRESOLVED

1. **Two skill anchors and two descriptive lines still call `CLAUDE.md` normative.** Fixing them is
   mechanical, but they sit in `.claude/skills/` and in reader-facing docs, and the instruction
   froze the perimeter at what the candidate needs. Listed here rather than edited silently.
2. **Rule 5c's `extraction_method` declaration has no schema field.** The obligation is now stated
   canonically in `gold_is_in_the_details.md`, and no manifest key carries it, so it is stated but
   unenforced — precisely the condition consequence 1 of `designed_for_growth.md` warns about.
3. **`framework/master/` now holds two masters.** `gold_is_in_the_details.md` grew from 31 to ~50
   lines and `designed_for_growth.md` is new. Whether the master layer should hold two peer
   principles or one file with two parts is a structural judgement Mirror should make, not Plan
   acting alone.
4. **The operator's home path appears in 11 tracked files**, one of which is
   `governance/design_records/materialization_log.md` (MAT-001, a measurement). Pre-existing
   practice, not introduced here, and the publication gate passes; flagged once because the
   repository otherwise commits under a project identity.
