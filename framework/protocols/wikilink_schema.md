# WIKILINK SCHEMA

> **Wikilinking rules for the LEGEND system.**
> Version: v3.3.1
> Normative — changes require a BATCH_COMMIT with a MAJOR WM bump.

---

## 0. PURPOSE

Define explicit rules for:

- wikilink syntax
- minimum mandatory links per record type
- validation via the LINT
- severity of violations

> **Without linking discipline, the system becomes an entropic wiki in 2 weeks.**
> The rules here are mandatory, not suggested.

---

## 1. SYNTAX

### 1.1 Base format

```
[[file_current]]
[[file_current#heading]]
[[file_current#ID-NNN]]
```

Examples:
```
[[paper_registry_current]]
[[paper_registry_current#PAPER 028]]
[[claim_registry_current#CLAIM 028]]
[[research_lines_current#RL-GT-001 — Gene therapy design principles]]
[[meta_metabolism_current]]
[[biomarker_candidates_current#BC-001]]
[[clinical_monitoring_endpoints_current#CME-001]]
```

### 1.2 Conventions

- Files without the `.md` extension in links
- Exact heading match (case-sensitive, spaces included)
- Exact ID match (e.g. `CLAIM 028` with a space, not `CLAIM_028`)
- Display alias: `[[file#Full heading text|RECORD-ID]]` — **the normal form for record links**, not an exception (see 1.2.1)

#### 1.2.1 Heading links carry the **whole** heading — three consequences

An Obsidian heading link resolves only against the **complete heading text** after `#`. An ID-only fragment (`file#DL-MECH-005`) does **not** resolve when the heading is `### DL-MECH-005 — …`. Enforced by `scripts/test_link_targets.py`. Three rules follow, and the third was learned the hard way.

1. **Always write the full heading plus an alias.** The alias keeps the rendered text short; the fragment keeps the link navigable:
   ```
   [[discovery_ledger_current#DL-MECH-005 — <full heading text>|DL-MECH-005]]
   ```

2. **Records that are not headings use a block ID, never a heading fragment.** Some record families (`FM-*` failure modes) are defined as list items, not headings — no fragment rewrite can ever resolve them. Anchor the definition line with an Obsidian block ID and link to it:
   ```
   - **FM-010 — …** ^fm-010          ← definition line
   [[discovery_ledger_current#^fm-010|FM-010]]   ← link
   ```
   This is link infrastructure, not a schema change: the record line is not promoted to a heading and no scientific assertion is touched.

3. 🔴 **A heading is inlined into every link that points at it. Treat heading text as published-everywhere text.** Two failure modes, both observed:
   - **Privacy.** A heading containing an exact variant string propagates that string into every referring line. On 2026-07-25 the heading migration alone re-created a re-identifying two-variant combination on six lines that had previously been clean, and the publication gate blocked. **Headings must not carry exact variant identifiers** — name the allele class (`the missense SDR allele`, `a canonical splice-acceptor allele`); the exact notation belongs in the body.
   - **Nesting.** A heading must never contain a wikilink. Inlining it would nest one double-bracket link inside another and break both. Put the cross-reference on the line *below* the heading.

### 1.3 What is NOT a wikilink

- Standard Markdown link `[text](url)` → external use (URL, DOI)
- Narrative references without a link → e.g. "see section X" (prefer a wikilink if possible)
- Paper citations → prefer `[[paper_registry_current#PAPER NNN]]` over "(Smith et al. 2024)"

---

## 2. MANDATORY MINIMUM LINKS BY RECORD TYPE

Each record must have specific minimum links. Missing → declared severity.

### 2.1 Paper record (in paper_registry_current)

Mandatory minimum links:
- ≥ 1 link to [[claim_registry_current#CLAIM NNN]] (the paper must support at least one operational claim) → `BLOCK_BATCH_COMMIT` if missing.
  - Exempt: statuses `archived`, `bridge_only`, `background_only`.
  - Epistemic note: do not create an artificial claim to satisfy the schema. If a paper is only context/non-operational hypothesis, the record stays `background_only` with no claim-link; the LINT must treat it as `INFO` or no finding.
- ≥ 1 link to a [[literature_tracking_log_current]] entry → `WARN_BUT_PROCEED` if missing
- 0+ links to [[meta_metabolism_current]] → `INFO` if missing
- 0+ links to [[research_lines_current#RL-XXX-NNN]] → `INFO`

### 2.2 Claim record (in claim_registry_current)

Mandatory minimum links:
- ≥ 1 link to [[paper_registry_current#PAPER NNN]] → `BLOCK_BATCH_COMMIT` if missing (a claim cannot exist without support)
- ≥ 1 link to a [[disease_model]] section **if** the status is `consolidated baseline` → `BLOCK_BATCH_COMMIT` if missing
- 0+ links to [[meta_metabolism_current]] → `INFO`

### 2.3 Meta record (in meta_*_current)

Mandatory minimum links:
- ≥ 3 links to [[claim_registry_current#CLAIM NNN]] (a meta requires ≥3 coherent papers) → `BLOCK_BATCH_COMMIT` if < 3
- ≥ 1 link to [[meta_index_current]] → `WARN_BUT_PROCEED` if missing
- 0+ links to [[research_lines_current]] → `INFO`

### 2.4 Research-line record (in research_lines_current)

Mandatory minimum links:
- ≥ 1 link to [[claim_registry_current]] or [[paper_registry_current]] (an orphan research line = WARN) → `WARN_BUT_PROCEED` if none
- 0+ links to [[research_candidates_current]] → `INFO`
- ≥ 1 link to [[biomarker_candidates_current]] **if** the research line is RL-BIOM-* → `BLOCK_BATCH_COMMIT`

### 2.5 Biomarker candidate (in biomarker_candidates_current)

Mandatory minimum links:
- ≥ 1 link to a pathway in [[meta_metabolism_current]] (mechanistic linkage) → `BLOCK_BATCH_COMMIT` if missing
- ≥ 1 link to a supporting [[claim_registry_current#CLAIM NNN]] → `BLOCK_BATCH_COMMIT` if status ≠ NOT VALIDATED without support
- ≥ 1 link to [[paper_registry_current#PAPER NNN]] → `BLOCK_BATCH_COMMIT` if status = DATO without a paper
- 1 link to [[research_lines_current#RL-BIOM-001 — WWOX functional-state biomarkers|RL-BIOM-001]] → `BLOCK_BATCH_COMMIT` if missing

### 2.6 Clinical monitoring endpoint (in clinical_monitoring_endpoints_current)

Mandatory minimum links:
- ≥ 1 link to [[paper_registry_current#PAPER NNN]] (reference paper for the scale/protocol) → `WARN_BUT_PROCEED` if missing
- 0+ links to [[biomarker_candidates_current]] in the "Linked biomarkers — combined reading" section → `INFO`
- 0+ links to a [[disease_model]] section → `INFO`

### 2.7 Inbox entry (in inbox_current)

Mandatory minimum links:
- 0+ links (the inbox is quarantine, may not have links yet)
- 1 link to [[paper_registry_current#PAPER NNN]] **if** status = `INBOX_PROMOTED_TO_DEEPDIVE` or later → `WARN_BUT_PROCEED`

### 2.8 Commit candidate (in session_commit_log)

Mandatory minimum links:
- 1 link to the origin paper ([[paper_registry_current]] or `inbox_current`) → `BLOCK_BATCH_COMMIT` if missing
- Links to the modified objects (impacted claim/meta/research/biomarker/endpoint) → `BLOCK_BATCH_COMMIT` if missing for objects declared in the "Files impacted" section

---

## 3. WIKILINK INTEGRITY (LINT severity)

Reference: [[prompt_lint_integrity_check]].

### 3.1 Severity by case

| Case | Severity |
|---|---|
| `[[file_current#ID]]` but file missing (one of the 4 scientific currents) | `BLOCK_SYSTEM` |
| `[[file_current#ID]]` but file missing (another current) | `BLOCK_BATCH_COMMIT` |
| `[[file_current#ID]]` with file present but ID non-existent in the registry | `BLOCK_BATCH_COMMIT` |
| `[[file_current#ID]]` with file present, ID existing, syntax broken | `BLOCK_BATCH_COMMIT` |
| `[[future_concept_current]]` (emerging concept, page not yet created) | `WARN_BUT_PROCEED` |
| Orphan page (no inbound link from any current) | `INFO` |
| Wikilink to a non-existent heading (heading renamed) | `BLOCK_BATCH_COMMIT` |

### 3.2 Examples

✅ **Valid:**
```
[[paper_registry_current#PAPER 028]]
```
(file exists, PAPER 028 is in the registry)

❌ **BLOCK_BATCH_COMMIT:**
```
[[claim_registry_current#CLAIM 999]]
```
(file exists, CLAIM 999 does NOT exist in the registry)

⚠️ **WARN_BUT_PROCEED:**
```
[[future_concept_current]]
```
(file does not exist but is declared as an "emerging concept, to be created")

❌ **BLOCK_SYSTEM:**
```
[[disease_model]]
```
(when disease_model.md is MISSING)

---

## 4. NAMING CONVENTIONS

### 4.1 ID formats

| Record type | Format | Example |
|---|---|---|
| Paper | `PAPER NNN` | `PAPER 028` |
| Claim | `CLAIM NNN` | `CLAIM 028` |
| Biomarker candidate | `BC-NNN` | `BC-001` |
| Clinical monitoring endpoint | `CME-NNN` | `CME-001` |
| Research line | `RL-XXX-NNN` | `RL-BIOM-001` |
| Inbox item | `INBOX-NNN` | `INBOX-001` |
| Commit candidate | `CC-YYYYMMDD-NNN` | `CC-2026-04-30-001` |
| Batch commit | `BATCH_YYYYMMDD_NNN` | `BATCH_20260430_001` |
| Branch | `BRANCH_X_YYYYMMDD` | `BRANCH_A_20260430` |
| Lint | `LINT_YYYYMMDD_NNN` | `LINT_20260430_001` |
| Conflict | `CONFLICT-NNN` | `CONFLICT-001` |
| Urgent request | `URG_YYYY-MM-DD_NNN` | `URG_2026-04-30_001` |

### 4.2 Filename conventions

- Current files: `<area>_current.md`
- Protocols: `prompt_<purpose>.md` or `<purpose>_protocol.md`
- Logs: `<purpose>_log.md`
- Reports: `<purpose>_report.md`
- Branch logs: `session_commit_log_branch_<X>.md`

### 4.3 Heading conventions

- IDs in headings: a space between prefix and number (`PAPER 028`, not `PAPER028`)
- Numbered sections with a dot: `## 1. Section name`
- Sub-sections: `### 1.1 Subsection`
- Headings in English; narrative content in the working language

---

## 5. INBOUND LINK REQUIREMENTS

To avoid orphan pages:

| File type | Min inbound links |
|---|---|
| Scientific currents (4 mandatory) | ≥ 5 inbound (they are the heart of the system) |
| Meta files | ≥ 3 inbound (from claims, research, WM) |
| Individual research lines | ≥ 1 inbound from the [[research_lines_current]] index |
| Biomarker candidates / Endpoints | ≥ 1 inbound from the corresponding research line |
| Inbox / commit log / activity log | no requirement (they are queues/logs) |
| Manifest | not necessarily linked from anywhere (it is a meta-file) |

Violation severity: all `INFO` or `WARN_BUT_PROCEED` (never blocking — orphanhood is a signal, not an error).

---

## 6. WIKILINK PROPAGATION (when records change)

When a record is modified (in BATCH_COMMIT), its wikilinks are re-validated.

### 6.1 File rename
If a file is renamed (rare, requires a MAJOR bump):
- All wikilinks pointing to the old name → `BLOCK_BATCH_COMMIT`
- They must be updated in the same BATCH_COMMIT (Phase 4)

### 6.2 Heading rename
If a heading changes:
- All wikilinks that pointed to the old heading → `BLOCK_BATCH_COMMIT`
- Mandatory update in the BATCH_COMMIT

### 6.3 Record deletion
If a record is archived/removed:
- Wikilinks to the archived record stay valid if the record still exists (even if archived)
- Wikilinks to a deleted record → `BLOCK_BATCH_COMMIT`
- **LEGEND rule:** records are never deleted. Only archived. So case 6.3 is rare.

---

## 7. AUTO-VALIDATION CHECKLIST (run by the LINT)

For each LINT run (see [[prompt_lint_integrity_check]]):

```
For each wikilink in the system:
  1. Target file exists?
  2. If file exists: target heading/ID exists?
  3. Severity assignment based on result
  4. Add to LINT report

For each record (paper, claim, meta, research, biomarker, endpoint):
  1. Has minimum mandatory outbound links? (section 2)
  2. Severity assignment if missing
  3. Add to LINT report

For each file:
  1. Has minimum inbound links? (section 5)
  2. Severity = INFO or WARN
  3. Add to LINT report
```

---

## 8. ANTI-PATTERNS

- Never use wikilinks for decorative narrative text (links must point to actual records)
- Never assume "the reader will understand" without an explicit link
- Never accumulate WARN_BUT_PROCEED without cleanup (a symptom of drift)
- Never violate naming conventions for "readability" (it breaks the LINT)
- Never use relative wikilinks with path segments such as `../folder/file` — always a flat basename
- Never link branch commit logs during standard operations (they are for merge only)
- Never put wikilinks inside code blocks (they are not rendered)
- 🔴 Never decorate a heading that wikilinks point into — an emoji, a `— ✅ CLOSED`, a status
  marker. A fragment must match the **complete** heading text, so decorating one breaks every
  link into it, and it breaks them by reporting "not found" rather than by failing loudly.
  Put the marker on the line below.

> 🔴 **DEFERRED WORK, written down so it is a line of work tomorrow rather than a fourth
> rediscovery.** Three occurrences on 2026-08-10, two actors, one cause. Two wikilinks aimed at
> `#DEFAULTS THAT BIT US` never resolved, because the heading is `## 🩸 DEFAULTS THAT BIT US`.
> A queue entry decorated as `## FT-039 — ✅ CHIUSA` broke the three links into `#FT-039` and
> had to be undecorated. And a dangling-reference probe reported twelve missing `DL-` records
> that all exist, because its pattern did not cross the emoji in `### 🔴 DL-MECH-029`.
>
> The repair is not a new guard. The LINT already walks headings and already resolves
> fragments: it needs to **normalise away emoji and decoration before comparing, in both
> directions** — when it collects anchors and when it resolves fragments. One site, no new
> mechanism. The anti-pattern above stands whether or not that lands, because a rule a person
> follows is cheaper than a rule a tool repairs.
>
> Priority argument: a decoration added tomorrow silently breaks yesterday's links. It does not
> fail loudly — it says "not found", which is the compounding-loss class.

---

## 9. EVOLUTION RULE

This schema is **normative**. Changes require:

- A BATCH_COMMIT with a MAJOR Working-Model bump
- Update of all impacted files in the same batch
- Update of [[index]]
- Update of [[prompt_lint_integrity_check]] if severities change
- Append to `legend_activity_log` with a framework_change event

---

## 10. CHANGE LOG (this schema)

| Date | Event |
|---|---|
| — | Created v3.3.1 — syntax, mandatory links per record type, severity scale per violation, naming conventions |

---

## 11. WIKILINKS

- Framework: [[LEGEND_CORE]]
- Index: [[index]]
- Lint prompt: [[prompt_lint_integrity_check]]
- State manifest: [[state_manifest_current]]

---

**End of `wikilink_schema.md`**

> Linking discipline = system discipline.
> Without it, it is an entropic wiki in 2 weeks.
