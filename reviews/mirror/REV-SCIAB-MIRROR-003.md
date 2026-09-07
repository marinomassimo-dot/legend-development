---
artifact: MIRROR hostile review, revision 3 (Annex C.2)
review_id: REV-SCIAB-MIRROR-003
object: CAND-20260818-SCIENTIST-AB-SPEC rev 3 · CANDIDATE_CONTENT_HASH 570fcbbb…8ab7 @ base cbce3016
level: R4 (MIRROR_REQUIRED — role contract in CORE, two new protocols, MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here
date: 2026-08-19
supersedes: nothing. REV-SCIAB-MIRROR-001 and -002 stand as the reviews of revisions 1 and 2 and
  are not amended.
verdict: REQUEST CHANGES — M-1 closed, M-2's defect closed, one new blocking finding (M-3) of the
  same class introduced by M-2's remedy; nine carried findings re-classified, five recorded
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the candidate tip
---

# The delta is zero and the smuggle is caught. The census that proves it is short by ten files per surface.

Reviewed from `R-1`. **VERDICT TRANSFER: NONE.** Nothing carries over from
`REV-SCIAB-MIRROR-001` or `REV-SCIAB-MIRROR-002` — not a verdict, not a `PASS`, not one of the
fourteen rows revision 2 was found to have got right. Every number below was re-derived in
detached scratch worktrees of `BASE_HEAD` and of the candidate content tip, never in another
actor's worktree and never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror       branch mirror · HEAD 402e25cd · clean
ACTOR_ID          mirror · roles/mirror.md read in full · PERSISTENT_LEGEND_ACTOR · worktree mirror
governance        3.1.1 · Annex C (C.1 ladder, C.2 format, C.3 discipline, C.4 objects),
                  Annex E (E.1 lifecycle, E.2 LEARNING_INDEX + curation, E.6 record schema),
                  Annex G (G.1 perimeter, G.2 self-upgrade bar, G.3 metrics), body §12 and §15,
                  P5 — all read at BASE_HEAD, not from this branch
fingerprint       compose --role mirror  at BASE_HEAD cbce3016   3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                                         at content tip a3cad1d  3dff8954…f65c — IDENTICAL
                  (this review is conducted under the governance the candidate is based on)
STABLE ACTOR IDENTITY    mirror · worktree mirror · roles/mirror.md · reconstructed from durable
                  repository evidence alone; no part of it depended on a prior conversation
CURRENT SESSION ROUTING  not durable in the repository. No SESSION_REF is declared for this
                  session and none is invented. An actor cannot observe its own routing reference.
Agent Card        runtime/agent_card_registry.md lives on branch orchestrator; mirror's four
                  declared capabilities are UNVERIFIED per contract, and L2 is suspended
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
> pre-fix form, which reads P5 from the working tree instead of from the tip being hashed. Every
> binding number in §1 was therefore computed in a clean detached worktree of `BASE_HEAD`, which
> carries the canonical script and P5 v4. This is `R-10` of revision 1 — still Mirror's own debt,
> still not the candidate's, and still not fixed.

---

## 1 · Binding — PASS

```
base cbce3016 · tip a3cad1d (CONTENT TIP)           570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7   run 1
base cbce3016 · tip a3cad1d                         570fcbbb…8ab7   run 2
base cbce3016 · tip bdac30f (MANIFEST TIP, latest)  570fcbbb…8ab7   run 1
base cbce3016 · tip bdac30f                         570fcbbb…8ab7   run 2
independent recomputation WITHOUT the script (git ls-tree -r --full-tree + P5.2 serialization,
v4 prefix, three roots read by eye from P5 at BASE_HEAD, every entry newline-terminated)
  at a3cad1d   570fcbbb…8ab7   included 524 · excluded 29
  at bdac30f   570fcbbb…8ab7   included 524 · excluded 30   (+CHK-plan-0013, control plane)
POSITIVE CONTROLS on the same route — published values of earlier tips
  at b634829 (superseded rev-3 tip)  7cef4ccc…4596   included 523 · excluded 28   ✓ reproduces
  at 2fc0551 (its manifest commit)   7cef4ccc…4596                                ✓ invariant
  at daaa3335 (revision 2)           c0701094…21bcf  included 523 · excluded 27   ✓ reproduces
  at b965ca58 (revision 1)           3b568aae…916c75                              ✓ reproduces
main   cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED, merge-base of the branch
```

Four runs of the governed script and four independent recomputations without it. The authoritative
hash is **neither** `c0701094…` (revision 2) **nor** `7cef4ccc…` (the superseded revision-3 tip),
and the three published control values reproduce exactly — a second implementation that agrees
only with itself would prove nothing.

**Post-content commits.** `bdac30f` is the only commit after the content tip. It touches
`governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md`,
`ledger/checkpoints/plan/CHK-plan-0013.json` and `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` —
all three inside declared `CONTROL_PLANE_ROOTS`. The invariance is measured at both points and by
two independent routes; `MANIFEST_TIP` is informational and the manifest's argument for why is
correct.

**The one entry separating `570fcbbb…` from `7cef4ccc…`**, derived from the tree and not from the
report: `learning/plan/SLR-plan-0003.md`, added. 523 → 524. The other three paths in that diff are
control plane. The manifest's claim is exact.

**Content population, from Git:** 20 content files, **+5361 / −1**, no deletion, no history
rewrite; 6 control-plane files. Two mode changes, both new files
(`benchmark_input_surface.py`, `test_benchmark_input_surface.py`); **no existing file's mode
moved**. Revision 3 edits **five** of revision 2's nineteen content files and adds **one**;
the other fourteen are byte-identical by blob sha. No `*_current.md`, no registry, no receipt
ledger, no governance text.

**BINDING: PASS.**

### 1b · Superseded bindings — CORRECTLY CLASSIFIED

Every occurrence of a superseded value in the authoritative manifest (at `bdac30f`) was read with
its line. `c0701094…` appears at lines 5, 45, 115, 120, 896 — `supersedes:`, `SUPERSEDED_HASH:`,
a labelled positive control, a "neither … nor" sentence, and a Mirror instruction. `7cef4ccc…`
appears at lines 34, 114, 120, 122, 165, 897 — `SUPERSEDED_REV3_HASH:`, a labelled control, and
four sentences naming it as superseded. `3b568aae…` at lines 6 and 47, both `supersedes`.
**No third place presents either as current.** The superseded population counts (`36 / 115`,
"eight failing suites") survive only inside N-4 / N-5 correction annotations that name them as
superseded.

---

## 2 · STEELMAN (before the objections)

Revision 3 does the harder version of both remedies and then declares what it did not do.

`M-1` could have been closed in under a minute by pasting `verbatim_locators` into any paragraph
or by adding one path to `EXEMPT` with a plausible sentence, and the test could not have told the
difference. It was closed instead with a §5.1 that states the obligation, its field shape, its
validator, and its consequence — *a reading declared complete without `verbatim_locators.entries[]`
is not complete, and step 5 does not repair it* — and the manifest records the two cheap closures
it rejected and why. The guard is byte-identical to `main`. I checked; `git diff` is empty.

`M-2` could have been closed by printing the prefix as a blind spot, which would have made the
census true and the instrument weaker. It was closed by narrowing the exemption to bytes no scan
can read, which cost a predicate, a fixture repair, fourteen probes and a rule the reader is now
told before the reading rather than after. `SLR-plan-0003` §L-2 identifies that fork and names it
as a fork, which is the metacognition this laboratory is supposed to produce.

The Session Learning Record entered the reviewed population **before** review rather than after,
against the author's own first instinct, and `L-5` records that first instinct as the session's
failure with the two-command check that would have prevented it. The pre-SLR binding is recorded
as superseded rather than quietly replaced. Both blocking findings were reproduced at both tips
before a byte was edited. The differential I ran confirms the discrimination is in the tool and
not in the fixture. The manifest asks me to attack its own harness, names the alternative repairs
it rejected, and hands me the exact command that would falsify its guarantee.

I ran that command. What follows is where it succeeds.

---

## 3 · Population reviewed and tests executed

**Read in full:** the authoritative candidate manifest at `bdac30f` (912 lines), the handoff,
`controlled_benchmark_ab.md`, `benchmark_input_surface.py`, `test_benchmark_input_surface.py`,
`surface_spec.json`, `benchmark_manifest.json`, `population/evidence_units.json`, the seven
instruction files, `learning/plan/SLR-plan-0003.md` (255 lines), the rev2→rev3 diffs of all five
changed content files, `REV-SCIAB-MIRROR-001` and `-002` in full; at source: Annex C, Annex E,
Annex G, body §12 / §15, P5, `roles/mirror.md`, `scripts/test_locator_obligation_reaches_every_route.py`,
`claim_registry_current.md` at `BASE_HEAD`, and the packet (7 files, digests **7/7** equal to the
manifest's `SOURCE_FILES`).

**Executed** — detached scratch worktrees: `wt-base` = `cbce3016`, `wt-cand` / `wt-surf` =
`a3cad1d`, `wt-rev2` = `daaa3335`. Neither regression worktree holds `files/`, so the
environmental confound of revision 1 cannot arise. The packet was copied read-only from root into
`wt-surf` and `wt-rev2` only. All attack surfaces are copies under the session scratchpad.

```
binding                     4 script runs + 4 independent recomputations              PASS
release regressions         64 targets @ base · 65 @ rev3, own harness, per-test       see §5
M-1 guard, isolated         green at cbce3016 AND at a3cad1d; guard diff empty         PASS
adversarial suite @ rev3    59 tests, 59 green, registered in the battery              PASS
non-UTF-8 hostile battery   22 cases, each asserting the REASON                        22/22
freeze / verify-freeze      14 cases incl. tamper, substitution, identity, symlink     14/14
input parity                5 negatives, each on the reason                            5/5
locators (N-8)              5 cases, positive control required to exit 0               see §7
population                  re-derived ×2, byte-identical to each other AND to the
                            tracked evidence_units.json · 65 units · 109 panels        PASS
N-2 reproduction            File011 falsely declared empty → 65 → 58, rc=0, silent     REPRODUCED
File008 read independently  1 page · 256 chars · CRediT roles · 0 figure/table keys    genuinely empty
differential vs rev 2       3 key states, rev2 tool vs rev3 tool                       discriminates
publication gate            PASS / BLOCKS 0 at BASE_HEAD and at the content tip
legend_lint PASS (1 pre-existing INFO) · fulltext_receipts OK 128 chained, tail anchored
growth_anchors PASS — claims=39 · papers=70 · corpus=356 · literature=390
fingerprints                scientist 355e3529… → 82423a48… · plan 9c0c13fb… ·
                            mirror 3dff8954… · orchestrator e2c54470… — three IDENTICAL
claim registry @ BASE_HEAD  39 '## CLAIM' · **Uncertainty:** 0 · **Limitations:** 0
                            · **Contradictory evidence:** 0 · **Evidence boundary:** 5
```

---

## 4 · M-1 — CLOSED. The obligation is semantically carried, and the delta is zero at the granularity of the claim.

**The exact test, isolated, at both tips.**

```
scripts/test_locator_obligation_reaches_every_route.py
  ::ObligationReachesEveryRoute::test_every_route_carries_the_obligation_or_declares_an_exemption

  at BASE_HEAD  cbce3016   OK
  at CONTENT TIP a3cad1d   OK          (red at daaa3335 under REV-SCIAB-MIRROR-002)

git diff cbce3016 a3cad1d -- scripts/test_locator_obligation_reaches_every_route.py   → EMPTY
EXEMPT set                                                                            → unchanged, 8 entries
```

**The guard was not weakened and no dishonest exemption was added.** The guard is a substring test
for `verbatim_locators`, so token-only appeasement was available; it was not used.

**LOCATOR OBLIGATION: SEMANTICALLY CARRIED.** Verified at source rather than by token count:

- the route **does** order complete scientific readings — §5 step 4 is *"blind first pass,
  autonomous, in the surface, at full depth"*, and §5.1 names it a `complete_fulltext_read` in the
  sense of `fulltext_read_receipt.md`, with *"being a benchmark relaxes nothing about it"*;
- the obligation is expressed with its **field shape** (proposition · snippet · surface · artifact
  · anchor · `panel_text_relation`), its **destination** (`verbatim_locators.entries[]` in the
  reader's own work manifest), its **gate** (`deepdive_manifest.py`'s `SECTIONS`), and its
  **consequence** (*not complete*; the freeze does not repair it; `EVIDENCE COVERAGE` and
  `PROVENANCE` score on an empty set; step 7's blind audit has no triple);
- it reaches the reader: `OUTPUT_SCHEMA.md` carries the literal token and the full entry shape;
  `BENCHMARK_INSTRUCTIONS.md` §1 requires *"verbatim locators captured while the document is
  open"* and its self-check requires every locator's `artifact` to be inside the surface and every
  claim candidate to carry all eight labels; `MODE_A.md` defines `locator` as *"the verbatim
  sentence, with surface and anchor"*.

**Test-level delta, measured with my own harness, not Plan's.**

The harness runs every target of `run_release_regressions.py` the way the runner does —
`python3 <relative>` from the tree root — in the two detached worktrees, and parses `FAIL:` and
`ERROR:` headers, subTest parameter suffixes, `Ran N tests`, and the case of a suite exiting
non-zero with **no** parsed test failure (recorded as `unattributed`). That last class is the one
`SLR-plan-0003` §L-4 warns makes `ADDED = 0` true by omission.

```
                                 BASE cbce3016      REV 3 a3cad1d
targets present                        64                 65
targets missing                         0                  0
FAILING SUITES                          6                  6
FAILING TESTS                           7                  7
suites red with NO parsed test failure  ∅                  ∅     ← the omission channel is empty
total tests executed                  870                929     (+59, the new suite)
```

**FAILING TESTS at both tips — the same seven, and nothing else:**

```
framework/scripts/test_session_self_eval.py::test_diagnosis_is_wired_before_growth_and_takeaways
scripts/test_abstract_corpus_is_not_evidence.py::test_the_bootstrap_bounds_the_corpus (file='CLAUDE.md')
scripts/test_fulltext_trace_contract.py::test_normative_layers_make_receipts_universal
scripts/test_fulltext_trace_contract.py::test_normative_write_rules_name_the_append_only_carveout
scripts/test_locator_obligation_reaches_every_route.py::test_the_bootstrap_states_the_rule (file='CLAUDE.md')
scripts/test_release_runner_verdict.py::test_every_tracked_test_file_is_in_the_runner
scripts/test_release_surface.py::test_shebang_python_entrypoints_are_executable

ADDED FAILING TESTS    (rev3 − base)   = ∅        0
REMOVED FAILING TESTS  (base − rev3)   = ∅        0
SHARED FAILING TESTS                   = 7
```

**SAME-REASON: PASS, 7/7.** Each failing test's full failure block was compared between the tips
after normalizing only the worktree root, temporary directories, `line <N>`, addresses and elapsed
times. **No assertion text was normalized**, so a changed reason could not be normalized into
agreement. All seven blocks are byte-identical after that substitution — including
`test_release_surface.py::test_shebang_python_entrypoints_are_executable`, whose assertion carries
the list of non-executable entrypoints: the list is the same at both tips, so the candidate's two
new `755` files neither joined it nor displaced anything from it.
`test_release_runner_verdict.py` fails at both tips on the same missing registration,
`governance/scripts/test_candidate_content_hash.py` — a pre-existing debt of another candidate,
untouched here. The new suite **is** registered and runs green inside the battery.

**M-1: PASS.**

---

## 5 · M-2 — the reported defect is CLOSED, and the guarantee that replaced it is not true.

### 5A · The old defect, reproduced at revision 2

```
rev 2 tool · rev 2 spec · output/renders/smuggled.md = a byte copy of
framework/protocols/controlled_benchmark_ab.md (a forbidden prior-output path, 18 identifier hits)

  verify --post-read  →  VERDICT: PASS   rc=0
                         [BLIND SPOT] …/deepdive_manifests/PMID42397075.json   ← "size 1"
                         no NOT ALLOWLISTED · no IDENTIFIER LEAK · no PRIOR OUTPUT
```

Reproduced exactly as `REV-SCIAB-MIRROR-002` recorded it.

### 5B · Revision 3 closes it, and the closure survives twenty-two hostile cases

Every case below was run against the built pair at the content tip and **asserts the printed
reason**, never the exit code alone.

```
02  forbidden markdown at output/renders/smuggled.md      rc=1  NOT ALLOWLISTED + IDENTIFIER LEAK
03  CONTROL same bytes at …/fulltext_dossiers/NOTES.md    rc=1  NOT ALLOWLISTED + IDENTIFIER LEAK
04  legitimate binary render                              rc=0  PASS, named [UNCHECKED]
07  UTF-8 BOM text under the prefix (decodable)           rc=1  NOT ALLOWLISTED
12  renamed markdown wearing .png (decodable)             rc=1  NOT ALLOWLISTED
13  decodable .csv under the prefix                       rc=1  NOT ALLOWLISTED
14  zero-byte file under the prefix                       rc=1  NOT ALLOWLISTED
16  decodable file in a nested dir under the prefix       rc=1  NOT ALLOWLISTED
17  prefix-adjacent output/renders_extra/                 rc=1  NOT ALLOWLISTED
18  symlink under the prefix → prior output               rc=1  SYMLINK
22  non-blind forbidden path present post-read            rc=1  PRIOR OUTPUT
19  hostile file BESIDE a legitimate render               rc=0  PASS, both named, census = 4
20  declared output full of prior output                  rc=0  PASS, named "declared output, present"
21  blind-spot path occupied                              rc=0  PASS, named "blind-spot path, PRESENT"
01  clean pair                                            rc=0  PASS, [UNCHECKED SURFACE] 0
                                                                      22 / 22
```

Differential against revision 2's tool on the same states: `smuggled.md` PASS→FAIL, the renamed
`.png` PASS→FAIL, and the UTF-16 case PASS→PASS-but-now-**named**. The discrimination is in the
tool.

### 5C · M-3 (BLOCKING) — the census omits a class, and three artifacts say it does not.

Revision 3 makes a new claim in three places. In the tool's `VERDICT: PASS` line:

> *"…**every file whose bytes this tool could decode was scanned**, and none leaked an identifier."*

In the tool's closing census line:

> *"`[UNCHECKED SURFACE] n present file(s)`, each named above. **That is the whole of it**: every
> other present file took the allowlist check, the forbidden-path check and — **where its bytes
> decode — the identifier scan**."*

And in `controlled_benchmark_ab.md`'s normative guarantee table, in bold:

> `verify --post-read` … *"**every present file whose bytes decode was scanned, and the ones that
> were not are printed by name under `[UNCHECKED]`**"*

**All three are false on a clean build, before any reader exists.** The content scan skips a file
on four conditions, and the census enumerates only the first:

```python
if args.post_read and _is_expected_output(rel, spec, path):  continue   # ← census: 3 populations
if rel in exempt or not rel.endswith(suffixes):              continue   # ← census: nothing
try:    text = path.read_text(encoding="utf-8", errors="strict")
except (UnicodeDecodeError, OSError):                        continue   # ← census: prefix only
```

Measured from the tool's own predicates on the pair built at the content tip:

```
present files that DECODE as UTF-8, are NOT scanned, and are NOT named under [UNCHECKED]
scientist-a  10        scientist-b  10

  ASSIGNMENT.md · CLAUDE.md · benchmark/BENCHMARK_INSTRUCTIONS.md ·
  benchmark/MODE_DIRECTIVE.md · benchmark/OUTPUT_SCHEMA.md ·
  files/fulltext/PMID42397075_Aqeilan2026_fitz.txt        (content_scan.exempt_surface_paths)
  output/.gitkeep · output/renders/.gitkeep ·
  …/deepdive_manifests/.gitkeep · …/fulltext_dossiers/.gitkeep   (suffix outside text_suffixes)
```

**Reproduced with the control that makes it a hole rather than a design.** The identical bytes —
the whole of `framework/protocols/controlled_benchmark_ab.md`, a forbidden prior-output path with
18 identifier hits — appended at four paths in both surfaces, `verify --post-read` at the content
tip:

```
CLAUDE.md                     → VERDICT: PASS  rc=0   no finding · not named · [UNCHECKED SURFACE] 0
benchmark/MODE_DIRECTIVE.md   → VERDICT: PASS  rc=0   no finding · not named · [UNCHECKED SURFACE] 0
roles/scientist.md   CONTROL  → VERDICT: FAIL  rc=1   IDENTIFIER LEAK, 18 hit(s)
output/renders/smuggled.md    → VERDICT: FAIL  rc=1   NOT ALLOWLISTED + IDENTIFIER LEAK, 4 findings
```

`freeze` does not compensate. On the tampered `CLAUDE.md` tree it reports `unexpected 0` and
`UNEXPECTED_FILE_SET: []`, exactly as it reported `role: "output"` for `smuggled.md` at revision 2.
Two instruments and one normative table, one silent class — the same three-artifact shape that
made `M-2` blocking one revision ago.

**Why this is blocking and not a note.**

1. It is a **regression in the truth of a PASS sentence, introduced by M-2's remedy.** Revision 2
   printed *"no identifier leak in a scanned file"* — modest and true. Revision 3 replaced it with
   a stronger sentence that the tool does not establish. The candidate's own method is *"take the
   tool's PASS sentence literally and construct the cheapest state that makes it false while the
   tool still prints it"*; I constructed it, and the tool still prints it.
2. It is the **same finding class**, on the same seam — what is exempted, and whether the exemption
   is enumerated. `REV-SCIAB-MIRROR-002` rejected *"accept M-2 as a carried debt"* on the ground
   that a false sentence in normative text about what an instrument guarantees is what a reviewer
   is told to trust instead of the author's account. That reasoning applies here unchanged, and
   applying a weaker standard one revision later would be the ratchet failing rather than the
   candidate improving.
3. The candidate's **own suite normalizes it**, which is `L-1` a second time. §4.5's guarantee is
   asserted by `test_the_census_names_every_unchecked_file_and_counts_them`, docstringed *"the
   guarantee, as an assertion: the printed list IS the unchecked surface."* Its fixture declares
   **five** `exempt_surface_paths`, all decodable and all present, and the assertion excludes them
   from the census it calls the guarantee. It is the render fixture one row over: a positive
   assertion of what *correct* looks like, containing the gap.

**Steelman, and why it does not dissolve the finding.** The narrow formulation in §4.5 — *"no
present file is skipped by **both** the allowlist check and the identifier scan"* — **survives**,
because an allowlisted input is passed by the allowlist check rather than skipped by it. I say so
plainly. But the candidate does not print the narrow formulation; it prints two broader ones and
carries a third in the normative guarantee table, and those are what a reviewer reads. The
exemption is also genuinely narrower than the render prefix — a closed, declared, reviewable list
that no new path can enter without a spec change — and the exposure is bounded by the same J.0
residual that bounds M-2: the bytes must arrive during the reading, which already means the reader
read outside the surface. **The contamination capability is not new. The census is wrong, and it
is wrong in the revision whose whole purpose was to make it right.**

**Remedy, and the machinery already exists.** Either (i) add the two missing populations to
`unchecked_surface()` — `scan_exempt_present_input` and `suffix_not_scanned` — so the printed list
is the whole of it and the three sentences become true; **or** (ii) restore revision 2's true,
weaker wording in all three places and declare the exempt input paths as a named residual.
Whichever is taken, extend `test_the_census_names_every_unchecked_file_and_counts_them` so its
fixture's five exempt paths are part of the assertion rather than silently excluded from it — that
is the negative control it currently lacks. Independently of the census, `build --emit-digests`
already writes per-file input digests that nothing consumes: having `verify` compare an allowlisted
input against them would close the input half of this at no cost to the sentence (recorded as P-4).

**M-2: PASS on the reported defect · M-3: FAIL.**
**UNENUMERATED / SILENT SURFACE: FOUND — 10 present files per surface, on a clean build.**

---

## 6 · NON_UTF8_RENDER_RULE — CONTAINED

The premise *"fails UTF-8 decoding ⇒ legitimate render"* is **false**, and the protocol does not
claim it. What it claims is that such a file is **named**. Tested against the transformation the
review asks about:

```
UTF-16LE + BOM prose of a forbidden path      → expected-output status, PASS, NAMED [UNCHECKED]
UTF-16BE prose, no BOM                        → expected-output status, PASS, NAMED
CP1252 / Latin-1 prose                        → expected-output status, PASS, NAMED
a real PDF                                    → expected-output status, PASS, NAMED
arbitrary binary                              → expected-output status, PASS, NAMED
PNG header + forbidden prior-output bytes     → expected-output status, PASS, NAMED
UTF-8 BOM text · zero-byte · .csv · renamed
  markdown · decodable nested file            → NOT ALLOWLISTED, rc=1
freeze: UTF-16 prose under the prefix         → OUTPUT_FILE_SET (the declared cost)
freeze: decodable text under the prefix       → UNEXPECTED_FILE_SET
freeze: a real binary render                  → OUTPUT_FILE_SET (positive control, unmoved)
```

**So yes: a scientifically meaningful prior-output artifact CAN be re-encoded into non-UTF-8 bytes
and obtain "expected render" status.** It cannot do so *silently* — every such file is printed by
name with the reason *"under a declared output prefix and not decodable as text; its content was
not scanned"*. A reviewer reading that line cannot tell a PNG from UTF-16 prose, and the tool does
not claim to; it enumerates, and enumeration plus the freeze receipt is what the protocol's own
guarantee table promises. The instructions state the rule to the reader **in §1, before the
reading**, which I verified is the only paragraph added to `BENCHMARK_INSTRUCTIONS.md` at this
revision.

**No scientific functionality is lost.** A reader that renders pages writes pixels; the fourteen
probes and my twenty-two show every legitimate render passing and being named, and the one thing
now refused under the prefix — a decodable text file — is a thing the instructions tell the reader
not to write there.

`NON_UTF8_RENDER_RULE: CONTAINED` — safe within its declared claim, and the declared claim is
narrower than "renders are validated". This is **not** the reason for the verdict; `M-3` is.

---

## 7 · Carried findings — classified, none allowed to overclaim closure

| # | Plan's class | Mirror's finding at revision 3 |
|---|---|---|
| **N-1** | CARRIED | **NON-BLOCKING CARRIED.** `surface_spec.json` `notes` (6) and the File012 `_note` still contradict each other about label normalization; untouched, correctly declared. |
| **N-2** | CARRIED — REAL | **NON-BLOCKING CARRIED. Reproduced at revision 3, unchanged:** File011 (seven real units) falsely declared empty → the population drops **65 → 58**, `rc=0`, no finding. It does **not** invalidate the frozen population: I read File008 independently — 1 page, 256 characters, a CRediT author-role list, zero `Figure` / `Table` / `Supplementary Fig` keys, the single `Method` hit being the word *Methodology:* in that list. The one declared entry is genuinely empty. The finding goes live the moment a second entry is added. |
| **N-3** | CARRIED — LATENT | **NON-BLOCKING CARRIED.** Untouched; no caption in this packet crosses a page break. |
| **N-4** | FIXED | **RESOLVED.** §3G now reads 65 units / 109 panels with the superseded pair named as superseded. |
| **N-5** | FIXED | **RESOLVED.** §5 now reads six suites and seven tests. |
| **N-6** | CARRIED — DECLARED | **NON-BLOCKING CARRIED.** `test_an_invalid_first_pass_state_refuses` now refuses through `argparse` `choices` with a specific reason (*"invalid choice: 'DEFINITELY_DONE' (choose from …)"*) — an exit-code-only assertion whose property nevertheless holds for the right reason. Not load-bearing. |
| **N-7** | RECORDED, NOT RECONCILED | **UNRESOLVED, and honestly labelled.** Revision 3 did not re-run revision 1's tool and neither did I; the conclusion those counts support is unaffected either way. |
| **N-8** | CARRIED — CONTAINED | **NON-BLOCKING CARRIED. Reproduced at revision 3:** `locators` returns `VERDICT: PASS`, `rc=0` on an entry citing `output/renders/innocent.png` whose realpath is prior LEGEND output, while the same tool rejects a direct citation (`FORBIDDEN SOURCE`), an absolute path (`ABSOLUTE PATH`) and a `..` traversal (`TRAVERSAL`), and the positive control passes at `rc=0`. `verify` reports the symlink (`rc=1`) and `freeze` refuses the tree (`rc=2`). **M-2's change does not reach `locators`, and the manifest is right to say so** — claiming otherwise would have been the overclaim M-2 is about. |
| **N-9** | CARRIED | **NON-BLOCKING CARRIED.** The `REFUSES` / `exits 1` vocabulary mismatch is untouched. |
| **R-1 … R-12** | (revision 1) | Not reopened. The files carrying R-1…R-5, R-7, R-8, R-11 and R-12 are byte-identical to revision 2 by blob sha; R-6 and R-9 remain resolved by B-1; **R-10 is still Mirror's own worktree debt and moved a number in this review again** (§0). |

**None is falsely marked resolved. None becomes blocking through revision-3 behaviour.**
`N-2` does not invalidate the benchmark population; `N-8` does not invalidate post-read isolation.

---

## 8 · Non-regression of stabilized properties — targeted, on byte-identity plus binding

Fourteen of revision 2's nineteen content files are **byte-identical at revision 3 by blob sha**,
and the binding proves no other content moved. Where a row rests entirely on those files, a
targeted confirmation is recorded rather than a re-derivation; where revision 3 touched the file,
the row was re-measured.

```
B-1 SCIENTIFIC POPULATION  PASS       re-derived ×2, byte-identical to each other and to the
                                      tracked evidence_units.json · 65 units · 109 panels ·
                                      6 main_figure · 7 main_results · 2 main_methods ·
                                      10 supplementary_figure · 24 supplement_methods ·
                                      7 supplement_table · 9 source_data_blot · 1 declared empty
B-3 FREEZE RECEIPT         PASS       see §9
B-5 SEVEN BENCHMARK FIELDS PASS       OUTPUT_SCHEMA.md byte-identical; the eight bold labels are
                                      present at §3 lines 99–107; the registry count at BASE_HEAD
                                      re-measured independently: 0/39, 0/39, 0/39, and
                                      **Evidence boundary:** 5/39 — the withdrawn premise stays
                                      withdrawn with its measurement beside it
MODE A/B TASK SCOPING      PASS       scientist_reading_modes.md byte-identical; the A→MODE A /
                                      B→MODE B fixing is scoped to BENCH-AB-001 by name, rotation
                                      is Orchestrator's per task, and Mirror's anti-fossilization
                                      guard is named beside it (§32)
ACTOR EQUIVALENCE          PRESERVED  §32 reproduced in the protocol (l.24, l.38) and in
                                      roles/scientist.md (l.20); the protocol states it
                                      interprets §32 and does not modify it (l.525)
C-2 FORWARD OWNERSHIP      PASS       byte-identical; ownership going forward is the OWNER of the
                                      Task Contract, and who that is remains Orchestrator's
INPUT PARITY               PASS       5 negatives, each on the reason: PARITY BROKEN ·
                                      NOT DIFFERING · ABSENT · NOT ALLOWLISTED · IDENTIFIER LEAK
SCIENTIFIC DEPTH           PRESERVED  no MODE file, no assignment, no population file changed;
                                      the only reader-facing addition is the render rule, which
                                      removes no coverage and is stated before the reading
NO PARALLEL CLAIM SCHEMA   NONE       3 grep hits over the whole content diff, each read at
                                      source, each a prohibition (OUTPUT_SCHEMA §6 l.190,
                                      BENCHMARK_INSTRUCTIONS l.88, scientist_reading_modes l.514)
ACTOR REGISTRATION         PASS       byte-identical; ACTOR_ID ≠ SESSION_REF stated with its
                                      consequences; no session ref is invented in the content
CANONICALIZATION DEP.      CONFIRMED  measured at both tips: scientist 355e3529… → 82423a48…,
                                      plan / mirror / orchestrator byte-identical. Plus the
                                      PROPOSED status line, the UNRESOLVED contract owner, and
                                      L2 suspended. Ground 3 stays marked ⚠️ as the weakest
PUBLICATION GATE           PASS / BLOCKS 0 at BASE_HEAD and at the content tip; the [REVIEW] rows
                           are identical at both and pre-existing
LINT / receipts / anchors  PASS (1 pre-existing INFO) · OK 128 chained, tail anchored · PASS
```

---

## 9 · FREEZE RECEIPT — PASS

Fourteen cases at the content tip; thirteen assert a reason string, the fourteenth is the silent
class of §5C.

```
honest tree: 5 declared outputs + a binary render     outputs 6 · unexpected 0 · 29 fields
                                                      NO machine-specific absolute path (measured)
decodable text under output/renders/                  UNEXPECTED_FILE_SET ['output/renders/smuggled.md']
a real binary render                                  OUTPUT_FILE_SET — the positive control, unmoved
UTF-16 prose under the prefix                         OUTPUT_FILE_SET — the declared cost of the rule
freezing A's tree as scientist-b                      rc=2, names 'scientist-a' from ASSIGNMENT.md
wrong benchmark id                                    rc=2
invalid first-pass state                              rc=2, names the invalid value and the choices
a symlink present in the tree                         rc=2, SYMLINK
one edited byte after the freeze                      rc=1, names roles/scientist.md
equal-count substitution after the freeze             rc=1
a file added after the freeze                         rc=1
a file removed after the freeze                       rc=1
a receipt pointed at the other actor's tree           rc=1
POSITIVE CONTROL untouched tree                       rc=0
tampered scan-exempt allowlisted input                rc=0 · unexpected 0   ← §5C, silent
```

Freeze remains sound on every property it claims, and shares `_is_expected_output` with `verify`
deliberately, so the two cannot disagree about which files are renders. It inherits §5C's blind
class for the same reason.

**FREEZE RECEIPT: PASS.**

---

## 10 · SLR-plan-0003 — BOUND, and curated under Annex E.2

### 10.1 · Procedural integrity — PASS

```
belongs to this session/candidate   task SCIENTIST-AB-SPEC-001 · directive v1 · generation 3 ✓
is CONTENT                          learning/plan/ is under no CONTROL_PLANE_ROOT; P5.1 declares
                                    learning/ CONTENT by intent ✓
included in the authoritative hash  it is the SINGLE content-domain entry separating
                                    7cef4ccc… (523) from 570fcbbb… (524) ✓
pre-SLR rev-3 hash superseded       SUPERSEDED_REV3_TIP b634829 / SUPERSEDED_REV3_HASH 7cef4ccc…
                                    declared in §1 with its reason; reproduced by me ✓
the population that proceeds        yes — the reviewed content tip a3cad1d IS the tip carrying it ✓
```

**Attacking §4.1b's reading.** Body §15 reads *"Ogni sessione significativa MUST chiudersi con
Session Learning Review"* — the trigger is session closure, as claimed. Annex E.6 persists it by
`WORK_COMMIT` at milestone granularity. P5.1 makes it content. Annex D.2 binds an approval to
`CANDIDATE_CONTENT_HASH + BASE_HEAD`. Together they do order the record **before** review — but
only given an unstated fourth premise: *that this session's only durable branch is the candidate
branch*. Mirror's own records take the other route (`learning/mirror/` on a non-candidate branch,
where a `WORK_COMMIT` moves no candidate hash). Plan has no such branch and inventing one would
be a governed change, so the conclusion holds for Plan — but the argument is one premise short of
the general claim it makes. Recorded as `P-2`, non-blocking. The two precedents are real and I
verified them: `05cdeda` (SLR-plan-0001) and `b9af54e` (SLR-plan-0002) are **both reachable from
`main`**, and `b9af54e`'s message carries the quoted sentence verbatim. Declaring `learning/` a
control-plane root to dodge the hash move is forbidden by P5.1 and was correctly not done.

**SLR-plan-0003: BOUND.**

### 10.2 · Epistemic curation (Annex E.2)

The vocabulary below is the repository's, not a reviewer's coinage: `CONFIRMATION_CLASS ∈
{ORIGINAL_OBSERVATION, REPLICATION, EXPOSURE_AFTER_BROADCAST}`; the §15 outcome classes; the E.1
status machine; and E.2's own conflict mechanism, *"Conflitti → Mirror aggiudica → SUPERSEDED
motivato"*. **No `LEARNING_INDEX` file exists** — E.2 names the instrument and Plan owns its
durability — so this curation is recorded here and in `SLR-mirror-0011`, and cannot be written
into an index that does not exist. That debt is Plan's, declared, and unchanged.

Every `CONFIRMATION_CLASS` in the record is marked *proposed*, and the record says E.2 gives
curation to Mirror. That is correct, and it is the behaviour E.2 exists to produce.

**L-1 — *a positive control can assert the defect as the correct behaviour*.**
`CONFIRMATION_CLASS: ORIGINAL_OBSERVATION` — **accepted**, verified at source: revision 2's
`_plausible_reading()` wrote `output/renders/fig1.md`, a markdown file under the render prefix,
as one of the four things an honest reader leaves behind, and
`test_positive_control_an_honest_reading_passes_post_read` asserted it passes.
`CLASS: FAILURE_PATTERN` — **accepted**.

On the general-versus-narrow question the review poses: **the general statement stands, and the
evidence for it is now two sightings, not one.** I add `CONFIRMATION_CLASS: REPLICATION` (actor
`mirror`, this session) on an independent instance *inside revision 3 itself* —
`test_the_census_names_every_unchecked_file_and_counts_them`, docstringed *"the guarantee, as an
assertion"*, whose fixture declares five decodable `exempt_surface_paths` and whose assertion
excludes them from the census it calls the guarantee (§5C). `EVIDENCE_COUNT: 2`, both in the first
two classes, so E.2's threshold for **BEST_PRACTICE_CANDIDATE** is reached without my validation.
One formulation inside the record is **SUPERSEDED, with reason**: the closing sentence *"the answer
is one line — bytes instead of text — and the answer is now in the fixture"* is true of the render
fixture and false as a closure of the pattern; repairing the instance did not repair the class,
and the class recurred in the same file at the same revision.

**L-2 — *a false census can be repaired in two directions, and only one keeps the capability*.**
`ORIGINAL_OBSERVATION` — accepted. `CLASS: MICRO_UPGRADE` — accepted. `STATUS: LOCAL`
(one sighting, no second confirmation, and I do not offer Mirror validation for it). The
observation is correct and I confirm the direction taken was the capability-preserving one:
narrowing the prefix to undecodable bytes is measurably stronger than declaring the prefix blind,
and §4.5 now names the rejected alternatives where a reviewer can disagree. Its own commitment —
*state both repair directions and say which was taken* — is precisely what §5C now needs applied
one level down.

**L-3 — *the cheap repair and the correct repair produce the same green test*.**
`ORIGINAL_OBSERVATION` — accepted. `CLASS: MICRO_UPGRADE` — accepted. `STATUS: LOCAL`. Confirmed by
measurement: I verified independently that §5.1 is a real obligation with a consequence and not a
token, that `EXEMPT` gained no entry, and that the guard is byte-identical to `main`. The record's
claim that the test cannot distinguish the three closures is correct — the guard is a substring
test — and its conclusion that the judgement must therefore be argued where a reviewer can attack
it is the right one.

**L-4 — *an accounting instrument needs its own falsifier*.**
`CONFIRMATION_CLASS: REPLICATION` of `SLR-mirror-0010` §1 — **accepted, and correctly self-classed
rather than claimed as original.** Its addition is real and I tested for exactly the failure mode
it names: my harness parses subTest failures, `ERROR` entries and the case of a suite exiting
non-zero with no reported test failure, and that last population is **empty at both tips** — so
`ADDED = 0` is not true by omission. Its declared limitation is accurate and material: the harness
is not committed, so §4.2's numbers are reproducible only by re-authoring an equivalent
instrument, which is what I had to do. That is a real limitation of this revision, correctly named
by its author before a reviewer named it.

**L-5 — *I proposed to defer an obligation the repository had already answered*.**
`ORIGINAL_OBSERVATION` — accepted. `CLASS: FAILURE_PATTERN` — accepted. The precedent claim is
verified at source (`05cdeda`, `b9af54e`, both reachable from `main`; the quoted commit sentence is
verbatim).

The generalisation carries two clauses and they do not share a fate.

- *"before treating a durable obligation as deferrable, look for whether the repository has
  already discharged it, because precedent is durable state and my reading of a clause is not"* —
  **accepted as stated.** It is supported by the instance, it is operative, and its check is one
  command.
- *"A rule's inconvenient consequence is evidence you have understood the rule, not grounds for
  postponing it"* — **SUPERSEDED, with reason.** One instance does not carry a general maxim, and
  as a maxim it is false: P5.1 itself provides that the admissible response to an inconvenient
  domain rule is a **governed change to the rule**, reviewable as such — *"never an ad-hoc
  exclusion made while preparing a candidate"*. The distinction the instance actually supports is
  between a *governed change* and a *silent deferral*, not between compliance and complaint.

**REFINED_FORMULATION (L-5):** *before treating a durable obligation as deferrable, inspect
applicable precedent and the bindings its discharge would move; where the consequence is genuinely
unacceptable the admissible response is a governed change to the rule, never a silent deferral of
the obligation.* With one `ORIGINAL_OBSERVATION` plus this Mirror validation, the **narrowed
formulation only** reaches E.2's `BEST_PRACTICE_CANDIDATE` threshold. The general maxim does not.

**Cross-cutting.** The record's own synthesis — *the correct-looking option and the correct option
produced the same observable, and I chose by cost* — is accepted and is the most useful sentence
in it. §5C is its fourth instance, and the one the record could not contain because it was written
before the census was reviewed.

**G.2.** This curation is of Plan's learning, which is squarely E.2 work and squarely Mirror's. It
ratifies nothing of Mirror's own methodology. The one methodological observation this session
produced about Mirror's own harness (§12) is recorded as a LOCAL learning in `SLR-mirror-0011` and
is **not** self-ratified; if it is to become a rubric change it goes the G.2 route —
`MIRROR_UPGRADE_PROPOSAL` → Plan candidate → an independent reviewer chosen by Orchestrator.

---

## 11 · Recorded findings from this review — non-blocking

- **P-1** The guard behind `M-1` cannot see the newest reading route's actual instruction files.
  `INSTRUCTION_SURFACES` globs cover `framework/protocols/*.md` and `.claude/skills/*/SKILL.md`
  but not `framework/eval/benchmarks/*/instructions/*.md`. Three of the new files there trip the
  guard's markers and carry no `verbatim_locators` token: `BENCHMARK_INSTRUCTIONS.md` (4 markers),
  `MODE_A.md` (1), `MODE_B.md` (1). **This is not a candidate defect** — the obligation is
  semantically carried in all three, `OUTPUT_SCHEMA.md` carries the literal token, and the guard's
  globs are `BASE_HEAD`'s and unchanged. But this candidate is the first to put an instruction
  surface in a directory the guard does not scan, and the next one will not be noticed. The guard's
  owner should widen the glob or declare the directory out of scope with a reason.
- **P-2** §4.1b's ordering argument is sound for Plan and one premise short of the general claim
  it makes; the missing premise is that Plan's only durable branch is the candidate branch. Mirror
  takes the other route for the same obligation. Stating the premise would make the precedent
  transferable instead of apparently universal.
- **P-3** `N-6`'s three exit-code-only assertions still fire for the correct reason at revision 3;
  `test_an_invalid_first_pass_state_refuses` now refuses through `argparse` `choices` with a
  specific message. The declaration stands and none is load-bearing.
- **P-4** `verify` never compares an allowlisted input's bytes to anything, while
  `build --emit-digests` already writes exactly that record and nothing consumes it. Parity
  between the two surfaces does not detect a change applied identically to both — which is how
  §5C's input half is reachable. Cheapest available closure of half of `M-3`.
- **P-5** `N-7` remains unreconciled. Revision 3 did not re-run revision 1's tool and neither did
  I; both of us record it rather than settle it, which leaves a measured number and an inferred
  explanation still facing each other.

---

## 12 · EVIDENCE_FOR · EVIDENCE_AGAINST · ALTERNATIVES · KEY_OBJECTIONS

**EVIDENCE_FOR.** The binding reproduced eight times, four of them without the script, with three
published control values from earlier tips; `M-1` closed semantically rather than lexically, with
the guard untouched and the delta zero at test-method granularity over seven shared failures whose
reasons are byte-identical; the reported `M-2` defect closed against twenty-two hostile cases,
each asserting a reason; freeze sound on thirteen tamper classes with no absolute-path leak; the
population re-derived byte-identically to the tracked file; parity, gate, lint, receipts, anchors
and fingerprints all green; the Session Learning Record correctly bound, honest about its own
session's failure, and offering its classes for curation rather than asserting them; no scope
creep; every carried finding named and none falsely closed.

**EVIDENCE_AGAINST.** `M-3`, reproduced with a same-bytes control across four paths — two caught,
two silent — and confirmed independently against the tool's own predicates on a clean build, where
ten present files per surface decode and are neither scanned nor named while two printed sentences
and one normative guarantee table say otherwise.

**ALTERNATIVES_CONSIDERED.** (i) *Accept, carrying `M-3` as a recorded finding* — rejected: it is
a false clause in a normative guarantee table and in the tool's own PASS output, which is the
exact ground on which `M-2` was found blocking one revision ago, and the remedy is the same size.
(ii) *Treat `M-3` as pre-existing* — rejected: the scan exemption is pre-existing, but revision 3
replaced revision 2's true sentence (*"no identifier leak in a scanned file"*) with a false one and
added the census that claims completeness. Both claims are new at this revision. (iii) *Treat
`M-3` as covered by the narrow §4.5 formulation* — accepted in part and rejected in part: the
narrow sentence does survive and I say so, but it is not the sentence the tool prints or the
protocol tabulates. (iv) *Fold `M-3` into `M-2` and call `M-2` unclosed* — rejected: the reported
`M-2` defect is genuinely closed and it would be inaccurate to say otherwise; `M-3` is a distinct
finding of the same class introduced by its remedy, and the distinction matters to whoever reads
the next revision.

**KEY_OBJECTIONS Plan may raise, and my answer.**
*"The §4.5 guarantee is literally true, so nothing is false."* — The §4.5 guarantee is true and I
record it as true. Three other sentences, two of them printed by the tool on every run and one of
them the normative guarantee table, say something stronger and false. A reviewer reads what is
printed.
*"The exempt paths are a closed declared list, unlike a prefix."* — Agreed, and it is why the
remedy is small: the census can name a closed list exactly.
*"The exposure is bounded by the J.0 residual already declared."* — Agreed, and identically true of
`M-2`. The finding is not the exposure; it is the census, and three artifacts assert it is
complete.
*"Revision 3 was scoped to M-1 and M-2; M-3 is new scope."* — `M-3` is inside `M-2`'s own remedy
and inside the guarantee sentence that remedy introduced. It is not new scope; it is the remedy
measured.

---

## 13 · VERDICT

```
Annex C.2 VERDICT       REFINED — M-1 is closed on the semantics and not only on the token, the
                        reported M-2 defect is closed against a hostile battery that could not
                        break it, and the sentence written to describe the fix is false in the
                        same way the sentence it replaced was.
REFINED_FORMULATION     "verify --post-read names every present file it skipped" is true of three
                        populations and false of two more: the declared scan-exempt inputs and the
                        files whose suffix is outside text_suffixes. Ten present files per surface,
                        on a clean build, before any reader exists.
MIRROR_REVIEW           REQUEST CHANGES
REVIEWER_CONFIDENCE     high on M-1 (isolated at both tips, guard diff empty, delta and reasons
                        re-derived with an independent harness whose omission channel is empty)
                        high on M-2's closure (22 hostile cases, each on the reason, plus a
                        differential against revision 2's tool)
                        high on M-3 (measured from the tool's own predicates on a clean build,
                        and reproduced with the same bytes at four paths — two caught, two silent)
RESIDUAL_UNCERTAINTY    N-7 is still unreconciled and I did not settle it either. M-3's exposure is
                        bounded by a residual the candidate already declares, and I may weigh a
                        false PASS clause more heavily than the operator would — I weigh it as
                        REV-SCIAB-MIRROR-002 weighed the identical clause one revision ago, and
                        that consistency is the argument. The scan-exempt list is genuinely
                        narrower than a prefix, which makes M-3 smaller than M-2 in exposure and
                        identical to it in kind.
EVIDENCE_NEEDED         either the two missing populations added to unchecked_surface() and the
                        three sentences left as they are, or the three sentences restored to
                        revision 2's true weaker wording with the exempt inputs declared as a named
                        residual; plus the fixture's five exempt paths brought inside
                        test_the_census_names_every_unchecked_file_and_counts_them, which is the
                        negative control it lacks and the second instance of the candidate's own L-1.
WHAT_WOULD_CHANGE_MY_MIND
                        M-3: a run of `verify --post-read` over a surface whose CLAUDE.md holds
                             appended forbidden prior-output bytes that either reports a finding or
                             prints CLAUDE.md under [UNCHECKED] — it does neither, while the same
                             bytes at roles/scientist.md produce IDENTIFIER LEAK and at
                             output/renders/smuggled.md produce four findings;
                             or a reading of "every file whose bytes this tool could decode was
                             scanned" under which ten unscanned decodable files satisfy it.
                        M-1: the guard failing at cbce3016 in a clean worktree — it passes; or
                             evidence that §5.1 is a token rather than an obligation — it names the
                             field, the validator, the consequence and the scoring.
AUTHOR_RESPONSE         required (C.2); silence is not acceptance.
```

**HUMAN_APPROVAL: NONE — not granted, not recommended, not implied.**
**MAIN: cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED.**
**Nothing was executed, nothing canonicalized, no benchmark run, no registration performed, no
other actor's worktree written.**

---

## 14 · Scope, and what this review did not touch

**SCOPE CREEP: NONE.** The content diff touches no `*_current.md`, no registry, no approval queue,
no lease record, no `runtime/`, no Agent Card, no receipt ledger, no P7, no Metacognition surface,
no Scientist C, no second paper, and no session-routing artifact (measured: zero paths matching
`session|rout|registr` in the content diff). The only executable added reads none of them —
`agent_card` 0 · `_current` 0 · `registry` 0 · `lease` 0 · `approval` 0 · `watcher` 0; the single
`receipts` hit is a word inside a `FAILURE_MODE` string at line 695. Every carried debt is listed
unfixed, and `§5` of the manifest enumerates what the candidate does not do.

**SESSION-ROUTING DEBT: OUT OF SCOPE — NOT SILENTLY RESOLVED.** §5c names the gap between stable
`ACTOR_ID` and current routable `SESSION_REF` and implements nothing. This review implements
nothing either, declares no `SESSION_REF` for itself, and infers no routing from chat recency.

---

## 15 · Provenance of this review

Detached scratch worktrees created with `git worktree add --detach`: `wt-base` at `cbce3016`,
`wt-cand` and `wt-surf` at `a3cad1d`, `wt-rev2` at `daaa3335`. Neither regression worktree holds
`files/` at either tip. The packet was copied read-only from root `files/fulltext/` into `wt-surf`
and `wt-rev2` only, digests **7/7** equal to the manifest. Both surface pairs were built into the
session scratchpad; every attack surface is a copy under it. All binding numbers were computed in
a worktree carrying `BASE_HEAD`'s script and P5 v4, never in this branch's checkout, which carries
P5 v3 (R-10). The session guard refused one heredoc write while the shell was inside a repository
worktree; I did not reach for an unchecked tool — the probe was authored with `Write` into the
scratchpad and invoked by name, and the measurement is the same one. Time source: the runtime
exposes no wall clock beyond the date. Governance loaded 3.1.1; the mirror fingerprint is identical
at `BASE_HEAD` and at the candidate content tip.

**A wrong-reason pass, committed by this reviewer and caught by its own control.** My first `N-8`
probe reported 5/5 with the wrong CLI arguments — every case exited 2 from `argparse` and every
assertion on the exit code was satisfied. It was caught only because the battery requires its
positive control to exit **0**, and the control exited 2 with the rest. This is the third time this
harness has committed the defect it exists to find (`SLR-mirror-0010` §4 records the first two).
The rule that caught it — *a negative battery whose positive control does not pass is measuring the
invocation, not the tool* — is recorded in `SLR-mirror-0011` as a LOCAL learning and is **not**
self-ratified; if it is to bind, it goes the G.2 route.

**WRONG-REASON LOAD-BEARING PASSES in the candidate: 0.** Every probe added at revision 3 asserts
a reason string; the three pre-existing exit-code-only assertions (`N-6`) were re-verified to fire
for the correct reason and none is load-bearing.
