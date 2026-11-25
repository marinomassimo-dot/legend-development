# Pre-registration — which WWOX records rest on a cell line registered as misidentified or contaminated? (IT, 2026-11-25)

Asked: proposed by IT after a blind check found HO-8910 registered as a HeLa derivative; accepted by ADV the same day with five conditions. Hypothesis level; nothing here is medical advice.

**Disclosed order.** The Cellosaurus flat file (version 57.0, retrieved 2026-11-25, sha256 3b5a9fc56b49854230ae90fb7cee57a3bf9f961df98be215a634203526f476ef) was downloaded before this text was written. Only its header and the number of entries carrying a «Problematic cell line» comment (1391) had been read. Four lines had been looked up earlier in the day through the same register's interface (HO-8910, SGC-7901, BGC-823 flagged); they are known positives and do not count as predictions.

**Perimeter (fixed before counting).** Claim registry, paper registry, literature tracking log, working model; discovery, therapeutic-hypotheses, experiment and dismissal ledgers; `drug_repurposing/cards/*.card.json` and `cards_early/*.card.json`; `analysis/wwox_expression_boost_census_20260922.md`. Not in the perimeter: dossiers, session reports, other analysis files, held full texts. A line named only there is not counted.

**Census first, two routes, before any register look-up.**
* Route S (structured fields): card `context.cell_type` and `cellular_context`; paper registry `Model/species` and `Genotype/model`; literature log `Species`, `Model type`, `Genotype/model tag`.
* Route T (text search): the whole perimeter, tokens shaped like a cell-line name (letters with digits or hyphens) plus a written list of names without digits, kept only after reading their context.
Which tokens are cell lines is decided by hand, from their context, before the register is queried. Both counts are reported and the difference explained.

**Classes (never used to infer the sign of a finding).** (A) registered as a problematic line: misidentified or contaminated; (B) registered with a problematic-derivative or partial note that is not a plain misidentification; (C) not flagged; (U) not found in the register under that name. For A and B: record id, the exact comment, retrieval date.

**For each affected row:** state whether only the label changes (species, tissue, independence) or an inference changes (a replication or a tissue-specific statement that does not exist). Corrections are wording, not new reading. A blind second reader checks every pivotal line before it enters a record.

**Predictions.** P1: between 1 and 8 flagged lines are named in the perimeter. P2: none of them carries a statement about a neural WWOX-deficient system (inference at the core of the disease model unaffected). P3: at least one affected row is used as independent support for a direction.
