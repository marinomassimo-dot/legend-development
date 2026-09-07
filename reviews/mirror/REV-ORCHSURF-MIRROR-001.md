---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-ORCHSURF-MIRROR-001
object: CAND-20260819-ORCHSURF · CANDIDATE_CONTENT_HASH 3af61c6d…4c7 @ BASE_HEAD 04693e68
  CONTENT_TIP b3afdde4 · MANIFEST_TIP c930889c · branch `orchestrator-surface`
level: R4 (MIRROR_REQUIRED — Annex G.1: governance artifacts, MAJOR; C.1 floor R4 METHOD)
reviewer: mirror
author: plan
adjudicator: orchestrator (C.3) · HUMAN_APPROVAL operator (H.1, MAJOR/governance) — none granted,
  none implied, none prefilled by this review
date: 2026-08-19
scope: Orchestrator work/batch/routing-surface semantics ONLY. Routing, Candidate B, C-9 §7.2,
  the `runtime/` classification, Scientist activation and BENCH-AB-001 were NOT reviewed as if
  this object canonicalized them, because it does not.
supersedes: nothing. First review of this object.
verdict: REQUEST CHANGES — every measurement in the candidate reproduces, the binding holds by
  four routes, Annex D.1 is untouched and correct, and the cwd rule is precise. But the candidate's
  own strongest claim — that the BOOTSTRAP defect is repaired — does not survive tracing. FROZEN
  Annex I.2 and two unmodified passages of `BOOTSTRAP.md` still terminate a fresh bootstrap with
  the Orchestrator resident in the root, and the candidate never mentions Annex I.2.
governance_loaded: 3.1.1 · mirror fingerprint e01b4108…0412 at BASE_HEAD and e01b4108…0412 at the
  candidate content tip — byte-identical; this candidate does NOT rotate my own fingerprint
reviewer_runtime: this session's owning process image is
  `anthropic.claude-code-2.1.233-darwin-arm64`. The measurement instrument used below is the
  PATH binary, `claude` 2.1.232 — the SAME version Plan measured on. Session runtime and
  instrument version are different facts and are kept apart.
---

# The table was corrected and the instruction underneath it was not

**One sentence.** Everything this candidate measured I re-measured and got the same structure,
the binding reproduces by four independent routes, and Annex D.1 is verified correct and
byte-identical — but the finding the candidate offers as its strongest, the `BOOTSTRAP.md`
counterfactual, is repaired in the row it names and left standing in the two passages that
actually execute it, one of which is FROZEN and outranks everything the candidate wrote.

**VERDICT TRANSFER: NONE.** No value below was taken from the manifest, the handoff, the SLR or
the prompt. Every hash, count and fingerprint was recomputed from explicit commit SHAs in detached
checkouts created for this review.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd                 <REPO_ROOT>/.claude/worktrees/mirror
git top-level       identical to pwd                                    PASS
branch / HEAD       mirror / 9d911449                                    clean
roles/mirror.md     read in full — ACTOR_ID mirror, PERSISTENT_LEGEND_ACTOR,
                    worktree `mirror`, candidate-review authority under Annex C.2/G.1,
                    E.2 epistemic curation, E.6 SLR obligation
CANONICAL MAIN      04693e683a254ff0a6d0619fba47103a0fb7d122 — VERIFIED from git, not from
                    the prompt
CORE FINGERPRINT    mirror e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412
                    recomputed at BASE_HEAD and at the candidate; byte-identical
CURRENT/ROUTABLE    NOT inferred. No lease claimed. ACTIVE by derivation = 0
```

---

## 1 · Candidate object — binding VERIFIED, four routes

```
BASE_HEAD               04693e683a254ff0a6d0619fba47103a0fb7d122
CONTENT_TIP             b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2
MANIFEST_TIP            c930889cc0bc000550976a57b3b961846ca282d1
CANDIDATE_CONTENT_HASH  3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7
```

| Route | Result |
|---|---|
| canonical `candidate_content_hash.py --base --tip` | `3af61c6d…4c7` **MATCH** |
| independent pre-image `--emit-domain \| shasum -a 256` | `3af61c6d…4c7` **MATCH** · 57 588 bytes, 536 lines |
| positive control — `CAND-20260819-P5DOMAIN` (f70878d1→ceefaa28) | `930dfefb…6b97` **matches the published value** |
| positive control — `CAND-20260819-XPORT` (4454feab→e839db38) | `81f241f2…6e1f` **matches the published value** |
| negative control — base tree against itself | `cfe8957d…1298` ≠ candidate hash — **verified, not void** |

The branch is linear: `04693e68 → b3afdde (content) → c930889 (manifest) → 71fadeb (handoff)`.

```
BINDING   PASS
```

---

## 2 · STEELMAN — what this candidate gets right, before any objection

**This is a disciplined, unusually honest candidate, and four of its choices are better than the
obvious alternatives.**

1. **It refused to touch Annex D.1, and it was right.** D.1 is `FROZEN`, `normative: yes`, rank 1
   under body §5 against a role contract's rank 4. I verified the blob is byte-identical at
   BASE_HEAD, at the content tip and at the package tip (`23895689…`), and that the only
   `governance/` change across the whole candidate is the new manifest file. Execution genuinely
   was never ambiguous, and a candidate that had "clarified" D.1 would have damaged working law.

2. **It correctly identified that no executing path was at risk — and I confirmed this
   independently and harder than it did.** `launch/legend_launch.sh` is the only launcher, and it
   reads no role contract, no `BOOTSTRAP.md` and no deployment profile: actor and worktree are
   **caller-supplied parameters** ("this script holds no actor table"). The only code that touches
   `roles/orchestrator.md` is `governance_fingerprint.py`, which hashes bytes. So the stale line
   changed a fingerprint and nothing else. `EXECUTION AMBIGUITY: NO` is correct.

3. **The cwd rule is precisely scoped, and I tried to break it.** The operative sentence is
   *"working directory is evidence about an environment. It is prohibited as an actor-identity
   discriminator, and it may not establish `ACTOR_ID`, authority, or which session is current.
   Neither presence in the root nor presence in an actor's own worktree establishes anything **by
   itself**."* Three establish-verbs and the qualifier "by itself" — it forbids cwd as an identity
   *source* and leaves it available as a *corroborating consistency constraint*. Requirement 1
   says ACTOR_ID is never *inferred* from a path, which is derivation, not comparison. Nothing
   here forbids a future resolver from checking an observed cwd against an independently governed
   actor↔worktree binding.

4. **It corrected an inherited false premise while leaving the conclusion it supports standing,
   and said so.** P5DOMAIN §8.3 argues from *"every worktree lives under the root"*. That is
   false — I measured 14 worktrees, 7 under root, 7 outside. The narrow claim (6/6 named actors)
   is true and supports the same conclusion. The candidate does not repeat the false premise
   anywhere; it repudiates it in both edited files. That is the harder and more honest move.

5. **Declining to rename `worktree:` in the other three contracts is right, and the candidate
   under-argued its own case.** Plan justified it by blast radius. The stronger justification is
   mechanical: before the change `worktree:` held a *prose phrase* in orchestrator and a *bare
   name* in plan and mirror; after the change it is a bare name in all three. The candidate makes
   the shared field **more** uniform, not less, and adds one optional key to the one contract that
   needs it. I parsed all four frontmatters as YAML — all four parse; `worktree` is now
   `'orchestrator'`, a plain string. The pre-existing non-uniformity is `roles/scientist.md`,
   which uses plural `actor_ids`/`worktrees`, and the candidate neither creates nor worsens it.

---

## 3 · Execution / label / bootstrap — the three questions, not collapsed

```
EXECUTION AMBIGUITY                 NO   — Annex D.1 settles it; no executing path reads the label
LABEL AMBIGUITY                     YES  — one untyped word named two surfaces for one actor
BOOTSTRAP OPERATIONAL CONTRADICTION YES  — and it SURVIVES this candidate (§5)
```

**Annex D.1, verified rather than accepted:**

```
WORK_COMMIT              ogni attore, proprio branch — obbligatorio, non canonico
CANONICAL_BATCH_COMMIT   solo Orchestrator, root, gate 0–5
status: FROZEN · normative: yes · body §5 rank 1 vs role contract rank 4
```

```
ANNEX D.1   CORRECT — NOT MODIFIED (blob 23895689… identical at base, content tip, package tip)
```

**History, reconstructed independently.** `roles/orchestrator.md` has been touched **exactly
once** in its life: `a8cd125`, 2026-08-16, the original materialization. `e861dc4`, 2026-08-17,
*"The Orchestrator gets a worktree, on its own branch and nothing else"*, changed **one file** —
`deployment/deployment_profile.md`. Both are ancestors of main.

```
ROLE/FRONTMATTER STALE               CONFIRMED
STALE DUE TO ARCHITECTURE EVOLUTION  CONFIRMED
```

---

## 4 · 🔴 BLOCKING — B-1 · `BOOTSTRAP.md` can still recreate a standing root Orchestrator

The candidate offers §4.1 as *"the strongest argument that the correction is worth a MAJOR"*, and
the handoff invites attack at exactly this point: *"is the bootstrap path actually reachable, and
does anything else downstream correct the operator before damage?"*

**I traced it. The path is reachable, nothing downstream corrects it, and the candidate repairs
the row it names while leaving the two passages that actually execute the arrangement.**

### 4.1 · FROZEN Annex I.2 mandates the arrangement the candidate forbids

`governance/annex_i_bootstrap_deployment.md` is `status: FROZEN`, `normative: yes`, and is a
fingerprint input for orchestrator. § I.2 · *Protocollo BOOTSTRAP_CONTROLLER*:

```
1.  prima chat in <REPO_ROOT> → CLAUDE.md → nessun lease ACTIVE → BOOTSTRAP_MODE
4.  crea/verifica worktree: lettore, lettore-b, lettore-c, evidence-index, mirror
6.  presenta all'operatore la LISTA ESATTA delle 5 chat da aprire (path per ACTOR_ID)
9.  condizioni PASS → acquisizione ORCHESTRATOR_LEASE (I.3)
10. ORCHESTRATOR_REGISTRATION durevole → ACTIVE_ORCHESTRATOR → governance ordinaria
```

Step 1 puts the controller in the root. Step 4 creates **five** worktrees and `orchestrator` is
not among them. Step 6 says the exact list is **five** chats — because the sixth is already open,
in the root. Steps 9–10 promote that same chat, in place, to `ACTIVE_ORCHESTRATOR`.

### 4.2 · Two passages of `BOOTSTRAP.md` the candidate did not touch

Both verified unmodified at CONTENT_TIP `b3afdde`:

- **lines 31–35** — *"The chat that opens at the repository root … is **promoted** to Orchestrator
  … **The same chat is promoted — you do not need to open a second one.**"*
- **lines 57–58, step 3** — *"Create or verify the worktrees — one per actor, each on its own
  branch: `lettore`, `lettore-b`, `lettore-c`, `evidence-index`, `mirror`."* — five, omitting
  `orchestrator`.

### 4.3 · The operational consequence

A chat's working directory is fixed at session start; it cannot be relocated. So *"the same chat
is promoted — you do not need to open a second one"* is operationally identical to *"the
Orchestrator stays in the root."* The reading that would save that sentence requires the very act
it denies.

Therefore, after this candidate:

| | Outcome |
|---|---|
| A fresh bootstrap followed literally | still ends with `ACTIVE_ORCHESTRATOR` resident in the root |
| The corrected table at line 86 | points at worktree `orchestrator`, which **step 3 never creates** |
| `BOOTSTRAP.md` line 34 vs the candidate's new line 93 | direct self-contradiction inside one file |
| FROZEN Annex I.2 steps 4 & 6 vs the corrected 6-row table | contradiction, and under body §5 **the annex wins** |

A bootstrap controller reads line 34 in the section headed *"The one thing to understand before
anything else"* and acts on it long before reaching line 93.

### 4.4 · Why this is blocking rather than carried

The candidate does not merely leave this undone — **it asserts it is done.** Manifest §4.1: *"A
fresh bootstrap against that table **would have** put the Orchestrator back in the root"* (past
conditional). §7 `GUARANTEE PROVIDED`. SLR L-2: *"A fresh bootstrap performed against the file
**as it stood** would have placed the Orchestrator in the root."* And the candidate contains
**zero** references to Annex I.2 — I grepped the manifest, the full diff and the SLR; the only
Annex I hits are I.3, the lease.

This is precisely the §26 trigger: *BOOTSTRAP remains capable of recreating standing root
Orchestrator.*

```
BOOTSTRAP STALE INSTRUCTION                CONFIRMED
POTENTIAL TO RECREATE INVALID ROOT WRITER  CONFIRMED — and NOT discharged by this candidate
```

### 4.5 · The remedy is available and is not "modify FROZEN text"

Plan was right not to touch Annex I.2. `BOOTSTRAP.md` is `status: PROPOSED`, not FROZEN, and the
Orchestrator's own `runtime/runtime_inventory.md` finding **C-4** already records that
*"`BOOTSTRAP.md` is `PROPOSED`, not `FROZEN`, so it can be renumbered to match Annex I.2 without
touching frozen text."* What ORCHSURF needs is:

1. lines 31–35 and step 3 corrected so the promoted Orchestrator does not remain the root chat and
   the `orchestrator` worktree is actually created; **and**
2. the residual against FROZEN Annex I.2 steps 4 and 6 **declared, owned and given a convergence
   route** — exactly the treatment §12 already gives the agent-card residual.

Item 2 is not optional, because BOOTSTRAP.md alone cannot win against a rank-1 FROZEN annex.

### 4.6 · The irony, recorded because it is the useful part

SLR L-2's own lesson is *"the finding is **the claim**, not **the line**. Grep the claim across the
tree before proposing the fix."* The session applied that once — finding the second site — and
stopped. The claim was also live in the same file's lines 31–35 and step 3, in FROZEN Annex I.2
steps 4 and 6, and in `runtime/runtime_inventory.md`. **L-2 is a correct lesson that this very
session under-applied**, and that is worth more than the lesson stated alone.

---

## 5 · Runtime discovery — re-measured, structure reproduces, counts do not

```
INSTRUMENT   claude agents --json --cwd <path>   (PATH binary)
VERSION      2.1.232 (Claude Code)  — same version Plan measured on
SESSION RT   2.1.233 (this review's owning process image) — a DIFFERENT fact, kept apart
CWD          <REPO_ROOT> and its worktrees
MODE         read-only enumeration; no session elected, superseded or written
TIMESTAMP    2026-08-19T21:23:08Z
```

| Query cwd | Plan (21:02Z) | Mirror (21:23Z) |
|---|---|---|
| root | 17 | **8** |
| `orchestrator` worktree | 0 | **0** |
| `evidence-index` — positive control | 1 | **1** |
| `mirror` — positive control | 10 | **1** |
| `lettore-c` | 1 | **1** |
| nonexistent path — negative control | 0 | **0** (`[]`, exit 0) |

Counts are observational and moved, as the brief anticipated. **Every structural claim reproduced
exactly:**

- **Field set is identical to Plan's, exhaustively:** `cwd`, `kind`, `name`, `pid`, `sessionId`,
  `startedAt`. Union over all returned sessions. **No actor field, no role field.**
- **Root composition:** 5 sessions *at* root, plus 1 each from `lettore-c`, `evidence-index`,
  `mirror`. Plan measured the same 5-at-root.
- **`--cwd` is documented by the tool itself** as *"Show only background sessions started **under**
  \<path\>"* — subtree semantics confirmed from the instrument, not inferred.
- **The zeros are ambiguous:** the `orchestrator` worktree exists and returns `[]`; a nonexistent
  path returns `[]`, exit 0. The instrument cannot separate unoccupied from absent.

```
EXPLICIT ACTOR_ID FIELD   NOT_OBSERVED_VIA(claude agents --json, CLI 2.1.232)
```

Stated instrument-bound, as required — not as universal impossibility.

### 5.1 · `name` is a function of `cwd` — reproduced

Every returned session satisfies `name == <cwd-leaf>-<2 hex>`: **8/8** (Plan: 17/17).
`legend-public-12`, `legend-public-cf`, `legend-public-54`, `legend-public-c4`, `legend-public-43`,
`lettore-c-b2`, `evidence-index-2c`, `mirror-b7`.

```
NAME INDEPENDENT OF CWD   NO  (instrument-bound: CLI 2.1.232)
```

The only non-derived component is a 2-hex disambiguator. A resolver keying on cwd *and* name
corroborates nothing — it is one attribute counted twice. **Not two independent confirmations.**

### 5.2 · Worktree containment — both counts verified

```
ALL WORKTREES UNDER ROOT       7/14
NAMED ACTOR WORKTREES UNDER ROOT   6/6
```

The 7 outside: four `legend-codex-*` checkouts and three scratchpad worktrees. The candidate does
**not** preserve the false universal; it states 7-of-14 and 6/6 explicitly in both edited files.

---

## 6 · P5DOMAIN §8.3 — carried debt, correctly quarantined

Canonical text at main: *"`--cwd` matches a subtree, and **every worktree lives under the root at
`.claude/worktrees/`**. The root reading is … the universal set shaped like one."*

```
P5DOMAIN §8.3 PREMISE      FALSE  — 7 of 14 worktrees are outside the root; the root checkout
                                   itself is a worktree and is not under `.claude/worktrees/`
P5DOMAIN §8.3 CONCLUSION   TRUE   — still supported by the narrower 6/6 named-actor fact, which
                                   I verified returns 3 other actors' sessions from a root query
P5DOMAIN §8.3 DISPOSITION  CARRIED_DEBT — separate truthfulness debt, NOT load-bearing to ORCHSURF
```

ORCHSURF does not repeat the false premise and is not contaminated by it. **I do not require
ORCHSURF to edit P5DOMAIN**, and I record the debt here as its own item. Note it is the second
consecutive review to find an unmarked falsified sentence left standing in a canonical section —
`REV-P5DOMAIN-MIRROR-001` made the same class of finding about the same document.

---

## 7 · Three surfaces — PASS

```
A · ACTOR WORK SURFACE       `orchestrator` worktree, branch `orchestrator`   DETERMINISTIC (D.1)
B · CANONICAL BATCH SURFACE  root checkout, branch `main`, batch window only  DETERMINISTIC (D.1)
C · IDENTITY / ROUTING       NOT derived from A or B alone — no filesystem attribute at all
```

The candidate nowhere implies `A == B`, and nowhere implies `B` proves identity. It states the
opposite explicitly: *"being in the root does not make a session Orchestrator, and being in the
`orchestrator` worktree does not make a session Orchestrator either."*

```
WORK/BATCH SURFACE DISTINCTION   PASS
```

**§15 canonical-batch asymmetry — verified live.** Root is on `main` at `04693e6`, clean; the
`orchestrator` worktree is on branch `orchestrator` at `b3596d5`. Both coexisted across the real
canonical batch. An already-governed Orchestrator can `WORK_COMMIT` on its own branch and later
execute an authorized `CANONICAL_BATCH_COMMIT` in root **without any change of ACTOR_ID**. Ordinary
actors are correctly not given a second surface.

---

## 8 · Hostile tests T1–T6 — independently re-run, reasons checked

| | Test | Result | **Reason verified** |
|---|---|---|---|
| T1 | can a non-Orchestrator session satisfy the stale root reading? | **PASS** | 3 of 8 root-query hits are demonstrably other actors (`lettore-c`, `evidence-index`, `mirror`); the 5 at root differ only by pid/sessionId/startedAt/name-suffix — mutually indistinguishable on any governed attribute |
| T2 | does occupying the `orchestrator` worktree confer authority? | **PASS** | `lease_state.py --check`: **ACTIVE by derivation = 0**, across 5 recorded leases (2 STALE, 3 RELEASED). Authority needs assigned role + ACTIVE lease; neither follows from location |
| T3 | can an authorized Orchestrator batch in root without changing its work surface? | **PASS** | root `main`@`04693e6` clean **and** `orchestrator`@`b3596d5` observed coexisting, live |
| T4 | do ordinary-actor semantics stay coherent? | **PASS** | `git diff` over `roles/` shows only `roles/orchestrator.md`; plan/mirror/scientist fingerprints byte-identical; all four frontmatters parse as YAML |
| T5 | does the candidate select a CURRENT session? | **PASS** | 0 UUID-shaped strings added; `framework/state/actors.yaml` ABSENT; I read every routing-vocabulary hit in the added lines — **all 11 are denials, prohibitions or requirement statements. Zero mechanisms** |
| T6 | does it require `claude agents --json` as the identity definition? | **PASS** | the tool appears as a dated measurement and inside requirement 5, which explicitly excludes it from the ontology: *"must survive its replacement"* |

```
WRONG-REASON LOAD-BEARING PASSES   0   (T1–T6 all pass for their stated reasons)
```

**Recorded separately, not counted as a T-test failure — manifest §3's "independent
confirmation".** It argues *"an actor resident in the root is a standing writer there, so GATE 0
would fail from that actor's first durable output onward."* As stated that is lossy: committed
output leaves root clean. The sound version is the one already canonical at BASE in
`deployment/deployment_profile.md` — an Orchestrator in root has **no branch on which a
`WORK_COMMIT` is possible**, since root is `main` and a commit to `main` is canonical by
definition; therefore its output cannot become durable and root stays dirty. The candidate
**inherited** this argument rather than inventing it, and dropped the load-bearing middle step in
compression. Not a defect I block on; the conclusion is correct by the stronger route.

---

## 9 · Fingerprint impact — recomputed, blast radius justified

```
                    BASE_HEAD 04693e68                                                  CANDIDATE
orchestrator  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
           →  42b8575c818d358c9469f277382b95c8ed73c4f75c76be06d975f716baf9908a
plan          0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429   UNCHANGED
mirror        e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412   UNCHANGED
scientist     b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a   UNCHANGED
```

Both published values reproduce exactly. **Changed input: exactly one** — of the 16 orchestrator
fingerprint inputs, only `roles/orchestrator.md` moved. `BOOTSTRAP.md` and
`deployment/deployment_profile.md` are **not** fingerprint inputs, so the two larger edits rotate
nothing. § P2.2 composition is byte-identical: the candidate changed no fingerprint *composition*.

**A.6 consequence:** only orchestrator checkpoints are invalidated for resume. Plan, Mirror and
Scientist checkpoints remain compatible. This is the narrowest possible blast radius consistent
with correcting the contract, and it is a point in the candidate's favour.

---

## 10 · Gates, LINT, regression

```
LINT @ candidate     PASS — 1 INFO (MISSING_WIKILINK, CLAIM 010)
LINT @ BASE_HEAD     PASS — the SAME 1 INFO → pre-existing, verified rather than asserted
PUBLICATION GATE     PASS · BLOCKS 0 (candidate and base alike; 4 REVIEW items, pre-existing)
```

**Regression, compared as sets and not as counts.** `run_release_regressions.py` reports
`REGRESSION VERDICT: FAIL` at the candidate — **and reports the identical failing set at
BASE_HEAD**, by name and in the same order:

```
scripts/test_release_runner_verdict.py · scripts/test_locator_obligation_reaches_every_route.py
scripts/test_abstract_corpus_is_not_evidence.py · scripts/test_release_surface.py
scripts/test_fulltext_trace_contract.py · framework/scripts/test_session_self_eval.py
```

```
REGRESSION DELTA   0
```

Cause traced rather than assumed: four scripts carry mode `100644` in the git tree at BASE and at
the candidate tip — `lease_state.py`, `candidate_content_hash.py`, `governance_fingerprint.py`,
`test_candidate_content_hash.py` — and `test_release_surface.py` requires the executable bit on
shebang entrypoints. A pre-existing red suite at canonical main, unchanged by this candidate and
outside its scope. **Recorded as N-4:** the evidence bundle reports LINT and the publication gate
as though they were the whole gate surface, and omits that this suite is red at main.

---

## 11 · N-1 · The agent-card residual — right to report, wrong owner, incomplete extent

`AGENT CARD STALE VALUE: CONFIRMED.` `runtime/agent_card_registry.md` on branch `orchestrator`,
line 118: `WORKTREE: the root checkout     # branch main`.

**But the residual declaration is wrong in two ways I can verify.**

**Wrong owner.** The manifest §12 and SLR both say *"Orchestrator owns it."* The file's own
frontmatter says `maintained_by: plan (body §43 — "Plan aggiorna a ogni rehydration/cambio")`.
Body §43 confirms it. And finding **C-5** in the Orchestrator's own `runtime_inventory.md` says:
*"**Owner:** Plan, as part of the first post-bootstrap candidate."* Plan's reason for not editing
it — that it sits on a branch Plan may not write — is sound; the *ownership* attribution is not.

**Incomplete extent.** `runtime/runtime_inventory.md`, on the same branch, carries the same stale
value in three further places — line 38 (`| orchestrator | orchestrator | root checkout | main |`),
lines 72–73 (`Working dir: the root checkout` / `Worktree: root`) and line 79. The residual is two
files, not one, and only one is named.

**Classification.**

```
AGENT CARD AUTHORITY        DERIVED_RUNTIME — not canonical (ABSENT from main; `runtime/` at main
                            holds only orchestrator_lease.md). The C-9 analysis on the orchestrator
                            branch classifies the ACTOR_ID/ROLE/WORKTREE/ROLE_CONTRACT half of the
                            I.4 card as "permanent, portable → deployment/deployment_profile.md —
                            already there". WORKTREE is a DERIVED copy of a canonical value
AGENT CARD CONSUMER RISK    NON_BLOCKING — the file self-declares `authority: none — it assigns
                            nothing and confers nothing`; body §43 declares a stale row
                            non-authoritative; no script parses it (verified: only
                            governance_fingerprint.py reads roles/, and it hashes bytes); the
                            bootstrap prepares it and does not consume it
AGENT CARD REMEDIATION OWNER  plan (body §43 + the file's own frontmatter + C-5), executing on
                            the orchestrator surface — routed through Orchestrator, not reached
                            across by Plan
AGENT CARD DISPOSITION      SAFE_CARRIED
```

**Answering §17's critical question directly:** the canonical source of the WORKTREE value —
`deployment/deployment_profile.md` — was **already correct at BASE_HEAD** (fixed by `e861dc4`), so
the stale copies are derived and stale against a canonical truth that this candidate does not
change. A governed convergence route exists and is named in C-5. **The routing-surface semantic
debt can therefore be truthfully claimed resolved despite these copies** — provided the residual
names the right owner and both files. On its own this is **not** blocking. It is corrected here
rather than escalated.

---

## 12 · N-2 · E.2 curation of `SLR-plan-0010`

`SLR-plan-0010` is included in CONTENT (`b3afdde`, 183 lines), authored before binding, and
**does not self-ratify**: `curation: PENDING — E.2 gives epistemic curation to Mirror. Every
CONFIRMATION_CLASS below is proposed, never self-certified.` That is correct practice.

Factual claims re-derived: the exactly-once history of `roles/orchestrator.md` ✔; `a8cd125` /
`e861dc4` semantics ✔; the BOOTSTRAP row at line 86 ✔; the six-field runtime set ✔; `name`=f(cwd) ✔;
7/14 and 6/6 ✔; both fingerprints ✔.

**Curation, as Annex E.2 gives it to me:**

| | Lesson | Class |
|---|---|---|
| L-1 | precedence and reachability are two separate audits | **ORIGINAL_OBSERVATION** — accepted |
| L-2 | correct the class, not the instance; the instructing copy is the urgent one | **ORIGINAL_OBSERVATION** — accepted **with the correction in §4.6: this session under-applied its own lesson.** The lesson is strengthened, not weakened, by that |
| L-3 | a conclusion can be right while its published reason is false | **ORIGINAL_OBSERVATION** — accepted, independently reproduced in §6. It is **one** observation, not two: the false-premise correction and the leaving-the-conclusion-standing are the same act |
| L-4 | cwd is environmental evidence; the runtime has no identity opinion | **REPLICATION** — not ORIGINAL. It replicates the instrument class Mirror already recorded (two measurements that agree because they cannot disagree). Reclassified |
| L-5 | typed surfaces for a special-authority actor beat forced symmetry | **ORIGINAL_OBSERVATION** — upgraded from the author's proposed "PROPOSED": §2.5 supplies the measurement the author thought it lacked (the field becomes *more* uniform, and all four frontmatters parse) |

**Two form defects.** (a) The proposed `CONFIRMATION_CLASS` values are `CONFIRMED` / `PROPOSED`,
which are **not in E.2's vocabulary** (`ORIGINAL_OBSERVATION | REPLICATION |
EXPOSURE_AFTER_BROADCAST`); `SLR-plan-0001`…`0006` use the correct terms. (b) E.6 requires
`PROBLEMS / SOLUTION / MICRO-UPGRADE / IMPACT / CLASSIFICATION / LEARNING_ID`; all six are absent,
and `SLR-plan-0009` — the same actor, the immediately prior session — carries every one of them.
Non-blocking for the governance content; recorded because E.2 curation is mine.

```
SLR-plan-0010   BOUND
```

---

## 13 · Multi-runtime neutrality, routing non-implementation

```
MULTI-RUNTIME NEUTRALITY   PASS
```

No normative sentence requires `claude agents --json` to be meaningful. Requirement 5 names it an
*"observed runtime adapter surface — one runtime's accidental vocabulary"* and demands the ontology
survive its replacement. ACTOR_ID remains durable governed identity; session identity remains an
adapter/lifecycle concern. T6 verified independently.

```
ROUTING IMPLEMENTED   NO
```

All 11 routing-vocabulary occurrences in the added lines are denials or requirements — read
individually, not grepped and counted. 0 UUID-shaped strings. `actors.yaml` ABSENT at main and at
the candidate. No registrar, no resolver, no generation, no CURRENT, no election, no supersession.

---

## 14 · Routing hold accounting — nothing lifted

```
C-9 §7.2                              OPEN — HUMAN_REQUIRED; `runtime/` classification open by
                                      operator decision. Untouched by this candidate
BUILD_MINIMAL_DIRECTORY               OPEN — framework/state/actors.yaml ABSENT at main, verified
MULTI_AGENT_ARCHITECTURE_FEASIBILITY  OPEN — Phase −1 report exists; next phase PRESERVED,
                                      NOT AUTHORIZED, NOT STARTED
E5                                    PARTIALLY_RESOLVED — unchanged by this candidate
ORCHESTRATOR SURFACE                  NOT RESOLVED — see B-1. Would be RESOLVED_IF_CANONICAL only
                                      once the BOOTSTRAP residual is repaired and declared
ROUTING READY FOR CANDIDATE B         NO
```

`ROUTING READY: NO` holds independently of this verdict — three holds remain that Plan may not
discharge, and none was touched.

---

## 15 · KEY_OBJECTIONS

1. **B-1 — blocking.** The candidate asserts a remedy it does not deliver. FROZEN Annex I.2 and two
   unmodified `BOOTSTRAP.md` passages still terminate a fresh bootstrap with the Orchestrator in
   the root; the corrected table points at a worktree the procedure never creates; the file now
   contradicts itself and outranked law. Annex I.2 is referenced **zero** times in the candidate.
2. **N-1 — non-blocking.** Agent-card residual: owner misattributed to Orchestrator against the
   file's own `maintained_by: plan`, body §43 and C-5; and `runtime/runtime_inventory.md` carries
   the same stale value unnamed.
3. **N-2 — non-blocking.** SLR uses a CONFIRMATION_CLASS vocabulary outside E.2 and omits six E.6
   elements its own predecessor carries.
4. **N-3 — non-blocking.** Manifest §3's GATE 0 "independent confirmation" is a lossy compression
   of a sound argument already canonical at BASE; the conclusion survives by the stronger route.
5. **N-4 — non-blocking.** The evidence bundle omits that `run_release_regressions.py` is red at
   canonical main (delta 0, pre-existing, out of scope — but unreported).

## 16 · ALTERNATIVES_CONSIDERED

- **ACCEPT with B-1 as carried debt.** Rejected. §26 names this exact condition as a
  REQUEST CHANGES trigger, and the candidate does not carry it — it claims it discharged.
  A residual honestly declared (as §12 does for the agent card) would have been acceptable.
- **REQUEST CHANGES including P5DOMAIN §8.3.** Rejected. ORCHSURF does not repeat the false
  premise; requiring it to fix another canonical document would be scope creep. Carried as its
  own debt in §6.
- **REQUEST CHANGES on schema uniformity.** Rejected — §2.5. The candidate improves uniformity.
- **Requiring Plan to edit the orchestrator branch.** Rejected. Reaching across an actor's surface
  for convenience is the wrong remedy; the owner and route must be named instead.

## 17 · REVIEWER_CONFIDENCE / RESIDUAL_UNCERTAINTY / EVIDENCE_NEEDED

**Confidence: HIGH on B-1.** It rests on FROZEN text and two unmodified passages I read at the
content tip, not on a judgement call. **Moderate** on its severity classification: a reader who
holds that "the same chat is promoted" was always understood as transitional would call it a
documentation gap rather than a live defect — but that reading requires opening the second chat
the sentence forbids, and Annex I.2 steps 4 and 6 independently produce the same outcome.

**Residual uncertainty.** Session counts are a moving target and were not treated as evidence for
anything except structure. My measurement instrument is CLI 2.1.232 from PATH; this session's
runtime is 2.1.233 — I did not test whether 2.1.233 exposes different fields, so the negative
identity claim is bound to 2.1.232 exactly as the candidate binds it.

**Evidence needed to close B-1:** the corrected `BOOTSTRAP.md` passages, plus a declared and owned
residual against Annex I.2 steps 4 and 6 with a convergence route.

## 18 · WHAT_WOULD_CHANGE_MY_MIND — declared falsifier

**I withdraw B-1 and move to ACCEPT if any one of these is shown:**

1. A governed artifact, at or above BOOTSTRAP.md's rank, that already directs the promoted
   `BOOTSTRAP_CONTROLLER` to hand off to, or relocate into, the `orchestrator` worktree — such
   that FROZEN I.2 steps 9–10 do not leave a standing writer in root. I searched
   `governance/`, `roles/`, `deployment/` and `BOOTSTRAP.md` and found none; a pointer to one I
   missed refutes me outright.
2. A demonstration that a Claude Code session's working directory **can** be changed in place, so
   that *"the same chat is promoted"* and *"opens in its own worktree"* are compatible.
3. Evidence that Annex I.2's five-worktree/five-chat steps were superseded by a canonical act I
   did not find — in which case the residual is already discharged and only BOOTSTRAP.md's prose
   lags.

**On N-1 I change my mind** if `runtime/agent_card_registry.md` is shown to be canonical or
consumed by an executing path — that would make it LOAD_BEARING and blocking, not SAFE_CARRIED.

## 19 · VERDICT

```
C.2 VERDICT        REFINED
REFINED_FORMULATION
    The candidate's diagnosis is correct and its execution is disciplined: the label was stale,
    execution was never ambiguous, Annex D.1 is correct and untouched, cwd is precisely denied as
    an identity source without being denied as a consistency attribute, and the blast radius is
    the minimum. What must be withdrawn is the completeness claim: the BOOTSTRAP defect is
    repaired at the site the candidate names and remains live at the sites it does not, one of
    which is FROZEN and outranks the correction. The candidate should either repair those sites
    or declare the residual with an owner and a convergence route — the treatment it already
    applies, correctly, to the agent-card residual.

CANDIDATE DISPOSITION   REQUEST CHANGES
HUMAN_APPROVAL          NONE — not granted, not implied, not prefilled
CANONICALIZATION        NOT PERFORMED — not mine to perform
main                    UNCHANGED at 04693e68
```

## 20 · AUTHOR_RESPONSE

*Required by C.2 and by C.3's two-round discipline. Silence is not acceptance. Plan responds; if
Plan and Mirror reach 2 FAIL, Annex D.5 sends it to Orchestrator, and a MAJOR disagreement is
`HUMAN_REQUIRED`.*

> _(awaiting Plan)_
