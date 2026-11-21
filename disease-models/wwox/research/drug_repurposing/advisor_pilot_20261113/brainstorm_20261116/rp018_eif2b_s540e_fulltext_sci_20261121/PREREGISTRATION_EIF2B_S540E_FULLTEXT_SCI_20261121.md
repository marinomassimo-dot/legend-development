# Pre-registration: full-text read of the eIF2B epsilon S540E preprint (SCI window X, 2026-11-21; hypothesis level; no dose; reference genotype class only; not medical advice)

Written and committed before the preprint's full text was opened. Only its title and abstract were known to this repository (ADV-114, `../adv114_eif2b_reagent_it_20261120/EIF2B_REAGENT_SEARCH_ADV114_IT_20261120.md`, section 1: "full text 429/1015, not retried"; the page was a rate limit, not a captcha).

Direction chosen by SCI (no assignment was open; ADV's standing instruction of 2026-11-21 asked for a choice with a duplicate check and a rejecting observation). Source row: RP-018 (portfolio, waiting) and open-question row IT47-Q02. Duplicate check done: `git grep` for the DOI suffix and for S540E finds only the ADV-114 record, the capability-scout log lines about the spelling miss, the IT checkpoint and the portfolio row; nothing holds the full text (`files/fulltext` has no copy). Discarded before this choice, with the prior-art file: IT46-Q07 (the loss-adequacy criterion is already written in INV-08 step X2, `../../nrf2_comparator_sci48_20261112/consumer_delta.md` row 4); the truncated product of the exon 9 escape alleles (`disease-models/wwox/analysis/wwox_nmd_assay_census_20260922.md` row T-1, the rat lde terminal-exon allele); mitotic dilution and the neuron-fraction arithmetic in the cerebellum (`disease-models/wwox/analysis/cerebellum_layer_localisation_20260922.md` H2 and section 2).

## Question
Does the full text of the preprint (bioRxiv, doi 10.1101/2025.11.03.686297; eIF2B epsilon S540E in SH-SY5Y) move IT47-Q02 from NARROWED to answered, and can the eIF2B/ISR arm of the broad panel be separated from the GSK-3 route by a published result?

## Decision it can change
The wording of IT47-Q02 and of the ISR slice design (ADV-114 section 3): whether the phosphomimetic has been compared with the phospho-resistant form and read on more than one reporter.

## Predictions fixed before reading (with my confidence)
* P1 (70 percent): the work is in SH-SY5Y (a neuroblastoma line) only, the main readout is a BACE1 5' UTR luciferase reporter, and no phospho-resistant S540A arm sits in the same experiment.
* P2 (60 percent): no global translation readout (puromycin labelling) and no ATF4 or other ISR marker is reported for S540E.
* P3 (50 percent): the pS540 signal in Alzheimer hippocampus is a small-n immunoblot (ten or fewer per group) without a phosphatase control for the antibody.
* P4 (95 percent): no oligodendrocyte-lineage, WWOX or Wwox-deficient system anywhere in the paper.

## Rejecting observation
The full text shows S540E next to S540A (or wild type) in the same system with a global translation or ATF4 readout and three or more biological replicates. Then IT47-Q02 is answered in that one system (still a neuroblastoma line, not a neural primary or a Wwox-deficient one), and the statement "cannot be separated by a published result" in ADV-114 needs a scoped correction.

## Stop rule
A rate-limit page (HTTP 429, Cloudflare 1015) gets one retry after a pause and one second lawful route; a captcha or a cookie wall is a stop and is recorded as a route result, not bypassed. No spoofed browser headers; no bursts. No e-mail address is sent to any service.

## What the result will carry
Verbatim locators for every number or sentence used; separate rows for what the text says and what it does not say; any figure value read from an image only with the figure's own scale and a blind second reading when the value decides a status.
