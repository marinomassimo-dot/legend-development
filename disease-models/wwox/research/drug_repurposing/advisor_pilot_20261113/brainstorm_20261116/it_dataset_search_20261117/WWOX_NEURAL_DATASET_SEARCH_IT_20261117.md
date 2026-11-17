# Search for public Wwox-deficient neural transcriptome datasets released since 2025-09-01 (IT; host clock 2026-11-17 ~09:00Z; non-canonical; a statement about the queries below, not about the repositories; no delegate, no spend, no key, no contact address sent)

Written for: ADV (SCI's value-of-information row 7: a neocortical Wwox nuclei table with three or more animals per arm). **Outcome: none found on these two routes, a statement about the queries.** No new neural Wwox-deficient series; nothing that could move a cell of arm table v8 (by cell_id), so no cell is named.
## Routes and tools (generic clients; the repository has no GEO census tool, so I used the public services directly)
1. **GEO** through NCBI E-utilities (esearch and esummary, database gds, no key, no e-mail parameter), host time 08:51Z. Queries (all with publication date 2025/09/01 to 2026/12/31): `Wwox`; `WWOX` (both: 82 records, 14 series after removing samples and platforms); `(Wwox OR WWOX) AND (knockout OR knockdown OR deficient OR mutant OR conditional)`: 22 records; `Fra16D`: 1; `(WWOX OR Wwox) AND (organoid OR iPSC OR neuron OR brain OR cortex OR hippocampus)`: 25; `(SCAR12 OR WOREE OR "WW domain-containing oxidoreductase")`: 9; `"WW domain containing oxidoreductase"`: 7.
2. **ArrayExpress / BioStudies** REST (collection arrayexpress, no key): `Wwox` and `WWOX` (16 hits each) and `WW domain-containing oxidoreductase` (236 text hits, none relevant); the listing has no release-date filter, I read the dates.
## What the GEO series are
| accession | in the census? | what it is | neural? |
|---|---|---|---|
| GSE158681, GSE158682, GSE158684, GSE158685 | yes (the S-line and conditional-deletion series: hippocampi, cortex, hippocampal nuclei; GSE158684 is the P17 nuclei pool, one pool per arm) | public date shown as 2026-10-01 | yes, already held |
| GSE245605 | yes | osteosarcoma Wwox RNA-seq | no |
| GSE245606, GSE245607 | no | osteosarcoma Wwox ChIP-seq and RNA-seq | no |
| GSE288262 | no | B-cell-specific Wwox deletion, plasmablastic tumour model | no |
| GSE300267, GSE300269, GSE300270 | partly (the first two yes) | Wwox loss in cutaneous squamous cell carcinoma | no |
| GSE298081, GSE298085 | yes | human cell genetic-landscape screens | no |
| GSE310210 | no | gold-nanoparticle response paper that matched the word | no |
BioStudies: E-MTAB-14948 and E-MTAB-14949 (2025-04-18, fly heads, neuronal Wwox knockdown or overexpression with a second transgene) are known to the census and are invertebrate; E-MTAB-14792 not repeated (known, not accessible). All other hits are 2014 or earlier.
## Limits
A deposit that never names Wwox in its title, summary or sample text would not be found (for example a mutant described by an allele name only); the GEO date field is the series public date, not the submission date; SRA and BioProject, Zenodo and supplement-only tables were not searched (outside the two routes); a new deposit in the last days may not be indexed yet. If SCI or ADV knows a deposit under another name, I search for it by accession.
