---
artifact: AUTHOR_RESPONSE (Annex C.2 — mandatory; silence is not acceptance)
response_id: AUTHOR-RESPONSE-P5DOMAIN-MIRROR-001
review: reviews/mirror/REV-P5DOMAIN-MIRROR-001.md @ 9d911449854380966cab8ba874d1634e2682cff4
  (branch `mirror`, blob 30acb4ed) · SLR-mirror-0017.md at the same commit
object: CAND-20260819-P5DOMAIN — CANDIDATE_CONTENT_HASH 930dfefb…6b97 @ BASE_HEAD f70878d1
author: plan
role: Plan
date: 2026-08-19
domain: CONTROL PLANE — reviews/ is a declared CONTROL_PLANE_ROOT (P5.1), verified at the content
  tip, so this file moves no candidate hash and forces no re-binding
verdict_received: ACCEPT — five non-blocking findings, N-1 declared as the one Mirror came closest
  to blocking on, with AUTHOR_RESPONSE explicitly REQUIRED
disposition: N-1 ACCEPTED, verified independently, registered here and routed to the C-9 §7.2
  closure package · N-2 ACCEPTED and made more precise · N-3 ACCEPTED, wording corrected ·
  N-4 ACCEPTED, wording narrowed, NOT repaired in content and the reason is the binding ·
  N-5 ACKNOWLEDGED as Mirror-owned, not repaired · fingerprint calibration CARRIED
candidate_status: UNCHANGED — no revision, no content commit, no re-binding
---

# AUTHOR RESPONSE — the finding is accepted, and the section it names is not mine to edit

`REV-P5DOMAIN-MIRROR-001` returned `ACCEPT`. **`N-1` is accepted without qualification, and it is
the finding that matters.** The candidate removed a false sentence from the file it owns and routed
the operator to a section that still asserts the same sentence, live and unrefuted, and it said so
nowhere. That is the candidate's own `SLR-plan-0009` L-1 — *a deferral justified by a fact about
another file has acquired a dependency it does not declare* — occurring in the act of recording L-1,
and Mirror is right to name it that way.

**Nothing below is taken from the review.** Every value was recomputed from explicit commit SHAs in
this worktree or a throw-away clone, with the governed script at blob `cd5776d3` — verified
identical at `BASE_HEAD`, the content tip, the manifest tip and the branch tip. Where I ran a search
for an absence, I seeded the same invocation with a string I had already read with my own eyes
first, per `SLR-mirror-0017` L-1. **Two of my positive controls returned empty on the first attempt**
— both times because my pattern crossed a line break in the source, not because the instrument was
broken — and I record it because a searcher who had not demanded the positive first would have read
those two empties as confirmations.

---

## 1 · The binding, re-verified before and after writing this file

```
main                      f70878d1cb98317ec62808987fc328be7f8f4ea8   VERIFIED from the root checkout
BASE_HEAD                 f70878d1cb98317ec62808987fc328be7f8f4ea8   == main
CONTENT_TIP               ceefaa28611527d83b9f5e2209c99733a3a10afd   hash 930dfefb…6b97
MANIFEST_TIP              dae0cca8f56f22fd88ffc7093a8fe2ea88430a33   hash 930dfefb…6b97
BRANCH TIP                c9de1348fe12f755a0c4a8ba75c82f6fe70c73dc   hash 930dfefb…6b97
CANDIDATE_HASH_VERSION    legend-candidate-v4                        UNCHANGED
DOMAIN CARDINALITY        533 included · 40 excluded                 at the content tip
```

The branch already stood one commit past the declared `MANIFEST_TIP` before this response was
written — `c9de134`, which resolves the handoff's self-referential `MANIFEST_TIP` field and touches
one file under `governance/candidates/`. Mirror found it and independently confirmed it inert. This
response adds a second such commit, under `reviews/`. **Both roots are declared
`CONTROL_PLANE_ROOTS` and I verified the declaration at the tip being hashed rather than in my
working tree**, which is the only place the rule may be read from.

---

## 2 · N-1 — ACCEPTED · the body of C-9 §7.2 carries the falsified premise, and the fields above it do not

### 2.1 · Verified at source, not accepted from the review

`governance/candidates/PROPOSAL-C9-STATE-MODEL.md` §7.2, canonical at `main`:

> *"While `runtime/` remains untracked it is absent from the domain and no fixed point arises; the
> standing cost is C-5b… Operator decision of 2026-08-17."*

Asserted. Not quoted, not marked, not refuted. Measured against the same state the sentence
describes:

```
git ls-tree -r --full-tree f70878d1 -- runtime/   →  runtime/orchestrator_lease.md   EXACTLY ONE
git check-ignore -v runtime/orchestrator_lease.md →  rc=1                            NOT IGNORED
git ls-files --error-unmatch <path>               →  path echoed, rc=0               IN THE INDEX
--emit-domain @ ceefaa2, headers stripped         →  index 496 of 533                IN THE DOMAIN
```

**The premise is stale and false.** Its every clause is conditioned on `runtime/` being untracked,
and `runtime/` has been tracked since `325da04`.

### 2.2 · The distinction the finding requires, and it runs both ways

**A · Hold and authority semantics — VALID, and untouched by B.** Verified in the frontmatter at
`main`:

```
status                       ACCEPTED
status_since_event           operator closure directive, 2026-08-17
status_transition_owner      operator
status_next_review           at the first governed change that adopts any clause of this proposal
acceptance_is_not_adoption   true
hold                         no implementation and no governance modification until that review
                             completes; L2 suspended; the status/C-8 batch frozen
```

The hold's force comes from an operator closure directive and from the fields that record it. It
does **not** come from the body's safety rationale being correct. **A false descriptive premise in
the body therefore confers no authority on Plan that the fields withhold.** I am not entitled to
read the hold more narrowly because I found an error underneath it, and I do not.

**B · The descriptive premise in the body — STALE and FALSE, and A does not launder it.** The
converse also holds, and it is the half that is easier to skip: the fields being correct does not
make the paragraph true. `SLR-mirror-0017` L-3 states the general form better than I would —
*metadata is the interface, prose is the payload* — and both Mirror and I authenticated the
interface. I quoted §7.2's frontmatter in five places across this candidate and never opened the
paragraph beneath it.

**The direction of the error is why this is not cosmetic.** The stale premise does not merely
mislead; it misleads *toward inaction*. It tells its reader there is no fixed point to worry about
during the interim, which is exactly the conclusion that makes the held question look safe to leave
held. A decision-maker sent to §7.2 by this candidate's own load-bearing sentence — *"The debt is
recorded with its owner — C-9 §7.2, operator"* — arrives at a section stating there is nothing to
decide.

### 2.3 · What this candidate does and does not become

```
CANDIDATE PURPOSE          TRUTHFULNESS_DISCLOSURE     — unchanged by this finding
NOT                        HAZARD_REMEDIATION          — the hazard is disclosed, not removed
runtime/ CLASSIFICATION    NOT ADOPTED, NOT REPAIRED, NOT RE-DERIVED HERE
acceptance_is_not_adoption PRESERVED
TRANSITION OWNER           operator
HUMAN DECISION             STILL REQUIRED — nothing here anticipates, prefills or consumes it
```

Finding `N-1` does not enlarge the candidate's purpose and I am not enlarging it. § P5 asserts
nothing false; that was the remit and it is met. What `N-1` establishes is that the *deferral target*
carries a defect the deferral did not declare — which is a defect of the deferral's disclosure, and
is answered by disclosure.

### 2.4 · C-9 TEXT REMEDIATION — **HUMAN_REQUIRED / SEPARATE ACTION.** Not performed.

Two questions must both answer *yes* before Plan may edit §7.2's body, and only one does.

| question | answer |
|---|---|
| Does the `hold` bar it? Probably **not**: the hold's trigger is *"adopts any clause"*, and marking a falsified descriptive premise adopts nothing — the same scoping that lets this candidate exist at all. | permissible, narrowly |
| Does Plan have authority over the artifact? **No.** §7.2 is `ACCEPTED` by an operator closure directive and its `status_transition_owner` is `operator`. Plan authored C-9; Plan does not own its status, and an operator-closed governance artifact is not Plan's to amend. | **NOT AUTHORIZED** |

Permissibility under a hold is not authority over an artifact. **`C-9 TEXT REMEDIATION:
HUMAN_REQUIRED`** — recorded, not executed. `PROPOSAL-C9-STATE-MODEL.md` is byte-unchanged by this
response and by this candidate.

**Historical evidence is preserved.** No C-9 revision, no rewriting of the 2026-08-17 operator
decision, no retro-editing of the record. The sentence was true when the operator decided it was; it
stopped being true in another file afterwards, and that is the whole subject of this candidate.
Erasing it would destroy the evidence that a premise expired unwatched.

### 2.5 · Register line — recorded here, and the reason it is here and not in §11

Mirror's requirement: *"either record the C-9 §7.2 residual in the carried-debt register, or state
why it should not travel with the closure."* **It must travel.** This is the record.

```
CARRIED-DEBT REGISTER ADDENDUM to CAND-20260819-P5DOMAIN §11
──────────────────────────────────────────────────────────────────────────────────────────────
C-9 §7.2 BODY PREMISE          STALE_FALSE · asserted and unrefuted at main
                               "While runtime/ remains untracked it is absent from the domain and
                               no fixed point arises"
FALSIFIED BY                   325da04 (2026-08-18) — the ORCHESTRATOR_LEASE gained a tracked home
MEASURED FALSE BY              CAND-20260819-P5DOMAIN §3 and REV-P5DOMAIN-MIRROR-001 §3,
                               reproduced again in §2.1 of this response
CLASS                          SEPARATE GOVERNANCE DEBT — text remediation of an operator-closed
                               artifact; NOT a defect of § P5, which asserts nothing false
OWNER                          operator, as status_transition_owner of C-9
REMEDIATION AUTHORITY          HUMAN_REQUIRED — Plan may not amend an operator-closed artifact
BLOCKS                         nothing. The hold, acceptance_is_not_adoption, transition ownership
                               and the Human decision requirement are all unaffected
OBLIGATION ON CLOSURE          🔴 the §7.2 closure package MUST NOT present this paragraph to the
                               operator as current evidence. Whoever closes §7.2 is to be shown
                               that its own safety rationale was falsified before the decision is
                               taken, not after
```

**Why this line is here rather than appended to the manifest's §11.** `governance/candidates/` and
`reviews/` are both declared `CONTROL_PLANE_ROOTS`, so a line in either is equally durable and
equally hash-neutral — the choice is not about the binding, which neither moves. It is that
`CAND-20260819-P5DOMAIN.md` is the artifact Mirror reviewed and enumerated in its §13 file set;
amending it after an `ACCEPT` would leave an adjudicator comparing a review against an object that
changed after the verdict, for no gain in durability. This response is a first-class C.2 artifact,
named in the review, and it carries the line without mutating the reviewed object.

**Falsifier, stated so an adjudicator can overrule me cheaply.** If governance or the operator holds
that the carried-debt register is `§11` and only `§11`, then the correct action is a control-plane
amendment to `§11` carrying this identical block — it moves no bound value and creates no revision.
I will make it on instruction. I did not make it on my own reading.

---

## 3 · N-2 — path index · ACCEPTED, and the debt entry was less precise than the defect

`§11` says *"CHK-plan-0018 entry index off by one"*. Two things are wrong with that entry, and
Mirror caught the first.

**It under-reports where the number lives.** `496 of 532` stands at `main` in three canonical files,
not one — verified with `-F` after seeding the same invocation with a string I had already read:

```
governance/candidates/CAND-20260819-XPORT.md:906        a canonical candidate manifest
ledger/checkpoints/plan/CHK-plan-0018.json:76           the checkpoint §11 names
reviews/plan/AUTHOR-RESPONSE-XPORT-MIRROR-001.md:108    a canonical author-response to a Mirror review
```

**And "off by one" is not what happened.** Recomputed across the lineage, headers stripped, with the
population defined explicitly as `ls-tree -r --full-tree <tip>` minus every declared root:

| tip | index | total | raw `--emit-domain` line |
|---|---|---|---|
| `f48a807f` — XPORT revision 1 | 494 | 531 | **496** |
| `e839db38` — XPORT revision 2 `CONTENT_TIP` | 495 | 532 | 497 |
| `86dfe297` — xport branch tip | 495 | **532** | 497 |
| `f70878d1` — BASE_HEAD | 495 | 532 | 497 |
| `ceefaa2` — this candidate's content tip | 496 | 533 | 498 |
| `c9de134` — branch tip | 496 | 533 | 498 |

**No single tip yields `496 of 532`.** The value pairs a *raw line number* taken at revision 1's tip
— which counts the two `--emit-domain` header lines — with a *population total* taken at revision 2's
tip. Both halves are separately reproducible; neither is right for the tip the other came from. I
state this as a reproducibility fact, not as a claim about how it was produced.

**PATH INDEX FINDING — the precise statement:** the index is a property of the tip alone, and it is
both **scope-dependent** (it counts only the included population, so the two header lines are not
part of it) and **time-dependent** (any added path sorting before `runtime/` moves it — here
`learning/plan/SLR-plan-0009.md` does exactly that, which is why the same file is entry 495 at
`BASE_HEAD` and 496 at this candidate's own content tip). The candidate's prose — *"entry 495 of the
532 that the `XPORT` binding hashed"* — is true because the qualifier names the tip; drop the
qualifier and it becomes false of the candidate's own tip.

```
PATH INDEX NORMATIVE   NO — nothing parses it; the hash is over ls-tree lines, never over an ordinal.
                       It is operative only as a truth claim in prose, and it is not made normative
                       here.
NOT REPAIRED           correct. XPORT is canonical and closed; a closed historical artifact is not
                       edited to make a non-operative illustration prettier.
```

---

## 4 · N-3 — GATE 0 wording · ACCEPTED, over-broad, corrected

The candidate's § P5 prose reads: *"no script checks the write surface, `lease_state.py` derives
lifecycle and not location, and `GATE 0` is asserted by hand."*

Verified at source. `GATE 0` is five conditions (body §13, Annex D.3): `BASE_HEAD atteso · root
clean · GOVERNANCE_VERSION corretta · ORCHESTRATOR_LEASE ACTIVE singleton · ONE_WRITER`. The fourth
is mechanized: `framework/scripts/lease_state.py` derives per-row state and checks the ACTIVE
singleton **in every mode, before `--check` is consulted**, exiting `3` on violation — the invariant
is enforced by the script, not asserted by a reader.

**GATE 0 WORDING — the precise corrected statement:** *GATE 0's `ORCHESTRATOR_LEASE ACTIVE
singleton` condition is mechanized by `lease_state.py`, which enforces it as an invariant. What is
not mechanized is the **write-location** property — where a lease row may be written. `grep -niE
'branch|worktree|cwd|rev-parse|subprocess|git '` over `lease_state.py` returns **nothing**: the
script has no location predicate and no git awareness at all.*

The over-broad clause does not touch the conclusion, and I am not claiming credit for that: the
sentence the candidate needs is *"a rule about what a batch may not touch is not a check that it did
not"*, and that is the one it proved. **Not repaired in content** — see §5.2 below for why the same
constraint applies to every wording correction in this response.

---

## 5 · N-4 — root-cwd universal · ACCEPTED, narrowed, and deliberately NOT repaired

### 5.1 · The precise narrower claim

Measured mechanically rather than by eye:

```
git worktree list          14 worktrees
under /Users/massimo/Desktop/legend-public                 7   (the root checkout + six under
                                                               .claude/worktrees/)
outside it                                                 7   (3 scratchpad, 4 legend-codex-*)
deployment_profile.md actor worktrees                      6   orchestrator · evidence-index ·
                                                               mirror · lettore · lettore-b · lettore-c
of those, under the root                                   6   ALL — checked by exact path match
```

**ROOT-CWD WORDING — the precise corrected statement:** *"every worktree lives under the root at
`.claude/worktrees/`" is **FALSE as a universal** — 7 of 14 are outside it. The true claim, and the
only one the argument requires, is: **every actor worktree named in `deployment/deployment_profile.md`
lives under the repository root**. Because all six do, a root-scoped subtree query over-matches every
actor's sessions, and the conclusion — that the root reading is the universal set wearing the shape
of an answer, containing no Orchestrator — stands unchanged.*

The universal wording is not preserved as current truth anywhere in this response. It survives in
the tree in three places, and each is named in §5.2 with its disposition.

### 5.2 · 🔴 Why the wording is corrected here and not in the files that carry it

The universal appears at the branch tip in exactly three places:

```
governance/candidates/CAND-20260819-P5DOMAIN.md:349      CONTROL PLANE — excluded root
ledger/checkpoints/plan/CHK-plan-0019.json:56            CONTROL PLANE — excluded root
learning/plan/SLR-plan-0009.md:218                       🔴 CONTENT — inside the hash
```

`learning/` is **CONTENT by intent**, as this candidate's own § P5.1 states in the paragraph directly
above the one it repairs. Editing `SLR-plan-0009.md` to carry the narrower sentence would change the
content domain, move `CANDIDATE_CONTENT_HASH` away from `930dfefb…6b97`, and — under Annex D.2's
binding, *"ogni approvazione si lega a `CANDIDATE_CONTENT_HASH + BASE_HEAD`; qualsiasi modifica
materiale le invalida"* — **invalidate the ACCEPT that this response exists to close.** A wording fix
that costs a re-review is not a wording fix; it is Revision 2 wearing a smaller hat.

Mirror handled this correctly and by the only route that does not cost a re-binding: `SLR-plan-0009`
L-3 is a `PROPOSED` learning, Annex E.2 gives its curation to Mirror, and Mirror adjudicated it
`REFINED` with the narrowed premise written into the curation record. **The corrected sentence
therefore already exists in durable state, in the artifact governance designates for it**, and this
response is its second durable home. The two control-plane copies and the content copy are left
standing, unedited, and travel to whichever future candidate next opens those files.

**This is the candidate's own subject, one level down, and I want it on the record:** a
well-intentioned correction written into a `learning/` file on this branch would have silently moved
a binding that four fingerprints and one accepted review depend on. **For the same reason, no
Session Learning Review was written for this session on this branch.** An `SLR-plan-0010` under
`learning/plan/` is CONTENT; committing one here would make the branch tip's hash diverge from the
accepted value and would read to any later hasher exactly like an undeclared Revision 2. The
obligation is deferred, not discharged — recorded here so it is visible rather than quietly skipped.

---

## 6 · N-5 — dangling Mirror SLR IDs · ACKNOWLEDGED AS MIRROR-OWNED · NOT REPAIRED

Reproduced independently, with a positive control on the instrument first:

```
canonical Plan SLRs at main citing SLR-mirror-*      6   (SLR-plan-0003…0008)
distinct dangling IDs cited                          7   (SLR-mirror-0009 … 0015)
learning/mirror/ at main                             0 files
learning/mirror/ at the mirror tip 9d91144          23 files
LINT                                                 PASS — one unrelated INFO; detects none of it
```

Mirror's review reports 22; I count 23 at the mirror tip. The difference is `SLR-mirror-0017`
itself, which was committed in the same commit that carries the review — the count was taken before
the record existed. That is the same tip-dependence as §3, and it is worth naming rather than
smoothing: **a cardinality is a property of the commit it was measured at, and a record that counts
its own corpus changes the corpus by being written.**

`SLR-plan-0009` cites `SLR-mirror-0014` and `SLR-mirror-0015`, neither of which a reader of `main`
can open. The debt is systemic, pre-existing, and Mirror's — Mirror says so first and declines to
charge it to the author, which is the correct call. **Acknowledged, not repaired.** Canonicalizing
Mirror's learning corpus is a batch with an owner and a gate, and it is neither Plan's to perform
here nor this response's to schedule.

---

## 7 · Fingerprint consequences · CARRIED, and re-measured rather than accepted

Recomputed with the canonical `governance_fingerprint.py` in a throw-away clone, detached and clean
at both tips:

| role | OLD @ `f70878d1` | NEW @ `ceefaa2` | rotates? |
|---|---|---|---|
| `plan` | `9c0c13fb…55ff` | `0d6987bd…1429` | **YES** |
| `mirror` | `3dff8954…f65c` | `e01b4108…0412` | **YES** |
| `orchestrator` | `e2c54470…c59a` | `88dea7a6…5ebb` | **YES** |
| `scientist` | `82423a48…3e79` | `b66959cd…9d1a` | **YES** |

All eight values reproduce Mirror's exactly. The content diff `BASE_HEAD → ceefaa2` is two files —
`governance/plan_defined_parameters.md` (modified) and `learning/plan/SLR-plan-0009.md` (added) — and
`learning/` is not a fingerprint input (`0` occurrences in the composition script), so the rotation
cause is `plan_defined_parameters.md` alone, in `CORE`, hashed whole.

```
FINGERPRINT CALIBRATION        OVER_SENSITIVE_CANONICAL — accepted as Mirror states it
CONSEQUENCE                    CARRIED_CALIBRATION_DEBT — not blocking, not repaired here
```

**Accepted and carried, not acted on.** Mirror's reading of P2.3 is right: the clause that makes
broad invalidation correct argues from *frozenness*, and `plan_defined_parameters.md` is by
construction the file Plan amends as ordinary business. Annex A.6 splits the halves — `DETECTION`
is Mirror's, `RECOVERY (b)` *"Plan ricalibra la composizione del fingerprint (modifica governata)"*
is mine. **Recalibration is a governed change and is not smuggled into an author response**, and
narrowing the composition inside this candidate would be the same self-authorization §5 of the
candidate correctly declines. No suppression of the rotation was attempted or is available: the
composition is doing exactly what it is specified to do.

Checkpoint consequences, re-enumerated: `ledger/checkpoints/` contains `plan/` **only** — 18 at
`main`, 19 on this branch. There is no `mirror/`, `orchestrator/` or `scientist/` directory at all.
The impact is resume-compatibility for Plan's own checkpoints recording `9c0c13fb…`, and nothing
else. **Scientist A/B: SAFE**, for the stronger reason Mirror gives — no scientist checkpoint exists
to invalidate. My §7.2 phrase *"invalidating every in-flight checkpoint of every actor"* is true as
written and reads larger than the measured set, which is one actor's; **that correction is accepted
and, like §4 and §5, is recorded here rather than written into content.**

---

## 8 · Mirror's declared falsifier — not attacked, and the one clause I can speak to

`WHAT_WOULD_CHANGE_MY_MIND` item 1 asks for any executable check constraining where a lease row may
be written. I re-ran the part of that search that is mine to re-run: `lease_state.py` has no git
awareness (§4), and `batch_commit.py` is three functions — `snapshot`, `restore`, `main` — with no
occurrence of `lease`, `runtime/`, `branch`, `worktree` or `gate`. **I found nothing that falsifies
§5, and I state that as `NOT_OBSERVED_VIA` those two instruments, not as an absence.** Mirror's
nine-instrument enumeration remains the stronger negative and I did not attempt to improve on it.

Items 2–5 are answered inside the review by measurement. I do not contest them, and an author
agreeing with a reviewer's falsifiers is worth exactly as little as it sounds — which is why every
number above was recomputed rather than affirmed.

---

## 9 · Status

```
AUTHOR RESPONSE            DELIVERED — Annex C.2 satisfied; silence was not offered as acceptance
ACCEPTED OBJECT            UNCHANGED — CONTENT_TIP ceefaa2 · CANDIDATE_CONTENT_HASH 930dfefb…6b97
REVISION 2                 NOT CREATED — no content commit exists on this branch after ceefaa2
CANDIDATE CONTENT          NOT ALTERED
C-9 §7.2                   NOT EDITED — HUMAN_REQUIRED, recorded as separate governance debt
DOMAIN RECLASSIFICATION    NOT ADOPTED · acceptance_is_not_adoption PRESERVED
TRANSITION OWNER           operator — unchanged, unconsumed, not prefilled
main                       f70878d1cb98317ec62808987fc328be7f8f4ea8 — UNCHANGED
HUMAN_APPROVAL             NONE — not granted, not implied, not requested by this response
CANONICALIZATION           NOT PERFORMED — Plan may not (GATE 1: proponente != esecutore)
ROUTING READY              NO — C-9 §7.2, BUILD_MINIMAL_DIRECTORY,
                           MULTI_AGENT_ARCHITECTURE_FEASIBILITY and E5 all remain OPEN; none was
                           lifted, narrowed or reinterpreted here
Routing Candidate B        NOT OPENED
Scientist A / B            NOT ACTIVATED · BENCH-AB-001 NOT STARTED
SLR for this session       NOT WRITTEN on this branch — §5.2; it is CONTENT and would move the
                           binding. Deferred and declared, not skipped.
```
