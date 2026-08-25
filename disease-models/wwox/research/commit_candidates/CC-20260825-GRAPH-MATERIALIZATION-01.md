# COMMIT CANDIDATE — graph materialization of an already-declared relation (CLAIM 025 → CLAIM 009)

**Candidate ID:** CC-20260825-GRAPH-MATERIALIZATION-01
**Status:** PREPARED — awaiting the next lawful BATCH_COMMIT
**Defect class:** traceability / graph-materialization repair — representational only
**Source of analysis:** [[PATHOGRAPH-TRANSPORT-CONSOLIDATION-001]] § 2.3
**Requires primary-evidence reading:** **NO**
**Changes scientific meaning:** **NO**

## The defect

`claim_registry_current.md`, CLAIM 025, `Clinical meaning` field:

> *"**Raffina CLAIM 009**: il branch metabolico non si riduce a HIF1A/glicolisi ma include
> inflammatory-metabolic coupling e possibili Wnt-adjacent state shifts."*

The relation to CLAIM 009 is **declared in words** but carries no wikilink. The graph cannot see
a relation the registry states in plain text, so CLAIM 025 → CLAIM 009 is invisible to every
machine reader while being fully visible to a human one.

Lane-A test, applied item by item:

| Question | Answer |
|---|---|
| SOURCE ASSERTION EXISTS? | ✅ CLAIM 025, status `in observation` |
| TARGET ASSERTION EXISTS? | ✅ CLAIM 009 |
| RELATION ALREADY DECLARED? | ✅ in words — *"Raffina CLAIM 009"* |
| DOES THE ANNOTATION CHANGE SCIENTIFIC MEANING? | ❌ no — only the syntax is absent |
| PERFORMABLE WITHOUT READING PRIMARY EVIDENCE? | ✅ yes |
| BATCHABLE AS GRAPH-MATERIALIZATION REPAIR? | ✅ yes |

## Proposed canonical effect at the next lawful BATCH_COMMIT

- In CLAIM 025's `Clinical meaning`, render the existing mention of CLAIM 009 as a wikilink
  (`[[claim_registry_current#CLAIM 009]]`), preserving the sentence and its wording.
- **No other change.** No new relation is asserted; no relation type is annotated; the direction
  is the one the sentence already states (025 refines 009), and the reverse is **not** added.

## Scope — why this is the only Lane-A item

The Pathograph inventory reports **12** annotation-lane items. They are three findings summed:
`asymmetric_links` (10) + `working_model_comentions` (1) + `unlinked_prose_mentions` (1). Only the
last is mechanical:

- **The 10 asymmetric links are routed out.** `wikilink_schema.md` § 2.2 imposes no claim↔claim
  reciprocity requirement, `legend_lint.py` enforces none, and LINT returns **PASS** — so no rule
  is violated. Seven of the ten are declared in prose fields (`Clinical meaning`,
  `Evidence boundary`, `⚠️ Counter-directional evidence`), where a back-link means authoring a
  sentence. Direction carries meaning: that CLAIM 033 bears on CLAIM 019 does not make the
  converse true. Symmetrising would originate relations the registry never declared.
- **The 1 working-model co-mention is routed out.** Two claims named in one parenthetical
  citation (*"CLAIM 025 / paper 191; CLAIM 026 / PAPER 032"*) assert a source for each, and
  nothing between them. Converting a co-mention to an edge invents the relation.
  *(Checked and cleared: "paper 191" resolves to `[[paper_registry_current#CORPUS P191]]`, which
  exists at `paper_registry_current.md:6128`. Not a defect.)*

**Target WM:** current at BATCH_COMMIT time; rebase required.
**Batch gate:** intentionally untouched.
**Ordering:** independent of the two CLAIM 016 candidates; no conflict.
