# STATE MANIFEST — LEGEND (public disease-level fixture)

> **Foundational file.** Active state of the LEGEND system.
> This is the only **state-control** file updatable outside a `BATCH_COMMIT`.
> Designated non-canonical append-only ledgers are explicit carve-outs: they may append
> through their validated writers, but never replace the four scientific current files.
> Every operational event (ingest, lint, commit candidate, batch commit, branch) must update it.
>
> **Public edition note.** This is a **disease-level fixture**, not the operational state of any private working instance. It carries no patient record and no session-specific operational history. It exists so the framework is internally coherent and (eventually) LINT-passable at the disease-model level. Values are illustrative placeholders for the public WWOX disease model.

---

## 0. PURPOSE

Track, unambiguously and readably:

- active framework version
- active disease-model (working-model) version
- state of each `*_current.md` file
- last completed `BATCH_COMMIT`
- last `LINT` run
- current operational state of the system
- active parallel branches (if any)

Without an up-to-date manifest → system in `UNKNOWN` state → `BLOCK_SYSTEM`.

---

## 1. SYSTEM VERSION

```yaml
framework_version: v3.3.1
framework_file: framework/instruction/LEGEND_CORE.md
manifest_schema_version: 1.0
edition: public
```

---

## 2. DISEASE-MODEL (WORKING-MODEL) VERSION

```yaml
working_model_version: WM_v3.2
working_model_file: disease-models/wwox/registries/working_model_current.md
narrative_view: disease-models/wwox/disease_model.md
notes: "Canonical disease-level working model derived from public literature; disease_model.md is its narrative reader-facing view. The private individual-level record is not part of this edition."
```

**Rule:** every `BATCH_COMMIT` that modifies the disease model **must** bump `working_model_version` (format `WM_vMAJOR.MINOR`).

- MINOR bump: claim addition/modification, block update without reversals
- MAJOR bump: reversal of a baseline claim, block redefinition, authorized urgent commit

Commit candidates must declare their intended `target_wm_version`.

---

## 3. CURRENT FILES STATE

### 3.1 Disease-model canonical files

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/registries/working_model_current.md` | present | **canonical** disease-level working model — claim mirror, changelog, decision blocks |
| `disease-models/wwox/disease_model.md` | present | narrative reader-facing view of the same model |
| `disease-models/wwox/registries/claim_registry_current.md` | present | canonical claims (public literature) |
| `disease-models/wwox/registries/paper_registry_current.md` | present | integrated / baseline-linked papers |
| `disease-models/wwox/registries/literature_tracking_log_current.md` | present | lifecycle state of every paper in the pipeline |

### 3.2 Meta-analyses

| File | Status |
|------|--------|
| `disease-models/wwox/meta/meta_index_current.md` | present |
| `disease-models/wwox/meta/meta_network_myelin_glia_current.md` | present |
| `disease-models/wwox/meta/meta_metabolism_current.md` | present |
| `disease-models/wwox/meta/meta_prenatal_structure_current.md` | present |
| `disease-models/wwox/meta/meta_human_spectrum_current.md` | present |
| `disease-models/wwox/meta/meta_gaba_paradox_current.md` | present |

### 3.3 Compounding-memory files (non-canonical, append-only)

| File | Status | Notes |
|------|--------|-------|
| `disease-models/wwox/research/discovery_ledger_current.md` | present | cumulative discovery capital — leads toward biomarkers, molecules, repurposing |
| `disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md` | present | scored hypothesis portfolio from the co-scientist loop |
| `disease-models/wwox/research/dismissal_ledger_current.md` | present | rejections with their `REVIVAL_TRIGGER` — nothing dies in silence |
| `framework/eval/learned_gates_registry.md` | present | reusable error-prevention gates distilled from failures |
| `disease-models/wwox/registries/fulltext_read_receipts.jsonl` | present | authoritative append-only full-text event ledger; hash-chained and tail-anchored (§6.1), LINT-verified; includes explicitly non-contemporaneous legacy reconstructions |

### 3.4 Operational files (private overlay — not in this repository)

| File | Status | Notes |
|------|--------|-------|
| `inbox_current.md` | not shipped | ingest quarantine |
| `session_commit_log.md` | not shipped | commit-candidate queue; the LINT checks it when present |
| `legend_activity_log.md` | not shipped | operational timeline |
| `capability_scout_log.md` | not shipped | capability-growth log |

---

## 4. LAST BATCH_COMMIT

```yaml
last_batch_commit_id: BATCH_20260726_001
last_batch_commit_date: 2026-07-26
last_batch_commit_type: MANUAL
commit_candidates_propagated: 3
commit_candidates_superseded: 0
commit_candidates_deferred: 0
target_wm_version: WM_v3.2
last_wm_update: 2026-07-26
last_wm_batch_commit_id: BATCH_20260726_001
trigger: "explicit operator request (below the 5-candidate threshold; manual trigger)"
notes: "CC-20260726-001/002/003 → PAPER 054/055/056, CLAIM 034/035 new, CLAIM 009/016/024 modified. Three lineage references in the candidates (CORPUS P376, CORPUS P263, and a conditional CORPUS P204 merge) were rejected in the conflict phase and not propagated. Pre-flight and post-propagation LINT PASS; snapshot backup/snap_20260726_1600."
```

---

## 5. LAST LINT

```yaml
last_lint_type: LINT_AUTOMATIC
last_lint_id: LINT_20260806_006
last_lint_date: 2026-08-06
last_lint_result: PASS
notes: "PMID 30290271 read completely from article HTML/PDF with all six figures, Table 1, both supplements and 90 references audited. Receipt FTR-20260806-30290271-01 appended (46 -> 47 events). After adversarial cross-review, its schema-v2 manifest carries 14 exact body-text locators plus 7 fingerprinted figure locators and passes strict verification with zero gaps. The candidate is explicitly MAJOR (target WM_v4.0_2026-08-06), deletes unsupported medication-safety language and requires operator authorization; unread-premise baseline is the live 13/13 and self-eval is 24/24 PASS. PubMed pipeline commits 212850e, 510414d and d9ccac9 merged and independently hardened. A fresh 2026-08-06 harvest preserves 706/706 records, 693 abstracts in the gitignored NOT_EVIDENCE corpus and a tracked no-abstract projection with 40 correction links. RefType direction was corrected: 7 affected publications are held, while 4 editorial notices remain admissible audit sources. Five held PMIDs occur on current surfaces, but none is integrated as a canonical PAPER and no claim wikilink depends on one; PMID 28151481 was already explicitly excluded. Legacy receipt FTR-20260726-23446842-01 was the sole receipt-to-PAPER identity mismatch and is quarantined append-only by FTR-20260806-23446842-02; active depth and generated coverage no longer attribute it to PMID 23446842. LINT PASS; public release gate PASS/BLOCKS 0. The pre-refresh clean-worktree release suite passed with one declared local-fulltext skip; post-refresh suite pending this lint event."
```

---

## 6. OPERATIONAL STATE

```yaml
current_state: READY
deep_dive_gate: OPEN
ingest_gate: OPEN
batch_commit_gate: OPEN
active_parallel_branches: none
```

---

## 6.1 FULL-TEXT RECEIPT LEDGER ANCHOR

The full-text receipt ledger is append-only. A per-event hash chain makes a rewritten or
deleted historical event detectable; it cannot detect a *truncated tail*, because the
surviving prefix stays self-consistent. The anchor below closes that gap: it pins how many
events the ledger must hold and the digest of its last one. `LINT_AUTOMATIC` verifies both,
and a mismatch is `BLOCK_SYSTEM` — reading history you cannot trust is worse than none.

```yaml
fulltext_ledger_path: disease-models/wwox/registries/fulltext_read_receipts.jsonl
fulltext_ledger_events: 48
fulltext_ledger_head: 7e72304ff2852a570ba92480d7ae7f7139817a3431e014d45396f951d7ac9e55
```

Maintained automatically — `fulltext_receipts.py record` re-anchors after every append.
To re-anchor by hand after an authorized repair:

```bash
python3 framework/scripts/fulltext_receipts.py anchor
python3 framework/scripts/fulltext_receipts.py verify
```

### Registry-declaration ratchet

Twenty registry records carry a historical `full text reviewed` declaration with no
surviving complete-coverage receipt. They are kept visible rather than deleted or
retroactively upgraded — the work happened, the evidence of *how completely* did not
survive. The baseline below is a **ratchet**: history is grandfathered by both count and
exact record identity. A count alone is insufficient because one old declaration could be
removed while a different unsupported declaration is added. Any *new* full-text declaration
must be backed by a persisted `complete_fulltext_read` receipt, or `LINT_AUTOMATIC` returns
`BLOCK_BATCH_COMMIT`.

```yaml
registry_only_fulltext_declarations_baseline: 20
registry_only_fulltext_declaration_ids: ["PAPER 005", "PAPER 010", "PAPER 011", "PAPER 012", "PAPER 014", "PAPER 016", "PAPER 028", "PAPER 029", "PAPER 031", "PAPER 032", "PAPER 039", "PAPER 040", "PAPER 042", "PAPER 043", "PAPER 044", "PAPER 045", "PAPER 046", "PAPER 049", "PAPER 050", "PAPER 053"]
```

Lowering the baseline is the intended direction of travel: back-fill a record with real
evidence, re-run `coverage_report.py`, then lower the number and remove that resolved ID
from the grandfathered list.

### Unread-premise ratchet

A separate and harsher debt, measured on 2026-07-26 by `session_self_eval.py`. The *reasoning*
layer — metas, therapeutic strategies, the analysis files — cites papers as **support for
conclusions**. The first measurement found seventeen of eighteen PMIDs with **no
complete-read receipt, no registry full-text declaration and no full-text-queue entry**. The
ratchet has since fallen as papers were read or their debt was made explicit; the current
baseline below must equal the live count, never preserve historical padding.

This is the failure mode that let PMID 22193544 be load-bearing in five files while unread,
with every existing check passing. It is invisible by construction, because leaning on a paper
writes nothing anywhere. So it is measured instead of assumed.

```yaml
unread_premise_baseline: 13
unread_premise_measured_on: 2026-08-06
```

**It is a ratchet, not a wall.** Blocking on the whole legacy backlog would only teach sessions
to route around the check; capping it makes every *new* unread premise a visible regression
(`UNREAD_PREMISE` → `BLOCK_BATCH_COMMIT`). Three things clear a citation, and only three: a
persisted `complete_fulltext_read` receipt, a registry record declaring the full text reviewed,
or an explicit `full_text_queue_current.md` entry. The third is what keeps the check honest
rather than punitive — **declared reading debt is legitimate work in progress; silence is not.**

---

## 7. NOTES

This fixture is intentionally free of any individual patient's operational history. The public edition separates three layers: the generic `framework/`, the disease-level `disease-models/wwox/`, and a private N-of-1 overlay that is **not** part of this repository.
