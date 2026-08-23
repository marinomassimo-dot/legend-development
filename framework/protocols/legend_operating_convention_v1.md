---
artifact: LEGEND Operating Convention v1 — the session layer
record_type: OPERATIONAL_CONVENTION
record_id: OPCON-V1
task_id: OPCON_V1_PLAN_001
dispatch_id: OPCON-V1-PLAN-001
author: plan
session_ref: evidence-index-58 [432290]
authored_on: 2026-08-23
dispatcher: operator (Transition Execution Mandate) · routed by legend-public-54 [9fa760]
governance_version: 3.1.1 — read from `main`, cited, NOT exercised and NOT modified

status: DRAFTED
binding: NO — an operational convention binds by adoption, never by governance
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

one_file_one_writer: >
  This is the whole convention. Section A was drafted by the orchestrator seat and handed over as
  INPUT — `learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md`, branch
  `legend-operating-convention-v1` @ cebca20, 403 lines — and integrated here by the Plan seat,
  which holds structural integration under H.1. Its author's competing path
  `operations/LEGEND-OPERATING-CONVENTION-v1.md` was withdrawn by its author; the Plan seat's two
  drafts under `operations/` are superseded by this file and removed by their own author. One
  convention, one path, one writer. Where Section A's text was corrected during integration, the
  correction is marked 🟠 INTEGRATION CORRECTION and says what it corrects and on what evidence.

domain: >
  CONTENT. `framework/` lies outside every declared CONTROL_PLANE_ROOT (P5.1 —
  `governance/candidates/`, `ledger/`, `reviews/`), so this file is inside CANDIDATE_CONTENT_HASH
  and moves it. Disclosed. MEASURED separately: it rotates NO role's fingerprint — every input of
  every role's pertinence set lies under `governance/` or `roles/`
  (`governance_fingerprint.py inputs --role <r>`, all four roles, zero paths outside those trees).

reads_normative_text_from: >
  `main` @ 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5, via `git show main:<path>` (A.5.5).
  One declared exception: `governance/plan_defined_parameters.md` was read from this working tree,
  because `git diff --stat main..HEAD` over the 13 fingerprint pertinence inputs — that file among
  them — is EMPTY. This tree's copy IS main's, measured, not assumed.
---

# LEGEND OPERATING CONVENTION v1

> **This is a working layer. It is not governance.** Where this document and a frozen normative
> file disagree, the frozen file wins and this document is the defect. Nothing here activates a
> role contract, confers an ACTOR_ID, grants authority, or reinterprets a frozen rule. Anything
> that would require a frozen rule to change is marked 🟡 **PROPOSAL — NOT IMPLEMENTED**.

---

## 0 · THE THREE LAYERS

| Layer | What lives there | Who may change it | Changed by this document |
|---|---|---|---|
| **FROZEN NORMATIVE** | `governance/` — body (`status: FROZEN`), annexes A–J, `plan_defined_parameters.md`, `roles/` | operator, through the governed path | **nothing, not one byte** |
| **OPERATIONAL CONVENTION** | this file | Plan drafts · Mirror reviews · operator ratifies | this *is* that layer |
| **IMPLEMENTATION MECHANISM** | `framework/scripts/`, `governance/scripts/`, `scripts/` | any actor, own branch, reviewable | only by proposal, Appendix D |

**The failure this separation prevents** is one the repository has already recorded: operating law
accumulating inside a router until nobody could tell which sentence bound them. `CLAUDE.md` became
a router on 2026-08-16 for exactly that reason. A convention that grows into governance repeats it.

### 0.1 · The test that keeps this layer honest

> **If a rule here were deleted tomorrow, would anything become permitted that governance forbids?**
> If yes, it is governance wearing a convention's clothes and does not belong here.
> If no, it is a convention: it makes correct behaviour cheaper, and its absence makes it harder.

### 0.2 · 🟠 INTEGRATION CORRECTION — the foundation claim, corrected before it was built on

The Plan seat's build claim asserted: *"Governance regulates ACTORS; this convention regulates
SESSIONS — an object the governance never named."* **The second clause is false, and the correction
makes the layer stronger rather than weaker.**

> **Measured at `main` @ 788c357.** Body line 184: *"ogni attore ha un **ACTOR_ID persistente**
> distinto dal **SESSION_REF effimero**."* Body § 43 lists among the runtime inventory's minimum
> columns: `… | SESSION_REF | Session ID | Agent ref | `**`Working dir`**` | Worktree | Branch |
> HEAD | …`. And `runtime/runtime_inventory.md` exists — 551 lines, on `refs/heads/orchestrator`,
> with a `Working dir:` line per actor.

**Governance named the session layer, specified the exact fields, and never mechanized them.** § 43's
own sentence — *"Plan aggiorna a ogni rehydration/cambio; riga stantia = non autoritativa"* — means
every row decays into non-authority by design, because nothing runs between turns.

So this convention **adds no layer. It fills one that has been specified, and empty, since
2026-08-17.** That is also the answer to *"does session ≠ actor smuggle authority in through the
back door?"* — it cannot, if the fields are governance's own.

**The falsifier, stated so a reviewer can aim at it:** if any clause below regulates an ACTOR rather
than a SESSION — allocates authority, binds a role, gates a governed act — it is governance in
disguise and must be struck or demoted to PROPOSAL. § B.10 lists every clause judged near that line.

---

# SECTION A — ACTORS, SESSIONS, DISPATCH, PRESERVATION

> Drafted by the orchestrator seat from evidence produced on 2026-08-23, in a session where seven
> sessions were polled, five of its own assertions were falsified by peers and two by
> re-measurement. **Every rule exists because something failed that day**, and the cause is named
> next to the rule so a later reader can attack the rule by attacking its cause.

## A.1 · A session has three identifiers, and they prove different things

| Identifier | Example | What it proves | What it does NOT prove |
|---|---|---|---|
| **routing name** | `mirror-75` | where a message will be delivered | anything about role, seat or authorship |
| **`[ref]`** | `[f3044e]` | disambiguates two rows sharing a name | same |
| **session id** | `2a6ffe75-…` | uniqueness; keys the transcript | same |
| **transport** | `uds:/tmp/cc-socks/27337.sock` | the wire a message arrived on | same |
| **`pwd`** | `.claude/worktrees/mirror` | **which working directory is occupied** | that this session is its sole occupant |

**A.1.1 — A session name is not evidence of actorhood.** Four `mirror-*` and three
`evidence-index-*` sessions were live on 2026-08-23; none held an ACTOR_ID; all seven declined to
infer one from their own name. *Cause: the registered refs `mirror-9c [3940a9]` and
`evidence-index-59 [de42c4]` were both dead while seven live sessions carried lookalike names.*

**A.1.2 — A session cannot resolve its own actorhood and must not try.** A session choosing the
reading that makes itself an actor is the failure the gate exists to prevent. **"None" is a correct
and useful answer.**

**A.1.3 — A dispatcher verifies its addressee before dispatching.** Delivery plus the addressee's
own peer list: a session's row is the one its own `ListAgents` omits, so the dispatcher derives it
by set complement rather than accepting a self-report. *Some harness builds print the session's own
name in the header line, so the complement is corroboration rather than necessity — but the
direction is what matters: it lets the DISPATCHER verify the ADDRESSEE without taking its word.*

**A.1.4 — 🔴 `started` is not evidence about a conversation.** It is a property of the runtime
incarnation.

> **Measured.** A transcript with `birth = 2026-08-22T20:00:50Z` was still being appended on
> 2026-08-23 — observed growing `1 603 926 → 1 612 311 B` — while its peer row read *"started 6h
> ago"*. A span of **19h56m** against a field reading 6h. Verified from two seats independently.

**Elimination by start time is therefore invalid.** *Cause: one such elimination was made and
withdrawn by its own author, in the dangerous direction — the one that clears a session.*

## A.2 · One writer per working directory — and how to establish it

`ONE_WRITER_PER_WORKING_DIRECTORY` (body § 14) is also a GATE 0 precondition (D.3, body § 12). It is
about a **path**, not a name.

**A.2.1 — The field is already mandated; the gap is mechanization.** See § 0.2. Governance specified
`Working dir` in § 43's minimum columns and an artifact carrying it was already materialized —
on 1 ref of 52, dated 2026-08-17. **"Adapt to LEGEND, not redesign LEGEND" in one rule:** the
convention adds no field, it fills one.

**A.2.2 — Seat occupancy is established by `(pwd, session id)`, nothing weaker.** Names, refs and
transports identify rows; only the pair identifies an occupant.

**A.2.3 — Occupancy is measured by polling, not inferred.** On 2026-08-23 this converted a suspicion
into a measurement in under ten minutes: 3 sessions in `.claude/worktrees/evidence-index`, 4 in
`.claude/worktrees/mirror`.

**A.2.4 — Co-location is a hazard even with zero conflicting writes.** Of twelve untracked files
across two seats, three were claimed and nine were claimed by nobody polled — yet **no session had
overwritten another's work.** The exposure is not what happened; it is that one `git clean` from any
co-occupant destroys everything. Report co-location as structural; **never round it up to a
lost-attribution event that did not occur.**

**A.2.5 — One writer per FILE is the achievable form while sessions are co-located.** A file has
exactly one authoring session for its lifetime in the working tree. Co-location is PERMITTED and
must be DECLARED. This does not replace body § 14; it is what a session can guarantee unilaterally
while § 14's precondition is unmet.

## A.3 · Attribution — what counts as evidence of authorship

| Rank | Evidence | Strength |
|---|---|---|
| 1 | the author claims the file, bounded by an artefact independent of the claim | **sufficient** |
| 2 | explicit claim + explicit disclaimers from every other polled occupant + an agreed digest | **sufficient to act on** |
| 3 | mtime inside a known session window | **candidate set, never an author** |
| 4 | elimination by `started` | **invalid — A.1.4** |

**A.3.1 — A matching digest corroborates the OBJECT, never the AUTHOR.** It would be identical if
the claimant were lying. *Cause: a seat recorded "hash-corroborated authorship" and the claimant
itself refused the phrasing.*

**A.3.2 — "Unclaimed" is a statement about who has spoken; "unknown-authored" is an inference.**
Prefer the first.

**A.3.3 — Preservation does not depend on attribution.** The protection is cheap and the attribution
expensive; do not gate the first on the second.

**A.3.4 — Every artifact declares its author and its session.**

```yaml
author:       plan                          # the SEAT
session_ref:  evidence-index-58 [432290]    # the SESSION — name + [ref]
```

🔴 **`session_ref` is an attribution AID, not proof — and the convention must say so**, because
self-declared identity is exactly what A.1 rules out. A session writing someone else's
`session_ref` is not caught by the field.

| state | meaning | worth |
|---|---|---|
| present, consistent with a live peer list | attribution corroborated | strong |
| present, contradicted by a live peer list | **finding** — escalate, never overwrite | decisive, negatively |
| **absent** | **UNATTRIBUTED** | must be claimed before anyone commits it |

**What it buys is not proof; it is the elimination of the question.** One unattributed file cost
four cross-session messages and produced a retracted "third writer" finding. A declared
`session_ref` would have cost one line. That argument does not require the field to hold against a
hostile writer — only against ambiguity. **Measured: 0 of 764 tracked paths carry one today.**

## A.4 · 🔴 Timestamps — the filesystem lies, and it lies when you are being careful

**A.4.1 — `stat -f '%Sm'` emits LOCAL time regardless of the format string wrapped around it.**
Three seats hardcoded a literal `Z` onto a CEST timestamp on 2026-08-23, independently, within one
hour. **A trap in the tool, not carelessness in a seat.**

> **Rule: derive every timestamp from the raw epoch — `date -u -r <epoch>`. Never `stat -f '%Sm'`.**
> Verified rather than assumed: on one file, naive `17:20:37Z` against true `15:20:37Z`.

**A.4.2 — Two ordinary operations forge timestamps, and both are what a careful person reaches for.**

| Operation | What it forges | Why someone runs it |
|---|---|---|
| `cp -p` | the source's mtime **and birthtime** | preserving files honestly, before they are lost |
| `git archive \| tar` | every entry stamped with the **commit's** time | verifying a fingerprint honestly |

> Files extracted at `2026-08-23T16:01:46Z` carried `mtime = 2026-08-22T16:01:01Z` — identical to
> `git show -s --format=%ct main`. Twenty-four hours in the past, one command, no flag involved.

**Any mechanism attributing work by mtime reads a field that two routine operations rewrite.**
Timestamp-bracketing of authorship was proposed on 2026-08-23 and **withdrawn** for this reason.

## A.5 · Dispatch conventions

**A.5.1 — A dispatch declares its authority basis and what it does not confer.** What authority it
traces to (body or a named annex — never a role contract standing alone, per `DEC-20260822`), and
explicitly that it confers no ACTOR_ID, activates no contract, creates no authority relationship.

**A.5.2 — A dispatcher declares its own state so the receiver can discount it.** Lease, checkout,
branch, HEAD. A receiver that cannot discount its dispatcher cannot refuse a bad dispatch.

**A.5.3 — Seat designation is a work assignment, not a registration.** One writing seat per role for
one mandate, rationale in measured terms, others stood down from writing, revocable in one line. It
never confers an ACTOR_ID, which is not the dispatcher's to give.

**A.5.4 — A dispatch carries the facts already established, each with the command that produced
them**, so the receiver can re-run rather than trust.

**A.5.5 — Read normative text from the sovereign ref, never from the working tree.**
`git show main:<path>`. *Cause: one seat's tree carried `plan_defined_parameters.md` at
`legend-candidate-v3` where `main` carried v4; another carried a contract revision with zero
approval records across all 52 refs.*

**A.5.6 — Corrections travel upward to the source, not sideways into a footnote.** A correction that
arrives after the decision is not a correction.

**A.5.7 — A dispatch names only objects that resolve, and only governed vocabulary.**
*Cause, twice: a dispatch specified "the existing canonical HANDOFF v2.1 format" — 0 hits over 52
content refs, control `AUTHOR_RESPONSE` at 268; and `NEXT_OWNER` / `NEXT_TRANSITION` / `HUMAN_GATE`
— 12 hits, all dispatch-supplied frontmatter, no repository source. The repository's real objects
are `HUMAN_REQUIRED` (body § 4), `HUMAN_APPROVAL` / `HUMAN_APPROVAL_QUEUE` (J.3) and `GATE 0–5`
(body § 12). A term outside that set is marked **local and non-binding** or is not used.*

**A.5.8 — A redelivery is not a new generation.** Same `DISPATCH_ID`, same date, no
`DIRECTIVE_VERSION` and no `GENERATION` increment → verify the durable evidence, do **not** repeat
completed work (A.3, A.7, body § 36.3). Cited, not restated.

## A.6 · Preservation rules

**A.6.1 — `WORK_COMMIT` of one's own named paths on one's own branch is the author's own authority**
under H.1 (*"WORK_COMMIT | ogni attore, solo proprio branch, granularità milestone"*). **No
coordinator relay may forbid it.** *Cause: a blanket "do not commit" was issued and two seats
correctly objected that foreclosing a safe route by relay, rather than by the authority that holds
it, is itself a decision — and not the relay's.*

**A.6.2 — Nobody commits, edits, repairs, relocates or deletes another session's artifact.** Report
it. `git add -A` / `git add .` is the mechanism of the failure; a named path is the remedy.
*Held twice on 2026-08-23: an untracked file carrying three `DIRECT_IDENTIFIER` hits was left
unrepaired because it was not the finder's.*

**A.6.3 — Held as HAZARD, not authority, in any shared working directory:**
`checkout · switch · reset · clean · stash · stash pop · add -A / add . · branch change ·
worktree remove/prune`. A prune sweep is destruction wearing a maintenance hat.

**A.6.4 — 🔴 The git stash stack is REPOSITORY-GLOBAL across every worktree.** A bare `git stash pop`
from any session pops another session's entry into the wrong tree. Reclaim with
`git stash apply <sha>` against a captured sha — never `pop`, and never from a seat that did not
create the entry.

**A.6.5 — An out-of-repository copy is declared or it does not exist.** A declared copy is: not a
commit, not durable, session-scoped, deletable, no transfer of the `WORK_COMMIT` act, and **never
counted as work preserved** — the originals remain the only record.

**A.6.6 — Redaction and commit are one act.** A file carrying a `public_release_gate.py`
`DIRECT_IDENTIFIER` block is redacted **in the same act** that commits it; a GATE 2 block is not
something a later commit clears retroactively. *Cause: two untracked records on two seats carry six
blocking lines between them, both inside the body of work that preservation would commit.*

**A.6.7 — 🟠 INTEGRATION CORRECTION — which part of A.6.3 is mechanized, and which is not.**
The PreToolUse guard already denies blanket staging and inline-heredoc repository writes. The Plan
seat proposed extending it with three more denials — bare `stash`/`pop`/`drop`, `reset --hard`, and
blanket `clean -f` / `checkout -- .` / `restore .` — and deliberately **excluded branch switching**,
because `git checkout <branch>` and `git checkout -- <path>` are indistinguishable by command string
and the guard's own test file states the reason: *"a guard that blocks ordinary work gets disabled
and then guards nothing."* **The guard extension is Appendix D work and is NOT built by this
document.** A.6.3 therefore stands as convention for the whole list, and mechanization covers the
part a machine can judge without misfiring.

## A.7 · Measurement conventions

**A.7.1 — Sweep the declared population, not the convenient one.** This repository's content
population is **52 refs** (43 heads + 4 remotes + 5 tags). `refs/heads` alone is 43. *Cause: a prior
record had to repair five heads-scoped counts inside a document declaring 52; the same error
recurred on 2026-08-23 and was caught by a peer before reaching the operator.*

**A.7.2 — Every sweep carries a positive control, and the control must be able to fail.**

**A.7.3 — 🔴 A control that shares the flaw of the search cannot detect it.** It proves the
instrument works; it cannot prove the instrument is aimed correctly. *Cause: a seat searched the
wrong root, ran its control inside that same wrong root, watched it pass, and reported a false
negative. Contributed by the seat that made the error.*

**A.7.4 — State the scope with the number.** "24" and "27" were both correct for one object on
2026-08-23, differing only by scope. A number without its denominator invites a contradiction that
does not exist.

**A.7.5 — A measured value is a photograph and it decays** (body § 43). Every reported value names
the command that reproduces it.

**A.7.6 — `VERDICT_TRANSFER: NONE` is the default.** A verdict carried from another record is not a
verdict. Where a record reproduces a prior measurement, it states the command and its own result.

## A.8 · `runtime/` — the fixed point this convention refuses to create already exists

> **Measured, `main` @ 788c357.** `runtime/orchestrator_lease.md` is the only tracked path under
> `runtime/`. It appears in none of the 45 control-plane exclusions, so it sits **inside the content
> domain** — the domain that defines candidate identity. Its blob has changed **9 times** across all
> refs. It is a *mutable control-plane record* (Annex I.3: `ACTIVATED_AT`, `LAST_RENEWED`,
> `EXPIRES_AT`, `RELEASED_AT`) living inside the hashed tree.

**What this convention does about it: nothing, deliberately, and it says so.** `runtime/` is a
registered OPEN CLASSIFICATION QUESTION routed to C-9 § 7.2, whose `hold` forbids resolving it, and
P5.1 states that declaring a fourth root *"would treat a container as a class"*.

> **Rule.** Where this convention states a principle the repository does not yet satisfy, it names
> the violation, names its owner, and claims no completeness it has not earned. Silence would be the
> convention asserting coverage it does not have.

Owner: C-9 § 7.2. Status: OPEN, held. Not this layer's to close.

## A.9 · The fingerprint recalibration — a FROZEN annex already ordered it

The whole-file hashing defect — a change to any delegated parameter moves **every** role's
fingerprint, because `plan_defined_parameters.md` is hashed whole in CORE while § P2.2 splits Annex
J into four sections precisely to avoid that — was found by a mirror seat and verified at `main`.

**Annex A.6 — FROZEN — anticipated this exact defect, named it, assigned detection and prescribed
the remedy.** Verbatim:

```
FAILURE:    (b) composizione del fingerprint mal calibrata: troppo larga → invalidazioni inutili,
                troppo stretta → ripresa sotto regole cambiate
DETECTION:  (b) Mirror monitora il tasso di invalidazioni e i casi di ripresa poi contestati
RECOVERY:   (b) Plan ricalibra la composizione del fingerprint (modifica governata)
GUARANTEE:  … nessuna invalidazione inutile per modifiche non pertinenti
```

Every clause fired as written: the composition **is** too broad; **Mirror detected it, unprompted**;
the recovery is **Plan's**.

**Sequencing, and it inverts an order:** recalibrate the composition *before* any correction to
`plan_defined_parameters.md`. Recalibrated first, such a correction is non-pertinent for every role
and the invalidation of the 19 checkpoints on `main` carrying `APPLICABLE_GOVERNANCE_FINGERPRINT`
never happens. Recalibrated after, it is paid for nothing.

### A.9.1 · 🟠 INTEGRATION CORRECTION — "no new governance" is true; "no operator decision" is not

Section A's source concluded that the recalibration *"needs no new governance"*. **That is correct
and it is not the whole gate.**

> **Measured at `main`, frontmatter of `governance/plan_defined_parameters.md` line 11:**
> `change_class: MAJOR — these values are governance; changing them follows gate 3`

GATE 3 is *"Plan candidate → Mirror hostile review → MIRROR PASS → HUMAN_APPROVAL (oggetto in coda,
J.3) → commit"*. A.6's `modifica governata` **is** that path, not an exemption from it.

```
Plan MAY     prepare the recalibration as a CAND, with the composition change and its rationale
Plan MAY NOT perform it. GATE 3 ends in HUMAN_APPROVAL, and J.3/E4 adds: APPROVAL ≠ AUTHORIZATION.
```

**This correction is load-bearing:** a session reading § A.9 alone could recalibrate unilaterally
under a frozen annex's name, which is precisely the accidental authority escalation this convention
exists to prevent. The sequencing conclusion is unaffected — prepare it first, still.

→ **PROPOSAL P-6, § B.10.**

**This is the pattern the whole convention follows.** The strongest moves available are not new
rules. They are frozen provisions written, never mechanized, and now owed: § 43's `Working dir`
column (A.2.1) and A.6(b)'s recalibration here.

---

# SECTION B — ARTIFACTS, LIFECYCLE, OWNERSHIP, HANDOFF, REVIEW, ESCALATION, MIGRATION

## B.1 · Artifact classes and their taxonomy

### B.1.1 · The rule, in three clauses

```
1. PATH defines CLASS.
2. CLASS declares DOMAIN — CONTENT or CONTROL_PLANE — explicitly, in the artifact.
   Path alone is demonstrably insufficient: B.1.3.
3. STATUS defines lifecycle validity, and PRESENCE OF AN ARTIFACT DOES NOT IMPLY AUTHORITY.
```

Clause 2 is not a hierarchy level and not a new root. It is a **declaration the artifact carries**,
so a reader — and a validator — sees the domain without re-deriving P5.1 by hand.

### B.1.2 · The classes that exist

Seven, all already in the repository. None invented; the convention names them.

| # | CLASS | WHAT IT IS | CANONICAL PATH | ID | DOMAIN | WRITER |
|---|---|---|---|---|---|---|
| 1 | **DEC** | an operator determination | `governance/decisions/DEC-<YYYYMMDD>-<SLUG>.md` | `DEC-` | CONTENT | operator |
| 2 | **CAND** | content proposed for canonical integration | `governance/candidates/CAND-<YYYYMMDD>-<SLUG>.md` | `CAND-` | CONTROL PLANE | plan (H.1) |
| 3 | **REVIEW** | a reviewer's judgement of a named object | `reviews/<ACTOR_ID>/REV-<OBJECT>-<REVIEWER>-<NNN>.md` | `REV-` | CONTROL PLANE | that reviewer, that directory |
| 4 | **APPROVAL** | a human resolution of a `HUMAN_REQUIRED` | `ledger/approvals/…` | `APR-` / `RES-` | CONTROL PLANE | 🔴 undeclared — B.3.2 |
| 5 | **PROPOSAL** | proposes a rule or model, not content for one candidate | 🔴 no correct home today — B.1.3 | `PROPOSAL-` | should be CONTENT | any actor |
| 6 | **HANDOFF** | transmits an artifact plus the determinations the sender is barred from making | author's own working root | `HANDOFF-` | follows its root | the sender |
| 7 | **WORKING RECORD** | analysis, preparation, response — `PREP`, `ADVISORY`, `DELTA`, `PLAN-`, `SLR-`, `AUTHOR-RESPONSE` | `learning/<actor>/`, `reviews/<actor>/` | various | follows its root | its author |

**Classes 6 and 7 are not promoted to path-governed classes.** They live beside their author's other
work, under one negative rule: *a working artifact never sits inside a class directory it does not
belong to.*

### B.1.3 · 🔴 The defect the taxonomy exists to fix — and it is one directory

Carried from the coordinator, attributed, verified from root at 52 refs with positive controls:

> `governance/candidates/` holds **six classes under one hash rule**: 7 CAND manifests, a PROPOSAL
> (`ACCEPTED`, imposing a live hold), an APPROVAL/deviation record, an ADVISORY, a DELTA REVIEW,
> 4 HANDOFF/REVIEW packages. Because that path is a declared `CONTROL_PLANE_ROOT`, **all sixteen are
> excluded from `CANDIDATE_CONTENT_HASH` by location alone** —
> `candidate_content_hash.py --base main~1 --tip main --show-domain` → 535 included, 45 excluded,
> `PROPOSAL-C9-STATE-MODEL.md` and `APPROVAL-GOV311-DEVIATIONS.md` among them.

**An `ACCEPTED` proposal that suspends L2 across the laboratory is normative in effect and moves no
candidate hash.** The directory conflates *"describes a candidate"* with *"lives near candidates"*;
P5.1's exclusion is right for the first and wrong for the second.

Independently measured here over 764 tracked paths across 52 refs:

| finding | count | detail |
|---|---|---|
| 🔴 `DEC-*` outside `governance/decisions/` | **3** | all in `governance/candidates/` |
| `DEC-*` correctly placed | 4 | the newest class was placed right |
| 🔴 `APPROVAL-*` in `governance/candidates/` | **1** | `APPROVAL-GOV311-DEVIATIONS.md` |
| ✅ `REV-*` outside `reviews/` | **0 of 40** | REVIEW already holds by construction |
| ⚠️ `HANDOFF-*` roots | **5** for 12 files | conformant under B.1.2's author-root rule |
| ⚠️ `PROPOSAL-*` roots | 2 for 3 files | one in the scientific `commit_candidates/` |

### B.1.4 · What the convention does about it — and what it refuses to do

```
DECLARED    PROPOSAL is a class. Its correct domain is CONTENT.
NOT DONE    No file is moved. Relocating changes which paths enter CANDIDATE_CONTENT_HASH, i.e.
            candidate identity. MIGRATION item (§ B.7), not a convention act.
NOT DONE    CONTROL_PLANE_ROOTS is not amended — a governed change to plan_defined_parameters.md
            with a version-prefix bump. The convention SAYS a change is needed; it performs none.
            → PROPOSAL P-1.
```

**🟠 INTEGRATION CORRECTION — the no-relocation ruling, stated at the strength the evidence
supports.** The coordinator first ruled that moving `reviews/` or `ledger/approvals/` under
`governance/` would contradict a frozen rule, then corrected itself after a hostile seat broke the
framing. The corrected form is adopted here:

- **P5.1 does not forbid the relocation.** It makes it a *governed amendment*: declare
  `governance/reviews/` as a prefix and exclusion is restored — exclusion is a literal prefix match,
  so `governance/reviews/x.md` simply does not begin with `reviews/`.
- The real cost is that such an amendment **falsifies a load-bearing sentence** of P5.1 — *"all of
  `governance/` except `candidates/` are outside every root and always in the domain"* — and P5.1
  already carries a 🔴 marker over a different load-bearing sentence falsified the same way.
- **Escalation class is "cost and fragility", not "a frozen rule must change".**

The outcome is unchanged: **nothing is relocated.** A hostile review that became CONTENT would let a
reviewer's verdict change the identity of the object under review — the fixed point P5's
`legend-candidate-v4` removed.

## B.2 · Lifecycle model — existing values, none invented

### B.2.1 · What is written today, read from `main`

| class | key | values observed |
|---|---|---|
| CAND | `state:` ×6, `status:` ×1 | `READY FOR MIRROR HOSTILE REVIEW` ×3 · `READY FOR MIRROR REVIEW (revision 6) — …` · `READY FOR MIRROR RE-REVIEW` · `APPROVED — …` · `PROPOSED — awaiting Mirror hostile review …` |
| DEC | `record_type:` + `status:` | `OPERATOR_DECISION` + `BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE` |
| REVIEW | `verdict:` | `ACCEPT` ×7 · `REQUEST CHANGES` ×17 · `BINDING VERIFIED` ×2 · 🔴 **absent ×13** (39 `REV-*` on `refs/heads/mirror`) |
| APPROVAL | `STATE` (JSONL) | J.3's five, plus `DEFERRED` ×2 and `RESOLVED` ×1 outside it |
| PROPOSAL | `status:` | `ACCEPTED` · `REVIEWED` |

Three problems visible without interpretation: **two keys for one concept**, **free prose fused into
the value**, **a third of reviews carrying no disposition field at all**.

### B.2.2 · 🔴 The REVIEW class has two verdict axes, and only one is governed

```
DISPOSITION  what frontmatter `verdict:` carries and what gates work:
             ACCEPT | REQUEST CHANGES | BINDING VERIFIED        — 26 files
             absent                                              — 13 files
C.2 VERDICT  the governed epistemic vocabulary — CONFIRMED | WEAKENED | REFINED | REFUTED —
             which appears in review PROSE and in ZERO frontmatter `verdict:` fields measured.
```

**Neither is wrong and they are not the same question.** The disposition says what happens next to
the object; the C.2 verdict says what happened to the claim's epistemic standing. The convention
names both because the repository already keeps both, and invents neither — the disposition set is
transcribed from the 26 files that carry one.

> This independently reproduces a finding Mirror raised against `PLAN-EXECUTION-TRANSITION-001`:
> that record's § 2.1 bound `verdict:` to the C.2 enum, which its own cited reviews
> (`verdict: ACCEPT`) do not satisfy. **A document-level DISPOSITION is a different object from a
> per-axis VERDICT.** The finding is accepted and this section is the repair.

### B.2.3 · The forward lifecycle rule

```
KEY          status:      one key, forward. `state:` is LEGACY on 6 CAND manifests, NOT retrofitted.
VALUE        a TOKEN — uppercase, underscore-joined, no spaces, no prose.
NOTE         everything after " — " on the same line is a NOTE, not part of the value; nothing
             may key off it.
REVIEW       two fields:  verdict:     ACCEPT | REQUEST_CHANGES | BINDING_VERIFIED   (disposition)
                          c2_verdict:  CONFIRMED | WEAKENED | REFINED | REFUTED      (Annex C.2)
             A review stating a disposition in prose and omitting it from frontmatter is a finding.
APPROVAL     J.3's enumeration ONLY. DEFERRED and RESOLVED are preserved verbatim as LEGACY and
             NEVER normalised in a source line — a record edited to agree with its own derivation
             has stopped being evidence.
DEC          record_type: OPERATOR_DECISION, plus a status token.
RECORD_TYPE  prefer `record_type:` (enumerated) over `artifact:` (free prose), forward only.
```

🔴 **Nothing in B.2.3 applies retroactively.** No existing file's status is rewritten. See § B.7.

## B.3 · Ownership — who may write what, where

Ownership of *sessions* is § A.2–A.3 and is not restated. This section covers what is class-specific.

**B.3.1 — A class's writer is the writer named in B.1.2, and nobody else writes that path.**
`reviews/<ACTOR_ID>/` accepts writes from that reviewer only; `governance/decisions/` from the
operator only; `governance/candidates/` from plan (H.1 — *integrazione strutturale / candidate*).

**B.3.2 — 🔴 One class has no writer, and the convention may not allocate one.**
`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` has **no declared writer**: J.3 names a requester and a
resolver and allocates no file writer; § P7's one-writer decision covers `ledger/events/`, not
`ledger/approvals/`. The consequence is measured (carried from the coordinator, attributed): the file
is **forked into three lineages** — 6 lines on 27 refs including `main`, 10 on `orchestrator`, 14 on
`evidence-index` + `p51c9-rebased` — and **all four MAJOR approvals (SUNSET-DEC3, SCIAB, XPORT,
P5DOMAIN) are reachable from `refs/heads/orchestrator` and from no other ref.**

Allocating a writer is a governance act (H.1). The convention declares the gap, names it as the
cause of the fork, and stops. → **PROPOSAL P-2.**

## B.4 · Handoff conventions

The dispatch rules A.5.7 and A.5.8 apply to handoffs unchanged and are not restated. Two rules are
handoff-specific:

```
H-1  A HANDOFF BINDS BY BLOB, NOT BY BRANCH TIP.  Declare the object's blob id; a branch tip may
     sit ahead of the content that was reviewed.
     Earned: a handoff bound a revision its own addendum had superseded.

H-2  A PRODUCER EMITS NO VERDICT TOKEN.  Annex C.2's vocabulary belongs to a REVIEWER reviewing an
     object. A producer's canonical equivalent is the ABSENCE of the field — which is what every
     existing HANDOFF-* in the repository does.
```

## B.5 · Review conventions

```
R-1  REVIEWS LIVE IN reviews/<REVIEWER ACTOR_ID>/.  Already true of 40 of 40. Codifies what holds.
R-2  REVIEWER ≠ AUTHOR.  A self-review emits an OBSERVATION, not a verdict.
R-3  TWO VERDICT AXES, DECLARED SEPARATELY — § B.2.2.
R-4  AUTHOR_RESPONSE IS OWED AND TRACKED (C.2 — silence is not acceptance). One is outstanding:
     REV-ROLES-MIRROR-001. An outstanding AUTHOR_RESPONSE blocks the reviewed object's activation
     and blocks nothing else.
R-5  BLIND REVIEW FOR INFRASTRUCTURE.  Where the object is plumbing rather than a claim, the
     reviewer SHOULD receive the artifact without its authorship and without the author's
     conclusions.  Earned: a blind reviewer found eight defects two informed reviewers had passed
     over twice.
R-6  A REVIEW RE-RUNS; IT DOES NOT RE-READ — A.7.6.
```

## B.6 · Escalation — the single test

**One test, integrated from Section A § A.8 and the Plan seat's draft.** Two lists of escalation
conditions in one document is the drift failure this convention is about; there is one list.

### B.6.1 · Escalate if and only if

```
E-a  a FROZEN object would have to change, or what a FROZEN object means would have to change;
E-b  an authority nobody currently holds would have to be allocated;
E-c  money would be spent (J.4 — DEFAULT_EXTERNAL_SPEND = 0);
E-d  the act is irreversible in the repository — history rewrite, deletion, publication, a push;
E-e  the act requires an ACTIVE lease and no lease is held;
E-f  two valid interpretations produce MATERIALLY DIFFERENT ARCHITECTURES, or a body §48 stop
     condition is live and cannot be discharged without a human.

OTHERWISE: choose the minimal reversible option, RECORD THE RATIONALE IN THE ARTIFACT, and continue.
```

### B.6.2 · Explicit NON-escalations

Stated positively, because a rule that only says when to stop produces sessions that stop.

```
NOT an escalation:  building a mechanism that measures and reports
                    running any report or read-only command
                    selecting an item from an existing queue by an existing ranking
                    wiring a new check at INFO severity
                    WORK_COMMIT of your own named paths on your own branch (H.1, A.6.1)
                    writing an artifact that declares itself non-binding
                    file naming, artifact organization, migration mechanics
                    seat designation for one mandate
                    choosing between two safe orders, or two reversible options
```

### B.6.3 · The form an escalation takes

**An escalation is a decidable question, never a blocker report.** It carries: the determination in
one sentence, phrased so it can be answered; which of E-a…E-f it trips; the options, exhaustive at
the level of the decision; a **recommendation with its reason**, which the operator is free to
reject; and what is already true regardless of the answer.

**A session with nothing to do while it waits has scoped its own work wrongly.** Everything
independent of the answer is done first, and the escalation is raised when the answer is needed.

## B.7 · Migration — separated from activation

**The forward system is defined by § A and § B. Nothing above applies retroactively.** Each item
below is a separate reversible act; none gates the convention.

| # | item | count | act | blocked by |
|---|---|---|---|---|
| M-a | `DEC-*` in `governance/candidates/` | 3 | `git mv` to `governance/decisions/` | a DEC — moving a governance artifact is a governance act |
| M-b | `APPROVAL-*` in `governance/candidates/` | 1 | `git mv` to the home the taxonomy declares | same |
| M-c | `PROPOSAL-C9-STATE-MODEL.md` domain conflict | 1 | domain determination, then relocation | **P-1** |
| M-d | `HANDOFF-*` across 5 roots | 12 | none — already conformant under B.1.2 | nothing |
| M-e | CAND manifests using `state:` | 6 | key rename at next touch, never a sweep | nothing |
| M-f | `REV-*` with no `verdict:` field | 13 | the reviewer adds what it already stated in prose | nothing; the reviewer owns it |
| M-g | artifacts carrying `session_ref:` | **0 of 764** | forward-only, never retrofitted | nothing |
| M-h | `runtime_inventory.md` on 1 ref, dated 2026-08-17 | 1 | mechanization — Appendix D | nothing |

🔴 **M-g is the honest headline.** No artifact carries a `session_ref` today. The attribution rule is
worth exactly what future artifacts make it worth, and repairs nothing that already happened.

## B.8 · Compatibility with the current repository

### B.8.1 · What this document does not touch

```
P5.1's CONTROL_PLANE_ROOTS          unchanged — a change is PROPOSED, never performed
CANDIDATE_CONTENT_HASH rule (P5.2)  unchanged — no byte layout, no version prefix, no domain edit
the fingerprint pertinence sets     unchanged — MEASURED: every input of all four roles lies under
                                    governance/ or roles/; this file rotates nobody's fingerprint
the LINT and its gates              unchanged — nothing wired, no severity changed
the receipt ledger and its chain    unchanged — 128 receipts, chained, tail anchored
Annexes A–J and the body            cited only; not restated, amended or activated
roles/*.md                          untouched; all four remain PROPOSED per DEC-20260822
the four scientific current files   untouched
```

### B.8.2 · 🔴 One compatibility claim that cannot be made

**The event ledger has never existed.** `ledger/events/` and `ledger/consolidated/` are on **0 of 52
content refs** (control: `ledger/approvals` on 30 of 52). No clause here reads it, writes it, or
assumes it. When a writer is built it adapts to this convention — the reverse is unavailable,
because there is nothing to adapt to. § B.2.3's lifecycle tokens are deliberately shaped to sit
inside J.1's event schema (`EVENT_TYPE`, `OBJECT`, `DURABLE_POINTER`) without translation.

### B.8.3 · Two known-stale surfaces, deliberately left alone

Under B.1.1 clause 3 — presence does not imply authority — **a stale status line is a finding, not a
licence, and correcting one is an ACTIVATION, which the mandate forbids.**

| surface | conditions | measured |
|---|---|---|
| `governance/plan_defined_parameters.md` (§ P7) | Mirror review passes · operator approves | `REV-P5DOMAIN-MIRROR-001` **ACCEPT** · `APR-20260819-P5DOMAIN-001` **APPROVED** · tip `ceefaa286115` ancestor of `main` |
| `framework/protocols/cross_session_transport.md` (§ 8) | canonical execution · Mirror ACCEPT · operator approval | `e839db383827` ancestor of `main` · `REV-XPORT-MIRROR-002` **ACCEPT** · `APR-20260819-XPORT-001` **APPROVED** |

Neither is touched. The second-order reason for the first is § A.9: that file is hashed whole in
CORE, so even an inert added block would rotate four fingerprints. **Recalibrate first (P-6), then
correct.**

## B.9 · What this document assumes from elsewhere

Facts carried **attributed, not re-derived**. Three are load-bearing; if they fall, the clauses
naming them fall with them.

| fact | source | used in | load-bearing? |
|---|---|---|---|
| six classes in `governance/candidates/`, 535 included / 45 excluded | coordinator, root, 52 refs | B.1.3, B.1.4, M-c, P-1 | 🔴 **YES** |
| approval queue forked 3 ways; 4 MAJOR approvals only on `orchestrator` | coordinator | B.3.2, P-2 | 🔴 **YES** |
| `ledger/events/` on 0 of 52 refs | coordinator; consistent with this seat's own sweep | B.8.2 | 🔴 **YES** |
| transcript birth vs `started` — 19h56m | orchestrator seat, two seats | A.1.4 | yes, for A.1.4 only |
| `cp -p` / `git archive` forge mtime | orchestrator seat, reproduced forward | A.4.2 | yes, for A.4 only |
| `runtime/orchestrator_lease.md` inside the content domain, 9 blob changes | mirror seat → coordinator | A.8 | no — corroborative |
| `plan_defined_parameters.md` hashed whole in CORE | mirror seat → coordinator | A.9, B.8.3 | no — explanatory |

**Everything else was measured by the authoring seat with the command shown in § B.12.**

## B.10 · PROPOSALS — conflicts with frozen governance, marked and not implemented

| # | proposal | conflicts with | why not implemented | trips |
|---|---|---|---|---|
| **P-1** | PROPOSAL's correct domain is CONTENT: give it a root outside `governance/candidates/`, or amend `CONTROL_PLANE_ROOTS` | P5.1 declares the roots exhaustively; a change needs a version-prefix bump | either form changes candidate identity | E-a |
| **P-2** | declare ONE writer for `ledger/approvals/`. Recommended: per-actor `requests/<ACTOR_ID>.jsonl` + `resolutions/operator.jsonl`, consolidated by replay — the topology § P7 already chose, dissolving the fork by construction rather than by discipline | J.3 allocates no file writer | allocating authority nobody holds | E-b |
| **P-3** | recognise `DEFERRED` / `RESOLVED` as LEGACY, surfaced in a derived view, never normalised in a source line | J.3's enumeration lacks them | recognising a value outside a frozen enumeration is a reading of J.3 | E-a |
| **P-4** | relocate the 3 misplaced `DEC-*` and 1 `APPROVAL-*` (M-a, M-b) | moving a governance artifact is a governance act (H.1) | changes what is in the content domain | E-a |
| **P-5** | make `verdict:` / `c2_verdict:` required REVIEW frontmatter | C.2 owns review method; G.2 puts Mirror's method beyond unilateral change — including by this convention | a convention changing a reviewer's method is governance | E-a |
| **P-6** | recalibrate `APPLICABLE_GOVERNANCE_FINGERPRINT` composition to hash `plan_defined_parameters.md` **by section** in CORE, as § P2.2 already does for Annex J. **Ordered by A.6 RECOVERY(b), assigned to Plan** | nothing — but the file's own `change_class: MAJOR` routes it through GATE 3, ending in HUMAN_APPROVAL | Plan may PREPARE the candidate; performing it needs Mirror PASS + operator approval | E-a |

**None is performed by this document.** Each carries its option and a recommendation so that, taken
up, it is decidable in one pass.

## B.11 · What this document does not do

Does not amend, restate, activate or reinterpret any FROZEN object · does not touch
`plan_defined_parameters.md` or any fingerprint input · does not change a `status:` line anywhere ·
does not move, rename or delete any repository file other than its own two superseded drafts ·
does not allocate a writer · does not open a `CAND`, write a `DEC` or create an `APPROVAL` · does
not write to `ledger/`, `runtime/` or `governance/` on any ref · does not activate a role contract ·
does not confer or claim an ACTOR_ID · does not acquire a lease · does not wire anything into the
LINT or CI · does not build Appendix D · does not touch the six untracked artifacts in this
worktree · does not advance `main`.

---

# APPENDIX D — MINIMAL PLUMBING, PROPOSED AND NOT BUILT

> **Deliverable 2 of dispatch `OPCON-V1-PLAN-001`.** Proposal-level by instruction. **Nothing here
> exists as code.** Folded into this file rather than given its own path: one convention, one
> writer, and a validator that must parse § B.1.2 should not live a directory away from it.

## D.0 · What it is for — four failures, each with its measured cost

| # | failure, this week | cost paid | function |
|---|---|---|---|
| 1 | an artifact appeared in a shared worktree; three sessions could not say whose | **4 cross-session messages**, one retracted finding | DISCOVERY |
| 2 | bytes-at-risk reported as 337 kB (one seat); true figure 746 kB (two seats) | an operator decides differently at 337 than at 746 | DISCOVERY |
| 3 | 3 `DEC-*` and 1 `APPROVAL-*` excluded from the candidate hash by location alone | an `ACCEPTED` proposal imposing a live hold moves no hash | VALIDATION |
| 4 | 8 operator approvals invisible from `main` | approval state unreadable from the sovereign ref | INDEXING |

## D.1 · DISCOVERY — `framework/scripts/artifact_index.py`

```
DOES    walk declared roots (default: working tree; --all-refs sweeps the 52 content refs),
        classify against § B.1.2, parse frontmatter, emit JSONL:
          path · class · id · declared_domain · derived_domain(P5.1) · record_type · author ·
          session_ref · status_key · status_token · status_note · refs_carrying
NEVER   writes into the tree it scans · resolves an ambiguity · repairs a field
EXIT    0 always. Discovery reports; it does not judge.
```

🔴 **`--all-refs` is not optional.** `reading_state.md`'s own header states the trap: *"true of ONE
checkout… a count over unmerged state is a count of work that is not in the model."* A working-tree
scan reported as a laboratory figure is failure 2 exactly. Every output states its population in the
same sentence as its counts (A.7.4).

## D.2 · VALIDATION — `framework/scripts/artifact_conventions.py`

```
CHECKS  1 PATH ⇄ CLASS   2 CLASS ⇄ DOMAIN vs P5.1   3 ATTRIBUTION (author, session_ref)
        4 LIFECYCLE token in the class enumeration   5 LEGACY KEY (`state:` where `status:` is forward)
MODES   --report  default, exit 0        --strict  exit 1 — SHIPS UNWIRED
NEVER   edits · normalises a legacy value · moves anything
```

**Why `--strict` ships unwired**, recorded as a minimal-reversible choice: a gate switched on the
same day as its first measurement blocks on its own novelty. Report for one cycle, then wire it —
one line in `run_release_regressions.py`, reverted by reverting that line.

**🔴 Parse the convention, never copy it.** The class table is parsed out of § B.1.2 at run time, by
column header — not restated in a constant, not in a fixture. Precedent:
`governance_fingerprint.py` parses § P2.2; `candidate_content_hash.py` parses § P5 — *"if the prose
stops parsing, this fails loudly instead of using a stale copy."* A guard test asserts no module
restates the table, in the shape of `test_record_conventions.py`'s test 2, **which exists because
five modules once held five private lists of one definition and the shortest was wrong: the
denominator was 168 records short and `PAPER 032` silently absorbed 168 stub bodies.** A
machine-readable duplicate of § B.1.2 was considered and rejected as the sixth copy.

## D.3 · INDEXING — a generated page

```
IS      derived. Header carries, in the file: "GENERATED by … — do not hand-edit", the population
        it covers IN THE SAME SENTENCE as its counts, and the instant of generation.
IS NOT  canonical · a second source of truth · an authority
        J.1: "lo stato repo resta sovrano — in conflitto vince il repo".
```

It is the only proposed surface that makes failure 4 visible: an approval reachable from one ref and
invisible from `main` becomes a row, not a discovery made two weeks later.

## D.4 · ROUTING — and the line it must not cross

```
DOES    print, per open artifact: who owns the next act (class + status + § B.6.1), whether it is
        blocked and by what, and whether it trips E-a…E-f and is therefore the operator's
NEVER   assigns a task · writes a queue · sends a message · claims an artifact · changes a status ·
        holds state between runs
```

🔴 **This is where a plumbing proposal would accidentally escalate authority, so it is stated before
Mirror has to find it.** Routing is derivation and printing. It is **not dispatch**. `TASK_ASSIGNED`
has exactly one authorized writer under H.1 row 1 and nobody holds it — `lease_state.py` returns
`ACTIVE by derivation: 0`. A router that assigned work would allocate an authority nobody holds:
**E-b**. The router answers *"whose act is this?"* — it never performs the act and never tells
anyone to.

## D.5 · The guard extension — mechanizing the judgeable part of A.6.3

Three denials added to the existing PreToolUse guard, each unambiguous and destructive with no undo:
bare `git stash` / `pop` / `drop`; `git reset --hard`; blanket `git clean -f` / `git checkout -- .` /
`git restore .`. Named paths stay allowed, mirroring the existing blanket-staging rule.
**Branch switching is excluded by design** — A.6.7.

## D.6 · Build order, cost, and the smallest useful subset

```
1 DISCOVERY   ~180 + 150 test   gated by § B.1.2 being stable enough to parse
2 VALIDATION  ~200 + 180 test   gated by 1, and by § B.2.3's enumerations
3 INDEXING    ~120 +  90 test   gated by 1
4 ROUTING     ~150 + 120 test   gated by 2, and by § B.6.1 being agreed
5 GUARD       ~ 60 +  80 test   gated by nothing
TOTAL ~1,330 lines.
```

**If only one thing is built: DISCOVERY.** ~330 lines with its test, writes nothing, needs no agreed
enumeration — only the class table — and eliminates failures 1 and 2 outright. The other three are
derivations of its output and none can be built without it.

## D.7 · What Appendix D cannot claim

```
NO EVENT-LEDGER COMPATIBILITY — it has never existed (B.8.2)
NO NEW ROOT · NO CI GATE (--strict unwired) · NO GOVERNED WRITE · NO RETROFIT
```

---

## VERIFICATION TRAIL

| # | claim | how | result |
|---|---|---|---|
| 1 | tracked paths | union of `git ls-tree -r` over 52 content refs | **764** |
| 2 | `DEC-*` placement | same | 4 in `decisions/`, **3 in `candidates/`** |
| 3 | `APPROVAL-*` placement | same | **1**, in `candidates/` |
| 4 | `REV-*` placement | same | 40 files, **0 outside `reviews/`** |
| 5 | `HANDOFF-*` roots | same | 12 files, **5** roots |
| 6 | review disposition vocabulary | `verdict:` of all 39 `REV-*` on `refs/heads/mirror` | `ACCEPT` 7 · `REQUEST CHANGES` 17 · `BINDING VERIFIED` 2 · **absent 13** |
| 7 | C.2 vocabulary in frontmatter `verdict:` | same sweep | **0** — it lives in prose |
| 8 | CAND lifecycle values | frontmatter of every `CAND-*` on `main` | 6 `state:`, 1 `status:`; transcribed in B.2.1 |
| 9 | SESSION_REF named in frozen text | `git show main:governance/GOVERNANCE_v3.1.1.md` | **line 184**, and § 43 line 418 lists `Working dir` |
| 10 | A.6 RECOVERY(b) | `git show main:governance/annex_a_task_contract.md` | *"Plan ricalibra la composizione del fingerprint (modifica governata)"* — verbatim |
| 11 | change_class of the recalibrated file | `git show main:governance/plan_defined_parameters.md` | **line 11** — `MAJOR … follows gate 3` → HUMAN_APPROVAL (A.9.1) |
| 12 | does this file rotate a fingerprint? | `governance_fingerprint.py inputs --role <r>`, all 4 roles | **NO** — every input under `governance/` or `roles/` |
| 13 | is this tree's `plan_defined_parameters.md` main's? | `git diff --stat main..HEAD` over the 13 pertinence inputs | **EMPTY** |
| 14 | plan fingerprint here | `governance_fingerprint.py compose --role plan` | `0d6987bd79e5…aefaec1429` — equals main's |
| 15 | timestamp method | `date -u -r <epoch>` vs naive `stat -f '%Sm'` | true `15:20:37Z` vs naive `17:20:37Z` — A.4.1 confirmed |
| 16 | `main` | `git rev-parse main` | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` — unchanged |

---

**Assembled by:** seat `plan`, session `evidence-index-58 [432290]`, worktree `evidence-index`,
branch `plan-orchsurf-r4-transcription`, 2026-08-23 — under the operator's Transition Execution
Mandate, routed by `OPCON-V1-PLAN-001`, integrating Section A from
`legend-operating-convention-v1:learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md` @ cebca20.
**Not** under the authority of `roles/plan.md`, which is `PROPOSED` and not binding.
