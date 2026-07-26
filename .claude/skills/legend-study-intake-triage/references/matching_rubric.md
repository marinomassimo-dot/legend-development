# Matching Rubric — legend-study-intake-triage

## Score

| Evidence | Score |
|---|---:|
| Same DOI / PMID / PMCID / preprint DOI | 100 |
| DOI missing but title normalized exact + year/author compatible | 92 |
| Title fuzzy >= 0.92 + same year + first author match | 88 |
| Title fuzzy >= 0.88 + year or first author compatible | 78 |
| Short-title/alias match only | 65 |
| Title fuzzy 0.75-0.87 without author/year | 55 |
| Weak lexical overlap only | <50 |

## Verdict thresholds

- `>=95`: exact duplicate / known.
- `88-94`: probable duplicate; verify metadata, especially preprint/published.
- `75-87`: ambiguous; resolve before processing.
- `<75`: likely new unless identifier says otherwise.

## Special cases

- Preprint -> published: classify as `KNOWN_METADATA_UPGRADE`.
- Same study in review + primary source: not duplicate; review can be background_only.
- Same cohort extended follow-up: not automatic duplicate; classify `AMBIGUOUS` until checked.
- Same title translated/capitalized/punctuation differences: normalized title exact.
- Multiple studies in one pasted row: `AGGREGATE_LINE`, split first.
- Missing identifiers but exact title in `full_text_queue_current.md`: `IN_PIPELINE`.

## Priority rubric for NEW items

Dedup score is not scientific priority.

After identifying `NEW`, rank by inferential value for the case, not by disease-label proximity:

| Priority signal | Why it can outrank descriptive WOREE papers |
|---|---|
| WWOX mechanism with actionable pathway | Can generate therapeutic hypotheses for the case even if discovered in cancer/adult tissue |
| Variant/domain/structure/folding data | Directly supports Q230P/chaperone/stabilizer reasoning |
| Neuroinflammation, microglia, GSK3b/tau, excitability, myelin/glia | Potentially maps to the case phenotype and endpoints |
| Molecule/peptide/drug/repurposing clue | Creates a testable therapeutic lead |
| Interactome/metabolism/stress response/proteostasis | Expands mechanism space beyond WOREE case descriptions |
| Direction promoted by trusted WWOX/WOREE groups or LEGEND discovery | Priorities evolve as the field and repo learn |
| WOREE/SCAR12 case series | High clinical relevance, but often phenotype/natural-history unless it adds mechanism or intervention |

Use these labels in shortlist notes:
- `MECHANISM_HIGH`
- `THERAPEUTIC_LEAD`
- `VARIANT_STRUCTURE`
- `NEURO_BRIDGE`
- `TRANSLATIONAL_BRIDGE`
- `PHENOTYPE_CONTEXT`
- `EVOLVING_PRIORITY`
- `BACKGROUND_LOW`

Never demote a WWOX oncology/adult-neuro paper solely because it is not pediatric WOREE. Demote only if it lacks a transferable mechanism, intervention, biomarker, or variant-relevant clue.

## Evolving priority sources

Boost a `NEW` item when it intersects a live priority direction. Current seed directions:

| Direction | Examples of signals |
|---|---|
| MYC/WNT | MYC, WNT, beta-catenin, Hippo cross-talk when tied to WWOX biology |
| Neuroinflammation | microglia, astrocytes, cytokines, ARDS/neuroimmune bridges, WWOX-inflammation tracks |
| Zfra/peptide biology | Zfra, WWOX7-21, WWOX7-11, peptide signaling, cytotoxic memory Z cells |
| Lithium/GSK3b | lithium, GSK3b/GSK3β, tau phosphorylation, Wnt/GSK3b axis |
| Proteostasis/chaperone | Q230P, misfolding, chaperone, stabilizer, proteostasis rescue, folding/stability |
| Splice rescue | c.1057-2A>G, splice acceptor, cryptic splice, SSO/ASO, exon definition |
| Internal LEGEND discovery | research candidates, discovery ledger, therapeutic strategies, wikilink clusters |

This list is not closed. Add directions when field evidence or LEGEND inference makes them important.
