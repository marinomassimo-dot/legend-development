# COMMIT CANDIDATE — CC-20261022-SCIENTISTD-R4D-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d` (stated assumption of the Orchestrator), task `REPURP-R4D-D-20261022`, branch `task/R4d-D-20261022`, 2026-10-22.
**context_policy:** `QUESTION_DRIVEN` (the group's questions in `repurposing_batch_selection_20261021.md`). **Not medical advice.** Class-level statements only; no individual-level record.
**target_wm_version:** `WM_v7.27` · **Change class:** MINOR (completing receipts for seven partial readings; one non-canonical comparison re-sourced; no claim status, baseline claim or working-model block is touched).

## 0 · Why

The coordinator asked for (1) the P5 comparison's old exposure wording replaced by the audited statement, (2) the owed sections of seven partial R4 readings completed, (3) two paragraphs on the limits a card would carry when drawing on the GNAO1 zinc pilot and the antisense eligibility consensus. Details in `repurposing_r4d_scientist-d_20261022.md`.

## 1 · Ops

None. `drug_repurposing/p5/` (`build_p5.py`, `p5_check.py`, `p5_comparison.md`, `cells.json`, `tables_deep.md`) is non-canonical and committed on this branch; `p5_check.py` reports 203 cells, 0 problems; the comparison's verdict is unchanged.

## 2 · Completing receipts proposed (staged under `receipt_staging/scientist-d/`; each names its prior receipt, `reread_reason: inadequate_prior_coverage`; the integrator records them in event-ID order)

| Receipt | PMID | Depth after | Not read or unavailable |
|---|---|---|---|
| `FTR-20261022-35499850-02` | 35499850 | partial | supplementary figures `captions_only`; the statistical analysis plan is not among the files |
| `FTR-20261022-39093319-02` | 39093319 | complete | none |
| `FTR-20261022-41250984-02` | 41250984 | complete | none |
| `FTR-20261022-39439575-02` | 39439575 | partial | eTable 1 `unavailable` (not open access in Europe PMC, publisher refused) |
| `FTR-20261022-39625912-02` | 39625912 | complete | none (scanned approvals opened as images; member lists only glanced at, no claim rests on them) |
| `FTR-20261022-39762914-02` | 39762914 | partial | protocol sections 5.2 to 5.4, 5.6, 6, 8, 10, 11 and 13 onward |
| `FTR-20261022-41999155-02` | 41999155 | complete | the numbered reference list of Data S2 |

The nine R4c receipts (`FTR-20261022-<PMID>-01` and `-02` of the previous lot) are not touched by this commit.

## 3 · Claim-level observations (all MINOR; none narrows or reverses a baseline claim)

- Nothing here concerns WWOX; no claim in the registry carries a statement about these indications.
- The P5 comparison's A51 exposure row now equals the audited D01 card sentence; the supralinear reading existed only through the lowest cohort of one patient.
- The two limits paragraphs (note section 3) are drafting guidance for any future card citing 42542632 or 42594875; they add no field to any existing card.

## 4 · Staged leads (not appended to the discovery ledger); all `IPOTESI`

1. **A trial protocol may define its own primary endpoint in more than one way.** In the fenfluramine phase 3 protocol the CGI-I improvement endpoint is worded three ways across protocol synopsis, protocol statistics and supplement table, and the analysis plan is not among the files. Falsifier: the analysis plan, if it fixes one definition and the published result uses it.
2. **Analysis-set names drift between the summary and the statistics section of one protocol** (EPISTOP: "Outcome analysis set" versus "Treatment analysis set"), as does the key secondary endpoint (epilepsy outcome versus neurodevelopmental outcome). A repurposing card that cites a protocol should cite one section and name it. Falsifier: a later protocol version that unifies the terms with the publication still matching.
3. **Single-participant protocols carry their own unblinding by design.** In the fluoxetine protocol the first 8 weeks and the month-7 assessments are unblinded to family and doctor. Falsifier: a published analysis that excludes those windows and finds the same pattern.

## 5 · Shared surfaces left to the Orchestrator

`pathograph`, `batch_queue`, `coverage_report` and `reading_state` not regenerated (commits carry `LEGEND_STALE_SURFACES_BECAUSE`). The four scientific current files, `full_text_queue_current.md`, the registries and the ledger are untouched.

### LOCATOR TRIPLES FOR BLIND AUDIT
87 triples audited blind by two separate agents: 30 SUPPORTED, 57 not (all NARROW, none unsupported); all narrowed before landing, no already-landed entry changed; record in `page_adjudications/locator_audit_R4d_20261022.md`.

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_014`

Propagated by `BATCH_20261019_014` (2026-10-22, MINOR, `WM_v7.27` preserved; integrator ACTOR_ID `integrator`, task `INTEG-BATCH-20261019-014`). The candidate has no ops and proposes no claim; what it supports was landed as registry depth only.

- **Landed:** the evidence depth, receipt, coverage, locator count and surfaces of the records of 35499850, 39093319, 41250984, 39439575, 39625912, 39762914 and 41999155 brought to their standing `-02` receipts (already in the ledger; depth `complete` for 39093319, 41250984, 39625912, 41999155 and `partial` for the other three, as the receipts hold it); `page_adjudications/locator_audit_R4d_20261022.md` cited as a sample audit (30 SUPPORTED, 57 NARROW, none unsupported; all narrowed before landing).
- **Not landed:** the three staged leads of section 4 (all `IPOTESI`); the two limits paragraphs are drafting guidance in the note and add no field to any card; the P5 comparison is a non-canonical file already committed by its author.
