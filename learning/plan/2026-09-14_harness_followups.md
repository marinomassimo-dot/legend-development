# Harness follow-ups — 2026-09-14

Actor: plan. Runtime: Codex. Operator authorised implementation of the six review topics.
Base: cb181dd (full object name in the task record). No scientific reading or conclusion
was performed here. No independent model review is claimed.

## Changes and measured limits

- Citation classification: two lexical/structural signs now yield POSSIBLE_CONTRAST,
  a review warning, never a verdict that a supporting link is forbidden. The synthetic
  sentence supporting two claims despite different conditions pins the counterexample.
  Existing declared edges are outside the scientific validation scope of this check.
- One Claim links parser serves support_linkage, trace_claim_foundation and the semantic
  graph generator. Six live records differ from the old whole-field digit scan:
  CORPUS P261, P268, P207; PAPER 082, 083, 094. Five are explicit non-links; P207 keeps
  CLAIM 028 while dropping the four numbers in its parenthesised source-mapping note.
  Four declared wikilinks initially lost by my first parser draft were caught in the
  whole-corpus comparison and restored before landing. Canonical files are unchanged.
- task_summary derives CURRENT_STATE and OUTCOME from all structured queues, checks
  nonempty steps and evidence declarations, and retains earlier display fields with a
  source digest. HARNESS-EXEC now says COMPLETE, 14/14, consistently. It does not verify
  evidence contents, release runtime sessions or edit queue steps. Manual concurrent
  writers remain outside its guarantees; use the owning task checkout.
- task_dispatch invokes task_id_collision under a shared-clone lock, checks linked
  worktrees and atomically publishes a new record without replacement. Native delivery,
  ACK and resume remain the actor's actions. No second ledger, no agent launched.
  Concurrent same-ID registration and a collision in another worktree are tested.
  Separate clones and writers bypassing the command remain outside this lock.
- Commit wrapper generates a closed-vocabulary subject from surface categories; all
  author text remains in the body. task_close uses a fixed merge subject. The older
  lexical checker stays available, explicitly without a blindness guarantee. Historical
  commits, bare git and other runtime-injected text are not changed. The wrapper's
  pre-existing .git-file lock defect in linked worktrees was fixed using git-common-dir.
- Batch protocol now follows state-manifest version semantics: structural-only batches
  preserve WM version, WM timestamps and changelog; scientific meaning/eligibility
  changes are not structural-only. Publication integrity remains orthogonal to lifecycle
  Status, using the existing corpus flags, batch_queue eligibility and LINT. LIT-0401
  remains unmapped and integrity-excluded; no new status or registry is invented.

## Verification

Eleven new adverse-case tests pass; five deliberate mutations are detected (contrast
verdict, negated links, always-complete summary, disabled collision check, free-text
subject). Related suites: support linkage 23, semantic graph 10, foundation trace 20,
task close 17, commit subjects 6, wrapper 8, collision check 12 pass.
Release comparison: pending on isolated base and changed checkouts without local corpus.
LINT: WARN, including explicit POSSIBLE_CONTRAST and the retained legacy Status.
Publication gate: PASS, zero blocks before this report; final-state run pending.

## DECISIONS_TAKEN / DEFAULTS_TAKEN

Use a fresh worktree and leave the other Harness actor's mandate-continuity repair alone.
Implement scientific relation *parsing*, not scientific relation adjudication. Preserve
existing retraction exclusion. Generate neutral subjects rather than expand a word ban.
All changes are reversible by ordinary corrective commits; no push or history rewrite.
Weekly scout: startup reports SCOUT_DUE; the Junior's weekly input is absent, not fabricated.
Micro-scout: reused the existing collision checker, task ledger and integrity eligibility
rather than introducing a parallel queue or integrity vocabulary.

## STOP_LOG / self-diagnosis

No operator clarification or quota wait. Implementation and validation continue to landing.
Gap: no new live-model blindness or agent-delivery experiment; tests exercise repository
behaviour. Learning: a lexical contrast marker is a review clue, not an epistemic verdict;
whole-corpus before/after comparisons protect valid exceptional declaration formats.
