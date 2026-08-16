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

---

## MAT-004 — The fingerprint composition stops being prose; first checkpoint written

```yaml
record_id: MAT-004
date: 2026-08-16
actor_id: plan
task_id: MAT-001
directive_version: 2
generation: 1
governance_version: 3.1.1
outcome: COMPLETE — debt 1 of MAT-002 closed; body §49.Q satisfied
closes_debt: MAT-002 debt 1 (fingerprint composition was specification only)
```

### Produced

`governance/scripts/governance_fingerprint.py`, and the first checkpoint
`ledger/checkpoints/plan/CHK-plan-0001.json` under the A.6 schema.

**The script does not carry its own copy of the pertinence sets.** It parses § P2.2 of
`plan_defined_parameters.md` — the CORE block and the per-role table — so the governance document
stays the single source of truth and the two cannot silently disagree. This is the repository's
own rule about constraints applied to itself: *updating a constraint must cost at least as much
as complying with it*. Had the script hard-coded the sets, someone could later change the prose,
watch nothing break, and ship a system whose documented rules and computed rules differ. A stale
or unparseable table now fails loudly instead.

### Verified, not asserted

The composition's load-bearing design choice is that Annex J is split by section so that a change
to the cost policy does not invalidate a scientist's in-flight reading — A.6's own worked example.
Checked against the tool rather than argued:

```
scientist    → J.0, J.2, J.3          (no J.1, no J.4)
orchestrator → J.0, J.1, J.2, J.3, J.4
```

A fingerprint is a pure function of its input list, so J.4's absence from the scientist set is a
proof rather than a sample: no edit to J.4 can move that fingerprint.

The mechanism was also observed working in the other direction. Editing P2.4 — a paragraph inside
`plan_defined_parameters.md`, which is in `CORE` — changed all four role fingerprints in the same
session. That is the intended behaviour and it is documented in P2.4 itself, because the first
time someone sees it, it looks like a defect.

### An attempted verification that was correctly refused

A mutation test was attempted first: copy the governance into the scratchpad, alter `J.4` there,
recompute. The shell guard blocked the write, and the block was right — the safe-looking path
(an inline heredoc) is the one that bypasses read-before-overwrite, which is how a file authored
by another actor was once destroyed unread. The refusal was not worked around with a different
shell primitive. The structural check above is stronger anyway: it proves the property for every
possible mutation instead of sampling one.

### SESSION LEARNING REVIEW (§15)

`OUTCOME: MICRO_UPGRADE` — one record, class `ORIGINAL_OBSERVATION`.

**Observation.** When a specification and its implementation both contain the same rule, the
implementation is not "executable documentation" — it is a **second source of truth**, and the
two diverge the moment someone edits one. The instinct when making prose executable is to
translate it into code. The stronger move is to make the code *read* the prose, so the document
stays authoritative and the tool cannot drift from it.

**The boundary.** This works when the prose is already structured enough to parse — a fenced
block, a table with stable columns — and fails when it is narrative. Where it fails, the honest
answer is to restructure the prose into something parseable, not to give the tool its own copy
and promise to keep them in sync.

**Durable persistence** (§18): via the WORK_COMMIT carrying MAT-004.

---

## MAT-005 — Step 1 could not be executed: the design record was again not transmitted

```yaml
record_id: MAT-005
date: 2026-08-16
actor_id: plan
task_id: CONS-001            # pre-candidate consolidation, operator instruction of 2026-08-16
directive_version: 1
generation: 1
outcome: BLOCKED — MISSING_INPUT
```

The consolidation instruction opens with *"In allegato a questa istruzione trovi il documento:
`LEGEND v3.1 — TARGETED HOSTILE PRIOR-ART REVIEW`"*. **No document accompanied the
instruction.** The transmission carried the seven steps and nothing else.

Nothing was archived, and nothing was reconstructed. The prior-art matrix, the E1–E10
amendments, the operator's corrections, the DEFER register and the source-verification markings
— including, per the instruction, an Agno entry to be preserved as unverified — are records of a
review Plan did not witness. Composing them would be provenance fabricated to fill a provenance
slot, which is precisely what `design_records/` exists to prevent.

Per the instruction, no earlier record was rewritten: MAT-001's `MISSING` classification stands
as written and remains accurate. The debt is unchanged, not resolved.

**This is a REPLICATION, not a new observation.** MAT-001 recorded the failure pattern *a
multi-part transmission whose second part is described as attached arrives as a single-part
transmission that looks complete*, and proposed the practice: **declare the parts and their
count, and register each as `RECEIVED` or `ABSENT` before writing any of them.** The same
failure has now occurred twice on the same channel, with the same document. Under Annex E.2 this
is a second confirmation of class `REPLICATION`, which — with the ORIGINAL_OBSERVATION in
MAT-001 — meets the `BEST_PRACTICE_CANDIDATE` threshold of two confirmations in the two classes
that count fully. It is recorded here and will be filed under that status when `LEARNING_INDEX`
is built.

---

## MAT-006 — Base alignment onto main, and a classification of mine that was wrong

```yaml
record_id: MAT-006
date: 2026-08-16
actor_id: plan
task_id: CONS-001
directive_version: 1
generation: 1
outcome: COMPLETE — branch rebased onto main, zero conflicts, nothing lost
corrects: MAT-001 "Foreign uncommitted change — classified, not touched"
```

### Measured before touching anything

| Fact | Value |
|---|---|
| `main` HEAD | `749a9a9` |
| `evidence-index` HEAD before | `e799f47` |
| merge-base | `3f72066` |
| main-only commits | 35 |
| branch-only commits | 4 (all Plan's) |
| dirty | `disease-models/wwox/research/deepdive_manifests/PMID42422765.json` |
| path overlap between main's 35 commits and Plan's paths | **none** — main touches no file under `governance/`, `roles/`, `deployment/`, `ledger/`, nor `.gitignore` or `BOOTSTRAP.md` |

### The order of steps 2 and 4 was inverted, deliberately

The instruction places the CLAUDE.md migration at step 2 and the base alignment at step 4. Doing
them in that order would have produced a **provably lossy migration**, because `main` commit
`f2b9067` adds twelve lines to `CLAUDE.md` — an *Observable-stop gate for long readings* — that
the pre-rebase base does not contain. Inventorying the stale file would have silently dropped a
live operating rule.

Non-loss is stated as non-negotiable in the same instruction (*"NON eliminare né indebolire
alcuna regola scientifica ancora valida"*, *"Nessuna perdita semantica silenziosa"*), and
sequence yields to it. The inversion is declared here rather than performed quietly.

### The dirty file: my MAT-001 classification was right in conclusion, wrong in reasoning

MAT-001 called it a stale receipt bump, `-04 → -05`, superseded because main already carried
`-05` and `-06`. That was measured against the **base**, not against `main`, and the full diff
against `main` shows something different: the working-tree file was not *ahead* of the base, it
was far *behind* main. Main additionally carried five figure artifacts
(`S_p02/03/04/06/07_300dpi.png`, each with its SHA-256) and **five figure verbatim locators** for
Supplementary Figures S1–S5 — the sample-size conflict in S2, the selection-conditioned survival
argument in S5, and three others. None of that was visible from the base-relative diff.

Had the file been "restored" or force-resolved on the strength of the MAT-001 reading, the
question of what was being discarded would never have been asked correctly. Reading the whole
diff **against the target**, not against the ancestor, is what made the difference.

**Proof of no unintegrated content**, as the instruction requires:

```
lines unique to the working tree vs main:   + "receipt": "FTR-20260810-42422765-05",   (exactly one)
that value in main's version:               line 7, inside "landing"                   (preserved)
main's "receipt" field:                     FTR-20260814-42422765-06                   (superseded forward)
```

One line, and it survives in main under a different field. Absorption loses nothing.

### How it was absorbed

Not by `checkout --`, which is a destructive write with no confirmation and no recovery. The file
was copied to the session scratchpad
(`preserved/PMID42422765.worktree-before-alignment.json`, SHA-256 `6c3fe60f…f888b83`) and then
`git stash push`ed with an explanatory message. **The stash is deliberately not dropped**: it
remains recoverable in this worktree as `stash@{0}`.

### Rebase

`git rebase main` — four commits replayed, zero conflicts, as the absence of path overlap
predicted.

| Before | After |
|---|---|
| `f89a4a9` | `318d117` |
| `e99aeb4` | `ccdbe94` |
| `40ba0b7` | `a8cd125` |
| `e799f47` | `36305c6` |

`main`-only commits after rebase: 0. Branch-only: 4. The deep-dive manifest is now byte-identical
to main's.

Consequence for the checkpoint: `CHK-plan-0001.json` records `head_at_write: 40ba0b7`, which is
now reachable only through the reflog. It is **not rewritten** — it is a true record of a state
that existed. The successor checkpoint carries the post-rebase pointers and this mapping.

**Durable persistence** (§18): via the WORK_COMMIT carrying MAT-005 and MAT-006.

---

## MAT-007 — CLAUDE.md migrated; single INTEGRATION_CANDIDATE prepared; STOP

```yaml
record_id: MAT-007
date: 2026-08-16
actor_id: plan
task_id: CONS-001
directive_version: 1
generation: 1
governance_version: 3.1.1
outcome: COMPLETE — candidate READY FOR MIRROR HOSTILE REVIEW
candidate_id: CAND-20260816-GOV311
candidate_content_hash: f869a5237a70634ada535343b7484ddc45f36111e9c79664179086a81f8b8909
```

### How the migration was made non-lossy

Three independent read-only inventories mapped the old root `CLAUDE.md` rule by rule against
`framework/`, `ARCHITECTURE.md`, the protocols, the manuals and the disease-model layer, under
one instruction: quote, do not paraphrase, when claiming a rule already exists elsewhere.
Terminological similarity was not accepted as equivalence.

What that produced was not a formality. **The growth principle existed in no other file** — and
`mission.md`, the only file that summarised it, delegated its five binding consequences *back
into `CLAUDE.md` by anchor*. Emptying the file without noticing would have removed a principle
and simultaneously broken the pointer that would have revealed the removal. Likewise
`gold_is_in_the_details.md` had been called the "full statement" of parity of sources while
stopping at rule 6, so rules 5b–5e, 7 and 8 had no master-level home at all; `MODE: Q&A` existed
nowhere else; and several literal strings a reader is instructed to emit verbatim —
`FULL STATE NOT AVAILABLE — COMMIT BLOCKED`, `PARTIAL FILE — NOT SAFE FOR REPLACEMENT` — appeared
in exactly one file in the repository.

The router was written **last, and only after every destination existed**, so that an
interruption at any point would have left the old file intact rather than half-emptied.

Complete map: [`claude_md_migration_map.md`](claude_md_migration_map.md). Counts: 36 rules
`PRESERVED` (moved in full), 20 `REPLACED_BY_EQUIVALENT`, 2 `UNRESOLVED` inbound pointers.

### The candidate

One candidate for the whole introduction, `CHANGE_CLASS: MAJOR`, six source commits on
`BASE_HEAD 749a9a9b`. Sixteen Plan implementation decisions are listed individually with their
delegating clause and state — four `PROVISIONAL` with expiry, two `UNRESOLVED`, the rest
`PROPOSED` — rather than left to be discovered inside file diffs.

The manifest declares one thing it cannot do: **the content hash excludes the manifest itself**.
A manifest containing a hash of a tree containing that manifest is a fixed point. The hash binds
the proposed content; the manifest is the declaration about it, in the relation a signature has
to what it signs. Said out loud rather than papered over.

### SESSION LEARNING REVIEW (§15)

`OUTCOME: FAILURE_PATTERN` — one record, class `ORIGINAL_OBSERVATION`.

**Observation.** A relocation is safe only when the inventory is taken against the state you are
migrating *to*, not the state you happen to be sitting on. Two separate near-misses in this
session had the same shape, and neither was visible from the working tree alone. The dirty
manifest looked ahead of its base and was far behind `main`, carrying five figure locators fewer.
The `CLAUDE.md` in hand looked complete and was missing a rule `main` had added twelve lines of.
In both cases the object being reasoned about was **stale in a way that only a diff against the
target could show**, and in both cases the confident-looking action — revert the file, inventory
the file — would have destroyed something while appearing careful.

**The reusable part.** Before migrating, reverting, absorbing or inventorying anything, diff it
against the branch you intend to end on, not against the ancestor you started from. The ancestor
tells you what *you* changed; only the target tells you what *you would lose*. This is the
sharpened form of the existing rule *read the whole diff before reverting* — the rule says read
it all, and this says read it against the right thing. Carried into
`parallel_legend_protocol.md` rule 4 as part of this migration, so the next actor inherits it
instead of rediscovering it.

**Durable persistence** (§18): via the WORK_COMMIT carrying MAT-007. Six session-learning records
now exist across MAT-001…007 and none is yet in `LEARNING_INDEX`, which does not exist; that
filing is the first item due after canonical commit.
