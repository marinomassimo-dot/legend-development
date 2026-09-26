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
