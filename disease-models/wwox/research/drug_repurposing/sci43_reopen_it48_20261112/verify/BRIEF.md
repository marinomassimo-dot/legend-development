# Verifier brief (IT48 increment 1): second independent reading of eight SCI43 rows at digit level

Not medical advice. Reference genotype class only. Public edition; no personal data. Zero spend; no contact with any person; never send an e-mail address to any service; no browser-header spoofing; plain requests only. Write files in English. Do not edit anything outside the output folder below.

## Why this is being done
SCI43 recorded eight decisive rows as producer-read only (the verifier of that package could not reach the sources). The stated reopen condition was "when bioRxiv, PMC or J Neurosci are reachable by the plain route". On 2026-11-12 the Orchestrator confirmed by one plain request each: the bioRxiv preprint (DOI 10.64898/2026.02.03.703439) returns HTTP 200; Europe PMC lists PMC5242407 for PMID 28100740 (Niday). The rows decide whether KH1 (a Ba2+-sensitive resting-conductance share of about 23 percent) keeps its magnitude for juvenile layer II/III neurons.

## What to do
Rows (file: disease-models/wwox/research/drug_repurposing/potassium_conductances_sci43_20261110/output/decisive.tsv, columns prop_id, statement, source, locator): D01, D02, D03, D04, D07, D08, D11, D13. Also read the earlier verifier's notes on these rows: .../potassium_conductances_sci43_20261110/verify/verdicts.tsv and verify/audit.md.
For each row open the ORIGINAL source (full text; figures or source data where the number is read off a panel) and judge the statement proposition by proposition. For each:
* verdict: SUPPORTED / PARTLY / NOT_SUPPORTED / STILL_UNVERIFIABLE (say which access route failed and what you tried, exactly);
* the verbatim sentence or table cell (with section, figure or table label) that carries each number; for a panel read-off say it is a read-off and give your own value;
* recompute every derived percentage from the printed numbers (state inputs); say where the statement says MORE or LESS than the source (age, temperature, layer, internal solution, synaptic blockers, species, drug concentration);
* depth actually reached (abstract / full text text-only / figures viewed / source data).
Save every full text you obtain under /home/desktop/legend-development/files/fulltext/reopen_it48/ with its SHA-256 listed in verify/READ_LOG.tsv (file, url, http status, bytes, sha256). A bounded "not retrieved" is an acceptable answer: write exactly the URLs and the status codes; never write that a conductance or effect does not exist.
Do not change the rows, the ranking or any other file; do not assess druggability.

## Deliverable (in disease-models/wwox/research/drug_repurposing/sci43_reopen_it48_20261112/verify/)
VERDICTS.md (one section per row plus a final table), READ_LOG.tsv. End VERDICTS.md with one paragraph: does the 23 percent adult auditory-cortex figure (D01/D02) survive, and what does the juvenile layer II/III evidence from the other rows say about the share? Say what you did not read.
