---
artifact: LEGEND Operating Convention v1 — the session layer
record_type: OPERATIONAL_CONVENTION
record_id: OPCON-V1
task_id: OPCON_V1_PLAN_001
dispatch_id: OPCON-V1-PLAN-001 · re-integrated under -002 and -003
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

integration_binding: >
  🔴 THIS DOCUMENT DECLARES THE BLOB OF EVERY SOURCE IT CONSUMED (rule H-1, extended by N-4).
  Section S integrated from
  `legend-operating-convention-v1:learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md` @ 30cb4f3
  (r3, which supersedes r2 @ ce2dc6e and adds S.7.7 plus the instant clause of S.7.6).
  SUPERSEDES: this file's own first integration, blob 27587908dde910f8cc2428fcf78bec26457e2178
  (commit 1562ed6, 2026-08-23T16:25:07Z), which consumed r1 @ cebca20 — correctly, because r2 did
  not exist for another 2m07s. `git merge-base --is-ancestor ce2dc6e 1562ed6` → NO, verified here.
  Nobody erred; a blob was described as containing a fix it predated.

one_file_one_writer: >
  Section S drafted by the orchestrator seat and handed over as INPUT; integrated by the Plan seat,
  which holds structural integration under H.1. One convention, one path, one writer. Corrections
  made during integration are marked 🟠 INTEGRATION CORRECTION and name what they correct and on
  what evidence.

domain: >
  CONTENT. `framework/` matches no declared CONTROL_PLANE_ROOT prefix (P5.1 —
  `governance/candidates/`, `ledger/`, `reviews/`), so this file is inside CANDIDATE_CONTENT_HASH
  and moves it. Disclosed. MEASURED separately: it rotates NO role's fingerprint — no `framework/`
  path appears in any role's pertinence set (`governance_fingerprint.py inputs --role <r>`, four
  roles).

reads_normative_text_from: >
  `main` @ 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5, via `git show main:<path>` (S.5.5).
  Declared exception: `governance/plan_defined_parameters.md` read from this working tree, because
  `git diff --stat main..HEAD` over the 13 fingerprint pertinence inputs — that file among them —
  is EMPTY. This tree's copy IS main's, measured.
---

# LEGEND OPERATING CONVENTION v1

> **This is a working layer. It is not governance.** Where this document and a frozen normative
> file disagree, the frozen file wins and this document is the defect. Nothing here activates a
> role contract, confers an ACTOR_ID, grants authority, or reinterprets a frozen rule. Anything
> that would require a frozen rule to change, or that determines behaviour frozen text leaves
> under-determined, is marked 🟡 **PROPOSAL — NOT IMPLEMENTED**.

> 🔴 **SECTION NUMBERING.** The session-layer section is **`S.n`**, never `A.n`. Annex A of the
> frozen governance already owns `A.1`–`A.7` — `A.6 · CHECKPOINT`, `A.7 · RESUME IDEMPOTENTE` — and
> **22 files at `main` cite `A.6`**. A protocol file that every actor reads must not publish a
> second `A.6` into the same namespace. *An earlier blob of this file did exactly that; the
> renumbering is the repair.*

---

## 0 · THE THREE LAYERS

| Layer | Home | Who may change it | Changed by this document |
|---|---|---|---|
| **FROZEN NORMATIVE** | `governance/` — body (`status: FROZEN`), annexes A–J, `plan_defined_parameters.md`, `roles/` | operator, through the governed path | **nothing, not one byte** |
| **OPERATIONAL CONVENTION** | `framework/protocols/` — the established protocol home, which carries an index | Plan drafts · Mirror reviews · operator ratifies | this *is* that layer |
| **IMPLEMENTATION MECHANISM** | `framework/scripts/`, `governance/scripts/`, `scripts/` | any actor, own branch, reviewable | only by proposal, Appendix D |

*A first draft gave layer 2 the home `operations/`; created and withdrawn in the same session.
`framework/protocols/` reuses what exists instead of adding a top-level root — which is what "adapt
to LEGEND, not redesign LEGEND" means.*

**The failure this separation prevents** is one the repository has already recorded: operating law
accumulating inside a router until nobody could tell which sentence bound them. `CLAUDE.md` became
a router on 2026-08-16 for exactly that reason.

### 0.1 · The honesty test — two limbs, because one limb was blind

**Limb 1 — contradiction.** *If this rule were deleted, would anything become permitted that
governance forbids?* If yes, it is governance wearing a convention's clothes.

**Limb 2 — accretion into silence.** *Does this rule determine behaviour a frozen rule leaves
UNDER-DETERMINED?* If yes, mark it 🟡 **PROPOSAL** and name the silence.

> 🔴 **Limb 2 exists because limb 1 alone clears the exact failure this layer was built to prevent.**
> Run limb 1 on `governance/decisions/`: deleting *"operator decisions live here"* permits nothing
> governance forbids, because governance says nothing about them at all. **Measured at `main` over
> the 15-file normative corpus** (body + 10 annexes + 4 role contracts):
>
> ```
> OPERATOR_DECISION        0        ← the record_type every DEC declares
> governance/decisions     0        ← the directory four DEC records live in
> HUMAN_APPROVAL_QUEUE     3        ← positive control, fires
> CANDIDATE_CONTENT_HASH   8        ← positive control, fires
> GATE                    15        ← positive control, fires
> ```
>
> **It passes limb 1 at every step of becoming load-bearing**, up to four `DEC-*` records citing one
> another as precedent for a container with no normative basis. *Found by a hostile-review seat.*
>
> 🟠 **INTEGRATION CORRECTION — my first run of this measurement returned 0 for the controls too.**
> An unquoted `for f in $CORPUS` in `zsh` does not word-split, so the loop ran once on a single
> 15-path string and every count was zero. The control caught it, which is S.7.2 working. Rerun with
> a line-fed sweep and a file count assertion (`must be 15`), the controls fire and the two terms
> above are genuinely zero.

**Re-run under limb 2, four rules in this document fail and are marked 🟡: S.2.2, S.6.6, S.8, and
B.1.1 clause 2.** None is wrong. Each decides something frozen text left open, and saying so is the
difference between a convention and a quiet amendment.

---

# SECTION S — SESSIONS, SEATS, DISPATCH, PRESERVATION

> Drafted by the orchestrator seat from evidence produced on 2026-08-23, in a session where seven
> sessions were polled and **ten** of its own assertions were falsified by peers or by
> re-measurement. **Every rule exists because something failed that day**, and the cause is named
> beside it so a later reader can attack the rule by attacking its cause.

## S.1 · A session's identifiers, and what each proves

| Identifier | Proves | Does NOT prove |
|---|---|---|
| routing name `mirror-75` | where a message is delivered | role, seat, authorship |
| `[ref]` `[f3044e]` | disambiguates two rows sharing a name | same |
| session id `2a6ffe75-…` | uniqueness; keys the transcript | same |
| transport `uds:/…sock` | the wire a message arrived on | same |
| **`pwd`** | **which working directory is occupied** | that the occupant is alone |

**S.1.1 — A session name is not evidence of actorhood.** Seven live sessions carried lookalike role
names on 2026-08-23; none held an ACTOR_ID; the two registered refs were both dead.

**S.1.2 — A session cannot resolve its own actorhood.** *An actor choosing the reading that makes
itself an actor is the failure the gate exists to prevent.* **"None" is a correct and useful answer.**

**S.1.3 — A dispatcher verifies its addressee.** A session's row is the one its own peer list omits,
so the dispatcher derives it by set complement rather than accepting a self-report. *Some harness
builds print the session's own name, making the complement corroboration rather than necessity — but
the direction is what matters: it lets the DISPATCHER check the ADDRESSEE without taking its word.*

**S.1.4 — 🔴 `started` is not evidence about a conversation.** It is a property of the runtime
incarnation.

> **Measured, two seats.** A transcript with `birth = 2026-08-22T20:00:50Z` was still live on
> 2026-08-23 — a span of **19h56m** against a peer row reading *"started 6h ago."*

**The warrant, stated because S.4.2 would otherwise dissolve it.** `cp -p` forges birthtime and
mtime, so a transcript's birth is as forgeable as any file's. Two properties rescue it and neither
is a timestamp: the file **grew** across successive readings (`1 603 926 → 1 612 311 B`) and a copy
does not grow; and it lives on a **harness-owned append-only path** keyed by session id.
*Honest limit: the growth was observed by one seat, the birth and span by two.*

**S.1.5 — The rule is fail-closed, so it does not depend on its own evidence being true.**
*"Elimination by start time is invalid"* withdraws a method that **CLEARS** a session. If the
measurement is wrong, the rule costs a discarded shortcut. If it is right and the rule absent, a
co-occupant is cleared on bad evidence and a `git clean` follows. **Correct under both readings.**

## S.2 · One writer per working directory

**S.2.1 — The field is already mandated; the gap is mechanization.**

> Body **§ 43 · RUNTIME / AUTHORITY INVENTORY — VIVO**, minimum columns, verbatim:
> `… | SESSION_REF | Session ID | Agent ref | `**`Working dir`**` | Worktree | Branch | HEAD | …`
> And body line 184: *"ogni attore ha un **ACTOR_ID persistente** distinto dal **SESSION_REF
> effimero**."* `runtime/runtime_inventory.md` **exists** — 551 lines, `updated_on 2026-08-17`, on
> **1 ref** of the content population.

Governance named the object, specified the field, and an artifact carrying it was materialized.
Nothing keeps it fresh, and § 43's own sentence is *"riga stantia = non autoritativa"* — every row
decays into non-authority by design. **The convention adds no field. It fills one specified and
empty since 2026-08-17.** That is also why "session ≠ actor" cannot smuggle authority in through the
back door: the fields are governance's own.

**S.2.2 — 🟡 PROPOSAL (limb 2).** Seat occupancy is established by `(pwd, session id)`, nothing
weaker. *Silence named: no frozen rule says what establishes occupancy; § 14 forbids two writers
without saying how one is identified.*

**S.2.3 — Occupancy is measured by polling, not inferred.** This converted suspicion into
measurement in ten minutes on 2026-08-23.

**S.2.4 — Co-location is a hazard with zero conflicting writes.** Twelve untracked files across two
seats, three claimed; **no session had overwritten another.** The exposure is not what happened — it
is that one `git clean` from any co-occupant destroys everything. **Never round co-location up to a
lost-attribution event that did not occur.**

**S.2.5 — One writer per FILE is the achievable form while sessions are co-located.** A file has one
authoring session for its lifetime in the working tree. This does not replace body § 14; it is what a
session can guarantee unilaterally while § 14's precondition is unmet.

## S.3 · Attribution

| Rank | Evidence | Strength |
|---|---|---|
| 1 | claim + an artefact independent of the claim | **sufficient** |
| 2 | claim + disclaimers from every other polled occupant + an agreed digest | **sufficient to act on** |
| 3 | mtime inside a session window | **candidate set, never an author** |
| 4 | elimination by `started` | **invalid — S.1.4** |

**S.3.0 — What rank 1's independent artefact is for an UNCOMMITTED file.** A reviewer objected that
rank 1 is instantiable only for committed work — where git settles it and the table is unnecessary —
leaving the top tier decorative exactly where it is needed. Right about the filesystem, wrong about
the available objects: **the transcript's `tool_use` entries are harness-written, carry real UTC, and
are independent of any later claim.**

> A seat parsed its own transcript: 358 lines, three `Write`/`Edit` calls in the whole conversation,
> one into the repository, at `2026-08-22T20:22:44.653Z` — equal to the file's mtime **to the
> second**, from two objects with different authors. **Negative, and sound:** three write calls total
> means that conversation wrote none of the other four records — a conclusion that survives even if
> every one of those files were copied into place afterwards.

**S.3.1 — A matching digest corroborates the OBJECT, never the AUTHOR.** It would be identical if the
claimant were lying.

**S.3.2 — "Unclaimed" states who has spoken; "unknown-authored" is an inference.** Prefer the first.

**S.3.3 — Preservation does not depend on attribution.** Protect regardless of author. The protection
is cheap and the attribution expensive; do not gate the first on the second.

**S.3.4 — Every artifact declares its author and its session.**

```yaml
author:       plan                          # the SEAT
session_ref:  evidence-index-58 [432290]    # the SESSION — name + [ref]
```

🔴 **`session_ref` is an attribution AID, not proof.** Self-declared identity is exactly what S.1
rules out; a session writing someone else's `session_ref` is not caught by the field.

| state | meaning | worth |
|---|---|---|
| present, consistent with a live peer list | corroborated | strong |
| present, contradicted by a live peer list | **finding** — escalate, never overwrite | decisive, negatively |
| **absent** | **UNATTRIBUTED** | must be claimed before anyone commits it |

**What it buys is not proof; it is the elimination of the question.** One unattributed file cost four
cross-session messages and produced a retracted "third writer" finding. **Measured: 0 tracked paths
carry one today.**

**S.3.5 — Attribution discipline applies to this document's own citations.** A seat is not an
identity; four live sessions shared one. Where provenance is implied, name session + transcript
birth, or imply none.

## S.4 · 🔴 Timestamps

**S.4.1 — Forbid the class, not the instance, and name the real cause.** The cause is **hardcoding a
literal `Z` into a renderer while the process timezone is unset** — the format string is exactly what
cannot fix it.

```
epoch                       1787501665
date -u -r      REFERENCE   2026-08-23T16:14:25Z
stat -f '%Sm'  (no TZ)      2026-08-23T18:14:25Z   ← CEST wearing a Z it has not earned
TZ=UTC stat -f '%Sm'        2026-08-23T16:14:25Z   ← correct
```

**Rule: derive from the raw epoch — `date -u -r <epoch>`.** If a renderer is used at all, `TZ=UTC` is
mandatory and a literal `Z` without it is a forgery. The same trap lives in `%SB`, in `date -r`
without `-u`, and in `tar -tvf`. *A blanket "never `stat -f '%Sm'`" over-reaches: one seat produced
every figure it sent with `TZ=UTC stat`, correctly, and a later auditor applying a total ban would
discard sound measurements.*

**S.4.2 — Two ordinary operations forge timestamps, and both are what a careful person reaches for.**

| Operation | Forges | Why someone runs it |
|---|---|---|
| `cp -p` | source's mtime **and birthtime** | preserving files honestly before they are lost |
| `git archive \| tar` | every entry stamped with the **commit's** time | verifying a fingerprint honestly |

> Extraction at `2026-08-23T16:01:46Z` yielded `mtime = 2026-08-22T16:01:01Z` = `git show -s
> --format=%ct main`; the same test on a second commit tracked that commit's time. **It follows the
> commit, never the clock.**

**Any mechanism attributing work by mtime reads a field two routine operations rewrite.**

## S.5 · Dispatch

**S.5.1 — A dispatch declares its authority basis and what it does not confer** — which body section
or named annex, never a role contract standing alone (`DEC-20260822`).

**S.5.2 — A dispatcher declares its own state so the receiver can discount it.** A receiver that
cannot discount its dispatcher cannot refuse a bad dispatch.

**S.5.3 — Seat designation is coordination, not conferral.** One writing seat per role for one
mandate, measured rationale, others stood down **from writing**, revocable in one line. *It is not
authority: a peer cannot designate a seat, and two seats correctly declined to treat one as doing
so — complying on the hazard instead. That is the right response and the convention expects it.*

**S.5.4 — A dispatch carries established facts with the command that reproduces them, AND the
receiver re-runs them anyway. Both halves, or neither works.**

> *Earned in this integration, and recorded with both halves because recording only one teaches the
> wrong lesson.* A dispatch whose stated purpose was to spare the receiver re-derivation carried
> `7 CAND manifests`; the true figure is **8**, and the enumeration then sums to 16, matching the
> same dispatch's own *"all sixteen"*. It was caught **because the receiver re-derived anyway**, on
> a row its own load-bearing-fact table had marked load-bearing. The hazard and its compensator both
> fired. **A changelog that records only the error teaches the next dispatcher to supply fewer
> facts, when the lesson is that the receiver re-runs them.**

**S.5.5 — Read the RULE from the sovereign ref; read the OBJECT from its own tip.**
`git show main:<path>` for normative text. **But a candidate is defined by its branch tip and its
declared `BASE_HEAD`, not by `main`** — a reviewer applying the rule to the reviewed object reads a
tree the candidate is not. **State which you read for each.**

**S.5.6 — Corrections travel to the source, not into a footnote.**

**S.5.7 — A dispatch names only objects that resolve, and only governed vocabulary.**
*Cause, twice: a dispatch specified "the existing canonical HANDOFF v2.1 format" — 0 hits over the
content population, control `AUTHOR_RESPONSE` at 268; and `NEXT_OWNER` / `NEXT_TRANSITION` /
`HUMAN_GATE` — all dispatch-supplied frontmatter, no repository source. The real objects are
`HUMAN_REQUIRED` (body § 4), `HUMAN_APPROVAL` / `HUMAN_APPROVAL_QUEUE` (J.3) and `GATE 0–5`
(body § 12). A term outside that set is marked local and non-binding, or is not used.*

**S.5.8 — A redelivery is not a new generation.** Same `DISPATCH_ID`, same date, no
`DIRECTIVE_VERSION` and no `GENERATION` increment → verify the durable evidence, do not repeat
completed work (A.3, A.7, body § 36.3).

## S.6 · Preservation

**S.6.1 — `WORK_COMMIT` of one's own named paths on one's own branch is the author's own authority**
(H.1). **A relay can neither forbid it nor license it.**

> 🔴 *Both halves were learned in one session. A blanket "do not commit" was issued and two seats
> objected that foreclosing a safe route by relay is a decision that was not the relay's — conceded.
> Then the relay wrote that committing was therefore "your call", and a seat objected that a
> convention authored by a peer cannot confer authority in the other direction either. Also
> conceded.* **The symmetric rule: a peer relay changes what you KNOW about the hazard, never what
> you MAY do.**

**S.6.2 — Nobody commits, edits, repairs, relocates or deletes another session's artifact.** Report
it. `git add -A` is the mechanism; a named path is the remedy.

**S.6.3 — Held as HAZARD, not authority:** `checkout · switch · reset · clean · stash · stash pop ·
add -A / add . · branch change · git rm · worktree remove/prune`. A prune sweep is destruction
wearing a maintenance hat.

**S.6.4 — 🔴 The stash stack is REPOSITORY-GLOBAL, and an entry's seat is not its owner.**

> **Measured.** One entry, created **2026-08-16 10:48:39 +0200** — seven days before any current
> session — message *"On evidence-index: PLAN base-alignment: **superseded** PMID42422765 worktree
> edit, preserved before rebase"*, one file, +2 −2, on a canonical deepdive manifest.

`pop` from any worktree takes it. **And it must not be reclaimed at all**: its own message says
`superseded`, so applying it would reintroduce a superseded edit into a canonical scientific
artifact. *A seat was told this entry was "yours, reclaim by apply". Wrong twice — not that
session's, and not to be reclaimed by anyone without an operator decision that it is still wanted.*

**S.6.5 — An out-of-repository copy is declared or it does not exist.** Declared means: not a commit,
not durable, session-scoped, deletable, no transfer of the `WORK_COMMIT` act, and **never counted as
work preserved.**

**S.6.6 — 🟡 PROPOSAL (limb 2). Redaction is owed before a branch is offered for integration.** A file
carrying a `public_release_gate.py` `DIRECT_IDENTIFIER` block must be redacted before the branch it
sits on is offered; a GATE 2 block is not cleared retroactively. *Stated first as "redaction and
commit are one act", which would have forbidden a `WORK_COMMIT` that S.6.1 declares the author's own
and that GATE 2 does not reach. Silence named: no frozen rule sequences redaction against
`WORK_COMMIT`.*

## S.7 · Measurement

**S.7.1 — 🔴 Mandate the COMMAND, never the integer.**

```bash
git for-each-ref --format='%(refname)' refs/heads refs/remotes refs/tags | wc -l
# excludes refs/codex/turn-diffs/* and refs/stash as non-content
```

> **An earlier draft hardcoded "52 refs (43 heads + 4 remotes + 5 tags)". It was already false.**
> Re-measured during this integration at `2026-08-23T16:42:37Z`: **53 = 44 + 4 + 5**, and the 44th head is
> `legend-operating-convention-v1` — the branch this convention was drafted on. **The act of drafting
> the rule falsified the constant the rule stated**, and it re-falsifies with every branch any seat
> opens. **Every ref-population figure in this document is therefore a command, not a literal.**

**S.7.2 — Every sweep carries a positive control, and the control must be able to fail. EVERY sweep —
the rule fails by omission long before it fails by design.** *Two instances from this document's own
construction, in opposite directions. § 0.1's corpus sweep HAD a control; the control returned 0,
caught an unquoted-glob fault, and the figure was repaired before use. B.2.2.1's field sweep had
**no control**, was scoped to the first 25 lines of each file, returned a clean `0 of 39`, and was
published as load-bearing. **The sweep that carried the most weight is the one that ran naked** — and
its control, when finally written, fired at 39 of 39 immediately.*

**S.7.2b — Anchor a field search to the field position.** An unanchored `grep -i FIELD_NAME` counts
prose mentions as declarations: over the same 39 files the unanchored form returns 28 lines, of which
**20 are prose**, against 8 real declarations. *A peer's count of the same object was inflated this
way while this seat's was scoped to zero — both wrong, in opposite directions, on one field.*

**S.7.3 — 🔴 A control that shares the flaw of the search cannot detect it.** It proves the instrument
works; it cannot prove it is aimed correctly.

**S.7.4 — 🔴 A silent false positive is the sweep's other failure mode, and it is quieter.**
`git rev-parse "$ref:path"` **prints the literal string** when the path is absent, so a naive
`sort -u` counts error strings as data. *One seat reported "9 distinct blobs" from exactly this.*
**Use `git cat-file -e` for existence and check the exit status, never the stdout.**

**S.7.5 — State the scope with the number.** "24" and "27" were both correct for one object on
2026-08-23, differing only by scope.

**S.7.6 — A measured value is a photograph and it decays** (body § 43). Every reported value names the
command that reproduces it **and stamps the instant it was run**, so a later reader who gets a
different number can tell whether the instrument moved or the repository did. *This rule failed
against its own author twice in one day: a coordinator told a reviewer two defects were "fixed" and
named a blob that contained neither, because "fixed" is a property of a blob and was asserted as a
property of a decision.*

**S.7.7 — 🔴 Say which CLASS a figure belongs to, because only one of the two decays.**

> **Re-measured independently during this integration, `2026-08-23T16:42:37Z`**, against figures
> stated roughly an hour earlier:
>
> | Class | Figure | Stated | Now |
> |---|---|---|---|
> | **population-derived** | refs carrying the approval queue | 30 of 52 | **31 of 53** |
> | **population-derived** | refs carrying the 6-line queue blob | 27 | **28** |
> | **population-derived** | union of tracked paths | 764 | **767** |
> | **object-derived** | distinct files in `governance/candidates/` | 28 | 28 |
> | **object-derived** | distinct files in `reviews/` | 74 | 74 |
> | **object-derived** | of those, `REV-*` basenames | 40 | 40 |

**Every figure derived from the REF POPULATION decayed. Every figure counting OBJECTS inside a
directory held.** Same cause in both columns — the paths this workstream itself added, on branches
that did not exist when the first sweep ran. New branches add refs, so population denominators move;
they added nothing under `governance/candidates/` and changed no `REV-*` basename, so object counts
did not.

**A reader who catches `27` reading `28` has no way to know which class they are looking at, and
therefore no way to know whether a CONCLUSION moved with it.** Label the class, and the mismatch
becomes interpretable instead of alarming.

🔴 **This settles the anxiety the decay otherwise creates across the whole document: the conclusions
that matter are population-independent.** Three queue lineages whatever the denominator. Zero
normative mentions of `governance/decisions/` whatever the ref count. Two distinct lease blobs
whatever the sweep. **That survival is stated here rather than left for a reader to work out.**

*Produced by a hostile-review seat that applied S.7.6 to its own report, found four of its eight
figures decayed, and said plainly that it had demanded of this document a discipline its own report
did not meet — a date with no time, and a command on two figures of fourteen, the two it had
self-excluded because it knew writing them down would falsify them. It is the second time in one day
that a seat produced its strongest rule out of its own defect.*

**S.7.8 — `VERDICT_TRANSFER: NONE` is the default.** A verdict carried from another record is not a
verdict.

## S.8 · 🟡 PROPOSAL (limb 2) · Escalation — a FLOOR, never a ceiling

**These ALWAYS reach the operator.** The list is a floor; it does not enumerate H.1's complement and
decides nothing about what is *not* the operator's.

1. A frozen rule would have to change.
2. An irreversible governance choice is required.
3. Two valid interpretations produce **materially different architectures**.
4. A body § 48 stop condition is live and cannot be discharged without a human.
5. Money would be spent (J.4 — `DEFAULT_EXTERNAL_SPEND = 0`).
6. An authority nobody currently holds would have to be allocated.
7. The act requires an ACTIVE lease and no lease is held.

> 🔴 **An earlier draft read *"only these"*, and that is a ceiling on human authority.** Worse, its
> exclusion list named *"seat designation for one mandate"* as a non-escalation, written in the same
> session as a seat designation the author had just performed. *The reviewer agreed the designation
> was right and objected that the convention must not be the instrument that clears it, because the
> next such act will cite the text and not the reasoning.* **Restated as a floor, which adds nothing
> to H.1 and removes nothing from it.**

**S.8.1 — An escalation is decision-shaped:** the decision in one sentence, the options, a
recommendation with its rationale, and what proceeds regardless. **A diagnostic report is not an
escalation.** A session with nothing to do while it waits has scoped its own work wrongly.

**S.8.2 — Anything decided under "minimal reversible, record the rationale, continue" is REPORTED to
the operator** — visible and reversible — rather than pre-cleared by this document as not their
business. That includes seat designation.

**S.8.3 — Work that is genuinely not an escalation, stated positively**, because a rule that only
says when to stop produces sessions that stop: building a mechanism that measures and reports ·
running any read-only command · selecting from an existing queue by an existing ranking · wiring a
check at INFO severity · `WORK_COMMIT` of your own named paths on your own branch · writing an
artifact that declares itself non-binding · file naming and migration mechanics · choosing between
two reversible options. **None of these is pre-cleared as outside the operator's interest — S.8.2
still reports them.**

## S.9 · Boundaries, and the no-relocation ruling restated

Confers nothing, activates nothing, registers nobody. Does not resolve seat ambiguity. Does not touch
`CONTROL_PLANE_ROOTS`, the four scientific current files, or any frozen text.

**The no-relocation ruling.** `reviews/` and `ledger/approvals/` do not move under `governance/`.
**The outcome is right; an earlier framing was overstated.**

- P5.1 does **not** forbid it. It makes it a *governed amendment*: declare `governance/reviews/` as a
  prefix and exclusion is restored — exclusion is a literal prefix match.
- The real cost is that the amendment would **falsify a load-bearing sentence**: *"all of
  `governance/` except `candidates/` are outside every root and always in the domain."* P5.1 already
  carries a 🔴 marker over a different load-bearing sentence falsified the same way.
- **Class: cost-and-fragility, not frozen-rule contradiction.**
- **Citation corrected.** What added `reviews/` is `CANDIDATE_HASH_VERSION: legend-candidate-v4`
  (P5 line 227). *"Revision 4"* at line 252 is the **manifest** revision — a different event.

## S.10 · 🔴 `runtime/` — the fixed point this layer refuses to create already exists

> **Measured, each number carrying its own noun.** `runtime/orchestrator_lease.md` is the only
> tracked path under `runtime/` at `main`. It matches no `CONTROL_PLANE_ROOT` prefix → **inside the
> content domain**. **2 distinct blobs** · **9 commits** touch the path · **23 refs** carry it.

**Two distinct blobs is already enough to move a hash, which is the whole point.** *An earlier draft
said "changed 9 times" — a commit count reported as a blob-change count, overstating mutability 4.5×,
in the section whose own rule forbids unearned numbers. Verified here by `git cat-file -e` for
existence and `rev-parse` only where the path was known present — S.7.4.*

A mutable I.3 record (`ACTIVATED_AT`, `LAST_RENEWED`, `EXPIRES_AT`, `RELEASED_AT`) inside the hashed
tree — the same shape S.9 declines to create for `reviews/`, one directory over, already real, and
already documented by P5.1's own 🔴 markers, which record that what prevents it is *"procedure, and
only procedure"*: declared `PROCEDURAL`, explicitly not `MECHANIZED`.

**What this convention does about it: nothing, deliberately, and it says so.** Owner: C-9 § 7.2.
Status: OPEN, held.

> **Rule.** Where this convention states a principle the repository does not yet satisfy, it names
> the violation, names its owner, and claims no completeness it has not earned.

## S.11 · The fingerprint recalibration needs no new governance — and does need a human gate

`plan_defined_parameters.md` is hashed **whole** in CORE, so a change to any delegated parameter moves
**every** role's fingerprint — while § P2.2 splits Annex J into four sections precisely to avoid that.

**Annex A.6 — FROZEN — anticipated this, named it, assigned detection and prescribed the remedy.**
Verbatim from `main`:

```
GUARANTEE:  … nessuna invalidazione inutile per modifiche non pertinenti
FAILURE:    (b) composizione del fingerprint mal calibrata: troppo larga → invalidazioni inutili
DETECTION:  (b) Mirror monitora il tasso di invalidazioni e i casi di ripresa poi contestati
RECOVERY:   (b) Plan ricalibra la composizione del fingerprint (modifica governata)
```

Every clause fired as written. The recalibration invents nothing.

> 🔴 **But it does NOT bypass the human gate.** Measured — `main:governance/plan_defined_parameters.md`
> line 11: `change_class: MAJOR — these values are governance; changing them follows gate 3`.
> GATE 3 is *Plan candidate → Mirror hostile review → MIRROR PASS → HUMAN_APPROVAL (oggetto in coda,
> J.3) → commit*. A.6's `modifica governata` **is** that path, not an exemption from it.
>
> ```
> Plan MAY      prepare the recalibration as a CAND, with its rationale
> Plan MAY NOT  perform it — GATE 3 ends in HUMAN_APPROVAL, and J.3/E4: APPROVAL ≠ AUTHORIZATION
> ```
>
> **This is exactly the failure Mirror is instructed to hunt: a frozen annex's name attached to an act
> that annex routes through a human gate.** The distinction that survives is narrow and real — *no NEW
> governance need be invented* — and that is a different sentence from *no operator decision*.

**Sequencing.** Recalibrate **before** any correction to `plan_defined_parameters.md`: after
recalibration the correction is non-pertinent for every role and the **19 of 19** checkpoints on
`main` carrying `APPLICABLE_GOVERNANCE_FINGERPRINT` are never invalidated. **But see P-6's dependency
row in § B.10 — the recalibration is fourth in the true order, not first, because it terminates in
two surfaces that do not yet work.**

**This is the pattern the whole convention follows.** The strongest moves are not new rules. They are
frozen provisions written, never mechanized, and now owed: § 43's `Working dir` column (S.2.1) and
A.6(b)'s recalibration here.

## S.12 · Owed elsewhere, recorded so it is not lost

**A recorded binding does not carry the rule version it was computed under.** Approvals bind
`CANDIDATE_CONTENT_HASH + BASE_HEAD`, and GATE 5 reads *"qualsiasi modifica materiale invalida le
approvazioni."* But the hash rule itself is versioned, and the queue does not record which version:

| Surface | carries `legend-candidate-v*` |
|---|---|
| `HUMAN_APPROVAL_QUEUE.jsonl` @ `main` | **0** |
| same @ `evidence-index` | **0** |
| same @ `orchestrator` | 3 |
| `CAND-*` manifests @ `main` | **8 of 8** |

One approved binding was reproduced under both rules — same base, same tip, **504 entries under
each**, different hash, single variable the version prefix. **A re-verifier cannot distinguish "the
rule moved" from "the content moved", and GATE 5 reads the second as approval-invalidating.** Owner:
the governance-surface decision package, as a J.3 schema question. Not this layer's.

---

# SECTION B — ARTIFACTS, LIFECYCLE, OWNERSHIP, HANDOFF, REVIEW, MIGRATION

## B.1 · Artifact classes and their taxonomy

### B.1.1 · The rule, in three clauses

```
1. PATH defines CLASS.
2. 🟡 PATH DECLARES DOMAIN.  The artifact TRANSCRIBES it; a disagreement between the transcription
   and the P5.1 prefix match is a FINDING, and the prefix match wins.
3. STATUS defines lifecycle validity, and PRESENCE OF AN ARTIFACT DOES NOT IMPLY AUTHORITY.
```

> 🟠 **INTEGRATION CORRECTION — clause 2 said the opposite, and the opposite was the lever.** It read
> *"CLASS declares DOMAIN, explicitly, in the artifact"*, while B.1.2 rows 6 and 7 said domain
> *"follows its root"*. **Those are different rules and the second is the true one** — P5.1 settles
> domain by literal prefix match, in its own prose: *"`learning/` is CONTENT — by intent, not by
> omission"*, *"a hostile review describes a candidate; it does not constitute one"*.
>
> The consequence of the wrong version, asked by the coordinator and answered by Mirror: **can an
> author change what is hashed by choosing a class? Yes — and without changing class.** Class 7
> (WORKING RECORD) names BOTH `learning/` (CONTENT) and `reviews/` (CONTROL PLANE), so an author
> decides whether a working record enters `CANDIDATE_CONTENT_HASH` by picking between two paths the
> same row permits.
>
> **Measured over the content population, this integration:**
> ```
> WORKING RECORD   learning/  85 paths   ·  reviews/  74 paths      → spans both domains
> HANDOFF          CONTENT     5 files   ·  CONTROL PLANE  7 files  → spans both domains
> ```
> Clause 2 restated above closes the lever by making the path the declarer. It is marked 🟡 under
> limb 2: no frozen rule says an artifact must transcribe its domain, so requiring the transcription
> is this layer deciding something P5.1 leaves open. **It moves no file and amends no P5.1.**

### B.1.2 · The classes that exist

| # | CLASS | WHAT IT IS | CANONICAL PATH | ID | DOMAIN (by path) | WRITER |
|---|---|---|---|---|---|---|
| 1 | **DEC** | an operator determination | `governance/decisions/DEC-<YYYYMMDD>-<SLUG>.md` | `DEC-` | CONTENT | operator |
| 2 | **CAND** | content proposed for canonical integration | `governance/candidates/CAND-<YYYYMMDD>-<SLUG>.md` | `CAND-` | CONTROL PLANE | plan (H.1) |
| 3 | **REVIEW** | a reviewer's judgement of a named object | `reviews/<ACTOR_ID>/REV-<OBJECT>-<REVIEWER>-<NNN>.md` | `REV-` | CONTROL PLANE | that reviewer, that directory |
| 4 | **APPROVAL** | a human resolution of a `HUMAN_REQUIRED` | `ledger/approvals/…` | `APR-` / `RES-` | CONTROL PLANE | 🔴 undeclared — B.3.2 |
| 5 | **PROPOSAL** | proposes a rule or model, not content for one candidate | 🔴 no correct home today | `PROPOSAL-` | 🔴 spans — P-1 | any actor |
| 6 | **HANDOFF** | transmits an artifact plus the determinations the sender is barred from making | author's own working root | `HANDOFF-` | 🔴 **spans: 5 CONTENT / 7 CONTROL PLANE** | the sender |
| 7 | **WORKING RECORD** | `PREP`, `ADVISORY`, `DELTA`, `PLAN-`, `SLR-`, `AUTHOR-RESPONSE` | `learning/<actor>/`, `reviews/<actor>/` | various | 🔴 **spans: 85 / 74 paths** | its author |

🔴 **Row 1 is declared and simultaneously escalated — see P-7.** Naming DEC here is the mechanism by
which it would acquire the appearance of authority, and this document is the strongest link in that
chain because it is CONTENT proposed for canonical integration. **P-7 escalates DEC's existence as a
class; this row records current practice and settles nothing.**

Classes 6 and 7 are not promoted to path-governed classes. They live beside their author's other
work, under one negative rule: *a working artifact never sits inside a class directory it does not
belong to.*

### B.1.3 · 🔴 The defect the taxonomy exists to fix — and it is three directories, not one

> 🟠 **INTEGRATION CORRECTION.** An earlier draft's headline said the defect *"is one directory"*
> while ratifying HANDOFF's five roots as conformant in the same section — so the passage written to
> end the container-vs-class conflation ratified it for two of seven classes. **Three sites: the
> candidates directory below, plus classes 6 and 7 spanning domains (B.1.1).**

Carried from the coordinator, attributed, and its one off-by-one repaired by measurement here:

> `governance/candidates/` at `main` holds **16 files: 8 `CAND-*` and 8 non-CAND** — `ADVISORY-FABLE-C9-001`,
> `APPROVAL-GOV311-DEVIATIONS`, `DELTA-20260817-P51C9-SPLIT`, `PROPOSAL-C9-STATE-MODEL`, and four
> `HANDOFF-*`. Because that path is a declared `CONTROL_PLANE_ROOT`, **all sixteen are excluded from
> `CANDIDATE_CONTENT_HASH` by location alone** — `candidate_content_hash.py --show-domain` → 535
> included, 45 excluded, the PROPOSAL and the APPROVAL among them.
>
> *The dispatch that supplied this said "7 CAND manifests". Measured at `main`: **8**, and the
> enumeration then sums to 16, matching its own "all sixteen". B.9 marks this row load-bearing,
> which is why the off-by-one mattered enough to re-measure.*

**An `ACCEPTED` proposal that suspends L2 across the laboratory is normative in effect and moves no
candidate hash.** The directory conflates *"describes a candidate"* with *"lives near candidates"*;
P5.1's exclusion is right for the first and wrong for the second.

Independently measured here over the content population:

| finding | count | detail |
|---|---|---|
| 🔴 `DEC-*` outside `governance/decisions/` | **3** | all in `governance/candidates/` |
| `DEC-*` correctly placed | 4 | — |
| 🔴 `APPROVAL-*` in `governance/candidates/` | **1** | `APPROVAL-GOV311-DEVIATIONS.md` |
| ✅ `REV-*` outside `reviews/` | **0 of 40** | REVIEW already holds by construction |
| 🔴 classes spanning both domains | **2 of 7** | HANDOFF, WORKING RECORD |

### B.1.4 · What the convention does about it — and what it refuses to do

```
DECLARED    PROPOSAL is a class. Its correct domain is CONTENT.
DECLARED    two classes span both domains, and the span is REPORTED, not resolved (Appendix D).
NOT DONE    no file is moved · CONTROL_PLANE_ROOTS is not amended · nothing is relocated (S.9)
            → PROPOSAL P-1
```

## B.2 · Lifecycle model — existing values, none invented

### B.2.1 · What is written today, read from `main`

| class | key | values observed |
|---|---|---|
| CAND | `state:` ×6, `status:` ×1 | `READY FOR MIRROR HOSTILE REVIEW` ×3 · `READY FOR MIRROR REVIEW (revision 6)` · `READY FOR MIRROR RE-REVIEW` · `APPROVED — …` · `PROPOSED — awaiting Mirror hostile review …` |
| DEC | `record_type:` + `status:` | `OPERATOR_DECISION` + `BINDING_AS_AN_OPERATOR_DETERMINATION_OF_STATE` |
| REVIEW | `verdict:` | `ACCEPT` ×7 · `REQUEST CHANGES` ×17 · `BINDING VERIFIED` ×2 · 🔴 absent ×13 (39 `REV-*`) |
| APPROVAL | `STATE` | J.3's five, plus `DEFERRED` ×2 and `RESOLVED` ×1 outside it |
| PROPOSAL | `status:` | `ACCEPTED` · `REVIEWED` |

### B.2.2 · 🔴 THERE ARE THREE VERDICT AXES, AND THE ONLY ONE A FROZEN GATE CONSUMES IS UNPOPULATED

> 🟠 **INTEGRATION CORRECTION — an earlier draft declared two axes and both gate nothing.**

```
1 DISPOSITION     frontmatter `verdict:` — ACCEPT | REQUEST CHANGES | BINDING VERIFIED
                  26 of 39 files; absent in 13.  Gates nothing normatively.
2 C.2 VERDICT     CONFIRMED | WEAKENED | REFINED | REFUTED — governed by Annex C.2.
                  Appears in review PROSE; ZERO frontmatter `verdict:` fields carry it.
3 MIRROR_REVIEW   🔴 n/a | PASS | FAIL + REVIEW_ID  —  annex_d_commit_batch.md line 38.
                  THE ONLY AXIS A FROZEN GATE READS: body GATE 3 requires "MIRROR PASS".
```

### B.2.2.1 · 🟠 INTEGRATION CORRECTION — the field is populated, and NOT in the frozen vocabulary

> **An earlier blob of this document asserted "0 of 39 `REV-*` files carry a `MIRROR_REVIEW` field."
> That negative was FALSE, and the defect was in my sweep: it read only the first 25 lines of each
> file, and the field is not always in the frontmatter.** Re-measured over whole files, anchored at
> `^ *MIRROR_REVIEW:`, 39 `REV-*` on `refs/heads/mirror`, **positive control `^ *(artifact|verdict):`
> → 39 of 39**:

```
MIRROR_REVIEW, field declarations          8 of 39 files      (object-derived)
  ACCEPT                3
  REVISION_REQUESTED    2
  REQUEST CHANGES       2
  PASS_WITH_NOTES       1
  ────────────────────────
  exact `PASS` or `FAIL`:   0    ← the frozen vocabulary at D.1 line 38 is: n/a | PASS | FAIL
```

**The accurate statement is neither "unpopulated" nor "populated consistently".** The field is
adopted in a **minority** of reviews — 8 of 39 — and **zero of those adoptions use the vocabulary the
frozen gate defines.** Partial adoption, zero conformance.

> 🟠 *A second figure is corrected in the same breath.* A peer reported **14** instances distributed
> `REQUEST CHANGES 7 · ACCEPT 4 · REVISION_REQUESTED 2 · PASS_WITH_NOTES 1`. Its **value set is
> exactly right** — the same four values, and no fifth exists on any content ref. Its **counts are
> inflated by an unanchored match**: `grep -i MIRROR_REVIEW` over the same 39 files returns 28 lines,
> of which **20 are prose mentions, not field declarations**. Anchoring the pattern to the field
> position is the difference. *Neither seat's number was right, both were wrong in opposite
> directions, and the conclusion below survives both.*

**🔴 The load-bearing fact survives every counting method: `PASS_WITH_NOTES` exists, and a canonical
commit's GATE 3 already rested on it.** `runtime/agent_card_registry.md` line 53 —
*"the `PASS_WITH_NOTES` that GATE 3 rested on is no longer stranded"*. And the question was already
registered before either seat looked: `REV-ORCHSURF-ADD-002-COMPLIANCE-VALIDATION` —
*"UNRESOLVED-A: may the corrected MIRROR_REVIEW carry a value outside D.2's vocabulary — routed by
DEC Decision 1 as a SCOPED_RULING for one field and one locus, explicitly non-generalizing. NOT
resolved by this record."*

**So this is not a gap to be declared. It is a live divergence between practice and a FROZEN
vocabulary, with a completed GATE 3 downstream of it and a pre-existing non-generalizing ruling
beside it.**

🔴 **No `ACCEPT → PASS` mapping is declared here, and the correction makes the refusal stronger, not
weaker.** Declaring one would define what satisfies a FROZEN gate — Mirror's method under G.2 —
**and it would retroactively characterise a canonical commit.** Consistent with P-5. The axis is
named, the divergence is measured, and the mapping is escalated. → **PROPOSAL P-8.**

### B.2.3 · The forward lifecycle rule

```
KEY          status:      one key, forward. `state:` is LEGACY on 6 CAND manifests, NOT retrofitted.
VALUE        a TOKEN — uppercase, underscore-joined, no spaces, no prose.
NOTE         everything after " — " on the same line is a NOTE; nothing may key off it.
REVIEW       three fields, none of them invented here:
               verdict:        ACCEPT | REQUEST_CHANGES | BINDING_VERIFIED    (disposition, observed)
               c2_verdict:     CONFIRMED | WEAKENED | REFINED | REFUTED       (Annex C.2)
               mirror_review:  n/a | PASS | FAIL  + REVIEW_ID                 (Annex D.1 — the gate)
             A review that omits `mirror_review:` cannot feed GATE 3, and one that fills it with a
             value outside `n/a | PASS | FAIL` has not fed it either — 8 of 39 fill it, 0 conform.
             Whether a disposition implies a PASS is NOT decided here — P-8, B.2.2.1.
APPROVAL     J.3's enumeration ONLY. DEFERRED and RESOLVED are preserved verbatim as LEGACY and
             NEVER normalised in a source line.
DEC          record_type: OPERATOR_DECISION plus a status token — recorded as practice, see P-7.
RECORD_TYPE  prefer `record_type:` (enumerated) over `artifact:` (free prose), forward only.
```

🔴 **Nothing in B.2.3 applies retroactively.**

## B.3 · Ownership — class-specific

Session ownership is S.2–S.3 and is not restated.

**B.3.1 — A class's writer is the writer named in B.1.2, and nobody else writes that path.**

**B.3.2 — 🔴 One class has no writer, and the convention may not allocate one.**
`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` has **no declared writer**: J.3 names a requester and a
resolver and allocates no file writer; § P7's one-writer decision covers `ledger/events/`. The file is
**forked into three lineages** — the 6-line blob on **28** refs including `main`, a 10-line blob on
`orchestrator`, a 14-line blob on `evidence-index` + `p51c9-rebased` — and **all four MAJOR approvals
are reachable from `refs/heads/orchestrator` and from no other ref.**

> **Figure class (S.7.7).** *Three lineages* and *four approvals on one ref* are **object-derived**
> and do not decay. *28 refs* is **population-derived**, measured `2026-08-23T16:42:37Z` — it read 27
> an hour earlier and will move again with the next branch. **The conclusion is
> population-independent: the fork exists at every denominator.**

Allocating a writer is a governance act (H.1). The convention declares the gap and stops.
→ **P-2, and it is first in the dependency order.**

## B.4 · Handoff and integration conventions

```
H-1  A HANDOFF BINDS BY BLOB, NOT BY BRANCH TIP.  Declare the object's blob id.
     Earned: a handoff bound a revision its own addendum had superseded.

H-1b 🟠 EXTENDED — the same hazard recurs where H-1 did not reach:
       · an INTEGRATION declares the blob of each source it consumed;
       · a REVIEW declares the blob it reviewed;
       · a CORRECTION REPORTED AS ACCEPTED names the blob it landed in.
     Earned twice more in one day: this file's own first integration consumed r1 while a reviewer
     was told two defects were fixed and given a blob containing neither — "fixed" is a property of
     a blob, asserted as a property of a decision (S.7.6). The frontmatter of this file carries the
     integration binding H-1b requires.

H-2  A PRODUCER EMITS NO VERDICT TOKEN.  C.2's vocabulary belongs to a REVIEWER reviewing an object;
     a producer's canonical equivalent is the ABSENCE of the field.
```

## B.5 · Review conventions

```
R-1  REVIEWS LIVE IN reviews/<REVIEWER ACTOR_ID>/.  True of 40 of 40. Codifies what holds.
R-2  REVIEWER ≠ AUTHOR.  A self-review emits an OBSERVATION, not a verdict.
R-3  THREE VERDICT AXES, DECLARED SEPARATELY — B.2.2. The gating one is `mirror_review:`.
R-4  AUTHOR_RESPONSE IS OWED AND TRACKED (C.2 — silence is not acceptance). One outstanding:
     REV-ROLES-MIRROR-001. It blocks the reviewed object's activation and nothing else.
R-5  BLIND REVIEW FOR INFRASTRUCTURE.  Earned: a blind reviewer found eight defects two informed
     reviewers had passed over twice.
R-6  A REVIEW RE-RUNS; IT DOES NOT RE-READ — S.7.8.
R-7  A REVIEWER DECLARES ITS CONFLICTS.  Where a review rests on evidence the reviewer itself
     produced, it says so and names the independent check. Earned: one Mirror seat did exactly this
     for § S.11, B.2.2 and parts of B.9.
```

## B.6 · Escalation

**The escalation floor is § S.8 and is not restated here.** One list, one place — two lists of
escalation conditions in one document is the drift failure this convention is about.

## B.7 · Migration — separated from activation

**The forward system is § S and § B. Nothing above applies retroactively.**

| # | item | count | act | blocked by |
|---|---|---|---|---|
| M-a | `DEC-*` in `governance/candidates/` | 3 | `git mv` | a DEC — and P-7 first: the class itself is escalated |
| M-b | `APPROVAL-*` in `governance/candidates/` | 1 | `git mv` | a DEC |
| M-c | `PROPOSAL-C9-STATE-MODEL.md` domain conflict | 1 | domain determination, then relocation | **P-1** |
| M-d | classes spanning both domains | 2 | report only (Appendix D); no file moves | nothing |
| M-e | CAND manifests using `state:` | 6 | key rename at next touch, never a sweep | nothing |
| M-f | `REV-*` with no `verdict:` field | 13 | the reviewer adds what it stated in prose | nothing |
| M-g | `REV-*` not conforming to D.1's `mirror_review:` vocabulary | **39 of 39** — 31 omit the field, 8 fill it with a non-vocabulary value | the reviewer adds or corrects it | **P-8** — and it cannot be a sweep: one such value already carried a canonical GATE 3 |
| M-h | artifacts carrying `session_ref:` | **0** | forward-only, never retrofitted | nothing |
| M-i | `runtime_inventory.md` on 1 ref, dated 2026-08-17 | 1 | mechanization — Appendix D | nothing |

🔴 **M-h is the honest headline.** No artifact carries a `session_ref` today. The attribution rule is
worth what future artifacts make it worth and repairs nothing that already happened.

## B.8 · Compatibility

### B.8.1 · What this document does not touch

```
P5.1's CONTROL_PLANE_ROOTS · the CANDIDATE_CONTENT_HASH rule · the fingerprint pertinence sets
(MEASURED: no framework/ path is in any of them) · the LINT and its gates · the receipt ledger and
its chain · Annexes A–J and the body (cited only) · roles/*.md (all four PROPOSED per DEC-20260822)
· the four scientific current files
```

### B.8.2 · 🔴 One compatibility claim that cannot be made

**The event ledger has never existed.** `ledger/events/` and `ledger/consolidated/` are on **0 refs**
of the content population (control: `ledger/approvals` present on 30). No clause reads it, writes it,
or assumes it. § B.2.3's tokens are shaped to sit inside J.1's event schema without translation.

### B.8.3 · Two known-stale surfaces, deliberately left alone

Under B.1.1 clause 3, **a stale status line is a finding, not a licence, and correcting one is an
ACTIVATION, which the mandate forbids.**

| surface | conditions | measured |
|---|---|---|
| `governance/plan_defined_parameters.md` (§ P7) | Mirror review passes · operator approves | `REV-P5DOMAIN-MIRROR-001` **ACCEPT** · `APR-20260819-P5DOMAIN-001` **APPROVED** · tip `ceefaa286115` ancestor of `main` |
| `framework/protocols/cross_session_transport.md` (§ 8) | canonical execution · Mirror ACCEPT · operator approval | `e839db383827` ancestor of `main` · `REV-XPORT-MIRROR-002` **ACCEPT** · `APR-20260819-XPORT-001` **APPROVED** |

🔴 **Neither correction is schedulable yet, and reading this table alone would suggest otherwise.**
The first requires P-6, which requires P-8 and P-2 first — see the dependency column in § B.10.

## B.9 · What this document assumes from elsewhere

**Figure class (S.7.7) is a column, because a load-bearing fact that is population-derived can move
without any conclusion moving — and one that is object-derived cannot move quietly at all.**

| fact | source | class | used in | load-bearing? |
|---|---|---|---|---|
| 16 files / 8 CAND / 8 non-CAND in `governance/candidates/`; 535 included, 45 excluded | coordinator; **count repaired by measurement here, 7→8** | object | B.1.3, P-1 | 🔴 **YES** |
| approval queue forked into 3 lineages; 4 MAJOR approvals reachable from `orchestrator` alone | coordinator | object | B.3.2, P-2 | 🔴 **YES** |
| `ledger/events/` on zero refs | coordinator; consistent with this seat's sweep | **population** | B.8.2 | 🔴 **YES** — but a zero survives every denominator |
| D.1 line 38 declares the `MIRROR_REVIEW` field, values `n/a` · `PASS` · `FAIL` + `REVIEW_ID` | Mirror → coordinator; **re-verified here at `main`** | object | B.2.2, P-8 | 🔴 **YES** |
| the field is filled in **8 of 39** `REV-*`, in 4 values, **0 of them `PASS` or `FAIL`**; `PASS_WITH_NOTES` carried a canonical GATE 3 | 🟠 **measured here after this seat's own false negative and a peer's inflated count — B.2.2.1** | object | B.2.2.1, M-g, P-8 | 🔴 **YES** |
| transcript birth vs `started` — 19h56m | orchestrator seat, two seats | object | S.1.4 | yes, for S.1.4 only; **S.1.5 is why the rule survives if it falls** |
| `cp -p` / `git archive` forge mtime | orchestrator seat, reproduced forward | object | S.4.2 | yes, for S.4 only |
| stash entry predates every current session; message says `superseded` | orchestrator seat | object | S.6.4 | yes, for S.6.4 only |
| approval-version gap; 504 entries under each rule | orchestrator seat | object | S.12 | no — routed elsewhere |
| lease: 2 blobs · 9 commits · 23 refs | mirror seat → coordinator; **re-verified here** | mixed | S.10 | no — corroborative; the *2 blobs* is the load-bearing half and is object-derived |
| `plan_defined_parameters.md` hashed whole in CORE | mirror seat → coordinator | object | S.11, B.8.3 | no — explanatory |

**Everything else was measured by the authoring seat with the command shown in the verification trail.**
One Mirror seat declared a C.3 conflict — § S.11, B.2.2 and parts of this table rest on evidence it
produced — and the other Mirror seat is the independent check on those (R-7).

## B.10 · PROPOSALS — the register, with its dependency order

**🔴 This is a dependency graph, not a menu.** *An earlier draft listed these as parallel rows, and a
reader of B.8.3 alone would have scheduled P-6 as available work. It is fourth.*

```
TRUE ORDER:   P-2  →  P-8  →  P-6  →  the B.8.3 status corrections
              (a writer for the queue) → (a token that feeds GATE 3) → (the recalibration)
Why: P-6 runs through GATE 3, which needs a MIRROR PASS nobody can currently emit (P-8), and
     terminates in HUMAN_APPROVAL "oggetto in coda, J.3" — the forked, writer-less queue (P-2).
```

| # | proposal | conflicts with | trips | **depends on** |
|---|---|---|---|---|
| **P-2** | declare ONE writer for `ledger/approvals/`. Recommended: per-actor `requests/<ACTOR_ID>.jsonl` + `resolutions/operator.jsonl`, consolidated by replay — the topology § P7 already chose, dissolving the fork by construction | J.3 allocates no file writer | S.8-6 | **nothing — this is the root** |
| **P-8** | **resolve the divergence between D.1's frozen `MIRROR_REVIEW` vocabulary and the values reviews actually emit.** Measured: filled in 8 of 39 `REV-*`, values `ACCEPT` 3 · `REVISION_REQUESTED` 2 · `REQUEST CHANGES` 2 · `PASS_WITH_NOTES` 1, and **0 exact `PASS` or `FAIL`**. It is not a fresh gap: `PASS_WITH_NOTES` **already carried a canonical GATE 3** (`agent_card_registry.md` line 53), and `REV-ORCHSURF-ADD-002-COMPLIANCE-VALIDATION` already registers `UNRESOLVED-A` — *"may the corrected MIRROR_REVIEW carry a value outside D.2's vocabulary"* — routed by a DEC as a **SCOPED_RULING for one field and one locus, explicitly non-generalizing**. Options: extend the vocabulary · declare a mapping · declare that no disposition implies PASS · generalize the scoped ruling | D.1 owns the field; C.2 and G.2 own review method; **and any mapping retroactively characterises a completed GATE 3** | S.8-1, S.8-2, S.8-3 | nothing — but it gates P-6 |
| **P-7** | **DEC is treated as a class with a path, domain and writer (B.1.2 row 1). Whether DEC is a governance object class at all — versus an instance of the J.3 queue object, which body § 4 names as the durable home of a HUMAN_REQUIRED, *"mai solo un messaggio"* — has no normative basis and is not decided here.** Measured: `OPERATOR_DECISION` 0, `governance/decisions` 0 in the 15-file normative corpus; controls 3 / 8 / 15 fire. Each DEC cites the previous DEC's *act* as its basis, and this document would be the next and strongest link — CONTENT, proposed for canonical integration. The domain is not free either: `governance/decisions/` is CONTENT, so **every DEC written moves the hash for every candidate rebased onto it**, while the three `DEC-*` in `governance/candidates/` move nothing | nothing frozen — the silence IS the finding (limb 2) | S.8-3 | nothing |
| **P-1** | PROPOSAL's correct domain is CONTENT: a root outside `governance/candidates/`, or amend `CONTROL_PLANE_ROOTS` | P5.1 declares the roots exhaustively | S.8-1, S.8-2 | nothing |
| **P-3** | recognise `DEFERRED` / `RESOLVED` as LEGACY in a derived view, never normalised in a source line | J.3's enumeration lacks them | S.8-1 | P-2 |
| **P-4** | relocate the 3 misplaced `DEC-*` and 1 `APPROVAL-*` (M-a, M-b) | moving a governance artifact is a governance act | S.8-1 | **P-7** — do not relocate a class whose existence is escalated |
| **P-5** | make the verdict fields required REVIEW frontmatter | C.2 owns review method; G.2 puts it beyond unilateral change | S.8-1 | P-8 |
| **P-6** | recalibrate `APPLICABLE_GOVERNANCE_FINGERPRINT` to hash `plan_defined_parameters.md` **by section** in CORE, as § P2.2 already does for Annex J. **Ordered by A.6 RECOVERY(b), assigned to Plan** | nothing — but `change_class: MAJOR` routes it through GATE 3, ending in HUMAN_APPROVAL | S.8-1 | **P-8, P-2** |

**None is performed by this document.**

## B.11 · What this document does not do

Does not amend, restate, activate or reinterpret any FROZEN object · does not touch
`plan_defined_parameters.md` or any fingerprint input · does not change a `status:` line anywhere ·
does not move, rename or delete any repository file · does not allocate a writer · does not declare
an `ACCEPT → PASS` mapping · does not open a `CAND`, write a `DEC` or create an `APPROVAL` · does not
write to `ledger/`, `runtime/` or `governance/` on any ref · does not activate a role contract · does
not confer or claim an ACTOR_ID · does not acquire a lease · does not wire anything into the LINT or
CI · does not build Appendix D · does not touch the untracked artifacts in this worktree · does not
advance `main`.

---

# APPENDIX D — MINIMAL PLUMBING, PROPOSED AND NOT BUILT

> **Deliverable 2.** Proposal-level by instruction. **Nothing here exists as code.**

## D.0 · What it is for — failures with measured costs

| # | failure | cost paid | function |
|---|---|---|---|
| 1 | an artifact appeared in a shared worktree; three sessions could not say whose | 4 cross-session messages, one retracted finding | DISCOVERY |
| 2 | bytes-at-risk reported as 337 kB (one seat); true figure 746 kB (two seats) | an operator decides differently at 337 than at 746 | DISCOVERY |
| 3 | 3 `DEC-*` and 1 `APPROVAL-*` excluded from the candidate hash by location alone | an `ACCEPTED` proposal imposing a live hold moves no hash | VALIDATION |
| 4 | 8 operator approvals invisible from `main` | approval state unreadable from the sovereign ref | INDEXING |
| 5 | **2 of 7 classes silently span both hash domains** | an author can change what is hashed without changing class | VALIDATION |

## D.1 · DISCOVERY — `framework/scripts/artifact_index.py`

```
DOES    walk declared roots (default working tree; --all-refs sweeps the content population),
        classify against § B.1.2, parse frontmatter, emit JSONL:
          path · class · id · domain_by_path · domain_transcribed · record_type · author ·
          session_ref · status_key · status_token · refs_carrying
NEVER   writes into the tree it scans · resolves an ambiguity · repairs a field
EXIT    0 always. Discovery reports; it does not judge.
```

🔴 **`--all-refs` is not optional** — `reading_state.md`'s own header: *"true of ONE checkout… a count
over unmerged state is a count of work that is not in the model."* A working-tree scan reported as a
laboratory figure is failure 2 exactly. **Every output states its population in the same sentence as
its counts (S.7.5), as a command result and never a literal (S.7.1).**
**Existence is tested with `git cat-file -e` and its exit status, never `rev-parse` stdout (S.7.4).**

## D.2 · VALIDATION — `framework/scripts/artifact_conventions.py`

```
CHECKS  1 PATH ⇄ CLASS
        2 DOMAIN: transcribed vs P5.1 prefix match — disagreement is a finding, prefix wins
        3 🔴 SPAN: a class whose instances land in both domains is REPORTED (N-1's cure)
        4 ATTRIBUTION (author, session_ref)
        5 LIFECYCLE token in the class enumeration, incl. `mirror_review:` presence on REVIEW
        6 LEGACY KEY (`state:` where `status:` is forward)
MODES   --report  default, exit 0        --strict  exit 1 — SHIPS UNWIRED
NEVER   edits · normalises a legacy value · moves anything
```

Check 3 is the whole of N-1's remedy: it **moves no file and amends no P5.1**, and turns an invisible
lever into a printed line.

**Why `--strict` ships unwired:** a gate switched on the same day as its first measurement blocks on
its own novelty. Report for one cycle, then wire it — one line, reverted by reverting that line.

**🔴 Parse the convention, never copy it.** The class table is parsed out of § B.1.2 at run time, by
column header. Precedent: `governance_fingerprint.py` parses § P2.2; `candidate_content_hash.py`
parses § P5 — *"if the prose stops parsing, this fails loudly instead of using a stale copy."* A guard
test asserts no module restates the table, in the shape of `test_record_conventions.py`'s test 2,
**which exists because five modules once held five private lists of one definition and the shortest
was wrong.**

## D.3 · INDEXING — a generated page

```
IS      derived. Header carries: "GENERATED by … — do not hand-edit", the population it covers IN
        THE SAME SENTENCE as its counts, and the instant of generation.
IS NOT  canonical · a second source of truth · an authority.  J.1: "lo stato repo resta sovrano".
```

## D.4 · ROUTING — and the line it must not cross

```
DOES    print, per open artifact: who owns the next act, whether it is blocked and by what, and
        whether it trips the § S.8 floor and is therefore the operator's
NEVER   assigns a task · writes a queue · sends a message · claims an artifact · changes a status
```

🔴 **Routing is derivation and printing. It is not dispatch.** `TASK_ASSIGNED` has exactly one
authorized writer under H.1 row 1 and nobody holds it — `lease_state.py` returns `ACTIVE by
derivation: 0`. A router that assigned work would allocate an authority nobody holds. **The router
answers *"whose act is this?"* — it never performs the act and never tells anyone to.**

## D.5 · The guard extension — mechanizing the judgeable part of S.6.3

Three denials added to the existing PreToolUse guard, each unambiguous and destructive with no undo:
bare `git stash` / `pop` / `drop`; `git reset --hard`; blanket `git clean -f` / `git checkout -- .` /
`git restore .`. Named paths stay allowed. **Branch switching is excluded by design**:
`git checkout <branch>` and `git checkout -- <path>` are indistinguishable by command string, and the
guard's own test file states the reason — *"a guard that blocks ordinary work gets disabled and then
guards nothing."* S.6.3 stands as convention for the whole list; mechanization covers the part a
machine can judge without misfiring.

## D.6 · Build order and the smallest useful subset

```
1 DISCOVERY   ~180 + 150 test   gated by § B.1.2 being stable enough to parse
2 VALIDATION  ~220 + 200 test   gated by 1, and by § B.2.3's enumerations
3 INDEXING    ~120 +  90 test   gated by 1
4 ROUTING     ~150 + 120 test   gated by 2, and by § S.8
5 GUARD       ~ 60 +  80 test   gated by nothing
```

**If only one thing is built: DISCOVERY.** ~330 lines with its test, writes nothing, needs no agreed
enumeration — only the class table — and eliminates failures 1 and 2 outright.

## D.7 · What Appendix D cannot claim

```
NO EVENT-LEDGER COMPATIBILITY — it has never existed (B.8.2)
NO NEW ROOT · NO CI GATE (--strict unwired) · NO GOVERNED WRITE · NO RETROFIT
```

---

## VERIFICATION TRAIL — this integration

> 🔴 **Every row carries its command, the INSTANT it was run, and its FIGURE CLASS (S.7.6, S.7.7).**
> *An earlier blob of this document printed "764 tracked paths across 52 refs" beside a command that
> already returned different values — the one place in a document where decay is not cosmetic, because
> the trail's only job is to let a reader re-run and get the same answer. The delta was this
> workstream's own footprint. A reader who now gets a different number can tell, from the class
> column, whether a conclusion moved with it.* **Population-derived rows are expected to move;
> object-derived rows are not, and a moved one is a real finding.**

**Sweep instant for every population-derived row below: `2026-08-23T16:42:37Z`.**

| # | claim | command | class | result |
|---|---|---|---|---|
| 1 | r2 not an ancestor of the prior integration | `git merge-base --is-ancestor ce2dc6e 1562ed6` | object | **NO** — r1 was all that existed |
| 2 | true UTC of the three commits | `date -u -r $(git show -s --format=%ct <c>)` | object | r1 `16:14:59Z` · integration `16:25:07Z` · r2 `16:27:14Z` |
| 3 | frozen Annex A owns A.6/A.7 | `git show main:governance/annex_a_task_contract.md` | object | `A.6 · CHECKPOINT` · `A.7 · RESUME IDEMPOTENTE`; **22 files at `main` cite A.6** |
| 4 | content population | `git for-each-ref --format='%(refname)' refs/heads refs/remotes refs/tags \| wc -l` | **population** | **53** = 44 + 4 + 5; 44th head is `legend-operating-convention-v1` |
| 5 | union of tracked paths | `git ls-tree -r` over every content ref, `sort -u` | **population** | **767** — read 764 an hour earlier; the delta is this workstream's own output |
| 6 | DEC normative basis | 15-file corpus sweep, line-fed, file count asserted `== 15` | object | `OPERATOR_DECISION` **0** · `governance/decisions` **0** · controls **3 / 8 / 15** fire |
| 7 | `MIRROR_REVIEW` field | `git show main:governance/annex_d_commit_batch.md` | object | **line 38** — `n/a \| PASS \| FAIL + REVIEW_ID`; GATE 3 at body line 244 requires MIRROR PASS |
| 8 | reviews filling it | whole-file sweep anchored at `^ *MIRROR_REVIEW:`, 39 `REV-*` on `refs/heads/mirror`, control `^ *(artifact\|verdict):` → **39/39** | object | **8 of 39** · `ACCEPT` 3 · `REVISION_REQUESTED` 2 · `REQUEST CHANGES` 2 · `PASS_WITH_NOTES` 1 · **exact `PASS`/`FAIL` 0**. 🟠 an earlier blob printed **0**, from a sweep scoped to the first 25 lines and run without a control |
| 9 | candidates directory | `git ls-tree --name-only main governance/candidates/` | object | **16 files · 8 CAND · 8 non-CAND** — the 7→8 repair |
| 10 | distinct files, `governance/candidates/` across refs | union sweep, `grep -c` | object | **28** — held across both sweeps |
| 11 | distinct files, `reviews/` · of those `REV-*` | union sweep | object | **74** · **40** — both held |
| 12 | class domain span | union sweep by root prefix | object | WORKING RECORD `learning/` **85** / `reviews/` **74** · HANDOFF **5 / 7** |
| 13 | refs carrying the approval queue | `git cat-file -e "$ref:<path>"`, exit status only | **population** | **31** — read 30 an hour earlier |
| 14 | lease | `cat-file -e` for existence; `rev-parse` only where present (S.7.4) | mixed | **2 blobs** (object) · **9 commits** (object) · **23 refs** (population) |
| 15 | review disposition vocabulary | `verdict:` of all 39 `REV-*` | object | `ACCEPT` 7 · `REQUEST CHANGES` 17 · `BINDING VERIFIED` 2 · absent 13 |
| 16 | does this file rotate a fingerprint? | `governance_fingerprint.py inputs --role <r>`, four roles | object | **NO** — no `framework/` path in any pertinence set |
| 17 | timestamp method | `date -u -r <epoch>` vs naive `stat -f '%Sm'` | object | true `15:20:37Z` vs naive `17:20:37Z` — S.4.1 confirmed |
| 18 | `main` | `git rev-parse main` | object | `788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5` — unchanged |

🔴 **Not one CONCLUSION in this document depends on a population-derived figure.** Three queue
lineages at any denominator. Zero normative mentions of `governance/decisions/` at any ref count. Two
distinct lease blobs at any sweep. Two classes spanning both domains at any population. **The
denominators decay; the findings do not.**

---

**Assembled by:** seat `plan`, session `evidence-index-58 [432290]`, worktree `evidence-index`,
branch `plan-orchsurf-r4-transcription`, 2026-08-23 — under the operator's Transition Execution
Mandate, routed by `OPCON-V1-PLAN-001/-002/-003`, integrating Section S from
`legend-operating-convention-v1:learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md` @ **ce2dc6e**.
**Not** under the authority of `roles/plan.md`, which is `PROPOSED` and not binding.
