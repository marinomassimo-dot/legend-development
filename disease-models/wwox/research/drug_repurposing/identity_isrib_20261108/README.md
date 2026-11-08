# ISRIB identity: the unnamed ChEMBL record is the published tool compound (2026-11-08)

Non-canonical research material. Not medical advice; no efficacy claim; no dose; nothing here changes the four scientific current files, a card, a need, a ranking or the catalogue build. No ledger was edited and no receipt was written (abstract-level and registry-record reads only).

## Decision (first)

**Resolved as an identity, nothing more.** `CHEMBL4303573` (no preferred name, no synonyms) is the molecule the FDA Substance Registration System names ISRIB (UNII `S6SZR97SBZ`). The row is `identity.tsv`. It closes the "not fixed" row of the ISR tool compound in [`generation_it35_20261108/README.md`](../generation_it35_20261108/README.md) without a generator, adapter or catalogue change: a reader who finds `CHEMBL4303573` among the `nearest` hits of `repurposing_search.py compound ISRIB` (answer `NO_MATCH_FOUND`) can now take it as the published probe.

## What was checked (2026-11-08, one request per host, no key, no login, no contact address)

| Source | Field | Value |
|---|---|---|
| ChEMBL REST, `molecule/CHEMBL4303573.json` (sha256 `336138af04d87f971962c0363c8fa3d55963f9aae05f1abfc97744f894e15807`) | pref_name / synonyms / max_phase | null / none / null |
| same | standard InChIKey | `HJGMCDHQPXTGAV-IYARVYRRSA-N` |
| GSRS, `substances(S6SZR97SBZ)` (sha256 `344052471b57b0947404868f3abcbe8fd117a4df77850cb8a80e4102cfa088ed`) | name / InChIKey | ISRIB / `HJGMCDHQPXTGAV-IYARVYRRSA-N` |
| same | molfile title | N,N'-trans-1,4-Cyclohexanediylbis[2-(4-chlorophenoxy)acetamide] |

The two keys are identical in all three blocks, including the stereo block. That is the whole basis; a name match is not used.

## Three things not to copy from the sources

1. **`status: approved` in the GSRS record** is the registry's own state for a validated record. It is not a drug approval, and ChEMBL gives `max_phase` null.
2. **`stereochemistry: RACEMIC`, optical activity (+/-)** in the GSRS record. By construction the molecule is trans-1,4-disubstituted with two identical arms, so it has an inversion centre and is achiral (the reviewer's inference from the structure, not a statement of the registry). Do not carry "racemic" into any entry as a property of the compound; the identity basis is the InChIKey.
3. **PubChem name queries** were reported to return a record without stereochemistry for both cis and trans names; this was not re-run here, so name-based joins stay refused.

## Licence and cost

GSRS data: public domain, CC0 1.0 (the service's own Licensing page, read in [`identity_gsrs_it26_a1_20261104/terms_findings.md`](../identity_gsrs_it26_a1_20261104/terms_findings.md)). ChEMBL: CC BY-SA 3.0, already the catalogue backbone; one identifier is cited, no table is copied. Spend: none.

## The 2026 eIF2B paper (reference only)

Dalwadi, Subramanian, Walter, Frost and colleagues, Nature Chemical Biology, 2026-06-29, PMID 42373951, DOI 10.1038/s41589-026-02256-4. **Abstract read only.** It says an eIF2B beta-subunit "latch-helix" couples to the alpha subunit, eIF2-P binding unhooks it and inhibits activity, and that the authors generated ISR-activating compounds that stabilise eIF2B in the inhibited state, so that allostery "can be pharmacologically manipulated to sustain or attenuate the ISR". That supports one sentence for INV-02: the same complex admits compounds with opposite effects on the ISR, so naming eIF2B as the target does not fix the direction of a compound's action.

Not attested here: compound names, the cell model, the apoptosis result and any statement about ISRIB in that paper. PubMed reports no PMC copy and no open-access licence for it, and no other route was tried. Do not cite any of those until the full text is read by a permitted route and recorded.

## Utility and what would change it

Small and honest: it makes a recorded gap closed and stops the next session from re-deriving the identity. It changes no candidate and no ranking; INV-02 stays blocked by the protein-level ISR measurement, not by the catalogue. KEEP if a later search that reaches `CHEMBL4303573` reads this row instead of redoing the join; DISCARD the folder if the catalogue ever gains the molecule by a build (the row then duplicates it).
