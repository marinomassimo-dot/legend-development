---
artifact: Session Learning Record (Annex E.6) + CANONICALIZATION RECORD
record_id: SLR-ORCH-003
learning_id: LEARN-ORCH-003
session_ref: NOT DECLARED — not observed, not inferred, not inherited
session_id: 378d27d7-41ad-4c2d-be7e-e9ddf9df249c
version_observed: 2.1.232 — from this session's own owning process image, pid 68877
date: 2026-08-19
actor_id: orchestrator
role: orchestrator (lease #8, acquired and released within this session)
task: CANONICAL_BATCH_COMMIT of CAND-20260819-XPORT revision 2
classification: FAILURE_PATTERN — a false PASS is shaped exactly like a true PASS
confirmation_class: REPLICATION of SLR-mirror-0014 / L-3 (shell as instrument), with one
  sub-shape that is NOT that class and is proposed as new
contributors: mirror (REV-XPORT-MIRROR-002 N-3, which fired on me before I reached it)
scope: how a canonicalization verifies itself, and which of its instruments can lie quietly
status: PROPOSED — NON NORMATIVE
slr_outcome: MICRO_UPGRADE
supersedes: none
---

# THREE INSTRUMENTS LIED IN ONE SESSION, AND EACH ONE LIED IN THE SHAPE OF A PASS

This record has two jobs. The second half is the canonicalization record required of the batch;
the first half is the only thing I learned that I did not already know, and it is not about
transport.

Mirror shipped `N-3` as a non-blocking observation: the manifest's published byte-identity command
is fragile in zsh, and on its first execution can hash two empty outputs and read `IDENTICAL`.
**It fired on me — and it was the second of three, not the only one.** I am recording all three
together because separately each looks like carelessness and together they are one shape.

## The three

| # | instrument | what it returned | what it should have returned | why it looked fine |
|---|---|---|---|---|
| 1 | `git show $b:ledger/approvals/…` in a loop over branches | `0` lines for **every** branch | `6 / 8 / 6 / 6` | zsh parsed `:l` as a parameter modifier. A column of zeros reads like a missing file, not like a broken command |
| 2 | the manifest's own `git show $TIP:framework/… \| awk \| shasum` | `e3b0c442…b855` at **both** tips | `91875ff7…98ad` at both tips | `:f` is a modifier too. The two hashes **agreed**, which is exactly the verdict the command exists to produce |
| 3 | `python3 lease_state.py --check \| tail -5; echo "exit=$?"` | `exit=0` | `1` | `$?` is the **pipeline's** last stage. `tail` succeeded. A clean exit is what a clean check looks like |

**Instances 1 and 2 are `L-3` — shell as instrument — and bring that class to its fifth and sixth
recorded instances.** Instance 2 is Mirror's `N-3` reproduced on a second reader, which is the
strongest possible confirmation of a finding about instrument fragility: it did not need me to
believe it.

## 🔴 Instance 3 is a different sub-shape, and I propose it as new

`L-3`'s mechanism is *the instrument silently produced nothing.* Instance 3 is not that. **The
instrument ran correctly and produced the right answer; I read a different instrument's answer.**
`lease_state.py` did exit 1. `tail` also exited 0. Both are true, and `$?` reported the one I was
not asking about.

```
L-3        the measurement did not happen, and the void was mistaken for a result
NEW (L-3b) the measurement happened and was correct, and a second, adjacent, healthier
           instrument's result was read in its place
```

The distinction earns its keep because the remedies differ. `L-3`'s remedy is *check the transform
actually transformed* — a count, a non-zero yield. That remedy **does not catch instance 3 at all**:
the yield was fine, the output was fine, every line printed was true. Its remedy is narrower and
duller: **do not read a status through a pipe.** Redirect, then read.

## What actually caught them, all three times

Not vigilance, and not re-reading the command.

```
1  caught by a count obtained MOMENTS EARLIER for another purpose — I had already measured
   main's queue at 6 lines by a different route, so a column of zeros contradicted something
   I held
2  caught by RECOGNISING THE CONSTANT. e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b
   7852b855 is the SHA-256 of the empty string. Nothing about the output said "empty"
3  caught by an EXPECTATION ABOUT THE INSTRUMENT — the derivation reports two standing
   historical findings on lease #3, so a clean exit was the one answer it could not honestly give
```

All three defenses are the same defense: **an independently-obtained expectation to contradict.**
None of them is "be careful", and none of them is available to a checker that only compares a
result against itself. This is `L-3`'s own conclusion — *compare a yield against a count obtained by
another route* — arriving from three directions in one session, which is why I am not claiming it
as original.

**The uncomfortable part.** Instance 2 was a *published* command in an approved manifest, and I ran
it while verifying that same manifest. Had I not recognised the constant, I would have recorded
`§§0–9 IDENTICAL` as a verified fact, and I would have been right by accident — the claim is true.
**A canonicalization that reaches a true conclusion through a void instrument has verified
nothing**, and it leaves no trace saying so.

## 🔴 A second finding: Mirror's mitigation was right and its stated mechanism is stale

Mirror's `§0` reports that computing the binding from its own worktree returns `533` and a
disagreeing digest, and attributes this to `candidate_content_hash.py` reading P5 *"from its own
working tree."* I verified the claim before relying on it, and it needs splitting:

```
mirror worktree P5      legend-candidate-v3, TWO control-plane roots        STALE
mirror worktree SCRIPT  parse_p5()     -> PARAMETERS.read_text()           STALE
canonical main SCRIPT   parse_p5(tip)  -> git show <tip>:P5                since b2c326b,
                                          "The hash was a function of the checkout,
                                           and now it is not"
```

**The `533` required BOTH to be stale.** The mirror branch is not a descendant of `main`, so its P5
*and* its copy of the script are old together. Canonical main's script reads the rule from the tip
being hashed, and the tip carries v4 — visible from any worktree, since worktrees share an object
database. Verified: `git -C .claude/worktrees/mirror show e839db3:…plan_defined_parameters.md`
returns `legend-candidate-v4`. **Canonical main's script would have returned 532 from Mirror's own
worktree.**

Mirror's *mitigation* — compute in a clean detached worktree — was correct and I followed it.
Mirror's *stated reason* for it describes a script that canonical governance replaced two days
earlier. That matters in one specific way, and it is branch (b) of `SLR-ORCH-002`: **a true warning
carried by a stale premise is the artifact most likely to be discarded for a good reason.** A reader
who upgrades the script, reads Mirror's mechanism, and concludes the detached worktree is now
unnecessary would be *right about the script* and wrong about every hand-rolled route beside it —
including the independent re-implementation this session used as its second instrument, which reads
the roots by eye and would happily read them from a stale checkout.

I did not repair Mirror's review: it is Mirror's artifact, `ACCEPT` is not reopened by an executor,
and the correction is recorded here for `E.2` curation rather than written into someone else's file.

## MICRO-UPGRADE

Proportional to what was learned, and it is the narrow one:

```
DO NOT READ A STATUS THROUGH A PIPE.  cmd > file 2>&1; rc=$?   — never   cmd | tail; echo $?
BRACE EVERY EXPANSION BEFORE A COLON. "${rev}:path"            — never   $rev:path
KNOW THE VOID CONSTANT.               e3b0c442…b855 is SHA-256("") and must be treated as an
                                      instrument failure, never as a value
```

The first is new here. The second and third are `L-3` and `N-3` restated at the point of use, which
is where they were needed and not where they were written down.

**Not proposed:** a script. `T-GENERIC-1` is already carried as a debt for being a stated procedure
rather than an executable (`REV-XPORT-MIRROR-002 §20.H`), and answering an instrument-discipline
lesson with a fourth unexecuted procedure would be the same defect one level out.

---

# CANONICALIZATION RECORD — CAND-20260819-XPORT revision 2

Required by Annex D and the Orchestrator role contract. The primary batch evidence is the commit
message of `f70878d1`; this section carries the fields a commit cannot carry about itself.

```
CANDIDATE                CAND-20260819-XPORT
REVISION                 2
CHANGE_CLASS             MAJOR (Annex G.1 — a normative protocol binding every actor)

HUMAN APPROVAL           APR-20260819-XPORT-001 / RES-20260819-XPORT-001
  statement, verbatim    "Approvo XPORT Revision 2"
  decided by             operator
  recorded at            a051d034a59d8d7072e1519d425662c4d8b7dbbe (orchestrator branch)
  recorded when          BEFORE lease acquisition and before any canonical write
  ledger                 ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl, appended, line 9
  scope                  this candidate ONLY. Not routing, not lifecycle, not activation

MIRROR ACCEPT            REV-XPORT-MIRROR-002 @ 94927355507ee87adf7531788edbc4ce9907b156
  verdict                ACCEPT · read IN FULL at source on the mirror branch
  bound to               81f241f2…6e1f @ base 4454feab, content tip e839db38, manifest tip 86dfe29
  verdict transfer       NONE — reviewed from R-1

MAIN BEFORE              4454feab72b7a0edf65f191be62aeedd899a15ad
MAIN AFTER               f70878d1cb98317ec62808987fc328be7f8f4ea8
  parents                4454feab72b7a0edf65f191be62aeedd899a15ad (canonical main)
                         86dfe297de7a7ccc286d815b0d4be786a3b0e31e (approved manifest tip)
SNAPSHOT                 snapshot/pre-CAND-20260819-XPORT @ 4454feab — tagged before anything
                         was applied

LEASE ACQUIRED           #8 @ 51b50f50dff04df814409c36f630f653a7ac3dbe
                         window 2026-08-19T17:07:54Z → 17:52:54Z
LEASE RELEASED           #8 @ 0e2c6a625681bb9a5633a7543fd2503c05de563a, 17:16:03Z, terminal
  singleton              0 ACTIVE before acquisition · exactly 1 during · 0 after — DERIVED at
                         each point, never read from the stored STATUS field
  expiry mid-batch       NO — 36m51s remained at release

P5 SOURCE                governance/plan_defined_parameters.md § P5, canonical at BASE_HEAD
  source commit          178ea2af7ad64aae95ef2d9f9fb67d4ab3a3818e
  version                legend-candidate-v4
  roots                  governance/candidates/ · ledger/ · reviews/
  read from              the TIP being hashed, by the script; not from any checkout
  local worktree copy    CURRENT — byte-identical to canonical main, verified, not assumed
  population             532 included · 38 excluded @ content tip; 532 · 40 @ manifest tip

P5 BINDING PRE-BATCH     PASS
  reproduced at          e839db38 · cedb4d5f · 86dfe29 — same digest, included 532 at all three
  independent route      re-implementation importing nothing from the script, roots read by eye,
                         git ls-tree via argv and never a shell: 57420 bytes, 532, same digest
  positive control 1     revision 1 @ f48a807 → 68173f01…c96a, 531 · 33 — EXACT
  positive control 2     SCIAB @ base cbce3016 tip 2a854177 → beef6db0…6061 — EXACT
  negative control       base cbce3016 VERIFIED different first (distinct commit, distinct tree
                         b4fc7810 vs c27a81ee, 33 differing paths) → bf3b9092…6b2c — DISAGREES

GATE 0                   PASS   BASE_HEAD as expected · root clean 0 entries tracked and
                                untracked · GOVERNANCE_VERSION 3.1.1 · lease derived ACTIVE
                                singleton · ONE_WRITER
GATE 1                   PASS   proposer plan ≠ reviewer mirror ≠ adjudicator operator ≠
                                executor orchestrator
GATE 2                   PASS   LINT · publication gate · anchors · receipts · full suite, all
                                re-run this window in clean detached worktrees
GATE 3                   PASS   MIRROR ACCEPT + HUMAN_APPROVAL, both bound to this exact object
GATE 4                   PASS   snapshot tagged at MAIN BEFORE before anything was applied
GATE 5                   PASS   merge proved to produce EXACTLY tree 6f6bb1c8 BEFORE it was made;
                                staged tree read back and compared again before the commit

APPROVED CONTENT →
  CANONICAL CONTENT      IDENTICAL — whole tree 6f6bb1c891ee21bca7ef9fed2a32ee7244cd8693;
                         532 CONTENT paths and 40 CONTROL-PLANE paths compared separately,
                         both identical, so content identity does not lean on the control plane
POST-BATCH P5            PASS — 81f241f2…6e1f reproduces against the new canonical main under
                         the same rule used before the batch

POST-BATCH SUITES        65          POST-BATCH TESTS   953
FAILING SUITES           6, identical set at BASE and at canonical main
FAILING TESTS            7, identical set at BASE and at canonical main
REGRESSION DELTA         0 — set-wise AND name-wise, ADDED 0 / REMOVED 0 at both granularities
NAMED EXPLICITLY         fresh-clone 3/3 green · documented-commands 2/2 green
FINGERPRINTS             scientist 82423a48 · plan 9c0c13fb · mirror 3dff8954 ·
                         orchestrator e2c54470 — unmoved, so no in-flight checkpoint invalidated
WRONG-REASON
  LOAD-BEARING PASSES    0 — three instrument defects were hit and corrected before any
                         conclusion rested on them; see the first half of this record

T-TRANSPORT-1            NOT_RUN — unchanged, and deliberately not turned into a PASS. No
                         recipient was elected and none was invented
T-GENERIC-1              EXECUTED independently this session: 9 changed lines at 5, 35, 286,
                         351, 370, 371, 372, 394, 454; no tenth site under a broader sweep;
                         0 clauses branching on actor identity
SCIENTIFIC DEPTH         PRESERVED — protocol §1.4 canonical and inside the byte-identical
                         §§0–9 range: only the transport representation may become shorter

ROUTING / LIFECYCLE      UNRESOLVED — expected, not a defect. No ACTOR_ID → CURRENT_SESSION_REF
                         mapping, no generation, no registrar, no activation, no supersession.
                         framework/state/actors.yaml still does not exist
HISTORICAL SESSIONS      NOT_PERFORMED — none closed, killed, renamed, superseded or cleaned
BENCH-AB-001             NOT_STARTED — input surface only; no run artifact exists
SCIENTIST A / B          NOT_ACTIVATED — worktrees observed read-only; their dirty C-2 files
                         left exactly as found

CARRIED, NOT REPAIRED
  N-1                    SLR-plan-0008 count/taxonomy contradiction — non-operative, partly
                         inherited from Mirror's own commit subject
  N-2                    manifest §15.2 says lease entry 496 of 532; independently re-measured
                         here as 495 — CONFIRMS MIRROR against the manifest
  N-3                    zsh-fragile published byte-identity command — REPRODUCED LIVE this
                         session and recorded above as instance 2
  N-4                    §11.1's locator column omits its own instance at line 454
  P5 RUNTIME PREMISE     CARRIED_SEPARATE_GOVERNANCE_DEBT — canonical P5.1 says runtime/ is
                         untracked and absent from the domain; runtime/orchestrator_lease.md is
                         tracked and is entry 495 of the 532 hashed. Confirmed at source. Not
                         repaired: P5 is canonical text at BASE_HEAD
  ORCHESTRATOR WORKTREE  CARRIED_ROUTING_DEBT — roles/orchestrator.md frontmatter vs
                         deployment/deployment_profile.md. Resolved for EXECUTION only, by
                         Annex D.1's frozen assignment of CANONICAL_BATCH_COMMIT to the root;
                         the labelling contradiction itself is untouched
  ROOT ENVIRONMENT       CARRIED — two suites enumerate the filesystem rather than git ls-files
  SNAPSHOT DEBT          CARRIED — four historical snapshot tags remain absent and were NOT
                         recreated; fabricating one today would assert a snapshot was taken then
  O-1 / O-2 / O-3        CARRIED from REV-XPORT-MIRROR-001
  T-GENERIC-1 EXECUTABLE CARRIED — a stated procedure, not a committed script
  QUEUE DIVERGENCE       CARRIED — HUMAN_APPROVAL_QUEUE has divergent copies across branches
  SCIAB FINDINGS         CARRIED — P-1, P-3…P-7, P-11, N-1…N-3, N-6…N-9

FINAL STATUS             CAND-20260819-XPORT REVISION 2 CANONICAL
```

## CLASSIFICATION

```
CLASSIFICATION:      FAILURE_PATTERN — a false PASS is shaped exactly like a true PASS
CONFIRMATION_CLASS:  REPLICATION (instances 1–2, class L-3, now at five and six instances)
                     ORIGINAL_OBSERVATION proposed (instance 3, sub-shape L-3b — the adjacent
                     healthy instrument's result read in place of the intended one)
WIDER SCOPE:         yes for L-3b — it applies to any pipeline whose status is consulted, which
                     is most of them, and it is invisible to L-3's own remedy
```

## ATTRIBUTION

Instance 2 is **Mirror's**, published as `N-3` in `REV-XPORT-MIRROR-002` before I met it; I
reproduced it rather than discovered it, and it fired on me in the ordinary course of verifying the
object Mirror had just reviewed. Instance 1 and instance 3 are mine. The stale-mechanism finding
about Mirror's `§0` is mine and is offered as a correction to a reviewer who was right about what
to do — which is the same shape as Plan refusing Mirror's suggested wording in this very candidate,
and it is worth noticing that the pattern recurred one layer down in the same object's lifecycle.

## EVIDENCE

```bash
for b in main orchestrator; do git show $b:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl | wc -l; done
                                                       # 0 0   — instance 1, zsh :l modifier
for b in main orchestrator; do git show "${b}:ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl" | wc -l; done
                                                       # 6 8   — braced, correct
git show $TIP:framework/protocols/cross_session_transport.md | awk … | shasum -a 256
                                                       # e3b0c442…b855 at BOTH tips — instance 2
git show "${TIP}:framework/protocols/…" | awk … | shasum -a 256
                                                       # 91875ff7…98ad, 372 lines, both tips
python3 framework/scripts/lease_state.py --check | tail -5; echo $?      # 0  — instance 3
python3 framework/scripts/lease_state.py --check > out 2>&1; echo $?     # 1  — correct
git show mirror:governance/scripts/candidate_content_hash.py | grep -n 'read_text'   # line 48
git show main:governance/scripts/candidate_content_hash.py  | grep -n '_git("show"'  # line 60
git -C .claude/worktrees/mirror show e839db3:governance/plan_defined_parameters.md \
  | grep CANDIDATE_HASH_VERSION                        # legend-candidate-v4, from the stale worktree
```

## LEARNING_ID

```
LEARNING_ID:        LEARN-ORCH-003
ORIGIN_ACTOR:       orchestrator
CONTRIBUTORS:       mirror (N-3, reproduced here as instance 2)
FIRST_OBSERVED:     2026-08-19
EVIDENCE_COUNT:     3 instrument instances + 1 stale-mechanism instance
OWNER:              durability — plan (E.2) · epistemic curation — mirror (E.2)
STATUS:             OBSERVED
AFFECTED_WORKFLOW:  any gate, review or canonicalization that reads a status, a digest or a
                    count out of a shell pipeline
EXPIRY_OR_REVIEW:   at the first MIRROR_RETROSPECTIVE — cadence N remains UNRESOLVED (ESC-3)
```

> **Not indexed.** `LEARNING_INDEX` does not exist. The index fields are declared so indexing is
> mechanical when it is built; this record does not claim to be indexed.
