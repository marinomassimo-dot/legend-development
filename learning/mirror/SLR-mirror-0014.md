---
artifact: MIRROR Session Learning Review (body §15, Annex E.6)
record_id: SLR-mirror-0014
actor_id: mirror
subject: review of CAND-20260818-SCIENTIST-AB-SPEC revision 6 — the sentence was repaired, the
  class it belonged to was not, and my own shell forged a clean set of zeros
review: reviews/mirror/REV-SCIAB-MIRROR-006.md
date: 2026-08-19
outcome: FAILURE_PATTERN (×1, in my own harness: the shell as instrument, second form) ·
  MICRO_UPGRADE (×2) · BEST_PRACTICE_CONFIRMATION (×1) ·
  CURATION (Annex E.2, over SLR-plan-0006)
derived_from: [SLR-mirror-0010, SLR-mirror-0011, SLR-mirror-0012, SLR-mirror-0013,
  SLR-plan-0004, SLR-plan-0005, SLR-plan-0006]
---

# A falsifier that returns zero is a claim, and mine was a syntax error

## 1 · FAILURE_PATTERN — my shell truncated a path and the loop reported clean zeros

`CONFIRMATION_CLASS: REPLICATION` of `SLR-mirror-0013` §2 (mirror, this session) on a **new form**
· `CLASS: FAILURE_PATTERN` · `SCOPE: LOCAL → offered for wider scope` · `STATUS: proposed`

The load-bearing negative in this review is `M-5`'s falsifier: *is there a clause, at `BASE_HEAD`
or at revisions 1–4, requiring an unanticipated-but-allowlisted artifact to exit non-zero?* If one
exists, the blocking level is entailed after all and the whole verdict inverts.

I ran it. It returned **zero at every tip**, which is the answer I expected, and I nearly wrote it
down.

```zsh
for tip in b965ca58 daaa3335 …; do
  c=$(git show "$tip:framework/protocols/controlled_benchmark_ab.md" 2>/dev/null | grep -c …)
```

In `zsh`, `$tip:fr…` consumes `:f` and `:r` as **history modifiers**. Every `git show` received
`b965ca58amework/protocols/…`, failed, and wrote its error to the `/dev/null` I had helpfully
supplied. The loop printed six clean zeros.

Two things made it survivable and neither was the script. The first is that a *different* number in
the same output was impossible: the rev-5 protocol showed `EXPECTED_BY_PROTOCOL 0` when I had read
that string in its §4.4 table twenty minutes earlier. The second is that I ran an instrument check
before using the result — a string I knew was present had to come back present.

`SLR-mirror-0013` §2 recorded the shell's `grep` shimming to `ugrep` and auto-decoding a UTF-16
BOM. This is the same family and a different organ: there the shell's *commands* were not what they
named, here the shell's *quoting* silently rewrote an argument. **The generalisation is not "check
your greps".**

> **The rule I am proposing:** *a harness whose negative result is load-bearing must carry a
> positive control in the same run and in the same shell, and `2>/dev/null` must never be inside
> the loop that produces the negative. A silenced error and a true zero are the same bytes on the
> terminal, and the only thing that tells them apart is a check that must fire.*

I have now committed a wrong load-bearing zero in three consecutive reviews (`-004` argv, `-005`
`--surfaces`, `-006` quoting). The instrument check caught all three. That is the practice earning
its keep, not me getting better at shells.

---

## 2 · FAILURE_PATTERN — my hostile harness wrote into the population it was measuring

`CONFIRMATION_CLASS: REPLICATION` of `SLR-mirror-0011` §3 (mirror, this session) · `CLASS:
FAILURE_PATTERN` · `SCOPE: LOCAL` · `STATUS: proposed`

To plant a UTF-16 payload and restore afterwards, I kept the pristine bytes beside the target —
`<file>.mirror-orig`, inside the surface. `verify` reported both copies as `NOT ALLOWLISTED`,
correctly, and my pre-handover run came back with **4 findings** where the tool produces 2.

The tool was right and my numbers were mine. What is worth recording is that the contamination
looked exactly like a finding: an extra `[BLOCK]` line naming a real path, in a review whose whole
subject is whether the tool blocks the right things. I could have written it up as a defect.

The repair is structural, not care: backups now live **outside** the surface tree, and a clean-pair
control must `PASS` in both modes at both revisions before any hostile run is read. That control is
what turns "2 findings" into evidence instead of a number.

---

## 3 · MICRO_UPGRADE — reconcile a disputed count by finding the convention, not by choosing a side

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (mirror, this session) · `CLASS: MICRO_UPGRADE` ·
`SCOPE: LOCAL → offered for wider scope` · `STATUS: proposed`

Plan published *"51 of 51 top-level definitions identical by `ast.dump`"*. I measured **32**. Two
actors, one file, two integers.

The reflex is to call it a false number — `P-10` was exactly that, one revision earlier, and I had
just been rewarded for it. Instead I enumerated the conventions: top-level `FunctionDef`/`ClassDef`
= 32; including nested = 33; including module-level assignments = 39; **all top-level statements =
51**. The claim reproduces exactly, under a convention Plan did not name. The defect is the noun
*definitions*, not the measurement — and the substantive claim (nothing added, removed or changed)
is true on all four conventions, which is a stronger result than agreeing on one.

My own memory of this laboratory says *two counts that agree verify nothing if you compared the
number and never the set underneath*. This is its converse and it is the more useful half:

> **The rule I am proposing:** *when two independently authored instruments disagree on a count over
> the same object, enumerate the plausible conventions before adjudicating. A disagreement resolved
> by convention is a vocabulary defect and gets a P-class finding; a disagreement that survives
> every convention is a false number. Deciding which without enumerating is how a correct claim gets
> recorded as a false one.*

Recorded because I nearly filed `P-13` as a false measurement, which would have been wrong, and
would have been wrong in the direction my last review's success biased me toward.

---

## 4 · BEST_PRACTICE_CONFIRMATION — the payload-controlled diff

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (mirror, this session) · `CLASS:
BEST_PRACTICE_CONFIRMATION` · `SCOPE: LOCAL` · `STATUS: proposed`

The two hostile `verify` runs differed between revisions in exactly two lines: the tree digests.
The manifest explains why — the planted payload *is* the edited protocol text, so the digests must
move. The explanation is correct and I could have accepted it.

I did not accept it; I removed it. I re-ran the pair with **identical bytes** planted at both
revisions, and the outputs became byte-identical including the digests. That converts an
explanation into a measurement, and it costs one rebuild.

The generalisable shape: *when a comparison has a residual and the author supplies a reason for it,
construct the run in which the reason cannot apply.* An explained difference and an unexplained one
read identically in a diff.

---

## 5 · CURATION under Annex E.2 — over `SLR-plan-0006`

Recorded in `REV-SCIAB-MIRROR-006` §10.2 and summarized here because E.2 curation is Mirror's
standing obligation, not a section of one review.

```
L-1  proposed REPLICATION            → SPLIT.  L-1a the defect instance = EXPOSURE_AFTER_BROADCAST
                                                    (origin mirror, -005 §4C)
                                               L-1b "a fail-closed choice is the kind most likely
                                                    to be written up as an entailment" =
                                                    ORIGINAL_OBSERVATION (plan) — the mechanism is
                                                    not in my review. Meets E.2's second threshold
                                                    (1 + Mirror validation) → BEST_PRACTICE_CANDIDATE
L-2  proposed ORIGINAL_OBSERVATION   → SPLIT.  the observed gap is -005 §4B = REPLICATION;
                                               the DETECTOR ("premises about what can be claimed,
                                               conclusion about what the machine does") is
                                               ORIGINAL_OBSERVATION and is the durable half
L-3  proposed ORIGINAL_OBSERVATION   → REPLICATION of SLR-plan-0004 L-1, by the record's own text,
                                               with SCOPE widened from a code population to a
                                               normative-claim population. That widening is the
                                               second confirmation SLR-plan-0004 L-1 needed →
                                               SLR-plan-0004 L-1 crosses E.2's ≥2 threshold
boundary section                     → RATIFIED AS WRITTEN. The target-list defect is correctly
                                               filed REPLICATION of SLR-plan-0005 L-3 on a new form
```

**None of this ratifies Mirror methodology (G.2).** E.2 curation of another actor's record is
Mirror's under H.1; nothing above touches my rubric, clustering, active-learning selection,
review-yield or autonomy method, and none of it is self-approved.

**What I learned from doing the curation, and it is uncomfortable.** Plan's three proposed classes
were each generous to me and each wrong in my favour: L-1 credited my review with a generalisation
it does not contain, L-2 credited Plan with an observation that is mine, and L-3 credited Plan with
an original that is Plan's own replication. Two of the three corrections *reduce* what is attributed
to me. An actor classifying its own learning is the shape E.2 exists to prevent; a curator ratifying
classes that flatter the curator is the shape E.2 does **not** yet have an instrument for, and I
have no proposal for one beyond naming it here.

---

## 6 · What this session did not do

No `HUMAN_APPROVAL` granted, recommended or implied — ACCEPT is a review verdict under H.1 and the
MAJOR approval is the operator's, unspent. Nothing canonicalized, no benchmark executed, no actor
registered, no capability verified, `main` untouched at `cbce3016`, no lease taken. The candidate
branch was not written; `scientist-ab-spec` was read from git objects only. No other actor's
worktree was written. The session-routing debt is untouched, no `SESSION_REF` was declared or
inferred, and this session supersedes no other Mirror session.

`R-10` — branch `mirror` carrying `plan_defined_parameters.md` at P5 v3 while `BASE_HEAD` carries
v4 — is **still my own debt, still unrepaired, and it moved numbers for the sixth review running**.
Six is no longer a workaround; it is a practice. It is the obvious first move of my next session and
I am recording that so the next session inherits it rather than rediscovers it.

`N-7` is unreconciled for the fifth review running. I did not re-run revision 1's tool and I make no
claim about it beyond §12 of the review, which establishes that nothing the candidate currently
claims depends on it.

## 7 · Boundary of this record

No `LEARNING_INDEX` file exists (Annex E.2 names the instrument; Plan owns its durability), so §15's
dedup step was performed by reading the record corpus at source — `SLR-mirror-0010` … `-0013`,
`SLR-plan-0004`, `-0005`, `-0006`. Every `CONFIRMATION_CLASS` above is **proposed**: I am classifying
my own learning here, which is exactly the shape I just corrected in Plan's record, and the honest
disposition is that §1–§4 need an independent reviewer under G.2 before any of them counts as more
than `LOCAL`. The event ledger (J.1/P7) still has no writer, so none of this is derived from ledger
data and the autonomy-ledger and review-yield metrics remain uncomputed.

## 8 · Persistence

`WORK_COMMIT` on branch `mirror`, under `learning/mirror/` (E.6, A.7), together with
`reviews/mirror/REV-SCIAB-MIRROR-006.md` and `ledger/checkpoints/mirror/CHK-mirror-0008.json`.
Branch `mirror` is not the candidate branch and carries no candidate content, so this record moves
no candidate hash — the asymmetry with Plan's records that `REV-SCIAB-MIRROR-003` `P-2` established
and that `SLR-plan-0006` correctly does not re-argue.
