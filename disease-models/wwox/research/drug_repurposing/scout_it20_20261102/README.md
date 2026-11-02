# IT20 P7 - capability-led radar tied to the named gaps (2026-11-02)

Non-canonical research material; not medical advice. Questions come from `../diagnosis_it20_20261102/README.md` (provenance through intermediaries, specific pharmacology, matching evaluation, public presentation). Queries started from the capability, not from the gene name. `decisions.tsv` has the shape of the earlier scout tables; rows starting WATCH / NEEDS-DATUM / PARTIAL are open and carry reopen conditions. Verdicts are for the stated question; a metadata triage is not a trial; a licence not read is not a prohibition. PROTON, BioPathNet, MATRIX, TxGemma, OREVID, npj benchmark, DrugAudit, EuTxGNN, Chem-PerturBridge, CLAMP and DeepPurpose were not reopened and nothing concrete about them was seen to change.

## What was found, by question
- **Q1 provenance.** Two things the module may already hold. (a) DGIdb interactions in the repository's own raw files carry a per-source version string (ChEMBL "37", GuideToPharmacology "2026.2"), so the release of a republished claim is already present. (b) ChEMBL's own mechanism and target endpoints (the one trial, below) carry the target type, component count, literature references and the release. The open piece is therefore a join and a field naming convention, not a missing external resource. The Biolink Model slots primary_knowledge_source (most upstream source) and aggregator_knowledge_source (intermediate republisher) give an established vocabulary for keeping the two apart (names only). ProvBench EGFR shows the same split in a flat table (source, access path, document, assay) but for one target and without a release column.
- **Q2 specific pharmacology.** A 2026 series comparing PDSP Ki records with Guide to Pharmacology per receptor subtype (with radioligand and assay system) is a method template; ion channels are 1.7 percent of its largest set and the per-ligand tables are in journal supplements, not read. Nothing located yet that carries Cav3.2 measurements to the engine without a name exception.
- **Q3 matching evaluation.** BenchAudit (Chem Sci 2026) audits duplicates, label conflicts and ligand/protein overlap in DTI benchmarks; it matches the three failure types but was not run (heavy pinned dependencies; inputs are train/test splits, the reference is 32 pairs). SCOPE-DTI builds a merged, balanced set and was judged on metadata only.
- **Q4 presentation.** The Translator release paper describes progressive disclosure of evidence, provenance and confidence; design reference only. EviDTI's uncertainty is a model score, not evidence uncertainty.

## The trial (one, small, free)
`chembl_mechanism_trial.py` (stdlib only, no install, no venv needed, writes nothing): for terodiline, suloctidil, phloroglucinol and bepridil, reads the ChEMBL molecule, mechanism and target endpoints. Release ChEMBL_37 (2026-05-01). Suloctidil and phloroglucinol each have one mechanism, action type BLOCKER, target CHEMBL2363032 of type PROTEIN COMPLEX GROUP (Voltage-gated calcium channel, 26 components), with literature references (suloctidil three, phloroglucinol one). Terodiline and bepridil returned no mechanism under the preferred-name molecule, so their DGIdb ChEMBL claim must come from another record form; salts, parents and activity-derived claims were not checked. Cost: about 20 public GETs including a repeated run, 1.5 s apart, no errors, no files kept. This shows the fields exist at source; it does not show the engine uses them.

## Channels (approximate counts)
| Channel | Requests | Waits | Errors |
|---|---|---|---|
| GitHub search API | 6 searches + 1 rate-limit check | 8 s between searches | 3 x HTTP 403 after 3 x HTTP 200 with zero items; channel stopped as instructed, cause (search quota or secondary limit) not examined |
| Hugging Face (datasets and models search, cards, 1 CSV of 24 MB deleted) | about 60 | 3 s | 2 gated cards unreadable without login (no account made) |
| Europe PMC / Crossref / PyPI / Zenodo / Biolink docs / ChEMBL | about 60 | 1.5 to 3 s | 1 x 404 (DGIdb GET path, not retried) |

Group count: eight groups were met at metadata level (above the 6-team guide); only Seifert, Sieber (BenchAudit), the Biolink/Translator documentation and ProvBench were read beyond abstract or availability statement. No raw README was imported; no e-mail or personal data copied; no operator address sent anywhere.

## What the radar's planned questions should change
1. Add a question: can the engine join DGIdb per-source versions with the ChEMBL mechanism target type and references without a name list (Q1, now an engine task rather than a search).
2. Replace "find a provenance resource" by "trace terodiline and bepridil DGIdb ChEMBL claims to a ChEMBL record form".
3. Re-run the GitHub channel with short queries (listed in decisions.tsv) once the quota allows.
4. For Q2, ask for a supplement table with channel subunits before any more database-comparison papers.
