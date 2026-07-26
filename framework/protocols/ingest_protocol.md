# INGEST PROTOCOL

> **Operational protocol for bringing new sources into the LEGEND system.**
> Version: v3.3.1
> Invoke with `MODE: INGEST`.

---

## 0. PURPOSE

Discipline the entry of new sources into LEGEND, deciding for each:

- whether it deserves a `deep dive now`
- whether it goes into the `queue` for future analysis
- whether it is `filtered out` (not relevant)
- in all cases, where it transits before being processed

> **Ingest does NOT update the current files.**
> Ingest only decides: deep dive, queue, filter.
> Any change to the current files goes through BATCH_COMMIT.

---

## 1. INVOCATION

### 1.1 Triggered by

- A new paper found via PubMed/Scholar
- A flagged preprint (bioRxiv, medRxiv)
- A suggestion from a clinician, researcher or other
- Auto-discovery during a deep dive (a paper cited as a critical reference)
- Periodic re-check of a preprint already in tracking (see LINT_DEEP)

### 1.2 Modes

- `MODE: INGEST_SINGLE` — one source at a time
- `MODE: INGEST_BATCH` — multiple sources in one session (e.g. the results of a weekly PubMed query)

---

## 2. SOURCE TYPES

Every source belongs to one of these categories. The category determines the evaluation path and priority.

| Type | Description | Default priority |
|---|---|---|
| `T1_NEW_PAPER` | Newly discovered peer-reviewed paper | High |
| `T2_KNOWN_PAPER_FT` | Known paper, now with full text available | Medium-High |
| `T3_PREPRINT` | bioRxiv / medRxiv not yet peer-reviewed | Medium (observation only) |
| `T4_REVIEW` | Peer-reviewed review article | Medium |
| `T5_ANIMAL_MODEL` | Animal-model study (mouse, rat, fly, zebrafish) | Variable per pathway |
| `T6_ORGANOID_CELL` | Organoids, iPSC-derived neurons, cell lines | Variable per pathway |
| `T7_OMICS_DATASET` | Transcriptomics, proteomics, metabolomics dataset | Medium-High if WWOX-direct |
| `T8_GENE_THERAPY_SOURCE` | Regulatory documents, trial protocol, gene-therapy paper | High |
| `T9_BIOMARKER_SOURCE` | Papers specific to biomarkers (validation, discovery) | High for RL-BIOM-001 |
| `T10_BRIDGE_LITERATURE` | Literature on related disorders (DEE, encephalopathies, generic IDD) | Low-Medium |

### Edge cases

- **Editorial / commentary**: ingest if it cites relevant papers; otherwise `filter out`
- **Conference abstract**: queue, revisit if it becomes a full paper
- **Retraction notice**: `URGENT` — trigger URGENT_COMMIT_REQUEST cat. 5
- **Erratum / correction**: queue for re-evaluation of the original paper

---

## 3. INGEST WORKFLOW

```
[Source detected]
       ↓
[Step 1: Initial assessment]
       ↓
[Step 2: Quarantine in inbox_current.md]
       ↓
[Step 3: Classification]
       ↓
[Step 4: Decision]
       ↓
   ┌───┴───┬───────┐
   ↓       ↓       ↓
[Deep   [Queue  [Filter
 dive]   for FT] out]
   ↓       ↓
[Commit  [full_text_queue
 candidate] _current.md]
```

---

### Step 1 — Initial assessment

For each incoming source, collect and record:

- Identifier (PMID, DOI, preprint ID)
- Title
- Authors (primary, last)
- Journal/source
- Year
- Source type (T1–T10)
- Abstract (if accessible)
- Full-text accessibility (open / paywall / preprint)
- WWOX-mention type (direct / pathway / bridge / none)

Output: a candidate entry in `inbox_current.md`.

---

### Step 2 — Quarantine in inbox

Append an entry to `inbox_current.md` with status `INBOX_PENDING`.

> **Critical rule:** a source never transits directly from discovery to `paper_registry_current.md`.
> It must pass through `inbox_current.md`.

The inbox is the quarantine layer: it protects the system from hasty classifications and keeps a complete audit trail of the ingest.

---

### Step 3 — Classification

For each inbox item, evaluate on 6 dimensions:

| Dimension | Questions |
|---|---|
| **WWOX relevance** | Direct WWOX? WWOX-linked pathway? Bridge literature? None? |
| **Evidence type** | RCT? Cohort? Case series? Mechanistic study? Computational? |
| **Case applicability** | Genotype overlap? Age/severity match? Different population? |
| **Decision impact** | Changes direct clinical decisions? Research? Background only? |
| **Novelty** | New evidence? Replication? Restatement of the already-known? |
| **Risk profile** | Safety signal? Therapeutic claim? Methodological concern? |

Output: a structured classification, appended to the inbox entry.

---

### Step 4 — Decision

Based on the classification, one of three outcomes:

#### 4.1 → `DEEP_DIVE_NOW`

Criteria (requires at least 1):
- WWOX-direct with new decision-relevant evidence
- A safety signal (even merely suspected)
- Paper cited as a critical reference in another ongoing deep dive
- Explicit operator request
- Retraction / invalidation of a baseline

Action:
- Mark the inbox entry as `INBOX_PROMOTED_TO_DEEPDIVE`
- Start the deep dive in the current or next session
- The deep dive **produces a commit candidate**, it does not update the current files

#### 4.2 → `QUEUE_FOR_FT`

Criteria:
- WWOX-relevant but full text not immediately available
- Mechanistic interest, but decision impact not urgent
- Potentially useful bridge literature
- Preprint to revisit at publication

Action:
- Mark the inbox entry as `INBOX_QUEUED`
- Append to `full_text_queue_current.md` with priority (High / Medium / Low)
- Re-evaluate at the next ingest cycle

#### 4.3 → `FILTER_OUT`

Criteria (at least 1):
- No WWOX relevance
- Exact replication of a paper already in the registry with no new evidence
- Evident quality issues (predatory journal, withdrawn without formal retraction)
- Out of scope (e.g. WWOX in oncology with no bridge to CNS)

Action:
- Mark the inbox entry as `INBOX_FILTERED_OUT` with a rationale
- The entry **stays in the inbox** as a record (not deleted)
- Periodically, archive filtered entries (but keep the history)

---

## 4. SPECIAL CASES

### 4.1 Preprint handling

Preprints always enter as `INBOX_PENDING` with a `PREPRINT` tag.

- They can be classified as `OBSERVATION_ONLY` (not usable for clinical decisions)
- Re-check every 90 days (see LINT_DEEP): if published, reclassify
- Never promote a preprint to a `consolidated baseline` claim

### 4.2 WWOX-direct urgent

If the paper is WWOX-direct with a safety signal or a direct clinical-decision impact:

- Skip the queue
- Skip waiting for the periodic BATCH_COMMIT
- Consider URGENT_COMMIT_REQUEST
- Requires operator authorization to accelerate

### 4.3 Retraction / invalidation

If the incoming source is a retraction or an erratum:

- Immediate `RETRACTION_SIGNAL` flag
- Identify the original paper and the claims/metas that cite it as support
- Trigger URGENT_COMMIT_REQUEST category 5
- Inbox entry with maximum priority

### 4.4 Animal/organoid/cell models

For non-human experimental models:

- Always ingest with an explicit `MODEL_TYPE` tag
- Classification must include a "transferability assessment":
  - Direct WWOX KO? Conditional? Patient-specific iPSC?
  - Comparable age/developmental stage?
  - Studied pathway transferable to human?
- Never replaces human evidence for clinical decisions

### 4.5 Auto-discovery during a deep dive

If, during a deep dive on Paper X, it emerges that Paper Y (cited) is critical:

- Pause the current deep dive (do not interrupt)
- Quick ingest of Paper Y into the inbox
- Minimal classification
- Decision: if decision-critical for the current deep dive, deep-dive Paper Y before continuing; otherwise queue

---

## 5. INGEST_BATCH — multiple sources

When ingest arrives from a weekly query (e.g. PubMed search results):

```
For each source in batch:
  Step 1 (Initial assessment) → applied serially
  Step 2 (Quarantine) → all items enter the inbox
Then:
  Step 3 (Classification) → by priority
  Step 4 (Decision) → by priority
```

Batch output:
- N items total processed
- N → DEEP_DIVE_NOW
- N → QUEUE_FOR_FT
- N → FILTER_OUT

Append a batch summary to `legend_activity_log.md`.

---

## 6. ANTI-PATTERNS

- Never update paper_registry directly from ingest
- Never promote a preprint to a baseline claim
- Never assume relevance without an explicit classification
- Never delete filtered entries from the inbox (archive only)
- Never skip the quarantine layer to "save time"
- Never turn ingest into an automatic deep dive without a formal decision
- Never accumulate items in the inbox without classification for > 30 days (see LINT)

---

## 7. INBOX HYGIENE

Weekly (together with LINT_DEEP):

- `INBOX_PENDING` items > 30 days → flag for urgent classification
- `INBOX_QUEUED` items > 90 days → re-evaluate priority
- `INBOX_FILTERED_OUT` items > 365 days → archive (move to a history section)
- `INBOX_PROMOTED_TO_DEEPDIVE` items with no associated commit candidate → flag

---

## 8. CHANGE LOG (this protocol)

| Date | Event |
|---|---|
| — | Created v3.3.1 — quarantine layer, 10 source types, special cases |

---

## 9. WIKILINKS

- Framework: [[LEGEND_CORE]]
- Inbox file: `inbox_current`
- Lint prompt: [[prompt_lint_integrity_check]]
- Batch commit prompt: [[prompt_batch_commit]]
- Full text queue: [[full_text_queue_current]]
- Activity log: `legend_activity_log`

---

**End of `ingest_protocol.md`**

> Everything enters through the inbox. Nothing skips quarantine.
> Ingest never writes to the current files. Ever.
