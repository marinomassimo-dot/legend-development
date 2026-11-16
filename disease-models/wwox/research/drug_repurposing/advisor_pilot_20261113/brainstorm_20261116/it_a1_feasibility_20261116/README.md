# IT feasibility census of the A1 series, 2026-11-16 (counts only; non-canonical; not medical advice)

Written for: ADV and the predictor sessions of the 2026-11-16 brainstorm. Reference genotype class only. No outcome direction, no per-agent outcome and no recommendation is in this folder; `census.tsv` holds counts and nothing else.

Source: `batch_sci_20261105/a1_wwox_reports/cases_a1.tsv` (57 rows, 12 reports), read by script on 2026-11-16. Counts are rows with distinct (report, case label); links marked "possible" in `same_patient_as` are NOT merged, so every child count is an upper bound (de-duplicated per-report counts are in `denominators_a1.tsv`). A grouped row (for example "3 pts") counts as one.

## Findings that decide feasibility
1. A1 codes five intervention classes only: vigabatrin (GABA-AT), hormonal (steroid/ACTH), ketogenic diet, cannabidiol and a residual `other_context`. Sodium-channel, valproate-type, benzodiazepine/GABA-A, carbonic-anhydrase/multi-target and SV2A agents appear only as free text in `co_therapy_stated` or in quotes (mention counts in `census.tsv`), with **no outcome attributable to them**. Those classes are **not scorable from A1**; scoring them would need a new extraction from the source reports, which is a different task and not a census.
2. Class-level scoring is possible only for the seizure endpoint of the four coded classes (stated outcome in 11, 8, 8 and 4 children) and for the development endpoint of GABA-AT (5) and steroid/ACTH (3). Ketogenic diet (2) and cannabidiol (1) are **not scorable** on development (fewer than 3).
3. Worsening: the outcome vocabulary of A1 has no worsening value, and a keyword scan of the co-therapy, quote, status and outcome fields found no worsening wording (worse, aggravat, exacerbat, deteriorat, more frequent, increased seizures). That is a count of zero **in fields not designed to record it**; unknown is not negative. The only adverse statement near this question is an imaging change after vigabatrin in two children (PMID 41442931, rows A1-09 and A1-10, abstract level); it is not a seizure worsening.
4. Not blind by construction: `cases_a1.tsv` is a public table in the repository and carries every outcome of the four coded classes. The predictor can read it; I cannot seal it. For these classes the score tests prediction against a table the predictor could have opened; it counts only if the predictor commits the ranking before opening it and says so. The three IT31 agents and the A1 table were seen by IT before this census.
5. Direction table: none exists in this folder, and none is made now. If the predictor freezes, the per-class direction cells will be produced after the freeze commit hash, from `cases_a1.tsv`, by a blind extractor.

## Limits
One reader (IT), script plus table, no new reading of any report; classes follow the A1 coding and ADV's list, not an independent pharmacological classification; the scan of worsening words covers four fields only.
