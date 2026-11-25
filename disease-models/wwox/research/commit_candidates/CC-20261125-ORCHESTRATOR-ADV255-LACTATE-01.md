# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV255-LACTATE-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-255 and ADV-259 wording, relayed by SCI at ADV's request; peer messages, not operator authority) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/adv255_lactate_table_sci_20261125/RESULT_ADV255_LACTATE_TABLE_SCI_20261125.md` (SCI: per-report table of lactate statements) and `adv259_chong_route_sci_20261125/RESULT_ADV259_CHONG_ROUTE_SCI_20261125.md` (SCI: the Chong 2023 passage is UNREACHABLE by every route tried). IT did not re-read the reports.
**Status:** PROPAGATED (`BATCH_20261125_003`; see the BATCH DISPOSITION block at the foot). No registry file is edited by this act. Ordinary-route lines (discovery ledger `DL-BIO-009`, `HYP-20260709-01`, mechanism map `N-06`, `meta_metabolism_current.md`, cards E02 and E04 with rebuilt cards) were placed the same day and are not part of this candidate.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** One unverified number marked, in two canonical places. No conclusion, grade or status changes.

## 2 · Proposed sentences (English)
| Record | Change |
|---|---|
| `CLAIM 009`, Summary, the clause «Chong 2023 aggiunge un piccolo segnale clinico (lattato lievemente elevato in P4)» | append: "Chong 2023, lactate: a mildly raised value in one of five subjects (2.4 to 3.3 mmol/L where the number is given) is a registry statement with no stored quote and no held passage (2026-11-25, ADV-259: unreachable by every route tried). Do not use it until the page is seen. Blood lactate is stated normal in 5 other publications (up to 14 subjects, no values printed); human spectroscopy is mixed." |
| `PAPER 017` (Chong 2023, PMID 36537114), Note | append: "Correction 2026-11-25 (ADV-255, ADV-259): the lactate value attributed to this paper has no stored quote and no held passage; the held copy is an 8-chunk surface without a lactate passage, and no open copy was found. Not verified, not contradicted. Do not use the number until the page is seen." |

## 3 · What this does NOT do
No change to status, grade, wikilinks or the dietary-response sentence of the same record (the 3-of-5 statement was corrected earlier by `BATCH_20260929_001`). No claim that the value is wrong.

## 4 · Statements for the blind check at propagation time
1. The held copy of PMID 36537114 has no sentence containing the word lactate (SCI, ADV-255 and ADV-259 route table).
2. Lactate is named normal in blood or an unspecified sample in publications 24456803, 27495153, 30361190, 30746283, 35792847, and the registry statement for Chong has no quote attached.
3. `CLAIM 009` and `PAPER 017` contain the clause to be amended, read in place at propagation.

## BATCH DISPOSITION — `BATCH_20261125_003` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED (verified remainder; wording corrected by the blind check)

2 record-scoped `replace-within` ops: `claim_registry_current.md` CLAIM 009 (correction sentence after the Chong 2023 clause) and `paper_registry_current.md` PAPER 017 (the correction placed inline after the raised-lactate value in the Note). **Change class restated: MINOR.** **Blind check:** one verifier (sonnet, effort high; call A of batch 2, report as delivered in `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_BATCH2A_IT_20261125.md`): the held copy of PMID 36537114 has no sentence with lactate (8 of at least 26 chunks; says nothing about the rest): SUPPORTED; lactate stated normal in 14 subjects of five publications, no value or range printed: SUPPORTED; small lactate peaks at 4 months and none at 2 years 4 months (PMID 35573960): SUPPORTED. **UNDERSHOOT, corrected before propagation:** the sample type is not only «blood or unspecified» (serum and CSF in Al-Baradie patient 1.2, serum, plasma); the propagated sentence says so. Not propagated here: nothing; the ordinary-route lines of this candidate were placed earlier the same day. Limits: IT did not re-read the SCI reports; the raised value itself (2.4 to 3.3 mmol/L) is not verified or contradicted.