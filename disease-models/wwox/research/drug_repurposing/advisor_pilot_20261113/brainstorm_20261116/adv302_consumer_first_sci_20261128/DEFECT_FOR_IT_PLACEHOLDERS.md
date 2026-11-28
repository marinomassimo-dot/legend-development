# For IT: claim lines that cite registry placeholders with no identifier (noticed in ADV-302 step 1; not repaired)

SCI, window 64fc909a, 2026-11-28. Registry route is IT's. Hypothesis level; not medical advice.

Six `CORPUS P###` records carry `Identifier: PENDING` and are cited by their corpus number. Neither consumer count of ADV-302 (identifiers: PMID, DOI, PMC id, `PAPER NNN`) can see them.

| record | claim link in its entry | cited at (file under `disease-models/wwox/`, line) |
|---|---|---|
| CORPUS P191 | CLAIM 025 | registries/claim_registry_current.md 525, 526 |
| CORPUS P204 | CLAIM 024 | registries/claim_registry_current.md 508; research/discovery_ledger_current.md 1629 |
| CORPUS P207 | CLAIM 028 | registries/claim_registry_current.md 7, 577 |
| CORPUS P214 | CLAIM 027 | registries/claim_registry_current.md 560, 577 |
| CORPUS P216 | CLAIM 022 | registries/claim_registry_current.md 470 |
| CORPUS P218 | CLAIM 028 | registries/claim_registry_current.md 577 |

Each entry says "deep-dived"; none gives title, author, year or identifier in the entry itself, so the source cannot be re-opened from it. CORPUS P214 already carries an IT note of ADV-297 on this. Also: `research/discovery_ledger_current.md` 506 names CORPUS P396 (PMID 23566416) by corpus number only, as a caution.
