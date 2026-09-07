---
record_type: HOSTILE_REVIEW
record_id: READINESS-001-HOSTILE-REVIEW-V1
title: Hostile review of LEGEND_OPERATIONAL_READINESS_PLAN_v1 — phase 2 of 4
reviewed_object: learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md
reviewed_blob_measured: f12d8acecb5acc6d5a7a96662a398dc846e57573
reviewed_blob_expected: f12d8acecb5acc6d5a7a96662a398dc846e57573
hash_match: YES — the bytes did not move under me
reviewed_blob_object_state: >
  ABSENT from the object database. `git cat-file -e f12d8ace…` fails while `git hash-object` of the
  working file returns exactly that hash. NO git object and NO ref preserves the bytes I reviewed.
  This review is bound to a hash that names a file on one disk.
actor_id: NOT ESTABLISHED — a session cannot resolve its own actorhood
registered_mirror_seat: >
  NO. `runtime/agent_card_registry.md` (in the `orchestrator` worktree) binds `ACTOR_ID mirror` to
  `CURRENT_SESSION_REF mirror-9c`, `LISTAGENTS_ROW mirror-9c [3940a9]`, worktree `mirror`,
  transport `uds:/tmp/cc-socks/6826.sock`. This session holds none of those and runs in the root
  checkout, not the `mirror` worktree. It is not that seat and does not claim to be.
role_contract: none held
lease: none held
binding: NO
authority_claimed: none
governing_activation_state: >
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE, OPTION B `ACTIVATION_NOT_CONFIRMED`:
  "No actor authority may be assumed from these contracts."
measured_at:
  branch: legend-operating-convention-v1
  commit: 30cb4f3fd700e2aaf6b608e363438f883ddc3760
  instant: 2026-08-24T08:25Z–08:52Z
  tree: working tree as found, 8 untracked records at open, 9 after this file
findings: 20 — 2 CRITICAL · 6 MAJOR · 8 MODERATE · 4 MINOR
disposition_rule: >
  A finding is not a blocker unless the operator makes it one. This review authorizes nothing,
  blocks nothing, resolves nothing, and grants nothing. It produces findings, which need no
  actorhood.
domain: CONTENT. `learning/` is not among the CONTROL_PLANE_ROOTS of P5.1.
---

# HOSTILE REVIEW — LEGEND OPERATIONAL READINESS PLAN v1

> **FINDINGS ONLY · NOT AN AUTHORIZATION · BLOCKS NOTHING · RESOLVES NOTHING**

## 0 · Standing, stated unprompted

I hold no `ACTOR_ID`, no role contract, no lease. I checked the registry rather than assuming:
`runtime/agent_card_registry.md` (in the `orchestrator` worktree) binds `mirror` to session ref
`mirror-9c [3940a9]` in the `mirror` worktree. I am in the root checkout on
`legend-operating-convention-v1`. **I am not the registered `mirror` seat.** Under
`DEC-20260822` no actor authority may be assumed in any case. The record predicted this in its
own § 13.6, and it was right: that is now four consecutive reviews performed by a non-seat.

## 0.1 · Verification classes used

`RE-DERIVED` — I ran the check myself at this HEAD. `READ` — I read the source object.
`AS REPORTED` — carried on someone else's report and marked as such.

## 0.2 · The hash, and what it does not name

```
git hash-object learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md
  f12d8acecb5acc6d5a7a96662a398dc846e57573        matches the expected value
git cat-file -e f12d8acecb5acc6d5a7a96662a398dc846e57573
  fails — ABSENT from the object database
```

Positive control: `HEAD:CLAUDE.md` = `bf807fec…`, `cat-file -e` succeeds. Negative control: the
all-zero hash, `cat-file -e` fails. **Both controls fire, in both directions.** The bytes I
reviewed exist in one place on one disk, and this review is bound to them. That is finding M-1's
subject, and the record is its own most acute example.

## 0.3 · A note on writing this file at all

`scripts/test_documented_commands.py` joins shell continuations into one logical line and asserts
that every `--flag` appearing after a `python3 <script>.py` token is exposed by that script's
`--help`. **Writing a review of that suite can turn that suite red.** I therefore kept every
Python invocation below on its own line with only real flags, and did not reproduce the record's
one-line continuation verbatim. This constraint is itself evidence for the record's own
self-reference point in N-2 — and evidence that the record did not apply that point to itself
(M-11).

---

# FINDINGS

## M-1 · CRITICAL · The frontmatter hazard block is false about the record's own inputs

**Section:** frontmatter `consumes:` / `hazard:` · **Class:** RE-DERIVED

The record declares five consumed blobs and then states:

> "All five consumed records are UNTRACKED files. **Four survive additionally as loose objects
> reachable from 0 refs.** The fifth — design v1, blob `9d744eb7…` — does NOT exist in the object
> database at all."

Measured at the same HEAD, with a positive and a negative control that both fire:

| Declared consumed blob | Record | Measured |
|---|---|---|
| `6bd903cb…` design v2 rev 2 — *the record the trial would run from* | survives | 🔴 **ABSENT** |
| `598afd35…` bootstrap audit | survives | 🔴 **ABSENT** |
| `635f1b21…` TRIAL-002 register | survives | 🔴 **ABSENT** |
| `ee00195f…` TRIAL-001 register | survives | PRESENT, 0 refs |
| `d5c0d296…` execution protocol | survives | PRESENT, 0 refs |

**Two survive, not four.** And design v1 is not one of the five consumed records at all — the
record's fifth consumed record is the execution protocol, which does survive. The hazard block
imports N-3's result, which was measured over *design v2's* consumes list, and reports it about
its own. **A figure measured on one population and reported about another: the W-1/W-2/W-3
shape, in the frontmatter, in the block most likely to be acted on.**

```
git cat-file -t 6bd903cb08b29da6db86467a70db127502585974   # could not get object info
git cat-file -t 598afd355bd4de2a94d67c7620f10c87b4e1e59d   # could not get object info
git cat-file -t 635f1b21bf61b419f673e6b2773e27514007d99b   # could not get object info
git cat-file -t ee00195fac0f7c317803120d2a5d335098c33778   # blob
git cat-file -t d5c0d296df69ea5a14426e2da351869959983c7b   # blob
```

**A `gc` explanation is ruled out.** The two surviving loose objects were written 2026-08-23 at
22:49:12Z and 22:25:26Z; `gc.pruneExpire` is unset, so the default `2.weeks.ago` protects every
unreachable object in this corpus. Nothing here could have been pruned. **The three absent blobs
were never written.**

**This error runs against the record's own thesis.** The object-loss problem is worse than it
says: of the eight untracked planning records, **four have no object at all** — design v1
(`9d744eb7…`), design v2 rev 2 (`6bd903cb…`), the audit (`598afd35…`), the TRIAL-002 register
(`635f1b21…`) — plus the readiness plan itself (`f12d8ace…`). Only three of eight are recoverable
from the object database at all, and only two of those from a ref.

---

## M-2 · CRITICAL · Φ−1 requires an authority the record's own standing denies it

**Section:** § 5 Condition 1, § 9 Φ−1, § 1.2 · **Class:** RE-DERIVED (governance) / READ (record)

Φ−1 is the record's one act — *"the only phase authorized to run before the operator's next
mandate"*, whose stated precondition is *"needs: decision B-1 only."* Its third step is:

> `WORK_COMMIT the 7 records on this branch (a session's own named paths, its own branch)`

`WORK_COMMIT` is a named governance act with a named grantee:

```
governance/annex_h_authority_matrix.md:34
  | WORK_COMMIT | ogni attore, solo proprio branch, granularità milestone |
governance/GOVERNANCE_v3.1.1.md:229
  WORK_COMMIT → ogni attore, PROPRIO worktree/branch.
```

*Ogni attore* — every **actor**. And `DEC-20260822` IMMEDIATE_CONSEQUENCES 2 reads:

> "No actor authority may be assumed from these contracts. **Any authority an actor exercises must
> be traced to the governance body or to a named annex — H.1 for the authority matrix, D for the
> commit path, C for the review ladder, I.3 for the lease** — never to a role contract clause
> standing alone."

The trace goes to H.1, and H.1's grantee is an actor on its own branch. The record's own
frontmatter says `actor_id: NOT ESTABLISHED` and `AUTHORITY_CLAIMED: none`; its § 2.3 last row
says *"Authority limit of this session: none."* No registry entry binds any actor to
`legend-operating-convention-v1`; the registry binds actors to the six named worktrees.
`governance/candidates/CAND-20260817-ORCHWT.md:162-164` records the adjacent case explicitly: an
actor resident in the root *"has NO branch on which a `WORK_COMMIT` is possible — uniquely among
six actors."*

**The premise was inherited, not re-derived.** Design v2's D-13 asserts it in one clause —
*"`WORK_COMMIT` of a session's own named paths on its own branch is that author's own
authority"* — and the readiness plan reproduces the act without testing that clause, while its
entire method is to re-derive design v2's premises (§ 1.2: *"the re-derivations in § 12 do not
disturb them"*). **§ 12 contains no re-derivation of the WORK_COMMIT authority.** It is the one
premise of design v2 the record carried through untouched, and it is the premise its only
proposed act stands on.

**Consequence for the record's sequencing:** Φ−1's precondition is not "B-1 only". It is B-1 **and**
an actor holding WORK_COMMIT on this branch — which is the activation act the record itself defers
to § 4.3 F-1 as *"Step 3's precondition"*. The one phase the record says is runnable now depends
on the one thing it says must wait until last.

---

## M-3 · MAJOR · "True positives by construction" is not entailed by the cited evidence

**Section:** § 0 N-1 · **Class:** RE-DERIVED

N-1's reading of the mechanism is **correct**: line 388 is
`exact_digest = hashlib.sha256(match.group(0).encode()).hexdigest()`, the allowlist holds 5 exact
and 3 casefold digests, digest interiors are excluded by `hex_run`, and no regex heuristic decides
anything. The record cited the right line and read it right.

**The conclusion drawn from it is stronger than the mechanism supports.** The candidate token is
`identifier_token = re.compile(r"(?<![A-Za-z])[A-Za-z]{3,24}(?![A-Za-z])")` — *any* bare alphabetic
word of three to twenty-four letters, matched case-insensitively via the casefold set, with no
context test whatsoever. If any allowlisted token is also an ordinary word, every non-personal use
of that word fires.

I demonstrated the collision without disclosing anything. I copied the gate to a scratchpad,
replaced only the two frozensets with the SHA-256 of the plainly non-personal English word
`Marker`, and scanned a scratchpad file that names no person:

```
The pipeline emits a Marker for each unit.
In lowercase the token is marker; uppercased, MARKER.
This file names no person and carries no clinical datum.
```

Result: **2 × `[BLOCK] DIRECT_IDENTIFIER` — "Legacy personal identifier remains in public
material."** Negative control, identical file with both allowlists emptied: **0
`DIRECT_IDENTIFIER`.** Both controls fire.

**What the gate proves** is *"a token whose (casefold) SHA-256 is in the registered allowlist
occurs at this line."* **What the record claims it proves** is *"a registered legacy personal
identifier occurs at this line."* The gap is the semantics of the allowlisted strings, and those
are — by the script's own design comment, *"Keep only digests in the publishable detector
source"* — unavailable to anyone reading this repository, including the record's author. The
record asserts a no-false-positive property whose evidence the repository deliberately withholds.

**The operational conclusion survives on different, sufficient grounds, and I say so with the same
weight.** D-13(a) is unsafe as written regardless, because the publication gate is the instrument
that decides publishability and it returns `BLOCK_PUBLICATION` on those files. The record reaches
a right answer; it overstates why.

---

## M-4 · MAJOR · The blocking decision set is 5 of 14, presented without its denominator, and one 🔴 is demoted into the non-blocking tier

**Section:** § 4, § 5, § 3 K-8 · **Class:** RE-DERIVED (enumeration) / READ (design v2)

Design v2 § 13 carries **14** decisions, `D-1 … D-14`, of which **9** are marked 🔴:
D-1, D-2, D-3, D-4, D-5, D-6, D-8, D-11, D-13.

The readiness plan's § 4 carries **5** of the 14 — D-1 (as B-4), D-3 (as B-5), D-8 (as I-4),
D-13 (as B-1), D-14 (as B-2) — i.e. **3 of the 9 red ones** in its blocking tier. The remaining
nine design-v2 decisions appear nowhere. § 4's preamble reads as exhaustive: *"Three tiers, as the
mandate requires. **Every one of them is the operator's**; none is assumed here."* No denominator
is given, and § 13.4's own rule — *"A finding not acted on says why. Silence is not a
disposition"* — is applied to findings about the record but not to the decisions it inherits.

Two of the omissions are load-bearing:

- **D-2** 🔴 *"The paper, and the re-authored question?"* — design v2's "Proceeds regardless"
  column reads **"nothing; Φ1 cannot start."** § 5's step-1 needs-list is *"B-2 · B-3 · B-5"*.
  It also needs D-2. The record knows the substance — § 2.1 measures the contamination and § 10
  criterion 5 requires someone to check the assignment against it — but never converts it into an
  operator decision, so the operator is never asked which question the reader is given.
- **D-4** 🔴 *"Unregistered rehearsal, or lift/scope the C-9 L2 hold first?"* — "under (a): **no
  governed Scientist artifact**". Absent from § 4 entirely. The only occurrence of the token
  `D-4` in the record is **the audit's** D-4 (skip boundary), at § 4.2 I-6 — a different decision
  in a colliding namespace. Design v2's D-4 is silently invisible, and § 8 row 8 is scored ✅ on
  the very design-v2 table whose `reader-L` row is ⚠️ *pending D-4* (see M-5).

**And an internal contradiction.** Design v2's D-8 is 🔴 with *"Φ7 cannot run without a path."*
The readiness plan's own § 3 lists the same fact as **K-8, a BLOCK, halting Φ7**. Its route out is
**I-4**, which sits in § 4.2 — the tier the record defines as *"they improve the system; **they do
not block the trial**."* A block whose only route out is in the non-blocking tier is not routed.

---

## M-5 · MAJOR · The entire "2 of 10" numerator is self-graded, and § 8 violates its own preamble

**Section:** § 8 · **Class:** READ

§ 8's preamble states the rule:

> "Each condition is stated so that **it can be evaluated by someone who was not here**, with the
> instrument that evaluates it. **A condition whose evaluation is a judgement says so.**"

Eight of the ten rows name an instrument or a file test: the gate, the runner, `git cat-file -e`,
file existence, `fulltext_receipts.py`, a directory listing. **The two rows scored ✅ are the only
two whose "Verified by" column is the reading of a document** — row 8 *"design v2 § 8.1"*, row 9
*"reading § 10.3"*. **Neither declares itself a judgement.** The score's whole numerator is
composed of the two rows the preamble required to be flagged and which are not.

**Row 8 — "Roles defined ✅ YES — this one is done, and done well."** Its criterion is *"every
phase has a named owner, and for each owner the record states whether its authority traces to an
instrument or to a contract clause standing alone."* Its cited evidence, design v2 § 8.1, is a
**six-seat** table, not a per-phase map; § 8.3 immediately below it records *"Plan owns 6 of 17
phase rows … **and nothing checks it (H-17)**"*; and the seat that produces the object the whole
trial audits — `reader-L` — carries **⚠️** and an open decision, **D-4**, which the readiness plan
never surfaces (M-4). A row cannot be "done, and done well" while the row beneath its evidence
says nothing checks the largest owner and the reader's standing is an unanswered question.

**Row 9 — "Falsifiers satisfiable ✅ YES", verified by "reading § 10.3".** This is the third
instance of the H-14/H-19 shape the register closed twice: **the check's input is authored by the
party the check is about, and the check is performed by reading it.** No observation could make
row 9 come out NO. It has no falsifier of its own, which is precisely the property it certifies
in others. Secondarily, § 10.3 contains a row — `D-LAYER` — whose falsifier column is `—`; design
v2 excuses it as *"not a dimension"*, but row 9's criterion says *"every dimension in § 10.3"*,
and the ✅ is given without naming the exclusion.

---

## M-6 · MAJOR · N-2's decomposition is by suite name; the causal attribution is incomplete, and one "fails in BOTH" suite has a local-only failure

**Section:** § 0 N-2, § 2.2 · **Class:** RE-DERIVED

The set arithmetic is **exact and I confirm it**. Local run at this HEAD, exit 1, the eight named:
`test_documented_commands` · `test_fresh_clone_reader_journey` · `test_release_runner_verdict` ·
`test_locator_obligation_reaches_every_route` · `test_abstract_corpus_is_not_evidence` ·
`test_release_surface` · `test_fulltext_trace_contract` · `test_session_self_eval`. Against the
audit's CI eight, the intersection is **6**, the symmetric difference **4**. Correct.

**The causal claim is not.** The record labels the six *"Content defects — fail in BOTH"* and
attributes them to *"audit causes A (5 tokens) + B (unregistered suite) + C (exec bits)"*. I ran
all six individually and read every failure. Five suites match the attribution exactly. **The
sixth does not.** `test_release_surface` fails locally on **two** tests:

```
test_shebang_python_entrypoints_are_executable   → the 4 exec bits          (cause C ✓)
test_no_public_file_is_silently_gitignored       → ['.claude/settings.local.json',
                                                    'deployment/local_instance.md']
```

Both of those files are **untracked at HEAD, gitignored, present only on this disk** — verified
individually, with `HEAD:CLAUDE.md` as a positive control for the tracked test. **They cannot
exist in a CI clean checkout.** That failure is working-tree contamination — the exact class the
record isolates as "local-only" — living inside the class it labels "fail in BOTH".

Neither `LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md` nor the readiness plan names
`test_no_public_file_is_silently_gitignored` (grep count 0 in each; positive control:
`test_release_surface` appears 6 and 1 time respectively). So:

- the "local-only working-tree contamination" class is **2 suites but ≥3 failures**;
- the "fails in both" class contains a suite whose local failure set is a **strict superset** of
  its CI failure set;
- N-2's decomposition is *"exact"* at suite granularity and **not exact at failure granularity**,
  which is the granularity its causal sentence claims.

This is the "a causal story is not a measurement" failure: the record explains *why* the six fail
by importing the audit's CI causes, rather than reading the local failures it had in hand.

**On licensing the comparison.** The two runs are at different commits (`788c357` vs `30cb4f3`),
different trees, different environments. I checked what makes it licensable: the three intervening
commits touch **one file**, `learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md`, +532 lines,
and no suite or subject file. On that basis the comparison **is** licensed for the tracked-content
half — and the record never states this, so it holds a licensed comparison without its licence. It
is *not* licensed for the working-tree half, which is exactly where it breaks (above).

---

## M-7 · MAJOR · Φ−1's exit criterion cannot detect the defect that motivates Φ−1, and Φ−1 makes that defect permanent

**Section:** § 9 Φ−1, § 0 N-3 · **Class:** RE-DERIVED

N-3's finding is that a record can cite a blob that does not exist: *"Design v2's
`consumes_by_blob` block already contains one unresolvable reference, and the register that cites
it does not know."*

Φ−1's exit criterion is:

> `EXIT: git cat-file -e fires on all 7 blobs · gate reports 0 identifier blocks`
> `FALSIFIER: any DIRECT_IDENTIFIER survives → Φ−1 did not close`

**That tests the blobs of the committed files. It does not test the blobs those files cite.** After
Φ−1, `cat-file -e` fires on all seven committed records and the dangling citation inside two of
them is untouched and undetected. **The falsifier does not cover the defect the phase exists to
repair.**

Worse, Φ−1 makes it irreparable. `9d744eb7…` is cited in exactly two places:

```
learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_EXECUTION_PROTOCOL_v1.md:27  (consumes block)
learning/orchestrator/LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v2.md:42
```

Both are among the **five "clean" records B-1(b) commits immediately**. B-1(b) also **redacts**
design v1 before committing it — which changes its bytes and therefore its hash. **After Φ−1, two
committed records permanently cite a blob that will never exist in any object database, and the
record does not say so.** The only window in which `9d744eb7…` could be preserved as cited is
before the redaction, and the record's recommended option closes it.

---

## M-8 · MAJOR · § 5's "Condition 2" is a promise with no detector, and two answers to B-2 make the success criterion unsatisfiable

**Section:** § 5 Recommendation, Condition 2 · **Class:** READ

> "**Condition 2** — if B-2 is answered (b) or (c), the recommendation degrades to A and must say
> so in the outcome. An option C without its audit instrument is option A with a longer phase
> table, and the record must not let that substitution happen silently."

The record names **no detector**: no phase, no artifact, no gate, no falsifier, and no party whose
job it is to notice. The nearest mechanism is Φ0's exit — *"every § 8 checklist row is YES or
carries an operator-signed waiver naming its cost"* — under which B-2 = (b) makes row 4 NO and the
waiver is permitted to name any cost at all. Nothing requires the waiver to say "this is now A".
The outcome record that "must say so" is authored at Φ1's close by the track itself. **Who would
notice: nobody named. The condition is a promise the record makes to itself.**

And it is worse than undetected. Design v2 § 10.1: **TRACK-M succeeds** only if *"the crossover ran
against the § 9.7 schema with the shuffle recorded first."*

- Under B-2 = **(c)** *"anchored condition only"*, the crossover cannot run → unsatisfiable.
- Under B-2 = **(b)** *"improvise at Φ7"*, no schema exists before the shuffle → unsatisfiable
  as written.

§ 10.1 is scoped *"to the chosen rung"*, and the degradation ladder's rungs are about **personnel**
(BL-2, Mirror, Plan, one auditor), never about the schema. **No rung covers a B-2 = (b)/(c) world.**
So the record recommends path C while leaving open a decision two of whose three answers leave
TRACK-M with a success criterion that cannot be met and no rung that rescopes it. **That is P-15's
defect — a success criterion unsatisfiable under a configuration the record itself offers —
reappearing on a new axis, in the record that quotes design v2's fix of it.**

---

## M-9 · MODERATE · § 7.3's "the object nobody gates" is gated, and § 7.4 says so

**Section:** § 7.3 vs § 7.4 A-1 · **Class:** RE-DERIVED (READ of the walker)

> "Neither gate sees what the other sees, and the union is not covered by running both. …
> **The object nobody gates is the one that matters most here: files that exist, carry
> identifiers, and are not yet committed.**"

`walk_publishable` is an `os.walk` over the **disk**, pruning `SKIP_DIRS`
(`.git .venv venv node_modules __pycache__ backup`), nested checkouts (so the sibling worktrees are
excluded), and `unpublishable_paths` — whose docstring defines it as *"paths that are
simultaneously untracked **and** gitignored"*. Everything untracked-and-not-ignored **is scanned**.

That set is exactly *"files that exist, carry identifiers, and are not yet committed."* **The
record's own N-1 is the proof that they are gated: N-1 was produced by running the gate locally.**
A local gate run covers the committed tree ∪ the uncommitted-and-not-ignored files, i.e. a
**superset** of CI's privacy scope. What CI has that a dirty local run lacks is the clean-clone
pass, which short-circuits after `DIRTY_RELEASE_TREE` — and those are release-surface checks, not
privacy.

The record's own § 7.4 A-1 states the true problem correctly: *"It needs no new rule — the rule
exists and fires correctly; **it needs a moment**."* § 7.3 escalates a missing *moment* into a
missing *mechanism*, and titles itself *"the finding that changes the architecture question"* on
that escalation.

---

## M-10 · MODERATE · "The tracked repository is clean" overstates, and the omitted output is where

**Section:** § 0 N-1 · **Class:** RE-DERIVED

The negative is correctly denominated and correctly scoped for its code: over the **581** tracked
files at HEAD, `DIRECT_IDENTIFIER` = **0**. I re-derived 581 and the 0. But the record generalises
to *"**The tracked repository is clean**; the planning corpus is not."*

The gate run the record quotes emits **four findings it does not show**:

```
[REVIEW] PARENT_OF_ORIGIN_ATTRIBUTED disease-models/wwox/research/deepdive_manifests/PMID39416860.json:116
[REVIEW] PARENT_OF_ORIGIN_ATTRIBUTED disease-models/wwox/research/deepdive_manifests/PMID42082822.json:22
[REVIEW] PARENT_OF_ORIGIN_ATTRIBUTED disease-models/wwox/research/deepdive_manifests/PMID42082822.json:84
[REVIEW] PARENT_OF_ORIGIN_ATTRIBUTED disease-models/wwox/research/full_text_queue_current.md:1662
```

All four are in **tracked** files, all four carry the message *"Not blocked; read it before
publishing"*, and the record's quoted block shows only the `[BLOCK]` lines. The blocks are
correctly reported; the **verdict about the tracked repository** is drawn from a filtered view of
the instrument's own output. "Zero blocks of one code" is not "clean" — and this matters
downstream, because Φ−1's exit (M-7, below) certifies privacy on exactly this code.

---

## M-11 · MODERATE · The record is now a source of the failures it reports, and did not disclose it

**Section:** § 0 N-2, § 11 · **Class:** RE-DERIVED

N-2 names the self-reference for the *audit* document — *"An audit document cannot be written in
this repository without turning the battery red, which is a self-reference worth naming"* — and
does not apply it to itself. At this HEAD, `test_documented_commands` fails on:

```
learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md:129   dot-slash file.py reference
learning/orchestrator/LEGEND_OPERATIONAL_READINESS_PLAN_v1.md:680   run_release_regressions.py
                                                                    does not expose --porcelain
```

The second is not a quoted example — it is the record's own § 12 verification command, whose shell
continuation is joined by the parser into one logical line so that `--porcelain` is read as an
argument to the runner. **The record's verification trail introduced a new, distinct CLI-contract
failure into the suite the record is reporting on.**

Consequently N-2's *"11 offending hits"* is **12** — I enumerated the set: 6 sibling-worktree, 3
audit, 2 backup (the record's three buckets, all correct) **plus the record itself** — and the
suite now fails on two tests rather than one. § 11's *"This one file is its only output"* is false
in effect: its other output is a changed value of the measurement N-2 reports.

---

## M-12 · MODERATE · § 12 is a transcript of commands, not a runnable trail, and one command writes into the repository

**Section:** § 12 · **Class:** RE-DERIVED

§ 12's header: *"Every figure in this record is below."* Three defects in the trail as printed:

**(a) The status sentinel cannot return what it claims.** The record's line writes `pre`, runs the
battery, writes `post`, and diffs them, commenting *"identical — the battery wrote nothing"*. I
reproduced the exact shell semantics in a sandbox repository:

```
[pre]   ?? pre
[post]  ?? post
        ?? pre
        → diff reports "0a1 > ?? post".  NOT identical.
```

The shell creates each sentinel before `git status` runs, so `post` always lists itself. Neither
`pre` nor `post` is gitignored here (`git check-ignore` exits 1 on both), so **running § 12 as
printed writes two untracked files into the repository root** — while § 11 states the record
*"stages nothing, commits nothing"* and *"This one file is its only output."*

**The underlying claim is nonetheless TRUE.** I ran the battery holding both sentinels in a
scratchpad outside the repository: the status output is byte-identical before and after. **The
battery wrote nothing.** The finding is about the receipt, not the fact — and the fix is the one
this review used: put the sentinel outside the thing you are measuring.

**(b) The blob loop is not executable.** `for b in e88dc043… d5c0d296… ee00195f…` uses the literal
ellipsis character. It cannot run.

**(c) One command does not produce its own number** — see M-13.

---

## M-13 · MODERATE · "13 files" is 10 files and 3 directories, and the prose enumeration says 9

**Section:** § 6, § 12 · **Class:** RE-DERIVED

§ 6: *"Benchmark packet — ✅ **EXISTS — 13 files**: `benchmark_manifest.json`,
`surface_spec.json`, `population/evidence_units.json`, and **6 instruction files**…"*
§ 12: `find framework/eval/benchmarks/BENCH-AB-001 -type f | wc -l   # 13`

Enumerated, not counted:

| # | Path |
|---|---|
| 1 | `benchmark_manifest.json` |
| 2 | `surface_spec.json` |
| 3 | `population/evidence_units.json` |
| 4–10 | `instructions/` — `ASSIGNMENT.scientist-a.md` · `ASSIGNMENT.scientist-b.md` · `BENCHMARK_INSTRUCTIONS.md` · `MODE_A.md` · `MODE_B.md` · `OUTPUT_SCHEMA.md` · `SURFACE_CLAUDE.md` |

**10 files**, on disk and at HEAD, identically. `find` **without** `-type f` returns **13** — the
10 files plus the 3 directories. The receipt's command is not the command that produced the
receipt's number. Three internally inconsistent figures in one row: the count says 13, the prose
enumeration adds to 9, and the truth is 10; the *"6 instruction files"* are **7**.

The conclusion — the packet exists and is built — survives. The row that carries it does not
survive its own arithmetic, in a record whose method rule is to enumerate before counting.

---

## M-14 · MODERATE · "43 lines" is wrong on every ref and in the file's only revision

**Section:** § 2.2 · **Class:** RE-DERIVED

*"CI — **one** workflow, `public-release-gate.yml`, **43 lines**, `on: push` unfiltered,
`fetch-depth: 1`, `--mode release`."* Every other clause verifies. The line count does not:

| Ref | lines |
|---|---|
| `legend-operating-convention-v1` · `main` · `mirror` · `orchestrator` · `lettore` · `evidence-index` · `scientist-ab-spec` | **48** each |

The file has **one** commit in its entire history (`a2e0dd0f`), at 48 lines. **There is no ref and
no revision at which it is 43.** § 12 carries no command for this figure. It is an object figure —
by the record's own § 12 classification, the kind that *does not decay* — and it is simply wrong.

---

## M-15 · MODERATE · The record misclassifies figures in the very sentence that teaches the classification

**Section:** § 12 closing note · **Class:** RE-DERIVED

> "`581`, `10 of 581`, `0 ACTIVE`, `72`, `174`, `16`, `25`, `57` are **population**. `9d744eb7…
> ABSENT`, `4 of 4 mode 100644`, **`65 vs 66`**, the per-ref matrix, and *'the gate blocks on 5
> identifiers'* are **object** facts about named objects."

**`66` is population.** It is `git ls-files | grep -cE '(^|/)test_[^/]*\.py$'` — a count over a
glob of tracked files at HEAD, structurally identical to `581`, which the same sentence classes as
population. It grows the instant anyone adds a test file. The derived *"exactly 1 never executed"*
is the difference between an object-derived count (65, the cardinality of `TESTS` in a named
script) and a population-derived one, and is therefore population-derived. Both re-derive to 65 and
66 today; the class is wrong, and the class is what tells a later reader whether a conclusion moved.

**And one figure is unclassified and already false.** N-3's *"Total corpus at risk from one `git
clean -fdx`: **7 files, 4 301 lines**"* appears in no class list. It is population, and it decayed
**within the record's own authorship**: I measure **8 files, 5 086 lines**, because the readiness
plan is the eighth. The record's own existence falsified its own count, in the section that warns
population figures decay.

---

## M-16 · MINOR · "67 findings … minus overlap" has an unstated subtrahend and is classed `object`

**Section:** § 2.1 · **Class:** READ

*"2 rounds, 4 reviews, **67 findings** total (33 on the protocol, 44 on design v2 rev 1, minus
overlap)"*, evidence column *"both registers"*, class column **`object`**. 33 + 44 = 77, so the
overlap term is 10. **That 10 is never stated, never enumerated, and carries no command in § 12.**
I re-derived 44 for the TRIAL-002 register (44 distinct `H-`/`P-` tokens, two independent
countings agreeing) but could not cleanly re-derive 33 or the overlap, and I do not report a
number I did not enumerate. A count reached by subtracting an unstated quantity is not an object
fact about a named object.

---

## M-17 · MINOR · § 7.1's linearity is asserted over a population that was not enumerated

**Section:** § 7.1, § 2.2 · **Class:** RE-DERIVED

> "**All three are on one strictly linear history** … 🔴 **Strictly linear — there is no divergence
> to reconcile, and therefore no merge problem to solve.** The mandate's question about *'merge
> manuali continui'* has, today, an empty referent."

The measurement is three `main` refs. `git ls-remote --heads origin` returns **two** branches:
`main` at `8ab8e4b` and **`harden-release-scan-scoping` at `86c349a`**, which the record never
names. I extended the check: `86c349a` **is** an ancestor of HEAD, so **the conclusion survives**
and I report that at full weight. But it survives by luck of the denominator, not by method: a
statement of the form *"there is no divergence anywhere"* was drawn from a sample of one branch
per remote, in a record whose § 8 preamble demands evaluability by someone who was not present.

---

## M-18 · MINOR · Two OPCON figures carry no command and one does not reproduce

**Section:** § 2.3 · **Class:** RE-DERIVED / UNVERIFIABLE

*"OPCON-v1 — `DRAFTED`. Reaches **1** file at HEAD … the convention proper lives on `mirror`
(**8 files**)"*, evidence *"per-ref sweep"* — but § 12 contains no OPCON sweep. The HEAD figure
re-derives (**1**: `learning/orchestrator/OPCON-V1-SECTION-A-SOURCE-001.md`). The `mirror` figure
does not: my pattern returns **5**. Without the record's pattern I cannot say which of us is
measuring the right set, so I report it as **unverifiable as printed** rather than as an error —
which is itself the finding, in a § 12 whose header claims every figure is below it.

---

## M-19 · MINOR · One word carries two incompatible meanings in the same record

**Section:** § 2.1 vs § 0 N-1 · **Class:** READ

N-1 uses *"identifier"* for a registered personal token whose presence blocks publication. § 2.1's
input-paper row uses it for the PMID/PMCID: *"**10 of 581** tracked files carry the identifier"*
(re-derived: 10). A reader arriving at § 2.1 after N-1 reads "ten tracked files carry a personal
identifier" — the exact opposite of N-1's finding, which is that zero do.

---

## M-20 · MODERATE · The plan's next act produces no observation about science

**Section:** § 0, § 3, § 8, § 9 · **Class:** READ

The mandate's guiding question is *"does LEGEND really improve the traceability, verifiability and
correctability of scientific analysis?"* Measured against that question, the record's mass sits on
the container:

- **All four new measurements** are about LEGEND's own machinery: a privacy gate (N-1), a test
  battery (N-2), a git object store (N-3), a freeze verifier (N-4). **None yields an observation
  about a scientific claim, a paper, or a reading.**
- **Of the eight blocks in § 3**, only K-2 (the audit instrument) and K-7 (acquisition) stand
  between today and a scientific observation. Six are repository state.
- **Of the ten checklist rows in § 8**, row 5 is the only one about the scientific input. Rows 1,
  2, 3, 4, 6, 7, 10 are process hygiene; rows 8 and 9 are about the record.
- **§ 7 is entirely infrastructure**, and is the record's longest analytical section after § 0.
- **Φ−1 — the one phase proposed as runnable — is a git-hygiene phase.** Redact, commit, re-run a
  gate. Its exit is `cat-file -e` and a gate verdict. **It produces zero scientific observation**,
  and it stands between the operator and the first one.

The record's own § 1.4 states the governing lesson — *"the trial must not become the construction
of the instrument it reports on"* — and § 9 states *"Infrastructure runs beside this, never inside
it."* **Both are honoured for the trial and abandoned for the roadmap:** the roadmap's first and
only currently-proposed step is maintenance of the container, and the record does not name that it
has moved from beside the path onto it.

**This is a finding about proportion, not about correctness.** Preservation is genuinely urgent
and K-1 is genuinely real. But a readiness plan whose four measurements, eight blocks, seven
checklist rows, longest section and only runnable phase are about the repository is, on the
mandate's own axis, a measurement of LEGEND's machinery reported as a measurement about the
readiness of science. **The record's strongest section, § 5, asks precisely the right question
— and the roadmap that follows it answers a different one.**

---

# WHAT I FOUND NOTHING WRONG WITH

Re-derived, at this HEAD, and correct. No padding: everything below I ran.

- **The hash.** `f12d8ace…`, matching. Both my controls fire, in both directions.
- **§ 2.2.1 — the per-ref control-plane matrix.** I re-ran all seven paths across all seven refs
  — **49 cells** — and added a negative-control row (`NO_SUCH_FILE_CONTROL.md`, all dots) the
  record did not have. **Every cell matches.** The registry on `orchestrator` only; the reading-modes
  protocol on `opcon`/`main`/`scientist-ab-spec` and **not** on `orchestrator`; `DEC-20260822` on
  2 of 7. All seven refs resolve. The record's zsh warnings — no word-splitting on unquoted
  variables, `${r}:${p}` braces against the `:p` history modifier — are correct and necessary; my
  own first sweep in this review hit the adjacent zsh trap (an unquoted `--include=*.md` glob
  returning a silent zero) and only the positive control caught it.
- **N-1's block set.** `BLOCK_PUBLICATION`, 6 blocks, 5 `DIRECT_IDENTIFIER` at
  `FIRST_SCIENTIFIC_RUN_COORDINATION-PLAN-001.md:359,386,484` and
  `LEGEND_FIRST_OPERATIONAL_TRIAL_DESIGN_v1.md:298,546`, 1 `DIRTY_RELEASE_TREE`. Exact, including
  every line number. The per-record 0/0/0/0/0/3/2 table is exact.
- **N-1's reading of the mechanism.** Line 388 is the SHA-256 line; the digest-interior exclusion
  is real; no regex heuristic decides. The citation is accurate (see M-3 for what it does not
  entail).
- **N-2's local eight.** Exactly the eight named, exit 1. The intersection with the audit's CI
  eight is 6 and the symmetric difference is 4.
- **The five-token cause.** All five `test_locator_obligation` / `test_abstract_corpus` /
  `test_fulltext_trace_contract` (×2) / `test_session_self_eval` failures are `CLAUDE.md` token
  absences, exactly as the audit classified them.
- **The local-only pair's mechanism.** `test_documented_commands` walks `ROOT.rglob("*.md")` minus
  `{.git, .venv, node_modules, __pycache__}` — the disk, not the repository — and the record's
  three buckets (6 worktree / 3 audit / 2 backup) are each correct.
- **N-3's core.** `9d744eb7…` is ABSENT while `git hash-object` of the working file returns exactly
  it. `d5c0d296…` and `ee00195f…` PRESENT and reachable from 0 refs. `959b57f4…` PRESENT and
  reachable. C-2's correction of design v2 — *"already gone as an object"*, not merely gc-prunable
  — is right.
- **All five `consumes` hashes.** Every declared blob hash equals `git hash-object` of its working
  file, byte for byte. The citation discipline is exact; only the survival claim about them is not
  (M-1).
- **N-4.** 44 tests, OK, `--is-shallow-repository` false. `test_figure_ppi_preflight` passes locally
  with PyMuPDF 1.26.5. The downgrade of F-08's risk from medium to low is earned.
- **§ 11's hardest disclosure — "It wrote no loose git objects."** This is checkable, and it holds:
  **0** loose objects with an mtime on 2026-08-24, against a positive control of **147** written on
  2026-08-23, over 1 674 total. (Caveat stated: mtime can be falsified by `cp -p` or `git archive`;
  for a negative over a window nobody had reason to backdate, it is sound.) The record disclosed a
  write class its own tooling cannot see, and the disclosure survives an adversarial check.
- **"The battery wrote nothing."** True — when the sentinels are held outside the tree (M-12(a) is
  about the printed command, not the fact).
- **Roughly thirty further § 12 figures**, each re-derived: 581 tracked · 51 framework scripts ·
  57 refs · 25 worktrees (14 prunable) · 174 full texts · 0 Bandini · 72 `FT-` · 16 `CC-` ·
  10 of 581 · 65 registered / 66 tracked / 1 never run · grep 0 for the unregistered suite ·
  4 of 4 mode `100644` · 3 of 5 bootstrap tokens in `AGENTS.md` with `state-control` and
  `session_self_evaluation.md` in neither (positive control fires) · 0 ACTIVE leases with lease #3
  `derived=STALE` vs `stored=EXPIRED` · 4 × `PROPOSED` · 6 `UNVERIFIED` · 1 file in
  `governance/decisions/` · LINT PASS · 128 chained receipts, tail anchored · growth anchors PASS
  at 39/70/356/390 · `origin ⊂ development ⊂ HEAD` with 455 and 3 · local `main` = `788c357` ·
  one workflow, `on: push`, `fetch-depth: 1`, `--mode release` · `requirements-analysis.txt` at one
  package · `4454feab` an ancestor · 526 and 122 lines · 988 · 102 · 678 · 44 · `reviews/` holding
  `plan/` and its 3 files · GATE 0's text · 0 of 16 `CC-*` carrying `MIRROR_REVIEW`.
- **The circularity design v2 was accused of, in § 5.** The crossover's comparator is the bare
  condition — a re-read against **the paper**, which is outside the system under test. The
  auditors are inside LEGEND but the referent is not. `ANCHOR-ADDS` and `ANCHOR-MISLEADS` are both
  reachable and neither is structurally favoured. **§ 5's axis-4 analysis is the strongest
  reasoning in the document**, and its conclusion — that only C can measure LEGEND's contribution,
  because a design in which the unfavourable cell cannot be populated is not a measurement — is
  correct and correctly argued. The circularity I did find is in § 8 (M-5), not here.
- **The refusal in § 1.4.** *"Where something must be built, it is named as construction and
  priced, never smuggled in as preparation."* I looked for a smuggled build across §§ 4, 5, 7, 9
  and did not find one. B-2 prices the schema. § 6 names actorhood as *"must be granted, not
  built."* A-1/A-3 are named as new. **This discipline holds throughout.**

---

# WHAT THE RECORD UNDERSTATES IN ITS OWN DISFAVOUR

- **The object-loss problem is roughly twice as bad as N-3 says.** N-3 reports one absent blob.
  Of the eight untracked planning records, **four have no object at all** — design v1, design v2
  revision 2, the bootstrap audit, and the TRIAL-002 register — plus the readiness plan itself. Of
  the eight, **three** are recoverable from the object database and **two** from a ref. K-1's
  urgency is understated by its own measurement (M-1).
- **The local-only contamination class is larger than 2 suites.** `test_release_surface` carries a
  third contamination failure inside the class the record calls "content defects" (M-6). B-3's
  option (c) — *"green in a laboratory worktree"* — is therefore even less reachable than the
  record argues, and A-3's *"scope the disk-walking suites to `git ls-files`"* has one more site to
  cover than the record enumerates.
- **§ 2.2.1's dispersal is wider than the seven rows sampled.** The BENCH-AB-001 packet, which § 6
  calls built, exists on **3 of the 7** sampled refs and on **0** of `mirror`, `orchestrator`,
  `lettore`, `evidence-index`. K-5 is broader than the record's table shows.
- **§ 11's disclosure discipline exceeds what anyone asked for**, and it survived the hardest test
  I could put to it. That is worth saying beside the defects.

---

# VERDICT

**Bound to blob `f12d8acecb5acc6d5a7a96662a398dc846e57573`, measured by me at
`legend-operating-convention-v1` @ `30cb4f3fd700e2aaf6b608e363438f883ddc3760` on
2026-08-24T08:25–08:52Z:** the record's instrumented measurements are unusually sound — I
re-derived roughly forty figures and the entire 49-cell control-plane matrix and found three wrong
— but its two load-bearing conclusions rest on a hazard block that is false about its own inputs
(M-1) and on a single act that requires an authority its own standing denies it (M-2), while its
only ✅ rows are self-graded (M-5), its blocking-decision set omits two of design v2's red
decisions (M-4), and its one runnable phase produces no observation about science (M-20); nothing
here is a blocker unless the operator makes it one.
