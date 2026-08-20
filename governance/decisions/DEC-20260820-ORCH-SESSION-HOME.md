---
record_type: OPERATOR_DECISION
id: DEC-20260820-ORCH-SESSION-HOME          # renumber per decision registry convention if needed
title: Orchestrator session home — operator architectural intent (CONFIRMATION)
date: 2026-08-20
authority: Operatore                 # per Annex H.1 (governance → Operatore) and body §4
status: BINDING_UPON_OPERATOR_RATIFICATION
change_class: CONFIRMATION           # confirms existing FROZEN governance and registers operator intent; amends nothing
supersedes: none
applies_to:
  - CAND-20260819-ORCHSURF (all revisions)
  - any future candidate touching Orchestrator surfaces, bootstrap, or promotion
drafted_by: external advisory (Claude/Fable), at operator request
ratified_by: ""                      # OPERATOR: fill name + date to make this record effective
---

# 1. Decision

The Human Operator states, as explicit architectural intent — not as a
legacy arrangement to be corrected:

1. **Orchestrator session home = repository ROOT** (`legend-public`).
   The Orchestrator chat/session is intentionally opened at the
   repository root. This has been the operator's consistent practice
   since the beginning, following instructions received, and it is the
   intended model going forward.

2. **The dedicated `orchestrator` worktree is the actor's technical
   surface** — WORK_COMMIT, scratch, intermediate work. It is NOT the
   chat/session home and must not be documented as such.

3. **Root residence confers neither identity nor authority.**
   `cwd = root` is not an ACTOR_ID oracle and not a write-authority
   oracle. This principle is already established and verified in the
   canonical record; nothing in this decision weakens it.

4. **Canonical writes on root/main remain separately gated** —
   exclusively within the batch window under lease + GATE 0–5.
   A root-resident session holds no standing write authority.
   The Orchestrator may inspect and coordinate from root, but any
   non-batch modification intended for persistence MUST occur on its
   assigned worktree surface. The historical risk is not root as a
   location but root as an accidental work surface:

   | Action                          | Root          | orchestrator worktree |
   |---------------------------------|---------------|-----------------------|
   | Open session                    | yes           | no                    |
   | Coordinate / observe            | yes           | yes                   |
   | Read repository                 | yes           | yes                   |
   | Write intermediate WORK_COMMIT artifacts | no (steady state) | yes        |
   | Canonical commit on main        | batch only    | no                    |

   This table describes **steady-state (post-promotion) operation**.
   The FROZEN pre-promotion perimeter — body §0.4 and Annex I.2:
   "SOLO artefatti di bootstrap" — is a prior, narrower allowance for
   root writes during bootstrap that this record does not modify and,
   sitting at rank 2, could not modify. The table is NOT an abrogation
   of that perimeter; any Rev4 text must state both regimes explicitly.

5. **Mechanical enforcement of (4) is a separate, deferred candidate**
   (working name CAND-20260820-ROOTGUARD-001; proposed trigger: first
   canonical batch after ORCHSURF canonicalization). It is explicitly
   OUT OF SCOPE for ORCHSURF and must not enter it.

# 2. Provenance and precedence effect

This record is a **CONFIRMATION of existing FROZEN governance**, not a
governance change:

- **Primary basis — body §8** ("ORCHESTRATOR — ROOT, AUTORITÀ,
  IDENTITÀ"): "Orchestrator vive nella chat grafica associata a
  <REPO_ROOT>" and "La posizione nella root NON conferisce autorità.
  L'autorità deriva dal ruolo esplicitamente assegnato e, per
  Orchestrator, dal LEASE ACTIVE." Items 1 and 3 of §1 above are
  therefore **already FROZEN normative text at rank 1** (per Plan
  finding F-1, session of 2026-08-20). This record does not grant the
  architecture; it recognizes it, and it removes the ambiguity under
  which three revisions and one hostile review cited §8 only for a
  subordinate clause while missing its operative statements.
- Body §0.2 ("la stessa chat viene promossa; non servono due chat
  root"), §0.4, §47 steps 10 and 14 — as identified by ORCHSURF rev 3 /
  test T10 — and Annex I.2 (root-promotion steps) encode the same
  architecture. All of these are correct and are to remain untouched.
- Consequently, **no FROZEN transition is required or requested**. The
  HUMAN_REQUIRED transition contemplated in ORCHSURF rev 3 §5 (amending
  body + Annex I.2 to extinguish root-promotion, rotating all four
  fingerprints, invalidating all checkpoints) is **superseded as a
  proposed remediation direction by this operator architectural
  intent**; no FROZEN transition is requested. The rev 3 finding itself
  (the body carries the mandate, at the top of precedence) remains
  valid and is part of the basis of this record.
- Section references above are taken from the ORCHSURF rev 3 report and
  MUST be re-verified by Plan against the documents themselves before
  citation in any candidate (no inherited source lists — per the T7/T8
  lesson recorded in that same revision).

# 3. Binding consequences for ORCHSURF

The review question is inverted. It is no longer:

> "how do we eliminate the legacy root-resident Orchestrator?"

but:

> "how does a persistent Orchestrator session live at root while root
> writes remain strictly governed by lease + GATE 0–5, and while
> cwd/root location alone confers neither ACTOR_ID nor authority?"

Accordingly:

- The rev 2/rev 3 remedy direction — removal of the root-promotion
  procedure from `BOOTSTRAP.md` — is identified, after operator
  ratification, as **inconsistent with the operator architectural
  intent** and should be reverted. The root-promotion
  model (first chat opened at root → promoted to Orchestrator → same
  chat remains at root) is the intended design.
- A **revision 4** is expected that: (a) restores the root-promotion
  procedure in `BOOTSTRAP.md` consistent with body §0.2/§47 and Annex
  I.2; (b) retains the creation of the `orchestrator` worktree as a
  technical surface (compatible with this intent); (c) re-scopes the
  post-ORCHWT documents (`deployment/deployment_profile.md`,
  `roles/orchestrator.md`, and any others) so that the worktree is
  described as technical WORK_COMMIT surface, never as session home;
  (d) **preserves intact the direction-independent evidence** of rev 3:
  test T10 and its FROZEN-universe enumeration method, SLR-plan-0012,
  the SLR-plan-0012 P-2 finding concerning SLR-plan-0011 truncation,
  and the T7/T8 inherited-universe correction.
- `runtime/bootstrap/STEP5-session-open-plan.md` ("The Orchestrator
  chat is already open in the root checkout") is, under this intent,
  **correct — not stale**. Any inventory that classified it as a stale
  declaration is to be re-adjudicated under this record.
- After operator ratification, Plan and Mirror MUST evaluate ORCHSURF
  revisions against this operator architectural intent record. The
  record does not replace or amend governance: it defines the external
  operator requirement that governance procedures are to apply. A
  review conducted without it is conducted against the wrong premise.
- **Precedence position**: this record sits at operator-directive rank
  (rank 2 per body §5), subordinate to NON-NEGOTIABLE governance at
  rank 1. No conflict arises: per F-1, rank 1 already states the same
  architecture. If a genuine conflict with rank 1 were ever found, rank
  1 prevails and this record must be revised, not the FROZEN text.

# 4. What this record does NOT do

- It does not modify, and does not authorize modifying, any FROZEN
  document.
- It does not grant, extend, or imply any write authority to any
  session by virtue of its location.
- It does not implement, schedule, or smuggle in ROOTGUARD or any other
  enforcement mechanism.
- It does not adjudicate ORCHSURF findings other than fixing the
  architectural premise under which they are to be read.

# 5. Root cause acknowledged (for the learning record)

The rev 1→3 drift originated **outside the repository**, in the
human↔AI advisory chain: a true fact (WORK_COMMIT → orchestrator
worktree) was collapsed into a false rule ("the Orchestrator session
must live in the worktree"), then handed to Plan as a prescriptive
premise. No diff, gate, or lint could observe it, because the premise
never existed as a repository artifact. This record exists precisely to
close that gap: operator architectural premises must live as citable
canonical artifacts, not in chat memory. This paragraph is offered as
input to the semantic-regression workstream (filone B). The episode also
surfaced a general architectural principle, recorded here for future
actors (A/B/C/D/E, LRR): **a session's location and the surface where it
may produce persistent artifacts are two independent dimensions**
(SESSION_LOCATION is not PERSISTENCE_SURFACE); conflating them was the
root of this drift.

# 6. Operator ratification

This record is drafted by the external advisory and has **no effect
until ratified**. To ratify: fill `ratified_by` in the frontmatter with
name and date, and deliver the file to Plan (manual transport, per
current routing status). Plan should register it per the decision-record
convention and treat §1–§4 as binding input for ORCHSURF revision 4 and
the subsequent Mirror review.
