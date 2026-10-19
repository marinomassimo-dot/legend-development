# Batch self-evaluation — metabolic batch 2026-10-19, group G4, scientist-d

> Written after the analytical work and before capability growth and takeaways. Part 1 was run first; the judgement below was written knowing its verdict. Not medical advice.

## Scope and executable verdict

- **Batch/session:** `METAB-G4-D-20261019`, branch `task/metab-g4-d`, 17 papers read, 2 parked, 3 extra-search items found and closed to retrieval.
- **Receipt IDs (staged, not yet in the ledger):** `FTR-20261019-<PMID>-01` for the 17 PMIDs listed in `metabolic_wave_20261019_scientist-d.md` section 1. All `partial_fulltext_read`; none is `complete_fulltext_read`.
- **`session_self_eval.py --workspace . --disease wwox`:** `VERDICT: PASS`, `unread_premises: 0/0`. The `[DECLARED GAP]` lines it prints belong to five other PMIDs (32000863, 34214506, 35716775, 36779245, 39507621); none concerns this wave.
- **Per-study manifests:** `deepdive_manifest.py --verify-artifacts --require-current-schema` returned `PASS`, zero gaps, for all 17, run from the task worktree with a copy of each XML under the worktree's ignored `files/`. A re-run against the shared checkout's `files/` is owed at landing (the XML digests are the same bytes; the manifests record the SHA-256 of the file in the shared tree).
- **Receipt verification:** `fulltext_receipts.py verify` OK (475 chained receipts). The 17 staged receipts were validated in isolation with `validate_receipt` and `validate_new_receipt`: all OK. None was appended (brief item 3).
- **Structural LINT:** `VERDICT: WARN`, no `BLOCK`; the warnings listed are pre-existing `UNLINKED_SUPPORT` lines on claims this wave did not touch.
- **Concurrent conditions:** `legend_commit.sh` refused four commits as `STALE` because the pathograph is a derived surface that drifts whenever a manifest lands. I committed with `LEGEND_STALE_SURFACES_BECAUSE` naming the parallel batch and leaving regeneration to the Orchestrator (dispatch brief item 3). Recorded in the task JSON as a default taken.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Body and tables read from JATS for all 17; tables extracted cell-wise where nested (Abdygalyk). **No figure image opened in any paper; every receipt says `captions_only`.** Review sections not read in detail are named in each receipt (Dumitrescu, Bagyinszky, Shi, Abdygalyk). No supplement examined. | partial | Figures and the named sections; supplements of the GWAS and microarray papers. |
| Main message and original contribution | Stated per paper in the note; for the group the main message is a negative: no catecholamine, monoamine or glutamate datum exists for WWOX loss of function. | strong | None. |
| Hidden gold beyond keywords/abstract | Four items an abstract does not show: Wainberg's nearest gene is MAF, not WWOX, and the PD side is barely Bonferroni-significant; Ferraro's WWOX is network centrality, not expression; Al Sari contradicts itself and Ng on VMAT2 CSF; Sathe and Stevering disagree on hormonal therapy and the MRI finding. | strong | None. |
| Source parity: context, type and recency | Reviews, case reports and cohort statistics are labelled as such; two reviews disclose generative-AI language help, two have no methods; the case reports are n = 1 to 3. | strong | None. |
| Team type, field density, observation vs interpretation | `group_assessment` and measured `field_density` counts (PubMed `rettype=count`, 2026-10-19) in every manifest. A count of WWOX-and-dopamine hits was first written from expectation in the note and corrected (incident G). | partial | Counts are search hits, not censuses; said so in the manifests. |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Leads L1-L4 and the VABAM-versus-GABA-T imaging comparison are labelled `IPOTESI`; no hypothesis is promoted. | strong | None. |
| Existing claims touched; conflicts/revival triggers | `CLAIM 001` gets a MINOR wave note (`CC-20261019-SCIENTISTD-G4-VABAM-01`, dry-run clean). The WM statement that depolarising GABA is unmeasured is confirmed unchanged. No baseline claim is narrowed or reversed, so the locator audit was not triggered. | strong | The blind audit remains available on the five triples in the candidate. |
| Multi-hop and corpus cross-query | `registry_records.py` run per PMID after the first pass; gene-direct references of Wainberg resolved or queued under real queue IDs (`FT-024`, `FT-109`), Chang 2015 resolved to an existing complete read. Reference lists otherwise counted, not read. | partial | The reference lists of the 16 other papers were not read. |

## Persistence diagnosis

- **Durable IDs:** manifests under `deepdive_manifests/`, staged receipts under `receipt_staging/scientist-d/`, analysis note, two commit candidates, this file, task JSON with `DEFAULTS_TAKEN` and `STOP_LOG`.
- **Reading queue/debt:** parked pair plus three extra-search items in note section 6 and in the REGISTRY candidate; reading debts in section 8.
- **Dossier and commit candidate:** no separate dossier per paper; the analysis note carries the per-paper substance, the manifests carry the locators. A comparator paper with no registry record gets its identity record from the REGISTRY candidate.
- **Receipt source fingerprint, coverage and supplement state:** SHA-256 of the XML in every receipt; coverage uses the closed vocabulary and understates (`captions_only`, `not_read`).
- **Can a future run distinguish full text from abstract only?** Yes: `source_kind: fulltext_local`, a fingerprint, `coverage` per section, and a manifest whose locators are verified against the body surface (the validator refused two locators that matched only the abstract).

## Process and capability diagnosis

- **Skills/gates/patterns used:** `paper_packet.py packet/check`, `deepdive_manifest.py` strict, `dependency_integrity.py screen --manifest-block`, `registry_records.py`, `record_scoped_edit.py` dry run, `find-fulltext` for the parked pair.
- **Plausible skills deliberately declined:** `legend-deepdive` (run inline), `legend-discovery` and `legend-hypothesis-forge` (no comparator paper matures a lever), `legend-safety-triage` (no compound proposed), `legend-locator-audit` (no baseline claim narrowed; triples offered to an auditor in the candidate), `legend-paperqa` (external spend).
- **Failures, retries, concurrency events:** see the census. The wave also ran on a single generator script that built manifest and receipt from a per-paper spec; the spec author (me) was the only check on whether a proposition said more than its quote.
- **What caught each failure before an overclaim:** see the census.
- **Disease-agnostic micro-upgrade shipped:** `paper_packet.py check --artifact-workspace <root>` passes the artifact root to the manifest validator, so a task worktree that holds a manifest but not the ignored `files/` tree can be checked without copying evidence into it.
- **Regression/evidence:** `ArtifactWorkspacePassthroughTests` in `framework/scripts/test_paper_packet.py` (69 tests, OK); manual run: with the worktree's `files/` moved away, `check --root . --artifact-workspace <shared root>` returned PASS where the same call without the flag returned a BLOCK ("artifact path escapes the workspace" when `files/` was a symlink; "No such file" when absent).
- **Residual risk and next decisive action:** the one real hole in the record is that no figure was opened; the decisive next acts are retrieval of the three closed-access WWOX-specific items, Nishino 2024 first, and reading the unread WWOX VABAM anchor.

## Attribution census

Incidents, one per defect or near-error, repeated instances of one class counted once:

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest schema rejections: `research_type` outside the closed list, field-density query list empty, snippet under 30 characters (7 instances over 4 papers) | machine | no |
| B | Two locators whose quote occurs in the abstract only (Sathe, Shi) | machine | no |
| C | Wainberg: gene-direct references neither resolved nor queued; first draft listed them as prose | machine | no |
| D | Proposition says more than its quote in six manifests (Naranjo-Lobo, Sugiyama, Stevering, Alammary, Nikkhah, Almutair; and an absence claim in Dumitrescu supported by a quote that cannot show absence). The validator checks that a quote exists, not that it supports the proposition | self (re-reading each spec against its snippets before committing; corrected before the commit) | would have |
| E | The selection file says the VABAM anchor (Choi 2026) was read; the ledger has no receipt and the anchor audit says it is blocked | self (cross-check with `fulltext_receipts.py status` and the 2026-09-21 anchor audit) | would have |
| F | The selection file says WWOX was "retained as a neurodegeneration player" in the nigral expression paper; the paper reports no WWOX expression value | self (reading the paper) | would have |
| G | The note's first draft described the three WWOX-and-dopamine search hits from expectation; re-running the search showed they were different papers | self (re-derived from the command output before saving) | would have |
| H | My text renderer skipped tables nested inside paragraphs, so a string search said WWOX was absent from the infantile-spasms review while its gene table has a WWOX row | self (cross-measurement against the raw XML, which the brief's rule on counts requires) | would have |
| I | `paper_packet.py check` could not resolve artifacts from a task worktree | machine | no |

```
ATTRIBUTION_CENSUS
incidents: 9
machine: 4   blind_auditor: 0   peer: 0   self: 5
severity_high: 5   of which self: 5
undetected_known: 0
```

**Reading of the census.** All five incidents that could have reached the record were caught by my own re-reading or cross-measurement; every machine catch was a malformed declaration. That ratio flatters the readers only partly: incident D exists because the validator is blind to a proposition that outruns its quote, and I was the only control on it. `undetected_known: 0` cannot be trusted, since the census is written by the actor; the figures-never-opened debt is the one known soft spot and is declared, not hidden. No blind audit was run (no triple was submitted to the blind-audit skill), so `blind_auditor: 0` is a statement about what I did not do.
