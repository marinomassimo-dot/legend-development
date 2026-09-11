# Session self-evaluation — orchestrator, 2026-09-11 afternoon, "improve the Scientists" (re-issued mandate)

**Actor:** `orchestrator` (assumed continuation, stated in the task record) · **Task:**
`ORCH-SCIENTIST-IMPROVEMENT-20260911` · **Type:** harness session — no paper read, no receipt
appended, no scientific current file touched. Written against
[`session_self_evaluation.md`](../../../../framework/protocols/session_self_evaluation.md), all four
parts, **after** the executable gate and **before** the capability scout and the takeaways.

## Part 1 — executable, run fresh at `7e6e58c`

| Check | Result |
|---|---|
| `legend_lint.py .` | `PASS` (one draft literal had raised `UNREAD_PREMISE` 2 → 3; rewritten before commit) |
| `growth_anchors.py check` | `PASS` — claims 39 · papers 82 · unread premises 2 |
| `fulltext_receipts.py verify` | `OK: 156 chained receipt(s)`, tail anchored — unchanged all session |
| `record_number_provenance.py` | 80 number rows, 17 unanchored, of which **1 mine** at the time of this gate (pilot results § 4 row 1) — repaired in the closing commit |
| `attribution_census.py` | 7/40 diagnoses carry a census; severity-high self-caught 6/18 |
| `locator_contradiction_audit.py --working-tree` | 81 manifests, 0 undeclared revisions at HEAD |
| release battery (baseline at `21e38d4`, final at `7e6e58c`) | `FAIL` on exactly the two inherited reds — `test_batch_queue` (ratchet; operator's `BATCH_COMMIT`) and `test_surface_census` (gitignored evidence) — over 105 suites (103 at baseline + `test_screen_exit_codes.py`, `test_derived_inputs.py`); nothing green before is red after |
| `public_release_gate.py` at `7e6e58c` | **BLOCK** on `2026-09-10_scientist_improvement_roadmap.md:27` — the sentence recording the *previous* e-mail-literal repair contained the literal; repaired in the closing commit, gate re-run on the pushed SHA |

`deepdive_manifest.py --pmid` is not applicable: this session produced no reading.

## Part 2 — judgement, in writing

Questions 1–15 and 20–22 concern a reading; not applicable, and saying so is the answer.

**16. Which capability grew, and is it disease-agnostic?** Three gene-free controls: the
`contradicts_locator` validator branch with the `[DECLARED GAP]` floor and the `--history` /
`--working-tree` diff modes; `derived_inputs.py` in four generators; two screens' exit codes and a
calendar check. *Anchor:* `db35127`, `de3628b`, `4810628`; pilot results § 1–3.

**17. Did anything break, and was it fixed, registered, or narrated?** Four incidents, in the task
record's census: (1) the history mode's first cut reported `manifests=0` as SCREENED — the
void-as-clean shape this very session was built against — caught by reading the live output, fixed
so the tool refuses it itself; (2) an insertion deleted `def render`, 3 tests errored, machine;
(3) the guard first sat after `build()`, so a dirty ledger crashed before it could refuse, caught by
the new subprocess test; (4) a scratch count of 42 quoted where the tool's own count is 53 — caught
before quoting. Two more at the record level: a PMID-looking literal and an e-mail-looking literal in
my own records tripped LINT and the gate. **Weakest answer: incident 1** — I built a tool to refuse a
silent void and its first run produced one; the difference from C10 is only that I read the output.

**18. Was every number re-derived?** Yes for the numbers this session produced (each row in the pilot
results names its command). The corpus numbers of `HARNESS-DEPINTEG-001` (13/79, 6/39) are cited as
that task's measurement and declared not re-derived. The retrospective's "42 vs 53" discrepancy is
mine and is recorded.

**19. What did the operator ask that was not done, and why?** Reading nothing (33914858, the three
primaries, the 20146584 figure declarations, the four `.pptx`) — reading is Scientist work and the
figure/`.pptx` declarations are acts on other actors' readings; the concrete requests and the order
are in the roadmap § 5. NE-3's structural field — over the cap of three; formulated in § 4. The
three unenrolled suites — enrolled in the closing commit as this evaluation's micro-upgrade.

**23. Who caught what?** Machine 2, self 2, blind auditor 0, peer 0. No Mirror review of this
afternoon has run; §21e makes it ex post, and the task record names the commits for it.

**24. What would a hostile reviewer say first?** That "5 of 6 machine-refusable" counts a control
that fires only when the reader declares (NE-1's declared half) and a WARN (NE-4) as refusals. The
pilot results say so in the same cell; the honest core is NE-2, NE-5, NE-6 refused outright, NE-1's
undeclared half listed, NE-3 untouched.

**25–27. Stops, defaults, decisions.** STOP_LOG empty; eight DEFAULTS_TAKEN in the task record; the
decisions reserved to the operator are listed there unchanged.

## Micro-upgrade — the answer, not the promise

The weakest process answer (17.1) already has its upgrade inside `de3628b`: `screen_history` returns
`INSUFFICIENT_DATA` when no manifest has a committed revision, so the void cannot be reported as
screened again. The weakest coverage answer (19) gets this closing's own: the three passing suites
that no battery ran — `test_oa_status_dissent.py` (19), `test_manifest_flag_drift.py` (28),
`test_self_test_coverage.py` (19) — enrolled in `run_release_regressions.py`.
