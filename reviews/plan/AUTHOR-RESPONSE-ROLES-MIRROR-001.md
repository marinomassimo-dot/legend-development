---
artifact: AUTHOR_RESPONSE (Annex C.2) — REV-ROLES-MIRROR-001
review: reviews/mirror/REV-ROLES-MIRROR-001.md
review_ref: refs/heads/mirror @ 1350477 — blob daec4e8a91dfb3c8da66d48a620e23f22724e1d4
  sha-256 53b47b248adf6dc449c032435c198ac3eec3daee57ce83e6ec0d5b30e6db62f7
from: plan — author of record for all four contracts, as the review's § 11 names
to: operator (adjudicator, per the review's frontmatter and H.1 `Spese / MAJOR approval /
  governance`) · mirror (reviewer, for the record)
object: roles/plan.md · roles/orchestrator.md · roles/scientist.md · roles/mirror.md
task_id: PLAN_COMMIT_AND_AUTHOR_RESPONSE_PREPARATION_v1
dispatcher: operator
date: 2026-08-22
governance_version: 3.1.1
mode: RESPONSE_ONLY — no contract is edited, no `status:` line is touched, no finding is closed
  by this document, and no repair is applied
domain: CONTROL PLANE — `reviews/` is a declared `CONTROL_PLANE_ROOT`
  (`plan_defined_parameters.md` § P5.1, `CONTROL_PLANE_ROOTS`), so this file moves no candidate
  content hash and no role fingerprint
authority: none. This response accepts findings against documents Plan authored and contests one
  with evidence. It activates nothing, ratifies nothing, and assigns no authority. No authority is
  read from `roles/plan.md`, which carries `status: PROPOSED`
verdict_transfer: NONE. Every mechanical fact below was executed or recomputed in this session at
  the HEAD named in § 1. Nothing is carried from the review, from
  `PREP-20260822-ROLE-CONTRACT-REPAIR` or from any handoff without independent re-measurement
disposition: MAJOR-1 ACCEPTED, falsifier discharged · MINOR-1 ACCEPTED, remedy blocked upstream ·
  MAJOR-2 ACCEPTED, stands on `main` · MINOR-2 ACCEPTED, owner is Plan, remedy not performable
  from this branch · MAJOR-3 ACCEPTED with changed character · MINOR-3 CONTESTED IN THE FORM
  TRANSMITTED, with evidence, and the true state is worse · § 6 NO VERDICT TO ANSWER
---

# AUTHOR RESPONSE — `REV-ROLES-MIRROR-001`

> **Six findings, five accepted, one contested with evidence.** Nothing here is accepted in
> silence and nothing is rejected without a measurement. Annex C.2 makes this response
> obbligatoria and states that *"il silenzio non è acceptazione"*; it also makes the response the
> author's act, and Plan is the author of record for all four objects.

---

## 0 · IDENTITY — established from repository evidence, not from a contract

| Field | Value | How established |
|---|---|---|
| `actor_id` | `plan` | `deployment/deployment_profile.md` maps `plan` → worktree `evidence-index`; this session stands in that worktree. **The profile's own caveat is carried:** *"Neither column is an ACTOR_ID oracle and neither is a write-authority oracle."* |
| authorship of the objects | `plan` | `REV-ROLES-MIRROR-001` § 11: *"Author of record: `plan`, for all four contracts"*; materialization `a8cd125`, and `384f05f` for `main`'s `roles/scientist.md` |
| worktree | `.claude/worktrees/evidence-index` | `git worktree list` |
| branch | `plan-orchsurf-r4-transcription` | `git rev-parse --abbrev-ref HEAD` |
| HEAD | `7246aa38ce6bd7de596390b5f065b3458c92fb51` | `git rev-parse HEAD` |
| authority claimed | **none** | `roles/plan.md` is `PROPOSED`. This document needs no authority: it is one file under `reviews/`, a `CONTROL_PLANE_ROOT`, committed as a `WORK_COMMIT` — H.1, *"ogni attore, solo proprio branch"* |

🔴 **The identity method here differs deliberately from `PREP-20260822-ROLE-CONTRACT-REPAIR` § 1**,
which established `actor_id` from `roles/plan.md`:3. That is the object under review and it carries
`status: PROPOSED`. The dispatch for this task forbids reading authority from it, so identity is
taken from the deployment profile instead. **The two methods agree on the value**; the divergence
is recorded because a response that answers findings about a contract should not stand on that
contract.

**The response is written by the author of the defective documents.** That is what C.2 requires and
it is also this document's principal limitation: no reading below carries independence, and § 4 is
where that bites hardest.

---

## 1 · SURFACE, AND WHAT WAS RE-MEASURED

```
MEASURED_FROM   worktree evidence-index · branch plan-orchsurf-r4-transcription
                HEAD 7246aa38 · working tree clean before this file
                43 refs surveyed (refs/heads + refs/tags + refs/remotes)
                date 2026-08-22

REVIEW PINNED   blob daec4e8a @ refs/heads/mirror, last touched 1350477
                sha-256 53b47b24…62f7 — unchanged since the review was issued.
                NOT MODIFIED BY THIS DOCUMENT and not modifiable by it: `reviews/mirror/`
                is another actor's branch surface.

OBJECT SURFACE  roles/plan.md         7e1e04cb  — identical at HEAD and on main
                roles/mirror.md       6e515059  — identical at HEAD and on main
                roles/scientist.md    fd30134d  — identical at HEAD and on main
                roles/orchestrator.md 24663eec at HEAD · 2bbb2141 on main  🔴 DIFFER

VALIDITY        NOT_FOUND on 43 refs is not NOT_EXIST. Clones, unpushed worktrees and
                unreferenced objects lie outside this surface.
```

🔴 **The review's surface and this one differ on exactly one object, and it is MAJOR-2's.** The
review measured `roles/orchestrator.md` at `2bbb2141` on `main` and `mirror`, and recorded that a
repair blob `24663eec` exists *"on a side ref"*. **This branch is one of those side refs.** Every
statement below about MAJOR-2 therefore names which blob it is about; the finding is answered
against `main`, because that is where it stands.

---

## 2 · STEELMAN — required by C.2, and placed before every response

**This review found three mechanically demonstrable defects in documents I wrote, and it found
them by the one method that could not be talked out of them: it ran the tools.**

MAJOR-1 is the strongest single finding in the set, and its strength is structural rather than
rhetorical. It does not say the row is out of date. It says the row *suppresses the test that would
correct it* — a capability declared structurally impossible is one nobody schedules an L2 smoke
for, and Annex I.4 makes that row an input to live assignment. **The defect is self-perpetuating,
and I wrote it.** The reviewer then declared a falsifier against its own finding, in writing, and
named the exact experiment that would overturn it.

The review's negative controls are the part I want most on the record. It went looking for a
dangling reference in `roles/scientist.md` between `384f05f` and `4454fea`, found the intermediate
blob present, and **reported the absence of a defect with the same care it reported the presence of
one**. It corrected its own instrument in § 0 — the `**35.2**` scan that returned a false negative
against my citations — and published the correction rather than the first result. It recorded two
findings against itself in § 6, including one located this session.

And it separated correctness from activation in § 8 with a sentence that costs the reviewer
something: *"ratifying the documents as they stand would canonicalize all three."* A reviewer whose
own contract is in the set had an available reading under which activation cures the defects. It
declined that reading explicitly.

**Where I contest a finding below, I am contesting one measurement inside a review whose method I
accept without reservation** — and the contest was only possible because the review published the
surface its measurement was taken on.

---

## 3 · FINDINGS — each addressed individually

### 3.1 · MAJOR-1 · `roles/plan.md`:73 — a capability declared structurally blocked by a tool that runs

**REVIEWER FINDING.** The row *"Fingerprint composition | emit a fingerprint for a named role —
**blocked: the composition is prose, not a script** | UNVERIFIED"* is false as measured;
`governance_fingerprint.py compose --all` exits 0 and emits a fingerprint for every named role.
MAJOR rather than cosmetic because I.4 and body §8 bind assignment to `VERIFIED` capabilities, so
the row suppresses its own remedy.

**AUTHOR RESPONSE. ACCEPTED without qualification, and the reviewer's declared falsifier has been
executed this session and did not fire.** C.2 § 10 named the settling experiment: *"recompose one
role by hand from P2.2 and compare."* It was run: a separate implementation of P2.1/P2.2 written
from the prose of `plan_defined_parameters.md` alone, importing nothing from
`governance_fingerprint.py`, composed `plan` from the 13 inputs it derived by reading § P2.2's
table by hand. It returns
`0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429` — **identical to the script's
output, and identical input-for-input across all 13 per-input digests.** The falsifier the reviewer
offered me is discharged against me, not for me.

🔴 **One thing the hand-composition found that I did not expect, recorded because it qualifies how
much the test proves.** My first pass, written strictly from P2.1's prose, produced a *different*
fingerprint — `0c911567…`. Nine of thirteen per-input digests matched; the four `Annex J` section
digests did not. The cause was two conventions **P2.1's prose does not pin**:

1. **the section identifier syntax** — P2.1 says inputs are *"identified by repo-relative path"* and
   says nothing about how a section is named within one. The script canonicalizes
   `governance/annex_j_runtime_control_plane.md#J.0`; my first pass wrote `… § J.0`, following
   P2.2's own notation. Different identifiers, different serialization, different fingerprint.
2. **the trailing byte of an extracted section** — *"from the line of the named heading up to (not
   including) the next heading"* does not say whether the newline terminating the last line is
   inside or outside the range. It is inside. One byte per section.

Aligning both to the script's convention made all four section digests and the fingerprint agree
exactly. **This does not rescue the contract row and I am not offering it as a defence of it.**
P2.4 is explicit that the script is the artifact and the prose is its input — *"no actor
hand-assembles a fingerprint"* — so a convention the script pins and the prose does not is the
intended relationship, not a gap. What it does mean is narrower and worth stating: the capability is
**executable**, which is what the row denies; it is not **reproducible from P2.2's prose alone**,
which is not what the row claims either. The row is false as written, and the reviewer's falsifier
had to borrow two conventions from the script before it could confirm that.

I add one thing the review left as an open question rather than a defect. Its § 9 residual
uncertainty 1 offers the reading *"as of materialization"*, under which MAJOR-1 would weaken to
staleness. **I do not take that reading, and not because it is inconvenient**: Annex I.4 makes the
capability row an input to *live* assignment, so a row read as a historical statement would be read
by the one mechanism that cannot use it historically. The reading remains available and is not
refuted; I decline it and say why.

**EVIDENCE — re-measured at HEAD `7246aa38`, this session:**

```
$ python3 governance/scripts/governance_fingerprint.py compose --all
mirror        e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412
orchestrator  f85d743c8b31597b8c96430ac36b77f62f650b94750f9df941a929dd4022fefe
plan          0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
scientist     b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
EXIT=0

$ sed -n '73p' roles/plan.md
| Fingerprint composition | emit a fingerprint for a named role — **blocked: the
  composition is prose, not a script** | UNVERIFIED |
```

The defective row is present, verbatim, at this HEAD. The script runs at this HEAD.
`roles/plan.md` is blob `7e1e04cb` here and on `main` — **the defect is not branch-local.**

**RESOLUTION STATE: `ACCEPTED · REPAIR PREPARED, NOT APPLIED · OPEN`.**
`PREP-20260822-ROLE-CONTRACT-REPAIR` § 4 records the repair intent and writes **no clause**, because
the choice between *(a)* deleting the false blocker phrase and *(b)* deleting it and promoting
`UNVERIFIED → VERIFIED` is not one change. Promotion is an Annex I.4 L2 act, and a self-declared
`VERIFIED` by the actor whose capability it is, is exactly what `CONFIGURED != PROVEN` forbids.
**The finding is not closed by this response.** Nothing about a repair being prepared makes the
contract at `main` any less defective than the review found it.

---

### 3.2 · MINOR-1 · `roles/plan.md`:47–48 — two contracts claim `ACTIVE_LESSONS` with opposite subjects

**REVIEWER FINDING.** `roles/plan.md` says Plan may *"maintain `LEARNING_INDEX` durability and the
role-specific `ACTIVE_LESSONS` subsets within budget"*. Annex E.5 gives Plan the **budget** and
Mirror the **subset**; G.2 corroborates; `roles/mirror.md`:37 states the partition correctly. The
em-dash gloss narrows the claim but does not remove the verb. Aggravating: H.1's row for this
decision leaves the Authority column **literally empty**.

**AUTHOR RESPONSE. ACCEPTED. Both halves — the drafting defect and the aggravating structural
cause — reproduce.** The reviewer's own falsifier in § 10 offers me an exit: E.5's *"ricomposizione
subset (Mirror…)"* could be read as covering only the epistemic act, leaving a separate durability
act on the same subsets to Plan. **I decline that exit and I want the reason recorded, because it
is the reason the finding cannot be closed by editing my contract.** Taking the exit would resolve
the ambiguity in the direction that favours the actor reading it, on a row where H.1 assigns the
authority to nobody. Repairing either contract first would **silently fill that empty cell** by
making one document's verb the survivor. The ordering is the decision, and the decision is not
Plan's.

**EVIDENCE — re-measured this session:**

```
$ sed -n '47,48p' roles/plan.md
- maintain `LEARNING_INDEX` durability and the role-specific `ACTIVE_LESSONS` subsets within
  budget — epistemic curation of learning belongs to Mirror, durability belongs to Plan;

$ grep -n 'Lifecycle learning' governance/annex_h_authority_matrix.md
40:| Lifecycle learning: epistemico Mirror, durevolezza Plan | — |
```

H.1 row 40 is the **only** row of the matrix whose Authority column is empty. Annex H is `FROZEN`
and marked `[MAJOR]`; filling that cell is a governed change routed by H.1 itself to `Operatore`.
**The reviewer reported it and declined to fill it. I reproduce it and decline for the same reason,
one degree more strongly**, since I am the actor one of the two candidate answers would favour.

**RESOLUTION STATE: `ACCEPTED · REMEDY BLOCKED UPSTREAM · OPEN`, and the blocker is an operator
determination on H.1 row 40** — carried, not resolved, and recorded as `U-1`/`U-2` in
`PREP-20260822-ROLE-CONTRACT-REPAIR` § 4.

---

### 3.3 · MAJOR-2 · `roles/orchestrator.md` — the mandatory `WORK_COMMIT` has nowhere legal to land

**REVIEWER FINDING.** Four clauses read together — `worktree: the repository root checkout`, *"must
not commit its own work"*, *"nor treat the root as free working space"*, and a Session Learning
Record *"persisted by `WORK_COMMIT`"* — leave a mandatory obligation that cannot be discharged
without violating one of the other three. The body is not the source: GATE 1 disambiguates §35.1,
and the contract reproduces the prohibition without the disambiguation. A repair blob `24663eec`
exists on side refs; **`main` and `mirror` both carry `2bbb2141`, so the defect stands on the
canonical branch.**

**AUTHOR RESPONSE. ACCEPTED, and it stands exactly where the review places it.** The reviewer's
falsifier — *"a canonical rule placing Orchestrator's Session Learning Record somewhere other than
its own branch"* — was searched for and not found; a runtime fact does not amend a contract, and I
agree that `refs/heads/orchestrator` existing does not repair a contract that does not name it.

**One corroboration the review did not have, offered as evidence and not as mitigation.**
`APR-20260819-XPORT-001` — operator-approved, dated 2026-08-19, on `refs/heads/orchestrator` —
already carried this defect **by name**, as `ORCHESTRATOR_WORKTREE_CONTRADICTION`, explicitly
`NOT repaired here`. That record is three days older than the review. Two instruments reached the
same defect independently, which strengthens the finding rather than excusing it, and it means the
defect was known and left standing before this review found it.

**EVIDENCE — blob-level, re-measured this session:**

```
roles/orchestrator.md @ HEAD 7246aa38  →  24663eec772e98b26b9b385c2689cbbcccac57e1
roles/orchestrator.md @ refs/heads/main →  2bbb214143df255ea6c366890a06b3687ee4c89e

$ sed -n '5,13p' roles/orchestrator.md          # at HEAD, the repair text
session_home: the repository root checkout — … It is a location and nothing more:
  it confers no ACTOR_ID and no write authority, and it is not a work surface.
worktree: orchestrator
canonical_batch_surface: the repository root checkout — CANONICAL_BATCH_COMMIT only,
  inside a batch window only.
```

🔴 **This branch carries the repair; `main` carries the defect; and the repair is unapproved.**
Zero `ORCHSURF` approvals across all 21 refs carrying `HUMAN_APPROVAL_QUEUE.jsonl` (re-counted this session; the 19 in `PREP-20260822` is superseded). **A repair
sitting on the branch of the actor who wrote it is not a repair of the canonical object**, and
naming it here does not convert it into one.

**RESOLUTION STATE: `ACCEPTED · UNREPAIRED ON THE CANONICAL BRANCH · OPEN`.** Whether the fix is
`CAND-20260819-ORCHSURF` rev 4 adopted whole or a narrow three-clause edit is `U-4` in the
preparation record and is not decided here — the candidate carries more than MAJOR-2's clauses, and
adopting it to close one finding would import the rest unreviewed.

---

### 3.4 · MINOR-2 · the authority premise rests on a registry that is stale and single-refed

**REVIEWER FINDING.** `roles/orchestrator.md`:36–37 grounds authority in an `ACTIVE`
`ORCHESTRATOR_LEASE` and in *"the explicitly assigned role"*, both pointing at
`runtime/agent_card_registry.md`, which exists on one ref only, is dated `2026-08-17`, records
*"no lease exists"* when nine now do, and carries MAJOR-2's stale worktree value into the registry.
The review states plainly: *"Plan owns the registry (I.4, body §43)"*, and reports it as bearing on
orchestrator.md's authority premise rather than as a verdict on the registry.

**AUTHOR RESPONSE. ACCEPTED, and the ownership attribution is accepted with it — this one is
mine.** Every sub-claim reproduces. I decline the available narrowing that this is a runtime-object
defect and not a contract defect: it is both, and the half that is a runtime defect belongs to Plan.

**What I cannot do, stated rather than left as silence.** `runtime/agent_card_registry.md` exists
on `refs/heads/orchestrator` and **on no other ref**, including this one. H.1 confines `WORK_COMMIT`
to *"solo proprio branch"*. **Plan owning an object does not give Plan a write surface on another
actor's branch**, and the repository offers no route by which the owner of that object can update it
from here. That is a genuine routing gap, not a scheduling excuse, and it is the same
`SESSION_ROUTING_DEBT` `APR-20260819-XPORT-001` records.

**EVIDENCE — re-measured this session:**

```
$ for r in <43 refs>; do git ls-tree -r --name-only $r | grep runtime/agent_card_registry.md; done
refs/heads/orchestrator          ← the only hit, 1 of 43

$ ls runtime/                     # at this HEAD
orchestrator_lease.md             ← registry absent here

$ python3 framework/scripts/lease_state.py
  lease #1 derived=STALE     stored=STALE
  lease #2 derived=RELEASED  stored=RELEASED
  lease #3 derived=STALE     stored=EXPIRED      ← stored/derived DISAGREE
  lease #4 derived=RELEASED  stored=RELEASED
  lease #5 derived=RELEASED  stored=RELEASED
ACTIVE by derivation: 0     @ 2026-08-22T15:56:17Z
```

**The review's separate lease observation is accepted in full as part of this finding.** It derived
rather than read, as `runtime/orchestrator_lease.md` instructs; I re-derived with the same governed
tool and reproduce `ACTIVE = 0` and the `#3` `stored='EXPIRED'` / `derived='STALE'` disagreement.
I concur with the reviewer's judgement that normalising `EXPIRED` — a token outside I.3's
`ACTIVE | STALE | RELEASED` vocabulary — would destroy the evidence, and I propose no normalisation.
**Zero `ACTIVE` leases means there is no `ACTIVE_ORCHESTRATOR` at this instant**, which is a
precondition failure for several routes named elsewhere in this response.

**RESOLUTION STATE: `ACCEPTED · OWNER IS PLAN · REMEDY NOT PERFORMABLE FROM THIS BRANCH · OPEN`.**

---

### 3.5 · MAJOR-3 · `roles/scientist.md` — the contract asserts a protocol binds; the protocol says it binds nobody

**REVIEWER FINDING.** `main`'s `roles/scientist.md` states that
`framework/protocols/scientist_reading_modes.md` *"binds every actor under this contract"*, while
that protocol's own frontmatter on the same ref reads *"Until then it binds nobody."* Two canonical
documents on one ref make opposite claims about one object. The complication the review measured:
the canonical execution **has happened** — `4454fea`, an ancestor of `main`, is the commit that
installed the protocol file itself, so the condition was satisfied by the very commit that wrote the
status line, and the line was never updated. Downstream, `scientist-a` and `scientist-b` have
identities fixed by a document declaring itself binding on nobody. The review does **not** answer
which reading governs; it certifies the measurement and routes the question to the operator.

**AUTHOR RESPONSE. ACCEPTED — and the finding's character changes, in a direction that makes the
repair question harder rather than easier.** The contradiction is real, reproduces at this HEAD, and
I authored both sides of it.

What changes: the review reached **one** of the status line's three conditions. All three are
independently evidenced by durable records.

| Condition in the status line | Evidence | Reachable from |
|---|---|---|
| canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC` | `4454fea` | `main` — the review found this one |
| Mirror hostile review | `REV-SCIAB-MIRROR-006`, ACCEPT | `refs/heads/mirror` **only** |
| `HUMAN_APPROVAL` | `APR-20260819-SCIAB-001` | `refs/heads/orchestrator` **only** |

In the required order, with approval six minutes before execution. 🔴 **The review reached the
execution but not the approval, and its own § 2 names the mechanism that hid it: the
branch-authority trap it documented catching itself.** I am not offering that as a criticism of the
review — I am recording that the same trap operated twice in one document, once caught and once not.

🔴 **This does not discharge the reviewer's falsifier, and I will not claim that it does.** § 10
requires *"a canonical object recording that the status line was superseded — a `DEC` record, a
candidate execution note, or an amended frontmatter on any ref."* Two independent searches this
session found none: `git log -S`/`-G` over the status string across all refs, and blob identity of
the protocol across all 10 refs carrying it — one blob, `2aae1ca7`, everywhere (re-counted this session; the 8 in `PREP-20260822` is superseded). **A satisfied condition that no
object records as satisfied is a staleness defect, not a discharge.** So the finding survives, with
its character changed from *unresolvable contradiction* to *three conditions met and none recorded*.

**RESOLUTION STATE: `ACCEPTED · CHARACTER CHANGED · UNREPAIRED · OPEN`.** Two questions block the
repair and neither is Plan's: whether a satisfied-but-unrecorded condition binds (`U-6` — and
`DEC-20260822` answered the structurally identical question `NOT_CONFIRMED` for `roles/`, on
reasoning that cites *this protocol* as the repository's gloss on the grammar, so extending it by
analogy would be a governance interpretation), and which document is defective — the contract for
over-claiming or the protocol for a stale line (`U-7`). 🔴 **Plan authored both, so Plan's reading
of which one is wrong carries no independence under C.2.** That is not a deferral of convenience;
it is the same bar § 4 applies to Mirror.

---

### 3.6 · MINOR-3 · 🔴 CONTESTED IN THE FORM TRANSMITTED — and the true state is worse

**This is the only finding I do not accept as issued, and it is contested with a measurement, not
with a reading.**

**REVIEWER FINDING.** *"All three Scientist worktrees — `lettore`, `lettore-b`, `lettore-c` — are on
refs carrying the superseded blob"* `e9328115`, so an actor rehydrating from its own worktree reads
a contract that does not know reading modes exist and does not know its own identity is fixed.

**AUTHOR RESPONSE.** The **consequence** the finding describes is real and I accept it. The
**mechanism** is not what was transmitted, and the difference matters because it determines whether
any contract repair can address it.

Measured: `lettore` and `lettore-b` carry **no `roles/` directory and no `governance/` directory at
all**. Neither has `a8cd125` — the materialization commit — as an ancestor. They branched before the
contracts existed. **Only `lettore-c` matches the finding as transmitted.**

🔴 **The true state is worse than the reported one.** A stale blob is a contract that is out of
date. What two of the three Scientist worktrees actually offer an actor rehydrating under body
§36.5 is **no contract and no constitution to rehydrate from at all.** A check that compares blobs
cannot see the difference between *superseded* and *absent*, because absence produces no blob to
compare — which is precisely how a defect of this shape survives an instrument built to find
divergence.

**Consequence for the remedy, and this is why the correction is not pedantic:** as transmitted, the
finding suggests refreshing three worktrees onto the current blob. As measured, **no contract repair
addresses it in any form.** It is a ref-topology defect. Editing `roles/scientist.md` — the object
under review — would change nothing for `lettore` or `lettore-b`, because the file is not on their
refs to be changed.

**EVIDENCE — re-measured this session:**

```
roles/scientist.md @ HEAD 7246aa38 = fd30134d = the blob on refs/heads/main
   (this HEAD is NOT on the superseded e9328115)

Each worktree's HEAD equals its branch tip, so the ref is the surface the actor reads:
   lettore 9b0cf47 · lettore-b cb50e17 · lettore-c 908197b

measured per ref — by ancestry and directory population, not by blob comparison:
   ref                    roles/    governance/   a8cd125 ancestor   scientist.md
   refs/heads/lettore     ABSENT    0 files       NO                 ABSENT
   refs/heads/lettore-b   ABSENT    0 files       NO                 ABSENT
   refs/heads/lettore-c   4 files   22 files      YES                e9328115  ← superseded
```

**One of three matches the finding as transmitted.** The other two produce no blob to compare,
which is why the blob-comparison instrument returned *superseded* for a state that is *absent*.

**RESOLUTION STATE: `CONTESTED IN THE FORM TRANSMITTED · UNDERLYING DEFECT ACCEPTED AND ENLARGED ·
OPEN`.**

🔴 **Two limits on this contest, stated so it is not over-read.**

1. **Restating a finding is the reviewer's act under C.2, not the author's.** I transmit the
   evidence; I do not rewrite MINOR-3's text, and this document does not touch
   `reviews/mirror/REV-ROLES-MIRROR-001.md`. Whether the finding is reissued, refined or left as
   written is Mirror's row.
2. **Whether `lettore` and `lettore-b` are *meant* to carry governance at all is not answered
   here** (`U-8`). Intent is not inferred from topology, and the answer requires operator or runtime
   authority. It is possible that the correct reading is that those refs are not rehydration
   surfaces — in which case the defect moves rather than disappearing, to whatever object asserts
   that they are.

---

## 4 · § 6 · `roles/mirror.md` — NO VERDICT TO ANSWER, and Plan cannot supply the missing one

**The review emitted no verdict on `roles/mirror.md`.** § 6 is a `SELF_REVIEW_OBSERVATION`, and its
closing reasoning is one I accept as correct: H.1 assigns *"Modifica rubrica/metodi di Mirror"* to
*"mai Mirror da solo (G.2)"*, and a `CONFIRMED` issued by the author of the evidence bundle *"carries
no independence and therefore no information."*

**There is therefore no finding here for an author to accept or contest, and this section creates
none.** What I record instead:

- **I accept § 6's four items as genuinely open**, including the one aimed at my own contract's
  pattern — *"whether any other clause of this contract asserts a state of the world that a tool
  would refute"*, i.e. whether MAJOR-1's shape recurs in `roles/mirror.md`. That test has not been
  run by anyone with standing to run it.
- **§ 6's negative control is accepted and is the sharpest thing in the review.** `roles/mirror.md`
  declares one blocker — *"Event ledger analysis — blocked: the ledger has no writer yet"* — and it
  is **true**. Re-measured this session: `ledger/events/` on **0 of 43 refs**. That is what
  separates MAJOR-1 from an honest declaration, and it is a comparison that costs the reviewer
  nothing to omit and that it did not omit.

🔴 **Plan cannot supply the independent review, and saying so is the substance of this section
rather than a caveat on it.** Mirror is barred by G.2/H.1 from self-review. **Plan authored all four
contracts**, so a Plan verdict on `roles/mirror.md` would be an author review — the same defect in
the other direction, and it would extinguish the finding without ever testing it. **Nothing in this
response resolves Mirror independence, and this document must not be read as having supplied it.**

🔴 **And the route the contract names for its own correction currently has no available executor.**
G.2 requires *"an independent reviewer chosen by Orchestrator"*. Measured: **0 `ACTIVE` leases** by
derivation (§ 3.4) → no `ACTIVE_ORCHESTRATOR` to choose one; and **0 `VERIFIED` capabilities in any
actor of any role** → no registered reviewer with a verified review capability. **The independence
gap is not merely unfilled; the mechanism for filling it is itself blocked**, and this response
does not unblock it.

**RESOLUTION STATE: `NO VERDICT TO ANSWER · INDEPENDENT REVIEW REQUIRED · NOT SUPPLIABLE BY PLAN ·
OPEN`.**

---

## 5 · § 7 ENFORCEABILITY and § 8 ACTIVATION

**§ 7 · Clause classification — ACCEPTED as issued.** I contest no row. Two consequences I accept
rather than soften: a large body of clauses in contracts I wrote is **prose-only** — including
*"Mirror does not review itself"*, the dissent ladder, peer-review rotation, `ORPHAN` discipline and
`APPROVAL ≠ AUTHORIZATION` — and a further body is **dependent on missing objects**, principally the
J.1 event ledger measured absent on all 43 refs. The `ACTIVE_LESSONS` clauses in *both* `plan.md`
and `mirror.md` are unenforceable for a second, independent reason: `active_lessons/` is not
materialized, which `CLAUDE.md` § 1 independently declares. **A contract can be internally coherent
and still bind nothing, and § 7 is the measurement of how much of mine is in that state.**

🔴 The `ONE_WRITER_PER_WORKING_DIRECTORY` observation is accepted and carried: conflict `C-7`,
recorded 2026-08-16, *"claimed by nobody"*, closed in no artefact the reviewer could find and none
that I can. **It is a body §14 / GATE 0 rule that is prose-only and has a known open violation.**
Not repaired here; recorded so it is not lost.

**§ 8 · ACTIVATION — ACCEPTED as measured, and NOT RESOLVED here.** Both named conditions appear
satisfied by durable records, all four contracts still advertise `PROPOSED`, and the `status:` line
has never been modified since materialization. Re-verified this session: all four read `status:
PROPOSED — binding once Mirror hostile review passes and the operator approves`, verbatim, at HEAD
`7246aa38`.

🔴 **I decline the reading that would make my own contracts binding, and I want the reason on the
record in my own words rather than only in the reviewer's.** The review put it as *"an actor
choosing the reading that makes its own contract binding would be exactly the convenient
interpretation the gate exists to prevent."* That applies to me with more force than to the
reviewer, because I authored all four documents and this response is written under a dispatch whose
own instruction is `Do not activate contracts`. **H.1 routes governance to `Operatore`.
`DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE` holds the contracts non-binding, and nothing in this
response changes that.**

And I accept § 8's closing sentence without qualification, because it governs the disposition of
everything above: **none of MAJOR-1, MAJOR-2 or MAJOR-3 is cured by ratification, and ratifying the
documents as they stand would canonicalize all three.**

---

## 6 · WHAT_WOULD_CHANGE_MY_MIND — declared falsifiers against *this response*

Each is a specific, runnable test. Any one overturns the part named.

1. **MINOR-3's contest falls** if `lettore` or `lettore-b` is shown to carry `roles/` on the ref its
   worktree actually occupies — or if either is rebased onto a governance-bearing lineage, which
   would convert `ABSENT` back into a blob comparison and restore the finding as transmitted.
   *Test:* `git ls-tree -r <that worktree's ref> -- roles/` and
   `git merge-base --is-ancestor a8cd125 <ref>`.
2. **MAJOR-1's acceptance weakens to staleness** if a governed reading establishes that a capability
   row means *"as of materialization"*. *Test:* a `DEC` or annex reading of I.4 that makes the row
   historical. I judge that reading unavailable and it is **not refuted**.
3. **MAJOR-3's character changes again** if any object anywhere records
   `scientist_reading_modes.md`'s status line as superseded. *Test:* `git log -S` over the status
   string across all refs, plus a prose search of every candidate document. I ran the first and it
   returned nothing; **I did not exhaust the second**, and that is a real gap in this response.
4. **MAJOR-2's "unrepaired on the canonical branch" falls** the moment any `HUMAN_APPROVAL` naming
   `ORCHSURF` appears on any ref. *Test:* grep `HUMAN_APPROVAL_QUEUE.jsonl` for `ORCHSURF` across all
   refs. Currently zero across all 21 refs carrying the queue.
5. **§ 4's claim that Plan cannot supply Mirror's independent review falls** only if a repository
   object establishes that authorship of a *sibling* contract does not disqualify a reviewer of
   `roles/mirror.md`. I did not find one and I did not search exhaustively for one; the bar I apply
   is C.2's independence requirement read directly.
6. **This whole response is superseded** if `REV-ROLES-MIRROR-001` is reissued or amended. It answers
   blob `daec4e8a` and nothing else, and it makes no claim about any later revision.

---

## 7 · WHAT THIS RESPONSE DOES NOT DO

- It does **not** close, resolve, downgrade or dismiss any finding. C.2 gives verdict and restatement
  to the reviewer; adjudication of disagreement on `MINOR-3` is not Plan's to perform.
- It does **not** modify `reviews/mirror/REV-ROLES-MIRROR-001.md`, which is byte-identical at blob
  `daec4e8a` and sits on another actor's branch.
- It does **not** edit any of the four contracts, change any `status:` line, activate or ratify
  anything.
- It does **not** resolve Mirror independence, and § 4 exists to say so explicitly rather than by
  omission.
- It does **not** fill H.1 row 40, answer `U-1` through `U-9`, resolve `MIRROR_RETROSPECTIVE` cadence
  `N`, or assign a reviewer — the last is Orchestrator's act under G.2, and there is no
  `ACTIVE_ORCHESTRATOR` to perform it.
- It does **not** promote any capability to `VERIFIED`.
- It does **not** claim independence for any reading in it. **Every judgement above is the author's
  judgement about the author's own documents**, which is what C.2 asks for and is also the reason
  C.2 makes it a *response* and not a verdict.

---

## 8 · OPEN ITEMS CARRIED OUT OF THIS RESPONSE

| # | Item | Owner | State |
|---|---|---|---|
| 1 | MAJOR-1 repair — blocker phrase only, or blocker + capability promotion (`U-3`) | Plan to prepare; I.4 L2 act to promote | OPEN |
| 2 | MINOR-1 — H.1 row 40's empty Authority cell (`U-1`), and the ordering it blocks (`U-2`) | Operator (H.1, `[MAJOR]`, FROZEN) | OPEN |
| 3 | MAJOR-2 — repair unapproved and absent from `main` (`U-4`, `U-5`) | Operator approval; Orchestrator for the canonical act | OPEN |
| 4 | MINOR-2 — `runtime/agent_card_registry.md` stale, on 1 of 43 refs, not writable from Plan's branch | Plan owns it; routing gap unresolved | OPEN |
| 5 | MAJOR-3 — does a satisfied-but-unrecorded condition bind (`U-6`); which document is defective (`U-7`) | Operator; not Plan, which authored both | OPEN |
| 6 | MINOR-3 — reissue or refine, at Mirror's discretion; and whether `lettore`/`lettore-b` are rehydration surfaces (`U-8`) | Mirror for the finding; operator/runtime for `U-8` | OPEN |
| 7 | Independent review of `roles/mirror.md` | Not Mirror (G.2), not Plan (authorship). **G.2 route has no available executor** | OPEN |
| 8 | Activation state of the four contracts (§ 8) | Operator (H.1) — held non-binding by `DEC-20260822` | OPEN |
| 9 | Conflict `C-7`, `ONE_WRITER_PER_WORKING_DIRECTORY`, open since 2026-08-16 | Unassigned in any artefact found | OPEN |
| 10 | Whether a repair may precede the activation act (`U-9`) | Operator sequencing question | OPEN |

---

*Written by `plan` — the author of the four objects under review — under the operator's dispatch and
**not** under the authority of `roles/plan.md`, which `DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE`
holds non-binding. This is a `WORK_COMMIT` on Plan's own branch (Annex D.1, H.1). It is not a
`CANONICAL_BATCH_COMMIT`, not an `INTEGRATION_CANDIDATE`, and it advances no canonical surface.*
