# IT27 P8 independent verification (2026-11-04)

Non-canonical research material, not medical advice. Zero spend, no registration, no e-mail address sent anywhere.
Table: `verdicts_it27_p8.tsv` (claim, class, evidence, limit). Sources: DGIdb cached TSVs and live GraphQL, ChEMBL
cache and REST, PubChem PUG REST, Europe PMC, ClinicalTrials.gov v2. Scratch work was outside the repository.

## Order of work
Own reading of DGIdb/ChEMBL/PubChem first; IT26 README and verdicts read afterwards.

## Result
1. Rabeprazole x FGFR/VEGFR: **collision verified** for the code E-3810 (ChEMBL and PubChem both carry it on rabeprazole
   and on lucitanib). Attribution of the MyCancerGenome rows to lucitanib is a strong inference (identical gene set,
   rabeprazole has no kinase measurement), not a seen record. TTD also has E-3810 rows on rabeprazole (FGFR, VEGFR, PDGFR).
2. Fexagratinib x AKT1/2/3: the AZD5363 alias on iuphar.ligand:7707 is real, but the AKT rows carry the drug claim name
   AZD4547, not AZD5363, and the same trial-listing source gives AKT1/2/3 to everolimus, omipalisib, ipatasertib, MK2206
   and perifosine. So the alias is not shown to cause the rows; the pair is an unmeasured listing (absence of a
   measurement). **Disagreement with IT26 on the mechanism**, not on the exclusion.
3. Gavine 2012 panel: not readable (not in PMC; Europe PMC supplement/fulltext 404; publisher 403). Limit stated.
4. No independent source for either pharmacology claim; no contrary measurement either.
5. PX-478: SMILES and PubChem show the N-oxide of melphalan (321.2 Da); ChEMBL says Protein with a MOL structure and
   no sequence. Evidence points to a small molecule; the catalogue code is for the caller.

## Blind
MyCancerGenome rows; Gavine supplement; kinome datasets; Welsh 2004 full text.
