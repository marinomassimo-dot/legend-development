---
artifact: Session Learning Record (Annex E.6) + CANONICALIZATION RECORD
record_id: SLR-ORCH-004
learning_id: LEARN-ORCH-004
session_ref: NOT DECLARED — not observed, not inferred, not inherited
session_id: 6c7493cd-25ec-44db-97ac-31f5d0fdf2e8
version_observed: 2.1.232 — from this session's own owning process image. A 2.1.233 image is
  also running on this machine; it is a different endpoint, not a mismatch to revalidate
date: 2026-08-19
actor_id: orchestrator
role: orchestrator (lease #9, acquired and released within this session)
task: CANONICAL_BATCH_COMMIT of CAND-20260819-P5DOMAIN revision 1
classification: FAILURE_PATTERN — I hit the exact trap the review I had just read described,
  on the exact task it described it on · plus one ORIGINAL_OBSERVATION proposed
confirmation_class: REPLICATION of SLR-mirror-0017 / REV-P5DOMAIN-MIRROR-001 §10.3, and of the
  L-3 shell-as-instrument class; one sub-shape proposed as new
contributors: mirror (REV-P5DOMAIN-MIRROR-001, whose §10.3 documented the trap before I met it)
scope: what a forewarning is worth against an instrument defect, and when a procedural invariant
  must be measured rather than asserted
status: PROPOSED — NON NORMATIVE
slr_outcome: MICRO_UPGRADE
supersedes: none
---

# THE REVIEW TOLD ME THE TRAP AND NAMED THE TASK, AND I WALKED INTO IT ANYWAY

This record has two jobs. The second half is the canonicalization record required of the batch.
The first half is the only thing I learned that I did not already know, and it is uncomfortable,
because the knowledge that would have prevented it was in a file I had read in full two hours
earlier.

## 1 · The instance

Mirror's `REV-P5DOMAIN-MIRROR-001` §10.3 says, about its own regression comparison:

> *"My first extraction over-matched and reported 8 entries; I re-derived with an anchored pattern
> and got the true 6."*

I read that sentence. I then ran the same comparison, with this extraction:

```bash
grep '^- ' $BASE | sed 's/: exit.*//' | sed 's/^- //' | sort
```

and got **8**. The two extras were not test suites. They were diff-style lines from inside an
`AssertionError` — `test_release_runner_verdict.py` asserts on a list difference, and unittest
prints the differing elements as `- ['governance/scripts/test_candidate_content_hash.py']` and
`- []`. My pattern could not tell a runner verdict line from an assertion payload.

**The comparison was not wrong.** Both sides over-matched identically, the diff was still empty,
and `REGRESSION DELTA 0` was still the true answer. That is precisely what makes it worth
recording: the defect produced a *correct conclusion from a wrong population*, and nothing in the
output looked off. Had the batch actually introduced a regression in a suite whose name did not
match my pattern, the same command would have reported the same clean diff.

## 2 · What caught it, and it was not the forewarning

Not memory of Mirror's sentence. What caught it was that the runner **prints its own verdict
block**, and that block listed six, while my derived set listed eight. Two independent counts of
the same thing disagreed, and the disagreement was visible on the same screen.

The remedy was to re-derive with a pattern anchored to the runner's exact verdict-line grammar,
`^- <path>.py: exit <n>$`, and then to put a positive and a negative control on that pattern
before reading its result: a suite I had watched fail must match (it did, once), and a suite that
passed must not (it did not, zero times).

**🔴 The sub-shape I propose as new.** `SLR-mirror-0014` L-3 and `SLR-ORCH-003` are about
instruments that return *nothing* or return an *adjacent healthy result*. This one is different:
the instrument returned a **superset** of the right answer. A superset is the hardest failure to
see, because every element you expected is present. You verify by checking that what you wanted
is there, and it is there. Nothing prompts you to ask what else came with it.

The general form, and it is testable: **when an extraction feeds a set comparison, over-matching
is invisible to both sides at once.** Symmetric contamination cancels in the diff. The only
defence is an independent cardinality — which is why the tool printing its own count was worth
more than my having been warned.

## 3 · A second observation — the batch that canonicalizes a disclosure is the first test of it

This candidate's whole content is the statement that `runtime/orchestrator_lease.md` sits inside
the content domain, that a lease row written in the wrong place would move
`CANDIDATE_CONTENT_HASH`, and that **nothing mechanizes** the convention preventing it — the
protection is `PROCEDURAL`.

Executing that candidate required me to write two lease rows.

So the batch is not merely governed by the invariant it canonicalizes; it is the first live
instance of it, performed by the actor the invariant constrains, while that actor holds the only
authority that could violate it. Asserting the invariant here would have been circular. I
therefore measured it: the binding was reproduced from the root checkout immediately before the
acquisition row was written and immediately after, and the root's state was re-read at each
point. I added `WRITE_SURFACE` as an explicit field on lease row #9 rather than leaving the
convention implicit as rows #1–#8 do.

**The reusable form:** *a candidate that discloses a procedural-only invariant makes the very next
batch an experiment on that invariant, and the batch should measure it rather than restate it. The
disclosure is what makes the measurement obligatory; before the disclosure, nobody knew it was
load-bearing.*

## 4 · What I did not do

I did not create `SLR-plan-0010` to repair Plan's deferred obligation, and I want the reason on
the record rather than in a gate output. Creating it would have changed the approved object — it
is `learning/`, which § P5.1 declares CONTENT by intent, and it would have moved the hash off
`930dfefb…` and voided the ACCEPT this batch executes. The instruction to determine the
deferral's validity and the temptation to discharge it are two different acts, and only the first
was mine.

I also did not repair `C-9 §7.2`, the three canonical files carrying the stale `496 of 532`, the
fingerprint composition, the Orchestrator routing-surface contradiction, or the dangling Mirror
SLR references. Each has an owner and a gate, and none of them is a canonicalization.

## MICRO-UPGRADE

```
UPGRADE:   Any set comparison derived by pattern extraction must be cross-checked against an
           independent cardinality produced by the tool itself, BEFORE the comparison is read.
           Where the tool prints its own summary, that summary is the control. Where it does not,
           the extraction pattern carries a positive control (something known present must match
           exactly once) and a negative control (something known absent must match zero times).
APPLIES:   regression comparisons, failing-set diffs, domain enumerations, path-index derivations,
           any "the sets are identical" claim
WHY:       symmetric over-matching cancels in a diff and is therefore invisible to the comparison
           it corrupts. A warning about the trap is not a defence against it — I had one.
```

---

# CANONICALIZATION RECORD — CAND-20260819-P5DOMAIN revision 1

Required by Annex D and the Orchestrator role contract. The primary batch evidence is the commit
message of `04693e68`; this section carries the fields a commit cannot carry about itself.

```
CANDIDATE                CAND-20260819-P5DOMAIN
REVISION                 1 — VERIFIED, not assumed. The branch stood two commits past the
                         declared MANIFEST_TIP; a branch head later than the manifest tip is not
                         itself a Revision 2. Both were classified by artifact semantics:
                         c9de134 (handoff MANIFEST_TIP field, governance/candidates/) and
                         3c4df9c (author response, reviews/) touch only declared
                         CONTROL_PLANE_ROOTS. NO Revision 2 exists.
CHANGE_CLASS             MAJOR (governance; Annex D and body §12)

HUMAN APPROVAL           APR-20260819-P5DOMAIN-001 / RES-20260819-P5DOMAIN-001
  statement, verbatim    "Approvo CAND-20260819-P5DOMAIN."
  decided by             operator
  recorded at            90735ea1dbdd1d5bf3571c3943ac3139c78688a1 (orchestrator branch)
  recorded when          BEFORE lease acquisition and before any canonical write
  ledger                 ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl, appended, line 10
  durable retrieval      PASS — read back from the commit object, all bound values present
  scope                  this candidate ONLY. NOT C-9 §7.2 adoption or text remediation, NOT the
                         runtime lease domain reclassification, NOT BUILD_MINIMAL_DIRECTORY, NOT
                         Routing Candidate B, NOT Orchestrator routing-surface remediation, NOT
                         fingerprint redesign, NOT Scientist activation, NOT BENCH-AB-001

MIRROR ACCEPT            REV-P5DOMAIN-MIRROR-001 @ 9d911449854380966cab8ba874d1634e2682cff4
  verdict                ACCEPT · read IN FULL at source on the mirror branch, with
                         learning/mirror/SLR-mirror-0017.md at the same commit
  bound to               930dfefb…6b97 @ base f70878d1, content tip ceefaa28, manifest tip dae0cca8
  verdict transfer       NONE — first review of this object
  findings               five non-blocking (N-1…N-5); N-1 declared the one Mirror came closest
                         to blocking on

AUTHOR RESPONSE          reviews/plan/AUTHOR-RESPONSE-P5DOMAIN-MIRROR-001.md
  commit                 3c4df9c4f3e76d5551d65d54b002d7f4ebc637c7
  status                 VALID · Annex C.2 obligation SATISFIED (silence is not acceptance)
  domain                 CONTROL_PLANE — reviews/ is a declared root, verified by parsing § P5
                         at the tip being hashed
  invariance             accepted content tip UNCHANGED · accepted manifest tip UNCHANGED ·
                         candidate hash UNCHANGED · no Revision 2 created
  closes A               C-9 §7.2 stale premise — ACCEPTED without qualification; registered in a
                         carried-debt register addendum and routed to the §7.2 closure package
  closes B               GATE 0 narrowed — ACTIVE-singleton MECHANIZED, write-location PROCEDURAL
  closes C               root-cwd narrowed — all six ACTOR worktrees in deployment_profile.md are
                         under the root; NOT all repository worktrees (7 of 14 are outside)
  closes D               path index is tip- and scope-dependent, and NON-NORMATIVE
  historical artifacts   no XPORT artifact edited; no closed review or response rewritten

SLR-plan-0010            NOT_CREATED
AUTHOR-RESPONSE
  SLR DEFERRAL           VALID — determined independently from current governance, not accepted
                         from Plan. (1) Body §21 makes durable persistence DISJUNCTIVE: "ogni
                         record MUST raggiungere lo stato durevole via WORK_COMMIT … o inclusione
                         nel prossimo candidate" — the deferral route is named in the frozen text.
                         (2) No condition of GATE 0–5 names a session learning record. (3) The
                         alternative is affirmatively FORBIDDEN: learning/ is CONTENT by intent,
                         so writing it on this branch would move the hash and void the ACCEPT
                         under Annex D.2. (4) The candidate DOES carry an SLR — SLR-plan-0009,
                         for the authoring session, curated by Mirror under E.2; what is deferred
                         is the record for the response session alone.
  residual               the obligation is CARRIED and OWED by Plan, not discharged. Orchestrator
                         did NOT create it; doing so would have changed the approved object

MAIN BEFORE              f70878d1cb98317ec62808987fc328be7f8f4ea8
MAIN AFTER               04693e683a254ff0a6d0619fba47103a0fb7d122
  parents                f70878d1cb98317ec62808987fc328be7f8f4ea8 (canonical main / BASE_HEAD)
                         3c4df9c4f3e76d5551d65d54b002d7f4ebc637c7 (approved branch tip)
SNAPSHOT                 snapshot/pre-CAND-20260819-P5DOMAIN @ f70878d1 — annotated tag object
                         2b510b493ef22c0aa37d494ed97d18658d362e72, tagged before anything applied

WORK SURFACE             branch orchestrator, worktree .claude/worktrees/orchestrator
BATCH SURFACE            root checkout, branch main
  execution semantics    DETERMINISTIC — Annex D.1 assigns WORK_COMMIT to the actor's own branch
                         and CANONICAL_BATCH_COMMIT to the root. No execution ambiguity arose.
  labelling              the stale `worktree: the repository root checkout` frontmatter in
                         roles/orchestrator.md was NOT treated as authority to collapse the two
                         surfaces, and was NOT repaired here

LEASE ACQUIRED           #9 @ c5b4864cb712585036a3e9902fa2587c4726ee8f
                         window 2026-08-19T20:12:15Z → 20:57:15Z
LEASE RELEASED           #9 @ c4c1b039184e04d2ef5441c3c82ee87f5973012e, 20:34:32Z, terminal
  singleton              0 ACTIVE before acquisition · exactly 1 during · 0 after — DERIVED at
                         each point, never read from the stored STATUS field. The derivation's
                         two findings are #3's, historical, and were NOT normalised
  exit-code contract     --check exits 1 on findings; the singleton INVARIANT exits 3 and did not
                         fire. Exit 1 was not misread as a singleton violation
  expiry mid-batch       NO — 22m43s remained at release
  🔴 WRITE SURFACE       branch orchestrator, path runtime/orchestrator_lease.md. NOT main, NOT
                         the candidate branch. LOAD-BEARING IN THIS BATCH SPECIFICALLY, because
                         the object canonicalized is the one measuring this path INSIDE the
                         content domain. Protection is PROCEDURAL and nothing checks it, so it
                         was MEASURED: binding reproduced 930dfefb… from the root checkout
                         immediately BEFORE the acquisition row and immediately AFTER it,
                         unchanged; root remained on main at f70878d1 with 0 entries

P5 SOURCE                governance/plan_defined_parameters.md § P5, canonical at BASE_HEAD
  version                legend-candidate-v4 — VERIFIED, unchanged by the candidate
  roots                  governance/candidates/ · ledger/ · reviews/ — identical when parsed at
                         BASE_HEAD, content tip, manifest tip and branch tip
  read from              the TIP being hashed, by the script; never from any checkout
  script blob            cd5776d329bc7c93d43807aeddaac43752dcbadf — IDENTICAL at all four commits
  historical correction  recorded: the canonical script has read the rule from the tip since
                         b2c326b. Mirror's earlier account that a stale working-tree P5 ALONE
                         produced the 533-path result was INCOMPLETE — that bad reproduction
                         required BOTH a stale P5 v3 AND the older script behaviour. Historical
                         review preserved unchanged; the CURRENT mechanism was used here
  population             533 included · 40 excluded @ content tip

P5 BINDING PRE-BATCH     PASS
  reproduced at          ceefaa28 · dae0cca8 · c9de1348 · 3c4df9c4 — same digest, included 533 at
                         all four. Excluded rises 40 → 44 → 44 → 45 as control plane accrues;
                         INCLUDED NEVER MOVES, which is the invariance the design requires
  independent route      re-implementation importing nothing from the script, roots and version
                         transcribed by eye from canonical § P5, git via argv and never a shell:
                         57504 bytes, 533 included, same digest
  🔴 PRE-IMAGE           BYTE-IDENTICAL — cmp of the script's --emit-domain bytes against the
                         independent serialization, 57504 vs 57504. Digest equality alone was not
                         relied on: two implementations agreeing on a digest can be one
                         implementation run twice
  positive control 1     XPORT revision 2 @ base 4454feab tip e839db38 → 81f241f2…6e1f,
                         532 · 38 — EXACT on both routes
  positive control 2     SCIAB @ base cbce3016 tip 2a854177 → beef6db0…6061, 527 — EXACT on both
  negative control A     BASE sensitivity, difference PROVEN FIRST — f70878d1 (tree 6f6bb1c8) vs
                         4454feab (tree c27a81ee), 13 differing paths → 326b1773… DISAGREES
  negative control B     INCLUDED-DOMAIN sensitivity, difference PROVEN FIRST — 2 differing paths
                         inside the domain → 06095c0c… DISAGREES, and independently reproduces
                         the value the candidate's own § P5 publishes for that probe
  neither is a parent shorthand; both had their input difference established before their
  disagreement was allowed to count

P5DOMAIN SEMANTICS       measured independently, not accepted from the manifest
  P5 PREMISE CONFLICT    CONFIRMED — exactly one tracked path under runtime/ at BASE_HEAD, not
                         git-ignored (check-ignore rc=1), in the index
  runtime lease          TRACKED · IN_DOMAIN — entry 496 of 533 at the content tip, enumerated
                         with a positive and a negative control on the extraction instrument
  FIXED-POINT HAZARD     CONFIRMED
  CURRENT MITIGATION     PROCEDURAL
  HAZARD MECHANICALLY
    ELIMINATED           NO
  CANDIDATE PURPOSE      TRUTHFULNESS_DISCLOSURE — not HAZARD_REMEDIATION
  P5 ALGORITHM           UNCHANGED
  P5 DOMAIN              UNCHANGED
  C-9 §7.2 RECLASSIF.    NOT ADOPTED

GATE 0                   PASS   BASE_HEAD as expected · root clean, 0 entries tracked AND
                                untracked · GOVERNANCE_VERSION 3.1.1 · lease derived ACTIVE
                                singleton · ONE_WRITER. Stated precisely: the ACTIVE-singleton
                                condition is MECHANIZED by lease_state.py, which enforces it as
                                an invariant in every mode; the write-location protection is
                                PROCEDURAL. GATE 0 is NOT reportable as "manual"
GATE 1                   PASS   proposer plan ≠ reviewer mirror ≠ adjudicator operator ≠
                                executor orchestrator
GATE 2                   PASS   LINT PASS (same single pre-existing INFO) · publication gate
                                PASS / BLOCKS 0 (same 4 [REVIEW] lines) · anchors PASS ·
                                128 receipts anchored — all re-run in this window, never
                                inherited from the manifest
GATE 3                   PASS   MIRROR ACCEPT + HUMAN_APPROVAL, both bound to this exact object;
                                author response delivered under C.2
GATE 4                   PASS   snapshot tagged at MAIN BEFORE before anything was applied
GATE 5                   PASS   merge proved to produce EXACTLY tree f450ec39 BEFORE it was made;
                                staged tree read back with write-tree and compared again before
                                the commit

APPROVED CONTENT →
  CANONICAL CONTENT      IDENTICAL — whole-tree diff against the approved branch tip is EMPTY;
                         canonical tree f450ec39d0ca58b3746602b2419b674a13289a9d. The CONTENT
                         difference from BASE is exactly the two accepted paths:
                         M governance/plan_defined_parameters.md · A learning/plan/SLR-plan-0009.md
CONTROL-PLANE CLOSURE    PASS — five control-plane paths, all under declared roots: the manifest,
                         the handoff, CHK-plan-0019, task P5DOMAIN-001 and the author response.
                         The branch tip was merged rather than the manifest tip because both
                         post-manifest commits belong to the candidate's durable control-plane
                         chain and neither moves the binding; merging the manifest tip would have
                         canonicalized a handoff still carrying an unresolved placeholder and
                         left the C.2-required author response outside canonical state
POST-BATCH P5            PASS — 930dfefb…6b97 reproduces against the new canonical main under
                         candidate-object semantics (base f70878d1 × tip 04693e68), 533 included.
                         Whole-new-main hash equality was NOT demanded and does NOT hold, as it
                         should not: BASE_HEAD is inside the hash
HISTORICAL CONTROLS      XPORT rev 2 → 81f241f2… · XPORT rev 1 → 68173f01… · SCIAB → beef6db0…
                         all still reproduce EXACTLY at the new canonical main

POST-BATCH SUITES        65          POST-BATCH TESTS   950
BASE FAILING SUITES      6  { framework/scripts/test_session_self_eval.py ·
                         scripts/test_abstract_corpus_is_not_evidence.py ·
                         scripts/test_fulltext_trace_contract.py ·
                         scripts/test_locator_obligation_reaches_every_route.py ·
                         scripts/test_release_runner_verdict.py · scripts/test_release_surface.py }
CANONICAL FAILING SUITES same 6, identical set
BASE FAILING TESTS       7  { test_diagnosis_is_wired_before_growth_and_takeaways ·
                         test_every_tracked_test_file_is_in_the_runner ·
                         test_normative_layers_make_receipts_universal ·
                         test_normative_write_rules_name_the_append_only_carveout ·
                         test_shebang_python_entrypoints_are_executable ·
                         test_the_bootstrap_bounds_the_corpus · test_the_bootstrap_states_the_rule }
CANONICAL FAILING TESTS  same 7, identical set
REGRESSION DELTA         0 — by SET, by TEST NAME, and by NORMALISED FAILURE REASON. Every failing
                         suite's output was normalised for path and elapsed time, digested, and
                         diffed: identical in all six. Counts alone were not relied on. All six
                         fail on pre-existing causes unrelated to § P5 — the CLAUDE.md router
                         migration, executable bits, and the runner inventory
LINT                     PASS
PUBLICATION GATE         PASS / BLOCKS 0
GROWTH ANCHORS           PASS 39/70/356/390
RECEIPTS                 128 chained, tail anchored

CORE FINGERPRINT BEFORE  plan          9c0c13fb2cba98bf4facfcb3a99bb75c7b1c21fe72cac087bd82c5b7d8af55ff
                         mirror        3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                         orchestrator  e2c544705e623a7761e627396724aab6fcb5a6f35466e6f1b978a0e8baaec59a
                         scientist     82423a48b700bc2b392b4c8e944eb6a0b07cefebddf63db00e96716cbed43e79
CORE FINGERPRINT AFTER   plan          0d6987bd79e54839cb33052b95bf85116d77c18537c27951fc08eeaefaec1429
                         mirror        e01b410891c4f3008b21418f695a4d60514b1810518b3c8d039bc8c6f08a0412
                         orchestrator  88dea7a635919c9faa73506f38a10aa5230011059d646885e86aa1c07b2a5ebb
                         scientist     b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
  method                 recomputed by the orchestrator with the canonical script (blob c6e05e10,
                         identical at both points) in a clean isolated clone at detached,
                         status-clean checkouts — not accepted from Mirror or Plan, which they
                         match exactly. The AFTER values were re-derived a second time at the
                         canonical surface after the batch and agree
FINGERPRINT ROTATION     EXPECTED_CANONICAL — all four rotate; cause isolated to
                         governance/plan_defined_parameters.md alone, in CORE, hashed whole.
                         learning/ is not a fingerprint input, so SLR-plan-0009 contributes none
FINGERPRINT CALIBRATION  CARRIED — OVER_SENSITIVE_CANONICAL. Composition NOT redesigned: A.6
                         gives DETECTION to Mirror and recalibration to Plan as a governed change
CHECKPOINT CONSEQUENCE   A.6 — RESUME-COMPATIBILITY ONLY. "la rehydration che trova … fingerprint
                         incompatibili NON riprende — segnala e chiede stato a Orchestrator."
                         Session IDENTITY unaffected (ACTOR_ID + worktree + contract, all
                         durable). Session ROUTING unaffected. Committed work unaffected. Fresh
                         rehydration unaffected. It is NOT true that all live sessions become
                         invalid, and A.6 does not say so
SCIENTIST A/B
  CHECKPOINT STATUS      SAFE — ledger/checkpoints/ holds plan/ ONLY. No mirror/, orchestrator/
                         or scientist/ directory exists, so there is no Scientist checkpoint to
                         invalidate and none to be silently reused later. Of plan's, CHK-0009–
                         0014, 0017 and 0018 record 9c0c13fb… and become resume-incompatible;
                         CHK-0001–0008 were ALREADY incompatible from two earlier rotations
WRONG-REASON
  LOAD-BEARING PASSES    0 — one extraction defect was hit (the over-matched failing set, §1
                         above), caught against the runner's own verdict block, and re-derived
                         with an anchored pattern plus positive and negative controls before any
                         conclusion rested on it. Specifically checked and clean: no shell
                         empty-output equality; no non-portable \b in a load-bearing path; no
                         stale script — every script blob was compared across the commits it ran
                         against; no wrong P5 source; no raw --emit-domain line number mistaken
                         for a domain index (headers stripped explicitly); no void negative
                         control; and `pytest` being absent from the interpreter was recorded as
                         a NON-RESULT rather than read as a pass

PATH INDEX               NON_NORMATIVE — nothing parses it; the hash is over ls-tree lines, never
                         over an ordinal. Independently reproduced: 494/531 @ XPORT rev 1 tip
                         f48a807 · 495/532 @ XPORT rev 2 and BASE_HEAD · 496/533 @ this
                         candidate's content and control-plane tips. The historical string
                         "496 of 532" corresponds to NO single valid tip — it pairs a raw line
                         number from one revision with a population total from another — and it
                         stands in three canonical files. NOT repaired: those artifacts are
                         closed and the value is non-operative
ORCHESTRATOR ROUTING-
  SURFACE DEBT           CARRIED — execution ambiguity NO, routing/label ambiguity YES. The
                         root-cwd claim stays narrowed to the six actor worktrees named in
                         deployment_profile.md; it is NOT stated of all repository worktrees,
                         7 of 14 of which are outside the root
ROUTING                  UNRESOLVED — no CURRENT routing, no registrar authority, no routing
                         generation, no supersession. The operator's manual delivery of this
                         instruction established a MANUAL EXECUTION ENDPOINT and nothing else
HISTORICAL SESSIONS      NOT_PERFORMED — none closed, killed, renamed, superseded or cleaned
BENCH-AB-001             NOT_STARTED — specification only (manifest, instructions, population,
                         surface spec); no run, result or output artifact exists, and
                         framework/eval/ is untouched by this batch
SCIENTIST A              NOT_ACTIVATED          SCIENTIST B   NOT_ACTIVATED
SCIENTIST C              EXISTING_UNTOUCHED — lettore-c at 908197ba, unchanged
D / E / F                NOT_CREATED

CARRIED, NOT REPAIRED
  C-9 §7.2 BODY          STALE_FALSE and asserted unrefuted at main. STATUS valid,
                         acceptance_is_not_adoption preserved, transition owner operator, hold
                         valid — all four verified at source. Text remediation is SEPARATE_DEBT
                         + HUMAN_REQUIRED. PROPOSAL-C9-STATE-MODEL.md byte-unchanged. The §7.2
                         closure package MUST NOT present that paragraph as current evidence
  P5 FIXED-POINT HAZARD  procedurally mitigated only; NOT mechanized in this batch
  FINGERPRINT CALIBRATION OVER_SENSITIVE_CANONICAL
  ORCHESTRATOR ROUTING   labelling/routing-surface semantics UNRESOLVED
  BUILD_MINIMAL_DIRECTORY OPEN — framework/state/actors.yaml still ABSENT, verified
  MULTI_AGENT_ARCH_FEAS. OPEN — preserved, not authorized, not started
  E5                     PARTIALLY_RESOLVED
  DANGLING MIRROR SLRs   CARRIED — Mirror-owned; LINT does not detect them
  HISTORICAL XPORT COUNTS CARRIED — "496 of 532" in three closed canonical files
  ROOT ENVIRONMENT       CARRIED — two suites enumerate the filesystem rather than git ls-files
  SNAPSHOT DEBT          CARRIED — four historical snapshot tags remain absent and were NOT
                         recreated; fabricating one today would assert a snapshot was taken then
  QUEUE DIVERGENCE       CARRIED — HUMAN_APPROVAL_QUEUE has divergent copies; main carries 6
                         lines, the orchestrator seat 10. NOT reconciled here
  SLR-plan-0010          CARRIED — owed by Plan, deferral VALID, obligation not discharged

FINAL STATUS             CAND-20260819-P5DOMAIN REVISION 1 CANONICAL
```

## CLASSIFICATION

```
CLASSIFICATION:      FAILURE_PATTERN — a forewarned instrument defect reproduced anyway, and the
                     defect returned a SUPERSET rather than a void
CONFIRMATION_CLASS:  REPLICATION of SLR-mirror-0017 / REV-P5DOMAIN-MIRROR-001 §10.3 and of the
                     L-3 shell-as-instrument class
                     ORIGINAL_OBSERVATION proposed (§2, sub-shape: symmetric over-matching is
                     invisible to the set comparison it corrupts)
                     ORIGINAL_OBSERVATION proposed (§3: the batch canonicalizing a disclosure
                     about a procedural invariant is the first experiment on that invariant, and
                     must measure it rather than restate it)
WIDER SCOPE:         yes for both — the first applies to any set-identity claim derived by
                     extraction, the second to any candidate that discloses a hazard it does not
                     mechanize, which is a class this laboratory is now producing deliberately
```

## ATTRIBUTION

The trap in §1 is **Mirror's**, published in `REV-P5DOMAIN-MIRROR-001` §10.3 before I met it. I
reproduced it rather than discovered it, and the honest finding is that having read the warning
did not prevent it — which is a fact about warnings, not about Mirror. The superset sub-shape and
the observation in §3 are mine. Plan's independent re-derivation of the fingerprints and the
`496` lineage in its author response were verified against my own and agree.

## EVIDENCE

```bash
grep '^- ' base_regressions.txt | sed 's/^- //; s/: exit.*//' | sort | wc -l     # 8 — over-matched
grep -E '^- [A-Za-z_./-]+\.py: exit [0-9]+$' base_regressions.txt | wc -l        # 6 — anchored
grep -cE '^- scripts/test_release_surface\.py: exit [0-9]+$' base_regressions.txt # 1 — pos control
grep -cE '^- scripts/test_public_release_gate\.py: exit [0-9]+$' base_regressions.txt # 0 — neg

python3 governance/scripts/candidate_content_hash.py --base f70878d1 --tip ceefaa2 --emit-domain \
  > canon.bytes ; cmp canon.bytes indep.bytes        # byte-identical, 57504 each
python3 governance/scripts/candidate_content_hash.py --base f70878d1 --tip 04693e68   # 930dfefb…
python3 governance/scripts/candidate_content_hash.py --base 4454feab --tip e839db38   # 81f241f2…

git ls-tree -r --full-tree f70878d1 -- runtime/     # exactly one path
git check-ignore -v runtime/orchestrator_lease.md   # rc=1 — NOT ignored
python3 framework/scripts/lease_state.py            # ACTIVE by derivation: 0 → 1 → 0; exit 0
python3 framework/scripts/lease_state.py --check     # exit 1 — #3's findings, NOT the invariant

git write-tree                                       # f450ec39 — compared BEFORE the commit
git diff --stat 3c4df9c 04693e68                     # empty — canonical == approved
```

## LEARNING_ID

```
LEARNING_ID:        LEARN-ORCH-004
ORIGIN_ACTOR:       orchestrator
CONTRIBUTORS:       mirror (REV-P5DOMAIN-MIRROR-001 §10.3, reproduced here)
FIRST_OBSERVED:     2026-08-19
EVIDENCE_COUNT:     1 extraction instance + 1 procedural-invariant measurement
OWNER:              durability — plan (E.2) · epistemic curation — mirror (E.2)
STATUS:             OBSERVED
AFFECTED_WORKFLOW:  any regression comparison, failing-set diff, domain enumeration or
                    "the sets are identical" claim derived by pattern extraction; and any batch
                    executing a candidate that discloses a procedural-only invariant
EXPIRY_OR_REVIEW:   at the first MIRROR_RETROSPECTIVE — cadence N remains UNRESOLVED (ESC-3)
```

> **Not indexed.** `LEARNING_INDEX` does not exist. The index fields are declared so indexing is
> mechanical when it is built; this record does not claim to be indexed.

> **Curation is Mirror's.** The two `ORIGINAL_OBSERVATION` proposals above are proposed, not
> ratified. Under Annex E.2 the epistemic classification belongs to Mirror, and I do not
> self-ratify my own learnings any more than Plan does.
