---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0013
actor_id: plan
role: Plan
date: 2026-08-20
task: ORCHSURF-001 · generation 3 — adjudication of CAND-20260819-ORCHSURF against
  DEC-20260820-ORCH-SESSION-HOME, an operator architectural intent that inverts the remediation
  direction of revisions 1–3 without disturbing any of their measurements
scope: the operator record registered and marked UNRATIFIED; every section reference it makes
  re-verified at source; four findings produced by that verification; every revision-3 finding
  sorted by whether it depends on the remediation direction; the revision-4 change set specified
  and held. No content file was edited. No FROZEN document was touched, proposed for amendment,
  or claimed superseded. Revision 4 was NOT bound. Routing NOT opened. ROOTGUARD NOT designed
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-1 is the entry I most expect to be reclassified, and the
  reason is stated in REVIEW.
derived_from: [SLR-plan-0012, SLR-plan-0011, SLR-plan-0010-COR-001, REV-ORCHSURF-MIRROR-001,
  DEC-20260820-ORCH-SESSION-HOME]
---

# SLR-plan-0013 — three revisions cited the section that refutes them, for the one clause that does not

## WORK COMPLETED

`PREP-20260820-ORCHSURF-REV4` and the registration of `DEC-20260820-ORCH-SESSION-HOME`. No
revision 4. The operator record is unratified by its own §6, and a bound candidate resting on an
unratified premise is revision 1's error with the sign flipped, so the preparation is complete
and the binding is held.

The record asked to be verified against source before reuse. Verifying it produced four findings,
and the first is the one that matters: **body §8 already states the architecture the record
proposes**, and the ORCHSURF package cites body §8 twice — both times for a subordinate clause,
in support of the opposite conclusion.

## PROBLEMS

**P-1 — I read §0.2 because Mirror's finding pointed at it, and never read the section titled
with the subject.** Body §8 is titled *"ORCHESTRATOR — ROOT, AUTORITÀ, IDENTITÀ"*. Its first
sentence is *"Orchestrator vive nella chat grafica associata a `<REPO_ROOT>`"*; its second
paragraph is *"La posizione nella root NON conferisce autorità (§0.2)"*. Three revisions and one
hostile review searched `governance/` for the root-promotion mandate and reached §0.2, §0.4, §47
and Annex I.2 — the four passages that describe the **bootstrap procedure**. None reached the
section that describes the **steady state**, and the steady state is what the candidate was about.

**P-2 — the package quoted §8 against itself and nobody noticed, including me at revision 3 when
I was re-reading the package adversarially.** Manifest line 209 and author-response line 102 both
read *"body §8 obliges it to produce durable output"*, used to argue that the root cannot host the
Orchestrator. The obligation is real and it is thirteen words below the sentence that says the
Orchestrator lives there. A citation that reaches a section and takes one clause out of it is
worse than a citation that never reached the section, because it produces a false record of
having read it.

**P-3 — the load-bearing premise was falsifiable in ninety seconds and no one tried for three
revisions.** *"An Orchestrator living in the root had no branch on which a `WORK_COMMIT` was
possible"* is canonical at `main`, was compressed by revision 1, corrected by Mirror as N-3,
restated by me as *the sound form*, and accepted by Mirror as *"the stronger route"*. It is false:
a process whose cwd is the root can commit on another branch in another worktree and leave the
root clean. I ran that test this session in a throwaway repository. **Four passes over this
sentence treated it as the thing that survives scrutiny, and none of them executed it.**

**P-4 — my own stopping rule did not discriminate, and I published it as the check.** Revision 3
§5.5 and `SLR-plan-0012`'s micro-upgrade both terminate the upward walk at *"a document with no
`authority:` field"*. All eleven FROZEN normative governance documents have no `authority:`
field. The rule terminates everywhere and therefore nowhere. What rescued revision 3 was reading
`BOOTSTRAP.md` line 5 past the semicolon; the terminus rule contributed nothing and I credited it.

**P-5 — T10 escaped the trap it was built for and re-entered it one axis over.** T10 enumerates
its document universe from the tree, which is why it beat T7/T8. Its five search terms came from
the candidate's own vocabulary. Body §8 contains none of them. **The universe I remembered to
enumerate was the one I had just been caught on.**

## SOLUTION

The record was registered as received and marked `RECEIVED — NOT RATIFIED`, with a Plan block
naming the single missing input and stating that Plan does not infer ratification from the fact
that the operator transmitted the record.

Every section reference was read at source and tabulated with its verbatim text. The four
findings are stated with the evidence that produced them: an enumeration of every `§8` occurrence
across seven documents, read individually rather than counted; a mechanical falsification run in
a throwaway repository so that no actor's surface was touched; a frontmatter census over eleven
documents; and a reproduction of T10 that confirms its counts and then tests its vocabulary
against the passage it missed.

Every revision-3 finding was sorted by one explicit test — **does it depend on the remediation
direction?** Eleven survive unchanged, seven invert, and the split is published as a table so a
reviewer can attack any row of it rather than the conclusion.

## LEARNING

**L-1 — a citation is evidence of reading a clause, not of reading a section.** The package
contains two citations of body §8 and no reading of body §8. Where a document is cited for a
subordinate clause in support of a conclusion the section's own topic sentence contradicts, the
citation is not weak evidence of having read it — it is **positive evidence of not having**, and
it is invisible to every check that looks for whether a source was named. The check that catches
it is: for each cited section, read the section, not the sentence.

**L-2 — when a search finds the procedure, ask whether the subject also has a steady state.** The
mandate was hunted through four bootstrap passages because a bootstrap defect was the finding.
The same subject had a section describing what is true *after* bootstrap, and that section was
where the architecture lived. Procedures and steady states are different genres of text about one
subject, and a sweep tuned to one is blind to the other by construction.

**L-3 — a premise that can be executed should be executed before it is defended.** The
`WORK_COMMIT` impossibility claim survived a compression, a hostile review, a correction and an
adversarial self-review, and was defeated by running it. Every actor in the chain reasoned about
it correctly from a false premise. Where a claim is about what a tool **can** do, argument is the
second-best instrument and the first one was available the whole time.

**L-4 — a rule offered as a stopping criterion must be shown to stop somewhere and not elsewhere.**
`SLR-plan-0012` proposed the `authority:`-terminus as a `PROVISIONAL_OPERATIONAL_PRACTICE` with a
success criterion about what it would find. It had no criterion about **discriminating**, and it
discriminates nothing. A detector's first test is not "does it fire on the case I have" but "does
it decline to fire anywhere else" — which is the negative control, and I supplied one for T10 and
none for this.

**L-5 — enumerating one dimension of a search from the tree does not make the search exhaustive.**
T7/T8 inherited the document list; T10 fixed that and inherited the vocabulary. A sweep is as
exhaustive as its **narrowest inherited dimension**, and fixing the dimension you were last
caught on is the move that feels like rigour and buys the least.

**L-6 — an operator decision that confirms existing law still has to be checked against it, and
the check can strengthen it.** The record classified itself as a CONFIRMATION and named four
passages. It missed the one that confirms it most directly. Verification of an operator record is
not deference or challenge; here it produced better grounds for the operator's own position than
the record carried.

## MICRO-UPGRADE

**Adopted, and stated as a correction to `SLR-plan-0012`'s practice rather than an addition to
it.** The upward walk terminates at the document a mandate can **originate** in, and the field
that detects it in this repository is **`body:`** — carried by all ten annexes, absent from
`GOVERNANCE_v3.1.1.md`, a clean 1-vs-10 split — and **not** `authority:`, which is absent from
all eleven and discriminates nothing. Success criterion unchanged; **a discrimination criterion
is added**: the detector must be shown to decline on the documents that are not the terminus,
before it is used on the one that is.

**Second, paired, because L-1 is what actually cost three revisions:** when a section is cited in
a candidate for a clause, the section is read whole and its topic sentence is recorded in the
evidence beside the clause. If the topic sentence bears on the conclusion, that is a finding
before it is a citation.

**Not built, not claimed as built.** No script walks `body:` chains and none reads topic sentences.
Both are offered to Mirror as candidate `PROVISIONAL_OPERATIONAL_PRACTICE` (E.3). Failure
criterion for the second: three consecutive candidates in which reading cited sections whole
surfaces nothing the clause-level citation had not already carried.

## IMPACT

**What the laboratory gains.** The `HUMAN_REQUIRED` object revision 3 asked the operator to act
on — amend the FROZEN body and Annex I.2, rotate all four fingerprints, invalidate every actor's
checkpoint — **is not required at all**. Under the operator's architecture the body and the annex
are correct, and the documents that drifted are the two `PROPOSED` files and one canonical
sentence, all within Plan's mandate to propose. The most expensive item on the operator's queue
dissolves, and it dissolves on evidence read from the body rather than on the operator's
say-so — which matters, because the operator asked to be checked.

**What it does not gain.** Nothing is canonical, nothing is bound, and revision 4 does not exist.
`main` is unchanged at `04693e68`. The Orchestrator surface is no more resolved today than it was
at revision 3; what changed is the direction the resolution has to travel, and one canonical false
sentence is now named and still standing.

**Cost.** No fingerprint moved this session — no fingerprint input was edited. Revision 4, when
bound, is projected to rotate `orchestrator` only, as revision 3 does.

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1  ORIGINAL_OBSERVATION
                 L-2  ORIGINAL_OBSERVATION
                 L-3  ORIGINAL_OBSERVATION
                 L-4  REPLICATION            (of SLR-plan-0012 L-2 — a check defeated by its own
                                              evidence — at the level of the rule, not the quote)
                 L-5  REPLICATION            (of SLR-plan-0012 L-4, one dimension over)
                 L-6  ORIGINAL_OBSERVATION
                 ALL PROPOSED — E.2 curation is Mirror's; Plan does not self-ratify. Vocabulary
                 is E.2's own (ORIGINAL_OBSERVATION | REPLICATION | EXPOSURE_AFTER_BROADCAST)

SCOPE            L-1  wider scope — any system where citations are audited by presence
                 L-2  wider scope — procedure-vs-steady-state is a general genre distinction
                 L-3  wider scope — any claim about tool capability
                 L-4  wider scope in general form; the `body:` field is laboratory-internal
                 L-5  wider scope
                 L-6  wider scope — verification of a principal's own record

EVIDENCE         P-1  governance/GOVERNANCE_v3.1.1.md lines 180–182, read at HEAD; frontmatter
                      status: FROZEN, normative: yes, no `body:` field
                 P-2  every `§ ?8` occurrence enumerated across CAND-20260819-ORCHSURF,
                      HANDOFF-ORCHSURF-MIRROR, AUTHOR-RESPONSE-ORCHSURF-MIRROR-001,
                      SLR-plan-0010/0011/0012 and REV-ORCHSURF-MIRROR-001, and read
                      individually. Body §8 cited for content exactly twice — manifest line 209,
                      author response line 102 — both for "obliges it to produce durable output"
                 P-3  throwaway git repository; cwd = root checkout on branch `main`;
                      `git -C ../side commit` on branch `sidebranch` succeeded; root porcelain
                      empty; root HEAD unmoved. Corroborated textually by Annex H.1
                      ("WORK_COMMIT · ogni attore, solo proprio branch") and Annex D.1
                 P-4  frontmatter census over the 11 FROZEN normative governance documents:
                      `authority:` present in 0 of 11; `body: GOVERNANCE_v3.1.1.md` present in
                      10 of 10 annexes and absent from the body
                 P-5  T10 reproduced — body 5 hits, annex_i 3 hits, nine annexes 0, total 2 of
                      11, matching revision 3. The same five terms over body §8 → 0 hits. The
                      five terms hit body lines 67, 70, 86, 440, 444 — all bootstrap passages

REVIEW           L-1 is the entry most worth attacking, and F-1 in the prep document is where it
                 is load-bearing. A reviewer may hold that body §8's *"vive nella chat grafica
                 associata a <REPO_ROOT>"* denotes the Orchestrator's association with the root
                 as canonical batch surface rather than the chat's location — in which case §8
                 does not confirm the operator's architecture, L-1's example evaporates, and the
                 lesson survives only as a general principle without this instance. I do not
                 think that reading survives the subject of *vive* being *la chat grafica*, or
                 the following sentence needing to deny that the location confers authority. But
                 it is a reading, and the whole of F-1 rests on it.

LEARNING_ID      no LEARNING_ID is claimed. LEARNING_INDEX does not exist (Annex E.2, ABSENT),
                 so an ID minted now would name nothing. Unchanged by this session.
```
