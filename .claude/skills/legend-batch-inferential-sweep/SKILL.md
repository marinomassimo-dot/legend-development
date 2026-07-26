---
name: legend-batch-inferential-sweep
description: 'Mandatory inferential second-pass for LEGEND study batches after study-intake-triage: takes all records of a PubMed/Scholar/Zotero list or a triage report, retrieves PubMed metadata/abstracts when possible, classifies each study as canonical-candidate, discovery-only, safety-signal, repurposing-seed, endpoint/biomarker-seed or discard, retrieves PMC full text for the top ones when free, and produces a Markdown report that feeds legend-discovery and legend-hypothesis-forge. Use it when a batch has been deduplicated but must be squeezed for super-inference, new therapeutic routes, biomarkers, safety or repurposing even if many items are OUT_OF_SCOPE_LIKELY.'
---

# legend-batch-inferential-sweep

Second-pass after `legend-study-intake-triage`.

Purpose: prevent `OUT_OF_SCOPE_LIKELY` from meaning "never look at it". It means only "no immediate canonical deep-dive". Every batch is still squeezed for small signals of:
- WWOX mechanisms;
- biomarkers or endpoints;
- safety/BLOCK-1;
- drug repurposing;
- new research lines;
- non-canonical therapeutic hypotheses.

## When it activates

Inside the `legend` autopilot, activate it right after triage and before choosing the deep-dives.

Typical triggers:
- the operator provides a study list and asks to start;
- a `staging/study_intake_triage_*.md` report exists;
- the operator asks for "super-inference", "squeeze them all", "hypothesis forge", "repurposing", "look for new routes".

## Input

Accepts:
- raw PubMed/Scholar/Zotero text;
- a Markdown triage report;
- any file with PMIDs/DOIs/titles.

If a triage report already exists, use it: preserve the classes `KNOWN_INTEGRATED`, `CORPUS_CATALOGUED`, `IN_PIPELINE`, `NEW`, `OUT_OF_SCOPE_LIKELY`, `AMBIGUOUS`.

## Procedure

1. Run the script:

```bash
python3 .claude/skills/legend-batch-inferential-sweep/scripts/batch_inferential_sweep.py \
  --workspace . \
  --input staging/study_intake_triage_YYYYMMDD.md \
  --out staging/batch_inferential_sweep_YYYYMMDD.md \
  --fetch-pubmed \
  --pmc-dir staging/fulltext_pmc_YYYYMMDD
```

If `.claude/skills/legend-proband-priority-matrix/references/proband_priority_matrix.json` exists, the script applies it automatically and adds `proband_score`, `proband_priority_tier`, `proband_axes`, `proband_rationale`.

2. Read the generated report and choose:
- `P0_FAST_TRACK` / `P1_HIGH` tier -> review first, even if the paper is oncology/adult/canonically out-of-scope;
- `CANONICAL_CANDIDATE` -> `legend-deepdive` if it deserves a CC;
- `DISCOVERY_ONLY` -> `legend-discovery`, append to the discovery ledger;
- `REPURPOSING_SEED` -> `legend-hypothesis-forge`, then `legend-safety-triage` if a concrete molecule emerges;
- `SAFETY_SIGNAL` -> BLOCK-1 review; do not promote without verification;
- `ENDPOINT_SEED` -> endpoint/biomarker discussion, without confusing Tier 3 with a WWOX biomarker;
- `READ_QUEUE_TAIL` (formerly `DISCARD_LOW_SIGNAL`) -> **at the back of the reading queue, with tracked debt. NOT discarded, NOT closed.** No category of this skill authorizes not reading: see **parity of sources** in `CLAUDE.md`.

3. If leads emerge:
- update the discovery ledger with a few real needles;
- update/create the therapeutic hypothesis ledger with ranked hypotheses;
- use `legend-safety-triage` only for molecule candidates with a concrete SMILES/name.

## Rules

- Do not touch the 4 canonical scientific current files.
- Do not create claims from abstract-only.
- Do not treat the script's ranking as evidence: it is operational triage.
- PubMed metadata: use only `PubmedData/ArticleIdList`, not the references' DOI/PMCID.
- PMC full text only if open/free; no paywall/paid API.
- The sweep persists a `FULLTEXT_READ_RECEIPT` with `evidence_depth: queried_not_full_read` for every study whose full-text corpus is queried or sampled non-exhaustively. A PMC article that is only downloaded remains `retrieved_not_read`. Neither state removes reading debt or permits a complete receipt; only a downstream workflow that reads and records every applicable section may do that.
- Every insight tagged `DATO`, `INFERENZA`, `IPOTESI`, `ESPANSIONE`.

## Expected output

- Markdown report in `staging/batch_inferential_sweep_*.md`.
- Optional PMC full text in `staging/fulltext_pmc_*/`.
- Chat synthesis:
  - how many records analyzed;
  - top canonical candidates;
  - discovery-only leads;
  - safety/repurposing seeds;
  - what enters the ledgers;
  - **the residual reading debt** (what stays in the queue, not "what was discarded" — nothing is discarded).

## What NOT to do

- 🔴 **Do not down-rank a study because its disease context is not WOREE.** Oncology = **twenty years ahead** on WWOX mechanics (folding, stability, degradation, partners): the mechanism of the allele of interest lives **there**. Adult neurology = pathways/biomarkers/molecules already tested in humans. WOREE papers are the most consistent but largely **descriptive**: consistency ≠ usefulness. **Real cost of this error: 2026-07-12** — see the capability scout log (2026-07-12).
- 🔴 **Do not treat any category as a trash bin.** `READ_QUEUE_TAIL` and `OUT_OF_SCOPE_LIKELY` are **transient states**, never destinations.
- Do not use `OUT_OF_SCOPE_LIKELY` as a definitive discard.
- Do not launch heavy workshop repos out of mere curiosity.
- Do not run ADMET without a concrete molecule.
- Do not promote a molecule with a red flag to the therapeutic tracker.
