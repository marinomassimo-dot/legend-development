# COMMIT CANDIDATE — CC-20260914-EVIDENCE-DEPTH-01

**Actor:** `orchestrator` · **Date:** 2026-09-14 · **Mandate:** `SCIENCE-EXEC-20260914` step E1
**Class:** MINOR, one added line in six records · **Scientific delta:** none — no claim, pathway, relevance or role changes
**§21d consultation:** requested with the next consultation batch; the line states a receipt that already exists
Public, disease-level, de-identified. **Nothing here is medical advice.**

## 1 · The defect, measured

`test_batch_queue.py` compares its read side (**105**; `batch_queue`'s report says 93 on a different
instrument) against `PAPER` records whose text carries
a full-text marker (63). Decomposed on 2026-09-14, by joining the receipt ledger on `study_id.pmid`
against the registry `Identifier` through the shared parser, the 30-row gap is **three different
things**, and only one of them is this candidate:

| Part | Rows | Where it is handled |
|---|---|---|
| placeholders read in place | 20 | step I3 (a disposition per record) |
| completed reads with no record | 5 | step I1 |
| **`PAPER` records with a complete receipt and no full-text marker** | **6** | **this candidate** |

For those six the reading exists and is attested; the record does not say so, in any of the four
marker forms the test and the coverage report read.

## 2 · The six records and their receipts, each verified in the ledger

| Record | PMID | Current `Status` | Complete receipt | Other receipts on the same PMID |
|---|---|---|---|---|
| `PAPER 007` | 36828035 | `integrated` | `FTR-20260913-36828035-03` | `-01`, `-02` partial |
| `PAPER 018` | 36779245 | `filtered_in` | `FTR-20260804-36779245-02` | `-01` partial; `-03` partial re-read |
| `PAPER 019` | 32000863 | `processed` | `FTR-20260804-32000863-01` | none |
| `PAPER 020` | 32581702 | `processed` | `FTR-20260810-32581702-01` | none |
| `PAPER 021` | 31340538 | `processed` | `FTR-20260806-31340538-01` | none |
| `PAPER 024` | 25012504 | `processed` | `FTR-20260814-25012504-01` | none |

Every complete receipt listed has **no `not_read`** section in its coverage map.

## 3 · The proposed change

For each record, insert one line immediately under `**Status:**`, in the form the three most recent
records already use (`PAPER 094`, `095`, `096`):

> `**Evidence depth:** complete_fulltext_read — receipt <FTR id>`

For `PAPER 018` the line adds: *"a later partial re-read, `FTR-20260810-36779245-03`, does not
supersede it"* — so the shallower later event cannot be read as the record's depth.

Nothing else changes. In particular **no `Status` value is touched**: `PAPER 018` reads `filtered_in`
while its paper is read in full, which is a real inconsistency, but a status is a lifecycle judgement
and moving it is a separate act with its own consultation, not a bookkeeping line. No role, pathway,
transferability, relevance or claim link is written.

## 4 · Predicted measurable effect, to be checked after propagation

- `test_batch_queue.py`: the **registry side** rises from **63 to 69**. The guard's **read side** is
  **105**, not 93 — 93 is `batch_queue`'s own `counts["full text"]`, a different instrument. The guard
  therefore stays **red at 105 > 69**
  until I1 and I3 are dispositioned too. This candidate does not claim to close it.
- `coverage_report` `full_text`: **63 → 72**, measured today as the baseline. 71 would mean `PAPER 018`
  was appended to rather than replaced, and that single number is the test.
- `coverage_report.md` and `batch_queue.md` must be regenerated inside Phase 4.7 of the same window.
- No LINT, publication-gate or growth-anchor change expected.

## 5 · Questions for the consultation

1. Is a depth line the right instrument, or should the marker live in `Status` — which would change six
   lifecycle values instead of adding six factual lines?
2. `PAPER 018`: is naming the superseding relation in the depth line enough, or does the later partial
   receipt need its own annotation?
3. Does stating a receipt that exists count as a zero scientific delta, as this candidate assumes, or
   as a provenance change that must move with any surface citing those six records?

---

## BATCH DISPOSITION — appended by the integrator, append-only

**Status:** **RE-QUEUED** — recovered 2026-09-26 from the VPS backup (`06ee25a`). The VPS batch that disposed of this candidate never reached `main`: re-queued for `BATCH_20260926_ALDAZ`. Identifiers written on the VPS are annotated in place as `(VPS numbering)` / `(VPS batch, never on main)`; full-text queue ids were renumbered (see `disease-models/wwox/research/vps_recovery_20260925/README.md`).


---

## BATCH DISPOSITION — `BATCH_20260926_ALDAZ_R2` (2026-09-26, ACTOR_ID `scientist-a`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260926_ALDAZ_R2`.

0 edits. All six records already carry the `Evidence depth` line this candidate proposed, written on main after the VPS split: `PAPER 018`, `019`, `020`, `021` and `024` by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (`BATCH_20260920_001`), and `PAPER 007` by `BATCH_20260926_ALDAZ` (receipt `FTR-20260913-36828035-03`). Verified record by record against main's text; each line names the same complete receipt this candidate's table lists. The VPS propagation (`BATCH_20260915_009`, VPS batch, never on main) is not reapplied.

### Disposition correction — 2026-09-26, ACTOR_ID `orchestrator`
The SUPERSEDED status above applies only to the six `Evidence depth` lines. The candidate's PAPER 018 proposal to state that the later partial re-read `FTR-20260810-36779245-03` does not supersede the complete read remains owed, as does reconciliation of PAPER 018's `filtered_in` status with its complete-fulltext receipt. These are open items, not zero-edit supersessions.

---

## WAVE-2 READINESS (2026-09-27)

**context_policy declared:** `SYNTHESIS`. The inputs are the ledger's own events
(`fulltext_receipts.py status --pmid 36779245`) and the live `PAPER 018` record reached with
`registry_records.py get --id`; no source was reopened for this item and nothing here turns on a
fact inside a paper.

**Actor:** `scientist`, wave-2 package `provenance`.

### What I did

1. **Re-derived the ledger state for PMID 36779245 rather than trusting the candidate's wording.**
   Four events exist:

   | event | depth | prior | reread_reason | coverage |
   |---|---|---|---|---|
   | `FTR-20260804-36779245-01` | partial | — | first_read | figures `captions_only` |
   | `FTR-20260804-36779245-02` | **complete** | `-01` | inadequate_prior_coverage | everything read; supplementary `unavailable` |
   | `FTR-20260810-36779245-03` | partial | `-02` | inadequate_prior_coverage | methods/results/tables/discussion |
   | `FTR-20260923-36779245-04` | partial | `-03` | new_version_or_supplement | **supplementary only** |

2. 🔴 **The candidate's clause is stale exactly as its triage said.** It names only `-03`, while a
   **second** later partial (`-04`, the supplement, 2026-09-23) now exists. Written as drafted, the
   clause would protect the complete read against one successor and be silent about the other —
   and the silent one is the one that read a surface `-02` recorded as `unavailable`. The clause is
   re-derived below to cover both, and to say what `-04` adds rather than only that it does not
   supersede.
3. **Checked the six-line part** the candidate opened with: six `Evidence depth` lines are present
   (e.g. `PAPER 018`'s own `complete_fulltext_read — FTR-20260804-36779245-02`), landed by
   `BATCH_20260920_001` / ALDAZ. That half is spent.
4. **Counted the manifest as it stands now**: `deepdive_manifests/PMID36779245.json` holds **27**
   locators after this package added seven (entries 20–26) for
   `CC-20260921-CLAIM033-REPLICATION-01`. The record's current text says 20, so the op below
   re-derives the number instead of leaving a count that was true last week. ⚠️ The record's
   *"strict PASS"* is also no longer reproducible in a fresh checkout: two declared artefacts,
   including the 2026-08 one the first 20 locators quote, are **absent from this deployment**, so
   the honest statement is structural PASS with the artefact locality named.

### Verdict — **READY_MINOR**

One provenance line on one registry record. No claim moves, no depth is upgraded or downgraded, no
reading is re-graded: the op writes down what the ledger already says.

### Operation list for `batch_commit.py propagate`

**File:** `disease-models/wwox/registries/paper_registry_current.md` — **full rewrite** (the paper
registry is propagated by full rewrite; `propagate` refuses it by name, exit 4). Every other
section is copied verbatim; only the two lines below change inside `PAPER 018`.

**OP 1 · record `PAPER 018` · replace one line**

*old (verbatim, from the current file):*

```
**Evidence depth:** complete_fulltext_read — `FTR-20260804-36779245-02`; manifest `deepdive_manifests/PMID36779245.json` (20 locators, schema v2, strict PASS, 3 declared gaps); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's
```

*new:*

```
**Evidence depth:** complete_fulltext_read — `FTR-20260804-36779245-02`; manifest `deepdive_manifests/PMID36779245.json` (27 locators, schema v2, 3 declared gaps; structural PASS — two declared artefacts, including the 2026-08 XML the first 20 locators quote, are absent from this deployment, which is an evidence-locality fact and not a provenance failure of the reading); declaration reconciled from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's. **Two later PARTIAL re-reads exist and NEITHER supersedes the complete one** (`CC-20260914-EVIDENCE-DEPTH-01`, re-derived from the ledger 2026-09-27): `FTR-20260810-36779245-03` (methods, results, tables, discussion) and `FTR-20260923-36779245-04` (**supplementary only** — it read `Table S1`, the surface `-02` recorded as `unavailable`, and found a variant/ACMG census with no age, outcome or survival column). A later partial is an ADDITION to the covered surface, never a downgrade of the complete event, and the two together are why this record's depth does not move. Seven locators were added on 2026-09-27 from a re-acquired PMC surface (`PMID36779245_Oliver2023_PMC_2026-09-27.xml`), declared beside the historical artefact rather than substituted for it.
```

### The second residual — **DEFERRED**, deliberately

`PAPER 018` carries `Status: filtered_in` against a complete receipt and `Claim links: pending`
while `CLAIM 033`, `CLAIM 017` and `CLAIM 030` name it as Source. The candidate itself refuses to
decide that, and so does this section: **it is a lifecycle judgement, not a provenance repair**,
and `BATCH_20260920_001` deliberately did not change it either (*"whether this reading produces a
claim is a scientific question it did not ask"*). **What would unblock it:** one decision, by the
Orchestrator under §21d, on whether a record cited as Source by three claims may keep
`filtered_in` / `Claim links: pending` — applied once across every record in that state, not on this
one alone. Writing it here would settle a vocabulary question for the whole registry from a sample
of one.

**Change class:** MINOR (registry provenance line). **Review floor:** R2 as declared.
**Pending:** the lifecycle decision above; the six-line part is spent — **CLOSE / SUPERSEDED** by
`BATCH_20260920_001` and the ALDAZ batches.

## BATCH DISPOSITION — `BATCH_20260927_003` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** **PROPAGATED IN PART** — `BATCH_20260927_003` (MINOR, MANUAL, `WM_v6.0` → `WM_v6.1`).

`OP 1` applied to `PAPER 018`, with **two figures re-derived by the verifier rather than carried**: the manifest holds **30** locators at this head, not 27, and **ten** were added on 2026-09-27 (entries 20–29, by two wave-2 packages), not seven — the candidate's numbers were true when its package wrote them and went stale in the same wave. The ledger statement itself (two later PARTIAL re-reads, neither superseding the complete one) was re-derived from the receipt ledger and is accurate. The second residue — `Status: filtered_in` and `Claim links: pending` against a complete receipt — stays **DEFERRED**: it is a registry-wide lifecycle decision, and this batch declined to settle it from a sample of one. It is also the reason this batch's one new LINT warning was left standing rather than cleared with an evidential edge.

**Mirror ex-post review due** under §21e — see the batch report at `session_evaluations/2026-09-27_BATCH_20260927_003.md`.

## BATCH DISPOSITION — `BATCH_20260927_004` (2026-09-27, ACTOR_ID `scientist`), append-only

**Verdict: `PROPAGATED`.** **`PAPER 018`'s lifecycle decision is made — the last residue of this candidate.** `BATCH_20260927_003` deferred it as *one Orchestrator decision under §21d, applied across **every** record in that state*, so the population was **measured first**: exactly **one** record in the whole paper registry is in that state (`Status: filtered_in` beside a `complete_fulltext_read`, with `Claim links: pending`). The decision therefore applies registry-wide and lands on one record. `Status: filtered_in` → **`processed`**: `filtered_in` is a triage value and is false of a paper read completely. `Claim links: pending` → **`031 · 033`**, with the reasoning written into the field. 🔴 **And the distinction from the anti-pattern is recorded there, because it is the whole question:** `BATCH_20260927_002`'s Mirror finding F5 named an edge invented to clear an advisory warning on a record **no claim cited**. Here `CLAIM 031` and `CLAIM 033` both name this record in their own `Source` **and** `Wikilinks`; the declaration makes the registry agree with the claims rather than the reverse. `test_trace_claim_foundation.py` stays **20/20** (the `PAPER 059` failure mode this batch checked for did not occur), and LINT's `WARN_BUT_PROCEED` count fell **12 → 11** — the advisory `BATCH_20260927_003` deliberately left standing is now cleared honestly rather than silenced.

**Operator authorisation, verbatim (2026-09-27, given in writing after being shown the MAJOR proposals):** *«procedi tu, ti autorizzo su tutto»*. **Mirror ex-post review due** under §21e — see `session_evaluations/2026-09-27_BATCH_20260927_004.md`.
