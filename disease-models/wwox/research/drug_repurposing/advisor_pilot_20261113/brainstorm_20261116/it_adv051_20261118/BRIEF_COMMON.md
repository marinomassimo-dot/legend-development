# Brief common to packages A and B (ADV-051; IT, 2026-11-18)

Producer, not verifier. Non-canonical research; reference genotype class only; no dose, no schedule, no recommendation for or against any use of any drug; not medical advice; no therapeutic target assumed. Follow `disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_ketamine_lanes_20261117/COMMON_RULES.md` (plain HTTP client, no key, no contact address or e-mail to any service, NO browser-style User-Agent, a challenge page or reCAPTCHA is a STOP for that source: do not retry, do not delete what you did not create; no spend). Work from `/tmp/it56_iso` (read-only for you; use `git grep` there; NEVER grep the two large registries `paper_registry_current.md` and `fulltext_read_receipts.jsonl`). Write only under your output folder.

## The question (decision it changes)
The only drugs with in vivo data in a Wwox-null mouse are lithium and ethosuximide (Cheng 2020, PMID 32000863: one experiment, one laboratory, provoked-seizure (PTZ) assay, Racine stage curves; lithium lowered the stage in all three genotypes, ethosuximide's effect is described as knockout-selective but no interaction test is possible). Decision: which agent gets the first in vivo Wwox-null arm and in which order with the NMDAR pore-blocker arm; and whether the lithium and ethosuximide effects look WWOX-specific or are a general anticonvulsant property.

## Rules
* Reuse before reading: first read what the repository already holds (listed in your section) and cite it by path; only then read primary sources for what is missing.
* Every row: source id (PMID or DOI), species and age, model or assay, agent and what was measured, the result (verbatim quote or numeric locator), n and unit of n, depth read per section (full text / abstract only / not read), route and sha256 of saved bytes in `SOURCES.tsv`, and an independence note (same laboratory or same preparation = one origin).
* Separate three things in every row: what the source states (DATO); what you infer (INFERENZA); what is hypothesis (IPOTESI). Do not carry a number from a review into a row without opening the primary source or saying "review only".
* An absence needs two routes (PubMed and Europe PMC, field-tagged queries) before you write "not found in these queries". Record each query and count in `SEARCHES.tsv`.
* Say what you could not read and why (route, status).
* Output: `REPORT.md` of at most 150 lines, answer first; tables as TSV (`ROWS.tsv`, `SOURCES.tsv`, `SEARCHES.tsv`). If your Write is refused, hand the whole report back in your final message.
