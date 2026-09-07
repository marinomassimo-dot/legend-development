---
artifact: HUMAN_REQUIRED — protocol scope conflict
id: DEC-20260817-006-GOV-SCOPE-RESOLUTION
status: PROTOCOL_CONFLICT_PENDING_DECISION
decision_owner: operator
review_required: mirror
prepared_by: plan (materialized) · orchestrator (composed from measurement) · operator (structure)
domain: CONTROL PLANE — governance/candidates/, so materializing this moves no candidate hash
reason_durable: §4 requires a HUMAN_REQUIRED to produce a durable object and never only a
  message. The Orchestrator can write nowhere durably — it has no worktree and the root must
  stay clean — which is the fourth unlisted cost of EVAC-20260817-001.
---

# Protocol scope conflict — decision required

> **PROVENANCE.** Structure composed by the operator; filled from measurement by the
> Orchestrator; materialized by Plan, who re-verified §B and added §C-3. Relayed, not
> originated. **If the operator states this directly, theirs is authoritative over this file.**

## A · Conflict statement — neutral

`framework/protocols/prompt_batch_commit.md` carries two clauses that have been read as
incompatible.

```
line 19    "BATCH_COMMIT is the only moment when the 4 scientific current files are
            modified. Outside BATCH_COMMIT, the current files are read-only."

Phase 3    snapshot required over nine patterns: working_model · claim_registry ·
            paper_registry · literature_tracking_log · meta_*_current ·
            research_*_current · biomarker_candidates · clinical_monitoring_endpoints ·
            state_manifest — closing "Without a complete snapshot: ABORT."
```

**Executed history.** Five commits self-identifying as batches modified `*_current.md`
outside `registries/` alongside the four registries: `BATCH_20260806_001`, `_002`,
`BATCH_20260810_003`, `_004`, `_005`. The specific case is `d0f6a78` /
`BATCH_20260806_002` — `meta_gaba_paradox`, `meta_prenatal_structure`,
`research/dismissal_ledger`.

Stated without argument for any reading. The structural evidence is in
`DEC-20260817-006-L2-SCOPE.md` §§5–5f and is deliberately not repeated here, so this section
stays neutral.

## B · Governance analysis — verified by Plan, not relayed

- **No declared rule resolves a conflict between clauses of the same document.** Checked:
  `CLAUDE.md:5` governs router-vs-normative — *"if this file and a normative file ever
  disagree, the normative file wins"* — and both clauses are inside the same normative file,
  so it does not reach. `LEGEND_CORE.md` and `protocols/index.md`: nothing on clause
  precedence.
- **§5's hierarchy does not resolve it.** Verified verbatim: it ranks *sources* — governance
  and safety rules, operator directive, Orchestrator directive, role rules, local
  optimization. Both clauses sit at the same level, in the same document, from the same
  author. The hierarchy has no axis along which they differ.
- **§12's doubt rule is scoped to `CHANGE_CLASS`**, not to clause conflict.

**Therefore the choice is normative, not technical.**

**One rule does govern the handling, though none governs the resolution.**

> **COR-20260817-GOV-001 — Plan's citation of `LEGEND_CORE.md:165` is withdrawn.** Read in
> full that line governs **claim status vocabulary**: *"Valid states: consolidated baseline |
> in observation | conflicting evidence | … Never invent states. … Non-standard states →
> flag, do not autonomously correct."* It is about claim states, not document interpretation.
> Plan applied it by analogy and the analogy is loose. Raised by the Orchestrator, verified
> here, corrected by append.
>
> **The behaviour it was cited to justify needs no citation.** The operator owns the
> governance question and commissioned a package on it; an actor concluding *"there is no
> question"* is exactly the kind of dissolution that must be **proposed rather than
> enacted**. That reason stands alone, and it is the actual basis on which no option below
> has been acted on.

## C · Decision required

### Option A — line 19 defines the normative boundary

- snapshot scope = 4 scientific current files + manifest
- Phase 3 must be interpreted or reformulated
- past history must be assessed against that boundary

### Option B — Phase 3 defines the normative boundary

- snapshot scope = every declared pattern
- line 19 must be corrected
- `batch_commit.py` must be brought into conformance

### 🔴 Option C — **the conflict may not exist.** Added by Plan; read the grammar

Both the Orchestrator and Plan read line 19 as an exclusivity claim about **which files a
batch modifies**. Its grammar makes an exclusivity claim about **when those four files are
modified**:

```
"BATCH_COMMIT is the only moment when the 4 scientific current files are modified"
                 └─ the ONLY MOMENT ─┘        └─ for THESE FOUR files ─┘
"Outside BATCH_COMMIT, the current files are read-only"     ← confirms the temporal reading
```

It says: *for those four files, a batch is the only time they change.* **It does not say a
batch modifies nothing else.** Neither sentence constrains the set of files a batch may
touch.

Under this reading:

| | constrains |
|---|---|
| line 19 | **when** the four registries may change — a read-only rule for everything outside a batch |
| Phase 3 | **what** must be captured before a batch applies — a safety rule inside it |

They address different questions, and **the executed history is consistent with both**: the
five batches modified the four registries, which line 19 permits, plus other files, which
line 19 never mentions and Phase 3 requires be snapshotted.

**If C is correct, then A and B are both answers to a question that was never posed** — and
`COR-20260817-006-001`'s conclusion was wrong for a reason neither correction identified.
This is the day's recurring signature once more, at clause scale: the reading was accurate
about a claim the sentence does not make. Both actors took *only* to scope the file set when
it scopes the moment.

> **RES-20260817-GOV-001 — C now rests on evidence, not only on grammar.** Four supports,
> each verified by Plan at source after the Orchestrator raised them:
>
> **1 · Distribution.** `current files` appears **six** times: lines 3, 11, 19, 20, 64, 106.
> **Exactly one carries the "4 scientific" qualifier — line 19**, the exclusivity sentence
> itself. Every other occurrence is unqualified.
>
> **2 · Immediate context.** §0's opening states the batch's purpose as *"actual updates to
> the current files"* — unqualified — and line 20, the very next sentence, reverts to
> unqualified. **The qualified form is bracketed on both sides by the wider set**, which is
> not how a scope declaration behaves.
>
> **3 · A fourth clause nobody had read.** Line 372: `| 4 (Propagation) | All types | Only
> impacted files |`. **Phase 4's write scope is a variable set determined by the candidates**,
> not a fixed four. A third clause treating the file set as open.
>
> **4 · Plan's addition — the gate-bearing clauses use the wide form.** Line 64 is a
> pre-flight `ABORT` condition: *"Backup of the current files available | ABORT — create a
> backup first"* — unqualified. So **both clauses that carry an ABORT** (line 64's backup
> gate, Phase 3's completeness gate) speak of the wide set; only the temporal-exclusivity
> sentence narrows. Where the protocol is protecting something, it never says four.
>
> **Reading, consistent across all four clauses:** line 19 quantifies **moments** for the four
> registries · Phase 3 governs **what is captured** before an apply · Phase 4 governs **what
> is written**, scoped to impact · line 64 gates on the backup existing. Four clauses, four
> questions, **no contradiction.**
>
> **Withdrawn: "the protocol contradicts itself"** (`DEC-20260817-006-L2-SCOPE.md` §5d,
> Orchestrator-originated, adopted by Plan). No conflict on scope is established.

**Plan does not adopt C.** It is flagged as the reading that must be excluded before A or B is
chosen, because choosing either would amend a document that may not need amending — and
because the dissolution of a question the operator posed is theirs to accept, not an actor's
to enact.

**What C does not dissolve.** The engineering findings in §D stand under every option: they
are about a tool that cannot fail, not about which clause is law. If C holds, the tool is
still narrower than Phase 3 and still cannot report it.

## D · Engineering invariants — independent of the decision, NOT to be implemented now

1. `restore()` never removes files absent from the snapshot
2. `snapshot()` cannot fail on incompleteness — **two independent paths**: a narrow list, and
   `if os.path.isfile(src)` skipping silently. **Widening the list repairs only the first.**
3. the test suite cannot exhibit the defect — a round trip over its own fixture in a
   temporary repository, shipped in `run_release_regressions`

**None of the three moves under any option.** The decision fixes the list; it does not make a
gate capable of failing.

## E · Authority

```
DECISION_OWNER    Operator
REVIEW_REQUIRED   Mirror
REASON            the choice changes the normative meaning of the protocol, not only its
                  implementation. framework/protocols/ is content domain, so every option —
                  including "Option C, no amendment" — is a governed outcome and needs a
                  recorded decision.
STATUS            PROTOCOL_CONFLICT_PENDING_DECISION
NEXT_STEP         Operator + Mirror resolution required
```

**No code change · no candidate opened · no batch · no capability promoted · 21 of 21
UNVERIFIED · `main` `908197ba` · root clean · `HASHDET` `c85acdb2…` unchanged.**

---

# RESOLVED — 2026-08-17

```
STATUS:         DECISION RESOLVED
BOUNDARY:       OPTION B — REGISTRY-DEFINED SCIENTIFIC STATE
NORMATIVE TEXT: FINALIZED
DECIDED_BY:     Operator
```

## 🔴 BINDING TRANSMISSION RULE

**The normative text below is FROZEN and must be copied VERBATIM into every future candidate,
amendment or derived document. Do not reformulate, condense or summarise it.**

The operator's recorded motivation: a previous condensation had already eliminated two agreed
normative properties — **(1) fail-closed on the minimum protected core**, and **(2) the
distinction between scientific-layer `BATCH_COMMIT` and governance-layer
`CANONICAL_BATCH_COMMIT`**. **Any free reformulation is a clause-loss point with no diff.**

Copied here character-for-character, with nothing added inside it.

## FROZEN NORMATIVE TEXT — verbatim

> Phase 3 defines the canonical snapshot boundary. The four scientific current files are the minimum protected core: BATCH_COMMIT fails closed if any of them is absent or invalid at snapshot time. The complete scientific state is defined by the SCIENTIFIC_SURFACE_REGISTRY, in which every `*_current` surface is classified CANONICAL (atomic snapshot/restore scope), DERIVED_REGENERABLE (regenerated and verified; audit preservation controlled by registry flag), or TRANSIENT (registered exclusion). Registry membership and classification change only through governed amendment. Batch scope is explicit and verified by bidirectional structural checks. Previous batches are classified only after empirical evaluation against this boundary. This scientific-layer BATCH_COMMIT is distinct from the governance-layer CANONICAL_BATCH_COMMIT.

## FROZEN_TEXT_INTEGRITY — addendum, 2026-08-18

> 🔴 **The frozen normative text above is UNCHANGED by this addendum.** The digest is a
> metadata field of this record and does not alter the frozen block. Nothing in this section
> is part of that block.

```
FROZEN_TEXT_INTEGRITY:

  SHA256:
  1a0460861862c7903a6d22ebcab6fcff5085c63fb16650b8aa618b8963e1ff0f

  LENGTH:
  832 characters

  CANONICALIZATION:
  blockquote markers ("> ") stripped; internal whitespace runs collapsed to single space;
  leading/trailing whitespace trimmed; no trailing newline.

  VERIFICATION:
  recompute-and-compare mandatory for every document deriving from DEC-006 that quotes the
  frozen normative text.
```

**The canonicalization travels with the digest, and that is the load-bearing half.** A digest
without its normalisation rule is not reproducible — whoever recomputes next would be
measuring a different object and getting a true answer about it, which is the failure mode
this entire record has catalogued.

**Independently verified against this file after registration**, applying the stated
canonicalization in full rather than assuming it is a no-op on a single-line block: extracted
from the committed artifact, `"> "` stripped per line, whitespace runs collapsed, trimmed, no
trailing newline → **832 characters, digest matches.**

Provenance of the value: transcribed by the Orchestrator from the operator's message, and
extracted by Plan from the committed blob. **Two actors, two source objects, one value** — and
neither computed it from the other's copy.

## FUTURE CANDIDATE SCOPE — recorded, NOT to be executed now

1. **PROTOCOL AMENDMENT** — `framework/protocols/prompt_batch_commit.md`, correcting the
   clause relating to the "4 scientific current files" and aligning it to the defined
   boundary.
2. **SCIENTIFIC_SURFACE_REGISTRY** — surfaces listed; each classified CANONICAL /
   DERIVED_REGENERABLE / TRANSIENT; rationale per surface; required registry flags.
3. **ACCEPTANCE CRITERIA** — bidirectional LINT between real filesystem and registry
   (`*_current` present but unregistered; surface registered but absent); fail-closed of the
   minimum protected core during snapshot; test of the real snapshot/restore failure path.
4. **HISTORICAL BATCH EVALUATION** — `BATCH_20260806_001`, `_002`, `BATCH_20260810_003`,
   `_004`, `_005` assessed against the new boundary, output `compliant` / `compliant under
   clarified boundary` / `non-compliant`, with no retroactive classification unsupported by
   evidence.

### Acceptance criterion 4 — restore atomicity · added 2026-08-18

```
4. Restore atomicity:

   restore() must remove non-snapshot files introduced during failed batch execution.
   Post-restore state must equal pre-snapshot state exactly, including the absence of files.
```

**The operator states explicitly that this criterion must NOT be considered implicit in the
word "atomic".**

**This closes the OPEN flag below.** The flag read: *"it may be intended inside `CANONICAL
(atomic snapshot/restore scope)` … but* may live inside *is not* enumerated*, and the criteria
enumerate."* It is now enumerated, in the operator's own words. **The ambiguity is removed
rather than resolved by interpretation** — which is the difference the flag was arguing for,
and it is the outcome that vindicates raising it while the candidate was still unwritten.

Status of the flag: **CLOSED — 2026-08-18, by enumeration.** Retained below unedited, per the
append-only discipline; superseded, not withdrawn.

## NOT AUTHORIZED BY THIS DECISION

No code change · no modification of `prompt_batch_commit.md` · no candidate opened now · no
batch · no `main` movement · no change to existing candidates · no capability state change ·
no `VERIFIED`/`DEMONSTRATED` promotion. **The decision queues behind the governance flow
already in progress.**

---

## 🔴 OPEN FLAG — invariant 1 is not in the acceptance criteria

Raised by the Orchestrator, verified by Plan against the list above. **Not a challenge to the
decision and not a reformulation of the frozen text** — a note on the acceptance-criteria
item, which is separate from the normative text.

Of §D's three engineering invariants, criterion 3 covers two:

| §D invariant | Covered by criterion 3? |
|---|---|
| 2 · `snapshot()` cannot fail on incompleteness | ✅ *"fail-closed of the minimum protected core during snapshot"* |
| 3 · the test cannot exhibit the defect | ✅ *"test of the real snapshot/restore failure path"* |
| **1 · `restore()` never removes files absent from the snapshot** | ❌ **not enumerated** |

It may be intended inside `CANONICAL (atomic snapshot/restore scope)`, since *atomic* implies
all-or-nothing. But the acceptance criteria enumerate three things and removal is not among
them — **and this is exactly the shape of loss the transmission rule exists to prevent**: a
property agreed in one document, absent from the checklist that will be implemented against
it.

Flagged while the candidate is still unwritten. **After it is written, the omission becomes a
diff nobody has.** No wording is proposed and nothing is added to the frozen text.

## Note on Option C — recorded because the resolution touches it

The operator resolved the question rather than dissolving it, so **C is not adopted**. Worth
recording that the frozen text does not simply declare line 19 false: it preserves the four
files' special status as the **minimum protected core** with a fail-closed condition, while
Phase 3 defines the boundary. What line 19 was protecting survives under a different name.
Item 1 of the future scope nonetheless amends that clause, so the ambiguity C identified is
removed rather than left standing. Recorded as an observation; the decision is the operator's
and is not reopened here.

## CHOSEN

```
OPTION B — REGISTRY-DEFINED SCIENTIFIC STATE
```

## RATIONALE

Phase 3 defines the canonical snapshot boundary; the four scientific current files are
retained as the minimum protected core with a fail-closed condition; the complete scientific
state is defined by the `SCIENTIFIC_SURFACE_REGISTRY` under governed amendment. See the frozen
normative text above, which governs over this summary line and must be quoted verbatim rather
than paraphrased from it.

## DECIDED_BY

```
Operator — 2026-08-17
```
