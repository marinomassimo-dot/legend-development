---
artifact: MIRROR hostile review, revision 1 (Annex C.2)
review_id: REV-SCIAB-MIRROR-001
object: CAND-20260818-SCIENTIST-AB-SPEC rev 1 · CANDIDATE_CONTENT_HASH 3b568aae…916c75 @ base cbce3016
level: R4 (MIRROR_REQUIRED — role contract in CORE, two new protocols, MAJOR)
reviewer: mirror
author: plan
adjudicator: operator (MAJOR → HUMAN_APPROVAL, Annex J.3) — none granted or implied here
date: 2026-08-18
verdict: REQUEST CHANGES — five blocking findings, all with a reproduced test; twelve recorded
governance_loaded: 3.1.1 · mirror fingerprint at BASE_HEAD 3dff8954…f65c (worktree HEAD carries a stale P5: 84d2b841…0738)
---

# The binding holds. The population, the regression claim, the freeze receipt and three "labels" do not.

Reviewed from `R-1`. Nothing transfers from any earlier Mirror review, from the sunset or P51C9
records, from Plan's own test evidence, or from a previous Mirror chat. Every number below was
re-derived in a detached scratch worktree of the candidate tip and of `BASE_HEAD`, never in
another actor's worktree and never in root.

---

## 0 · Rehydration — fail-closed, PASS

```
pwd == git top-level == .claude/worktrees/mirror        branch mirror · HEAD 9cf939f2 · clean
ACTOR_ID mirror · roles/mirror.md read in full (identical on main and on this branch)
governance body §2,5,7,8,9,10,11,12,14,20–29,31,32,35,36,38,48 · Annex A,C,D,G,H,I,J · plan_defined_parameters P2/P5 read at BASE_HEAD
fingerprint  compose --role mirror   at BASE_HEAD  3dff8954d4f6a56f6be14bc72be369095a1436437913a1e908c4b33c9762f65c
                                     at this HEAD  84d2b841b6081929e59d61e961e49077aca69c03136451d1000c72d902ef0738
                                     (difference = plan_defined_parameters.md P5 v3→v4; this review is conducted under BASE_HEAD's)
STABLE ACTOR IDENTITY  mirror · worktree mirror · roles/mirror.md · PERSISTENT_LEGEND_ACTOR
CURRENT SESSION ROUTING  not durable in the repository; deployment/local_instance.md (git-ignored, root) carries a
                         stale row `mirror: mirror-9c` from a prior incarnation — NOT authoritative (§43), NOT inherited.
                         No SESSION_REF is declared for this session and none is invented.
Agent Card               runtime/agent_card_registry.md exists on branch orchestrator; capabilities of mirror UNVERIFIED per contract.
authority                no command over any actor; no primary evidence; may not self-approve changes to its own rubric (G.2);
                         may not grant HUMAN_APPROVAL (H.1: operator); may not CANONICAL_BATCH_COMMIT (H.1: orchestrator);
                         WORK_COMMIT only on branch mirror, control-plane roots reviews/ · ledger/ · learning/ (content).
review authority         epistemic / method review; MAJOR classification when in doubt (H.1); C.2 format; CONFIRMED ≠ true.
Plan / Orchestrator      Plan proposes (GATE 1) and integrates; Mirror reviews; Orchestrator opens reviews, sets level, executes
                         canonical commit under lease. Proposer ≠ executor ≠ reviewer holds here: author plan, reviewer mirror,
                         adjudicator operator. Nothing in the candidate touches Mirror's rubric (G.2 not engaged).
```

**MIRROR REHYDRATION: PASS.** No essential part of identity or authority depended on a prior chat.

---

## 1 · Binding — PASS

```
base cbce3016 · tip b965ca58 (content tip)         3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75   run 1
base cbce3016 · tip b965ca58                       3b568aae…916c75                                                    run 2
base cbce3016 · tip 07564905 (ledger commit)       3b568aae…916c75
base cbce3016 · tip 7641dfdf (manifest rev 1)      3b568aae…916c75
base cbce3016 · tip e9b8680  (manifest correction) 3b568aae…916c75
base cbce3016 · tip 6cb3b446 (LATEST MANIFEST TIP) 3b568aae…916c75
independent recomputation without the script (git ls-tree + P5.2 serialization, v4, three roots)
                                                   3b568aae…916c75 · 522 entries · 27 excluded
main                                               cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED, merge-base of the branch
```

Commits after the content tip touch only `governance/candidates/` and `ledger/` (declared roots).
Content files `17` (+2910 / −1), control-plane files `4`, mode change only `create mode 100755
framework/scripts/benchmark_input_surface.py`. The manifest's `MANIFEST_TIP` note is correct: the
field is informational and the binding is `BASE_HEAD + CANDIDATE_CONTENT_HASH`.

---

## 2 · STEELMAN (before the objections)

The candidate solves the §32 tension in the right place — the mode is a property of the Task
Contract, the fixing to A/B is stated inside the BENCH-AB-001 scope with the anti-fossilization
guard named beside it — and it makes blindness a property of an enumerated, digested directory
rather than a promise. It reuses the three existing surfaces (manifest schema 2 · dossier ·
`## CLAIM` twelve fields) and forbids every parallel container by name. It states its residuals
(J.0) where the claims are, refuses to score with a composite, keeps speed/tokens in a separate
table, defers mechanistic value to the ladder, and freezes the evaluation population before any
reading. Its own test evidence includes negatives, and two of the defects it reports were found
by running the tool. The candidate does not execute itself, does not register anyone, and reads
the canonicalization dependency off the fingerprint rather than off prudence. As a specification
of *what* to build it is the strongest artifact this laboratory has produced for the Scientists.

What follows is where the artifact says more than what it ships.

---

## 3 · Population reviewed and tests executed

**Read in full:** manifest (all three revisions), handoff, `scientist_reading_modes.md`,
`controlled_benchmark_ab.md`, `benchmark_input_surface.py` (575 lines), `surface_spec.json`,
`benchmark_manifest.json`, `population/evidence_units.json`, the seven instruction files, the
four diffs to existing files, `CHK-plan-0010.json`, `SCIENTIST-AB-SPEC-001.json`; at source:
`claim_registry_current.md` label conventions, the packet (7 files, digests equal to the
manifest 7/7), File009/File010 captions and headings via PyMuPDF.

**Executed** (scratch worktrees `wt-base` = cbce3016, `wt-cand` = 6cb3b446, packet copied into
`wt-cand/files/` from root, git-ignored):

```
build ×2 → digests identical · verify ×2 → PASS (24 files/surface, tree A 81214cca…, tree B 2fbcd0a6…)
NEG-1 prior manifest in slot pre-read     4 findings (NOT EMPTY, NOT ALLOWLISTED, PRIOR OUTPUT, IDENTIFIER LEAK)   caught
NEG-2 paper_registry planted              3 findings                                                              caught
NEG-3 MODE_DIRECTIVE identical            NOT DIFFERING                                                           caught
NEG-4 one byte appended in B              PARITY BROKEN, both digests                                             caught
NEG-5 identifier in failure_taxonomy.md   IDENTIFIER LEAK + PARITY BROKEN                                         caught
NEG-6 innocuous extra file                NOT ALLOWLISTED                                                         caught
NEG-7 allowlisted file missing in B       ABSENT                                                                  caught
POS-8 honest synthetic output, --post-read PASS (no false positive on own manifest / own PMID)   Plan's fix reproduced
CTRL-8b same tree without --post-read     FAIL (proves the pre-read checks see the slots)
NEG-9 registry planted outside slot, post-read   3 findings                                                       caught
NEG-10 LEGEND's prior manifest in slot, post-read PASS — declared blind spot, confirmed
NEG-11 prior partial_locators dossier in dossier slot, post-read  PASS — NOT declared: non-colliding path, still skipped   🔴
NEG-12 file symlink → LEGEND prior manifest, pre-read   PASS "allowlist is exhaustive"                            🔴 not caught
NEG-12b directory symlink → LEGEND deepdive_manifests   PASS                                                      🔴 not caught
NEG-12c symlink AT a forbidden path                     PRIOR OUTPUT                                              caught (exists() follows)
LOC-POS all inside surface                PASS
LOC-NEG-A entry cites LEGEND dossier by repo-relative path
          disease-models/wwox/research/fulltext_dossiers/PMID42397075_partial_locators.md   PASS                 🔴 not caught
LOC-NEG-B absolute path                   OUTSIDE SURFACE                                                        caught
LOC-NEG-C output/../../../…<root>/…       PASS                                                                    🔴 traversal admitted
LOC-NEG-D output/../secret_notes.md       PASS                                                                    🔴 traversal admitted
LOC-NEG-F manifest absent                 REFUSE, rc=1 (docstring promises 2)
freeze  deterministic (same digest twice) · one appended byte moves it · records surface(ABSOLUTE PATH), actor_id,
        benchmark_id, tree_sha256, file_count, files[] · ABSENT: mode, timestamp, commit sha, input-manifest digest,
        instructions/schema version, first-pass state, order · actor_id/benchmark_id accepted unchecked (wrong values recorded)
population ×2 → identical bytes · identical to tracked evidence_units.json (sha256 a385cc35…)
        36 units · 115 panels · Figure 6 = ABCDE (range fix reproduced) · Supp Fig 1 = A–I,K,L,M (as declared)
        Figure 2 = ABCDEFGHIJKL — caption read verbatim (fitz.txt l.2232–2245): (A)…(F). SIX panels, not twelve.   🔴
        File009 blank-bounded headings: 23 · enumerated in spec: 20 · missing: "Ca2+ Imaging" (p6),
        "WWOX and MYC expression invivo" (p10), "Chromatin immunoprecipitation sequencing (ChIP-seq) analysis" (p13)   🔴
deepdive_manifest.py inside a built surface  BLOCK on absent manifest (imports resolve)   as declared
run_release_regressions.py   wt-base 6 suites FAIL · wt-cand 9 (one, test_surface_census, is my staged partial corpus:
        fails identically at base with the same files/, passes at cand without) → 8 · DELTA +2   🔴
public_release_gate.py       PASS / BLOCKS 0 at base and cand · positive control on a plain copy with two surface-relative
        links reintroduced → BLOCK_PUBLICATION, BROKEN_MARKDOWN_LINK ×2 · reverted → PASS
legend_lint PASS (1 INFO) · fulltext_receipts verify OK 128 · growth_anchors PASS · fingerprints: scientist 355e3529→82423a48,
        plan/mirror/orchestrator byte-identical at base and cand
claim registry, at BASE_HEAD: 39 '## CLAIM' · bold labels present in 39/39: the twelve canonical only ·
        **Evidence boundary:** 5/39 (+4 suffixed variants) · **⚠️ Counter-directional evidence …:** 1/39 ·
        **Nota epistemica** 1 · "limiti metodologici" 1 · Uncertainty/Limitations as label 0/39 ·
        Status: conflicting evidence 1/39 (lifecycle enum, cross-paper)
```

---

## 4 · BLOCKING FINDINGS — each with the test that found it and the remedy that would close it

### B-1 · The ex-ante evaluation population is wrong, in both directions

- **Figure 2 carries twelve panels; the caption has six.** `panel_window: 3600` runs 925 characters
  past Figure 2's caption into Figure 3's and absorbs G–L. `evidence_units.json` therefore holds
  six phantom units no locator can ever anchor, and Figure 2 coverage of a complete reading
  computes as 6/12. The declared count `panels: 115` is 109. Reproduced independently by reading
  the caption (`fitz.txt` l.2232–2245) and by measuring the gap between consecutive caption
  matches (Fig 1→2 1829, 2→3 925, 3→4 2846, 4→5 2045, 5→6 1275 — every one shorter than the
  window; only Figure 2 gains letters, the others happen not to). The same fixed window
  *truncates* Supplementary Figures 1 and 3 (captions 2370 and 2510 chars against a 2200 window;
  no letter lost this time, by luck). **A window bounded by the next label match, or the end of
  the segment, is the rule that measures the paper; a fixed integer is not.**
- **Three supplement methods sections are missing** — the "pattern" is a hand-enumerated list of
  twenty headings; File009 has at least twenty-three (`Ca2+ Imaging`, `WWOX and MYC expression
  invivo`, `Chromatin immunoprecipitation sequencing (ChIP-seq) analysis` — the last is distinct
  from the wet-lab section that *is* listed). A short denominator on methods flatters both readers
  — the candidate's own sentence.
- **Protocol §8.1 promises what the spec never enumerates**: "Results subsection headings" (no
  rule exists), "supplementary … tables" and "supplement sections" (File011 resource table and
  File012 uncropped blots yield zero units, so their coverage is unmeasurable).

The population's digest is meant to be frozen in the manifest *before* any reading precisely so
that it cannot be redefined afterwards. That is the reason it must be right before it is
canonical, not after. **Remedy:** bound the caption window at the next label; derive the methods
sections structurally (blank-bounded headings) or enumerate all twenty-three and say it is an
enumeration; add the Results-heading rule or strike the promise from §8.1; state which supplements
have no units and why. Then re-derive, re-count, re-digest.

### B-2 · The candidate adds two release-suite failures and reports "identical at BASE_HEAD"

```
BASELINE_FAILURES  (cbce3016, clean scratch checkout)      6   test_release_runner_verdict · test_locator_obligation_reaches_every_route
                                                               · test_abstract_corpus_is_not_evidence · test_release_surface
                                                               · test_fulltext_trace_contract · framework/scripts/test_session_self_eval
CANDIDATE_FAILURES (6cb3b446, same environment)            8   the six above + scripts/test_documented_commands.py
                                                               + scripts/test_fresh_clone_reader_journey.py
DELTA REGRESSION                                          +2
```

Both new failures are candidate-caused and were isolated with controls (each passes at
`wt-base`; `test_surface_census` fails at *both* tips only when my staged partial `files/` is
present, and is excluded from the delta):

- `scripts/test_documented_commands.py` — `controlled_benchmark_ab.md:133` names
  `scripts/deepdive_manifest.py` (a fragment of the layout tree under `framework/`); the suite
  reads it as a repository-local Python target and finds none.
- `scripts/test_fresh_clone_reader_journey.py` — `OUTPUT_SCHEMA.md:60` carries the inline path
  `disease-models/wwox/research/fulltext_dossiers/PMID42397075.md`, a *surface* path that does not
  exist in the repository. This is exactly the class the candidate says it fixed for the
  publication gate; two other suites read plain paths the same way.

The manifest and `CHK-plan-0010` state *"8 suites, IDENTICAL at BASE_HEAD"*. Neither enumerates
them; the equality is of counts. **The handoff's own drafting rule — an enumerated set is
falsifiable, a bare integer is not — was not applied to the one claim it exists for.** The
classification the operator would accept (PREEXISTING FAILURE, DELTA 0) is not what the
measurement shows. No suite was masked, disabled or bypassed (64 `RUN` lines at both tips; the
runner is unchanged; the only mode change is the new script). **Remedy:** repair the two paths
(write `framework/scripts/deepdive_manifest.py`; mark the surface path so the journey test does
not read it as a repository path, or teach the test the benchmark surface); re-run; enumerate the
failing sets at both tips in the manifest.

### B-3 · The freeze receipt does not carry what the protocol says it carries

`controlled_benchmark_ab.md` §6/§7: the receipt is *"commit sha, tree digest, file digests,
timestamps"*, taken *"before reading the content"* because *"a freeze taken after Plan has read
the content is a freeze whose timing cannot be shown."* The `freeze` subcommand emits
`surface` (an **absolute local path** — the very `BENCH_ROOT` §2.3 says is *"never written
here"*), `actor_id` and `benchmark_id` **as typed on the command line, unchecked against the
`ASSIGNMENT.md` inside the tree** (I froze A's tree as `scientist-b` / `BENCH-XX-999` and it
recorded both), `tree_sha256`, `file_count`, `files[]`. It emits **no timestamp, no commit sha,
no mode, no input-manifest digest, no first-pass state, no order** — and no receipt schema
exists anywhere in the candidate to make Plan add them by hand. The tree digest does bind the
instruction bytes and `ASSIGNMENT.md` transitively (files[] carries their digests, which can be
matched to the manifest's), and it is unique per content, so **Mirror can reconstruct *which*
first pass was evaluated**; what it cannot reconstruct from the receipt is *when*, *in what
order*, *under which manifest*, and it must trust two unverified strings for *whose*. The
declared post-read blind spot (§4.3) is compensated, in the candidate's own words, by *"the
pre-handover run plus the freeze receipt"* — so the receipt has to bind. **Remedy:** a receipt
schema (BENCHMARK_ID · ACTOR_ID · MODE · TASK_ID read from the tree's `ASSIGNMENT.md` and
cross-checked with the flags · INPUT_MANIFEST_SHA256 · surface `git rev-parse HEAD` · UTC
timestamp · tree digest · files[] split into packet / common / per-actor / output · relative
surface path only); `freeze` writes it; the tree-digest at handover and at freeze are both
recorded in the manifest's HANDOVER block; the order rule (second reader not shown the first
until its own freeze is recorded) named as PROCEDURAL, which is what it is.

### B-4 · The tool's PASS says more than the tool checks (J.0's rule, applied to the tool)

- **Symlinks are invisible to `verify`.** `iter_files` skips `is_symlink()`; a surface holding a
  file symlink to LEGEND's prior manifest, or a directory symlink to `deepdive_manifests/`, prints
  *"PASS — allowlist is exhaustive, no prior output"* (NEG-12, NEG-12b). Plan builds by copy, so
  no built surface has one; but `verify` is the instrument a reviewer is told to trust *instead*
  of Plan's account, and it should report a symlink as a finding, not skip it.
- **`locators` admits forbidden prior-output paths verbatim.** Any artifact under an output-slot
  prefix is treated as "produced in it"; `disease-models/wwox/research/fulltext_dossiers/
  PMID42397075_partial_locators.md` — LEGEND's prior dossier, at the path the repository always
  cites it by — passes (LOC-NEG-A). The manifest's test line *"a locator citing LEGEND's dossier
  + an absolute-path artifact → FAIL"* was carried by the absolute path alone. And
  `output/../../…` traversal passes (LOC-NEG-C/D). Chained with the next bullet, a reader who
  copied the prior dossier into its slot and cited it would pass `verify --post-read`, `locators`
  and `--verify-artifacts` (the file exists, its digest matches).
- **`--post-read` skips every forbidden path under the slots, not only the colliding one.** The
  declared blind spot is *"the reader's own manifest lands at the same path as LEGEND's"*; that
  is one path. The other six forbidden paths under those two slots (three `_partial_locators`
  dossiers, `PMID42128308.json`, `PMID18487609.json`, `PMID24550385.json` — 7 of the 23 sit under
  the slots) do not collide with
  anything the reader is instructed to write and could still be checked; they are not (NEG-11).
- `REFUSE` exits 1, not the documented 2, so a refusal and a finding are indistinguishable by
  return code.

**Remedy:** report symlinks; in `locators` reject any artifact ∈ `forbidden_prior_output_paths`
regardless of prefix, normalize with `posixpath.normpath` and refuse `..`/absolute; in
`--post-read` skip only the exact reader-output paths, keep every other forbidden path under
check; fix the exit code or the docstring. Then re-record the negative controls in the manifest,
including the ones above.

### B-5 · The three "refused" fields are fields — and the refusal's premise fails measurement

`scientist_reading_modes.md` §6.2 and `OUTPUT_SCHEMA.md` §3 state that `UNCERTAINTY`,
`LIMITATIONS`, `CONTRADICTORY_EVIDENCE` are not promoted because *"the registry already carries
them as labelled prose under stable labels."* Measured at `BASE_HEAD`, the registry does not:
the twelve canonical bold labels appear in 39/39 claims; `**Evidence boundary:**` in 5/39
(plus four suffixed variants), `**⚠️ Counter-directional evidence …:**` in 1/39, *Nota
epistemica* once, *limiti metodologici* once, `Uncertainty` and `Limitations` as labels **0/39**;
`Status: conflicting evidence` is a cross-paper lifecycle value (1/39), not intra-paper
contradiction. In the canonical registry an evaluator cannot locate any of the three across
claims without reading prose. Meanwhile `OUTPUT_SCHEMA.md` §3 **requires** `**Uncertainty:**`,
`**Limitations:**`, `**Contradictory evidence:**` and `**Locators:**` in a fixed block after the
twelve — and in this data model, where every canonical field *is* a bold label, a required bold
label in a fixed position *is* a field. So the information **is** addressable and comparable in
the benchmark — the strong property holds — but by the very mechanism the text says it did not
use. Consequences: the normative text carries a false premise; the "separate governed promotion
decision" is scoped to four fields when eight benchmark-only labelled fields will exist in every
output; §3.6 acceptance test 4 and `BENCHMARK_INSTRUCTIONS.md` §5.3 check *"the twelve and the
four"* while the schema demands eight, so a claim missing `**Limitations:**` passes the
acceptance test and fails the schema. Per field: **UNCERTAINTY → BENCHMARK_FIELD_NEEDED (and de
facto provided) · LIMITATIONS → BENCHMARK_FIELD_NEEDED (and de facto provided) ·
CONTRADICTORY_EVIDENCE → BENCHMARK_FIELD_NEEDED (and de facto provided, plus MODE B's axis).**
**Remedy:** say what was done — eight benchmark-only labelled fields, none canonical, all subject
to the later promotion decision; replace "stable labels" with the measured counts; align §3.6,
§5.3 and §8.2 to the schema. No data-model change is needed; the refusal of a *parallel schema*
stands and is right.

---

## 5 · RECORDED FINDINGS — non-blocking, to be carried or answered

- **R-1** §6 lists `instructions/ASSIGNMENT.template.md` — it does not exist (two concrete files
  do); §3 says the manifest's digest is *"recorded in each actor's ASSIGNMENT.md"* — neither file
  carries one and `build` does no templating. Both are claims about artifacts that are not there.
- **R-2** Both readers receive `scientist_reading_modes.md` §4–§5 in full (it must be common — it
  is normative for both), so each can read the other's mode. *"Do not speculate about what the
  other directive says"* is vacuous; the experimental variable is *which directive is addressed
  to you*, and §0/§4.2 should say so as a known contamination of the variable, next to the
  session-variance caveat.
- **R-3** `BOOTSTRAP.md` asserts *"already fixed, by the operator's approval"* in the past tense —
  true only after the execution it names. Consistent with the manifest's *"no approval
  pre-filled"* only because the sentence becomes canonical through that approval; worth phrasing
  as *"fixed on canonical execution of …"*, as `roles/scientist.md` does.
- **R-4** `PARALLEL_READ_GROUP` extends the Annex A.1 contract schema by protocol. Annex A is not
  amended; the candidate says no governance text is amended. Admissible as an extension field
  under a MAJOR candidate, and it should be named as an extension where §2.2 rule 2 introduces it.
- **R-5** MODE A is told *"a critique you volunteer is not what is being measured here"* — a
  demand characteristic that suppresses A's critical findings beyond what the variable requires;
  A still records weaknesses in the three labelled fields, so depth is not reduced. Note it.
- **R-6** The methods-section "pattern" is an enumeration, not a structural rule (see B-1); the
  population's claim to be *"a function of (spec, source)"* is true only in the trivial sense.
- **R-7** `verify` requires exactly two actors — right for AB, and it means rotation to a
  three-arm benchmark needs a tool change; say so or generalize.
- **R-8** Canonicalization ground 3 (*no contract can be issued to an unresolved owner*) is the
  weakest of the four: PID-12's *"confirmed at registration"* path exists in governance
  independent of this candidate, so ground 3 rests on the candidate's own choice to fix IDs at
  approval. Grounds 2 (fingerprint rotation, measured: scientist `355e3529…` → `82423a48…`, other
  three byte-identical) and 4 (§8/I.4, L2 suspended) are decisive on their own.
- **R-9** `benchmark_manifest.json` `EVALUATION_POPULATION.counts_at_first_derivation` repeats
  `36 / 115` — after B-1 both numbers change; the manifest must not keep a count the command no
  longer produces (its own rule).
- **R-10** `governance/plan_defined_parameters.md` on branch `mirror` is stale (P5 v3). This is Mirror's own
  worktree debt, not the candidate's; recorded so the fingerprint declared in §0 is explained.
- **R-11** The freeze ordering rule (§7, "neither sees the other until both are frozen") has no
  mechanism — correct under J.0, and it should be labelled PROCEDURAL the way `runtime/
  orchestrator_lease.md` labels its own.
- **R-12** The handoff carry: body byte-identical to blob `8e59df08` (sha256 `f3f883c1…`); the
  file itself differs by the status line and `carried_from` block, exactly as declared. Not a
  finding — recorded because "byte-identical copy" in the front matter refers to the body, and a
  reader hashing the file will get `79d40804…`.

---

## 6 · What was verified and PASSES

```
MODE A/B TASK-SCOPED         PASS   the only A→MODE A / B→MODE B pairings are inside BENCH-AB-001 files and §0's explicitly
                                    scoped sentence; roles/scientist.md pairs nothing; rotation is Orchestrator's per task
ACTOR EQUIVALENCE            PRESERVED   §32 language reproduced in the role contract; MODE B ⊇ MODE A; B ≠ Mirror table holds
C-2 FORWARD OWNERSHIP        PASS   owner = OWNER of the contract; duplication detectable by two contradicting records + actor
                                    pre-claim query + Plan reconciliation → Orchestrator adjudicates; no authority moved to Plan;
                                    C.2 content CLOSED, verified at source (both worktrees dirty on PMID42422765.json, sha 6c3fe60f)
PARALLEL CLAIM SCHEMA        NONE   the three grep hits are all prohibitions, as the manifest says; receipt.json and
                                    critical_reading.md are files, not claim models — but see B-5 for the count of labels
BLIND INPUT SURFACE          PASS   environmental: separate standalone repos, allowlist, digests, empty slots, identifier scan;
                                    residuals stated where the claim is
INPUT PARITY                 PASS   24/24 files per surface, digests equal, exactly two per-actor paths, all four parity negatives caught
PRIOR OUTPUT EXCLUSION       PASS ex ante (23 forbidden paths absent, proven) · FAIL for the post-read instruments (B-4)
SCIENTIFIC DEPTH             PRESERVED   full packet incl. all five supplements; renders excluded by design (attention, not
                                    source); "do not compress for budget" in both modes and §3; negatives/methods/limitations
                                    in both mandates; secondary metrics never combine, never break ties
ACTOR REGISTRATION           PASS   ACTOR_ID ≠ SESSION_REF with consequences; nothing keyed by session ref; no ref invented;
                                    second seat under ledger/ (control plane); registrar seat exists on branch orchestrator
CANONICALIZATION DEPENDENCY  CONFIRMED   GATE 3 (§12) · role-contract status line · §8/I.4 VERIFIED capabilities · A.6 refusal on
                                    the rotated scientist fingerprint · H.1 lease for assignment and commit — the sequence
                                    candidate → Mirror → HUMAN_APPROVAL → canonical → L2 → lease/task → execution is the rule
SCOPE CREEP                  NONE   no registry validator, P7, watcher, queue, ACK, routing, Mirror rubric, lease, disease model,
                                    Scientist C, Metacognition; the only new executable reads no registry/ledger/current file
PUBLICATION GATE             PASS / BLOCKS 0 at both tips; class of the 18 links reproduced by positive control; fixes are inside
                                    new files only — the four modified existing files are the ones the manifest lists
LINT / receipts / anchors    PASS · OK 128 · PASS at both tips
```

---

## 7 · EVIDENCE_FOR · EVIDENCE_AGAINST · ALTERNATIVES_CONSIDERED · KEY_OBJECTIONS

**FOR:** §1 binding; every ex-ante negative caught; Plan's two reported tool defects reproduced as
fixed; population deterministic and identical to the tracked file; gate PASS with a positive
control; scope and authority boundaries respected throughout; the design of the surface, the
data-model reuse and the no-composite evaluation are right.

**AGAINST:** B-1…B-5 above, each reproduced twice or by an independent route.

**ALTERNATIVES CONSIDERED:** (i) accept with notes, treating B-1/B-3/B-4 as debts to fix in the
build phase — rejected: the population and the tool are *content*, hashed and canonical on
execution, and the manifest says the population "cannot be redefined after the readings exist";
(ii) treat B-2 as pre-existing — rejected by the controls; (iii) treat B-5 as wording — rejected
because it is a false premise in normative text that changes the scope of a later governed
decision.

**KEY_OBJECTIONS Plan may raise, and my answer:** *"the population is re-derived at build time
anyway"* — the spec that derives it is what is being canonicalized, and it produces the wrong
denominator by construction; *"symlinks are not a threat model"* — the tool's PASS sentence is
the reviewer's evidence, and it currently over-states; *"the three labels are labels, not
fields"* — in a markdown section form every field is a label; the distinction has no operational
content.

---

## 8 · VERDICT

```
Annex C.2 VERDICT       WEAKENED — the specification stands in design; five of its measurable claims fail measurement
MIRROR_REVIEW           REQUEST CHANGES
REVIEWER_CONFIDENCE     high on B-1, B-2, B-4 (each reproduced twice, with controls); high on B-3 (read from the tool);
                        medium-high on B-5 (the measurement is certain; whether the operator wants the reclassification
                        or a fourth intermediate-field promotion is the operator's)
RESIDUAL_UNCERTAINTY    I could not reproduce Plan's "18 broken links" count (pre-commit state); the class and remedy are
                        reproduced. Plan's "8 at BASE_HEAD in root" is not reproducible in a clean checkout (6); the two
                        extra are environmental and irrelevant to the delta.
EVIDENCE_NEEDED         a revision with: corrected population + spec + counts; the two path repairs and enumerated suite sets
                        at both tips; a freeze-receipt schema implemented by `freeze`; symlink/forbidden-path/traversal
                        fixes with their negative controls recorded; §6.2 / OUTPUT_SCHEMA §3 / §3.6 / §5.3 aligned and
                        the registry counts stated
WHAT_WOULD_CHANGE_MY_MIND
                        B-1: a caption of Figure 2 that names panels G–L (it does not; l.2232–2245) or a rule under which
                             a coverage denominator may include units the source does not contain.
                        B-2: `scripts/test_documented_commands.py` and `scripts/test_fresh_clone_reader_journey.py` failing
                             at cbce3016 in a clean checkout — they pass.
                        B-3: a `freeze` output, from the candidate's script, carrying a timestamp and a commit sha — it does not.
                        B-4: `verify` reporting NEG-12; `locators` failing LOC-NEG-A — neither does.
                        B-5: `**Limitations:**` or `**Uncertainty:**` present as a label in a majority of the 39 claims — 0/39.
AUTHOR_RESPONSE         required (C.2); silence is not acceptance.
```

**HUMAN_APPROVAL: NONE — not granted, not recommended yet, not implied.**
**MAIN: cbce30168091f7769c56c4f019055fa55fd0d66a — UNCHANGED.**
**Nothing was executed, nothing registered, no worktree of another actor written.**

---

## 9 · Provenance of this review

Scratch worktrees (`git worktree add --detach`, removed at the end of the session): `wt-base` at
`cbce3016`, `wt-cand` at `6cb3b446`; packet copied read-only from root `files/fulltext/` into
`wt-cand/files/` (git-ignored, digests 7/7 equal to the manifest); all builds under the session
scratchpad. Nothing under `lettore`, `lettore-b`, `evidence-index`, `orchestrator` or root was
written. Time source: none exposed by the runtime — dates only. Governance loaded 3.1.1 at
`BASE_HEAD`.
