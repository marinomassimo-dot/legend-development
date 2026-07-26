# Template — discovery_ledger_current.md

Create the discovery ledger with this structure if it does not exist. It is structured-append: leads are not deleted, their status changes. Every change goes through the change-log at the bottom. **It is not a canonical scientific file**: no canonical claims enter it (those go via COMMIT CANDIDATE → BATCH_COMMIT). Wikilinks per `framework/protocols/wikilink_schema.md`.

---

```markdown
# Discovery Ledger — cumulative discovery capital (WWOX → biomarkers / molecules / repurposing)

> Research-layer working file (a carve-out). Append-only on leads; status, never deletion.
> Epistemic tags: DATO / INFERENZA / IPOTESI / ESPANSIONE. Promotion to canonical ONLY via COMMIT CANDIDATE.
> Lead status: open · maturing · promoted-to-CC · parked · refuted

## Index by pathway
- Myelin/glia · Metabolism/sphingolipids · Prenatal structure/GSK3β · GABA · Neuroinflammation · Cerebellar axis · Cross-pathway

---

## BIO — biomarker leads

### DL-BIO-001 — <short title>
- **Status**: open · **Tag**: IPOTESI · **Tier**: 1/2 (WWOX-linked) | 3 (distal)
- **Source**: paper_registry_current#PAPER NNN / PMID / DOI
- **What is measured**: <readout> · **Assay**: <method> · **Matrix**: blood/CSF/fibroblasts/imaging/EEG
- **Closeness to WWOX**: <how direct the signal is>
- **ABC map**: A=<WWOX /pathway> · B=<intermediate> · C=<this biomarker>
- **Reasoning chain**: <from [datum] → [step] → [lead]; tagged because [what is missing]>
- **Evidence**: supports=<…> · refutes=<…> · neutral/unknown=<…>
- **What would validate it**: <missing experiment/datum>
- **Case relevance**: <which test 1–4 passed> · **Interconnections**: (DL-MECH-0xx: strengthens/contradicts/extends)

## MOL — molecule / therapy leads

### DL-MOL-001 — <compound/target>
- **Status**: · **Tag**: · **Compound/target**: · **Pathway touched**:
- **Source**: · **Effect direction**: <corrects what, in which direction> · **Model**: cell/animal/human
- **ABC map**: A=… · B=… · C=<this molecule> · **Signature to reverse** (if avail.): ↑{genes} ↓{genes}
- **Causal statement**: <Subj —relation→ Obj> · **Belief**: low/medium/high
- **Reasoning chain** (anchor to figure/table/sentence): · **Evidence**: supports=… · refutes=… · neutral=…
- **Proposed experiment** (+ expected readout, feasible in the case context if possible): <…>
- **Transfer rationale to WWOX**: · **Novelty**: new | corroborates claim_registry_current#CLAIM NNN · **Case relevance**: · **Interconnections**:

## REPO — drug repurposing

### DL-REPO-001 — <drug>
- **Status**: · **Tag**: · **Drug**: · **Approved indication**: · **Target/pathway**:
- **Source**: · **ABC map**: A=… · B=<target/pathway> · C=<this drug> · **Signature to reverse** (if avail.): ↑{} ↓{}
- **Causal statement**: · **Belief**: low/medium/high · **Reasoning chain** (anchor): · **Evidence**: supports=… · refutes=… · neutral=…
- **Proposed experiment** (+ expected readout): · **Bridge to WWOX**: · **Known safety (pediatric if avail.)**:
- **Novelty**: new | corroborates CLAIM NNN · **Case relevance**: · **Interconnections**:

## MECH — mechanistic clues (needles in the haystack)

### DL-MECH-001 — <clue>
- **Status**: · **Tag**: · **Source** (anchor to figure/table/sentence): · **The clue**: <what you noticed>
- **ABC map** (if applicable): A=… · B=… · C=… · **Causal statement**: <Subj —relation→ Obj> · **Belief**: low/medium/high
- **Reasoning chain**: · **Why it might matter**: · **Possible next step**: · **Interconnections**:

---

## Learned heuristics (compounding the method)
> When a reasoning path works, distill it here as a line reusable by future sessions.
| ID | Heuristic | Born from |
|----|-----------|-----------|
| H-001 | <e.g. "fibroblast assays in Methods give the most solid BIO leads"> | DL-… |

## Next-search agenda (curriculum — ordered by expected gain)
| ID | Query/target | Perspective | Which lead it comes from | Priority | Status | Outcome |
|----|--------------|-------------|--------------------------|----------|--------|---------|
| NS-001 | <PubMed query or molecule/pathway/author> | metabolic/electrophysiology/genetic/structural/immuno/clinical/pharmacological | DL-... | high/medium/low | open/done | <papers found> |

## Process reflections (what works, dead ends)
| Date | Hop/paper | What gave the best leads | Dead end (do not reopen) | To do differently |
|------|-----------|--------------------------|--------------------------|-------------------|

## Discarded leads (so as not to re-evaluate them)
| Source | Lead | Why discarded |
|--------|------|---------------|

---

## Change-log
| Date | Action | Entry | Note |
|------|--------|-------|------|
| YYYY-MM-DD | created | DL-BIO-001 | from PAPER NNN |
```

---

## Numbering rules
- ID per type, zero-padded: `DL-BIO-001`, `DL-MOL-001`, `DL-REPO-001`, `DL-MECH-001`, `NS-001`.
- Never reuse an ID, even after `refuted` (it stays as history).
- Every append → one line in the change-log with an absolute date.
