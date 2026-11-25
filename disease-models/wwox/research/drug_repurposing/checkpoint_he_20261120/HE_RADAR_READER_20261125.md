# Radar reader: untriaged hits worth a look (HE, 2026-11-25)

One page for the weekly triage, agreed by ADV. Population: the radar blocks that were `TO_TRIAGE` on 2026-11-25 (dated 2026-10-29 to 2026-11-25). Everything here is a **search hit judged by its title**: nothing was read, nothing is evidence. "Not held" means the identifier appears in no repository file outside the radar's own outputs. Each hit once, under the consumer who could act on it.

**Correction first.** `HE_RADAR_YIELD_20261125.md` lists PMID 41757738 as a paper on knowledge graphs for target prioritisation. It is not: that identifier is a paper on small-molecule ring systems. The knowledge-graph paper (Artemis) is PMID 42614934. The cause was an extraction that joined a title to the next hit's address when a hit carried no date; it also hid 26 of 360 hits from the first screen, which are screened here.

## Ranked first

| rank | hit | why first | consumer |
|---|---|---|---|
| 1 | [PMID 40125810](https://pubmed.ncbi.nlm.nih.gov/40125810/) QO-83, a Kv7 modulator against acute and chronic seizures in rodents | a compound with a measured anti-seizure effect, beside the Kv7 comparisons | SCI (routed by ADV) |
| 2 | [doi 10.1038/s42003-026-10958-7](https://doi.org/10.1038/s42003-026-10958-7) axon initial segment development and Kv7 dysfunction, Fmr1 knockout rat | circuit-level context for the same lever | SCI (routed by ADV) |
| 3 | [PMID 42723519](https://pubmed.ncbi.nlm.nih.gov/42723519/) vigabatrin loading-dose pharmacokinetics by enteral tube (post-anoxic status epilepticus) | exposure data; the population is not infantile spasms | SCI (routed by ADV) |
| 4 | [PMID 42441989](https://pubmed.ncbi.nlm.nih.gov/42441989/) vigabatrin-related MRI changes and tapering, one infant | a safety signal from a single case | SCI (routed by ADV) |

## Others not held, by consumer

| consumer | hit | one line |
|---|---|---|
| Biomarkers | [PMID 42884085](https://pubmed.ncbi.nlm.nih.gov/42884085/) biofluid markers of neuronal and glial injury in epilepsy and seizures | the title reads as a review; check against the biomarker strand |
| Electrophysiology | [PMID 41137858](https://pubmed.ncbi.nlm.nih.gov/41137858/) chemogenetic astrocyte modulation and spontaneous hippocampal discharges | astrocyte lever on discharges |
| Method | [PMID 42837326](https://pubmed.ncbi.nlm.nih.gov/42837326/) how many animal and human tissue samples inadequate antibody validation puts at risk | relevant when a protein claim rests on one antibody |
| Method | [PMID 42614934](https://pubmed.ncbi.nlm.nih.gov/42614934/) Artemis, knowledge graphs for target prioritisation | precedent for the provenance question |
| Harness | [K-Dense-AI/drug-discovery-agent-skills](https://github.com/K-Dense-AI/drug-discovery-agent-skills) | licence and content unread |

## Left out

The rest: one-word matches (property prices, video pipelines, a company named GABA, sales and churn predictors), reviews and papers about other diseases or organisms, personal web pages, and hits the repository already holds (among them the cannabidiol Gabrb3 mouse, add-on ethosuximide, an SLC12A5 case, vigabatrin optic nerve injury and the tazemetostat withdrawal).

## For the next triage

Open the ranked items first. A block counts as yield only if something LEGEND does changes because of it (`HE_RADAR_YIELD_PREREG_20261125.md`).
