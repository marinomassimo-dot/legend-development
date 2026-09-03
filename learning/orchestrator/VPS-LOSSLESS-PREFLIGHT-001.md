---
artifact: LOSSLESS VPS READ-ONLY PREFLIGHT — what must travel, what must stay private, what fails in a clean clone
record_id: VPS-LOSSLESS-PREFLIGHT-001
task_id: VPS_LOSSLESS_PREFLIGHT_v1
author: orchestrator
authored_on: 2026-09-03
dispatcher: operator
governance_version: 3.1.1 (read, not exercised)
mode: ANALYSIS_ONLY
STATUS: READ_ONLY_MEASUREMENT · ACTIVATION: NOT_REQUESTED · APPROVAL: NOT_GRANTED · AUTHORITY_CLAIMED: none
canonical_effect: NONE
impact_authority: NONE
classification:
  - MEASUREMENT AND DISPOSITION REPORT · NOT A TRANSFER — no disposition was executed
  - NOT A CAND, DEC, ANNEX, SLR OR POLICY · NOT A GOVERNANCE DECISION · NO NEW VOCABULARY
  - NO NEW IDENTIFIER FAMILY — `TOPIC-NNN` under `learning/`, the existing ANALYSIS_ONLY shape
---

# LOSSLESS VPS — READ-ONLY PREFLIGHT

| field | value |
|---|---|
| record id | `VPS-LOSSLESS-PREFLIGHT-001` · date 2026-09-03 |
| baseline SHA | `b1b5a581b9b1af85dd4de8a05212433e0aab21a2` |
| BASELINE_SURFACE | **BOTH** · `LOCAL_EQUIVALENT_TO_REMOTE_MAIN = YES` — local `main`, `refs/remotes/development/main` and live `ls-remote` all `b1b5a58`; `rev-list --left-right --count` = `0 0` |
| clone source | `development` = `https://github.com/marinomassimo-dot/legend-development.git` |
| PUBLIC vs DEVELOPMENT | **DEVELOPMENT**. Publicly readable? **UNVERIFIED** — §9 Q1 |
| remote evidence state | **LIVE_REMOTE** — the guard permitted `ls-remote` and `clone`; nothing rests on stale tracking refs |
| scratch | `/private/tmp/claude-501/…/scratchpad/{vps-preflight,mirror-d8}` — isolation PASS vs **19** worktrees, 0 relations, 2 positive controls |
| session start / end | 2026-09-02T23:25:52+0200 → 2026-09-03T00:14:30+0200 |
| Phase 0A overlap | **2026-09-02T23:39:13+0200 → session end** — first observed Phase 0A ref write inside this window; the overlap may have begun earlier, since a ref write was observed, not a session |
| actors | Orchestrator (identity, baseline, D2 out-of-repo, D5, consolidation) · Plan (D1–D4, D6, D7) · Mirror (D8) |

```
UNKNOWN:                              5
BLOCKERS:                             8
OPERATOR_DECISIONS:                   8 binary decisions, none taken here
D5_PASS_FAIL_ERROR:                   5 PASS / 2 FAIL / 0 ERROR   (clean clone, 7 instruments)
ADJUDICATION_DRIFT new/changed/gone:  0 / 0 / 0   (15 records, 14 TRUE_HUMAN_REQUIRED, 14 RUNTIME_DURABLE)
STATE_PARITY:                         PASS for state transfer — no instrument regresses from working tree to
                                      clean clone, and the one divergence is INVERTED. The baseline battery is
                                      nonetheless red, for repository-content defects, not for lost state.
ENVIRONMENT_PARITY:                   NOT_YET_TESTED_ON_VPS
PREFLIGHT_VERDICT:                    READY_AFTER_OPERATOR_DECISIONS — conditional on B3: if `staging/` proves
                                      required for resume, this becomes BLOCKED_BY_RECONSTRUCTION.
```

**Exclusion boundary.** ⟨0A branch⟩ was an unfilled placeholder, so a conservative rule was adopted at bootstrap and held by all three actors: **no non-`main` branch content was read, diffed or cited**; branches entered as metadata only. Phase 0A was later identified from executable evidence as `refs/heads/plan-modular-evolution-p0a` (ref file written 23:39:13+0200, at exactly the main tip, **0 unique commits**). It was never opened.

**Cap notice.** The 300-line cap binds. §15's truncation order was applied: D2 detail rows are collapsed to totals with evidence pointers, D1's `PRESENT_BUT_NOT_REQUIRED` is a single line, and the 15 unchanged prior adjudications are one reference. D4, D5, D6 and D8 are complete.

## 1 · D1 — PUBLIC_RECONSTRUCTION_SET

`CLONE_AVAILABLE` = 686 tracked files at `b1b5a58`. The clone's tracked tree SHA is `948bf948faf2f3c95873454d34f158f2029bc56f` — **byte-identical to the source's**, 686 files each (independently corroborated: Mirror's mode tally 534 × `100644` + 152 × `100755` = 686). Any working-tree/clean-clone divergence therefore cannot come from tracked content.

Required and verified present in the clone: ROUTER_CHAIN (6 surfaces, `AGENTS.md` §1); the four scientific CURRENTS; `current_state: READY` (`state_manifest_current.md:141`, clone **and** source); receipt chain — `OK: 128 chained receipt(s), tail anchored`; growth anchors — `claims=39 · papers=70 · corpus=356 · literature=390`, `VERDICT: PASS`; **64 deepdive manifests** re-derived three ways (`ls`, `*.json`, `git ls-files`) in both roots; runtime/bootstrap paths; the release battery.

```
NEEDED_BUT_ABSENT         = ∅
PRESENT_BUT_NOT_REQUIRED  = files/, staging/, tmp/, backup/, Library/, .playwright-mcp/   (informational; infer no discard)
PUBLIC_RELEASE_SURFACE    = public_release_gate.py → VERDICT PASS, BLOCKS 0, 4 REVIEW (PARENT_OF_ORIGIN_ATTRIBUTED)
```

**Carrier drift.** The dispatch names `runtime_parity.py` at repository root: **ABSENT** there. Current path is `framework/scripts/runtime_parity.py`, tracked; canonical invocation `AGENTS.md:62`. Every other named carrier is PRESENT and tracked.

---

## 2 · D5 — FRESH CLONE SIMULATION *(not truncated)*

Clone taken from the remote over the network. `objects/info/` is **empty** — no `alternates`, so it borrows nothing from the local object store. HEAD arrived already at the baseline.

| instrument | working tree | clean clone | verdict | first failure | cause class | conf. |
|---|---|---|---|---|---|---|
| `runtime_parity.py --bootstrap` | 1 | 1 | FAIL both | `READ_ONLY_PARITY FAIL` → `ACTOR_ID is unassigned`, `ROLE_REACHABILITY` | **ENVIRONMENT** — `AGENTS.md` states `--bootstrap` will not choose an actor and exits non-zero until one is assigned | high |
| `legend_lint.py .` | 0 | 0 | PASS | `VERDICT: PASS` | — | high |
| `fulltext_receipts.py verify` | 0 | 0 | PASS | — | — | high |
| `growth_anchors.py check` | 0 | 0 | PASS | — | — | high |
| `public_release_gate.py` | 0 | 0 | PASS | `BLOCKS: 0` | — | high |
| `run_release_regressions.py` | 1 | 1 | FAIL both | `REGRESSION VERDICT: FAIL` — 8 suites WT, **7** clone | **REAL_DEFECT** | high |
| `test_fresh_clone_reader_journey.py` | **1** | **0** | **DIVERGENT (inverted)** | walks into `.claude/worktrees/plan-rev13/**` | **MISSING_LOCAL_STATE, inverted** | high |

**The 7 shared failures are neither environment nor lost state.** Re-run under `python3` 3.9.6 *and* the CI-pinned 3.12: identical exits, identical assertions, with a positive control passing under both (`test_md_run_matrix.py` = 0). `run_release_regressions.py` carries **no** expected-failure allowlist — its `TESTS` tuple is hardcoded. Four of the seven share **one** cause: they assert strings in `CLAUDE.md` that the 2026-08-16 router migration moved out — `verbatim_locators`, `pubmed_corpus_harvest`, `FULLTEXT_READ_RECEIPT`, `session_self_evaluation.md`. All four still exist in the repository (114 / 14 / 29 / 10 tracked files; positive control `BATCH_COMMIT` = 203), so the content was **moved, not lost**, and the tests were not moved with it. The other three are distinct: `test_documented_commands.py` (`cross_host_handoff.md:225-226` documents `--table`, `--reconstruct-real`, `--root`, `--payload`, `--scratch` on `test_legend_handoff.py`, which exposes none of them); `test_release_runner_verdict.py` (a suite on disk absent from the runner's tuple); `test_release_surface.py` (the inverse).

🔴 The first of those defects is **inside `cross_host_handoff.md`** — the protocol this preflight depends on for the private transport. **The document under evaluation cannot be checked by the method it prescribes**: its own §5 "re-derive rather than quote" commands do not run at baseline.

**The inverted divergence is a D2 finding** (§7 makes it one automatically): local gitignored state is a *contaminant* for that instrument, not a requirement. A VPS clone will do better than this Mac.

**CI-canonical form.** `.github/workflows/public-release-gate.yml` runs `ubuntu-latest` + Python **3.12** and installs `requirements-analysis.txt` (`numpy==2.0.2`) before the battery; its gate form is `--root . --mode release --report-json …`. Run verbatim in the clone: `VERDICT: PASS`, `BLOCKS: 0`, exit 0. CI does **not** run receipts, anchors, the reader journey or runtime parity — D7 Stage A1 adds them.

## 3 · D2 — LOCAL-ONLY STATE INVENTORY *(detail rows truncated per §15; totals and evidence pointers kept)*

Uniqueness is measured at **object** level, never ref level. Positive control in-table: `refs/heads/main` = 0. Local `refs/remotes/development/*` was first proven **set-identical** to live `ls-remote` (both `comm` directions empty) — that is what licenses `--not --remotes=development` as a proxy for the published surface.

**Git-local** *(measured 23:45–23:57+0200; this population is LIVE — §10)*. 90 heads: **69 published, 21 unpublished carrying 185 unique commits (union)** — the per-ref sum is 378, so per-ref counts are **not additive**; Mirror by object: 1,139 objects / 5,294,298 B. `refs/preserved/*` 3 refs, **7 unique commits** even against development ∪ all branches. `refs/pii-backup/*` 2 refs (`a7139ec`, `299492b`, both commits, 2026-08-26), **5 unique commits**; metadata only, content never opened. `refs/stash` → `b688470` = **the same object as** `refs/preserved/stash-worktree-evidence-index`, **0 unique beyond preserved**. `refs/codex/*` 14 refs, **all `tree`-typed**, → 8 distinct trees → **5 absent from the published clone, covering 10 refs**. 6 tags (4 loose, 2 packed), of which `bench-participant/withdrawn-non-orphan` carries 1 unique commit. `refs/remotes/local/*` orphan — no `local` remote in config. Config: `branch.main.remote=origin` (the out-of-scope repo), main **631 ahead / 0 behind** origin/main, `push.default=nothing`. **No git hook anywhere** (`core.hooksPath` unset, `.git/hooks/` 14 entries all `.sample`, `extensions.worktreeConfig` unset, no `config.worktree` in any worktree). **0** tracked symlinks (mode `120000`) and 0 on disk; no `.gitmodules`; **0** `.gitattributes`.

🔴 **A commit-level sweep of `refs/codex/*` returns 0 and means nothing** — `rev-list` walks commits and these refs hold trees. The right instrument is object-store membership. Positive controls: all 90 heads are `commit`; the baseline tree resolves inside the clone. A tree-typed ref also **cannot be moved by any push**, whatever the branch policy. 🔴 **"52 unpublished heads" and "21 unpublished heads" are both true**: by *name* 90 − 38 = 52, by *reachability* 69 are published. They answer different questions and must never be quoted for each other.

**Worktrees (19)** — dirty/untracked is **per-working-directory**. Root `main` 0/0/0. `evidence-index` **19 dirty tracked / 0 untracked / 0 unique commits**. `mirror` 0/11/103. `lettore-c` 0/3/28. `lettore-b` 0/0/25. `legend-codex-partials` 0/1/0. Other 13: 0/0/0.

🔴 **The single largest lossless exposure.** `evidence-index` carries **19 uncommitted tracked modifications, all `framework/scripts/*`** — the guard/runtime engine (`effect_model.py`, `post_effect_verify.py`, `repo_topology.py`, `session_binding.py`, `guard_revision.py`, … and 7 `test_*`) — while its branch has **0 unique commits**. That content exists **in no ref anywhere**. Verified twice, independently. A clone reproduces none of it.

**Gitignored durable populations.** `files/` 805 files / 950,608,770 B (surface `fs.external.fulltext_corpus`, re-fetched) · `.claude/` 10,485 / 657,820,334 (worktree surfaces) · `tmp/` 86 / 72,763,243 (**no surface**) · `staging/` 138 / 10,502,152 (**no surface**, though `growth_anchors.py:277,336` reads it) · `backup/` 33 / 4,889,579 (**no surface** — all 9 `backup` hits in the classifier are `pii-backup`) · `Library/` 54 / 900,016 (**no surface**) · `grants/` + `grant-applications-private/` 17 / 144,704 (**no surface**) · ignored children of `disease-models/`, `governance/` 9 / 2,175,232 (**coverage UNVERIFIED**) · `.playwright-mcp/`, `.DS_Store` 5 / 28,650 (`EPHEMERAL_UNTRACKED`, `legend_handoff.py:79-80`).

🔴 **`UNKNOWN_REQUIRED_STATE: 0` is a counter over a population the classifier itself defines.** Its fail-closed rule is real — *"anything untracked and NOT matching one of these is UNKNOWN, and UNKNOWN that is required for resume is a hard DENY"* (`legend_handoff.py:76-77`) — but its enumeration is `git status --porcelain --untracked-files=all` (`:210`) with **no `--ignored`**. A gitignored path can therefore never enter the UNKNOWN bucket. Measured blind spot: **328 files, 85.1 MB** over six top-level populations, plus 9 ignored paths of unverified coverage. Positive control: `files/`, which *does* have a surface, correctly falls outside the blind spot. Mirror's independent sweep discriminated on the same axis (`_qa/`, `overlay/`, `md-output/` returned ABSENT).

**Out-of-repository** *(existence/dependency only; no value was read or recorded)*. Population derived **from executable evidence in the repository first**, then measured — not by sweeping `$HOME`. Positive controls: `~` present, a fabricated sibling absent.

| path | status | files | bytes | evidence |
|---|---|---|---|---|
| `~/.legend/lineage/mac-dev-001/` | PRESENT | 2 | 3,408 | `legend_launch.sh:50`; `legend_handoff.py:605,870,1217` |
| `~/.legend/state/payload/` | PRESENT | 14 | 785,976 | `legend_handoff.py:293`; `cross_host_handoff.md:141,155` |
| **`~/.legend/keys/legend-luks.key`** | **PRESENT, UNENUMERATED** | **1** | **64** (mode `0600`, dir `0700`, 2026-08-31 23:44) | found only by Mirror's probe 2 |
| `~/.legend/.DS_Store` | PRESENT | 1 | 6,148 | — |
| `~/.legend/attestation/` | **ABSENT** | 0 | 0 | `execution_attestation.py:61,323` — **absent by design** |
| `~/.legend-venvs/` | PRESENT | 71,114 | 8,387,913,245 (`models/` alone 6,612,977,504 over 2 files) | `legend_handoff.py:710` |
| `~/.codex/config.toml` · `~/.codex/sessions/` | PRESENT | 1 / 73 | 3,655 / 466,787,732 | `codex_runtime_probe.py:48-49` |
| `~/.claude/settings.json` | PRESENT | 1 | 13,943 | **7 top-level keys, and `hooks` is not one of them** — §7 probe 3 |
| `~/.gitconfig` | PRESENT | 1 | 192 | `guard_policy.py:3122` — 6 keys |

🔴 **The key material was missed by the population I derived, and by the classifier.** `~/.legend` holds 18 files; `lineage` (2) + `state` (14) = 16, and the two unaccounted files were never itemised until Mirror looked. `legend_handoff.py` enumerates a **hardcoded pair list** — `("lineage", …)`, `("state/payload", …)` at `:870` and `:1217` — not a walk of `~/.legend/`. A 64-byte LUKS key is therefore not merely unclassified, it is **uncounted**, so `UNKNOWN_REQUIRED_STATE: 0` is green partly because the denominator excludes it. Its content was not read. The absent attestation store, by contrast, is **not** a loss: the source says so — *"runtime-local state, not a repository control … not committed, not reviewed, and **not present in a fresh clone**"* (`execution_attestation.py:61-70`); `LEGEND_ATTESTATION_HOME` is UNSET.

**Required environment-variable NAMES** (names only; all UNSET in the measuring process): `LEGEND_ACTOR_ID`, `LEGEND_ASSIGNED_WORKTREE`, `LEGEND_RUNTIME`, `LEGEND_RUNTIME_INSTANCE`, `LEGEND_LINEAGE_DIR`, `LEGEND_STATE_DIR`, `LEGEND_STATE_PAYLOAD`, `LEGEND_ATTESTATION_HOME`, `LEGEND_CORPUS_DIR`, `LEGEND_TRANSPORT_SETTINGS`, `LEGEND_CERTIFIED_VERSION`, `LEGEND_SOURCE`, `LEGEND_COLLABORATOR`, `CODEX_HOME`, `CODEX_SANDBOX`, `CODEX_VERSION`, `CLAUDE_CODE_VERSION`, `NCBI_EMAIL`, `NCBI_API_KEY`.

---

## 4 · D3 — UNIQUENESS / NECESSITY / PRIVACY

`legend_handoff.py classify` was re-derived at baseline by two actors independently: exit 0, **24 surfaces**, its own internal positive control satisfied, `UNKNOWN_REQUIRED_STATE: 0`, `git.worktree.dirty` = 19, `git.worktree.untracked.adjudicated` = 15, `fs.legend.state` = 14, `fs.legend.lineage` = 2, **no `HANDOFF_DENY` at baseline**. Mirror verified it read-only first: every write site (`:791-1225`) sits inside `cmd_handoff@782` / `cmd_resume@1042`, and `cmd_classify@1345` is past them all.

**ADJUDICATION DRIFT = 0/0/0.** 15 records, 14 `TRUE_HUMAN_REQUIRED`, 14 `RUNTIME_DURABLE`, 4 `required_for_resume` — all UNCHANGED, restated here in one reference and **not re-analysed**: `framework/state/handoff_adjudication.jsonl`, 15 rows keyed `mirror` (11), `lettore-c` (3), `legend-codex-partials` (1).

**A count that disagreed, reconciled at the set level.** 15 adjudication records but **14** payload copies under `~/.legend/state/payload/` (mirror 11→10, lettore-c 3→3, codex-partials 1→1). The one record with no copy is `mirror/.codex-hook-probe.tmp`, `EPHEMERAL`, `required_for_resume=false`, 17 bytes, `destination_decision: "none — reproducible byte-for-byte from the recorded command; retained, not needed"`. **Correct by design, not a defect.** Both numbers were right; they measure different things.

🔴 **PRIVACY INSTRUMENTS DISAGREE — `PRIVATE = UNADJUDICATED`, and neither implementation is preferred here.** On the same clean clone: `public_release_gate.py` = **PASS, 0 BLOCK, 4 REVIEW**; `independent_privacy_scan.py` = **exit 2, 47 findings, 17 BLOCK across 11 tracked paths**. Categories only (`ITALIAN_CITY` 5, `PRIVATE_NAME` 4, `CALENDAR_DATE` 4, `EMAIL` 3, `ITALIAN_HOSPITAL` 1); no matched value is reproduced anywhere in this report.

## 5 · D4 — DISPOSITION TABLE *(not truncated)*

```
TOTAL_IN_SCOPE = 29   RECONSTRUCT = 8   TRANSPORT_PRIVATE = 11   DISCARD_PENDING_DECISION = 5   UNKNOWN = 5
```

| # | object | uniq | nec | priv | prior adj | drift | **disposition** | why | blocker |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 69 published heads | N | — | N | — | — | **RECONSTRUCT** | `git clone` | — |
| 2 | `refs/codex` 4 refs / 3 published trees | N | — | N | — | — | **RECONSTRUCT** | in the clone object store | — |
| 3 | handoff blob tag | N | — | N | — | — | **RECONSTRUCT** | published | — |
| 4 | 5 remaining local tags | N | N | N | — | — | **RECONSTRUCT** | published | — |
| 5 | local git config | Y | Y | N | — | — | **RECONSTRUCT** | re-declared on the VPS, not copied | B6 |
| 6 | `~/.legend/attestation/` | — | N | N | — | — | **RECONSTRUCT** | absent from any fresh clone by design | — |
| 7 | `~/.legend-venvs/` (8.39 GB) | Y-loc | N | N | — | — | **RECONSTRUCT** | `REBUILDABLE_CACHE` — but see B8 | **B8** |
| 8 | `files/` (805 files, 908 MB) | Y-loc | N | UNADJ | — | — | **RECONSTRUCT** | `EXTERNAL_REFERENCE`, re-fetched | B4 |
| 9 | 21 unpublished heads (**185 commits / 1,139 objects**) | **Y** | Y | N | — | — | **TRANSPORT_PRIVATE** | unreachable from remote; bundle | — |
| 10 | `refs/preserved/*` (**7 commits**) | **Y** | Y | N | — | — | **TRANSPORT_PRIVATE** | unique even vs development ∪ branches | — |
| 11 | `refs/pii-backup/*` (**5 commits**) | **Y** | Y | **Y** | — | — | **TRANSPORT_PRIVATE** | bundle only — **never push** | B1 |
| 12 | `refs/stash` | N (0 beyond preserved) | name | N | — | — | **TRANSPORT_PRIVATE** | the *name* is the record of preservation | — |
| 13 | `refs/codex` 10 refs / **5 unpublished trees** | **Y** | Y | N | — | — | **TRANSPORT_PRIVATE** | absent from the published object store; a push cannot move a tree-ref | — |
| 14 | **evidence-index 19 dirty tracked files** | **Y** | Y | N | — | — | **TRANSPORT_PRIVATE** | in no ref; `patch in bundle` | **B2** |
| 15 | 15 adjudicated untracked | Y | 4 yes | N | **×15** | UNCHANGED | **TRANSPORT_PRIVATE** | bundle + durable payload | B1 |
| 16 | `~/.legend/lineage/mac-dev-001/` | Y | Y | N | — | — | **TRANSPORT_PRIVATE** | copied into bundle | — |
| 17 | `~/.legend/state/payload/` (14) | Y | Y | N | — | — | **TRANSPORT_PRIVATE** | copied into bundle | — |
| 18 | `bench-participant/withdrawn-non-orphan` | Y (1c) | Y | N | — | — | **TRANSPORT_PRIVATE** | 1 unique commit | — |
| 19 | **`~/.legend/keys/legend-luks.key`** | **Y** | **UNVERIFIED** | **Y** | — | — | **TRANSPORT_PRIVATE** | key material; loss is irreversible and no other copy is known. **Uncounted** by the classifier | **B7** |
| 20 | `grants/` + `grant-applications-private/` | Y | UNVERIFIED | **Y** | — | — | **DISCARD-PENDING-DECISION** | privacy-designated by name; not LEGEND state | B5 |
| 21 | `deployment/local_instance.md`, `.claude/settings.local.json` | Y | N | **Y** | — | — | **DISCARD-PENDING-DECISION** | `SECRET_MACHINE_LOCAL`, re-authored | — |
| 22 | `refs/remotes/local/*` | N | N | N | — | — | **DISCARD-PENDING-DECISION** | orphan; remote absent from config | — |
| 23 | `.codex-hook-probe.tmp` | Y | N | N | ×1 | UNCHANGED | **DISCARD-PENDING-DECISION** | EPHEMERAL, reproducible byte-for-byte | — |
| 24 | `~/.legend/.DS_Store` | Y | N | N | — | — | **DISCARD-PENDING-DECISION** | OS artefact | — |
| 25 | `staging/` (138 files, 10.5 MB) | Y-loc | **UNVERIFIED** | UNADJ | — | — | **UNKNOWN** | no surface, yet read by `growth_anchors.py:277,336` | **B3** |
| 26 | `tmp/` (86 files, 72.8 MB) | Y-loc | **UNVERIFIED** | UNVERIFIED | — | — | **UNKNOWN** | no surface, no ephemeral pattern | **B3** |
| 27 | `backup/` (33 files, 4.9 MB) | Y-loc | **UNVERIFIED** | UNVERIFIED | — | — | **UNKNOWN** | no surface | **B3** |
| 28 | `Library/` (54, 0.9 MB) | Y-loc | **UNVERIFIED** | UNVERIFIED | — | — | **UNKNOWN** | no surface | **B3** |
| 29 | 9 ignored paths under tracked roots | Y-loc | **UNVERIFIED** | UNVERIFIED | — | — | **UNKNOWN** | coverage unverified | B3 |

No row received a bare `DISCARD`. Nothing was reconstructed, transported, discarded or deleted.

---

## 6 · D6 — BLOCKERS AND DECISIONS *(not truncated; sorted by objects unblocked)*

| id | objects | binary decision / required fact | A → consequence → reversibility | B → consequence → reversibility |
|---|---|---|---|---|
| **B3** | **5 rows, 328 files, 85.1 MB** | Are `staging/`, `tmp/`, `backup/`, `Library/` (+9 ignored children) required for resume? `UNKNOWN_REQUIRED_STATE: 0` cannot see them — mechanism proven at `legend_handoff.py:210`. | Give the classifier an ignored-path surface, re-run → UNKNOWN → 0. **Reversible** | Declare them out of scope by fiat. Silent loss over a population never examined. **Irreversible once the Mac is retired** |
| **B1** | **17** (15 adjudicated + 2 pii-backup) | Restated, not re-analysed: transport the 14 `TRUE_HUMAN_REQUIRED` payloads under owner/operator authority? | Bundle all 14, plus the 2 never-push refs. **Reversible** | Transport only the 4 `required_for_resume`; 10 payloads do not travel. **Recoverable only while the source host lives** |
| **B2** | **19** | The evidence-index dirty tree exists in no ref. Carry as patch, or require its owner to commit first? | `patch in bundle` — the classifier already routes it. **Reversible** | Owner commits in its own worktree first; blocks until they act. **Reversible** |
| **B8** | 12 surfaces, **8.39 GB** | `~/.legend-venvs/` is declared `REBUILDABLE_CACHE`, but the only tracked recipe is `requirements-analysis.txt` = `numpy==2.0.2`; `models/` is **6.61 GB with no pin, no URL, no digest**, and PaperQA is `DESCRIBED`, not `REPRODUCED`. | Pin a recipe (versions + digests) before relying on rebuild. **Reversible** | Trust the class. Rebuild may be impossible or non-identical, and needs a provider secret that is UNSET. **Irreversible if the Mac is wiped** |
| **B4** | 805 | Is a re-fetch of `files/` byte-identical to the recorded receipt digests for paywalled items? `--verify-artifacts` needs `--pmid`, so this is **untested at corpus scale**. | Verify before relying on re-fetch. **Reversible** | Trust re-fetch; receipt verification may break. **Irreversible if the corpus is cleared** |
| **B7** | **1** (64 bytes) | Does the VPS plan involve an encrypted volume — i.e. is `~/.legend/keys/legend-luks.key` required? It is uncounted, unclassified and has **no integrity mechanism**. | Enumerate, classify, transport privately with a digest. **Reversible** | Leave it. If a LUKS volume is in the plan, that volume becomes **unrecoverable**. **Irreversible** |
| **B5** | 17 | `grants/` + `grant-applications-private/` are privacy-designated by name and unclassified. Transport privately, or leave? | Leave. **Reversible** | Private transport. **Reversible** |
| **B6** | 1 | `branch.main.remote=origin` binds main to the out-of-scope repo (631 ahead / 0 behind). The VPS must bind main → `development`. | Re-declare on the VPS. **Reversible** | Inherit the shape; wrong-remote hazard. **Reversible** |

Not blockers, deliberately: the tag removed mid-session and `plan-modular-evolution-p0a` — both carry **0 unique commits**.

## 7 · D8 — MIRROR: PRIVACY ON THE TRAVELLING SETS, AND FALSIFICATION *(not truncated)*

Mirror worked from its **own** clone at `b1b5a58`, never reusing Orchestrator's. **Two independent methods produced the same set, not merely the same count** — Mirror scanning its own clone, Orchestrator filtering a whole-tree scan to tracked paths: both → **47 findings, 17 BLOCK, 11 distinct paths**, identical membership.

```
whole working tree      1523 findings  (1159 BLOCK)      of which .claude/worktrees/** = 1374 (1044 BLOCK)
REMOTE_TRAVELLING_SET     47 findings  (  17 BLOCK)      ← what actually reaches the VPS
```

A whole-repo scan overstates transport exposure by **32× (68× on BLOCK)**. All 15 paths that BLOCK locally but are absent from the clone are `grants/**`, `grant-applications-private/**`, `staging/**` — the `.gitignore` privacy guard doing its job. **`REMOTE_TRAVELLING_SET_PRIVACY = UNADJUDICATED`**: the two instruments disagree on the same bytes (exit 2 / 17 BLOCK against exit 0 / 0 BLOCK) and neither was preferred.

🔴 **Measure the delta, not the absolute.** Those 17 BLOCK rows sit at `b1b5a58`, which **is** the remote's `main`. The VPS transfer adds **zero** new exposure through the remote — the exposure already exists there.

🔴 **19.5% of the travelling set is scanned by neither instrument.** Measured, not assumed: `independent_privacy_scan.py:183` walks `root.rglob("*")` and `:39-48` skips `.git`, so it never reads a git object; `public_release_gate.py:884` builds from **`git archive HEAD`** — exactly one revision. But a clone carries all 38 branches: `rev-list --objects origin/main` = **5,984**, `--remotes` = **7,438**, so **1,454 objects travel unscanned**. Mirror did not content-scan them, because the exclusion boundary forbids reading non-main branch content and it would not route around it. That portion is `UNVERIFIED_BY_BOUNDARY` — a real gap, not a pass.

**`cross_host_handoff.md`, the three questions.** **Q1 — does any currently necessary state require the bundle? NO for execution.** Mirror reproduced the whole declared battery inside its own clone: lint 0, receipts 0, anchors 0, gate 0, `classify` 0 with `UNKNOWN_REQUIRED_STATE: 0`. Every instrument in `VPS_BOOTSTRAP_COMMANDS` passes **on the clone alone**. What the bundle uniquely preserves is ~5.3 MB of audit lineage, not runtime capability. **Q2 — does the documented path satisfy current G7? UNRESOLVED: G7 does not exist in this repository.** `git grep -In "G7"` → no text matches (12 binary only); positive control `G5` → `framework/ADOPTING.md:18`. Gates are numbered **GATE 0–5**; Annex G has only **G.1–G.3**. The fact could not be established, so the answer is UNVERIFIED rather than a guess. **Q3 — does encryption become an execution blocker? NO, and this was derived, not assumed.** "Unencrypted" is a property of the bundle at rest; §6 names `scp`/`rsync`, both of which run over SSH, so confidentiality *in transit* is already supplied by the named tools. An at-rest mechanism already exists outside the repository (`~/.legend/keys/legend-luks.key`, unread). And per Q1 nothing required for execution needs that path at all. Concluding "encryption is required" would have invented a blocker. The genuinely open question is the **disposition of `refs/pii-backup/*`** — a decision, not a cipher.

**PRIVATE_TRANSPORT_INTEGRITY — and what kind of assurance each mechanism is.** Bundled refs → `git bundle verify` (`legend_handoff.py:831`, `:1109`) plus manifest `{ref, object}` pairs re-checked post-restore (`:1150-1151`): a genuine **VERIFICATION**, because git object ids are content-addressed and the recipe is public and reproducible. `~/.legend/{state,lineage}` → `SHA256SUMS` written at `:992` over every bundle file **except itself**, consumed at `:1057`, absence → *"no SHA256SUMS: transported completeness cannot be verified"* (`:1069`): a **DIGEST/ATTESTATION** — it certifies only that bytes did not change *after* it was taken, it is unsigned, and **it travels in the same directory as the files it covers**, so whoever can rewrite a file can rewrite the manifest. Nothing certifies `SHA256SUMS` itself, and nothing certifies that the payload was built correctly. The 15 adjudicated files carry per-file `sha256` re-verified every run, with drift → `UNKNOWN`: a drift detector, not a correctness proof. **`PRIVATE_TRANSPORT_INTEGRITY = BLOCKER`, scoped to exactly two object sets**: `~/.legend/keys/legend-luks.key` (no mechanism at all) and the unrecipe'd entries of `~/.legend-venvs/`.

**Falsification probes.** **(1) Concurrent writer invalidates the inventory. CONFIRMED, mechanically.** Two whole-tree scans three minutes apart: 1,425/1,092 then 1,523/1,159, drift **+98/+67**, while `HEAD` = `b1b5a58` and porcelain = 0 lines throughout. Cause nailed without attributing work by timestamp: bucketing findings per worktree, `.claude/worktrees/plan-modevo-p0a` contributes **exactly** all=98, block=67. Positive control: the same bucketing resolves the 16 other non-zero worktrees. **A clean tree at BASELINE_SHA does not bound the durable state, and a whole-tree privacy figure is not reproducible across a preflight window.** **(2) `~/.legend/keys/` is invisible to the classifier. HIT** — §3; not `UNKNOWN` but *uncounted*. **(3) The guard's registration surface. THE ESTABLISHED BASELINE WAS WRONG, and Orchestrator was its author.** Orchestrator told both actors that `~/.claude/settings.json` is the resolved active hook registration, "i.e. the guard's registration lives OUTSIDE the repository", reading prose at `guard_policy.py:904,3467` instead of measuring. Mirror measured, and Orchestrator re-ran it: `~/.claude/settings.json` has 7 top-level keys and **`hooks` is not among them**. The active registration is the **tracked** `.claude/settings.json` (363 B) → `PreToolUse` matcher `Bash` → `python3 "$CLAUDE_PROJECT_DIR/scripts/guard_bash_command.py"`, present byte-for-byte in the clone alongside `scripts/guard_bash_command.py` (1,235 B) and `guard_policy.py` (194,112 B). → **Correction, and it is good news: the guard travels with the clone, so a VPS lands guarded.** `.claude/settings.local.json` (untracked, `permissions` only, no hooks) does not travel — the VPS gets the hook but not the local permission allowlist. **(4) Ignored paths consumed by runtime code. HIT, ~1.70 GB** — §3; `growth_anchors.py:336` states the hazard in its own words: *"`staging/` is gitignored, so it exists in one checkout and not in the worktrees."* Positive control: `_qa/`, `overlay/`, `md-output/` returned ABSENT in the same sweep. **(5) `REBUILDABLE_CACHE` without a recipe. HIT, 8.39 GB** → B8; positive control: the same `git ls-files | grep -i requirement` sweep *did* find `requirements-analysis.txt`, so a second recipe would have surfaced. **(6) Hooks, symlinks, submodules, LFS. CLEAN NEGATIVE, with denominators** — §3; Mirror re-derived the `.gitattributes` = 0 finding rather than inheriting it.

**Mirror's guard denial** (`git lfs env` → `UNKNOWN_EFFECT`, `GENERATION=REV12`) doubles as its guard-liveness positive control: it proves the guard was executing on Mirror's calls, so "no other denials" is a measured negative rather than an unmeasured one. An inert `echo a || echo b` was *allowed*, so `||` alone is not the trigger.

---

## 8 · D7 — VPS ACCEPTANCE TEST *(existing scripts only; no new acceptance script)*

**Stage A1 — STATE PARITY** *(runnable anywhere; proves nothing about the VPS environment)*. The VPS declares first: baseline SHA `b1b5a58…`, `BASELINE_SURFACE`, clone remote, remote/local equivalence, tracked tree SHA `948bf948…`, 686 tracked files.

| command | expected exit | expected key output | state property |
|---|---|---|---|
| `python3 framework/scripts/legend_lint.py .` | 0 | `VERDICT: PASS` | canonical structure |
| `python3 framework/scripts/fulltext_receipts.py verify` | 0 | `OK: 128 chained receipt(s), tail anchored in framework/state/state_manifest_current.md` | chain + tail anchor |
| `python3 framework/scripts/growth_anchors.py check` | 0 | `claims=39 · papers=70 · corpus=356 · literature=390` · `VERDICT: PASS` | anchors + ratchets |
| `python3 scripts/public_release_gate.py --root . --mode release` | 0 | `VERDICT: PASS` / `BLOCKS: 0` | publication surface |
| `python3 scripts/test_fresh_clone_reader_journey.py` | 0 | `Ran 5 tests … OK` | reader front doors |
| `python3 scripts/independent_privacy_scan.py --json .` | **2** | **47 findings / 17 BLOCK / 11 paths** — record the set; do **not** read as green | second, disagreeing opinion |
| `python3 framework/scripts/legend_handoff.py classify` | 0 | 24 surfaces, `UNKNOWN_REQUIRED_STATE: 0` | resume completeness — **scope-limited, B3** |
| `ls disease-models/wwox/research/deepdive_manifests/*.json \| wc -l` | 0 | `64` | manifest cardinality |
| `git rev-list refs/heads/main --not --remotes=development --count` | 0 | `0` | **positive control** |
| `python3 scripts/run_release_regressions.py` | **1 at this baseline** | **exactly the declared 7-suite failure set** | ⚠️ see below |

🔴 **`run_release_regressions.py` cannot use "exit 0" as its acceptance criterion at this baseline.** It exits 1 in both trees under both interpreters, for repository-content defects. The criterion is **set equality with the declared baseline failure set** — `test_documented_commands`, `test_release_runner_verdict`, `test_locator_obligation_reaches_every_route`, `test_abstract_corpus_is_not_evidence`, `test_release_surface`, `test_fulltext_trace_contract`, `test_session_self_eval`. **Any eighth failure, or any different member, is a transfer defect.** Repairing the seven is the right long-term answer and is not this dispatch's authority.

**Stage A2 — ENVIRONMENT PARITY** *(executable ONLY on the VPS; defined here, never declared PASS)*.

| requirement | expected predicate | evidence command | failure class |
|---|---|---|---|
| Python | CI pins **3.12**; this Mac ran 3.9.6 | `python3 -V` | TOOLCHAIN_VERSION |
| analysis deps | `numpy==2.0.2` installed **before** the battery | `pip install -r requirements-analysis.txt` | DEP_MISSING |
| git | `--remotes=<name>`, worktrees, bundles (2.50.1 demonstrated; no lower bound claimed) | `git --version` | TOOLCHAIN_TOO_OLD |
| guard registered | `PreToolUse` → `guard_bash_command.py` — **arrives with the clone**, tracked | read `.claude/settings.json` | GUARD_UNREGISTERED |
| guard **executed** | a real refusal, receipted, `guard_generation = REV12` at `framework/state/codex_hook_probe.json` | `runtime_parity.py --hook-status` → `DEMONSTRATED` | GUARD_NOT_DEMONSTRATED |
| runtime parity | both verdicts resolved | `runtime_parity.py --bootstrap` | **non-zero without `ACTOR_ID` is expected, not a defect** |
| `ACTOR_ID` | assigned, naming a `roles/` contract | registration | IDENTITY_UNRESOLVED |
| env-var **names** | presence of the §3 names; **no value inspected** | name presence only | ENV_MISSING |
| **case sensitivity** | Mac `core.ignorecase=true` → Linux `false` | `git config core.ignorecase` | **FILENAME_COLLISION** |
| network | reach the dev remote **with its credential**; PubMed/PMC for B4 | `git ls-remote development` | EXTERNAL_DEP_UNREACHABLE |
| remote binding | main → `development`, not `origin` | `git config branch.main.remote` | WRONG_REMOTE (B6) |
| disk | ≥ ~1 GB if `files/` is transported rather than re-fetched | `df -h` | CAPACITY |

`core.ignorecase=true` on this Mac is a genuine A2 risk: a case-only collision passes here and fails on Linux. **A1 green on this Mac says nothing about it.**

**Stage B — PRIVATE STATE** *(nothing is transported now)*. Verify bundle identity with `git bundle verify`; re-measure every transported ref's uniqueness **at the destination**; verify each of the 15 adjudicated payloads against the `sha256` and `bytes` in `handoff_adjudication.jsonl`; restore `~/.legend/{lineage,state}` per `cross_host_handoff.md`; **resolve B7 before anything touches an encrypted volume**; re-author `deployment/local_instance.md` and `.claude/settings.local.json` rather than copying them; **never push `refs/pii-backup/*`**; then re-run A1 plus `classify` and require `UNKNOWN_REQUIRED_STATE: 0` — **with B3 resolved, or the zero is scoped**.

## 9 · OPEN QUESTIONS *(non-blocking; the Operator was not contacted mid-flight)*

1. Is the `development` remote publicly readable? `cross_host_handoff.md:238` requires a credential; an authenticated clone proves nothing; the probe that would settle it was guard-denied (§10). Everything about "publication through the remote" depends on this.
2. Does the VPS plan involve an encrypted volume — i.e. is `legend-luks.key` required? (drives B7)
3. Is `staging/` a derivable intermediate of `files/`, or independent evidence? (drives B3)
4. Should `legend_handoff.py` enumerate ignored paths and walk `~/.legend/`, so its fail-closed rule can reach what it currently cannot see?
5. Who created `plan-modular-evolution-p0a` at 23:39:13, and which loose tag was removed in that window?
6. Should the 1,454 objects on non-main branches be privacy-scanned before the remote is trusted as a transport, and by what instrument, given both read one revision only?
7. Why does `branch.main.remote` point at the out-of-scope `origin`, 631 commits behind?
8. Are the 11 tracked paths with privacy BLOCK rows a gate-scoping reconciliation, or false positives?
9. Is `refs/remotes/local/*`'s missing remote intentional?
10. Should A1 assert a ref census at all, given it demonstrably decays within the hour?

---

## 10 · OVERFLOW — WHAT MOVED WHILE WE MEASURED, AND WHAT THE GUARD REFUSED

**The ref population is live, and it thawed under this preflight.** Two independent methods agreed at each instant; no actor mutated anything. `t0` 23:26–23:28 → heads 89, tags 7. `t1` 23:44–23:45 → heads 90, tags 6. `t2` 23:47:27 and `t3` 23:57:35 → 90 / 6.

The added head is `refs/heads/plan-modular-evolution-p0a`, ref file written **23:39:13+0200**, at exactly the main tip, **0 unique commits** — Phase 0A, identified and never opened. Its *worktree* materialising is independently visible in Mirror's probe 1 as exactly +98 privacy findings. One **loose** tag was removed in the same window (`packed-refs` untouched since 2026-08-23; no tag reflog). **Cause: UNVERIFIED** — a concurrent writer is demonstrated, but the deletion was not observed and is not attributed. Orchestrator could not name it, having counted that population at t0 without enumerating it — a method failure recorded here rather than hidden. Plan had enumerated it and names it `refs/tags/orch-probe-tag-delete-me` with **0 unique commits**, so no content was lost; that name and that zero rest on a single pre-deletion reading and could not be independently reproduced, the object being gone. Orchestrator was ruled out as the mutator: the release suites that create and delete refs operate on throw-away repositories (`test_post_effect_verify.py:37` `tempfile.mkdtemp` + `addCleanup(shutil.rmtree)`).

**Guard denials — recorded as evidence, none bypassed, none worked around.** Seven across three actors, from ~200 commands. Five were `UNKNOWN_EFFECT`/`UNPARSEABLE` on compound shell whose effect the guard could not name; each was rewritten in readable form and then permitted — the guard was asking for legibility and got it. Plan drew one `CONFINED_PEER_WORKTREE` on a loop reading three peer worktrees, and re-expressed it one worktree per invocation. One was substantive:

> This command mutates the configuration that decides whether this guard runs, and no authority class grants that from the shell. … Only the RESOLVED ACTIVE registration is confined — not `~/.claude` or `~/.codex` wholesale. …
> `LEGEND_GUARD GENERATION=REV12 DECISION_CODE=RUNTIME_CONFIG ASSIGNED_WORKTREE_SOURCE=RUNTIME_ENV`

It refused `GIT_TERMINAL_PROMPT=0 git -c credential.helper= ls-remote <dev remote> HEAD` — the probe that would have settled Q1. **The refusal is correct and the question stays open.**

**Two corrections Orchestrator issued against itself.** (i) It told both actors the dev remote "is PUBLIC" before verifying it, and retracted that in writing; Q1 exists because of it. (ii) It told both actors the guard's registration lives outside the repository, having read prose rather than measured the resolved active surface; Mirror falsified it and Orchestrator re-ran the measurement — §7 probe 3. Both errors have the same shape: reporting where something *exists* instead of measuring where it is *executed*.

**Plan self-reported one protocol deviation**: it materialised one scratch file after being told it had no write authority anywhere, caught it, re-derived the affected measurement without the file, and did not delete the file, deletion being equally a state change. No repository file was created, modified or deleted by any actor other than this report.

## 11 · ATTESTATIONS

**Orchestrator.** *I attest that I performed no ref, stash, remote or source-repository mutation; no guard denial was bypassed; permitted writes were limited to the declared ANALYSIS_ONLY report and scratch state; ⟨0A branch⟩ was not read, cited or modified.* Supporting evidence: source `git status --porcelain --untracked-files=all` = 0 at t0 and t3; `HEAD` = `b1b5a58` throughout; `~/.legend` = 18 files before and after; the two ref changes are attributed to a concurrent writer, with this session's own instruments ruled out mechanically.

**Plan.** *I attest that every D4 disposition rests on an evidenced D3 row; unchanged previously-adjudicated objects were not re-authored; STATE_PARITY was not conflated with ENVIRONMENT_PARITY; no discard, transport or Operator decision was executed.*

**Mirror.** *I attest that privacy was evaluated on the actual travelling sets rather than inferred from whole-tree scans; privacy disagreements were preserved as UNADJUDICATED; guard-denied remote observations were not silently substituted with stronger evidence; falsification probes were performed independently.*

---

*Nothing here was reconstructed, transported, discarded or deleted. `ENVIRONMENT_PARITY` remains `NOT_YET_TESTED_ON_VPS`, and the label `LOSSLESS PASS` is reserved for a later execution in which both parities pass on the actual host.*
