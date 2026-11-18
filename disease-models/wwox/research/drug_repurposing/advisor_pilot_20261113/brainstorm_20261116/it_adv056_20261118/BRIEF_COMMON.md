# Brief common to packages A and B (ADV-056, vigabatrin dossier; IT, 2026-11-18)

Producer, not verifier. Non-canonical; reference genotype class only; no dose, no schedule, no recommendation for or against any use of any drug; not medical advice. Follow `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_ketamine_lanes_20261117/COMMON_RULES.md` (plain HTTP client, no key, no contact address or e-mail to any service, NO browser-style User-Agent, a challenge page or reCAPTCHA is a STOP for that source, no spend). Read repository files from the ROOT CHECKOUT `/home/desktop/legend-development` (read-only; use `git grep` there; NEVER grep the two large registries `paper_registry_current.md` and `fulltext_read_receipts.jsonl`); write only under your output folder.

## CLINICAL CASE LINKAGE RULE (binds both packages; a breach is a failure of the package)
Children are described in AGGREGATES only. No per-child table, no per-child row, no identifier, no variant string, no sex, no country, no date, no site, nothing that could identify a person. One row per REPORT (not per child) with only: report id (PMID), design, number of children treated with the agent as a count; for reports with fewer than 3 such children, merge them into one row labelled "reports with 1 or 2 treated children (k reports)" and give only summed counts; any cell with a count under 3 is written "fewer than 3". Age is given only as a band (under 1 year, 1 to 3 years, over 3 years) and only as counts per band. If a source gives a family's own account, do not record it.

## Rules
* Reuse before reading: first read the repository items in your section, cite by path; then primary sources for what is missing.
* Every row: source id (PMID or DOI), what the source states (verbatim quote or numeric locator), depth read per section (full text / abstract only / not read), route and sha256 of saved bytes in SOURCES.tsv. Separate DATO (source states it), INFERENZA, IPOTESI.
* An absence needs two routes (PubMed and Europe PMC, field-tagged queries); record each query and count in SEARCHES.tsv. Say what you could not read and why.
* Output: REPORT.md at most 150 lines, answer first; tables as TSV (ROWS.tsv, SOURCES.tsv, SEARCHES.tsv). If your Write is refused, hand the whole report back in your final message.
