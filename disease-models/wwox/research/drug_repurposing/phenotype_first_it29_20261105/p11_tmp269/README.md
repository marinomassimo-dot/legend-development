# P11 - TMP269 identity check (second actor), 2026-11-05

Not medical advice. Zero spend; public key-less REST only; no e-mail or registration used.

## Verdict: IDENTITY_CONFIRMED_FULL_KEY

TMP269 and CHEMBL3110004 share the full 27-character standard InChIKey:

    HORXBWNTEDOVKN-UHFFFAOYSA-N   (no stereocentres, no charge/isotope layer)

## Structure

- Name: N-[[tetrahydro-4-(4-phenyl-2-thiazolyl)-2H-pyran-4-yl]methyl]-3-[5-(trifluoromethyl)-1,2,4-oxadiazol-3-yl]benzamide
- SMILES (ChEMBL canonical): O=C(NCC1(c2nc(-c3ccccc3)cs2)CCOCC1)c1cccc(-c2noc(C(F)(F)F)n2)c1
- Formula C25H21F3N4O3S, MW 514.5 (PubChem CID 53344908). Neutral parent, no salt.

## Sources and independence

| # | Source (route) | Key returned | Derivation |
|---|---|---|---|
| 1 | PubChem PUG REST, compound by name "TMP269" -> CID 53344908 | HORXBWNTEDOVKN-UHFFFAOYSA-N | PubChem depositor-derived, key computed by PubChem |
| 2 | NCI CACTUS resolver, IUPAC-style name string (taken from the PubChem synonym list) parsed to structure -> stdinchikey | HORXBWNTEDOVKN-UHFFFAOYSA-N | Structure generated from the name text by NCI's own parser; key not copied from PubChem or ChEMBL. Independent of 1 and 3 as to structure/key, though the name string itself came from PubChem synonyms |
| 3 | ChEMBL REST, molecule/CHEMBL3110004 | HORXBWNTEDOVKN-UHFFFAOYSA-N | ChEMBL-curated structure |
| - | PubChem SMILES lookup (ChEMBL SMILES) -> CID | CID 53344908 | Not independent: input SMILES came from ChEMBL; shows only that PubChem holds the same structure |
| - | PubChem synonym list contains "CHEMBL3110004" | - | Depositor cross-reference; not independent of ChEMBL. Names it as TMP269's synonym |
| - | GtoPdb REST | not obtained | The service answered "API key is missing" (registration required, not done). The GtoPdb cross-reference to CHEMBL3110004 was therefore not re-checked here |
| - | Lobera 2013 paper text | not used | no figure/abstract key available; no local RDKit/OpenBabel for a third computation |

Independence is partial in kind: sources 1 and 3 are two curated databases that may share depositor lineage; source 2 is an algorithmic name-to-structure derivation, the only route not copying a database record.

## ChEMBL record CHEMBL3110004 (fetched live)

- molecule_type Small molecule; pref_name None; no ChEMBL synonyms listed.
- molecule_hierarchy: molecule_chembl_id = parent_chembl_id = active_chembl_id = CHEMBL3110004. It is the parent itself, not a salt/stereo/labelled variant.
- Exact full-key query (standard_inchi_key=HORXBWNTEDOVKN-UHFFFAOYSA-N): 1 record, CHEMBL3110004.
- First-block query (standard_inchi_key__startswith=HORXBWNTEDOVKN): 1 record, CHEMBL3110004 only. No other id shares the first block. (A free-text molecule search for "TMP269" also returns CHEMBL4081343, key FMMAEPUXSQUHEM-UHFFFAOYSA-N: a different first block, a text hit only, NOT the same entity.)
- First-block match alone would not be identity; here the full key matches.

## ChEMBL potency activity, HDAC4/5/7/9 (activity endpoint, 239 records total; none averaged)

The first ChEMBL ids of the 2013 J Med Chem paper (document CHEMBL3108758, PMID 24261862, "...class IIa HDAC inhibitors as a potential therapy for Huntington's disease"), same assay family for all four isoforms:

| Target | Type | Rel | Value | Assay | Assay description | Document |
|---|---|---|---|---|---|---|
| HDAC4 | IC50 | = | 130 nM | CHEMBL3112174 | Inhibition of human recombinant HDAC4 catalytic domain using Boc_Lys_TFA as substrate after 60 mins by fluorescence assay | CHEMBL3108758 |
| HDAC5 | IC50 | = | 80 nM | CHEMBL3112173 | same, HDAC5 catalytic domain | CHEMBL3108758 |
| HDAC7 | IC50 | = | 40 nM | CHEMBL3112172 | same, HDAC7 catalytic domain | CHEMBL3108758 |
| HDAC9 | IC50 | = | 20 nM | CHEMBL3112171 | same, HDAC9 catalytic domain | CHEMBL3108758 |

Other documents (full set in the TSV, columns: activity_id, target, type, relation, value, units, assay, document, description). Many are TMP269 used as a reference compound in later papers, so values differ by assay:

- CHEMBL3792358: IC50 HDAC4 134.4, HDAC5 108.4, HDAC7 40.85, HDAC9 23.24 nM (recombinant, Boc-K(TFA)-AMC, 60 min).
- CHEMBL4041521: IC50 127 / 263 / 112 / 19.4 nM (HDAC4/5/7/9).
- CHEMBL4043295: Ki 90.5 / 86.9 / 46.3 nM (HDAC4/5/7); CHEMBL4765362: Ki 126 / 80 / 36 / 19 nM (HDAC4/5/7/9).
- CHEMBL4402587: IC50 244 / 333 / 108 / 49 nM; CHEMBL6177932: 190 / 219 / 46.8 / 9.63 nM; CHEMBL5625236: 13 / 191 / 44 / 17 nM; CHEMBL4828751: 180 / 110 / 60 / 10 nM; CHEMBL5537119: HDAC4/5/7 157 / 97 / 43 nM.
- Outliers/other formats: HDAC5 IC50 990 nM (CHEMBL4130471, Ac-peptide); HDAC4 Ki 1770 nM (CHEMBL4396934); HDAC4 IC50 753 nM (CHEMBL5365542); HDAC4 IC50 3.48 x10^-1 microM = 348 nM (as stored units; CHEMBL6078697); HDAC4 353 nM (CHEMBL4251569, plus % remaining-activity dose series); percent inhibition at 10 uM for HDAC4/7 (CHEMBL5365438); cellular H3K9ac readouts for HDAC5/7/9 with no value (CHEMBL4433239); kon/k_off rows with null values (CHEMBL5727872, CHEMBL5727156).
- Off-target in the first paper: HDAC8 IC50 3600 nM, HDAC6 2300 nM, HDAC3 > 43000 nM.
Caveat: several documents describe the compound as a reference; whether each value was measured in that paper or quoted was not checked.
