---
artifact: BENCH-AB-001 — precondition report from scientist-b
actor_id: scientist-b
task_id: BENCH-AB-001-B
benchmark_id: BENCH-AB-001
status: NOT_STARTED — input surface never handed over
reported_on: 2026-08-26
---

# BENCH-AB-001-B — precondition report: the reading was not started, and why

**This is the report the surface router asks for.**
`instructions/SURFACE_CLAUDE.md`: *"If you believe something essential is missing, **say so and
stop**: a missing input is a finding about the benchmark, not a reason to go looking."*
Something essential is missing. This says so, and stops.

---

## 1 · What was read, and nothing else

Exactly four participant-facing files, all from `framework/eval/benchmarks/BENCH-AB-001/instructions/`,
read out of the `lettore-c` tree with `git show` (no checkout, no working-tree change):

| File | Why |
|---|---|
| `instructions/BENCHMARK_INSTRUCTIONS.md` | the common contract; declares the packet and the two prohibitions |
| `instructions/SURFACE_CLAUDE.md` | the surface router; declares what the surface is and what to do when an input is missing |
| `instructions/ASSIGNMENT.scientist-b.md` | **my own** assignment |
| *(frontmatter only, of the above)* | `identical_for: scientist-a, scientist-b` |

**Not read, deliberately:**

| File | Why not |
|---|---|
| `population/evidence_units.json` | evaluator artifact — the ground truth. Excluded by the Operator's Phase-7 instruction and by the benchmark's own design |
| `benchmark_manifest.json` | evaluator artifact |
| `surface_spec.json` | evaluator artifact |
| `instructions/ASSIGNMENT.scientist-a.md` | **not needed.** `BENCHMARK_INSTRUCTIONS.md` carries `identical_for: scientist-a, scientist-b` in its frontmatter and names the paper in §1, so the shared `CASE_ID` is established from the common contract without opening the other reader's assignment |
| `instructions/MODE_A.md` | the other reader's mode directive. `ASSIGNMENT.scientist-b.md` says *"your mode, and only yours"* |
| every LEGEND artifact naming PMID 42397075 | the benchmark's first prohibition |

**`BLIND_CASE_ID: PMID 42397075`** · doi `10.1093/brain/awag239` · *Brain*, 2026, accepted manuscript.
Established from the common contract, not from A's assignment and not from A.

---

## 2 · Why the reading was not started — three blockers, each sufficient on its own

### Blocker 1 — the input surface was never built

`ASSIGNMENT.scientist-b.md` declares `WORKING SURFACE: this directory — its own git repository, its
own branch`, and `SURFACE_CLAUDE.md` opens with *"This directory is **not** the LEGEND repository."*

**That directory does not exist.** A filesystem search for any `BENCH*` directory under
`<HOME>/Desktop` and `/private/tmp/claude-501` (depth 4) returns nothing. The builder
`framework/scripts/benchmark_input_surface.py` is committed and has a test suite; it has not been
run to produce a surface for `scientist-b`, or if it has, the result was not handed over.

### Blocker 2 — the paper packet is absent from every path I am permitted to use

`BENCHMARK_INSTRUCTIONS.md` §1 lists seven files: the article PDF, its extracted text surface, and
five asset PDFs (author contributions, detailed methods, supplementary figures 1–10, resource table,
uncropped westerns).

```
files/fulltext/  →  no PMID42397075 artifact of any kind
files/fulltext/PMID42397075*  →  no match
```

**The article does not exist on this surface.** No amount of discipline substitutes for the paper.
The instruction for exactly this case is to say so and stop, and the alternatives available to me —
fetching the PDF from outside, reading the prior LEGEND manifest, or reconstructing the paper's
content from `evidence_units.json` — are, in order: an unauthorized external retrieval, the
benchmark's first prohibition, and reading the answer key.

### Blocker 3 — `lettore-b` is disqualified as a substitute surface

Running the reading here instead was considered and rejected. This worktree contains, tracked and
on `main`:

| Path | Occurrences of `42397075` | What it is |
|---|---|---|
| `disease-models/wwox/research/deepdive_manifests/PMID42397075.json` | **57** | LEGEND's prior work manifest on the benchmark paper |
| `disease-models/wwox/research/fulltext_dossiers/PMID42397075_partial_locators.md` | 15 | its locator dossier |
| `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | 34 | its read receipts |
| `disease-models/wwox/research/discovery_ledger_current.md` | 10 | prior discovery entries |
| `disease-models/wwox/research/full_text_queue_current.md` | 9 | prior queue entries |
| **`framework/eval/benchmarks/BENCH-AB-001/population/evidence_units.json`** | **67** | 🔴 **the evaluator's ground truth, in the same working tree** |

Thirty-two files in this worktree name the paper. The surface exists to make a first reading *"blind
by construction rather than by promise"*; here it could only ever be blind by promise, in a tree
where an ordinary sweep prints ±300-character context windows out of thirty-nine files at a time.
**A promise is not the property the benchmark is measuring.**

---

## 3 · `BLINDNESS_BROKEN: NO` — measured, not asserted

The claim that nothing was contaminated is checkable, so it was checked rather than asserted.

| Check | Method | Result |
|---|---|---|
| Did any file I opened this session contain prior work on 42397075? | line-number intersection of the `42397075` occurrences against the exact ranges read | `full_text_queue_current.md` carries the string on lines **147, 149, 153, 928, 1049, 1062, 1117, 1120**; the ranges read this session were **1–50**, **3489–3530** and the final 30 lines. **Intersection: empty** |
| Was `deepdive_manifests/PMID42397075.json` opened? | never referenced in any tool call this session | no |
| Was `fulltext_dossiers/PMID42397075_partial_locators.md` opened? | never referenced | no |
| Was `population/evidence_units.json` opened? | never referenced | no |
| Was `reviews/scientist-b/REV-EVIDENCE-SCIB-001.md` opened? | committed by this branch at `cbcd364` on 2026-08-25; **not opened this session**; its two `42397075` occurrences were located by line number only (368, 372) and not read | no |
| Did any sweep print 42397075 content into context? | the Phase-5 sweeps printed contexts from `mechanism_intervention_map.md`, `therapeutic_translation_second_pass.md`, `claim_registry_current.md`, `paper_registry_current.md`, `therapeutic_hypotheses_ledger_current.md` and a set of manifests; none of the printed windows contained the string | no |

⚠️ **And the honest qualification.** The intersection came out empty **by the arithmetic of line
numbers, not by method**. Nothing in how I worked today prevented a sweep from printing prior
42397075 analysis into my context; the queue read stopped 775 lines short of the first occurrence
because of where `FT-071` happens to sit. That is luck, and it is the strongest argument in this
report for Blocker 3: a surface where blindness survives on luck is not a surface where blindness
can be attested.

> ## `BLIND_REPLICATION_EXECUTED: NO`
> ## `BLINDNESS_BROKEN: NO`
> ## `FROZEN_ARTIFACT_ID: — none. Nothing was read, so nothing was frozen.`
> ## `BLIND_REPLICATION_FINGERPRINT: — not computed; a fingerprint over no reading is an attestation of nothing.`

**No `FROZEN_CONTENT_HASH` is offered.** A hash without a reading behind it is an attestation, and
this report's whole point is the difference between the two.

---

## 4 · What would make `BENCH-AB-001-B` runnable

1. **Build the surface** with `framework/scripts/benchmark_input_surface.py` and hand over its path.
2. **Include the seven-file packet** — article PDF, text surface, and the five asset PDFs — with the
   digests the manifest records, verified equal in both surfaces before handover.
3. **Hand it over as a directory outside any LEGEND checkout**, so that the two prohibitions are
   enforced by the allowlist rather than by my restraint.
4. Nothing else is needed. The mode directive, output schema and discipline files are already
   inside the instructions set, and my assignment is unambiguous.

Until then this task is `NOT_STARTED`, not `FAILED` and not `PARTIAL`. **No reading was begun, so
no partial reading exists to declare.**

---

## 5 · A finding about the benchmark, not about the paper

The instructions ask that a missing input be reported as a finding. Three, ordered by how much they
would cost the experiment if uncaught:

1. 🔴 **The evaluator's ground truth (`population/evidence_units.json`) is committed on `main` and is
   therefore present in every LEGEND worktree**, including both readers'. It is excluded from the
   input surface by the allowlist, which is correct — and it is one `git show` away from either
   reader at any moment, which the allowlist cannot prevent. If the surface is ever not used, the
   answer key is already local.
2. 🔴 **LEGEND's prior reading of the benchmark paper is likewise on `main`** — a 57-occurrence
   manifest and a locator dossier — so the first prohibition is a rule about restraint in every
   checkout rather than a property of any of them.
3. ⚠️ **The handover step has no receipt.** There is a builder script, a surface spec and a
   manifest, and no artifact that records *"surface built for actor X at path P on date D"*. The
   absence of the surface was discoverable only by looking for it and failing to find it, which is
   how this report started.

**Nothing here is medical advice**, and a benchmark does not change that.
