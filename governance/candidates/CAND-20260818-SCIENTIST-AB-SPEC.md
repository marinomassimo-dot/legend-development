---
artifact: INTEGRATION_CANDIDATE manifest (Annex D.2)
candidate_id: CAND-20260818-SCIENTIST-AB-SPEC
revision: 1
governance_version: 3.1.1
change_class: MAJOR
prepared_by: plan
prepared_on: 2026-08-18
state: READY FOR MIRROR REVIEW — no approval requested, granted or implied
scope: HANDOFF-20260818-SCIENTIST-AB, as transmitted. Not reduced and not widened.
---

# INTEGRATION_CANDIDATE — the definitive Scientist A / Scientist B specification

## 1 · Manifest (Annex D.2)

```yaml
CANDIDATE_ID:               CAND-20260818-SCIENTIST-AB-SPEC
REVISION:                   1
BASE_HEAD:                  cbce30168091f7769c56c4f019055fa55fd0d66a
BRANCH:                     scientist-ab-spec
CONTENT_TIP:                b965ca5880e93ad57770a0483aaa4652ec5f390c
MANIFEST_TIP:               7641dfdf3b42a0312bfeae304b03832a94181633 — and every later
                            control-plane commit on this branch, including the one carrying
                            this correction.
                            # 🔴 A MANIFEST CANNOT NAME THE COMMIT THAT CARRIES IT. Writing the
                            # value creates the commit the value would have to name, so the field
                            # lags by one by construction and chasing it is an infinite regress.
                            # It is therefore INFORMATIONAL. The binding is BASE_HEAD +
                            # CANDIDATE_CONTENT_HASH, and it holds because governance/candidates/
                            # and ledger/ are declared CONTROL_PLANE_ROOTS (P5.1): the hash is
                            # identical at the content tip, at the ledger commit between, and at
                            # every manifest revision. Measured at all four, not asserted.
                            # `git log --oneline cbce3016..HEAD` shows the branch; the hash
                            # command shows the invariance.
CANDIDATE_CONTENT_HASH:     3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75
CANDIDATE_HASH_VERSION:     legend-candidate-v4
CHANGE_CLASS:               MAJOR
LINT_RESULT:                PASS (1 pre-existing INFO)
PUBLICATION_GATE:           PASS / BLOCKS: 0
MIRROR_REVIEW:              REQUESTED — none exists; no prior attestation transfers
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
  --tip  b965ca5880e93ad57770a0483aaa4652ec5f390c --show-domain
```

```
EXPECTED             3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75
OBTAINED (run 1)     3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75
OBTAINED (run 2)     3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75
OBTAINED at the ledger commit (control plane, after the content tip)
                     3b568aae6c76848da197cacd43e517373ab7ca9532cf9289a73097e261916c75
```

Domain counts are **outputs of that command at that tip**, never constants maintained here —
read them from `--show-domain`.

---

## 2 · File list and classification

| File | Status | Domain | Classification |
|---|---|---|---|
| `framework/protocols/scientist_reading_modes.md` | **added** | CONTENT — hashed | **NORMATIVE** — reading modes, actor identity of A and B, task-ownership rule |
| `framework/protocols/controlled_benchmark_ab.md` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — normative for the benchmark it defines, and for nothing outside it |
| `framework/scripts/benchmark_input_surface.py` | **added** | CONTENT — hashed | **NORMATIVE (tooling)** — it decides whether a surface may be handed over; it is not documentation |
| `roles/scientist.md` | modified | CONTENT — hashed | **NORMATIVE** — `actor_id_status` front matter + the *Reading modes* section. 🔴 In the `CORE` fingerprint set |
| `BOOTSTRAP.md` | modified | CONTENT — hashed | **NORMATIVE** — records that A and B are fixed and C is not |
| `framework/protocols/index.md` | modified | CONTENT — hashed | **DOCUMENTATION** — two rows in the protocol table |
| `framework/eval/README.md` | modified | CONTENT — hashed | **DOCUMENTATION** — the reader-benchmark axis, and what it does not have |
| `framework/eval/benchmarks/BENCH-AB-001/surface_spec.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the allowlist; a command reads it, a reviewer reads the same file |
| `…/benchmark_manifest.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the experiment record, `PREPARED — NOT FROZEN` |
| `…/population/evidence_units.json` | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — the ex-ante evaluation population, derived by command |
| `…/instructions/` ×7 | **added** | CONTENT — hashed | **BENCHMARK_PROTOCOL** — surface router, common instructions, output schema, `MODE_A`, `MODE_B`, and the two per-actor assignments |
| `governance/candidates/HANDOFF-SCIENTIST-AB-SPEC.md` | **added** | **CONTROL PLANE — excluded** | the durable handoff, carried byte-identically |
| `governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md` | added | **CONTROL PLANE — excluded** | this manifest |
| `ledger/tasks/plan/SCIENTIST-AB-SPEC-001.json` | **added** | **CONTROL PLANE — excluded** | task ACK + claim |
| `ledger/checkpoints/plan/CHK-plan-0010.json` | **added** | **CONTROL PLANE — excluded** | checkpoint |

```
content        17 files · +2910 / −1        no file deleted · no history rewritten
control plane   4 files                     excluded from the hash by construction

  git diff --shortstat cbce3016 HEAD -- . ':!governance/candidates' ':!ledger'
```

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

The population is fixed **before either reading exists**, by command: 36 units, 115 panels,
identical across two runs, digest in the manifest. A denominator chosen afterwards is a
denominator chosen to fit.

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

Both are fixed by skipping the output slots post-read, with the reasoning written at the check:
authorship is not decidable from a path, so the guarantee is carried by the pre-handover run
(slot proven empty, forbidden path proven absent) plus the freeze receipt. **The second is also
the sharpest argument for §2.1** — in a checkout, the reader would be writing its manifest on top
of the prior one.

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

**`run_release_regressions.py` — `FAIL`, and it fails identically at `BASE_HEAD`.** Eight suites,
measured in the clean root checkout at `cbce3016`, not assumed. Pre-existing, carried forward,
**not resolved inside this work**; the new script was made executable so this candidate does not
add a ninth.

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
classification open · L2 suspended · eight failing release suites.

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

## 6 · What Mirror is asked to verify

Independent review of the binding **and** the content. **No prior attestation transfers**: the
sunset and P51C9 reviews say nothing about this candidate.

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
 8  genuine benchmark-only extensions           §6.2 — four promoted, THREE REFUSED. Attack the
                                               refusals first: are those three really covered?
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
2. **Are the three refused fields genuinely covered by labelled prose?** If `Uncertainty` as a
   convention is weaker than `Uncertainty` as a field, the refusal is wrong and the operator's
   sixteen were right. Plan measured the practice and judged the convention adequate; that
   judgment is exactly the kind that looks obvious to its author.
3. **Does §0 of the benchmark protocol admit enough?** One paper, one session per actor: the
   design cannot separate the mode from session variance. It is stated in the opening section.
   If it still reads as a controlled experiment whose result will mean more than that, the
   wording has failed and Plan cannot see it from here.
