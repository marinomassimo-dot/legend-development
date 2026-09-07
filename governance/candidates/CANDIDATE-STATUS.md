---
artifact: CANDIDATE STATUS REGISTER
maintained_by: plan
updated_on: 2026-08-17
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT, so maintaining
  this register moves no candidate's content hash
purpose: one place that says which candidates exist, what state each is in, and on whose evidence
status_field_form: value · since_event · owner — the transitional form C-9 §6 proposes, used here
  because a status register is the artifact that goes stale first
---

# Candidate status

## 2026-08-18 — `ORCHWT` CANONICAL. The convergence event has happened.

```
main                     005888b6 → f5b321556e5f1f081482f13fbbabb4f90f3d6295
orchestrator worktree    .claude/worktrees/orchestrator @ 632ad22 — verified present
EVAC-20260817-001        9 of 9 returned · 0 digest mismatches · 0 destination clashes
runtime/ instance        agent_card_registry.md · runtime_inventory.md — verified present
```

**Three canonical batches in one day**, and the third changed what this laboratory is: the
Orchestrator has a worktree, the root is a `CANONICAL_BATCH_COMMIT` surface and nothing else, and
`632ad22` is the first commit an Orchestrator has ever made outside the root.

🔴 **Everything that was recorded as resolving "at the same event" has resolved.** Three separate
items were parked on `ORCHWT` execution across two days — the lease sunset trigger, the evacuated
files' return, and **P1's precondition**. All three land here.

**`P1` → `SATISFIABLE, NOT ATTEMPTED`.** The object exists again, verified on the `orchestrator`
branch — and it is now **tracked**, readable from the root via git, **which is a different state
from the one it held before the evacuation**, when it was merely present. The evacuation's
reversal did not restore the prior condition; it improved on it.

**It is not attempted.** No authorization covers it in the message conveying this, and **a
precondition becoming satisfiable is not an instruction to act** — the same reading the
Orchestrator applied to its own `O4` flag, and the rule is not about which actor benefits.
Recorded as a live row for the next L2 pass, under whatever authorization covers that pass.

### P1 SMOKE TEST — executed by Plan, in Plan's worktree, 2026-08-18

**Outcome: `CRITERION_MET / NAME_NOT_DELIVERED`.** Not `VERIFIED`.

**Population 1 — the five validators `CLAUDE.md` §3 names.** All `rc=0`:

```
legend_lint.py .                      PASS (1 INFO: MISSING_WIKILINK)
fulltext_receipts.py verify           OK: 128 chained receipts, tail anchored
growth_anchors.py check               VERDICT: PASS
public_release_gate.py                PASS (1 REVIEW item)
governance_fingerprint.py compose --all   PASS, four role fingerprints emitted
```

**Population 2 — the registry instance**, read from `orchestrator@632ad22`:
`agent_card_registry.md` 314 lines / 30 table rows · `runtime_inventory.md` 551 lines.

🔴 **The finding the operator invited: the registry's presence was NOT what this row was blocked
on.**

The row was recorded `SUBORDINATE — precondition unmet (no registry instance)`. But **the five
validators run to `PASS` without the registry, and always did** — none of them reads it. What the
absence blocked was the *registry* half of *"Registry / structural validation"*, and **there is
no registry validator.** The object is back and **still nothing validates it**; reading 314 lines
and counting 30 rows is measurement, not validation.

So the block was correctly identified and **the remedy does not discharge it.** The criterion —
*"run the repository validators and report"* — is met. The capability's **name** is not
delivered. **Same shape as `M2`/`S6`**, and this time on Plan's own row, from the opposite
direction: there the criterion was too weak for the name, here the criterion is met and the name
covers an object no criterion reaches.

🔴 **Second finding, and it is about the tester.** Plan's *first* run reported three validators
failing with `can't open`. **False.** The harness used `python3 $v` with an unquoted variable —
and **zsh does not word-split unquoted parameters**, so `"legend_lint.py ."` was passed as a
single filename. The validators were never at fault.

**This is the third occurrence of that exact defect in this session**, twice previously recorded.
A smoke test whose first result was a harness artifact is the day's signature landing on the
instrument one final time — and it is only visible because the failure was investigated instead
of retried.

**`SLR-C2-001` and `SLR-ORCH-002` are durable again but still carry no Mirror-verified
confirmation class.** `E.2` assigns that to Mirror; their current classes are the author's
assertions about the author's own records. **The return changed their availability, not their
status** — which is what was recorded when they were frozen, and it held.

## 2026-08-18 — HANDOFF: the lease sunset candidate is Plan's to author · **NOW AUTHORIZED, still not started**

**Preparation authorized by the operator** — preparation only, not part of any batch, not
executable by Plan, and it reaches Mirror as a normal candidate. **The authorization removes the
permission blocker. It does not remove the one Plan actually stated**, which was capacity, and
which is unchanged.

**The operator names the distinction the candidate must not collapse, and it is binding:**

> **VISIBILITY is not LIFECYCLE ENFORCEMENT.** A tracked home makes the record readable; it does
> not make the transition happen. The candidate must treat them as different and say so.

**Off the debt list:** the seven C.2 records are **`CLOSED`** by operator determination, 7/7 both
directions. **Do not carry them into the sunset candidate.**

**Recorded durably because the specification would otherwise live only in chat**, which is the
operative clause registered in `DEC-20260818-007` today. Plan accepted the handoff and deferred
authoring it — see *why* below, which is part of the specification rather than an excuse.

```
PURPOSE   retire the interim git-ignored lease home; restore I.3's cross-actor detector
FROM      deployment/local_instance.md    untracked, .gitignore:49, unreadable by any peer
TO        a tracked file in the Orchestrator worktree that ORCHWT creates
MUST      be observable from every checkout via git, so Mirror can read a lease record again
TRIGGER   ORCHWT execution — downstream of it, NOT bundled with it
```

### The finding that decides the candidate's shape

The three lease failures caught today separate on one axis, and a tracked home answers only two:

| Failure | Does a tracked home fix it? |
|---|---|
| stored `ACTIVE` past expiry | **no** — makes it visible, not correct |
| derivation read `ACTIVE` on a released lease | already fixed by a two-input rule |
| **lease expired unused between turns, before `GATE 0` could be asserted** | **no — nothing was watching** |

**A tracked file makes the record readable; it does not make the transition happen.** That is
`DECISION 3`'s display-versus-check problem one layer down, and **the candidate must answer it
rather than inherit it.** The lease lifecycle is currently **an instruction, not a mechanism**:
the derivation tool is ephemeral and dies with its session, and the obligation to write the
terminal row is prose.

### The correction it must carry — a paragraph, not four line-edits

`main:deployment/deployment_profile.md:80–85`, under a heading reading ***Current instance —
status***, contains **four false claims in four lines**:

```
:82  "The local instance file has not been created"        FALSE — the file exists
:83  "lettore-c does not exist yet"                        FALSE — it ran S2/S3/S4/S6 today
:84  "no ORCHESTRATOR_LEASE has ever been recorded"        FALSE — 4 lease records
:85  "The first chat to run BOOTSTRAP.md creates it…"      FALSE as future tense — it has run
```

`ORCHWT` modifies that file and leaves those lines untouched, verified.

🔴 **It is not four stale fields. It is a paragraph describing a laboratory that has not
started** — still standing after that laboratory ran a qualification round, canonicalised two
candidates and recorded four leases. **Correcting it field by field would leave the tense and
the framing intact, and the next reader would inherit the same shape.**

### One further input, not a falsehood

`lettore-c` is at `908197b`, **two canonical commits behind**, as is any scientist worktree cut
before today. **Whatever this candidate says about instance status will be read from checkouts
that do not contain it.**

### Why it is deferred rather than drafted

Authoring it properly means writing the lifecycle as a mechanism, which is the hardest of the
three problems and the one nothing currently addresses. **Handing a fresh session an intact
specification is better than an artifact authored at the end of a long one** — and a candidate
about a discipline that failed for want of a watcher should not itself be produced by a tired
one.

**Nothing waits on this tonight. No lease is operative.**

## 2026-08-18 — HASHDET is CANONICAL. `main` moved, and three things follow

```
main                908197ba → c89c2217a46bf28379c7720dc957e763fa496784
evidence-index      350a6e32 — UNCHANGED, verified after; GATE 1 held
parse_p5(tip) in main   present — the determinism fix is canonical
908197ba            now an ANCESTOR of main, not main
```

**1 · `P51C9` re-baselined.** New binding
`f0671ca980d64b2e5f1ddc887a64e5cc8b62184b378119c4a23acf461572e668 @ c89c2217`, old
`f325bd9d… @ 908197ba` retired. **10/10 blob identity** against the reviewed range; the rebase
added exactly HASHDET's four files. Content unchanged — the package with Mirror re-attests the
**binding**, not the content.

**2 · 🔴 `ORCHWT`'s binding is now stale, and the report does not mention it.**
`CAND-20260817-ORCH WT` declares `BASE_HEAD 908197ba`, which is no longer `main`. Its hash
`280dc497…` was computed against that base. **It requires the same re-baseline `P51C9` just
received**, and `HA-4` deferred its approval, so nothing was voided — but its recorded binding
now describes a base that has moved. Registered here so it is not discovered at execution.

**3 · 🔴 `RES-20260817-HA-1` did not travel into canonical state.** It lives in `ledger/approvals/`
on `evidence-index`. **`main` now carries a MAJOR change while the queue authorising it is not
canonical.** `GATE 3` asks the object be in the queue and it is; *where the queue is canonical*
is a separate question. Registered rather than repaired — §7 bars the work and it is
operator-owned.

## 🔴 The delivery-scope question — `P51C9` as a range, not as a branch

The rebased branch is **44 commits**; `main..evidence-index` confirms 44. Roughly 37 landed
**after** Mirror's review — Plan's decision records, checkpoints and status registers.

**Plan's answer, and the reason matters more than the answer.** *"The hash is unchanged"* and
*"the merge is scoped to what was reviewed"* are different claims, and they differ **by
construction**: the content hash **excludes `CONTROL_PLANE_ROOTS` by design**, so control-plane
additions are invisible to it. **The identity check was built to be insensitive to exactly the
content this question is about.** It cannot detect control-plane scope creep, and it was never
meant to — which is a property of P5, not a defect in it, but it means **the hash cannot serve
as the scoping guarantee.**

That is why 37 commits could land after review with the identity never moving. The Orchestrator
notes the same property held across `b5eaf81e`, `47c7ad9`, `d070a72` and `350a6e3` — a
robustness result for the candidate, and simultaneously the reason a branch merge needs a
separate check.

**Plan recommends: deliver `P51C9` as the reviewed range replayed alone.** The decision records
are legitimate governance artifacts and most of this week's findings live in them, but **they
were not reviewed under `P51C9` and must not reach canonical state on its approval.** They need
their own path — which is a smaller and cleaner request than it looks, since they are entirely
control-plane and move no hash.

**Plan does not decide it.** Recommended, not chosen; the operator's.

> **COR-20260818-SCOPE-001 — Plan's recommendation, taken literally, was the worst of three.**
> Challenged by the Orchestrator, **measured by Plan at source before accepting**:
>
> ```
> at 05cdedae — "the reviewed range replayed alone", literally
>   BRANCH_TIP              629bc89a…      ← revision 1's tip
>   CANDIDATE_CONTENT_HASH  b1f3729b…      ← the SUPERSEDED hash Mirror REQUEST CHANGES'd
>   MIRROR_REVIEW           PENDING        ← it is ACCEPTed
>
> at 5cd7f85 — the same range plus the two records describing it
>   BRANCH_TIP              b5eaf81e…      ← revision 2
>   CANDIDATE_CONTENT_HASH  f325bd9d…
>   SUPERSEDED_HASH         b1f3729b…      ← recorded, not silently dropped
> C adds over A exactly: CAND-20260817-P51C9.md · DELTA-20260817-P51C9-SPLIT.md
> ```
>
> `47c7ad9` — *"P51C9 revision 2: manifest, provenance and delta review"* — landed **after**
> `b5eaf81e`. So the literal reviewed range ends **before** the manifest that describes it, and
> shipping it would put a manifest describing the **rejected** revision into canonical state,
> with a declared hash contradicting the object containing it. **The stale-representation class
> this laboratory catalogued all week, entering canonical state through the option chosen to be
> careful.**
>
> **The principle stands; the object it named was wrong.** *"Deliver what was reviewed, not the
> branch"* is correct. **C is what A was trying to be** — the reviewed range plus the two
> records that describe that range, nothing else, and both are control plane so the content hash
> is identical across all three.
>
> This is the record's signature landing on Plan's own recommendation: **the scope was named
> correctly and the object that name denotes is not the object intended.**
>
> **Revised: Plan recommends C**, and does not choose it.

### 🔴 None of the three is deliverable as-is — and the remedy is Plan's

Every option's manifest declares `f325bd9d @ 908197ba`. The actual binding is
**`f0671ca9…572e668 @ c89c2217`**. A rebase preserves file content, so **no replay can update
the manifest that describes the replay.**

**A revision-3 manifest is required under every scope**, declaring the new binding and recording
`f325bd9d` as **superseded by re-baseline, not by defect** — a distinction that must be explicit,
since every prior supersession in this candidate's history was a defect.

Verified additionally by Plan: even option C's manifest still reads `MIRROR_REVIEW: PENDING`,
though the review returned ACCEPT at `REV-P51C9-MIRROR-002`. **r3 must correct the review status
as well as the binding** — two stale fields, not one.

**This is candidate preparation: Plan's, under `GATE 1`.** The Orchestrator has already executed
once today against a manifest whose declared tip was one commit stale, and will not author the
manifest it would execute.

**Dependency, stated rather than discovered:** the binding is identical across all three options,
but `BRANCH_TIP` is not. **r3 cannot be finalised until the scope is chosen.** Plan will prepare
it on that decision.

> **COR-20260818-SCOPE-002 — "two stale fields" was a count against an undefined set.**
>
> Plan found two by noticing two. The Orchestrator derived them against a defined set — *manifest
> fields at option C whose declared value differs from current verifiable state* — and the answer
> is not two:
>
> ```
> STALE (6)      BASE_HEAD          908197ba       → c89c2217
>                BRANCH             evidence-index → the re-baselined branch
>                BRANCH_TIP         b5eaf81e       → scope-dependent
>                CAND_CONTENT_HASH  f325bd9d       → f0671ca9
>                MIRROR_REVIEW      PENDING        → ACCEPT        ← Plan's
>                HUMAN_APPROVAL     PENDING        → DEFERRED (HA-2)
> INCOMPLETE     SUPERSEDED_HASH    b1f3729b only  → f325bd9d joins it, different cause
> CHANGED BY ACT REVISION           2              → 3
> RE-VERIFIED    LINT · PUBLICATION_GATE — both PASS at 5cd7f85 against the new base
> ```
>
> **The count was not wrong about the two; it was wrong about being a count.** The whole record
> has been about bare numbers needing their bound, and this one was mine — the ninth instance.
>
> **🔴 One field looks stale and must NOT be "fixed".** Verified by Plan at source:
>
> ```
> canonical P5 on main   legend-candidate-v3 · roots: candidates, ledger
> P5 at the tip 5cd7f85  legend-candidate-v4 · roots: candidates, ledger, reviews/
> ```
>
> The manifest declares **v4 because the candidate introduces v4**, and `f0671ca9` was computed
> under v4 **read from the candidate's own tip** — HASHDET behaving exactly as committed this
> morning. A reader comparing the field against canonical `main` would see a mismatch and correct
> it into a defect.
>
> **🔴 And the guard is stronger than a warning, because the field verifies itself.** Confirmed
> by Plan from two independent sources — the canonical script on `main` and P5's own declared
> layout:
>
> ```
> serialized = CANDIDATE_HASH_VERSION + "\n" + BASE_HEAD + "\n" + <entries>
> ```
>
> **The version is not a label beside the computation. It is the first line of the hashed
> bytes.** Changing `v4` to `v3` changes the object and therefore changes the hash — so a reader
> who "corrects" this field produces a manifest that **no longer describes anything**, and the
> mismatch is detectable by recomputation rather than by having followed this argument.
>
> That is the property this record has been asking for all week and rarely found: **a rule whose
> violation announces itself.** After I.3's removed detector, Phase 3's unfireable ABORT, the
> transmission rule's missing diff, the manifest's unwatched condition and the lease's absent
> transition owner — here is one that has it, and it has it because the value was put **inside**
> the thing it describes rather than beside it.
>
> *(Recorded also that the Orchestrator flagged its own earlier version of this claim as
> inferred from the docstring rather than observed — in the very field it was warning against
> correcting. It then measured it. The strengthening came from that admission.)*

### The delta record selects the scope — and it makes r3's key sentence provable

Verified by Plan: `DELTA-20260817-P51C9-SPLIT.md` is **ABSENT from A** and present in C.

It is the **only canonical record of why `b1f3729b` was superseded** — `responds_to
REV-P51C9-MIRROR-001`, findings F-1/F-2/F-3, before/after, *5 commits 4 orphaned → 6 of 6
ancestry PASS*.

**Under option A that record never lands.** A reader would see `b1f3729b → f325bd9d → f0671ca9`
with no canonical explanation of any link, and **no way to distinguish the defect-supersession
from the re-baseline one** — which is precisely the confusion r3's *"superseded by re-baseline,
not by defect"* sentence exists to prevent. **Option A would make that sentence unprovable from
canonical state.**

A manifest is superseded by a manifest; **a delta record is not.** C's advantage over A is
therefore **durable, not cosmetic** — and it is the strongest argument on the page, because it is
the only one that survives everyone in this conversation forgetting the context.

## Human decisions of 2026-08-17 — one approval live at a time

| Candidate | Human decision | Effect |
|---|---|---|
| `HASHDET` r3 | **APPROVED** (HA-1) | intent approved; **not executable** — GATE 0 unmet |
| `P51C9` rev 2 | **DEFERRED** (HA-2) | review valid, no blocker; re-baseline · re-hash · new approval after HASHDET |
| `ORCHWT` | **DEFERRED** (HA-4) | same; and the §8 divergence is **not adopted** — HA-3 chose B |

`MIRROR_ACCEPTED ≠ HUMAN_APPROVED ≠ EXECUTION_AUTHORIZED`. The deferrals are not doubts about the
candidates: an approval binds to hash **and** base, and executing HASHDET moves the base, so a
second live approval would be void the moment the first executed.

## CAND-20260817-HASHDET · **MIRROR_ACCEPTED**

```
value          MIRROR_ACCEPTED
since_event    REV-HASHDET-MIRROR-003 @ e0da42b0 — verdict ACCEPT
owner          operator — the next transition is authorisation, and it is not Mirror's
branch/tip     hash-determinism @ b9af54ebe2fd24d94ec0eee71fcb064797922082
content_hash   c85acdb2d3e55f71bed9aa985ff996fdcfdd5b43c4b1e097c3b6063b80ad05d8
change_class   MAJOR — confirmed by the review
blockers       0 — "## 2 · REMAINING BLOCKERS · **None.**", verbatim
```

Verified at this update: the review commit exists, its verdict line reads `ACCEPT`, its blocker
section reads *None*, and the tip and hash it names are the r3 values this register records.

**🔴 ACCEPT is not authorisation to execute.** Mirror reviews; it does not approve, and it holds no
gate. `HASHDET` has had no `HUMAN_APPROVAL`, no snapshot, and no `GATE 0` assessment. Under Annex
D.4 and J.3 an approval would authorise the *intent* and still leave execution subject to gates
0–5 — and there is no approval here at all, only a clean review.

**Why it is nonetheless a validation prerequisite for everything after it.** `HASHDET` restores the
reproducibility of a candidate's identity: before it, the hash was a function of the checkout, so
an approval bound under gate 5 could not be re-verified by a third party and an already-approved
value decayed the moment governance moved. Every later candidate's binding depends on that
property holding. It is a prerequisite in the order of *validation*, not a licence to execute
first — those are different claims and only the first is made here.

**Four non-blocking observations (N-4) remain open**, recorded and not waived. The review is
explicit that `ACCEPT` means no blocker, not no finding.

## CAND-20260817-P51C9 · **MIRROR_ACCEPTED**

```
value          MIRROR_ACCEPTED
since_event    REV-P51C9-MIRROR-002 — verdict ACCEPT (REV-…-001 @ fe08e685 was REQUEST CHANGES)
owner          operator — DEC-1 in DECISION-RECORD-20260817 may still remove content and
               discard this acceptance
branch/tip     evidence-index @ b5eaf81ed50b3c994c6ee7cede47a2114cdcaa6c
content_hash   f325bd9d1667638eeda718b73bc106263fea3a509f832bcc62e082cdba0651da
change_class   MAJOR — amends plan_defined_parameters.md, in the CORE set of all four roles
```

Awaiting completion of the remediation and review cycle. **Content unmodified**, verified at this
update: the hash at its recorded tip is unchanged.

## CAND-20260817-ORCHWT · **MIRROR ACCEPTED — AWAITING HUMAN DECISION ON ADOPTION**

```
value          MIRROR_ACCEPTED · adoption of the §8 divergence OPEN as DEC-2b
since_event    REV-ORCHWT-MIRROR-001 — ACCEPT, no blockers, MAJOR confirmed
owner          operator — the ACCEPT covers technical correctness under Option B only; it
               adopts nothing, authorises nothing, and clears no gate
branch/tip     orchestrator-worktree @ ab4856b1d90c4361f63705f487d5285c54ecba0e
content_hash   280dc4973cf046123a3356ebdf3e8ae2e575b83d6cce9e8b7b58987f2065763d
change_class   MAJOR — authority/deployment contract change
```

Carries a declared formal divergence from §8 (Option B) that requires operator adoption, and an
open question on how the R3 STOP condition should be read. Content unmodified, verified.

*(The task text names this candidate `CAND-202617-ORCHWT`; the id of record is
`CAND-20260817-ORCHWT`, as in its own manifest. Noted rather than silently normalised.)*

## CAND-20260816-GOV311 · **CANONICAL**

```
value          CANONICAL — in main's history
since_event    canonical batch commit 908197ba, 2026-08-16
content_hash   c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
```

Recorded because it is the anchor of HASHDET's historical-replay test: it still replays exactly
from a branch carrying neither its rule nor its content.

---

## Verification performed for this update

| Check | Result |
|---|---|
| `main` unchanged | `908197ba62a064546f17c9c277ff497ffc753656` — the canonical commit, no movement |
| No `CANONICAL_BATCH_COMMIT` executed | none; Plan holds no such authority |
| Accepted candidate unmodified | `HASHDET` hash at `b9af54eb` still `c85acdb2…` |
| Pending candidates unmodified | `P51C9` `f325bd9d…` and `ORCHWT` `280dc497…`, both unchanged at their recorded tips |
| No gate bypassed | `GATE 0` not assessed, no lease, L2 suspended, no snapshot taken |
| This update's own domain | control plane — no candidate content hash moved by writing it |

## Residual blocks — none of them lifted by the ACCEPT

- **`GATE 0` cannot pass for any candidate.** No `ORCHESTRATOR_LEASE` exists and the one-commit
  exemption is spent. *(The root-clean condition is no longer among the blockers — see below.)*
- **L2 is suspended**; six Plan capabilities remain `UNVERIFIED`.
- **The status/C-8 batch is frozen** pending an operator decision.
- **C-9's clauses are accepted as a document and not adopted.**

### Cleared 2026-08-17 — the root, without moving `main`

The circularity this section used to record — the nine untracked files could not leave the root
until the Orchestrator had a worktree, which was `ORCHWT`'s subject, which needed a clean root —
was not resolved by ordering. The operator authorised evacuating the files out of the repository
entirely (`EVAC-20260817-001`), which is the one route that clears the root **without moving
`main`**. Committing them canonically would have moved `BASE_HEAD` past `908197ba` and voided
`HASHDET`'s approval hours after it was granted.

Verified independently by Plan, negative included — `git status` reporting clean and the root being
clean are different claims:

```
root, --untracked-files=all   0 entries
.git/info/exclude             0 non-comment lines — not used to conceal
.gitignore                    identical to main
git stash list                1 entry, Plan's own pre-existing one
runtime/ · learning/          absent from the filesystem, not hidden
```

**A clean root is a preparatory condition, not an authorisation.** No `GATE 0` assessment follows
from it, and the remaining blocker — the lease — sits behind L2, which is suspended.

```
GATE 0    BASE_HEAD ✓ 908197ba · root ✓ cleared · lease ✗ absent · ONE_WRITER ~ cf79f1
```

The files return on `ORCHWT`'s execution, as a `WORK_COMMIT` into the Orchestrator's new worktree
and never canonically, with SHA-256 re-checked on arrival.

## Next candidate for review

**`CAND-20260817-P51C9` revision 2.** It has been remediated (F-1, F-3) and has not been
re-reviewed; `ORCHWT` has never been reviewed at all and carries an unresolved question that is the
operator's before it is Mirror's. Plan recommends P51C9 next and decides nothing.
