---
artifact: MIRROR hostile review (Annex C.2) — Claude Code ↔ Codex runtime failover parity
review_id: RUNTIME_FAILOVER_CLAUDE_CODEX_HOSTILE_REVIEW_MIRROR_v1
object: the proposition "An actor can move from Claude Code to Codex without silently changing
  its authority, obligations, information boundary or enforcement."
level: R4 (METHOD — Mirror) · touches R5 (CROSS-MODEL) by subject matter
reviewer: mirror
author: — (the proposition is the operator's, put to Mirror for falsification; no actor authored it)
adjudicator: operator (Annex H.1 — governance decisions are the operator's)
date: 2026-08-26
verdict: REFUTED
personal_data: none. The human role is **Operator** throughout.
scope_note: every figure below was produced by executing a command in this session, in this
  worktree. Where a Codex-side fact is derived from configuration rather than executed, the row
  says DERIVED. I did not start a Codex model session and did not execute any write or any
  staging under Codex — deliberately.
---

# The control exists in every worktree, byte-identical, and Codex does not run it

---

## 0 · OBSERVATION_SCOPE

Every negative below is scoped to this table. **Local NOT_FOUND is not repo-wide NOT_EXIST.**

| Fact | Value |
|---|---|
| Derivation instant | `2026-08-26T20:47:00Z` |
| My worktree / HEAD | `.claude/worktrees/mirror`, branch `mirror` @ `1440428` — 0 behind `main`, 97 ahead |
| Shared checkout | `<REPO_ROOT>`, branch `main` @ `788c357` |
| Worktrees enumerated | **14**, by `git worktree list` (not by directory scan) — **10 Claude-side, 4 `legend-codex-*`** |
| `legend_lint.py .` | **PASS** |
| `fulltext_receipts.py verify` | **OK — 128 chained receipts, tail anchored** |
| `growth_anchors.py check` | **PASS** — claims 39 · papers 70 · corpus 356 · literature 390 |
| `state_manifest_current.md` | `current_state: READY` |
| Codex prompt artefact | `codex debug prompt-input` run in **this** worktree, 23,653 B, sha256 `37bc652bd876429b…` |
| `scripts/guard_bash_command.py` | sha256 `c030168abd594eb8…` — **identical in all 14 worktrees** |
| `.claude/settings.json` | sha256 `76afc02e2b0f5d38…` — **identical in all 14 worktrees** |
| Skills counted | 21 `SKILL.md` under `.claude/skills/` · 5 agents under `.claude/agents/` |
| Positive controls | every `strings` and every sandbox measurement below is reported in the same table as its control; two runs were **voided** by a failing control and are marked as such |

### Two measurements I discarded

Reported because a discarded measurement is evidence about method, and because both nearly
became findings.

1. **`strings` over `~/.local/bin/codex` returned 0 hits for `hook`.** It also returned 0 for
   `sandbox_mode`, `trust_level` and every other positive control: that path is a 7,236-byte
   Node shim, not the binary. Re-measured against the real 219,997,536-byte binary, `hook`
   returns 495 hits and `PreToolUse` returns 43. **The first result would have inverted this
   review's central finding.**
2. **`codex sandbox -- touch` denied a write inside cwd.** The control failed, so the two
   boundary probes beside it were void: bare `codex sandbox` defaults to read-only, not to the
   session's profile. Re-run under `-c sandbox_mode=workspace-write`, the control passed and the
   probes became measurements (§ 4, CE-6).

---

## 1 · STEELMAN (mandatory, before the objections)

**The architecture anticipated almost all of this, and the anticipation is good.**

`AGENTS.md` is a genuine thin pointer. It carries no operating law and says why: *"two parallel
normative files drift."* That is the correct shape — one normative corpus, two entrypoints — and
it is the reason CONTENT_PARITY is near-perfect by construction rather than by vigilance. The
normative files themselves are runtime-agnostic Markdown, and the three executable gates are
runtime-agnostic Python: `legend_lint.py`, `fulltext_receipts.py`, `growth_anchors.py` enforce
byte-identically from either runtime, and all three PASS right now.

Nobody forgot to propagate anything. `scripts/guard_bash_command.py` and `.claude/settings.json`
are byte-identical in **all 14 worktrees**, including the four Codex ones. This is not a
distribution failure.

Governance already refuses the naive position. Body **§33.1**: *"Codex ≠ Orchestrator; nessuna
governance per posizione."* **§33.3** routes repository-bound Codex work to a dedicated worktree
and advisory work to no shared writes. **§33.4**: *"Senza control plane →
`ON_DEMAND_LEGEND_COLLABORATOR`"* — absent a control plane, Codex is explicitly **not an actor**.
**§43** already names `Technology` as a minimum column of the runtime inventory. **Annex J.0**
already declares *"RBAC enforced a runtime (attori interattivi)"* to be a guarantee the system
does **not** possess. And **R5 CROSS-MODEL (Codex)** makes Codex's difference an asset in one
defined function, where independence is the point.

So the honest steelman is not "the design assumes parity". It is: **the design already forbids
what the proposition asserts.** Every objection below is therefore an objection about
materialization, not about doctrine — which is the weaker class of finding, and I say so before
pressing.

---

## 2 · VERDICT

**REFUTED.**

The proposition is false as stated, and the word that fails is **silently**. An actor moving
from Claude Code to Codex changes its enforcement surface, its obligation set and its startup
authority context, and **nothing in the repository, the runtime or the ledger emits a signal
when it does.**

The load-bearing finding is narrow and specific:

> **`.claude/settings.json`'s PreToolUse Bash guard is part of LEGEND's effective security
> model, and it is Claude-only.** The repository says so itself, in the guard's own docstring:
> *"An instruction that can be bypassed by choosing a different tool is not a control; this is
> the control."* — and, in the next paragraph, *"Claude and Codex work in it concurrently."*
> The file naming Codex as the reason the control is needed is the file Codex does not execute.

Codex failover is therefore **not SAFE merely because `AGENTS.md` describes the same rule.**
`AGENTS.md` does not describe this rule at all: the guard is not reachable from `AGENTS.md`, and
`guard_bash_command` appears **0 times** in Codex's entire 23,653-byte startup prompt.

---

## 3 · PARITY TAXONOMY

| Dimension | Status | Load-bearing measurement |
|---|---|---|
| **CONTENT_PARITY** | **HIGH, with a measured hole** | One normative corpus, two entrypoints. But of 31 targets named by `CLAUDE.md` and 18 by `AGENTS.md`: **20 CLAUDE-only, 7 AGENTS-only, 11 shared** |
| **SEMANTIC_PARITY** | **FAILS** | `AGENTS.md` § "Inviolable facts (**valid before you have finished reading `CLAUDE.md`**)" omits the § 0 authority gate. The set of rules that bind *pre-reading* differs between routers |
| **AUTHORITY_PARITY** | **FAILS** | `ORCHESTRATOR_LEASE` = **0** and `BOOTSTRAP` = **0** occurrences in Codex's whole startup prompt |
| **CAPABILITY_PARITY** | **FAILS, both directions** | Codex lacks 21 skills + 5 agents; Codex has 10 plugins / 15 skills / a `node_repl` MCP that Claude lacks; Codex **cannot commit** in a `.claude/worktrees/*` worktree without escalation, Claude can |
| **ENFORCEMENT_PARITY** | **FAILS** | The only deterministic write control in the repository does not execute under Codex, and its absence is silent |

Byte equality was never required and is not the problem. Authority and enforcement parity are
required, and both fail.

---

## 4 · COUNTEREXAMPLES

**Strict form** — SAME ACTOR `mirror` · SAME WORKTREE `.claude/worktrees/mirror` · SAME BRANCH
`mirror` · SAME HEAD `1440428` · SAME TASK · DIFFERENT RUNTIME → different permitted action or
different governance result.

| # | Task | Claude Code | Codex | Evidence class |
|---|---|---|---|---|
| **CE-1** | `git add -A` to stage this review | **DENIED** by PreToolUse hook (`permissionDecision: deny`) | **No hook loaded.** `settings.json` 0 hits in Codex's prompt; 0 `hooks` keys in `~/.codex/config.toml`; no enabled plugin ships `hooks.json`; cwd is a write root | Claude MEASURED · Codex DERIVED |
| **CE-2** | Repo write via inline heredoc | **DENIED** — *and it fired live on my own read-only probe in this session* | Same as CE-1: nothing intercepts it | Claude MEASURED (in-session) · Codex DERIVED |
| **CE-3** | Discharge `CLAUDE.md` § 2 ("apply without being asked", 9 trigger rows) | 21 LEGEND skills registered and auto-triggered | **15 skills, zero of them LEGEND.** `legend-start` appears **0 times** in Codex's entire prompt | MEASURED both sides |
| **CE-4** | Establish authority at session start | § 0 auto-injected: no lease → `BOOTSTRAP_MODE`; lease ACTIVE → *"You are NOT Orchestrator"* | § 0 absent. Reachable only by following a link `AGENTS.md` places at read-order step **2**, and omits from its own pre-reading binding list | MEASURED both sides |
| **CE-5** | Any output at all | No global instruction text loaded (`~/.claude/settings.json` has 6 keys, none instructional, no `hooks`) | `~/.codex/AGENTS.md` injected **above** the project doc, inside the same `<INSTRUCTIONS>` block: a standing brevity directive (*"sintetico… risposte troppo lunghe mi mettono ansia… usa icon, grassetti, tabelle"*) that pulls against the verbatim-locator and complete-read obligations | MEASURED |
| **CE-6** | `WORK_COMMIT` (H.1: *"ogni attore, solo proprio branch"*) | Unrestricted | **DENIED by sandbox.** Under `workspace-write` with a *passing* positive control: write inside cwd allowed; write to the worktree's real gitdir `…/legend-public/.git/worktrees/mirror` **denied**. That path is where a commit must write, and it is not a write root | MEASURED both sides |
| **CE-7** | Delegate a sub-task | 5 subagents in `.claude/agents/` | Absent. Codex runs a different topology (*"You are `/root`, the primary agent in a team of agents"*) | MEASURED |
| **CE-8** | Apply accumulated operating discipline | 46 memory files injected from `~/.claude/projects/…/memory/` | `~/.codex/memories_1.sqlite` — a disjoint store. Neither is repository state; neither transfers | MEASURED (existence) |

**COUNTEREXAMPLE_COUNT: 8 strict.**

### CE-9 — the stale class (different HEAD; reported separately, and it is worse)

Four `legend-codex-*` worktrees are **live right now** on `codex/*` branches. They are the four
`§42` names them: `aqeilan`, `partials`, `reading`, `wwox-mouse-series`. Their routers:

| Worktree | `CLAUDE.md` bytes | `ORCHESTRATOR_LEASE` | `BOOTSTRAP_MODE` | `OBSERVER` | `governance/` |
|---|---|---|---|---|---|
| `legend-codex-aqeilan` | 43,173 | 0 | 0 | 0 | 0 |
| `legend-codex-partials` | 43,173 | 0 | 0 | 0 | 0 |
| `legend-codex-wwox-mouse-series` | 43,173 | 0 | 0 | 0 | 0 |
| `legend-codex-reading` | 44,166 | 0 | 0 | 0 | 0 |
| **`mirror` (control)** | **6,745** | **1** | **1** | **1** | **5** |

These carry the **pre-router** `CLAUDE.md` — 6.4× the size of the current one — with **no
reference to the governance layer at all**. Not divergence: absence. Three distinct router
digests are in circulation (`1f1356bb…` on all Claude worktrees, `9d2f161e…` and `ed8a12e8…` on
the Codex side).

This does not satisfy the strict same-HEAD spec, so I do not count it among the 8. It is
nonetheless the finding with the highest operational severity, because it is **not
hypothetical failover — it is the current state.** `§42` mandates a census of exactly these four
*"prima di toccare"*; `ANNEX_INDEX.md` records the runtime inventory as **`pending`**.

---

## 5 · THE HOOK QUESTION, ANSWERED DIRECTLY

**Is a Claude-only hook currently part of LEGEND's effective security model?**

**Yes.** Not incidentally — by the repository's own stated reasoning. Both failure modes the
guard blocks *already happened here*, on 2026-08-04, to an agent that *"had every relevant
instruction in front of it"*. The guard exists precisely because instruction was proven
insufficient.

But the finding is sharper than "Codex has no hooks", and the sharper version matters:

**Codex has a hook subsystem, and it is wire-compatible with Claude's.** Measured in the binary:
`PreToolUse`, `PostToolUse`, `PreCompact`, `PostCompact`, `SessionStart`, `SessionEnd`,
`SubagentStart`, `SubagentStop`, `matcher`, `PreToolUseHookSpecificOutputWire`,
`PreToolUsePermissionDecisionWire`, and the runtime string `Command blocked by PreToolUse hook:`.
Codex further ships an `external_agent_config.detect` / `.import` path that references
`.claude/settings.json`, `settings.local.json` and `CLAUDE.md` by name.

So parity here is **achievable and cheap**. It has simply never been performed:

- `~/.codex/config.toml`: **0** occurrences of `hooks`
- `.codex-global-state.json`: no hook key at any depth
- The only `hooks.json` on disk belong to two plugins (`replayio`, `figma`) that are **not** among
  the 10 enabled plugins
- Codex declares hooks through a **plugin manifest**, and this repository ships no plugin

**HOOK_BYPASS_STATUS: BYPASSED — completely, silently, and by default.**

### And the guard is narrower than its docstring

Measured through the real stdin protocol (`verdict()` and the hook binary agree on all 10 cases):

| Command shape | Verdict |
|---|---|
| `git add -A` · `git add .` · `git commit -am` | **DENY** |
| `python3 - <<EOF … write_text('<repo path>')` | **DENY** |
| `sed -i '' 's/READY/BLOCK/' framework/state/state_manifest_current.md` | **ALLOW** |
| `echo '' > governance/annex_j_runtime_control_plane.md` | **ALLOW** |
| `echo 'x' \| tee framework/state/state_manifest_current.md` | **ALLOW** |
| malformed stdin · empty stdin | **rc=0, no output → fail-open** |

The docstring's stated purpose is to stop *"the shell [as] the way around"* Write's
read-before-overwrite rule. Three ordinary shell shapes walk around it. This is a **Claude-side**
finding, not a parity finding — I record it because it bounds the parity delta honestly: the
Claude/Codex enforcement gap is exactly two textual shapes wide, not "everything". It is also the
reason the gap must not be closed by porting this regex: porting it would transfer the hole.

---

## 6 · FAIL-CLOSED ANALYSIS

**FAIL_CLOSED_STATUS: FAILS OPEN, in three independent places.**

1. **The guard itself fails open.** Malformed or empty stdin → `rc=0`, no output → allow.
   Deliberate (*"never block on a malformed payload"*) and defensible in isolation; it means the
   control's absence and the control's failure are indistinguishable from the outside.
2. **The runtime swap emits no signal.** No error, no warning, no degraded mode. A Codex session
   in this worktree starts, reads `AGENTS.md`, and proceeds — with the guard file sitting on disk
   beside it, byte-identical to the Claude copy, inert.
3. **The compensating control is not running.** J.0 offers, in place of runtime-enforced RBAC:
   *"authority matrix testuale + audit + event ledger (H.1, J.1)"*. The textual matrix exists.
   **The event ledger does not**: `ledger/` holds `approvals`, `checkpoints`, `retirements`,
   `tasks` — and no `events/`. Mirror's own role contract records the ledger capability as
   *"blocked: the ledger has no writer yet"*. So the one compensation for the one missing
   guarantee that this review is about is itself unmaterialized.

The consequence is exact: **a runtime swap is undetectable by design and by current state.**

---

## 7 · AUTHORITY SURFACES

### CLAUDE_ONLY_AUTHORITY_SURFACES — 8

1. `.claude/settings.json` PreToolUse Bash guard → `scripts/guard_bash_command.py`
2. `CLAUDE.md` § 0 lease / `BOOTSTRAP_MODE` / OBSERVER gate — auto-injected before anything else
3. `CLAUDE.md` § 2 skill bootstraps — 9 trigger rows, "apply without being asked"
4. `.claude/skills/` — 21 skills, auto-discovered
5. `.claude/agents/` — 5 subagents
6. `Write`/`Edit` read-before-overwrite tool guard — the thing the hook exists to protect
7. Claude per-project memory — 46 files of LEGEND-specific operating discipline
8. Claude permission allow-list / `defaultMode` (`.claude/settings.json.example`, `settings.local.json`)

### CODEX_ONLY_AUTHORITY_SURFACES — 7

1. `~/.codex/AGENTS.md` — global instruction, injected **above** the project doc
2. `~/.codex/config.toml` → `[projects."<REPO_ROOT>"] trust_level = "trusted"` — the whole tree,
   worktrees included, is a trusted project outside any repository artefact
3. Sandbox `permission_profile` — `workspace-write`, `:root` **read**, write roots = worktree + `/tmp` + tmpdir. A real enforcement boundary Claude has no equivalent of
4. `~/.codex/memories_1.sqlite` + `goals_1.sqlite`
5. Plugin / marketplace layer — 10 enabled plugins, 15 skills, `node_repl` MCP with `NODE_REPL_TRUSTED_CODE_PATHS`
6. Codex's own hook subsystem — present, wire-compatible, **unconfigured**: a latent surface
7. `~/.codex/automations/`

Note the asymmetry is **not** one-directional. Surface 3 is stricter than anything Claude
enforces (it produced CE-6). "Codex is less safe" is the wrong summary; **"the two enforce
different things, and neither knows which one is running"** is the right one.

---

## 8 · GITIGNORED AND WORKTREE-LOCAL CONTEXT

**GITIGNORED_CONTEXT_STATUS: ASYMMETRIC, but not along the runtime axis** — and I record that
because it was my first hypothesis and it was wrong.

- `deployment/local_instance.md` (24,071 B) — holds `REPO_ROOT`, `WORKTREE_ROOT`,
  `RUNTIME_INSTANCE_ID` and the live `SESSION_REF`s (Annex I.5). It exists **only in the root
  checkout**. Absent from all 13 other worktrees, because gitignored state does not propagate.
  Annex I.1 lists the deployment profile in the canonical bootstrap nucleus. **Every actor in a
  worktree — Claude or Codex — is blind to the runtime instance record.** That is a
  working-directory asymmetry both runtimes share, not a runtime one.
- I read that file from this Claude session without a permission prompt. **Claude is not
  boundary-confined either**, so I make no claim that Codex's `:root` read grant creates a
  boundary Claude lacks. What differs is declared friction, not reach.
- `.claude/worktrees/` is gitignored — the 6 Claude worktrees are invisible to git from the root.
  The 4 Codex worktrees live *outside* the repository entirely, so no `.gitignore` reasoning
  covers them at all. Neither set appears in any tracked inventory. The census `§42` mandates has
  never run.

**SKILL_DISCOVERY_STATUS: ZERO — 0 of 21.** Codex's skill list in this worktree contains 15
entries, all Codex system or plugin skills. `legend-session-takeaways` and
`legend-capability-scout` appear in Codex's prompt twice each, but only as **path strings inside
`AGENTS.md`'s read-order item 3** — not as registered, auto-triggering skills. `legend-start`,
which `CLAUDE.md` § 2 mandates at session start, appears **0 times**: `AGENTS.md` does not name it.

---

## 9 · ACTOR IDENTITY (attack item 20)

**Identity is established by self-declaration in a session, anchored to a working directory.**
`BOOTSTRAP.md` step 6 receives *"each actor's registration: ACTOR_ID, session reference, declared
capabilities"*; step 7's L1 smoke is *"a declaration of ACTOR_ID"*. The deployment profile locates
actors **by worktree name**.

The Agent Card (Annex I.4) carries: `ACTOR_ID / ROLE / WORKTREE / ROLE_CONTRACT /
ROLE_CONTRACT_HASH / CAPABILITIES / CURRENT_SESSION_REF / CURRENT_SESSION_ID / STATUS /
LAST_SEEN`.

**It carries no runtime field.** The operator's distinction — `ACTOR_ID != MODEL/RUNTIME !=
SESSION != WORKTREE != AUTHORITY` — is half-implemented: the Card separates ACTOR_ID from SESSION
and from WORKTREE, and does not represent RUNTIME at all. `§43` *does* specify `Technology` as a
minimum inventory column — and `ANNEX_INDEX.md` records that inventory as **`pending`**. The one
artefact that would record which runtime an actor is in does not exist.

Two consequences:

- **Capabilities VERIFIED under one runtime stay VERIFIED after a move**, with no re-smoke. I.4
  names the failure mode — *"capability degradata dopo L2 (**deriva del runtime**)"* — but its
  detection is *"fallimenti ripetuti sullo stesso tipo di task"*. That is drift-shaped detection.
  A runtime swap is a **step change**, and would be caught only after repeated failures, i.e.
  after damage.
- **No ACTOR_ID is mapped to any `legend-codex-*` worktree.** Four actively-branched worktrees,
  zero identities. Per the governance's own model, whoever works there is an unidentified actor.

---

## 10 · KEY_OBJECTIONS, ranked

1. **[BLOCKING]** The only deterministic write control in the repository is Claude-only, and its
   absence is silent. The guard's own docstring names Codex as the reason it is needed.
2. **[BLOCKING]** Four Codex worktrees are live on routers that contain **zero** references to
   the lease, `BOOTSTRAP_MODE`, OBSERVER or `governance/`. This is present-tense, not failover.
3. **[BLOCKING]** J.0's compensating control for absent runtime RBAC — the event ledger — has no
   writer. There is no detection surface for any of this.
4. **[MAJOR]** `AGENTS.md`'s pre-reading binding list omits the § 0 authority gate that
   `CLAUDE.md` places *"before anything else"*. A precedence inversion, not an omission of content.
5. **[MAJOR]** `~/.codex/AGENTS.md` takes precedence over the project doc and issues a standing
   brevity directive that pulls against the verbatim-locator obligation. Outside the repository;
   invisible to every gate.
6. **[MAJOR]** 20 of 31 `CLAUDE.md` targets are unreachable from `AGENTS.md`, including
   `BOOTSTRAP.md`, `governance/ANNEX_INDEX.md`, `governance/annex_j_runtime_control_plane.md` and
   five of the nine mandatory skills.
7. **[MODERATE]** CE-6 inverts: Codex **cannot** discharge `WORK_COMMIT` in a `.claude/worktrees/*`
   worktree without escalation. An obligation H.1 places on every actor is not equally executable.
8. **[MODERATE, Claude-side]** The guard allows `sed -i`, `>` and `tee` against repository files,
   and fails open on malformed input. Porting it to Codex verbatim would transfer the hole.

---

## 11 · SAFE / UNSAFE ACTORS NOW

**SAFE_ACTORS_NOW: 0 (zero).**

Under the proposition as stated — move *without silently changing* authority, obligations,
boundary or enforcement — no actor qualifies, because the silence clause fails for all of them
before any role-specific analysis begins.

One precision, because it is the useful part: an actor whose task is **read-only, advisory, and
produces no durable state** exercises none of the surfaces that diverge. That is `§33.3`'s
*"advisory → nessuna scrittura condivisa"* and the R5 CROSS-MODEL function. Such work is not
"safe to fail over" — **the divergence is simply not reached.** That is a scoping property of the
task, not a property of the actor, and it is exactly the posture `§33.4` already prescribes:
`ON_DEMAND_LEGEND_COLLABORATOR`.

**UNSAFE_ACTORS_NOW: all 6 named ACTOR_IDs**, for distinct reasons:

| ACTOR_ID | Why unsafe |
|---|---|
| `orchestrator` | The § 0 lease gate is precisely what is absent under Codex; holds `CANONICAL_BATCH_COMMIT` (H.1, unique, lease ACTIVE) |
| `plan` | Integration / candidate writes; maintains the very inventory that is `pending` |
| `scientist-a` / `-b` / `-c` | Mandatory skills (0/21 discoverable), full-text receipts, verbatim locators — and CE-5 pulls against the last of these |
| `mirror` | `WORK_COMMIT` blocked by sandbox (CE-6); perimeter depends on § 2 skills |

---

## 12 · MINIMUM_REQUIRED_BEFORE_CODEX

Stated as **falsifiable preconditions**, not as design. Mirror does not repair and does not
create governance; each line below is a condition whose satisfaction is checkable, and whose
mechanism is Plan's and the operator's to choose.

| # | Precondition | Checkable by |
|---|---|---|
| 1 | The `§42` census of the four Codex worktrees exists, with per-worktree HEAD, branch, dirty state, unintegrated output and learning — and no worktree is `RETIRED` holding unintegrated content | Reading the census artefact |
| 2 | No actor operates from a router that predates governance materialization | Router digest equal to the tracked one in every working directory in the inventory |
| 3 | The `§43` runtime inventory exists and is populated, carrying `Technology` per actor, refreshed at every rehydration; a stale row is non-authoritative by its own rule | The artefact exists and its rows are current |
| 4 | The event ledger has a writer, so that a runtime change is an observable event rather than an inference | `ledger/events/` exists and is being appended |
| 5 | Either the two guarded shapes are enforced under Codex, **or** the governance states in writing that they are not and names what replaces them | `codex debug prompt-input` resolves a PreToolUse hook, or a governance clause says otherwise |
| 6 | Whichever enforcement is chosen covers the shapes § 5 shows the current regex misses — porting the regex is not sufficient | Re-running the 10-case table against the new control |
| 7 | The pre-reading binding sets of `CLAUDE.md` and `AGENTS.md` are the same set | Diffing the two inviolable-facts lists |
| 8 | The status of `~/.codex/AGENTS.md` — an out-of-repository instruction with precedence over the project doc — is adjudicated | An operator decision on record |
| 9 | `deployment/deployment_profile.md` leaves `PROPOSED`. **It also disagrees with `BOOTSTRAP.md` about where the Orchestrator lives** (`BOOTSTRAP.md` line 86: the root checkout; the profile: its own worktree, with an argument). That conflict is unresolved and the profile is awaiting this review | Both artefacts naming the same working directory |
| 10 | `§33.4` is either satisfied (a control plane exists) or enforced (Codex remains `ON_DEMAND_LEGEND_COLLABORATOR` and holds no ACTOR_ID) | The runtime inventory's authority column |

**TRUE_HUMAN_REQUIRED** — the operator's, per H.1 (*"Spese / MAJOR approval / governance |
Operatore"*), and no actor's:

1. Whether Codex becomes an **actor** or remains `§33.4` `ON_DEMAND_LEGEND_COLLABORATOR`. This is
   the governance decision the whole review reduces to.
2. Disposition of the four `legend-codex-*` branches and their unintegrated reading work
   (`§42` forbids retirement with unintegrated contents).
3. Any change to Annex I.4 (adding a runtime field to the Agent Card) — annex material,
   and H.1 marked **[MAJOR]** for H.1 itself.
4. Approval of `deployment/deployment_profile.md`, and resolution of its conflict with
   `BOOTSTRAP.md` (§ 12 row 9).
5. The status of the out-of-repository global instruction (§ 12 row 8).

---

## 13 · REVIEWER_CONFIDENCE · RESIDUAL_UNCERTAINTY · EVIDENCE_NEEDED

**REVIEWER_CONFIDENCE: HIGH** on the enforcement and discovery findings (CE-1…CE-8 rest on a
prompt artefact and a sandbox probe executed in this worktree, each with a passing positive
control). **HIGH** on CE-9 (four digests, one control). **MODERATE** on the Codex-side halves of
CE-1 and CE-2, which are DERIVED.

**RESIDUAL_UNCERTAINTY:**

- **I never started a Codex model session.** Every Codex behavioural claim rests on
  `codex debug prompt-input` run in this worktree, `codex sandbox` with a passing control, static
  configuration, and binary strings. I did not execute a write or a stage under Codex — a
  deliberate limit, and it is the main thing another reviewer could tighten.
- Whether Codex applies any *built-in* command-safety heuristic to `git add -A` independent of
  hooks. I found no such rule; **absence of evidence here is weaker than the rest of this review**,
  and it is the assumption CE-1's Codex half stands on.
- Whether the four Codex worktrees are currently *attended*. I measured their trees, not their
  sessions. If they are dormant, objection 2 drops from present-tense to latent — it does not
  drop further, because `§42` requires the census before touching them either way.
- `~/.codex/config.toml` is the state at `2026-08-26T20:47Z`. It is outside the repository and
  outside every gate; it can change without any LEGEND artefact moving.
- All figures here are object-derived (digests, byte counts, file counts) except the
  worktree population (14) and the router-digest distribution, which are population-derived and
  **decay**: a new worktree or a rebase changes them without changing anything else in this review.

**EVIDENCE_NEEDED:** a Codex session in this worktree, on this HEAD, given one identical task —
producing its own `prompt-input` dump, its resolved hook set, and its verdict on the 10-case
command table. That single artefact would convert every DERIVED row above to MEASURED.

---

## 14 · WHAT_WOULD_CHANGE_MY_MIND (declared falsifier, mandatory)

I would withdraw or downgrade this verdict on any of the following:

1. **`codex debug prompt-input` in this worktree resolves a PreToolUse hook to
   `scripts/guard_bash_command.py`, and a Codex session demonstrably denies `git add -A`.**
   → flips HOOK_BYPASS_STATUS; CE-1 and CE-2 fall; verdict downgrades to REFINED.
2. **A materialized `§43` runtime inventory carrying `Technology` per actor, plus a
   `ledger/events/` with an active writer.** → the swap acquires a detection surface;
   FAIL_CLOSED_STATUS changes and objection 3 falls.
3. **Evidence that the four `legend-codex-*` branches have been censused per `§42`, and that no
   actor operates from a pre-governance router.** → CE-9 retires.
4. **A demonstration that Codex auto-loads `.claude/skills/`, or that an equivalent LEGEND skill
   set is registered in `~/.codex/skills/`, such that § 2's "apply without being asked" holds.**
   → SKILL_DISCOVERY_STATUS changes and CE-3 falls.
5. **A governance clause stating that the guarded shapes are deliberately unenforced under Codex,
   naming what replaces them.** → the finding becomes a documented accepted risk rather than a
   silent gap. Note this satisfies the *silence* clause without satisfying parity: it would make
   the verdict REFINED, not CONFIRMED.

What would **not** change my mind: `AGENTS.md` being updated to describe the guard. Description
is the thing the guard's own docstring rejects as insufficient — *"An instruction that can be
bypassed by choosing a different tool is not a control."*

---

## 15 · AUTHOR_RESPONSE

*Mandatory. Silence is not acceptance (Annex C.2).* Addressed to Plan (inventory, census,
deployment profile) and to the Orchestrator (adjudication and routing). The governance decision
in § 12 is the operator's alone.

---

## 16 · FINAL OUTPUT

| Field | Value |
|---|---|
| **RUNTIME_FAILOVER_VERDICT** | **REFUTED — NOT SAFE.** The proposition fails on *silently*. Failover changes enforcement, obligations and startup authority, and nothing signals it |
| **COUNTEREXAMPLE_COUNT** | **8 strict** (same actor/worktree/branch/HEAD/task) **+ 1 stale class** (CE-9, different HEAD, present-tense, higher severity) |
| **CLAUDE_ONLY_AUTHORITY_SURFACES** | **8** — § 7 |
| **CODEX_ONLY_AUTHORITY_SURFACES** | **7** — § 7 |
| **HOOK_BYPASS_STATUS** | **BYPASSED — total, silent, by default.** Codex *has* a wire-compatible hook subsystem; this repository has never configured one. The guard file is present and byte-identical in **all 14** worktrees and executes in **none of the 4** Codex ones (10 Claude-side / 4 Codex-side, by `git worktree list`) |
| **SKILL_DISCOVERY_STATUS** | **ZERO — 0 of 21.** `legend-start` absent from Codex's prompt entirely |
| **GITIGNORED_CONTEXT_STATUS** | **ASYMMETRIC, not along the runtime axis.** `deployment/local_instance.md` exists only in the root checkout; all 13 worktrees are blind to it regardless of runtime. Neither runtime is read-confined |
| **SAME_ACTOR_DIFFERENT_RESULT_CASES** | **8** — CE-1…CE-8, § 4 |
| **FAIL_CLOSED_STATUS** | **FAILS OPEN ×3** — guard fails open on malformed input; swap emits no signal; J.0's compensating event ledger has no writer |
| **MINIMUM_REQUIRED_BEFORE_CODEX** | **10 preconditions** — § 12 |
| **SAFE_ACTORS_NOW** | **0.** Read-only advisory work does not reach the divergent surfaces — a scoping property, not safety, and already `§33.4`'s prescribed posture |
| **UNSAFE_ACTORS_NOW** | **6** — `orchestrator`, `plan`, `mirror`, `scientist-a`, `scientist-b`, `scientist-c` |
| **TRUE_HUMAN_REQUIRED** | **5 decisions** — § 12; the first (actor vs `ON_DEMAND_LEGEND_COLLABORATOR`) is the one the rest reduce to |

---

> The system did not fail to anticipate this. `§33`, `§42`, `§43`, `I.4`, `J.0` and `R5` are all
> pointed straight at it, and `§33.4` already gives the correct answer. What is missing is that
> every one of those clauses is `pending`, `PROPOSED`, or has no writer — while four Codex
> worktrees are live on branches whose router has never heard of any of them.
>
> The distance between a governance that anticipated the problem and a governance that prevents
> it is, in this case, one inventory and one ledger writer.
