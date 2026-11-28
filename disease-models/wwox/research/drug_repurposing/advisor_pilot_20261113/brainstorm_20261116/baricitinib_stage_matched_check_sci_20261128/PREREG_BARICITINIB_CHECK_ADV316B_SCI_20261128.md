# Baricitinib bounded dataset check: frozen note before any search (SCI bb, 2026-11-28)

Hypothesis level; not medical advice. ADV approval 2026-11-28 (route 2 of LAB-RESUME-COMPOUND-FOLLOWTHROUGH-20261128). Consumer: INV-14 (inflammatory fork) and the baricitinib dossier's reopen condition (continuous_compounds/baricitinib/README.md, "One discriminating comparison"). Nothing in this note is a result.

## Question
Does any held or public dataset hold, in ONE developing mouse (or other) model with a WWOX-related or comparable glial/myelin lesion, a stage-matched pSTAT3 (Y705) or JAK-STAT-dependent glial marker readout together with an animal-linked functional readout (myelin, conduction, seizure or behaviour per animal)?

## Two explanations (fixed before the search)
* **E-INFL (inflammatory target engagement):** a local excess of gp130/IFN-family signalling (pSTAT3 or pSTAT1, reactive-glia markers) rises BEFORE the functional defect at matched initial activity, so lowering it should help.
* **E-TROPH (loss of trophic support or downstream state):** the STAT3 signal is a CNTF/LIF-dependent maintenance or injury response that follows neuronal or oligodendroglial loss; lowering it removes support.

## Predicted observable (what each explanation says the dataset would show)
* E-INFL: in a stage series, pSTAT3 or the glial marker is already raised at the youngest age before the functional or structural deficit, and per-animal marker level correlates with the later deficit.
* E-TROPH: pSTAT3 rises at or after the deficit, tracks neuronal or precursor loss, and loss of Stat3 in the lineage worsens the structural outcome (the known neonatal Stat3 conditional result already in the dossier points this way).
Prior expectation (stated before searching): such a matched, animal-linked dataset is NOT held or public (dossier: "no such matched dataset was retrieved"; RP-012: pooled libraries and bulk composition make public reuse unanswerable). I expect NONE; a single qualifying dataset is the rejecting observation.

## Qualifying rule (frozen)
A dataset qualifies only if ALL hold: (1) one model; (2) at least two ages including one before the first functional or structural deficit; (3) pSTAT3/pSTAT1 or a named JAK-STAT-dependent glial marker measured per animal or per section with n stated; (4) a functional or structural readout for the SAME animals (linked by animal or litter id, or plotted per animal); (5) the raw values or per-animal figure points are held or openly downloadable. Partial matches are listed as near-misses, never as qualifying.

## Method and stop rule
1. Ledger lookup by PMID in fulltext_read_receipts.jsonl and files/fulltext for any paper named from the dossier, the portfolio and the anakinra/INV-14 records (the dossier's Stat3 conditional model, the opposing developmental study, the Laitman workbook).
2. Public deposits (GEO, PRIDE, Zenodo, Figshare, Dryad, SRA metadata) with abbreviation searches (Stat3, pSTAT3, Gfap, Lcn2, Socs3, Cntf, Lif, Wwox) AND the article data statement.
3. Check animal and sample ids, not only gene names, in the duplicate check against the receipt ledger and the portfolio.
4. Stop after one pass of 1 to 3 (no re-scoring of already-replayed aggregates). If none qualifies: register the exact missing observation in the portfolio row text (sent to ADV to land) and take the next held-source question with a named consumer. A challenge page, 401, 403 or 429 is a result.
