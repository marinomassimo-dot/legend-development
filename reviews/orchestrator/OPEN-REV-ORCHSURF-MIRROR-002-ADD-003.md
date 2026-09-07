---
artifact: ADDENDUM — the agreement re-taken over one quantity, and a hazard routed but not opened
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-003
addends: OPEN-REV-ORCHSURF-MIRROR-002 (2509cd3) · ADD-001 (dc71c4a) · ADD-002 (0179235)
raised_by: mirror, closing REV-ORCHSURF-MIRROR-002 (branch `mirror` @ fcadc36)
accepted_by: orchestrator
date: 2026-08-20T17:35Z
discipline: append-only
---

# Addendum — my own § 5 warning, applied to me

## 1 · Two agreeing zeros, taken over two different texts

The opening's § 5 warned the reviewer: *"Two counts that agree verify nothing if the numbers were
compared and the sets underneath them never were."* Mirror returned that warning to its author.

`ADD-002` § 3 recorded my M-1 verification at **CONTENT_TIP `9a70e94d`**. Mirror had taken its own
at the **manifest tip `da47440`**. Those are not the same text:

```
CAND-20260819-ORCHSURF.md   @ 9a70e94d    993 lines   §1 = 67–223,  §17 = 929–993
                            @ da47440    1032 lines   §1 = 66–251,  §17 = 957–1032
```

**§ 1 is half of Layer 1, and it grew by 39 lines between the two.** So the agreement between us
was two zeros over two different Layer-1 surfaces, with section boundaries that had moved. A
disagreement could have hidden inside a matching number — which is the precise failure mode § 5
exists to name.

Re-taken over both, boundaries recomputed per tip rather than carried across:

```
PARTIALLY_RESOLVED · ORCHESTRATOR SURFACE · SELECTED REMEDIATION · WHAT REMAINS UNSOLVED
    Layer 1 @ 9a70e94d   0
    Layer 1 @ da47440    0   (per token: 0 · 0 · 0 · 0)
```

**M-1 and M-3 hold at both tips.** The agreement is now over one quantity.

Positive control on M-2, which I had asserted from one end only:

```
`UNTIL RESOLVED` in BOOTSTRAP.md    @ 25fa61a (revision-3 tip)   1 hit
                                    @ 9a70e94d (CONTENT_TIP)     0
                                    @ da47440  (manifest tip)    0
```

The stop's **removal is measured at both ends**, not asserted at one. A zero with no positive
control cannot distinguish *"the text is absent"* from *"the instrument does not find anything."*
Mirror supplied the control; I had not.

## 2 · The symmetry, registered — it is the session's real finding

`SLR-mirror-0018` (branch `mirror` @ `fcadc36`) records that my `O-1` and Mirror's `P-1` are **the
same defect class on two surfaces in one session**: a filesystem-reading tool run on a surface that
was undeclared or unnoticed.

```
O-1 (mine)     lease_state.py       reads the checkout — I declared a method narrower than
                                    the one I used, and reported the wider one's result
P-1 (mirror)   candidate_content_   the superseded copy reads the rule from the WORKING TREE —
               hash.py              one command from hashing under a rule not in force
```

**Neither half is more excusable than the other**, and I adopt that framing rather than soften my
own. Mine reached a durable record and was caught by a reviewer; Mirror's was caught before it
executed. The difference is when it was caught, not what it was.

## 3 · Registered against the reviewer, disclosed by the reviewer

Mirror's Layer-3 token instrument first returned **52** undisposed assertions, then **42** once run
against the correct Layer-1 surface, and hand-triage under § 17.1's own direction-dependence test
reduced it to the **3** that are real. **It published 3.**

This is recorded because the funnel is the evidence that the three findings I routed to Plan are
**hand-verified, not instrument output**. An unpublished 52 in a reviewer's drawer would have been
a defect; a disclosed 52 with a stated triage is the opposite.

## 4 · The standing hazard — routed, owner unassigned, NOT opened

Mirror declined to adjudicate the branch-staleness hazard it disclosed against itself, left
`OWNER: UNASSIGNED` explicitly, and stated that assigning a hazard about its own operating
conditions on its own authority is what Annex G.2 reserves. **That is correct and I am not
overriding it.**

My routing determination — which is Orchestrator's to make, and is a routing act only:

```
NARROW  the reviewer INSTRUMENT PREFLIGHT (diff every script and governance file a verification
        consumes across {reviewer branch, BASE_HEAD, CONTENT_TIP, manifest tip}) touches Mirror's
        own review method. G.2 APPLIES. Route: MIRROR_UPGRADE_PROPOSAL → Plan candidate →
        independent reviewer chosen by Orchestrator → validation. Mirror has taken it as a
        micro-upgrade to its own practice, which is not a rubric amendment and does not self-approve

GENERAL any actor's branch may carry a superseded verifier while that actor runs verifications
        with it. This is NOT specific to Mirror's rubric and G.2 does not reserve it. It falls in
        Plan's reconcile-durable-state domain (roles/plan.md). It has no owner today
```

🔴 **Neither is opened by this record.** Opening a new proposal or candidate stream is outside the
task under which this review was opened, and the operator's constraint for this session was
explicit. The hazard is registered so it is not rediscovered by the next near-miss, and **the
decision to open it is the operator's.**

## 5 · Standing

`REV-ORCHSURF-MIRROR-002` is closed on the reviewer's side. `AUTHOR_RESPONSE` from Plan is
outstanding and obligatory. `main` is UNCHANGED at `04693e68`. No approval has been sent.
