# Startup context audit — 2026-09-09

Actor: `plan` (Harness Engineering), assigned by the operator in this session.
Task: `STARTUP-CONTEXT-AUDIT-20260909`, directive 1, generation 1; ACK/CLAIM accepted.
Governance loaded: 3.1.1; Plan fingerprint at start:
`198d4e0d45dffea592f4323465bfc41bdd49008840b8636c3403ee9a6685fa51`.
Base: `451e12adfc5174fc06364306320ac39068fae3fe`.
Scope: audit recurring context costs; implement the operator-authorized task-specific startup.
Acceptance: preserve scientific obligations and data; route technical work without automatic
scientific-registry preload; reconcile current callers; check regressions; land on `main`.

## Result and measurement limits

The largest avoidable startup payload for a technical session is the **993,131 characters**
in the four scientific registries. The new HARNESS profile removes their unconditional
preload while structural LINT still reads and checks them from disk. Files needed for a
technical inspection remain readable, with complete relevant records and expanding context.
Scientific MINIMAL, STANDARD and FULL retain their reading requirements.

These are **source-text measurements, not observed provider token usage**. No subscription
telemetry, message-by-message usage, cache accounting, compaction frequency, reasoning/output
usage or provider tokenizer was available to this audit. The earlier chat estimate of
250–330k tokens for these registries was a rough characters/3–4 conversion; it is not a
measurement and cannot predict hours gained in a five-hour allowance.

The audit inventories **92 tracked instruction/documentation surfaces, 1,054,169 characters**
at the base commit, separately from those four registries. That total is a searchable
inventory, **not an assertion that every session loads it**. Scope: root entrypoints,
framework instruction/master/manual/protocol/state Markdown, role contracts, skill packages
including references, agent definitions and top-level governance Markdown. Research output,
archives, external runtime instructions and untracked/private configuration are excluded.
Routing and selected sections were inspected; this is not a line-by-line semantic equivalence
proof for all 92 files. The complete per-file sizes and hashes are in
[the measurement snapshot](startup-context-audit-20260909.json).

Reproduce the snapshot measurements from repository root (no tokenizer or network required):

```bash
python3 - <<'PY'
import hashlib, json, subprocess
from pathlib import Path
audit = json.loads(Path('learning/plan/startup-context-audit-20260909.json').read_text())
for group in ('instruction_surfaces', 'scientific_startup_registries'):
    total = 0
    for row in audit[group]:
        raw = subprocess.check_output(['git', 'show', audit['base_commit'] + ':' + row['path']])
        assert hashlib.sha256(raw).hexdigest() == row['sha256'], row['path']
        assert len(raw.decode('utf-8')) == row['characters'], row['path']
        total += row['characters']
    print(group, len(audit[group]), total)
PY
```

## Where recurring context comes from

| Surface at base | Characters | When loaded / evidence | Judgment |
|---|---:|---|---|
| `literature_tracking_log_current.md` | 475,916 | `legend-start` step 5, previously unconditional | High-value state; low relevance to most harness tasks |
| `paper_registry_current.md` | 375,531 | Same | High-value state; avoid indiscriminate preload |
| `claim_registry_current.md` | 96,645 | Same | Preserve claims; load for scientific work and relevant technical inspection |
| `working_model_current.md` | 45,039 | Same | Preserve model and scientific context |
| `state_manifest_current.md` | 51,778 | CLAUDE §0: first, every session | Priority candidate for separating live state from history |
| Governance body + ten annexes | 72,318 | AGENTS instruction chain | Binding law plus frozen/superseded law and materialization prose; needs a clause-level migration map |
| `plan_defined_parameters.md` | 23,555 | Role/fingerprint reference, applicable governance | Numeric declarations and long historical explanations share one file |
| `LEGEND_CORE.md` | 31,989 | §21c–e mandatory at start; whole file on other routes | Mandatory sections are not the same cost as the full file |
| `AGENTS.md` + `CLAUDE.md` | 14,105 | Runtime entrypoint and repository router | Secondary savings; keep all obligations reachable |
| `framework/protocols/index.md` | 9,814 | AGENTS chain | Large navigation map; links do not imply loading all targets |
| `legend-capability-scout` + `legend-session-takeaways` | 12,710 | `legend-start`, every session | Scientific examples and closing details are good candidates for conditional references |
| `fulltext_read_receipt.md` | 37,641 | Named initial obligation / every full-text route | Preserve operative contract; separate schema maintenance and incident history |
| `legend_operating_convention_v1.md` | 90,538 | Task-specific protocol / index link | Largest policy-like file, but not proven unconditional at startup |
| `controlled_benchmark_ab.md` | 56,918 | Controlled benchmark work | Large, specialized; lower priority for ordinary session savings |
| `scientist_operating_practice_v1.md` | 44,701 | Scientific operating-practice reference | Conditional; do not count as universal overhead |
| `deep_dive_manual.md` | 34,031 | Deep-dive method | Scientific value is high; size alone is not a reason to cut it |

The scientific autopilot also calls `legend-start`, and the deep-dive skill/agent prescribe
registry reads again. That is a **potential repeated-load route**, not proof of multiple
loads in a particular runtime. Existing full-text duplicate-work rules already require
reusing adequate reads and resuming partial ones; they should be retained, not reinvented.

## Ranked opportunities beyond the implemented change

1. **Manifest: live state plus an exact historical archive.** `LAST BATCH_COMMIT` occupies
   16,273 characters and `LAST LINT` 11,518: together 27,791 (53.7% of the manifest), before
   considering the 12,218-character growth-anchors section. These totals include live fields,
   so they are an upper bound on those sections' removable payload, not a promised saving.
   Move historical narratives verbatim; retain active fields, unresolved conditions and a
   direct historical reference. Update readers in the same change. In particular,
   `growth_anchors.measure_candidate_backlog` currently normalizes **the whole manifest**
   to recognize consumed candidates, despite comments describing only `batch_*_scope`.
   A naive move would make consumed work look pending. Acceptance: identical candidate
   membership, gates, anchors and ratchets before/after, plus archive hashes and repaired links.

2. **Receipt contract: separate ordinary reading from schema maintenance.** The span from
   `Named open schema items` to, but excluding, `Invalidating a receipt whose study identity
   is unsupported` is 13,028 characters (34.6% of the file). It mixes historical cases,
   prospective schema rules and proposed fixtures. Preserve all of it in a maintenance
   reference; keep operational rules and an explicit maintenance trigger reachable.
   The 764-character invalidation procedure after it is operative and must not disappear
   with the historical section. A summary alone cannot prove this split lossless.

3. **Governance: expose current rules without replaying every amendment.** Frozen body,
   amended annexes, the core and role contracts make the reader reconcile old and new
   authority rules repeatedly. Preserve the original texts and use a clause-to-source map
   to design a current operating surface. Keep reserved guarantees verbatim and mandatory
   startup reachability. The fingerprint input set measures resume compatibility; it is
   explicitly **not** permission to ignore obligations outside that set. No percentage
   saving is established without the clause inventory.

4. **Skill discovery and mandatory closings.** There are 22 tracked `SKILL.md` entrypoints.
   Their single-line `description` values total roughly 14.5k characters; the harness scout
   description alone is 1,421. Descriptions repeat source lists, workflow steps and limits
   already in bodies. Keep triggers and discriminating boundaries in metadata; move recipes
   to the body. For the two mandatory closing skills (12,710 characters together), place
   scientific examples behind their scientific trigger while retaining the technical close
   and proportional micro-upgrade. Whether descriptions are all injected depends on the
   runtime; this audit does not claim they all appeared in this Codex session.

5. **Scientific record access and repeated dispatch context.** The two largest registries
   account for 851,447 characters. For technical queries, targeted lookup is now permitted.
   Extending that policy to scientific sessions needs separate validation of complete
   relevant records, linked claims, negative evidence, exceptions and cross-paper context.
   Do not replace full-text reading with keyword search. Indexing is a candidate mechanism,
   not evidence that selective scientific loading is already lossless.

6. **Tool-output discipline.** Large `cat` results in this audit were truncated and required
   follow-up reads. Inventory sizes before selecting output limits; use complete bounded
   sections, inspect omitted ranges, and return compact validator verdicts with durable logs.
   Truncation is neither a successful full read nor a useful compression mechanism.

These are audited options, not approved mass deletions. Only task-specific startup was
selected for implementation in this task. No repository instructions or scientific records
were automatically summarized to reach a numerical budget.

## Implemented route and checks of its meaning

The canonical context profile definitions live in `framework/manuals/operator_manual.md` §1;
`legend-start` points there rather than maintaining a second load matrix. The skill declares
`SESSION_PROFILE` and distinguishes validator inspection from actual context reading.
The manual's prior assertion that framework changes require Full was corrected. The live
skill catalogue, FAQ and scientific autopilot reference the new routing. The startup skill's
reference to retired `runtime_parity.py` was removed: that file is absent, and both runtimes
use the existing `harness_session_start.py` command directly.

| Scenario checked against the resulting instructions | Required behavior |
|---|---|
| Maintain a skill or documentation as Plan | HARNESS; initial chain, relevant files and structural LINT; no automatic four-registry preload |
| Debug a registry parser | HARNESS; inspect complete relevant records and dependencies; validator inspection does not attest a scientific read |
| A Scientist is assigned a code-only fix | HARNESS follows the task, not the actor's scientific role |
| Plan is asked to analyze a paper | Scientific profile; Harness role does not excuse scientific reads |
| Technical task expands into scientific reasoning | Switch profile and load its context before that work |
| Undefined task | MINIMAL default; no unsupported assumption that it is technical |
| MINIMAL / STANDARD / FULL scientific task | Existing scientific loads, receipts, locators and BATCH_COMMIT obligations remain |
| LINT reports BLOCK_SYSTEM / BLOCK_BATCH_COMMIT | Existing severity distinction remains; selecting HARNESS does not override it |

This is procedural routing, not a runtime-enforced context firewall. Static validation and
these scenario checks do not demonstrate subscription savings or behavior in a fresh live
session. A useful follow-up measurement compares matched technical tasks before/after:
files actually read, complete tool payloads, retries, omissions and provider usage if exposed.

## Session learning and decisions

WORK COMPLETED / MICRO-UPGRADE: task-specific startup plus a reproducible context inventory.
LEARNING: separate file size, required reading frequency and observed runtime usage; separate
program disk I/O from model context. Existing `PLAN-MODULAR-EVOLUTION-001.md` §M3 already
identified the context-manifest gap. This is a fresh measurement and implementation over that
prior observation, not a claim to have first discovered it. No LEARNING_INDEX was found among
tracked paths in this checkout; the record remains local rather than inventing an index entry.
CLASSIFICATION: MICRO_UPGRADE; SCOPE: harness startup; scientific delta: zero.

DEFAULTS_TAKEN: root contained unrelated dirty work → isolated task worktree from main; no
external tools or telemetry imports → local character counts; no additional agent sessions.
DECISIONS_TAKEN: implement HARNESS in the existing manual and update its callers; rejected a
second router/script and indiscriminate scientific compression. Reversible by reverting this
task's commit, restoring the prior startup contract. No peer review requested or claimed.
STOP_LOG: prior turn requested an assigned identity under AGENTS §4; the operator assigned
Harness Engineering and work resumed as `plan`. No further approval or identity wait.
Weekly startup check: `SCOUT_DUE` for 2026-W37; Junior's report is absent, so no weekly triage
or external scouting completion is claimed. No external spend, API or privacy exposure.

## Validation

`SESSION_PROFILE: HARNESS`; framework v3.3.1 / WM_v4.3; manifest READY, ingest/deep-dive/batch
gates OPEN. Structural LINT PASS; the four canonical scientific files are present and remain
byte-identical to the base. `legend-start` skill validation PASS; whitespace check PASS.
Tool preflight: all six declared tools available. Public release gate PASS, BLOCKS 0;
existing scientific REVIEW notices remain, and no publication was performed.

The full regression runner executed **90 targets before and after**. Outcomes match:
**85 non-failing suites, five failing suites, seven skipped tests**. The five failing targets
were also reproduced independently in an unmodified checkout of the exact base commit.
No new failing target, failing test case or changed skip reason was introduced. The full
suite verdict is still FAIL; this is compliance with §21e's no-regression requirement,
not a claim that the repository's tests are all green.

| Pre-existing failed suite | Finding reproduced on the clean base |
|---|---|
| `scripts/test_link_targets.py` | Candidate CC-20260909-26499798-01 references a paper-registry heading that does not exist |
| `framework/scripts/test_coverage_report.py` | Committed coverage report has drifted |
| `framework/scripts/test_batch_queue.py` | Queue drift and read count 78 exceeds the compared registry count 67 |
| `framework/scripts/test_pathograph.py` | Generated Markdown/export have drifted |
| `framework/scripts/test_reading_state.py` | Committed reading-state view has drifted |

The seven skips concern filesystem case behavior, an absent embeddable font and five checks
requiring the gitignored local full-text corpus. Detailed comparison and reproduction commands:
[validation snapshot](startup-context-validation-20260909.json). Scientific drift repairs are
outside this startup change and were not mixed into it. Self-diagnosis: startup improvement
verified at the instruction/structural level; runtime usage savings remain unmeasured.

Landing procedure: the shared root has unrelated dirty files, so the closure helper's
whole-checkout cleanliness precondition cannot be met without disturbing another task.
Use a direct `git merge --ff-only --no-overwrite-ignore` only after confirming the root has
not advanced and every dirty path is disjoint from this task; compare dirty-file hashes,
status and staged diff before/after. Never stash, stage or commit another task's work.
Detach this task worktree and delete its branch only after verifying ancestry on `main`.
