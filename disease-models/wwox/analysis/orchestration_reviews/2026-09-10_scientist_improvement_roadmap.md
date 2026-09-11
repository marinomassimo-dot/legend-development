# Scientist improvement roadmap — from the Aqeilan sweep's near-errors to verified controls

**Written:** 2026-09-11 · **By:** `orchestrator`, task `ORCH-SCIENTIST-IMPROVEMENT-20260911`
(continuation of [`ORCH-SCIENTIST-IMPROVEMENT-20260910`](../../../../ledger/tasks/orchestrator/ORCH-SCIENTIST-IMPROVEMENT-20260910.json), closed 2026-09-11 morning) ·
**Mandate:** turn the errors, near-errors and difficulties observed in the 2026-09-09 Aqeilan sweep
into verifiable improvements of how the Scientists work — incident → cause → control → test case →
measured result → residual limit — using the censused repositories only where a pattern solves a
documented problem.

**This file is the authoritative index for the decisions it lists.** The per-incident matrix is
[`data/2026-09-10_scientist_incident_controls.jsonl`](data/2026-09-10_scientist_incident_controls.jsonl);
the pattern comparison is [`governance/candidates/2026-09-10_scientist_pattern_selection.md`](../../../../governance/candidates/2026-09-10_scientist_pattern_selection.md);
the pilot measurements are [`2026-09-10_scientist_pilot_results.md`](2026-09-10_scientist_pilot_results.md).
Other documents link here; nothing is decided twice.

---

## 0 · State found on arrival (reconciliation before any edit)

| Checked | Found |
|---|---|
| user / directory / branch | `desktop` · `/home/desktop/legend-development` · `main`, clean tree, no worktrees |
| HEAD at start | `21e38d4` — 51 commits after the handover's `3973ada`; every file the handover listed as modified or untracked had landed (`HARNESS-DEPINTEG-001`, `HARNESS-VALIDATOR-001`, `HARNESS-ACQREC-001`, `HARNESS-SELFTEST-001`, `HARNESS-HANDOFF-001`, Mirror `REV-EXPOST-20260911-001`, all `COMPLETE`) |
| identity | the previous orchestrator task carries the same objective; this session continues it as `orchestrator` — assumed, not inferred from the directory, and named as an assumption in the task record |
| live actors / owners | no open task in `ledger/tasks/*` besides Mirror's queued follow-ups (`MF-1…8`); no peer session; nothing of another actor's in flight |
| remotes | `origin` and `development` → the same URL; push rule §21d applies |
| publication gate | **BLOCK** at `HARNESS-ACQREC-001.json:215` on the literal `someone@example.org` inside a sentence describing a test fixture — repaired (`0c90fbe`) |
| release battery baseline | `FAIL` on exactly the two declared reds (`test_batch_queue` ratchet, `test_surface_census` gitignored evidence) |

Already completed before this session (verified in code, not from reports): P1, P2, P3, H2, §9.1–9.8
of the retrospective, the 14 tools of 2026-09-10, brief v2, the four learned gates, the bwrap
recommendation. Still open at arrival: Mirror's MF-1…MF-8; the four receipt-schema decisions
(operator's); the `BATCH_COMMIT` that clears the ratchet (operator's); NE-3's structural gap; the
scientific reading debt.

## 1 · The six near-errors, verified at the source

One row each in the JSONL. Summary of what each verification changed against the retrospective's
wording:

| ID | Case | Verified at | Caught by | Control before | Control now | Status (six-state scale) |
|---|---|---|---|---|---|---|
| NE-1 | False correction of a correct locator (29724996 Fig 6A, entries[21]) | `SLR-scientist-b-0002.md`, receipt `FTR-20260909-29724996-01` | self | none mechanical; R4 did not fire | validator knows `contradicts_locator`; unaudited declaration blocks a complete read; `--history`/`--working-tree` list undeclared rewrites | integrated + collaudato; adopted when the next wave runs M3 |
| NE-2 | Green screen over an unscreened filename (16223882) | wave-3 evaluation; `test_suspect_surface_call_shape.py` | self | write-time defence in depth only | call-shape guard; digests 7/7; exit codes 7/7 (MF-6 today) | integrated + collaudato + adopted (write-time) |
| NE-3 | Cross-panel bridge across cell lines (15070730 Fig 6 → Fig 5) | wave-3 evaluation, PMID15070730.json audit | blind auditor | R4 audit (worked) | unchanged structurally | **proposto** — § 4 |
| NE-4 | PMID from a search while in the artefact (31428585, 29581896 vs 29310447) | manifest audit_note, `ef02e94`, `FTR-20260909-31428585-02` | both auditors | none | provenance WARN + declaration; calendar check (MF-5 today) | integrated + collaudato + adopted |
| NE-5 | REFUSED accepted without its reason (25245215) | `1e12c82`, SLR-scientist-b-0006 | coordinator | refusal for the wrong reason | signature named; positive and negative fixtures | integrated + collaudato + adopted |
| NE-6 | Derived surfaces over peers' uncommitted work | `a8a6a1d` | self (reverted) | none | `derived_inputs.py` refuses; phase 4.7 states its reason | integrated + collaudato + adopted |

Machine-caught before: **0 of 6**. Machine-refusable now, on the same inputs: **NE-1 (declared
half), NE-2, NE-4 (as WARN), NE-5, NE-6 — 5 of 6**, each demonstrated on the incident's own fixture or
on the live checkout (§ 3 of the pilot results). NE-3 remains the blind audit's. The denominator is
still the six errors that *surfaced*; nothing here measures the invisible ones.

## 2 · Improvements already realised — status verified, not restated

| Improvement | Verified how | Status |
|---|---|---|
| identifier / count provenance (§ 9.4) | `provenance_warnings` in the validator; 19 undeclared historical | integrated · collaudato · adopted (WARN at M3) |
| bytes screened named by every screen (§ 9.2) | `screen_verdict.py`; 7/7 records; exit codes now 7/7 (`db35127`) | integrated · collaudato · adopted |
| `text_surface_intrusion_check` | wired for PDF-derived `article_text`; 17 tests incl. the motivating artefact | adopted |
| `oa_status_dissent` | exists with tests; **not enrolled in the battery, not called by the validator or `session_self_eval`** — used when the reader runs it | implementato localmente · collaudato (24510053) · not adopted mechanically |
| `manifest_flag_drift` | exists with tests; same enrolment gap | same |
| `erratum_scope_check` | exit code repaired today; **no separate test file** — self-test only, now pinned through `test_screen_exit_codes.py` | integrated · collaudato |
| `genre_discriminator` | same as above | integrated · collaudato |
| queue-ID ↔ PMID cross-check (§ 9.5a) | validator BLOCK; B7 draft as fixture; `manifest_queue_id_crosscheck.py` baseline in `HARNESS-VALIDATOR-001.json` MEASUREMENTS: 0 unresolved / 0 foreign over 81 manifests | adopted |
| self-tests exercise their tools (§ 9.3) | `self_test_coverage.py`; both-false 10 → 0 (`83edd70`) | collaudato; **not enrolled** in the battery |
| first contact after `legacy_reconstruction` (H2) | `fulltext_receipts.py verify` after the H2 fix: 94 of 94 receipts pass (`2026-09-10.md` § 1); the stricter rule measured there at 0 live violations and left as a separate decision | adopted (legacy case) |
| `HARNESS-VALIDATOR-001` / `HARNESS-DEPINTEG-001` | code, pins, tests and task JSON read; corpus numbers taken as the task's own measurement in `2026-09-10_dependency_integrity_screen.md` (`dependency_integrity.py`: 13 of 79 screenable papers flagged, 6 of 39 claims on a flagged chain), **not re-derived here** | COMPLETE, landed |

The enrolment gaps (three test files outside the battery) are named here and not closed today: the
cap was three interventions and the battery's runtime is already ~8 min; enrolling them is a one-line
change each for the next harness session.

## 3 · The three interventions (order of preference applied to the data)

1. **Complete and wire the existing controls** → MF-6 + MF-5 (`db35127`). Two screens, one date check.
2. **Protect high-risk corrections** → MF-3a + MF-3b (`de3628b`). The NE-1 shape gets its gate and its
   diff.
3. **Close a concrete reproducibility gap** → NE-6 (`4810628`). Derived surfaces bind to committed
   inputs.

Each: problem and desired behaviour, historical case, previous behaviour recorded, minimal change,
one wrong and one right case, missing/empty/unexaminable input, the entry point the Scientists use,
regressions, what the control cannot establish — in the pilot results file, with the mutation matrix
per commit message.

## 4 · Gaps that remain, with the concrete next step for each

| Gap | Why still open | Concrete step |
|---|---|---|
| **NE-3 structural** | no field carries the experimental system on either side of a relation | Add optional `experimental_context: {system, cell_line, genotype, treatment, timepoint, comparator, endpoint}` to coupled-relation entries; validator **WARN** when a bridge joins two entries whose declared `system`/`cell_line` differ; grandfathered set in `growth_anchors.py`; fixture = 15070730 Fig 6/Fig 5. WARN not BLOCK: history, and a declared discordance can be the finding. Estimated 3 h. |
| **MF-4** dependency block binding | design line owned by the validator | as queued: `references_declared == multihop.references_enumerated` and `reference_source` naming this PMID |
| **MF-1 / MF-2** write guard at the kernel | bwrap measured; not wired | as queued |
| **MF-7** | operator's own session | as queued |
| **MF-8** four `.pptx` declarations | a reading act | next scientist wave |
| The 53 cross-date undeclared locator revisions in history | a review queue, not 53 defects | the next wave reads its own paper's entries from `--history --json`; a revision that was a contradiction gets a retroactive `contradicts_locator` + audit, one that was re-anchoring gets nothing |
| Three test files not in the battery | one line each | next harness session |

## 5 · Scientific queue (acquisitions and reading debt)

### 5.1 · PMID 33914858 (Repudi 2021, *Brain*) — **still absent; needs the operator's browser**

Replay verdict on this host (2026-09-10): `FAILED_HTTP_403_CLOUDFLARE` on the resolved bronze-OA
route `https://academic.oup.com/brain/advance-article-pdf/doi/10.1093/brain/awab174/40854472/awab174.pdf`
(OpenAlex `best_oa_location`, key-less). The 19-tier cascade was exhausted on 2026-09-09; repeating
it is not proposed. **Concrete request:**

1. Open `https://doi.org/10.1093/brain/awab174` in the browser, download the article PDF.
2. Save it as `/home/desktop/legend-development/files/fulltext/PMID33914858_Aqeilan2021.pdf`.
   Expected digest of the copy the queue declares: `960569a9c0d4e7634a53e3b829fc29145767f9df0ce620cf827b891c6708d559`
   — if it differs, that is a fact to record (a later publisher version), not a failure.
3. Download the supplementary data from the same page into
   `/home/desktop/legend-development/files/supplement/PMID33914858/`.
4. Then a Scientist runs M1–M5: identity and digest, figures at native resolution, supplements,
   receipt and locators, impact on CLAIM 003 (*consolidated baseline*, so R4 applies).

Downloading is not reading; nothing in the record changes until the receipt exists.

### 5.2 · PMID 20146584 — the two figures are on disk and are real

`files/figures/PMID20146584/nihms-180622-f0001.jpg` (600×365) and `…f0002.jpg` (601×481) were
recovered on 2026-09-11 06:10 by `reacquire.py` from the CDN routes the article HTML names; both
opened in this session and are the Future Oncology 2010 figures (organ map; interactome schematic),
not challenge pages. The manifest still declares neither: declaring them and reading them is a
reading act for a Scientist, and the receipt stays `partial` until then. Not promoted on captions.

### 5.3 · Three unread primaries — ordered by scientific dependency

| Order | PMID | Why this position | Current state |
|---|---|---|---|
| 1 | **29808465** Johannsen 2018 (Q230P, SDR domain) | bears **CLAIM 030** (*in observation*, VERY HIGH, T1) directly and 47 citations in 7 canonical files; a claim-bearing primary read from a restatement is the compression § 7.3 measured | receipt `FTR-20260810-29808465-01` **`abstract_only`** — clears no debt; closed as unrecoverable by open routes (Springer, subscription); needs institutional access or an author copy |
| 2 | **25411445** Mignot 2015 (phenotypic spectrum; P47R survival) | defines the spectrum every later genotype-phenotype sentence cites, including the P47T/P47R contrast in CLAIM 030 — read before re-weighing CLAIM 030's evidence line | no receipt; `pmcid null`, `unrecoverable_by_these_routes` (FT-057) |
| 3 | **15126504** Sze 2004 (WWOX knockdown → Tau phosphorylation) | named as the revival trigger of dismissal **D-14** (*a figure shows what its legend says*, Wang 2012's absent Tau blot); independent of the two above | no receipt; `absent` (FT-024) |

Order rationale: 1 and 2 share one claim and one evidence line, so they are read as a pair with
29808465 first because it carries the claim's DATO; 3 touches a different ledger.

## 6 · Schema decisions — formulated, not taken

The two proposals the operator reserved are already concrete in
[`framework/protocols/proposals/2026-09-09_receipt_schema_proposals.md`](../../../../framework/protocols/proposals/2026-09-09_receipt_schema_proposals.md):
§ 1 study-level rollup (`study_coverage_rollup`, `coverage_provenance`, parent-depth floor,
fall-with-parents rule; adverse case 4: a rollup whose parents are `abstract_only` is refused however
clean its map — the operator's mandatory adverse case is covered) and § 2 coupled relations on
adjudicated locators (`adjudicated_surface` beside `surface`; 25331887 and 34268881 measured; 0
records change). Both carry before/after semantics, admitted and refused examples, impact on existing
and future attestations, migration, adverse tests and the required authority. **Nothing was
implemented**, per the mandate; the four yes/no questions (§4.1, §4.1b, §4.3, §4.3b) stand as
written there. `identity_correction`: no regression found — `reading_state.py` and
`coverage_report.py` both subtract corrected events, suites green.

## 7 · Scientific limits kept explicit

- A citation edge is not an experimental dependency; shared co-authors do not invalidate; a
  correction, an expression of concern and a retraction are three different facts. The dependency
  screen produces **reading priority** (13 papers, 6 claims), never a verdict.
- The absence of a rescue design in this lot bounds what the lot licenses; it does not show
  inefficacy (retrospective § 8.3 wording kept).
- The 53 historical undeclared locator revisions are *changes*, not contradictions, until read.

## 8 · Integration and publication

Commits on `main`: `db35127`, `de3628b`, `4810628`, `0c90fbe`, plus this record's commit. Battery,
gate and push results are in the pilot results file § 5 and the task record.
