---
name: legend-study-intake-triage
description: Mandatory bibliographic triage at session start when the operator provides one or many studies to analyze. Normalizes small or massive lists (1, 500, thousands of records), splits aggregated lines, dedups against the paper registry, literature tracking log, inbox, full-text queue and commit queue, disambiguates DOI/PMID/titles/authors/year/preprint-vs-published, and returns what is already analyzed, already in pipeline, new, ambiguous or to verify before any deep-dive. Always use it before legend-ingest, fulltext-dossier or legend-deepdive when a list of papers/studies/sources arrives, even if the user does not name it.
---

# legend-study-intake-triage — Study dedup and disambiguation

## Purpose

Avoid wasting tokens, time and energy on studies already processed or already in pipeline.

This skill is the **first gate** when the operator provides studies to analyze:

`raw study list -> normalize -> retraction check -> match -> triage -> only new/ambiguous pass to INGEST`

It works with a single study or with massive lists. It produces no scientific claims.

## 🛑 Retraction gate (mandatory, before assigning any tier)

A **retracted** paper must never be ranked as `CANONICAL_CANDIDATE` nor enter a claim. Keyword ranking is blind to retractions: in the 2026-07-09 run the sweep ranked **P1_HIGH / CANONICAL_CANDIDATE** a paper retracted for western-blot manipulation (PMID 26041563). The registry had correctly confined it, but the upstream gate had not seen it.

```bash
python3 .claude/skills/legend-study-intake-triage/scripts/retraction_check.py \
  --pmids <list> | --file <pmids.txt>
```

- `exit=2` → at least one paper is **RETRACTED** or has an **Expression of Concern**.
- Every flagged paper: force to `archived` / exclude from `CANONICAL_CANDIDATE`, **never** rank it high, and note it in the inbox as a `retraction signal`.
- If an author group has serial retractions, note it in the research-group knowledge base (credibility watchlist).

## Priority principle: inferential potential for the case

Do not order studies by nominal proximity to WOREE/SCAR12 alone.

WOREE/SCAR12 studies are clinically close to the case, but are often case reports or descriptive series with few children. They matter for phenotype, natural history and clinical comparison, but do not exhaust the useful research.

For real therapeutic inference you need critical mass from the whole WWOX corpus and from the mechanistic bridges:
- WWOX/FRA16D oncology, for stress response, apoptosis, p73/p53, EMT, metabolism, interactome, genomic fragility;
- adult neuro/Alzheimer/tau/GSK3b, for neuroinflammation, microglia, excitability, degeneration, circuits;
- metabolism, hypoxia/HIF1A, mitochondria, glia/myelin, proteostasis;
- Zfra/peptides, lithium/GSK3b, proteostasis rescue, chaperones/stabilizers, drug repurposing;
- rare disease/genotype-to-drug even if not WOREE, when the workflow is transferable to the case.

Guiding question for each study:

`Is there a useful lead for the specific case, given phenotype and alleles, even if the paper comes from cancer, Alzheimer, adult-neuro or another disease?`

So the triage must separate duplicates and noise, but must not automatically penalize oncology or adult neurology. A WWOX oncology paper can be a priority if it contains an actionable mechanism, a target, a pathway, a molecule, a peptide, a biomarker or a repurposing logic.

## Evolutionary priorities

Priorities are not static. They must change when new credible directions emerge from the WOREE/WWOX community or from the LEGEND repo.

Sources that can raise a direction to active priority:
- WWOX/WOREE groups opening a pharmacological or mechanistic route (e.g. MYC/WNT, neuroinflammation, Zfra/peptides, lithium/GSK3b);
- new LEGEND research candidates, claims, discoveries, inbox items, therapeutic strategies or wikilinks;
- convergence of multiple independent lines, even if from oncology, Alzheimer, adult-neuro, metabolism or non-WOREE rare disease;
- a direction that becomes testable on the case: alleles, phenotype, biomarkers, fibroblasts/LCL/iPSC/organoids, pediatric safety.

Every shortlist must therefore apply two levels:
1. **inferential baseline**: mechanism/therapy/variant/translation;
2. **evolutionary boost**: directions currently hot for LEGEND or for authoritative WWOX research.

If a new priority direction emerges, update the skill or the operational log; do not wait for a general rewrite.

## Mandatory automatic use

If the session input contains one or more studies, papers, PMIDs, DOIs, titles, bibliographies, PubMed/Scholar/Zotero/CSV exports, or mixed bibliographic lines:

1. activate this skill before `legend-ingest`, `find-fulltext`, `fulltext-dossier`, `legend-deepdive`;
2. do not analyze papers until a `KNOWN / IN_PIPELINE / NEW / AMBIGUOUS` verdict exists;
3. pass only `NEW` and `AMBIGUOUS_RESOLVED_NEW` to the pipeline.

## Comparison sources

Read/index:
- the paper registry
- the literature tracking log
- the inbox
- `disease-models/wwox/research/full_text_queue_current.md`
- the commit-candidate log

Optional, if needed:
- the discovery ledger
- `disease-models/wwox/analysis/README.md`
- the external workshop manifest (`_external_repos/MANIFEST.md`)

## Output classes

- `KNOWN_INTEGRATED`: already in the paper registry or the literature log with status processed/integrated/claim_linked/background_only.
- `KNOWN_METADATA_UPGRADE`: same paper but a new form (preprint -> published, new DOI/PMID, full-text upgrade).
- `IN_PIPELINE`: already in inbox, full-text queue, commit queue or deep-dive pending.
- `NEW`: no robust match.
- `AMBIGUOUS`: possible title/author/year match but not strong enough.
- `AGGREGATE_LINE`: one line contains multiple studies and must be split.
- `INSUFFICIENT_METADATA`: too little material to decide.
- `OUT_OF_SCOPE_LIKELY`: not WWOX/bridge, but only after a minimum check.

`OUT_OF_SCOPE_LIKELY` does not mean "not useful because it is oncology/adult/non-WOREE". It means only: no WWOX/WOREE/case signal and no obvious mechanistic or therapeutic bridge in the title/citation. Keep it recoverable.

## Matching hierarchy

1. **Identifier exact:** PMID, PMCID, DOI, bioRxiv/medRxiv DOI, arXiv/preprint ID.
2. **Published/preprint bridge:** same title/authors with a new DOI; do not create a new paper without verification.
3. **Title normalized exact:** lowercase, no punctuation, light stopword, unicode normalized.
4. **Title fuzzy + year + first author:** high similarity and at least one bibliographic constraint.
5. **Short title / known alias:** match against short title, notes, queued items.
6. **Aggregated/corrupted lines:** split and repeat.

Rule: identifier exact wins; fuzzy title is not enough to declare a definitive duplicate if year/author is missing.

## Procedure

### 1. Normalize input

Accepts:
- free lines pasted in chat;
- PMID/DOI one-per-line;
- numbered/bulleted lists;
- CSV/TSV/Zotero/PubMed export;
- lines with multiple papers separated by `;`, `|`, `PMID:`, `doi:`, repeated numbering.

If the list is huge, write it first to `staging/study_intake_raw_<date>.txt` and work from the file.

### 2. Run the local script

Use the bundled script:

```bash
python3 .claude/skills/legend-study-intake-triage/scripts/study_dedup_triage.py \
  --workspace . \
  --input staging/study_intake_raw_YYYYMMDD.txt \
  --out staging/study_intake_triage_YYYYMMDD.md
```

The script is stdlib-only: it indexes the Markdown registries and does DOI/PMID/fuzzy-title matching.

### 3. Targeted manual disambiguation

For each `AMBIGUOUS`:
- search DOI/PMID in the original text;
- compare first author, year, journal;
- if needed use PubMed/Crossref/web to resolve identity;
- do not deep-dive before resolution.

### 4. Output

Return:

| Class | Count | Action |
|---|---:|---|
| KNOWN_INTEGRATED | n | skip / optionally note metadata |
| KNOWN_METADATA_UPGRADE | n | ingest metadata-upgrade, not a new paper |
| IN_PIPELINE | n | skip or update status |
| NEW | n | proceed to legend-ingest |
| AMBIGUOUS | n | resolve first |
| AGGREGATE_LINE | n | split and repeat |
| INSUFFICIENT_METADATA | n | ask for DOI/PMID/title |

Then the operational list:
- **SKIP**
- **METADATA-UPGRADE**
- **ALREADY-IN-PIPELINE**
- **INGEST-NOW**
- **NEEDS-DISAMBIGUATION**
- **NEEDS-METADATA**

When a shortlist of the `NEW` is needed, use inferential categories, not nosological hierarchy:
- **CASE-ACTIONABLE-MECHANISM**: pathway, protein, domain, interactome, GSK3b/tau, p73/p53, HIF1A, metabolism, glia/myelin, microglia, neuroinflammation, excitability.
- **THERAPEUTIC-LEAD**: molecule, peptide, chaperone, lithium/GSK3b, proteostasis rescue, gene/RNA therapy, drug repurposing.
- **VARIANT/STRUCTURE**: WW/SDR domains, PPxY, folding, stability, allostery, variant effect.
- **PHENOTYPE/NATURAL-HISTORY**: WOREE/SCAR12/case series/DEE, useful but often descriptive.
- **TRANSLATIONAL-BRIDGE**: cancer/adult-neuro/Alzheimer/metabolism paper with a transferable mechanism.
- **BACKGROUND-LOWER**: WWOX context without a new mechanism or clear actionability.
- **EVOLVING-PRIORITY**: a direction LEGEND or WWOX/WOREE groups have made a priority over time, e.g. MYC/WNT, neuroinflammation, Zfra/peptides, lithium/GSK3b, Q230P proteostasis, splice rescue c.1057-2A>G.

Ranking rule: high priority if it increases the testable hypotheses for the case or opens a therapeutic lever, even if it does not mention WOREE.

## Writing

READ-ONLY toward the canonical current files and registries.

Writable:
- `staging/study_intake_raw_*.txt`
- `staging/study_intake_triage_*.md`
- optionally append to a `study_intake_triage_log.md` if the operator wants a historical audit.

Do not create inbox entries automatically: after the report, `legend-ingest` handles only the new ones.

## What NOT to do

- Do not deep-dive before dedup.
- Do not create a new PAPER for a published version of an already-registered preprint.
- Do not treat a fuzzy match as certainty if author/year is missing.
- Do not ignore the full-text queue and inbox: "not integrated" does not mean "new".
- Do not waste web lookups on thousands of records: local batch first, then web only on the ambiguous ones.
