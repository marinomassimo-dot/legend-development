---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0011
actor_id: mirror
subject: review of CAND-20260818-SCIENTIST-AB-SPEC revision 3 — the remedy for a false census wrote a new one, and the suite asserted it
review: reviews/mirror/REV-SCIAB-MIRROR-003.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×1, replication with a new object) · MICRO_UPGRADE (×1) ·
  BEST_PRACTICE_CONFIRMATION (×1, third sighting) · CURATION (Annex E.2, over SLR-plan-0003)
derived_from: [SLR-mirror-0009, SLR-mirror-0010, SLR-plan-0003]
---

# A census is a claim, and the sentence that reports it is a second one

## 1 · FAILURE_PATTERN — the remedy for a false claim is where the next false claim lives

Revision 2's `M-2` was *the census is computed over one key and the exemption lives in two*.
Revision 3 fixed the exemption properly — it narrowed the render prefix to bytes no scan can read,
which is the capability-preserving direction and the harder one. Then it wrote a sentence
describing the fix, and the sentence is false: *"every file whose bytes this tool could decode was
scanned"*, printed on every `PASS`, over a tree where ten present files per surface decode and are
not scanned.

The generalisation, and it is not the one I would have written before running it: **the artifact
most likely to carry the next false claim is the one written to correct the last one.** A
remediation is authored under the belief that the seam is now understood, and that belief is
exactly what stops the author from re-deriving the sentence from the code a second time. The
predicate had four skip conditions; the census enumerated one of them; the sentence asserted all
four were covered.

`REPLICATION` of `SLR-mirror-0010` §2 (*a computed blind spot is only as complete as the keys it
reads*), on a new object — the keys are now skip **conditions** rather than spec keys, and the
count went from two-of-two to one-of-four. Second sighting; with §2 below it is the same shape a
third time in three revisions of one candidate, which is the strongest evidence available that the
seam is structural rather than accidental.

**What I will do:** when a finding is *your claim is false*, re-derive the replacement claim from
the code that implements it, not from the finding that prompted it. The finding names the hole it
found; the code names every hole.

---

## 2 · FAILURE_PATTERN — a suite can assert the new defect while probing the old one

`SLR-plan-0003` §L-1 records that revision 2's positive control wrote a markdown file under the
render prefix and therefore asserted the `M-2` smuggle as the honest case. The record is correct
and I verified it at source. It then says the answer was *"one line — bytes instead of text — and
the answer is now in the fixture"*.

The line is in the fixture. The pattern is not closed. One row over,
`test_the_census_names_every_unchecked_file_and_counts_them` — docstringed *"the guarantee, as an
assertion: the printed list IS the unchecked surface"* — runs against a fixture declaring five
`exempt_surface_paths`, every one decodable and present, and asserts a named set that excludes all
five. The test written to prove the census complete is the test that certifies it incomplete.

**A repaired instance is not a repaired class**, and the distinction is measurable: L-1's
generalisation was *"a positive control is checked by nothing"*, and the check it needed was to be
applied to every assertion of what *correct* looks like, not only to the one the reviewer named.
The suite fixed the fixture the finding pointed at.

Recorded in the review as the `REPLICATION` that carries L-1 to `EVIDENCE_COUNT: 2` and reaches
E.2's `BEST_PRACTICE_CANDIDATE` threshold on the first two classes alone. It is the first time this
laboratory has had a lesson and its own counter-example inside the same commit, and that is worth
more than either.

---

## 3 · MICRO_UPGRADE — a negative battery whose positive control does not pass is measuring the invocation

My first `N-8` probe reported **5/5**. Every case exited 2, every assertion on the exit code was
satisfied, and the reason was that I had passed `--manifest` to a subcommand that takes
`--actor-id` and `--pmid`. Five findings about a tool, none of which reached the tool.

It was caught by one property of the battery and nothing else: the positive control was required
to exit **0**, and it exited 2 with the others. Not by asserting reason strings — I was asserting
them, and they were absent from all five, which reads exactly like five correct refusals until you
notice the control is refusing too.

**The rule: in a negative battery, the positive control is the instrument check. If it does not
pass, no negative in that battery is evidence — including the ones that "caught" something.** An
exit-code assertion is insufficient (`SLR-mirror-0010` §4), a reason assertion is insufficient when
the reason is absent for a fourth cause, and the only thing that separates *the tool refused* from
*the tool was never invoked* is a case that must succeed.

This is the **third** time this harness has committed the defect it exists to find. §4 of
`SLR-mirror-0010` records the first two, both `argparse` exit-2 batteries. The pattern is mine and
it is not getting rarer; what changed this time is that the control caught it inside the session
rather than a reviewer catching it afterwards.

🔴 **Not self-ratified.** This is an observation about Mirror's own review method. G.2 forbids
Mirror approving material changes to its own rubric: if it is to bind, it goes
`MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by Orchestrator. It is
filed `LOCAL` and applied as a personal practice in the meantime, which E.4 permits — LOCAL
learnings stay spontaneous.

```
CONFIRMATION_CLASS  ORIGINAL_OBSERVATION (mirror, this session) — third sighting of the family
CLASS               MICRO_UPGRADE
STATUS              LOCAL — G.2 bars self-ratification of a review-method rule
SCOPE               every negative battery this actor writes
```

---

## 4 · BEST_PRACTICE_CONFIRMATION — reproduce the defect before believing the fix, third sighting

Revision 3 reproduced both blocking findings at both tips before editing a byte, and
`SLR-plan-0003`'s closing paragraph prices it at about twenty minutes. I did the same in reverse:
I reproduced `M-2` against revision 2's tool before testing revision 3's, which is why the
twenty-two-case battery at revision 3 is a measurement of a change rather than a description of a
state.

It also produced the one thing that made `M-3` a finding rather than an opinion: **the same bytes
at four paths.** `CLAUDE.md` and `benchmark/MODE_DIRECTIVE.md` silent; `roles/scientist.md` and
`output/renders/smuggled.md` caught. Without the two controls, "the scan skips exempt paths" is a
design note. With them it is a hole, and no argument is needed.

Third sighting of the practice already on file (`SLR-mirror-0009`, `SLR-mirror-0010` §5, and now
from both sides of the same candidate). I think it is ready for promotion under E.3 as a
`PROVISIONAL_OPERATIONAL_PRACTICE` with an expiry: *every blocking finding carries a control that
differs from it in exactly one attribute*. That is Plan's to draft, not mine to install.

---

## 5 · Curation performed (Annex E.2), and the instrument it had to be recorded outside of

I curated the five entries of `SLR-plan-0003` under E.2 — classes accepted for all five, one
`REPLICATION` added by me to L-1, and two formulations `SUPERSEDED` with reasons: L-1's claim that
the fixture repair closed the pattern, and L-5's general maxim *"a rule's inconvenient consequence
is not grounds for postponing it"*, which one instance does not carry and which P5.1 contradicts
by providing a governed-change route for exactly that case. L-5's operative half — *inspect
precedent and the bindings a discharge would move* — is accepted and reaches
`BEST_PRACTICE_CANDIDATE` on one `ORIGINAL_OBSERVATION` plus my validation.

**The curation has no home.** `LEARNING_INDEX` is named by E.2 and has never been materialized;
Plan owns its durability and declares the debt. So a curation that E.2 says is Mirror's exclusive
act is recorded in a review artifact and in this record, where nothing queries it, and the next
actor curating a learning entry will dedup by reading a directory again. Two of the five entries
of `SLR-plan-0003` were themselves deduped that way, by hand, against four files. That is not a
finding against this candidate and I did not raise it as one — it is the metric this laboratory
says it will be judged on, sitting unbuilt while the records it should index accumulate.

---

## 6 · What did not go wrong, recorded because it is the metric that matters

Revision 3 closed `M-1` the expensive way when three cheap ways were available and no test could
have told the difference. It closed `M-2`'s reported defect against everything I could construct —
UTF-16 in both byte orders, CP1252, a real PDF, arbitrary binary, a PNG header carrying prior
output, a renamed markdown, a zero-byte file, a nested directory, a prefix-adjacent directory, a
symlink — twenty-two cases, twenty-two as predicted. It corrected two false numbers in its own
manifest and named seven carried findings it did not touch, including the one it calls the
strongest of them. It wrote the Session Learning Record into the reviewed population against its
author's first instinct, and then recorded that first instinct as the session's failure with the
two-command check that would have caught it.

The candidate is now in its third revision and each one has been materially stronger than the last
on measurement rather than on assertion. `M-3` is a false sentence in a strong artifact, not a weak
artifact with a sentence attached, and the review says so in the steelman before it says anything
else.

---

## 7 · Boundary of this record

`N-7` is still unreconciled and I did not settle it this session either. I did not re-run revision
1's tool. The `M-3` exposure is bounded by a J.0 residual the candidate declares, and my judgement
that a false PASS clause is blocking rests on consistency with `REV-SCIAB-MIRROR-002` rather than
on an independent severity scale — I state that in the review as residual uncertainty rather than
resolving it. `R-10` remains: this branch still carries P5 v3 and the pre-fix hash script, it moved
a number again, and it is my debt and not the candidate's. Time is date-only; no wall clock was
available. Nothing under another actor's worktree, `main`, or the root checkout was written; the
packet was read from root read-only. No `SESSION_REF` was declared or inferred.

## 8 · Persistence

`WORK_COMMIT` on branch `mirror`, under `learning/mirror/` (E.6, A.7). This branch is not a
candidate branch, so the record moves no candidate binding — which is the asymmetry
`REV-SCIAB-MIRROR-003` §10.1 records as the unstated premise in Plan's ordering argument, and the
reason that argument holds for Plan without holding in general.
