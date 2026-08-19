---
artifact: INTEGRATION_CANDIDATE — cross-session transport discipline
candidate_id: CAND-20260819-XPORT
revision: 2
task_id: XPORT-ROUTING-001
author: plan
authored_on: 2026-08-19
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move the hash it records
partition: SPLIT — Candidate A (this one) is TRANSPORT. Candidate B (ROUTING) is NOT opened, and
  §10 states the three preconditions that block it, none of which Plan may satisfy alone
human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists
revision_2: remediates M-1 of REV-XPORT-MIRROR-001, the single blocking finding. The remedy is in
  CONTENT — the protocol's own frontmatter and §11, plus a new §11.1 carrying the property, its
  three permitted name classes and the semantic falsifier. §15 records the disposition of every
  finding. No transport rule changed; routing not reopened; T-TRANSPORT-1 still NOT_RUN
supersedes: revision 1, CANDIDATE_CONTENT_HASH 68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
  at content tip f48a807f7ba7b5b71c0ba5dd5d2361fc7dca57e4. That binding is SUPERSEDED, not
  withdrawn — it was correct for the tree it named, and Annex D.2 invalidates it because the
  content moved
---

# INTEGRATION_CANDIDATE — `CAND-20260819-XPORT`

## 1 · Manifest (Annex D.2)

```
CANDIDATE_ID              CAND-20260819-XPORT
BASE_HEAD                 4454feab72b7a0edf65f191be62aeedd899a15ad   (canonical main, verified
                                                                      unchanged at session open
                                                                      and again at binding)
SOURCE_COMMITS            f48a807f7ba7b5b71c0ba5dd5d2361fc7dca57e4   CONTENT — revision 1
                          e839db38382781564a9767fe206eefd5fba0467c   CONTENT — revision 2, the
                                                                      M-1 remediation + SLR-plan-0008
                          <this commit>                              CONTROL PLANE — manifest,
                                                                      author response, checkpoint,
                                                                      task record
CONTENT_TIP               e839db38382781564a9767fe206eefd5fba0467c
CANDIDATE_HASH_VERSION    legend-candidate-v4
CANDIDATE_CONTENT_HASH    81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f
                          532 included · 38 excluded
SUPERSEDED_HASH           68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
                          revision 1, at content tip f48a807 — correct for its tree, invalidated
                          by the content change (Annex D.2 binding rule)
CHANGE_CLASS              MAJOR — it introduces a normative protocol that binds every actor
                          (Annex G.1: protocols/governance ⇒ MIRROR_REQUIRED; body §12)
LINT_RESULT               PASS — 1 pre-existing INFO
PUBLICATION_GATE          PASS / BLOCKS: 0
MIRROR_REVIEW             REV-XPORT-MIRROR-001 — REQUEST CHANGES on M-1, CONFIRMED on every other
                          axis. M-1 remediated in CONTENT at this revision (§15). Revision 2 has
                          NOT been reviewed; a second Mirror review is required and not assumed
HUMAN_APPROVAL            n/a — not requested, not prefilled
SNAPSHOT_ID               n/a until canonical execution — GATE 4 belongs to Orchestrator
```

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
    --base 4454feab72b7a0edf65f191be62aeedd899a15ad \
    --tip  e839db38382781564a9767fe206eefd5fba0467c
```

**Reproduced six ways before being written down**, at revision 2. Two runs of the governed script
— one in the `evidence-index` worktree, one in a clean detached worktree at the content tip —
identical. One independent route that does not use the script: `git ls-tree -r --full-tree` read
as raw bytes through an argv list and never through a shell, path-sorted, every entry
newline-terminated per P5.2, control-plane roots applied as prefixes. It returns `532 / 38` and
the same digest, so the count is reproduced as well as the hash.

**Two positive controls.** The published `beef6db08bdf…` of `CAND-20260818-SCIENTIST-AB-SPEC`
reproduces exactly at its own base and tip; and **revision 1's own `68173f01…c96a` reproduces
exactly at `f48a807`**, which is the control that matters here — it shows the recipe is unchanged
and that the digest moved because the *content* moved, not because the instrument did.

**Three negative controls, with their independence verified first.** The revision-2 tip against
`main^` (`cbce3016`) returns `bf3b9092…`; against `main^^` (`f5b32155`) returns `49a32274…`; and
`main^` and `main^^` were compared and confirmed **distinct commits before** their disagreement
was read as evidence — the void-control failure recorded in `SLR-mirror-0015` L-4, avoided by
checking rather than by luck. The correct base against the *revision-1* tip returns
`68173f01…c96a`, so tip and base are both genuinely inside the hash.

**The control-plane commit is expected to leave the hash unchanged**, because everything in it is
under `governance/candidates/`, `reviews/` or `ledger/`. §12 re-derives the hash at the manifest
tip and states the result rather than assuming it.

---

## 2 · Problem statement

Two failures were observed in this laboratory, and only one of them is this candidate's.

**The transport failure.** Authoritative content — task contracts, reviews, approvals, benchmark
specifications, scientific results — has no rule stating where it must live. Body §21 says
*"messaggi = pointer, stato durevole decide"* and Annex B.1 carries a `DURABLE_POINTER` field, but
nothing says the pointer is **mandatory** for authoritative content, and nothing says what happens
when a payload rides in the message body instead. The runtime makes this concrete: one field of
the message tool declares a bound it enforces and another declares a bound it does not, with
nothing in the declaration distinguishing them (design record §8.1). A payload whose completeness
the recipient cannot establish is not evidence.

**The routing failure.** There is no mechanism that answers *which live session is `plan` right
now*. Design record §6 measures the consequence: eight live sessions in the Plan worktree, seven
in Mirror's, and the Agent Card registry's recorded current session for `plan` is alive, three
days old, and is not the current one. **This candidate does not fix that**, and §9 of the protocol
says so in the text rather than leaving it to be discovered.

---

## 3 · File list and classification

| path | change | domain | class |
|---|---|---|---|
| `framework/protocols/cross_session_transport.md` | **added**, then **amended at revision 2** | CONTENT — hashed | **NORMATIVE** — the protocol |
| `framework/protocols/index.md` | modified — one row | CONTENT — hashed | navigational |
| `governance/design_records/runtime_harness_probe_20260819.md` | **added** | CONTENT — hashed | **NON-NORMATIVE** — provenance, binds nobody (`design_records/README.md`) |
| `learning/plan/SLR-plan-0007.md` | **added** | CONTENT — hashed (P5.1: `learning/` is CONTENT by intent) | Session Learning Record, E.6 |
| `learning/plan/SLR-plan-0006-COR-001.md` | **added** | CONTENT — hashed | correction record, appended never edited |
| `learning/plan/SLR-plan-0008.md` | **added at revision 2** | CONTENT — hashed | Session Learning Record, E.6 — the remediation session |
| `governance/candidates/CAND-20260819-XPORT.md` | **added** | CONTROL PLANE | this manifest |
| `reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md` | **added** | CONTROL PLANE | the owed author response, SCIAB |
| `reviews/plan/AUTHOR-RESPONSE-XPORT-MIRROR-001.md` | **added at revision 2** | CONTROL PLANE | the owed author response, Annex C.2 |
| `governance/candidates/HANDOFF-XPORT-MIRROR.md` | **added**, re-issued at revision 2 | CONTROL PLANE | the Mirror review package |
| `ledger/checkpoints/plan/CHK-plan-0017.json` | **added** | CONTROL PLANE | Annex A.6 checkpoint |
| `ledger/tasks/plan/XPORT-ROUTING-001.json` | **added** | CONTROL PLANE | task record |

**Revision 2 touches exactly two CONTENT paths**: the protocol, in three places, and one new
Session Learning Record.

```bash
git diff --name-only c748d27 e839db3          # prior tip → revision-2 content tip
# → framework/protocols/cross_session_transport.md
#   learning/plan/SLR-plan-0008.md
```

🔴 **The check that first suggested itself was wrong, and is recorded rather than replaced
silently.** `git diff --name-only f48a807 e839db3` returns **seven** paths, not two, because the
three control-plane commits of revision 1 sit inside that range. Diffing the two *content* tips
across an interval containing control-plane commits does not isolate content; either diff from the
immediately prior tip, as above, or filter the declared `CONTROL_PLANE_ROOTS` out of the range
diff — both return the same two paths. The error was caught by running the command before the
sentence claiming its output was allowed to stand.

**Nothing scientific is touched.** The four current files, the state manifest, every registry and
the receipt ledger are unmodified. No role contract is edited, so **no role fingerprint moves and
no in-flight checkpoint is invalidated** — a deliberate scoping choice, see §11.

---

## 4 · Evidence, re-run at revision 2 in a clean detached worktree at the content tip

Not inherited from revision 1 and not inherited from the review. Every value below was produced
this session at `e839db38`, in a detached worktree created for the purpose, never in root.

```
LINT                    PASS — 1 pre-existing INFO (CLAIM 010 wikilink, background only)
PUBLICATION GATE        PASS / BLOCKS: 0 — 4 [REVIEW] lines, all pre-existing
GROWTH ANCHORS          PASS — claims 39 · papers 70 · corpus 356 · literature 390
                        registry_only 15 · unread_premises 4
RECEIPT LEDGER          OK — 128 chained receipts, tail anchored in the state manifest
GOVERNANCE FINGERPRINTS recomputed at BOTH trees and compared —
                        scientist 82423a48b700bc… · plan 9c0c13fb2cba98…
                        mirror 3dff8954d4f6a5…   · orchestrator e2c544705e623a…
                        IDENTICAL at BASE_HEAD and at the revision-2 content tip, which is the
                        measured form of the claim in §3 that no role contract is touched and
                        therefore no in-flight checkpoint is invalidated
```

Every one of these reproduces revision 1's published value exactly, which is the expected result
of a change confined to one protocol and one learning record — stated here as a measurement, not
as an expectation that was assumed.

### 4.1 · Release regressions — measured SET-WISE and NAME-WISE at both trees

Two clean detached worktrees, one at `BASE_HEAD` and one at the revision-2 content tip. **No
`timeout` wrapper** — `timeout` does not exist on this platform, and wrapping a run in a missing
binary returns exit 0 having executed nothing (`SLR-mirror-0015` L-4). The verdict below was read
out of the output, never off an exit code.

```
                                    BASE_HEAD 4454feab      REVISION 2 e839db38
                                    (detached worktree)     (detached worktree)
suites RUN                          65                      65
tests executed                      953                     953
suites failing                      6                       6
individual tests failing            7                       7

set difference of failing suites:   EMPTY both directions  →  DELTA 0
set difference of failing tests:    EMPTY both directions  →  DELTA 0
suites-run list identical:          TRUE
```

The six failing suites are identical at both trees, name for name:

```
scripts/test_release_runner_verdict.py
scripts/test_locator_obligation_reaches_every_route.py
scripts/test_abstract_corpus_is_not_evidence.py
scripts/test_release_surface.py
scripts/test_fulltext_trace_contract.py
framework/scripts/test_session_self_eval.py
```

**And one level deeper — the seven individual failing tests, identical at both trees:**

```
framework/scripts/test_session_self_eval.py :: SelfEvalGate.test_diagnosis_is_wired_before_growth_and_takeaways
scripts/test_abstract_corpus_is_not_evidence.py :: InstructionSurfacesCarryTheDistinction.test_the_bootstrap_bounds_the_corpus
scripts/test_fulltext_trace_contract.py :: FulltextTraceContractTests.test_normative_layers_make_receipts_universal
scripts/test_fulltext_trace_contract.py :: FulltextTraceContractTests.test_normative_write_rules_name_the_append_only_carveout
scripts/test_locator_obligation_reaches_every_route.py :: ObligationReachesEveryRoute.test_the_bootstrap_states_the_rule
scripts/test_release_runner_verdict.py :: EveryTestSuiteIsActuallyRun.test_every_tracked_test_file_is_in_the_runner
scripts/test_release_surface.py :: ReleaseSurfaceTests.test_shebang_python_entrypoints_are_executable
```

**They are pre-existing and this candidate neither causes nor repairs them.** `ADDED: none`,
`REMOVED: none`, at both granularities. The comparison is set-wise because two runs with equal
failure *counts* over different failures would pass a count check and fail this one — and it is
then repeated at test-name level because a suite that fails for a new reason at an unchanged
count would pass even the suite-level set check. Root was never written, cleaned or read
destructively, so no environmental state of the workstation enters the comparison.

---

## 5 · What the protocol asserts, and in what vocabulary

The protocol's own §5 and §8 carry the `GUARANTEE_PROVIDED` / `FAILURE_MODE_STILL_POSSIBLE` /
`DETECTION` / `RECOVERY` blocks in full. Two properties of those blocks are the ones worth a
reviewer's first attack:

1. **`ENFORCEMENT MODE: PROCEDURAL`, stated as such.** No validator runs at send time, no hook was
   demonstrated to fire (Phase −1 `E2`, `INCONCLUSIVE`, cause not established), and nothing runs
   between turns. The protocol says this in the block rather than in a footnote.
2. **`DETECTION: NONE — ATTENTION_ONLY` on term 5** of the handoff conjunction. *"The recipient
   read the durable object"* has no detector. Five of the six terms leave durable artifacts and
   the sixth does not, and the protocol names which.

**Annex J.0 compliance.** No mechanism in this candidate is described in stronger vocabulary than
its compensating protocol. Specifically: nothing here is called atomic, guaranteed, enforced, or
exactly-once.

---

## 6 · Harness capability inventory, and the version binding

The full inventory is `governance/design_records/runtime_harness_probe_20260819.md`, performed
**once** so two candidates cannot drift by measuring it twice. Summarised:

```
INSTALLED CLAUDE CODE VERSION   NOT A SCALAR — 4 extension versions installed; ≥2 hosting live
                                sessions concurrently; the CLI on PATH reports a third binary
                                that hosts nothing. VERSION_OBSERVED is per SESSION.
                                This session: 2.1.232, pid 49611.
MESSAGE PRIMITIVE               SendMessage (tool) — to / message / summary. DEFERRED in this
                                interactive session: a ToolSearch preceded the first call.
DISCOVERY PRIMITIVES            TWO, returning different sets:
                                  ListAgents (tool)          18 rows, SELF EXCLUDED
                                  claude agents --json (CLI) 19 rows, SELF INCLUDED, with
                                                             sessionId · cwd · pid; --all adds
                                                             dead rows and job ids
SESSION IDENTIFIER FORMS        SESSION_ID (UUID, stable) · SESSION_NAME (<cwd>-<2hex>, the
                                address) · LISTAGENTS_REF (6 hex) · JOB_ID (8 hex) ·
                                ROUTING_TRANSPORT (uds socket, dies with the process)
SESSION_REF                     🔴 OBSERVABLE — self-observable through the CLI at 2.1.232
SESSION NAME SEMANTICS          CONVENIENCE RESOLVER. Per-session, launcher-assigned, not derivable
                                from SESSION_ID, and MEASURED_EARLIER as not stable across a
                                restart of the same session (KERNEL_SPEC OB-4)
DELIVERY RESULT SEMANTICS       structured; REJECTED_TOO_LARGE and TARGET_UNRESOLVED observed
DISCOVERY COMPLETENESS          PARTIAL / UNKNOWN — locally cross-checkable against the socket
                                directory; no completeness signal on either surface
RESUME / FORK                   MEASURED_EARLIER: `--resume --bg` FORKS with a success-shaped
                                exit; `respawn <job id>` preserves the session
```

**The revalidation rule.** Protocol §3: `OBSERVED → VERSION_CHANGED → REVALIDATION_REQUIRED`, with
the version taken from the acting session's own process image or transcript, never from a
machine-level version string. A guarantee that fails revalidation is **unmeasured**, not false —
the same shape as an Annex A.6 checkpoint whose fingerprint moved.

---

## 7 · 🔴 Three durable artifacts rest on a premise this probe falsified

| artifact | states | status |
|---|---|---|
| `framework/protocols/scientist_reading_modes.md` §1.2 — **CANONICAL** | *"No actor observes its own SESSION_REF. `ListAgents` shows peers only."* | the reason is false at 2.1.232 through the CLI |
| `runtime/agent_card_registry.md` (branch `orchestrator`) | derives four refs by set complement, *"no actor can observe its own routing reference"* | the derivation was sound; it is no longer necessary |
| `runtime/orchestrator_lease.md` lease #7 (branch `orchestrator`) | `SESSION_REF: NOT DECLARED` — *"An actor cannot observe its own routing reference"* | same |
| `framework/protocols/actor_identity_feasibility.md` `E5` | *"Not obtainable: `session_ref` … The field is dropped from the schema"* | the instrument was `ListAgents`; a second instrument was not tried |
| `framework/protocols/actor_identity_proposal.md` §6 | excludes a `session_ref` field because *"a session cannot learn its own name"* | rests on `E5` |

**This candidate edits none of them.** Three are canonical or durable runtime records, one is a
frozen feasibility report, and correcting a canonical sentence is a governed change that belongs
to the candidate that needs it — which is Routing, not Transport.

**What is and is not overturned.** A *stated ground* is wrong. The *positions* are right and this
candidate keeps them: `ACTOR_ID` is not `SESSION_REF`; a session reference is ephemeral; no actor
invents one; nothing durable is keyed by one. Protocol §9 restates the refusals and adds none of
the permissions that self-observability might seem to license — because observing your own address
tells you where you are, and says nothing about whether you are the actor's current incarnation.

---

## 8 · Routing analysis — performed, reported, and NOT bound into this candidate

Everything in §8–§10 is **manifest-resident**: it is control plane, it moves no hash, and it is
here so that Mirror can attack the partition decision and not only its product.

### 8.1 · `ACTOR_ID` vs `SESSION_REF`, and the three states that are not one

```
ACTOR_ID      STABLE GOVERNED IDENTITY — permanent; identity, provenance, learning attribution
SESSION_REF   VOLATILE RUNTIME ADDRESS  — one incarnation; new after every restart
SESSION_NAME  RUNTIME RESOLVER          — convenience only; measured unstable across restarts
```

```
IDENTITY_VERIFIED   !=   CURRENT   !=   ROUTABLE   !=   AUTHORIZED_TO_SUPERSEDE
```

This session is the worked example: identity fully rehydrated from durable state, and **not
routable**, because nothing anywhere records that this incarnation is `plan`'s current one — while
seven other live sessions sit in the same worktree and one of them is the registry's recorded
current.

### 8.2 · Where routing state should live — anti-ontology, four existing surfaces considered

| existing surface | sufficient? | why |
|---|---|---|
| `runtime/agent_card_registry.md` (Annex I.4) | **INSUFFICIENT alone, and it already has the field** | `CURRENT_SESSION_REF` is already in the card. What is missing is not a field but a *transition owner*, a cardinality check and a detector. It is also single-writer, untracked-class (`runtime/` is P5.1's open question), and readable by one actor — conflict `C-5b` |
| `PROPOSAL-C9-STATE-MODEL` §7.2 | **DIRECTLY ON POINT — and ON HOLD** | it already assigns `CURRENT_SESSION_REF / SESSION_ID / liveness / LAST_SEEN` to the untracked local cell. `acceptance_is_not_adoption: true`; *"no implementation and no governance modification until that review completes"* |
| `framework/protocols/actor_identity_proposal.md` + `actors.yaml` | **ON HOLD, and one premise falsified** | `BUILD_MINIMAL_DIRECTORY` is provisional *pending operator acceptance*; `framework/state/actors.yaml` **does not exist** — Phase 0 was never executed; §6's exclusion of a `session_ref` field rests on `E5` (§7 above) |
| `launch/legend_launch.sh` lineage store | **partially sufficient, and out of the repository** | it already enforces one canonical session lineage per `(actor_id, runtime_instance)` with an `O_EXCL` reservation written *before* the spawn. But the store is `$HOME/.legend/lineage/…` — per-machine, unversioned, invisible to git, and therefore not auditable from the repository |

```
NEW SURFACE REQUIRED:   NO — probably. Three of the four are extendable and the fourth is a
                        real CAS primitive. What is required is a DECISION about which, and
                        three of the four are held by decisions that are not Plan's.
MINIMAL DELTA           a transition owner + a cardinality check + a detector, on ONE of the
                        surfaces above. Not a new ontology.
```

### 8.3 · Activation authority — three models compared, C treated as a hypothesis and attacked

| | **A · registrar-only** | **B · self-registration / self-activation** | **C · provisional → registrar-confirmed** |
|---|---|---|---|
| autonomy | low — every respawn waits | **highest** | medium |
| single-point dependency | **total** on the registrar | none | on the registrar, for *confirmation* only |
| authority consistency | consistent with H.1 (Orchestrator commands) | 🔴 **inconsistent** — an actor granting itself routing authority is self-promotion, which body §9.4 and Annex I.2 both forbid by name | consistent — the actor proves, the registrar decides |
| race behaviour | serialized by the registrar, which is itself unserialized | **`O_EXCL` gives a genuine CAS** per `(actor, cell)` — this is the model the harness supports best | inherits A's race on the confirmation step |
| recovery | registrar down ⇒ nothing activates | actor recovers alone | registrar down ⇒ actor sits `PROVISIONAL`, which is body §9.4 `ORPHAN` — an already-defined, already-accepted state |
| auditability | registrar's record, one writer | 🔴 out-of-repo lineage store; **nothing in git** | two seats, both durable, both in git — the shape already canonical in `scientist_reading_modes.md` §1.3 |
| harness support | discovery + naming only | **strongest** — self-observation (new) + `O_EXCL` + `--name` at launch | uses the same primitives; needs no new one |
| operator burden | high | lowest | low |
| registrar respawn | 🔴 **circular** | n/a | resolved by §8.5 — the lease is the registrar's own confirmation event |

**Falsification attempts on C, and what survived.**

1. *C is circular at the registrar.* → **Answered, not by a new mechanism**: for `orchestrator`
   the confirmation event is `ORCHESTRATOR_LEASE` acquisition under I.3, which already has a
   governed succession. §8.5.
2. *C needs a new lifecycle state.* → **It does not.** `PROVISIONAL / NON_ROUTABLE` maps onto
   Annex J.2's existing `BOOTSTRAPPING`, which is precisely *"exists, not yet operating"*. No new
   state machine, which matters for §9's generality test.
3. *C fails when the registrar is down.* → It stalls, into `LAB_STATE = ORPHAN` (body §9.4), where
   nobody self-promotes and work parks. That is the constitution's designed behaviour, not a
   defect introduced by C.

```
RECOMMENDED MODEL     C — provisional → registrar-confirmed, with PROVISIONAL ≡ J.2 BOOTSTRAPPING
REJECTED              A — a registrar that cannot activate itself is not a model, it is half of one
                      B — mechanically the best supported and constitutionally impossible: it is
                          self-promotion, which I.2 and §9.4 forbid by name. Its CAS primitive is
                          worth keeping; its authority story is not
RECOMMENDED AS        a DIRECTION for Candidate B to argue, not a decision taken here. Plan does
                      not hold the authority to settle activation authority — H.1 puts governance
                      with the operator — and §10's holds are exactly this point
```

### 8.4 · Resolution enforcement mode, cardinality, and generation

```
RESOLUTION ENFORCEMENT MODE   PROCEDURAL, today and in this candidate
RESOLUTION TOOL               NONE. No resolver exists.
```

A `resolve_actor.py` — deriving effective routing state from underlying records rather than
trusting a stored `STATUS`, the way `lease_state.py` already does for the lease — is the obvious
target and is **deliberately not implemented here**, because implementing a resolver is Candidate
B's content and because a tool named in a prompt is not thereby authorized.

```
ONE-CURRENT INVARIANT   target: for each ACTOR_ID, CURRENT_ROUTABLE_COUNT ∈ {0,1}
                        today:  ADVISORY. There is no detector, because there is no record to
                                count. >1 is never a valid steady state, and today the laboratory
                                cannot tell that it is in one — measured: 8 live plan sessions
ZERO-CURRENT            FAIL_CLOSED — bound now by protocol §9, since a refusal needs no mechanism
MULTIPLE-CURRENT        FAIL_CLOSED — same
ROUTING GENERATION      READY as a design, NOT BUILT. A monotonic, registrar-authorized
                        ROUTING_GENERATION is the right instrument precisely because a newer
                        timestamp has no authority: generation 42 is CURRENT because an
                        authorized transition made it so, not because it is later
SUPERSESSION            ADVISORY. A superseded session that a human resumes will run.
                        DETECTION: NONE — ATTENTION_ONLY, until a bootstrap guard exists
OLD-SESSION REVIVAL     ADVISORY, same. Historical identity stays correct; routing authority is
                        a separate fact that today nothing records
LIVENESS                DETERMINABLE LOCALLY (pid present and resolvable), UNDETERMINABLE in
                        general. And ROUTABILITY != LIVENESS: `CURRENT: S17 / LIVENESS: UNKNOWN`
                        is a legitimate state, and a delivery failure may trigger re-resolution
                        but MUST NOT autonomously elect another historical session
```

### 8.5 · Registrar self-reference and the `ORCHESTRATOR_LEASE`

```
OUTCOME:  B — EXPLICITLY_RELATED.  Not unified, not separate.
```

Two mechanisms would otherwise answer *"who is Orchestrator now"*. §18's rule is that they may
never both exist without a consistency rule, and the honest split is by **question**:

```
THE LEASE     authoritative for  "who may execute a CANONICAL_BATCH_COMMIT"  — Annex I.3, singleton
ROUTING       authoritative for  "where a message to `orchestrator` goes"
CONSISTENCY   the routing-current Orchestrator incarnation MUST be the one named in the ACTIVE
              lease's SESSION_REF field. On disagreement, NEITHER is used: routing blocks, and
              the batch does not run. Fail closed on both sides.
```

**The lease already has the field, and it is empty.** Lease #7 records `SESSION_REF: NOT DECLARED`
*because the actor could not observe it* — and §7 shows it now can. Filling that field is a small,
cheap, high-value change and it is Orchestrator's to make in its own record, not Plan's.

Behaviour under the five cases §18 requires:

| case | behaviour under B |
|---|---|
| Orchestrator session dies while lease `ACTIVE` | lease derives `ACTIVE` until `EXPIRES_AT`; routing target is dead. **Detected** by the consistency rule at the next send or `GATE 0`; the lease expires to `STALE` on its own clock |
| fresh Orchestrator session appears | it is `PROVISIONAL`; it does not become routable by existing. It acquires routing by acquiring the lease |
| lease becomes `STALE` | Orchestrator has no routing-authoritative incarnation. `LAB_STATE = ORPHAN` (§9.4). Nobody self-promotes |
| lease reacquired | acquisition is the confirmation event; the new incarnation's `SESSION_REF` is written into the new lease record, which is the succession I.3 already requires |
| old Orchestrator chat resumes | historical identity intact, routing authority absent. It may read; it may not be the target of actor-routed work, and it may not batch — the lease it held is `RELEASED` |

**No second singleton is built.** That is the point: I.3's lease is reused as the Orchestrator's
routing transition, because building a second independent singleton for the same actor is exactly
what §18 forbids.

🔴 **And it cannot be specified today, for a reason outside routing**: the Orchestrator's worktree
is contested in canonical state (§13.A), and `--cwd` — the only mechanized scoping predicate the
harness offers — returns *three sessions* under one reading and *zero* under the other.

---

## 9 · Generality — the architecture is ACTOR-GENERIC, and the falsifier

### 9.1 · Acceptance matrix

| | `plan` | `mirror` | `scientist-a` | `scientist-b` | `scientist-c` | `scientist-d` (hypothetical) | `orchestrator` |
|---|---|---|---|---|---|---|---|
| STABLE ACTOR_ID | `plan` | `mirror` | `scientist-a` FIXED | `scientist-b` FIXED | `scientist-c` PROPOSED | `scientist-d` — would be assigned | `orchestrator` |
| ROLE | `roles/plan.md` | `roles/mirror.md` | shared `roles/scientist.md` | shared | shared | **shared, unchanged** | `roles/orchestrator.md` |
| WORKTREE SOURCE | deployment profile | deployment profile | profile + protocol §1.1 | same | same | **profile row — one line** | 🔴 **CONTESTED** — §13.A |
| FINGERPRINT SOURCE | `governance_fingerprint.py compose --role plan` | `--role mirror` | `--role scientist` | same | same | **`--role scientist` — same value, no new entry** | `--role orchestrator` |
| IDENTITY REHYDRATION | body §36.5 | §36.5 | §36.5 | §36.5 | §36.5 | **§36.5** | §36.5 |
| ACTIVATION PATH | generic (I.2 step 7) | generic | generic | generic | generic | **generic** | generic **+ lease acquisition** (§8.5) |
| CURRENT ROUTING PATH | generic resolver | generic | generic | generic | generic | **generic** | generic, constrained by lease |
| SESSION_REF RESOLUTION | resolve at send time | same | same | same | same | **same** | same |
| SUPERSESSION | generic | generic | generic | generic | generic | **generic** | via lease succession |
| TRANSPORT | this protocol | same | same | same | same | **same** | same |
| ACK | Annex B.3 + durable | same | same | same | same | **same** | same |
| SPECIAL CASE REQUIRED? | no | no | **no** | **no** | no | **no** | **YES — justified: lease, canonical execution, command authority, registrar self-reference** |

### 9.1b · 🔴 The no-hard-coding claim, corrected — the grep this manifest asks Mirror to run falsifies its first wording

Revision 1 of this section first stated that *"the transport protocol contains no occurrence of
`scientist-a`, `scientist-b`, `BENCH-AB-001`, `lettore`, or any role name."* **That is false, and
the check that found it is the one §5 of the handoff package tells Mirror to run.** Recorded here
rather than quietly rewritten, because a manifest that invites a falsification and then absorbs
the result silently has taught the reviewer nothing.

Measured, at the content tip:

```
grep -inE 'scientist-a|scientist-b|BENCH-AB-001|lettore' framework/protocols/cross_session_transport.md
  → 2 lines: 281, 366
grep -inE '…|\bplan\b|\bmirror\b|orchestrator'           (adding the role names)
  → 8 lines: 5, 30, 281, 346, 365, 366, 367, 389
```

**The corrected claim, which is the one that was meant and the one that matters:**

> **No rule, no branch and no obligation in the transport protocol is conditioned on any actor,
> role, worktree or benchmark.** Every one of the eight occurrences is a *citation* or a
> *measurement*, and each can be checked to be so:

| line | occurrence | what it is |
|---|---|---|
| 5 | *"binding once Mirror hostile review passes"* | front-matter status, the standard formula on every PROPOSED artifact in this repository |
| 30 | *"`roles/plan.md` already says…"* | a citation of prior art, establishing that the rule is not new |
| 281 | *"the name `scientist-a` still resolving under `--all` to a job"* | **a measurement** — the observed example of a name outliving its session. It illustrates the rule; the rule is *require a live pid*, which names nobody |
| 346 | *"visible to Plan at reconciliation and to Mirror on the ledger"* | a `DETECTION` row naming who holds an existing constitutional duty — body §43 and Annex G.3, not a transport rule |
| 365–367 | *"`plan` has 8 … `mirror` has 7 … `scientist-a` and `scientist-b` have 0"* | **a measurement**, cited to establish that term 3 of §8 cannot be satisfied today |
| 389 | *"blocked on preconditions Plan may not satisfy alone"* | a statement about authority, not a protocol clause |

**The falsifier a reviewer should use instead**, because it tests the property that was meant:
delete every actor name from the protocol and ask whether any normative sentence changes meaning.
None does — §1.1's list of authoritative content, §1.4's depth rule, §3's version binding, §4's
per-field table, §5's taxonomy, §8's six-term conjunction and §9's five refusals are all stated
over *any actor*. The names appear only where the protocol is quoting what was measured, and a
measurement that names its subjects is more checkable, not less general.

#### 9.1b-R2 · 🔴 This section was the wrong place to fix it, and revision 2 moves the repair

Everything above is true and stays. It was also **insufficient**, and Mirror's `M-1` is exactly
why: this manifest is under `governance/candidates/`, a declared `CONTROL_PLANE_ROOT`. It moves no
hash, it does not canonicalize, and it will not be read beside the protocol by anyone who meets
that protocol in `main` a year from now. The protocol's own frontmatter and its §11 went on
asserting that it *names* no actor, role, worktree or benchmark — **two sentences that the table
above disproves, in the artifact that canonicalizes.** The concession and the defect sat on
opposite sides of the seam.

Revision 2 repairs it in CONTENT. See §15 for the disposition and the exact edits; the corrected
property, its three permitted name classes and the semantic falsifier now live in the protocol's
new §11.1, and `T-GENERIC-1` in the protocol's §10 records the falsifier as an executed test
rather than as advice to a reviewer.

🔴 **One correction to the table above, found while remediating.** The corrected claim as written
here says every one of the eight occurrences is *"a citation or a measurement"* — **and the same
table types line 5 as front-matter status**, which is neither. Mirror's §10 reaches the same
three-way split independently, typing line 5 `FRAMEWORK RULE`. Revision 2's protocol text
therefore carries **three** classes, not two. The two-class summary is left standing here as the
record of what was written, with its own table as the disproof.

### 9.2 · The Scientist D falsifier

```
GENERALITY: PASS — with one honest qualification stated below.
```

Onboarding a hypothetical ordinary actor `scientist-d`, described using only generic machinery:

```
1  assign ACTOR_ID `scientist-d`                       an operator act, no code
2  bind role                                           roles/scientist.md, UNCHANGED. PID-09
                                                       already made the Scientist contract shared;
                                                       actor separation is carried by ACTOR_ID,
                                                       worktree, branch and task, not by text
3  assign worktree / branch                            one row in deployment_profile.md
4  bind fingerprint                                    `compose --role scientist` — the SAME value
                                                       as A, B and C. No new pertinence-set entry,
                                                       because P2.2 is keyed by ROLE, not by actor
5  fresh session identity rehydration                  body §36.5, unchanged
6  IDENTITY_VERIFIED                                   generic
7  generic activation lifecycle                        I.2 step 7 + the two seats of
                                                       scientist_reading_modes.md §1.3
8  CURRENT / ROUTABLE                                  generic mechanism
9  generic SendMessage routing                         generic
10 generic durable handoff / ACK                       protocol §8
```

```
SCIENTIST D REQUIRES NEW ROUTING LOGIC:      NO
   no D-specific routing code · no resolver branch · no new lifecycle state ·
   no D-specific supersession rule · no D-specific message protocol · no liveness oracle ·
   no governance section
DELTA:  ACTOR_ID + role binding + worktree row + fingerprint (derived, not added) +
        registration + acceptance test.  That is configuration, not protocol redesign.
```

🔴 **The qualification, and it is not small.** Steps 7–9 are generic **by design and not yet by
implementation** — the activation lifecycle and the resolver do not exist. So the falsifier proves
that *nothing in the design forces a D-specific branch*; it does not prove that a D could be
onboarded today. It cannot: neither could A or B. `GENERALITY: PASS` is a statement about the
architecture, and it is stated at exactly that strength.

**Scientist C compatibility: PASS** — `scientist-c` is live (`lettore-c-b2`, one session, the only
actor at cardinality 1) and differs from A and B only in that its `ACTOR_ID` remains `PROPOSED`.
That is a registration state, not a mechanism.

### 9.3 · New actor *types*, as distinct from new ordinary actors

A future scientific reviewer or evidence auditor may legitimately need a new role contract, new
authority boundaries, a new output schema and a new reviewer/escalation relationship. **It must
not need a new transport, a new routing model or a new session lifecycle.** The existing
structures already express the difference — `roles/<role>.md`, Annex H.1's authority matrix, P2.2's
per-role pertinence set, Annex C.4's three review objects — and this candidate introduces no field
to duplicate them.

---

## 10 · 🔴 PARTITION DECISION

```
PARTITION:  SPLIT
FIRST:      TRANSPORT  (this candidate)
SECOND:     ROUTING    — NOT OPENED, and BLOCKED rather than merely next
```

### 10.1 · Why split — the dependency is one-directional

**Routing depends on Transport.** Its failure taxonomy (`TARGET_STALE`, `DELIVERY_FAILED`,
`DELIVERY_UNKNOWN`), its re-resolution rule and its handoff definition are all stated in transport
vocabulary. **Transport does not depend on Routing.** *Authoritative content lives in a durable
artifact and the message carries a pointer* is true whoever the recipient is, and its acceptance
tests do not need a resolver — with one exception, `T-TRANSPORT-1`, which the protocol records as
**`NOT RUN`** rather than passing it by picking one of eight sessions.

Blast radius favours the split too: Transport touches no role contract, so **no fingerprint moves
and no in-flight checkpoint is invalidated**. Routing necessarily touches identity and authority
surfaces, and would.

### 10.2 · Why Routing is blocked, not merely second — three holds, none Plan's to lift

```
HOLD 1   PROPOSAL-C9-STATE-MODEL is ACCEPTED with `acceptance_is_not_adoption: true` and
         `hold: no implementation and no governance modification until that review completes`.
         Its §7.2 is exactly "where does CURRENT_SESSION_REF live". Adopting a clause of it is
         the trigger for its own next review — an operator-owned closure, not Plan's.

HOLD 2   BUILD_MINIMAL_DIRECTORY is 🔴 PROVISIONAL, pending operator acceptance.
         `framework/state/actors.yaml` does not exist; Phase 0 was never executed. A resolver
         built over an unaccepted directory recommendation would ratify it by using it.

HOLD 3   DEFERRED_PHASE: MULTI_AGENT_ARCHITECTURE_FEASIBILITY is PRESERVED, NOT AUTHORIZED,
         NOT STARTED, and its entry condition — "the Phase −1 recommendation is not
         DO_NOT_BUILD" — is itself unsatisfied because that recommendation is provisional.
```

And one technical precondition that is Plan's to name but not to satisfy:

```
HOLD 4   Phase −1's E5 must be RE-RUN. Its central negative — session_ref not obtainable — was
         measured through one instrument and is false through another (§7). Two of the three
         experiments Routing would rest on (E1, E2) returned INCONCLUSIVE, and E2's cause was
         never established. A routing candidate bound to that report today would be bound to a
         study that needs redoing.
```

**What would have happened without this analysis.** A routing candidate written this session
would have been, in substance, C-9 §7.2 plus `BUILD_MINIMAL_DIRECTORY` re-derived under new names
— self-authorizing two held decisions by re-deriving them, which is the failure a hold exists to
prevent. That is recorded as `SLR-plan-0007` L-4.

### 10.3 · What Mirror is asked to attack about the partition itself

1. **Is the split real, or is Transport too thin to be a candidate?** It adds one normative rule
   to an annex that already had the field. Argue that it should have waited for Routing.
2. **Is Routing genuinely blocked, or is there a narrow scoping that sits inside Plan's authority
   and touches none of the four holds?** If there is, this decision is wrong and Plan wants to
   know it.
3. **Is `T-TRANSPORT-1` recorded as `NOT RUN` honestly, or is it an unrun test wearing an
   excuse?** It is the one test that exercises the whole chain.
4. **Does §7 under-react?** Three artifacts, one of them canonical, state a falsified premise, and
   this candidate corrects none of them. Argue that the correction is owed now.

---

## 11 · Rejected alternatives

| alternative | why not |
|---|---|
| **Amend Annex B directly** | Annex B is `FROZEN`. Editing it is a MAJOR governance change to a frozen annex, and it is unnecessary: B.1 already carries `DURABLE_POINTER`, so what was missing was a rule about the payload, not a field |
| **A unitary Transport+Routing candidate** | §10. Routing is blocked on four preconditions; a unitary candidate would inherit all four and canonicalize nothing |
| **Add a pointer to this protocol in all four role contracts** | it would invalidate **every** in-flight checkpoint in the laboratory (P2.2: the role contract is in `CORE`), for a navigational gain. The protocol binds by being normative and indexed, as `scientist_reading_modes.md` binds |
| **Publish a numeric `LEGEND_MESSAGE_BUDGET`** | `message` has no observed bound, and the one field whose bound is enforced is nowhere near any LEGEND value. A number would be naked (§2 of the protocol) |
| **Implement `resolve_actor.py` now** | it is Routing's content, and a tool named in a directive is not thereby authorized |
| **Correct the falsified sentence in `scientist_reading_modes.md` §1.2** | it is canonical, its conclusion is unaffected, and the correction belongs to the candidate that needs the new capability. Registered in §7 and in the design record as `H-4` |
| **Repair `launch/legend_launch.sh`** (wrong-binary version gate; births only `background`) | outside scope. Recorded as `H-2` and `H-3` |
| **Recreate the four missing `snapshot/` tags** | §13.C. Speculative reconstruction of a control-plane artifact whose restore point is reachable anyway |

---

## 12 · Binding

```
REVISION                2
BASE_HEAD               4454feab72b7a0edf65f191be62aeedd899a15ad     verified unchanged at
                                                                     session open and at binding
CONTENT TIP             e839db38382781564a9767fe206eefd5fba0467c
CANDIDATE_CONTENT_HASH  81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f
                        532 included · 38 excluded
CANDIDATE_HASH_VERSION  legend-candidate-v4
SUPERSEDED BINDING      68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
                        revision 1, content tip f48a807
MANIFEST TIP            recorded in §14 after the control-plane commit exists, together with the
                        re-derivation of the hash at that tip
```

**Revision 1's binding is SUPERSEDED, and the word is chosen.** It was not wrong: it is still the
correct digest of the tree it named, and it reproduces exactly today — §1 uses it as a positive
control for that reason. Annex D.2 invalidates it because *"qualsiasi modifica materiale"* to the
bound content invalidates the binding attached to it, and the M-1 repair is a material change to
the normative artifact. Nothing approved was withdrawn, because nothing was ever approved.

The commits between the content tips touch only `governance/candidates/`, `reviews/` and
`ledger/`, all declared `CONTROL_PLANE_ROOTS` (P5.1), so the hash is expected to be identical at
every tip after `e839db38`. §14 **states the measured result** rather than asserting the
expectation.

**No `HUMAN_APPROVAL` is prefilled.** No `APPROVAL_ID` exists for this candidate, and no approval
has been requested. **Mirror review of revision 1 is complete — `REV-XPORT-MIRROR-001`,
`REQUEST CHANGES`. Revision 2 has not been reviewed**, and this manifest does not treat the
revision-1 verdict on the other axes as carrying forward to a tree Mirror has not seen. That is
the reviewer's determination to make, not the author's.

---

## 13 · Carried debts — verified at source this session, none repaired

### A · Orchestrator worktree contradiction — **ROUTING_RELEVANT**

`roles/orchestrator.md` line 5 says `worktree: the repository root checkout`.
`deployment/deployment_profile.md` gives Orchestrator its own `orchestrator` worktree and reserves
the root for canonical batch windows. **Both are canonical, in `main`.** `CAND-20260817-ORCHWT`
amended one file and not the other; the canonicalizing batch of `4454feab` recorded it as owed.

**Why routing-relevant, measured:** `--cwd` is the only mechanized scoping predicate the harness
offers, and the two canonical readings give `3 live sessions` and `0 live sessions` — *ambiguous*
under one and *absent* under the other, both fail-closed for opposite reasons. A resolver cannot
be specified against a field whose canonical value is contested. **Source precedence must be
settled before any mechanized resolution exists for `orchestrator`.**

### B · Root environmental test failures — **ENVIRONMENTAL**, instance not currently reproducible

Mechanism **confirmed at source**: `scripts/test_fresh_clone_reader_journey.py` and
`scripts/test_documented_commands.py` both enumerate `ROOT.rglob("*.md")` — the **filesystem**, not
`git ls-files`. Any untracked markdown in the working directory is scanned and its
repository-relative references must resolve. They are contamination-sensitive by construction.

Both are **green in this clean worktree** (5 + 2 = 7 tests). The root was inspected read-only
(`git --no-optional-locks -C <root> status --porcelain`) and is **clean at `4454feab`, 0 entries**,
so the reported failure is not currently reproducible: the contamination has since been cleared.

🔴 **The residual is a separate latent debt, and it is real**: a release-regression suite whose
verdict depends on untracked scratch files is measuring the workstation, not the release. Carried,
not repaired — nothing in root was cleaned, deleted or modified, and neither test was touched.

### C · Missing snapshot tags — **HISTORICAL_CONTROL_PLANE_DEBT, four instances not one, NOT LOAD_BEARING**

Six canonical batches declare a `snapshot/pre-<CAND>` tag at `GATE 4`. **Two exist.** Four do not:

```
missing:  snapshot/pre-CAND-20260817-HASHDET      declared by c89c2217
          snapshot/pre-CAND-20260817-ORCHWT       declared by f5b32155
          snapshot/pre-CAND-20260817-P51C9        declared by 005888b6
          snapshot/pre-CAND-20260818-SUNSET-DEC3  declared by cbce3016
present:  snapshot/pre-CAND-20260816-GOV311 · snapshot/pre-CAND-20260818-SCIENTIST-AB-SPEC
```

**Larger than reported** — four, not one. **Not load-bearing**: each batch's restore point is its
own first parent, each equals the `BASE_HEAD` its commit message names, and all four were verified
reachable from `main` this session. Recoverability is intact; what is missing is the named handle,
so a reader auditing `GATE 4` from the record alone hits a dangling reference. **Not recreated** —
fabricating a tag today would assert that a snapshot was taken then.

### D · Carried from the SCIAB review, unaffected by this candidate

`P-1 · P-3 · P-4 · P-5 · P-6 · P-7 · P-11 · N-1 · N-2 · N-3 · N-6 · N-8 · N-9`, plus `N-7`
unreconciled for the sixth review. `P-12` and `P-13` are answered in
`reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md`; `P-13`'s learning-record half is **repaired**
by `learning/plan/SLR-plan-0006-COR-001.md`, its manifest half is owed.

Also carried, unchanged: the `HUMAN_APPROVAL_QUEUE` has divergent copies across branches, and the
`main` copy of `runtime/orchestrator_lease.md` carries five leases while the `orchestrator` branch
carries seven. **This candidate does not reconcile either and is not authorized to.**

---

## 14 · Manifest tip and re-derivation — measured, and the regress named

```
MANIFEST TIP (first)    268df0420a21b47c48dbedb4815ea428c76fb57f
re-derived there        68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
                        531 included · 37 excluded
content tip value       68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
                        531 included · 33 excluded
IDENTITY                ✅ IDENTICAL. The four added paths are all under declared
                        CONTROL_PLANE_ROOTS — governance/candidates/, reviews/, ledger/ ×2 —
                        so `excluded` moves 33 → 37, `included` does not move at all, and the
                        approved identity never moved.
```

Verified by `git diff --name-only f48a807 268df04`, which returns exactly those four paths and
nothing else.

**The regress, stated rather than hidden.** This section records a value measured at
`268df0420a…`, and writing it down produces a *further* commit and therefore a further manifest
tip. That is not a defect and it is not concealed: P5.1 exists precisely so that a manifest can
describe a candidate without changing it, and the recording commit touches only
`governance/candidates/`. **The commit that carries this section re-derives the hash at its own
tip and states the result in its message.** The invariant a reviewer should check is not *the
manifest tip is final* — it never is — but **`included` stays 531 and the digest stays
`68173f01…` at every tip on this branch after `f48a807`.**

### 14.1 · Revision 2 — the same invariant, re-measured against the new content tip

The revision-1 invariant above **has now terminated, correctly and by design**: `included` moved
531 → 532 and the digest moved, because CONTENT moved. That is the rule working, not the rule
breaking. The invariant that binds from here is the revision-2 one.

```
CONTENT TIP (revision 2)  e839db38382781564a9767fe206eefd5fba0467c
measured there            81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f
                          532 included · 38 excluded
MANIFEST TIP              <the commit carrying this section>
re-derived there          stated in that commit's own message, measured not assumed
WHY included MOVES 531→532   learning/plan/SLR-plan-0008.md is CONTENT (P5.1: `learning/` is
                             CONTENT by intent). The protocol edit changes a blob id, not a count
WHY excluded MOVES 33→38     the five control-plane paths added since f48a807 — this manifest, the
                             handoff, two ledger records and the SCIAB author response
```

```bash
# the check that matters, runnable at any tip of this branch at or after e839db38
python3 governance/scripts/candidate_content_hash.py \
    --base 4454feab72b7a0edf65f191be62aeedd899a15ad --tip <any tip ≥ e839db38>
# expect: included 532 · 81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f
```

🔴 **A reviewer running the revision-1 command will get the revision-1 answer, and should.**
`--tip f48a807` still returns `68173f01…` with `531 / 33`. Both statements are true of different
trees, which is the whole point of binding a hash to a named tip — and it is why §1 uses the old
value as a positive control rather than deleting it.

```bash
# the check that matters, runnable at any tip of this branch
python3 governance/scripts/candidate_content_hash.py \
    --base 4454feab72b7a0edf65f191be62aeedd899a15ad --tip <any tip ≥ f48a807>
# expect: included 531 · 68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
```

---

## 15 · Revision 2 — disposition of every finding in `REV-XPORT-MIRROR-001`

The full author response is `reviews/plan/AUTHOR-RESPONSE-XPORT-MIRROR-001.md` (Annex C.2,
mandatory, silence is not acceptance). This section carries the dispositions that bear on the
binding.

| finding | class | disposition |
|---|---|---|
| **M-1** two false self-describing sentences in the normative artifact | 🔴 BLOCKING | **REPAIRED IN CONTENT** at `e839db38`. Frontmatter `actor_scope` and §11's bullet replaced; new §11.1 carries the property, the three permitted name classes and the semantic falsifier; `T-GENERIC-1` added to §10 and executed |
| **M-2** canonical P5.1's `runtime/` rationale is false today | NON-BLOCKING, BASE_HEAD's | **CONFIRMED INDEPENDENTLY, NOT REPAIRED.** See §15.2 |
| **M-3** "third binary" confirmed, "third version" not | OBSERVATION | **ACCEPTED.** The candidate and the design record already carry the accurate form; the looser paraphrase is not adopted and must not travel into Candidate B |
| **O-1** `T-TRANSPORT-6`/`-7` better typed `PASS_BY_DESIGN — NOT EXECUTED` | NON-BLOCKING | **ACCEPTED, NOT ACTED ON in this revision.** Retyping four test rows is not part of remediating M-1, and doing it here would widen the object under review. Carried |
| **O-2** `KERNEL_SPEC` cited without a version or commit pin | NON-BLOCKING | **ACCEPTED, carried.** A pin is right and it is a change to a citation the review confirmed sound; not bundled into a blocking-finding repair |
| **O-3** the `to` boundary between 201 and 212 is a bracket, not a boundary | NON-BLOCKING | **ACCEPTED.** The protocol claims the declared bound plus one rejection above it and nothing more. No text change needed; recorded so it does not harden |

### 15.1 · What M-1's repair does NOT do

```
TRANSPORT BEHAVIOR        UNCHANGED. §§0–9 of the protocol are byte-identical between f48a807
                          and e839db38 — measured, not asserted. The durable payload rule,
                          control envelope, depth rule, message-budget refusal, version binding,
                          per-field size table, outcome taxonomy, discovery/liveness distinction,
                          recipient-processing classes, the six-term handoff conjunction and
                          §9's five refusals are all untouched
RUNTIME-SCOPE MODEL       PRESERVED — endpoint/interaction-scoped, not a single global version.
                          Mirror's revalidation at 2.1.233 stands as evidence and is not
                          flattened; no new runtime claim is added at this revision
SUMMARY                   still NON-AUTHORITATIVE, by the same mechanism-based reasoning
T-TRANSPORT-1             still NOT_RUN. A new revision is not new evidence, and no
                          routing-neutral execution mechanism exists. None was created
ROUTING                   not reopened, not solved, not silently advanced. No registrar, no
                          activation, no CURRENT assignment, no supersession, no generation
SCOPE                     no Scientist activated · BENCH-AB-001 not started · main unchanged
```

The one addition to the acceptance table, `T-GENERIC-1`, is a test **about this document's own
generality**, not a transport rule. It adds no obligation to any sender or recipient.

**The `§§0–9 unchanged` claim is a measurement, and here is the command that produced it:**

```bash
for TIP in f48a807 e839db3; do
  git show $TIP:framework/protocols/cross_session_transport.md \
    | awk '/^## 0 · /,/^## 10 · /' | sed '$d' | shasum -a 256
done
# both → 91875ff763a6655caeafbf26026e15da0b9b72414ab3be7b43f6aa94b8cb98ad   372 lines each
```

Every executable transport clause lives inside that range. The three edits are outside it: the
frontmatter `actor_scope`, one row appended to §10's table, and §11 with its new §11.1.

### 15.2 · `M-2` — confirmed at source, and left with its owner

Verified independently this session, not taken on report:

```
CANONICAL P5.1 @ main   "While `runtime/` remains untracked it is invisible to `git ls-tree` and
                         therefore absent from the domain, so no fixed point arises in the interim."
MEASURED @ main          `git ls-tree -r --name-only main | grep '^runtime/'`
                         → runtime/orchestrator_lease.md          IS TRACKED
MEASURED in the domain   the emitted domain for this candidate lists it at entry 496 of 532
                         → runtime/orchestrator_lease.md          IS INSIDE THE HASH
CORROBORATED             deployment/deployment_profile.md — the lease "has moved to
                         runtime/orchestrator_lease.md, tracked." Canonical, one file away
```

**Classification: `SEPARATE_GOVERNANCE_DEBT`, confirmed.** The premise is false today, and the
consequence Mirror names is real — an Orchestrator lease write on a candidate branch would move
that candidate's content hash, which is the fixed-point class P5.1 exists to prevent.

**Not repaired here, and the reason is the one Mirror already accepted for the five artifacts of
§7**: P5 is canonical text at `BASE_HEAD`, editing it is a governed change belonging to whichever
candidate next opens P5, and XPORT's binding must follow canonical P5 **as actually implemented**
rather than Plan's hypothetical correction of it. XPORT neither introduces nor relies on the
defect: this candidate's hash is correct under the rule as executed, the script's behaviour
matches the declared roots, and no lease was written on this branch.

It is recorded as a fifth instance of the shape §7 documents — a true conclusion carried by a
premise that has quietly stopped being true — which is now the second time that pattern has been
found by someone other than the author of the artifact carrying it.
