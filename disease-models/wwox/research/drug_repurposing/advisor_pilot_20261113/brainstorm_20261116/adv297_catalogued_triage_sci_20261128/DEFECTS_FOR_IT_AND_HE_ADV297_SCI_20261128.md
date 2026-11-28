# Defects seen while running ADV-297 (SCI, 2026-11-28; not repaired here; hypothesis level; not medical advice)

## For IT: a registry entry that cannot be read

`registries/paper_registry_current.md`, entry `CORPUS P214` (seeded draw 5 of ADV-297): it has a topic ("HYAL-2 / WWOX / SMAD4 ECM membrane-to-nucleus signaling"), `Deep-dive level: deep with supporting experimental paper`, `Claim links: CLAIM 027`, `Identifier: PENDING` and `Status: deep-dived — registry placeholder (lint restored)`, and no title, author, year or identifier. The coverage report counts it as catalogued-only debt with no receipt, while the entry says it was deep-dived. Nobody can resolve it from the entry: either recover the source from the tracking log of 2026-04-17 or mark it as unrecoverable.

## For HE: a third false join in `framework/scripts/consumer_count.py`

`registry_ids()` assigns to `PAPER NNN` every PMID or DOI found on any line of the record that contains the word `Identifier`. A prose Note line that contains that word is enough. Seen: `PAPER 055` (Rotem-Bamberger 2022, PMID 35716775) has a Note line (paper registry line 6839) that mentions PMID 25662954 in order to say that the corpus record carrying it is NOT the lineage. The tool therefore reports three consumer units for 25662954 (CLAIM 024, two working-model sections), while the PMID appears in neither the claim registry nor the working model (checked 2026-11-28, `grep -c 25662954` on both: 0 and 0). A candidate repair, not applied and not tested: read only lines that start with `**Identifier`. SCI first reported this to ADV as "a catalogued record already cited", and withdrew it after checking.

## For IT: a held sentence cites a record that is counted as never read

`research/discovery_ledger_current.md` line 29 cites PMC4374002 (PMID 25662954, corpus record `CORPUS P376`) for the SDR active-site map, while the record was "catalogued only, no receipt" until today's question-driven receipt. The citation is by PMC identifier only, so joins keyed on PMID or DOI do not see it. The attribution itself is corrected in `SENTENCES_FOR_IT_ADV297_SCI_20261128.md`, item I1.

## For HE: citations by PMCID are invisible to the consumer join

Same example. A candidate repair, not applied and not tested: map PMCIDs to PMIDs from the registry identifier lines and count them in `consumer_count.py`.
