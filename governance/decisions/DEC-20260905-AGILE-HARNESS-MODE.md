---
record_type: OPERATOR_DECISION
id: DEC-20260905-AGILE-HARNESS-MODE
title: Agile operating mode — T0 changes, task-scoped worktrees landed on main by their author, root and main writable by every actor, no active gates on harness changes, Plan becomes Harness Engineering with a Junior scout
date: 2026-09-05
authority: >
  Operatore — Annex H.1 rows "Spese / MAJOR approval / governance" and "Strategia
  complessiva" (governance/annex_h_authority_matrix.md), and body §5 rank 2
  (OPERATOR STRATEGIC DIRECTIVE / OPERATOR_OVERRIDE). The operator dictated the decision
  in session and instructed that it be made without permission requests and without
  hostile review.
status: RATIFIED
status_note: >
  Ratified by the operator's own dictation and landed on `main` in the same session at the
  operator's explicit instruction ("semplicemente vanno fatte"). The 2026-09-03 practice
  of ratification-at-merge presupposed a branch-then-merge ceremony that this decision
  abolishes for harness changes; the landing commit on `main` from the operator's session
  is the ratification act. No HUMAN_APPROVAL_QUEUE entry: the operator authored the
  decision and the operator's session lands it — one act, one authority.
change_class: MAJOR
change_class_rationale: >
  governance/GOVERNANCE_v3.1.1.md:250 — "SOLO governance/authority/gate/epistemic policy".
  This decision changes authority (who lands on main), gates (none active on harness
  changes) and governance (roles). It is the operator's to make, and the operator made it.
supersedes: >
  Partially — DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY item "worktree provisioning:
  agents, once the guard false refusal is fixed (0B)" is now discharged (the guard is
  fixed by this change). Its RESERVED list, §21c and §21d bodies are NOT changed.
applies_to:
  - framework/instruction/LEGEND_CORE.md (§21e, new — the canonical home of the rule)
  - governance/GOVERNANCE_v3.1.1.md (amendment callout; §11, §12, §14, §30, §35.1, §47, §48 superseded where they conflict)
  - governance/annex_d_commit_batch.md (amendment callout; D.1, D.3, D.4 superseded where they conflict)
  - governance/annex_h_authority_matrix.md (amendment callout + amended H.1 rows)
  - governance/plan_defined_parameters.md (§ P2.2 — junior-harness row)
  - roles/plan.md (rewritten — HARNESS ENGINEERING), roles/junior_harness.md (new), roles/orchestrator.md, roles/mirror.md, roles/scientist.md (amendment callouts)
  - BOOTSTRAP.md, deployment/deployment_profile.md, CLAUDE.md §0, AGENTS.md §1 (amendment callouts / links)
  - framework/protocols/parallel_legend_protocol.md (rules 1–2), framework/protocols/legend_operating_convention_v1.md (S.6.3)
  - framework/scripts/guard_policy.py, framework/scripts/effect_model.py and their suites (landing operations allowed)
  - framework/scripts/branch_hygiene.py (new), .claude/skills/legend-harness-scout/SKILL.md (new)
task_id: AGILE_HARNESS_MODE_v1
mode: OPERATOR_DICTATED_DECISION → LANDED_ON_MAIN_AT_T0
---

# AGILE OPERATING MODE — 2026-09-05

## DECISION_ID

`DEC-20260905-AGILE-HARNESS-MODE`

## OPERATOR_TEXT (verbatim, Italian, as dictated in session)

> vorrei fare alcune modifiche a questa repo molto importanti: avere una struttura agile e non
> rigida, se dobbiamo fare cambiamenti sempre in poche ora in T0 e non più T1, T2 o T3, voglio
> che si lavori sul worktree dedicato solo fino a fine task e poi si metta tutto in main una
> volta concluso il task, voglio che tutti possano scrivere in root e main. Su tutte queste
> modifiche non chiedo il permesso o hostile review, semplicemente vanno fatte. Tutte le repo
> simili a Legend hanno strutture agili e flessibili, solo Legend è così rigida, l'alternativa
> e tornare ala prima Legend non quella development. Anche Plan a tendere lo vorrei trasformare
> in un Harness Engeneering che ha un Junior Harness Engeneering che fa scouting su repo simili
> facendo github, hugging face e Nature portfolio mining, propone settimanalmente candidate a
> Plan (Harness Engenering) che le implemente in ore non settimane, senza passare per MIrror e
> senza gate attivi

And, from the question that preceded it in the same session: *"includi anche Codex nel
ragionamento"* — Codex is inside the scope of the rule, not outside it.

English rendering (Orchestrator's, non-ratified): an agile, non-rigid structure; decided
changes are made in hours, at T0, never deferred to T1/T2/T3; work happens in the dedicated
worktree only until the task ends, then everything goes to `main`; everyone may write in root
and on `main`; none of this asks permission or hostile review — it is simply done; the
alternative is a return to the first LEGEND, not the development one; Plan is to become
Harness Engineering, with a Junior Harness Engineer scouting similar repositories (GitHub,
Hugging Face, Nature portfolio mining) and proposing candidates weekly, which Harness
Engineering implements in hours not weeks, without Mirror and without active gates.

## QUESTIONS_DECIDED

| # | Question | Decided |
|---|---|---|
| Q1 | When is a decided change implemented? | **T0 — the same session, in hours.** T1/T2/T3 are abolished as resting places for a decided change (§21e "T0"). |
| Q2 | How long does work live on a worktree/branch? | **Until the task ends.** Then the **author** lands it on `main` and deletes the merged branch. Nothing unmerged at rest; a branch ahead of `main` for more than one day is a finding (§21e "WORKTREE AND BRANCH LIFECYCLE"). |
| Q3 | Who may write in the root checkout and on `main`? | **Every actor.** No canonical-batch surface reserved to one actor, no session-home/work-surface split, no integrating-session monopoly, no lease precondition (§21e "SURFACES"). |
| Q4 | Which gates apply to harness changes? | **None active.** No Mirror precondition, no HUMAN_APPROVAL, no GATE 0–5, no MAJOR classification. Mirror reviews ex post and on request (§21e "GATES"). |
| Q5 | What becomes of Plan? | **HARNESS ENGINEERING** (ACTOR_ID `plan` kept for continuity of ledgers, fingerprints and inventories). It implements harness changes at T0. A new **JUNIOR HARNESS ENGINEER** (ACTOR_ID `junior-harness`) scouts weekly and proposes; it does not gate (§21e "ROLES"). |
| Q6 | Does Codex follow a separate regime? | **No.** Same lifecycle under its assigned ACTOR_ID; `codex/*` branches are task-scoped and landed by their author (§21e item 5). |
| Q7 | What is NOT changed? | §21d's RESERVED list (publication, history rewrite, irreversible deletion of unique material, external spend, private-data exposure, changes to §21c/§21d/§21e); the scientific discipline (the four current files change only through `BATCH_COMMIT` under `LINT`; read receipts; locators; BLOCK-1); the guard's refusal of force, `git clean`, blanket staging, shell writes into the repository and every `git push`. |

## WHERE THE RULE LIVES

`framework/instruction/LEGEND_CORE.md` **§21e AGILE OPERATING MODE** is the single canonical
home. Every other file touched by this decision carries a pointer or an amendment callout, not
a second copy. Where older text — body §11, §12, §14, §30, §35.1, §47, §48; Annex D.1, D.3, D.4;
Annex H.1; the role contracts; `BOOTSTRAP.md`; `parallel_legend_protocol.md` rules 1–2;
`legend_operating_convention_v1.md` S.6.3 — conflicts with §21e, **§21e prevails**. The older
text is preserved for provenance and is not rewritten line by line: the operator asked for a
working laboratory in hours, and a full re-materialisation of the constitution would itself
have been a T2 act.

## MAPPING — Annex H.1 rows amended by this decision

| H.1 row (frozen text) | Was | Now (§21e) |
|---|---|---|
| Integrazione strutturale / candidate | Plan | Harness Engineering (`plan`) lands its own harness changes; every author lands its own task branch. The INTEGRATION_CANDIDATE object is no longer required for landing. |
| CANONICAL_BATCH_COMMIT | Orchestrator (unico, lease ACTIVE) | Whoever holds the `BATCH_COMMIT` task, under `LINT`, one batch at a time, no lease. The four scientific current files still change only through `BATCH_COMMIT`. |
| WORK_COMMIT | ogni attore, solo proprio branch, granularità milestone | Every actor, on its task branch **or directly on `main`** for a change that is finished when it is written. Milestone granularity stands. |
| Spese / MAJOR approval / governance | Operatore | Unchanged for spend and for the RESERVED list. Harness changes are no longer "MAJOR approval" items: they are T0 work of Harness Engineering. |
| Classificazione MAJOR dubbia | Mirror (fail-closed) | Not applicable to harness changes (no classification). Unchanged for scientific baseline reversals (`legend-locator-audit`, `MAJOR` working-model bumps). |
| Epistemic / method review | Mirror | Unchanged — but ex post and on request, never a precondition for landing. |

## VERIFICATION_TRAIL

| Check | Command | Result |
|---|---|---|
| Live actor sessions at decision time | `ListAgents` | 5 peers open in the five actor worktrees (evidence-index, lettore, lettore-b, lettore-c, mirror), this session in root |
| Worktrees and branch divergence before the change | `git worktree list`; `git rev-list --left-right --count main...<branch>` | 6 actor worktrees; `mirror` +103, `evidence-index` +55, `orchestrator` +43, `lettore` +37, `lettore-c` +28, `lettore-b` +25 commits not on `main` — the pathology this decision ends |
| Guard behaviour before the change | `guard_policy.classify` on `git merge`, `git worktree add`, `git branch -d` | all `PROHIBITED` / `REF_WRITE_REQUIRED` |
| Guard behaviour after the change | same, plus the negative controls (`--force`, `-D`, `push`, `add -A`, `reset --hard`) | see the landing commit's test output; the negative controls stay `PROHIBITED` |
| Regression suites | `python3 scripts/run_release_regressions.py`; `python3 -m unittest discover -s framework/scripts -p 'test_*.py'` | recorded in the landing commit message |

## OUT_OF_SCOPE

Not done, not authorised, not implied by this record:

- any `git push` — publication stays the operator's, on every remote;
- merging the six existing actor branches into `main` — each author lands its own branch under
  §21e; this record changes the rule, it does not perform six merges over other actors' work;
- removing existing worktrees — a persistent chat keeps its worktree as a home; removal
  happens when a chat is closed and its branches are landed;
- any change to the scientific discipline or to the RESERVED list.

## ATTESTATION

**Recorded by:** the operator's root session (Claude Code, `main`), at the operator's explicit
dispatch, 2026-09-05. OPERATOR_TEXT is the operator's own words. Everything else in this record
is the recording session's rendering and mapping, and is not itself ratified text; where it
and §21e disagree, §21e is the rule.
