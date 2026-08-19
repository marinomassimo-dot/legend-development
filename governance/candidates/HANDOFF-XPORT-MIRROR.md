---
artifact: MIRROR REVIEW PACKAGE — manual handoff, not an actor-routed send
handoff_id: HANDOFF-XPORT-MIRROR
candidate: CAND-20260819-XPORT revision 1
from: plan
to: mirror — DELIVERY IS THE OPERATOR'S, deliberately. See §0.
opened_by: nobody yet. Annex C.3: a review is opened only through Orchestrator.
date: 2026-08-19
domain: CONTROL PLANE — governance/candidates/ is a declared CONTROL_PLANE_ROOT (P5.1)
---

# Review package — `CAND-20260819-XPORT`

## 0 · 🔴 Why this is a file and not a message

The candidate's own protocol §9 says an actor-routed send must resolve its target at send time
against governed routing state, and that no such state exists. Design record §6 measures the
consequence: **seven live sessions in Mirror's worktree**, and nothing anywhere records which is
Mirror. Sending this to one of them would be electing a target by guesswork, in the same session
that argues guesswork is the defect.

So the package is a durable artifact and the notification is the operator's to make. **That is
the protocol behaving as written, on its own first use** — and it is also `T-TRANSPORT-1`
recorded as `NOT RUN` rather than passed.

## 1 · The object

```
CANDIDATE_ID            CAND-20260819-XPORT · revision 1
BRANCH                  xport
BASE_HEAD               4454feab72b7a0edf65f191be62aeedd899a15ad   (canonical main)
CONTENT_TIP             f48a807f7ba7b5b71c0ba5dd5d2361fc7dca57e4
MANIFEST_TIP            6ce65f6a57f8b3cc2ab1aaac1889fc7129acfe95
CANDIDATE_CONTENT_HASH  68173f010392e57b1b7cf252df6efa8b6fe7c017f563584bf3cd10695978c96a
CANDIDATE_HASH_VERSION  legend-candidate-v4      531 included · 37 excluded at the manifest tip
CHANGE_CLASS            MAJOR
REVIEW FLOOR            R4 METHOD (Mirror) — Annex C.1; Annex G.1 MIRROR_REQUIRED
HUMAN_APPROVAL          none. Not requested, not prefilled.
```

**Read at source, from the branch, without merging:**

```bash
git show xport:governance/candidates/CAND-20260819-XPORT.md
git show xport:framework/protocols/cross_session_transport.md
git show xport:governance/design_records/runtime_harness_probe_20260819.md
git show xport:reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md
git show xport:learning/plan/SLR-plan-0007.md
git show xport:learning/plan/SLR-plan-0006-COR-001.md

python3 governance/scripts/candidate_content_hash.py \
    --base 4454feab72b7a0edf65f191be62aeedd899a15ad --tip 6ce65f6a
```

## 2 · What to attack — TRANSPORT

1. **Size and rejection.** `to` rejects at 213 characters; `summary` declares `maxLength: 200`
   and accepted 264 silently. The protocol concludes that a declared bound may not be enforced
   and that enforcement is established per field, per version. Is that the right generalisation
   from two fields, or is it one measurement wearing a rule?
2. **`message` has no bound and none was probed.** The protocol sets no numeric budget and says
   why. Attack the refusal: is `UNKNOWN` the honest answer, or an unprobed gap dressed as
   discipline?
3. **Version-bound claims.** Every runtime guarantee is bound to `2.1.232` and to the *session's*
   version, not the machine's. Four extension versions are installed and at least two host live
   sessions. Does the revalidation rule actually bite, or is it a sentence nobody will run?
4. **Durable artifact vs message body.** §1.3's deletion test — *delete the body, keep the
   pointer, does the handoff still work* — is the whole enforcement. Is it checkable by anyone
   other than the author?
5. **Recipient-side processing.** The protocol cites `KERNEL_SPEC`'s classes rather than
   restating them, including `MESSAGE_TURN_TRUNCATION`. Is citing a non-normative launch spec
   from a normative protocol sound, or does it import an unreviewed artifact into canon?
6. **ACK.** §8 requires the ACK to be *durable* for authoritative content. Annex B.3 requires an
   ACK and does not say durable. Is that a minimal extension or a new requirement wearing one?
7. **Wrong-reason successes.** `T-TRANSPORT-4`, `-6`, `-7` and `T-DEPTH-1` are marked **PASS by
   construction**. Four of eight tests passing by construction is a claim that the design cannot
   fail them. Attack each.

## 3 · What to attack — ROUTING, which is analysis and not content

Everything in manifest §8–§10 is control plane and binds nothing. It is here to be reviewed
because the partition decision rests on it.

1. **Activation authority.** A / B / C compared on nine dimensions. C is recommended *as a
   direction*, with three falsification attempts recorded. Was C attacked hard enough, or is the
   fact that `scientist_reading_modes.md` §1.3 already canonicalized a two-seat shape doing the
   arguing?
2. **Self-promotion.** Model B is rejected as constitutionally impossible while being the model
   the harness supports best. Is that the right trade, or is the constitution being read too
   strictly against the only mechanism with a real CAS?
3. **`O_EXCL` and Annex J.0.** The design record says J.0's *"no compare-and-swap"* row is about
   the lease over the shared root and stands, while `legend_launch.sh` demonstrably uses an
   atomic create-or-fail for a per-actor file. Is that a legitimate narrowing or a J.0 violation?
4. **Registrar self-reference.** Resolved as `EXPLICITLY_RELATED`, reusing the lease rather than
   building a second singleton, with all five cases walked. Attack the consistency rule: *on
   disagreement neither is used.* Does that fail closed, or does it deadlock?
5. **One-current is declared `ADVISORY`.** There is no detector because there is no record to
   count. Verify Plan does not anywhere call it enforced.
6. **`PROVISIONAL` ≡ J.2 `BOOTSTRAPPING`.** Load-bearing for the generality claim, because it is
   what makes "no new lifecycle state" true. Is the mapping honest?

## 4 · What to attack — THE PARTITION ITSELF

The four questions Plan most wants answered are in manifest §10.3, and the second is the one
that matters:

> **Is Routing genuinely blocked, or is there a narrow scoping that sits inside Plan's authority
> and touches none of the four holds?**

If such a scoping exists, this session's central decision is wrong. The four holds are quoted at
source so each can be contested separately:

```
C-9 §7.2                            acceptance_is_not_adoption: true, explicit hold
BUILD_MINIMAL_DIRECTORY             PROVISIONAL pending operator acceptance; actors.yaml absent
MULTI_AGENT_ARCH_FEASIBILITY        PRESERVED, NOT AUTHORIZED, NOT STARTED
Phase −1 E5                         central negative falsified; needs re-running
```

## 5 · What to attack — GENERALITY

1. **Scientist D falsifier: `GENERALITY: PASS`**, qualified because steps 7–9 are generic *by
   design and not yet by implementation*. Is a `PASS` with that qualification meaningful, or
   should it be `NOT_TESTABLE`?
2. **No A/B hard-coding.** Plan states the transport protocol contains no occurrence of
   `scientist-a`, `scientist-b`, `BENCH-AB-001` or `lettore`. Falsify it by grep.
3. **The seven-actor matrix.** Orchestrator is the only special case, on four named grounds. Is
   the special case justified or overgeneralized?
4. **Scope creep.** `learning/plan/SLR-plan-0006-COR-001.md` is a second artifact in a session
   asked for an author response. Manifest §0.4 of the response flags it and states the
   alternative that was refused. Judge the choice, not only the content.

## 6 · The falsified-premise question, which Plan could not decide alone

Manifest §7: five artifacts, one of them **canonical**
(`framework/protocols/scientist_reading_modes.md` §1.2), state that no actor can observe its own
`SESSION_REF`. `claude agents --json` returns this session's own row. Plan corrected **none** of
them, on the ground that the conclusions are unaffected and that correcting canonical text
belongs to the candidate that needs the capability.

**Is that under-reaction?** A canonical protocol carries a false sentence today. The argument for
leaving it: the position it supports is right, and editing canon to fix a reason is a governed
change with its own review. The argument against: a false canonical sentence is quoted forward,
and this is the third document in a chain where exactly that happened.

## 7 · Evidence Mirror should re-run rather than read

```
python3 framework/scripts/legend_lint.py .                    → PASS, 1 pre-existing INFO
python3 scripts/public_release_gate.py                        → PASS / BLOCKS: 0
python3 framework/scripts/growth_anchors.py check             → PASS 39/70/356/390
python3 framework/scripts/fulltext_receipts.py verify         → 128 chained, anchored
python3 scripts/run_release_regressions.py                    → 65 suites, 953 tests, 6 red
python3 governance/scripts/governance_fingerprint.py compose --all
claude agents --json                                          → the cardinalities of §6
git worktree add --detach <tmp> 4454feab && (cd <tmp> && python3 scripts/run_release_regressions.py)
                                                              → the same 6 red, SET-WISE
```

**The regression comparison is set-wise.** Two runs with equal failure counts over different
failures pass a count check and fail this one. Re-run it that way.

## 8 · What this package does not ask for

- **no `HUMAN_APPROVAL`.** None exists, none is prefilled, and Plan does not request one here.
- **no review opened.** Annex C.3 gives that to Orchestrator.
- **no verdict transfer.** Nothing from `GOV311`, `HASHDET`, `P51C9`, `ORCHWT`, `SUNSET-DEC3` or
  `SCIENTIST-AB-SPEC` carries into this object.
- **no activation of anything.** `BENCH-AB-001` is not started, no Scientist is activated, and
  `main` is unchanged at `4454feab`.
