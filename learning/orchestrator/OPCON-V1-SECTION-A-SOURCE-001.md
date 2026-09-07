---
record_type: CONVENTION_SOURCE_INPUT
id: OPCON-V1-SECTION-S-SOURCE-001
title: Section S source — sessions, seats, dispatch, preservation, measurement
status: DRAFT INPUT r2 — revised under two hostile reviews. Handed to the Plan seat for
  integration into framework/protocols/legend_operating_convention_v1.md. NOT a competing artifact
  and NOT the convention itself. Plan holds structural-integration authority (H.1); one file has
  one writer; this is content offered to that author.
authoring_session: legend-public-54 [9fa760] · root checkout · session id 2277abdd-47f3-4124-aa03-76216861748d
reviewed_by:
  - mirror-75 [f3044e] — by message under ANALYSIS_ONLY; 2 BLOCKING, 1 non-blocking
  - mirror-87 [103de0] — reviews/mirror/REV-OPCONA-MIRROR-001.md, sha256 e6205f23ba1f9fe3…; 7 findings,
    4 marked SELF-INTERESTED by the reviewer under C.3 (AUTHOR ≠ REVIEWER)
  - evidence-index-86 [7483d0], evidence-index-61 [765ff9], mirror-1b [a85964], mirror-42 [6cb8b5]
    — targeted corrections by message
citation_namespace: >
  🔴 SECTIONS ARE `S.n`, NOT `A.n`. The first draft numbered them A.1–A.11 and collided head-on with
  FROZEN Annex A — where A.6 is CHECKPOINT (cited in 17 governance files at `main`) and A.7 is
  RESUME IDEMPOTENTE. Same tokens, different meanings, both normative in tone. Renumbered to `S`
  (sessions); annexes are A–J, so `S` cannot collide. Cite as `OPCON-v1 § S.6`, never bare `§ S.6`.
  Found by the plan seat, whose own dispatch forbade converting local labels into governed
  vocabulary.
governance_version: 3.1.1 — read from `main` via `git show`, never from a working tree
domain: CONTENT. Neither `learning/` nor `framework/protocols/` is a declared CONTROL_PLANE_ROOT
  (P5.1), so this file and its integration target are both inside CANDIDATE_CONTENT_HASH.
measured_at: main @ 788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5
activates_nothing: true
confers_nothing: true
---

# OPCON v1 — SECTION S · SESSIONS, SEATS, DISPATCH, PRESERVATION

> **A working layer, not governance.** Where this and a frozen normative file disagree, the frozen
> file wins and this document is the defect. Nothing here activates a role contract, confers an
> ACTOR_ID, grants authority, or reinterprets a frozen rule.

---

## 0 · The three layers

| Layer | Home | Who may change it | Changed by this document |
|---|---|---|---|
| **FROZEN NORMATIVE** | `governance/` — body (`status: FROZEN`), annexes A–J, `plan_defined_parameters.md`, `roles/` | Operator, through the governed path | **Nothing. Not one byte.** |
| **OPERATIONAL CONVENTION** | `framework/protocols/` — the established protocol home, which carries an index | Plan drafts · Mirror reviews · Operator ratifies | This *is* that layer |
| **IMPLEMENTATION MECHANISM** | `framework/scripts/`, `governance/scripts/`, `scripts/` | Any actor, own branch, reviewable | Only by proposal |

*A first draft gave Layer 2 the home `operations/`. That path was created and withdrawn in the same
session — `framework/protocols/` reuses what exists instead of adding a top-level root, which is
what "adapt to LEGEND, not redesign LEGEND" means. The table said `operations/` for an hour after
the withdrawal; `operations/` exists on 0 of 53 refs. Caught by a hostile-review seat.*

### 0.1 · The honesty test — two limbs, because one limb was blind

**Limb 1 — contradiction.** *If this rule were deleted, would anything become permitted that
governance forbids?* If yes, it is governance wearing a convention's clothes.

**Limb 2 — accretion into silence.** *Does this rule determine behaviour a frozen rule leaves
UNDER-DETERMINED?* If yes, mark it 🟡 **PROPOSAL** and name the silence.

> 🔴 **Limb 2 exists because limb 1 alone clears the exact failure this layer was built to prevent.**
> Run limb 1 on `governance/decisions/` at any point in its history: deleting *"operator decisions
> live here"* permits nothing governance forbids, because governance says nothing about them at all
> — 0 normative mentions, control `HUMAN_APPROVAL_QUEUE` → 3 in the same scope. **It passes at every
> step of becoming load-bearing**, up to and including four `DEC-*` records citing one another as
> precedent for a container with no basis. It also clears the operating law that accumulated in
> `CLAUDE.md` until 2026-08-16 — the precedent § 0 cites as its own justification.
> *Found by a hostile-review seat. A test that clears both instances of the failure it was written
> to prevent is aimed at the wrong axis.*

**Re-run under limb 2, three rules in this document fail and are marked 🟡 accordingly: S.2.2,
S.6.6, S.8.** None is wrong. Each decides something frozen text left open, and saying so is the
difference between a convention and a quiet amendment.

---

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

**S.1.2 — A session cannot resolve its own actorhood.** *"An actor choosing the reading that makes
itself an actor is the failure the gate exists to prevent"* — a mirror seat, near-verbatim. "None"
is a correct and useful answer.

**S.1.3 — A dispatcher verifies its addressee.** A session's row is the one its own peer list omits,
so the dispatcher derives it by set complement rather than accepting a self-report. *Some harness
builds print the session's own name, making the complement corroboration rather than necessity — but
the direction is what matters: it lets the DISPATCHER check the ADDRESSEE without taking its word.*

**S.1.4 — 🔴 `started` is not evidence about a conversation.** It is a property of the **runtime
incarnation**.

> **Measured, two seats.** A transcript with `birth = 2026-08-22T20:00:50Z` was still live on
> 2026-08-23 — a span of **19h56m** against a peer row reading *"started 6h ago."*

**The warrant, stated because § S.4.2 would otherwise dissolve it.** `cp -p` forges birthtime and
mtime, so a transcript's birth is exactly as forgeable as any file's. Two properties rescue it, and
neither is a timestamp: the file **grew** across successive readings (`1 603 926 → 1 612 311 B`) and
a copy does not grow; and it lives on a **harness-owned append-only path** keyed by session id.
*Honest limit: the growth was observed by one seat; the birth and span by two.*

**S.1.5 — The rule is fail-closed, so it does not depend on its own evidence being true.**
*"Elimination by start time is invalid"* withdraws a method that **CLEARS** a session. If the
measurement were wrong, the rule costs a discarded shortcut. If it were right and the rule absent, a
co-occupant is cleared on bad evidence and a `git clean` follows. Correct under both readings.
*Formulated by a reviewer who could not verify the measurement and said so.*

---

## S.2 · One writer per working directory

**S.2.1 — The field is already mandated; the gap is mechanization.** I first proposed adding a
`WORKING_DIRECTORY` field to the Agent Card as a governance change not to be performed. Unnecessary:

> Body **§43 · RUNTIME / AUTHORITY INVENTORY — VIVO**, minimum columns, verbatim:
> `… | SESSION_REF | Session ID | Agent ref | `**`Working dir`**` | Worktree | Branch | HEAD | …`
> `runtime/runtime_inventory.md` **exists** — 551 lines, `updated_on 2026-08-17T11:31:44Z`, four
> `Working dir` occurrences, on **1 ref of 53**.

Governance named the object, specified the field, and an artifact carrying it was materialized.
Nothing keeps it fresh, and §43's own sentence is *"riga stantia = non autoritativa"* — so every row
decays into non-authority by design. **The convention does not add a field. It fills one specified
and empty since 2026-08-17.**

**S.2.2 — 🟡 PROPOSAL (limb 2).** Seat occupancy is established by `(pwd, session id)`, nothing
weaker. *Silence named: no frozen rule says what establishes occupancy; §14 forbids two writers
without saying how one is identified.*

**S.2.3 — Occupancy is measured by polling, not inferred.** Ask every candidate for its `pwd`. This
converted suspicion to measurement in ten minutes on 2026-08-23.

**S.2.4 — Co-location is a hazard with zero conflicting writes.** Twelve untracked files across two
seats, three claimed; no session had overwritten another. **The exposure is not what happened — it
is that one `git clean` from any co-occupant destroys everything.** Never round co-location up to a
lost-attribution event that did not occur.

---

## S.3 · Attribution

| Rank | Evidence | Strength |
|---|---|---|
| 1 | Claim + an artefact independent of the claim | **sufficient** |
| 2 | Claim + disclaimers from every other polled occupant + an agreed digest | **sufficient to act on** |
| 3 | mtime inside a session window | **candidate set, never an author** |
| 4 | Elimination by `started` | **invalid — S.1.4** |

**S.3.0 — What rank 1's independent artefact can be for an UNCOMMITTED file.** A reviewer objected
that rank 1 is instantiable only for committed work — where git metadata settles it and the table is
unnecessary — leaving the top tier decorative exactly where it is needed. The objection was right
about the filesystem and wrong about the available objects. **The transcript's `tool_use` entries
are harness-written, carry real UTC, and are independent of any later claim:**

> A seat parsed its own transcript: 358 lines, three `Write`/`Edit` calls in the whole conversation,
> one into the repository, at `2026-08-22T20:22:44.653Z` — equal to the file's mtime **to the
> second**, from two objects with different authors.
> **Positive:** the write is bounded. **Negative, and sound:** three write calls total means that
> conversation wrote none of the other four records — a conclusion that survives even if every one
> of those files were copied into place afterwards.

*Rank 1 for uncommitted work therefore reads: the author's own transcript `tool_use` record. Rank 2
remains the practical ceiling when no transcript is available — which is itself a reason to commit
rather than to argue.*

**S.3.1 — A matching digest corroborates the OBJECT, never the AUTHOR.** It would be identical if
the claimant were lying.

**S.3.2 — "Unclaimed" states who has spoken. "Unknown-authored" is an inference.** Prefer the first.

**S.3.3 — Preservation does not depend on attribution.** Protect regardless of author.

**S.3.4 — Attribution discipline applies to this document's own citations.** A seat is not an
identity; four live sessions shared one. Where provenance is implied, name session + transcript
birth, or imply none. *This revision names sessions in its frontmatter for that reason; a reviewer
found the first draft citing "a mirror seat" with nothing a reader could check.*

---

## S.4 · 🔴 Timestamps

**S.4.1 — Forbid the class, not the instance, and name the real cause.**

> The cause is **hardcoding a literal `Z` into a renderer while the process timezone is unset** —
> the format string is exactly what cannot fix it. Measured on one file:
>
> ```
> epoch                          1787501665
> date -u -r        REFERENCE    2026-08-23T16:14:25Z
> stat -f '%Sm'  (no TZ)         2026-08-23T18:14:25Z   ← CEST wearing a Z it has not earned
> TZ=UTC stat -f '%Sm'           2026-08-23T16:14:25Z   ← correct
> ```

**Rule: derive from the raw epoch — `date -u -r <epoch>`.** If a renderer is used at all, `TZ=UTC`
is mandatory and a literal `Z` without it is a forgery. **The same trap lives in `%SB`, in `date -r`
without `-u`, and in `tar -tvf`** — all measured. *A blanket "never `stat -f '%Sm'`" over-reaches:
one seat produced every figure it sent with `TZ=UTC stat`, correctly, and a later auditor applying
a total ban would discard sound measurements. Three seats fell into the unset-TZ form within one
hour; two caught it before transmitting.*

**S.4.2 — Two ordinary operations forge timestamps, and both are what a careful person reaches for.**

| Operation | Forges | Why someone runs it |
|---|---|---|
| `cp -p` | source's mtime **and birthtime** | preserving files honestly before they are lost |
| `git archive \| tar` | every entry stamped with the **commit's** time | verifying a fingerprint honestly |

> **Reproduced forward on two commits.** Extraction at `2026-08-23T16:01:46Z` yielded
> `mtime = 2026-08-22T16:01:01Z` = `git show -s --format=%ct main`; the same test on a second commit
> tracked that commit's time. It follows the commit, never the clock.

**Consequence: any mechanism attributing work by mtime reads a field two routine operations
rewrite.** Timestamp-bracketing of authorship was proposed on 2026-08-23 and **withdrawn** for this
reason, before it was run.

---

## S.5 · Dispatch

**S.5.1 — A dispatch declares its authority basis and what it does not confer.** Which body section
or named annex it traces to — never a role contract standing alone (`DEC-20260822`) — and explicitly
that it confers no ACTOR_ID and activates nothing.

**S.5.2 — A dispatcher declares its own state so the receiver can discount it.** A receiver that
cannot discount its dispatcher cannot refuse a bad dispatch.

**S.5.3 — Seat designation is coordination, not conferral.** It names one writing seat per role for
one mandate, states measured rationale, stands others down **from writing**, and is revocable in one
line. *It is not authority: a peer cannot designate a seat, and two seats correctly declined to
treat mine as doing so — complying on the hazard instead. That is the right response and the
convention should expect it.*

**S.5.4 — A dispatch carries established facts with the command that reproduces them**, so the
receiver re-runs rather than trusts.

**S.5.5 — Read the RULE from the sovereign ref; read the OBJECT from its own tip.**
`git show main:<path>` for normative text. **But a candidate is defined by its branch tip and its
declared `BASE_HEAD`, not by `main`** — a reviewer who applies the rule to the reviewed object reads
a tree the candidate is not and reports on the wrong bytes. **State which you read for each.**
*The first form of this rule lacked the bound and would have converted one class of error into a
harder-to-see one, because the command looks canonical. Caught by a mirror seat within the hour.*

**S.5.6 — Corrections travel to the source, not into a footnote.** Ten of this session's assertions
were falsified by peers or by re-measurement and corrected before reaching the operator as fact.

---

## S.6 · Preservation

**S.6.1 — `WORK_COMMIT` of one's own named paths on one's own branch is the author's own authority**
(H.1). **A relay can neither forbid it nor license it.**

> 🔴 *Both halves were learned the hard way, in the same session. I issued a blanket "do not commit"
> and two seats objected that foreclosing a safe route by relay is a decision that was not mine —
> conceded. Then I wrote that committing was therefore "your call", and a seat objected that a
> convention authored by a peer cannot confer authority in the other direction either. Also
> conceded. **And a "stand down from writing" relay is itself that shape** — noted by a seat that had
> nothing to commit and raised it anyway.*
>
> **The symmetric rule: a peer relay changes what you KNOW about the hazard, never what you MAY do.**

**S.6.2 — Nobody commits another session's unfinished work.** `git add -A` is the mechanism; a named
path is the remedy.

**S.6.3 — Held as HAZARD, not authority:** `checkout · switch · reset · clean · stash · stash pop ·
add -A / add . · branch change · git rm · worktree remove/prune`. A prune sweep is destruction
wearing a maintenance hat.

**S.6.4 — 🔴 The stash stack is REPOSITORY-GLOBAL, and an entry's seat is not its owner.**

> **Measured.** One entry: `b688470f…`, created **2026-08-16 10:48:39 +0200** — seven days before
> any current session — message *"On evidence-index: PLAN base-alignment: **superseded**
> PMID42422765 worktree edit, preserved before rebase"*, contents one file, +2 −2, on a canonical
> deepdive manifest.

`pop` from any worktree takes it. **And it must not be reclaimed at all**: its own message says
`superseded`, so applying it would reintroduce a superseded edit into a canonical scientific
artifact. *I told a seat this entry was "yours, reclaim by apply". Wrong twice — not that session's,
and not to be reclaimed by anyone without an operator decision that it is still wanted. The seat
measured it and refused.*

**S.6.5 — An out-of-repository copy is declared or it does not exist.** Declared means: not a commit,
not durable, session-scoped, deletable, no transfer of the `WORK_COMMIT` act, and **never counted as
work preserved** — the originals remain the only record.

**S.6.6 — 🟡 PROPOSAL (limb 2). Redaction is owed before a branch is offered for integration.** A
file carrying a `public_release_gate.py` `DIRECT_IDENTIFIER` block must be redacted before the
branch it sits on is offered; a GATE 2 block is not cleared retroactively. *Stated first as
"redaction and commit are one act", which would have forbidden a `WORK_COMMIT` that S.6.1 declares
the author's own and that GATE 2 does not reach. Silence named: no frozen rule sequences redaction
against `WORK_COMMIT`. Grounded in the public edition's privacy design, not invented here.*

---

## S.7 · Measurement

**S.7.1 — 🔴 Mandate the COMMAND, never the integer.**

```bash
git for-each-ref --format='%(refname)' refs/heads refs/remotes refs/tags | wc -l
# excludes refs/codex/turn-diffs/* and refs/stash as non-content
```

> **The first draft hardcoded "52 refs (43 heads + 4 remotes + 5 tags)". It was already false.**
> Value at `2026-08-23T16:23:30Z`: **53** = 44 + 4 + 5. **The 44th head is
> `legend-operating-convention-v1` — the branch this document is written on. The act of drafting the
> rule falsified the constant the rule stated**, and it will re-falsify with every branch any seat
> opens. Found independently by two seats within minutes.

That contradicted S.7.5 four lines below it. The rule *"sweep the declared population, not the
convenient one"* survives intact and gets stronger by not depending on a literal.

**S.7.2 — Every sweep carries a positive control, and the control must be able to fail.**

**S.7.3 — 🔴 A control that shares the flaw of the search cannot detect it.** It proves the
instrument works; it cannot prove it is aimed correctly. *Produced by a seat that searched the wrong
root, ran its control inside that same wrong root, watched it pass, and reported a false negative.*

**S.7.4 — A silent false positive is the sweep's other failure mode, and it is quieter.**
`git rev-parse "$ref:path"` **prints the literal string** when the path is absent, so a naive
`sort -u` counts 30 error strings as data. *I reported "9 distinct blobs" from exactly this. Use
`git cat-file -e` for existence and check the exit status, never the stdout.*

**S.7.5 — State the scope with the number.** "24" and "27" were both correct for one object on
2026-08-23, differing only by scope.

**S.7.6 — A measured value is a photograph and it decays** (body §43). Every reported value names
the command that reproduces it **and stamps the instant it was run**, so a later reader who gets a
different number can tell whether the instrument moved or the repository did.

**S.7.7 — 🔴 Say which CLASS a figure belongs to, because only one of the two decays.**

> **Measured twice, an hour apart, across the same refs.**
>
> | Class | Figure | Stated | Now |
> |---|---|---|---|
> | **population-derived** | refs carrying the approval queue | 30 of 52 | **31 of 53** |
> | **population-derived** | refs carrying the 6-line queue blob | 27 | **28** |
> | **object-derived** | distinct files in `governance/candidates/` | 28 | 28 |
> | **object-derived** | distinct files in `reviews/` | 74 | 74 |
> | **object-derived** | of those, `REV-*` basenames | 40 | 40 |

**Every figure derived from the REF POPULATION decayed. Every figure counting OBJECTS inside a
directory held.** The cause is the same fifteen paths in both cases — this workstream's own output,
on branches that did not exist when the first sweep ran. New branches add refs, so population
denominators move; they added nothing under `governance/candidates/` and changed no `REV-*`
basename, so object counts did not.

**A reader who catches `27` reading `28` has no way to know which class they are looking at, and
therefore no way to know whether a conclusion moved with it.** Label the class, and the mismatch
becomes interpretable instead of alarming.

*Produced by a hostile-review seat that applied § S.7.6 to its own report, found four of its eight
figures decayed, and said plainly that it had demanded of this document a discipline its own § 0 did
not meet — a date with no time, and a command on two figures of fourteen, the two it had
self-excluded because it knew writing them would falsify them. Its conclusions survived because they
are population-independent: three queue lineages whatever the denominator, zero normative mentions
whatever the ref count, two lease blobs whatever the sweep. **That survival is worth stating rather
than assuming**, which is the whole of this rule.*

---

## S.8 · 🟡 PROPOSAL (limb 2) · Escalation — stated as a FLOOR, never a ceiling

**These ALWAYS reach the operator:**

1. A frozen rule would have to change.
2. An irreversible governance choice is required.
3. Two valid interpretations produce materially different architectures.
4. A body §48 stop condition is live and cannot be discharged without a human.

> 🔴 **The first draft read *"only these"*, and that is a ceiling on human authority.** By
> enumerating H.1's complement it decided what is *not* the operator's — contradicting nothing, so
> limb 1 cleared it. **Worse, its exclusion list named "seat designation for one mandate" as a
> non-escalation, written in the same session as the seat designation I had just performed.** The
> reviewer who raised it agreed the designation was right and objected that *the convention must not
> be the instrument that clears it, because the next such act will cite the text and not the
> reasoning.* Restated as a floor, which adds nothing to H.1 and removes nothing from it.

**S.8.1 — An escalation is decision-shaped:** the decision, the options, a recommendation with
rationale, and what proceeds regardless. A diagnostic report is not an escalation.

**S.8.2 — Seat designation, and anything else decided under "minimal reversible, record the
rationale, continue", is REPORTED to the operator in the escalation channel** — visible and
reversible — rather than pre-cleared by this document as not their business.

---

## S.9 · Boundaries of this section

Confers nothing, activates nothing, registers nobody. Does not resolve seat ambiguity. Does not
touch `CONTROL_PLANE_ROOTS`, the four scientific current files, or any frozen text.

### S.9.1 · The no-relocation ruling, restated

I ruled that `reviews/` and `ledger/approvals/` must not move under `governance/`, and called the
alternative a frozen-rule contradiction. **The outcome is right; the framing was overstated.**

- P5.1 does **not** forbid it. It makes it a *governed amendment*: declare `governance/reviews/` as
  a prefix and exclusion is restored — exclusion is a literal prefix match.
- The real cost is that the amendment would **falsify a load-bearing sentence**: *"all of
  `governance/` except `candidates/` are outside every root and always in the domain."* P5.1 already
  carries a 🔴 marker over a different load-bearing sentence falsified the same way.
- **Class: cost-and-fragility, not frozen-rule contradiction.** Sent up as *forbidden*, the ruling
  looks overstated to anyone who then opens P5.1.
- **Citation corrected.** What added `reviews/` is `CANDIDATE_HASH_VERSION: legend-candidate-v4`
  (P5 line 227). *"Revision 4"* at line 252 is the **manifest** revision — a different event that
  explicitly left the checkpoint hazard standing. *Measured 2026-08-23 by
  `git show <ref>:governance/plan_defined_parameters.md`; a seat that first cited a commit message
  for it re-measured and corrected its own provenance.*

---

## S.10 · 🔴 `runtime/` — the fixed point this layer refuses to create already exists

> **Measured, with each number carrying its own noun.**
> `runtime/orchestrator_lease.md` is the **only** tracked path under `runtime/` at `main`.
> It matches no `CONTROL_PLANE_ROOT` prefix → it is **inside the content domain**.
> **2 distinct blobs** across 53 refs · **9 commits** touch the path · **23 refs** carry it.

Two distinct blobs is already enough to move a hash, which is the whole point. *The first draft said
"changed 9 times" — a commit count reported as a blob-change count, overstating mutability 4.5×, in
the section whose own rule forbids unearned numbers. Caught by the seat that supplied the finding,
which said that if it went up overstated it would be its own defect travelling under my name.*

A mutable I.3 record (`ACTIVATED_AT`, `LAST_RENEWED`, `EXPIRES_AT`, `RELEASED_AT`) inside the hashed
tree — the same shape S.9.1 declines to create for `reviews/`, one directory over, already real, and
already documented by P5.1's own 🔴 markers, which record that what prevents it is *"procedure, and
only procedure"*: declared `PROCEDURAL`, explicitly not `MECHANIZED`.

**What this convention does about it: nothing, deliberately, and it says so.** `runtime/` is a
registered OPEN CLASSIFICATION QUESTION routed to C-9 §7.2, whose `hold` forbids resolving it, and
P5.1 states a fourth root *"would treat a container as a class"*.

> **Rule.** Where this convention states a principle the repository does not yet satisfy, it names
> the violation, names its owner, and claims no completeness it has not earned.

Owner: C-9 §7.2. Status: OPEN, held. Not this layer's to close.

---

## S.11 · The fingerprint recalibration needs no new governance

`plan_defined_parameters.md` is hashed **whole** in CORE, so a change to any delegated parameter
moves **every** role's fingerprint — while § P2.2 splits Annex J into four sections precisely to
avoid that, and says so in its own prose.

**Annex A.6 — FROZEN — anticipated this, named it, assigned detection and prescribed the remedy.**
Verbatim from `main`:

```
GUARANTEE:  … nessuna invalidazione inutile per modifiche non pertinenti
FAILURE:    (b) composizione del fingerprint mal calibrata: troppo larga → invalidazioni inutili,
                troppo stretta → ripresa sotto regole cambiate
DETECTION:  (b) Mirror monitora il tasso di invalidazioni e i casi di ripresa poi contestati
RECOVERY:   (b) Plan ricalibra la composizione del fingerprint (modifica governata)
```

Every clause fired as written: the composition **is** too broad; **Mirror detected it, unprompted**;
the recovery is **Plan's, as a governed change**. The recalibration therefore invents nothing.

> 🔴 **But it does NOT bypass the human gate, and I said it did.** I wrote that it *"consumes no
> operator decision."* False, and the Plan seat caught it by reading the frontmatter of the file the
> recalibration would edit:
>
> ```
> main:governance/plan_defined_parameters.md, line 11
> change_class: MAJOR — these values are governance; changing them follows gate 3
> ```
>
> A.6's *`modifica governata`* **is** GATE 3 — Plan candidate → Mirror hostile review → MIRROR PASS
> → HUMAN_APPROVAL → commit — not an exemption from it. So Plan **may prepare** the recalibration as
> a candidate with its rationale; Plan **may not perform** it.
>
> **This is exactly the failure Mirror is instructed to hunt: a frozen annex's name attached to an
> act that annex routes through a human gate.** I attached it. The distinction that survives is
> narrow and real — *no NEW governance need be invented*, because A.6(b) already prescribes the
> remedy and H.1 already assigns it — and that is a different sentence from *no operator decision*.

**Sequencing, and it inverts an order.** Recalibrate **before** any correction to
`plan_defined_parameters.md`. After recalibration the correction is non-pertinent for every role and
the **19 of 19** checkpoints on `main` carrying `APPLICABLE_GOVERNANCE_FINGERPRINT` are never
invalidated. Done in the other order it is paid for nothing — and A.6's rejection rule routes every
stale rehydration to *ask an Orchestrator*, of which **zero** hold an ACTIVE lease.

**This is the pattern the whole convention should follow.** The strongest moves are not new rules.
They are frozen provisions written, never mechanized, and now owed: §43's `Working dir` column
(S.2.1), and A.6(b)'s recalibration here.

---

## S.12 · Owed elsewhere, recorded so it is not lost

**S.12.1 — A recorded binding does not carry the rule version it was computed under.** Approvals
bind `CANDIDATE_CONTENT_HASH + BASE_HEAD`, and GATE 5 reads *"qualsiasi modifica materiale invalida
le approvazioni."* But the hash rule itself is versioned, and:

| Surface | Carries `legend-candidate-v*` |
|---|---|
| `HUMAN_APPROVAL_QUEUE.jsonl` @ `main` | **0** |
| same @ `evidence-index` | **0** |
| same @ `orchestrator` | 3 |
| `CAND-*` manifests @ `main` | **8 of 8** |

A seat reproduced one approved binding under both rules — same base, same tip, **504 entries under
each**, different hash, single variable the version prefix. So a re-verifier cannot distinguish *"the
rule moved"* from *"the content moved"*, and GATE 5 reads the second as approval-invalidating.
**The object GATE 5 binds is the one missing the field needed to reproduce the binding.**
Owner: the governance-surface decision package, as a J.3 schema question. **Not a repair, and not
this layer's.**

---

## S.13 · Under review

Every rule above. Two hostile reviews found **two blocking defects** — both unearned numbers in
sections whose own rules forbid them — plus the § 0.1 blindness, the S.8 ceiling, the S.5.5 missing
bound, and the S.7.4 silent false positive. All are fixed above. **§ S.1.4's transcript measurement
remains the one load-bearing fact a reviewer declined to verify**, on the correct ground that it
requires reading another session's transcript; S.1.5 is why the rule survives that refusal.

**Owed to § B, not defects here:** whether an author can change what is hashed by choosing a class
(the general lever; S.10 is one instance) · container-vs-class in general · status/path separation,
which § S does not address at all · who maintains `(pwd, session id)` — §43's unmechanized column
again.
