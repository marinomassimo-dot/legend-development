---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0014
actor_id: plan
role: Plan
date: 2026-08-20
task: ORCHSURF-001 · generation 4 — the ratified DEC-20260820-ORCH-SESSION-HOME built into
  CAND-20260819-ORCHSURF revision 4, bound, re-bound after an identifier redaction, handed to
  Mirror, and carried through REV-ORCHSURF-MIRROR-002 rounds 1 and 2 to closure
scope: revision 4 built and bound; the publication gate caught the ratification signature and was
  cleared by an operator-approved redaction; four Mirror findings and one adjudicator instruction
  accepted and remediated; nothing contested. NO FROZEN document touched, proposed for amendment
  or claimed superseded — verified mechanically across the whole range. ROOTGUARD NOT opened.
  No lease held, no approval requested, main UNCHANGED at 04693e68
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-1 is the entry I most expect to be contested, because it
  generalises from seven instances collected inside a single session by three actors who were all
  looking for it by the end
derived_from: [SLR-plan-0013, SLR-plan-0012, REV-ORCHSURF-MIRROR-002, REV-ORCHSURF-MIRROR-002-R2,
  OPEN-REV-ORCHSURF-MIRROR-002 and ADD-001…009, CLOSE-REV-ORCHSURF-MIRROR-002,
  DEC-20260820-ORCH-SESSION-HOME]
binding_note: THIS RECORD IS OUTSIDE THE CANDIDATE'S BOUND CONTENT. `learning/` is an INCLUDED
  entry of the candidate content domain, and this file is committed AFTER the review closed and
  AFTER `CONTENT_TIP 9a70e94d`. The binding
  `(04693e68, 9a70e94d) → 844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc`
  is a measurement over a fixed pair and remains true and unaffected. But a reader fetching the
  BRANCH TIP now gets domain content the binding does not cover and the review never examined.
  That is stated here rather than discovered, because it is this session's own finding pointed at
  this session's own record: a surface and an instant, or the number means nothing
---

# SLR-plan-0014 — every instrument was working, and four of seven were measuring the wrong thing

## WORK COMPLETED

The ratified operator record was built into content, bound, re-bound, reviewed twice and closed.

```
CONTENT       BOOTSTRAP.md · deployment/deployment_profile.md · roles/orchestrator.md
              the BLOCKED_BY_GOVERNANCE stop removed; step 3 narrowed to Annex I.2's five;
              step 11 ADDED and declared as new; SESSION HOME typed as a fourth concept
BINDING       (04693e68, 1a650d85) → 79af3e52, then (04693e68, 9a70e94d) → 844de909 after the
              identifier redaction moved an included domain entry
REVIEW        REV-ORCHSURF-MIRROR-002 rounds 1 and 2 → M-1…M-4 + R-1, all accepted, none
              contested, CLOSE @ 0a1929e
FROZEN        untouched across the entire range, verified by git diff over the body and A–J
NOT DONE      no lease, no approval, no canonicalization, ROOTGUARD unopened, six items owed
```

## PROBLEMS

**P-1 · The precedence clause resolved conflicts and could not reach silence.** I built a
three-layer package — operative §1+§17, historical §§2–15, resolved findings §17.1 — and routed it
with *"where they conflict with this section, this section governs."* Mirror's M-1 found that
§§11 and 16 stated `ORCHESTRATOR SURFACE = PARTIALLY_RESOLVED — HUMAN_REQUIRED` while §1 and §17
stated **no status at all**. Where the governing layer is silent there is no conflict, so the
superseded statement stood unopposed on the one question the package existed to answer. **I named
this exact hazard as attack 6 in my own handoff and still could not see the instance.**

**P-2 · A findings ledger relied on as an assertions ledger.** §17.1 is titled *"Every revision-3
FINDING"*. The mandate asked whether it disposed of every **assertion** §§2–15 make. Different
sets, and all four findings lived in the difference.

**P-3 · Evidence cells surviving the deletion of their evidence.** §9 recorded T7 and T8 as PASS,
citing a STOP at line 90 and `UNTIL RESOLVED` at line 154. Revision 4 deleted both: at CONTENT_TIP
`grep -c` returns **0** for each. Two load-bearing passes resting on artefacts the same revision
removed, inside a package whose §9 closes with `WRONG-REASON LOAD-BEARING PASSES 0`.

**P-4 · A derived statement not following its source.** §17.3 asserted, in the present tense, that
the publication gate does not pass — while §1, one section away, recorded `PASS · 0`. I corrected
§1 when the redaction cleared the block and left the sentence **pointing at §1** uncorrected. Both
Layer 1, so precedence had nothing to resolve; structurally identical to P-1.

**P-5 · A window published as a population.** I reported eight commits on branch `orchestrator`
from a truncated `git log -8`. `git rev-list --count main..orchestrator` returns **19**. Caught by
me before it reached a reviewer, which is precisely why no second actor raised it.

**P-6 · A corrected count that inherited the same defect.** I called `BLAST RADIUS 5`
*arithmetically wrong* and offered three. Both were unstated over their population. §8 is headed
*"at revision 2"*, where five reproduces; and my three excluded the DEC, a content-domain file
revision 4 also edits. Then row 4 of the very block written to state populations carried
`537 → 539` under a header declaring `BASE..CONTENT_TIP`, where the count is `533 → 539`.

## SOLUTION

Every finding accepted, none contested, all remediated in the control plane so the binding never
moved: §17.1a states the operative status; §17.1 splits the row whose conflation caused P-3 and
withdraws T7/T8's results while preserving their method; §17.3 discloses that T1–T10 were not
re-run and is now past tense on the gate; the population block enumerates four surfaces and names
what each excludes.

**Two things I did NOT do, and both were rulings I asked for rather than took.** I did not re-frame
T7 inside the candidate — routed to the adjudicator, which ruled withdrawal on a better ground than
mine: the answer is now *entailed by the design under test*, so the test no longer discriminates
and any PASS is unearned by construction. And I did not write this record while the review was
open, because `learning/` is inside the hashed domain and writing it would have moved the binding
mid-round.

## LEARNING

**L-1 · An instrument reporting faithfully about the wrong object is invisible to running it more
carefully.** Seven instances this session, across three actors:

```
1  CANDIDATE_CONTENT_HASH, invariant across control-plane commits BY DESIGN        orchestrator
2  line anchors valid only against a surface not carried with them                 orchestrator
3  a superseded verifier on a reviewer's own branch                                mirror
4  testimony standing where measurement was available                              plan
5  `git log -8` published as a population                                          plan
6  a grep for `PROBLEM DECLARED NOT SOLVED` against a document holding the comma   orchestrator
7  a population failure about to be filed as an arithmetic one, by the actor who
   had just ruled against exactly that, while applying the rule                    orchestrator
```

None returned a wrong value. Each answered its question correctly about something other than the
intended object. **The discriminating question is *what surface is this actually measuring*, and
it is a question an instrument cannot ask about itself.** `CONFIRMATION_CLASS: proposed`.

**L-2 · Recording a rule does not cause it to be applied.** Instance 7 is the evidence and it is
stronger than the other six: the adjudicator had written the rule one record earlier, from a
control Mirror supplied against its own assertion, and then reproduced the error while applying
that rule. **If a rule cannot survive contact with the person who just wrote it, "record the rule"
is not the mitigation.** Every mitigation this session actually produced has one of two shapes — a
second actor who did not share the first's assumption, or a mechanical check of the other
population before the claim was written. **None of them is "be more careful."**
`CONFIRMATION_CLASS: proposed`.

**L-3 · A population needs a surface AND an instant.** My 19 was right in the surface dimension and
unspecified in the instant; it measures 27 once the adjudicator's own addenda land. `git log -8`
was wrong in the surface dimension. Same defect, two axes, and I had seen only one.
`CONFIRMATION_CLASS: proposed`.

**L-4 · A precedence rule needs a completeness rule beside it.** Layering that routes by priority
has a hole wherever the governing layer says nothing, and the hole is invisible precisely because
precedence *looks* total. Both P-1 and P-4 are this. `CONFIRMATION_CLASS: proposed`.

**L-5 · `SLR-plan-0012` L-1 has an inverse, and it cost as much.** L-1: a claim removed from a
derived document is not thereby removed. The inverse, P-4: **a claim corrected at its source is not
thereby corrected where it was echoed.** Neither is caught by re-running anything.
`CONFIRMATION_CLASS: proposed`.

**L-6 · A record edited to agree with its own derivation has stopped being evidence.** From lease
#3, which stores `EXPIRED` — outside Annex I.3's vocabulary — and derives `STALE`. I raised it
twice as an observation; it is deliberately preserved, and the correct act is to **block** anyone
tidying it. `CONFIRMATION_CLASS: proposed, and the closest to already-held of the six.`

**L-7 · A pattern assembled only from instances a second actor caught is itself an instrument
measuring the wrong object.** Instance 5 was mine and self-caught, so no reviewer would ever have
supplied it. Adding it was the only way the count was measured over the population rather than over
the reports. `CONFIRMATION_CLASS: proposed`.

## MICRO-UPGRADE

**Adopted this session, and already exercised in both directions.** When committing during an open
review, **announce the tip change AND publish the object blob.** The announcement is testimony —
it depends on the sender being honest, remembering, and still existing. The blob is measurement and
survives all three failing. Two channels, one independent of the sender.

It proved itself inside three exchanges: at `5ea744c` the blob was unchanged and the adjudicator
skipped a re-bind it would otherwise have taken; at `f627ea5` and `5a69a05` the blob had moved and
told it not to skip. **The rule earned its place by firing in both directions, not by being
plausible.**

**Offered, not adopted:** a candidate that layers historical against operative text should carry a
completeness obligation, not only a precedence clause — an explicit statement of which questions
the operative layer must answer, so silence is a detectable defect rather than an unreachable one.
That is L-4 made procedural, and it belongs to Mirror to accept or reject, not to me to install.

## IMPACT

```
FINDINGS ACCEPTED        M-1 · M-2 · M-3 · M-4 · R-1 — five, none contested, none adjudicated
                         against me because I disputed nothing that was right
RULINGS REQUESTED        two, both where the judgement was mine to make and better made elsewhere:
                         the T7 re-framing, and the scope of the §8 population correction
IMPROVED ON A RULE       twice — "announce the tip change" → announce AND publish the blob; and
                         "silent instrument" → BLIND instrument, since the property that makes the
                         hash a good binding is the same property that makes it a bad tripwire
FROZEN                   untouched, verified mechanically, across every commit of this session
BINDING                  never moved by any remediation; all of it landed in excluded paths
GATE                     caught the ratification signature carrying a registered private
                         identifier into public canonical content, BEFORE canonicalization.
                         Cleared by operator-approved redaction. Three hashes recorded for one
                         record, because ratification attaches to the pre-signature content
```

## CLASSIFICATION · SCOPE · EVIDENCE

```
OUTCOME              MICRO_UPGRADE (announce + blob, exercised in both directions)
                     + six proposed learnings, curation Mirror's under E.2
NOT CLAIMED          that the package may be canonicalized. The cycle establishes that it was
                     EXAMINED. HUMAN_APPROVAL on a MAJOR is the operator's alone, and
                     canonicalization additionally requires a lease and GATE 0–5 — neither exists
                     nor is claimed by anyone in this chain
NOT DISCHARGED       PROBE-ORCHWT-001 leg 3 · the Orchestrator's undeclared WORK_COMMIT capability
                     · Plan's cross-worktree write refusal · the regression suite · SLR-ORCH-005
                     · and this record's own successor obligations
EVIDENCE             every claim above is reproducible from the repository at branch
                     orchestrator-surface and from branches `mirror` and `orchestrator` at the
                     refs the closure names. The counts in L-3 and P-6 were re-measured at close
                     rather than carried from the messages that reported them
```
