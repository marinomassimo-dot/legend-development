# IT18 P4 controls — popularity and construction leakage (pre-registration, 2026-11-01)

Dated addition to `../` (the IT18 P4 matching comparison). Written and committed before `controls.py` existed or ran. Non-canonical research material; not medical advice; pharmacological compatibility only. Public edition, WWOX-DEE genotype class. The locked P4 files (`answers.tsv`, `answers_lock.json`, `priors.tsv`, results and pre-registrations) are read, never written.

## Why these two controls and not the others

The task list for this package named five controls (popularity, near-equivalent disease in the inputs, answer leakage through therapeutic labels or literature, same candidate universe and same treatment of missing pairs and abstentions, shared-source dependence). P4 already satisfies three by design: one universe for T, X and L (`answers.tsv` holds every path's label on every row), unknown references kept unknown and abstentions reported with reasons, and a shared-PubMed-id check between ChEMBL and GtoPdb with the shared-literature caveat stated. Two are missing: **popularity** and **construction leakage** (including the near-equivalent-disease shortcut). Only those two are run.

## Declared prior knowledge

The EVAL reference has already been read (P4 runs 1 and 3): 2 of 33 EVAL directed rows are determinate (tezampanel, amantadine), both compatible. This control is therefore **post hoc on EVAL** and descriptive. It changes no label, rescues no decision, and the P4 decision stays as registered. It reuses `matching_task.py` functions unchanged to rebuild the universe and the reference for DEV and EVAL. The author knows, before running, that `NEED-T-TYPE-CALCIUM` is labelled after an ethosuximide experiment.

## C1 — popularity

Popularity of a parent compound: `pop` = number of distinct human gene symbols carrying a `DGIdb interaction` record over every catalogue entry whose parent is that compound (catalogue as committed; DGIdb cache of 2026-10-27). Secondary: `pop_atc` = distinct ATC level-5 codes over the same entries (a multi-indication proxy; the catalogue holds no indication table, so OREVID's "number of diseases already treated" cannot be computed and is not imitated). Percentile of `pop` among all catalogue parents with at least one DGIdb gene.

Measured on the 76 directed (need, compound) rows, DEV and EVAL, labels from the locked `answers.tsv` (L v1, the registered rule):

- (a) median `pop` percentile of L-compatible rows, of the whole T set, and of L-non-compatible rows.
- (b) popularity-only path **P**: per directed need, the k most popular T candidates, k = the number of L-compatible rows on that need (ties by lowest sha256 of the parent id). Report Jaccard(P, L-compatible) per need and pooled, and P's precision on rows with a determinate reference, beside L's and T's.
- (c) reference-coverage bias: Mann-Whitney AUC of `pop` for determinate-reference rows against the rest (DEV + EVAL directed rows), with the number of determinate rows.

Decision rules, fixed now:
- "L selects popular compounds beyond T" only if the median percentile of L-compatible exceeds that of T by at least 10 points; otherwise "L adds no popularity selection over T".
- "The scoreable set is the popular end of the candidates" only if the AUC in (c) is at least 0.70 on at least 5 determinate rows; then any reference-scored P4 figure is stated as not transferring to the less-studied candidates. Otherwise "no popularity bias of the reference measured at this denominator".
- P's precision is reported; if all determinate rows are compatible, write that popularity and L cannot be discriminated by this reference, which is not a result in favour of either.

## C2 — construction leakage and near-equivalent disease

- **Leakage.** A directed row is *leaked* when the compound's name or one of its catalogue synonyms (case-insensitive, whole-word, at least 4 characters) occurs in the need's own record in `needs/needs.json` — the text from which L takes its direction. Report the leaked rows, their L labels and reference category, and L's compatible precision on determinate rows with leaked rows excluded.
- **Near-equivalent disease.** A directed row carries the *indication shortcut* when its compound has an ATC code under N03 (antiepileptics): a lookup of existing seizure indications would put it forward without any WWOX input. Report the count among L-compatible rows per need.
- Rule: if any determinate row is leaked, write that the reference-scored figure contains a circular row and give the figure without it. Otherwise report the leakage as a construction fact that the reference cannot see.

## Outputs

`controls.py` (stdlib, safe `--help`), `test_controls.py` (unittest, verbosity 2), `controls_result.json`. Zero network calls; raw third-party files stay in the gitignored cache.
