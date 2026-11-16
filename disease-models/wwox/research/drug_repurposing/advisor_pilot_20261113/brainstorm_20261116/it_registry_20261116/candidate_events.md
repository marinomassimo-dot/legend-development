# Prospective registry: candidate events (IT, ledger keeper; non-canonical; not medical advice)

Written for: SCI and the baseline-arm delegate (the predictors), and ADV. Reference genotype class only. IT names events and outcome sources and keeps the freeze; IT writes NO prediction. A row is registrable only when the predictor commits a statement BEFORE the event and the outcome source is dated and public. Trivial baseline for every row: "no change / the observed base rate", stated with its number at freeze.

| ID | Event not yet happened | Dated outcome source and check | Window | Trivial baseline | Information value |
|---|---|---|---|---|---|
| PR-01 | Pooled count of WWOX children with both a seizure and a development endpoint reaches 10 or more | PubMed WWOX radar plus the case table (new rows from new reports only) | to 2027-02-16 | current count 6, accrual rate from the table | high: it is the INV-10 trigger |
| PR-02 | Share of discordant children among the next 4 or more newly reported children with both endpoints (is it still 4 of 6?) | same | to 2027-02-16 | 4 of 6 | high |
| PR-03 | A new WWOX case report states an outcome for steroid/ACTH or GABA-AT treatment | PubMed query fixed at freeze; hit list dated | 90 days | at least one in 90 days at the past reporting rate (12 reports in the A1 series) | medium |
| PR-04 | A new WWOX report states a worsening after any antiseizure agent | same | 90 days | zero, at the A1 base rate (no worsening wording in the coded fields; unknown is not negative) | high for aggravation |
| PR-05 | A new report with a drug-by-genotype contrast in a WWOX model (any agent) | Europe PMC query fixed at freeze | 90 days | none (to date one experiment with no contrast) | high |
| PR-06 | ClinicalTrials.gov WWOX-related registered trials: change in count of recruiting interventional trials | clinical_census.py rerun, dated, same queries as the 2026-10-20 census | 30 days | unchanged | low (administrative) |
| PR-07 | A second laboratory reports the GluN2B-sensitive share of the NMDAR EPSC in a Wwox model | Europe PMC query fixed at freeze | 90 days | none | medium |
| PR-08 | The 2015 OPC screen supplement or a public MEA screen becomes lawfully reachable for the frozen compounds (access event, not science) | access check by one plain request | 30 days | still blocked | low (access) |
| PR-09 | A new peer-reviewed report on a Cav3 isoform-specific measurement for any compound of the Cav3 pair | Europe PMC query fixed at freeze | 90 days | none | medium |
| PR-10 | A new WWOX report on the age dependence (P6-P8 versus later) of any NMDAR measure | Europe PMC query fixed at freeze | 90 days | none | medium |

## Honest limit
The events that can occur within weeks are mostly publications; a hit rate on bibliometric events is weak evidence of generative skill and a hit on PR-08 or PR-06 is none. The registry can reach n = 10 only by counting such rows; I propose to report the n split into "scientific content" (PR-01, 02, 04, 05, 07, 09, 10) and "administrative" (PR-06, 08), and to say that nothing counts as generative improvement below 10 scientific-content rows. If SCI judges that fewer than 7 of these can carry a falsifiable statement, the registry is declared underpowered in advance rather than padded.
