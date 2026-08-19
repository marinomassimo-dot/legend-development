---
artifact: SESSION LEARNING RECORD (Annex E.6)
record_id: SLR-plan-0005
actor_id: plan
role: Plan
date: 2026-08-19
task: SCIENTIST-AB-SPEC-001 · directive v1 · generation 5 — targeted remediation of
  REV-SCIAB-MIRROR-004 (M-4) on CAND-20260818-SCIENTIST-AB-SPEC
scope: this candidate's revision 5, the two `verify` modes, and the claims printed under both
curation: PENDING — E.2 gives epistemic curation to Mirror. Every class below is **proposed**,
  not self-certified. L-1 is offered as a REPLICATION of `SLR-mirror-0012` §1, which named the
  pattern from the reviewer's side before this session began and which I read at source.
derived_from: [SLR-plan-0003, SLR-plan-0004, SLR-mirror-0011, SLR-mirror-0012]
---

# SLR-plan-0005 — a guarantee is a property of a run, and I had been writing it as a property of a predicate

## Context

One blocking finding. `REV-SCIAB-MIRROR-004` confirmed `M-3` closed in `--post-read` — the census
complete, non-circular, independently oracled — and found that the two sentences written to
describe that closure are printed unchanged by `verify` **without** `--post-read`, where no census
runs at all. That is the command §5 step 1 runs and §1's `P-7` names: the run that gates handover.
On a clean build, 32 present files, 16 per surface, before any reader exists.

I reproduced it before editing anything. The counts came out exactly as reported — `PRESENT 48 ·
SCANNED 16 · CENSUSED 0 · SILENT 32` — and so did the sharpest case: the whole of
`controlled_benchmark_ab.md`, UTF-16LE+BOM, written identically into both surfaces at an
allowlisted `.md`, gave `VERDICT: PASS` with the path named **zero** times.

---

## L-1 · FAILURE_PATTERN — I fixed the predicate and reasoned as if that fixed the report

`CONFIRMATION_CLASS: REPLICATION` of `SLR-mirror-0012` §1 (mirror, prior session; read at source
on branch `mirror` before this remediation began) · `CLASS: FAILURE_PATTERN` ·
`SCOPE: LOCAL → offered for wider scope` · `STATUS: proposed`

`SLR-plan-0004` L-1 said *a finding is a lower bound on its own population*, and I applied it: I
derived the census from `scan_skip_reason()` rather than from the finding, found the fourth skip
condition nobody had named, got all six classes, and bound the scan and the census to **one call**
so that no second implementation could drift.

Every one of those was right, and the argument I built on it was wrong. Here is the sentence I
wrote into the code at revision 4:

> *"Skipping a file silently is no longer expressible: the same predicate decides the skip and the
> printing."*

A shared predicate makes the two populations agree **wherever both are computed**. It says nothing
about whether the printing site is reached. Mine sat behind `if args.post_read:`, and the sentence
that depended on it was printed on both sides of that conditional.

```
M-2   scoped to one spec key         → the exemption lived in two
M-3   scoped to one skip condition   → the predicate had four
M-4   scoped to one CLI flag         → the sentence is printed under two
```

The recurrences are not the same mistake three times. `M-2` and `M-3` were both **population**
errors, and `SLR-plan-0004` L-1 is a rule about populations. `M-4` is a **mode** error, and the
rule I had just written does not reach it. That is why holding the rule did not help: I was
enumerating the inputs that reach the defect and never the invocations that reach the claim.

**The generalisation I am proposing.** *A guarantee is a property of a run, not of a predicate.
Before believing a remediation, enumerate every code path that PRINTS the claim and measure each
one; a predicate shared between two computations removes drift between them and establishes
nothing about a reporting site behind a conditional.*

**What I did about it, in the code rather than in this record.** The census is now unconditional
and `post_read` is a parameter of what it *means*, never of whether it *runs*; the parameter has
**no default**, so no future call site can acquire the post-read universe by omission — which is
exactly how the existing one acquired it. And the tool prints a `MODE` line on every run, so the
mode is a fact a reviewer reads rather than one they reconstruct from which block is missing.

---

## L-2 · MICRO_UPGRADE — the two modes were one contract in my head and two in the code

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (plan, this session) · `CLASS: MICRO_UPGRADE` ·
`SCOPE: LOCAL` · `STATUS: proposed`

Asked to make the printed claim true, the cheap move is to scope the sentence to `--post-read` and
carry the pre-handover skip population as a named residual. Mirror offered that route explicitly.
I did not take it, and the reason is worth recording because it is the reason the remedy is
larger than the finding.

Scoping the sentence would have required weakening the pre-handover row of the guarantee table,
whose `GUARANTEE_PROVIDED` reads *"no identifier leak — all of it observed, not attested"*. That
row is the epistemic content of the handover gate. Weakening it, while the mechanism to satisfy it
already existed and was already correct, would have been the permissive choice dressed as
precision.

Writing the two contracts out separately — §4.4, one row per property — did something I did not
expect. It made a question answerable that I had been about to answer by analogy: whether
`EXPECTED_BY_PROTOCOL: NO` blocks. Mirror ruled it **informational** post-read, from the normative
text, and that ruling is right. Transferring it to the gate would have been reasoning from the
wrong end of the transfer. §2.2 already says Plan is the surface's only writer **until handover**;
`build` copies and does no templating; so pre-handover an allowlisted text-suffixed file that is
not text is a state `build` cannot produce, and §3's remedy for it is already written — *rebuilt
from the spec, never patched*. Post-read the writer is the reader, who may legitimately emit
UTF-16, and what the protocol claims there is enumeration.

**The rule I am proposing:** *when one mechanism runs at two points of a transfer of authorship,
write its contract once per point before deciding anything about either. The asymmetry, if there
is one, is usually already stated somewhere as a fact about who the writer is — and inherited from
the other point it looks like a design decision when it is an unexamined transfer.*

---

## L-3 · MICRO_UPGRADE — my own harness produced three wrong numbers, and each was caught by a control I nearly left out

`CONFIRMATION_CLASS: REPLICATION` of `SLR-mirror-0010` §4 / `SLR-mirror-0011` §3 / `SLR-mirror-0012`
§2 · `CLASS: MICRO_UPGRADE` · `SCOPE: LOCAL` · `STATUS: proposed`

Three times this session, an instrument of mine reported a clean, plausible, wrong result.

1. **The hostile UTF-16 rows failed against my own fixed tool**, and I was briefly ready to call
   it a defect in the fix. It was the payload: I had put an em dash in it to make it non-ASCII.
   `—` is `U+2014`, and UTF-16LE encodes it `14 20` — both bytes below `0x80`, so the file decodes
   as valid UTF-8 and is *genuinely scanned*. The tool was right and my test was wrong. See L-4.
2. **The regression harness reported 421 of ~850 tests**, because it invoked
   `python3 -m unittest <dotted-module>` and twelve targets have hyphens or dots in their paths and
   cannot be named that way. It also matched unittest's single-line verbose form only, so every
   test with a **docstring** — which here is most of them — was dropped. `ADDED: 0` over a
   population that size is a number about my parser.
3. **It then reported five failing tests where Mirror measured seven.** The two it missed are
   `subTest` failures, which print a `FAIL:` header while the top-level line still ends `... ok`.
   The authoritative signal that a test failed is the header, not the outcome line. Corrected, my
   independent count reconciles with Mirror's exactly: 7 at both tips, same reason, 7/7.

Each was caught by a control I could have omitted and would still have had a green-looking run:
the positive control that must fail, the count reconciliation against another actor's independent
measurement, and the explicit omission channel. **The rule is not new — Mirror has paid for it
five times — and this is the first session in which I paid for it, three times, in one sitting.**
What I add is where it bit: not one of the three was an exit-code battery. All three were
assertions on *content*, and each read exactly like a correct negative.

---

## L-4 · FAILURE_PATTERN — a review's conclusion can be right while the test it states for it is not

`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` (plan, this session) · `CLASS: FAILURE_PATTERN` ·
`SCOPE: LOCAL` · `STATUS: proposed`

`REV-SCIAB-MIRROR-004` §8 records `P-7`: a **pure-ASCII** payload in BOM-less UTF-16 decodes as
UTF-8, so the file is really scanned and the census is right to omit it. Correct. It bounds the
residual with: *"It disappears the moment the payload contains one non-ASCII character, which the
real forbidden artifacts all do."*

**That criterion is too loose, and I measured it while trying to use it.** UTF-16LE encodes
`—` U+2014 as `14 20`, `–` U+2013 as `13 20`, and `‘ ’ “ ”` U+2018–201D as `18 20 … 1D 20` — every
byte below `0x80`. Those are non-ASCII characters, they are most of what makes ordinary prose
non-ASCII, and BOM-less UTF-16 text made only of them still decodes and is still scanned. The
condition is about a **byte**, not a character: the payload needs a code point one of whose UTF-16
bytes lands where UTF-8 cannot read it — `§` U+00A7 → `A7 00`, an accented Latin letter, an emoji —
or a BOM, which is `FF FE` and invalid UTF-8 by itself.

Mirror's **conclusion** survives its test: the real artifacts do carry `§` and `🔴`, so `P-7` stays
narrow and is a scan limit rather than a census hole. I am not reclassifying it and it did not
change this verdict. But the sentence a later reader would reach for as the falsifier is one that
fails, and it is now pinned as an executable test with all three rows —
`test_bomless_utf16_decodes_as_utf8_unless_a_byte_exceeds_7f` — rather than left in prose.

**The generalisation:** *a residual recorded with a stated boundary has two claims in it, and the
boundary is the one nobody re-derives. Executing it costs one test and is the only thing that
distinguishes a bounded residual from a bound that was never measured.*

---

## What this session did not do

The remedy touched **two functions**: `cmd_verify` and `unchecked_surface`. Verified by AST
segment: 37 of 39 top-level definitions are byte-identical to revision 4, and `scan_skip_reason`,
`SCAN_SKIP_CLASSES`, `iter_files`, `_is_expected_output`, `_is_decodable_text`, `cmd_build`,
`cmd_freeze`, `cmd_verify_freeze`, `_classify`, `cmd_population`, `cmd_locators`, `tree_digest`,
`_pdf_pages` and `_regex_units` are among them. **The predicate that decides the skip did not
move.** `M-3`'s closure rests on that predicate, and the pre-handover census is the same call
answering the same question about a smaller universe — three of six classes are reachable before
handover, because the other three exist only once reader outputs do.

`M-1`, `M-2` and the freeze battery were retested and not redesigned. Freeze cannot have
interacted with the change: its three functions are byte-identical and none of them calls either
changed function, verified by AST rather than by reading.

## Boundary of this record

The delta harness is **still not committed** — `SLR-plan-0003` L-4 declared that limitation,
revision 4 did not repair it and neither does this one; the numbers in §16 of the manifest remain
reproducible only by re-authoring an equivalent instrument, which is what I did and what Mirror
did. Three regression targets are custom harnesses rather than unittest and yield no test-id
granularity to my parser; they are recorded as the omission channel, identical and `rc=0` at both
tips, rather than counted as passes. `N-7` is unreconciled for the fourth review running and I did
not settle it; I did not re-run revision 1's tool. `P-1`, `P-4`, `P-5` and `P-6` are carried, not
closed — `P-6`'s *printed-claim* half is addressed, in that the partition sentence now says its
`present` excludes `.git/`, but `iter_files` is byte-identical and the exclusion itself stands.
`P-7` is carried with its boundary corrected, not resolved. No `LEARNING_INDEX` exists to dedup
against; the debt is Plan's, it is unchanged, and dedup was again done by reading five records at
source. No `SESSION_REF` was declared or inferred, and the session-routing debt is untouched.
Nothing under `main`, the root checkout or another actor's worktree was written;
`reviews/mirror/REV-SCIAB-MIRROR-004.md`, `learning/mirror/SLR-mirror-0012.md` and
`CHK-mirror-0006` were read from git objects on branch `mirror` without merging it. The session
guard refused two inline heredocs that would have written files while the shell was inside a
repository worktree; I did not reach for an unchecked tool — both probes were authored with
`Write` into the scratchpad and invoked by name, and the measurements are the same ones.

## Persistence

`WORK_COMMIT` on branch `scientist-ab-spec`, under `learning/plan/` (E.6, A.7). `learning/` is
CONTENT by intent (P5.1), so this record is inside the population Mirror reviews and moves the
candidate hash. It is committed **before** any revision-5 binding is declared, so nothing is
superseded within the revision — the correction `SLR-plan-0003` L-5 asked for, held for a second
consecutive revision.
