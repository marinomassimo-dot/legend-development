---
artifact: MIRROR handoff — role contract hostile review
handoff_id: HANDOFF-ROLE-CONTRACTS-001
review_id: REV-ROLES-MIRROR-001
reviewer: mirror
task_id: MIRROR_ROLE_CONTRACT_HOSTILE_REVIEW_v2.2
dispatcher: operator
date: 2026-08-22
process_status: WAITING_EXTERNAL_DECISION
next_owner: operator
next_transition: HUMAN_GATE
next_transition_note: >
  `HUMAN_GATE` is the dispatch's vocabulary and has NO repository source — absent across all 41
  content refs. It is reproduced here because the dispatch requires the field, and it creates no
  repository meaning. The repository's real objects for this transition are HUMAN_REQUIRED
  (body §4), HUMAN_APPROVAL / HUMAN_APPROVAL_QUEUE (Annex J.3) and GATE 0–5 (body §12).
scope: transmission of findings only. No contract text proposed, no ratification, no DEC record,
  no HUMAN_APPROVAL record, no cadence resolved, no ownership assigned.
---

# HANDOFF — four role contracts, hostile review

## OBSERVATION_SCOPE

```
checkout        <REPO_ROOT>/.claude/worktrees/mirror
branch          mirror
HEAD            9e6cf0ccb3b0f8f923189cf31e4fa7daec9fa97a
refs surveyed   41 content refs (32 heads · 4 remotes · 5 tags)
                excluded: 4 refs/codex/turn-diffs/* and refs/stash (non-content)
LINT            PASS (1 INFO)
main ref state  04693e683a254ff0a6d0619fba47103a0fb7d122 — observed only, NOT moved
```

### Limitations — read before the findings

1. 🔴 **This checkout is 63 commits behind `main`** (70 ahead, merge-base `908197ba`). It is
   **missing** `runtime/orchestrator_lease.md`, `framework/scripts/lease_state.py` and
   `framework/protocols/scientist_reading_modes.md`, all present on `main`; and
   `runtime/agent_card_registry.md` + `runtime/runtime_inventory.md`, which exist on
   **`refs/heads/orchestrator` alone**. Those objects were read from the refs that carry them.
2. 🔴 **`roles/scientist.md` on this checkout is superseded.** Local `e9328115…`, `main`
   `fd30134d…`. Verdict anchored on `main`'s blob.
3. 🔴 **Every role's fingerprint differs between this checkout and `main`** — including roles whose
   contract file is byte-identical, because `plan_defined_parameters.md` is in `CORE` and differs.
   No actor may resume across these two refs under A.6.
4. The dispatch named paths, not a ref. Where the two refs disagree I measured both and said so.
5. I did not audit the 63 trailing commits beyond the four objects and their fingerprint inputs.
6. Nothing here is inherited: no previous review, conclusion or hash was carried. All values
   recomputed this session.

---

## PER_CONTRACT_STATUS

### `roles/plan.md` — **CHANGES_REQUIRED** *(C.2: WEAKENED)*

| Sev | Finding |
|---|---|
| **MAJOR-1** | Declares the fingerprint-composition capability *"blocked: the composition is prose, not a script"*. **False as measured**: `governance_fingerprint.py compose --all` exits 0 and emits all four role fingerprints, and `CLAUDE.md` § 3 advertises it. Because I.4 binds Orchestrator to assign on `VERIFIED` capabilities, a row declaring a capability structurally impossible suppresses the L2 smoke that would verify it — the defect is self-perpetuating. |
| **MINOR-1** | Claims Plan *"maintain[s] … the role-specific `ACTIVE_LESSONS` subsets within budget"*. Annex E.5 gives Plan the **budget** and Mirror the **subset** (*"ricomposizione subset (Mirror, via G.2 se materiale)"*); G.2 presupposes selection is Mirror's; `roles/mirror.md` states the split correctly. Two contracts use the same verb on the same object. Aggravated by **Annex H.1's `Lifecycle learning` row, whose Authority column is literally `—`** — the only unassigned row in the matrix. |
| INFO | Negative controls clean: worktree matches I.2 step 4 · fingerprint set matches P2.2 exactly · byte-identical across all 19 refs · epistemic boundary matches §28 and H.1. |

### `roles/orchestrator.md` — **CHANGES_REQUIRED** *(C.2: WEAKENED)*

| Sev | Finding |
|---|---|
| **MAJOR-2** | Four clauses lock: frontmatter `worktree: the repository root checkout` · *"must not: commit its own work"* · *"nor treat the root as free working space"* · *"Session Learning Review … persisted by `WORK_COMMIT`"*. D.1/§11 make `WORK_COMMIT` obligatory on the actor's **own** branch; §8 makes the SLR mandatory. **The contract names one surface, forbids working in it, forbids the commit, then requires it, and declares no branch of its own.** The body is not the source: §35.1's prohibition is disambiguated by GATE 1 as *canonical* commit of own work; the contract drops that disambiguation. An `orchestrator` worktree and branch exist in the runtime, and `refs/heads/orchestrator-surface` carries a repair (`24663eec…`) — **on neither ref under review.** |
| **MINOR-2** | Authority premise rests on `runtime/agent_card_registry.md`: one ref only, dated 2026-08-17, records *"no lease exists"* (now stale — 9 lease records), records the MAJOR-2 stale worktree value, and records every capability `UNVERIFIED`. Its `ROLE_CONTRACT_HASH e1155911…` **verified matching** by recomputation. |
| INFO | Lease **derived, not read**, per the record's own instruction: **0 `ACTIVE` on both lease-bearing refs**; lease #3 `DISAGREEMENT` (stored `EXPIRED`, derived `STALE`; `EXPIRED` is outside I.3's vocabulary) and `EXPIRED_WITHOUT_RENEWAL`. Negative controls clean: D.4 + J.3 both resolve with the E4 clause · F.4 · I.3 · §9.4 · J.2 · fingerprint set matches P2.2 including the J.4 rationale. |

### `roles/scientist.md` — **CHANGES_REQUIRED** *(C.2: WEAKENED)* — anchored on `main`'s `fd30134d…`

| Sev | Finding |
|---|---|
| **MAJOR-3** | Contract: `scientist_reading_modes.md` *"binds every actor under this contract."* That protocol's own frontmatter on the same ref: *"status: PROPOSED … **Until then it binds nobody.**"* Complication measured: `4454fea` — an ancestor of `main` HEAD, titled *"The Scientist A/B specification becomes canonical"* — is the commit that **installed the protocol**, so its stated condition was satisfied by the commit that wrote the line, which was never updated. Downstream: `scientist-a`/`scientist-b` identities are declared `FIXED` **by a document that declares itself binding on nobody**. Direction of resolution is a governance question; **not answered here**. |
| **MINOR-3** | All three Scientist worktrees (`lettore`, `lettore-b`, `lettore-c`) sit on refs carrying the **superseded** blob, which lacks `actor_id_status` and the whole reading-modes section. An actor rehydrating per §36.5 from its own worktree reads a contract that does not know its identity is fixed. |
| INFO | **Suspected dangling reference — tested and NOT found**: the link landed at `384f05f` and blob `e6e2b472…` was already present there. Negative controls clean: worktrees match I.2 step 4 · I.2-step-7 deviation is real, declared **and ratified** as `PID-09` · fingerprint set matches P2.2 · J.4 exclusion reproduces A.6's worked example. |

### `roles/mirror.md` — **SELF_REVIEW_OBSERVATION** *(no verdict, no eligibility assigned)*

- **Observable:** byte-identical on all 19 refs · fingerprint set matches P2.2 · `ROLE_CONTRACT_HASH`
  recomputed · **its declared blocker is TRUE** — the J.1 event ledger has no instance and no writer
  across all 41 refs, which is the control that separates it from MAJOR-1 · therefore the entire
  "Analysis surface" section and both metrics it claims as Mirror's responsibility are **dependent on
  a missing object** (checkpoint proxy covers 2 of 6 actors) · a finding already stands against me in
  `L2-OUTCOME-MIRROR-001` (M1: *CRITERION MET · FORMAT NOT UNIFORM*) · `CHK-mirror-0007/0008` record a
  fingerprint (`3dff8954…`) that is the reviewed work's `BASE_HEAD` value, matching neither this
  worktree nor `main` — A.6 admits both readings and **I do not rule**.
- **Requires independent review:** whether the self-review bar's scope (rubric/clustering/selection/
  yield/autonomy) deliberately excludes perimeter, analysis surface and metrics — all of which I just
  reviewed · **whether the G.2 correction route is executable at all**, given 0 `ACTIVE` leases (no
  Orchestrator to choose a reviewer) and 0 `VERIFIED` capabilities anywhere (no qualified reviewer) ·
  the fingerprint practice above · whether MAJOR-1's pattern recurs in clauses I did not probe.
- **Why no self-certification:** H.1 — *"Modifica rubrica/metodi di Mirror | mai Mirror da solo
  (G.2)"*. And C.2's `CONFIRMED` means only *"no defect found given the available evidence bundle"*;
  issued by the author of the bundle it carries no independence, therefore no information.

---

## DISPATCH_CONTAMINATION

Six terms carry **no repository source**, confirmed across all 41 content refs:
`HUMAN_GATE` · `DISPATCH_CORRECTION` · `BLOCKED_DISPATCH` · `DISPATCH_CONTAMINATION` ·
`SELF_REVIEW_OBSERVATION` · `TERMINATED`.

🔴 **The prescribed verdict vocabulary is also external.** `{COMPLIANT, CHANGES_REQUIRED,
BLOCKED_WITH_REASON}` appears nowhere in the governance. Annex C.2 is FROZEN, prescribes
`{CONFIRMED, WEAKENED, REFINED, REFUTED}`, and marks `STEELMAN` and `WHAT_WOULD_CHANGE_MY_MIND`
*obbligatorio* — and `roles/mirror.md` binds me to *"the single format of Annex C.2"*. Both
vocabularies are emitted in the review. **A dispatch asking Mirror to review under a non-C.2 format
is asking Mirror to depart from the contract under review.** Recorded, not resolved.

Concepts that **did** validate: role contract *(normative — I.1, I.4, A.6)* · hostile review
*(normative — C.2, §12 GATE 3, §29)* · `G.2` *(normative, FROZEN)* · `status: PROPOSED` and the
binding sentence *(observational — self-declared frontmatter)*.

---

## ACTIVATION — the question this handoff exists to transmit

| Condition (as the contracts state it) | Evidence | State |
|---|---|---|
| Mirror hostile review passes | `REV-GOV311-MIRROR-003` `PASS_WITH_NOTES` @ `84407c1`, bound to `c39ecae8…`; provenance corrected by `COR-20260816-GOV311-001` | SATISFIED for `CAND-20260816-GOV311` |
| The operator approves | `RES-20260816-GOV311-001` `APPROVED`, bound to `c39ecae8…` @ `749a9a9b…` | SATISFIED for that candidate |
| Contracts canonically installed | `a8cd125`, ancestor of `main` | SATISFIED |
| `status:` line reflects any of it | `git log --all -S` over `roles/` → **only the materialization commit** | ❌ **NEVER MODIFIED** |

🔴 **Both named conditions appear satisfied; all four contracts still advertise `PROPOSED`.**
Either activation occurred and four canonical objects carry a stale status line, or it was never
recorded on the objects it governs. **Not resolved here** — H.1 assigns governance to the operator,
and an actor choosing the reading that makes its own contract binding would be the convenient
interpretation the gate exists to prevent.

Supporting facts: GATE 0's lease precondition was ruled `NOT_YET_APPLICABLE` **for the installation
commit only** and explicitly not generalised · **0 `ACTIVE` leases** at review time · **0 `VERIFIED`
capabilities in any actor of any role** · two Scientists recorded unregistered as of 2026-08-17 while
`main`'s contract declares their identities `FIXED`.

**Correctness and activation are independent:** MAJOR-1/2/3 are not cured by ratification, and
ratifying the contracts as they stand would canonicalize all three.

---

## OPEN QUESTIONS — transmitted, not answered

1. Do the four contracts bind today? (§ ACTIVATION.)
2. Does `scientist_reading_modes.md` bind — its status line, or the commit that satisfied its
   condition?
3. Which ref is the surface of record for `roles/`? `mirror` and `main` disagree on
   `roles/scientist.md` and on **every** role fingerprint.
4. `MIRROR_RETROSPECTIVE` cadence `N` — `UNRESOLVED`, carried forward by explicit operator decision
   (`ESC-3`). **Left unresolved, as instructed.**
5. Who executes G.2's *"independent reviewer chosen by Orchestrator"* with 0 `ACTIVE` leases and
   0 `VERIFIED` capabilities?
6. Should H.1's `Lifecycle learning` row carry an authority, given `plan.md` and `mirror.md` both
   claim the `ACTIVE_LESSONS` subsets?
7. Conflict `C-7` — session `legend-public-12 [cf79f1]`, interactive, open since 2026-08-16, claimed
   by no registered actor — appears never closed. It bears on `ONE_WRITER` (GATE 0).
8. Is a J.1 event-ledger writer to be scheduled? Four clauses across two contracts are unenforceable
   without one, and the lease record itself names `LEASE_ACQUIRED`/`LEASE_STALE` as the closure for
   its own unwatched-window failure.

---

## PROCESS_STATUS

```
PROCESS_STATUS     WAITING_EXTERNAL_DECISION
NEXT_OWNER         operator
NEXT_TRANSITION    HUMAN_GATE   (external vocabulary — see next_transition_note)
```

**Nothing is ratified. No contract text is proposed. No governance change is recommended. No DEC
record, no HUMAN_APPROVAL record, no ownership assignment, no cadence resolution.** `main` was
observed and not moved.
