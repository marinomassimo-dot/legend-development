# REVIEW INDEX — routing table for the 2026-08-25/26 candidate set

**Index ID:** CC-20260826-REVIEW-INDEX
**Date:** 2026-08-26
**Status:** navigation instrument. **Asserts no claim and changes nothing.**
**Purpose:** let the Orchestrator route each candidate without opening all of them.

> 🔴 **No new schema is introduced.** The commit-candidate format has no machine-readable
> `change_class` field, and inventing one here would make thirty-seven existing candidates
> retroactively non-conformant. This is a human-readable index over what the candidates
> **already say in prose**. Where a candidate does not declare something, the cell says so
> rather than guessing.

**Measured, not asserted** — reproduce with:

```bash
python3 framework/scripts/candidate_durability_index.py
```

Run over `disease-models/wwox/research/commit_candidates/` on 2026-08-26:

| Property | Count |
|---|---|
| `TRACKED` | **38 / 38** |
| `COMMITTED` (tracked, no unstaged diff vs `HEAD`) | **38 / 38** |
| `BASE_DECLARED` (`Target WM` / `Batch gate` line present) | 31 / 38 |
| `CHANGE_CLASS_DECLARED` (explicit `**Change class:**` line) | 17 / 38 |
| `CANONICAL_TARGETS_DECLARED` | 24 / 38 |
| `LOCATOR_AUDIT_TRIGGER_DECLARED` | **4 / 38** |

⚠️ **The gaps are almost entirely the pre-2026-08-25 candidates** (the sixteen `CC-20260810…` /
`CC-20260811…` / `CC-20260814…` records, 17–63 lines each), which predate the fields. **This index
does not retrofit them** — it records that they are unrouted by the modern fields and leaves them
where they are.

🔴 **These counts are object-derived and dated.** They describe the 38 files in this directory on
2026-08-26 and will move the moment a candidate is added — as they did while this index was being
written, when a first draft recorded `37 / 37` for a population that had already become 38. **Re-run
rather than cite**, and note that `COMMITTED` is measured against `HEAD`, so any file staged in the
same commit as this index reads as uncommitted at measurement time and committed immediately after.

---

## 1. 🔴 REQUIRES OPERATOR AUTHORIZATION — MAJOR, live

Route these first. Each rewrites or deletes something in a `consolidated baseline` or `DATO` claim.

| Candidate | Canonical targets | What is MAJOR | Locator audit |
|---|---|---|---|
| [`CC-20260826-FIVECLAIM-PACKAGE-01`](CC-20260826-FIVECLAIM-PACKAGE-01.md) | `CLAIM 004` `005` `011` `016` `037` + new `040` | Δ1 `CLAIM 037` Title clause deleted as **false**; Δ2 evidence boundary; Δ3 `CLAIM 005` prohibition **retargeted** | ✅ **REQUIRED** — [`CC-20260826-LOCATOR-PACKET-01`](CC-20260826-LOCATOR-PACKET-01.md) groups A, B, D |
| [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md) | `CLAIM 004` `011` + dismissal-ledger entry | Qualifies a `consolidated baseline` dose quantity; contradicts a threshold used for trial reasoning | ✅ **REQUIRED** — packet group C |
| [`CC-20260826-PROVENANCE-PAPER007-01`](CC-20260826-PROVENANCE-PAPER007-01.md) **§3.C only** | `CLAIM 006` | *"progressive microgliosis"* falsified by its own source's Fig 3b | ✅ **REQUIRED** — Fig 3b/3c/4b/4c |

**§3.A and §3.B of the provenance candidate need no authorization** — mechanical identity and
read-status repair, content-neutral. They can ship independently and should.

---

## 2. Superseded — do NOT route

| Candidate | Superseded by | Why |
|---|---|---|
| [`CC-20260825-ADVERSARIAL-FALSIFICATION-01`](CC-20260825-ADVERSARIAL-FALSIFICATION-01.md) §2 | `CC-20260826-CLAIM037-01` → `CC-20260826-FIVECLAIM-PACKAGE-01` | Contains a retracted universal negative, corrected append-only in place |
| [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md) | [`CC-20260826-FIVECLAIM-PACKAGE-01`](CC-20260826-FIVECLAIM-PACKAGE-01.md) | Found a two-claim contradiction where there is a five-claim one; dated the mouse evidence to 2026 when it is 2020 |
| [`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md) | same | Consolidated into the bounded per-claim package. **Its content is not withdrawn** — it is re-expressed |
| [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md) **§A item (4)** | [`CC-20260826-PROVENANCE-PAPER007-01`](CC-20260826-PROVENANCE-PAPER007-01.md) | Suspension recommendation was conditional on the paper being unread. It has been read; the recommendation lapses on its own terms. **Recorded append-only in §A**, table left unedited |
| [`CC-20260826-CROSS-CLAIM-CENSUS-01`](CC-20260826-CROSS-CLAIM-CENSUS-01.md) **§2** | [`CC-20260826-DOSE-ADJUDICATION-01`](CC-20260826-DOSE-ADJUDICATION-01.md) | Its predicted context resolution was **falsified**. Marked in place; the failed prediction is left legible |
| [`CC-20260826-PMID36828035-01`](CC-20260826-PMID36828035-01.md) **§2.1** | [`CC-20260826-PMID36828035-02`](CC-20260826-PMID36828035-02.md) §6.3 | Reproduced the paper's text means; the Kaplan-Meier panel does not support them |

🔴 **Every supersession above is recorded inside the superseded document as well**, not only here.
An index is a convenience; a document that does not carry its own supersession will be read alone
one day.

---

## 3. Ready to route without authorization

| Candidate | Class as declared | Canonical targets |
|---|---|---|
| [`CC-20260826-PMID36828035-01`](CC-20260826-PMID36828035-01.md) | MINOR + one MODERATE | `PAPER 007`, `CORPUS-STUB-053`, `CLAIM 016` premise tag |
| [`CC-20260826-PMID36828035-02`](CC-20260826-PMID36828035-02.md) | MODERATE | neuroinflammation / cerebellar / longevity statements |
| [`CC-20260826-UPSTREAM-CITATION-FAILURE-01`](CC-20260826-UPSTREAM-CITATION-FAILURE-01.md) | MINOR + capability proposal | `PAPER 011` `019` `063` annotations |
| [`CC-20260826-CROSS-CLAIM-CENSUS-02`](CC-20260826-CROSS-CLAIM-CENSUS-02.md) | MINOR + capability upgrade *(shipped)* | reciprocal cross-links between contradicting claims |
| [`CC-20260826-EGABA-EXPERIMENT-01`](CC-20260826-EGABA-EXPERIMENT-01.md) | MINOR | `RL-GABA-002` |
| [`CC-20260826-CLAIM002-01`](CC-20260826-CLAIM002-01.md) | MINOR | `CLAIM 002` |
| [`CC-20260826-CLAIM003-01`](CC-20260826-CLAIM003-01.md) | MINOR | `CLAIM 003` |
| [`CC-20260826-CLAIM032-01`](CC-20260826-CLAIM032-01.md) | MINOR-with-scope-change | `CLAIM 032` |
| [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md) §B–§E | MINOR per item | `PAPER 001` `027` `030` `039`, two metas |

---

## 4. Instruments — never route as changes

| Document | What it is |
|---|---|
| [`CC-20260826-LOCATOR-PACKET-01`](CC-20260826-LOCATOR-PACKET-01.md) | Blind verification packet. **Contains the word MAJOR throughout and proposes nothing** |
| [`CC-20260826-BLIND-REPLICATION-NOTRUN-01`](CC-20260826-BLIND-REPLICATION-NOTRUN-01.md) | Determination record. Declares `BLINDNESS_BROKEN` and emits no artifact |
| [`CC-20260826-INDEX-PRIORITY`](CC-20260826-INDEX-PRIORITY.md) | Earlier priority index |
| [`PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION`](PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION.md) | Gate proposal, one of four **refused** rather than deferred |
| **this file** | routing only |

⚠️ **A keyword scan for `MAJOR` over this directory returns **10** documents; only **3** propose a
MAJOR canonical change.** The other seven are instruments, superseded copies, or candidates whose MAJOR
is carried elsewhere. **Do not route by grep.**

---

## 5. Blocked, and what unblocks each

| Item | Blocker | Unblocked by |
|---|---|---|
| PMID 36828035 → `complete_fulltext_read` | `SOURCE_ACCESS_BLOCKED`: 4 supplementary files behind a JS download interstitial; Figures 2, 6–9 uninspected | a JS-capable client; then inspect the five remaining figures |
| `CLAIM 004` ↔ `CLAIM 011` residual dose gap | delivered genome copies per brain never compared across the two studies | tissue qPCR on banked Repudi material, or the Obeid Fig 5A–D assay applied to both |
| `EPILEPTOGENESIS` on any axis | **never measured in any WWOX model** | longitudinal video-EEG through the transition, from P7 |
| `E_GABA` sign | **zero measurements in the corpus** | [`CC-20260826-EGABA-EXPERIMENT-01`](CC-20260826-EGABA-EXPERIMENT-01.md) |
| `Wwox^+/−` electrophysiology | does not exist at any age | the het arm of the same cohort |

---

## 6. What this index deliberately does not do

- **Does not retrofit** the sixteen pre-2026-08-25 candidates with fields they never had.
- **Does not adjudicate** anything. Every classification here is copied from the candidate's own
  declared prose; where none exists, the cell says `NOT DECLARED`.
- **Does not supersede** any document. It points at supersessions recorded elsewhere.

---

## 7. Addendum — the 2026-08-26 hardening set (appended, table above left unedited)

🔴 **The counts in the header are stale.** The population was **38** when they were measured, **41**
when `candidate_durability_index.py` was re-run during this addendum, and **48** with the six new
candidates plus this one on disk (`ls …/commit_candidates/*.md | wc -l`). **Re-run rather than
cite** — the header warned this would happen, and it has now happened twice.

Seven candidates were added by the hardening run. **None supersedes anything.** Two change the
routing of documents already in §1.

| Candidate | Class | Route with |
|---|---|---|
| 🔴 [`CC-20260826-FIVECLAIM-HARDENING-01`](CC-20260826-FIVECLAIM-HARDENING-01.md) | 🔴 **MAJOR ×6** | **§1 row 1 — and it enlarges it.** The falsified proposition sits on **seven** surfaces; the package targets two. Adds `working_model:185`, `meta_gaba_paradox:19–20`, `DL-MECH-075`, and a **revival of `DIS-011`** |
| 🔴 [`CC-20260826-CROSS-CLAIM-CENSUS-03`](CC-20260826-CROSS-CLAIM-CENSUS-03.md) | 🔴 **MAJOR** | **route alone, first.** `working_model:165` asserts a **ketogenic-diet claim at `consolidated baseline` that exists in no registry entry**, under `CLAIM 017`'s ID. Zero new claim-vs-claim contradictions |
| 🔴 [`CC-20260826-CLAIM006-HARDENING-01`](CC-20260826-CLAIM006-HARDENING-01.md) | 🔴 MAJOR | **§1 row 3.** Confirms the panel read independently; corrects a **region error** in the drafted replacement; adds `DL-MECH-012`, `discovery_ledger:2298`, `RL-NEUROINF-001` |
| [`CC-20260826-DOSE-DECISION-TABLE-01`](CC-20260826-DOSE-DECISION-TABLE-01.md) | MODERATE | **§1 row 2.** Closes Repudi's per-hemisphere ambiguity from the Results text; relocates the **unresolvable** ambiguity to Obeid |
| [`CC-20260826-PMID36828035-DURABILITY-01`](CC-20260826-PMID36828035-DURABILITY-01.md) | MINOR + 3 handoffs | **§3.** Durability verified 4 ways; `17/17` locators matched. Status stays `PARTIAL` |
| [`CC-20260826-EGABA-CLOSURE-01`](CC-20260826-EGABA-CLOSURE-01.md) | MINOR | **§3, with `EGABA-ANALYSIS-PLAN-01`** |
| [`CC-20260826-CANDIDATE-METADATA-01`](CC-20260826-CANDIDATE-METADATA-01.md) | MINOR | **§3.** No canonical target |

🔴 **Two routing corrections to §1 and §3 above:**

1. **§1 is no longer a list of independent rows.** `FIVECLAIM-HARDENING-01` §0 shows the same
   falsified proposition routed at **MAJOR** in §1 and at **MINOR** inside
   [`CC-20260826-PROVENANCE-01`](CC-20260826-PROVENANCE-01.md) §E. **Approving either alone leaves
   the corpus self-contradictory.** Route the eleven deltas as one unit.
2. **`CC-20260826-PROVENANCE-01` §E must not ship on its own.** Its justification cites
   [`CC-20260826-CLAIM037-01`](CC-20260826-CLAIM037-01.md), which §2 lists as **superseded**.
