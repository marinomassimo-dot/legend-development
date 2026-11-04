# IT27 P13: targeted scouting, five named gaps (2026-11-04)

Non-canonical. Not medical advice. Zero spend; no registration, login or contact; no e-mail address sent anywhere. Only
generic topic words went to the search service; no compound list and no gene panel. Nothing installed, cloned or downloaded;
no third-party raw data imported. WWOX was not used as a keyword. Reuses the IT22/IT23/IT24 verdicts (SIGMA-KG, scPerturb,
G-SRS, hiPSC NPC drug screen, KG-Bench, IxIDN, Papyrus, DTC, EUbOPEN, B3DB are not repeated). Table: `candidates.tsv`.
Depth caveat: one bounded window, web search plus two page reads; repositories were not opened, so code revisions are unread.

## Gaps and verdicts

| Gap | Hit | Verdict |
|---|---|---|
| G3 direct v indirect action | Van Vranken et al., proteome-wide thermal shift (PISA) in cells and in lysate, 96 compounds, eLife 2024 (PMC11554310), raw data on PRIDE (accession reported by a search summary only: PXD048009, not verified) | **TRIAL** (data only, about 3 h) |
| G1 partial v complete loss; composition v within-cell-type | iPSC-derived astrocyte and microglia CRISPRi screens with single-cell readout (GEO GSE182307 astrocytes, submitted 2021-08-24; Drager 2022 microglia) | **WATCH** |
| G2 assay-matched potency/selectivity, class IIa, EZH2/1, ROCK2/1, IAP | nothing new: only vendor datasheets and one Promega assay note for TMP269 | **nothing new** |
| G4 benchmark with reusable controls | GraphGuest (arXiv 2311.12670, biologically driven negative sampling, Python package) | **WATCH** (repository unread) |
| G5 identity/collision offline | preon (PyPI, name normaliser, exact-match F1 about 87 percent in its paper) | **WATCH**, low value |

## Reading notes

**G3 (the one useful hit).** The paper runs the same compounds in live cells and in lysates. A shift in lysate is read as direct
binding (signalling is disrupted there); a shift in cells only is read as downstream. The text read names eight HDAC inhibitors
(vorinostat; HDAC1 repeatedly stabilised), a ROCK1-directed compound (GSK429286A) and says ROCK1/2 behave as correlated in the
kinase network; EZH2 and IAP/SMAC mimetics are not mentioned in the portion read (about 40 percent of the page, the compound
list is in Supplementary file 1, not read). The authors themselves flag that some lysate changes (vorinostat among them) may be
artefacts, so lysate is not clean proof of binding. Licence: article CC BY 4.0; supplementary and PRIDE terms not read.
What it can do for LEGEND: for the compared families, give a cell-versus-lysate tag on whether a protein is directly engaged,
as an annotation on an action claim, never as potency. Smallest test: read Supplementary file 1, list which compared-family
compounds are present (expect HDAC1/2 and ROCK1 inhibitors, probably no TMP269, EZH2 or IAP compounds), and stop if fewer than
three compared compounds are covered. Cell type is a cancer line, not neural: context, not support.

**G1.** CRISPRi lowers expression; it does not delete, so it brackets partial loss from one side and cannot give a complete-loss
arm. Single-cell readouts do separate within-cell-type change from composition inside one culture, but these are monocultures
of one iPSC-derived cell type, so they do not address tissue-dissection confound of bulk brain deposits. Whether any panel gene
was targeted is unstated on the pages read (the astrocyte record lists none; the page reports STAT3 and IRF1 as highlights).
The GEO title says bulk RNA-seq although the abstract says single-cell. Reopen if a gene-by-gene target list shows a panel gene,
or if a dosage-series perturbation in neural cells appears. Complements the open IT24 P13-3 scPerturb check; do that one first.

**G2.** TMP269 class IIa IC50 values on vendor pages (about 157, 97, 43, 23 nM for HDAC4/5/7/9) are vendor-restated and I could not
tie them to a primary methods section; the Promega page is a format-specific live-cell luminogenic readout with its own substrate.
Neither is assay-matched across the family. Not adoptable; the primary paper stays a dossier reading.

**G4.** The search surfaced no 2026 benchmark with reusable controls beyond the IT24 ones. GraphGuest addresses leakage and negative
sampling in drug-target graphs; I did not open its repository, so licence, revision and whether it is a method or reusable
control set are unknown. Reopen after reading the repository.

**G5.** The tools found split the problem: name matching (preon, no explicit salt or stereo handling in the summary read), rule-based
salt-keeping (NLM 2010 study: strip most salts, keep where an ingredient has several salt forms), and structure-based parent
extraction (RDKit standardiser, already in the environment per the safety-triage skill). The gap that remains is the collision
check itself (one code or synonym mapping to two parents), and none of these provides it; it is a few hours of in-house code over
the existing UniChem and G-SRS routes, not an import.

## Negative result

For gaps G2 and G5 nothing new beats what is held. No adoption quota applies.
