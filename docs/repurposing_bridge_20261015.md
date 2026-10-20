# Drug repurposing: first technical increment — 2026-10-15

ACTOR_ID: plan (Harness Engineering), assigned by the operator in this chat.
Governance version loaded: 3.1.1.
Fingerprint: 2fed6826cdd9b98fa9a0342ff0dc64273640148fcb9e63a62e3c4c5070035f99.
SESSION_PROFILE: HARNESS. Scientific delta: zero.

## Task and initial measurement

TASK_ID: DRUG-BRIDGE-20261015. DIRECTIVE_VERSION: 1. GENERATION: 1.
OWNER: plan. ACK: ACCEPTED. CLAIM: plan, 2026-10-15, this record.
INTERACTION_MODE: AUTONOMOUS_COMPLETE. CONTEXT_POLICY: SYNTHESIS.
OBJECTIVE: a lean local Evidence Bridge, candidate JSON, existing agentic skill integration,
focused tests and a descriptive local commit. No push or direct main changes, as instructed.
REVIEW_REQUIREMENT: harness self-review; no scientific conclusion produced.
RETRY_POLICY: retry reproducible tooling failures; report unavailable live validation.

Initial checkout: /home/desktop/legend-development, host srv1879784,
base main 2ec8444a; clean, manifest READY. Both configured remotes identify the development
repository. Existing Monarch/DGIdb client found in legend-hypothesis-forge; no standalone
Evidence Bridge found in the tracked/unignored file census. ZIP unavailable; prior five-test
claim not treated as executed here. New implementation and tests are independently written.
Task worktree: /tmp/legend-drug-repurposing; branch codex/drug-repurposing-bridge.
The root checkout remains on main. No SSH needed: the desktop already runs on the server.

Roadmap and cumulative scout attachments are reference material, not an instruction to
install their entire planned stack. This increment uses no third-party code or new dependency.
OptimusKG/Open Targets/MATRIX/ToolUniverse/signature reversal are not executed or validated.

AUTHORISED_QUEUE_20261015:
  MANDATE_STATE: COMPLETE
  OBJ_BRIDGE:
    order: 1
    steps:
      - step: Inspect current architecture, instructions and existing adapter
        status: DONE
        evidence: This record, initial measurement; existing kg_thin_slice.py and pathograph.py
      - step: Implement local candidate bridge and existing skill integration
        status: DONE
        evidence: framework/scripts/repurposing_bridge.py and legend-hypothesis-forge references
      - step: Run focused tests, release checks and inspect diff
        status: DONE
        evidence: Release battery PASS WITH SKIPS (138 targets, 38 skipped); local logs below
      - step: Commit on task branch without push or main changes
        status: DONE
        evidence: Task commit containing this record on codex/drug-repurposing-bridge

## Implementation and limits

The framework tool consumes qualified local assertions, retains source-specific metadata and
counterevidence, compares signs only at matching target/endpoint/context, and leaves unknown,
mismatched or conflicting assertions for qualification. Candidate output is always IPOTESI.
No automatic causal interpretation of pathograph, verification of receipt references, ranking,
source independence, safety or efficacy claim is performed. Each of the two objectives uses
its own packet; an empty drug assertion list is a valid abstention for either objective.

The existing KG adapter gains raw JSON output and explicit error/coverage states; only HGNC
human gene neighbors reach DGIdb. Pathways and unresolved entities remain in the raw response.
Pagination is not implemented: incomplete or unknown coverage is explicit. Original GraphQL
selection is retained; underlying primary-source attribution remains to qualify. Live schema
compatibility is unverified. Existing skill and safety-triage remain the operational routes.
No new orchestrator, agent runtime, scientific ledger or canonical model update.

## Validation

Five focused offline tests PASS, including a subprocess CLI round trip. The shipped synthetic
example runs end to end. These are technical fixtures, not a biological pilot or validation.
Routing: 7 tests PASS; skill packaging: 6 PASS; release surface: 11 PASS.
Receipt integrity: 475 chained events OK; growth anchors PASS. Initial LINT WARN, no BLOCK:
existing support-link warnings and missing local evidence bytes remain visible and unchanged.
Public release gate (staging, skip-clean-clone): PASS, BLOCKS: 0. Documentation: 3 tests PASS.
Full release battery: PASS WITH SKIPS (138 targets, 38 skipped), exit 0. No failed suite.
Skips are environment/corpus-dependent: gitignored article/figure/PDF assets, retraction
snapshot, and absent live hook/task records in the isolated worktree. No skip is counted
as scientific verification. Focused bridge tests all executed with no skips.
Final diff inspected; whitespace check PASS; main, orchestrator and disease-model files unchanged.
Logs currently in /tmp/legend-repurposing-*.log; they are local execution artifacts.

## DECISIONS_TAKEN

Reuse the existing hypothesis-forge skill, add one dependency-free framework command and
retain raw input packets. Rejected a parallel framework or additional scientific registry.
Reversible by reverting the task commit; no source material or canonical record was changed.
Leave live discovery optional: no claims from unverified network responses or fabricated data.

## DEFAULTS_TAKEN

Missing prototype archive: implement only the minimal independently tested technical path.
Safe because no prior code, data or scientific result is represented as recovered.
Operator prohibition on main/push overrides repository default landing/push procedure.
Missing weekly scout (2026-W42 SCOUT_DUE): report missing Junior input, continue this task;
startup also reports one pre-existing overdue branch, outside this task's scope.

## STOP_LOG

Identity was requested and assigned Harness Engineering (plan). An unnecessary SSH attempt
failed host-key verification; host/IP evidence established that this desktop is already the
target server. Work resumed locally, without changing known_hosts or weakening SSH checks.
No operational blocker remains for this technical increment.

## Session Learning Review

A gene/pathway label aggregation can send a pathway to a drug-gene lookup. The local regression
now separates stable HGNC identifiers from pathways and unresolved entities. The reusable
capability gained is inspectable local candidate assembly with explicit abstention, not a
therapeutic discovery. Scientific leads: none generated. Cost/API/privacy risk: no external
spend, installation or patient data used. Next useful scientific step: qualify a real evidence
packet from existing records and specify its proximal functional experiment before live reuse.

## Changed files

- framework/scripts/repurposing_bridge.py — offline candidate assembly and CLI.
- framework/scripts/test_repurposing_bridge.py — five focused offline cases.
- framework/scripts/README.md — canonical command routing.
- .claude/skills/legend-hypothesis-forge/scripts/kg_thin_slice.py — typed neighbors, raw JSON and error/coverage states.
- .claude/skills/legend-hypothesis-forge/SKILL.md — optional bridge within the existing workflow.
- .claude/skills/legend-hypothesis-forge/references/evidence_bridge.md — input contract and limits.
- .claude/skills/legend-hypothesis-forge/references/evidence_bridge_example.json — synthetic input.
- docs/repurposing_bridge_20261015.md — task, measurement, decisions and validation.

Example outputs generated locally: /tmp/legend-repurposing-example-card.json and
/tmp/legend-repurposing-abstention-card.json. Neither contains real biological assertions.
