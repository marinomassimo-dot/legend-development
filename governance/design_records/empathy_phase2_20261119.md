# EMPATHY Phase 2 — selective learning and current guidance (2026-11-19)

Author: Harness Engineering (`plan`), Codex runtime. Operator authorised this implementation in chat after the [Phase 1 report](empathy_phase1_20261119.md). This record is non-normative; the method lives once in cross-session transport section 12, EMPATHY. No scientific result, clinical advice or individual information is introduced.

## What changed and why

Phase 1 is sufficient for the first implementation. It distinguishes missing provenance from an application failure: cold readers could find a continuity rule that the warm host still failed to apply. More copies of the same instruction would not establish improvement.

- The receiving actor now has the selective two-question method, including rationale, scope, provenance, temporary tasks, inferred preferences and brainstorming. This is a reasoning habit, not an automated classifier or a write on every message.
- The existing operator roadmap has a short current section, organised by situation. Its old operator block is retained byte-for-byte as historical provenance, outside the current operator markers. Historical pilot caps, expired scheduling and old host identity no longer appear as current guidance. Existing control-line syntax is preserved; no authorisation or counter is reset.
- `mandate_continuity.py guidance` is a read-only, runtime-independent reader of that current section. The shared router and startup skill point to it. It reads no private memory and writes no state.
- The current guidance is read again in the existing ADV tick and the revival request. An already installed recall receives changed guidance through its tick output; a second cron, host or model call is not needed. The recall text also points to this field. The renewal/drift procedure remains the existing one.
- The optional analyst and accountable host are distinguished in the ADV skill; outdated identity and recall-loss statements point to the current role and measured recovery rule.

The active criteria are faithful paraphrases of documented operator directions: useful continuity, knowledge-to-research loops, broad discovery with precise evidence, reversible lean design, validation of the consumed output, and efficient use of resources. The translation principle now records the operator correction and its rationale. These criteria are not a second authority or an exhaustive list of future situations.

## Design choices and limits

This implements Phase 1 O1/O4 and a narrow part of O3: existing decision-time channels read the same live section instead of embedding a stale copy or selecting fixed top-three lessons. It adds no memory store, schema for each prompt, new agent, service, scheduler, gate, scientific-field mutation or model-mediated capture. An inferred preference is revisable interpretation in an existing design note; a clearly tentative pointer can make it retrievable when useful without promoting it into operator authority. The hot section contains current guidance; superseded interpretations and dated instructions remain consultable as history.

The complete original operator block had 46,100 UTF-8 bytes and SHA-256 `4a108dce4bcce213369a765a989c1f8377f041bb5a23c26e2cd3b3ed88ef4c5d`; preservation was checked after the edit. The new situation section is about 4.3 KB. These are source sizes, not token prices or demonstrated behavioural gains. The old block's complete originals are available when a decision needs their detail; a current guide does not substitute for a full scientific input.

No new paid service or model probe was launched. Phase 1 A/B/C are single-model, scenario-cued observations; their memory canary is not proof of all runtime isolation. Codex's implementation session has the operator conversation and is not a blind reader. A new process reading the repository section is a retrieval check, not a model-level cold-start or crash test.

## Verification

Focused checks passed: mandate continuity (80 tests, one existing environment skip), mandate watch (59 tests), Strategic Advisor suite (exit 0), tool routing, section references, skill packages, closed-world assertions, daily scout and documented commands. Structural LINT had no BLOCK; receipt-chain and growth checks are recorded with the release checks. The complete release battery and publication are recorded in the task record, with their exact revisions. Focused regressions cover a replacement process recovering a rationale without the old chat, exclusion of dated/superseded text and a temporary task, a changed criterion reaching the next read/tick without rebind, missing or ambiguous markers staying visible without a new gate, revival reading the requested checkout, and operator PAUSE retaining precedence without a model launch.

## What remains observable in production

EMPATHY is technically connected after landing; improved autonomy is not yet demonstrated. At the next pertinent closures, ADV and the receiving actors should record in existing decision/mandate notes which criterion and rationale changed a choice, actual follow-through and useful outcome, or no effect. Do not force activity, novelty, a positive result, or a scheduled re-test. If guidance was present but unused again, diagnose application/context rather than add another copy. Use the existing DREAM/self-evaluation path to revise or retire an unhelpful interpretation. No new monitoring service or learning ledger is required.

## Removal

Remove the `guidance` reader and its calls in the tick/revival, the added router/start pointers and the method if this pattern adds no value. The original dated operator block remains in the same roadmap history. Preserve operator controls and canonical scientific/authority rules. No database, private-memory migration or background process needs undoing.

## Session Learning Review

Session: Codex EMPATHY Phase 2, 2026-11-19; ACTOR_ID `plan`, Harness Engineering; task `PLAN-EMPATHY-PHASE2-20261119`. Classification: `MICRO_UPGRADE`, local technical observation, not a promoted best practice or a replication of the Phase 1 model probes. Scope: operator-intent retrieval and its existing consumers, not scientific inference.

**Work, problem and solution.** Phase 1's missing provenance and warm-host application failure are different problems. The change records selective rationale in the existing current seat and carries it into existing startup, tick and revival paths; it does not claim that another saved instruction cures an application failure. The operator's original block remains lossless. Concurrent HE routing corrections were reconciled in the implementation worktree, leaving the standalone battery clone unchanged. One post-merge test command named `test_tool_routing.py` under the wrong directory and failed to import it; the actual `scripts/test_tool_routing.py` was then run and passed. This was an invocation error, not a product regression.

**Learning and impact.** A source can be durable yet hard to recover, and easy recovery can still fail to influence a choice. The measured micro-upgrade is current, scoped retrieval without a private index or an additional model invocation. The behavioural question remains whether a later different situation produces a better choice and follow-through. No new scientific candidate or therapeutic conclusion is asserted. Evidence: the Phase 1 artifacts, the source-history equality check and the focused subprocess/tick/revival regressions listed above; no new `LEARNING_ID` or learning index is invented.

**DEFAULTS_TAKEN / DECISIONS_TAKEN.** Reuse the shared roadmap and existing readers rather than introduce a new memory store; retain history while shortening the active input; run no further paid model probe; integrate concurrent changes only in this task's worktree. No local worktree holds `main`, so publication uses the existing serialized author-push path rather than switching or stashing a peer's primary checkout. These choices are reversible through the removal steps above. No independent scientific adjudication was needed for this harness-only change.

**STOP_LOG.** No operator confirmation or external decision was requested. Waiting on the existing isolated battery is verification in progress, not a new assignment left for the operator. The task record preserves the tested revision and distinguishes it from later integration/publication revisions.
