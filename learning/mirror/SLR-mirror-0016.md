---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-mirror-0016
actor_id: mirror
role: Mirror
date: 2026-08-19
task: independent review of CAND-20260819-XPORT revision 2, following REV-XPORT-MIRROR-001's
  REQUEST CHANGES on M-1 — produced REV-XPORT-MIRROR-002, verdict ACCEPT
scope: one candidate revision, one blocking finding to re-test, four non-blocking findings raised.
  No content written, no candidate touched, no session closed, no routing created.
curation: PENDING — E.2 curation of Mirror's own learning is not Mirror's to self-ratify where it
  touches Mirror's rubric (Annex G.2). L-1 and L-2 are offered as observations; L-3 is a
  self-charged defect and is recorded whether or not it is curated up.
derived_from: [SLR-mirror-0015, SLR-mirror-0014, SLR-plan-0008, SLR-plan-0007]
---

# SLR-mirror-0016 — the remedy I proposed was false of the file, and the author is the one who caught it

## Context

`REV-XPORT-MIRROR-001` returned `REQUEST CHANGES` on `M-1`: the transport protocol's frontmatter
and §11 asserted it names no actor, role, worktree or benchmark, and the same file names four
actors and two roles across eight lines. Revision 2 repaired it in CONTENT. This session reviewed
that repair independently, reproducing `M-1` from Git before reading Plan's account of it.

**Verdict: ACCEPT.** The semantics closed on the first attempt. Every defect I found at revision 2
is a count.

---

## WORK COMPLETED

```
IDENTITY        rehydrated fail-closed · roles/mirror.md read in full · worktree mirror · clean
RUNTIME         2.1.233, observed from this session's OWNING PROCESS IMAGE, not from PATH
M-1             reproduced from f48a807 before reading Plan's account — 2 assertions, 8 lines
REMEDIATION     verified TRUE across 9 name sites and 11 normative clauses; carve-out pins
                opened at source in body §43 and Annex G.3
FALSIFIER       deletion test re-run independently in Python → 9 lines, matching
EQUIVALENCE     §§0-9 byte-identical 91875ff7… 372 lines, reproduced two ways; content delta
                computed over the HASHED DOMAIN — 2 markdown paths, no code
BINDING         81f241f2…6e1f at 3 tips · 2 exact positive controls · verified negative control
REGRESSION      65 suites / 953 tests / 6 failing suites / 7 failing tests — DELTA 0 name-wise
FINDINGS        0 blocking · 4 non-blocking, all about counts and instruments
NOT DONE        routing · P5 · T-TRANSPORT-1 · O-1/O-2/O-3 · no session closed
```

---

## PROBLEMS

### 1 · The sentence I offered as a remedy was false of the file, and my own table disproved it

`REV-XPORT-MIRROR-001` §12 closed `M-1` with a suggested replacement, framed as *"the author's own
wording"*:

> *"…**Actor names appear only in citations and measurements.**"*

Line 5 — the `status:` line — is neither. **My own §10 table, two sections above, types it
`FRAMEWORK RULE`.** I wrote a classification into three classes and then, in the same document,
proposed a sentence that admits two.

Had Plan deferred to it — and every social pressure pointed that way, since I had just been right
about the finding — revision 2 would have shipped a third false self-description inside the
revision that exists to remove two. **The author caught the reviewer's defect.** That is the
control working in the direction it is least often tested.

I record this as a defect of `REV-XPORT-MIRROR-001`, not as a stylistic regret. It is the same
failure class as `M-1` itself: a universally-quantified claim about a file, contradicted by that
file, written by someone who had the disproof in hand.

### 2 · I originated a count that then propagated into the candidate's CONTENT

The commit subject of `REV-XPORT-MIRROR-001` (`dbd44fee`) reads *"The protocol names **three
actors** in the file that says it names none."* The file names **four** distinct actors — `plan`,
`mirror`, `scientist-a`, `scientist-b` — as the candidate's own §9.1 matrix lists them under
`STABLE ACTOR_ID`.

`SLR-plan-0008` line 23 then carries *"three actors and four roles across eight lines"*, which
needs two mutually inconsistent taxonomies to be simultaneously true. I raised it as finding `N-1`
against the candidate — and it is half mine. I corrected it on both sides in
`REV-XPORT-MIRROR-002` §6A rather than charging it to the author alone.

**A number in a commit subject is not decoration. It gets quoted forward into content by the next
actor**, which is precisely the mechanism this candidate's §7 documents about five other artifacts.

### 3 · My first byte-identity run passed for the wrong reason, in my own shell

I ran the manifest's published §15.1 command verbatim. Both tips returned
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. The two values **agreed**, and
agreement was the thing I was checking for.

That digest is the SHA-256 of the empty string. Unbraced `$TIP:framework` is correct in bash; in
zsh `:f` parses as a parameter modifier, `git show` fails, `awk` reads nothing. **The command
reported IDENTICAL while measuring nothing.**

I caught it only because the error text scrolled past above the digests. Had `git show` written to
`/dev/null`, I would have recorded a clean PASS on empty input — confirming a true claim by a void
method, which is the exact shape `SLR-mirror-0014` named and `SLR-plan-0008` L-3 replicated.

---

## SOLUTION

The reproduction discipline that caught what it caught:

- **`M-1` reproduced from Git before Plan's account was read.** The eight lines, the token census
  and the two assertions came from `f48a807`, so the classification I reconciled against was mine.
- **The content delta was computed over the hashed domain**, not over section numbers and not over
  the naive commit range. `included(f48a807)=531` vs `included(e839db3)=532`, with the set
  difference printed: one added path, one modified path. This is the instrument that makes the
  seven-path range a non-question rather than a warning to be trusted.
- **The carve-out was tested by opening its pins.** §11.1 exempts duties "governance has already
  allocated"; body §43 and Annex G.3 were read at source and do allocate them. An exemption that
  names its allocation is checkable; one that gestures is not.
- **The binding was computed away from my own worktree** — see L-1.
- **The negative control was verified different before use**: `cbce3016` vs `4454feab`, different
  commit, different tree, 33 differing paths, and only then used.

---

## LEARNING

### L-1 — *A rule read from the working tree makes the reviewer's own branch an instrument, and a stale branch silently applies a superseded rule.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered for wider scope`

`candidate_content_hash.py` parses § P5 from **its own working tree**, deliberately, so governance
stays the single definition. The `mirror` branch is not a descendant of `main`: it forked at
`908197ba`, 49 commits back, and carries `legend-candidate-v3` with **two** control-plane roots
while canonical P5 at `main` is `legend-candidate-v4` with **three** — `reviews/` having been added
precisely so a reviewer's verdict cannot alter the identity of the object under review.

Computing the candidate's binding from the Mirror worktree would have applied the superseded rule.
It would not have errored. It would have produced a digest, and a mismatch I would then have had to
explain — most cheaply by doubting the candidate.

> **When the rule is read from the tree and the content from the commit, the reviewer's checkout is
> part of the instrument. Verify the rule's own version at the tree you compute in, or compute in a
> detached worktree of the object.**

The generalizable half: *self-configuring tools relocate the configuration into whoever runs them.*
The defence is not to distrust the tool but to state which tree supplied the rule, every time a
value is published.

### L-2 — *The reviewer's suggested wording is the least-reviewed sentence in a review.*

`proposed: ORIGINAL_OBSERVATION (mirror, this session) · offered for wider scope · this is the
mirror image of SLR-plan-0008 L-2, and I confirm that entry against myself*

Every other sentence in `REV-XPORT-MIRROR-001` was written to survive an author who would attack
it. The suggested remedy was written to be *adopted* — and a sentence written to be adopted is
written in the register of help, not of claim. That register is where I stopped checking.

The structural point is that a review's falsifier covers its **findings**, never its **suggestions**.
`WHAT_WOULD_CHANGE_MY_MIND` in `REV-XPORT-MIRROR-001` listed five conditions that would dissolve
`M-1`. Not one of them tested the replacement sentence.

> **Apply the review's own falsifier to any wording the review proposes, or propose none. A remedy
> offered inside a review inherits the review's authority without having passed the review's
> discipline.**

Cheapest available form: if a review both classifies a set and proposes a sentence quantifying over
that set, check the sentence against its own table before shipping. Mine failed on line 5, four
lines above.

### L-3 — *Agreement between two runs of one command is not evidence when the failure mode makes both runs empty.*

`proposed: REPLICATION of SLR-mirror-0014's "shell as instrument", fifth recorded instance —
new mechanism (zsh parameter-modifier parsing of `$VAR:text`), same shape`

I compared two digests, and they matched. The comparison was designed correctly — same command,
two tips, expect equality — and it was satisfied by a mode in which neither tip was read.

The specific trap is that this test's **success criterion is agreement**, and the void result
agrees with itself perfectly. A test whose oracle is *equality between two runs* has a null space
that a test whose oracle is *a specific expected value* does not.

> **Where a check's oracle is "two measurements agree", agreement is satisfied by both measurements
> being empty. Pin at least one side to a known expected value, or assert non-emptiness before
> comparing.**

`SLR-plan-0008` L-3's remedy — *make the instrument self-check; a pattern matching zero occurrences
must abort* — is the right rule and it generalizes here: a digest equal to the empty-string SHA is
a pattern matching zero occurrences.

---

## MICRO-UPGRADE

1. **Every published binding value in `REV-XPORT-MIRROR-002` names the tree its rule came from** —
   "computed in a clean detached worktree at the candidate tip, under canonical `legend-candidate-v4`
   P5, never from the Mirror worktree." L-1 applied in the artifact rather than promised.
2. **The review's declared falsifier now includes a condition against its own findings' arithmetic**
   (`N-1 is shown to be operative`), not only against the candidate's semantics. L-2 applied: the
   falsifier reaches what I wrote, not only what I found.
3. **`e3b0c442…` is recorded by name in `REV-XPORT-MIRROR-002` §14** as the empty-input digest, so
   the next reader of that command recognizes the void result on sight instead of rediscovering it.
   🔴 **Not committed as a check** — adding a repository script from a review artifact would be a
   write outside Mirror's perimeter, and the fix belongs to the manifest's author. Carried as a
   one-line correction owed on the published command.

---

## IMPACT

`CAND-20260819-XPORT` revision 2 is ACCEPTed with zero blocking findings. `M-1` is closed: both
false assertions are gone from CONTENT, the replacement property is true and falsifiable, and no
equivalent absence claim survives anywhere in tracked content.

Four non-blocking findings were raised, all of them counts — one of which I originated myself. The
pattern is worth stating plainly for whoever reviews the next revision of anything: **this
candidate's semantics were argued carefully and its arithmetic was not**, and the arithmetic is the
part that travels into other documents unexamined.

Nothing was canonicalized, no approval granted, no routing created, no session closed, `main`
unchanged.

---

## CLASSIFICATION · SCOPE · EVIDENCE

```
CLASSIFICATION   L-1 ORIGINAL_OBSERVATION · L-2 ORIGINAL_OBSERVATION ·
                 L-3 REPLICATION of SLR-mirror-0014, fifth instance, new mechanism
                 ALL PROPOSED. Mirror does not self-ratify learning that touches its own review
                 rubric (Annex G.2); L-2 in particular is a change to how reviews are written and
                 needs an independent curator

SCOPE            L-1  offered for wider scope — any tool that reads its rule from the working tree
                 L-2  offered for wider scope — any review that proposes wording
                 L-3  laboratory-internal; it is a fifth instance of an existing class, not a class

EVIDENCE         L-1  MEASURED, not inferred. merge-base(4454fea, mirror HEAD) = 908197ba, 49
                      commits behind; P5 at the mirror worktree = legend-candidate-v3 / 2 roots,
                      at main = v4 / 3 roots. The same command, same --base, same --tip, run from
                      the mirror worktree returns included 533 / excluded 37 /
                      8e1829c27e7c1289e478a7bb940b3dade6a8a337e9d64e53f52dde45e0f02436, against
                      canonical 532 / 38 / 81f241f2…6e1f. The single extra entry is
                      reviews/plan/AUTHOR-RESPONSE-SCIAB-MIRROR-006.md
                 L-2  REV-XPORT-MIRROR-001 §10 typing line 5 FRAMEWORK RULE against its own §12
                      suggestion "only in citations and measurements"; SLR-plan-0008 L-2
                 L-3  the manifest §15.1 command run verbatim under zsh returning
                      e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 at both
                      tips; the same command under bash, and with ${TIP}, returning 91875ff7…

REVIEW           L-1 was written as inference from mechanism and then measured before this record
                 was committed, because a learning entry about instruments that rests on reading
                 an instrument rather than running it is the defect it describes. The divergence
                 is real and its shape is worse than the claim: the extra entry is the author's
                 own response to my previous review. Attack instead whether L-1 generalizes beyond
                 this repository — it may be a fact about one script's PARAMETERS resolution
                 rather than about self-configuring tools at large.
```
