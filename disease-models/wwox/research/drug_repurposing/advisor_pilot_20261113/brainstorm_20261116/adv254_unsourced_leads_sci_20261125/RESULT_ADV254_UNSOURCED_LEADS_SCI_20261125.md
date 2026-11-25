# ADV-254 result: ledger leads with no primary PMID that consumers lean on (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; nothing here is medical advice. Identification only: no primary was read. No spend, no contact, no delegate. Pre-registration: `PREREG_ADV254_SCI_20261125.md`. Scan: `scan_unsourced_leads_adv254.py` → `unsourced_leads.tsv` (all 83).

## 1. Answer

* **83 leads carry no PubMed identifier, not 86.** ADV-249's rule missed a PMID written in bold in DL-MECH-050, DL-METH-081 and DL-MECH-083. All four of their PMIDs hold receipts, so ADV-249's never-read list does not change.
* **"No PMID" mostly is not "no source":** 58 of the 83 name a PAPER record that resolves to a PMID, 3 more name only a CLAIM id, 2 only a DOI or accession, 7 only an author and year, 13 nothing of these.
* **9 of the 83 have a consumer** (both routes; E1 expected at most five: **not met**). Only three are consumed by a card or a hypothesis record: DL-BIO-009, DL-MECH-153, DL-REPO-004.
* **6 of the 9 have identifiable primaries; 3 are inferences with no literature primary** (DL-MOL-011, DL-MOL-013, DL-MECH-052).
* E2 (at least half name a registry id, DOI or accession): **met** (63 of 83).

## 2. The nine leads with a consumer

| Lead | Consumers | Outcome | Primaries (PMID) | Missing, or wording to carry |
|---|---|---|---|---|
| DL-BIO-009 (human metabolism "normal") | cards E02, E04; HYP-20260709-01, HYP-20261026-11; mechanism map CHAIN E and N-06 | found | 30361190, 24456803, 38161429 (secondary), 30362252; counter side 25012504, 34268881 | the statement itself is what ADV-255 tests |
| DL-MECH-153 (G6PD / NFE2L2 direction) | card L01 | found | 31543760 (PAPER 022), 37897534 (PAPER 130) | lead is a tagged hypothesis |
| DL-REPO-004 (LDH lowering, stiripentol) | HYP-20261026-11 | found | 42909904, 39769031, 42035940 (the "2026 abstract"), 31539780 (ChEMBL document CHEMBL4311969) | write the ids into the lead's source line |
| DL-MECH-009 (WPRE raises expression) | TX-007 analyses | found | 42422765 (PAPER 011, complete read on file) | the lead cites only the review PAPER 029 and "attached Fig S3" |
| DL-MECH-010 (neuronal rescue sufficient) | TX-007 analyses | found | 42422765, 33914858 (Repudi 2021) | add both ids |
| DL-MOL-002 (gap junctions) | superior-node search note | found | 34634460 (Breton 2021) | "Riccardi does not touch it" is an unsourced absence |
| DL-MOL-011 (an SSO cannot rebuild the acceptor) | splice-allele and TX-001 notes; mechanism map | **inference** | none named for the U1, ADAR and editing statements | label "mechanistic inference, no primary cited" |
| DL-MOL-013 (verdict on the ASO thesis) | mechanism map | **inference** | none named; the rat `lde` clause names no report | same label; name the `lde` report if the clause is kept |
| DL-MECH-052 (helix packing, weakened) | Q230P notes, MD protocol | **inference** | none: an internal AlphaFold computation (`scripts/legend/kferq_geometry.py` exists) | already tagged weakened hypothesis; keep "computation, no experiment" |

The mechanism map already classes R-08 as a transfer hypothesis (level T6, no WWOX evidence). It also calls the "mechanistic exclusion" of the other RNA routes its contribution, citing DL-MOL-013, without saying that no primary stands behind that exclusion. That is the one place found where the missing source changes how strong a line looks.

## 3. Next reading queue

1. A primary for the three biology statements under DL-MOL-011/013 (U1 snRNA corrects donor and not acceptor sites; antisense masking cannot restore a destroyed invariant AG; direction of ADAR editing). Rejecting observation: a published acceptor-site rescue by an oligonucleotide or modified snRNA at a destroyed AG dinucleotide. Consumers: the mechanism map, TX-001.
2. Nothing else is owed: the other six leads resolve to papers already registered or identified here.

## 4. Wording for IT (not applied)

* Add the PMIDs above to the source lines of DL-BIO-009, DL-MECH-009, DL-MECH-010, DL-MOL-002 and DL-REPO-004.
* DL-MOL-011, DL-MOL-013 and their two mechanism-map entries: "mechanistic inference from splicing biology; no primary cited".

## 5. Limits

Consumers are surfaces named in the pre-registration; ledger cross-references, batch reports, mirror reviews, dismissal and drug-repurposing notes appear only in the `route1_only_files` column and were not counted as consumers. PMIDs 34268881, 34634460, 31539780 and 42035940 were identified by title and abstract through Europe PMC, not read. "Author and year" matching is a pattern and can over- or under-count.
