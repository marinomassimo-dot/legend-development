# Clinical census — WOREE/WWOX, ClinicalTrials.gov API v2, 2026-10-20

Actor `plan` (Harness Engineering), task `PLAN-CLINICAL-CENSUS-20261020`. Produced by
`framework/scripts/clinical_census.py` (public ClinicalTrials.gov API v2, read-only, key-less,
standard library only, zero spend). Data file: [`clinical_census_20261020.json`](clinical_census_20261020.json);
original responses, one per query page, under `clinical_census_20261020_raw/` with each path
recorded inside the JSON. **Those stored responses are the registry's documents with personal
contact values (e-mail, phone, fax) replaced by `[REDACTED_CONTACT]` — 146 replacements across
the seven pages, each page's count recorded beside its path.** Every scientific field is
untouched; the files are declared redacted rather than byte-faithful, because this repository
is public material and `scripts/public_release_gate.py` blocks a live e-mail address in it. The
largest page (the broad `WWOX` query, ~4.8 MB) is stored gzipped at the recorded path. Public
disease-level record. **Nothing here is a scientific claim,
nothing here is `DATO`, and nothing here is medical advice.** This is a retrieval record: what
seven queries returned from one registry on one date.

## 1 · What each query returned

Seven queries, run separately, with no phase, masking, placebo or status pre-filter sent or
applied. Counts are the registry's own `totalCount` and the records collected.

| Query (synonym kept with the record) | Field | State | Collected / registry total |
|---|---|---|---|
| WOREE | `query.term` | MATCH | 1 / 1 |
| WWOX-related epileptic encephalopathy | `query.term` | MATCH | 1 / 1 |
| EIEE28 | `query.term` | MATCH | 1 / 1 |
| DEE28 | `query.term` | NO_MATCH | 0 / 0 |
| WWOX | `query.term` | MATCH | 83 / 83 |
| MZ-9138 | `query.term` | NO_MATCH | 0 / 0 |
| Mahzi Therapeutics (sponsor of CIRM `CLIN1-14825`) | `query.spons` | MATCH | 1 / 1 |

84 distinct identifiers after deduplication. No query ended `QUERY_ERROR` or
`COVERAGE_INCOMPLETE`; every query exhausted its pagination.

Three measured observations about the records themselves, with no interpretation added:

- The four synonym-driven matches (WOREE, the spelled-out name, EIEE28, and the single
  overlapping record of the broad WWOX query) are the **same one identifier**, `NCT01793168` —
  an observational rare-disease registry and natural-history study (Sanford Health, recruiting,
  no phase, first posted 2013-02-15, last update posted 2025-05-29) whose condition list
  carries many disorders. It is not an interventional study of a WWOX-directed therapy.
- Of the 83 records returned by the free-text `WWOX` query, **1 contains the literal string
  `WWOX`** anywhere in its returned record; the other 82 were reached by the registry's own
  text expansion and none of them was returned by any WOREE-specific synonym. Their presence
  in the answer says nothing about their relation to WWOX, and this census asserts nothing
  about them.
- The sponsor query returned one Mahzi Therapeutics record, `NCT07135050`: a phase 1/2 AAV9
  gene-therapy study by intracerebroventricular injection, **condition Pitt Hopkins Syndrome**,
  intervention MZ-1866, recruiting, first posted 2025-08-21, start date 2025-12-19. It is a
  different candidate and a different indication from MZ-9138/WOREE; it is recorded here
  because the sponsor query returned it, not because it bears on WOREE.

## 2 · What a missing hit does and does not establish

- **A missing hit does not prove that no study exists.** `NO_MATCH` is an answer about one
  query against one registry on one date. A study may be unregistered, registered under
  wording none of these seven synonyms reaches, registered in a non-NLM registry, or
  registered after 2026-10-20.
- **`COVERAGE_INCOMPLETE` is not `NO_MATCH`**, and the connector keeps the two apart precisely
  so a partial retrieval can never be read as an absence. Likewise `QUERY_ERROR`: a query that
  did not complete returns no information about existence at all.
- **An NCT number proves neither recruitment nor first dosing.** It evidences registration, on
  the date the registry shows, and nothing further. A registry record is also not an IND
  authorisation and not a therapeutic approval; ClinicalTrials.gov is NLM/NIH, not an FDA
  archive.

## 3 · MZ-9138 — events kept separate, unverified ones UNKNOWN

Six events are distinct and are never collapsed into one another. Only the registry rows above
were observed in this run; the rest of this table is `UNKNOWN` by design, not by oversight.

| Event | State after this run | Basis |
|---|---|---|
| Programme active | OBSERVED (grant level) | CIRM award `CLIN1-14825`, "Development of a Gene Therapy for the Treatment of WWOX related epileptic encephalopathy (WOREE)", PI Dr. Yael Weiss, Mahzi Therapeutics, award status *Active*, read 2026-10-20 from the public CIRM award page |
| Sponsor-declared authorisation (e.g. an IND cleared) | UNKNOWN | not observed in this retrieval |
| Public regulatory confirmation | UNKNOWN | not observed; **absence of a public document is not evidence against an authorisation** — an IND need not be publicly exposed, and no public FDA document is required as the only admissible proof |
| Registration of a WOREE/MZ-9138 study | UNKNOWN (no such registry record returned) | `MZ-9138` → `NO_MATCH`; the one Mahzi sponsor record is MZ-1866 / Pitt Hopkins |
| Enrolment | UNKNOWN | not observed |
| First dose | UNKNOWN | not observed |

The CIRM page's **"Project Objective: Phase 1-2 trial initiated"** is an objective of the
award, listed beside proposed activities that are preclinical and start-up (GLP studies in
mouse and non-human primate, cGMP manufacture, phase 1–2 start-up, initiation of a natural
history study). It is **not** a completed-milestone report, and no access timing may be
estimated from it.

## 4 · Repeating this

```bash
python3 framework/scripts/clinical_census.py --list-queries        # no network call
python3 framework/scripts/clinical_census.py \
  --out disease-models/wwox/research/drug_repurposing/clinical_census_<YYYYMMDD>.json \
  --raw-dir disease-models/wwox/research/drug_repurposing/clinical_census_<YYYYMMDD>_raw
```

Exit codes: `0` every query terminal (MATCH/NO_MATCH), `1` at least one `QUERY_ERROR`,
`3` at least one `COVERAGE_INCOMPLETE`. Offline regressions:
`python3 framework/scripts/test_clinical_census.py` (21 assertions covering the seven separate
queries, the absence of any pre-filter, the four states, pagination, deduplication with the
finding synonym kept, the contact redaction, and provenance including the original-response
path).

Counts in § 1 are what the registry returned on 2026-10-20; a later run may legitimately
differ, and that is why none of them is pinned in a test.
