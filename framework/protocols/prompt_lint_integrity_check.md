# PROMPT — LINT / INTEGRITY CHECK

> **Operational protocol for checking the consistency and integrity of the LEGEND system.**
> Version: v3.3.1
> Invoke with `MODE: LINT_AUTOMATIC` or `MODE: LINT_DEEP`.

---

## 0. PURPOSE

Verify the integrity and consistency of the entire LEGEND system before allowing critical operations (BATCH_COMMIT) or confirming the operational state (READY).

The LINT **flags**. It does not auto-correct. Corrections always go through BATCH_COMMIT or a manual operator intervention.

---

## 1. INVOCATION

### 1.1 LINT_AUTOMATIC

- Run automatically at the start of every LEGEND session
- Run automatically before every BATCH_COMMIT
- Run automatically at the end of a parallel-branch merge
- Fast, deterministic, full-state check

### 1.2 LINT_DEEP

- Run weekly (or on-demand at operator request)
- Run when semantic drift is suspected
- Exploratory, more expensive, includes cross-paper analysis
- Does not block operations if LINT_AUTOMATIC has already passed

### 1.3 Combined triggers

```
session start → LINT_AUTOMATIC
batch_commit trigger → LINT_AUTOMATIC → if BLOCK, abort batch
weekly schedule → LINT_AUTOMATIC + LINT_DEEP
parallel branch merge → LINT_AUTOMATIC + merge_conflict_report check
```

---

## 2. SEVERITY SCALE

Normative reference: `LEGEND_CORE.md`.

| Severity | Effect on operations |
|---|---|
| `INFO` | Report only, no block |
| `WARN_BUT_PROCEED` | Batch commit possible, warning persists in the queue |
| `BLOCK_BATCH_COMMIT` | Batch commit blocked; deep dive/ingest possible |
| `BLOCK_SYSTEM` | Everything blocked (even deep dive) → recovery mandatory |

**Global outcome:** the maximum across all findings. If at least one is `BLOCK_SYSTEM`, the outcome = `BLOCK_SYSTEM`.

---

## 3. LINT_AUTOMATIC — CHECKLIST

Run in order. Stop at the first `BLOCK_SYSTEM` (recovery first).

### 3.1 State-manifest integrity

| Check | Severity if it fails |
|---|---|
| state_manifest_current.md present and readable | BLOCK_SYSTEM |
| framework_version consistent with the active LEGEND file | BLOCK_SYSTEM |
| working_model_version present and valid format | BLOCK_BATCH_COMMIT |
| current_state field valid (READY / BLOCKED_* / IN_*) | BLOCK_SYSTEM |
| pending_urgent_requests declared with valid status | WARN_BUT_PROCEED |

### 3.2 Four scientific currents (mandatory)

| Check | Severity if it fails |
|---|---|
| working_model_current.md present | BLOCK_SYSTEM |
| claim_registry_current.md present | BLOCK_SYSTEM |
| paper_registry_current.md present | BLOCK_SYSTEM |
| literature_tracking_log_current.md present | BLOCK_SYSTEM |

### 3.3 ID integrity (no duplicates, no orphans)

| Check | Severity if it fails |
|---|---|
| No duplicate PAPER ID in paper_registry | BLOCK_BATCH_COMMIT |
| No duplicate CLAIM ID in claim_registry | BLOCK_BATCH_COMMIT |
| No duplicate BC (biomarker candidate) ID | BLOCK_BATCH_COMMIT |
| No duplicate CME (clinical monitoring endpoint) ID | BLOCK_BATCH_COMMIT |
| Every paper in the registry is also present in the tracking log | WARN_BUT_PROCEED |
| Every claim has at least one supporting paper | BLOCK_BATCH_COMMIT |
| Every paper in the tracking log exists in the registry | WARN_BUT_PROCEED |

### 3.4 Claim-status integrity

| Check | Severity if it fails |
|---|---|
| All claims have a status from the standard vocabulary | BLOCK_BATCH_COMMIT |
| Non-standard status (typo, custom) present | BLOCK_BATCH_COMMIT |

Vocabulary: `consolidated baseline | in observation | conflicting evidence | flagged for review | background only | archived`.

### 3.5 Wikilink integrity

| Check | Severity if it fails |
|---|---|
| Wikilink to an **existing** file/heading but broken (file renamed) | BLOCK_BATCH_COMMIT |
| Wikilink to an ID **existing in the registry** but with broken syntax | BLOCK_BATCH_COMMIT |
| Wikilink to a **non-existent** ID that should exist (e.g. `[[claim_registry_current#CLAIM 028]]` but CLAIM 028 is missing) | BLOCK_BATCH_COMMIT |
| Wikilink to a page/concept **not yet created** (emerging concept) | WARN_BUT_PROCEED |
| Wikilink to one of the 4 **missing** scientific currents | BLOCK_SYSTEM |
| Orphan page (no inbound link) | INFO |

### 3.6 Working-Model consistency

| Check | Severity if it fails |
|---|---|
| working_model_version consistent with the manifest | BLOCK_BATCH_COMMIT |
| Claim IDs in the Working Model BLOCK 2 mirror differ from claim_registry | BLOCK_BATCH_COMMIT |
| Every claim cited by the WM exists in claim_registry | BLOCK_BATCH_COMMIT |
| Claim status consistent with its use in the WM (e.g. an "archived" claim not cited as baseline) | BLOCK_BATCH_COMMIT |
| WM changes tracked in the change log | BLOCK_BATCH_COMMIT |

### 3.7 Commit-candidate queue

| Check | Severity if it fails |
|---|---|
| session_commit_log.md present and readable | BLOCK_BATCH_COMMIT |
| No commit candidate marked "propagated" still in the queue | BLOCK_BATCH_COMMIT |
| Every commit candidate declares `target_wm_version` | BLOCK_BATCH_COMMIT |
| Number of accumulated commit candidates (for the ≥ 5 threshold trigger) | INFO |

### 3.8 Urgent requests

| Check | Severity if it fails |
|---|---|
| Urgent requests pending with status `AWAITING_AUTHORIZATION` | INFO (notify the operator) |
| Urgent request marked `AUTHORIZED` but not executed | WARN_BUT_PROCEED |
| Urgent request with an invalid category (not in 1–5) | BLOCK_BATCH_COMMIT |

### 3.9 Parallel branches

| Check | Severity if it fails |
|---|---|
| active_branches declared in the manifest exist as files | BLOCK_BATCH_COMMIT |
| Active branch + a BATCH_COMMIT attempt without a merge | BLOCK_BATCH_COMMIT |
| merge_conflict_report.md present with status `UNRESOLVED` during a merge | BLOCK_BATCH_COMMIT |

### 3.10 Biomarker / clinical-monitoring discipline

| Check | Severity if it fails |
|---|---|
| biomarker_candidates_current.md contains Tier 3 endpoints (EEG, neuroimaging, etc.) | BLOCK_BATCH_COMMIT |
| clinical_monitoring_endpoints_current.md contains biochemical/molecular biomarkers | BLOCK_BATCH_COMMIT |
| Candidate biomarker described as "WWOX-validated" without a validation paper | BLOCK_BATCH_COMMIT |
| Candidate biomarker without a filled-in scorecard | WARN_BUT_PROCEED |

---

## 4. LINT_DEEP — ADDITIONAL CHECKS

In addition to all LINT_AUTOMATIC checks, run these more expensive checks.

### 4.1 Semantic consistency

| Check | Severity if it fails |
|---|---|
| Contradictions between consolidated claims (claim X asserts A, claim Y asserts ¬A without a `conflicting evidence` flag) | BLOCK_BATCH_COMMIT |
| Meta citing an "archived" claim as active support | WARN_BUT_PROCEED |
| Working Model citing a deprecated meta | WARN_BUT_PROCEED |
| Orphan research line (no linked claim) | WARN_BUT_PROCEED |

### 4.2 Preprint re-check

| Check | Severity if it fails |
|---|---|
| Preprint in the tracking log > 90 days without a re-check | INFO (queue for re-check) |
| Published preprint (DOI changed) still marked as a preprint | WARN_BUT_PROCEED |

### 4.3 Inbox / quarantine

| Check | Severity if it fails |
|---|---|
| Item in inbox_current.md > 30 days without classification | INFO |
| Item in the inbox with a complete classification but not promoted to paper_registry | WARN_BUT_PROCEED |

### 4.4 Biomarker scorecard refresh

| Check | Severity if it fails |
|---|---|
| Candidate biomarker with a scorecard filled in > 180 days ago and new relevant papers added | INFO (queue for refresh) |
| Candidate biomarker promoted to the shortlist without score ≥ 30 | WARN_BUT_PROCEED |

### 4.5 Cross-file referential integrity (deep)

| Check | Severity if it fails |
|---|---|
| Concept cited in ≥ 3 files but with no dedicated page | INFO (consider creating a page) |
| Dedicated page with no inbound link from any current | WARN_BUT_PROCEED |
| Isolated page cluster (no cross-link to the rest of the system) | WARN_BUT_PROCEED |

### 4.6 Gap analysis (informational only)

| Check | Severity if it fails |
|---|---|
| Pathway cited in the WM without a recent supporting claim (> 1 year) | INFO |
| Active research line with no new commit candidate for > 60 days | INFO |
| A Working-Model block with < 3 supporting claims | INFO |

---

## 5. OUTPUT FORMAT

Every LINT run produces a structured block.

```markdown
# LINT REPORT — [LINT_AUTOMATIC | LINT_DEEP]

## Metadata
- lint_id: LINT_YYYYMMDD_NNN
- type: LINT_AUTOMATIC | LINT_DEEP
- timestamp: YYYY-MM-DD HH:MM
- triggered_by: session_start | pre_batch_commit | weekly | manual | post_merge
- framework_version: v3.3.1
- working_model_version: WM_vX.Y_YYYY-MM-DD

## Summary
- overall_severity: PASS | INFO | WARN_BUT_PROCEED | BLOCK_BATCH_COMMIT | BLOCK_SYSTEM
- total_checks_executed: N
- findings_by_severity:
  - INFO: N
  - WARN_BUT_PROCEED: N
  - BLOCK_BATCH_COMMIT: N
  - BLOCK_SYSTEM: N

## Findings

### [SEVERITY] Finding ID — Brief description
- Check section: [3.X / 4.X]
- Affected file(s): [...]
- Detail: [...]
- Suggested action: [...]

[repeat for every non-PASS finding]

## Manifest update
- last_lint_id → LINT_YYYYMMDD_NNN
- last_lint_outcome → [overall_severity]
- unresolved_warnings → N
- unresolved_blocks → N

## Operational-state recommendation
- [READY | BLOCKED_BY_LINT | BLOCKED_SYSTEM]
- Reason: [...]
```

---

## 6. POST-LINT ACTIONS

### If overall = `PASS` or `INFO`
- Update manifest: `current_state: READY`
- Append to legend_activity_log.md
- Proceed with the requested operation

### If overall = `WARN_BUT_PROCEED`
- Update manifest: `current_state: READY`
- Append to legend_activity_log.md
- Proceed with the requested operation
- Notify the operator of the persistent warnings

### If overall = `BLOCK_BATCH_COMMIT`
- Update manifest: `current_state: BLOCKED_BY_LINT`
- Append to legend_activity_log.md
- BATCH_COMMIT blocked
- Deep dive / ingest / query remain possible
- Notify the operator with the findings list

### If overall = `BLOCK_SYSTEM`
- Update manifest: `current_state: BLOCKED_SYSTEM`
- Append to legend_activity_log.md
- ALL operations blocked
- Recovery mandatory
- Notify the operator immediately with escalation

---

## 7. RECOVERY PROTOCOL

If the LINT exits with `BLOCK_SYSTEM`:

1. LEGEND explicitly declares the BLOCKED_SYSTEM state
2. Shows the BLOCK_SYSTEM findings one by one
3. For each, proposes recovery actions (e.g. "reload working_model_current.md", "restore manifest from backup")
4. Does NOT perform recovery autonomously
5. The operator authorizes each recovery action
6. After recovery, re-runs LINT_AUTOMATIC
7. Only if the new LINT exits ≤ WARN_BUT_PROCEED does it unblock the state

---

## 8. ANTI-PATTERNS (what the LINT must NOT do)

- Never auto-correct files
- Never add missing wikilinks
- Never promote a candidate biomarker from NOT VALIDATED to VALIDATED
- Never modify a claim status
- Never assume conflict resolution
- Never ignore a BLOCK because "it looks like a false positive"
- Never compact findings for brevity (loss > elegance)

---

## 9. CHANGE LOG (this prompt)

| Date | Event |
|---|---|
| — | Created v3.3.1 — LINT_AUTOMATIC / LINT_DEEP separation, granular severity scale |

---

## 10. WIKILINKS

- Framework: [[LEGEND_CORE]]
- State manifest: [[state_manifest_current]]
- Activity log: `legend_activity_log`
- Batch commit prompt: [[prompt_batch_commit]]
- Parallel protocol: [[parallel_legend_protocol]]

---

**End of `prompt_lint_integrity_check.md`**

> The LINT is LEGEND's immune system. It flags, it does not heal.
