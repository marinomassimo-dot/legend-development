---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0013
actor_id: mirror
subject: review of CAND-20260818-SCIENTIST-AB-SPEC revision 5 — the remedy is complete and the
  sentence justifying it says the decision inside it was not a decision
review: reviews/mirror/REV-SCIAB-MIRROR-005.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×1, fourth sighting on one seam, moved one level up) ·
  MICRO_UPGRADE (×1, a new form: the instrument was the shell) ·
  BEST_PRACTICE_CONFIRMATION (×1) · CURATION (Annex E.2, over SLR-plan-0005)
derived_from: [SLR-mirror-0010, SLR-mirror-0011, SLR-mirror-0012, SLR-plan-0004, SLR-plan-0005]
---

# The family moved from what was measured to what was claimed about why

## 1 · FAILURE_PATTERN — the justification of a remedy is an artifact, and nobody reviews it as one

Four revisions, one seam:

```
M-2  scoped to one spec key          → the exemption lived in two          (population)
M-3  scoped to one skip condition    → the predicate had four              (population)
M-4  scoped to one CLI flag          → the sentence printed under two      (mode)
M-5  the remedy is complete          → the section justifying it overreaches (provenance of the rule)
```

`M-5` is not a scope error and it is not a false claim about what the instrument checks — I looked
for one and there is none. It is in the section revision 5 **added** to explain why its one new
rule is right, and it says the rule was *derived* when the derivation reaches only half of it: the
writer-identity premise entails that an unanticipated file is an **anomaly** before handover and an
**artifact** after, and it does not entail that an anomaly must **block** rather than be enumerated.

**Why my own three prior rules did not catch it.** `SLR-mirror-0011` §1 and `SLR-plan-0004` L-1 are
about **populations**. `SLR-mirror-0012` §1 is about **modes** — *enumerate the invocations that
reach the printing site*. I applied all three, and all three passed: the census runs in both modes,
every population reconciles, every printed sentence is true of its own run. The defect was in
**none of the things any of those rules point at**. It was in the prose that argues the remedy is
correct, which no rule of mine had ever named as a reviewable object.

**The generalisation.** *A remediation has three artifacts, not two: the behaviour, the claim it
prints, and the argument that the behaviour is right. The third is the one written last, reviewed
least, and canonicalized anyway. Read it as a claim with premises, write the premises out, and
check whether the conclusion is the one they reach — especially when it introduces a rule that
needs an approval the argument makes look unnecessary.*

The sharpest form of the test, which is what I actually did: **for every new normative rule, ask
whether a design consistent with all the same premises would have chosen differently.** If one
exists, the rule is a decision, and the text must say so — because a decision described as an
entailment is a decision removed from whoever holds the authority to make it.

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (mirror, this session) — the provenance axis is new; the
family it belongs to has four sightings and is `SLR-mirror-0011` §1 / `SLR-mirror-0012` §1 /
`SLR-plan-0004` L-1 / `SLR-plan-0005` L-1.
`CLASS: FAILURE_PATTERN` · `STATUS: LOCAL` · `SCOPE: every remediation this actor reviews`.

**What I will do:** when a candidate adds normative text to justify a remedy, write the premises
and the conclusion out as numbered lines with their sources before reading the implementation, and
test each inference for the alternative it does not exclude. In this review that took about twenty
minutes and it was the whole finding.

---

## 2 · MICRO_UPGRADE — a new form: the instrument was the shell, and no control of mine could have caught it

Sixth and seventh sightings in my own harnesses, and the second is not like the others.

**(1) The familiar form.** My independent file-universe probe reported
`PRESENT 48 · SCANNED 0 · CENSUSED 0 · SILENT 48` in **both** modes — a partition claim false in
the opposite direction, produced in a review whose subject is a partition claim, and identical in
shape to the defect `SLR-mirror-0012` §2 records. The cause was a wrong `--surfaces` argument
giving `rc=2` on every run. Caught by the instrument check requiring `roles/scientist.md` to be
observed leaking. Run discarded, harness re-authored. The rule held, again, for the fifth time.

**(2) The new form.** Checking a load-bearing premise of the candidate's §4.4 — that the ex-ante
blinding `grep` §2.3 records returns `0` over a UTF-16 file — my check returned **7** for the
BOM'd case. That would have falsified the premise, and I was one step from writing it as a finding.

The defect was not in my script. `grep` in this session's shell is a Claude Code shell **function**
that shims to `ugrep`, and `ugrep` auto-decodes a UTF-16 BOM. `/usr/bin/grep` — the one the
protocol's recorded command means — returns `0`. Plan's premise is true.

**No positive control inside my probe could have caught this.** Every control I could have written
would have run through the same shimmed binary and agreed with itself. What caught it was that the
result contradicted a premise I had independent reason to expect held, so I went and asked which
`grep` had answered.

The rule that follows is narrower than the one I already hold, and it is not a substitute for it:
**when a measurement depends on a tool the artifact names by bare name — `grep`, `python3`, `diff`,
`sort` — the identity of that tool is part of the measurement. Resolve it before reporting a result
that turns on its behaviour.** The general instrument-check rule protects against my *script* being
wrong; it does not protect against my *environment* answering a different question. This is the
first time in seven sightings that the failure was below my own code.

🔴 **Not self-ratified.** This is an observation about Mirror's own review method. G.2 forbids
Mirror approving material changes to its own rubric: if it is to bind, it goes
`MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by Orchestrator. Filed
`LOCAL` and applied as a personal practice, which E.4 permits.

**(3) A third, minor.** My AST audit of the thirteen added probes reported two as exit-code-only
because it did not follow their delegation into `_assert_partition`. Reading the helper corrected
it; `N-6`'s claim is true. Same family as (1): a container-level reading standing in for the thing
inside it, which is `REV-SCIAB-MIRROR-002`'s *"a set of containers is a count wearing a list"*
pointed at my own instrument.

```
CONFIRMATION_CLASS  ORIGINAL_OBSERVATION (mirror, this session) for the tool-identity form;
                    REPLICATION of SLR-mirror-0010 §4 / -0011 §3 / -0012 §2 for (1) and (3)
CLASS               MICRO_UPGRADE
STATUS              LOCAL — G.2 bars self-ratification of a review-method rule
SCOPE               every battery this actor writes
```

---

## 3 · BEST_PRACTICE_CONFIRMATION — compare the sets, not the counts, and it paid twice

`REV-SCIAB-MIRROR-004` and the operator's own standing rule both say a count agreeing is not a
check. Twice this session the counts agreed and only the sets settled it.

**(a) The discrimination.** Plan reports *"the 3 that stop failing are the two positive controls and
the post-read partition"*. Raw: 20 non-passing against revision 4's tool; with the `MODE` line
back-ported: 17. A count check says *3 stopped, claim confirmed*. The set check says something the
counts hide: **five** entries changed status, because two tests moved from `FAIL` to `ERROR` and
remained non-passing. Comparing test **names** rather than result lines gives exactly three, and
they are exactly the three Plan names. **Plan's claim is exact — and a count comparison would have
"confirmed" it through an arithmetic coincidence.**

**(b) The regression.** Six failing suites and seven failing tests at both tips is the same pair of
numbers Plan reports. What makes it evidence is that the two *sets* are identical, that the seven
per-test failure blocks are byte-identical after a normalization that touches no assertion text,
and that the three targets with no test-id granularity were compared on their whole normalized
output rather than counted as passes.

`CONFIRMATION_CLASS: REPLICATION` (mirror, this session) of the standing rule · `CLASS:
BEST_PRACTICE_CANDIDATE` · `STATUS: LOCAL`. Its addition from this session is that the rule has a
**failure mode of its own**: a set comparison run over *result lines* rather than *identities*
reintroduces exactly the defect it exists to prevent. The key is the thing being compared, not the
fact that a set was used.

---

## 4 · Curation performed (Annex E.2), and the instrument it still has no home in

I curated the four entries of `SLR-plan-0005`. All four classes accepted, two `REPLICATION`s added
by me (on L-3's extension, and on L-4's encoding facts, which I reproduced by construction). One
formulation **SUPERSEDED with reason** — L-2's *"inherited from the other point it looks like a
design decision when it is an unexamined transfer"* — because the inverse happened here: a
writer-identity fact settled the direction of an asymmetry and was read as settling its level,
making a design decision look like an unexamined transfer pointed the other way. That is `M-5`
stated from the learning side, and Plan's own L-4 already contains the discipline that catches it.

Two of Plan's entries are about **me**, and both are right. L-4 shows my `P-7` boundary sentence is
false — an em dash in BOM-less UTF-16 is non-ASCII and encodes entirely below `0x80` — while my
conclusion survives, and Plan declined to inflate the correction into a finding. That is the
behaviour I would want from a reviewer and I got it from an author. L-1 credits the mode-axis
observation to my `SLR-mirror-0012` §1 rather than claiming it, and then **adds** the diagnosis I
did not have: my prior rule was about populations and could not reach a mode error. I adopt the
refinement.

**The curation still has no home.** `LEARNING_INDEX` is named by E.2 and has never been
materialized. This is the **fourth** consecutive review in which a curation E.2 calls Mirror's
exclusive act is recorded in a review artifact and a session record, where nothing queries it, and
the fifth in which dedup was performed by reading a directory by hand — this time seven records
across two actors. It is not a finding against this candidate, I did not raise it as one, and it is
the metric this laboratory says its next governance will be born from, still unbuilt while the
records it should index accumulate faster than before.

---

## 5 · What did not go wrong, recorded because it is the metric that matters

Revision 5 refused the cheaper of the two remedies I offered and said why, in the durable record,
before I could ask. It removed the default from the mode parameter rather than fixing the one call
site, so the class of defect cannot recur by omission. It made the mode a runtime fact the tests
assert from the tool's own output, and when I mutated the helper to point the handover oracle at
the wrong mode, **eighteen tests failed** — the repair is not the same shape one level up, which is
the specific thing I told it to check. It corrected my own false boundary while using it, kept my
conclusion, and converted my prose into three executable rows. It disclosed three wrong numbers
from its own harnesses rather than replacing them, and the corrected count reconciles with mine
exactly — same seven tests, same seven reasons, two independently authored instruments. It carried
`P-4`, `P-6` and `N-7` without letting the remedy's stronger language absorb any of them, and it
closed exactly one thing: `P-8`, a number in a manifest.

The fifth revision of this candidate is the fourth in a row that is better on measurement rather
than on assertion, and `M-5` is the mildest blocking finding I have written against it.

---

## 6 · Boundary of this record

`N-7` is unreconciled for the fourth review running and I did not settle it; I did not re-run
revision 1's tool. `M-5` is a judgement about how a normative sentence will be read, not a
measurement, and I weigh it as blocking on consistency with `REV-SCIAB-MIRROR-002`'s rejection of
carrying a false claim as a debt and on H.1 placing MAJOR approval with the operator — an
adjudicator could reasonably weigh it as `P`-class, and the review says so rather than hiding it.
`P-6` (`.git/**`) is pre-existing and did not influence the verdict; `P-9` and `P-10` are
control-plane numbers and did not either. `R-10` remains: this branch still carries P5 **v3** and
the pre-fix hash script, it moved numbers again, and it is my debt and not the candidate's — fifth
review running. Time is date-only. Nothing under another actor's worktree, `main`, or the root
checkout was written; the packet was read from root read-only; `scientist-ab-spec` was read from
git objects without merging. No `SESSION_REF` was declared or inferred, and no prior Mirror session
was superseded.

## 7 · Persistence

`WORK_COMMIT` on branch `mirror`, under `learning/mirror/` (E.6, A.7). This branch is not a
candidate branch, so the record moves no candidate binding.
