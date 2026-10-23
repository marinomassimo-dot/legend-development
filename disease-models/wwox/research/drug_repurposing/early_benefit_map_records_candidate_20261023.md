# Candidate map records so the join sees the early-benefit axis — 2026-10-23

Actor `scientist-d`, task `MODULE-D-20261023`. **A candidate file, not an edit:** nothing here is in
`analysis/mechanism_intervention_map.md`, and nothing here is a candidate recommendation. Every record
below is `IPOTESI`-grade, carries no dose, no suitability statement, no score and no rank, and is not
medical advice. Adjacent sources are NOT WWOX EVIDENCE unless a record id says otherwise. No paper was
read for this file: each field is copied from a card in `cards_early/` or from a registry record
named in it.

## What the join can read in a record (`repurposing_join.mechanism_queries`)

A record is `### R-nn — <candidate> (...)` or `### N-nn — ...`; the candidate NAME is the heading up to
the first bracket or arrow; the fields are `| **NAME** | value |` rows; every `CLAIM nnn`, `DL-XXX-nnn`
and `PAPER nnn` token anywhere in the record body is a route to papers. Only R- and N- records produce a
card. An id in the body is the whole fix.

## Records proposed (three new, three existing receive one row each)

### New records — placed after R-09, in the map's own table form

```
### R-10 — Ethosuximide (T-type calcium-channel blocker; class contrast, DL-MECH-170)

| Field | Value |
|---|---|
| **INTERVENTION** | ethosuximide, as a T-type calcium-channel blocker contrast |
| **TARGET** | T-type calcium channel (CACNA1G / CACNA1H / CACNA1I family) |
| **MECHANISM** | a T-type blocker suppressed a provoked seizure genotype-specifically in one mouse experiment; the drug-by-genotype interaction was not tested |
| **DECISIVE_PRECLINICAL_TEST** | late-phase PTZ-provoked behavioural seizure score in a three-genotype design with an explicit drug-by-genotype interaction test and a concurrent same-day PTZ-alone control |
| **EARLY_BENEFIT_ENDPOINT** | late-phase PTZ-provoked seizure score (preclinical; no human endpoint is defined) |
| **SOURCE_IDS** | DL-MECH-170, DL-MECH-171, DL-MECH-172, CLAIM 016, PAPER 019 |

### R-11 — Cannabidiol (class level)

| Field | Value |
|---|---|
| **INTERVENTION** | cannabidiol, class level |
| **TARGET** | UNKNOWN (no WWOX-system test of the class exists in the repository) |
| **MECHANISM** | UNKNOWN |
| **DECISIVE_PRECLINICAL_TEST** | none can be named until a response is first defined (see the card) |
| **EARLY_BENEFIT_ENDPOINT** | clinician-reported seizure control, if a response is first defined |
| **SOURCE_IDS** | PAPER 189 |

### R-12 — ACTH, corticosteroids and phenobarbital-containing regimens (class level)

| Field | Value |
|---|---|
| **INTERVENTION** | hormonal and phenobarbital-containing regimens, class level |
| **TARGET** | UNKNOWN |
| **MECHANISM** | UNKNOWN |
| **DECISIVE_PRECLINICAL_TEST** | none: the open datum is a matched West-syndrome base rate and a comparator, which is a reading and a cohort question, not a bench one |
| **EARLY_BENEFIT_ENDPOINT** | clinical cessation of epileptic spasms, if and only if a comparator separates a WWOX-genotype response from ordinary West-syndrome pharmacology |
| **SOURCE_IDS** | DL-MECH-134, DL-THER-106, CLAIM 001 |
```

### One row added to three existing records (so the endpoint each card pursues is on the record)

| Existing record | Row to add | Card it pairs with |
|---|---|---|
| `R-05` Ketogenic diet | `\| **EARLY_BENEFIT_ENDPOINT** \| clinician-reported seizure control, symptomatic only \|` | `EB-KD-01` |
| `N-04` Broad GABAergic push (vigabatrin) | `\| **EARLY_BENEFIT_ENDPOINT** \| clinical cessation of epileptic spasms with a stated criterion; the exposure limit (MRI abnormality) sits on the same record \|` (N-04 is prose; the line is `**Early-benefit endpoint:** ...`) | `EB-VGB-01` |
| `N-01` mTOR inhibitors | `**Early-benefit endpoint:** none supported for this class` | `EB-MTOR-AX-01` |

The join does not read `EARLY_BENEFIT_ENDPOINT`. It is proposed because it is where a reader and the next
Scientist find the endpoint, and because a one-line change to `mechanism_queries` (`target` and
`decisive_test` are read the same way) would carry it into the derived card's `p4_fields.endpoint_pursued`
instead of `UNKNOWN`. That change is optional and is not part of the minimum below.

## Which existing queries each record sits beside

| Card in `cards_early/` | Map record | Existing query it sits beside | What the join does today |
|---|---|---|---|
| `EB-KD-01` | `R-05` (exists) | `Q-R-05`; also `Q-CLAIM042`, `Q-DL-MECH-121`, guard `Q-N-15` | abstains, 0 papers (record cites by description) |
| `EB-VGB-01` | `N-04` (exists) | `Q-N-04`; also `Q-CLAIM001`, `Q-DL-MECH-038`, guard `Q-N-15` | abstains, 0 papers |
| `EB-MTOR-AX-01` | `N-01` (exists) | `Q-N-01`; the calcium-axis neighbour is none | abstains, 0 papers |
| `EB-ETX-01` | `R-10` (new) | `Q-DL-MECH-170` (20 papers, no card because a lead has no candidate name), `Q-DL-MECH-171`, `Q-DL-MECH-172`; differential `Q-N-03` (sodium-channel blockers) | a lead query exists and yields no card |
| `EB-CBD-AX-01` | `R-11` (new) | none (`Q-` text contains no cannabidiol) | nothing |
| `EB-HORM-AX-01` | `R-12` (new) | `Q-DL-MECH-134`, `Q-DL-THER-106`, `Q-CLAIM001` | leads and a claim exist, no card |
| `EB-GROWTH-AX-01`, `EB-DEV-AX-01`, `EB-PDANCHOR-AX-01` | **none, on purpose** | `Q-DL-MECH-140`, `Q-CLAIM036`; `Q-N-15`, `Q-DL-MECH-039`; `Q-CLAIM046` | an endpoint is not an intervention; the join's candidate universe is interventions |

## The axis row (one line of data in `AXES`, no code)

```
"early_benefit": ["vigabatrin", "ketogenic", "ethosuximide", "cannabidiol", "ACTH", "corticosteroid",
                  "epileptic spasm", "seizure control", "early benefit"],
```

Measured on the 2026-10-23 query set with the join's own filter (case-insensitive substring over the
serialised query), the nine terms select 10 of 332 queries today: `Q-CLAIM001`, `Q-CLAIM031`,
`Q-CLAIM042`, `Q-DL-MECH-038`, `Q-DL-MECH-121`, `Q-DL-MECH-134`, `Q-DL-MECH-170`, `Q-N-04`, `Q-N-15`,
`Q-R-05`. Four terms (`cannabidiol`, `corticosteroid`, `epileptic spasm`, `early benefit`) select
nothing today and would select `R-11` and `R-12` once those records exist. `growth` is deliberately not a
term: it matches pathograph lines about body weight, not the growth endpoint of `EB-GROWTH-AX-01`.
`Q-N-01` (mTOR) is not selected by these terms; it is already inside the `wnt` axis through `mTOR`.

## What the three new records would resolve to (checked with the join's own parsers, not run live)

Candidate map text = the current map plus the code block above. Papers reached through the named ids,
using the 2026-10-23 query table: `R-10` 21 papers (the three T-type leads and `CLAIM 016`; `PAPER 019`
is inside them), `R-11` 1 paper (`PAPER 189`, a cohort table row, not a cannabidiol study in a WWOX
system), `R-12` 14 papers. The join would derive three new cards, each with `NO_DRUG_ASSERTIONS_SUPPLIED`
like every derived card; their value is the evidence-depth table and the audit status, not an assertion.
The ids were taken from `cards_early/*.packet.json` and from `registry_records.py get --theme`; whether
`PAPER 189` is the right and only source for `R-11` is a reading question this file does not settle.
