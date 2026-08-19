---
artifact: INTEGRATION_CANDIDATE — Orchestrator surface semantics
candidate_id: CAND-20260819-ORCHSURF
revision: 1
task_id: ORCHSURF-001
author: plan
authored_on: 2026-08-19
governance_version: 3.1.1
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1), so this
  file is outside the candidate content domain and cannot move the hash it records
partition: this is the SECOND half of the split declared in CAND-20260819-P5DOMAIN §9. P5 went
  first and is canonical. This candidate carries the Orchestrator surface debt and nothing else
scope_negative: Routing is NOT implemented. No resolver, no registrar, no actors.yaml, no routing
  generations, no CURRENT, no session elected, superseded or registered. Annex D.1 NOT modified.
  P5 NOT reopened. C-9 §7.2 NOT altered. Scientist A/B NOT activated. BENCH-AB-001 NOT started
human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists
---

# INTEGRATION_CANDIDATE — `CAND-20260819-ORCHSURF`

## 1 · Manifest (Annex D.2)

```
CANDIDATE_ID              CAND-20260819-ORCHSURF
BASE_HEAD                 04693e683a254ff0a6d0619fba47103a0fb7d122   (canonical main, verified
                                                                      from git at session open
                                                                      and again at binding)
SOURCE_COMMITS            b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2   CONTENT — the correction,
                                                                      the rule, and SLR-plan-0010
                          <this commit>                              CONTROL PLANE — this manifest
CONTENT_TIP               b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2
CANDIDATE_HASH_VERSION    legend-candidate-v4
CANDIDATE_CONTENT_HASH    3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7
                          534 included · 45 excluded
CHANGE_CLASS              MAJOR — it edits a role contract and the deployment profile, which is
                          governance (H.1: "Spese / MAJOR approval / governance → Operatore";
                          Annex G.1 MIRROR_REQUIRED). Classified MAJOR fail-closed; H.1 gives a
                          doubtful MAJOR classification to Mirror, not to the author
LINT_RESULT               PASS — 1 pre-existing INFO (MISSING_WIKILINK, CLAIM 010), on a
                          disease-model path this candidate does not touch
PUBLICATION_GATE          PASS / BLOCKS: 0
MIRROR_REVIEW             NOT PERFORMED — required, and not assumed
HUMAN_APPROVAL            n/a — not requested, not prefilled
SNAPSHOT_ID               n/a until canonical execution — GATE 4 belongs to Orchestrator
FINGERPRINT IMPACT        orchestrator  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
                                     →  42b8575c818d358c9469f277382b95c8ed73c4f75c76be06d975f716baf9908a
                          plan · mirror · scientist  UNCHANGED, byte-identical
```

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 04693e683a254ff0a6d0619fba47103a0fb7d122 \
  --tip  b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2
# 3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7
```

**Independent route.** The digest was also reproduced without trusting the script's own final
step, by re-digesting the published pre-image with a different tool:

```bash
python3 governance/scripts/candidate_content_hash.py --base … --tip … --emit-domain \
  | shasum -a 256
# 3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7   (57 588 bytes, 536 lines)
```

**Positive controls — two published values, authored by earlier sessions, reproduced here.**
This is what makes the instrument trustworthy rather than merely self-consistent:

```
CAND-20260819-P5DOMAIN  base f70878d1 tip ceefaa28  → 930dfefb…  MATCHES the published value
CAND-20260819-XPORT     base 4454feab tip e839db38  → 81f241f2…  MATCHES the published value
```

**Negative control — verified, not void.** The BASE_HEAD tree hashed under the same rule gives
`cfe8957d2de46acced711f9e31a3454e4d74a25d0a37e3f6edf5d5ecf34d1298`, which differs from this
candidate's value. The binding is sensitive to the change it claims to bind.

---

## 2 · What this candidate does, in one paragraph

`roles/orchestrator.md` said its worktree was the repository root checkout. That was true on
2026-08-16 and stopped being true on 2026-08-17. This corrects the label, gives the canonical
batch surface its own typed field so one untyped word stops naming two things, fixes the *same*
stale claim in `BOOTSTRAP.md` — where it is an instruction to a human rather than a description —
and states once, for every actor, that a working directory cannot establish who an actor is.
It records five requirements for a future resolver and builds none of them.

---

## 3 · Execution was never ambiguous — Annex D.1 is correct and untouched

```
WORK_COMMIT              ogni attore, proprio branch — obbligatorio, non canonico
CANONICAL_BATCH_COMMIT   solo Orchestrator, root, gate 0–5
```

`governance/annex_d_commit_batch.md` is `status: FROZEN`, `normative: yes`, and sits at rank 1 of
body §5 against a role contract's rank 4. Both clauses bind Orchestrator and they name different
surfaces deliberately.

```
ORCHESTRATOR EXECUTION AMBIGUITY   NO
ANNEX D.1                          CORRECT — NOT MODIFIED
WORK_COMMIT SURFACE                the `orchestrator` worktree, branch `orchestrator`
CANONICAL_BATCH_COMMIT SURFACE     the root checkout, branch `main`, batch window only
```

**Independent confirmation that the root cannot be the Orchestrator's home**, derived from a
different rule than the one that says so: `D.3 GATE 0` requires *"root clean"*. An actor resident
in the root is a standing writer there, so GATE 0 would fail from that actor's first durable
output onward. The architecture forbids the arrangement twice, from two directions.

---

## 4 · The label was stale, and the file's own body already refuted it

`roles/orchestrator.md` has been touched **exactly once** in its history — `a8cd125`, 2026-08-16,
the original materialization. `e861dc4`, 2026-08-17, *"The Orchestrator gets a worktree, on its own
branch and nothing else"*, changed **one file**: `deployment/deployment_profile.md`. Both commits
are ancestors of `main`; a non-ancestor was checked as a control to confirm the test discriminates.

```
ORCHESTRATOR ROLE/FRONTMATTER LABEL   STALE — accurate when written, overtaken and never revisited
ORCHESTRATOR ROUTING-SURFACE AMBIGUITY  CONFIRMED
```

The same file's body already contradicted its own frontmatter, twice:

> *"**Position in the root confers nothing.** … A chat that opens in the root and finds a valid
> ACTIVE lease is **not** Orchestrator; it is an OBSERVER."*

> *"**Orchestrator must not:** … treat the root as free working space."*

**The `worktree:` field was type-inconsistent.** Every other contract carries a bare worktree
name — `plan → evidence-index`, `mirror → mirror`, `scientist → {lettore, lettore-b, lettore-c}`.
Only Orchestrator carried a prose phrase, and only Orchestrator has two surfaces to name.

### 🔴 4.1 · A second site, not previously named — and it instructs rather than describes

`BOOTSTRAP.md` carried the same stale row, in the table headed **"The chats to open"**. That table
tells a human where to open each actor's chat when standing the laboratory up from nothing.

**A fresh bootstrap against that table would have put the Orchestrator back in the root**,
restoring the standing writer that `e861dc4` removed and that `GATE 0` requires absent. The defect
was not cosmetic and it was not inert: it was one bootstrap away from re-executing itself. This is
offered to Mirror as the strongest argument that the correction is worth a MAJOR, and as the fact
that most changes the prior session's ordering rationale.

---

## 5 · Three concepts, and the one that gets no filesystem attribute

```
1. ACTOR WORK SURFACE       per-actor, named by `worktree:` in every contract
2. CANONICAL BATCH SURFACE  Orchestrator only, named by `canonical_batch_surface:`
3. ROUTING / DISCOVERY      NO filesystem attribute — the candidate declines to create one
```

`worktree:` keeps exactly one meaning across all four contracts — *the actor's work surface*. The
second concept gets its own field in the one contract that has one. **The three ordinary contracts
are not touched**, which is deliberate: their `ACTOR_ID ↔ worktree` mapping was never ambiguous,
and flattening a real asymmetry to make the schema uniform would be a second error. It also holds
the blast radius to one fingerprint.

---

## 6 · The measurement — why cwd cannot carry concept 3

```
INSTRUMENT     claude agents --json --cwd <path>
VERSION        2.1.232 (Claude Code)
SCOPE          local runtime instance, this machine
TIMESTAMP      2026-08-19T21:02Z
MODE           read-only enumeration; no session elected, superseded or written
```

| Query cwd | Sessions | Composition |
|---|---|---|
| root | **17** | 5 root · 10 `mirror` · 1 `lettore-c` · 1 `evidence-index` |
| `orchestrator` worktree | **0** | — |
| `evidence-index` — POSITIVE CONTROL | **1** | the query can return non-zero |
| `mirror` — second POSITIVE CONTROL | **10** | — |
| nonexistent path — NEGATIVE CONTROL | **0** | — |

```
ROOT-CWD DISCOVERY                17   (CLI 2.1.232)
ORCHESTRATOR-WORKTREE DISCOVERY   0    (CLI 2.1.232)
POSITIVE CONTROL                  plan / evidence-index / 1 · mirror / mirror / 10
ROOT-CWD INTERPRETATION           OVER_BROAD_FOR_ACTOR_DISCRIMINATION
CWD AS ROUTING ATTRIBUTE          PROHIBITED as an actor-identity discriminator
```

### 6.1 · 🔴 A correction to a canonical candidate's reasoning — its conclusion stands

`CAND-20260819-P5DOMAIN` §8.3 argued the root reading is useless because *"every worktree lives
under the root at `.claude/worktrees/`"*, calling it *"the universal set shaped like one"*.

**The conclusion is right and the reason is false.** Measured on this machine: **7 of 14 worktrees
are outside the root** — four `legend-codex-*` checkouts and three scratchpad worktrees. The true
statement is the narrow one:

```
NAMED ACTOR WORKTREES UNDER ROOT   6/6
UNIVERSAL "every worktree is under root"   FALSE
```

Both support the same conclusion by different routes, so nothing downstream of P5DOMAIN moves.
But a reader who accepted the universal would think containment is a structural guarantee of the
repository, when it is a fact about where six worktrees happened to be created. **This candidate
does not edit P5DOMAIN**; the correction is recorded here and in `SLR-plan-0010` L-3, and Mirror
decides whether the canonical text needs its own remedy.

### 6.2 · Two further reasons, independent of breadth

- **The runtime exposes no identity.** A session carries `cwd`, `kind`, `name`, `pid`,
  `sessionId`, `startedAt`. No actor field, no role field. There is nothing to read.
- **`name` is a function of `cwd`** — verified 17/17, with a negative control matching nothing.
  Keying on both looks like corroboration and is one attribute counted twice.
- **The zeros are ambiguous.** The `orchestrator` worktree exists and returned 0; a path that does
  not exist also returned 0. The instrument cannot separate *unoccupied* from *absent*.

---

## 7 · Remediation classes considered

| | Class | Verdict |
|---|---|---|
| A | role-label correction alone | **insufficient** — corrects one site, leaves `worktree` untyped, and leaves the root-cwd reading available to the next resolver |
| B | typed-surface semantics alone | **insufficient** — types the fields but leaves BOOTSTRAP instructing the old arrangement |
| C | cwd-nonauthoritative rule alone | **insufficient** — states the prohibition while the contract keeps asserting the thing it prohibits |
| **D** | **A + B + C, each minimal** | **SELECTED** |
| E | rename `worktree:` in all four contracts | **rejected as more change than the evidence supports** — rotates four fingerprints to fix an ambiguity that exists in one contract |

```
SELECTED REMEDIATION CLASS   D — combination, minimal in each part
PROBLEM SOLVED               the stale label at both sites; the untyped word; the availability of
                             cwd as an identity discriminator
GUARANTEE PROVIDED           a future resolver cannot read a canonical-execution surface as an
                             actor home, and cannot read any filesystem location as identity
WHAT REMAINS UNSOLVED        which session is CURRENT for an ACTOR_ID. Untouched, and four holds
                             still block it
BLAST RADIUS                 3 content files, 1 SLR, 1 fingerprint
BACKWARD COMPATIBILITY       no rule changes; no published hash moves; no executing behaviour
                             depends on the corrected line
WHY LESS IS INSUFFICIENT     rows A–C above
WHY MORE IS UNNECESSARY      row E; and Annex D.1 already settles execution correctly
```

---

## 8 · Authority

```
FROZEN GOVERNANCE CHANGE REQUIRED   NO
ANNEX D.1 MODIFIED                  NO   (FROZEN, verified correct)
ANNEX H.1 MODIFIED                  NO   (FROZEN)
```

Both edited governance artifacts are `status: PROPOSED`, and `roles/` and the deployment profile
are Plan's to maintain under its own mandate. The route is unchanged and verified against H.1:

```
plan proposes  →  mirror reviews  →  operator approves (governance, MAJOR)  →  orchestrator
canonicalizes under an ACTIVE lease and gates 0–5
```

Plan does not execute this. GATE 1 keeps proposer and executor distinct.

---

## 9 · Hostile tests

| | Test | Expected | Result |
|---|---|---|---|
| T1 | can a non-Orchestrator session satisfy the stale root-cwd reading? | YES (proving it unsafe) | **PASS** — 12 of 17 are demonstrably other actors; the remaining 5 sit at the root and are mutually indistinguishable |
| T2 | does occupying the `orchestrator` worktree confer authority? | NO | **PASS** — authority needs the assigned role + an ACTIVE lease; ACTIVE by derivation is 0 |
| T3 | can an authorized Orchestrator batch in root without changing its work surface? | YES | **PASS** — root at `main`/clean and the `orchestrator` branch at `b3596d5` coexisted across the real canonical batch `04693e6` |
| T4 | do ordinary-actor semantics stay coherent? | YES | **PASS** — `roles/plan.md` unmodified, plan fingerprint byte-identical, `worktree: evidence-index` still names its work surface |
| T5 | does the candidate select a CURRENT session? | NO | **PASS** — 0 UUID-shaped strings added; every routing-vocabulary match in the diff is a *prohibition*, not an implementation |
| T6 | does it require `claude agents --json` as the identity definition? | NO | **PASS** — the tool appears twice: once as a dated measurement, once inside requirement 5, which excludes it from the ontology |

```
WRONG-REASON LOAD-BEARING PASSES   0
```

Every load-bearing probe carried an expected value, a positive control and, where meaningful, a
negative control. Four would have passed for the wrong reason and were caught: an empty
`git diff` that was empty because a merge tree is identical to its branch tip rather than because
nothing changed; a blank session count produced by a missing interpreter rather than by an empty
result; a `grep -L` "failure" that was `roles/scientist.md` using the plural key; and the inherited
universal-containment claim in §6.1.

---

## 10 · Routing holds — accounting only, nothing lifted

```
C-9 §7.2                              OPEN — HUMAN_REQUIRED. Untouched
BUILD_MINIMAL_DIRECTORY               OPEN — framework/state/actors.yaml still ABSENT at main,
                                      Phase 0 never executed. Verified this session
MULTI_AGENT_ARCHITECTURE_FEASIBILITY  OPEN — PRESERVED, NOT AUTHORIZED, NOT STARTED
E5                                    PARTIALLY_RESOLVED — unchanged by this candidate
ORCHESTRATOR SURFACE                  RESOLVED_BY_CANDIDATE_IF_CANONICAL
ROUTING READY FOR CANDIDATE B         NO — three holds remain, none of which Plan may discharge
```

**Candidate B is not opened here.**

---

## 11 · Requirements for a future resolver — requirements only

Recorded in `deployment/deployment_profile.md`. Restated for the reviewer:

1. `ACTOR_ID` is stable and never inferred from a path, a session name, or a `pid`.
2. `ROOT CHECKOUT != ORCHESTRATOR IDENTITY`.
3. `DEDICATED WORKTREE != CURRENT/ROUTABLE`.
4. `MANUAL OPERATOR SELECTION != CANONICAL ROUTING`.
5. The identity model must not be defined by `claude agents --json`, which is an observed runtime
   adapter surface and must be replaceable without changing the ontology.

---

## 12 · Residual, reported and not edited

`runtime/agent_card_registry.md` on branch `orchestrator` carries `WORKTREE: the root checkout
# branch main`. It is runtime state on another actor's branch, it is not canonical, and Plan may
not touch another actor's worktree. **Orchestrator owns it.** It is named here so the correction
is not mistaken for complete.
