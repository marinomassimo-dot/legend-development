---
artifact: LEGEND governance — materialization log
governance_version: 3.1.1
normative: NO — provenance record
maintained_by: plan
---

# MATERIALIZATION LOG

Append-only. A record already written is never modified; a later record supersedes an earlier
one by pointing at it, never by rewriting it.

---

## MAT-001 — Governance v3.1.1 body materialized; annexes blocked

```yaml
record_id: MAT-001
date: 2026-08-16
actor_id: plan
session_ref: e49d3bd1-2c63-4969-be19-f7fca4b240fc
worktree: .claude/worktrees/evidence-index
branch: evidence-index
head_at_start: 3f720662d9215d9a4fcaae68ea7892b484f830bc
task_id: MAT-001
directive_version: 1
generation: 1
governance_version: 3.1.1
applicable_governance_fingerprint: UNAVAILABLE
outcome: PARTIAL — body materialized, annexes A–J blocked on missing source
```

### Produced

| Artifact | SHA-256 | Nature |
|---|---|---|
| `governance/GOVERNANCE_v3.1.1.md` | `bb8e356ff4ee6d59b5143db40334059661f6def8a9b7bac5bf43d04bdc8322a2` | The frozen body, verbatim, under a materialization header. 466 lines. |
| `governance/ANNEX_INDEX.md` | `ce161956c1950b320704d35c74a0452760d0d07c91aff1597836bc0b7fdeb2ff` | Register of A–J: binding requirements, authorship class, blocked downstream artifacts. |
| `governance/design_records/README.md` | *(see git)* | Scope of design_records + the missing prior-art matrix and DEFER register. |
| `governance/design_records/materialization_log.md` | *(this file)* | This record. |

The hashes are recorded now because they are the first real inputs any future
`APPLICABLE_GOVERNANCE_FINGERPRINT` will consume. They are inputs, **not** the fingerprint: the
composition function is Annex A.6, which does not exist yet.

### Refused

Plan did **not** compose: the ten canonical annexes, `/BOOTSTRAP.md`, `/roles/*.md`, the
deployment profile, the runtime inventory / Agent Card, `LEARNING_INDEX`, role-specific
`ACTIVE_LESSONS`, the fingerprint composition, or the prior-art matrix and DEFER register.

The body presents the annexes as *"(allegato)"* — attached — and they were not transmitted.
Composing them from the body would convert Plan's derivation into normative law under a
governance version that is frozen, and would do so invisibly: an annex authored by Plan and one
supplied by the operator are indistinguishable once written to `governance/`. §12 prescribes
fail-closed on doubt; this is the same rule applied to authorship rather than to batch class.

Stub files were also refused. The LEGEND file protocol invalidates placeholders, and an empty
`ANNEX_A.md` would report presence to a directory listing while carrying nothing.

### Initial state recorded (body preamble, obligation 1) and measured (obligation 2)

| Fact | Measured value |
|---|---|
| Root checkout | `/Users/massimo/Desktop/legend-public`, branch `main`, HEAD `749a9a9`, **clean** |
| Plan worktree | `evidence-index`, HEAD `3f72066` |
| Branch vs main | `evidence-index` is **35 commits behind** `main`, with **0 commits of its own**; merge-base is its own HEAD — a strict ancestor |
| Worktrees present | root(main) · evidence-index · lettore · lettore-b · mirror · 4 Codex worktrees (aqeilan, partials, reading, wwox-mouse-series) |
| `lettore-c` (Scientist C, §32) | **absent** — bootstrap step 6 not yet performed |
| Governance artifacts before this record | none: no `governance/`, `BOOTSTRAP.md`, `roles/`, `design_records/`, `runtime/`, `LEARNING_INDEX`, `ACTIVE_LESSONS` |
| LEGEND scientific state | `framework_version: v3.3.1`, `current_state: READY`, `deep_dive_gate`/`ingest_gate`/`batch_commit_gate` all OPEN |
| GATE 2 tooling | present and runnable: `framework/scripts/legend_lint.py`, `scripts/public_release_gate.py` |
| `governance/` gitignore status | not ignored — the tree is tracked |

### Contradictions with the real repository state (body preamble, obligation 5)

1. **§0.3 · root CLAUDE.md as a MINIMAL router.** The current root `CLAUDE.md` is not a router:
   it is the load-bearing scientific operating core — parity of sources, rules 5b–5e on
   locators and corrupted text surfaces, epistemic discipline, commit rules. Reducing it to a
   router at bootstrap step 8 would delete operating law that no annex replaces. The rewrite
   MUST relocate that content to a durable, referenced home before the router replaces it,
   otherwise step 8 is a lossy edit dressed as a structural one.
2. **§35 · paths `/protocols/` and `/active_lessons/`.** Neither exists at top level. Protocols
   live at `framework/protocols/`. Either the governance paths are adopted and the framework
   layout is bridged, or the governance is materialized against the existing layout. This is a
   decision, not a detail: `/roles/` and `/governance/` are equally new top-level entrants into
   a repository whose layering (`framework/` vs `disease-models/`) is itself the privacy design.
3. **§32 · Scientist C.** `lettore-c` does not exist; A and B do.
4. **Public-edition exposure.** This repository is the public edition and is pushed to a public
   remote under a publication gate. Governance material now sits at top level and will travel
   with it. No governance artifact may reach a public push without `public_release_gate.py`, and
   — per the root CLAUDE.md — without a human reading `git diff origin/main..main --stat`, which
   is the one judgement no gate makes.
5. **Base staleness.** Any `INTEGRATION_CANDIDATE` from this branch would be computed against a
   35-commit-old base. GATE 0 binds `BASE_HEAD`; the branch must be brought up to `main` before
   a candidate is prepared, and the four files produced here are new paths, so they carry no
   merge risk of their own.

### Foreign uncommitted change — classified, not touched

`disease-models/wwox/research/deepdive_manifests/PMID42422765.json` was already modified in this
worktree when Plan rehydrated, by an unidentified prior actor: `receipt` and the first `landing`
entry bumped from `FTR-20260810-42422765-04` to `-05`.

Classification: **SUPERSEDED_BY_MAIN, not pending work.** `main` already carries `-05` in
`landing` *and* a later `FTR-20260814-42422765-06` as the active receipt. Nothing is at risk of
being lost.

It was left exactly as found. Reverting it is a destructive write on another actor's file, and
the root CLAUDE.md records the day `git checkout -- <path>` destroyed a receipt-ledger anchor
under precisely this reasoning ("it looked like only my own change"). It resolves itself when
the branch is brought up to `main`.

### SESSION LEARNING REVIEW (§15)

`OUTCOME: FAILURE_PATTERN` — one record, class `ORIGINAL_OBSERVATION`.

**Observation.** A two-level specification whose second level is described as *"(allegato)"*
transmits, over a chat channel, as a single-level specification that *looks* complete. The body
is self-consistent, ends with a numbered bootstrap sequence, and never announces its own
incompleteness; the gap is visible only by cross-referencing every `(Annex X)` mention against
what actually arrived. The failure mode is not that the annexes are missing — it is that the
body reads as sufficient, which invites the receiving actor to close the gap by derivation and
call it materialization.

**Why it matters here specifically.** The receiving actor is the one entitled to write
`governance/`. Derived and supplied annexes are byte-indistinguishable once written, and
`APPLICABLE_GOVERNANCE_FINGERPRINT` would then hash Plan's own inventions as constitutional
input — the fingerprint would be perfectly valid and would certify the wrong constitution.

**Candidate practice** (to be filed against `LEARNING_INDEX` when it exists, per §15's
duplicate check): a multi-part governance transmission declares its parts and their count, and
the materializing actor registers every part as `RECEIVED` or `ABSENT` **before** writing any of
them. The register precedes the materialization; that ordering is what makes the absence
visible instead of inferable.

**Durable persistence** (§18): this record reaches durable state via the WORK_COMMIT that
carries MAT-001. It is not yet in `LEARNING_INDEX`, because `LEARNING_INDEX` does not yet exist
and its schema is bound to Annex E. Tracked here as a debt, not as a completed filing.

---

## MAT-002 — Annexes A–J materialized; the seven delegated parameters defined

```yaml
record_id: MAT-002
supersedes: none — extends MAT-001
date: 2026-08-16
actor_id: plan
session_ref: e49d3bd1-2c63-4969-be19-f7fca4b240fc
task_id: MAT-001
directive_version: 2
generation: 1
governance_version: 3.1.1
outcome: COMPLETE for the annex scope; downstream artifacts pending
```

### Produced

Ten annex files, verbatim under materialization headers, named per the transmitted convention
(`governance/annex_a_task_contract.md` and siblings). Hashes are in
[`../ANNEX_INDEX.md`](../ANNEX_INDEX.md), which was rewritten from a register of absences into a
register of contents, carrying the transmitted preamble verbatim.

Plus [`../plan_defined_parameters.md`](../plan_defined_parameters.md): the seven values the
annexes delegate to Plan by name — `RETRY_POLICY` default, fingerprint composition, ACK timeout,
heartbeat cadence, `CANDIDATE_CONTENT_HASH` definition, lesson budgets, event ledger design.
Collected in one artifact rather than seven footnotes, so the fingerprint has one thing to hash
and a reader can see every knob at once.

Four of those values are numbers that no evidence yet supports. None was left as a bare
constant: each is registered as a `PROVISIONAL_OPERATIONAL_PRACTICE` (E.3) with a success
criterion, a failure criterion, an expiry and a rollback. The repository's own rule — *never pin
a number a human must remember to update* — is satisfied by machinery the governance already
owns, rather than by a comment asking someone to remember.

### Debts opened, stated as debts and not as work done

1. **The fingerprint composition is prose.** P2 specifies the pertinence sets and the hashing
   function precisely enough to execute, and nothing executes it. Until a script takes a role
   and emits the hex, every fingerprint would be hand-assembled — and the repository has already
   recorded what prose-only recipes do: they decay silently, and the one that was made
   executable immediately caught two of seven entries that prose had recorded wrongly. **No
   checkpoint's fingerprint is load-bearing until that script exists.**
2. **The event ledger has a chosen design and no writer.** P7 picks option (a) and specifies the
   format; the append machinery is not built. It must be built on the existing receipt-ledger
   pattern rather than as a second mechanism — `PATTERN_ALREADY_SOLVED_GATE` names uneven
   application as this system's characteristic failure, and an append-only ledger with a hash
   chain and a tail anchor already runs here.
3. **`MIRROR_RETROSPECTIVE ogni N batch` has no owner.** G.3 assigns `N` to nobody. Plan did not
   take it: G.2 places retrospective methodology inside Mirror's own method, which Mirror may
   not change alone. Flagged `UNASSIGNED_PARAMETER` for bootstrap.

### SESSION LEARNING REVIEW (§15)

`OUTCOME: MICRO_UPGRADE` — one record, class `ORIGINAL_OBSERVATION`.

**Observation.** The obvious way to compose `APPLICABLE_GOVERNANCE_FINGERPRINT` is at file
granularity: hash each annex the role depends on. That choice is wrong, and the specification
that delegated the parameter contains the proof. A.6 illustrates a change that must **not**
invalidate anything with *"un cambio alla COST_POLICY mentre uno Scientist legge un paper"* —
and COST_POLICY is J.4, a section of Annex J. Hashing Annex J whole would invalidate every
scientist checkpoint on precisely the change the annex uses to illustrate the opposite. The
composition had to split Annex J by section.

**The reusable part.** A specification that delegates a parameter usually also contains its test
case, phrased as an example rather than as a requirement — and the example is easy to read past,
because it appears to be explaining the concept rather than constraining the answer. Before
choosing any delegated value, re-read the delegating clause for worked examples and treat each
one as a test the chosen value must pass. Here it cost one paragraph to check and would have
cost a governed re-calibration to discover from invalidation rates months later.

**Durable persistence** (§18): via the WORK_COMMIT carrying MAT-002. `LEARNING_INDEX` is now
unblocked (E.2 schema received) but not yet built; both this record and MAT-001's remain to be
filed there, and that filing is itself a tracked debt.

---

## MAT-003 — Role contracts, bootstrap and deployment profile

```yaml
record_id: MAT-003
date: 2026-08-16
actor_id: plan
task_id: MAT-001
directive_version: 2
generation: 1
governance_version: 3.1.1
outcome: COMPLETE for §47 step 7 except the fingerprint script; step 8 deliberately not attempted
```

### Produced

`roles/orchestrator.md`, `roles/plan.md`, `roles/mirror.md`, `roles/scientist.md`,
`/BOOTSTRAP.md`, `/deployment/deployment_profile.md`, and one `.gitignore` entry for
`deployment/local_instance.md`.

All are marked `status: PROPOSED`. They become binding when Mirror's hostile review passes and
the operator approves — Plan materializes governance, it does not enact it.

### Three declared deviations

Stated rather than silently diverged from, per the repository's own rule that a divergence from
an existing pattern must carry its reason.

1. **One scientist contract, not three.** Annex I.2 step 7 says each actor reads
   `/roles/<suo>.md`. Body §32 makes the three scientists equivalent in mandate, protocol,
   authority, obligations and isolation. Three byte-identical files would fork the day one is
   edited, and the divergence would be invisible until it mattered; one contract also gives the
   three a single `ROLE_CONTRACT_HASH`, which is what makes their fingerprints comparable. The
   Agent Card records the ACTOR_ID → contract mapping.
2. **The §35.2 common section is a pointer table, not a paste.** §35.2 requires the common
   AUTHORITY & ROUTING section in every worktree. `governance/` is tracked, so it is *already*
   in every worktree; what each contract needs is routing to it. Pasting the section into six
   files would create six copies that drift — the same uneven-application failure the repository
   names as characteristic of systems that grow by accretion, arriving from the duplication side
   rather than the omission side.
3. **The local runtime instance is untracked.** I.5 forbids absolute paths in the governance and
   defines a local half that holds them. That half is `deployment/local_instance.md`, gitignored:
   an absolute path in the tracked portion breaks the clone-and-run test the profile exists to
   protect, and in a public repository a machine path also carries a username. The release gate
   checks for patient re-identification and would not catch either.

### Proposed, not decided

The ACTOR_IDs `scientist-a`, `scientist-b`, `scientist-c` are a proposal. `orchestrator` is fixed
by Annex I.3, which writes it literally; `plan` was assigned by the operator; `mirror` follows.
The scientists' worktrees are named `lettore`, `lettore-b`, `lettore-c`, so the identifier does
not follow from the directory. An ACTOR_ID is permanent and carries identity, provenance and
learning attribution, so it is confirmed at registration (I.2 step 7), not fixed by a
materialization.

### Verification

`legend_lint.py` → `VERDICT: PASS`. `public_release_gate.py` → `VERDICT: PASS, BLOCKS: 0`. The
four `[REVIEW]` items in the gate output are pre-existing and unrelated to this work. Introducing
four new top-level entrants (`governance/`, `roles/`, `deployment/`, `BOOTSTRAP.md`) into a
repository whose layering is itself the privacy design was worth verifying rather than assuming.

### Held deliberately: bootstrap step 8

The root `CLAUDE.md` rewrite is **not** attempted. Contradiction 1 in MAT-001 stands: the current
root CLAUDE.md is not a router but the load-bearing scientific core, and replacing it with a
minimal router deletes operating law that no annex replaces. That relocation is an operator
decision, and doing it as a side effect of materialization is exactly the lossy edit the record
warned about.

### SESSION LEARNING REVIEW (§15)

`OUTCOME: MICRO_UPGRADE` — one record, class `ORIGINAL_OBSERVATION`.

**Observation.** A specification that says *"this section must appear in every worktree"* reads
as an instruction to duplicate. In a version-controlled repository it usually is not: the file is
already in every worktree by virtue of being tracked, and the requirement is satisfied by
presence plus routing. Duplicating it instead creates N copies that are identical exactly once —
at creation — and silently diverge afterwards.

**The reusable part.** Before satisfying a replication requirement by copying, ask what mechanism
already replicates. Where one exists, copying does not add availability; it only adds surfaces
that can disagree. Where none exists, the copy is necessary and its drift must be guarded. Both
answers are defensible; the failure is not asking, because copying always looks like compliance.

**Durable persistence** (§18): via the WORK_COMMIT carrying MAT-003.
