# Session self-evaluation — orchestrator, 2026-09-10 → 11, "improve the Scientists"

**Actor:** `orchestrator` · **Session:** `legend-development-2e`, resumed on the desktop VPS ·
**Mandate:** restart from the problems the Aqeilan sweep exposed and improve the Scientists,
using the saved census · **Type:** harness session — no paper was read, no receipt appended, no
scientific current file touched. Written against
[`session_self_evaluation.md`](../../../../framework/protocols/session_self_evaluation.md), all
four parts, **after** the executable gate and **before** the capability scout and the takeaways.

## Part 1 — executable, run fresh at `72e96b6`

| Check | Result |
|---|---|
| `session_self_eval.py` | `PASS` — every complete read has landed and every declared output resolves. Visible debts, all pre-existing: `[UNREAD PREMISE]` ×2 (baseline 2, ratchet holds), `[DECLARED GAP]` on the legacy manifests 22193544 / 32000863 / 34214506 / 35716775, `[RATCHET]` `retraction_check.dependencies` absent on 69, `acquisition_recipe` absent on 66 — both new today, both non-blocking by design |
| `fulltext_receipts.py verify` | `OK: 156 chained receipt(s)`, tail anchored — unchanged all session |
| `legend_lint.py .` | `PASS` |
| `growth_anchors.py check` | `PASS` — claims 39 · papers 82 · unread premises 2 |
| release battery under the lock (`06:33`, and Mirror's copy) | `FAIL` on exactly `test_batch_queue` (ratchet; operator's `BATCH_COMMIT`) and `test_surface_census` (gitignored evidence); nothing green before the session is red after it |
| `attribution_census.py` | 6/39 diagnoses carry a census; severity-high self-caught **5/12**; 8/12 waves carry the two §21c keys |

`deepdive_manifest.py --pmid` is not applicable: this session produced no reading.

## Part 2 — judgement, in writing

Questions 1–15 and 20–22 concern a reading; this session read nothing and claims nothing about
any paper. They are **not applicable, and saying so is the answer** — a harness session that
answered them would be grading a reading that did not happen.

**16. Which capability grew, and is the growth disease-agnostic?** Every tool landed today is
gene-free: `screen_verdict.py`, `self_test_coverage.py`, `attribution_census.py`,
`lot_internal_edges.py`, `locator_contradiction_audit.py`, `dependency_integrity.py`,
`reacquire.py`, the runner guard, the wrapper. The one disease-scoped output is the dependency
screen's *result* — 13 of 79 WWOX papers, 6 of 39 claims — and the tool that produced it would run
unchanged on another model. *Anchor:* `2026-09-10.md` § 1, § 2b–2i.

**17. Did anything break, and was it fixed, registered, or merely narrated?** Broke: my first
receipt-writer fix (7 tests red; narrowed and fixed); my census parser (blind to the shape three
actors used; fixed at the instrument); a heredoc that let the shell eat a filename (rewritten
before commit); the standing brief v2 failing the locator-obligation suite (fixed); 54 dossiers
overwritten by a stream's mutation harness (restored from `HEAD`, guarded at two layers,
attributed by its author). Registered, not narrated: two findings, four learned gates, one
follow-up task file. *Anchor:* `FINDING-20260911-DOSSIER-TRUNCATION.md`, `learned_gates_registry.md`.

**18. If a check caught me, did I strengthen the check or just satisfy it?** Mirror caught four
defects in my tools; each repair carries the reviewer's fixture as a test and a mutation back to
the defect that turns it red (`72e96b6`). The obligation suite caught the brief; the brief was
made to name the manifest field, not the test relaxed. *Bad answer avoided:* renumbering.

**19. Where ranking and judgement diverged, did I record the divergence?** Three times the
specification was measured and not followed: the prose grep (261/1458), the citation-only edge
detector (3 of 4), the "13 on 20530675" attribution. Each divergence is in the commit and in the
record with the number that decided it.

**23. Which skill, gate or pattern was used, and which declined with a reason?** Used:
`legend-locator-audit` as the object of § 9.1; the Mirror ex-post review (§21e); the Agent
dispatch pattern with exclusive file ownership; `SPECIFICATION_NUMBER_PROVENANCE_GATE` — landed
today and then applied against this session's own record twice. Declined: `legend-deepdive`,
`legend-discovery`, `legend-hypothesis-forge` — no reading was in scope, and the operator had
halted a reading sweep over cost; `legend-paperqa` — external spend, reserved. `legend-commit` —
`BATCH_COMMIT` is the operator's and the paper-registry ratchet (`test_batch_queue`) waits on it.

**24. Where did each output land?** `framework/scripts/` (13 tools + suites), `framework/protocols/`
(brief v2, self-eval Parts 3–4, reading modes, receipt rule), `governance/` (Annex A.1b,
`INTERNAL_EDGES`, Annex C.1 row, follow-up tasks), `roles/orchestrator.md`, `.claude/skills/`
(locator-audit trigger, scout preflight), `learning/` (two findings, five censuses),
`reviews/mirror/`, `ledger/tasks/plan/` ×6, and this record. Nothing in the four current files.

**25. Can the next run answer, mechanically, what was done?** Yes for the tools — each has a
`--self-test` or a suite that drives its entry point on a real artefact, and the meta-test reports
both axes at 0 both-false. For the session: `2026-09-10.md` § 1–2i and the commit messages carry
every number with the command that produced it — **except one, the 9.3 baseline, which Mirror found
derivable from no run and which is struck.**

**26. What friction occurred, and did the system catch it before overclaim?** Five rate-limit
kills across two nights; two streams resumed twice by hand from their transcripts, nothing
re-done. The dossier overwrite: caught by `git status` after the fact, restored, and the class
closed only by the incident's author building the refusal layer — **the runner guard I built could
never have seen it**, which Mirror said and the record now says. The record's own "class closed"
was an overclaim, caught by the blind reviewer.

**27. What capability delta helps on a different gene, and what makes it persist?** The two
that matter most: a screen cannot say `CLEAN` without naming what it screened (unrepresentable, not
discouraged), and a self-test must drive its own entry point on a real artefact — *read, never
write*. Both are executable and enrolled. The measurement that should outlive this session:
**on the severity-high incidents of this session, the self-caught share was 1 of 6.** Blind
auditor 3, peer 2, machine 0. The retrospective's § 5.2 pattern, reproduced on the orchestrator.

## Micro-upgrade — from the weakest answer

The weakest answer is 25: twice in one session an operator-facing number was quoted into a
record instead of derived — the 13-on-20530675 attribution into a dispatch, the 26/46 baseline into
this record — and both were caught by someone else. The gate exists since this afternoon; it had
no instrument. **Shipped alongside this diagnosis:** `framework/scripts/record_number_provenance.py`
— over `orchestration_reviews/*.md`, every table row carrying a ratio or an arrow (`17/1458`,
`13 → 10`, `26/46`) must also carry a command in backticks, a commit hash or a tool name; rows that
do not are listed as `UNANCHORED_NUMBER`, a review queue, never a block. Its first run is its
baseline, printed in the commit.

## Part 3 — attribution census

Counting rule per Part 3. Incidents are this actor's own — made by the orchestrator, or made by a
stream and caught by the orchestrator — thirteen in all.

| # | Incident | Caught by | High? |
|---|---|---|---|
| 1 | First `first_read` fix too strict, 7 tests red | machine | |
| 2 | Census parser blind to single-wave contracts — invisible compliance | self, via the record | 🔴 |
| 3 | Heredoc backtick expansion ate a filename from three files | self | |
| 4 | Dispatch quoted the retrospective's wrong paper attribution into a task | peer (two streams measured) | 🔴 |
| 5 | Incident finding's "class closed" and its mechanism wrong | peer (stream self-attributed) | 🔴 |
| 6 | Wrapper directory pathspec sweeps a peer's file | blind auditor | 🔴 |
| 7 | Audit-evidence inference credits `NOT AUDITED` | blind auditor | 🔴 |
| 8 | Census parser accepts impossible arithmetic | blind auditor | |
| 9 | Record's 9.3 baseline derivable from no run | blind auditor | 🔴 |
| 10 | Handoff finding's hypothesis (b) false about the tool | peer (fixture) | |
| 11 | Brief v2 failed the locator-obligation suite | machine | |
| 12 | Dependency pin asserted an unverified licence bare (peer's file, my catch) | self | |
| 13 | Executable bit missing on my own new test | machine | |

```
ATTRIBUTION_CENSUS
incidents: 13
machine: 3   blind_auditor: 4   peer: 3   self: 3
severity_high: 6   of which self: 1
undetected_known: 0
```

`undetected_known` is 0 today and the line exists because that is unlikely; the follow-up tasks
MF-1 to MF-8 are the places it will move first.

## Part 4 — §21c output

`DEFAULTS_TAKEN` and `STOP_LOG` for this session are in
[`ledger/tasks/orchestrator/ORCH-SCIENTIST-IMPROVEMENT-20260910.json`](../../../../ledger/tasks/orchestrator/ORCH-SCIENTIST-IMPROVEMENT-20260910.json),
single-wave shape, both keys, and are summarised in `2026-09-10.md` § 2c and § 2g. No class-1 or
class-2 stop was taken in two days; the four schema decisions referred to the operator on the
morning of 2026-09-10 remain the operator's and were never a reason to wait.
