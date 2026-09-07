---
artifact: MIRROR hostile review (Annex C.2)
review_id: REV-XPORT-MIRROR-002
object: CAND-20260819-XPORT rev 2 · CANDIDATE_CONTENT_HASH 81f241f2…6e1f @ base 4454feab
level: R4 (MIRROR_REQUIRED — Annex G.1: a normative protocol binding every actor; MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted, none implied here
date: 2026-08-19
scope: TRANSPORT ONLY, and within it the truthfulness/generalization remediation of M-1. Actor
  session lifecycle, CURRENT routing, activation and supersession are NOT canonicalized by this
  object and were not reviewed as if they were.
supersedes: nothing. REV-XPORT-MIRROR-001 stands unedited as the review of revision 1; this is a
  separate artifact about a separate revision.
verdict: ACCEPT — M-1 is repaired in CONTENT, in the artifact that canonicalizes, and the
  replacement property is true, falsifiable and stronger than the sentence it replaces. Four
  non-blocking findings, all about counts and instruments, none about semantics.
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the
  candidate content tip
reviewer_runtime: 2.1.233, observed from this session's own owning process image — SAME runtime as
  REV-XPORT-MIRROR-001. No version mismatch, so no revalidation was triggered for prior runtime
  evidence. `claude --version` on PATH reports 2.1.232 and is not evidence about this session.
---

# The semantics closed on the first attempt, and every defect left is a number

Reviewed from `R-1`. **VERDICT TRANSFER: NONE.** No finding of `REV-XPORT-MIRROR-001` was carried
forward on Plan's report that behaviour is unchanged. Every number below was re-derived in
detached worktrees of `BASE_HEAD` and of the candidate content tip, or observed live from this
session's own runtime. Never in another actor's worktree, never in root.

**One sentence.** Revision 2 does exactly what it says: it removes two false self-describing
sentences from the normative artifact and replaces them with the property that was meant, which I
independently verify is true. It also confirms — correctly — that the wording *I* suggested in
`M-1` was itself false of the file. What it does not do cleanly is count: four of its tallies are
loose, one is off by one, and one requires two mutually inconsistent taxonomies to be true at
once. None of them is operative, none is in the normative artifact, and none changes the verdict.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd                  <REPO_ROOT>/.claude/worktrees/mirror
git top-level        <REPO_ROOT>/.claude/worktrees/mirror   IDENTICAL
branch               mirror
HEAD                 dbd44feee5ae8fac4430529ccc560e05d2c37e3d
git status           clean
ACTOR_ID             mirror
ROLE CONTRACT        roles/mirror.md — READ IN FULL at this worktree
```

`pwd` == git top-level == assigned Mirror worktree. **MIRROR WORKTREE: PASS.**

Reconstructed from durable repository state, not from this chat:

| item | source | value |
|---|---|---|
| review authority | `roles/mirror.md` "Hostile review layer" + Annex C.2 | review under the single format; `CONFIRMED` means *no defect found given the evidence bundle*, never *true* |
| perimeter | Annex G.1 via `roles/mirror.md` | `MIRROR_REQUIRED` for MAJOR, protocols and governance, R4 → this object qualifies on three grounds |
| allowed writes | `roles/mirror.md` | `reviews/mirror/`, `learning/mirror/`. **No write to CONTENT, no write to the candidate, no write to `main`** |
| forbidden | `roles/mirror.md` "Mirror does not review itself" | no self-approval of its own rubric; **no command over any actor; produces no primary evidence** |
| proposer/reviewer/executor | Annex G.2 route | proposer `plan` · reviewer `mirror` · executor/adjudicator operator. I am none of the other two |
| E.2 | Annex E.2 via `roles/mirror.md` | epistemic curation of learning is Mirror's; the author proposes and may not self-ratify |
| P5 binding | `governance/plan_defined_parameters.md` § P5 **at `main`** | `legend-candidate-v4`, three CONTROL_PLANE_ROOTS |
| SLR obligation | body §15, Annex E.6, `roles/mirror.md` | SLR every significant session, persisted by `WORK_COMMIT` |

🔴 **One rehydration fact that changed a method.** The `mirror` branch is **not** a descendant of
`main`: `git merge-base 4454fea HEAD` → `908197ba`, with 49 `main` commits absent here. Its
checked-out `governance/plan_defined_parameters.md` is therefore a **stale `legend-candidate-v3`
with two control-plane roots**, while canonical P5 at `main` is **`legend-candidate-v4` with
three**, `reviews/` having been added. `candidate_content_hash.py` reads P5 from its own working
tree. **Computing this candidate's binding from the Mirror worktree would have computed it under a
superseded rule.** Every binding number in §16 was therefore produced in a clean detached worktree
at the candidate tip, which carries canonical v4.

**Measured, not merely reasoned about.** The same command, same `--base`, same `--tip`, run from
the Mirror worktree:

```
from the MIRROR worktree (stale v3)   included 533 · excluded 37
                                      8e1829c27e7c1289e478a7bb940b3dade6a8a337e9d64e53f52dde45e0f02436
canonical v4, detached at the tip     included 532 · excluded 38
                                      81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f
the one extra entry v3 includes       reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md
```

🔴 **The extra entry is the author's response to my own previous review.** Under the stale rule,
this candidate's identity would have absorbed a document written *about* it by its author in answer
to *me* — the exact fixed point P5 v4 added `reviews/` to prevent. The digest would have disagreed
with the published one, and the cheapest available explanation for a disagreeing digest is that the
candidate is wrong.

**MIRROR REHYDRATION: PASS. ROLE CONTRACT: READ AND VERIFIED.**

---

## 0A · Manual review endpoint — OBSERVATION ONLY

```
SELECTION METHOD      MANUAL OPERATOR SELECTION
PURPOSE               Revision-2 independent review
SESSION_REF           UNAVAILABLE — not observed. No instrument was run that returns it
SESSION RUNTIME       2.1.233 — OBSERVED
CURRENT ROUTING CLAIM NONE
SUPERSESSION CLAIM    NONE
REGISTRAR CLAIM       NONE
```

**How the runtime was observed, and why not with `claude --version`.** The owning process of this
session is pid 65466, whose command is
`<HOME>/.vscode/extensions/anthropic.claude-code-2.1.233-darwin-arm64/resources/native-binary/claude`.
The runtime is read from that process image. `claude --version` on `PATH` returns **2.1.232** — a
different binary, which hosts no session.

🔴 **The protocol under review predicted this exact observation, and it fired correctly on its
second reader.** §3: *"An actor establishes its own runtime version from its own process image or
its own transcript's `version` field. A machine-level version string is not evidence about any
session, including the one reading it."* Had I used the PATH CLI I would have recorded 2.1.232 and
declared a version mismatch against `REV-XPORT-MIRROR-001`'s 2.1.233 that does not exist.

**Consequence for §13:** this session runs **the same 2.1.233** as the revision-1 review. There is
no version mismatch, so no prior runtime evidence enters `REVALIDATION_REQUIRED`, and none was
silently inherited across a mismatch that did not occur.

No session was closed, cleaned, renamed, activated or superseded. No historical session touched.

---

## 1 · Canonical base and revision chain — verified, nothing assumed

```
main                       4454feab72b7a0edf65f191be62aeedd899a15ad   UNCHANGED ✅
merge-base(main, xport)    4454feab72b7a0edf65f191be62aeedd899a15ad   → base is an ancestor
branch xport tip           86dfe297de7a7ccc286d815b0d4be786a3b0e31e
REV1 content tip           f48a807f7ba7b5b71c0ba5dd5d2361fc7dca57e4   exists, is a commit
REV2 content tip           e839db38382781564a9767fe206eefd5fba0467c   exists, is a commit
REV2 manifest tip          86dfe297de7a7ccc286d815b0d4be786a3b0e31e   exists, is a commit
ancestry  f48a807 → e839db3 → 86dfe29                                 all ANCESTOR ✅
```

**REV1: SUPERSEDED BY REV2, NOT REWRITTEN.** `f48a807` is reachable, is an ancestor of the
revision-2 tip, and its tree still contains the two false sentences verbatim — which is how §4
below reproduces `M-1` from the object rather than from a report. Revision 1 was superseded by
appending commits, never by rewriting history.

**MAIN: UNCHANGED.** `4454feab` is byte-for-byte the value the operator declared and the value
`REV-XPORT-MIRROR-001` bound to.

---

## 2 · The handoff package — read, and treated as navigation

`governance/candidates/HANDOFF-XPORT-MIRROR.md` §-R2 read in full at `86dfe29`. It is control
plane and I used it only to locate the object. Every claim it makes was re-derived. Its two red
warnings — that recording a manifest value produces a further manifest tip, and that
`git diff f48a807 e839db3` is the wrong instrument for isolating content — are both correct, and
§8 below shows the stronger instrument that settles the second.

---

## 3 · The previous review, and what M-1 actually was

`reviews/mirror/REV-XPORT-MIRROR-001.md` (953 lines — Plan's count of it is exact) and
`learning/mirror/SLR-mirror-0015.md` read in full.

**M-1 reconstructed, and it was not a wording preference.** The defect was that canonical CONTENT
stated a **literal absence property** — *no actor, role, worktree or benchmark is named* — which
was **false of the same file**, while the substantive semantic property — *no actor-specific
transport behaviour* — was **true**. A truthfulness defect in the artifact that canonicalizes, with
the concession filed in a control-plane manifest that moves no hash and does not travel beside the
protocol.

---

## 4 · Revision-1 M-1 — REPRODUCED from Git

The two operative assertions, quoted from `f48a807`:

```
line 16–17   actor_scope: ACTOR-GENERIC. Nothing in this protocol names an actor, a role, a
             worktree or a benchmark. It binds every actor that sends or receives a
             cross-session message.
line 424     - does not name any actor, role, worktree, or benchmark;
```

**Independently reproduced occurrence inventory at revision 1 — my own sweep, not Plan's
classifications.** Case-insensitive over the whole file, then filtered to *proper names* rather
than the common nouns `actor`/`role`/`worktree`/`benchmark` and the generic variable `ACTOR_ID`:

| line | name tokens | form |
|---|---|---|
| 5 | `Mirror` | capitalized role |
| 30 | `roles/plan.md` | role-contract path |
| 281 | `scientist-a` | actor id |
| 346 | `Plan`, `Mirror` | capitalized roles |
| 365 | `plan` | actor id |
| 366 | `mirror`, `scientist-a`, `scientist-b` | actor ids |
| 367 | `plan` | actor id |
| 389 | `Plan` | capitalized role |

```
8 name-bearing lines: 5, 30, 281, 346, 365, 366, 367, 389
11 name tokens
4 distinct actors named: plan, mirror, scientist-a, scientist-b
2 distinct roles named:  Plan, Mirror   (+ the role-contract path roles/plan.md)
```

My line set matches Plan's and matches `REV-XPORT-MIRROR-001` exactly. **REV1 M-1: REPRODUCED.**

**ORIGINAL FALSE ASSERTIONS: 2** — `cross_session_transport.md` @ `f48a807` line 16 (frontmatter
`actor_scope`) and line 424 (§11 bullet).

---

## 5 · Revision-2 remediation text — TRUE, FALSIFIABLE, and not a reversion

Both assertions are gone from `e839db3`. The replacement, quoted:

```
frontmatter  actor_scope: ACTOR-GENERIC in the semantic sense, which is the only sense in which
             it is true. No rule, no branch and no obligation in this protocol is conditioned on
             which actor is acting; … Actor, role and worktree names DO occur in this file …
§11          - does not condition any rule, branch or obligation on any actor, role, worktree or
             benchmark — §11.1 states that property, the three classes in which names do
             legitimately occur here, and the falsifier that tests it;
§11.1        THE PROPERTY. No rule, no branch and no obligation in this protocol is conditioned
             on which actor is acting. Every clause is stated over any actor, and a new actor
             needs no new transport clause.
```

Judged against the five required properties:

| | requirement | verdict |
|---|---|---|
| **A** | must be TRUE | **PASS** — §6 and §10 verify it occurrence by occurrence and clause by clause |
| **B** | must be FALSIFIABLE | **PASS** — §11.1 declares the falsifying form explicitly: *any clause of the form "if the actor is X, transport rule P applies, otherwise Q"*. It can fail |
| **C** | preserves generic Transport semantics | **PASS** — §8: §§0–9 byte-identical |
| **D** | must not revert to literal name absence | **PASS** — it does the opposite, stating *"Actor, role and worktree names DO occur in this file"* |
| **E** | no unlimited carve-out | **PASS with the carve-out tested at source** — see below |

🔴 **Property E is the one that could have hidden everything, so I tested the carve-out rather
than reading it.** §11.1 exempts *"an authority class governance has already allocated, cited here
and not created here"*, and pins it to `body §43` and `Annex G.3` for §8's `DETECTION` row. Both
pins were opened:

```
body §43   "RUNTIME / AUTHORITY INVENTORY — VIVO … Plan aggiorna a ogni rehydration/cambio;
            riga stantia = non autoritativa."          → Plan's reconciliation duty PRE-EXISTS
Annex G.3  "MIRROR_RETROSPECTIVE … condotta primariamente sull'EVENT LEDGER consolidato (J.1)"
                                                       → Mirror's ledger duty PRE-EXISTS
```

Both duties are allocated elsewhere and would bind identically if `cross_session_transport.md` did
not exist. The carve-out is bounded by three independently checkable conditions — authority class,
already allocated, cited-not-created — and it names its allocation instead of gesturing at one.
**It is load-bearing, not an escape hatch.**

**Mirror's suggested wording was correctly rejected, and Plan is right about why.** `M-1` proposed
*"Actor names appear only in citations and measurements."* Line 5 — the `status:` line — is
neither, and `REV-XPORT-MIRROR-001` §10 typed it `FRAMEWORK RULE` four lines above the suggestion.
**I confirm the finding against my own prior review.** Adopting my sentence would have planted a
third false self-description in the revision that exists to remove two. This is recorded as a
defect of `REV-XPORT-MIRROR-001`, not as a defect of the candidate.

---

## 6 · Occurrence inventory and classification reconciliation

**My own deletion sweep at `e839db3`**, run in Python — not BSD `sed`, whose `\b` failure is the
recorded L-3 defect — over every actor, role, worktree and benchmark name in the laboratory:

```
TOTAL CHANGED LINES: 9   →  5, 35, 286, 351, 370, 371, 372, 394, 454
```

| line | § | actual text (abridged) | name(s) | TYPE | NORMATIVE? | BRANCHES ON IDENTITY? | rationale |
|---|---|---|---|---|---|---|---|
| 5 | front | *"binding once Mirror hostile review passes"* | Mirror | **GOVERNANCE STATUS** | no — governance-plane standing, not a transport rule | **NO** | the standard PROPOSED formula; the rule that gives it force lives in the framework, not here |
| 35 | §0 | *"`roles/plan.md` already says…"* | roles/plan.md | **CITATION** | no | **NO** | prior art, establishing the rule is not new |
| 286 | §6 | *"the name `scientist-a` still resolving under `--all`"* | scientist-a | **MEASUREMENT** | no | **NO** | the observed example; the rule is *require a live pid*, stated over any name |
| 351 | §8 | *"visible to Plan at reconciliation and to Mirror on the ledger"* | Plan, Mirror | **CITATION** | no — a `DETECTION` row inside a `PROCEDURAL` block, descriptive of who would notice | **NO** | duty allocated by body §43 / Annex G.3; verified at source |
| 370 | §9 | *"`plan` has 8 live sessions"* | plan | **MEASUREMENT** | no | **NO** | evidence that §8 term 3 cannot be satisfied today |
| 371 | §9 | *"`mirror` has 7, `scientist-a` and `scientist-b` have 0"* | mirror, scientist-a, scientist-b | **MEASUREMENT** | no | **NO** | same measurement |
| 372 | §9 | *"recorded current session for `plan` is alive… not the current one"* | plan | **MEASUREMENT** | no | **NO** | same measurement |
| 394 | §9 | *"blocked on preconditions Plan may not satisfy alone"* | Plan | **CITATION** | no | **NO** | a statement about authority, not a protocol clause |
| 454 | §11.1 | the CITATION row of §11.1's own class table | roles/plan.md | **CITATION** | no | **NO** | points at the same prior art; see the observation below |

```
OCCURRENCE INVENTORY:          COMPLETE — 9 sites, all classified
CLASSIFICATION RECONCILIATION: PASS
```

**Reconciliation of the two taxonomies, explicitly mapped.** `REV-XPORT-MIRROR-001` §10 typed line
5 `FRAMEWORK RULE`; §11.1 types it `GOVERNANCE STATUS`. **Same referent, renamed class** — both
mean *the artifact's own standing under framework rules that bind every artifact*, and both agree
it is neither a citation nor a measurement, which is precisely the fact that falsified my
suggested wording. This is a rename, not a contradiction.

**Why 8 at revision 1 and 9 at revision 2 — the count that looked like a contradiction and is
not.** Revision 2 adds §11.1, whose CITATION row names `roles/plan.md`. `8 + 1 = 9`. Plan's
"eight lines" is about revision 1; Plan's "nine" is about revision 2. Both are correct about their
own tree, and I reproduced both.

🔴 **Observation N-4 — §11.1's locator column does not locate its own instance.** The `where`
column names eight of the nine sites; line 454, the row itself, is not among them. The operative
claim — *names occur in three classes* — remains **TRUE**, because line 454's occurrence is a
citation of prior art and falls inside `CITATION`. But a future reader who runs the deletion test
will find a ninth line the column does not point to. Non-blocking; recorded so it does not harden.

### 6A · The one genuine contradiction — finding N-1

`learning/plan/SLR-plan-0008.md` is **CONTENT**, hashed, and it says at line 23:

> *"the same file names **three actors and four roles** across eight lines."*

Measured against `f48a807`, this needs **two mutually inconsistent taxonomies to be true at
once**:

```
IF `plan`/`mirror` are ACTORS (as manifest §9.1's own matrix lists them —
   "STABLE ACTOR_ID: plan | mirror | scientist-a | scientist-b"):
       actors  = 4 distinct / 6 tokens        → "three" FALSE
       roles   = 2 distinct / 4 capitalized tokens → "four" true only as a token count
IF `plan`/`mirror` are ROLES:
       actors  = 2 distinct / 3 tokens        → "three" true only as a token count
       roles   = 8 tokens                     → "four" FALSE
```

There is no single taxonomy under which both sub-counts hold. **"eight lines" is exact and I
reproduced it; the actor/role split is not.**

A second instance in the same file, in the `EVIDENCE` block: *"cross_session_transport.md lines 16
and 424 **at f48a807**, against the **nine** name occurrences in the same file"* — at `f48a807`
there are **8** name-bearing lines and **11** name tokens. Nine is the revision-2 figure,
attributed to the revision-1 tree. The same document says "eight lines" at line 23 and "nine …
at f48a807" in `EVIDENCE`.

**This is NOT blocking, and the reason is the same distinction that made M-1 blocking.** M-1 sat in
the **normative** artifact, asserted **that artifact's own governing property**, and would have
canonicalized as the protocol's self-description. These are narrative recitals in a
**non-normative learning record**, describing a **superseded** revision's defect; no rule, gate or
test depends on them, and the correct figure is present in the same document and in the manifest's
own table. **The normative artifact carries no count at all** — `T-GENERIC-1`'s row states a
property, not a tally. That is the right place for the load to sit.

🔴 **And the phrase is partly mine.** The commit subject of `REV-XPORT-MIRROR-001` (`dbd44fee`) is
*"The protocol names **three actors** in the file that says it names none."* Plan inherited the
figure from my own review. I correct it here on both sides rather than charging it to the author
alone. **A correction by append is owed on `SLR-plan-0008`; it is not a condition of this ACCEPT.**

```
UNEXPLAINED COUNT/TAXONOMY CONTRADICTION: 1   (N-1, non-blocking, non-operative, inherited)
```

---

## 7 · T-GENERIC-1 — what it measures, and whether it says it

**Semantics reconstructed from the canonical row, not from the paraphrase.** The row in the
protocol's §10 states a **three-part conjunction**:

```
1  no normative sentence changes meaning
2  no clause branches on ACTOR_ID
3  every remaining occurrence falls in one of §11.1's three classes
```

Answering the six questions put to this review:

1. **"9 changed lines" means nine *lines of this file altered by the deletion transform*** — not
   diff lines, not classified sites. I reproduced exactly nine, independently, in Python.
2. **"none normative"** means none of those nine is a normative sentence *of this protocol* —
   i.e. none imposes a transport obligation on a sender or a recipient.
3. **Is it literally true under the protocol's own definition?** **YES.** The two candidates for
   normativity were tested rather than waved through. Line 5 is the artifact's governance
   standing, whose force comes from framework rules external to this file. Line 351 sits inside
   §8 but within an `ENFORCEMENT MODE: PROCEDURAL` block, in a `DETECTION` row that is descriptive
   of who would notice — and the duty it names is allocated by body §43 and Annex G.3, verified at
   source. Neither imposes a transport obligation, and §11.1 states the taxonomy that makes this
   checkable instead of arguable.
4. **Does it detect actor-conditioned behaviour, or only name presence?** Conjunct 2 detects
   behaviour; conjuncts 1 and 3 detect the description. Taken together the row is about
   behaviour. **The deletion half alone would not detect a variable-mediated branch** — and
   §11.1 says so itself, which is the part that impressed me most: *"a grep … would return **zero**
   on a protocol that branched on `ACTOR_ID` through a variable."* The row does not rest on the
   deletion test alone.
5. **Can it pass for the wrong reason?** The oracle, no. **The published command for the adjacent
   §§0–9 measurement, yes — see N-3 in §11.**
6. **Can it miss an indirect branch?** The deletion half can; conjunct 2 covers it, and I
   discharged conjunct 2 by reading §§0–9 clause by clause (§10 below), not by deleting strings.

```
T-GENERIC-1 SEMANTICS: RECONSTRUCTED — a deletion transform over every actor/role/worktree/
                       benchmark name, conjoined with an ACTOR_ID-branch check and a
                       class-exhaustiveness check
T-GENERIC-1 CLAIM:     TRUE
T-GENERIC-1 ORACLE:    SEMANTICALLY_LOAD_BEARING
```

🔴 **Two honest qualifications on the oracle, neither blocking.** (a) It is a **stated procedure,
not an executable** — `SLR-plan-0008`'s micro-upgrade 3 declares this as a deliberate trade and
carries it as a debt, which is the correct disposition; the consequence is that Plan's nine and my
nine agree because we independently built the same-shaped instrument, not because we ran the same
one. (b) The compressed paraphrase *"9 changed lines, none normative"* travels in the SLR and the
handoff without the taxonomy that makes "normative" precise. The canonical row is the precise one.
**The loose form should not travel alone** — the same caution `M-3` raised about "third version".

---

## 8 · Behavioural equivalence — reconstructed by domain, not by section numbering

I did not accept section numbering as a proxy for executable behaviour, and I did not use the
naive range. **The strongest available instrument is the hashed domain itself**, so the delta was
computed over the *included content sets* at each tip:

```
included(f48a807) = 531        included(e839db3) = 532
ADDED    learning/plan/SLR-plan-0008.md
MODIFIED framework/protocols/cross_session_transport.md
REMOVED  (none)
```

**Exactly two content paths. Both markdown. No executable code, no test file, no script.**

The naive `git diff f48a807 e839db3` does return seven paths, and I confirmed why: the five extras
are `governance/candidates/` ×2, `ledger/` ×2 and `reviews/plan/` ×1 — all under declared
CONTROL_PLANE_ROOTS at canonical v4, all belonging to intermediate control-plane commits. Plan's
warning is correct, and the domain route settles it without needing the warning.

**§§0–9 byte-identity — reproduced two ways:**

```
awk range, per Plan's §15.1 command (run under bash, and under zsh with braces):
  f48a807  91875ff763a6655caeafbf26026e15da0b9b72414ab3be7b43f6aa94b8cb98ad   372 lines
  e839db3  91875ff763a6655caeafbf26026e15da0b9b72414ab3be7b43f6aa94b8cb98ad   372 lines
independent Python segmentation on §0…§10 boundaries:
  R1 §0 at line 22, §10 at 394 → 372 lines      R2 §0 at 27, §10 at 399 → 372 lines
  SHA-256 of both segments IDENTICAL (d314b8aa…, differing from Plan's only by
  trailing-newline convention — the equality, which is the claim, holds)
```

The three edits all sit outside that range: the frontmatter `actor_scope`, one appended row in
§10's table, and §11 with its new §11.1.

```
EXECUTABLE TRANSPORT BEHAVIOR REV1→REV2:                          IDENTICAL
NORMATIVE TRANSPORT SEMANTICS EXCEPT GENERALITY DESCRIPTION:      IDENTICAL
```

---

## 9 · The manifest's historical false claim — correctly preserved

Manifest §9.1b still carries revision 1's two-class summary — *"every one of the eight occurrences
is a citation or a measurement"* — and §9.1b-R2, immediately below it, marks it:

> 🔴 *"One correction to the table above… the same table types line 5 as front-matter status,
> which is neither… Revision 2's protocol text therefore carries **three** classes, not two. The
> two-class summary is left standing here as the record of what was written, with its own table as
> the disproof."*

The correction is **adjacent, flagged, dated to the revision, and traceable**, and §9.1b-R2 also
concedes that the manifest was the wrong place for the repair at all. No reader can mistake the
two-class statement for current candidate truth: the correcting paragraph sits in the same section,
and the corrected property now lives in the protocol where it canonicalizes.

```
MANIFEST HISTORICAL FALSE CLAIM: PRESERVED_WITH_EXPLICIT_CORRECTION
```

---

## 10 · The true generality property — semantic falsifier, not string absence

String absence was **not** used as the oracle. Each normative clause was read and asked whether it
would change for a different actor:

| clause | actor-conditioned? |
|---|---|
| §1.1 authoritative-content list + the MUST-live-in-a-durable-artifact rule | **no** — enumerates content kinds, no actor |
| §1.2 control envelope | **no** — `ACTOR_ID` is a *variable field carrying sender identity*, never a value tested |
| §1.3 body contents · §1.4 depth rule | **no** |
| §2 message budget (structural, no number invented) | **no** |
| §3 version binding + `VERSION_CHANGED → REVALIDATION_REQUIRED` | **no** — per-session, over any session |
| §4 per-field size table (`to` enforced, `summary` not) | **no** — per field, not per actor |
| §5 outcome taxonomy + the four boundaries | **no** |
| §6 discovery ≠ liveness ≠ routability | **no** — `scientist-a` is the measured example, the rule is *require a live pid* |
| §7 recipient-side processing failure | **no** |
| §8 six-term handoff conjunction + ACK | **no** — stated over any sender/recipient; `DETECTION` names observers whose duty is external |
| §9 the five refusals | **no** |

Attacked specifically for: explicit actor-name branches; role names aliasing actor identity;
actor-specific exceptions, budgets, envelope requirements, ACK rules, delivery semantics; and A/B
benchmark special-casing. **`BENCH-AB-001`, `scientist-c`, `lettore`, `evidence-index` and
`orchestrator` appear zero times in the file.**

```
ACTOR-CONDITIONED TRANSPORT BRANCHES:  0
A/B-SPECIFIC TRANSPORT LOGIC:          NONE
```

**False-claim sweep across tracked CONTENT** at the candidate tip, for every universal-absence
formulation (*names no / does not name / no occurrence of / actor-free / names nobody*) and for
every `actor_scope` / `ACTOR-GENERIC` declaration, excluding the three control-plane roots:

```
FALSE OPERATIVE CLAIMS REMAINING: 0
```

The only surviving universal-absence statements about actor names are the two in
`governance/candidates/` — §9.1b and the handoff §5.2 — both **CONTROL_PLANE**, both **HISTORICAL**,
both **CORRECTED** in place. Unrelated hits elsewhere (`launch/KERNEL_SPEC.md:300`,
`controlled_benchmark_ab.md:636`, two skill descriptions) are about different subjects entirely and
are untouched canonical text.

---

## 11 · Scientist D falsifier — PASS

`scientist-d` was instantiated **conceptually only**. Nothing was created, registered, activated or
routed.

```
new Transport clause        NONE      §§0–9 enumerate no actor
new message-size rule       NONE      §4 is keyed by field, not by actor
new durable payload rule    NONE      §1.1 is keyed by content kind
new envelope semantic       NONE      ACTOR_ID is a carried value, never a tested one
new delivery class          NONE      §5's taxonomy is actor-free
new ACK semantic            NONE      §8 terms 4–6 are over any recipient
new summary semantic        NONE      §4: summary is non-authoritative for every sender
new runtime-scope rule      NONE      §3 is per-session and self-observed
```

D's delta is an `ACTOR_ID`, a role binding, a worktree row and a **derived** fingerprint
(`compose --role scientist` — role-keyed, and I re-verified all four fingerprints are role-keyed
and identical at both trees). All four are **routing/registration** concerns, not transport ones.

```
SCIENTIST-D TRANSPORT FALSIFIER: PASS
```

---

## 12 · Runtime model — PRESERVED, and not inherited across a mismatch

All seven properties live inside the byte-identical §§0–9 range, which is the strongest
preservation proof available: identical bytes, identical semantics. Spot-verified in the revision-2
text rather than assumed:

```
endpoint/interaction runtime scope    PRESERVED — §3, "an actor establishes its own runtime
                                      version from its own process image"; no global version
field-specific `to` vs `summary`      PRESERVED — §4 table: `to` 200 enforced via pattern;
                                      `summary` 200 declared, NOT enforced at 264
summary NON_AUTHORITATIVE             PRESERVED — §4, "summary is a UI preview. Nothing
                                      authoritative goes in it"
structural-only message budget        PRESERVED — §2, no number invented
durable payload authority             PRESERVED — §1.1 MUST/MUST NOT
delivery ≠ processing ≠ ACK           PRESERVED — §5 four boundaries, §7, §8 terms 4/5/6
version/revalidation semantics        PRESERVED — §3, VERSION_CHANGED → REVALIDATION_REQUIRED
```

No peer-dependent probe was re-run gratuitously. **No runtime version mismatch arose** (§0A), so
`REV-XPORT-MIRROR-001`'s 2.1.233 evidence stands on its own terms rather than being inherited
across a version gap.

---

## 13 · T-TRANSPORT-1 — honestly NOT_RUN

`T-TRANSPORT-1` remains `NOT RUN` at revision 2, with the reason unchanged and correct: executing
it requires electing one of several live sessions as the recipient, and Routing is unresolved, so
the election would measure luck rather than transport. **No recipient was elected by me, and none
was invented to turn the row green.** No routing-neutral execution mechanism existed independently,
and none was created.

```
T-TRANSPORT-1: NOT_RUN
```

---

## 14 · Wrong-reason discipline

| instrument defect | status |
|---|---|
| BSD `sed -E` with `\b`, substituting 3 of 9 occurrences and printing a clean two-line diff | **corrected before use.** Re-run in Python by Plan → nine; **I reproduced nine independently in Python.** The void result supports nothing |
| naive `git diff f48a807 e839db3` spanning seven paths | **corrected, and superseded.** I did not rely on either range; §8 computes the delta over the hashed domain |
| macOS has no `timeout` | **hit by me** while probing `claude agents --json`. That probe therefore **returned nothing and supports nothing** — it is recorded as NOT RUN, not as a negative result |
| `main^` as a void negative control (carried lesson) | **avoided.** §7's negative control uses `cbce3016`, verified genuinely different: different commit, different tree, 33 differing paths |

🔴 **N-3 — a NEW wrong-reason hazard I found in a published oracle.** Manifest §15.1 publishes the
byte-identity command as:

```bash
git show $TIP:framework/protocols/cross_session_transport.md | awk … | shasum -a 256
```

Unbraced `$TIP:framework` is correct in bash. **In zsh — the operator's shell — `:f` is parsed as a
parameter modifier**, `git show` fails, `awk` receives nothing, and `shasum` returns
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — the SHA-256 of the empty
string — **at both tips**. The two values agree, and the reviewer reads `IDENTICAL`.

I hit this on my first run. **The claim is TRUE** — verified with `${TIP}` and again under bash —
so no conclusion of Plan's rests on the defect. But the *published* command can pass for the wrong
reason in the default shell of this machine, which is the same class as the `sed` defect L-3
records, one layer out. **Fix: brace the expansion.** Non-blocking.

```
WRONG-REASON LOAD-BEARING PASSES: 0
```

---

## 15 · Regression accounting — DELTA 0, set-wise and name-wise

Run in two clean detached worktrees under the session scratchpad — `BASE_HEAD 4454feab` and
candidate content tip `e839db38`. Never in root, never in another actor's worktree. No `timeout`
wrapper.

```
                        BASE_HEAD 4454feab        REVISION 2 e839db38
suites RUN              65                        65          sets IDENTICAL
tests executed          953                       953
failing suites          6                         6
failing test names      7                         7

SET DIFFERENCE (suites) EMPTY both directions  →  DELTA 0
SET DIFFERENCE (tests)  EMPTY both directions  →  same reason, not merely same count
ADDED 0 · REMOVED 0
```

```
FAILING SUITES — identical set at both trees:
  framework/scripts/test_session_self_eval.py
  scripts/test_abstract_corpus_is_not_evidence.py
  scripts/test_fulltext_trace_contract.py
  scripts/test_locator_obligation_reaches_every_route.py
  scripts/test_release_runner_verdict.py
  scripts/test_release_surface.py

FAILING TESTS — identical set at both trees:
  SelfEvalGate.test_diagnosis_is_wired_before_growth_and_takeaways
  EveryTestSuiteIsActuallyRun.test_every_tracked_test_file_is_in_the_runner
  FulltextTraceContractTests.test_normative_layers_make_receipts_universal
  FulltextTraceContractTests.test_normative_write_rules_name_the_append_only_carveout
  ReleaseSurfaceTests.test_shebang_python_entrypoints_are_executable
  InstructionSurfacesCarryTheDistinction.test_the_bootstrap_bounds_the_corpus
  ObligationReachesEveryRoute.test_the_bootstrap_states_the_rule
```

**Other gates, re-run at the candidate tree — all reproduce:**

```
LINT               PASS — 1 pre-existing INFO (CLAIM 010 wikilink)             ✅
PUBLICATION GATE   PASS / BLOCKS: 0 — 4 [REVIEW] lines, all pre-existing        ✅
FINGERPRINTS       mirror 3dff8954… · plan 9c0c13fb… · scientist 82423a48… ·
                   orchestrator e2c54470… — IDENTICAL at BASE_HEAD and tip      ✅
```

Fingerprint identity confirms no role contract is touched, so no in-flight checkpoint is
invalidated. **REGRESSION DELTA: 0.**

---

## 16 · Binding — PASS, with two positive controls and a verified negative

Computed in a clean detached worktree at the candidate tip, under **canonical `legend-candidate-v4`
P5** with its three declared roots — never from the Mirror worktree, whose P5 is a stale v3 (§0).

```
REVISION 2 — the invariant is "included stays 532 and the digest stays 81f241f2… at every tip
at or after e839db38", not "the manifest tip is final":

  e839db3   included 532 · excluded 38   81f241f26ed668ee02e6b04d191c98a4deaa025355d9212bc999b80c6e056e1f ✅
  cedb4d5f  included 532                 81f241f2…6e1f  ✅
  86dfe29   included 532 · excluded 40   81f241f2…6e1f  ✅
```

```
POSITIVE CONTROL 1 — revision 1 reproduces
  --base 4454feab --tip f48a807  →  68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
  published superseded value      →  68173f01…c96a                                    ✅ EXACT

POSITIVE CONTROL 2 — SCIAB reproduces
  --base cbce3016 --tip 2a854177  →  beef6db08bdf8489b68078fc00c08fee913a585a4e1ee8359b592fc9e31a6061
  SCIAB manifest published value  →  beef6db0…6061                                    ✅ EXACT

NEGATIVE CONTROL — the alternate BASE_HEAD was VERIFIED different before use, not assumed
  4454feab vs cbce3016: different commit ✓ different tree ✓ 33 differing paths ✓
  --base cbce3016 --tip e839db3   →  bf3b9092…6b2c   ≠ 81f241f2…6e1f                  ✅ DISAGREES
  --base 4454feab --tip f48a807   →  68173f01…c96a   ≠ 81f241f2…6e1f                  ✅ DISAGREES
```

**Path sorting and byte layout verified independently**, by a re-implementation that imports
nothing from the script and reads the three roots by eye from canonical P5:

```
sort key    the path field of each ls-tree line, explicitly re-sorted
layout      "legend-candidate-v4\n" + BASE_HEAD + "\n" + every entry newline-terminated,
            the last one included → 57,420 bytes at e839db3
result      532 / 81f241f2…6e1f  — IDENTICAL to the script at all four tips tested
```

```
BINDING: PASS
```

---

## 17 · P5 runtime premise — confirmed, classified, NOT repaired

```
CANONICAL P5.1 @ main   "While `runtime/` remains untracked it is invisible to `git ls-tree` and
                         therefore absent from the domain, so no fixed point arises in the interim."
MEASURED                 runtime/orchestrator_lease.md IS TRACKED at main AND at e839db3
MEASURED IN THE DOMAIN   entry 495 of 532, between roles/scientist.md and
                         scripts/guard_bash_command.py — confirmed by three independent routes
                         (the script's own domain(), my re-implementation, and a plain
                         git ls-tree | grep -v | sort | grep -n pipeline)
NOT EXCLUDED             no runtime/ path appears in the excluded set
```

**The premise is false today. It does not make the binding indeterminate.** The rule *as
implemented* is unambiguous — everything not under a declared root is content — and the digest
reproduced identically under four instruments at three tips. The staleness is in P5's *rationale*,
not in its *operation*. XPORT neither introduces nor relies on the defect: `git diff 4454fea
e839db3 -- runtime/` is empty, so no lease was written on this branch.

```
P5 RUNTIME PREMISE: SEPARATE_GOVERNANCE_DEBT
```

**Not repaired here. P5 is canonical text at `BASE_HEAD` and is not Mirror's to edit.**

🔴 **N-2 — the manifest's index is off by one.** §15.2 states *"entry 496 of 532"*. Measured: **495
of 532**. Control-plane, non-load-bearing — the finding it supports (the lease is inside the hash)
is correct and independently confirmed. Recorded for accuracy, and because it is the third loose
count in this revision.

---

## 18 · Scope — NONE

Classified diff inspected over the hashed domain (§8): two content paths, both markdown. The
protocol edits are confined to the frontmatter, one appended row in §10's table, and §11 plus
§11.1.

```
routing              NOT introduced — §9 still declares the dependency unresolved
lifecycle            NOT introduced
CURRENT              NOT assigned
activation           NONE
registrar            NONE
supersession         NONE — of sessions; the candidate's own revision supersession is not that
routing generation   NONE
lease redesign       NONE
Scientist activation NONE
benchmark execution  NONE
```

**`T-GENERIC-1` was tested for scope creep and I judge it in scope.** It adds one row and one
subsection, both *about this document's own generality*; it imposes no obligation on any sender or
recipient. It is the minimum that makes the replacement property falsifiable inside the artifact
that carries it — and a property claim shipped without its falsifier is the shape of M-1.

```
SCOPE CREEP: NONE
ROUTING:     UNRESOLVED
```

---

## 19 · SLR-plan-0008 — BOUND, and curated under Annex E.2

```
BOUND         learning/plan/SLR-plan-0008.md, committed in e839db38 — the content tip itself
POPULATION    present in the 532-entry included domain (the +1 over revision 1's 531)
TIMING        committed before the binding was published; not appended afterwards
SESSION       written for this revision-2 session — task XPORT-ROUTING-001, directive v1,
              generation 1, referencing REV-XPORT-MIRROR-001
SELF-RATIFY   NONE — `curation: PENDING`, every CONFIRMATION_CLASS marked proposed
```

**E.2 curation — the classification is Mirror's, and I do not accept the author's proposals
automatically:**

| | proposed | curated | reasoning |
|---|---|---|---|
| **L-1** | ORIGINAL_OBSERVATION, wider scope | **CONFIRMED — ORIGINAL_OBSERVATION, wider scope** | *A property expressed as the absence of a string is refuted by the cheapest check it invites and passed by the failure it exists to exclude.* The asymmetry is demonstrated, not asserted: the grep is non-zero on a compliant file and would be zero on the actual failure. This is the generative half of M-1 and it generalizes beyond this laboratory |
| **L-2** | ORIGINAL_OBSERVATION, wider scope | **CONFIRMED — ORIGINAL_OBSERVATION, wider scope** | *A reviewer's suggested remedy is evidence, not a patch.* I verified this against my own review rather than accepting the author's account: `REV-XPORT-MIRROR-001` §10 types line 5 `FRAMEWORK RULE`, four lines above a suggestion asserting names appear *only* in citations and measurements. **The finding is correct and it is against me.** Plan's framing — that the three reasons to adopt it were all reasons to read it more carefully — is the transferable part |
| **L-3** | REPLICATION of SLR-mirror-0014, 4th instance | **CONFIRMED as REPLICATION, and the added mechanism is accepted** | The class is `shell as instrument`, and Plan is right not to re-claim it. What is genuinely new is the **detector**: a count obtained earlier for an unrelated purpose caught the void transform. **N-3 in §14 is now the fifth instance of the same class, found in this candidate's own published command** — which strengthens rather than weakens the entry |

**Proposed for `ACTIVE_LESSONS`:** L-1, on the ground that it is the shortest statement of the
defect this candidate exists to remove, and it is checkable — *inventory with a grep, decide with a
test that deletes*.

**Curation note against the record.** `SLR-plan-0008` is also where finding N-1 lives (§6A). I
record the count defect and the confirmed learnings in the same breath deliberately: the document
that correctly diagnoses *how counts are produced by instruments* is the document whose own counts
do not reconcile. That is not hypocrisy, it is the ordinary difficulty, and L-3's own conclusion —
compare a yield against a count obtained by another route — is the remedy it needed one paragraph
further out.

**No new false universal or generalization** was found in the SLR. Its three learnings are scoped,
hedged, and each names what it does not claim. The defect is a tally, not a generalization.

---

## 20 · Carried debts — carried, none repaired, none newly load-bearing

```
A · ROUTING / SESSION LIFECYCLE UNRESOLVED        CARRIED — and correctly still unresolved
B · ORCHESTRATOR WORKTREE CONTRADICTION           CARRIED — routing-relevant, untouched
C · ROOT ENVIRONMENTAL HISTORY                    CARRIED — no root run performed by me
D · MISSING HISTORICAL SNAPSHOT TAGS              CARRIED — historical control-plane debt
E · P5 RUNTIME PREMISE                            CARRIED — §17, SEPARATE_GOVERNANCE_DEBT
F · PHASE −1 E5 NARROWED TO INSTRUMENT-BOUND      CARRIED — and §0A is a fresh instance of the
                                                  same lesson, on a different instrument
G · HISTORICAL MULTI-SESSION INVENTORY            CARRIED — not closed, not cleaned, not counted
H · T-GENERIC-1 IS A PROCEDURE, NOT AN EXECUTABLE NEW, declared by the author (§7), accepted as
                                                  a debt for whichever candidate next touches the
                                                  protocols' test surface
```

**No historical session was closed.** Carried debts from `REV-XPORT-MIRROR-001` — `O-1`
(`T-TRANSPORT-6`/`-7` better typed `PASS_BY_DESIGN — NOT EXECUTED`), `O-2` (`KERNEL_SPEC` cited
without a version pin) and `O-3` (the `to` bracket is not a boundary) — were accepted by Plan with
stated reasons and deliberately not acted on. **I agree with the disposition:** each is a change to
text the review confirmed sound, and bundling them into a blocking-finding repair would have
widened the object. They remain open and correctly attributed.

---

## 21 · Annex C.2 — the single format

**REVIEW_ID** `REV-XPORT-MIRROR-002` · **OBJECT** `CAND-20260819-XPORT` rev 2,
`CANDIDATE_CONTENT_HASH 81f241f2…6e1f` @ `BASE_HEAD 4454feab` · **LEVEL** R4 ·
**REVIEWER** `mirror` · **AUTHOR** `plan` · **ADJUDICATOR** operator (MAJOR)

### STEELMAN — mandatory, and before the objections

**Plan was handed a suggested sentence by its reviewer, and refused it on the ground that the
reviewer's own table disproved it.** That is the single most valuable thing in this revision, and
it is worth more than the repair itself. The path of least resistance was to paste my wording —
short, explicitly framed as the author's own, offered by a reviewer who had just been right about
everything else. Taking it would have shipped a third false self-description inside the revision
whose entire purpose was to remove two, and it would have been *my* defect wearing Plan's name.
Plan read the suggestion against the artifact instead of against my authority, found the
counterexample four lines above the suggestion in my own §10 table, and said so plainly.

**The repair itself is correctly located.** M-1 was not "a false sentence" — it was a false
sentence *on the wrong side of the content/control-plane seam*. Revision 2 moves the property, the
class taxonomy and the falsifier into the artifact that canonicalizes, and leaves the manifest's
old wording standing as marked testimony. The candidate's own §7 indicts five artifacts for
carrying premises that quietly stopped being true; revision 2 declines to become the sixth, at the
cost of a new content tip and a re-derived hash, which is what a revision is for.

**And the replacement is stronger than the sentence it replaces.** It is true, it survives the grep
that falsified the original, it states why the grep is the wrong instrument, and it ships a
declared falsifier with a stated failing form. `T-GENERIC-1` can fail — which distinguishes it from
the four rows `O-1` correctly flagged as passing by construction.

### EVIDENCE_FOR

Two false assertions reproduced at `f48a807` and verified absent at `e839db3`. Replacement property
independently verified true across all 9 name sites and all 11 normative clauses. §§0–9
byte-identical, 372 lines, `91875ff7…`, reproduced two ways. Content delta computed over the hashed
domain: two markdown paths, no code. Binding reproduces at three tips under four instruments, with
two exact positive controls and a verified negative. Regression delta 0, set-wise and name-wise.
Carve-out pins opened at source in body §43 and Annex G.3. LINT, publication gate and all four
fingerprints reproduce.

### EVIDENCE_AGAINST

Four loose counts (§6A N-1, §17 N-2, §14 N-3, §6 N-4), one of which requires two inconsistent
taxonomies and one of which is off by one. The falsifier is a stated procedure, not a committed
executable, so its reproduction depends on each reader rebuilding the instrument. The compressed
paraphrase "none normative" travels without the taxonomy that makes it precise.

### ALTERNATIVES_CONSIDERED

**(a) REQUEST CHANGES on N-1.** Genuinely considered, and rejected on the distinction that made
M-1 blocking in the first place: M-1 was a *normative self-description in the canonicalizing
artifact*, asserting that artifact's own governing property. N-1 is a narrative recital in a
non-normative learning record about a superseded revision, on which nothing gates, with the correct
figure present in the same document. Blocking it would also charge Plan for a phrase my own
review's commit subject originated. **(b) ACCEPT silently.** Rejected: four loose counts in one
revision is a pattern, and an unrecorded pattern gets quoted forward. **(c) Demand the falsifier be
committed as a script.** Rejected: that is exactly the object-widening Plan correctly refused for
`O-1`, and the author declared it as a debt rather than hiding it.

### KEY_OBJECTIONS

`N-1` (count/taxonomy contradiction in CONTENT, non-operative, partly inherited from me) ·
`N-2` (off-by-one domain index, control plane) · `N-3` (zsh-fragile published oracle that can pass
for the wrong reason) · `N-4` (§11.1's locator column omits its own instance). All non-blocking.

### VERDICT

**ACCEPT.** M-1 is reproduced, both false operative assertions are removed from CONTENT, the
replacement property is literally true and falsifiable, no equivalent absence claim survives
anywhere in tracked content, occurrence classifications reconcile completely across both
taxonomies, `T-GENERIC-1` says exactly what its oracle proves, semantic actor-generality is intact,
Scientist D needs no new transport logic, executable transport behaviour is unchanged, the runtime
model is preserved, `T-TRANSPORT-1` remains honestly `NOT_RUN`, wrong-reason load-bearing passes are
zero, regression delta is zero, the SLR is bound and curated, P5 is not silently repaired, Routing
remains unresolved, and the binding reproduces under two positive controls and a verified negative.

`CONFIRMED` here carries its Annex C.2 meaning: **no defect found given the available evidence
bundle** — never "true".

### REVIEWER_CONFIDENCE

**High** on the binding, the regression delta and the byte-identity — all reproduced under
independent instruments with controls. **High** on the truth of the replacement property: the
carve-out was tested by opening its two pins at source rather than by reading the claim. **High**
on N-1: the token census is mechanical and I ran it three ways. **Medium** on the completeness of
the false-claim sweep — it is a semantic search over natural language, and a formulation I did not
imagine could have escaped it.

### RESIDUAL_UNCERTAINTY

The deletion test is not executable, so Plan's nine and my nine agree because two independently
built instruments of the same shape agreed — not because one instrument ran twice. That is weaker
evidence than a committed script would give, and it is exactly the debt the author declared.

### EVIDENCE_NEEDED

For the debt in §20.H: a committed, self-checking deletion-test script that aborts when a pattern
matches zero occurrences. For N-3: a braced expansion in the published command.

### WHAT_WOULD_CHANGE_MY_MIND — declared falsifier

**This ACCEPT dissolves if any one of these is shown:**

1. **A tenth name occurrence exists in `cross_session_transport.md` @ `e839db3`** that my sweep
   missed and that falls into none of §11.1's three classes. My pattern covered the roster
   `plan · mirror · orchestrator · scientist · scientist-a…d · lettore · evidence-index ·
   BENCH-AB-001` plus capitalized role forms and role-contract paths. A name outside that roster
   would defeat it.
2. **A normative transport clause is shown to change meaning under the deletion test** — meaning a
   clause that imposes an obligation on a sender or recipient, not a governance-status line and not
   a `DETECTION` row whose duty is allocated in body §43 / Annex G.3. Then `T-GENERIC-1`'s first
   conjunct is false and this becomes M-1 repeated at a smaller size.
3. **The `DETECTION` carve-out is shown to create local transport behaviour** rather than cite
   allocated duty — i.e. body §43 or Annex G.3 do *not* impose the duties I read there, or §8's row
   adds an obligation they do not carry.
4. **N-1 is shown to be operative** — some rule, gate or test that consumes `SLR-plan-0008`'s
   actor/role counts. Then a false count acquires force and the finding becomes blocking.
5. **The binding fails to reproduce under canonical v4 P5** at any tip at or after `e839db38`, or
   `included` moves off 532.

### AUTHOR_RESPONSE

`reviews/plan/AUTHOR-RESPONSE-XPORT-MIRROR-001.md` exists at the candidate tip and is bound.
Annex C.2 makes a response to *this* review mandatory; silence is not acceptance. The four
non-blocking findings each ask for a correction by append, not a new revision.

---

## 22 · Status statements required of this review

```
ROUTING / SESSION LIFECYCLE IS NOT SOLVED BY XPORT.
```

Revision 2 does not touch it, and this review creates no routing policy, elects no recipient,
assigns no CURRENT and registers nothing.

```
CANONICAL ROUTING CLAIM: NONE
```

The operator's manual selection of this session established a **review execution endpoint only**.
It established no CURRENT routing, no activation, no registrar authority, no routing generation and
no supersession, and nothing in this review may be read as any of them.

```
HISTORICAL SESSION CLEANUP: NOT_PERFORMED
```

No session was closed, killed, renamed, superseded, activated or cleaned.

```
HUMAN_APPROVAL   NONE — not granted, not requested, not implied by this review
CANONICALIZED    NO — this review canonicalizes nothing
MAIN             4454feab72b7a0edf65f191be62aeedd899a15ad — UNCHANGED
BENCH-AB-001     NOT STARTED
SCIENTIST A      NOT ACTIVATED
SCIENTIST B      NOT ACTIVATED
SCIENTIST D      NOT CREATED — instantiated conceptually only, in §11
```

This review is written to `reviews/mirror/`, which is a declared `CONTROL_PLANE_ROOT` under
canonical `legend-candidate-v4` P5, and lands on branch `mirror`, which is not an ancestor of the
candidate tip. **It contributes nothing to the candidate's content domain and moves no hash** —
which is the property P5 v4 added `reviews/` precisely to guarantee.
