---
artifact: MIRROR hostile review, revision 4 (Annex C.2)
review_id: REV-SCIAB-MIRROR-004
object: CAND-20260818-SCIENTIST-AB-SPEC rev 4 · CANDIDATE_CONTENT_HASH 07b65b37…5198 @ base cbce3016
level: R4 (MIRROR_REQUIRED — role contract in CORE, two new protocols, MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here
date: 2026-08-19
supersedes: nothing. REV-SCIAB-MIRROR-001, -002 and -003 stand as the reviews of revisions 1, 2
  and 3 and are not amended.
verdict: REQUEST CHANGES — M-3 is genuinely closed in `--post-read`, and the sentence written to
  describe the closure is printed unchanged by the pre-handover run, where no census exists at
  all (M-4). One new blocking finding, two recorded, nine carried re-classified.
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the candidate tip
---

# The census is complete, non-circular and independently oracled. It is printed in one of the two modes, and the sentence is printed in both.

Reviewed from `R-1`. **VERDICT TRANSFER: NONE.** Nothing carries over from
`REV-SCIAB-MIRROR-001`, `-002` or `-003` — not a verdict, not a `PASS`, not `M-1`'s closure, not
one of the twenty-odd rows revision 3 was found to have got right. Every number below was
re-derived in detached scratch worktrees of `BASE_HEAD` and of the candidate content tip, never
in another actor's worktree and never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror       branch mirror · HEAD 015574a1 · clean
ACTOR_ID          mirror · roles/mirror.md read in full · PERSISTENT_LEGEND_ACTOR · worktree mirror
                  (deployment/deployment_profile.md maps actor `mirror` → worktree `mirror` →
                  roles/mirror.md; read at BASE_HEAD, not from this branch)
governance        3.1.1 · Annex C (C.1 ladder, C.2 format, C.3 discipline, C.4 objects),
                  Annex D (D.1–D.5), Annex E (E.1, E.2 curation, E.6 record schema),
                  Annex G (G.1 perimeter, G.2 self-upgrade bar, G.3 metrics), Annex H.1,
                  body §12 / §15 / §36.5, P5 — all read at BASE_HEAD
                  roles/mirror.md and Annexes C, D, E, G verified BYTE-IDENTICAL to main
fingerprint       compose --role mirror at BASE_HEAD cbce3016
                  3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                  at content tip a210f73  3dff8954…f65c — IDENTICAL
STABLE ACTOR IDENTITY    mirror · worktree mirror · roles/mirror.md · reconstructed from durable
                  repository evidence alone; no part of it depended on a prior conversation
CURRENT SESSION ROUTING  not durable in the repository. No SESSION_REF is declared for this
                  session and none is invented or inherited. An actor cannot observe its own
                  routing reference.
Agent Card        runtime/agent_card_registry.md is not on main and not on this branch; mirror's
                  four declared capabilities are UNVERIFIED per contract, and L2 is suspended
mission           governance layer (MAJOR when in doubt, fail-closed, body §12) · hostile review
                  layer (Annex C.2 format, STEELMAN before objections, declared falsifier;
                  CONFIRMED ≠ true) · metacognitive layer (learning clustering, E.2 curation,
                  dissent lifecycle, review yield, autonomy ledger)
review authority  review of SYSTEM objects (C.4) at R4; no command over any actor; no primary
                  evidence; may NOT grant HUMAN_APPROVAL (H.1: operator); may NOT
                  CANONICAL_BATCH_COMMIT (H.1: orchestrator); may NOT self-approve changes to
                  its own rubric, clustering, active-learning selection, review-yield or
                  autonomy methodology (G.2)
permitted writes  branch mirror only, under reviews/ · ledger/ · learning/
forbidden writes  main, root, any other actor's worktree, any *_current.md, any registry, the
                  receipt ledger, the candidate branch
proposer ≠ reviewer ≠ executor   author plan · reviewer mirror · adjudicator operator — holds
G.2               NOT ENGAGED: nothing in the candidate touches Mirror's rubric, clustering,
                  active-learning selection, review-yield or autonomy methodology
```

**MIRROR REHYDRATION: PASS.**

> **Worktree debt, disclosed because it moves numbers.** Branch `mirror` carries
> `governance/plan_defined_parameters.md` at **P5 v3** and `candidate_content_hash.py` in its
> pre-fix form. Every binding number in §1 was computed in a clean detached worktree of
> `BASE_HEAD`, which carries P5 v4 and the canonical script, or by an implementation I wrote in
> the scratchpad from the normative text. This is `R-10` of revision 1 — still Mirror's own debt,
> still not the candidate's, still not fixed.

> **A checkpoint is missing and it is mine.** `ledger/checkpoints/mirror/` ends at
> `CHK-mirror-0005` (revision 2). The revision-3 session wrote `REV-SCIAB-MIRROR-003` and
> `SLR-mirror-0011` and no checkpoint. A.6 asks for one; this session writes `CHK-mirror-0006`
> and records the gap rather than renumbering over it.

---

## 1 · Binding — PASS

```
base cbce3016 · tip a210f738 (CONTENT TIP)          07b65b3707a4e63df23918b844140e7548929b27a8a182f8ebf2d9b0ab165198
  governed script, run 1 · run 2 · run 3            07b65b37…5198  ×3
  at 0ec863b3 (MANIFEST TIP)                        07b65b37…5198   — invariant, measured
INDEPENDENT recomputation, my own implementation of P5.1/P5.2 written from the normative text
(git ls-tree -r --full-tree, three declared roots removed, PATH-sorted, v4 prefix, every entry
newline-terminated, no shell in the path of the listing)
  at a210f738   07b65b37…5198   included 525 · excluded 30
  at 0ec863b3   07b65b37…5198   included 525 · excluded 31   (+CHK-plan-0013, control plane)
  at b1061ebb   1613fa3b…9332   included 524 · excluded 30   — the mid-revision commit
POSITIVE CONTROLS — the four PUBLISHED values of earlier tips, same route
  at a3cad1d  (revision 3)               570fcbbb…8ab7    524 · 29   ✓ reproduces
  at b634829  (superseded rev-3 tip)     7cef4ccc…4596    523 · 28   ✓ reproduces
  at daaa3335 (revision 2)               c0701094…21bcf   523 · 27   ✓ reproduces
  at b965ca58 (revision 1)               3b568aae…916c75  522 · 24   ✓ reproduces
THE TRAP, exercised deliberately: sorting the whole ls-tree LINE instead of the path
  at a210f738   63ce2525…e3ce   — a different value, because 100644 sorts before 100755 and
                                 this candidate creates two executable files
main   cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED, merge-base of the branch
```

Four runs of the governed script and seven independent recomputations without it, of which four
are historical controls. **An implementation that agreed only with itself would prove nothing**;
mine reproduces every published value, and I ran the line-sorted variant to confirm the hazard
Plan reports is real in this tree rather than taking its word for it.

**The single content-domain entry separating `07b65b37…` from `1613fa3b…`**, derived from the
tree: `learning/plan/SLR-plan-0004.md`, added. 524 → 525. The manifest's claim is exact.

**BINDING: PASS.**

### 1b · Superseded bindings — CORRECTLY CLASSIFIED

Every occurrence of every superseded value in the authoritative manifest was read with its line.
`570fcbbb…` at lines 5, 44, 120, 185, 1141; `7cef4ccc…` at 47, 121, 185, 1143; `c0701094…` at 6,
49, 122, 1142; `3b568aae…` at 7, 51, 123. Each is a `supersedes:` clause, a `SUPERSEDED_*` field,
a labelled positive-control row, or a sentence naming it as superseded. **No third place presents
any of them as current.** `1613fa3b…` is declared *not* a binding, at line 133, and it never was
one — which is the correction `SLR-plan-0003` L-5 owed and revision 4 pays.

---

## 2 · STEELMAN (before the objections)

**Revision 4 does the structural repair when two arithmetical ones were available and either
would have closed the finding I wrote.**

`REV-SCIAB-MIRROR-003` named two remedies: add the two missing populations to
`unchecked_surface()`, or restore revision 2's weaker wording. Plan rejected both and says why:
either one leaves the census and the scan as *two statements of the same rule*, agreeing until
one is edited — which is exactly how `M-2`'s remedy produced `M-3`. The repair is
`scan_skip_reason()`, one predicate called by the scan loop and by the census, so
`actual unscanned == declared unscanned` stops being a property somebody maintains. I verified
this structurally: 34 top-level definitions byte-identical to revision 3, **exactly two changed**
(`cmd_verify`, `unchecked_surface`), three added (`scan_skip_reason` and two constants). The
manifest's function-level claim is exact, and it is the kind of claim a reviewer can check.

**The reproduction was larger than my report and Plan says so in the record.** I wrote ten
silent files per surface. Ten is the decodable subset — the population my false-sentence argument
was about. The true silent population at revision 3 is **sixteen per surface**, and I confirmed
it: 24 present, 8 scanned, 16 skipped, 0 named. Plan derived that from the predicate rather than
from my number, found a class no review had ever named — an allowlisted `.md` re-encoded UTF-16,
carrying the whole forbidden protocol text, `PASS` and invisible — and wrote *the finding is a
lower bound* as the session's learning. That is the correct relationship between a review and a
remediation, and it is rarer than it should be.

**The test oracles were rebuilt rather than patched.** The test that encoded the defect is gone.
In its place: a hand-written literal enumerated path by path from what the fixture puts on disk,
and a behavioural probe that plants the paper's identifier in each present file and measures
scanning **by its consequence** — with an anti-vacuity guard requiring the scanned set to be
non-empty. That is the design I built independently before reading theirs, down to the instrument
check, and my first run of my own version failed it. Twelve of the seventy-one tests fail against
revision 3's tool, including the honest-reading positive control, which is the differential that
turns a green suite into evidence.

I ran the falsifier the protocol hands me. In `--post-read` it holds, against every construction
I could build. Then I ran the other mode.

---

## 3 · Population reviewed and tests executed

**Read in full:** the authoritative candidate manifest at `0ec863b3` (1 225 lines), the rev3→rev4
diffs of all five changed content files, `benchmark_input_surface.py` at revision 4,
`test_benchmark_input_surface.py`, `surface_spec.json`, `controlled_benchmark_ab.md` §3–§4.5 and
the guarantee table, `learning/plan/SLR-plan-0004.md`, `reviews/mirror/REV-SCIAB-MIRROR-003.md`
and `learning/mirror/SLR-mirror-0011.md`; at source: `roles/mirror.md`, Annexes C, D, E, G, H,
body §12/§15/§36.5, P5, `deployment/deployment_profile.md`,
`scripts/test_locator_obligation_reaches_every_route.py`, `scripts/run_release_regressions.py`.

**Executed** — detached scratch worktrees: `wt-base` = `cbce3016`, `wt-rev4` = `a210f738`,
`wt-rev4m` = `0ec863b3`, `wt-rev3` = `a3cad1d`, `wt-rev4mid` = `b1061ebb`, `wt-diff` = `a3cad1d`
with revision 4's test file, `wt-surf4` / `wt-surf3` for surface construction. Neither regression
worktree holds `files/`. The packet was copied read-only from root into the two surface
worktrees only; all attack surfaces are copies under the session scratchpad.

```
binding                    4 governed runs + 7 independent recomputations + 1 trap  PASS
content population         21 files · +6125 / −1 · derived from git, not from the report
rev4 delta                 5 content files (4 modified + 1 added); 16 byte-identical to rev3
function-level delta       34 identical · 2 changed · 3 added · 0 removed
INDEPENDENT FILE UNIVERSE  os.walk + behavioural scan probe, both modes                see §6
census, clean build        rev3 printed 0 while 16/surface were skipped   M-3 REPRODUCED
                           rev4 prints 32 (16/surface)                    M-3 CLOSED post-read
same bytes, six paths      both modes, two caught / four by location      see §5, §6
encoding matrix            13 rows, UTF-16 LE/BE ±BOM, CP1252, latin-1, ASCII-in-UTF-16  §8
candidate suite @ rev4     71 tests, 71 green, registered in the battery
differential vs rev 3      12 of 71 fail against revision 3's tool        discriminates
freeze / verify-freeze     16 cases, each on its reason, positive controls first      16/16
input parity               5 negatives each on the reason + positive control          5/5
release regressions        64 targets @ base · 65 @ rev4, my own harness, per test    §15
population (B-1)           re-derived ×2, byte-identical to each other AND to the
                           tracked evidence_units.json (b41c7b9f…) · 65 units · 109 panels
N-2 reproduction           File011 declared empty → 65 → 58, rc=0, silent   REPRODUCED
publication gate           PASS / BLOCKS 0 at the content tip
legend_lint PASS (1 pre-existing INFO) · growth_anchors PASS — claims=39 · papers=70 ·
                           corpus=356 · literature=390
fingerprints               scientist 355e3529… → 82423a48… · plan, mirror, orchestrator IDENTICAL
```

---

## 4 · M-3 — CLOSED in `--post-read`, and the closure is not circular

### 4A · The defect, reproduced at revision 3 before anything was believed

Built both surfaces from `a3cad1d` and ran the census on a clean tree:

```
rev 3 · verify --post-read · clean build
  [UNCHECKED SURFACE] 0 present file(s), each named above. That is the whole of it…
  measured, same tree:  24 present per surface · 8 scanned · 16 skipped · 0 named
```

**Sixteen silent per surface, not ten.** Ten is the decodable subset my own review reported;
the six packet PDFs are skipped by the suffix test and were also named by nothing. Plan's
correction of my number is right, and the difference is the point: my number was scoped to the
sentence I was falsifying, and the population is scoped to the code.

### 4B · The skip conditions, derived from executable control flow

Read off `scan_skip_reason()` top to bottom, in the order the scan loop takes them — not from
`SCAN_SKIP_CLASSES`, and not from any document:

```
1  post_read and _is_expected_output(rel, spec, path)      → blind_spot            (rel ∈ blind)
                                                           → scan_exempt_present   (rel ∈ exact)
                                                           → undecodable_prefix    (otherwise)
2  rel ∈ content_scan.exempt_surface_paths                 → scan_exempt_input
3  not rel.endswith(content_scan.text_suffixes)            → suffix_not_scanned
4  not _is_decodable_text(path)                            → undecodable_text
   otherwise                                               → None, the scan reads it
```

**Four conditions, six classes**, and the set is exactly `SCAN_SKIP_CLASSES`. Order is
load-bearing and correct: `benchmark/OUTPUT_SCHEMA.md` full of UTF-16 reports `scan_exempt_input`
and not `undecodable_text`, because the exempt test returns first — the class is the reason the
scan **actually** stopped, not the first reason that would also have applied. I verified that
case at runtime.

### 4C · The census is not circular, because it is not a second implementation

The concern the directive raises — one predicate, two consumers, both agreeing with the same
wrong rule — is real and is why §6 does not compare the two callers. It is also structurally
guarded here: `test_the_scan_and_the_census_call_the_same_predicate` asserts both call sites go
through `scan_skip_reason`, and `test_every_class_the_predicate_can_return_has_an_explanation`
parses the predicate's own source and requires `SCAN_SKIP_CLASSES` to have an entry for every
value it can return, so a fifth condition is a loud failure rather than a file that quietly stops
being printed.

**M-3 (as reported): PASS in `--post-read`.**

---

## 5 · M-4 (BLOCKING) — the pre-handover run prints the census sentence and produces no census

`unchecked_surface()` gained a `post_read` parameter at revision 4. Its only call site is inside
`if args.post_read:`, so the parameter **can never be False from the CLI**. The mechanism to
enumerate the pre-handover unchecked surface exists, is passed the right argument, and is
unreachable.

The two sentences `cmd_verify` prints on **every** `PASS`, in both modes:

> *"…every present file was either **scanned** for the paper's identifiers or **printed above
> under `[UNCHECKED]`** with the reason it was not, and nothing scanned leaked an identifier."*

> *"**`SCANNED` and `[UNCHECKED]` partition the present files** — one predicate decides both, so
> **no present file is skipped by the identifier scan without appearing in that list**, and none
> appears in it that was scanned."*

**Measured on a clean build, `verify` without `--post-read` — the run that gates handover:**

```
[UNCHECKED] lines printed                            0
present regular files (os.walk, both surfaces)      48
scanned  (behavioural probe, instrument check ✓)    16
censused                                             0
SILENT                                              32      ← 16 per surface
```

### 5A · The same bytes, six paths, both modes

The whole of `controlled_benchmark_ab.md` — a declared `forbidden_prior_output_path` naming the
paper — appended identically to both surfaces, so parity cannot see it:

```
                                                 PRE-HANDOVER          --post-read
CLAUDE.md                (scan_exempt_input)     PASS · not named      PASS · NAMED scan_exempt_input
benchmark/MODE_DIRECTIVE.md (scan_exempt_input)  PASS · not named      PASS · NAMED scan_exempt_input
files/…/File011.pdf      (suffix_not_scanned)    PASS · not named      PASS · NAMED suffix_not_scanned
output/renders/.gitkeep  (suffix_not_scanned)    PASS · not named      PASS · NAMED suffix_not_scanned
roles/scientist.md       CONTROL, scanned        FAIL · IDENTIFIER LEAK          FAIL · IDENTIFIER LEAK
output/renders/smuggled.md CONTROL, not allowed  FAIL · NOT ALLOWLISTED + LEAK   FAIL · same
```

The controls fail in both modes, so the difference is the **location and the mode**, not the
payload and not the invocation.

### 5B · The sharpest form: the whole forbidden text, at handover, unnamed

`framework/eval/failure_taxonomy.md` — allowlisted, `.md`, normally scanned — overwritten in
**both** surfaces with the UTF-16LE+BOM encoding of the entire protocol text (46 709 characters):

```
PRE-HANDOVER verify   VERDICT: PASS   rc=0   mentions of the path anywhere in the output: 0
                      …and both sentences above printed verbatim
same tree --post-read [UNCHECKED] ×2  undecodable_text  EXPECTED_BY_PROTOCOL NO
                      [UNCHECKED SURFACE] 2 of them are NOT a consequence the protocol declares
```

### 5C · Four artifacts assert the property, and the fourth is the learning record

1. the tool's `VERDICT: PASS` output, both sentences above, printed in **both** modes;
2. the tool's own inline comment at the scan loop: *"Skipping a file silently is no longer
   expressible: the same predicate decides the skip and the printing."*
3. `controlled_benchmark_ab.md` §4.5, bullet 2, in bold and **unscoped**: *"The command
   enumerates the unchecked surface from the tree, per actor, **on every run**, under
   `[UNCHECKED]`"* — and, four lines below, *"a file is named in the census exactly when the scan
   skipped it, because the same call decides both"*;
4. `SLR-plan-0004` L-2: *"The equality `actual unscanned == declared unscanned` stops being a
   property somebody maintains and becomes one that cannot be expressed otherwise."*

The **falsifier** sentence in §4.5 is correctly scoped (*"Falsify it with a file that
`verify --post-read` neither scans nor names"*), and the guarantee-table row for `verify
--post-read` is accurate. But bullet 2 says *on every run*, the tool prints the unscoped claim in
both modes, and the pre-handover row of the same table says *"no identifier leak — all of it
observed, not attested"* over 16 files per surface that were never opened.

### 5D · The candidate's own oracle finds it

`test_every_present_file_is_either_scanned_or_named_and_never_both` is the behavioural probe, and
its literal is named `FIXTURE_PRESENT_AT_HANDOVER` / `FIXTURE_CENSUS_AT_HANDOVER` — *handover*
being the pre-read state. Every assertion in it is made under `--post-read`. I changed that one
call and nothing else:

```
AssertionError: … SILENT: ['ASSIGNMENT.md', 'CLAUDE.md', 'benchmark/BENCHMARK_INSTRUCTIONS.md',
 'benchmark/MODE_DIRECTIVE.md', 'benchmark/OUTPUT_SCHEMA.md',
 'disease-models/wwox/research/deepdive_manifests/.gitkeep',
 'disease-models/wwox/research/fulltext_dossiers/.gitkeep', 'files/paper.txt',
 'output/.gitkeep', 'output/renders/.gitkeep']
```

The instrument that finds `M-4` is already in the suite. It is pointed at one of the two modes,
and the constant it asserts against is named for the other.

### 5E · Why this is blocking and not a note

1. It is a **false clause in the tool's own `PASS` output about census completeness** — the exact
   ground on which `M-2` was blocking at revision 2 and `M-3` at revision 3. `REV-SCIAB-MIRROR-002`
   rejected *"carry it as a debt"* because a false sentence in normative text about what an
   instrument guarantees is what a reviewer is told to trust instead of the author's account.
   That reasoning applies here unchanged, and applying a weaker standard a revision later would
   be the ratchet failing rather than the candidate improving.
2. The sentence is **new and strictly stronger at revision 4**. Revision 3 printed *"every file
   whose bytes this tool could decode was scanned"*; revision 4 replaced it with an explicit
   two-way partition and a reference to a printed list. Both are false pre-read; the new one is
   more specific about a thing that does not happen.
3. It is **inside `M-3`'s own remedy**, as `M-3` was inside `M-2`'s. Third iteration of one
   pattern on one seam, which is `SLR-mirror-0011` §1 and `SLR-plan-0004` L-1 stated from both
   sides — and neither record's rule was applied to the second mode.
4. Pre-handover `verify` is a **normative gate**: §3 lists `CONTENT_SCAN hits == 0` among the
   ex-ante checks, §4.3 *"Before:"* rests on it, and step 1 of §7's sequence is *build; `verify`*.
   It is the run that decides whether a surface may be handed over.
5. **The remedy is smaller than the finding.** The census block's guard is the whole of it; the
   parameter is already threaded and already correct. Whatever is chosen, the pre-read case
   belongs inside `test_every_present_file_is_either_scanned_or_named_and_never_both`, which is
   the negative control it lacks and the fourth instance of the candidate's own `L-1`.

**Steelman, stated because it is real and does not dissolve the finding.** At handover the
surface is a function of the allowlist and `build` has just written it, so the 16 skipped files
per surface came from a reviewed source root minutes earlier; the exposure is smaller than
post-read. Agreed — and identically true of `M-3`, whose exposure was bounded by the same
declared J.0 residual. **The finding is not the exposure. It is the census, and four artifacts
assert it is complete on every run.**

**M-4: FAIL. SILENT FILES, pre-handover: 32 (16 per surface), on a clean build, before any
reader exists.**

---

## 6 · Independent file-universe check — the partition, measured without the predicate

The universe is built with `os.walk`, never with `iter_files()`. Scan membership is decided
**behaviourally**: plant a marker matching `content_scan.pattern` in each present file in turn
and observe whether `verify` reports `IDENTIFIER LEAK` naming it. Census membership is parsed
from the printed `[UNCHECKED]` lines. Nothing in the harness calls `scan_skip_reason()`,
`unchecked_surface()`, or imports the module.

**Instrument check first, because a battery whose positive control fails is measuring its own
invocation.** My first run reported `SCANNED 0` — including for `roles/scientist.md`, which must
leak. The parser was indexing the wrong field. No negative in that run was evidence, and I say so
rather than report the count it produced.

```
                                       --post-read        PRE-HANDOVER
PRESENT regular files (os.walk)             48                  48
PRESENT symlinks                             0                   0
SCANNED  (observed by effect)               16                  16
CENSUSED as unscanned                       32                   0
SILENT   (neither)                           0                  32
IN BOTH  (overlap)                           0                   0
instrument check (roles/scientist.md)     PASSED              PASSED
```

**FILE-UNIVERSE PARTITION: PASS in `--post-read`, FAIL pre-handover.**

Symlinks are in neither population by construction, and cannot be silent: `iter_symlinks` reports
every one as a `SYMLINK` finding, which forces `rc=1`, and the partition sentence is printed only
on `PASS`. Verified.

`.git/**` **is** a third population, and it is not named. `iter_files` excludes it in both the
scan and the census, documented in its own docstring. I wrote 47 327 bytes of the forbidden
protocol text to `.git/info/notes.md` in a surface: `VERDICT: PASS`, census unchanged at 32,
`files 24` unchanged, the path named zero times, and `freeze` does not name it either. This is
**pre-existing** — `iter_files` is byte-identical to revisions 2 and 3 — documented in code and
absent from a built surface, so it is **recorded as `P-6`, non-blocking**. But the printed
partition sentence is scoped to `iter_files()`'s notion of *present*, and that scoping is nowhere
printed.

---

## 7 · Test oracles — INDEPENDENT

Both oracles were inspected for the form the directive rejects — `expected =
filter(actual, implementation_predicate)` — and neither has it.

| Oracle | What it is | Independent? |
|---|---|---|
| `FIXTURE_PRESENT_AT_HANDOVER` / `FIXTURE_SCANNED_AT_HANDOVER` / `FIXTURE_CENSUS_AT_HANDOVER` | 11 / 1 / 10 paths, hand-written from what `build_fixture` puts on disk, with the class per path | **YES.** A literal. It does not move when the skip logic moves, and `11 = 1 + 10` is asserted |
| `test_every_present_file_is_either_scanned_or_named_and_never_both` | plants `PMID 42397075` in each present file and reads the finding | **YES.** Scanning measured by consequence; contains no copy of the skip rule |
| `test_every_class_the_predicate_can_return_has_an_explanation` | regex over `scan_skip_reason`'s own source vs `SCAN_SKIP_CLASSES` | derived from the implementation **by design** — it is a consistency guard between two implementation artifacts, not the census oracle, and it does not claim otherwise |

**The behavioural oracle checks every property the directive asks for:** the identifier is
detectable (`IDENTIFIER LEAK` names the path); the scanned case detects it; the unscanned case
does not; the result is not CLI rejection, because the verdict and the census are parsed from a
successful run; and the classes are asserted, not just the counts. Its anti-vacuity guard —
`assertTrue(scanned, "positive control: the scan never fired…")` — is `SLR-mirror-0011` §3 applied
by the author to their own battery, and it is the property that caught my equivalent harness.

**TEST ORACLE: INDEPENDENT.** Its coverage is not: both oracles run `--post-read` only (26 of 33
`verify` calls in the suite; the 7 pre-read calls assert no census). That is §5D.

---

## 8 · UTF-16 / non-UTF-8 textual artifacts — PASS in `--post-read`

Target: `framework/eval/failure_taxonomy.md`, an allowlisted common `.md` the scan normally
reads. Written identically to both surfaces. Instrument checks first: untouched tree
`verify rc=0` and `freeze rc=0`; UTF-8 payload → `rc=1` with `IDENTIFIER LEAK`.

| payload | SCANNED | CENSUS | EXPECTED | VERDICT | NOT-DECLARED line | PARITY | FREEZE |
|---|---|---|---|---|---|---|---|
| clean UTF-8 (positive control) | YES | — | — | PASS | n | holds | input, unexpected 0 |
| UTF-8 + forbidden payload | YES | — | — | **FAIL** | n | holds | input |
| UTF-16LE + BOM | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| UTF-16LE no BOM | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| UTF-16BE + BOM | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| UTF-16BE no BOM | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| UTF-16 (Python default, BOM) | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| CP1252 | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| latin-1 | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input, unexpected 0 |
| ASCII-only payload, UTF-8 | YES | — | — | **FAIL** | n | holds | input |
| ASCII-only payload, UTF-16LE + BOM | no | `undecodable_text` | **NO** | PASS | **Y** | holds | input |
| **ASCII-only payload, UTF-16LE no BOM** | **YES** | — | — | PASS | n | holds | input |
| **ASCII-only payload, UTF-16BE no BOM** | **YES** | — | — | PASS | n | holds | input |

`undecodable_prefix` is reached instead when the same bytes sit under `output/renders/`, and
`freeze` then classifies the file `OUTPUT` — the declared cost of the byte-based prefix rule,
unchanged from revision 3.

**The partition holds in every row**, including the last two, and those two are worth stating
plainly. A **pure-ASCII** payload encoded UTF-16 without a BOM produces bytes that are all below
0x80, so `read_text(encoding="utf-8", errors="strict")` **succeeds**: the file is genuinely
scanned, the regex runs over a NUL-interleaved decoding, and no identifier matches. The tool's
claim — *"nothing scanned leaked an identifier"* — remains literally true, and the census is
right to leave the file out because the scan did read it. **This is a limit of the scan, not a
defect in the census**, the protocol claims enumeration rather than encoding-robust scanning, and
I record it as `P-7` rather than inflating it into a census finding. It disappears the moment the
payload contains one non-ASCII character, which the real forbidden artifacts all do.

**UTF16 HOSTILE CASE: PASS** — in `--post-read`. Pre-handover it is §5B, and that is `M-4`.

---

## 9 · `EXPECTED_BY_PROTOCOL: NO` — INFORMATIONAL, and correctly so

Answered from the normative text, not from intuition.

```
RUNTIME             VERDICT: PASS · rc=0 · the file is named with its class and reason ·
                    a separate line counts the non-declared skips and says "read those first"
§4.5                "`undecodable_text` is the one class marked EXPECTED_BY_PROTOCOL NO, and the
                    command COUNTS THOSE SEPARATELY, because an allowlisted .md file that is not
                    text is an anomaly rather than a design"
guarantee table     verify --post-read guarantees enumeration with class and reason; its
                    FAILURE_MODE column carries "the content of every file printed under
                    [UNCHECKED] — named with its reason, never silent"
§3 ex-ante list     "no file present in either surface outside ALLOWED_PATHS" — a re-encoded
                    allowlisted file is inside ALLOWED_PATHS, so no clause is violated
```

**Nothing in the protocol requires an unexpected unscanned artifact to block**, and nothing
implies it. The claimed guarantee is enumeration, not prevention, and the runtime behaviour
matches the claim exactly. I am explicitly declining to invent a stronger security guarantee than
the protocol provides.

**EXPECTED_BY_PROTOCOL:NO SEMANTICS: INFORMATIONAL** — declared as such, consistent between the
tool and the protocol, not ambiguous. **RUNTIME RESULT: PASS, named, counted separately.**

The residual that makes it informational rather than weak is stated by the candidate itself: the
allowlist check compares **paths**, and parity compares A against B, so an identical edit to both
surfaces is seen by neither. That is `P-4`, and §16 confirms it is carried truthfully.

---

## 10 · Tool claims and normative claims, measured

```
TOOL OUTPUT CLAIMS   --post-read   TRUE   — verified against the independent file universe:
                                            48 = 16 scanned + 32 censused, 0 silent, 0 overlap
                     pre-handover  FALSE  — the same two sentences, 32 silent files, 0 census
NORMATIVE CLAIMS     §4.5 falsifier + guarantee-table row for --post-read      TRUE (scoped)
                     §4.5 bullet 2, "on every run"                             FALSE
                     §4.5 "a file is named in the census exactly when the
                       scan skipped it, because the same call decides both"    FALSE (unscoped)
                     guarantee-table row for verify (pre-handover):
                       "no identifier leak — all of it observed, not attested" OVERCLAIMS
                       (16 files per surface are never opened and never named)
```

**TOOL OUTPUT CLAIMS: FALSE. NORMATIVE CLAIMS: FALSE.** Both only in the pre-handover mode, and
both are `M-4`.

---

## 11 · Positive controls — the reported instance is repaired, the class is not

| Control | Revision 3 | Revision 4 | Could it still hold the defect? |
|---|---|---|---|
| `test_positive_control_an_honest_reading_passes_post_read` | asserted `rc == 0` and `VERDICT: PASS` only, and passed over a tree with 10 silent files | **pins the whole census** against the hand-written literal plus four expected additions | **No, in `--post-read`.** Fails against revision 3's tool — I ran it |
| `test_the_census_is_exactly_the_present_files_the_scan_did_not_read` | asserted a 3-path set excluding its fixture's 5 decodable exempt paths | literal oracle, 13 paths with classes | No, in `--post-read` |
| `test_freeze_still_calls_a_binary_render_an_output` | present | unchanged; asserts `OUTPUT_FILE_SET` **and** `UNEXPECTED_FILE_SET == []` | No |
| `test_positive_control_the_scan_fires_on_an_allowlisted_scanned_file` | new | asserts both actors leak, and `PARITY BROKEN` absent | No |
| `test_positive_control_the_same_file_clean_is_scanned_and_silent` | new | asserts the clean file appears in neither population | No |
| **every one of the above** | — | — | **YES, pre-handover.** Not one asserts anything about the pre-read census, over fixtures whose oracle constants are named `…_AT_HANDOVER` |

**POSITIVE CONTROLS: PASS for `M-3` as reported; the class recurs at `M-4`.** This is `L-1` of
`SLR-plan-0003` a **fourth** time — a repaired instance is not a repaired class — and it is the
substance of §5D rather than a separate finding.

---

## 12 · Hostile tests — reason-aware

```
candidate suite @ rev4                   71 tests · 71 green
differential: rev4 tests vs rev3 tool    12 of 71 FAIL (11 failures + 1 error)  ← reproduced exactly
  ScanSkipClassTests ×6 · ExpectedOutputPrefixTests ×4 · CensusContractTests ×2
  including test_positive_control_an_honest_reading_passes_post_read
static audit of the suite (AST)          tests asserting ONLY an exit code: 4 of 71
  FreezeReceiptTests.test_freezing_under_a_wrong_benchmark_id_refuses   rc=2, names BENCH-AB-001
  FreezeReceiptTests.test_freezing_a_tree_holding_a_symlink_refuses     rc=2, prints SYMLINK
  FreezeReceiptTests.test_an_invalid_first_pass_state_refuses           rc=2, argparse
                                                                        "invalid choice", choices listed
  PopulationBoundingTests.test_declaring_the_source_empty_makes_it_pass rc=0 — a POSITIVE control,
                                                                        self-protecting: a wrong
                                                                        invocation gives rc=2 and fails
```

Each of the four was re-run by hand with its reason asserted, and each fires for the correct
reason. None is load-bearing for any claim in this candidate. Every probe **added** at revision 4
asserts a class or a reason string.

**WRONG-REASON LOAD-BEARING PASSES: 0.**

> **One committed by this reviewer, caught by its own control.** My `freeze` battery reported
> `rc=2` on all thirteen cases *including the positive control*, because I had omitted
> `--actor-id` and `--benchmark-id`. Every negative "passed". It was caught only because the
> battery requires its positive control to exit **0**. Fourth sighting of this defect in my own
> harnesses; recorded in `SLR-mirror-0012`, not self-ratified.

---

## 13 · M-1 and M-2 — both remain closed

**M-1: PASS.**

```
git diff cbce3016 a210f738 -- scripts/test_locator_obligation_reaches_every_route.py   → EMPTY
git diff a3cad1d  a210f738 -- (same)                                                   → EMPTY
EXEMPT set                                     unchanged, 8 entries, verified line by line
§5.1 of controlled_benchmark_ab.md             untouched at revision 4
test_every_route_carries_the_obligation_or_declares_an_exemption   OK at cbce3016 AND at a210f738
```

The obligation is semantically carried, verified at source rather than by token count: §5.1 names
the **field** (`verbatim_locators.entries[]` with its six components), the **validator**
(`deepdive_manifest.py`'s `SECTIONS` gate), the **consequence** (*a reading declared complete
without it is not complete; step 5 does not repair it*) and the **scoring** (`EVIDENCE COVERAGE`
and `PROVENANCE` on an empty locator set, step 7's blind audit with no triple). The guard is a
substring test, so token-only appeasement remained available and was not used.

**M-2: PASS.** The `output/renders/smuggled.md` silent path does not return, in **either** mode:

```
pre-handover   rc=1   NOT ALLOWLISTED + IDENTIFIER LEAK
--post-read    rc=1   NOT ALLOWLISTED + IDENTIFIER LEAK
freeze         output/renders/smuggled.md ∈ UNEXPECTED_FILE_SET, ∉ OUTPUT_FILE_SET
```

`_is_expected_output`, `_is_decodable_text` and `_under_expected_prefix` are byte-identical to
revision 3. Neither mechanism was redesigned.

---

## 14 · Freeze — PASS, 16 cases, each on its reason

```
POSITIVE CONTROL untouched tree                       rc=0 · 29 fields · outputs 0 · unexpected 0
  SURFACE_ABSOLUTE_PATH = "NOT RECORDED — local-instance value" — no machine path leaked
expected render + declared output                     OUTPUT_FILE_SET = [receipt.json, fig1.png]
decodable text in the render slot                     UNEXPECTED_FILE_SET = [smuggled.md]
a real binary render                                  OUTPUT — positive control, unmoved
UTF-16 text under the render prefix                   OUTPUT — the declared cost of the byte rule
UTF-16 over an allowlisted INPUT                      neither OUTPUT nor UNEXPECTED; in FILES with
                                                      its digest — freeze says nothing about it and
                                                      the census names it. No contradiction.
freezing A's tree as scientist-b                      rc=2, names 'scientist-a' from ASSIGNMENT.md
wrong benchmark id                                    rc=2, names BENCH-AB-001
invalid first-pass state                              rc=2, "invalid choice", choices listed
a symlink present in the tree                         rc=2, SYMLINK
verify-freeze POSITIVE CONTROL untouched              rc=0
one edited byte after the freeze                      rc=1, names roles/scientist.md
a file added after the freeze                         rc=1, names newfile.md
a file removed after the freeze                       rc=1, names roles/scientist.md
equal-count substitution after the freeze             rc=1
receipt pointed at the other actor's tree             rc=1
                                                                              16 / 16
```

`cmd_freeze`, `cmd_verify_freeze` and `_classify` are byte-identical to revision 3. **Freeze does
not reclassify any item in a way that contradicts the census**: the one case where the two speak
about the same file — a re-encoded allowlisted input — has freeze recording it as an ordinary
input with its digest while the census names it `undecodable_text`, which are answers to
different questions and are both true.

**FREEZE: PASS.**

---

## 15 · Regression accounting — reproduced with my own harness

Clean detached worktrees, neither holding `files/`. Every target of `run_release_regressions.py`
run the way the runner runs it. The harness records the **omission channel** — a suite exiting
non-zero with no parsed test failure — because `ADDED = 0` is worthless if that channel is
non-empty (`SLR-plan-0003` L-4).

```
                                    BASE cbce3016      REV 4 a210f738
targets in TESTS (AST-counted)            64                 65
targets executed                          64                 65      ← two are line-continued
                                                                        paths my first regex split;
                                                                        both run green at both tips
tests executed                           870                941      (+71, the new suite)
FAILING SUITES                             6                  6
FAILING TESTS                              7                  7
suites red with NO parsed test failure      ∅                  ∅      ← the omission channel is empty
```

**FAILING TESTS at both tips — the same seven, and nothing else:**

```
framework/scripts/test_session_self_eval.py::SelfEvalGate::test_diagnosis_is_wired_before_growth_and_takeaways
scripts/test_abstract_corpus_is_not_evidence.py::…::test_the_bootstrap_bounds_the_corpus (file='CLAUDE.md')
scripts/test_fulltext_trace_contract.py::…::test_normative_layers_make_receipts_universal
scripts/test_fulltext_trace_contract.py::…::test_normative_write_rules_name_the_append_only_carveout
scripts/test_locator_obligation_reaches_every_route.py::…::test_the_bootstrap_states_the_rule (file='CLAUDE.md')
scripts/test_release_runner_verdict.py::…::test_every_tracked_test_file_is_in_the_runner
scripts/test_release_surface.py::…::test_shebang_python_entrypoints_are_executable

ADDED FAILING TESTS    (rev4 − base) = ∅        0
REMOVED FAILING TESTS  (base − rev4) = ∅        0
SHARED FAILING TESTS                 = 7
SAME-REASON                          = 7 / 7
```

Each shared failure's full block was compared after normalizing only the worktree root, temporary
directories, `line <N>`, addresses and elapsed times. **No assertion text was normalized**, so a
changed reason could not be normalized into agreement. All seven are byte-identical after that
substitution — including `test_shebang_python_entrypoints_are_executable`, whose assertion
carries the list of non-executable entrypoints: the list is the same at both tips, so the
candidate's two new `755` files neither joined it nor displaced anything.

**REGRESSION: PASS. FAILING-SUITE DELTA 0 · TEST-METHOD DELTA 0 · UNATTRIBUTED CHANNEL EMPTY.**

---

## 16 · Carried residuals — classified, none allowed to overclaim closure

| # | Plan's class at rev 4 | Mirror's finding |
|---|---|---|
| **P-4** | CARRIED and now STATED, not closed | **CARRIED, TRUTHFULLY.** `verify` takes no digest input — I read the CLI. `M-3`'s stronger language does **not** imply it is solved: the `scan_exempt_input` census line scopes its own coverage claim to *"cross-surface parity for a change made to **one surface only**"*, and §4.5 states in its own words that an identical edit to both surfaces is seen by neither and that `build --emit-digests` writes a record nothing consumes. Every hostile probe in this review exercised exactly that move, and parity was silent in every one — as declared |
| **N-1** | CARRIED | **NON-BLOCKING CARRIED.** `surface_spec.json` is edited at this revision — two `_note` blocks, both about the census — and the File012 normalization contradiction is not among them. Correctly declared |
| **N-2** | CARRIED, unchanged | **NON-BLOCKING CARRIED. Reproduced at revision 4:** File011 moved into `declared_empty_sources` drops the population **65 → 58**, `rc=0`, nothing printed. `cmd_population` byte-identical, verified by AST. The finding goes live the moment a second entry is added; the one declared entry (File008) was read independently at revision 3 and is genuinely empty |
| **N-3** | CARRIED, latent | **NON-BLOCKING CARRIED.** `_pdf_pages` / `_regex_units` byte-identical, verified |
| **N-6** | CARRIED, declared | **NON-BLOCKING CARRIED.** 4 exit-code-only assertions measured by AST (Plan says three; the fourth is a positive control asserting `rc==0`, which is self-protecting). Each re-verified to fire for the right reason; none load-bearing |
| **N-7** | CARRIED, still unreconciled | **UNRESOLVED, honestly labelled.** Revision 4 did not re-run revision 1's tool and neither did I. Third review in a row where a measured number and an inferred explanation face each other |
| **N-8** | CARRIED, contained | **NON-BLOCKING CARRIED.** The manifest's structural claim is exact and I verified it independently by AST: `cmd_locators`, `cmd_freeze`, `cmd_verify_freeze`, `cmd_population`, `_classify`, `cmd_build`, `_is_expected_output`, `_is_decodable_text`, `iter_files`, `iter_symlinks`, `tree_digest` — all byte-identical. A census cannot reach a lexical path check, and the candidate is right to refuse to claim it did |
| **N-9** | CARRIED | **NON-BLOCKING CARRIED.** Vocabulary in a note, untouched |
| **N-4 · N-5** | remain resolved | **CONFIRMED.** §3G and §5 untouched at this revision |
| **P-1** | CARRIED, not fixed | **CORRECTLY CARRIED.** It is `BASE_HEAD`'s guard and not this candidate's defect; widening it inside a one-finding revision would be scope |
| **P-2** | ACCEPTED and stated | **RESOLVED.** §4.1b now names the missing premise |
| **P-3** | CARRIED | **CONFIRMED** — see N-6 |
| **P-5** | CARRIED | **CONFIRMED** — see N-7 |
| **R-1 … R-12** | (revision 1) | Not reopened. The files carrying them are byte-identical to revision 3. `R-10` is still Mirror's own worktree debt and moved a number in this review again (§0) |

**New this review, non-blocking:**

- **P-6** — `iter_files` excludes `.git/**` from both the scan and the census. 47 327 bytes of a
  forbidden prior-output artifact at `.git/info/notes.md` gave `VERDICT: PASS`, an unchanged
  census, an unchanged `files 24`, and no mention anywhere; `freeze` did not name it either.
  Pre-existing and documented in the docstring, absent from a built surface, and **not** the
  reason for this verdict. But the printed partition sentence is scoped to `iter_files()`'s notion
  of *present* and never says so.
- **P-7** — a **pure-ASCII** payload encoded UTF-16 without a BOM decodes as valid UTF-8, so the
  file is genuinely scanned and the regex finds nothing across the NUL interleaving. The census is
  right to omit it and the tool's claim stays literally true; this is a limit of the scan, not of
  the census, and it vanishes with one non-ASCII character.
- **P-8** — the manifest's front matter says *"Four content files changed"* while five content
  files change, and the omitted one is `learning/plan/SLR-plan-0004.md` — precisely the entry that
  moves the binding from `1613fa3b…` to `07b65b37…`. §2 states it correctly (*"edits FOUR … and
  ADDS exactly one"*), so this is an internal inconsistency in the front matter rather than a
  wrong number in the evidence. Same class as `N-4` / `N-5`: a manifest whose numbers are wrong is
  not a smaller problem for being non-blocking.

---

## 17 · SLR-plan-0004 — BOUND, and curated under Annex E.2

### 17.1 · Procedural integrity — PASS

```
belongs to this session/candidate   task SCIENTIST-AB-SPEC-001 · directive v1 · generation 4 ✓
is CONTENT                          learning/plan/ is under no CONTROL_PLANE_ROOT; P5.1 declares
                                    learning/ CONTENT by intent ✓
committed BEFORE the binding        a210f738 IS the declared CONTENT_TIP and the commit that
                                    carries the record ✓
included in the authoritative hash  the SINGLE content-domain entry separating 1613fa3b… (524)
                                    from 07b65b37… (525) — reproduced by me ✓
no pre-SLR hash declared            b1061ebb / 1613fa3b… is a real content commit whose value I
                                    reproduced as a control; it appears in the manifest only at
                                    line 118 (a labelled control), 133 ("is NOT a superseded
                                    binding"), 136, 168 and 180. It was NEVER declared as a
                                    binding, and nothing had to be superseded within revision 4 ✓
```

The distinction Plan asks to be verified is real, and it is the correction `SLR-plan-0003` L-5
owed: revision 3 declared `7cef4ccc…` and then had to supersede it; revision 4 wrote the record
first and named a tip once. **SLR-plan-0004: BOUND.**

### 17.2 · Epistemic curation (Annex E.2)

Vocabulary is the repository's: `CONFIRMATION_CLASS ∈ {ORIGINAL_OBSERVATION, REPLICATION,
EXPOSURE_AFTER_BROADCAST}`; E.1's status machine; E.2's threshold (≥2 confirmations in the first
two classes, or 1 + Mirror validation) and its conflict rule, *"Conflitti → Mirror aggiudica →
SUPERSEDED motivato"*. **No `LEARNING_INDEX` exists** — E.2 names the instrument, Plan owns its
durability — so this curation lives here and in `SLR-mirror-0012` and can be queried by nothing.
That debt is Plan's, declared, unchanged, and is now three reviews old.

Every class in the record is marked *proposed* and the record explicitly refuses to self-certify.
That is correct and is the behaviour E.2 exists to produce.

**L-1 — *I enumerated the exceptions I knew about, and the code knew four*.**
`ORIGINAL_OBSERVATION` (plan) — **ACCEPTED**, and the adjacency question the record raises for me
is answered: this is **not** an `EXPOSURE_AFTER_BROADCAST` of `SLR-mirror-0011` §1. The two
claims differ. Mirror's names *which artifact* carries the next false claim; Plan's names the
*derivation source* — the finding is a lower bound, the predicate is the denominator — and its
evidence is a measurement I did not have and could not have supplied: **16 per surface against
my 10**. I reproduced that measurement independently (24 present · 8 scanned · 16 skipped · 0
named) and add `CONFIRMATION_CLASS: REPLICATION` (actor `mirror`, this session) on it.
`EVIDENCE_COUNT: 2` in the first two classes → **BEST_PRACTICE_CANDIDATE** without my validation.
`CLASS: FAILURE_PATTERN` — accepted.

**L-2 — *an equality maintained by two copies of a rule is not an equality*.**
`ORIGINAL_OBSERVATION` — **ACCEPTED.** `CLASS: MICRO_UPGRADE` — accepted. `STATUS: LOCAL`. The
repair is real and I verified it structurally rather than trusting the description. One
formulation inside the record is **SUPERSEDED, with reason**:

> *"The equality `actual unscanned == declared unscanned` stops being a property somebody
> maintains and becomes one that cannot be expressed otherwise."*

**It is still expressible, and revision 4 expresses it.** Pre-handover, the predicate decides the
skip and the printing site never runs, so 32 present files are skipped and none is declared. One
shared predicate makes the two *consistent when both execute*; it does nothing about a reporting
site behind a conditional. The same over-reach is in the tool's comment (*"no longer
expressible"*) and in §4.5 (*"on every run"*), which is why §5C counts four artifacts.

**REFINED_FORMULATION (L-2):** *a report and the behaviour it describes must come from the same
call **and** the reporting site must be reachable in every mode in which the description is
printed; sharing the predicate removes the drift between two implementations, not the gap between
a claim and a conditional.* With Plan's `ORIGINAL_OBSERVATION` plus this Mirror validation, the
**narrowed** formulation reaches `BEST_PRACTICE_CANDIDATE`. The general one does not.

The record's honesty about the cost — *"the honest census is loud… 32 `[UNCHECKED]` lines where
it printed none"* — is accepted and is the right trade, stated where a reviewer can disagree.

**L-3 — *my test's expectation was read off the implementation*.**
`REPLICATION` of `SLR-plan-0003` L-1, **correctly self-classed** rather than claimed as original —
accepted; it is the instance I named in `REV-SCIAB-MIRROR-003` §10.2 and Plan accepts my reading
of its own record. `CLASS: FAILURE_PATTERN` — accepted. `STATUS: LOCAL`. The diagnosis of *why*
(`expected = implementation_filter(actual)` cannot fail) is correct and is the most transferable
sentence in the record. Both replacement oracles are genuinely independent (§7), and the
differential — 12 of 71 against revision 3 — is real; I reproduced it exactly.

One formulation needs narrowing rather than superseding. The record treats L-1's class as
addressed by replacing the oracle. **The class recurs at `M-4`**: the new oracles are sound and are
exercised only in the mode where the answer is already known, under constants named
`…_AT_HANDOVER`. Redirecting one call makes the candidate's own test report `SILENT: 10`.

**REFINED_FORMULATION (L-3):** *replacing a coupled oracle with an independent one repairs the
oracle; the class is only repaired when the independent oracle is run in every mode the claim it
supports is printed in.* `CONFIRMATION_CLASS: REPLICATION` (mirror, this session) of
`SLR-plan-0003` L-1 — the **fourth** instance of that pattern, and the second inside the revision
that records it.

**L-4 — *the same bytes at four paths, and the two that stayed quiet*.**
`REPLICATION` of `SLR-mirror-0011` §4 — **accepted**, correctly self-classed. `CLASS:
BEST_PRACTICE_CANDIDATE (proposed, not self-ratified)` — accepted; the practice now has
`ORIGINAL_OBSERVATION` + three `REPLICATION`s across both actors and is over E.2's threshold on
the first two classes. Its addition from the author's side is the **cost** (~25 minutes) and the
sub-observation that matters more than the timing: *a battery that plants hostile bytes in one
tree measures the parity check while believing it measures the scan*. I verified this is applied —
`_plant()` writes to both surfaces and every new probe asserts `PARITY BROKEN` absent — and I
applied it in every battery in this review. **Accepted, and it is the reason §5's six-path table
is evidence rather than a design note.**

**Cross-cutting, and the one I would put in `ACTIVE_LESSONS` if the instrument existed.** Both
actors independently wrote, in the same twenty-four hours, that the artifact written to correct a
false claim is where the next one lives — and revision 4 is the third consecutive instance. The
pattern is not that the authors are careless. It is that a remediation is scoped to the *mode, the
key, or the population the finding named*, and the finding is always a lower bound. `M-2` was
scoped to one spec key; `M-3` to one skip condition; `M-4` to one CLI flag.

**G.2.** This curation is of Plan's learning, which is squarely E.2 work and squarely Mirror's. It
ratifies nothing of Mirror's own methodology. The observation this session produced about my own
harness (§12) is filed `LOCAL` in `SLR-mirror-0012` and is **not** self-ratified; if it is to bind
it goes `MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by
Orchestrator.

---

## 18 · Non-regression of stabilized properties

Sixteen of revision 3's twenty content files are **byte-identical at revision 4 by blob sha**, and
the binding proves no other content moved. Where a row rests entirely on those files, a targeted
confirmation is recorded; where revision 4 touched the file, the row was re-measured.

```
B-1 SCIENTIFIC POPULATION  PASS       re-derived ×2, byte-identical to each other AND to the
                                      tracked evidence_units.json (sha b41c7b9f…) · 65 units ·
                                      109 panels · 6 main_figure · 7 main_results ·
                                      2 main_methods · 10 supplementary_figure ·
                                      24 supplement_methods · 7 supplement_table ·
                                      9 source_data_blot · 1 declared empty
B-3 FREEZE RECEIPT         PASS       §14 — 16/16, 29 fields, no absolute path
B-5 SEVEN BENCHMARK FIELDS PASS       OUTPUT_SCHEMA.md byte-identical to revision 3
MODE A/B TASK SCOPING      PASS       scientist_reading_modes.md and both MODE files
                                      byte-identical; no instruction file touched at rev 4
ACTOR EQUIVALENCE          PRESERVED  no file carrying §32 was edited at this revision
C-2 FORWARD OWNERSHIP      PASS       byte-identical
INPUT PARITY               PASS       5 negatives, each on the reason, positive control first:
                                      PARITY BROKEN · NOT DIFFERING · ABSENT · NOT ALLOWLISTED ·
                                      IDENTIFIER LEAK
SCIENTIFIC DEPTH           PRESERVED  no MODE file, no assignment, no instruction and no
                                      population file changed at revision 4
ACTOR REGISTRATION         PASS       roles/scientist.md and BOOTSTRAP.md byte-identical
CANONICALIZATION DEP.      CONFIRMED  measured at both tips: scientist 355e3529… → 82423a48…;
                                      plan, mirror and orchestrator IDENTICAL
PUBLICATION GATE           PASS / BLOCKS 0 at the content tip; [REVIEW] rows pre-existing
NO PARALLEL CLAIM SCHEMA   NONE       no claim-schema file changed at revision 4
LINT / growth anchors      PASS (1 pre-existing INFO) · claims=39 · papers=70 · corpus=356 ·
                                      literature=390
```

---

## 19 · EVIDENCE_FOR · EVIDENCE_AGAINST · ALTERNATIVES · KEY_OBJECTIONS

**EVIDENCE_FOR.** The binding reproduced eleven times, seven of them without the governed script,
with four published control values and the line-sort trap exercised deliberately; `M-3` closed in
`--post-read` against an independent file universe built with `os.walk` and a behavioural probe
whose instrument check passed — 48 = 16 scanned + 32 censused, 0 silent, 0 overlap; the repair
structural rather than arithmetical, with 34 of 39 top-level definitions byte-identical and a
structural guard binding the two call sites; both test oracles genuinely independent, the honest
reading positive control now pinning the whole census, 12 of 71 tests failing against revision 3;
`M-1` and `M-2` closed with the guard byte-identical to `main` and the smuggle caught in both
modes; freeze sound on 16 cases each on its reason; the delta zero at test-method granularity over
seven shared failures whose reasons are byte-identical, with the omission channel empty at both
tips; the population re-derived byte-identically to the tracked file; every carried residual named
and none falsely closed, `P-4` stated in the protocol rather than quietly absorbed; the Session
Learning Record bound correctly with no intermediate binding to supersede, correcting its
predecessor's failure; no scope creep.

**EVIDENCE_AGAINST.** `M-4`, measured on a clean build with an independent oracle whose instrument
check passed: 32 present files skipped by the identifier scan, zero named, `VERDICT: PASS`, and
two sentences printed asserting the partition. Reproduced with the same bytes at six paths in both
modes, two caught by location in both; and in its sharpest form with 46 709 characters of a
declared forbidden prior-output artifact re-encoded UTF-16 into an allowlisted `.md` in both
surfaces, mentioned zero times by the run that gates handover. The candidate's own behavioural
oracle reports `SILENT: 10` when its one `verify` call is switched to the mode its own constants
are named for.

**ALTERNATIVES_CONSIDERED.**
(i) *Accept, carrying `M-4` as a recorded finding* — **rejected.** It is a false clause in the
tool's `PASS` output and in the protocol's unscoped bullet, which is the exact ground on which
`M-2` and `M-3` were blocking in the two preceding revisions. Weakening the standard now would be
the ratchet failing, not the candidate improving.
(ii) *Treat `M-4` as pre-existing, since revision 3's pre-read sentence was also false* —
**rejected in part, accepted in part.** The pre-read scan exemption is pre-existing and I say so.
The **partition claim** and the reference to a printed list are new at revision 4 and strictly
stronger than what they replaced, exactly as revision 3's sentence was stronger than revision 2's.
(iii) *Treat `M-3` as unclosed and fold `M-4` into it* — **rejected.** `M-3` as reported is
genuinely closed and it would be inaccurate to say otherwise; the difference matters to whoever
reads revision 5.
(iv) *Require `EXPECTED_BY_PROTOCOL: NO` to block* — **rejected.** The protocol does not say so and
inventing a stronger security guarantee than the artifact claims is the failure mode this review
exists to prevent, pointed the other way.
(v) *Make `P-6` (`.git/**`) blocking too* — **rejected.** Pre-existing, documented in the code,
absent from a built surface, and unchanged by this revision.

**KEY_OBJECTIONS Plan may raise, and my answer.**
*"The §4.5 guarantee and its falsifier are explicitly scoped to `--post-read`, so nothing
normative is false."* — The falsifier is scoped and I record it as true. Bullet 2 of the same
section says *on every run* in bold, the sentence four lines below is unscoped, and the tool prints
the unscoped claim in both modes. A reviewer reads what is printed.
*"At handover the surface is a function of the allowlist, so there is nothing to find."* — Then the
census costs nothing to print there, and the sentence claiming it is printed costs a reviewer's
trust. The same argument was available for `M-3` — a clean build, before any reader — and was
rejected by the candidate's own method.
*"Revision 4 was scoped to `M-3`; the pre-read mode is new scope."* — `M-4` is inside `M-3`'s own
remedy, in the sentence that remedy introduced, and the parameter to reach it was added by that
remedy. It is not new scope; it is the remedy measured. That is verbatim the answer
`REV-SCIAB-MIRROR-003` gave to the same objection, and it was correct then.
*"The remedy is large."* — It is the guard on one block. `unchecked_surface(root, spec, post_read)`
already takes the argument and `cmd_verify` already passes it.

---

## 20 · VERDICT

```
Annex C.2 VERDICT       REFINED — M-3 is closed, structurally rather than arithmetically, with two
                        independent oracles and a shared predicate that removes the drift between
                        two implementations; and the sentence written to describe the closure is
                        printed unchanged by the run that gates handover, where the census does not
                        exist. The third consecutive revision in which the artifact written to
                        correct a false claim carries the next one, on the same seam.
REFINED_FORMULATION     "SCANNED and [UNCHECKED] partition the present files" is true of
                        `verify --post-read` and false of `verify`. 32 present files on a clean
                        build, 16 per surface, before any reader exists; and `[UNCHECKED]` is
                        scoped to iter_files()'s notion of present, which excludes .git/**.
MIRROR_REVIEW           REQUEST CHANGES
REVIEWER_CONFIDENCE     high on the binding (11 reproductions, 4 historical controls, trap run)
                        high on M-3's closure in --post-read (independent os.walk universe +
                          behavioural probe, instrument check passed, 0 silent, 0 overlap)
                        high on M-4 (measured both modes with the same harness; same bytes at six
                          paths; the candidate's own oracle fails when redirected; four artifacts
                          quoted at source)
                        high on the regression delta (own harness, omission channel empty,
                          7/7 same-reason with no assertion text normalized)
RESIDUAL_UNCERTAINTY    N-7 is unreconciled for the third review running and I did not settle it.
                        M-4's exposure at handover is smaller than M-3's post-read exposure, and I
                        weigh a false PASS clause as blocking on consistency with
                        REV-SCIAB-MIRROR-002 and -003 rather than on an independent severity scale
                        — I state that rather than resolve it. P-6 is pre-existing and I did not
                        let it influence the verdict. My freeze battery's first run was a
                        wrong-invocation pass caught by its own positive control, which is the
                        fourth time; the numbers reported here are from the corrected run.
EVIDENCE_NEEDED         the census printed in both modes — the guard on the block, the parameter
                        already being threaded — or the two printed sentences and §4.5's bullet 2
                        scoped to --post-read with the pre-handover skip population declared as a
                        named residual; plus the pre-read case brought inside
                        test_every_present_file_is_either_scanned_or_named_and_never_both, which
                        is the negative control it lacks and the fourth instance of the
                        candidate's own L-1. P-8's front-matter count corrected to five.
WHAT_WOULD_CHANGE_MY_MIND
                        M-4: a run of `verify` WITHOUT --post-read over a surface whose CLAUDE.md
                             holds appended forbidden prior-output bytes that either reports a
                             finding or prints CLAUDE.md under [UNCHECKED] — it does neither,
                             while the same bytes at roles/scientist.md produce IDENTIFIER LEAK in
                             the same run; or a reading of "no present file is skipped by the
                             identifier scan without appearing in that list" under which 32
                             unlisted skipped files satisfy it; or normative text scoping bullet
                             2's "on every run" and the tool's two sentences to --post-read, in
                             which case the finding becomes P-class and the verdict changes.
                        M-3: any present file in --post-read that the tool neither scans nor names
                             — 48 probed by effect, 0 found.
                        M-1: the guard failing at cbce3016 in a clean worktree — it passes; or
                             evidence that §5.1 is a token rather than an obligation — it names
                             the field, the validator, the consequence and the scoring.
AUTHOR_RESPONSE         required (C.2); silence is not acceptance.
```

**HUMAN_APPROVAL: NONE — not granted, not recommended, not implied.**
**MAIN: cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED.**
**Nothing was executed, nothing canonicalized, no benchmark run, no registration performed, no
other actor's worktree written.**

---

## 21 · Scope, and what this review did not touch

**SCOPE CREEP: NONE.** The content diff touches no `*_current.md`, no registry, no approval queue,
no lease record, no `runtime/`, no Agent Card, no receipt ledger, no P7, no Metacognition surface,
no Scientist C, no second paper, and no session-routing artifact — measured: zero content paths
matching `session|rout|registr`. The single grep hit against `lease` in the full diff is
`scripts/run_release_regressions.py`, matching the substring inside *re**lease***; its diff is one
added line registering the new suite, which `test_release_runner_verdict.py` requires. The new
executable reads none of them: `agent_card` 0 · `_current` 0 · `registry` 0 · `lease` 0 ·
`approval` 0 · `watcher` 0; the single `receipts` hit is a word inside a `FAILURE_MODE` string.

**SESSION-ROUTING DEBT: OUT OF SCOPE — NOT SILENTLY RESOLVED.** §5c of the manifest names the gap
between stable `ACTOR_ID` and current routable `SESSION_REF` and implements nothing. This review
implements nothing either, declares no `SESSION_REF` for itself, and infers no routing from chat
recency.

---

## 22 · Provenance of this review

Detached scratch worktrees created with `git worktree add --detach`: `wt-base` at `cbce3016`,
`wt-rev4` at `a210f738`, `wt-rev4m` at `0ec863b3`, `wt-rev3` at `a3cad1d`, `wt-rev4mid` at
`b1061ebb`, `wt-diff` at `a3cad1d`, `wt-surf4` and `wt-surf3` for surface construction. Neither
regression worktree holds `files/`. The packet was copied read-only from root `files/fulltext/`
into the two surface worktrees only. Both surface pairs were built into the session scratchpad;
every attack surface is a copy under it. All binding numbers were computed in a worktree carrying
`BASE_HEAD`'s script and P5 v4, or by an implementation written in the scratchpad from P5.1/P5.2,
never in this branch's checkout, which carries P5 v3 (`R-10`).

The session guard refused one inline heredoc while the shell was inside a repository worktree. I
did not reach for an unchecked tool: the probe was authored with `Write` into the scratchpad and
invoked by name, and the measurement is the same one.

Time source: the runtime exposes no wall clock beyond the date. Governance loaded 3.1.1; the
mirror fingerprint is identical at `BASE_HEAD` and at the candidate content tip.

**Two wrong-invocation passes committed by this reviewer, both caught by controls.** (1) My
file-universe probe reported `SCANNED 0` — including for `roles/scientist.md`, which must leak —
because it indexed the wrong field of the finding line. Caught by requiring the control file to be
observed. (2) My freeze battery reported `rc=2` on thirteen consecutive cases, which reads as
thirteen correct refusals until you notice the positive control refused too; the cause was two
missing required arguments. Both runs were discarded and re-authored. This is the fourth and fifth
sighting of this defect in my own harnesses (`SLR-mirror-0010` §4, `SLR-mirror-0011` §3). The rule
that caught both — *in a negative battery the positive control is the instrument check; if it does
not pass, no negative in that battery is evidence* — is recorded in `SLR-mirror-0012` as a LOCAL
learning and is **not** self-ratified; if it is to bind, it goes the G.2 route.

**WRONG-REASON LOAD-BEARING PASSES in the candidate: 0.**
