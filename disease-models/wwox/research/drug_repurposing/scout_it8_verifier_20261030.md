# Independent verification of scout_it8_20261029.md (verifier, 2026-10-30)

Read-only checks against primary sources (GitHub API and raw files, PyPI JSON, NCBI GEO esummary and SOFT text, Europe PMC full text and metadata). No e-mail address or personal datum was sent to any service. Nothing installed.

## 1. Verdict

The report is accurate on existence, licences and dates for every item checked. One factual error (B3DB lithium), two imprecise statements, and several items left UNVERIFIED by the scout that remain unverified here. No licence is mis-stated; the non-commercial / share-alike items are all flagged by the scout.

## 2. Item-by-item

| Item | Existence / date | Licence (primary) | Claim check | Result |
|---|---|---|---|---|
| PavlidisLab/CMap-Evaluation | exists; last push 2021-12-15 | GPL-3.0 (API) | as stated | CONFIRMED |
| Lim and Pavlidis 2021, PMC8413422 | Sci Rep 2021 | Europe PMC: CC BY | full text: correct compound top-10 % (rank <= 68) for 99/588 signatures = 17 %; mean CMap1-CMap2 correlation 0.05-0.11; top-10 % = rank <= 68. The scout says "recommends lower confidence for self-retrieval rank above 68" and "at least 3 replicates / 3 concentrations": the 68 threshold is the paper's top-10 % cut; the replicate recommendation was not located by my keyword search (not checked beyond that) | MOSTLY CONFIRMED; the recommendation sentence UNVERIFIED here. Note the paper states CC BY in metadata only ("cc by"); scout says CC BY 4.0, version not confirmed |
| cmapPy | exists; push 2026-08-26 | BSD-3-Clause | as stated | CONFIRMED |
| GSE295444 / GSE295447 | both public 2025-04-30, 840 samples each, QuantSeq 3' mRNA-seq, 7 h, 12 compounds in 0.1 % DMSO, authors as listed, BioProject PRJNA1254690 for set 1 (PRJNA1254692 for set 2 not checked), only RAW.tar as supplementary | no licence line in SOFT record; GEO reuse terms not stated in series | Per-compound counts, cell lines, per-neural-arm numbers not re-derived (needs sample-level parsing). Series design text matches | EXISTENCE and DESIGN CONFIRMED; reuse terms UNVERIFIED (agree with scout) |
| GSE322511 (8 samples, public 2026-10-24), GSE308370 (9 samples, public 2026-03-19) | confirmed by esummary | none stated | sample counts and dates match; AKT3 / rapamycin text consistent | CONFIRMED |
| B3DB (theochem/B3DB) | exists; push 2025-09-10 | CC0-1.0 (API and LICENSE file "CC0 1.0 Universal") | classification TSV has about 7,809 rows and regression about 1,060 (scout/paper: 7,807 and 1,058; 2-row difference, likely file version, immaterial). Hits confirmed: ethosuximide, vigabatrin BBB+, sirolimus, bumetanide BBB-. **ERROR: lithium IS present** (classification row listed under CAS 7439-93-2 / "lithium", BBB+, logBB -0.3; regression has it too). The scout wrote "no hit for ... lithium" and "logBB only ethosuximide -0.3, valproate -0.2". Correct: logBB for three of the names (ethosuximide -0.3, valproate -0.2, lithium -0.3). Also the TSV has several rows whose name column says "ethosuximide" but whose structure is a different compound (rows 3949, 4458): a name-only match is unsafe | PARTLY WRONG. Lithium is a firewalled compound, so this matters for the card cross-check. Source-dataset terms (50 papers) not checked, agree |
| chembl_structure_pipeline 1.2.4 | PyPI 1.2.4 released 2025-11-24 | PyPI MIT; GitHub API MIT | The 5-of-8 parent test was not re-run (no venv built) | Existence, version and licence CONFIRMED; test result NOT REPRODUCED |
| rdkit | exists | BSD-3-Clause (API) | scout cites rdkit 2026.9.1; not checked | licence CONFIRMED |
| OREVID (orevid-org/orevid) | exists; push 2026-10-29; Zenodo DOI 10.5281/zenodo.23323226 and Preprints.org citation in README | code MIT (API, LICENSE); LICENSE-DATA.md: derived data and results **CC BY-NC-SA 4.0**; PrimeKG sources DrugBank CC BY-NC, SIDER/DisGeNET CC BY-NC-SA; CTD kept out; "Not for commercial use" | README confirms: zero-shot Recall@100 0.811 vs TxGNN 0.412; 0.809 vs 0.421 after adjustment; temporal 0.283 vs 0.181; hidden lines 2-4 %; direct extensions 13-59 %; hubs (>= 500 diseases) excluded; hub candidates right 1-3 %. docs/LINCS.md confirms 2,410 drugs, 239 diseases, temporal reversal Recall@100 0.055 vs random 0.055. "0.59 before, 0.37 strict" not located in README (may be in a doc; UNVERIFIED). Zenodo licence field not read (same as scout). Preprint page not reachable by the scout and not retried here | CONFIRMED; single-author self-benchmark caveat is correct. NC-SA flag is correct and complete |
| TxGNN | repo is mims-harvard/TxGNN (the path TxGNN/TxGNN does not exist); MIT; push 2024-05-06 | MIT | as stated | CONFIRMED |
| MATRIX (everycure-org/matrix) | push 2026-10-27 | Apache-2.0 (code) | scores licence limit is from a different record; not re-fetched | code licence CONFIRMED; scores licence UNVERIFIED (agree) |
| Pharm Res 2025 (10.1007/s11095-025-03828-0) | Europe PMC: "Prediction of the Extent of Blood-Brain Barrier Transport Using Machine Learning and Integration into the LeiCNS-PK3.0 Model", 2025 | cc by | licence matches scout | CONFIRMED |
| Morales 2024 (10.3389/fddsv.2024.1360732) | not in Europe PMC | not found | agree: UNVERIFIED | UNCHANGED |
| NeMoCAD, DrugReX, XG4Repo, molIEreVIS, UniChem, orchestration arXiv titles, similarity-bias preprint | not opened | not read by the scout either | scout labels them WATCH / UNVERIFIED, which is honest | not verified here either |

## 3. Flags: licence classes

- Non-commercial / share-alike: OREVID data and results (CC BY-NC-SA 4.0), correctly flagged and the TRIAL is limited to the design. Upstream NC terms in PrimeKG (DrugBank CC BY-NC, SIDER/DisGeNET CC BY-NC-SA) correctly named. NeMoCAD (restricted, non-commercial) carried from iteration 7, not re-fetched.
- Copyleft: CMap-Evaluation GPL-3.0, correctly "do not import".
- Gated or unstated: GEO series GSE295444/GSE295447 (no licence line; reuse terms unstated), Morales 2024 supplement, MATRIX scores. All flagged UNVERIFIED by the scout; none promoted beyond TRIAL/WATCH.
- No licence found that is stricter than the scout stated.

## 4. ToolUniverse-Reactome verdict scope

The scout report does not issue a ToolUniverse verdict: it says only "ToolUniverse was NOT reinstalled (no new named need)". The verdict comes from the iteration-7 entry in capability_scout_log.md (24-call Reactome trial by UniProt accession; decision REMOVE). The trial's own bullet is scoped to Reactome-by-accession. The later iteration-7 "Not adopted" bullet reads "ToolUniverse removed after the Reactome trial (adds only a 404-as-success hazard)": the words "adds only" generalise beyond the single trial (the iteration-6 entry separately gave WATCH on the GluN2B ChEMBL/GtoPdb check, and the log's "Not verified" bullet admits other ToolUniverse categories were not tested). Assessment: the evidence supports "the Reactome wrapper has no advantage and one hazard"; it does not support a general statement about ToolUniverse. Suggested wording: "removed after a Reactome-only trial; other categories untested". The iteration-8 report/log entry itself does not restate or extend the verdict, so it is within bounds.

## 5. Structure requirements

- Two complementary searches: NOT met as written. The report's section 3 lists one pooled set of 14 web searches plus GEO, GitHub and Europe PMC probes, organised by named gap (G-a to G-g), and does not separate (1) science relevant to the needs from (2) methods / tools / datasets / practices. In substance both occur (G-b, G-c, G-d are science; G-a, G-e, G-f, G-g are methods) but the report never states them as two searches. Recommend a one-line split in section 3.
- No installation quota: MET. The perimeter says "Verdicts are not a quota"; one venv was built for a named gap and deleted; ToolUniverse not reinstalled; no minimum count of installs or adoptions appears. Verdict mix (1 ADOPT reading, 4 TRIAL, several WATCH, 3 REJECT) is consistent with need-driven selection.
- No duplicated monitor: MET. The scout proposes no new monitor or watcher; section 4 only reads the existing daily radar and hourly control. It notes the radar log/JSON discrepancy (SigCom-LINCS etag) without adding a probe. No new cron, script or watch is introduced.

## 6. Corrections to request

1. B3DB: lithium is present (BBB+, logBB -0.3, listed under CAS 7439-93-2); change "no hit for ... lithium" and "logBB: ethosuximide, valproate only". Add that the name column has mismatched structures for some rows, so match on structure/InChIKey too.
2. Section 3: state the two complementary searches explicitly.
3. Soften the "adds only a 404-as-success hazard" wording in the iteration-7 log to Reactome-only scope.
4. Mark "0.59 before, 0.37 strict" and the Lim and Pavlidis replicate recommendation as not located in the primary text by the verifier.

Limits of this check: sample-level GEO counts, the chembl_structure_pipeline SMILES test, Zenodo and Preprints.org pages, and all WATCH items were not re-examined.
