# SCI48 tail — IT46-Q02: which entity is the panel entry labelled ABAT in the EUbOPEN selectivity data? (2026-11-12)

Non-canonical research material. Not medical advice; no dose or recommendation. Reference genotype class only. Labels DATO / INFERENZA. Paths relative to `disease-models/wwox/research/drug_repurposing/`. Written for: the integrator and whoever reads the S7 ladder rows.

## Answer first

1. **Not resolved from primary documentation by the routes allowed; the question stays OPEN with a sharper blocking reason.** What can be stated from ChEMBL's own records (DATO, read 2026-11-12 from the ChEMBL REST, plain curl): the four rows (BAY-3827, BI 2545, BI-605906, IPP/CNRS-A017; assays CHEMBL5476318, CHEMBL5476369, CHEMBL5479831, CHEMBL5476659) carry the description "Selectivity interaction (GPCR panel (PDSP screen)) EUB… ABAT"; `assay_type` B (binding), `bao_format` single protein, `confidence_score` 9 ("direct single protein target assigned"), target CHEMBL2044 (mitochondrial 4-aminobutyrate aminotransferase, *Homo sapiens*), document CHEMBL5465560 (a DATASET from EUbOPEN, ChEMBL 35, 1 December 2024, DOI 10.6019/CHEMBL5465560). The activity properties carry "Selectivity number of targets 45", "off-targets 2", "Screened at 10 uM (in-vitro potency)" and a link to the SGC probe page of the compound. **No protein identifier, construct, species of the preparation, radioligand or protocol is in those records**: the trailing symbol is a label, and ChEMBL's confidence 9 describes its own mapping, not the assay biology (INFERENZA).
2. **The primary documentation was tried and is unreachable by plain routes.** The SGC probe page named in the record is a single-page application with no static content (1,776 bytes of shell); the PDSP Ki download returned HTTP 403 ("That document is forbidden"), recorded as unreachable and not retried by another route; the PDSP assays page is a dynamic shell with no target list (4,402 bytes); the Ki database landing page describes the content in general terms only. Nothing was requested by e-mail or any contact route.
3. **Consequence for the module (unchanged, now explicit).** The four pointers stay what the IT46 reader and the ladder already say they are: rows of a 10 uM receptor-panel screen, **not** shown to be measurements on GABA transaminase; the S7 ladder flags them (`generation_it46_20261111/test_ladder.py`). An identity resolved in either direction would not give activity, selectivity or benefit in the WWOX model; it would only decide whether four activity-only pointers are dropped. No consumer changes beyond the question's blocking reason.

## Consumer delta (proposal; nothing applied)

| Recipient | Previous | Proposed | Limit |
|---|---|---|---|
| `batch_sci_20261105/map/open_questions_map.tsv`, row IT46-Q02, `blocking_reason` and `last_touched` | "The panel documentation was not reachable by the reader." | "ChEMBL records read 2026-11-12: label-only mapping (target CHEMBL2044 by symbol, confidence 9, no construct or protocol); the SGC probe page is a single-page application, the PDSP Ki download is HTTP 403 (not retried), the PDSP assays page has no target list; first undone step: the PDSP panel definition or the EUbOPEN selectivity table through a route the operator authorises." | not resolved; no protein identity claimed |

## Not done

The identity of the protein behind the label; the panel's protocol and construct. Zero spend, no contact, no personal data.
