# M1 · Adoption audit of Waves 2–3, and the evidence behind the C5 and B4 deferrals

> Design record, harness only (non-normative). Nothing here changes a claim, the working model,
> an evidence grade, a registry or a ledger. Author: `junior-harness`, assigned by the
> Orchestrator for Harness Engineering (roadmap v1.1, Wave 5 item M1). Date: 2026-09-26.
> Audit point: `main` at `e30b8ec`. Supersedes the "Adoption observation" paragraph of
> [`state_hot_cold_20260924.md`](state_hot_cold_20260924.md), which found nothing to observe.

## 1 · What was being adopted

| Wave | Commits (2026-09-24 UTC) | What an artefact or a session should now show |
|---|---|---|
| B1–B3 | `6113e4a` 20:31 · `9aff689` 20:32 · `175d131` 20:33 | no forced positive lead; no hypothesis count target; convergence raises priority, never epistemic level |
| C1 | `c9bfbaa` 21:12 | `context_policy` declared at the top of dossier / reading notes / Task Contract `SCOPE`; the written `FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` transition |
| C2–C4 | `a54de5b` · `ece1c6f` · `73fb5f3` 21:14–21:17 | `legend`, `legend-discovery`, `legend-deepdive` read the source before ledger, registries and working model; forge is `SYNTHESIS`, PaperQA is `QUESTION_DRIVEN` |
| D1–D6 | `f8b19f6` … `96f8cec` 21:31–21:44 | LEGEND records reached through `registry_records.py`, not by grepping or loading the large registries |

## 2 · Method

**Cut.** Everything after `96f8cec` (2026-09-24T21:44Z): 59 commits to `e30b8ec` (70 after `175d131`).

**Authored vs landed.** The dominant post-cut science is the VPS recovery (`af09f7a`, G4.3). Its
readings, dossiers, manifests, candidates and self-evaluations were **authored on 2026-09-12/14**,
before any of Waves 2–3 existed, and only **landed** after the cut. They are a *baseline cohort*,
not adoption evidence. Authoring dates were taken from each artefact's own header and, for
receipts, from `event_at` / `analysis_at` (read with Python, read-only; the ledger was never
edited; `fulltext_receipts.py verify` OK before and after).

**Transcripts.** `~/.claude/projects/-home-desktop-legend-development/`: every JSONL with events
after the cut, excluding this auditing session (in progress, four concurrent sibling tasks) —
**42 transcripts: 3 main sessions, 39 subagents**. For each: every tool call in order, tagged as
*LEGEND prior* (registries, working model, ledgers, dossiers, candidates, handoffs, analysis
notes), *full-text source* (`get_full_text_article`, `files/fulltext/`, PMC/Europe PMC full-text
XML, PDF extraction), or *targeted retrieval* (an executed `registry_records.py` subcommand).
Accesses to the five large surfaces (claim registry, paper registry, working model, discovery
ledger, literature log) were classed: identifier lookup (grep/sed/awk on a CLAIM, PAPER, DL or
PMID key), theme grep, whole read, or diff/structural (`git show`/`diff`, formatting audits,
cross-branch comparison — out of the retrieval tool's scope and excluded from the denominator).
The classifier is heuristic; §5 lists the rows it rests on so they can be re-checked by hand.

## 3 · Adoption, with denominators

### 3.1 Repository artefacts

| Artefact class | Landed after cut | Authored after cut | `context_policy` declared | Notes |
|---|---:|---:|---:|---|
| Read receipts | 29 (ledger 207 → 236) | **0** (newest `event_at` 2026-09-23T20:32Z) | n/a (not a receipt field, C1) | `reread_reason` 29/29, `workflow` 29/29 |
| Full-text dossiers | 29 | 0 | 0/29 | blind / source-first first pass stated in 25/29 (baseline) |
| Deep-dive manifests | 28 | 0 | 0/28 | — |
| Commit candidates | 37 recovered + dispositions | dispositions only | 0 | — |
| Session self-evaluations | 3 | 0 | — | — |
| Comparison / M4b notes | 4 | 0 | — | the comparison was already a separate phase (baseline) |
| Batch reports (`state_history`) | 6 (`ALDAZ_R1`, `ALDAZ`, `MALLARET`, `LITVOCAB`, `ALDAZ_R2`, `ALDAZ_R3`) | 6 | 0/6 | all `SYNTHESIS` by nature; C1 does not require the declaration outside a reading |
| Blind locator audits | 2 | 2 | 0/2 | blindness declared in the audit's own vocabulary (inputs listed and restricted) |
| Mirror consultations | 2 | 2 | 0/2 | review, `SYNTHESIS` |
| Discovery / therapeutic ledger appends | 16 | 16 | — | 10 narrowing notes (ALDAZ, MALLARET) + 6 retractions (ALDAZ_R3) |

**The finding that frames every other row: no full-text reading was authored after C1–C4.** The
denominator for a `SOURCE_FIRST` first pass in the repository is **zero**, exactly as it was on
2026-09-24. Adoption of the reading-route changes cannot be measured from repository artefacts yet.

### 3.2 Sessions (transcripts)

| Route class (by task) | n | Policy declared | Full text opened | Source before any LEGEND prior (tool order) | Receipt emitted |
|---|---:|---:|---:|---:|---:|
| Blind locator auditor | 8 | 0 | 7 | 7/7 | — (audit, not a reading) |
| Literature census / reconnaissance | 16 | 0 | 12 | 12/12 | 0 |
| Targeted full-text extraction (first contact) | 1 | 0 | 1 | 1/1 | 0 |
| Scientist question streams (`SYNTHESIS` + question) | 6 | 0 | 6 | 1/6 (priors are intended input) | 0 |
| Record survey / batch planning | 2 | 0 | 0 | — | — |
| Mirror review / verifier | 4 | 0 | 2 | 0/2 (priors are the object) | — |
| Batch commit | 1 | 0 | 0 | — | — |
| Harness | 1 | 0 | 0 | — | — |
| Main sessions | 3 | 0 | 2 | 0/2 | 0 |
| **Total** | **42** | **0/42** | **30** | **21/30** | **0/30** |

- **Declaration: 0/42.** Not one transcript — prompt, reply or tool input — contains
  `context_policy`, `SOURCE_FIRST` or `QUESTION_DRIVEN`.
- **Order in substance: compliant wherever it matters.** The 21 transcripts that met the source
  before any LEGEND record are exactly the audit, census and extraction routes; the 9 that met
  priors first are all `SYNTHESIS` or review routes, where C1 makes priors the intended input.
  **No transcript is a `SOURCE_FIRST` first reading** in LEGEND's sense (none emitted a receipt).
- **Targeted retrieval: 2 of 105 retrieval acts (1.9 %), in 1 of 12 transcripts.** 12 transcripts
  retrieved LEGEND knowledge from the large surfaces: 103 manual accesses (89 identifier lookups,
  13 theme greps, 1 whole read of the working model) against 2 executed `registry_records.py get`
  calls, both in the recovery / harness main session. By purpose:

| Purpose | Transcripts | Manual accesses | `registry_records.py` calls |
|---|---:|---:|---:|
| Knowledge retrieval (Q230P streams D, E, F; Q230P main; record survey) | 5 | 21 | 0 |
| Review (three Mirror reviews, one verifier, one batch planner) | 5 | 41 | 0 |
| Editing / recovery (one batch commit; the recovery main session) | 2 | 41 | 2 |

  Editing a record needs line numbers, so part of the third row is correct as manual access. The
  first two rows are what D1–D6 were built for, and there adoption is **0/10 transcripts**. Nine
  of the ten were `general-purpose` or `Explore` delegates dispatched by ad-hoc prompts that did
  not name the tool; the tenth is the Q230P main session. No post-cut session invoked a route
  whose contract names the tool (`legend-deepdive` or `fulltext-dossier` agents, `legend-discovery`,
  scientist brief M4b, `study-intake-triage`): the only LEGEND skills invoked were `legend-commit`
  and `legend-locator-audit`.

## 4 · Counterexamples, with locators

| # | Where | What | Class |
|---|---|---|---|
| CE1 | Ludes-Meyers 2004 dossier, `research/fulltext_dossiers/`, § 7 lines 141–147 (landed `af09f7a`, authored 2026-09-13) | a `first_read` by the reader who had drafted the `CLAIM 007` wording that rests on this paper, hours earlier; under C1 that context could not declare `SOURCE_FIRST` | baseline (pre-C), form |
| CE2 | [`locator_audits/2026-09-26_…_CLAIM006_007_blind_audit.md`](../../disease-models/wwox/research/locator_audits/) line 42 (`d0a579f`) | round-0 triple 7 of the Hussain 2023 resume reading carried "abolishes PPxY binding", the then-canonical `CLAIM 007` wording; the auditor ruled OVERSHOOT and traced it to the authors' caption title | baseline (pre-C), ambiguous cause |
| CE3 | transcript `197cf03f…/subagents/agent-affe982f2ad1be32a` tools 10, 29–30, 44, 53–54 | whole read of the working model; paper-registry records located by grepping an identifier and read with `sed` slices, where `get --pmid` returns the whole record | targeted retrieval |
| CE4 | transcript `197cf03f…/subagents/agent-a370a80210a53586b` tools 16–22 | claim records found with `grep "^### CLAIM 0"` and read by line range — `get --id` | targeted retrieval |
| CE5 | transcript `680ebf62…/subagents/agent-a517a8ec1885ff856` tools 5–18 | a survey of "what LEGEND already records" run as 11 greps across both registries and the ledgers — `get --theme` / `mentions` | targeted retrieval |
| CE6 | transcript `ab3d83fa…/subagents/agent-a5c6e85fffe618159` | Mirror review with 14 identifier lookups by `awk` / `sed`, 0 tool calls | targeted retrieval |
| CE7 | transcript `197cf03f…/subagents/agent-a7fbe30ae63529c91`, dispatch prompt | first contact with a full text, dispatched with a companion paper's result and the programme's open decision; `QUESTION_DRIVEN` in substance, undeclared; no receipt; output left in a session scratchpad | declaration, receipt |
| CE8 | the 30 full-text-opening transcripts of §3.2 | 0 receipts; every output stayed in session scratchpads and nothing entered the repository, so no claim rests on them — but if any lands as evidence, its receipt is owed first | receipt |

## 5 · C5 — is a `SOURCE_FIRST` enforcement or routing-order test needed?

**Question.** Is there real contamination — LEGEND's conclusions loaded before the first pass of a
`SOURCE_FIRST` route, and shaping the reading?

**Evidence.**
- After C1–C4: **0** `SOURCE_FIRST` readings, repository or transcript. Nothing to observe.
- Baseline, 29 readings authored 2026-09-12/14 under the scientist standing brief: **1** explicit
  prior-held first read (CE1), whose outcome went **against** the prior (it narrowed the claim
  further); **1** ambiguous overshoot aligned with the prior's wording (CE2), attributable to the
  source's own caption. Both were caught by the blind locator audit before canon.
- The post-cut overshoots that did occur (round 1 of the same audit: 3 OVERSHOOT + 3 NOT_IN_SOURCE
  in the rewritten claims) are `SYNTHESIS` distortion, not a first-pass effect, and the existing
  audit caught them.

**Verdict: C5 stays DEFERRED.** No instance where a prior demonstrably shaped a first pass, and
the one control that would catch it downstream (R4 locator audit) worked every time it ran.
**Revival trigger:** the first post-C `SOURCE_FIRST` reading whose blind audit returns an OVERSHOOT
or UNDERSHOOT aligned with a LEGEND wording the reader held before its transition line; or a
second `first_read` declared by the author of the claim under test.

## 6 · B4 — is a regression test against returning quota phrasing needed?

**Evidence.**
- Harness surfaces (`.claude/skills`, `.claude/agents`, `framework/protocols|manuals|instruction|master|templates`,
  `roles/`, `SKILLS.md`, `CAPABILITIES.md`, `FAQ.md`, `ARCHITECTURE.md`, `AGENTS.md`, `BOOTSTRAP.md`),
  searched for mandatory positive leads ("zero leads … not admissible", "at least one lead"),
  fixed hypothesis counts ("10–30", "N–M hypotheses") and convergence-as-promotion, in English
  and Italian: **0 recurrences** (the one hit is B3's own negating sentence).
- The 42 post-cut transcripts (prompts, replies, dispatches): **0** (one false positive: a
  sequence-identity range).
- The 16 post-B ledger appends: **0** new leads, **0** promotions; the 6 `ALDAZ_R3` appends cite
  B3 and **retract** convergence-derived certainty, one of them a legacy "DATO (convergente su ≥3
  modelli)" tag. Legacy ledger entries from before B3 still carry convergence-as-promotion
  wording; they are append-only history, correctable only by append, not a recurrence.
- B1's explicit reading outcome (`NEW_LEAD` … `NO_NEW_LEAD`): no post-B discovery reading exists,
  so it is unmeasured.

**Verdict: B4 stays DEFERRED.** **Revival trigger:** a quota phrase back on any harness surface
above, or a post-B discovery reading that closes on a lead its own coverage does not support.

## 7 · Fixes landed with this record (T0, harness-owned)

| Defect surfaced | Fix |
|---|---|
| The route that produced every landed reading — [`scientist_standing_brief.md`](../../framework/protocols/scientist_standing_brief.md), M0 → M5 — already reads blind but never names `context_policy` or the transition line, so a reading that follows it declares nothing (0/29) | M2 now opens with the `context_policy:` declaration in reading notes and dossier header, including the "a context that holds the conclusion declares `QUESTION_DRIVEN`" case that CE1 is; M4b now writes the transition line and names what it admits. Both route to the protocol rather than restating it |
| Ad-hoc `general-purpose` dispatches carried neither a policy (0/42) nor the retrieval route (0/10) | [`fulltext_read_receipt.md`](../../framework/protocols/fulltext_read_receipt.md) *Before reading*: an ad-hoc subagent prompt that sends a reader to a full text is a dispatch — its first line names the policy, a prompt that states LEGEND's answer is `QUESTION_DRIVEN`, and a prompt that sends a reader to LEGEND's records names `registry_records.py` |

**Not fixed here, and why.** Annex A carries no `context_policy` slot in the Task Contract, though
C1 names `SCOPE` as its home — a governance annex, outside the skills/protocols/templates perimeter
assigned for this audit; handed to Harness Engineering. The receipts of CE7–CE8 belong to whoever
lands that work; the Orchestrator owns it.

## 8 · What the next adoption sample should wait for

The first `SOURCE_FIRST` reading authored after the cut — a scientist wave under the brief, or a
`legend` / `legend-discovery` run. Its dossier header and reading notes are then greppable for the
declaration and the transition line; this record's §3.1 table is the before-state.
