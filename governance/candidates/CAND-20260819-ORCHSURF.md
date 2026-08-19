---
artifact: INTEGRATION_CANDIDATE — Orchestrator surface semantics
candidate_id: CAND-20260819-ORCHSURF
revision: 2
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
  Annex I.2 NOT modified and NOT claimed superseded. P5 NOT reopened. C-9 §7.2 NOT altered.
  Scientist A/B NOT activated. BENCH-AB-001 NOT started
human_approval: NOT REQUESTED — no APPROVAL_ID is prefilled here, and none exists
revision_2: remediates B-1, the single blocking finding of REV-ORCHSURF-MIRROR-001, and N-1. The
  remedy is in CONTENT. It does NOT complete the bootstrap transition — it removes the stale
  instructions that recreated the invalid arrangement, and declares the FROZEN Annex I.2 residual
  that no lower-precedence document may discharge. §13 records the disposition of every finding.
  The completion claim of revision 1 is WITHDRAWN, in this manifest and in the content
supersedes: revision 1, CANDIDATE_CONTENT_HASH
  3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7 at content tip
  b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2. That binding is SUPERSEDED, not withdrawn — it was
  correct for the tree it named, it is used as a positive control in §1, and Annex D.2 invalidates
  it because the bound content moved
---

# INTEGRATION_CANDIDATE — `CAND-20260819-ORCHSURF` · revision 2

## 1 · Manifest (Annex D.2)

```
CANDIDATE_ID              CAND-20260819-ORCHSURF
REVISION                  2
BASE_HEAD                 04693e683a254ff0a6d0619fba47103a0fb7d122   (canonical main, verified
                                                                      from git at session open
                                                                      and again at binding)
SOURCE_COMMITS            b3afdde4423b62fc7f0ddf18cc8183fb989fe1b2   CONTENT — revision 1
                          7b6a9d9aeaf2a162fc16de4e4abdb713ddead603   CONTENT — revision 2, the
                                                                      remediation + two SLRs
                          <this commit>                              CONTROL PLANE — this manifest
CONTENT_TIP               7b6a9d9aeaf2a162fc16de4e4abdb713ddead603
CANDIDATE_HASH_VERSION    legend-candidate-v4
CANDIDATE_CONTENT_HASH    b0a0c9ed6849521a1331a4d6c0850de252ae7c4b5e3b227a477b21f4386465d1
                          536 included · 47 excluded
SUPERSEDED_HASH           3af61c6d87eb17de786c8592a0a3d42e7b7bc996a100a1d310398332feaad4c7
                          revision 1, at content tip b3afdde — correct for its tree, invalidated
                          by Annex D.2 because the content moved. Reproduced below as a control
CHANGE_CLASS              MAJOR — it edits a role contract, the deployment profile and the
                          bootstrap procedure, which is governance (H.1: "Spese / MAJOR approval
                          / governance → Operatore"; Annex G.1 MIRROR_REQUIRED). Classified MAJOR
                          fail-closed; H.1 gives a doubtful MAJOR classification to Mirror
LINT_RESULT               PASS — 1 pre-existing INFO (MISSING_WIKILINK, CLAIM 010), identical at
                          BASE_HEAD
PUBLICATION_GATE          PASS / BLOCKS: 0
REGRESSION                DELTA 0 — measured in matched environments, §15. The suite is RED at
                          canonical main and this candidate does not move it
MIRROR_REVIEW             REV-ORCHSURF-MIRROR-001 returned REQUEST CHANGES on revision 1.
                          Revision 2 requires a NEW review. None performed, none assumed
HUMAN_APPROVAL            n/a — not requested, not prefilled
SNAPSHOT_ID               n/a until canonical execution — GATE 4 belongs to Orchestrator
FINGERPRINT IMPACT        orchestrator  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
                                     →  9d8d823ca490063550997f092e4eb7c3c16e241c74e1830d996ff22035271871
                          plan · mirror · scientist  UNCHANGED, byte-identical — §14
```

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base 04693e683a254ff0a6d0619fba47103a0fb7d122 \
  --tip  7b6a9d9aeaf2a162fc16de4e4abdb713ddead603
# b0a0c9ed6849521a1331a4d6c0850de252ae7c4b5e3b227a477b21f4386465d1
```

**Independent route** — the digest reproduced without trusting the script's own final step, by
re-digesting the published pre-image with a different tool:

```bash
… --emit-domain | shasum -a 256
# b0a0c9ed…65d1   (57 764 bytes, 538 lines: 536 domain entries + 2 header lines)
```

**Three positive controls — published values authored by earlier sessions, reproduced here.** This
is what makes the instrument trustworthy rather than merely self-consistent:

```
CAND-20260819-P5DOMAIN   base f70878d1 tip ceefaa28  → 930dfefb…6b97   MATCHES published
CAND-20260819-XPORT      base 4454feab tip e839db38  → 81f241f2…6e1f   MATCHES published
ORCHSURF revision 1      base 04693e68 tip b3afdde4  → 3af61c6d…d4c7   MATCHES published
```

**Three negative controls, verified rather than void.**

```
BASE tree against itself           cfe8957d…1298   ≠ candidate — and it is the value Mirror
                                                    independently measured at revision 1
revision 1 vs revision 2           3af61c6d… ≠ b0a0c9ed…   the binding moved with the content
SHA-256 of the empty string        e3b0c442…b855   ≠ candidate, and the pre-image is 57 764
                                                    bytes — this comparison is not two voids
```

```
BINDING   PASS
```

---

## 2 · What revision 2 does, and what it deliberately does not

`roles/orchestrator.md` said its worktree was the repository root checkout. That was true on
2026-08-16 and stopped being true on 2026-08-17. Revision 1 corrected the label, typed the second
surface, stated that a working directory cannot establish who an actor is, and corrected the same
stale row in `BOOTSTRAP.md`.

**Revision 1 then claimed the bootstrap defect was repaired, and it was not.** Two passages of the
same file still executed the old arrangement, and a `FROZEN` annex that outranks everything the
candidate wrote still mandates it. Revision 2 closes the editable half and **declares** the half
that is not Plan's to close.

```
WITHDRAWN AT REVISION 2   the claim that the BOOTSTRAP defect is repaired
                          the claim that no FROZEN governance change is required
                          ORCHESTRATOR SURFACE = RESOLVED_BY_CANDIDATE_IF_CANONICAL
ADDED AT REVISION 2       a fail-closed stop in BOOTSTRAP.md at the promotion step
                          the FROZEN Annex I.2 residual, declared with owner and route
                          the residual's correct owner and its full extent
```

---

## 3 · Execution was never ambiguous — Annex D.1 is correct and untouched

```
WORK_COMMIT              ogni attore, proprio branch — obbligatorio, non canonico
CANONICAL_BATCH_COMMIT   solo Orchestrator, root, gate 0–5
```

`governance/annex_d_commit_batch.md` is `status: FROZEN`, `normative: yes`, and sits at rank 1 of
body §5 against a role contract's rank 4.

```
ORCHESTRATOR EXECUTION AMBIGUITY   NO
ANNEX D.1                          CORRECT — NOT MODIFIED at either revision
WORK_COMMIT SURFACE                the `orchestrator` worktree, branch `orchestrator`
CANONICAL_BATCH_COMMIT SURFACE     the root checkout, branch `main`, batch window only
```

### 3.1 · N-3 accepted — the independent confirmation is restated at its sound strength

Revision 1 argued that an actor resident in the root *"is a standing writer there, so GATE 0 would
fail from that actor's first durable output onward."* Mirror is right that this is lossy:
committed output leaves the root clean. **The sound version was already canonical at BASE**, in
`deployment/deployment_profile.md`, and revision 2 uses only that one:

> The root's branch is `main`, and a commit to `main` is canonical by definition — so an
> Orchestrator living in the root has **no branch on which a `WORK_COMMIT` is possible**. Its
> output cannot become durable; body §8 obliges it to produce durable output; so the root cannot
> reach clean by anything that actor is permitted to do alone.

That argument, in that form, is what `BOOTSTRAP.md` and the deployment profile now carry. The
compressed version appears nowhere in the content.

---

## 4 · The label was stale, and the file's own body already refuted it

`roles/orchestrator.md` has been touched **exactly once** in its history — `a8cd125`, 2026-08-16,
the original materialization. `e861dc4`, 2026-08-17, changed **one file**:
`deployment/deployment_profile.md`.

```
ORCHESTRATOR ROLE/FRONTMATTER LABEL     STALE — accurate when written, overtaken, never revisited
ORCHESTRATOR ROUTING-SURFACE AMBIGUITY  CONFIRMED
```

**The `worktree:` field was type-inconsistent.** Every other contract carries a bare worktree name;
only Orchestrator carried a prose phrase, and only Orchestrator has two surfaces to name. After the
change all four frontmatters parse as YAML and `worktree` is a bare string in three of them —
`roles/scientist.md` uses plural `worktrees`, which this candidate neither creates nor worsens.

---

## 5 · 🔴 B-1 accepted in full — and the reason it cannot be repaired the obvious way

**Reproduced before accepting, from git and not from the review.** At revision-1 content tip
`b3afdde`, `BOOTSTRAP.md` carried:

| Site | Text | Revision 1 |
|---|---|---|
| lines 31–35 | *"The same chat is promoted — you do not need to open a second one."* | **untouched** |
| step 3, lines 57–58 | creates `lettore`, `lettore-b`, `lettore-c`, `evidence-index`, `mirror` — five, omitting `orchestrator` | **untouched** |
| line 86, the table | `orchestrator` → `the repository root checkout` | **corrected** |

```
REV1 TABLE FIX                        PRESENT
REV1 ROOT-PROMOTION INSTRUCTION       PRESENT — live, in the section headed "The one thing to
                                      understand before anything else", read long before line 93
REV1 ORCHESTRATOR WORKTREE CREATION   ABSENT — the corrected table pointed at a worktree the
                                      procedure never created
```

**A chat's working directory is fixed at session start and cannot be relocated**, so *"the same
chat is promoted"* is operationally identical to *"the Orchestrator stays in the root."* The
reading that would save the sentence requires the act it forbids.

### 5.1 · FROZEN Annex I.2 mandates the same arrangement, and it outranks the fix

`governance/annex_i_bootstrap_deployment.md` is `status: FROZEN`, `normative: yes`, and § I.2
reads, verbatim:

```
1.  prima chat in <REPO_ROOT> → CLAUDE.md → nessun lease ACTIVE → BOOTSTRAP_MODE
4.  crea/verifica worktree: lettore, lettore-b, lettore-c, evidence-index, mirror
6.  presenta all'operatore la LISTA ESATTA delle 5 chat da aprire (path per ACTOR_ID)
9.  condizioni PASS → acquisizione ORCHESTRATOR_LEASE (I.3)
10. ORCHESTRATOR_REGISTRATION durevole → ACTIVE_ORCHESTRATOR → governance ordinaria
```

```
ANNEX I.2 ROOT-PROMOTION MODEL   CONFIRMED — step 1 seats the controller in the root; steps 9–10
                                 promote that same chat in place
ANNEX I.2 CONFLICT               CONFIRMED — against the canonical deployment profile, which
                                 reserves the root to CANONICAL_BATCH_COMMIT and gives the
                                 Orchestrator its own worktree
ANNEX I.2 PRECEDENCE OVER        YES, by two independent routes:
BOOTSTRAP.md                     (a) I.2 is FROZEN + normative, body §5 rank 1; BOOTSTRAP.md is
                                     status: PROPOSED
                                 (b) BOOTSTRAP.md line 5 declares `authority: Annex I.1, I.2,
                                     I.6` — it derives from I.2 and cannot outrank its source
ANNEX I.2 CHANGE AUTHORITY       operator. Annex H.1: "Spese / MAJOR approval / governance →
                                 Operatore". Body §4: "Cambio governance / authority model →
                                 attende → human required". Plan may propose; Plan may not adopt
SECOND ORCHESTRATOR CHAT         excluded — not by a prohibition sentence, but determinately, by
                                 step 6's *LISTA ESATTA* of **five** combined with step 1 and
                                 steps 9–10. Stated as a reading of the arithmetic, because that
                                 is what it is
```

**A sixth chat is what I.2 excludes; a sixth *directory* is not.** Step 4 enumerates worktrees to
create and does not prohibit others, and the `orchestrator` worktree is canonical at `main` through
`CAND-20260817-ORCHWT`. Nothing load-bearing rests on that reading: creating a directory confers no
authority, and the blocked act is the promotion.

### 5.2 · The remedy — fail closed, because both executable options are wrong

Revision 2 does **not** make `BOOTSTRAP.md` independently executable in the new topology. That
would be a `PROPOSED` document overriding a `FROZEN` one, which is the failure mode, not the fix.

| Option | Verdict |
|---|---|
| Leave I.2's topology executable | **rejected** — recreates the standing root writer. §26 names this exact condition |
| Publish the new topology in `BOOTSTRAP.md` | **rejected** — a lower-precedence document silently superseding rank-1 FROZEN law |
| **Surface the conflict, stop, name the owner** | **SELECTED** — body §48's `BLOCKED_BY_GOVERNANCE`, Annex J.3's queue object, `TYPE: GOVERNANCE` |

What that looks like in the file, and where a reader meets it:

```
line  36–39   the top section — the question is open, stop before step 9
line  61–68   step 3 creates the orchestrator worktree, and says creating a directory
              promotes nobody
line  70–75   step 5 holds the operator's chat list at the five I.2 step 6 requires and
              explicitly withholds the sixth line
line  87–90   step 9 carries a STOP *before* the lease-acquisition verb
line  96–136  the block itself: both sources, both statuses, why I.2's topology is defective,
              why that is still not this file's decision, and the route
line 142      the `orchestrator` row is marked BLOCKED, do not open
line 149–157  the table's prose: the row records a work surface, not an instruction
```

```
BOOTSTRAP EDITABLE                              YES — status: PROPOSED
BOOTSTRAP ROOT-PROMOTION INSTRUCTION AFTER R2   REMOVED
BOOTSTRAP ORCHESTRATOR WORKTREE OMISSION        REMOVED — step 3 creates it
BOOTSTRAP FRESH-RUN STATUS                      FAIL_CLOSED_PENDING_FROZEN_TRANSITION
FROZEN RESIDUAL                                 HUMAN_REQUIRED — declared, owned, routed
ANNEX I.2 MODIFIED                              NO
ANNEX I.2 CLAIMED SUPERSEDED                    NO
```

### 5.3 · Where the residual is declared, so it is not carried by this manifest alone

`deployment/deployment_profile.md` — a new subsection under the section that made the change,
carrying `RESIDUAL / INTRODUCED BY / OWNER / AUTHORITY REQUIRED / STATE / CONVERGENCE ROUTE /
BLAST RADIUS`. `roles/orchestrator.md` — a paragraph stating that for this already-bootstrapped
laboratory the question is settled and for a fresh bootstrap it is not. `BOOTSTRAP.md` — the block
itself. **Three content files, not a control-plane note.**

### 5.4 · Who introduced it, measured rather than assumed

`CAND-20260817-ORCHWT` corrected the deployment profile and left Annex I.2 mandating the
arrangement it replaced. The conflict therefore **pre-dates this candidate at BASE_HEAD**; ORCHSURF
exposes it and does not create it.

```
CAND-20260817-ORCHWT manifest      "I.2" → 0 hits   "Annex I" → 0 hits
REV-ORCHWT-MIRROR-001              "I.2" → 0 hits   "Annex I" → 0 hits
REV-ORCHWT-MIRROR-002              "I.2" → 0 hits   "Annex I" → 0 hits
ORCHSURF revision 1, all 4 content files            "Annex I.2" → 0, 0, 0, 0
```

Two hostile reviews and an operator approval passed over it. That is recorded as `SLR-plan-0011`
L-5 and is the finding this session considers most worth carrying forward.

---

## 6 · Three concepts, and the one that gets no filesystem attribute

```
1. ACTOR WORK SURFACE       per-actor, named by `worktree:` in every contract
2. CANONICAL BATCH SURFACE  Orchestrator only, named by `canonical_batch_surface:`
3. ROUTING / DISCOVERY      NO filesystem attribute — the candidate declines to create one
```

The three ordinary contracts are untouched. Their `ACTOR_ID ↔ worktree` mapping was never
ambiguous, and flattening a real asymmetry to make the schema uniform would be a second error. It
also holds the blast radius to one fingerprint.

---

## 7 · The measurement — why cwd cannot carry concept 3

```
INSTRUMENT     claude agents --json --cwd <path>   (PATH binary)
VERSION        2.1.232 (Claude Code)
SESSION RT     2.1.232 — this session's owning process image. Same version here; recorded
               separately because instrument version and session runtime are different facts
TIMESTAMP      2026-08-19T21:55:28Z
MODE           read-only enumeration; no session elected, superseded or written
```

| Query cwd | Sessions | Composition |
|---|---|---|
| root | **8** | 5 root · 1 `lettore-c` · 1 `mirror` · 1 `evidence-index` |
| `orchestrator` worktree | **0** | — |
| `evidence-index` — POSITIVE CONTROL | **1** | the query can return non-zero |
| `mirror` — POSITIVE CONTROL | **1** | — |
| `lettore-c` — POSITIVE CONTROL | **1** | — |
| nonexistent path — NEGATIVE CONTROL | **0** | — |

**Counts are volatile and are evidence for nothing but structure.** Plan measured 17 at 21:02Z,
Mirror 8 at 21:23Z, this session 8 at 21:55Z. **Every structural claim reproduced exactly, a third
time:**

```
FIELD SET                  cwd · kind · name · pid · sessionId · startedAt — exhaustive union
EXPLICIT ACTOR/ROLE FIELD  NOT_OBSERVED_VIA(claude agents --json, CLI 2.1.232)
NAME == <cwd leaf>-<2 hex> 8/8
ROOT-CWD INTERPRETATION    OVER_BROAD_FOR_ACTOR_DISCRIMINATION — 3 of 8 hits are other actors
ZEROS                      AMBIGUOUS — the orchestrator worktree exists and returns 0; a
                           nonexistent path returns 0. The instrument cannot separate
                           unoccupied from absent
CWD AS ROUTING ATTRIBUTE   PROHIBITED as an actor-identity discriminator
```

The negative claim is stated **instrument-bound**, not as universal impossibility, and requirement 5
in the content excludes the tool from the ontology.

### 7.1 · Worktree containment, counted precisely rather than conveniently

```
TOTAL WORKTREES                    14
AT OR UNDER THE ROOT               7   = the root checkout itself + 6 named actor worktrees
OUTSIDE THE ROOT ENTIRELY          7   = 4 legend-codex-* checkouts + 3 scratchpad worktrees
NAMED ACTOR WORKTREES UNDER ROOT   6/6
UNIVERSAL "every worktree is under root"   FALSE
```

The two figures differ by whether the root counts as under itself; both are stated so neither can
be read as the other. The content asserts only *7 outside* and *6/6 named actors under*, which are
the two that are true under either convention.

### 7.2 · P5DOMAIN §8.3 — carried, not edited

Canonical P5DOMAIN §8.3 supports a **true conclusion** with a **false universal premise**
(*"every worktree lives under the root"*). This candidate does not repeat the premise, states the
narrow 6/6 fact instead, and **does not edit P5DOMAIN**.

```
P5DOMAIN §8.3   CARRIED_SEPARATE_TRUTHFULNESS_DEBT — owner: whichever candidate next opens P5.
                Not load-bearing to ORCHSURF, and requiring ORCHSURF to fix it would be scope creep
```

---

## 8 · Remediation classes considered, at revision 2

| | Class | Verdict |
|---|---|---|
| A | role-label correction alone | **insufficient** — one site, `worktree` still untyped, root-cwd reading still available |
| B | typed-surface semantics alone | **insufficient** — leaves BOOTSTRAP executing the old arrangement |
| C | cwd-nonauthoritative rule alone | **insufficient** — states the prohibition while the contract asserts the thing it prohibits |
| D | A + B + C, each minimal | **insufficient — this was revision 1.** It corrects the sites it names and leaves the procedure beneath them |
| **E** | **D + full BOOTSTRAP remediation + declared FROZEN residual** | **SELECTED** |
| F | E + amend Annex I.2 | **not available to Plan** — H.1 gives governance change to the operator; §25 of the directive forbids it here |
| G | rename `worktree:` in all four contracts | **rejected** — rotates four fingerprints to fix an ambiguity that exists in one |

```
SELECTED REMEDIATION CLASS   E
PROBLEM SOLVED               the stale label at both sites; the untyped word; the availability of
                             cwd as an identity discriminator; and — new at revision 2 — the
                             executable instruction that recreated the root Orchestrator
PROBLEM DECLARED, NOT SOLVED FROZEN Annex I.2 still mandates the legacy topology. HUMAN_REQUIRED
GUARANTEE PROVIDED           scoped deliberately: (a) a future resolver cannot read a
                             canonical-execution surface as an actor home, and cannot read any
                             filesystem location as identity; (b) a fresh bootstrap following this
                             file cannot silently seat a standing root Orchestrator. **NOT**
                             guaranteed: that a fresh bootstrap can complete
WHAT REMAINS UNSOLVED        the Annex I.2 transition; and which session is CURRENT for an
                             ACTOR_ID, untouched, with three holds still blocking it
BLAST RADIUS                 5 content files, 1 fingerprint
BACKWARD COMPATIBILITY       no rule changes; no published hash moves; no executing behaviour
                             depends on any corrected line
```

---

## 9 · Hostile tests — T1–T6 re-run, T7–T9 added

| | Test | Expected | Result | Reason verified |
|---|---|---|---|---|
| T1 | can a non-Orchestrator session satisfy the stale root-cwd reading? | YES (proving it unsafe) | **PASS** | 3 of 8 root-query hits are demonstrably other actors; the 5 at root differ only by `pid`/`sessionId`/`startedAt`/name-suffix — mutually indistinguishable on any governed attribute |
| T2 | does occupying the `orchestrator` worktree confer authority? | NO | **PASS** | `lease_state.py --check`: **ACTIVE by derivation 0** over 5 leases (2 STALE, 3 RELEASED). Authority needs assigned role + ACTIVE lease |
| T3 | can an authorized Orchestrator batch in root without changing its work surface? | YES | **PASS** | measured live: root `main`@`04693e6`, **0 porcelain lines**; `orchestrator` worktree on branch `orchestrator`@`b3596d5`. Coexisting |
| T4 | do ordinary-actor semantics stay coherent? | YES | **PASS** | `git diff --name-only 04693e68 -- roles/` returns **only** `roles/orchestrator.md`; all four frontmatters parse as YAML; plan/mirror/scientist fingerprints byte-identical |
| T5 | does the candidate elect a CURRENT session? | NO | **PASS** | 0 UUID-shaped strings in 235 added lines — with a positive control confirming the regex finds real UUIDs in `ledger/`; `actors.yaml` ABSENT at base and tip; every routing-vocabulary hit read individually — all denials, requirements or descriptions |
| T6 | does it require `claude agents --json` as the identity definition? | NO | **PASS** | two occurrences: a dated measurement, and requirement 5, which excludes it — *"must survive its replacement"* |
| **T7** | **following all CURRENT executable BOOTSTRAP instructions after revision 2, and respecting the declared residual, can the procedure silently create or promote a standing root Orchestrator?** | **NO** | **PASS** | **not tested by phrase absence.** The procedure was walked step by step: the only sites that can seat an Orchestrator are step 9 (lease acquisition) and step 10 (durable registration). Step 9 carries the STOP **before** its acquisition verb; three further pointers (lines 36–39, 73, 87) precede it; the block itself states `UNTIL RESOLVED do not promote any chat to ACTIVE_ORCHESTRATOR, in the root or anywhere`. **The reason is NOT "BOOTSTRAP overrides I.2"** — it is that execution halts and defers. Negative control: the same walk on the revision-1 tree reaches step 9 with no stop and line 34 instructing promotion in place |
| **T8** | can an operator reach the Orchestrator bootstrap without being told that Annex I.2 still mandates the legacy topology? | **NO** | **PASS** | the first reference to the block (line 36) precedes the first lease-acquisition verb (line 90) in file order, and step 1 directs a linear read of this file first. 14 references to Annex I.2 across three content files. **Positive control**: the same probe on the revision-1 tree returns **0, 0, 0, 0** — reproducing Mirror's zero independently |
| **T9** | can the stale `agent_card` / `runtime_inventory` declarations independently confer or redefine Orchestrator work-surface authority? | **NO** | **PASS** | three legs: (a) each file self-declares `authority: none`; (b) body §43 — *"riga stantia = non autoritativa"*; (c) **no executable consumes them** — `git grep` over every `*.py`/`*.sh` on both `HEAD` and branch `orchestrator` returns zero, with a **positive control** (the same search finds the three real consumers of `plan_defined_parameters`) and a **negative control** (a nonexistent token returns empty). `launch/legend_launch.sh` references none of them |

```
WRONG-REASON LOAD-BEARING PASSES   0
```

**Four traps avoided at this revision, recorded because they nearly landed.** (i) T7 as a grep for
the deleted sentence — it would have passed on a file that still walked an operator into the root
by a different route, so the test walks the procedure instead. (ii) T9's consumer search run only
on `HEAD`, which does not contain the runtime files — repeated on branch `orchestrator`, where they
live. (iii) the regression comparison run between a working worktree and a fresh checkout, where a
**git-ignored** local corpus (`files/`, `.gitignore:7`) turned four `skipped` into `ok` and looked
like a delta — re-run in matched fresh checkouts, §15. (iv) a worktree-containment count of 6/14
that is 7/14 under the other convention — both stated, §7.1.

---

## 10 · Authority — corrected from revision 1

Revision 1 stated `FROZEN GOVERNANCE CHANGE REQUIRED: NO`. **That was false**, and it is the
sentence that let the completion claim stand.

```
FROZEN GOVERNANCE CHANGE REQUIRED FOR COMPLETION   YES — Annex I.2 steps 4, 6, 9–10
FROZEN GOVERNANCE CHANGE MADE HERE                 NO — and none is proposed in this candidate
ANNEX D.1 MODIFIED                                 NO   (FROZEN, verified correct, blob identical)
ANNEX H.1 MODIFIED                                 NO   (FROZEN)
ANNEX I.2 MODIFIED                                 NO   (FROZEN — and this is the residual)
```

Every artifact this candidate edits is `status: PROPOSED` or is Plan's to maintain under its own
mandate. The route is unchanged and verified against H.1:

```
plan proposes  →  mirror reviews  →  operator approves (governance, MAJOR)  →  orchestrator
canonicalizes under an ACTIVE lease and gates 0–5
```

Plan does not execute this. GATE 1 keeps proposer and executor distinct.

---

## 11 · Routing holds — accounting only, nothing lifted

```
C-9 §7.2                              OPEN — HUMAN_REQUIRED. Untouched
BUILD_MINIMAL_DIRECTORY               OPEN — framework/state/actors.yaml ABSENT at main and at
                                      the candidate tip. Verified this session
MULTI_AGENT_ARCHITECTURE_FEASIBILITY  OPEN — PRESERVED, NOT AUTHORIZED, NOT STARTED
E5                                    PARTIALLY_RESOLVED — unchanged by this candidate
ORCHESTRATOR SURFACE                  PARTIALLY_RESOLVED — HUMAN_REQUIRED.
                                      Semantics corrected and stale instructions removed;
                                      adoption of the bootstrap topology BLOCKED_BY_FROZEN
                                      Annex I.2, whose amendment is the operator's
ROUTING READY FOR CANDIDATE B         NO — three holds remain, none of which Plan may discharge
```

`PARTIALLY_RESOLVED` and `HUMAN_REQUIRED` are the vocabulary already in use in this table (E5, C-9
§7.2). No new lifecycle state is invented. **Candidate B is not opened here.**

---

## 12 · Residual — N-1 accepted, owner corrected, extent enumerated

**Owner, verified from three sources that agree, none of them the review:**

```
runtime/agent_card_registry.md   frontmatter   maintained_by: plan (body §43)
body §43, canonical at main                     "Plan aggiorna a ogni rehydration/cambio;
                                                 riga stantia = non autoritativa"
runtime_inventory.md, finding C-5               "Owner: Plan, as part of the first
                                                 post-bootstrap candidate"

AGENT CARD OWNER   plan   ← revision 1 said "Orchestrator owns it". WITHDRAWN
```

Revision 1's *reason* for not editing it — it sits on a branch Plan may not write — is sound and
unchanged. Location decides the **route**; ownership metadata decides the **owner**.

**Extent — two tracked files and seven occurrences, plus a third artifact nobody had named:**

| Path (branch `orchestrator`) | Loc | Text | Class | Consumer | Code-read? | Load-bearing? |
|---|---|---|---|---|---|---|
| `runtime/agent_card_registry.md` | 118 | `WORKTREE: the root checkout # branch main` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 38 | table row, Worktree = `root checkout` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 72 | `Working dir: the root checkout` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 73 | `Worktree: root` | DERIVED_RUNTIME | none | **no** | no |
| `runtime/runtime_inventory.md` | 79 | `Write access: root checkout; bootstrap artifacts only` | DERIVED_RUNTIME | none | **no** | no — it describes the I.2 pre-promotion perimeter, which is still FROZEN law |
| `runtime/bootstrap/STEP5-session-open-plan.md` | 32 | *"The Orchestrator chat is already open in the root checkout and is not reopened."* | OBSERVATIONAL — `status: PLAN`, `authority: none` | none | **no** | no — a record of a step executed on 2026-08-17, not a template |
| `runtime/bootstrap/STEP5-session-open-plan.md` | 38 | table row, `orchestrator` \| root checkout \| `main` | OBSERVATIONAL | none | **no** | no |

**Not stale, and recorded so the list is not mistaken for one:**
`deployment/deployment_profile.md` on branches `mirror` and `lettore-c` carries the pre-`e861dc4`
row. Verified: `e861dc4` is **not** an ancestor of either branch, so these are branch-lag copies of
a canonical file, not independent declarations. They refresh when those branches rebase.

```
AGENT CARD AUTHORITY        DERIVED_RUNTIME — not canonical (`runtime/` at main holds only
                            orchestrator_lease.md). WORKTREE is a derived copy of a canonical
                            value that was ALREADY CORRECT at BASE_HEAD (fixed by e861dc4)
CONSUMER RISK               NON_BLOCKING — verified in T9 with positive and negative controls
REMEDIATION OWNER           plan (body §43 + frontmatter + C-5), executing on the Orchestrator
                            surface — routed through Orchestrator, never reached across by Plan
RUNTIME STALE DECLARATIONS  SAFE_CARRIED
```

**No other surface was modified to make this review green.** Plan does not write another actor's
branch, and the correct extent is reported rather than repaired.

---

## 13 · Disposition of every finding in `REV-ORCHSURF-MIRROR-001`

| | Finding | Disposition |
|---|---|---|
| **B-1** | BOOTSTRAP can still recreate a standing root Orchestrator; Annex I.2 never mentioned | **ACCEPTED, REMEDIATED + DECLARED** — §5. Editable half closed; FROZEN half declared with owner and route. Reproduced independently before accepting |
| **N-1** | agent-card residual: wrong owner, incomplete extent | **ACCEPTED, CORRECTED** — §12, and `SLR-plan-0010-COR-001`. One further artifact found beyond Mirror's list |
| **N-2** | SLR uses CONFIRMATION_CLASS values outside E.2; six E.6 elements absent | **ACCEPTED, APPLIED FORWARD** — `SLR-plan-0011` uses E.2's vocabulary and carries all E.6 elements. `SLR-plan-0010` left **byte-identical**: a learning record records what a session understood, and Mirror's E.2 curation of it is already durable in the review |
| **N-3** | manifest §3's GATE 0 argument is a lossy compression | **ACCEPTED, RESTATED** — §3.1. Only the canonical no-branch-for-WORK_COMMIT form appears in the content |
| **N-4** | the evidence bundle omits that the regression suite is red at main | **ACCEPTED, DISCLOSED** — §1 and §15 both state it, with the cause traced independently |
| §6 | P5DOMAIN §8.3 false premise | **CARRIED** as a separate truthfulness debt — §7.2. Not edited |
| §12 | `SLR-plan-0010` BOUND, L-4 reclassified to REPLICATION, L-5 upgraded | **ACCEPTED** — Mirror's curation stands; `SLR-plan-0011` proposes its own classes and does not revisit Mirror's |
| §2 | five steelman points | noted; §2.5's mechanical argument for the schema decision is adopted in §4 |

**Author response (C.2 §20):** `reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-001.md`.

---

## 14 · Fingerprint impact — recomputed from scratch at four trees

```
                    BASE_HEAD 04693e68        REVISION 1 b3afdde        REVISION 2 7b6a9d9
orchestrator        88dea7a6…5ebb        →    42b8575c…908a        →    9d8d823c…1871
plan                0d6987bd…1429             0d6987bd…1429             0d6987bd…1429
mirror              e01b4108…0412             e01b4108…0412             e01b4108…0412
scientist           b66959cd…9d1a             b66959cd…9d1a             b66959cd…9d1a
```

Full values:

```
orchestrator BASE  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
orchestrator REV2  9d8d823ca490063550997f092e4eb7c3c16e241c74e1830d996ff22035271871
plan               0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
mirror             e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412
scientist          b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
```

**Recomputed, not carried forward.** All four were composed in fresh detached checkouts at
BASE_HEAD and at the revision-2 content tip, and revision 1's published `42b8575c…` was reproduced
at `b3afdde` as a positive control on the instrument.

```
CHANGED INPUT           exactly one of orchestrator's sixteen: roles/orchestrator.md
NOT FINGERPRINT INPUTS  BOOTSTRAP.md · deployment/deployment_profile.md · learning/ —
                        confirmed by enumerating the input set, so the three larger edits of
                        this revision rotate nothing
P2.2 COMPOSITION        untouched — the candidate changes no fingerprint composition
A.6 CONSEQUENCE         only orchestrator checkpoints are invalidated for resume. Plan, Mirror
                        and Scientist checkpoints remain compatible
```

---

## 15 · Gates, LINT, regression

```
LINT @ candidate   PASS — 1 INFO (MISSING_WIKILINK, CLAIM 010)
LINT @ BASE_HEAD   PASS — the SAME 1 INFO → pre-existing, verified rather than asserted
PUBLICATION GATE   PASS · BLOCKS 0 · 4 REVIEW items, pre-existing
```

**Regression — compared as sets, in matched environments.** `run_release_regressions.py` reports
`REGRESSION VERDICT: FAIL` at the candidate **and reports the identical failing set at BASE_HEAD**:

```
SUITE SET              IDENTICAL — 65 suites
FAILING SET            IDENTICAL — 6 suites, by name:
                         scripts/test_release_runner_verdict.py
                         scripts/test_locator_obligation_reaches_every_route.py
                         scripts/test_abstract_corpus_is_not_evidence.py
                         scripts/test_release_surface.py
                         scripts/test_fulltext_trace_contract.py
                         framework/scripts/test_session_self_eval.py
TEST-NAME/OUTCOME SET  IDENTICAL — 476 test lines each side, zero differences
REGRESSION DELTA       0
```

**Both sides were run in fresh detached checkouts**, at `04693e68` and at `7b6a9d9`. A first
comparison against the working worktree showed four `skipped → ok` differences; the cause was
traced rather than assumed — `files/` is git-ignored (`.gitignore:7`), the working worktree holds
13 full-text entries and a fresh checkout holds 0 — and the comparison was redone in matched
environments, where the difference disappears.

**Cause of the red suite, traced independently (N-4).** Four shebang entrypoints carry mode
`100644` in the git tree at BASE **and** at the tip — `lease_state.py`,
`candidate_content_hash.py`, `governance_fingerprint.py`, `test_candidate_content_hash.py` — and
`test_release_surface.py::test_shebang_python_entrypoints_are_executable` requires
`st_mode & 0o111`. **A pre-existing red suite at canonical main, unchanged by this candidate, and
deliberately not repaired here.**

---

## 16 · What this candidate does NOT claim

Stated as a list because revision 1's defect was a claim that outran its evidence.

- **It does not claim the Orchestrator surface is resolved.** `PARTIALLY_RESOLVED — HUMAN_REQUIRED`.
- **It does not claim Annex I.2 is amended, superseded, or interpreted away.** It is FROZEN, it
  still mandates the legacy topology, and this candidate says so in three content files.
- **It does not claim a fresh bootstrap can complete.** It claims a fresh bootstrap cannot silently
  do the wrong thing, which is a smaller and checkable claim.
- **It does not claim the runtime residual is repaired.** `SAFE_CARRIED`, with an owner.
- **It does not claim the regression suite is green.** It is red at main and red here, identically.
- **It does not claim Routing is advanced.** Three holds stand, none of them Plan's to lift.
- **It grants no approval and implies none.** `HUMAN_APPROVAL: NONE`. `main` UNCHANGED at
  `04693e68`.
