# TS-02: clinical-trial census re-run (map row `TS-02`), 2026-11-05

Non-canonical research record, a retrieval record and not a scientific claim. Not medical advice. Zero spend; the public ClinicalTrials.gov API v2 was queried through the repository's own tool, key-less, with no contact parameter.

## What was run

`python3 framework/scripts/clinical_census.py --out <scratch>/census_now.json --raw-dir <scratch>/raw` on 2026-11-05 at 23:26:58 UTC, with the default query set (seven queries). The output and the original responses were kept in the session scratch directory, outside the repository; the earlier census of 2026-10-20 (`the 2026-10-20 trial-registry census file`, retrieved 2026-10-20 at 21:03 UTC) was left untouched and is the comparator.

## Result

| Query | State on 2026-10-20 | State on 2026-11-05 |
|---|---|---|
| DEE28 | NO_MATCH | NO_MATCH |
| EIEE28 | MATCH | MATCH |
| MZ-9138 | NO_MATCH | NO_MATCH |
| WOREE | MATCH | MATCH |
| WWOX | MATCH | MATCH (83 collected) |
| WWOX-related epileptic encephalopathy | MATCH | MATCH |
| sponsor:Mahzi Therapeutics | MATCH | MATCH (1 collected) |

* DATO: both runs hold the same **84 distinct registry identifiers**; the set difference is empty in both directions. No study was registered, withdrawn or re-identified within these seven queries between the two dates.
* The interpretation limits of the 2026-10-20 census stand unchanged: `NO_MATCH` means a query returned zero records on that date and does not establish that no study exists; an identifier evidences registration only, not sponsor authorisation, enrolment or a first dose; a matching record is not an interventional study of the disease (the WWOX query returns mostly records that mention the gene for other reasons, which the 2026-10-20 filters and reading separated).
* Consequence for the module: the clinical-context flags that cite the 2026-10-20 census need no change; the statement "no registered WOREE interventional study on that registry on that date" can be re-dated to 2026-11-05 by the integrator if wanted, with this file as the source. Nothing was re-read at the record level in this pass: only the identifier set and the per-query states were compared.

## Not done

No record-level comparison of status fields (recruitment status changes inside an unchanged identifier set were not examined). The scripts' raw responses are not copied into the repository (they carry redacted contact values and are third-party bytes).
