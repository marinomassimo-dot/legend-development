---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260818-SCIENTIST-AB-SPEC
revision: 5
supersedes: revision 4 (content tip a210f738, hash 07b65b37…5198) — REQUEST CHANGES under
  REV-SCIAB-MIRROR-004; revision 3 (content tip a3cad1d, hash 570fcbbb…8ab7) — REQUEST CHANGES
  under REV-SCIAB-MIRROR-003; revision 2 (content tip daaa3335, hash c0701094…21bcf) — REQUEST
  CHANGES under REV-SCIAB-MIRROR-002; and revision 1 (content tip b965ca58, hash 3b568aae…916c75)
  — REQUEST CHANGES under REV-SCIAB-MIRROR-001. No verdict, finding or PASS from any of the four
  transfers to this content: a revision is reviewed from R-1 (CHK-mirror-0006 RESUME_RULE). That
  includes M-1's closure, M-2's closure and M-3's closure in `--post-read`, which
  REV-SCIAB-MIRROR-004 recorded and which its own RESUME_RULE says do not transfer.
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-19
state: READY FOR MIRROR REVIEW (revision 5) — no approval requested, granted or implied
scope: HANDOFF-20260818-SCIENTIST-AB, as transmitted. Not reduced and not widened. Revision 5
  adds no scope: it repairs M-4 — the census now runs in both `verify` modes and the two modes
  are written as two contracts — corrects the artifacts that asserted the census unscoped,
  repairs the positive control that exercised the wrong mode, and touches nothing else. FIVE
  content files change: four edited and one added, the added one being this revision's Session
  Learning Review, which is the entry that moves the hash. No architecture was redesigned; M-1,
  M-2 and M-3's post-read closure were retested and not reopened, and the predicate M-3's
  closure rests on is byte-identical to revision 4.
---

# INTEGRATION_CANDIDATE — the definitive Scientist A / Scientist B specification

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260818-SCIENTIST-AB-SPEC
REVISION:                   5
BASE_HEAD:                  cbce30168091f7769c56c4f019055fa55fd0d66a
BRANCH:                     scientist-ab-spec
CONTENT_TIP:                2ffaedb2218ae9a9d96acf99fa6051ee545d6fef — ONE content commit for
                            this revision, carrying the remediation AND the Session Learning
                            Review together
                            # 🔴 NO BINDING WAS DECLARED AND THEN SUPERSEDED WITHIN THIS
                            # REVISION, for the second revision running. Revision 4 achieved
                            # that by writing SLR-plan-0004 before naming a tip; revision 5
                            # achieves it more simply, by not naming any tip until the single
                            # content commit — SLR-plan-0005 included — existed. Revision 3 did
                            # it the other way round and had to supersede its own value;
                            # SLR-plan-0003 L-5 recorded that as its session's failure.
SUPERSEDED_CONTENT_TIP_4:   a210f7381e5adc2fc43fc0f202213532ec6e80ed   (revision 4)
SUPERSEDED_HASH_4:          07b65b3707a4e63df23918b844140e7548929b27a8a182f8ebf2d9b0ab165198
SUPERSEDED_CONTENT_TIP_3:   a3cad1dcffc4090c23aaa972ad5e5fb817a7b912   (revision 3)
SUPERSEDED_HASH_3:          570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
SUPERSEDED_REV3_TIP:        b63482978dab13383177ed60ab55f4ca29fb1ed3   (the M-1/M-2 remediation
                            commit — a revision-3 content tip, superseded WITHIN revision 3)
SUPERSEDED_REV3_HASH:       7cef4cccb6684ef39cd6e17f605d396b2a1ad62a52c5d2c1413d64f97a794596
SUPERSEDED_CONTENT_TIP:     daaa33353840304aaa7d288b393a2b3bb4faa08d   (revision 2)
SUPERSEDED_HASH:            c0701094da01e6eb13a69a2194e040327ad6d2b691a4b31d9a1fb29bcba21bcf
SUPERSEDED_CONTENT_TIP_1:   b965ca5880e93ad57770a0483aaa4652ec5f390c   (revision 1)
SUPERSEDED_HASH_1:          3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75
MANIFEST_TIP:               the control-plane commit carrying this revision — and every later
                            control-plane commit on this branch, including the one carrying
                            this correction.
                            # 🔴 A MANIFEST CANNOT NAME THE COMMIT THAT CARRIES IT. Writing the
                            # value creates the commit the value would have to name, so the field
                            # lags by one by construction and chasing it is an infinite regress.
                            # It is therefore INFORMATIONAL. The binding is BASE_HEAD +
                            # CANDIDATE_CONTENT_HASH, and it holds because governance/candidates/
                            # and ledger/ are declared CONTROL_PLANE_ROOTS (P5.1): the hash is
                            # identical at the content tip, at the ledger commit between, and at
                            # every manifest revision. Measured at each point, not asserted —
                            # the count of points is not maintained here, because a count that
                            # has to be edited when a commit is added is the same fixed point
                            # in miniature. `--show-domain` prints what was excluded at each.
                            # `git log --oneline cbce3016..HEAD` shows the branch; the hash
                            # command shows the invariance.
CANDIDATE_CONTENT_HASH:     5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
CANDIDATE_HASH_VERSION:     legend-candidate-v4
CHANGE_CLASS:               MAJOR
LINT_RESULT:                PASS (1 pre-existing INFO)
PUBLICATION_GATE:           PASS / BLOCKS: 0   — at BASE_HEAD and at this tip
DELTA_REGRESSION:           0 ADDED FAILING TESTS — at TEST-METHOD granularity, which is the
                            granularity the claim is about (Mirror M-1). Failing suites AND
                            failing tests are enumerated as sets at both tips in §4.2, with a
                            same-reason comparison over every shared test. A set of suite names
                            is not evidence for this claim: an already-red suite absorbs a new
                            failing test without changing its name, and in revision 2 one did.
MIRROR_REVIEW:              REV-SCIAB-MIRROR-004 → REQUEST CHANGES, on revision 4 (M-1 CLOSED,
                            M-2 CLOSED, M-3 CLOSED in `--post-read` with the partition measured
                            independently, one new blocking finding M-4, three recorded P-6…P-8,
                            nine carried findings re-classified). Revision 5 requires a NEW
                            independent review from R-1. No PASS, no PRESERVED and no CONFIRMED
                            from that review — or from -003, -002 or -001 — transfers to this
                            content: M-3's post-read closure and M-1's included.
HUMAN_APPROVAL:             NONE — not requested, not granted, not implied
SNAPSHOT_ID:                n/a until canonical execution — GATE 4 belongs to Orchestrator
```

**`CHANGE_CLASS: MAJOR`**, on two independent grounds, either sufficient: it **fixes two
permanent ACTOR_IDs** — identity, provenance and learning attribution, and PID-12 held them
proposed precisely because that is not reversible; and it **edits a role contract in the `CORE`
fingerprint set**, rotating the scientist fingerprint. Classification is not contested and is
offered to Mirror to attack rather than to accept.

### Reproduction

```bash
python3 governance/scripts/candidate_content_hash.py \
  --base cbce30168091f7769c56c4f019055fa55fd0d66a \
  --tip  <the content tip> --show-domain
```

```
EXPECTED             5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
OBTAINED (run 1)     5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
OBTAINED (run 2)     5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
OBTAINED (run 3)     5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
OBTAINED at the control-plane commit carrying this revision
                     5307d4d213c1d25c42a51e27811b7e375907ceed77682b343dee68e0e2b8423f
```

**Recomputed without the script**, from P5.1 and P5.2 directly — `git ls-tree -r --full-tree`,
the three declared roots removed, **path-sorted**, `legend-candidate-v4\n` + `BASE_HEAD\n` +
every entry newline-terminated:

```
at 2ffaedb (CONTENT TIP, revision 5)     5307d4d2…423f     included 526 · excluded 31
TRAP RUN, deliberately wrong — the whole ls-tree LINE sorted instead of the PATH:
at 2ffaedb, line-sorted                  ab884df6…db2c     included 526 — a DIFFERENT value,
                                         because two 100755 entries move when the mode leads
                                         the key. P5.2 says path-sorted, and an implementation
                                         that agrees only with itself is not a second one.
POSITIVE CONTROLS, same route — the four PUBLISHED values of the earlier tips
at a210f73 (revision 4)                  07b65b37…5198     included 525 · excluded 30
at a3cad1d (revision 3)                  570fcbbb…8ab7     included 524 · excluded 29
at b634829 (superseded rev-3 tip)        7cef4ccc…4596     included 523 · excluded 28
at daaa3335 (revision 2)                 c0701094…21bcf     included 523 · excluded 27
at b965ca58 (revision 1)                 3b568aae…916c75   included 522 · excluded 24
```

The controls are the point, and this revision is the run where they earned their keep. **My
first recomputation reproduced none of the four**, with every included/excluded count exactly
right: it sorted the whole `ls-tree` line instead of the path, which orders by mode and moves the
two `100755` entries. P5.2 says *path-sorted*. A second implementation that agreed only with
itself would have shipped a wrong "independent" confirmation of a right hash, and the only thing
that caught it was requiring the published values to come back.

`1613fa3b…` is **not** a superseded binding — it was never declared as one. It is the
mid-revision content commit, printed so the single-entry delta below is checkable.

**The one entry that separates `07b65b37…` from `1613fa3b…`** is
`learning/plan/SLR-plan-0004.md` — 524 included entries becomes 525. That is `learning/` being
CONTENT by intent (P5.1) rather than by omission, behaving exactly as the declaration says it
must, and it is the fourth Plan record to exercise it (`SLR-plan-0001` @ `05cdeda`,
`SLR-plan-0002` @ `b9af54e`, `SLR-plan-0003` @ `a3cad1d`).

The invariance across the content tip and every later control-plane commit is the property that
makes `MANIFEST_TIP` informational, and it is **measured at each point, never asserted**.

Domain counts are **outputs of that command at that tip**, never constants maintained here —
read them from `--show-domain`.

---

## 2 · File list and classification

| File | Status | Domain | Classification |
|---|---|---|---|
| `framework/protocols/scientist_reading_modes.md` | **added** | CONTENT — hashed | **NORMATIVE** — reading modes, actor identity of A and B, task-ownership rule |
| `framework/protocols/controlled_benchmark_ab.md` | **added**, modified **(rev 3, rev 4)** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — normative for the benchmark it defines, and for nothing outside it. **Rev 3:** new §5.1 carries the verbatim-locator obligation into the route that instructs the reading (M-1); §4.3 and the guarantee table state what `--post-read` leaves unchecked (M-2). **Rev 4:** §4.5 and the guarantee row state the complete skip population and the partition, and name what the census does **not** say (M-3) |
| `framework/scripts/benchmark_input_surface.py` | **added**, modified **(rev 3, rev 4)** | CONTENT — hashed | **NORMATIVE (tooling)** — it decides whether a surface may be handed over; it is not documentation. **Rev 2: substantially rewritten**; **rev 3:** the prefix exemption is written on bytes rather than position, and the unchecked surface is enumerated from the tree; **rev 4:** `scan_skip_reason()` — one predicate, called by the scan loop **and** the census, so the two cannot disagree (M-3). Twelve functions byte-identical to rev 3; only `cmd_verify` and `unchecked_surface` changed |
| `framework/scripts/test_benchmark_input_surface.py` | **added (rev 2)**, modified **(rev 3, rev 4)** | CONTENT — hashed | **NORMATIVE (tooling)** — **71** probes, one per clause of every PASS sentence, each null finding with a positive control. Rev 3 adds fourteen and repairs a fixture whose "render" was a markdown file; **rev 4** replaces the census test whose expectation reproduced the implementation, adds `ScanSkipClassTests` (8) and `CensusContractTests` (3), and makes the honest-reading positive control assert the whole census instead of the verdict alone |
| `scripts/run_release_regressions.py` | modified **(rev 2)** | CONTENT — hashed | **DOCUMENTATION/INFRA** — one line: the new suite registered in the battery, which `test_release_runner_verdict.py` requires of every tracked test file |
| `roles/scientist.md` | modified | CONTENT — hashed | **NORMATIVE** — `actor_id_status` front matter + the *Reading modes* section. 🔴 In the `CORE` fingerprint set |
| `BOOTSTRAP.md` | modified | CONTENT — hashed | **NORMATIVE** — records that A and B are fixed and C is not |
| `framework/protocols/index.md` | modified | CONTENT — hashed | **DOCUMENTATION** — two rows in the protocol table |
| `framework/eval/README.md` | modified | CONTENT — hashed | **DOCUMENTATION** — the reader-benchmark axis, and what it does not have |
| `framework/eval/benchmarks/BENCH-AB-001/surface_spec.json` | **added**, modified **(rev 3, rev 4)** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the allowlist; a command reads it, a reviewer reads the same file. **Rev 3:** `_expected_output_prefix_note` states what the prefix admits and why, and the note claiming a blind spot "cannot widen a silent one" is corrected where it was false. **Rev 4:** two `_note` blocks only — the census is six classes and not three, and `content_scan` says out loud that an exempt path's content is **not read** and is now printed under `[UNCHECKED]`. No key, path or rule changed |
| `…/benchmark_manifest.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the experiment record, `PREPARED — NOT FROZEN` |
| `…/population/evidence_units.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the ex-ante evaluation population, derived by command |
| `…/instructions/` ×7 | **added**, one modified **(rev 3)** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — surface router, common instructions, output schema, `MODE_A`, `MODE_B`, and the two per-actor assignments. **Rev 3:** `BENCHMARK_INSTRUCTIONS.md` §1 tells the reader that `output/renders/` holds image files — before the reading, so the rule is a rule and not a trap |
| `learning/plan/SLR-plan-0003.md` | **added (rev 3)** | CONTENT — hashed | **LEARNING RECORD** — the Session Learning Review §15 / E.6 owed for revision 3's session. `learning/` is CONTENT by intent (P5.1), so it is in the population and moves the hash; §15 requires it at session closure, and D.2 binds an approval to the hash, so it enters **before** review rather than after |
| `learning/plan/SLR-plan-0004.md` | **added (rev 4)** | CONTENT — hashed | **LEARNING RECORD** — the same obligation for revision 4's session, and the single entry separating `07b65b37…` from `1613fa3b…`. Written and committed **before** any revision-4 binding was declared, so unlike revision 3 nothing had to be superseded |
| `learning/plan/SLR-plan-0005.md` | **added (rev 5)** | CONTENT — hashed | **LEARNING RECORD** — the same obligation for **this** session, and the entry that takes the domain from 525 to 526. Revision 5 makes one content commit carrying the remediation and this record together, so no tip could be named before it existed |
| `governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md` | **added** | **CONTROL PLANE — excluded** | the durable handoff, carried byte-identically |
| `governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md` | added | **CONTROL PLANE — excluded** | this manifest |
| `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` | **added** | **CONTROL PLANE — excluded** | task ACK + claim |
| `ledger/checkpoints/plan/CHK-plan-0010.json` | **added** | **CONTROL PLANE — excluded** | checkpoint |

```
content        22 files · +6855 / −1        no file deleted · no history rewritten
control plane   6 files                     excluded from the hash by construction

  Revision 5 edits FOUR of revision 4's twenty-one content files and ADDS exactly one —
  learning/plan/SLR-plan-0005.md. The four are benchmark_input_surface.py,
  test_benchmark_input_surface.py, controlled_benchmark_ab.md and surface_spec.json.
  The other seventeen are byte-identical to revision 4 by blob sha. Included entries
  move 525 → 526, and the added record is the entry that moves them. Within the
  executable, 37 of 39 top-level definitions are byte-identical to revision 4 by AST
  segment; the two that changed are cmd_verify and unchecked_surface.

  Revision 4 edited FOUR of revision 3's twenty content files and added exactly one —
  learning/plan/SLR-plan-0004.md. The other sixteen were byte-identical to revision 3
  by blob sha. That single addition is the whole difference between 1613fa3b… and
  07b65b37…, and between 524 and 525 included entries. The control-plane count moves
  as CHK-plan-0015 accumulates.

  Revision 3 edited five of revision 2's nineteen content files and added exactly one —
  learning/plan/SLR-plan-0003.md, the difference between 7cef4ccc… and 570fcbbb….

  git diff --shortstat cbce3016 HEAD -- . ':!governance/candidates' ':!ledger' ':!reviews'

  git diff --shortstat cbce3016 HEAD -- . ':!governance/candidates' ':!ledger'
```

**Mode changes, enumerated — two, both new files, both deliberate.**

```
create mode 100755 framework/scripts/benchmark_input_surface.py
create mode 100755 framework/scripts/test_benchmark_input_surface.py
```

Every other created file is `100644`. **No existing file's mode is changed by this candidate**,
in either revision.

**No governance text is amended.** Annex I.2 step 7, I.4, A.1 and A.3 are *satisfied* here, not
edited. The domain is stated per row so a reviewer does not have to infer which side of the
hash a file falls on.

**One file is executable and it is deliberate.** `benchmark_input_surface.py` carries mode
`755`. `scripts/test_release_surface.py` asserts that every shebang entrypoint is executable and
currently fails on four canonical files; this candidate does not fix those and does not add a
fifth.

---

## 3 · What the specification does, clause by clause against the handoff

### A · Scientist A and Scientist B are actors, and the §32 tension is resolved on the task

Body §32 makes the three Scientists equivalent; the operator's scope asks for a primary reader
and a critical one. **The difference is a mode assigned by a Task Contract, not a property of the
actor**: `MODE A · PRIMARY_EVIDENCE_READ` and `MODE B · INDEPENDENT_CRITICAL_READ`, fixed to A
and B *for `BENCH-AB-001` only*, rotating afterwards under Mirror's anti-fossilization guard.
A mode that stops rotating has become the static specialization §32 forbids, and that is stated
where the assignment is made rather than in a closing caveat.

MODE A carries the full list the handoff transmits — findings, methods, population/model/context,
genotype, cell type, developmental stage, intervention, endpoint, directionality, negatives,
figures and tables, caveats, locator, provenance, typing, uncertainty, limitations, claim
candidates, mechanistic implications, unresolved ambiguity. MODE B carries **all of it plus**
eleven mandatory critical axes, each of which must be answered — with findings, or with
*"searched; none found"* and what was searched. Silence on an axis is an incomplete reading.

**🔴 B is not Mirror**, and the distinction is a table with four rows — object, authority,
visibility, output — rather than a sentence: B's object is the paper, Mirror's is the process;
B does not adjudicate A and does not see A during the blind pass; Mirror remains the reviewer
and adjudicator of the benchmark's method.

### B · Registration — the canonical path, made concrete, with a second seat

`scientist-a` → `lettore`/`lettore`, `scientist-b` → `lettore-b`/`lettore-b`, contract
`roles/scientist.md`, `ROLE_CONTRACT_HASH` **derived and never stored** in the spec.

The path is Annex I.2 step 7 and no second path is invented. What the spec adds is the content
of the declaration, what the registrar checks (the same six checks the 2026-08-17 registrations
passed), and a **second seat**: `ledger/registrations/<ACTOR_ID>/…` on the actor's own branch.
The reason is specific — the Agent Card registry makes identity survive from the *registrar's*
side; nothing made it survive from the *actor's*. After a crash the new session finds its own
last declaration in its own worktree, with the ACTOR_ID it must re-declare and the SESSION_REF
it must not reuse.

**ACTOR_ID vs SESSION_REF is stated with its consequences, not as a slogan:** no actor observes
its own routing reference; a stale SESSION_REF does not unregister the actor it names; and
nothing in the benchmark — task claim, checkpoint, frozen receipt, output — is keyed by a
session reference. **This session declares no `CURRENT_SESSION_REF` for `plan`**, for the same
reason, and says so in the task record.

**Why the IDs are fixed at approval rather than when a session appears.** The benchmark prepares
task contracts, input surfaces and frozen receipts **named per ACTOR_ID before the sessions
open**. An identity that becomes permanent only on arrival would leave every one of those
records pointing at a proposal. `BOOTSTRAP.md` asks for one deliberate moment before an ACTOR_ID
is fixed; the operator's approval of this candidate is that moment. **`scientist-c` is
untouched** and stays proposed until its own registration.

### C · C-2 — the forward question is answered, the content is not reopened

Verified at source before any of this: both worktrees hold the same modified file, byte-identical
(`sha256 6c3fe60f…`, blob `86bba8bb`, matching tag `handoff/C-2/PMID42422765-working-blob`).
**Nothing was reset, checked out, deleted, committed or reinterpreted.** `C.2 CONTENT: CLOSED`
stands.

The question C-2 deferred *to registration* is answered there, in two ways:

- as a **rule**: ownership of a source going forward **is the `OWNER` of the Task Contract that
  names it**; before such a contract exists no Scientist owns PMID 42422765; the two stale
  working copies are each actor's own (§14); **who that OWNER is remains Orchestrator's under an
  ACTIVE lease** and is not assigned here;
- as a **declaration**: `C2_STATE_ACK` from both actors, and `C2_ORIGIN_STATEMENT` from
  `scientist-b` on how the identical edit came to exist there. `"unknown"` is admissible; a
  missing field is not.

### D · Duplicated assignment — a rule, a check, and an honest verb

```
PARALLEL_INDEPENDENT_READING   two contracts, one source, SAME declared PARALLEL_READ_GROUP
DUPLICATED_ASSIGNMENT          two contracts, one source, no shared group
```

One `OWNER` per contract; the actor queries the receipt and task ledgers **before** `TASK_CLAIM`
and raises a `BLOCKER` rather than claiming; Plan detects the pair at reconciliation and routes
it to Orchestrator, who adjudicates. **There is no lock (J.0).** What is guaranteed is that a
duplication cannot exist without leaving two records that contradict each other, and that both
the actor and Plan look at those records at defined moments. The spec says *detectable*, not
*prevented*.

### E · One data model, three surfaces, four intermediate fields

Re-verified at source rather than inherited:

```
deepdive_manifests/*.json      schema_version 2 · provenance of a READING · no per-claim array
fulltext_dossiers/*.md         artifact digests, verbatim locators, joins
claim_registry_current.md      39 '## CLAIM' · 43 '## ' · 0 '### CLAIM' · twelve fields
AUTHOR_INTERPRETATION as a field name in tracked state: 0
```

Eleven of the operator's sixteen names map onto canonical homes; the table gives each mapping.
**Four have none — `OBSERVATION`, `AUTHOR_INTERPRETATION`, `LEGEND_INTERPRETATION`,
`DIRECTION`** — and they are **BENCHMARK / INTERMEDIATE fields**: written in benchmark outputs,
evaluated in the comparison, and **not added to the claim registry**. Whether they are later
promoted is a separate governed decision after an outcome exists.

**Three that were NOT promoted, and this is the discipline the instruction asks for.**
`UNCERTAINTY`, `LIMITATIONS` and `CONTRADICTORY_EVIDENCE` already exist in the registry as
labelled prose under stable labels — *"Nota epistemica"*, *"con limiti metodologici dichiarati"*,
*"⚠️ Counter-directional evidence"*, `Status: conflicting evidence`. Promoting them would have
been the second noun for one object. The benchmark schema requires the labels and adds no fields.

**No parallel schema exists**: no `claims.json`, no `claim_schema.yaml`, no second locator
format, no renamed canonical field.

> **The check, stated as what it actually shows.** `grep -l 'claims\.json\|claim_schema'` over
> the diff returns **three files, not zero** — `scientist_reading_modes.md` §6.3,
> `OUTPUT_SCHEMA.md` §6 and `BENCHMARK_INSTRUCTIONS.md` §4. **Every hit is a clause forbidding
> the thing**, and a reviewer should confirm that rather than take this sentence for it. The
> first draft of this line claimed the grep returned nothing; it was corrected after running it.
> A count asserted from memory is the failure this repository keeps finding in itself.

### F · Blinding is a property of a directory, not a promise

At `BASE_HEAD`, twenty-one tracked files name PMID 42397075. A first pass inside `lettore` or
`lettore-b` is blind only because someone said so. So the surface is **built by allowlist into a
standalone repository that shares no object store with LEGEND**, and every input is enumerated,
digested and re-verifiable from the manifest.

```
build       two surfaces × 24 files, from the allowlist alone
verify      parity across surfaces · exactly two per-actor files · allowlist exhaustive ·
            forbidden prior-output paths absent · output slots empty · identifier scan = 0
freeze      tree digest, per-file digests, taken BEFORE the content is read
locators    after the reading: every cited artifact inside the surface
```

**Two residuals, stated where the claim is:** an actor can read outside the surface by absolute
path — nothing enforces otherwise (J.0) — and the model may carry training knowledge of the
paper. The surface makes the blind path the default one and any departure visible in the
reader's own locators. It is not a barrier and the protocol does not call it one.

### G · Evaluation — population first, dimensions separate, no composite

The population is fixed **before either reading exists**, by command: **65 units, 109 panels**,
identical across two runs, digest in the manifest. A denominator chosen afterwards is a
denominator chosen to fit. *(Mirror N-4: this sentence read "36 units, 115 panels" through
revision 2 — the pair `B-1` superseded. The correction reached `benchmark_manifest.json` and not
this paragraph, which is precisely the failure R-9 exists for, one document over.)*

Ten dimensions, each with its unit, measure, route and evaluator, each reported separately. The
mechanical ones are commands; the substantive ones are Mirror's, on the process; **the one that
is scientific judgment — mechanistic value — is listed by Plan and deferred to the review
ladder**, because §28 forbids Plan from resolving what a claim means.

`TIME`, `TOKEN/CONTEXT`, `OUTPUT VOLUME` are recorded in a table of their own and are **never**
combined, never break ties, and never make a reading better. Agreement between A and B is
descriptive, not a quality measure: two readers agreeing on an overshoot is two overshoots.
**No overall score, no weighting**, and `DISAGREEMENT_UNRESOLVED` with an explanation is a
legitimate outcome (§27).

### H · Canonicalization — determined at source, four independent grounds

```
BLIND FIRST PASS:  BLOCKED BY CANONICALIZATION
```

1. `roles/scientist.md` is `PROPOSED — binding once Mirror hostile review passes and the operator
   approves`; the modes are a directive on how a Scientist reads under a task.
2. **The fingerprint, measured:** scientist `355e3529…` → `82423a48…`; plan, mirror and
   orchestrator unchanged. A checkpoint written before execution is `INCOMPATIBLE` after it
   (A.6 refusal rule).
3. A Task Contract names an `OWNER (ACTOR_ID)`; both are `UNRESOLVED` until this executes.
4. Assignment runs on `VERIFIED` capabilities; none is verified and **L2 is suspended** by
   operator decision — independent of canonicalization, and also unmet.

The work therefore ends at **candidate complete + Mirror review**, which is what the handoff
said it would.

---

## 4 · Test and validator evidence

### 4.0aaa · Revision 5 — the one blocking finding, reproduced before anything was changed

Reproduced at revision 4's content tip `a210f738`, on a clean build of the real benchmark, before
a byte was edited. The universe is `os.walk`; scan membership is measured **by effect** — the
paper's identifier planted in each present file in turn, and `IDENTIFIER LEAK` naming it observed
— and census membership is parsed from the printed `[UNCHECKED]` lines. Nothing in the harness
calls `scan_skip_reason()` or `unchecked_surface()` or imports the module. The instrument check
runs first: `roles/scientist.md` must be observed as scanned, or no negative in the battery is
evidence.

| Mirror | Finding | Reproduced | Now |
|---|---|---|---|
| **M-4** | the census block sits behind `if args.post_read:` while both partition sentences print in **both** modes; `unchecked_surface()` takes `post_read`, defaults to `True`, and its only call site is inside the guard, so the parameter cannot be `False` from the CLI. 32 present files silent pre-handover on a clean build, 16 per surface | ✅ **exactly**: `PRESENT 48 · SCANNED 16 · CENSUSED 0 · SILENT 32 · OVERLAP 0`, instrument check PASSED, against `PRESENT 48 · SCANNED 16 · CENSUSED 32 · SILENT 0` in `--post-read`. §5B reproduced verbatim: the whole of `controlled_benchmark_ab.md` UTF-16LE+BOM, identical bytes into both surfaces at `framework/eval/failure_taxonomy.md` → **`VERDICT: PASS`, `rc=0`, path named 0 times**, both sentences printed | the census is **unconditional**; `post_read` has **no default**; the two modes print **two different** `PASS` sentences, each stating only what its own run checked; `EXPECTED_BY_PROTOCOL: NO` is a **finding** pre-handover and informational post-read (§4.4); and the tool prints a `MODE` line on every run. Silent files: **0 in both modes**, measured. §4.6 |

**The remedy is not the sentence, and the cheaper remedy was the review's own suggestion.**
`REV-SCIAB-MIRROR-004`'s `EVIDENCE_NEEDED` offers two routes: print the census in both modes, or
scope the two sentences and §4.3's bullet 2 to `--post-read` and declare the pre-handover skip
population a named residual. The second closes the finding. It also requires **weakening the
pre-handover row of the guarantee table**, whose `GUARANTEE_PROVIDED` is *"no identifier leak —
all of it observed, not attested"* — the epistemic content of the handover gate — while the
mechanism to satisfy it already existed, was already correct, and was one `if` away from running.
Weakening a guarantee that the code can meet is the permissive choice with a precision argument
in front of it, and this candidate has been told once already (`REV-SCIAB-MIRROR-002`) that
carrying a false claim as a debt is not available. `SLR-plan-0005` L-2 states the reasoning and
it is offered for Mirror to attack, not to accept.

**The scope was not widened.** `verify` still does not consume `build --emit-digests` (`P-4`),
`iter_files` is byte-identical so `.git/**` is still excluded from both populations (`P-6`), and
`N-7` is still unreconciled. Two functions changed — `cmd_verify` and `unchecked_surface` — and
37 of 39 top-level definitions are byte-identical to revision 4 by AST segment, `scan_skip_reason`
and `SCAN_SKIP_CLASSES` among them. **The predicate M-3's closure rests on did not move.**

### 4.0aa · Revision 4 — the one blocking finding, reproduced before anything was changed

Reproduced at revision 3's content tip `a3cad1d`, in the surfaces the tool itself builds, before a
byte was edited. Mirror's report is not the evidence here; the runs are — and one of them measured
more than the report did.

| Mirror | Finding | Reproduced | Now |
|---|---|---|---|
| **M-3** | the content scan skips on **four** conditions and the census enumerates the three shapes produced by **one**; two printed sentences and the §4.5 guarantee row say the list is complete. Ten present decodable files per surface, on a clean build | ✅ and **larger**: sixteen silent files per surface, not ten. Mirror's ten are the decodable ones its sentence is about; the six packet PDFs are skipped on the suffix test and were also named by nothing. Four-path same-bytes control reproduced exactly — `CLAUDE.md` and `benchmark/MODE_DIRECTIVE.md` silent, `roles/scientist.md` and `output/renders/smuggled.md` caught. **Plus a fourth class no review had named**: an allowlisted `.md` re-encoded UTF-16 into both surfaces reaches the decode guard, is skipped, is silent, and parity cannot see it | `scan_skip_reason()` is **one predicate with two callers** — the scan loop and the census — so a file is censused exactly when it is skipped. Six classes, each printed with reason, `EXPECTED_BY_PROTOCOL` and which checks did run. Silent files: **0**, measured. §4.5 |

**What revision 4 did NOT do, stated because both shortcuts were on offer and one was the
review's own suggestion.** `REV-SCIAB-MIRROR-003`'s remedy (i) is *add the two missing populations
to `unchecked_surface()`*; remedy (ii) is *restore revision 2's weaker wording*. Either closes the
finding and survives re-review. **Both leave the census and the scan as two separate statements of
one rule**, which is the thing that failed here twice: revision 3's census was not wrong because
it had three branches, it was wrong because it had *its own* branches, and `M-2`'s remedy edited
one copy of the rule and not the other. The repair is the shared predicate. That reasoning is
`SLR-plan-0004` L-2 and it is offered for Mirror to attack, not to accept.

The scope was also not widened. `verify` still does not consume `build --emit-digests`' per-file
input digests (`P-4`); that gap is now **stated** in the protocol and on every `scan_exempt_input`
census line — *parity detects a change made to one surface only* — rather than closed, because
closing it is a new check and this revision was given one finding.

### 4.0a · Revision 3 — the two blocking findings, reproduced before anything was changed

Both were reproduced at `BASE_HEAD` **and** at revision 2's content tip, in clean detached
worktrees, before a single byte was edited. Mirror's report is not the evidence here; the runs
are.

| Mirror | Finding | Reproduced | Now |
|---|---|---|---|
| **M-1** | `DELTA_REGRESSION: 0` is false. `test_every_route_carries_the_obligation_or_declares_an_exemption` is green at `cbce3016` and red at `daaa3335`, inside a suite already red, so a set of **suite names** could not see it | ✅ exactly — base 6 suites / **7** failing tests; revision 2, 6 suites / **8**. The assertion names the cause: `controlled_benchmark_ab.md` trips the guard's marker and carries `verbatim_locators` zero times | the route **carries the obligation** (§5.1 of the protocol), because it does instruct two complete readings; **the guard is untouched**; and the delta is stated at test-method granularity in §4.2 |
| **M-2** | the blind spot is computed over `expected_output_paths` while the exemption also lives in `expected_output_prefixes`, so prior LEGEND output at `output/renders/smuggled.md` passes `--post-read` while the same bytes one directory away produce two findings | ✅ exactly — `VERDICT: PASS`, rc=0, `blind spot: size 1`, no finding; control at `…/fulltext_dossiers/NOTES.md` → `NOT ALLOWLISTED` + `IDENTIFIER LEAK 18 hit(s)`, rc=1. `freeze` called the same file `role: "output"` and left `UNEXPECTED_FILE_SET` empty | the prefix admits **only bytes this tool cannot decode**; a decodable file there takes every check it would take anywhere else and `freeze` calls it `UNEXPECTED`; and `verify --post-read` **enumerates the unchecked surface from the tree** — §4.5 |

**What revision 3 did NOT do, stated because the temptation was available.** M-1 was not closed by
dropping the literal token into prose, and not by adding the path to `EXEMPT`: the benchmark
protocol instructs two complete full-text readings, so the honest classification is that it
**carries** the obligation, and §5.1 states it with its consequence — a reading declared complete
without `verbatim_locators.entries[]` is not complete, and freezing it does not repair it. The
guard was not weakened, and `git diff` over
`scripts/test_locator_obligation_reaches_every_route.py` between `main` and this tip is empty.
M-2 was not closed by printing the prefix and moving on, because that would have declared a
residual the tool could have checked instead: the scan can read a markdown file, so it does.

### 4.0 · Revision 2 — what the five blocking findings cost, measured

Every finding was **reproduced before anything was changed**. Mirror's numbering is authoritative
here; the remediation prompt paired B-2 with the post-read finding and B-4 with the regressions,
which is the reverse of the review, and the review is the durable artifact.

| Mirror | Finding | Reproduced | Now |
|---|---|---|---|
| **B-1** | Figure 2: 12 panels for a 6-panel caption; 3 Methods sections missing; §8.1 promised what no rule enumerated | ✅ exactly — gap Fig 2→3 measured at 925 chars against a 3600 window; `panels 115` → 109 | caption bounded by the **next label of its own rule** or end of segment; Methods derived by **typography**; Results, main Methods, table categories and blots given rules; File008 declared empty; the command **refuses** an unaccounted packet source |
| **B-2** | `DELTA +2`: `test_documented_commands` and `test_fresh_clone_reader_journey` red at the candidate, green at base; manifest said *"8, IDENTICAL"* over counts nobody enumerated | ✅ exactly — base **6**, candidate **8**, both sets enumerated below | both paths repaired; **DELTA 0**, set-wise |
| **B-3** | receipt: no time, no commit, no mode, no state, absolute path, ids unchecked | ✅ — A's tree froze as `scientist-b` / `BENCH-XX-999` | identity **read from `ASSIGNMENT.md` in the tree**, command line checked against it (refuses, exit 2); 18 fields; `verify-freeze` compares set-wise |
| **B-4** | `verify` blind to symlinks; `locators` admits forbidden paths under slots and `..`; `--post-read` skips 6 non-colliding forbidden paths; `REFUSE` exits 1 | ✅ all four | all four closed; the blind spot is **computed and printed**, and is size 1 |
| **B-5** | the three "stable labels" measure 0/39 | ✅ re-counted independently: `**Uncertainty:**` 0/39, `**Limitations:**` 0/39, `**Contradictory evidence:**` 0/39, `**Evidence boundary:**` 5/39 + 3 variants | **seven** benchmark fields, not four; schema, protocol and acceptance test aligned; **nothing enters the registry** |

**B-1 produced one thing Mirror's own count did not.** The review found three missing Methods
sections by a blank-line heuristic; the typographic derivation finds **four**. The fourth is
*"Library preparation and Single-cell RNA-seq (scRNA-seq) (10x Chromium)"*, a heading that
**wraps across two lines** — invisible to any rule that requires a heading to be one blank-bounded
line, including the one that found the other three. Recorded because a remediation that quietly
exceeds its review is still a change nobody reviewed.

### 4.1 · The population, re-derived

```
                              rev 1      rev 2      why
units                            36         65      four kinds had no rule at all
panels                          115        109      six phantom panels on Figure 2 removed
main_figure                       6          6      unchanged
main_table                        0          0      measured; now REPORTED at zero, not omitted
main_results_section              —          7      §8.1 promised these; no rule existed
main_methods_section              —          2      the article's own methods subsections
supplementary_figure             10         10      unchanged
supplement_methods_section       20         24      hand list → typography; +Ca2+ Imaging,
                                                    +WWOX and MYC expression invivo,
                                                    +ChIP-seq analysis, +Library preparation…(10x Chromium)
supplement_table_section          —          7      File011 yielded zero units; coverage was unmeasurable
source_data_blot                  —          9      File012 likewise
declared empty                    —          1      File008 — author contributions, with its reason
```

Byte-identical across two consecutive runs. `File008`'s exclusion is a **declared evidence
boundary**, not silence: the command exits 1 on a packet source that is neither enumerated nor
declared.

### 4.2 · Regression accounting at TEST-METHOD granularity — the granularity the claim is about

🔴 **Revision 2's version of this section is the finding.** It enumerated failure **sets**, which
answered revision 1's *"counts, not sets"* — and the sets were of **suite names**, while the claim
being made is about regressions, and a regression is a test. `test_release_runner_verdict.py`
appeared in both columns and said nothing about the failing test that appeared underneath it.
A set of containers is a count wearing a list.

Every target of `scripts/run_release_regressions.py` is executed the way the runner executes it —
`python3 <relative>` from the tree root — at each tip, in **clean detached worktrees** holding
exactly that commit and nothing else. Neither has `files/`, so the confound that inflated
`test_surface_census` in an earlier round cannot arise. Per-test identities and failure
signatures are parsed from the unittest failure blocks.

```
                              BASE cbce3016  REV 2 daaa3335  REV 3 b634829  REV 4 a210f73  REV 5 2ffaedb
targets present                     64             65             65             65            65
targets missing                      0              0              0              0             0
FAILING SUITES                       6              6              6              6             6
FAILING TESTS                        7              8              7              7             7
tests executed                     850              —              —            941           933
suites red, NO parsed test failure   ∅              —              —              ∅             ∅
targets with no test-id granularity  3              —              —              —             3
```

The second-to-last row is the omission channel `SLR-plan-0003` L-4 warns makes `ADDED = 0` true by
silence — a suite that exits non-zero while reporting no failing test. **It is empty at both
tips**, measured, so the zero below is a measurement and not an absence of measurement.

🔴 **The last row is new, and it is a declared limitation rather than a clean zero.** Three
regression targets — `launch/test_legend_launch.py` and the two skill-package suites — are custom
harnesses, not `unittest`, and print their own verdicts. They exit `0` at both tips and their
suite-level result is accounted for; my harness can attribute **no test id** inside them, so they
are recorded here rather than counted as passes. They are identical at both tips.

🔴 **My harness produced two wrong numbers before these, and both are recorded in
`SLR-plan-0005` L-3 rather than quietly replaced.** It first reported 421 tests, because it
invoked `python3 -m unittest <dotted-module>` — which cannot name the twelve targets whose paths
contain hyphens or dots — and matched only unittest's single-line verbose form, dropping every
test that has a docstring. It then reported **five** failing tests where Mirror measured seven;
the two it missed are `subTest` failures, which print a `FAIL:` header while the top-level line
still ends `... ok`. Corrected, the count reconciles with Mirror's independent measurement
exactly: **7 at both tips, same reason, 7/7.** A number that was wrong once is evidence about the
harness, and the reconciliation against another actor's number is what caught the second one.

**FAILING SUITES — identical at all three tips, and that is exactly why it is not the evidence:**

```
framework/scripts/test_session_self_eval.py
scripts/test_abstract_corpus_is_not_evidence.py
scripts/test_fulltext_trace_contract.py
scripts/test_locator_obligation_reaches_every_route.py
scripts/test_release_runner_verdict.py
scripts/test_release_surface.py
```

**FAILING TESTS at `BASE_HEAD` — 7:**

```
framework/scripts/test_session_self_eval.py::test_diagnosis_is_wired_before_growth_and_takeaways
scripts/test_abstract_corpus_is_not_evidence.py::test_the_bootstrap_bounds_the_corpus (file='CLAUDE.md')
scripts/test_fulltext_trace_contract.py::test_normative_layers_make_receipts_universal
scripts/test_fulltext_trace_contract.py::test_normative_write_rules_name_the_append_only_carveout
scripts/test_locator_obligation_reaches_every_route.py::test_the_bootstrap_states_the_rule (file='CLAUDE.md')
scripts/test_release_runner_verdict.py::test_every_tracked_test_file_is_in_the_runner
scripts/test_release_surface.py::test_shebang_python_entrypoints_are_executable
```

**FAILING TESTS at this candidate tip `2ffaedb` — 7, the same seven, and nothing else.**
The same was true at revision 4's tip `a210f73` and at revision 3's tip `b634829`.

```
ADDED FAILING TESTS      ∅      REMOVED FAILING TESTS      ∅      SAME-REASON      7 / 7
```

Same-reason is a comparison of the parsed assertion text, per test id, base against candidate —
not an inference from the two sets having the same size.

**FAILING TESTS at revision 2 `daaa3335` — 8: those seven plus**
`scripts/test_locator_obligation_reaches_every_route.py::test_every_route_carries_the_obligation_or_declares_an_exemption`.
That one test is `M-1`, and it is what a set of suite names could not show.

```
ADDED FAILING SUITES   (rev 4 − base)   = ∅        0
REMOVED FAILING SUITES (base − rev 4)   = ∅        0
ADDED FAILING TESTS    (rev 4 − base)   = ∅        0
REMOVED FAILING TESTS  (base − rev 4)   = ∅        0
SHARED FAILING TESTS                    = 7
DELTA REGRESSION at test granularity    = 0
  for the record, revision 2 measured the same way:  ADDED = 1
```

**`M-1` re-measured, not assumed.** `REV-SCIAB-MIRROR-003` closed it; no verdict transfers, so it
was measured again here.
`test_locator_obligation_reaches_every_route.py::ObligationReachesEveryRoute::test_every_route_carries_the_obligation_or_declares_an_exemption`
is **green at `BASE_HEAD` and green at `a210f73`**, and it is absent from both failing sets above.
The guard file is untouched by revision 4 — `git diff` over
`scripts/test_locator_obligation_reaches_every_route.py` between `bdac30f` and `a210f73` is empty —
and revision 4 edits `framework/protocols/controlled_benchmark_ab.md`, which is one of the files
that guard scans; the `verbatim_locators` obligation in §5.1 is untouched and the token is still
present three times.

**SAME-REASON CHECK — over all seven shared tests, not one selected suite.** Each failing test's
signature (the exception line and its message) is compared between the two tips. Normalized:
absolute worktree paths, temporary directories, `line <N>`, elapsed times and memory addresses —
the substrings that differ because a run is a run. **No assertion text is normalized**, so a
changed reason cannot be normalized into agreement.

```
SAME-REASON CHECK            PASS   7 / 7 identical after normalization
UNEXPLAINED REASON CHANGES   0
```

Revision 2 performed this check on `test_release_runner_verdict.py` alone — one suite of six, and
not the one whose reason changed. It is now done over every shared failing test, which is what
makes it capable of finding a semantic change hidden inside an already-red suite.

`test_release_runner_verdict.py` fails at all three tips for the same reason, verified by reading
the assertion: `governance/scripts/test_candidate_content_hash.py` is not registered in the
battery. That is a pre-existing debt of another candidate, untouched here. The new suite **is**
registered and runs green inside the battery.

No suite was disabled, weakened, skipped, or removed from `TESTS`; the baseline was not
redefined. The six suites and the seven tests under them are `PREEXISTING FAILURE`, carried
forward and classified, not resolved.

### 4.1b · The Session Learning Record, and why it is inside the reviewed population

`learning/plan/SLR-plan-0004.md` is in this candidate's content, and it was written and committed
**before any revision-4 binding was declared**. `learning/plan/SLR-plan-0003.md` is also here, and
at revision 3 it was added *after* a binding had been declared, which forced a supersession.

🔴 **That ordering error is not repeated.** `b1061eb`, the `M-3` remediation commit, was never
named as this candidate's tip; the record was written, committed, and only then was
`a210f73` declared. `SUPERSEDED_REV3_TIP` / `SUPERSEDED_REV3_HASH` stay in §1 as the record of
what revision 3 did, and revision 4 adds no equivalent pair because it produced none.

🔴 **`REV-SCIAB-MIRROR-003` `P-2` — the argument below is sound for Plan and one premise short of
the general claim it made, and the premise is now stated.** The missing premise is *that this
session's only durable branch is the candidate branch*. Mirror discharges the same §15 obligation
on branch `mirror`, under `learning/mirror/`, where a `WORK_COMMIT` moves no candidate hash;
Plan has no such branch and inventing one would be a governed change. So the conclusion holds
**for Plan**, by role contract and deployment, and not universally. Accepted as stated.

**The rule, at source.** Body §15: *"Ogni sessione significativa MUST chiudersi con Session
Learning Review."* — the trigger is **session closure**, not review submission. Annex E.6 gives
the record's schema and its persistence route: *"Persistenza: `WORK_COMMIT` alla granularità delle
milestone (A.7)."* P5.1 classifies the destination: *"`learning/` is CONTENT — by intent, not by
omission … they therefore belong to the content domain and **must** move the candidate hash when
they change."* And Annex D.2: *"ogni approvazione si lega a `CANDIDATE_CONTENT_HASH + BASE_HEAD`;
qualsiasi modifica materiale le invalida."*

**Read together they order it.** The record is owed now; it is content; content changes invalidate
a binding. So writing it after review would mean Mirror reviewed a population that is **not** the
one carried to canonicalization, and an ACCEPT would attach to a hash that no longer describes the
candidate. The record therefore enters before review, and the binding declared before it is
recorded as superseded in §1 rather than quietly replaced.

**Precedent, and it is durable rather than inferred.** Both earlier Plan records took this route
inside their own candidates: `SLR-plan-0001` @ `05cdeda`, and `SLR-plan-0002` @ `b9af54e`, whose
commit message states the consequence in as many words — *"The candidate content hash moves only
because SLR-plan-0002 is a content file on this branch — the documentary change the instruction
anticipated."* `SLR-plan-0001` closes by calling itself *"the first artifact to exercise that
declaration, and moving the candidate hash exactly as the declaration says it must."*

**What was NOT done.** `learning/` was not declared a control-plane root to avoid the hash move:
P5.1 forbids exactly that — *"Adding a root is a governed change to this file, reviewable as such —
never an ad-hoc exclusion made while preparing a candidate"* — and it declares `learning/` content
by intent. The record was not deferred to a later candidate either; §15 attaches it to this
session, and this session's work is this candidate.

**Declared debt, unchanged by this record.** No `LEARNING_INDEX` file exists (Annex E.2 names the
instrument; Plan owns its durability). §15's dedup step was therefore performed against the record
corpus read at source — `SLR-plan-0001`, `SLR-plan-0002`, `SLR-mirror-0009`, `SLR-mirror-0010` —
and two of the five entries are filed as `REPLICATION` of Mirror's patterns rather than as
originals. Every `CONFIRMATION_CLASS` is **proposed**: E.2 gives epistemic curation to Mirror, and
an actor classifying its own learning is the shape E.2 exists to prevent.

### 4.2b · The corrections revision 2's own numbers needed (Mirror N-4, N-5)

Two numbers in this manifest were superseded and survived anyway, which is the failure the
finding they came from exists to prevent.

- **N-4** — §3G said the population is *"36 units, 115 panels"*. That pair was superseded by
  `B-1` and correctly annotated in `benchmark_manifest.json`, but not here. **Corrected in §3G**:
  the population is **65 units, 109 panels**, and the superseded pair is named as superseded.
- **N-5** — §5 listed *"eight failing release suites"* among the open debts while §4.2 of the
  same document enumerated six, and six is what three independent measurements show.
  **Corrected in §5** to six suites, and to the seven failing tests under them, since a suite
  count is the object M-1 showed to be the wrong one.

### 4.3 · The adversarial suite — and the proof that it probes the defects

`framework/scripts/test_benchmark_input_surface.py` — **59 tests, all green** (45 at revision 2),
registered in the release battery. Built on the method Mirror used to find the defects: *take the tool's PASS
sentence literally and construct the cheapest state that makes it false while the tool still
prints it.* Every null finding carries a **positive control**, because a check that never fires
and a check that cannot fire look identical from outside.

**Differential control — the suite run against the PRE-FIX tool** (revision 1's script, patched
only to accept a v2 spec so the probe isolates the defect rather than the version bump):

```
against the pre-fix tool     41 ran · 22 FAIL · 10 ERROR · 9 pass
against this revision        45 ran · 45 pass
```

The nine that passed pre-fix are the checks that **already worked** — parity, `NOT DIFFERING`,
identifier leak, pre-handover prior output, and the positive controls. That asymmetry is the
control: a suite that failed everything against the old tool would be evidence of nothing.

⚠️ **Two of those nine are spurious and are declared rather than counted as evidence.**
`test_freezing_a_tree_holding_a_symlink_refuses` and `test_an_invalid_first_pass_state_refuses`
pass against the old tool because `argparse` rejects the unknown flags `--spec` and
`--first-pass-state` with exit 2 — the code the test asserts, reached for the wrong reason. The
honest count of genuine pre-fix passes is **seven**.

The ten ERRORs are `PopulationBoundingTests` and one `setUpClass`: the old tool does not
understand `sub_unit_pattern` and produces units with no sub-units, so the probes raise rather
than assert. That is the defect, arriving as an exception instead of a failure; it is reported
as an error and not dressed up as a clean red.

> **Mirror could not reproduce these counts (N-7)** and measured 45 / 9 ERROR / 14 pass / 12
> genuine against the 41 / 10 / 9 / 7 above, inferring a `setUpClass` abort in this environment
> that collapses a five-test class into one error — the arithmetic fits exactly. The
> discrimination conclusion is the same either way and neither count is load-bearing. Recorded
> rather than reconciled, because Mirror's numbers were measured and this explanation is
> inferred, and revision 3 did not re-run revision 1's tool to settle it.

### 4.5 · M-2 and M-3 — the exact guarantee, its mechanism, and the census that must match it

**The guarantee revision 4 makes, written so it can be falsified in one command:**

> `SCANNED` and `[UNCHECKED]` **partition** the present files. No file present in a surface is
> skipped by the identifier scan without being printed by name with the class and the reason,
> and no file is printed that was scanned.

Falsify it by producing a file that `verify --post-read` neither scans nor names. It is not the
claim *"post-read verification reads every file"* — it cannot, and it says so; and it is not
*"all unchecked paths are enumerated in advance"* — renders cannot be enumerated in advance,
which is why the prefix exists at all. It is the claim that the unscanned surface is **named at
run time, from the tree, exhaustively**.

🔴 **Revision 3's guarantee was the narrow one** — *no present file is skipped by **both** the
allowlist check and the identifier scan without being printed by name*. `REV-SCIAB-MIRROR-003`
found it true and I do not dispute that. The problem was that the tool printed two broader
sentences and this manifest tabulated a third, and all three were false: the scan skips on **four**
conditions and the census enumerated the three shapes produced by **one** of them. The narrow
formulation survives and is now strictly weaker than what holds, so it is no longer what anything
claims.

**Mechanism — one predicate changed, and the census follows it.** `_is_expected_output()` admits
an exact declared path as before; under `expected_output_prefixes` it now admits a file **only
when the tool cannot decode its bytes as UTF-8 text**. The exemption was written for pixels, and
a render is pixels. A decodable file under the prefix is exempt from nothing: the allowlist check
reports it, the identifier scan reads it, and `freeze` — which shares the predicate — puts it in
`UNEXPECTED_FILE_SET` instead of counting it as the reader's work. Alternatives considered and
rejected: printing the prefix as a blind spot (declares as unchecked a file the scan can read);
an extension allowlist (a `.png` that is text walks through it, and case 07 below is that file).

**The complete skip population, derived from the executable logic and not from the finding.**
`REV-SCIAB-MIRROR-003` measured ten silent decodable files per surface. Re-derived here from the
scan loop's own exits, on a clean build of `BENCH-AB-001` before any reader exists, the silent
population was **sixteen** — the six decodable ones Mirror counted plus four `.gitkeep` and six
packet PDFs, all skipped on the suffix test and all named by nothing. A finding is a lower bound
on its own population; the predicate is the population.

| SKIP_CLASS | PREDICATE (the scan loop's own exit) | EXPECTED BY PROTOCOL | WHAT STILL COVERS THE FILE |
|---|---|---|---|
| `blind_spot` | post-read · `expected_output_paths` ∩ `forbidden_prior_output_paths` | yes | the pre-handover `verify` run, the freeze receipt |
| `scan_exempt_present` | post-read · in `expected_output_paths` | yes | forbidden-path check, freeze receipt |
| `undecodable_prefix` | post-read · under `expected_output_prefixes` and bytes do not decode | yes | forbidden-path check, freeze receipt |
| `scan_exempt_input` | in `content_scan.exempt_surface_paths` | yes | allowlist check, forbidden-path check, cross-surface parity **for a change made to one surface only**, freeze receipt |
| `suffix_not_scanned` | suffix outside `content_scan.text_suffixes` | yes | allowlist check, forbidden-path check, freeze receipt |
| `undecodable_text` | text suffix, not exempt, bytes do not decode | **NO** | allowlist check, forbidden-path check, freeze receipt |

The last two rows were named by nothing at revision 3. `undecodable_text` was named by nothing
**and** reported by no review: an allowlisted `.md` re-encoded UTF-16 into *both* surfaces carries
the whole forbidden protocol text through `VERDICT: PASS` with `[UNCHECKED SURFACE] 0`, and
parity is silent because the change is identical on both sides. It is the one class the protocol
does not declare, the census marks it `EXPECTED_BY_PROTOCOL NO`, and the command counts those
separately so a reviewer reads them first.

**The census, in the vocabulary the review asked for.** Sizes are for a built pair before any
reading; every population is computed from the tree, and `[UNCHECKED SURFACE] n present file(s)`
closes the printed list on every run.

| | | |
|---|---|---|
| EXPECTED EXACT OUTPUT PATHS | **5** | declared in `expected_output_paths` — a static spec fact |
| EXPECTED OUTPUT PREFIXES | **1** | `output/renders/` — admits only undecodable bytes |
| PRESENT FILES, clean build | **24** per surface | 48 across the pair |
| SCANNED | **8** per surface | allowlist + forbidden-path + symlink checks **and** the identifier scan read their bytes |
| UNSCANNED / CENSUSED | **16** per surface, 32 printed | each with path, class, reason, `EXPECTED_BY_PROTOCOL`, and which checks did run |
| UNENUMERATED / SILENT SURFACE | **0** | not an argument this time: `scan_skip_reason()` is one predicate and the scan loop and the census are its two callers, so a file is censused exactly when it is skipped |

**Reproduced, with the control that makes it a hole rather than a design.** Same bytes, one
directory apart, against this tip:

```
output/renders/smuggled.md                       → NOT ALLOWLISTED + IDENTIFIER LEAK 18 hit(s), rc=1
…/fulltext_dossiers/NOTES.md      (control)      → NOT ALLOWLISTED + IDENTIFIER LEAK 18 hit(s), rc=1
output/renders/fig1_page1.png     (real render)  → VERDICT: PASS, rc=0, and [UNCHECKED] names it
freeze, smuggled.md present                      → UNEXPECTED_FILE_SET ['output/renders/smuggled.md']
freeze, real render present                      → OUTPUT_FILE_SET   ['output/renders/fig1.png']
against revision 2's tool, same states           → PASS rc=0 · blind spot size 1 · role "output"
```

**M-3 reproduced before anything was edited**, with Mirror's construction: the whole of
`framework/protocols/controlled_benchmark_ab.md` — a forbidden prior-output path, identifiers in
it — appended at four paths in **both** surfaces, at content tip `a3cad1d`.

```
                              REVISION 3 (before)              REVISION 4 (after)
CLAUDE.md                     PASS rc=0 · no finding ·         PASS rc=0 · NAMED
                              NOT NAMED · [UNCHECKED] 0        scan_exempt_input
benchmark/MODE_DIRECTIVE.md   PASS rc=0 · no finding ·         PASS rc=0 · NAMED
                              NOT NAMED · [UNCHECKED] 0        scan_exempt_input
roles/scientist.md  CONTROL   FAIL rc=1 · IDENTIFIER LEAK 18   FAIL rc=1 · unchanged
output/renders/smuggled.md    FAIL rc=1 · 4 findings           FAIL rc=1 · unchanged
```

Identical bytes; two caught, two silent. Without the two controls this is a design note about an
exemption; with them it is a hole and no argument is needed. **`M-2`'s closure is untouched** —
the two rows that caught it still catch it, with the same reasons and the same counts.

**`freeze` does not compensate, and revision 4 does not claim it does.** On the tampered
`CLAUDE.md` tree the receipt reports `outputs 0 · unexpected 0`, which is *correct*: `CLAUDE.md`
is a declared input, so `_classify` calls it input, exactly as it should. What the receipt does
carry is the file's digest in `FILES`, so `verify-freeze` detects any change made **after** the
freeze — measured, `rc=1` on one appended byte, `VERDICT: PASS` on the untouched tree. That is
the whole of the row's *"still covered by the freeze receipt"*, and it says nothing about a
substitution made before the freeze.

**Twelve hostile cases, each asserting the REASON and not only the exit code**, plus two spec
contracts — added to the tracked suite as `ExpectedOutputPrefixTests` and run in the release
battery. `SLR-mirror-0010` §4 is the argument for the discipline and it is Mirror's own: its
first B-4 battery reported 13/13 caught, and all thirteen were `rc=2` from `argparse` rejecting
`--out` where the command takes `--surfaces`. An expected exit code is never sufficient.

```
positive control · binary render passes and is named   forbidden bytes under the prefix
same bytes under prefix AND outside it                 nested directory under the prefix
renamed copy wearing a .png extension                  empty render prefix adds nothing
several legitimate renders, each named                 hostile file beside a legitimate render
late arrival on the next run                           the census IS the unscanned set
freeze calls a decodable prefix file UNEXPECTED        freeze still calls a render an output
```

**Revision 4 adds `ScanSkipClassTests` (8) and `CensusContractTests` (3), and replaces the test
that encoded `M-3`.** One probe per derived skip class, each asserting the printed **class** and
not the exit code, and each planting into **both** surfaces — a probe that edits one surface is
caught by `PARITY BROKEN`, which is a real check firing correctly and answering a question the
probe did not ask.

```
positive control · the scan fires on an allowlisted scanned file
positive control · the same file clean is in neither population
the same bytes at an exempt path and at a scanned one  (Mirror's four-path reproducer, as one test)
hostile bytes under a non-text suffix are named        an allowlisted .md that is not UTF-8 is
a non-UTF-8 hostile payload under the render prefix      named AND flagged EXPECTED_BY_PROTOCOL NO
all six classes present at once, each with its reason  an edit to an exempt input does not move
                                                         the census
CONTRACT · every class the predicate returns has an explanation
CONTRACT · the scan and the census call the same predicate
CONTRACT · every scan-exempt path in the real spec is an allowlisted path
```

That last contract is the probe behind a census line rather than the line repeated: the census
tells a reviewer an exempt input *still took the allowlist check*, and that is only true if every
exempt path is in the allowlist.

**Differential against revision 3's tool, which is the evidence the suite discriminates.** The
revision-4 tests, run unchanged against the tool at content tip `a3cad1d`:

```
71 tests · 12 FAIL/ERROR against revision 3 · 71 green at this tip

among them  test_every_present_file_is_either_scanned_or_named_and_never_both   FAIL
            test_the_census_is_exactly_the_present_files_the_scan_did_not_read  FAIL
            test_positive_control_an_honest_reading_passes_post_read            FAIL  ← the one
              that matters: at revision 3 it passed over ten silent files per surface, because
              it asserted rc == 0 and VERDICT: PASS and nothing else
            CensusContractTests::the scan and the census call the same predicate FAIL
```

**The oracle is not the implementation.** `REV-SCIAB-MIRROR-003` requires a census test whose
expected population does not reproduce the filter it validates, and the replaced test failed
exactly that way: its expectation was written by asking *what does the census produce here*,
which is a question the implementation answers. Revision 4 uses two oracles and neither is that —
a **hand-written literal** (`FIXTURE_CENSUS_AT_HANDOVER`, path by path from what the fixture puts
on disk, which does not move when the skip logic moves), and a **behavioural** probe that plants
the paper's identifier in each present file in turn and measures the scan by whether it *reports*
it. The behavioural one contains no copy of the skip rule at all, asserts the partition in both
directions, and requires the scanned set to be non-empty — because a battery whose detector never
fires is measuring its own invocation (`SLR-mirror-0011` §3).

**Differential against the pre-fix tool** — the same fourteen probes, revision 2's script,
revision 3's spec:

```
11 of the 12 hostile probes FAIL against the pre-fix tool
 1 passes: `freeze still calls a binary render an output` — the positive control that must NOT
   move, and it did not
 2 spec-contract probes pass against both, correctly: they read the spec, not the tool
```

Five of the eleven discriminate on the **exit code** (the detector itself); six on the census
output. A separate out-of-tree battery of the same ten cases required by the review ran
11/11 on exit code and reason against this tip, and 1/11 against revision 2.

**LOAD-BEARING WRONG-REASON PASSES: 0.** Every new probe asserts a reason string. The three
pre-existing exit-code-only assertions Mirror flagged (`N-6`) are unchanged in this revision and
remain declared, not load-bearing: Mirror verified independently that all three fire for the
correct reason.

### 4.6 · M-4 — the two modes as two contracts, and the partition measured in each

**The claim revision 5 makes, stated so it can be falsified:** *`SCANNED` and `[UNCHECKED]`
partition the present files in `verify` **and** in `verify --post-read`; each mode prints only
what its own run checked; and pre-handover a skip class the protocol does not declare is a
finding rather than a note.* Falsify it with a present file that either mode neither scans nor
names, or with a clause in one mode's `PASS` sentence that is true only of the other's run.

**The independent file universe, both modes, before and after.** `os.walk` for the population,
a planted identifier for scan membership by effect, `[UNCHECKED]` parsed for census membership;
the harness imports nothing from the module.

```
                        REVISION 4                    REVISION 5
                   --post-read  PRE-HANDOVER    --post-read  PRE-HANDOVER
PRESENT                 48           48              48           48
SCANNED                 16           16              16           16
CENSUSED                32            0              32           32
SILENT                   0           32               0            0
OVERLAP                  0            0               0            0
instrument check     PASSED       PASSED          PASSED       PASSED
```

**The same bytes at six paths, in both modes — Mirror §5A, re-run against revision 5.** The
payload is the whole of `controlled_benchmark_ab.md`, appended identically to both surfaces so
parity cannot see it.

```
                                                 PRE-HANDOVER              --post-read
CLAUDE.md                (scan_exempt_input)     PASS · NAMED ×2           PASS · NAMED ×2
benchmark/MODE_DIRECTIVE.md (scan_exempt_input)  PASS · NAMED ×2           PASS · NAMED ×2
files/…/File011.pdf      (suffix_not_scanned)    PASS · NAMED ×2           PASS · NAMED ×2
output/renders/.gitkeep  (suffix_not_scanned)    PASS · NAMED ×2           PASS · NAMED ×2
roles/scientist.md       CONTROL, scanned        FAIL · IDENTIFIER LEAK    FAIL · IDENTIFIER LEAK
output/renders/smuggled.md CONTROL, not allowed  FAIL · NOT ALLOWLISTED    FAIL · NOT ALLOWLISTED
                                                        + IDENTIFIER LEAK         + IDENTIFIER LEAK
```

Every `NAMED ×2` was `not named` at revision 4 in the pre-handover column. The two controls fail
in both modes at both revisions, which is what makes the difference attributable to the mode and
not to the payload or the invocation.

**The hostile UTF-16 case, at the gate.** `framework/eval/failure_taxonomy.md` — allowlisted,
`.md`, normally scanned — overwritten in **both** surfaces with the UTF-16 encoding of the entire
protocol text:

```
                                    REVISION 4                REVISION 5
PRE-HANDOVER verify        PASS · rc=0 · named 0×     FAIL · rc=1 · named 4× · UNANTICIPATED in
                           both sentences printed     both surfaces · census: undecodable_text ·
                                                      "pre-handover that is a finding above"
same tree --post-read      PASS · [UNCHECKED] ×2      PASS · [UNCHECKED] ×2 · EXPECTED_BY_PROTOCOL
                           undecodable_text           NO · counted separately   ← UNCHANGED
```

The post-read column is deliberately unchanged. `REV-SCIAB-MIRROR-004` §9 ruled
`EXPECTED_BY_PROTOCOL: NO` **informational** there, from the normative text, and that ruling is
not disturbed. §4.4 of the protocol now derives why the same fact blocks at the gate: §2.2 makes
Plan the surface's only writer until handover and `build` copies without templating, so a
text-suffixed file that is not text is a state `build` cannot produce — the source root carries
one, or the surface was patched, which §3 forbids by name. Post-read the writer is the reader,
who may legitimately emit UTF-16. **Who the writer is decides whether an unanticipated file is an
anomaly or an artifact**, and that premise was already in §2.2 rather than invented here.

**The positive control that proved the wrong property, repaired as a pair.**
`test_every_present_file_is_either_scanned_or_named_and_never_both` asserted constants named
`FIXTURE_…_AT_HANDOVER` and made every assertion under `--post-read`; it passed because on a
fixture with no reader output the two censuses coincide. It is now a mode-parameterised helper
with **two** public tests, `…_at_handover` and `…_post_read`, and every mode-specific test in the
suite asserts its mode on **argv and on the tool's printed `MODE` line** before reading a
population. A fixture name is nowhere evidence.

```
suite                                      71 → 83 tests, 83/83 green
new HandoverGateCensusTests                12 cases: clean-pair control, scan-fires control,
                                           census-at-the-gate, exempt-input named, non-text
                                           suffix named, 5 UTF-16 rows ×2 surfaces, the
                                           post-read informational counterpart, the UTF-8
                                           discriminator, the clean-UTF-16 state control, and
                                           the blind-spot-exempts-nothing row
DISCRIMINATION vs revision 4's tool         20 of 83 fail; with the MODE line back-ported so the
                                           witness is not the discriminator, 17 still fail on
                                           SUBSTANCE. The 3 that stop failing are the two
                                           positive controls and the post-read partition —
                                           exactly the rows that must NOT discriminate
```

**`P-7`'s boundary, corrected while using it.** `REV-SCIAB-MIRROR-004` §8 bounds `P-7` with *"it
disappears the moment the payload contains one non-ASCII character"*. It does not: UTF-16LE
encodes `—` U+2014 as `14 20`, `–` U+2013 as `13 20` and `‘ ’ “ ”` U+2018–201D as `18 20 … 1D 20`
— every byte below `0x80`, so BOM-less UTF-16 text made of them decodes as UTF-8 and is genuinely
scanned. The criterion is a **byte**, not a character. Mirror's conclusion survives its test — the
real artifacts carry `§` and `🔴` — so `P-7` remains narrow and is a scan limit, not a census
hole; it is now pinned as `test_bomless_utf16_decodes_as_utf8_unless_a_byte_exceeds_7f` with all
three rows and the BOM case, rather than left in prose. This cost the battery four red rows
before it was understood, and that is `SLR-plan-0005` L-4.

### 4.4 · Revision 1's evidence, retained

**The surface tool, exercised — two positives and six negatives, before any reader exists:**

```
build + verify, clean                                          PASS   (twice)
prior output planted in an output slot                         FAIL   4 findings, rc=1
a repository file naming the paper planted                     FAIL   2 findings, rc=1
the two MODE_DIRECTIVE files made identical                    FAIL   NOT DIFFERING
one byte appended to the text surface in B                     FAIL   PARITY BROKEN, both digests
a locator citing LEGEND's dossier + an absolute-path artifact  FAIL   OUTSIDE SURFACE, rc=1
a registry planted outside an output slot, post-read           FAIL   3 findings, rc=1
```

**🔴 Two real defects came out of running it rather than reading it**, and both are the same
shape — a check that fires on the correct case:

1. post-read, the content scan fired on the reader's **own** manifest, which must name the PMID;
2. post-read, the forbidden-path check fired on the reader's own manifest, because it lands at
   **exactly the path LEGEND's prior manifest occupies** — `deepdive_manifest.py` derives that
   path from disease and PMID and it cannot be elsewhere without breaking the validator.

Revision 1 fixed both by skipping the output slots post-read. **That fix was too wide and Mirror
was right about it (B-4):** the collision is ONE path, and the skip covered six other forbidden
paths that collide with nothing. Revision 2 exempts the **exact declared output set**, computes
the blind spot as its intersection with the forbidden list, and prints it by name on every run.
**The second defect is also the sharpest argument for §2.1** — in a checkout, the reader would be
writing its manifest on top of the prior one.

**The population enumerator, exercised:** per-line segmentation truncated every caption window at
one line, reporting **1 panel for a six-panel figure**; and a single-letter pattern read Figure 6
as `A,B,E` when the caption uses the range `(C-D)`. Both fixed — **a short denominator flatters
both readers.** The caption anomalies that are the *paper's* and not the tool's (Supplementary
Figure 1 labels `(G)` twice and never labels J) are carried into the population file as declared
notes rather than repaired.

**The validator runs inside a built surface**: `deepdive_manifest.py` imports `corpus_firewall`
and refuses an absent manifest with the expected `BLOCK`.

**Repository validators, at the content tip:**

```
legend_lint.py .                        PASS  (1 pre-existing INFO)
fulltext_receipts.py verify             OK — 128 chained receipts, tail anchored
growth_anchors.py check                 PASS — claims=39 · papers=70 · corpus=356 · literature=390
public_release_gate.py                  PASS / BLOCKS: 0
governance_fingerprint.py compose --all  4 roles composed; 1 rotated, 3 identical
candidate_content_hash.py               identical on two runs, and at the later control-plane commit
```

**🔴 The publication gate found a real defect and is the reason it is not in the diff.** It
returned **18 BLOCKs** on the benchmark instruction files: their relative links resolve inside a
surface and not in the repository where they are authored. Rewritten as plain paths, with the
reason stated in the file — *a link that resolves in one place and silently misleads in the other
is worse than no link.*

**~~`run_release_regressions.py` — `FAIL`, and it fails identically at `BASE_HEAD`. Eight
suites…~~** — 🔴 **WITHDRAWN. This assertion was wrong, and §4.2 replaces it.** It compared
counts, never sets; the eight were never enumerated; the count itself was environmental (a clean
checkout has six); and it concealed **two candidate-introduced failures**. The handoff that
opened this work carries the rule *"an enumerated set is falsifiable, a bare integer is not"*, and
this was the one claim that rule existed for. Kept struck through rather than deleted: a wrong
number that quietly disappears is a wrong number nobody can audit.

---

## 5 · What this candidate does NOT do

Execute itself · move `main` · take a lease · start `BENCH-AB-001` · register anyone · verify a
capability · lift the L2 suspension · issue a Task Contract · fix `scientist-c`'s ACTOR_ID ·
amend any governance text · touch a `*_current.md`, the receipt ledger, or any registry ·
promote the four intermediate fields into the claim registry · integrate any benchmark claim ·
build the registry validator or the P7 ledger · repair the approval queue, the ACK criteria or
the Plan→Mirror routing · ratify Mirror's methodology observation · add a Metacognition Agent ·
benchmark Scientist C · name a second paper.

**Open debts carried forward, none silently resolved:** registry validator (MISSING INSTRUMENT) ·
P7 (OWED, NOT BARRED) · approval queue non-canonical · ACK criteria · Plan→Mirror routing ·
Mirror's methodology observation (UNRATIFIED) · lease expired between turns (detectable, not
prevented) · `DEBT-20260818-LEASE-SNAPSHOT` · C-9 clauses accepted and unadopted, `runtime/`
classification open · L2 suspended · **six** failing release suites carrying **seven** failing
tests, enumerated in §4.2. *(Mirror N-5: this line read "eight failing release suites" through
revision 2 — the withdrawn revision-1 number surviving in a second place. It is corrected here,
and it now names tests as well as suites, because M-1 is the demonstration that a suite count is
the wrong object for this claim.)*

**No `HUMAN_APPROVAL` is pre-filled. None exists and none is implied.**

### Scope-creep check, stated so a reviewer can falsify it

The only executable added is `benchmark_input_surface.py`. It reads a spec, copies an allowlist,
digests files, and enumerates captions. It does **not** read the Agent Card registry, the runtime
inventory, the receipt ledger, the claim registry, or any `*_current.md`:

```
grep -c agent_card  → 0      grep -c _current  → 0
grep -c registry    → 0      grep -c receipts  → 0
```

Every file in the diff is named by a clause of the handoff, and §2 gives the clause for each.

---

## 5b · Recorded findings R-1 … R-12 — classified, none ignored

| # | Finding | Class | What was done |
|---|---|---|---|
| **R-1** | `ASSIGNMENT.template.md` does not exist; the manifest digest is promised "in each actor's `ASSIGNMENT.md`" and is in neither | **FIX_IN_THIS_REVISION** | §6 names the two concrete files; the digest moves to the freeze receipt as `INPUT_MANIFEST_SHA256`, where it binds the manifest to the pass that ran under it. `build` copies, it does not template — so nothing promises templating |
| **R-2** | both readers hold `scientist_reading_modes.md` §4–§5 and can read the other's mode; *"do not speculate"* is vacuous | **FIX_IN_THIS_REVISION** | §0 now carries it as caveat **2 of 2**, beside session variance: the variable is *which directive is addressed to you*, not knowledge of the modes. Declared as a **known contamination**, not softened |
| **R-3** | `BOOTSTRAP.md` asserts A and B *"are already fixed"* in the past tense | **FIX_IN_THIS_REVISION** | now *"become fixed on canonical execution of …, with the operator's approval"*, matching `roles/scientist.md` |
| **R-4** | `PARALLEL_READ_GROUP` extends the Annex A.1 schema by protocol, unnamed as an extension | **FIX_IN_THIS_REVISION** | named as an **extension field** where rule 2 introduces it, standing on A.1's *extendible, never removable*; promotion into Annex A declared a separate governed change |
| **R-5** | MODE A's *"a critique you volunteer is not what is being measured"* is a demand characteristic | **FIX_IN_THIS_REVISION** | rewritten: what is excluded is the **systematic apparatus**, not the observation. The three fields are named as required, with *"do not suppress an observation because it reads as critical"* |
| **R-6** | the Methods "pattern" is an enumeration; *"a function of (spec, source)"* is true only trivially | **ALREADY_RESOLVED_BY_BLOCKING_FIX** (B-1) | the enumeration is gone; selection is by typography, and the claim is now true non-trivially |
| **R-7** | `verify` requires exactly two actors; a three-arm benchmark needs a tool change | **DOCUMENT_AND_CARRY** | said at the refusal site: the cost is declared where it is paid, rather than discovered |
| **R-8** | canonicalization ground 3 is circular — PID-12's *confirmed at registration* path exists independently | **FIX_IN_THIS_REVISION** | marked ⚠️ in §9 as **the weakest of the four and not load-bearing**; grounds 2 and 4 each decisive alone |
| **R-9** | the manifest repeats `36 / 115`, which B-1 changes | **ALREADY_RESOLVED_BY_BLOCKING_FIX** (B-1) | new counts recorded; the old pair kept under `_superseded_counts` with the reason, because a count that vanishes cannot be audited |
| **R-10** | `plan_defined_parameters.md` is stale on branch `mirror` (P5 v3) | **OUT_OF_SCOPE_DEBT** | Mirror's own worktree; Plan may not write there. Recorded, not touched |
| **R-11** | the freeze ordering rule has no mechanism | **FIX_IN_THIS_REVISION** | labelled `PROCEDURAL` in §7 with the full `GUARANTEE / FAILURE / DETECTION / RECOVERY` block, the way `runtime/orchestrator_lease.md` labels its own. Detection is **after the fact, never prevention** |
| **R-12** | "byte-identical" refers to the handoff **body**; hashing the file gives a different value | **FIX_IN_THIS_REVISION** | the `carried_from` block now says exactly that, so a reviewer who hashes the file is not reading a discrepancy |

Nothing here silently fixes an unrelated governance debt, and no R finding became material
enough to change a blocking remedy.

### 5b.2 · `REV-SCIAB-MIRROR-002`'s nine recorded findings — what revision 3 did with each

The remediation was scoped to M-1 and M-2. Where a recorded finding is a **false sentence in this
manifest**, it is corrected here, because a manifest whose numbers are wrong is not a smaller
problem for being non-blocking. Where it is a change to content outside the two findings, it is
carried and named, not smuggled into a targeted revision.

| # | Finding | Class | Revision 3 |
|---|---|---|---|
| **N-1** | `surface_spec.json` `notes` (6) and the File012 rule `_note` contradict each other about label normalization | **CARRIED** | not touched. The output is as printed and `notes` (6) is the correct one; the fix is one word in a note and belongs with the next change to that rule, not inside an M-1/M-2 revision |
| **N-2** | `declared_empty_sources` is accepted on declaration and never measured | **CARRIED — REAL** | not touched, and it is the strongest of the nine: a declared-empty source shortens the denominator and a short denominator flatters both readers. Named here so it cannot be read as closed |
| **N-3** | for a PDF the regex segment is one page, so a caption crossing a page break is truncated | **CARRIED — LATENT** | not touched; no caption in this packet crosses a break, Mirror checked all ten. The bound is real and unstated, and it becomes live on the next paper |
| **N-4** | §3G still states the superseded `36 / 115` | **FIXED** | §3G, above — with the superseded pair named as superseded |
| **N-5** | §5 says "eight failing release suites" while §4.2 enumerates six | **FIXED** | §5, above — corrected to six suites and seven tests |
| **N-6** | three suite tests assert an exit code with no reason | **CARRIED — DECLARED** | not touched. Mirror verified independently that all three fire for the correct reason, so none is load-bearing; every probe **added** at revision 3 asserts a reason |
| **N-7** | Mirror cannot reproduce Plan's differential counts | **RECORDED, NOT RECONCILED** | Mirror's numbers are measured, Plan's explanation is inferred, and revision 3 did not re-run revision 1's tool to settle it. §4.3 now carries both |
| **N-8** | `locators` is purely lexical: a symlink under the produced prefix is cited and passes | **CARRIED — CONTAINED** | not touched. `verify` reports the symlink and `freeze` refuses the tree outright; the M-2 change does not reach `locators`, and saying it did would be the exact overclaim M-2 is about |
| **N-9** | the population completeness failure exits 1 while the spec `_note` says "REFUSES" | **CARRIED** | not touched — a vocabulary correction in a note, with the same reasoning as N-1 |

**Two are fixed and seven are carried, and the split is not convenience.** N-4 and N-5 are false
statements in this document about its own evidence, which is what §9 of the remediation asks to
be true. The other seven require edits to content that neither finding touches, and a targeted
revision that also repairs a caption bound or a completeness check is no longer targeted — it is
a revision Mirror would have to review from R-1 across a wider surface, for defects it has
already classified as non-blocking.

### 5b.3 · `REV-SCIAB-MIRROR-003` — the carried nine at revision 4, and the five it recorded

Revision 4 touches four content files, none of which is the file any carried finding lives in.
**Nothing below is marked resolved by `M-3`'s repair**, and the one finding whose status could
plausibly have moved is stated with why it did not.

| # | Mirror's class at rev 3 | Revision 4 |
|---|---|---|
| **N-1** | NON-BLOCKING CARRIED | **CARRIED.** `surface_spec.json` is edited by this revision — two `_note` blocks, both about the census — and the File012 `notes` contradiction is **not** among them. Deliberately: it is a one-word fix in an unrelated rule and belongs with the next change to that rule |
| **N-2** | NON-BLOCKING CARRIED — reproduced | **CARRIED, unchanged.** `cmd_population` is byte-identical to revision 3. A declared-empty source is still accepted on declaration; the finding goes live the moment a second entry is added |
| **N-3** | NON-BLOCKING CARRIED — latent | **CARRIED.** `_pdf_pages` / `_regex_units` byte-identical |
| **N-4 · N-5** | RESOLVED | remain resolved; §3G and §5 are untouched by this revision |
| **N-6** | NON-BLOCKING CARRIED — declared | **CARRIED.** The three exit-code-only assertions are untouched. Every probe added at revision 4 asserts a class or a reason string |
| **N-7** | UNRESOLVED, honestly labelled | **CARRIED, still unreconciled.** Revision 4 did not re-run revision 1's tool either. Neither side has moved and neither pretends it has |
| **N-8** | NON-BLOCKING CARRIED — contained | **CARRIED, and `M-3` does not change its status.** Verified structurally rather than asserted: `cmd_locators` is **byte-identical** between `bdac30f` and this tip, as are `cmd_freeze`, `cmd_verify_freeze`, `cmd_population`, `_classify`, `cmd_build`, `_is_expected_output`, `_is_decodable_text`, `iter_files`, `iter_symlinks` and `tree_digest`. Only `cmd_verify` and `unchecked_surface` changed, and one function was added. A census cannot reach a lexical path check, and claiming it did would be the overclaim `M-2` was about |
| **N-9** | NON-BLOCKING CARRIED | **CARRIED.** Vocabulary in a note, same reasoning as N-1 |

| # | Recorded at revision 3 | Revision 4 |
|---|---|---|
| **P-1** | the `M-1` guard's `INSTRUCTION_SURFACES` globs do not cover `framework/eval/benchmarks/*/instructions/*.md` | **CARRIED, not fixed.** Mirror states it is *not a candidate defect* — the obligation is semantically carried in all three files and the globs are `BASE_HEAD`'s. Widening a guard that `BASE_HEAD` owns is a change to another candidate's file inside a revision scoped to one finding. Recorded here so its owner inherits it rather than rediscovers it |
| **P-2** | §4.1b's ordering argument is sound for Plan and one premise short of the general claim | **ACCEPTED and stated.** The missing premise is that Plan's only durable branch is the candidate branch; Mirror's own records take the other route. §4.1b now says so |
| **P-3** | `N-6`'s three exit-code-only assertions fire for the right reason | **CARRIED**, none load-bearing |
| **P-4** | `verify` never compares an allowlisted input to `build --emit-digests`' record; parity cannot see a change applied identically to both surfaces | **CARRIED and now STATED, not closed.** It is the residual on every `scan_exempt_input` census line and in §4.5 of the protocol. Closing it is a new check, and this revision was given one finding. It is the cheapest available closure of the input half and the next revision's obvious first move |
| **P-5** | `N-7` remains unreconciled | **CARRIED** — see N-7 |

---

### 5b.4 · `REV-SCIAB-MIRROR-004` — the carried findings at revision 5, and the three it recorded

Same rule as 5b.2 and 5b.3: a false sentence **in this manifest** is corrected here; a change to
content outside the one finding is carried and named, never smuggled into a targeted revision.

| # | Class at revision 5 | What revision 5 did |
|---|---|---|
| **P-4** | **CARRIED, STATED, NOT CLOSED** | `verify` still takes no digest input — re-verified by AST: `cmd_verify` contains zero references to `emit_digests`. Every hostile probe in this revision made the identical-edit-to-both-surfaces move, and parity was silent in every one, **as declared**. `M-4`'s remedy does not touch it and this revision claims nothing about it. The `scan_exempt_input` census line still scopes its own coverage claim to *"a change made to one surface only"* |
| **P-6** | **CARRIED — printed-claim half addressed, exclusion unchanged** | `iter_files` is byte-identical, so `.git/**` is still outside both populations. What changed is that the partition sentence no longer leaves its own scope unstated: both modes now print *"`Present` is every regular file in the surface tree outside `.git/`, which iter_files() excludes from both populations."* The finding is **not** closed — a forbidden artifact under `.git/` is still invisible to `verify` and to `freeze`, and Mirror is right that it is pre-existing |
| **P-7** | **CARRIED — boundary corrected, residual unchanged** | the residual stands: BOM-less UTF-16 whose bytes are all below `0x80` decodes and is genuinely scanned. Its stated boundary does not: `—`, `–` and the curly quotes are non-ASCII and encode below `0x80`. Now an executable test with three rows plus the BOM case. §4.6 |
| **P-8** | **FIXED** | the front matter said *"Four content files changed"* while five changed. Revision 5 changes five — four edited, one added — and the front matter says so, naming the added record as the entry that moves the hash |
| **N-1** | **CARRIED** | `surface_spec.json` is edited at this revision — one `_note` block, about the census in both modes — and the File012 normalization contradiction is again not among them. Named so it cannot read as closed |
| **N-2** | **CARRIED, unchanged** | `cmd_population` byte-identical, verified by AST segment. `declared_empty_sources` is still accepted on declaration |
| **N-3** | **CARRIED, latent** | `_pdf_pages` and `_regex_units` byte-identical, verified |
| **N-6** | **CARRIED, declared** | no exit-code-only assertion was added. Every one of the twelve new probes asserts a reason, a class or a population, and the mode |
| **N-7** | **UNRESOLVED, honestly labelled** | fourth review running. Revision 5 did not re-run revision 1's tool either. A measured number and an inferred explanation still face each other |
| **N-8** | **CARRIED, contained** | `cmd_locators` byte-identical. A census reaching further into `verify` cannot reach a lexical path check in another subcommand, and claiming it did would be the overclaim `M-2` is about |
| **N-9** | **CARRIED** | vocabulary in a note, untouched |
| **P-1** | **CARRIED, not fixed** | `BASE_HEAD`'s guard, not this candidate's defect |
| **P-3 · P-5** | **CARRIED** | see N-6 and N-7 |
| **R-1 … R-12** | not reopened | `R-10` remains Mirror's own worktree debt and Plan may not write there |
| **M-1 · M-2 · M-3** | **RETESTED, NOT REOPENED** | M-1: `test_locator_obligation_reaches_every_route.py` and `roles/scientist.md` untouched at this revision; §5.1 of the protocol has zero lines in the revision-5 diff; its one failing test is one of the seven that fail identically at `BASE_HEAD`. M-2: the smuggled decodable file under the render prefix is `NOT ALLOWLISTED + IDENTIFIER LEAK` in **both** modes, and a clean decodable file there is `NOT ALLOWLISTED`. M-3: `SILENT 0` in `--post-read`, re-measured with the independent oracle, and the six census classes are unchanged because `SCAN_SKIP_CLASSES` and `scan_skip_reason` are byte-identical |
| **freeze** | **RETESTED, NOT REDESIGNED** | `cmd_freeze`, `cmd_verify_freeze` and `_classify` byte-identical, and — verified by AST rather than by reading — **none of them calls either changed function**, so there is no interaction surface to regress. Live re-run on the real surface: 29 fields, `SURFACE_ABSOLUTE_PATH` not recorded, outputs 0, unexpected 0, symlinks 0; `verify-freeze` PASS on the untouched tree; the wrong-actor-id negative control refuses with `scientist-a` read from `ASSIGNMENT.md` inside the tree |

**Nothing here is marked resolved by `M-4`'s repair.** `P-8` is the only closure, and it is a
number in this manifest rather than a property of the system.

## 5c · The session-routing debt — named, not resolved

A real gap exists between **stable `ACTOR_ID`** and **current routable `SESSION_REF`**:
supersession, deterministic `SendMessage` routing, `CURRENT`/`ROUTABLE` semantics. This session
observed it directly — it can establish that it is an incarnation of stable actor `plan`, and it
**cannot** observe its own routing reference, so it declares none.

**It is out of scope for this candidate and nothing here addresses it.** No session registry, no
supersession, no routing validator, no change to `SendMessage` resolution. It is recorded so that
its absence is a decision rather than an oversight, and it is not mixed into this review object.

---

## 6 · What Mirror is asked to verify

Independent review of the binding **and** the content, **from R-1**. **No prior attestation
transfers** — including `M-1`'s closure, `M-2`'s closure, `M-3`'s closure in `--post-read` and
every row `REV-SCIAB-MIRROR-004` passed, the fourteen rows `-002` re-tested, and the ten `-001`
found acceptable. The content they were found acceptable over no longer exists.

### 6.0000 · Revision 5 — the one finding, and the claim it was about

**The claim:** *`SCANNED` and `[UNCHECKED]` partition the present files in **both** `verify`
modes; each mode's `PASS` sentence states only what that run checked; and pre-handover a skip
class the protocol does not declare is a finding, not a note.*

**Attack it here, in this order:**

1. **The mode the claim is measured in.** Every number in §4.6 is labelled with a mode. Re-derive
   both — the pre-handover one is the one that did not exist at revision 4. The falsifier is a
   present file that `verify`, in *either* mode, neither scans nor names. I probed 48 by effect
   in each mode and found none; the instrument check (`roles/scientist.md` must leak) passed in
   both, and if it does not pass in yours, no negative in that run is evidence.
2. **The derivation in §4.4, not the behaviour.** `EXPECTED_BY_PROTOCOL: NO` blocks pre-handover
   and is informational post-read. I did **not** transfer your §9 ruling in either direction: the
   post-read half is yours and is unchanged; the pre-handover half is derived from §2.2's
   single-writer rule plus `build` doing no templating plus §3's *rebuilt from the spec, never
   patched*. If that derivation does not hold, the blocking behaviour is an invented security
   guarantee and should be struck — which is the objection I most want run.
3. **Whether the remedy is the sentence.** Your `EVIDENCE_NEEDED` offered scoping the sentences
   instead. I refused it, and the refusal costs a weakened guarantee row either way if I am
   wrong; §4.0aaa states the reasoning and `SLR-plan-0005` L-2 states it again from the learning
   side. Both are offered to be attacked.
4. **The positive controls, in the mode they name.** The instrument that found `M-4` was already
   in the suite, pointed at the other mode, asserting constants named for this one. Check that
   the repair is not the same shape one level up: every mode-specific test asserts its mode from
   the tool's printed `MODE` line **and** from argv, before it reads any population. Redirect one
   and see it fail.
5. **The discrimination, not the green.** 83/83 pass here; 17 of them fail against revision 4's
   tool *with the `MODE` line back-ported*, so the failures are on substance rather than on the
   new witness. The three that do **not** discriminate are the two positive controls and the
   post-read partition — verify that those three are exactly the ones that must not.
6. **`P-7`'s corrected boundary.** §4.6 asserts your §8 conclusion survives while its stated test
   does not. If `—` U+2014 in BOM-less UTF-16LE is undecodable on your platform, my correction is
   wrong and the test that pins it should fail for you.
7. **The regression numbers, and my two harness defects.** §4.2 records both, and the count that
   reconciles with yours is the corrected one. If your seven and my seven are the same seven for
   the same reasons, that is two independent instruments agreeing on the set and not only on the
   number.

### 6.000 · Revision 4 — the one finding, and the claim it was about

```
M-3  the reproducer    append framework/protocols/controlled_benchmark_ab.md to CLAUDE.md in
                       BOTH surfaces and run verify --post-read. At revision 3 it printed
                       VERDICT: PASS with no mention. It must now PASS and print CLAUDE.md
                       under [UNCHECKED] as scan_exempt_input. The same at
                       benchmark/MODE_DIRECTIVE.md. The controls must not move:
                       roles/scientist.md → IDENTIFIER LEAK, output/renders/smuggled.md → 4
                       findings. Plant into BOTH surfaces — one surface only is caught by
                       PARITY BROKEN, which is a different check answering.
M-3  the population    derive the skip conditions from the code, not from this manifest and
                       not from your own review. §4.5 claims six classes out of four
                       predicates and SILENT = 0 on a clean build. I measured sixteen silent
                       files per surface where -003 reported ten, and found a fourth class
                       (undecodable_text) no review had named. Is there a fifth? The claim to
                       attack is that scan_skip_reason() has no exit that reaches `continue`
                       without a census line.
M-3  the partition     the PASS sentence now says SCANNED and [UNCHECKED] partition the present
                       files. Construct a file that is in both, or in neither. The behavioural
                       test asserts exactly this and it is the one to distrust first.
M-3  the oracle        test_the_census_is_exactly_the_present_files_the_scan_did_not_read uses
                       a hand-written literal, and
                       test_every_present_file_is_either_scanned_or_named_and_never_both
                       measures the scan by planting an identifier and watching for the
                       finding. Neither should reproduce the implementation's filter — check
                       that, because the test this replaces did, and that is why it agreed
                       with the defect. Is the anti-vacuity guard real, or does the scanned
                       set have some other way to be non-empty?
M-3  the truthfulness  the census says a scan_exempt_input "still took the allowlist check".
                       Verify the contract test behind that sentence, and verify the freeze
                       claim: freeze reports unexpected 0 on a tampered CLAUDE.md — is that
                       correct classification or a second blind spot? I claim correct, because
                       the digest is in FILES and verify-freeze catches any later change.
M-3  what I did NOT do  P-4 is stated, not closed: verify still ignores build --emit-digests,
                       so a change applied identically to both surfaces is seen by nothing at
                       verify time. Is stating it enough, or does the census line overclaim by
                       naming parity at all?
```

### 6.00 · Revision 3 — the two findings, and the two claims they were about

```
M-1  the exact test    run test_every_route_carries_the_obligation_or_declares_an_exemption
                       alone at cbce3016 and at b634829. It was green at base and red at
                       daaa3335; it must now be green at both. If it is not, this fix failed.
M-1  test-level delta  re-derive FAILING TESTS, not FAILING SUITES, at both tips, and compute
                       both differences. §4.2 claims ADDED = 0 over 7 shared. Attack the
                       harness too: does it parse subTest failures, ERRORs and a suite that
                       dies before any test runs? A parser that under-reports failures makes
                       this claim by omission.
M-1  same-reason       over all seven shared tests, not one. The normalization is declared in
                       §4.2 and removes paths, temp dirs, line numbers, times, addresses — and
                       no assertion text. Is a semantic change being normalized into agreement?
M-1  the semantics     is `controlled_benchmark_ab.md` genuinely a route that carries the
                       obligation, or was an EXEMPT entry the honest answer? §5.1 argues the
                       first. And is §5.1 a real obligation or a token placed to satisfy a
                       grep? The guard is untouched — verify that too:
                       `git diff main b634829 -- scripts/test_locator_obligation_*.py`
M-2  the smuggle       copy a forbidden file to output/renders/smuggled.md and run
                       verify --post-read. It must FAIL with NOT ALLOWLISTED and IDENTIFIER
                       LEAK — the same two findings the same bytes produce one directory away.
M-2  the census        is the printed [UNCHECKED] list really the whole unchecked surface?
                       Construct a file that verify --post-read neither checks nor names.
                       That is the guarantee of §4.5 and it is one command from falsified.
M-2  the prefix rule   the exemption is now on undecodable bytes. Attack it: a UTF-16 render,
                       a zero-byte file, a decodable file with a binary-looking name, a
                       symlink whose realpath is prior output (N-8, unchanged and declared).
M-2  legitimate use    does a real render still pass? Is any scientific functionality lost by
                       refusing a text file under output/renders/? The instructions now say
                       renders are images — is that visible to the reader before the reading?
M-2  freeze            re-run the B-3 tamper battery, and check the freeze interaction: a
                       decodable file under the prefix must be UNEXPECTED, a render must not.
M-2  reason discipline every new probe asserts a reason token. Find one that would pass for
                       the wrong reason — that is the defect Mirror's own harness committed.
N-4 · N-5              §3G and §5 are corrected. Are any other superseded numbers still alive
                       in this manifest?
     binding           reproduce 570fcbbb… at the content tip a3cad1d and at every later
                       control-plane commit, and verify it is NEITHER c0701094… (revision 2)
                       NOR 7cef4ccc… (the superseded revision-3 tip b634829) — a content
                       change that left the hash alone would be the more serious finding.
                       Both superseded values are declared in §1; check that no third place
                       in this document still presents either as current.
     SLR ordering      §4.1b argues that §15 + E.6 + P5.1 + D.2 REQUIRE the Session Learning
                       Record inside the reviewed population rather than after it. Attack the
                       reading: is §15's trigger really session closure? Is there a
                       review-safe mechanism the argument missed? And is SLR-plan-0003
                       truthful about this session — in particular L-5, which records that
                       Plan first proposed to defer this very record, and L-1, which says the
                       suite's own positive control asserted the M-2 defect as correct
                       behaviour. E.2 gives you the curation: every CONFIRMATION_CLASS in it
                       is proposed, and two are filed as REPLICATION of your own patterns.
```

### 6.0 · Revision 2 — retest these first, none of it transfers

```
B-1  population        the caption bound, the typographic Methods derivation, the four
                       recovered sections (one of which Mirror's own heuristic missed),
                       the four new kinds, the declared-empty refusal. Re-derive; compare
                       to evidence_units.json byte for byte.
B-2  delta regression  SUPERSEDED BY M-1 above — the suite-set answer was the finding. Read
                       §4.2, which now answers it at test granularity.
B-3  freeze receipt    freeze A's tree as scientist-b. Tamper after freezing. Point a receipt
                       at the other actor's tree. Does anything pass that should not?
B-4  post-read         plant each of the six previously-skipped forbidden paths. Symlink,
                       `..`, absolute. The blind SPOT is still one path; the unchecked
                       SURFACE is not the blind spot — see M-2 above and §4.5.
B-5  benchmark fields  re-count the registry. Are the seven right, is `Locators` correctly
                       classified apart, and do §3.6 / §5.3 / the schema now agree?
R-*  affected findings §5b above — each classification is Plan's and each is attackable
     depth             did any of this buy tooling cleanliness with scientific coverage?
     scope creep       19 content files, five edited at revision 3. Is any change outside
                       M-1, M-2, N-4 and N-5?
```

### 6.1 · The seventeen from revision 1, still open

The seventeen the operator named, each with where to look:

```
 1  A/B separation is real                     scientist_reading_modes.md §0, §4, §5
 2  stable identity vs session routing         §1.2, §1.3 — and the task record, which declines
                                               to assert a session ref for plan
 3  duplicated-assignment rule                 §2 — is "detectable" the honest verb?
 4  A vs B scientific-role distinction          §4 vs §5.2 — is B's addition real, or A restated?
 5  B ≠ Mirror                                  §5.4 — four rows; is any of them wrong?
 6  reuse of the existing data model            §6.1 — measured; re-measure it
 7  no parallel claim schema                    §6.3 + OUTPUT_SCHEMA.md §6
 8  genuine benchmark-only extensions           §6.2 — SEVEN promoted (rev 2). The three
                                               refusals were wrong and are withdrawn; attack
                                               the promotion now, and §6.3's measurement
 9  blind input surface enforceable             controlled_benchmark_ab.md §2, §4 — and run the tool
10  input parity                                §3, §4.1 — the four negative parity cases
11  prior-output exclusion                      §4.3 — including the post-read blind spot, which
                                               is declared rather than closed
12  frozen first passes                         §7 — freeze BEFORE reading; is the ordering real?
13  evaluation population ex ante                §8.1 + population/evidence_units.json
14  no reduction of scientific depth             MODE_A/MODE_B "do not compress for budget";
                                               BENCHMARK_INSTRUCTIONS §3
15  no speed/token/cost as quality proxy         §8.4, §8.5
16  no scope creep                               §5 above, with a falsifiable check
17  canonicalization dependency                 §9 — four grounds; is the fingerprint one right?
```

**Three things to attack first, because Plan is the wrong actor to judge them:**

1. **Does `PARALLEL_READ_GROUP` actually distinguish intent, or does it only record it?** A group
   name written into both contracts by the same assigner who duplicated them proves nothing. Plan
   believes the answer is that it makes duplication *visible* and cannot make it *impossible* —
   and cannot see from here whether the spec's wording claims more than that.
2. ~~**Are the three refused fields genuinely covered by labelled prose?**~~ **ANSWERED, against
   Plan.** They were not: 0/39, 0/39, 0/39. Plan *measured the practice and judged the
   convention adequate*, and the measurement it should have made — counting the label — it did
   not make. The question to put in its place: **are seven fields now one too many?** If
   `Contradictory evidence` and MODE B's contradiction axis are the same object under two
   nouns, the promotion has bought comparability with a duplicated concept, and Plan is again
   the wrong actor to see it.
3. **Does §0 of the benchmark protocol admit enough?** One paper, one session per actor: the
   design cannot separate the mode from session variance. It is stated in the opening section.
   If it still reads as a controlled experiment whose result will mean more than that, the
   wording has failed and Plan cannot see it from here.
