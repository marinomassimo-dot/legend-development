# ADV-240 step 1: published solved-case series and their public supplements (IT, 2026-11-25)

Hypothesis level; nothing here is medical advice. Individual-level rows in published tables are cited as the source reports them; shareable text uses the reference genotype class only. No contact, no spend, no e-mail address sent to any service.

## Duplicate check (what the repository already carries; read before searching)
* `CC-20261004W7-B-REGISTRY-01` registered `PAPER 201` to `PAPER 206` (Karaer 2026: 250 Turkish children, two homozygous WWOX patients; Alotibi 2023: 105 Saudi children, two WWOX rows; Sabau 2025: 140 Romanian children, one compound heterozygous WWOX patient; Khadija 2026: 107 Tunisian patients, one deletion including WWOX; two further records). `CC-20261004W8-A-REGISTRY-01` registered `PAPER 217` to `PAPER 220` (Colin 2023, Pagnamenta 2023 whose WWOX case re-reports Piard 2019 Patient 11, Hamanaka 2025, Yigit 2026). The `PMID38074073` manifest (an Indian infantile-spasms cohort) carries three WWOX rows and a 34-reference enumeration.
* What those carry: **per-series WWOX row counts, found by searching for WWOX**. What they do not carry: a denominator of solved cases for a set of series chosen **without regard to WWOX**, nor a pooled share. That is the gap this step measures; the registry series are a numerator-biased sample and are **not** used as the base here.

## Searches (PubMed, field-tagged, free full text filter, run 2026-11-25; each count read as returned)
1. `("developmental and epileptic encephalopath*"[Title/Abstract] OR "epileptic encephalopath*"[Title/Abstract]) AND ("exome sequencing"[Title/Abstract] OR "genome sequencing"[Title/Abstract]) AND ("diagnostic yield"[Title/Abstract] OR "solved"[Title/Abstract] OR "molecular diagnosis"[Title/Abstract]) AND free full text[Filter]` -> **46** records (40 returned).
2. `("infantile epileptic encephalopath*"[Title/Abstract] OR "early-onset epilep*"[Title/Abstract] OR "infantile spasms"[Title/Abstract]) AND ("gene panel"[Title/Abstract] OR "exome"[Title/Abstract] OR "genome"[Title/Abstract]) AND "diagnostic yield"[Title/Abstract] AND free full text[Filter]` -> **18** records.
Union read: 51 distinct PMIDs with metadata (the 46 of query 1 beyond the first 40 were **not** retrieved: 6 records unread by list; the cap of the tool is the stated limit, not a judgement). 45 have a PMC record (of which 24 list at least one table-like supplement file in the bucket: counted below); 6 have none.

## Public supplements in the PMC open-data bucket (listing by PMCID; table-like files only)
Rows marked **IN** pass the frozen inclusion rule (see PREREG): a cohort of DEE, epileptic encephalopathy or early-onset epilepsy that reports solved cases, with a machine-readable or document supplement present in the bucket. Others are listed with the reason.
| PMID | Series (short) | Bucket supplement files | Rule |
|---|---|---|---|
| 40183601 | pediatric epilepsy clinical WGS, Epilepsia 2025 | s001.xlsx, s002.xlsx, s003.docx | IN |
| 35701389 | DEE exome in clinical practice, Dev Med Child Neurol | s002.xlsx | IN |
| 40347095 | 1000 pediatric-onset epilepsies, large NGS panel, Epilepsia Open | s001.xlsx, s002.xlsx, s003.docx | IN |
| 36967109 | individualised HPO panels, epilepsy exome and genome, MGG | s001.csv, s004.csv, s007.csv, s005.docx | IN |
| 31164858 | targeted exome in early-onset epilepsy, Front Neurol | Table_1.xlsx, Table_2.xlsx, Table_3.docx, Table_4.docx | IN |
| 24463883 | WGS in severe early-onset epilepsy, Hum Mol Genet 2014 | supp table3.xls, tables.doc | IN |
| 35328054 | ultrarare DEEs, Genes 2022 | s001.zip | IN (zip to open) |
| 29314763 | exome in a diagnostic pathway for epileptic encephalopathy, MGG | s001.docx | IN |
| 42949433 | neonatal-onset DEE, Epilepsia Open | s001.docx | IN |
| 31440733 | infantile DEE, Tasmania, Epilepsia Open | s001.docx | IN |
| 30552426 | recessive inheritance in early-onset epileptic encephalopathies, Eur J Hum Genet | MOESM1.docx | IN |
| 35330882 | 541 infantile spasms cases, Front Pediatr | Data_Sheet_1.docx | IN |
| 42400436 | 219 adult DEE patients, CNV, Epilepsia | s001.docx | IN |
| 39570184 | Nigerian children, early-onset epilepsy | s001.docx | IN |
| 38539105, 31875159, 33287870, 34070668, 36785910, 42650055, 32358097 | GDD/ID, adult focal, small mixed, systematic or single-gene reports | xlsx or zip present | OUT (not a DEE or early-onset severe epilepsy solved series) |
| 29100083 (Hamdan 2017), 26795593, 37471090, 37596007, 42094173, 39148850, 40722196 | large DEE or epilepsy yield series and reviews | **none in the bucket** | OUT: supplement not in the bucket; publisher or repository route not tried (access list below) |
| 29997391, 40220696, 42927712, 29396846, 36279597 | no PMC record | none | OUT: no free full text found by these routes |

## Access list (series that would need another route; for the operator PDF request file, not contacted)
Hamdan 2017 AJHG (29100083, PMC5673604; supplement on the publisher side), Trump 2016 Genet Med (26795593, no PMC), the large exome-in-pediatric-epilepsy JAMA Netw Open 2023 series (37471090) and the Lancet Neurology rapid-genome series (37596007): each is a large solved-case series whose per-gene table was not in the bucket; they are the series that would most move a denominator.
