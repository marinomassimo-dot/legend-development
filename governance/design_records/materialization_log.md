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
