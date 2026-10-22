# COMMIT CANDIDATE — CC-20261021-SCIENTISTD-R4-REGISTRY-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist-d`, ten-hour repurposing batch `ORCH-REPURPOSING-10H-20261021`, group R4, branch `task/repurp-r4-d`.
**target_wm_version:** `WM_v7.20_2026-10-04` · **Change class:** MINOR (additive PAPER/LIT identity records for 22 staged receipts; no claim status, no working-model block and no baseline changes).
**Not medical advice. NOT WWOX EVIDENCE for any row below.** Every row is a comparator trial, protocol, natural-history study or review in another disease; class-level statements only.

## Target and need
The 22 staged receipts under `disease-models/wwox/research/receipt_staging/scientist-d/` (event IDs `FTR-20261021-<pmid>-01`) need `PAPER` and `LIT` identity records to attach to; provisional numbers are left to the integrator. Reading touched no existing claim. The note `repurposing_10h_scientist-d_20261021.md` reads the rows against CLAIM 046 (no pharmacodynamic readout) and the PMID 36537114 developmental-delay row, and proposes no change to either.

| PMID | Short title | Type | Disease | Transferability | Depth | Receipt |
|---|---|---|---|---|---|---|
| 33180985 | Kotulska 2021 EPISTOP | randomised open-label trial | TSC | T3 | complete | FTR-20261021-33180985-01 |
| 39625912 | Wied 2024 EPISTOP secondary analysis | re-analysis | TSC | T3 | partial | FTR-20261021-39625912-01 |
| 34270884 | French 2021 antiepileptogenesis | regulatory review | epilepsy | T3 | complete | FTR-20261021-34270884-01 |
| 38959712 | Downs 2024 ganaxolone non-seizure outcomes | placebo-controlled trial analysis | CDKL5 | T3 | complete | FTR-20261021-38959712-01 |
| 42246937 | Correale 2026 cognitive/behavioural COAs | measure evaluation | DEE | T3 | complete | FTR-20261021-42246937-01 |
| 41784472 | Sullivan 2026 soticlestat Dravet | phase 3 RCT | Dravet | T3 | complete | FTR-20261021-41784472-01 |
| 41891667 | Guerrini 2026 soticlestat LGS | phase 3 RCT | LGS | T3 | complete | FTR-20261021-41891667-01 |
| 35841234 | Hahn 2022 soticlestat phase 2 | phase 2 RCT | Dravet/LGS | T3 | complete | FTR-20261021-35841234-01 |
| 41999155 | Jha 2026 n-of-1 repurposing | single-patient trial | KCNC1 | T3 | partial | FTR-20261021-41999155-01 |
| 38015929 | Xian 2023 STXBP1 outcomes | natural-history cohort | STXBP1 | T3 | partial | FTR-20261021-38015929-01 |
| 42481851 | Kim-McManus 2026 individualised ASO | n-of-1 series | SCN2A | T3 | partial | FTR-20261021-42481851-01 |
| 42446932 | McKee 2026 synaptic-disorder NH protocol | protocol | synaptic disorders | T3 | partial | FTR-20261021-42446932-01 |
| 39762914 | Driedger 2025 pre-emptive mTOR long-term | follow-up cohort | TSC | T3 | partial | FTR-20261021-39762914-01 |
| 39726432 | Capal 2024 preventative sirolimus | phase 1 | TSC | T3 | complete | FTR-20261021-39726432-01 |
| 38144875 | den Hollander 2023 L-serine protocol | n-of-1 protocol | GRIN2B | T3 | complete | FTR-20261021-38144875-01 |
| 37537625 | Lewis 2023 intrathecal magnesium | n-of-1 case | GRIN1 | T3 | complete | FTR-20261021-37537625-01 |
| 37638552 | Bebin 2023 PREVeNT primary | placebo-controlled trial | TSC | T3 | complete | FTR-20261021-37638552-01 |
| 41061327 | O'Kelley 2025 PREVeNT neurodevelopment | placebo-controlled trial secondary | TSC | T3 | complete | FTR-20261021-41061327-01 |
| 40372822 | Downs 2025 caregiver meaningful change | survey | DEE/CDKL5/others | T3 | complete | FTR-20261021-40372822-01 |
| 38165374 | Berg 2024 FDA PFDD trial readiness | guidance review | rare DEE | T3 | complete | FTR-20261021-38165374-01 |
| 41237355 | Sullivan 2025 BUTTERFLY Dravet NH | natural-history cohort | Dravet | T3 | complete | FTR-20261021-41237355-01 |
| 41531035 | Liogier d'Ardhuy 2026 CANDID | baseline/feasibility | CDKL5 | T3 | partial | FTR-20261021-41531035-01 |

## Owed audits (declared, not performed; no baseline claim narrowed or reversed)
Blind locator audit is OWED on 42481851, 39625912, 33180985, 35841234, 41784472, 41891667, 41999155, 37537625, 39726432, 37638552 (the readings carrying a figure-panel or arithmetic observation the note leans on). Highest value: the Figure 4 panel a labelling in 42481851 (caption "change from baseline", panel is 12-month minus pretreatment).

## Queue and register notes
- Parked with cascade (no circumvention): paywalled 41904855, 40646322, 38677101, 41135308; figures and supplement of 37638552 and 41061327 (PMC bucket 404, Europe PMC image route 403); R4 BLOCKED primary trials.
- HELD row 36537114: question written first, not answerable from the record (endpoint is a clinician statement); no receipt (manifest belongs to scientist-b).

## Discovery-ledger proposals
None appended. Design leads are in the note and are `IPOTESI`.

## BATCH DISPOSITION

**Verdict:** PROPAGATED
**Batch:** `BATCH_20261019_012`

Propagated by `BATCH_20261019_012` (2026-10-22, MINOR, `WM_v7.27` preserved; integrator ACTOR_ID `orchestrator` by stated assumption, task `ORCH-REPURPOSING-10H-20261021`).

- **Landed:** `PAPER` and `LIT` identity records for the twenty-two receipts of the table (and the ten of the second wave, which carry the same shape), each class-level, NOT WWOX EVIDENCE, `Claim links: none`. The grade is **T4** for every row: the candidate's table says T3, but the registry's scale defines T3 as WWOX measured outside a loss-of-function neural system and T4 as WWOX not measured, and no row measures WWOX (the read artefacts contain no occurrence of the gene, with one registry-row mention counted in the Spanish multicentre record); the grade was applied by the scale, not by the table.
- **Not landed:** the held row `36537114` (no receipt; its manifest belongs to another actor); no ledger lead, none being proposed.
- **Still owed (declared by the candidate):** the blind locator audit of the readings it lists; a later audit file covers ten of those manifests and holds the per-triple verdicts.
