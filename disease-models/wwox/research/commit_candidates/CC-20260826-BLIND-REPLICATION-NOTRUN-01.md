# RECORD — blind replication NOT RUN: prerequisite absent, and blindness already broken

**Candidate ID:** CC-20260826-BLIND-REPLICATION-NOTRUN-01
**Date:** 2026-08-26
**Status:** determination record. No test was run; **no result is claimed**.
**Mode:** Phase 6 prerequisite check
**Change class:** none — this modifies nothing and asserts no scientific finding

---

## Verdict

**`BLIND_REPLICATION_EXECUTED: NO`** — on **two independent grounds**, either of which alone is
sufficient.

---

## Ground 1 — no clean participant-facing handoff exists

Phase 6 specifies a participant handoff containing **only** `CASE_ID`, `QUESTION`,
`CORPUS_BOUNDARY`, `ALLOWED_SURFACES`, contamination/access constraint expressed without revealing
the answer, and `STOP_CONDITION`.

What was found, by **filename inspection only**:

| Artifact | What it is | Why it is not the handoff |
|---|---|---|
| `lettore-c`: `PHASE1_PMID32000863_SCIC_FIRSTPASS_v1.md`, `PHASE2_CROSS_REVIEW_SCIC_v1.md`, `HOSTILE_REVIEW_RECUSED_PROPOSITIONS_SCIC_v1.md`, `SCHEMA_GAPS_PER_EDGE_OUTPUT_SCIC_v1.md` | Scientist C's own **analytical outputs** on PMID 32000863 | These are **solutions**, not a participant brief. Opening them is contamination, not preparation |
| `lettore-c`: `HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1.md` *(untracked)* | evaluator-side **case mining** | 🔴 **Explicitly out of bounds** — Phase 6 forbids opening the benchmark evaluator artifact to choose the case. **Not opened.** |
| `orchestrator`: `runtime/handoff/C-2/HANDOFF-C-2-PMID42422765.md` + `PMID42422765.working.lettore-and-lettore-b.json` | a cycle-2 handoff on PMID 42422765 | The companion file is named **`.lettore-and-lettore-b.json`** — a **shared** working surface for two actors. A jointly-held working file is the opposite of a blind case |
| `framework/eval/benchmarks/BENCH-AB-001/instructions/ASSIGNMENT.scientist-b.md` | Scientist B's assignment | Phase 7 forbids reading B's material for the case. **Not opened.** |

⇒ **No clean handoff.** Per Phase 6's own instruction — *"Se non esiste un handoff pulito: non
aspettare; passa alla Phase 8"* — no waiting occurred and Phase 8 was executed
([`CC-20260826-UPSTREAM-CITATION-FAILURE-01`](CC-20260826-UPSTREAM-CITATION-FAILURE-01.md)).

---

## Ground 2 — 🔴 `BLINDNESS_BROKEN: YES` for both candidate cases, pre-existing

Even had a handoff existed, neither candidate case could have been run blind by **this** actor.
The contamination is documented, not inferred:

### PMID 32000863 (Cheng 2020) — contaminated **before** this session

Tracked on branch `lettore`, authored 2026-08-25:

- `learning/scientist/PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md`
- `learning/scientist/FINAL_SCIENTIFIC_SYNTHESIS_PMID32000863_v1.md`
- `learning/scientist/SCIENTIST_TEAM_RECONCILIATION_PMID32000863_v1.md`
- `learning/scientist/TEAM_PHASE1_LETTORE_01_PMID32000863_ADDENDUM.md`

**And again during this session:** the paper was re-read from
`files/fulltext/PMID32000863_Cheng2020_PMC.xml` and quoted verbatim in
[`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md) (3 references)
and in [`CC-20260826-UPSTREAM-CITATION-FAILURE-01`](CC-20260826-UPSTREAM-CITATION-FAILURE-01.md).

### PMID 42422765 (Obeid 2026) — contaminated **during** this session

Read from `files/fulltext/PMID42422765_Obeid2026_PMC.html` in the first third of the session:
Figure 7 legend, the *"Surgery and ECoG data acquisition"* Methods, the WPRE dose passage, the
LD/HD figures. Quoted verbatim in commit `ba7da24`.

🔴 **Note the ordering, because it matters.** The contamination on 42422765 was **caused by the
work the operator assigned in Phases 2–4** — the reconciliation package *required* reading that
paper. Phase 6 came after. **The instruction sequence itself made the later blind test impossible
on that case**, and no amount of care at Phase 6 could have recovered it. That is a finding about
the run design, not a failure of execution, and it is recorded here so the next benchmark is
sequenced with case reservation *before* the analytical phases rather than after.

---

## What was deliberately NOT done

- The benchmark evaluator artifact was **not opened** to choose a case.
- Scientist B's assignment, outputs, branch notes and scratchpad were **not read**.
- Scientist C's analytical outputs were **not read**.
- 🔴 **No frozen artifact was produced, no `FROZEN_CONTENT_HASH` and no
  `BLIND_REPLICATION_FINGERPRINT` were computed.** Producing them would attest to a test that did
  not happen. **An artifact hash is not a hash of the artifact's validity**, and freezing a
  contaminated run would give a broken test the badge of a completed one — the exact class of
  silent false positive this repository treats as its worst failure mode.

---

## What a valid future run requires

1. **Case reservation before analysis.** The case must be sealed *before* the session's other
   phases, or those phases will contaminate it — as happened here.
2. **A participant-facing handoff carrying only the six declared fields**, authored by an actor
   that is not a participant.
3. **A case no participant has touched.** Mechanically checkable: the case PMID must appear in
   **no** commit, tracked file or receipt on the participant's branch. For `lettore`, both
   candidate PMIDs fail this check today, and the check is one `git log -S` away from being
   automatic.
4. **A declared corpus boundary naming artifacts the participant's worktree actually holds.**
   ⚠️ This worktree holds **37** of the shared checkout's **174** full-text artifacts; a boundary
   specified against the shared checkout would be unsatisfiable here without saying so.

**Proposed capability micro-upgrade:** a `BLIND_CASE_ELIGIBILITY` pre-check —
`git log -S<PMID> --all` plus a scan of the participant's tracked files and receipt ledger —
returning `ELIGIBLE` / `CONTAMINATED` with the naming object. It would have returned
`CONTAMINATED` for both candidates here in under a second, before any handoff was written.

---

## Review required

None. This record makes no claim and changes nothing. It exists so that the absence of a blind
result is legible as a **deliberate refusal to fabricate one**, rather than as an omission.
