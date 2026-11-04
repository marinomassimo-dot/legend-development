# IT26 source check: listing-tier pairs left open by IT25

Non-canonical research material; not medical advice. Zero spend, no registration, no e-mail, only compound and gene
names and PMIDs sent to public endpoints (PubMed E-utilities, Europe PMC, PMC efetch, DGIdb GraphQL, ChEMBL REST).
Receipts in `receipts/` passed `fulltext_receipts.py record --dry-run` (8 of 8) and are handed to the integrator
unrecorded. Table: `verdicts_it26.tsv`.

## Outcome per pair
| Pair | Outcome | Basis |
|---|---|---|
| Pilaralisib -> PIK3C3 | NOT_MEASURED | Foster 2015 abstract (class I selective, >130 protein kinases) and Shapiro 2014 abstract (pan-class I); abstract only |
| GSK2636771 -> PIK3C3 | NOT_MEASURED | Mateo 2017 abstract (PI3K beta selective); abstract only |
| Fexagratinib -> AKT1 | EXCLUDE_FROM_SIGNED_PROPAGATION | DGIdb alias AZD5363 on the fexagratinib concept; Gavine 2012 abstract (FGFR1-3); TALC lists FGFR1,2,3 |
| Afuresertib hydrochloride -> AKT1 | CONFIRMED | Dumble 2014 full text, Ki* 0.08 nM |
| TALC rows sorafenib / regorafenib -> ZHX2 | EXCLUDE_FROM_SIGNED_PROPAGATION (reinforced) | TALC Table 1 read: targets are RAF/MEK and RAF |

## 1. What TALC is (item 5)
DGIdb source list (live, 2026-11-04): `TALC` = "Targeted Agents in Lung Cancer (Commentary, 2014)", version 12-May-2016,
trust level "Expert curated", citation Morgensztern D, ... Govindan R. "Molecularly targeted therapies in non-small-cell
lung cancer annual update 2014", J Thorac Oncol 2015;10(1 Suppl 1):S1-63, PMID 25535693, PMCID PMC4346098. It is therefore
not the Simon and Somaiah 2013 item named in the brief (both are co-authors of this paper).
Free legal route that worked: PMC author manuscript PMC4346098 through NCBI E-utilities (`efetch db=pmc`, XML, 764 kB).
Europe PMC `fullTextXML` returned HTTP 500 for it (the record is not flagged open access) and the PMC PDF link returned an
HTML page; the XML route gave the whole text including Table 1 (a tabulated summary of targeted agents: sponsor, name,
type, target(s), phase, side effects, ClinicalTrials.gov link).
What Table 1 shows for the pairs: regorafenib `VEGFR-1,2,3,TIE2,PDGFRβ,FGFR, KIT,RET, RAF`; sorafenib
`VEGFR-2,3,PDGFR β,KIT,RAF/MEK,FLT-3`; XL147 `PI-3K (class 1 isoforms)`; AZD4547 `FGFR1,2,3`; MK2206, nelfinavir and
perifosine all `Akt`. The text has no occurrence of ZHX2, PIK3C3, Vps34, GSK2636771, GSK2110183 or afuresertib. The
DGIdb TALC regorafenib rows (TEK, KIT, PDGFRB, RET, FLT4, KDR, FLT1, FGFR2, ZHX2) map one to one onto that target cell, with
"RAF" landing on ZHX2 (NCBI alias RAF, IT25). So TALC is a listing of author-stated targets with no measurement, and the
ZHX2 rows are an alias artefact now confirmed at the source. The TALC "Akt" rows for MK-2206, nelfinavir and perifosine are
likewise unmeasured labels (IT25 verdicts for them stand).

## 2. Fexagratinib and the AZD5363 alias (item 3)
Live DGIdb GraphQL (`drugs(names:["fexagratinib"])`) returns three concepts with that name. ncit:C88272 (aliases AZD4547,
TTD, CIViC) has FGFR1-4 and others, no AKT. drugbank:DB12247 has alias AZD-4547 only. **iuphar.ligand:7707** has aliases
AZD-4547, **AZD5363**, AZD4547, CHEMBL:CHEMBL3348846, and interaction rows FGFR1/2/3/4, KDR, IGF1R (ChEMBL / GtoPdb /
MCG trial) plus **AKT1, AKT2, AKT3 from MyCancerGenomeClinicalTrial only**. Capivasertib's concept iuphar.ligand:7709 has
the alias AZD5363 too and AKT1/2/3 from ChEMBL, Clearity and GtoPdb. The two ligand records are adjacent (7707/7709; PubChem
substance 223366040/223366042), so the mix-up is plausible as an ID-adjacency or name-merge error. ChEMBL CHEMBL3348846
has no AKT1 activity row for AZD4547. The MCG trial row is no longer public, so this stays a database-level hypothesis.
Gavine 2012 (abstract only): "a novel and selective inhibitor of the FGFR1, 2, and 3 tyrosine kinases"; the kinase panel is
behind a paywall (not in PMC), so whether AKT1 was assayed is unknown.

## 3. PIK3C3 rows
Nothing in PubMed links pilaralisib or GSK2636771 to Vps34/PIK3C3/class III (searches returned 0). Bago 2014 was re-read at
full text (open access): it tests GDC-0941 and BKM120 and VPS34-IN1 but never XL147 or GSK2636771. One secondary datum
exists and was NOT read at its source: ChEMBL lists pilaralisib VPS34 IC50 7000 nM (document CHEMBL3860068, a J Med Chem
2017 review on class II PI3Ks, PMID 27644332, paywalled and not in PMC; primary study not traced). If correct, the action
is weak (micromolar) and not contradicted in sign. The IT25 exclusion pattern (pictilisib, buparlisib: contradicted)
does not transfer: these two are NOT_MEASURED, not contradicted, so exclusion needs the operator's rule (a pair withheld only
when a check has read and named it) rather than a measured negative.

## 4. Other database leads (context, not receipts)
ChEMBL document CHEMBL3991601 = Klaeger 2017 Science "The target landscape of clinical kinase drugs" (PMID 29191878;
kinobeads in lysate). It holds, for GSK2636771, AKT1/2/3 Kd > 30000 nM, and for afuresertib AKT1 Kd = 63 nM, AKT3 7 nM,
AKT2 2800 nM. No PIK3C3 row for either compound. The paper's main text (PMC author manuscript PMC6542668, fetched) names none
of these compounds; the numbers sit in supplementary tables that were not opened, so no receipt was written for it.
GSK2636771 p110beta IC50 0.89 nM with >800-fold over p110alpha/gamma appears in ChEMBL from a J Med Chem 2015 review
(PMID 25387153, not opened).

## 5. Read, with depth
Full text (partial): TALC 25535693 (Table 1 rows and section 9 text), Dumble 24978597 (open access), Bago 25177796 (open access).
Abstract only: Foster 25637314, Shapiro 24166903, Gavine 22369928, Mateo 28645941 (the brief called it Mayer), Hosford 27903677.
Not read: Klaeger supplement, Falasca 2017 review, PMID 25387153, Gavine full text, Mateo and Foster full text (not in PMC),
GtoPdb ligand pages (web services need an API key, HTTP 401), MCG/Clearity listings (no longer public).
Receipts: Gavine and Bago carry `prior_receipt` FTR-20261104-NNN-02 (IT25 abstract-level receipts) because the ledger
requires a parent for a second reading of the same study.

## Integrator status (IT26)
* The producer's reports named a different title for TALC than the IT25 note: DGIdb's TALC is "Targeted Agents in Lung Cancer (Commentary, 2014)", i.e. Morgensztern et al. 2015 (PMID 25535693, author manuscript PMC4346098, read through E-utilities `efetch db=pmc`); Simon and Somaiah are co-authors. The IT25 note's "Simon and Somaiah 2013" is superseded.
* Verdicts applied: fexagratinib AKT1/AKT2/AKT3 (alias artefact hypothesis with a database basis; the MyCancerGenome rows are not public) and the six rabeprazole pairs (added by the integrator: DGIdb alias E-3810 shared with lucitanib, PMID 24446259 and 25193991 at abstract level) are excluded from signed propagation. Pilaralisib and GSK2636771 at PIK3C3 are NOT_MEASURED (class I selectivity stated, no Vps34 value) and stay in: a pair is withheld only when a source check has read and named it as contradicted or artefact. Afuresertib hydrochloride at AKT1 is CONFIRMED by full text (Dumble 2014, Ki* 0.08 nM). Pilaralisib at Vps34 IC50 7000 nM appears only as a ChEMBL lead, not read at source.
* Single producer for most rows; five papers abstract-level; the kinase-panel supplements of Gavine 2012 were not opened. Ten receipts (-03) recorded by the integrator.
