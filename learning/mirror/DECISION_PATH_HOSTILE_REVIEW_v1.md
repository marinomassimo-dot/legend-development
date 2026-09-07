---
artifact: HOSTILE METHODOLOGICAL REVIEW — the path from decision preparation to a minimum
  decision path. Learning artefact only. Separates OBSERVATION, INFERENCE, LIMITATION and
  OPEN QUESTION, and emits nothing else
record_id: DECISION_PATH_HOSTILE_REVIEW_v1
date: 2026-08-24
dispatcher: operator
governance_version: 3.1.1 (read, not exercised) — 🔴 and see L-6: it has three fingerprints

actor_id: >
  🔴 NOT ESTABLISHED. This record is not authored under a role contract, and does not claim the
  Mirror seat. The dispatch instructed that ACTOR_ID, the Mirror role and the validity of a
  review floor must not be assumed. None is assumed. See § 1.

mode: ANALYSIS_ONLY

STATUS: READ_ONLY_METHODOLOGICAL_REVIEW
ACTIVATION: NOT_REQUESTED
APPROVAL: NOT_GRANTED
AUTHORITY_CLAIMED: none

classification:
  - NOT AN R4 VERDICT — and not a review at any Ladder level; see L-5
  - NOT A C.2 REVIEW — no VERDICT token of the C.2 enum is emitted anywhere in this file
  - NOT A DECISION, NOT A DEC, NOT A CAND, NOT AN APPROVAL
  - NOT A RECOMMENDATION — no option is selected, ranked or preferred
  - NOT A SCHEMA MODIFICATION, NOT A CANONICAL PATH DECLARATION
  - NOT A REPOSITORY MODIFICATION beyond this one file; see L-9 for why that sentence is
    narrower than it looks

domain: >
  🔴 CONTENT. `learning/` is not a CONTROL_PLANE_ROOT under § P5.1 at `main`
  (`legend-candidate-v4`: `governance/candidates/`, `ledger/`, `reviews/`) nor under § P5.1 on
  the branch this file is written on (`mirror`, `legend-candidate-v3`: `governance/candidates/`,
  `ledger/`). "Everything not under a declared root is content." This file is therefore in the
  candidate content domain on **both** readings — the one case on this surface where the P5 fork
  does not change the answer. It is untracked at the moment of writing. See L-9 and I-8.

verdict_note: >
  🔴 NO VERDICT TOKEN IS EMITTED, of any vocabulary. The dispatch forbids an R4 verdict; the C.2
  enum (CONFIRMED | WEAKENED | REFINED | REFUTED) attaches to a review of a claim id /
  CANDIDATE_CONTENT_HASH / directive id and none is under review here; and the document-level
  dispositions in circulation (ACCEPT, REQUEST CHANGES, PASS_WITH_NOTES, …) belong to no frozen
  enum at all — which is itself D-7. Emitting none is the only move that invents nothing.
---

# DECISION PATH — HOSTILE METHODOLOGICAL REVIEW

> **Nothing is decided. Nothing is selected. Nothing is reconciled. No object is approved,
> activated, ordered or scoped by this file.**
>
> The dispatch asked one question: *does the path let LEGEND evolve without incorporating
> authority accidentally?* The honest first answer is that **"the path" has no referent in this
> repository** (L-1). Everything below therefore does two things and says which is which: it
> measures what exists, and it reasons about the nearest objects that exist, naming them as *my*
> identification rather than as the dispatch's.

---

## 0 · MEASUREMENT SCOPE AND METHOD

```
OBSERVATION INSTANT   2026-08-24, this session
ACTING WORKTREE       .claude/worktrees/mirror
BRANCH                mirror        27673332e964732edd95d3f7644efd3a2408ead5
                      🔴 65 commits behind main · 83 ahead · merge-base 908197ba
CANONICAL main        788c357d9b7ca7afcbe7c1efc3a06b426cf7e2d5    OBSERVED, NOT MOVED
REF POPULATIONS       🔴 TWO, and every count below names which one it used:
                      · CONTENT population = 55 refs
                        git for-each-ref refs/heads refs/remotes refs/tags | grep -Ev '^refs/(codex|stash)'
                        Used for every ZERO in this file — L-1, L-3, O-D — because a negative
                        measured on the narrower set is a weaker claim than it reads as.
                      · LOCAL HEADS = 44 refs. Used where the claim is about branch state
                        rather than existence — O-F (queue fork), L-7 (contract status).
                      The content population was 52 on 2026-08-22 and 53 on 2026-08-23. Do not
                      copy 55 forward; re-run the command.
WORKING TREE          6 untracked paths, 0 tracked modifications, before this file
STATE MANIFEST        current_state: READY
LINT                  python3 framework/scripts/legend_lint.py .  →  VERDICT: PASS
```

**The normative corpus** for every "is this defined?" question below is the frozen governance
body, the ten annexes, `governance/plan_defined_parameters.md`, `framework/**`, `roles/**`,
`ARCHITECTURE.md`, `BOOTSTRAP.md`, `CLAUDE.md`. Nothing under `governance/candidates/`,
`governance/decisions/`, `reviews/`, `ledger/` or `learning/` is admitted as evidence that a
class exists — admitting an artefact as proof of its own authority is the circularity this
review is about.

**Every negative below carries a positive control measured in the same invocation**, and the
denominator is stated with the count. Two disclosures about the instrument itself:

🔴 **This session reproduced the recorded zsh ref-sweep fault, live.** A first pass measuring the
approval queue across refs was written `"$r:ledger/…"`; zsh applied the `:l` history modifier,
swallowed the `l`, and returned an unresolvable path for every ref. A second fault compounded it:
`git rev-parse` echoes its argument on stdout when it cannot resolve, so the `[ -n "$b" ]` guard
passed on the failures. Both were caught only because the output was visibly wrong. The measured
values in O-G come from the corrected form — `"${r}:path"` with `git rev-parse --verify -q` —
and were re-derived, not repaired.

🔴 **Recording a negative can falsify it.** Every "0 hits" below excludes this file. The two that
this file would otherwise break are given with their reproduction command:

```bash
# L-1a — cross-ref sweep. Population: the 55 CONTENT refs (heads+remotes+tags, less codex/stash),
#        not the 44 heads. Both are reported below because they are different claims.
REFS=$(git for-each-ref --format='%(refname)' refs/heads refs/remotes refs/tags \
       | grep -Ev '^refs/(codex|stash)')                                   # → 55 refs
echo "$REFS" | while IFS= read -r r; do
  git grep -l -iE "minimum decision path|decision preparation" "$r"; done          # → 0 hits
#   Control, same sweep, same 55 refs: "decision surface"
#   → 45 ref:path lines, which are 22 DISTINCT refs.  Over the 44 heads alone: 37 lines, 18 refs.
#
#   🔴 TWO instrument errors were made and corrected in producing this line, recorded rather
#      than silently fixed:
#      (i)  a first draft reported the control as "37 refs". It was 37 ref:path LINES over 18
#           refs. A line count is not a ref count when a ref carries the string in two files.
#      (ii) the first draft's control was swept over 44 heads while validating a claim later
#           widened to 55 refs. A control measured over a different population than the finding
#           validates nothing. Both are now measured over the same 55.

# L-1b — working tree, including untracked, this file excluded.  Population: 1 tree.
grep -ril "minimum decision path\|decision preparation" . --include="*.md" \
     --exclude=DECISION_PATH_HOSTILE_REVIEW_v1.md                                  # → 0 files
#   Control, same command form, same tree: "decision surface"                      # → 1 file
#   (a thin control — it proves the grep form resolves on this tree, nothing more)
```

---

# PART I · LIMITATION

*Recorded, not compensated. The dispatch instructed that a missing necessary condition be
registered rather than worked around. Each entry below states what is missing and then states
what I did* not *do about it.*

---

### L-1 · 🔴 The object of review has no repository referent

`minimum decision path` and `decision preparation` occur **zero times across the 55 content refs**
and across the working tree including untracked files, in any casing, and with no Italian
equivalent (`percorso decisionale`, `decisione minima`, `minimo percorso` → 0). `MDP` as a whole
word → 0. Controls, with their denominators, in § 0: `decision surface` → **22 of 55 content
refs** (45 ref:path lines), and 1 file in this working tree.

**Not compensated.** I did not select an artefact and proceed as though it were the dispatch's
object. Part III reasons about two artefacts I identify as the nearest existing referents, and
every inference that depends on that identification says so. If the identification is wrong, the
inferences that rest on it fall with it, and Part IV records that as OQ-1.

The two artefacts:

| Identified as | Object | Where | Date |
|---|---|---|---|
| "decision preparation" — enumerating what must be decided | `SCIENTIFIC-PIPELINE-PREPARATION-001` § 8 `HUMAN_TOUCHPOINT_MAP` (HT-1…HT-10) and § 9 open observations (O-1…O-8) | `main`, `learning/orchestrator/` | 2026-08-22 |
| "decision preparation" — second, later enumeration | `CLASS-DECISION-SURFACE-001` § 5 `REQUIRED DECISION PACKAGE` (D-1…D-8) | branch `mirror`, `reviews/mirror/`, **untracked** | 2026-08-23 |
| "minimum decision path" | 🔴 **no object** | — | — |

The phrase closest to it in the repository is § 5's own opening line — *"The minimum set of
unresolved decisions"* — which is a claim about a set, not a path. A set is unordered. A path is
ordered. The difference is exactly where the hidden decisions live (I-2).

### L-2 · 🔴 The dispatch's CURRENT STATE block is an unfilled placeholder

The dispatch's `# CURRENT STATE` section contains the literal string
`[STESSO BLOCCO DI CONTESTO SOPRA]` — "same context block above". No such block precedes it in
this session. The dispatch therefore declares a current state and supplies none.

**Not compensated.** I did not reconstruct a state from the repository and treat it as the state
the dispatcher meant. What Part II measures is the state I observed at the instant in § 0, and it
is labelled as mine.

### L-3 · 🔴 No ACTOR_ID, no assignment, no ACK, no claim

| Condition | Annex | Measured |
|---|---|---|
| `ACTOR_ID` established for this session | body § 19 (`ACTOR_ID` persistent, distinct from `SESSION_REF`) | **absent** — no registration record for this session exists |
| `TASK_ASSIGNMENT` | A.1 | **absent** |
| `TASK_ACK` — *"Nessun lavoro senza ACK"* | A.2 | **absent** |
| `TASK_CLAIM` — *"Assigned ≠ claimed … claim durevole prima di iniziare"* | A.3 | **absent** |

`ledger/tasks/mirror*` → **0 distinct paths across the 55 content refs**. Control, same sweep,
same population: `ledger/tasks/plan*` → **5 distinct paths**
(`C9-STATE-MODEL-001`, `GOV311-PLAN-REMEDIATION-001`, `P5DOMAIN-001`, `SCIENTIST-AB-SPEC-001`,
`XPORT-ROUTING-001`).

**Not compensated.** I did not write a claim, a checkpoint or a ledger event to manufacture the
missing precondition. The consequence is stated plainly in I-14: by A.2 and A.3, the work in this
file is unclaimed work, and nothing durable distinguishes it from a rehearsal.

### L-4 · 🔴 Lease state is UNDERIVABLE from this worktree

`runtime/orchestrator_lease.md` is **absent on branch `mirror`**; it is present on `main` and on
at least nine other heads. `framework/scripts/lease_state.py` is likewise absent here and present
on `main`. Executing `main`'s blob of the script against this worktree returns:

```
LEASE STATE UNDERIVABLE: cannot read runtime/orchestrator_lease.md
```

`runtime/runtime_inventory.md` exists on exactly **one** head (`orchestrator`) and not here.
Both antecedents of `CLAUDE.md` § 0 hold: no valid runtime inventory, no derivable ACTIVE lease.

**Not compensated.** I did not read the lease from another ref and report it as this session's
state. A lease read from a ref this session is not on measures that ref, not this session — and
which ref governs is itself D-3, undecided.

### L-5 · 🔴 No review floor is validated, and none can be

- **C.3**: *"Apertura solo via Orchestrator."* No opening artefact exists for this dispatch, on
  any ref. The dispatcher is the operator.
- **C.1**: the floor for *processo inferenziale methodology-changing* is **R4 METHOD (Mirror)**,
  and floors are *"derogabili solo verso l'ALTO; sotto il floor solo con rationale registrato."*
- **G.1**: `MIRROR_REQUIRED` is triggered by *protocolli/governance* and by *R4* — the class this
  object falls in.
- The dispatch forbids an R4 verdict.

So the object sits at a floor whose verdict the dispatch withholds, opened by a route C.3 does
not name.

**Not compensated.** I did not emit a lower-level verdict to fill the gap, and I did not record a
sub-floor rationale, because writing one would assert that a floor applies to this artefact —
which presupposes it is a Ladder review, which presupposes the opening C.3 requires. **This file
satisfies no Ladder floor and is not a Ladder review.** It is an analysis record.

### L-6 · 🔴 "Which governance is this running under" has three answers

`governance/scripts/governance_fingerprint.py compose --role mirror`:

| Where | Fingerprint |
|---|---|
| branch `mirror`, this worktree | `84d2b841b6081929e59d61e961e49077aca69c03136451d1000c72d902ef0738` |
| `main`, detached worktree, same script | `e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412` |
| `CHK-mirror-0008`, recorded 2026-08-19 | `3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c` |

Three distinct values for one role. § 48 lists *"riprendere lavoro su checkpoint incompatibile
(fingerprint/directive/generation mismatch)"* among the stop conditions.

**Not compensated.** I did not pick one and declare it authoritative. Every normative citation in
this file was read on branch `mirror` unless the text says `main`, and where the two differ
(§ P5.1) both values are given. Which one binds is D-3, and D-3 is open.

### L-7 · 🔴 The Mirror role contract is not binding, on any ref

`roles/mirror.md` line 7, byte-identical on `main` and on this branch and on 28 of 44 heads:

```
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
```

`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` (operator, H.1) selected **OPTION B —
`ACTIVATION_NOT_CONFIRMED`**, and its consequence 2 is directly binding on how this file may be
written: *"No actor authority may be assumed from these contracts. Any authority an actor
exercises must be traced to the governance body or to a named annex … never to a role contract
clause standing alone."*

**Not compensated.** Every rule cited in this file is cited from the body or a named annex.
`roles/mirror.md` is cited nowhere as the source of a rule.

### L-8 · 🔴 The branch this runs on carries a stale § P5

| | `CONTROL_PLANE_ROOTS` | Hash version |
|---|---|---|
| branch `mirror` | `governance/candidates/`, `ledger/` | `legend-candidate-v3` |
| `main` | `governance/candidates/`, `ledger/`, **`reviews/`** | `legend-candidate-v4` |

So `CLASS-DECISION-SURFACE-001` — one of the two artefacts this review reasons about — is
**control plane** if measured at `main` and **content** if measured on the branch it physically
sits on. That artefact's own frontmatter resolves this by declaring that every domain statement
in it is measured at `main`. See I-7: that declaration is not neutral.

### L-9 · 🔴 The dispatch's two output instructions are in tension, and I resolved it one way

The dispatch says *produce* `learning/mirror/DECISION_PATH_HOSTILE_REVIEW_v1.md` and, four lines
later, *do not produce* a `modifica repository`. Writing a file into a tracked repository's
working tree is a modification of that tree.

**Resolution taken, stated so it can be overridden:** I read "no repository modification" as *no
commit, no staging, no edit to any pre-existing file, no branch or ref movement* — and wrote
exactly one new untracked file, the one named. Nothing else in the tree changed. If the intended
reading was stricter, this file should not exist, and I could not have discovered that without
writing it.

The residue is not cosmetic: an untracked file is the surface no gate reads. `legend_lint.py`
does not read `learning/`; the release gate runs on what is committed; CI sees what is pushed.
This file is currently governed by nothing.

---

# PART II · OBSERVATION

*Mechanical facts, measured this session. No interpretation.*

---

### O-A · Three enumerations of what the operator must decide exist, and none references another

| Enumeration | Items | Artefact | Ref | Date |
|---|---|---|---|---|
| `HT-1 … HT-10` | 10 | `SCIENTIFIC-PIPELINE-PREPARATION-001` § 8.1 | `main` | 2026-08-22 |
| `O-1 … O-8` | 8 | same artefact, § 9 | `main` | 2026-08-22 |
| `D-1 … D-8` | 8 | `CLASS-DECISION-SURFACE-001` § 5 | `mirror`, untracked | 2026-08-23 |

Cross-references, measured:

```
CLASS-DECISION-SURFACE-001  →  "HT-[0-9]"        0 hits
CLASS-DECISION-SURFACE-001  →  "O-[1-8]"         0 hits
SCIENTIFIC-PIPELINE-PREP    →  "D-[1-8]"         6 hits, all incidental —
    CAND-20260818 (×3), CAND-20260819, PID-12, 2bb2700 context; zero refer to a D-item
```

The prep record predates the D-report by one day, so the second direction is chronologically
explicable. The first is not.

### O-B · § 5 asserts minimality; the structure of its own items qualifies it

- Header, verbatim: *"The minimum set of unresolved decisions."*
- 8 items · 34 options · **0 items offer an open-set escape** ("none of the above", "an option not
  listed here", "the question is malformed").
- **4 of 8** carry a dependency option in the closed set — `(d) subsumed by D-1` (D-5, D-6, D-8)
  and `(e) … a consequence of D-1/D-2 and not separately decidable` (D-3).
- Every item carries a `WHY IT CANNOT BE DEFERRED` block.
- § 5's own preamble states: *"These are not DECs and this section is not a decision package
  object."*

### O-C · J.0 declares that runtime authority enforcement is a guarantee LEGEND does not possess

| Guarantee absent | Compensating protocol |
|---|---|
| `RBAC enforced a runtime (attori interattivi)` | `authority matrix testuale + audit + event ledger (H.1, J.1)` |
| `Singleton garantito (compare-and-swap)` | `lease record + rilevazione doppio ACTIVE + stop condition (I.3)` |
| `Task checkout atomico (lock)` | `single-assigner + claim record + rilevazione conflitto (A.3)` |

And the closing rule of J.0, verbatim:

> *Vietato a qualsiasi documento o attore descrivere questi meccanismi con vocabolario più forte
> del protocollo compensativo.*

### O-D · The metrics named as the exclusive source of the next governance version do not exist as objects

G.3 names `AUTONOMY LEDGER`, `REVIEW YIELD` and `AUTO-METRICHE`, and closes:
*"Queste metriche sono la fonte esclusiva della futura v3.2 (freeze)."*

Distinct paths matching `autonomy`, over the enumerated trees of all **55 content refs**: **0**.
Control, same enumeration, same population: paths matching `checkpoint` → **28**. `review yield`
appears as *prose* in 15+ files; in no file as a measurement.

### O-E · No executable gate reads a governance or role `status:` field

`framework/scripts/legend_lint.py` contains **zero** references to `roles/` or `governance/`. Its
only status validation (`_check_ids_states`, line ~176) applies to `Status` fields inside CLAIM
and CANDIDATE blocks of the four scientific current files. LINT on this tree: `VERDICT: PASS`.

The instrument that would encode a richer status grammar — `PROPOSAL-C9-STATE-MODEL`, whose
four-field status form separates presence from force — is on hold, in its own words:
*"no implementation and no governance modification until that review completes; L2 suspended;
the status/C-8 batch frozen pending a later operator decision."*

### O-F · The approval queue is forked, re-measured independently this session

Distinct blobs of `ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` across **44 local heads**:

```
20c24a2ba478f08c27a97d985232b14aa306b08f    6 lines   25 heads  (incl. main, mirror)
bb603d9a270b312cf4eda832d73d1a15ec8de8e0   10 lines    1 head
95fc8163901459b4baeab2fa854aceaa2fd4c330   14 lines    2 heads
                                                      ── 28 of 44 heads carry the file
```

Control on the same loop: `roles/mirror.md` resolves on 28 of 44 heads. **Denominator note:** 44
local heads. `CLASS-DECISION-SURFACE-001` reports three blobs across "30 of 52 content refs" — a
different denominator (its sweep included remotes and tags). The three blob hashes agree; the
fractions are not comparable and neither is wrong.

### O-G · Both failure directions of "document vs state" are already realized

| Direction | Instance | Measured |
|---|---|---|
| Conditions **not** met, document installed and in practical use for six days | `roles/*` | `DEC-20260822` OPTION B; the only hostile review of those four objects returned CHANGES_REQUIRED on three, no verdict on the fourth |
| Conditions **all** met, document still reads `PROPOSED`, status line never once modified | `framework/protocols/scientist_reading_modes.md` | prep record § 3.3: three clauses each measured ✅ SATISFIED; `git log --all -S…` returns only the materialization commit |

### O-H · "Rehearsal" is a defined repository term, and it does not mean what the dispatch means

Two occurrences, both in `disease-models/wwox/analysis/`:

> *"A contaminated run is retained as a rehearsal but is void as independent evidence."*
> *"A run performed by an actor with retained knowledge of the first pass is a rehearsal, even if
> the filesystem is clean."*

Repository sense: **retained, but void as evidence.** The dispatch's sense — a rehearsal later
read as governed execution — has no term. The nearest instrument is § 38 L2:
*"Orchestrator → dry-run batch (snapshot + lint, senza commit; collauda GATE 0/2/4 e restore)"* —
and L2 is **SUSPENDED** by operator hold dated 2026-08-17, with all six declared capabilities
`UNVERIFIED`.

### O-I · The mark that distinguishes a rehearsal from an execution is currently self-written

- **A.3**: *"Assigned ≠ claimed. Dopo l'ACK, claim durevole prima di iniziare."*
- `lease_state.py`, quoted in the prep record § 8.2: *"Nothing compels the Orchestrator to record
  an acquisition, and nothing runs between turns."*
- **A.3 detection**: `CLAIM_CONFLICT` *"alla scrittura o alla riconciliazione di Plan"* — post hoc.
- The one existing mitigation is an actor's own note about itself. `CHK-mirror-0008`, verbatim:
  *"Operator-directed review (body §10.2 OBSERVE/ASK/STEER), not a Task Contract issued under
  H.1 — no ACTIVE lease was consulted and none is needed for a review. Recorded for provenance,
  not to assert that an assignment authority was exercised."*

### O-J · The governance already contains an ordered path, and it is frozen

§ 47 `BOOTSTRAP SEQUENCE (migration path corrente)` — 17 numbered steps. Step 13 is
*"L2 capability smoke (incl. verifica capabilities + dry-run batch + prova restore)"*; step 14 is
*"promozione: BOOTSTRAP_CONTROLLER → ACTIVE_ORCHESTRATOR (lease ACTIVE)"*; step 17 is
*"primo batch scientifico A/B/C — piccolo (§41)"*.

### O-K · The anti-overload instruments exist and are named

- § 48, closing sentence: *"Non bloccare su decisioni routinarie."*
- G.1: `NO_MIRROR (routine coperta da validator)`.
- G.3: *"yield nullo persistente → rituale → declassare."*
- § 10.2: OBSERVE/ASK *"sempre lecito, non cambia il task."*
- prep record § 8.2 enumerates eight checks that are *"mechanical, and should stay that way."*
- **Asymmetry, C.1 verbatim:** *"Derogabili solo verso l'ALTO; sotto il floor solo con rationale
  registrato."*

### O-L · APPROVAL ≠ AUTHORIZATION is already frozen doctrine

GATE 3, `[v3.1.1] E4`: *"l'HUMAN_APPROVAL autorizza l'intento, non bypassa i gate — l'esecuzione
approvata resta soggetta a GATE 0–5, stop conditions e authority matrix. Un MAJOR approvato con
root dirty resta NO BATCH."*

---

# PART III · INFERENCE

*Reasoning, not measurement. Each carries what would falsify it. None is a verdict, and none
selects an option.*

---

## 1 · Hidden decisions — does the path embed choices that belong to the operator?

### I-1 · Minimality is asserted and is not demonstrable by inspection of the set

§ 5 calls itself the minimum set. Minimality means no item is implied by another and no item is
removable. **Four of the eight items carry, inside their own option lists, the possibility that
they are subsumed** (O-B). A set in which half the members might be consequences of one other
member has not been shown minimal; whether it collapses is one of the questions in it.

Asserting minimality is a scope decision. It says *this is all of it*. Under H.1
(*Strategia complessiva → Operatore*), the scope of what must be decided is not a reviewer's to
fix. The report does not claim the authority — but the word "minimum" in a header does work that
the body never justifies, and a reader building a path from that header inherits the claim.

**What would falsify I-1:** a derivation showing pairwise independence of D-1…D-8, or an explicit
statement that "minimum" means "the fewest I found" rather than "the fewest there are".

### I-2 · Ordering is decided by prose, and ordering is where a set becomes a path

Every item carries `WHY IT CANNOT BE DEFERRED`. D-1's reads: *"Every subsequent question on this
surface is downstream of it … Deciding path before class produces a container that defines its own
contents."*

That is a correct-sounding argument, and it is also **an ordering decision made inside an
enumeration that declares it selects nothing**. The step from "here are eight questions" to "here
is the order to answer them" is precisely the step from *preparation* to *path* — and it is the
step the dispatch is asking about. It has already been taken, rhetorically, by eight
`CANNOT BE DEFERRED` blocks.

An operator who wanted D-5 first — to stop hash movement immediately, before deciding what a
`DEC` is — would be arguing against the document rather than choosing within it.

**What would falsify I-2:** a statement in the enumeration that the ordering is illustrative, or
the absence of ordering language in the items. Neither is present.

### I-3 · Closed option sets foreclose the solution space, quietly

34 options, 0 open-set escapes (O-B). The four dependency options are not escapes — they redirect
to another item *inside* the same set. There is no option anywhere that says *the question as
posed is the wrong question*, and no option that says *none of these*.

This is the mildest of the hidden-decision findings and the most mechanical: the shape of an
option list is itself a proposal about the answer, and a list with no exit reads as exhaustive
whether or not it is.

**What would falsify I-3:** an "other" option, or a preamble stating the lists are illustrative.

### I-4 · 🔴 Three unreconciled enumerations mean any path built on one silently decides the other two are not in it — the strongest finding in this review

O-A is the load-bearing measurement. Right now the repository contains three separate answers to
"what must the operator decide": HT-1…HT-10, O-1…O-8, D-1…D-8. **No artefact reconciles them, and
they do not cite one another.**

Concretely, and this is checkable: `HT-3` is *role contract activation*. It appears in **no**
D-item. `O-1` — `scientist_reading_modes.md`'s three activation clauses all measuring SATISFIED
while the status line reads `PROPOSED` — is an operator `STATE_DETERMINATION` of exactly the kind
`DEC-20260822` performed, and it appears **neither** in the `HUMAN_TOUCHPOINT_MAP` of its own
artefact **nor** anywhere in D-1…D-8. It is on one list, in the section explicitly labelled
"recorded, not resolved".

So a "minimum decision path" assembled from D-1…D-8 would omit role-contract activation and
protocol activation. A path assembled from HT-1…HT-10 would omit the entire decision-surface
question. **Whichever is chosen, the omission is a decision, and it is made by selection rather
than by anyone deciding it.**

**What would falsify I-4:** an artefact that maps the three enumerations onto each other, or a
demonstration that one strictly contains the others. 🔴 **Scope of what I actually measured:** the
cross-reference counts in O-A are greps *within* the two artefacts, not a sweep of the ref
population for a third, reconciling artefact. I did not run that sweep, and its absence is not
claimed. What is claimed is narrower and sufficient for the finding: neither of the two
enumerations references the other's items.

### I-5 · The two artefacts jointly imply that scientific work waits on governance, and that implication is nowhere stated as a decision

Prep record § 8.3, verbatim: *"The dispatch's goal — 'Scientist execution can start with minimal
human coordination' — is reachable **for the recurring set**, and only after the one-time set is
discharged by someone with the authority to discharge it."*

§ 47 places `primo batch scientifico` at step 17 of 17 (O-J).

Neither text says "no scientific reading until governance is settled". Together they entail it.
An entailment that nobody wrote down is the definition of an implicit decision — and this is the
one with the largest cost, because it is the decision to produce no evidence. It reappears from
the opposite direction as I-17.

**What would falsify I-5:** an explicit statement of which evidence-producing activity may proceed
while the one-time set is open. I found none.

---

## 2 · Governance by implementation — can building something amount to deciding it?

### I-6 · It has already happened, four times, and the enumeration says so about itself

D-1's own evidence: the first `DEC` *"proposes"* the convention; the second declares itself
*"a proposed convention exercised, not a legislated one"*; the directory did not exist on `main`
before the third. `record_type: OPERATOR_DECISION` and `governance/decisions/` have **zero**
normative mentions.

Four records now exist, are cited as precedent, and constitute the entire basis of a class that
has no definition. D-1 states this as the reason it cannot be deferred: *"each further one deepens
a practice basis for a class that has none."* The mechanism is not hypothetical and not future.

### I-7 · The enumeration must answer D-3 in order to state its own domain, and it does

`CLASS-DECISION-SURFACE-001` sits under `reviews/` on branch `mirror`. Under `mirror`'s § P5 it is
**content**; under `main`'s § P5 it is **control plane** (L-8). Its frontmatter resolves this:
*"Every domain statement in this report is measured at `main`, never at this branch."*

**Choosing the measurement ref is the operational content of D-3(a)** — *"`main` is authoritative"*
— which the same document lists as an open question with no option selected. The report discloses
the fork prominently (its § 2.5 is titled "THE SURFACE DEFINITION IS ITSELF FORKED") and this
inference does not accuse it of hiding anything. But **disclosure is not resolution**: the
artefact still had to act, acting required a ref, and the ref it picked is one of D-3's options.
An enumeration that must exercise one of its own open questions in order to exist is the purest
observable form of governance-by-implementation on this surface.

**What would falsify I-7:** a domain rule that does not depend on ref, or a demonstration that
both P5 readings give the same class for that path. On `learning/` they do (this file, see
frontmatter). On `reviews/` they do not.

### I-8 · This file reproduces the same defect, one directory over

`learning/` is content under both P5 readings. So producing this review moves the content-domain
tree of branch `mirror`, on a branch 83 commits ahead of `main` whose § P5 is stale. And it is
untracked, so no gate reads it (L-9). I state it here rather than only in the frontmatter because
a review that names this defect in another artefact and not in itself would be making the
argument it is refusing.

### I-9 · 🔴 No path can be described as *preventing* accidental authority — J.0 forbids the vocabulary

O-C is decisive here. `RBAC enforced a runtime` is a guarantee LEGEND **does not possess**. The
compensating protocol is *authority matrix textual + audit + event ledger*. And J.0 closes:
*"Vietato a qualsiasi documento o attore descrivere questi meccanismi con vocabolario più forte
del protocollo compensativo."*

Therefore:

- Nothing mechanically stops an actor from performing an act it lacks authority for.
- The only compensator is **post-hoc**: audit against a textual matrix, over an event ledger.
- The audit surfaces themselves are the objects D-2 (who may write the approval queue) and D-3
  (which ref is authoritative) leave undefined — and the queue is measurably forked three ways
  across 28 heads (O-F).
- The metrics G.3 names as the *exclusive* source of the next governance version are
  unmaterialized (O-D).

**The compensator for the missing guarantee is itself the thing under review.** That is not a
defect of the enumeration; it is the shape of the problem the enumeration is pointed at. But it
bounds what any answer can claim: an honest minimum decision path can promise **auditability**,
and may not promise **prevention**.

---

## 3 · State vs document — does the path distinguish present, approved and operative?

### I-10 · In prose, yes — and better than most systems manage

`DEC-20260822` is a sustained, explicit refusal to read installation as activation, argued in
seven numbered points, including a stated counter-argument (its ¶7) and a fail-closed resolution
(¶6). The prep record § 3.3 does the inverse case with equal care: it measures three activation
clauses as SATISFIED and then explicitly declines to rule, on the ground that the ruling belongs
to H.1. Both directions are handled, and handled well.

### I-11 · 🔴 In mechanism, nowhere

- No executable gate reads a `status:` field on any governance or role document (O-E).
- The instrument that would encode the distinction — `PROPOSAL-C9-STATE-MODEL`'s four-field status
  form — is accepted-but-not-adopted and explicitly held (O-E).
- `status: PROPOSED` in `roles/` has been **written twice and changed never**, across all refs.

So the three-way distinction is currently a property of **individual authors' discipline**, not a
property of the system. Every instance of it working is an instance of someone choosing to make
it work. That is exactly the class of guarantee J.0 says LEGEND does not have, and it degrades
silently: nothing fires when it stops happening.

### I-12 · Both drift directions are already realized simultaneously

O-G measures them: `roles/` is non-activated and in practical use; `scientist_reading_modes.md`
is fully-conditioned and marked non-binding. The system currently contains a document that binds
in practice while reading `PROPOSED`, and a document that reads `PROPOSED` while every clause
that would lift it measures satisfied.

The distinction between present, approved and operative is therefore not merely unmechanized —
it is **known to be wrong in two places, in opposite directions, at the same time**. A decision
path that inherits this without an explicit item for it inherits both errors.

**What would falsify I-11/I-12:** any gate, script or CI check that reads a `status:` field
outside the four scientific current files. I found none.

---

## 4 · Rehearsal risk — can a rehearsal later be read as governed execution?

### I-13 · The risk is real, and the mechanism is identifiable rather than speculative

Three facts compose it (O-H, O-I, L-3):

1. The repository has **no term** for "a run later read as governed execution". Its "rehearsal"
   means something else — retained, void as evidence — so the risk has no name to be caught by.
2. The only sanctioned rehearsal instrument (§ 38 L2 dry-run batch) is **suspended**. Rehearsals
   that occur therefore occur outside the only frame that would classify them.
3. The mark separating a rehearsal from an execution is a **claim record**, and A.3 plus
   `lease_state.py`'s own caveat establish that nothing compels one to be written and nothing
   runs between turns. Detection is at reconciliation, after the fact.

The existing mitigation is an actor writing a disclaimer about itself inside its own checkpoint
(O-I). That is self-attestation, and self-attestation is the exact failure mode that the
cross-session dispatch discipline in this laboratory already rejects on other grounds: the
receiving party proves identity by delivery, never by declaring it. A rehearsal marked as a
rehearsal only by its author is marked by the party with the motive.

### I-14 · 🔴 This session is a live instance, and I cannot exempt myself from the finding

No `TASK_ASSIGNMENT`, no `TASK_ACK`, no `TASK_CLAIM` (L-3). By A.2 — *"Nessun lavoro senza ACK"* —
the work in this file is unclaimed. If this artefact is later cited as a Mirror review of the
decision path, that transition will have occurred with **no durable object marking it**, and the
only text standing against it will be this file's own frontmatter — which is the self-attestation
I-13 just identified as insufficient.

I record this rather than solving it because solving it would mean writing the claim record whose
absence L-3 registers, and the dispatch forbade compensating for a missing condition.

### I-15 · The generalizable form

A rehearsal becomes an execution retroactively whenever three conditions coincide: the artefact
is durable, the artefact is citable, and no durable object records which mode produced it. All
three hold here, and all three hold for every artefact in the `learning/` and `reviews/` trees
produced under an operator-directed dispatch rather than a Task Contract. The count of such
artefacts is not small.

---

## 5 · Governance overload — does the path block activity that could produce evidence?

*Argued in the opposite direction, as the dispatch requires. This section is the steelman against
everything above.*

### I-16 · The instruments against overload exist, are named, and are frozen

O-K lists five. The system explicitly forbids blocking on routine decisions, explicitly provides a
`NO_MIRROR` class, explicitly requires downgrading a review level whose yield is persistently
zero, explicitly permits the operator to ask anything without changing a task, and explicitly
enumerates what must stay mechanical. This is a real defence and it should be credited.

### I-17 · 🔴 But the brake's measurement surface does not exist

C.1 permits derogation **upward freely** and downward **only with recorded rationale** (O-K).
The one instrument that pushes down is G.3's *"yield nullo persistente → rituale → declassare"*.
Its input is review yield per Ladder level, drawn from the autonomy ledger and the event ledger.

**No autonomy ledger object exists on any of the 55 content refs** (O-D, control at 28 checkpoint
paths over the same population).
So the escalation direction is frictionless and the de-escalation direction has no data. Over
time that is not neutral; it is a ratchet. And by G.3's own closing sentence, those same absent
metrics are *"la fonte esclusiva della futura v3.2"* — meaning the mechanism by which this
governance is supposed to evolve is currently unfed.

### I-18 · The concrete overload exposure

Nothing states which evidence-producing activity may proceed while D-1…D-8 are open (I-5), and
§ 47 places the first scientific batch at step 17 of 17 (O-J). Meanwhile the enumerations grow:
three of them now (O-A), the newest untracked and one day old.

The failure mode this points at is not that any single gate is wrong. It is that **the decision
surface is being enumerated faster than it is being decided**, each enumeration is itself an
artefact in the content domain that must then be classified, and no instrument measures the ratio.
G.3 is the instrument that would, and O-D says it has no object.

**What would falsify I-17/I-18:** an autonomy ledger or review-yield measurement anywhere in the
repository; or an explicit carve-out permitting scientific reading while the governance surface is
open. I found neither.

---

## 6 · The central question

> *Does the path allow LEGEND to evolve without incorporating authority accidentally?*

**As posed, not determinable: "the path" has no referent** (L-1). For the two artefacts I
identified as its nearest existing form, the reasoning above supports a bounded answer, offered as
inference and not as verdict:

**On disclosure — the strongest part.** Both artefacts refuse to convert analysis into authority,
in ways that are checkable rather than merely declared: `authority_claimed: none`, identity
established from repository evidence against the dispatch's own address (prep § 1), options
enumerated with none selected, a report that emits no verdict because no verdict vocabulary fits
its object. `DEC-20260822` refused an activation reading that would have been convenient for the
actors refusing it. These are not small things and no finding above weakens them.

**On prevention — not available, and not claimable.** J.0 removes the possibility (I-9). The
compensator is post-hoc audit; the audit surfaces are forked (O-F) and the audit metrics
unmaterialized (O-D). Any minimum decision path may therefore promise that accidental authority
will be *visible afterwards*, and may not promise it will be *stopped*. Language stronger than
that is forbidden by J.0's closing sentence, to any document, including this one.

**On the accident that is actually happening.** The measured route by which authority is being
incorporated is not a hidden clause. It is **selection**: three enumerations exist, none
references another (I-4), and building a path from any one of them decides that the others are out
of scope without anyone deciding it. That is the accidental authority this surface is currently
producing, and it is produced by the act of enumerating, not by any actor overreaching.

**On the symmetric risk.** The de-escalation instrument G.3 has no data (I-17) while the
escalation direction is frictionless (C.1). Both failure modes — too much governance and
accidental authority — are currently unmeasured, by the same missing object.

---

# PART IV · OPEN QUESTION

*For whoever holds the authority. Each states why it is not mine. No options are offered, because
an option list is itself a proposal (I-3) and this file has just finished arguing that.*

---

**OQ-1 — What is "the minimum decision path"?**
It has no referent on the 55 content refs (L-1). Part III reasons about
`SCIENTIFIC-PIPELINE-PREPARATION-001`
§§ 8–9 and `CLASS-DECISION-SURFACE-001` § 5 because I identified them as the nearest existing
objects. If that identification is wrong, every inference resting on it is void. *Belongs to the
dispatcher: only they know what was meant.*

**OQ-2 — Are HT-1…HT-10, O-1…O-8 and D-1…D-8 one enumeration or three?**
No artefact reconciles them (O-A, I-4). Until this is answered, every "minimum" claim over any one
of them is a claim about a set whose boundary is undecided. *Belongs to the operator under H.1
(Strategia complessiva); a reviewer choosing which list is the path would be choosing the scope.*

**OQ-3 — In what order, and is the order a decision or a property?**
Eight `WHY IT CANNOT BE DEFERRED` blocks have already answered this rhetorically (I-2). Whether
that ordering is binding, advisory, or an artefact of how the questions were found is unstated.
*Belongs to the operator: ordering the discharge of one's own decisions is not delegable to the
party enumerating them.*

**OQ-4 — Which evidence-producing activity may proceed while the governance surface is open?**
Nothing says. Two documents jointly imply "none" (I-5); § 47 puts the first batch last (O-J); the
opposite risk is unmeasured (I-17, I-18). *Belongs to the operator: it is a scope-and-priority
call, and it is the one with the largest cost either way.*

**OQ-5 — What durably distinguishes a rehearsal from a governed execution?**
Today: an actor's own note about itself (O-I, I-13). This session has no assignment, ACK or claim
and is producing a durable, citable artefact (I-14). *Belongs to whoever may issue a Task
Contract; I cannot write my own claim record without manufacturing the precondition L-3 records
as absent.*

**OQ-6 — Does anything read a `status:` field?**
No gate does (O-E). The distinction between present, approved and operative is author discipline,
and is currently wrong in two opposite directions at once (I-12). *Belongs to the operator:
`PROPOSAL-C9-STATE-MODEL` is the instrument and it is explicitly held pending an operator
decision.*

**OQ-7 — Where do the G.3 metrics live?**
`AUTONOMY LEDGER` has no object on any head (O-D), and G.3 names it as the exclusive source of
v3.2. Without it the only downward pressure on governance load has no input (I-17). *Belongs to
Plan for the schema and the operator for the governance; and expressly not to Mirror, because G.2
bars Mirror from self-approving material change to autonomy-classification or review-yield
methodology — which is what specifying the object would be.*

**OQ-8 — Under which governance is a review on a stale branch running?**
Three fingerprints for one role (L-6); § P5 forked (L-8); § 48 names fingerprint mismatch a stop
condition. *Belongs to the operator, and it is D-3 restated from the reviewer's side rather than
the artefact's.*

---

## 7 · WHAT THIS RECORD DOES NOT DO

- It emits **no verdict** — not R4, not a C.2 token, not a document-level disposition.
- It **selects no option**, ranks none, and recommends none, in any of the three enumerations.
- It **decides nothing** about `DEC` class, storage surface, writer, ref authority, enum validity,
  or domain — D-1…D-8 are as open after this file as before it.
- It **activates nothing**: no role contract, no protocol, no capability, no lease. It does not
  perform, schedule or specify the act `DEC-20260822` consequence 3 requires.
- It **claims no seat**: not Mirror, not any ACTOR_ID. Where the dispatch addressed a role, the
  address is recorded and not accepted (L-3, L-7).
- It **creates no** Task Contract, claim, checkpoint, ledger event, queue entry, candidate,
  review round, or handoff.
- It is **not an `AUTHOR_RESPONSE`** to anything, and does not discharge the outstanding one
  (`REV-ROLES-MIRROR-001`, still owed under C.2).
- It **reconciles nothing** between the three enumerations — I-4 identifies the gap and leaves it
  open as OQ-2, deliberately, because closing it is the scope decision the finding is about.
- It **modifies no existing file**, stages nothing, commits nothing, moves no ref. It adds exactly
  one untracked file, and L-9 records why that sentence is narrower than it sounds.
- It **is not a Ladder review** and satisfies no floor (L-5).
- It asserts **no prevention guarantee**, for itself or for any path, per J.0 (I-9).
