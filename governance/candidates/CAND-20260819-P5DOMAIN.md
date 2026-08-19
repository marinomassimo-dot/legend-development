---
artifact: INTEGRATION CANDIDATE — § P5 domain truth
candidate_id: CAND-20260819-P5DOMAIN
task_id: P5DOMAIN-001
author: plan
worktree: evidence-index
branch: p5-domain-truth
date: 2026-08-19
governance_version: 3.1.1
change_class: MAJOR
status: PROPOSED — awaiting Mirror hostile review, which Orchestrator opens (Annex C.3)
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
partition: SPLIT — this candidate is P5 INTEGRITY only. The Orchestrator work/batch/routing-surface
  debt is analysed to a conclusion in §8 and deliberately NOT bound here. Routing Candidate B is
  NOT opened.
---

# `CAND-20260819-P5DOMAIN` — the interim ended in another file

## 0 · Binding

```
CANDIDATE_ID              CAND-20260819-P5DOMAIN
BASE_HEAD                 f70878d1cb98317ec62808987fc328be7f8f4ea8
CONTENT_TIP               ceefaa28611527d83b9f5e2209c99733a3a10afd
CANDIDATE_CONTENT_HASH    930dfefb3ce69bfaedc3920c96b3cddafbd07c9560498da4291b04b1f5476b97
CANDIDATE_HASH_VERSION    legend-candidate-v4    (UNCHANGED — the rule did not move)
DOMAIN_CARDINALITY        533 included · 40 excluded    (derived by the command, not by hand)
CHANGE_CLASS              MAJOR
LINT_RESULT               PASS — 1 pre-existing INFO (CLAIM 010 wikilink)
PUBLICATION_GATE          PASS / BLOCKS: 0 — 4 [REVIEW] lines, all in disease-models/, untouched here
MIRROR_REVIEW             REQUIRED · NOT PERFORMED · NOT ASSUMED
HUMAN_APPROVAL            NONE — not requested, not prefilled, not implied
SNAPSHOT_ID               n/a — Plan does not execute the batch
```

`SOURCE_COMMITS`: `ceefaa2` (content) and this manifest's commit (control plane).

**The hash was reproduced by a route independent of the governed script**: `--emit-domain` prints
the exact serialized bytes, and `shasum -a 256` over them returns `930dfefb…`. A negative control —
the same tip against `BASE_HEAD 4454feab` — returns `326b1773…`, so the digest is not indifferent to
its base.

---

## 1 · Problem

§ P5 is *"the single authoritative definition"* of `CANDIDATE_CONTENT_HASH`. Two sentences in it
are false. One of them is load-bearing: it is the entire safety argument for leaving a
classification question open.

Three parties — Plan, Mirror and Orchestrator — observed the inconsistency independently. This
candidate is not a finding; it is the repair of a finding already made three times.

---

## 2 · The false premises, and what is actually true

### 2.1 · The load-bearing one

§ P5.1 said, in the paragraph deferring the `runtime/` classification:

> *"While `runtime/` remains untracked it is invisible to `git ls-tree` and therefore absent from
> the domain, so no fixed point arises in the interim."*

Every clause after the first is conditioned on `runtime/` being untracked. It is not.

```
git ls-tree -r --full-tree main -- runtime/
  100644 blob c34f4866…  runtime/orchestrator_lease.md          exactly one tracked path
git check-ignore -v runtime/orchestrator_lease.md
  rc=1                                                          NOT git-ignored
--emit-domain | awk 'NR>2 {n++; …}'  at the XPORT tip
  entry 495 of 532                                              INSIDE the content domain
```

**The premise was falsified by `325da04`**, which gave the `ORCHESTRATOR_LEASE` a tracked home when
`DECISION 3` sunset — a change argued correctly and at length in the deployment profile, on the
grounds that Annex I.3 specifies the lease's `DETECTION` as *"doppio record sulla stessa
successione"* and a file no other checkout can read cannot produce one. The change was right. It
was in a different file, and nothing connected the two.

### 2.2 · The stale one

§ P5.3 closed with *"The version prefix moves to `v3`"*, eight lines below a declaration reading
`CANDIDATE_HASH_VERSION: legend-candidate-v4`. It is a leftover from the revision that introduced
`v3`, left standing when `v4` was added. Harmless to the script — which parses the declaration, not
the prose — and a direct contradiction to a reader with no way to tell which of the two binds.

---

## 3 · Actual observed behaviour — the fixed-point hazard, measured

The directive forbade assuming this was prose-only. It is not.

A throw-away clone with no checkout, synthetic trees built with plumbing, no ref updated, canonical
repository untouched. The oracle is the published `XPORT` value.

```
T0  unmodified XPORT tip                     81f241f2…    reproduces the published hash — ORACLE
T1  lease blob → the orchestrator branch's   ddc0b08d…    HASH MOVES     tree SHA verified changed
T2  reviews/ blob → the SAME blob as T1      81f241f2…    HASH HOLDS     tree SHA verified changed
T3  BASE_HEAD advanced, tree unchanged       06095c0c…    HASH MOVES
```

**`T2` is the control that carries the argument, and it is the one most easily faked.** A negative
control whose hash does not move proves nothing unless the tree *did* move — otherwise it reports
the instrument's indifference to an edit that never happened. `T2` asserts the tree SHA changed
before reading the hash, and substitutes the identical 18 837-byte blob that `T1` used, so the two
probes differ in domain membership and in nothing else.

So: **a tracked, mutable, control-plane record sits inside the domain that defines candidate
identity, and mutating it moves that identity.**

### 3.1 · Why no candidate has ever been bitten

Not because the domain excludes the hazard. Because of a convention:

```
lease rows are written on branch `orchestrator`, never on main, never on a candidate branch
```

Verified: `git log --all -- runtime/orchestrator_lease.md` puts rows #6, #7 and #8 on
`orchestrator` alone; `main` and `xport` carry the identical blob `c34f4866`, `orchestrator` carries
`2795dfe0`, 146 lines longer.

🔴 **Nothing mechanizes it.** `lease_state.py` derives `ACTIVE`/`STALE` and the singleton invariant
and has no location predicate. `batch_commit.py` is a snapshot/restore helper for the four
scientific current files and implements no gate. `GATE 0` is asserted by hand. The convention is
stated nowhere in governance; the closest thing is the lease record's own frontmatter,
`writer: orchestrator ONLY — one writer, from the orchestrator worktree`, which is a declaration
inside the artifact rather than a rule outside it, and is not a check.

### 3.2 · One consequence is structural

`GATE 0` requires an `ACTIVE` lease. A lease's terminal row is written after the batch it
authorized. **The row recording a lease can therefore never sit inside the batch that lease
authorized.** `main` carries rows #1–#5; `orchestrator` carries #1–#8.

This is not fixed by care, and it means Annex I.3's `DETECTION` is weaker than a tracked home
suggests: the rows an actor must compare to see a double succession are on a branch it has to know
to read, not in `main`. Recorded, not repaired — the repair is a classification decision, and §5
says whose.

---

## 4 · Authority

```
PROPOSER          plan     — D.2 delegates the CANDIDATE_CONTENT_HASH definition to Plan
                             ("tree/patch deterministico definito da Plan"); H.1 gives Plan
                             "Integrazione strutturale / candidate"; roles/plan.md permits
                             maintaining the governance as a governed change
REVIEWER          mirror   — Annex G.1 MIRROR_REQUIRED; C.1 floor R4 METHOD
ADJUDICATOR       orchestrator — AUTHOR != REVIEWER != ADJUDICATOR (C.3)
HUMAN APPROVAL    REQUIRED — H.1 "Spese / MAJOR approval / governance | Operatore"
EXECUTOR          orchestrator — CANONICAL_BATCH_COMMIT, sole, under ACTIVE lease, gates 0–5
```

`CHANGE_CLASS: MAJOR` is not in doubt: §12's strict definition is *"SOLO governance/authority/gate/
epistemic policy"*, and this edits the definition that `GATE 0` and D.2's approval binding both
reference. Where classification were doubtful, H.1 gives the call to Mirror, fail-closed.

**Plan is authorized to propose this. Plan is not authorized to decide the classification question
in §5**, and does not.

---

## 5 · What this candidate deliberately does NOT do

§ P5 routes the `runtime/` classification to C-9 §7.2. That proposal is `ACCEPTED` with
`acceptance_is_not_adoption: true`, `status_transition_owner: operator`, and

> `hold: no implementation and no governance modification until that review completes`

Declaring `runtime/` a control-plane root here would answer the question the hold reserves, under a
different name, in a candidate whose stated remit is two false sentences. **That is the
self-authorization a hold exists to prevent** — the failure `SLR-plan-0007` L-4 already recorded
about Routing, arriving a second time by a different door.

So the classification stays open, the debt is recorded with its owner, and the mitigation is
declared `PROCEDURAL` rather than described as an enforced invariant.

---

## 6 · Options considered

| | Option | Verdict |
|---|---|---|
| **P5-A** | prose alignment only | **SELECTED, extended** — see below |
| **P5-B** | domain reclassification: exclude `runtime/` or the lease path | **REJECTED — barred, not merely unattractive** |
| **P5-C** | write-surface / ordering guarantee, path stays in domain | **REJECTED on the structure, not on the difficulty** |
| **P5-D** | detector without classification | **DEFERRED with a named owner** |

**P5-A as selected is not "prose only".** Correcting the sentence without stating what replaces its
guarantee would leave the section silent on a hazard it had previously denied — a smaller false
impression than the one removed, which is still a false impression. The amendment therefore
corrects the sentence *and* carries the three measured values, the convention, the
`PROCEDURAL`/`MECHANIZED` distinction and the structural consequence of §3.2.

**P5-B is barred by §5**, and the bar is worth stating precisely because P5-B is probably right on
the merits: the lease is control plane by § P5's own definition — *"artifacts whose function is to
describe or manage … an actor's runtime state"* — and is currently content by omission. It also
faces § P5's own objection that declaring a root for `runtime/` *"would treat a container as a
class"*. Both point at C-9 §7.2, and both are the operator's to close.

**P5-C cannot work, for a reason independent of mechanization.** Freezing the lease between binding
and execution does not address §3.2: the terminal row is written *after* the batch, so no ordering
guarantee can place it inside. And the mechanization is unavailable anyway — the lease record itself
states that *"nothing executes between turns"*.

**P5-D** — a check that a candidate's tip mutates no tracked `runtime/` path — would mechanize §3.1.
It is not here because a detector that enforces a classification is one step from making it, and
because the candidate's remit is two sentences. Carried, owner named: it belongs with the C-9 §7.2
closure, not before it.

### 6.1 · Guarantees, per option

```
                        P5-A (selected)                      P5-B                    P5-C
GUARANTEE_PROVIDED      § P5 states only true things;        the hazard cannot        none that
                        the hazard is disclosed with its     arise: mutation of       survives §3.2
                        mitigation named as procedural       the lease cannot
                                                             move identity
FAILURE_MODE_STILL      a lease row committed to a           a control-plane          the terminal
_POSSIBLE               candidate branch or to main still    artifact's history       row is still
                        moves the binding — nothing          stops being part of      outside the
                        prevents it                          candidate identity       batch
DETECTION               binding mismatch at GATE 0, or       --show-domain prints     —
                        Mirror re-deriving the hash          every excluded path
RECOVERY                re-bind; approval re-sought,         n/a                      —
                        because D.2 binds approval to
                        hash + BASE_HEAD
BLAST_RADIUS            all four CORE fingerprints (§7)      same, plus every         —
                                                             future binding's domain
BACKWARD_COMPAT         total — no rule changed              prefix must move to v5   —
HASH_COMPATIBILITY      no published hash moves              no published hash moves; —
                                                             v4 values stay valid
MIGRATION IMPACT        none                                 none, by construction    —
```

---

## 7 · Hash and governance impact

### 7.1 · No published hash moves, and this was checked rather than asserted

The domain rule — version prefix and the three control-plane roots — parses **identically** before
and after. Verified with a mutation control that adds `- runtime/` to the roots block, to prove the
checker can see a rule change at all.

`candidate_content_hash.py` has read the rule **from the tip being hashed** since `b2c326b`, so a
historical value is computed under the governance its own commit carries. Re-derived from this
branch: `XPORT` at `(4454feab, 86dfe297)` still returns `81f241f2…`. **Editing § P5 prose cannot
move a historical hash, and none was recomputed.**

### 7.2 · 🔴 All four role fingerprints move — declared, not buried

`plan_defined_parameters.md` sits in `CORE`, which binds every actor.

```
                 BASE_HEAD f70878d1        content tip ceefaa2
mirror           3dff8954…            →    e01b4108…
orchestrator     e2c54470…            →    88dea7a6…
plan             9c0c13fb…            →    0d6987bd…
scientist        82423a48…            →    b66959cd…
```

P2.2: *"A change inside CORE invalidates all in-flight checkpoints, which is the intended
behaviour."* On canonicalization this is a `GOVERNANCE_UPDATE` requiring ACK, and H.2's *"mismatch
su area → assegnazioni sospese"* applies until each actor re-ACKs.

### 7.3 · 🔴 And that is itself a calibration signal, which is Mirror's to weigh

P2.3 names the exact condition to watch:

> *"If that stops being true — if the body starts absorbing minor edits — the composition is too
> broad and must be narrowed to sections. A.6 assigns Mirror the monitoring of the invalidation
> rate; this is the specific signal to watch."*

P2.3 says it of the body. **The same argument applies one file over, and more sharply**:
`plan_defined_parameters.md` is hashed whole in `CORE`, and unlike the frozen body it is by
construction the file Plan amends as ordinary business. This candidate is the demonstration — a
correction to two prose sentences, changing no rule, invalidating every in-flight checkpoint of
every actor.

**Plan does not propose narrowing the composition here** — that is a P2 change, it is Mirror's
monitoring duty under A.6, and doing it inside a candidate about P5 would be the same overreach §5
declines. It is surfaced as a data point, with its measurement.

---

## 8 · The Orchestrator surface debt — analysed, NOT bound here

Executed to a conclusion because the directive required it, and reported here rather than fixed.

### 8.1 · Execution is not ambiguous

Annex D.1, `FROZEN`, distinguishes:

```
WORK_COMMIT              ogni attore, proprio branch — obbligatorio, non canonico
CANONICAL_BATCH_COMMIT   solo Orchestrator, root, gate 0–5
```

Both bind Orchestrator, and they name different surfaces on purpose. The root's branch is `main`,
so an Orchestrator resident in the root has no branch on which a `WORK_COMMIT` is possible — which
is precisely the argument `deployment/deployment_profile.md` already makes, at length, in the
section that gave Orchestrator a worktree. **Annex D.1 is correct, is higher precedence than a role
rule (body §5 rank 1 vs rank 4), and is not touched by anything proposed here.**

```
ORCHESTRATOR EXECUTION AMBIGUITY        NO
WORK_COMMIT SURFACE                     the `orchestrator` worktree, branch `orchestrator`
CANONICAL_BATCH_COMMIT SURFACE          the root checkout, branch `main`, batch window only
```

### 8.2 · The label is ambiguous, and the role contract contradicts itself

`roles/orchestrator.md` frontmatter: `worktree: the repository root checkout`.
`deployment/deployment_profile.md`: `orchestrator` — its own worktree.
Every other contract names a worktree: `plan → evidence-index`, `mirror → mirror`.

The frontmatter has been touched **once**, at `a8cd125` (2026-08-16), the original materialization.
`e861dc4` — *"The Orchestrator gets a worktree, on its own branch and nothing else"* — rewrote the
deployment profile and never updated it. **It is a pre-ORCHWT artifact, not a competing position.**

And the same file's body already refutes its own frontmatter:

> *"**Position in the root confers nothing.** … A chat that opens in the root and finds a valid
> ACTIVE lease is **not** Orchestrator; it is an OBSERVER."*

### 8.3 · The `--cwd` divergence — reproduced

`claude agents --json --cwd <path>`, CLI 2.1.232, 2026-08-19T17:35:40Z, read-only, no session
elected:

```
--cwd <root>                        24    10 evidence-index · 9 mirror · 4 root · 1 lettore-c
--cwd <orchestrator worktree>        0
--cwd <evidence-index>              10    POSITIVE CONTROL — the query CAN return non-zero
```

```
ORCHESTRATOR --cwd DIVERGENCE       CONFIRMED
```

**The two readings do not disagree about which session is Orchestrator's — one of them returns
every other actor's.** `--cwd` matches a subtree, and every worktree lives under the root at
`.claude/worktrees/`. The root reading is not a hard-to-evaluate answer; it is the universal set
shaped like one, and it contains no Orchestrator at all. The `0` is the honest result.

Session `name` is derived from the cwd leaf (`evidence-index-56`, `mirror-9c`, `legend-public-12`),
so name and cwd are one attribute rather than two, and a resolver keying on either keys on both.

### 8.4 · Remediation class, and who owns it

```
ORCHESTRATOR SURFACE REMEDIATION CLASS   correct the stale frontmatter to the assigned worktree,
                                         and type the attribute so a resolver cannot read a
                                         canonical-execution surface as an actor-home surface
FROZEN GOVERNANCE CHANGE REQUIRED        NO — Annex D.1 and Annex H.1 are untouched; the defect is
                                         one frontmatter line in a `status: PROPOSED` contract
OWNER                                    plan proposes (roles/ is Plan's to maintain) ·
                                         mirror reviews · operator approves (governance, MAJOR) ·
                                         orchestrator executes
```

Design class **C** — *cwd is prohibited as an Orchestrator identity discriminator* — is the one the
measurement supports, because containment makes the root non-discriminating for **every** actor,
not only for Orchestrator. It is recorded as the analysis outcome and **not selected here**:
selecting it is the next candidate's decision, on its own evidence, under its own review.

---

## 9 · Partition

```
PARTITION            SPLIT
FIRST CANDIDATE      P5
```

**Rationale, stated so it can be attacked independently of the content.** The two debts share no
semantics. P5 is candidate-integrity and hashing; the Orchestrator surface is actor-location and a
future resolver. Neither depends on the other: the surface fix needs a correct binding, and the
binding demonstrably works; P5 needs no fact about worktrees. *"Both block Routing"* is not a
dependency, and the directive is right to say so.

P5 goes first on blast radius rather than on urgency of symptom: every future candidate's identity
is computed under § P5, and a section that is authoritative and false is worse than a section that
is stale about a label. The Orchestrator surface has **no execution consequence today** — §8.1 —
and its only consequence is to a resolver that four holds already block from being built.

**What would change this ordering:** if Mirror finds that the Orchestrator frontmatter is load-
bearing for something already executing, it goes first. I looked and found only D.1-governed
execution, which is unambiguous.

---

## 10 · Routing holds — accounting only, nothing lifted

```
C-9 §7.2                              OPEN — ACCEPTED, acceptance_is_not_adoption: true,
                                      status_transition_owner: operator, hold in force.
                                      HUMAN_REQUIRED. This candidate respects it (§5).
BUILD_MINIMAL_DIRECTORY               OPEN — 🔴 PROVISIONAL pending operator acceptance;
                                      framework/state/actors.yaml still ABSENT at main,
                                      Phase 0 still never executed. Verified this session.
MULTI_AGENT_ARCHITECTURE_FEASIBILITY  OPEN — PRESERVED, NOT AUTHORIZED, NOT STARTED. Its entry
                                      condition depends on a provisional recommendation.
E5                                    PARTIALLY_RESOLVED — the central negative is FALSIFIED
                                      (below). The re-run is still owed and is not Plan's to
                                      close; E1 and E2 remain INCONCLUSIVE and untouched.

ROUTING READY FOR CANDIDATE B         NO
```

### 10.1 · E5, with the instrument discipline the finding requires

E5 concluded *"Not obtainable: `session_ref` … the field is dropped from the schema"*. That was
measured through `ListAgents`. Through a second instrument it is false, and this session
demonstrated **self**-observation rather than peer observation:

```
CAPABILITY        an actor observing its own SESSION_REF
INSTRUMENT SET    claude agents --json  +  ps ancestor-pid walk
RUNTIME SCOPE     this machine, VISIBLE_VSCODE profile
VERSION           CLI 2.1.232
OBSERVATION       sessionId 8070f738-419e-45c0-b071-8da0224eb4ab · name evidence-index-56
INDEPENDENT       the same UUID appears in this session's own scratchpad path, assigned by the
ORACLE            harness and not read from the CLI — two routes, one value
```

**This is not a claim that E5 is resolved.** One negative in one experiment is falsified. Phase −1
is a report with three experiments, two of them `INCONCLUSIVE` with one cause never established,
and re-running it is owned elsewhere. *Not observed via tool X* was never *not obtainable*; the
converse discipline applies equally to me — *observed on this machine at this version* is not
*obtainable in every runtime*.

---

## 11 · Carried debts

```
runtime/ classification                 OPEN · owner: C-9 §7.2 closure, operator
the P5-D detector                       OWED NOT BARRED · belongs with that closure
Annex I.3 DETECTION weaker than claimed §3.2 · recorded, not repaired
Orchestrator surface                    ANALYSED, UNBOUND · §8 · next candidate
P2 composition calibration              §7.3 · Mirror's monitoring duty under A.6
CHK-plan-0018 entry index off by one    reported, NOT repaired — XPORT is canonical and closed
lease rows #6–#8 uncanonicalized        15 commits on branch `orchestrator` await integration;
                                        whichever candidate carries them will carry a lease blob
                                        into main, which §3 is the analysis of
T-TRANSPORT-1                           still NOT_RUN · unchanged · not this candidate's
```

---

## 12 · What Mirror is asked to attack

Listed in the handoff, `HANDOFF-P5DOMAIN-MIRROR.md`. The four I most expect to lose:

1. **Is P5-A under-reacting?** A hazard is measured and the fix is deferred to a hold. Argue that
   the hold does not in fact cover a *domain* correction, or that disclosure without mechanization
   is the same defect XPORT's §7 was criticized for.
2. **Is the convention in §3.1 real?** I claim lease rows are written on `orchestrator` and that
   nothing enforces it. Find it written in governance, or find any check constraining a lease row's
   write surface, and the central claim weakens.
3. **Is §3.2 actually structural**, or have I mistaken a procedure for a necessity?
4. **Does §7.2 disqualify the candidate?** Moving all four CORE fingerprints to fix two sentences
   may be a worse trade than leaving them false until a larger P5 change carries the cost.

---

## 13 · Session Learning Review

`learning/plan/SLR-plan-0009.md`, inside the content tip at `ceefaa2`, written **before** binding.
Three learnings, all `PROPOSED`; E.2 curation is Mirror's and Plan does not self-ratify.

---

## 14 · Not done

```
main                     UNCHANGED at f70878d1cb98317ec62808987fc328be7f8f4ea8
canonicalization         NOT PERFORMED — Plan may not (GATE 1: proponente != esecutore)
HUMAN_APPROVAL           NOT GRANTED, NOT PREFILLED
XPORT                    NOT REOPENED, NOT MODIFIED
Routing Candidate B      NOT OPENED
CURRENT sessions         NOT DECIDED — no session elected, superseded, closed or renamed
Scientist A / B          NOT ACTIVATED · Scientist D NOT CREATED
BENCH-AB-001             NOT STARTED
historical sessions      NOT CLEANED — the 24-session population is left as evidence
Mirror historical ACCEPT NOT REWRITTEN
snapshot tags            NOT RECREATED
scientific current files NOT TOUCHED
```
