---
artifact: LEGEND — Scientist Review Standard v1
scope: review of CANONICAL EVIDENCE OBJECTS (claims, paper records, model lines)
author: scientist-b
date: 2026-08-25
status: PROPOSED — not normative. Canonicalization requires Mirror hostile review and operator
  approval; its home if approved is framework/protocols/, not this directory.
composes: governance/annex_c_review_protocol.md (format and ladder, FROZEN) ·
  framework/eval/benchmarks/BENCH-AB-001/instructions/MODE_B.md (critical axes over a PAPER) ·
  framework/eval/learned_gates_registry.md (70 gates) ·
  framework/eval/failure_taxonomy.md · framework/instruction/epistemic_discipline.md ·
  .claude/skills/legend-locator-audit/SKILL.md (quote↔proposition triples)
---

# LEGEND Scientist Review Standard v1

## 0 · What this standard is for, and what it must not become

Four review instruments already exist in this repository and each owns a different object:

| Instrument | Object it reviews | Where |
|---|---|---|
| `MODE_B` / `INDEPENDENT_CRITICAL_READ` | **a paper** — its evidence and inferences | `BENCH-AB-001/instructions/MODE_B.md` |
| `legend-locator-audit` | **a (proposition, quote, anchor) triple** — does the quote support the proposition | `.claude/skills/legend-locator-audit/` |
| Mirror (Annex G) | **the process** — how the laboratory reasoned, reviewed and recorded | `governance/annex_g_mirror.md` |
| Annex C | **the format and the level** of any review | `governance/annex_c_review_protocol.md` — FROZEN |

None of them reviews **the canonical evidence object itself** — a `CLAIM NNN` in the registry, a
`PAPER NNN` record, a line of the working model — asking whether what it asserts is what its
sources support. `MODE_B` says explicitly: *"your object is the paper"*, not another reading.
Annex C gives the shape of a review and not its criteria. That is the gap this standard fills,
and it is the only thing it adds.

🔴 **The first obligation of this standard is not to duplicate the seventy gates.** Before
writing a finding, grep `framework/eval/learned_gates_registry.md` for the vocabulary of the
concern. If a gate covers it, cite the gate and stop. `PATTERN_ALREADY_SOLVED_GATE` applies to
reviewers first, because a reviewer who re-derives an existing rule produces a finding that looks
new and is noise.

## 1 · The output format is Annex C.2, unchanged

Annex C.2 is FROZEN and normative. A review under this standard emits exactly its fields:

```
REVIEW_ID / OBJECT / LEVEL / REVIEWER / AUTHOR / ADJUDICATOR
STEELMAN (mandatory, before the objections)
EVIDENCE_FOR / EVIDENCE_AGAINST / ALTERNATIVES_CONSIDERED / KEY_OBJECTIONS
VERDICT: CONFIRMED | WEAKENED | REFINED (+REFINED_FORMULATION) | REFUTED
REVIEWER_CONFIDENCE / RESIDUAL_UNCERTAINTY / EVIDENCE_NEEDED
WHAT_WOULD_CHANGE_MY_MIND (declared falsifier, mandatory)
AUTHOR_RESPONSE (mandatory; silence is not acceptance)
```

Where a requester asks for *accepted elements / concerns / required corrections / confidence /
recommended edge type*, those are not a second format — they map onto the frozen one:

| Requested field | Annex C.2 field |
|---|---|
| accepted elements | `STEELMAN` + `EVIDENCE_FOR` |
| concerns | `KEY_OBJECTIONS` + `EVIDENCE_AGAINST` |
| required corrections | `REFINED_FORMULATION` (with `VERDICT: REFINED`) or `EVIDENCE_NEEDED` |
| confidence | `REVIEWER_CONFIDENCE` + `RESIDUAL_UNCERTAINTY` |
| recommended edge type | recorded inside `REFINED_FORMULATION`; an edge is never emitted by a review |

`CONFIRMED` means *"no defect detected given the available evidence bundle"* — never *"true"*.
That sentence is Annex C's, and this standard does not soften it.

## 2 · Preconditions — mechanical, run before reading anything

A review that skips these produces opinion. Each is one command against a named tree, and each
scales: they cost the same at forty claims and at forty thousand.

| # | Precondition | How |
|---|---|---|
| P-1 | **Name the tree.** Every number is a measurement of one object at one commit | `git rev-parse HEAD`, and say whether the branch is behind `main` |
| P-2 | State is healthy | `legend_lint.py` · `fulltext_receipts.py verify` · `growth_anchors.py check` |
| P-3 | Generated views are not stale | regenerate `coverage_report.py` / `reading_state.py` into a scratch path and diff |
| P-4 | The object's sources are **identifiable** | every source resolves to a PMID or DOI |
| P-5 | The object's sources have a **measured reading depth** | join the source PMIDs to the receipt ledger |
| P-6 | A verified reading exists and is compared **in both directions** | if a `deepdive_manifest` exists for a source, read its locators before the claim text |

🔴 **P-1 is not ceremony.** A review conducted on a worktree 203 commits behind `main` reviews a
state nobody holds. Check before, not after.

## 3 · The five questions, and what each one is allowed to conclude

For every reviewed object:

1. **What was directly measured?** Name the measurement, its system and its n. If the object's
   own source field names an abstract, a review, or a corpus placeholder, the answer is *nothing
   was measured that this object can reach* — stop and record it as a finding.
2. **What is only interpretation?** Separate the authors' interpretation from the registry's.
   Two distinct overshoot sites: the paper may overclaim, and the registry may firm up a paper
   that did not. The second is invisible from inside the paper and is this standard's specialty.
3. **What alternative explanation exists?** Including the one the authors did not exclude, and
   including *ascertainment* — see § 4, A-5.
4. **What evidence would falsify this?** If the answer is "none, because the source cannot be
   located", the object is not weakly supported — it is **unreviewable**, which is a different
   and worse state, and it must be reported as such.
5. **Is the causal strength appropriate?** Compare the verb in the object to the verb the
   measurement licenses. *Improves* is not *normalizes*; *dependent* is not *contributed to*;
   *causes* is not *is associated with*.

## 4 · The criteria — what makes a canonical evidence object justified

Each axis is either cited to an existing gate or declared new. **An axis with no finding carries
"searched; none found" and says what was searched.** Silence on an axis is an incomplete review,
not a clean object. This rule is `MODE_B`'s and is adopted verbatim.

| # | Axis | Existing gate | What is new here |
|---|---|---|---|
| A-1 | **Provenance depth floor.** The declared epistemic type must be reachable from the deepest verified reading of its sources. `DATO` requires at least a partial full-text reading of a source that carries the asserted measurement | `EVIDENCE_SURFACE_BINDING_GATE` (fail-closed at the persistence choke point) · `HISTORICAL_DEBT_RATCHET_GATE` | **The choke point guards the door; it does not audit the room.** Objects written before it exists keep their type unchallenged. The floor must be evaluated over the *standing* state, not only at append |
| A-2 | **Source identifiability.** An object whose sources carry no PMID/DOI cannot be reviewed by anyone and cannot satisfy the registry's own consolidation rule, which requires counting *studies* | — | new; mechanical |
| A-3 | **Corroboration independence.** Count distinct **papers**, not distinct **records**. Two registry records for one PMID present one source as two | `EVIDENCE_REUSE_GATE` covers reused cohorts and lineage in the *literature* | the duplication inside the *registry* is a different object and no gate reaches it |
| A-4 | **Claim↔reading drift, in both directions.** Claim stronger than its verified locators, and reading richer than the claim | `READING_MUST_LAND_GATE` | that gate is satisfied by landing in **any** ledger, queue or registry. A reading that lands in the discovery ledger while the canonical claim stays at abstract level **passes the gate and is still drift** |
| A-5 | **Ascertainment conditioning.** An observation whose value is fixed by how the cohort was assembled carries no evidential weight for that value | `DENOMINATOR_FIRST_COHORT_GATE` covers percentages read as prevalence | extends it to *qualitative* observations, where there is no percentage to inspect |
| A-6 | **Conclusion re-derivation.** When counter-evidence is appended to an object, the object's **operative sentence** must be re-derived or explicitly reaffirmed with a reason | — | new. Appending a caveat below a conclusion leaves the conclusion running. The caveat is read by an auditor; the conclusion is read by everyone else |
| A-7 | **Mirror parity and vocabulary** | `CLAIM_MIRROR_PARITY_GATE` · LINT | cite and re-run; do not re-derive |
| A-8 | **Publication integrity** | `SOURCE_INTEGRITY` · LINT integrity gate | cite and re-run |
| A-9 | **Transfer boundaries.** Species, stage, dose, cell type, allele class | `MECHANISM_TRANSFER_FIREWALL` · `MECHANISTIC_OVERTRANSFER` | cite; report only the instance |
| A-10 | **Rescue and repurposing validity.** Comparator present; abundance vs function; a pharmacological rescue does not identify its target; genotype-specificity actually tested | `STAGE_MATCHED_COMPARATOR_GATE` · `PROTEIN_STATE_IDENTITY_GATE` · `TARGET_ATTRIBUTION_GATE` | cite; report only the instance |

## 5 · The discipline that is specifically the reviewer's

**A criticism is a claim and carries the same burden.** Every finding names the object, the
line or field, the command that reproduces it, and what it would take to be wrong. *"The
evidence is thin"* without the join is not a finding.

**Undershoot is a finding too.** If the object supports **more** than it states — a reading whose
locators are richer than the claim built on them — say so. A narrowing nobody challenges becomes
a permanent false negative, and this repository treats false negatives as the compounding loss.

**Do not manufacture criticism.** An object that is strong on an axis gets *"searched; none
found — searched: …"*. A finding invented to fill a row is indistinguishable from a real one
until someone checks, which is exactly the cost the review existed to save.

**Audit, do not rewrite.** A review emits `REFINED_FORMULATION` as a *proposal*. It never edits a
canonical file, and it never opens a `BATCH_COMMIT`. Correction of the four scientific current
files happens only through that path.

**Report negatives with their denominator.** *"Six of thirty-nine claims"* — never *"six claims"*.
A count without its population is a number nobody can audit and that ages silently.

**A failing check is evidence about the check until you have diagnosed it.** An enumerated set of
failures is falsifiable and is the right first move; it is not a diagnosis. Before treating a red
suite as a defect in the state, ask whether the *guard* moved: `designed_for_growth` forbids
pinning a number a human must remember to update, and **a path inside a test is the same class of
pin as a number**. Five of the seven suites failing at the tree reviewed in
`REV-EVIDENCE-SCIB-001` were pinned to strings in `CLAUDE.md` that a deliberate, documented
migration moved elsewhere. The rules survived; the alarms did not. A suite red across four tips
has stopped being an alarm, and the tests still green inside it have stopped being read.

**Declare the review's own level and its authority.** Annex C.1 sets floors and says reviews open
only through Orchestrator. A review opened outside that channel — by direct operator instruction,
or with no lease active — is legitimate and must **say so in `LEVEL`**, rather than borrowing a
rung of a ladder it did not climb.

## 6 · What this standard does not claim

- It is **not normative**. It is `PROPOSED` and binds nobody until Mirror reviews it and the
  operator approves.
- It does **not** replace primary reading. A review under it is only as good as the readings
  underneath, and where those are absent the correct output is *unreviewable*, not a verdict.
- It does **not** grade a paper. `MODE_B` does that, and its eleven axes are not restated here.
- Its axes are **not executable**. A-1 through A-6 are method until someone encodes them; until
  then they carry the weight of discipline, which is the weaker kind, and this file says so
  rather than implying otherwise.
