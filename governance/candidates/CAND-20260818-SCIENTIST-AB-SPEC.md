---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260818-SCIENTIST-AB-SPEC
revision: 3
supersedes: revision 2 (content tip daaa3335, hash c0701094…21bcf) — REQUEST CHANGES under
  REV-SCIAB-MIRROR-002; and revision 1 (content tip b965ca58, hash 3b568aae…916c75) — REQUEST
  CHANGES under REV-SCIAB-MIRROR-001. No verdict, finding or PASS from either review transfers
  to this content: a revision is reviewed from R-1 (CHK-mirror-0004 RESUME_RULE). That includes
  the fourteen rows REV-SCIAB-MIRROR-002 §5 re-tested and passed.
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-19
state: READY FOR MIRROR REVIEW (revision 3) — no approval requested, granted or implied
scope: HANDOFF-20260818-SCIENTIST-AB, as transmitted. Not reduced and not widened. Revision 3
  adds no scope: it repairs M-1 and M-2, corrects the manifest sentences those findings made
  false, and touches nothing else. No architecture was redesigned and no passed row reopened.
---

# INTEGRATION_CANDIDATE — the definitive Scientist A / Scientist B specification

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260818-SCIENTIST-AB-SPEC
REVISION:                   3
BASE_HEAD:                  cbce30168091f7769c56c4f019055fa55fd0d66a
BRANCH:                     scientist-ab-spec
CONTENT_TIP:                a3cad1d… — the Session Learning Record, which is the last content
                            commit of this revision; see the block below for the reproduced
                            value at every tip
SUPERSEDED_REV3_TIP:        b63482978dab13383177ed60ab55f4ca29fb1ed3   (the M-1/M-2 remediation
                            commit — a revision-3 content tip, superseded WITHIN revision 3)
SUPERSEDED_REV3_HASH:       7cef4cccb6684ef39cd6e17f605d396b2a1ad62a52c5d2c1413d64f97a794596
                            # 🔴 Declared, then superseded by a content commit of this same
                            # revision. learning/ is CONTENT by intent (P5.1) and the Session
                            # Learning Review is owed by §15 at session closure, so the record
                            # had to enter the population BEFORE review: Annex D.2 binds an
                            # approval to CANDIDATE_CONTENT_HASH + BASE_HEAD and any material
                            # change invalidates it. Writing it afterwards would have had
                            # Mirror review a population that is not the one carried forward.
                            # Not preserved for convenience; recorded so the supersession is
                            # visible rather than quiet.
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
CANDIDATE_CONTENT_HASH:     570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
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
MIRROR_REVIEW:              REV-SCIAB-MIRROR-002 → REQUEST CHANGES, on revision 2 (M-1, M-2,
                            nine recorded). Revision 3 requires a NEW independent review from
                            R-1. No PASS, no PRESERVED and no CONFIRMED from that review — or
                            from REV-SCIAB-MIRROR-001 — transfers to this content, including
                            the fourteen §5 rows revision 2 was found to have got right.
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
EXPECTED             570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
OBTAINED (run 1)     570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
OBTAINED (run 2)     570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
OBTAINED (run 3)     570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
OBTAINED at the control-plane commit carrying this revision
                     570fcbbbc7439a4dfa3bddaefa1166ce7e92fa280948a43851b9bef12ab78ab7
```

**Recomputed without the script**, from P5.1 and P5.2 directly — `git ls-tree -r --full-tree`,
the three declared roots removed, path-sorted, `legend-candidate-v4\n` + `BASE_HEAD\n` + every
entry newline-terminated:

```
at a3cad1d (CONTENT TIP)                 570fcbbb…8ab7     included 524 · excluded 29
POSITIVE CONTROLS, same route
at b634829 (superseded rev-3 tip)        7cef4ccc…4596     included 523 · excluded 28
at daaa3335 (revision 2)                 c0701094…21bcf     included 523 · excluded 27
```

The controls are the point: a second implementation that reproduces the **published** hashes of
the earlier tips is a second implementation, and one that only agrees with itself is one. Neither
`7cef4ccc…` nor `c0701094…` is the binding of this candidate, and the three values above are why.

**The one entry that separates `570fcbbb…` from `7cef4ccc…`** is
`learning/plan/SLR-plan-0003.md` — 523 included entries becomes 524. That is `learning/` being
CONTENT by intent (P5.1) rather than by omission, behaving exactly as the declaration says it
must, and it is the third Plan record to exercise it (`SLR-plan-0001` @ `05cdeda`,
`SLR-plan-0002` @ `b9af54e`, whose commit message states the same consequence).

The invariance across the content tip and every later control-plane commit is the property that
makes `MANIFEST_TIP` informational, and it is **measured at each point, never asserted**.

Domain counts are **outputs of that command at that tip**, never constants maintained here —
read them from `--show-domain`.

---

## 2 · File list and classification

| File | Status | Domain | Classification |
|---|---|---|---|
| `framework/protocols/scientist_reading_modes.md` | **added** | CONTENT — hashed | **NORMATIVE** — reading modes, actor identity of A and B, task-ownership rule |
| `framework/protocols/controlled_benchmark_ab.md` | **added**, modified **(rev 3)** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — normative for the benchmark it defines, and for nothing outside it. **Rev 3:** new §5.1 carries the verbatim-locator obligation into the route that instructs the reading (M-1); §4.3 and the guarantee table state what `--post-read` leaves unchecked (M-2) |
| `framework/scripts/benchmark_input_surface.py` | **added**, modified **(rev 3)** | CONTENT — hashed | **NORMATIVE (tooling)** — it decides whether a surface may be handed over; it is not documentation. **Rev 2: substantially rewritten**; **rev 3:** the prefix exemption is written on bytes rather than position, and the unchecked surface is enumerated from the tree — see §4.5 |
| `framework/scripts/test_benchmark_input_surface.py` | **added (rev 2)**, modified **(rev 3)** | CONTENT — hashed | **NORMATIVE (tooling)** — **59** probes, one per clause of every PASS sentence, each null finding with a positive control. Rev 3 adds fourteen and repairs a fixture whose "render" was a markdown file |
| `scripts/run_release_regressions.py` | modified **(rev 2)** | CONTENT — hashed | **DOCUMENTATION/INFRA** — one line: the new suite registered in the battery, which `test_release_runner_verdict.py` requires of every tracked test file |
| `roles/scientist.md` | modified | CONTENT — hashed | **NORMATIVE** — `actor_id_status` front matter + the *Reading modes* section. 🔴 In the `CORE` fingerprint set |
| `BOOTSTRAP.md` | modified | CONTENT — hashed | **NORMATIVE** — records that A and B are fixed and C is not |
| `framework/protocols/index.md` | modified | CONTENT — hashed | **DOCUMENTATION** — two rows in the protocol table |
| `framework/eval/README.md` | modified | CONTENT — hashed | **DOCUMENTATION** — the reader-benchmark axis, and what it does not have |
| `framework/eval/benchmarks/BENCH-AB-001/surface_spec.json` | **added**, modified **(rev 3)** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the allowlist; a command reads it, a reviewer reads the same file. **Rev 3:** `_expected_output_prefix_note` states what the prefix admits and why, and the note claiming a blind spot "cannot widen a silent one" is corrected where it was false |
| `…/benchmark_manifest.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the experiment record, `PREPARED — NOT FROZEN` |
| `…/population/evidence_units.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the ex-ante evaluation population, derived by command |
| `…/instructions/` ×7 | **added**, one modified **(rev 3)** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — surface router, common instructions, output schema, `MODE_A`, `MODE_B`, and the two per-actor assignments. **Rev 3:** `BENCHMARK_INSTRUCTIONS.md` §1 tells the reader that `output/renders/` holds image files — before the reading, so the rule is a rule and not a trap |
| `learning/plan/SLR-plan-0003.md` | **added (rev 3)** | CONTENT — hashed | **LEARNING RECORD** — the Session Learning Review §15 / E.6 owes for this session. `learning/` is CONTENT by intent (P5.1), so it is in the population and moves the hash; §15 requires it at session closure, and D.2 binds an approval to the hash, so it enters **before** review rather than after |
| `governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md` | **added** | **CONTROL PLANE — excluded** | the durable handoff, carried byte-identically |
| `governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md` | added | **CONTROL PLANE — excluded** | this manifest |
| `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` | **added** | **CONTROL PLANE — excluded** | task ACK + claim |
| `ledger/checkpoints/plan/CHK-plan-0010.json` | **added** | **CONTROL PLANE — excluded** | checkpoint |

```
content        20 files · +5361 / −1        no file deleted · no history rewritten
control plane   6 files                     excluded from the hash by construction

  Revision 3 edits five of revision 2's nineteen content files and ADDS exactly one —
  learning/plan/SLR-plan-0003.md, the Session Learning Record §15 owes. That single
  addition is the whole difference between 7cef4ccc… and 570fcbbb…, and between 523
  and 524 included entries. The control-plane count moves 4 → 6 as CHK-plan-0011,
  CHK-plan-0012 and CHK-plan-0013 accumulate.

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
                                  BASE cbce3016    REV 2 daaa3335    REV 3 b634829
targets executed                        64               65               65
FAILING SUITES                           6                6                6
FAILING TESTS                            7                8                7
```

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

**FAILING TESTS at this candidate tip `b634829` — 7, the same seven, and nothing else.**

**FAILING TESTS at revision 2 `daaa3335` — 8: those seven plus**
`scripts/test_locator_obligation_reaches_every_route.py::test_every_route_carries_the_obligation_or_declares_an_exemption`.
That one test is `M-1`, and it is what a set of suite names could not show.

```
ADDED FAILING TESTS    (rev 3 − base)   = ∅        0
REMOVED FAILING TESTS  (base − rev 3)   = ∅        0
SHARED FAILING TESTS                    = 7
DELTA REGRESSION at test granularity    = 0
  for the record, revision 2 measured the same way:  ADDED = 1
```

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

`learning/plan/SLR-plan-0003.md` is in this candidate's content, and it was added **after** a
revision-3 binding had already been declared. That is deliberate, and the alternative was a
review-integrity defect.

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

### 4.5 · M-2 — the exact guarantee, its mechanism, and the census that must match it

**The guarantee revision 3 makes, written so it can be falsified in one command:**

> No file present in a surface is skipped by **both** the allowlist check and the identifier
> scan without being printed by name under `[UNCHECKED]`.

Falsify it by producing a file that `verify --post-read` neither checks nor names. It is not the
claim *"post-read verification reads every file"* — it cannot, and it says so; and it is not
*"all unchecked paths are enumerated in advance"* — renders cannot be enumerated in advance,
which is why the prefix exists at all. It is the claim that the unchecked surface is **named at
run time, from the tree, exhaustively**.

**Mechanism — one predicate changed, and the census follows it.** `_is_expected_output()` admits
an exact declared path as before; under `expected_output_prefixes` it now admits a file **only
when the tool cannot decode its bytes as UTF-8 text**. The exemption was written for pixels, and
a render is pixels. A decodable file under the prefix is exempt from nothing: the allowlist check
reports it, the identifier scan reads it, and `freeze` — which shares the predicate — puts it in
`UNEXPECTED_FILE_SET` instead of counting it as the reader's work. Alternatives considered and
rejected: printing the prefix as a blind spot (declares as unchecked a file the scan can read);
an extension allowlist (a `.png` that is text walks through it, and case 07 below is that file).

**The census, in the vocabulary the review asked for.** Sizes are for a built pair before any
reading; every population is computed from the tree, and `[UNCHECKED SURFACE] n present file(s)`
closes the printed list on every run.

| | | |
|---|---|---|
| EXPECTED EXACT OUTPUT PATHS | **5** | declared in `expected_output_paths` — a static spec fact |
| EXPECTED OUTPUT PREFIXES | **1** | `output/renders/` — admits only undecodable bytes |
| VERIFIED POST-READ SURFACE | every present file **not** in the three rows below | allowlist + forbidden-path + symlink checks, and the identifier scan wherever the bytes decode |
| DECLARED RESIDUAL SURFACE | printed `[UNCHECKED]`, per actor, per run | (i) the blind-spot path when occupied — one path, `deepdive_manifests/PMID42397075.json`, whose authorship is not decidable post-read; (ii) each **present** declared output, whose content the scan does not read because it must name the paper; (iii) each file under a prefix whose bytes do not decode |
| UNENUMERATED / SILENT SURFACE | **NONE** | there is no fourth class: a present file is allowlisted input, an exact declared output, under a prefix, or none of those — and the last is reported by the allowlist check |

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

**Twelve hostile cases, each asserting the REASON and not only the exit code**, plus two spec
contracts — added to the tracked suite as `ExpectedOutputPrefixTests` and run in the release
battery. `SLR-mirror-0010` §4 is the argument for the discipline and it is Mirror's own: its
first B-4 battery reported 13/13 caught, and all thirteen were `rc=2` from `argparse` rejecting
`--out` where the command takes `--surfaces`. An expected exit code is never sufficient.

```
positive control · binary render passes and is named   forbidden bytes under the prefix
same bytes under prefix AND outside it                 nested directory under the prefix
renamed copy wearing a .png extension                  empty prefix, empty unchecked surface
several legitimate renders, each named                 hostile file beside a legitimate render
late arrival on the next run                           the census names every unchecked file
freeze calls a decodable prefix file UNEXPECTED        freeze still calls a render an output
```

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

---

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
transfers** — including the fourteen rows `REV-SCIAB-MIRROR-002` §5 re-tested and passed, and the
ten `REV-SCIAB-MIRROR-001` §6 found acceptable. The content they were found acceptable over no
longer exists.

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
