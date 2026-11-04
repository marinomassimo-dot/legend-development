# IT25 A3: G-SRS name -> UNII -> structure trial on the 22 unresolved identity rows (2026-11-04)

Non-canonical research material. Not medical advice. Zero spend, no key, no login. Only the public compound names of the 22 rows were sent.

## Step 1: terms read before any query

The site gsrs.ncats.nih.gov is a single-page application; its own about/disclaimer text could not be rendered by a plain fetch (https://gsrs.ncats.nih.gov/ and its beta about page returned only the app shell), and no robots file exists (404).
No site-specific terms page, licence sentence or rate limit could therefore be read. What could be read:

- Peryea et al., Nucleic Acids Research 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC7779023 : "This work is written by (a) US Government employee(s) and is in the public domain in the US"; software Apache 2.0, "intended to be freely distributable to academic, government and commercial entities"; "The UNII is a non-proprietary, free to use ... identifier"; the public API returns JSON and its use is shown in the paper; bulk download is not offered on the public site.
- The FDA SRS page (fda.gov .../fda-global-substance-registration-system) returned 404.
- The earlier scout (P13-1) had likewise found no licence sentence on the download or about pages.

Judgement: nothing forbids automated reads and the data are US Government work, so the trial was run, but with the conservative reading that the site's own terms page was NOT read. Politeness: one GET per name, 1.5 s apart, 22 requests in total, honest user agent without any contact address. Derived values (UNII, matched name, verdict, SMILES) are committed; raw responses are not (kept in the session scratchpad cache, outside git).
This is a reported limit of the gate, not a pass of a read terms page; if the operator wants the formal terms read first, the 22 rows are a ten-line re-run (`--offline` re-evaluates the cache).

## Step 2: method

Per name: `GET https://gsrs.ncats.nih.gov/api/v1/substances/search?q="<name>"&top=20&view=full`. A record counts only if it is a `chemical` substance with an approval id (UNII) and its preferred name or one of its listed names equals the LEGEND name after case and punctuation folding (salt names such as "... HYDROCHLORIDE" do not match). Then:

- **firm** (R4): exactly one matching substance AND an independent identifier of the catalogue row agrees (a catalogue synonym other than the name appears in the G-SRS name list, or the row's own ChEMBL id equals UniChem(UNII)), with no contradiction.
- **weak**: exactly one matching substance, name only (the UNII and structure are G-SRS's; nothing else of the row confirms them).
- **ambiguous**: two substances share the name, or the row's ChEMBL id contradicts UniChem(UNII). None occurred.
- **no hit**.

The catalogue InChIKey is taken from the catalogue entry of the ChEMBL id that the cached UniChem file (src1 to src14) gives for the UNII (the service returns SMILES, not an InChIKey; no RDKit here, so no key is computed). Nothing was merged by name.

## Result (22 rows)

| Verdict | Rows |
|---|---|
| firm | **10** (nitroglycerin, pivaloyloxymethylbutyrate, 4-phenylbutyric acid, idronoxil, fenebrutinib, tolebrutinib, evobrutinib, abivertinib, berzosertib, tazemetostat) |
| weak | **10** (PX-478, martinostat, pirtobrutinib, elsubrutinib, vecabrutinib, remibrutinib, orelabrutinib, poseltinib, sunvozertinib, gartisertib) |
| ambiguous | 0 |
| no hit | **2** (the antisense oligonucleotide EZN-2968, an oligonucleotide not a chemical record; MSC-2364447) |

So **10 of 22 gain a firm structure**, 10 a weak one (G-SRS structure and UNII exist; identity rests on the name alone, which this brief does not accept as identity), and **2 stay unresolved** (the IT24 22 become 12 still without a firm structure). The scout's earlier probe of MSC-2364447 (no hit) is reproduced. Caveats: nitroglycerin's corroboration is brand names only (all one substance, so accepted, but weaker than a code); martinostat has a UNII and a ChEMBL id but no catalogue InChIKey. Weak rows are candidate identities for a verifier, not results.

## Does it change a family key?

The census R0 to R3 keys for these 22 are empty, so nothing is contradicted. For 19 rows the UNII leads to a ChEMBL id with a catalogue InChIKey. For **12 rows (6 firm: fenebrutinib, tolebrutinib, evobrutinib, abivertinib, berzosertib, tazemetostat; 6 weak: pirtobrutinib, elsubrutinib, vecabrutinib, orelabrutinib, poseltinib, gartisertib)** that ChEMBL id is already a separate `FAM:CAT:CHEMBL...` family in the all-questions table, with the same InChIKey skeleton: the DGIdb-only family and the ChEMBL family are the same structure but were kept as two families (existing twin pairs, as the IT24 verifier noted). The route therefore adds the structure and a twin-family flag; it does NOT merge them: merging stays the job of the existing bridge rule. One notable case: gartisertib's ChEMBL family appears in the table under the name M4344 (a synonym; the G-SRS list and the catalogue agree on the chain, but this was not independently verified here). The other 7 keyed rows (nitroglycerin, PX-478, pivaloyloxymethylbutyrate, 4-phenylbutyric acid, idronoxil, remibrutinib, sunvozertinib) carry a new key not present elsewhere in the table.
Effect on the IT23 LINCS zero (top-20 overlap, 136 rows): not recomputed; a key for 10 firm rows could be added to `recheck_lincs_it24.py` input, which was not done (census scripts untouched).

## What was not done

No terms page of the service itself was read (not renderable); no verifier sample of the joins (scout condition); weak rows not upgraded; census and recheck scripts not edited; no full suites run (only `test_gsrs_trial_it25.py`, 5 offline tests); the IT23 LINCS comparison not recomputed; no ChEMBL or UniChem live query.

## Files

`gsrs_trial_it25.py` (run with `--run` or `--offline`), `test_gsrs_trial_it25.py`, `gsrs_results.tsv`. Reproduce: `gsrs_trial_it25.py --offline --cache <cache> --catalog-cache <catalog cache> --out .` (cache is outside git).
