# CC-20260928-WM-HISTORY-SPLIT-01 — the working model's history leaves its hot surface

- **Status:** committed — `BATCH_20260928_004` (structural, MANUAL)
- **Author:** Harness Engineering (`plan`), under the operator's decision of 2026-09-28 (*Decision A — Working Model: proceed with Option A*), given in the queue mandate of that day.
- **Target files:** `disease-models/wwox/registries/working_model_current.md` (record-scoped, 7 ops) · new `disease-models/wwox/registries/working_model_history.md` (verbatim move)
- **Change class:** structural, **no disease-model change**: `working_model_version` stays `WM_v7.3`. Six live qualifications that lived only in history-shaped text are restated, in their own words, where they apply.
- **context_policy:** SYNTHESIS — LEGEND's own records classified against LEGEND's own records; no paper was read and no claim was written.

## Why

The working model was 109,924 B, ≈68 % history-shaped (per-batch `Last update` notes 23.9 KB, `## Changelog` 39.8 KB, three MAJOR-batch sections 11.5 KB), and every scientific route loads it whole. Both of G1's revival triggers had fired ([`g1_i4_residual_decisions_20260926.md`](../../../../governance/design_records/g1_i4_residual_decisions_20260926.md) § A5; [`harness_cost_20260928.md`](../../../../governance/design_records/harness_cost_20260928.md) § 9). G1 refused the split because some live qualifications existed only in that history; the operator's Option A is *live truth first, then cold history*.

## Method — producer ≠ verifier

1. The history-shaped regions (lines 7–22, 250–359 at `a923e10`) were cut into **99 units** deterministically: 16 `Last update` lines, 38 changelog rows (header and rule included), 45 paragraphs/bullets of the three MAJOR sections.
2. Two agents classified every unit **independently and blind to each other**, under one brief: **A** live and already represented, **B** live only in history, **C** pure history, **D** ambiguous. "Represented" meant the working model's live sections or the claim record the statement qualifies (every route that loads the working model loads the claim registry whole). Every `represented_at` quote was machine-checked verbatim by each reviewer.
3. Producer: A 66 · B 6 · C 27 · D 0. Verifier (told to be adversarial toward "history is dead"): A 68 · B 10 · C 21 · D 0. The two never disagreed across A/C versus B in a way that lost content: pairs were A/A 61, A/B 5, B/B 5, B/A 1, C/C 21, C/A 6.
4. **Rule applied: the union of the two B sets is B.** Of its 11 units, four (H003, H019, H028, H035) carry **paper-level measurement caveats that live in the paper registry or the literature log** — canonical current files, read with the paper whenever it is in play. They are not lost by moving the working model's history and were not duplicated into it. The other seven collapse to **six promotions** (table below).
5. A third agent, which wrote none of it, verified each promotion for strength, scope, additions and placement. It found three to fix; two were fixed as proposed in substance, and one (H061) is recorded below as an open scientific question rather than decided here.

## The six promotions

| Unit(s) | Live qualification (own words) | Now in |
|---|---|---|
| H059, H060 (+H020) | the NMD premise that closed the splice axis is withdrawn; `PAPER 044`'s NMD sentence is the abstract's and a legend's inference, the body's own disjunction stands | Worked example B |
| H061 | Wang 2012 blots and densitometers total GSK3β; the **stated invariance** is `NOT_ASSERTED`, not `MEASURE_ABSENT` | Mechanistic architecture — SDR-domain function, as a labelled qualification of the parenthesis it bears on |
| H066 (+H020) | `TX-007` `SAFETY 1`: a measured efficacy floor with no measured ceiling, no tumour surveillance | Gene therapy context |
| H072 | no drug recommended, no dose transferred; the carbenoxolone withdrawal does not promote memantine; d-APV never given to a human | Network hyperexcitability |
| H097 | an SDR stabilizer is `conditional / not design-ready` | Worked example A |

**Verifier fixes applied.** H072's label names the batch-wide guarantee (*Unchanged in `BATCH_20260927_004`, and binding here*) instead of narrowing it to one withdrawal. H060's "both alleles" is pinned to the ledger entry it describes, and says the worked examples stay carried independently (the verifier's own wording, "compound-heterozygous genotype class", was not used: it is the pairing vocabulary the privacy gate exists to catch beside the worked examples).

**Open, not decided here (H061).** The SDR paragraph's parenthesis says *GSK3β abundance and phospho-S9 unchanged*; `CLAIM 035` backs the S9 invariance and says nothing about total abundance, and `BATCH_20260927_004` recorded that the source does not *state* total-GSK3β invariance. The verifier proposed deleting "GSK3β abundance and". That would narrow a live statement on a judgement about what the blot shows, which a structural batch does not make. The qualification is placed immediately after the parenthesis and labelled as qualifying it, so the tension is visible to every reader; whether the parenthesis should be narrowed is referred to the Scientist.

## Verification (deterministic)

`migration_check.py` (session scratch, reproduced in the batch report): every one of the 99 units is present **verbatim** in `working_model_history.md`; all **389** `represented_at` quotes of both reviewers still stand in the new live working model or the claim registry; all **17** promoted key phrases are in the live sections; the live region changed **only by insertions** (1,689 chars) plus the one-line `Last update` pointer. `batch_commit.py propagate` applied the seven operations atomically and proved every byte outside them unchanged.

## Migration map — every unit

Final: A 71 (4 of them paper-level) · B → promoted 7 · C 21.

| Unit | Kind | Lines at `a923e10` | Producer | Verifier | Final | Live destination |
|---|---|---|---|---|---|---|
| H001 | last update | 7–7 | A | A | A | — |
| H002 | last update | 8–8 | A | A | A | — |
| H003 | last update | 9–9 | A | B | A (paper level) | the paper / literature-log record that already carries it (canonical current file) |
| H004 | last update | 10–10 | A | A | A | — |
| H005 | last update | 11–11 | A | A | A | — |
| H006 | last update | 12–12 | A | A | A | — |
| H007 | last update | 13–13 | A | A | A | — |
| H008 | last update | 14–14 | A | A | A | — |
| H009 | last update | 15–15 | A | A | A | — |
| H010 | last update | 16–16 | A | A | A | — |
| H011 | last update | 17–17 | A | A | A | — |
| H012 | last update | 18–18 | A | A | A | — |
| H013 | last update | 19–19 | A | A | A | — |
| H014 | last update | 20–20 | A | A | A | — |
| H015 | last update | 21–21 | A | A | A | — |
| H016 | last update | 22–22 | A | A | A | — |
| H017 | changelog row | 254–254 | A | A | A | — |
| H018 | changelog row | 255–255 | A | A | A | — |
| H019 | changelog row | 256–256 | A | B | A (paper level) | the paper / literature-log record that already carries it (canonical current file) |
| H020 | changelog row | 257–257 | A | B | B → promoted | Worked example B · Gene therapy context (twin of H059/H060/H066) |
| H021 | changelog row | 258–258 | A | A | A | — |
| H022 | changelog row | 259–259 | A | A | A | — |
| H023 | changelog row | 260–260 | A | A | A | — |
| H024 | changelog row | 261–261 | A | A | A | — |
| H025 | changelog row | 262–262 | A | A | A | — |
| H026 | changelog row | 263–263 | A | A | A | — |
| H027 | changelog row | 264–264 | A | A | A | — |
| H028 | changelog row | 265–265 | A | B | A (paper level) | the paper / literature-log record that already carries it (canonical current file) |
| H029 | changelog row | 266–266 | A | A | A | — |
| H030 | changelog row | 267–267 | A | A | A | — |
| H031 | changelog row | 268–268 | A | A | A | — |
| H032 | changelog row | 269–269 | A | A | A | — |
| H033 | changelog row | 270–270 | C | C | C | — |
| H034 | changelog row | 271–271 | A | A | A | — |
| H035 | changelog row | 272–272 | A | B | A (paper level) | the paper / literature-log record that already carries it (canonical current file) |
| H036 | changelog row | 273–273 | A | A | A | — |
| H037 | changelog row | 274–274 | A | A | A | — |
| H038 | changelog row | 275–275 | C | C | C | — |
| H039 | changelog row | 276–276 | C | C | C | — |
| H040 | changelog row | 277–277 | A | A | A | — |
| H041 | changelog row | 278–278 | A | A | A | — |
| H042 | changelog row | 279–279 | C | C | C | — |
| H043 | changelog row | 280–280 | C | C | C | — |
| H044 | changelog row | 281–281 | C | C | C | — |
| H045 | changelog row | 282–282 | A | A | A | — |
| H046 | changelog row | 283–283 | C | C | C | — |
| H047 | changelog row | 284–284 | C | C | C | — |
| H048 | changelog row | 285–285 | A | A | A | — |
| H049 | changelog row | 286–286 | C | A | A | — |
| H050 | changelog row | 287–287 | A | A | A | — |
| H051 | changelog row | 288–288 | C | A | A | — |
| H052 | changelog row | 289–289 | A | A | A | — |
| H053 | changelog row | 290–290 | C | C | C | — |
| H054 | changelog row | 291–291 | C | C | C | — |
| H055 | batch section block | 297–297 | C | A | A | — |
| H056 | batch section block | 299–299 | C | C | C | — |
| H057 | batch section block | 300–300 | A | A | A | — |
| H058 | batch section block | 301–301 | A | A | A | — |
| H059 | batch section block | 302–302 | B | B | B → promoted | Worked example B |
| H060 | batch section block | 303–303 | B | B | B → promoted | Worked example B |
| H061 | batch section block | 304–304 | B | B | B → promoted | Mechanistic architecture — SDR-domain function (qualification of the parenthesis) |
| H062 | batch section block | 306–306 | C | C | C | — |
| H063 | batch section block | 307–307 | A | A | A | — |
| H064 | batch section block | 308–308 | A | A | A | — |
| H065 | batch section block | 309–309 | A | A | A | — |
| H066 | batch section block | 310–310 | B | B | B → promoted | Gene therapy context |
| H067 | batch section block | 312–312 | C | C | C | — |
| H068 | batch section block | 313–313 | A | A | A | — |
| H069 | batch section block | 314–314 | A | A | A | — |
| H070 | batch section block | 315–315 | A | A | A | — |
| H071 | batch section block | 316–316 | C | C | C | — |
| H072 | batch section block | 317–317 | B | B | B → promoted | Network hyperexcitability |
| H073 | batch section block | 318–318 | C | A | A | — |
| H074 | batch section block | 320–320 | C | A | A | — |
| H075 | batch section block | 322–322 | C | C | C | — |
| H076 | batch section block | 326–326 | A | A | A | — |
| H077 | batch section block | 328–328 | C | C | C | — |
| H078 | batch section block | 329–329 | A | A | A | — |
| H079 | batch section block | 330–330 | A | A | A | — |
| H080 | batch section block | 331–331 | A | A | A | — |
| H081 | batch section block | 332–332 | A | A | A | — |
| H082 | batch section block | 333–333 | A | A | A | — |
| H083 | batch section block | 334–334 | A | A | A | — |
| H084 | batch section block | 336–336 | C | C | C | — |
| H085 | batch section block | 337–337 | A | A | A | — |
| H086 | batch section block | 338–338 | A | A | A | — |
| H087 | batch section block | 339–339 | A | A | A | — |
| H088 | batch section block | 340–340 | A | A | A | — |
| H089 | batch section block | 342–342 | C | C | C | — |
| H090 | batch section block | 344–344 | C | C | C | — |
| H091 | batch section block | 348–348 | A | A | A | — |
| H092 | batch section block | 350–350 | C | C | C | — |
| H093 | batch section block | 351–351 | A | A | A | — |
| H094 | batch section block | 352–352 | A | A | A | — |
| H095 | batch section block | 353–353 | A | A | A | — |
| H096 | batch section block | 354–354 | A | A | A | — |
| H097 | batch section block | 355–355 | B | A | B → promoted | Worked example A |
| H098 | batch section block | 357–357 | C | A | A | — |
| H099 | batch section block | 359–359 | C | C | C | — |

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED

- **Batch:** `BATCH_20260928_004` (structural, MANUAL, 2026-09-28) · **WM version:** `WM_v7.3`, unchanged
- **Landed:** `c5eb296` (propagation, 7 record-scoped ops) · `001b1ea` (Phase 4.7 pathograph) · `0bfe4c2` (batch report) · published at `1e130f0`
- **Propagated in full**, with one item deliberately left open rather than decided by a structural
  batch: **H061** — the SDR parenthesis *«GSK3β abundance and phospho-S9 unchanged»* beside the
  `NOT_ASSERTED` total-GSK3β qualification. The ex-post review then established that `CLAIM 035`
  asserts only *«fosfo-GSK3β-S9 invariata»*, so aligning the parenthesis with its own cited claim is
  mechanical rather than scientific; the repair is carried by a later batch, with the review's
  falsifier attached (if Wang 2012 Fig. 1 shows total invariance, `CLAIM 035` is the under-scoped
  record instead).
- **Ex-post Mirror review (2026-09-28): CONFIRMED**, three MINOR and two NOTEs, no BLOCKING finding.
  The four self-nominated weak points all survived; `1e130f0^` was reconstructed and diffed against
  hot + cold by two independent routes — 0 lines lost, insertions only, 1,689 chars across 5 sites —
  and `git revert -m 1 1e130f0` restores the pre-split file byte for byte.
- **Findings routed to Harness Engineering and closed with this disposition:** `A11` (this block was
  missing, so a fully propagated candidate still counted in the backlog), `A14` and `X2` (the class-A
  routing premise and the enumeration limit, recorded in
  [`wm_history_split_20260928/README.md`](../wm_history_split_20260928/README.md)), `X1`
  (`roles/mirror.md`'s stale push clause).
