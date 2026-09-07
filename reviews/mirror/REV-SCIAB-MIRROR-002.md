---
artifact: MIRROR hostile review, revision 2 (Annex C.2)
review_id: REV-SCIAB-MIRROR-002
object: CAND-20260818-SCIENTIST-AB-SPEC rev 2 · CANDIDATE_CONTENT_HASH c0701094…21bcf @ base cbce3016
level: R4 (MIRROR_REQUIRED — role contract in CORE, two new protocols, MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here
date: 2026-08-19
supersedes: nothing. REV-SCIAB-MIRROR-001 stands as the review of revision 1 and is not amended.
verdict: REQUEST CHANGES — two blocking findings, both reproduced with controls; nine recorded
governance_loaded: 3.1.1 · mirror fingerprint 3dff8954…f65c, identical at BASE_HEAD and at the candidate tip
---

# Five findings closed, measured. Two survive: the delta is not zero, and the blind spot is not one.

Reviewed from `R-1`. Nothing transfers from `REV-SCIAB-MIRROR-001` — not a verdict, not a
finding, and none of the ten rows that review found acceptable. Every number below was
re-derived in detached scratch worktrees of `BASE_HEAD` and of the candidate content tip, never
in another actor's worktree and never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror      branch mirror · HEAD ff8b15cc · clean
ACTOR_ID          mirror · roles/mirror.md read in full · PERSISTENT_LEGEND_ACTOR
governance        3.1.1 · Annex C (C.1 ladder, C.2 format, C.3 discipline, C.4 objects),
                  Annex G (G.1 perimeter, G.2 self-upgrade bar, G.3 metrics), P5 read at BASE_HEAD
fingerprint       compose --role mirror  at BASE_HEAD cbce3016  3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                                         at content tip daaa3335  3dff8954…f65c — IDENTICAL
                  (this review is conducted under the governance the candidate is based on)
STABLE ACTOR IDENTITY   mirror · worktree mirror · roles/mirror.md
CURRENT SESSION ROUTING not durable in the repository. No SESSION_REF is declared for this
                  session and none is invented. An actor cannot observe its own routing reference.
authority         review of SYSTEM objects (C.4); MAJOR when in doubt (body §12); no command over
                  any actor; no primary evidence; may not grant HUMAN_APPROVAL (H.1: operator);
                  may not CANONICAL_BATCH_COMMIT (H.1: orchestrator); WORK_COMMIT only on branch
                  mirror under reviews/ · ledger/ · learning/
proposer≠reviewer≠executor   author plan · reviewer mirror · adjudicator operator — holds
G.2               not engaged: nothing in the candidate touches Mirror's rubric, clustering,
                  active-learning selection, review-yield or autonomy methodology
```

**MIRROR REHYDRATION: PASS.** No essential part of identity or authority depended on a prior chat.

> **Worktree debt, disclosed because it changed a number.** Branch `mirror` carries
> `governance/plan_defined_parameters.md` at **P5 v3** and `candidate_content_hash.py` in its
> pre-fix form, which reads P5 from the *working tree* instead of from the tip being hashed.
> Run in this worktree, that pair produces `02231e82…` for the candidate — a v3 prefix over a
> two-root domain. Every binding number in §1 was therefore computed in a clean detached
> worktree of `BASE_HEAD`, which carries the canonical script and P5 v4. This is `R-10` of
> revision 1, still Mirror's own debt, still not the candidate's.

---

## 1 · Binding — PASS

```
base cbce3016 · tip daaa3335 (CONTENT TIP)          c0701094da01e6eb13a69a2194e040327ad6d2b691a4b31d9a1fb29bcba21bcf
base cbce3016 · tip 90fcfa25 (LATEST MANIFEST TIP)  c0701094…21bcf   run 1
base cbce3016 · tip 90fcfa25                        c0701094…21bcf   run 2
base cbce3016 · tip 90fcfa25                        c0701094…21bcf   run 3
independent recomputation without the script
  (git ls-tree -r --full-tree + P5.2 serialization, v4, three roots, newline-terminated)
  at daaa3335   c0701094…21bcf   523 included · 27 excluded
  at 90fcfa25   c0701094…21bcf   523 included · 28 excluded   (+CHK-plan-0011, control plane)
main            cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED, merge-base of the branch
```

`90fcfa25` is the only commit after the content tip and touches exactly
`governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md`, `ledger/checkpoints/plan/CHK-plan-0011.json`
and `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` — all inside declared `CONTROL_PLANE_ROOTS`.
The invariance is measured at both points and by two independent routes. `MANIFEST_TIP` is
informational and the manifest is right about why.

**Content population, from Git, not from the report:** 19 content files (+4738/−1) · 4 control
plane · no deletion · no history rewrite · two mode changes, both new files
(`benchmark_input_surface.py`, `test_benchmark_input_surface.py`), no existing file's mode moved.
Classification: **NORMATIVE** 4 (`scientist_reading_modes.md`, `roles/scientist.md`, `BOOTSTRAP.md`,
`benchmark_input_surface.py`) · **BENCHMARK_PROTOCOL** 11 (`controlled_benchmark_ab.md`,
`surface_spec.json`, `benchmark_manifest.json`, `evidence_units.json`, instructions ×7) ·
**RUNTIME/TOOLING** 1 (`test_benchmark_input_surface.py`) · **DOCUMENTATION** 3
(`protocols/index.md`, `eval/README.md`, `run_release_regressions.py`) · **CONTROL PLANE** 4.
**Nothing unexpected.** No `*_current.md`, no registry, no receipt ledger, no governance text.

---

## 2 · STEELMAN (before the objections)

Revision 2 does the hard version of every remedy rather than the cheap one. The caption window is
not a bigger integer — it is *gone*, replaced by a bound at the next match of the rule's own
label, which is the axis that actually fails. The Methods list is not extended by four entries —
it is *deleted* and replaced by a typographic derivation, which then found a fifth thing Mirror's
own heuristic could not see. Four kinds of evidence that had no rule at all — Results headings,
main Methods, resource-table categories, uncropped blots — were given rules instead of being left
unmeasurable, and the one source that yields nothing is declared with its reason while the command
*refuses* a spec that leaves any packet source unaccounted for. The freeze receipt stopped taking
identity as free text and now reads it out of the tree and refuses a command line that disagrees.
The over-wide post-read skip was narrowed to the exact declared output set and the blind spot
became a computed, printed object. The B-5 refusal was withdrawn *against Plan's own earlier
position*, with the measurement that refutes it written into the schema. The wrong regression
claim of revision 1 is struck through rather than deleted. Forty-five adversarial probes were
written on the method that found the defects, run against the pre-fix tool as a differential
control, and two of the nine survivors were declared spurious by the author before any reviewer
asked. That is not remediation theatre; it is the behaviour the laboratory exists to produce.

What follows is where the artifact still says more than it ships — twice, both times at the same
seam: the granularity of a comparison, and the completeness of a declared blind spot.

---

## 3 · Population reviewed and tests executed

**Read in full:** the candidate manifest rev 2 (620 lines), the handoff, `scientist_reading_modes.md`,
`controlled_benchmark_ab.md`, `benchmark_input_surface.py` (1183 lines), `test_benchmark_input_surface.py`
(644 lines), `surface_spec.json`, `benchmark_manifest.json`, `population/evidence_units.json`,
the seven instruction files, the diffs to `roles/scientist.md`, `BOOTSTRAP.md`,
`protocols/index.md`, `eval/README.md`, `run_release_regressions.py`; at source: Annex C, Annex G,
`plan_defined_parameters.md` P5, `claim_registry_current.md` at `BASE_HEAD`,
`scripts/test_locator_obligation_reaches_every_route.py`, the packet (7 files, digests 7/7 equal
to the manifest), and File008–File012 + the main PDF via PyMuPDF.

**Executed** — scratch worktrees `wt-base`/`rg-base` = `cbce3016`, `wt-cand`/`rg-cand` = `daaa3335`;
the regression worktrees hold **no `files/`** at either tip, so the environmental confound of
revision 1 cannot arise:

```
binding                    4 runs + 2 independent recomputations                        PASS
population ×2              byte-identical to each other AND to the tracked file
                           (sha256 b41c7b9f…) · 65 units · 109 panels                    PASS
captions, read verbatim    Fig 1 A–F(6) · Fig 2 A–F(6) · Fig 3 A–L(12) · Fig 4 A–J(10)
                           Fig 5 A–G(7) · Fig 6 A,B,C,D,E(5, range C-D expanded)         = 46
                           Supp 1 A–I,K,L,M(12) 2(5) 3(5) 4(10) 5(3) 6(6) 7(7) 8(6)
                           9(3) 10(6)                                                    = 63
segment partition          Fig 2 span 80141..81076 ends exactly at Fig 3's start;
                           every caption span is bounded by the next match, none by an integer
typography, File009        Bold 15.96 between 'Materials and methods'(18.0) and
                           'References'(15.96 by name) = 25 lines → 24 headings, the
                           'Library preparation … (10x' + 'Chromium)' pair joined       matches
typography, main PDF       Aptos Display 15.77 in Results scope = 11 lines → 7 headings
                           (four wrapped, joined); in Methods scope = 2                 matches
File011                    Bold 8.04 centred x≈291.4 from p2 = 7; column headers at
                           x≈112/302/467 excluded by geometry                           matches
File012                    10 label hits, 'Supplementary Fig. 1J' twice (p3,p4) → 9 units matches
File008                    1 page, CRediT author-role list, no figure/table/method/datum  declared empty, correctly
completeness refusal       File011 removed from sources → [BLOCK] UNACCOUNTED SOURCE, rc=1
                           same source DECLARED empty → rc=0, 58 units                  POS control
B-4 battery (13 cases)     12 caught with the correct reason code; 1 not — see M-2
B-3 battery (13 cases)     13/13, each on the reason, not only the exit code
locators battery (8 cases) 7/7 substantive; 1 lexical-only residual (N-8)
suite, at the candidate    45 tests, 45 green, registered in the release battery
differential, pre-fix tool 45 ran · 22 FAIL · 9 ERROR · 14 pass · 2 spurious confirmed directly
release regressions        base 6 suites FAIL · candidate 6 suites FAIL · suite DELTA 0
                           test-method level: base 7 failing tests · candidate 8         see M-1
publication gate           PASS / BLOCKS 0 at BASE_HEAD and at the content tip
legend_lint PASS (1 pre-existing INFO) · fulltext_receipts OK 128 · growth_anchors PASS
fingerprints               scientist 355e3529… → 82423a48… · plan, mirror, orchestrator byte-identical
claim registry @ BASE_HEAD 39 '## CLAIM' · **Uncertainty:** 0 · **Limitations:** 0
                           · **Contradictory evidence:** 0 · **Evidence boundary:** 5
```

---

## 4 · BLOCKING FINDINGS

### M-1 · `DELTA_REGRESSION: 0` is false. The candidate turns a green test red.

Revision 1's `B-2` was *"counts, not sets"*. Revision 2 enumerated the sets — **of suite
names** — and the claim it is making is about regressions, not about suites. At the granularity
the claim is about, the delta is **+1**.

```
scripts/test_locator_obligation_reaches_every_route.py

  BASE_HEAD cbce3016   failing tests: {test_the_bootstrap_states_the_rule}
  CANDIDATE daaa3335   failing tests: {test_the_bootstrap_states_the_rule,
                                       test_every_route_carries_the_obligation_or_declares_an_exemption}
  ADDED: test_every_route_carries_the_obligation_or_declares_an_exemption
```

Isolated and run alone at both tips: **OK at `cbce3016`, FAILED at `daaa3335`.** The assertion
names the cause, and the cause is the candidate's own file:

```
AssertionError: ['framework/protocols/controlled_benchmark_ab.md'] is not false : these instruct
or describe a complete full-text read without the verbatim-locator obligation, and without a
declared exemption:
  framework/protocols/controlled_benchmark_ab.md
```

Measured at source: `controlled_benchmark_ab.md` trips the guard's marker (`"coverage map"` ×2)
and carries the obligation token `verbatim_locators` **zero** times, and is not in `EXEMPT`. Its
sibling `scientist_reading_modes.md` trips the same marker (×4) and carries the token **three**
times, which is why that file passes. The guard itself is **untouched by the candidate**
(`git diff main daaa333 -- scripts/test_locator_obligation_reaches_every_route.py` is empty), so
this is not a moved goalpost.

The same-reason check the manifest performs is real but partial: §4.2 verifies it for
`test_release_runner_verdict.py` — *"fails at both tips for the same reason, verified by reading
the assertion"* — one suite of six, and not the one whose reason changed. I compared all six;
five are identical up to worktree path and timing, and the sixth is above.

**Why this is blocking and not a note.** The guard exists because on 2026-08-04 no verbatim
locator existed anywhere in the canonical state, across every complete read in the ledger. The
candidate adds a new route that instructs two complete full-text readings, and that route does not
carry the obligation. This is not only a red test; it is the locator obligation failing to reach
the newest reading route in the laboratory — the exact failure the guard was built to make
expensive. And the manifest's sentence *"The six are `PREEXISTING FAILURE`, carried forward and
classified, not resolved"* reads as *nothing new is red*, which is not what the trees show.

**Remedy:** carry `verbatim_locators` into `controlled_benchmark_ab.md` where §4/§8 already
describe the obligation in prose, **or** add the path to `EXEMPT` with a reason a reviewer can
disagree with; re-run; and state the delta at test-method granularity, not suite granularity,
since a suite that is already red can absorb a new failure without moving a set of names.

---

### M-2 · The blind spot is computed over one key and the exemption is spread over two.

`verify --post-read` prints `[BLIND SPOT]` for exactly one path, and both the protocol and a
contract test assert that this is the whole of it:

- `controlled_benchmark_ab.md:284–289` — *"The blind spot is that one path… computed as the
  intersection of `expected_output_paths` with `forbidden_prior_output_paths`, so it cannot be
  wider than what the spec declares and **cannot be widened silently**."*
- `surface_spec.json _expected_output_note` — *"A path added here that collides with a forbidden
  path therefore widens a printed blind spot; **it cannot widen a silent one**."*
- `controlled_benchmark_ab.md:297`, the guarantee table — `verify --post-read` provides
  *"**nothing outside the allowlist and the declared output set is present**"*.
- `test_the_declared_blind_spot_is_exactly_one_path` asserts on that intersection.

`_is_expected_output()` admits a path by the exact list **or** by
`expected_output_prefixes = ["output/renders/"]`. `declared_blind_spots()` intersects only the
exact list. So the prefix is an exemption that is never computed and never printed.

**Reproduced.** A copy of `framework/protocols/controlled_benchmark_ab.md` — itself on
`forbidden_prior_output_paths`, and dense with the paper's identifiers — placed at
`output/renders/smuggled.md`:

```
verify --post-read   →  VERDICT: PASS   rc=0
                        [BLIND SPOT] …/deepdive_manifests/PMID42397075.json   ← still says size 1
                        no NOT ALLOWLISTED · no IDENTIFIER LEAK · no PRIOR OUTPUT
CONTROL, same bytes at …/fulltext_dossiers/NOTES.md (non-exempt slot)
                     →  VERDICT: FAIL   NOT ALLOWLISTED + IDENTIFIER LEAK 18 hit(s)   rc=1
```

The control is what makes it a hole rather than a design: the identical bytes are caught one
directory away. `freeze` does not compensate — it classifies the same file as `role: "output"`
and leaves `UNEXPECTED_FILE_SET` **empty** — and `verify-freeze` then treats it as legitimately
frozen output. `locators` admits a citation of it under the same produced-prefix. Four
instruments, one uncovered prefix.

**Steelman, and why it does not dissolve the finding.** Renders cannot be enumerated in advance —
the reader chooses which pages to render — so a prefix is the only workable rule, and a real
render is binary and unscannable anyway. Both true. But the exemption is written on *position*,
not on *type*, so a decodable text file under that prefix is skipped by a scan that could read it
and by an allowlist check that would reject it. And the exposure is genuinely narrower than it
looks: at handover the slots are provably empty, so the bytes must arrive during the reading,
which means the reader already read outside the surface — the residual §4.3 declares under J.0.

**So the contamination capability is not new; the census of what is unchecked is wrong.** That is
exactly the shape of revision 1's `B-4`, one level down, and it fails the standard this candidate
sets for itself: a PASS sentence is the reviewer's evidence, and *"nothing outside the allowlist
and the declared output set is present"* is false while the tool prints it.

**Remedy** (small, and the candidate already has the machinery): include
`expected_output_prefixes` in `declared_blind_spots()` so the printed set names the prefix, **or**
keep the content scan and the allowlist check running for any decodable text file under a prefix
and exempt only what the reader was told to write; then correct §297 and the two "cannot be
widened silently" sentences, and extend `test_the_declared_blind_spot_is_exactly_one_path` to the
prefix key. My `NEG-8a` is the negative control it currently lacks.

---

## 5 · What was re-tested from R-1 and PASSES

```
B-1 POPULATION           PASS   65 units · 109 panels · byte-identical ×2 and to the tracked file.
                                Every figure verified against the caption as printed. Figure 2 is
                                six panels and stops at Figure 3's first character; the six phantom
                                units are gone. Figure 6's (C-D) expands. Supp Fig 1 is A–I,K,L,M —
                                the caption labels (G) twice and never labels J, and the enumeration
                                reports the paper rather than repairing it.
EXTRA METHODS HEADING    VALID  'Library preparation and Single-cell RNA-seq (scRNA-seq) (10x
                                Chromium)' is set in the same Bold 15.96 as all 23 others and wraps
                                across two lines on File009 p8. It is a heading, not body text
                                (body is Times New Roman 12), and no rule that requires one
                                blank-bounded line can see it. The typographic derivation produces
                                exactly the 24 headings the PDF sets, with no false positive and no
                                wrongly joined pair.
RESULTS / SUPPLEMENT     PASS   7 Results headings (four of them wrapped and correctly joined; the
                                margin line-numbers are removed before adjacency is tested, or four
                                headings would read as eight) · 2 main Methods · File011 7 categories
                                by geometry · File012 9 blots, 1J met twice counted once.
FILE008 BOUNDARY         HONEST 1 page of CRediT author roles. It carries no evidence unit, it stays
                                in the packet so both readers see the same packet (verified: File008
                                present in both surfaces, 24 files each), and it is excluded only
                                from the denominator. No scientific evidence is removed.
B-3 FREEZE RECEIPT       PASS   RECEIPT_SCHEMA_VERSION 2 · 29 fields. Identity READ FROM THE TREE:
                                freezing A's tree as scientist-b refuses (rc=2, "ASSIGNMENT.md inside
                                this surface says 'scientist-a'"); wrong benchmark refuses. Tamper:
                                edited byte, added file, removed file, EQUAL-COUNT substitution,
                                late symlink, and A's receipt against B's tree — all caught, each
                                with its own reason code. Untouched tree passes. Pre-existing symlink
                                refuses the freeze. NO machine-specific absolute path enters the
                                receipt (measured: zero). INPUT_MANIFEST_SHA256, INSTRUCTIONS_VERSION,
                                OUTPUT_SCHEMA_VERSION, MODE, TASK_ID, FIRST_PASS_STATE, UTC timestamp,
                                SURFACE_RELATIVE all present; GUARANTEE_PROVIDED and
                                FAILURE_MODE_STILL_POSSIBLE state what it does not provide.
SYMLINK / TRAVERSAL      PASS   file symlink, directory symlink (reported, not walked), nested
                                symlink under the exempt prefix, symlink at a forbidden path — all
                                reported. locators: absolute path, `..` out of the tree, and
                                `..` resolving to a sibling inside the tree all rejected, the last
                                as NON-CANONICAL + OUTSIDE SURFACE, which is the correct reading.
                                The six previously-skipped forbidden paths are each caught post-read.
B-5 SEVEN FIELDS         PASS   OBSERVATION · AUTHOR_INTERPRETATION · LEGEND_INTERPRETATION ·
                                DIRECTION · UNCERTAINTY · LIMITATIONS · CONTRADICTORY_EVIDENCE, plus
                                Locators, as eight required bold labels in OUTPUT_SCHEMA §3 and
                                scientist_reading_modes §6.2. The false premise is withdrawn IN the
                                schema with the measurement beside it, and my count at BASE_HEAD
                                confirms it: 0/39, 0/39, 0/39. Acceptance tests now read "the twelve
                                canonical fields AND all eight labels" (§5.3) and "the twelve …
                                the SEVEN benchmark fields" (§3.6) — aligned with the schema.
PARALLEL CLAIM SCHEMA    NONE   the three grep hits are read at source and every one is a
                                prohibition (BENCHMARK_INSTRUCTIONS §4, OUTPUT_SCHEMA §6,
                                scientist_reading_modes §6.3). No canonical file is touched by the
                                diff; the twelve fields are reused unrenamed.
MODE A/B TASK-SCOPED     PASS   §0 and §1 scope the A→MODE A / B→MODE B fixing to BENCH-AB-001 by
                                name, with rotation named as Orchestrator's per task and Mirror's
                                anti-fossilization guard beside it. roles/scientist.md repeats the
                                rule and pairs no actor to a mode permanently.
ACTOR EQUIVALENCE        PRESERVED  §32 reproduced in the role contract; §7 states the protocol does
                                not modify §32 but interprets it; MODE B ⊇ MODE A; B ≠ Mirror by a
                                four-row table.
C-2 FORWARD OWNERSHIP    PASS   ownership going forward is the OWNER of the Task Contract; who that
                                is remains Orchestrator's under an ACTIVE lease and is not assigned
                                here. PARALLEL_READ_GROUP distinguishes intent; the verb is
                                "detectable", not "prevented", and the spec says so. C.2 content
                                stays CLOSED and was not reopened.
ACTOR REGISTRATION       PASS   ACTOR_ID ≠ SESSION_REF stated with consequences (§1.2): no actor
                                observes its own routing reference; a stale ref does not unregister;
                                nothing is keyed by a session ref. Grep for an invented session ref
                                in the content: none. SESSION_REF is "observed via L1 `from`, or
                                DERIVED_BY_COMPLEMENT — never invented".
CANONICALIZATION DEP.    CONFIRMED  measured, not inherited: scientist 355e3529… → 82423a48…, and
                                plan/mirror/orchestrator byte-identical at both tips. A checkpoint
                                written before execution is INCOMPATIBLE after it (A.6). Plus the
                                PROPOSED status line, the UNRESOLVED contract owner, and L2 suspended.
                                Ground 3 is marked ⚠️ as the weakest and not load-bearing (R-8).
SCIENTIFIC DEPTH         PRESERVED AND INCREASED  the population grows 36 → 65 by giving rules to
                                four kinds that had none; panels fall 115 → 109 only by deleting six
                                units the source does not contain. "Do not compress depth or coverage
                                for token, time or cost" in MODE_A, MODE_B and BENCHMARK_INSTRUCTIONS
                                §3. Speed/token/volume in a separate table, never combined, never
                                tie-breaking. Full packet incl. all five supplements to both readers.
PUBLICATION GATE         PASS / BLOCKS 0 at BASE_HEAD and at the content tip; the four [REVIEW] rows
                                are identical at both and pre-existing.
SESSION-ROUTING DEBT     OUT OF SCOPE — NOT SILENTLY RESOLVED  §5c names it and implements nothing;
                                no file matching session/rout/registr is added by the diff.
SCOPE CREEP              NONE   the only executable added reads no Agent Card, no registry, no
                                receipt ledger, no *_current.md, no lease, no approval queue, no
                                watcher (measured: 0,0,0,0,0,0; the single "receipts" hit is a word
                                inside a FAILURE_MODE string). Every carried debt is listed unfixed.
LINT / receipts / anchors PASS · OK 128 chained, tail anchored · PASS at the candidate tip
```

---

## 6 · RECORDED FINDINGS — non-blocking, to be carried or answered

- **N-1** `surface_spec.json` contradicts itself about File012. `notes` (6) says labels are
  *"reported AS PRINTED, not normalized"*; the File012 rule's `_note` says *"the label is
  normalized to a single space"*. The output is as printed — `Supplementary Fig. 5B` and
  `Supplementary Fig.6E` both survive — so `notes` (6) is right and the rule note is wrong. It
  matters because a reader is told to grep these labels.
- **N-2** `declared_empty_sources` is accepted **on declaration and never measured**. The
  completeness check proves every packet source is *either* enumerated *or* declared empty; it
  does not check that a declared-empty source is empty. My positive control declared File011 —
  seven real units — empty, and the command accepted it and dropped the denominator to 58
  without a word. The one real entry (File008) is genuinely empty; I read it. A short denominator
  flatters both readers, which is the candidate's own sentence.
- **N-3** For a PDF the regex segment is one **page**, so a caption crossing a page break is
  truncated at the break. Demonstrated on a synthetic two-page fixture: a caption split after
  `(B)` reports `['A','B']` and loses C, D, E. No caption in this packet crosses a break — I
  checked all ten supplementary captions (each alone on its page, each page's tail past the
  caption's natural end) and the main text is one segment — so the frozen population is correct.
  The bound is latent, and the spec's population notes do not name it.
- **N-4** Manifest §3G still reads *"the population is fixed before either reading exists, by
  command: **36 units, 115 panels**"*. R-9's remedy reached `benchmark_manifest.json`
  (`_superseded_counts`, correctly annotated) but not the candidate manifest's own prose, which
  now states a superseded pair as current — the finding R-9 exists for.
- **N-5** Manifest §5 carries *"**eight** failing release suites"* among the open debts, while
  §4.2 of the same document enumerates **six** at both tips and my measurement agrees with §4.2.
  The eight is the withdrawn revision-1 number surviving in a second place.
- **N-6** Three suite tests assert an exit code with no reason:
  `test_freezing_a_tree_holding_a_symlink_refuses` and `test_an_invalid_first_pass_state_refuses`
  (both declared spurious by Plan) and `test_freezing_under_a_wrong_benchmark_id_refuses` (not
  declared). I verified independently that all three fire for the correct reason against the
  post-fix tool, so none is a load-bearing false positive — but the assertion should carry the
  reason, which is the discipline the rest of the suite follows.
- **N-7** The differential counts do not reproduce. Plan reports *41 ran · 10 ERROR · 9 pass ·
  7 genuine*; I measure **45 ran · 9 ERROR · 14 pass · 12 genuine** with all classes executing.
  The five extra passes are `test_identical_mode_directives_are_caught`, two positive controls,
  `test_declaring_the_source_empty_makes_it_pass` and
  `test_no_population_rule_uses_a_fixed_character_window` — every one an invariant guard, a
  positive control, or a spec-only contract test that never touches the tool, which is exactly
  the categories Plan's *prose* names. The likely cause is a `setUpClass` abort in Plan's
  environment collapsing a five-test class into one error (45 − 5 + 1 = 41; 9 + 1 = 10). The
  conclusion is unaffected: 31 probes discriminate here against Plan's 32.
- **N-8** `locators` is purely lexical. A symlink at `output/renders/innocent.png` whose realpath
  is prior LEGEND output is cited and passes. Contained — `verify` reports the symlink and
  `freeze` refuses the tree outright — and the command's own NOT CHECKED line already says it
  reads a declaration. Worth naming there explicitly.
- **N-9** The population completeness failure exits **1**, while the spec `_note` says the command
  *"REFUSES"* — a word this tool's own exit vocabulary reserves for rc=2. Manifest §4.1 says
  "exits 1" and is correct; the spec note should match the vocabulary.

**Revision-1 R-findings, verified at source, none lost:** R-1 FIXED (no `ASSIGNMENT.template.md`
reference survives; the digest moved to `INPUT_MANIFEST_SHA256` and the text says `build` copies
rather than templates) · R-2 FIXED (caveat 2 of 2, verbatim, named a *known contamination of the
variable*) · R-3 FIXED (*"become fixed on canonical execution … with the operator's approval"*) ·
R-4 FIXED (named an EXTENSION FIELD on A.1, standing on *extendible, never removable*) · R-5 FIXED
(the exclusion is the systematic apparatus, with *"do not suppress an observation because it reads
as critical"*) · R-6 RESOLVED BY B-1 (the enumeration is gone; selection is typographic, so *a
function of (spec, source)* is now true non-trivially) · R-7 DOCUMENTED at the refusal site, in
the code, with the cost named · R-8 FIXED (⚠️ weakest, not load-bearing) · R-9 RESOLVED BY B-1 in
`benchmark_manifest.json` — **but see N-4: not in the candidate manifest's own §3G** · R-10 OUT OF
SCOPE, still Mirror's worktree debt, and it moved a number in this review (§0) · R-11 FIXED
(`PROCEDURAL`, with GUARANTEE/FAILURE/DETECTION/RECOVERY, detection after the fact) · R-12 FIXED
and verified: `git show b22968d:…` hashes to `f3f883c1e767…`, exactly the body digest declared,
and the whole file differs as the `carried_from` block now says it will.

---

## 7 · EVIDENCE_FOR · EVIDENCE_AGAINST · ALTERNATIVES · KEY_OBJECTIONS

**FOR:** the binding reproduced four times and twice without the script; the population correct
against the source figure by figure and heading by heading, deterministic, and byte-identical to
the tracked file; the freeze receipt verifying rather than storing identity and detecting every
tamper class including equal-count substitution; twelve of thirteen post-read attacks caught with
the right reason code; B-5 withdrawn against the author's own earlier position with the
measurement that refutes it; gate, lint, receipts and anchors green; scope and authority
boundaries respected throughout; scientific coverage increased, not traded away.

**AGAINST:** M-1 and M-2, each reproduced with a control that isolates it.

**ALTERNATIVES CONSIDERED:** (i) accept with M-1 and M-2 as carried debts — rejected: both are
false sentences in normative text about what an instrument guarantees, and both instruments are
what a reviewer is told to trust *instead of* the author's account; (ii) treat M-1 as
pre-existing — rejected, the test is green at `cbce3016` and red at `daaa3335` in identical clean
worktrees and the guard is untouched by the diff; (iii) treat M-2 as covered by the J.0 residual —
rejected in part and accepted in part: the *exposure* is contained by that residual and I say so,
but the *census* is wrong and three artifacts assert it cannot be.

**KEY_OBJECTIONS Plan may raise, and my answer:** *"the failure SET is unchanged, so DELTA is 0"* —
the set of suite names is unchanged; the set of failing tests is not, and a claim about
regressions is about the second. *"a render prefix cannot be enumerated in advance"* — agreed,
which is why the remedy is to print the prefix as part of the blind spot or to keep scanning
decodable text under it, not to remove the prefix. *"no reader can obtain prior output anyway"* —
true and already declared; the finding is that three artifacts say the unchecked region is one
path when it is one path plus a prefix.

---

## 8 · VERDICT

```
Annex C.2 VERDICT       REFINED — the specification is materially stronger than revision 1 and
                        five of its six remediations survive independent measurement; two claims
                        about what its instruments guarantee do not.
MIRROR_REVIEW           REQUEST CHANGES
REVIEWER_CONFIDENCE     high on M-1 (green at base, red at candidate, isolated, cause named by the
                        assertion, guard untouched by the diff)
                        high on M-2 (reproduced with a same-bytes control one directory away, and
                        the omission is visible in the code, the protocol table and the test)
RESIDUAL_UNCERTAINTY    N-7: I cannot reproduce Plan's 41/9/7 differential counts and infer the
                        cause rather than observe it; the conclusion those counts support is
                        unaffected either way. The exposure behind M-2 is bounded by a residual
                        the candidate already declares, and I may be weighing the false sentence
                        more heavily than the operator would.
EVIDENCE_NEEDED         the locator obligation carried into controlled_benchmark_ab.md or an
                        EXEMPT entry with a reason, re-run, with the delta stated at test-method
                        granularity; expected_output_prefixes folded into the printed blind spot
                        (or the scan kept over decodable text under it), the three sentences
                        corrected, and NEG-8a added as its negative control; N-4 and N-5 reconciled
                        with §4.1/§4.2.
WHAT_WOULD_CHANGE_MY_MIND
                        M-1: test_every_route_carries_the_obligation_or_declares_an_exemption
                             failing at cbce3016 in a clean worktree — it passes; or a rule under
                             which a new red test inside an already-red suite is not a regression.
                        M-2: a run of `verify --post-read` over a tree holding
                             output/renders/smuggled.md that reports a finding, or prints the
                             prefix as part of the blind spot — it does neither, while the same
                             bytes at …/fulltext_dossiers/NOTES.md produce two findings.
AUTHOR_RESPONSE         required (C.2); silence is not acceptance.
```

**HUMAN_APPROVAL: NONE — not granted, not recommended yet, not implied.**
**MAIN: cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED.**
**Nothing was executed, nothing registered, no benchmark run, no worktree of another actor written.**

---

## 9 · Provenance of this review

Detached scratch worktrees (`git worktree add --detach`): `wt-base`/`rg-base` at `cbce3016`,
`wt-cand`/`rg-cand` at `daaa3335`. The regression pair holds **no `files/`** at either tip, so the
environmental confound of revision 1 (`test_surface_census` inflated by a staged partial corpus)
cannot arise and did not. The packet was copied read-only from root `files/fulltext/` into
`wt-cand` only, digests 7/7 equal to the manifest; the differential tree is a plain non-git copy
carrying revision 1's script with its `SPEC_VERSION` line as the single patch. All attack surfaces
were copies under the session scratchpad. The session guard refused two heredoc writes while the
shell was inside a repository worktree; I did not reach for an unchecked tool — the probe scripts
were authored with `Write` into the scratchpad and invoked by name, and the measurements are the
same ones. Time source: the runtime exposes no wall clock beyond the date. Governance loaded
3.1.1; the mirror fingerprint is identical at `BASE_HEAD` and at the candidate tip.
