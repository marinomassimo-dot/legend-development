# Unattended delegation readiness

**Status:** `OPEN` — six preconditions, none closed.
**Opened:** 2026-08-14.
**Lifecycle:** this document retires when all six preconditions are closed and their
verifications are executable. It is a plan with an end, not a standing protocol; a plan that
outlives its preconditions becomes decoration.
**Scope:** what must hold before the operator can hand over a task and be consulted only by
exception.
**Not in scope:** the multi-agent cockpit itself. See §7 — it is under a preserved debt.

---

## Why this exists

On 2026-08-14 the operator specified the interface he wants: hand a list of PMIDs or a task to
an orchestrating session, and be consulted only for the declared exceptions. Two concrete tasks
were used as probes — a **DisMech export** after the Aqeilan and Aldaz batches, and a
**Q230P-style in-silico analysis** of a further variant. Auditing both against the repository
found six preconditions. Four are gaps in the machinery; two are decisions only the operator
can make.

🔴 **None of the six requires the cockpit.** Each is needed under the current
manually-coordinated model too. They are listed together because the same audit surfaced them,
not because they share an implementation.

---

## The exception list, after this audit

An orchestrating session escalates to the operator on, and only on:

1. **URGENT cat-1** — a direct safety signal.
2. **MAJOR baseline-reversal** — overturning a baseline claim or a BLOCK-1 policy change.
3. **Any paid service** — currently a hard stop that forbids even asking; see `P3`.
4. **Any permission outside the allowlist** — a property of the runtime, not a rule: no session
   can approve another session's permission prompt.
5. **Any push or PR to a public remote** — 🔴 **new, added by this audit.** See `P4`.

An ordinary `BATCH_COMMIT` is **not** on this list and does not require the operator's signature.

---

## P1 — Wire `assert_exportable()` into the export path

**Problem.** The gate that refuses an export built on drifted claims is unreachable from any
command.

**Evidence.** [`dismech_independent_protocol.py`](../../disease-models/wwox/analysis/scripts/dismech_independent_protocol.py)
defines `scope_drift()` (L321), `unresolved_drift()` (L370) and `assert_exportable()` (L388) —
the last documented as *"The gate. […] This is where the freeze bites, and the only place it
does."* Its CLI registers eight subcommands (`verify-baseline`, `build-blind-bundle`,
`verify-blind-bundle`, `verify-canonicalisation`, `verify-receipt-projection`,
`verify-reconciliation`, `reconcile-locator-receipts`, `compare`) and **`assert-exportable` is
not among them**. [`export_dismech_dryrun.py`](../../disease-models/wwox/analysis/scripts/export_dismech_dryrun.py)
imports `fulltext_receipts` but never the gate. The only caller in the repository is its own
test suite. `DRIFT_LOG` points at `dismech_drift_acknowledgements.jsonl`, which **does not
exist on disk** — the acknowledgement mechanism has never been exercised.

**Why now.** The six sealed `scope_blocks` are `CLAIM 016 / 024 / 035` and
`PAPER 019 / 055 / 056`. A batch of Aqeilan and Aldaz readings is the single most likely event
to move them. The gate must bite exactly when this plan's first task runs.

**Change.** (a) Register an `assert-exportable` subcommand. (b) Call it from
`export_dismech_dryrun.main()` before anything is written, fail-closed. (c) Decide and encode
what an absent acknowledgement log means — absence must be a defined state, not an exception
traceback.

**Verification.** A regression that mutates one sealed block and asserts the **exporter**
refuses. Testing the function alone is what the current suite already does, and it is what let
the gate ship unwired.

**Owner:** delegable.

---

## P2 — Give the export a machine-readable gate

**Problem.** An orchestrating session has no flag to consult before exporting.

**Evidence.** `framework/state/state_manifest_current.md` §6 carries `current_state`,
`deep_dive_gate`, `ingest_gate`, `batch_commit_gate`, `active_parallel_branches`. There is no
`export_gate`. Export state lives instead in the `window` object of
`dismech_phase2_baseline.json` and in a prose phase table in `analysis/README.md`.

**Change.** Add `export_gate` to the operational state block — **derived, never hand-declared.**
CLAUDE.md is explicit that a fact must be re-anchored by the tool that causes it, and that at
scale "visible in review" means invisible. The value is computed from `unresolved_drift()` plus
the phase table, so it cannot rot into a comforting `OPEN` nobody rechecked.

**Verification.** LINT reads it; a drifted sealed block flips it closed without a human edit.

**Owner:** delegable. The state manifest is writable outside `BATCH_COMMIT`.

---

## P3 — Reclassify paid services from HARD STOP to ESCALATION

**Problem.** 🔴 **The current rule forbids the orchestrator from even asking**, so the decision
the operator now wants to make would never reach him.

**Evidence.** [`.claude/skills/legend/SKILL.md`](../../.claude/skills/legend/SKILL.md),
*Autonomy contract*: *"**Anything paid** (service, API, model, paid license) → **you are not
authorized, period. Do not ask for the ok (the operator will never give it)**: stop on that
branch, use the local/free alternative if one exists, and flag the block."*

**Consequence today.** An orchestrator asked for a BioNeMo, Nebius or AlphaFold-3-server run
stops, records a gap, and continues elsewhere. The operator is never consulted — which is the
opposite of the interface he asked for, and the failure is silent.

**Change.** Move paid services from case 3 (hard stop) to the escalation list, keeping every
other guarantee: never self-authorize, never enter payment details, never start a paid run to
"see what it costs". The escalation must carry a cost estimate, what leaves the machine, and
the free/local alternative if one exists.

**Owner:** 🔴 **OPERATOR.** One line, but it changes the autonomy contract.

---

## P4 — Add "push or PR to a public remote" to the exception list

**Problem.** The one irreversible action in the export path has no gate, by design and by
statement.

**Evidence.** CLAUDE.md: *"The privacy gate does not and cannot cover this.
`public_release_gate.py` looks for patient re-identification and does it well; copyright is
outside its domain. […] It is the one judgement no gate here makes for you, and publishing is
not reversible."* Confirmed against the script: its five scanners check declarations, not
licence adjudication. There is a `MIN_SNIPPET_CHARS` in `deepdive_manifest.py`; **there is no
maximum** anywhere, so nothing mechanically caps how much verbatim third-party text an export
could carry.

**Where the boundary actually falls.** Phase 3 writes to `staging/`, which is gitignored —
**generating an export is not publishing.** Phase 5, the upstream PR to
`monarch-initiative/dismech`, is `NOT STARTED` and is placed out of scope by the export spec
itself. Everything up to a validated bundle in `staging/` is delegable; the submission is not.

**Change.** Record the exception in the autonomy contract, next to URGENT and MAJOR.

**Owner:** 🔴 **OPERATOR** — decided in conversation on 2026-08-14; this records it.

---

## P5 — Name the target variant for the in-silico task

**Problem.** The structural pipeline is variant-parameterised. Without an allele, an
orchestrator stops at step 1 — an avoidable interruption.

**Change.** The task input names the variant, the comparison baseline, and whether the MD arm
is in or out (it needs GPU-hours the repository has already recorded as not runnable in-session).

**Owner:** 🔴 **OPERATOR** — an input, not a change.

---

## P6 — Rebuild the in-silico environment, and declare what is not reproducible

**Problem.** A Q230P-style analysis cannot be re-run today.

**Evidence.** `~/.legend-venvs/insilico/` contains **biotite 0.40.0 and nothing else** relevant
— no ESM, no ThermoMPNN, no OpenMM, PDBFixer or MDTraj. `environment-md.yml` declares
`openmm 8.1.1 / pdbfixer 1.12 / mdtraj 1.10.3` but marks itself *"reconstructed […] not part of
the release-gate dependency set"*. `DATA_SOURCES.md` records the ThermoMPNN artifact as
`LEGACY_UNREPRODUCIBLE`: *"exact original commit/model checkpoint was not retained; the clone
does not claim to reproduce it."*

🔴 **The epistemic consequence, which is larger than the install.** Q230P's headline number is
`ThermoMPNN +1.51 kcal/mol`, produced by a checkpoint nobody kept. A new variant scored with a
*different* checkpoint **cannot be compared to it** — the comparison would be between two
models, not two alleles. So the rebuild must either pin a checkpoint and re-derive the Q230P
value for comparability, or the new analysis must declare non-comparability in writing. Doing
neither produces a number that looks like a ranking and is not one.

**Change.** Rebuild, pin versions and checkpoints, record what was re-derived and what stays
unreproducible.

**Owner:** delegable, local and free — but dependency installation requires separate approval
under the autonomy contract.

---

## §7 — The cockpit is deliberately not in this plan

`MULTI_AGENT_ARCHITECTURE_FEASIBILITY` is **`PRESERVED, NOT AUTHORIZED, NOT STARTED`.**

Phase −1 closed on 2026-08-11 with `BUILD_MINIMAL_DIRECTORY` accepted **as direction, not as
implementation authority**. Its two documents — `actor_identity_feasibility.md` and
`actor_identity_proposal.md` — exist only on the `evidence-index` branch and have not reached
`main`. The result is limited to **routing**: it does not authenticate identity or content and
does not solve attribution or authority. `declared_authority_non_enforced` is not a capability.

🔴 **The satisfied entry condition is the dangerous moment, not the safe one.** A debt whose
precondition has just been met is maximally easy to mistake for a work item, because the only
thing that was ever stopping it has visibly gone away. **The sequencing is the instruction, and
it did not change when the gate opened.**

**When the operator opens it, the acceptance criteria already exist** and were written before
anyone wanted a particular answer: compare the formal organization against the older
manually-coordinated model, measuring scaling 2→4→8→N readers · marginal throughput · fan-in
and Orchestrator load growth · context/token/cost amplification · collision rate and
integration latency · separation between Plan, Mirror, DMAIC and orchestration · model
diversity with Codex · whether a broker is needed · rollback conditions and `DO_NOT_SCALE`.

So **"two Scientists or four" is not a design argument to win — it is a measurement the debt
already asks for.** Any cockpit work that skips it is building the thing the debt exists to
evaluate.

---

## Summary

| # | Precondition | Owner | Blocks |
|---|---|---|---|
| P1 | Wire `assert_exportable()` into the exporter, fail-closed | delegable | DisMech export after any new batch |
| P2 | `export_gate` in the state manifest, derived not declared | delegable | unattended export |
| P3 | Paid services: hard stop → escalation | **operator** | any external compute (BioNeMo, Nebius, AF3) |
| P4 | Public push/PR added to the exception list | **operator** | Phase 5 submission |
| P5 | Name the target variant | **operator** | the in-silico task |
| P6 | Rebuild the in-silico env; settle ThermoMPNN comparability | delegable | any variant analysis |
| §7 | The cockpit | **operator authorization** | — preserved debt, do not start |
