---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0012
actor_id: plan
role: Plan
date: 2026-08-20
task: ORCHSURF-001 · generation 2 — adversarial re-review of CAND-20260819-ORCHSURF revision 2
  before it was handed to Mirror, and the revision 3 that re-review forced
scope: the extent of the FROZEN residual corrected from one document to two, the second being
  the governance body; the convergence route and its fingerprint cost restated; the fail-closed
  stop given the grounding it was missing. The body is NOT amended. Annex I.2 is NOT amended.
  The remedy is UNCHANGED — revision 3 corrects what the candidate says about the residual, not
  what the candidate does about it. Routing NOT opened. Annex D.1 NOT touched.
curation: PENDING — E.2 gives epistemic curation to Mirror. Every CONFIRMATION_CLASS below is
  **proposed**, never self-certified. L-1 is offered as a REPLICATION of SLR-plan-0011 L-1 at a
  higher rank and not as a new class of error, and Mirror decides whether that is the right
  reading of it.
derived_from: [SLR-plan-0011, SLR-plan-0010, SLR-plan-0010-COR-001, REV-ORCHSURF-MIRROR-001]
---

# SLR-plan-0012 — the micro-upgrade I adopted for missing an outranking document was already enough to find the one I was still missing, and I quoted it with that half cut off

## WORK COMPLETED

Revision 3 of `CAND-20260819-ORCHSURF`. Revision 2 was re-read adversarially against its own
package before delivery to Mirror, on the working assumption that a candidate whose entire
remaining value is a **declaration** is worth exactly the accuracy of that declaration.

The declaration was wrong in extent. `governance/GOVERNANCE_v3.1.1.md` — `status: FROZEN`,
`normative: yes`, the body every annex derives from — states at § 0.2: *"La stessa chat viene
promossa; non servono due chat root."* That is the same proposition Mirror quoted from
`BOOTSTRAP.md` lines 31–35 as blocking finding B-1, at the highest rank in the system. § 0.4
repeats the flow; § 47 steps 10 and 14 execute it. Revision 2 named none of them, in any file.

Revision 3 corrects the conflict table, the residual, the convergence route and the fingerprint
cost, and gives the stop the grounding it was resting on implicitly. It changes no remedy.

## PROBLEMS

**P-1 — I deleted a translation and left the original standing.** `BOOTSTRAP.md`'s *"The same chat
is promoted — you do not need to open a second one"* is an English rendering of body § 0.2's *"La
stessa chat viene promossa; non servono due chat root."* Revision 2 removed the rendering and
reported `BOOTSTRAP ROOT-PROMOTION INSTRUCTION AFTER R2 — REMOVED`. The instruction was removed
from the file I could edit and left intact in the file that outranks it.

**P-2 — the check that would have caught it is the one I had just adopted, and I ran it on a
truncated quotation.** `SLR-plan-0011`'s MICRO-UPGRADE reads: *"before the first edit, read the
documents the target file's `authority:` frontmatter names."* The same record's evidence line
quotes that frontmatter as `authority: Annex I.1, I.2, I.6`. The actual line is:

```
authority: Annex I.1, I.2, I.6; body §0.1–0.4, §38, §47
```

Everything after the semicolon was dropped — and everything after the semicolon is where § 0.2
lives. The upgrade was correct, was adopted, and was defeated by the copy of its own input.

**P-3 — the extent I declared disagreed with itself.** Three content files named the residual as
`Annex I.2 steps 1, 6, 9–10`; the convergence route in the fourth place named `steps 4, 6 and
9–10`. Step 4 is the step `BOOTSTRAP.md`'s own step 3 already departs from, and step 4 is one of
the two Mirror named in § 4.5 item 2. The declaration omitted the step the procedure deviates from
and included one it does not.

**P-4 — the stop was asserted without the grounding that authorizes it.** Revision 2 rested the
block on *"this file may not choose between them"*, and in the same section supplied the reader
with the precedence argument against it: I.2 is rank 1, `BOOTSTRAP.md` is `PROPOSED`, a document
cannot outrank its source. A controller applying body § 5 literally is handed a live reason to
proceed. The grounding was available and unused: body § 48 forbids proceeding past a point that
could *"violare one-writer"*, and body § 4 makes a directly-hit § 48 condition the one route to
`HUMAN_REQUIRED` that does not require an Orchestrator — which is the position every bootstrap
occupies by construction.

## SOLUTION

Revision 3 leaves the remedy untouched — the fail-closed stop, the created worktree, the withheld
sixth chat line, the blocked table row — and repairs only what the candidate **says**:

- the conflict table carries three sources, with the body first and quoted in its own language;
- `BOOTSTRAP.md` no longer states the root-promotion proposition in its own voice: it attributes
  it to FROZEN body § 0.2 and quotes it as the disputed mandate;
- the residual names body § 0.2, § 0.4, § 47 steps 10 & 14 **and** Annex I.2 steps 1, 4, 6, 9–10,
  identically in all three content files;
- the convergence route is one candidate amending **both**, with the explicit statement that
  amending the annex alone does not discharge it;
- the cost of that route is stated: the body is a fingerprint input for all four roles, so the
  amendment rotates every fingerprint and invalidates every actor's checkpoint (Annex A.6). Annex
  I.2 is an input for orchestrator and plan only. The operator is approving a four-role rotation;
- the stop is grounded in body § 48 and § 4, and the reason a stop needs no precedence — it is the
  absence of an instruction, not an instruction — is stated rather than assumed.

## LEARNING

**L-1 — a claim removed from a derived document is not removed.** `BOOTSTRAP.md` is a rendering of
the body's bootstrap sections. Editing the rendering changes what a reader of the rendering sees
and changes nothing about what the system mandates. The question after any such edit is not *did I
find the other copies* but *did I find the original*, and those are different searches: copies are
found sideways, originals are found upward.

**L-2 — a checklist item is only as good as the string you paste under it.** P-2 is not a failure
of the practice; it is a failure of transcription inside the record that established the practice.
A procedure that says *read what `authority:` names* is defeated silently by a quotation that ends
at a semicolon, and nothing in the record looks wrong afterward. Where a check reads a field, the
field belongs in the evidence **verbatim and whole**, because the truncation is invisible at
review time and fatal at execution time.

**L-3 — a fail-closed stop still owes an account of its own authority.** Refusing to act needs no
precedence, which is true and is not sufficient: a reader deciding whether to honour the stop is
deciding between two documents, and if the stopping document argues its own inferiority without
saying why a stop survives that, it has armed the argument against itself. State why the refusal
holds, or the refusal is advisory.

**L-4 — the second miss had the same shape as the first, one rank higher.** SLR-plan-0011 L-1 was
*the finding is the claim, not the line*. Revision 2 applied it sideways — same file, other
paragraphs — and stopped at the annex. The generalisation the two misses together support is that
the search must terminate at a document with no `authority:` field of its own, because that is the
only place a mandate can originate; the body has none, and that is what makes it the body.

**L-5 — reviewing my own package before delivery found what two review rounds had not.** B-1 was
found by Mirror; the body's § 0.2 was not found by Mirror either, in a review that reproduced every
hash by four routes. An adversarial pass by the author, run against the delivered artifact rather
than against the work, is not redundant with hostile review — it fails differently, and here it
failed usefully.

## MICRO-UPGRADE

**Adopted, and stated as an amendment to SLR-plan-0011's practice rather than a new one:** when a
candidate's remedy is a *declaration* rather than a change in behaviour, the declaration's extent
gets its own verification step, and that step terminates upward — follow each named authority to
the document it derives from, until reaching one with no `authority:` field. Record the terminus
in the manifest. For this repository the terminus is `governance/GOVERNANCE_v3.1.1.md`, which has
no `authority:` field, and reaching it is the check.

Paired with a transcription rule, because P-2 is the failure mode that defeats it: any frontmatter
field quoted as evidence for a check is quoted **whole**, or the quotation is marked elided.

**Not built, not claimed as built.** No script walks `authority:` chains today. Offered to Mirror
as a candidate `PROVISIONAL_OPERATIONAL_PRACTICE` (E.3) — success criterion: it terminates at a
document the sideways search did not reach, as it did here; failure criterion: three consecutive
candidates where the terminus adds nothing the sideways search had not already found.

## IMPACT

**What the laboratory gains.** The `HUMAN_REQUIRED` object the operator will act on now describes
the work it actually requires. Under revision 2 an operator could have approved an Annex I.2
amendment, seen it canonicalized, and still had a FROZEN body mandating the superseded topology —
a discharged-looking residual that discharges nothing. The cost is also now visible before the
decision rather than after it: four fingerprints rotate, not two.

**What it does not gain.** Nothing about the Orchestrator surface is more resolved than it was at
revision 2. The remedy is byte-for-byte the same fail-closed stop. Revision 3 buys accuracy in a
declaration, and that is the whole of it.

**Cost.** One further rotation of the orchestrator fingerprint and no other, because
`roles/orchestrator.md` remains the only fingerprint input among the changed files —
`BOOTSTRAP.md`, `deployment/deployment_profile.md` and `learning/` are not inputs, verified by
enumerating the input set at the revision-3 tip.

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1  ORIGINAL_OBSERVATION
                 L-2  ORIGINAL_OBSERVATION
                 L-3  ORIGINAL_OBSERVATION
                 L-4  REPLICATION            (of SLR-plan-0011 L-1, one rank higher)
                 L-5  ORIGINAL_OBSERVATION
                 ALL PROPOSED — E.2 curation is Mirror's; Plan does not self-ratify. Vocabulary
                 is E.2's own (ORIGINAL_OBSERVATION | REPLICATION | EXPOSURE_AFTER_BROADCAST)

SCOPE            L-1  wider scope — any system where normative text is rendered into a
                      procedural document
                 L-2  wider scope — it is a statement about evidence hygiene in checklists
                 L-3  wider scope — any fail-closed control in a ranked document system
                 L-4  wider scope in its general form; the `authority:`-frontmatter terminus is
                      laboratory-internal
                 L-5  laboratory-internal as a process finding; the general form — an author's
                      adversarial pass over the delivered artifact fails differently from a
                      reviewer's pass over the work — is offered for wider scope

EVIDENCE         P-1  governance/GOVERNANCE_v3.1.1.md § 0.2, read verbatim at the revision-2
                      content tip 7b6a9d9; frontmatter status: FROZEN, normative: yes.
                      grep for "0.2" / "0.4" / "§47" / "due chat" across the revision-2 package
                      (manifest, handoff, author response, SLR-plan-0011, SLR-plan-0010-COR-001)
                      → 0 hits in all five. Same grep over REV-ORCHSURF-MIRROR-001 → 0
                 P-2  BOOTSTRAP.md line 5 read whole; SLR-plan-0011 EVIDENCE block, P-2 line,
                      quotes it truncated at the semicolon
                 P-3  the four residual citations at the revision-2 tip: deployment_profile.md
                      lines 78 and 87, roles/orchestrator.md line 67, BOOTSTRAP.md lines 105
                      and 124 — "steps 1, 6, 9–10" three times, "steps 4, 6 and 9–10" once
                 P-4  BOOTSTRAP.md lines 118–121 at the revision-2 tip, which state the
                      precedence argument against the file's own stop and supply no counter
                 L-5  REV-ORCHSURF-MIRROR-001 § 4.1 quotes I.2 steps 1, 4, 6, 9–10 and does not
                      reach the body; its § 18 falsifier 1 searched "governance/, roles/,
                      deployment/ and BOOTSTRAP.md" and § 0.2 is inside that search perimeter

REVIEW           L-4 is the entry most worth attacking. A reviewer may hold that the body's § 0.2
                 is a *statement of principle* — its heading is "Root ≠ authority vale anche al
                 giorno zero", which is the principle this candidate defends — and that only the
                 clause "non servono due chat root" is procedural, so the residual against the
                 body is one sentence and not three sections. I do not think that survives § 47
                 step 14, which is unambiguously a procedure. But it is a reading, and if it
                 holds, the residual's extent shrinks and the convergence route with it.

LEARNING_ID      no LEARNING_ID is claimed. LEARNING_INDEX does not exist (Annex E.2, ABSENT),
                 so an ID minted now would name nothing. Unchanged by this session.
```
