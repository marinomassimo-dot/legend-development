# IT25 A2 source check: sorafenib/regorafenib -> ZHX2 and the Q6 AKT1 / PIK3C3 listing-tier rows

Non-canonical research material; not medical advice. Zero spend, no registration, no e-mail, only
compound and gene names sent to public endpoints (PubMed, Europe PMC, DGIdb GraphQL, mygene.info,
HGNC). Receipts in `receipts/` passed `fulltext_receipts.py record --dry-run` (8 of 8) and are handed to
the integrator unrecorded. Full table: `verdicts.tsv`. Proposed exclusions: `source_exclusions_it25_proposed.tsv`
(the IT24 file was not edited).

## 1. Scope found in the engine outputs

- ZHX2: families `FAM:CAT:DGIDB:0bc1cf72f3bb` (sorafenib) and `FAM:CAT:DGIDB:18c39af2d48d` (regorafenib),
  sign -1, group `DGIdb_other`, n_rows 1, claim source TALC (catalog `interaction_type: inhibitor`).
  Proposals IT21P2-0035 (sorafenib, handed over in `handoff_it21.tsv`, CONDITIONAL_H_PROTECT, main target
  ZHX2, chain ZHX2 -T(-)-> HK2) and IT21P2-0036 (regorafenib, not handed over).
- Q6: 30 AKT1/PIK3C3 proposals, all CONDITIONAL_H_PROTECT, none handed over. By the catalog, 12 rest on a
  DGIdb claim whose only signed sources are listing-tier (rows in `verdicts.tsv`); the rest have a
  ChEMBL / GuideToPharmacology / DTC claim and were not in scope. Ipatasertib and capivasertib carry both
  listing and measured sources and are not affected.

## 2. Main finding: sorafenib/regorafenib -> ZHX2 is an alias artefact, not pharmacology

- NCBI gene 22882 (ZHX2) has the alias **RAF** (mygene.info: `alias: ["AFR1","RAF"]`). Sorafenib and
  regorafenib are RAF inhibitors; a listing that says "RAF" was mapped to ZHX2.
- The same DGIdb gene node ZHX2 also lists LY3009120, tovorafenib and avutometinib (TTD, type empty), all
  RAF inhibitors, and sorafenib from CIViC with publication PMID 32743370, a case report about **Raf**
  overexpression: "As sorafenib blocks Raf signaling, the expression of Raf may serve as a useful predictor
  of the efficacy of sorafenib." (Abstract).
- The only ZHX2-sorafenib paper PubMed returns (PMID 32114388, full text read) has ZHX2 as the variable that
  modulates resistance: "DOX induced ZHX2 overexpression significantly suppressed, while ZHX2 silence with
  siRNA increased the resistance of HCC cells to sorafenib." (Results 3.2). That is not an action of the drug
  on ZHX2. No regorafenib-ZHX2 paper exists in PubMed.
- Verdict: EXCLUDE_FROM_SIGNED_PROPAGATION for both. The TALC row itself (a lung-cancer summary table,
  paywalled) was not seen, so the alias route is the best-supported explanation, not a proof of what the table
  says. HGNC lists only KIAA0854 as alias, so a symbol-level HGNC check does not catch it.
- Consequence: IT21P2-0035 (handed over) and IT21P2-0036 rest on ZHX2 -> HK2 with an unsupported ZHX2 sign
  and should be flagged or withdrawn by the integrator. Sorafenib/regorafenib signs at BRAF/RAF1 are unaffected.
  Scan idea (not done): other catalog rows whose gene is the target of a symbol that is also an alias.

## 3. Q6 AKT1 / PIK3C3 rows

| Pair | Verdict | Reading |
|---|---|---|
| Pictilisib, buparlisib -> PIK3C3 (MCG) | EXCLUDE | Bago 2014: "class I PI3K inhibitors (GDC-0941 and BKM120) that do not inhibit Vps34". Contradicted, not flipped. |
| Pilaralisib, GSK2636771 -> PIK3C3 (MCG) | EXCLUDE (truth UNKNOWN) | Nothing read; MCG row has no publication. Same pattern as the two above. |
| Fexagratinib -> AKT1 (MCG trial list) | EXCLUDE (truth UNKNOWN) | AZD4547 described as selective FGFR1-3 inhibitor; DGIdb gives the concept the alias AZD5363 (capivasertib), a probable identity mix-up (hypothesis; row not seen). |
| Nelfinavir, perifosine, triciribine -> AKT1 | INDIRECT_QUALIFIED | Lower Akt signalling/phosphorylation by upstream or PH-domain routes; perifosine "does not directly affect ... Akt activity", TCN-P "inhibits neither Akt activity ...". Sign not contradicted. |
| MK-2206 -> AKT1 | CONFIRMED (abstract) | "novel allosteric Akt inhibitor". |
| Afuresertib hydrochloride -> AKT1 | UNKNOWN | Primary paper not located; free-base record supports the sign by non-listing sources. |

## 4. What was not read

TALC table (Simon and Somaiah 2013, paywalled), the MyCancerGenome and MyCancerGenomeClinicalTrial rows and
Clearity listings (no longer public), full text of Gills 2007, Kondapaka 2003, Berndt 2010, Hirai 2010, Gavine
2012 (abstract only), kinase panels for AZD4547, pilaralisib and GSK2636771 selectivity, the afuresertib
primary paper. Live DGIdb differs from the 2024-06-10 export used by the catalog (for example Drug
Repurposing Hub rows on perifosine, triciribine and MK-2206 AKT1), so live checks are context, not the
engine's input.

## 5. Suggested engine action (proposal, not applied)

Add the 7 rows of `source_exclusions_it25_proposed.tsv`. Do not add nelfinavir, perifosine, triciribine,
MK-2206 or afuresertib (supported, indirect or unknown). The wider listing-tier rule stays unadopted.

## Integrator status (IT25)
* Single producer, not independently verified. Two decisive facts were re-checked by the integrator against a second route: ZHX2 carries the NCBI alias `RAF` (mygene.info gene 22882), and the Bago 2014 abstract (PMID 25177796) states that GDC-0941 and BKM120 "do not inhibit Vps34".
* Applied: four exclusions (sorafenib and regorafenib to ZHX2; pictilisib and buparlisib to PIK3C3). NOT applied: fexagratinib to AKT1, pilaralisib and GSK2636771 to PIK3C3 (truth unknown, nothing read), because a pair is withheld only when a check has read and named it. `source_exclusions_it25_proposed.tsv` is kept as the producer's proposal.
* The 8 receipts were recorded in event-id order (ledger now 1,043 chained). Five of the papers are abstract-level only; the receipts say so.
* Open: the same alias artefact may exist for other DGIdb nodes; no scan was run.
