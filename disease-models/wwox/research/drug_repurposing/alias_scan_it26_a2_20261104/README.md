# IT26 A2: scan of the listing-tier DGIdb pairs for alias artefacts (2026-11-04)

Non-canonical research material; not medical advice. Zero spend, no e-mail, only public gene symbols sent to mygene.info (one batch POST, 172 symbols).

## Method
1. `refresh_actions_it21.py run --listing-tier tier` (the existing sensitivity mode) lists every signed DGIdb row whose only direction comes from a listing source: 648 rows, 172 genes (TALC 174, MyCancerGenome 246, MyCancerGenomeClinicalTrial 130, ClearityFoundationClinicalTrial 75, CancerCommons 23).
2. NCBI aliases of each gene (mygene.info) minus the HGNC symbol/alias/previous symbols of that gene (`hgnc_complete_set_20261022.json`, already in the repository) leave the NCBI-only aliases (523 of the 648 rows have some).
3. A pair is a pointer when an NCBI-only alias is a stem of, or equal to, a target the same compound acts on in another row (`alias_scan_it26.py`). Positive control: the IT25 case sorafenib/regorafenib -> ZHX2 (alias RAF, stem of RAF1) is found. A first detector (alias equals another gene's HGNC symbol) found 80 collisions, almost all noise (MENA/ENAH, AIM1/CRYBG1) and missed the control, so it was dropped.

## Result: 4 pairs, 3 new
| Compound | Gene | Source | Alias | Reading |
|---|---|---|---|---|
| Sorafenib, regorafenib | ZHX2 | TALC | RAF | already excluded in IT25 |
| Sorafenib | VEGFC | MyCancerGenomeClinicalTrial | Flt4-L | VEGFC is the ligand of FLT4; sorafenib acts on the receptor. Probable mapping artefact; row not seen. No proposal rests on it |
| GSK2636771 | PIK3CG | MyCancerGenome | PIK3 | generic PI3K label; the compound is PIK3CB-directed. No proposal rests on it |

Of the 996 stage-S6 proposals, 26 have a main target that rests on a listing-only pair; none of them is in the 15 hand-overs.

## A second artefact class, found by reading the 26: a drug-side alias collision
Rabeprazole (family `FAM:CAT:DGIDB:0a77d333b9fe`, proposal IT21P2-0304, FGFR3) carries signed MyCancerGenome rows at FGFR1, FGFR2, FGFR3, FLT1, FLT4 and KDR. That is the target profile of lucitanib, not of a proton-pump inhibitor. DGIdb gives both drug nodes the alias `E-3810` (live query, 2026-11-04): rabeprazole has `E-3810`, lucitanib has `E-3810`. PubMed itself maps "E 3810" to rabeprazole (Eisai's code), while PMID 24446259 and PMID 25193991 use E-3810 / lucitanib for the FGFR1/VEGFR1-3 inhibitor. The ChEMBL claims of the same family (ATP4A, ATP4B) are the real pharmacology. Judgement: the six MyCancerGenome rows belong to lucitanib; the six pairs are excluded from signed propagation (`source_exclusions_it24.tsv`). Evidence level: abstract (receipts below), single producer, not verified by a second actor.
The detector above cannot see this class (it needs a drug-side comparison of two nodes sharing a code). A name-based DGIdb API query does not return alias matches, so a general scan was not possible; this is an open limit.

## Files
`alias_scan_it26.py` (scan), `test_alias_scan_it26.py` (5 tests), `suspect_pairs.tsv`, `ncbi_alias_listing_genes.json` (public NCBI aliases, 172 genes).
