# PMID 25331887 — supplementary completion preflight blocker

Date: 2026-08-12  
Workspace: `<WORKTREE:legend-codex-partials>`  
Branch: `codex/pmid-25331887-29724996-38499540-partials`  
Starting HEAD: `d06a4a162359a9e949e577198a183173cf08c665`  
Artifact workspace required by the operator: `<REPO_ROOT>`  
Status: `BLOCKED_BEFORE_SUPPLEMENT_READ` — this is not a `complete_fulltext_read` and no new receipt was emitted.

## Scope and sequencing

This session opened only PMID 25331887. PMID 29724996 and PMID 38499540 were not opened because the operator required each paper to close independently before the next paper begins.

The scientific current registries were not modified. No `BATCH_COMMIT` was requested. No file under `framework/scripts/` or `framework/state/` was modified.

## Gate and receipt preflight

- `framework/state/state_manifest_current.md` reports `current_state: READY`.
- `python3 framework/scripts/legend_lint.py .` returned `VERDICT: PASS` with only the pre-existing informational `MISSING_WIKILINK` note for CLAIM 010.
- `git for-each-ref --format=%(refname)` enumerated 25 refs.
- For every ref, `git show <ref>:disease-models/wwox/registries/fulltext_read_receipts.jsonl` was parsed in full. Ledgers contained 34–106 events depending on the ref.
- Every ref containing a PMID 25331887 event contained the same prior event: `FTR-20260810-25331887-01`, `partial_fulltext_read`, with `prior_receipt: null`.
- The new completion receipt, if the blocker is lifted, must therefore declare `prior_receipt: FTR-20260810-25331887-01`.
- Instruction discrepancy: the operator described the prior debt as `supplementary: not_read`; the authoritative current ledger records `supplementary: unavailable`. The existing manifest states that S1–S7 were not read and that the unavailability of the supplementary PDF is the sole reason the receipt remained partial.
- `python3 framework/scripts/fulltext_receipts.py verify` returned `OK: 93 chained receipt(s), tail anchored in framework/state/state_manifest_current.md`.

## Primary surface and artifact verification

Primary text surface: `files/fulltext/PMID25331887_AbuOdeh2014_PMC.html` (PMC HTML). The PDF was not used as a text surface.

| Artifact | Bytes | SHA-256 | Verdict |
|---|---:|---|---|
| `PMID25331887_AbuOdeh2014_PMC.html` | 219148 | `8c629a545f7cc6961dfe349148a2878709f046e6892d33328eda7dbbf3c008f2` | exact match |
| `PMID25331887_AbuOdeh2014.pdf` | 1880319 | `42df070aa1f699ad84a654e8526d9a332731219f66c9a9f640d870d7ae6b4642` | exact match |

Verified identifiers: PMID 25331887, DOI `10.1073/pnas.1409252111`, PMCID `PMC4226089`.

The authoritative validator source was read from `git show d06a4a1:framework/scripts/deepdive_manifest.py` and executed with `PYTHONPATH=framework/scripts`. Its `--font-screen` verdict for the PDF was `0 UNTRUSTWORTHY · 0 SUSPECT_FONTS · 1 UNDECIDED`; this is not a clean verdict and the PDF text layer was not touched or normalized.

## Main-figure inventory and PPI preflight

The PMC structure contains seven main figures, enumerated from captions as Figures 1–7. The existing persistent artifact directory was initially missed by a basename-only search and then found by a path-aware inventory:

`<REPO_ROOT>/files/fulltext/PMID25331887_AbuOdeh2014_assets/`

It contains seven publisher JPEGs and seven lossless PDF-xref PNG extractions. All seven PNG digests match the manifest:

| Figure | PDF page / xref | Native pixels | Effective PPI ceiling | PNG SHA-256 |
|---|---|---:|---:|---|
| 1 | 2 / 20 | 682×717 | 200.0 | `c8c485e40c36a046da1039179a5593d00960fb05c2ff0203f4aa42bcc79790bd` |
| 2 | 3 / 98 | 1397×1007 | 200.0 | `08ce0765e19c9ce60a3dd201a3ac16c9ae7c646ddaa9c54e00217a82cd44acae` |
| 3 | 4 / 171 | 1397×1029 | 200.0 | `1c5427f53eb5b30467365cfcc5ea2f336786afe8c504dd0625ae69435e643250` |
| 4 | 5 / 9 | 1397×1051 | 200.0 | `6af07e05611e032ae200c2f65aa7b7f70563178ba222955940aabb6db4bc02c5` |
| 5 | 6 / 85 | 682×1144 | 200.0 | `608c91c299aa07ea6f548b8809b0c7614cdefc997bd54c5140190ebeaa2b9a03` |
| 6 | 7 / 160 | 1397×859 | 200.0 | `9c075363ce9a8f63e7700c1a7ddf9c4e385b5f5af5e54de6d8bcc0fe7cca1f53` |
| 7 | 8 / 221 | 682×1012 | 200.0 | `5e3e59178f0e388e9fd0dff4ff1a7ba5dbc0af4b487592e90b035f260d7c1282` |

`framework/scripts/figure_ppi_preflight.py` was run before any rendering. The repeated page-decoration raster has a 144.0 ppi ceiling and is not a scientific figure. No new rendering was performed.

The existing partial manifest already records pixel inspection of all seven main figures and `panel_text_relation` for every locator. Running the validator from commit `d06a4a1` with:

```bash
git show d06a4a1:framework/scripts/deepdive_manifest.py | \
  PYTHONPATH=framework/scripts python3 - \
  --workspace <WORKTREE:legend-codex-partials> \
  --artifact-workspace <REPO_ROOT> \
  --disease wwox --pmid 25331887 \
  --verify-artifacts --require-current-schema
```

returned `VERDICT: PASS` with zero manifest gaps. That verdict certifies the existing partial reading and its main-figure artifacts; it does not convert the unread supplement into a complete reading.

## Supplement denominator and retrieval attempts

The body and captions cite Supplementary Figures S1–S7. The supplement is identified as `pnas.201409252SI.pdf` (approximately 1.5 MB). The existing manifest names load-bearing content in S2B, S3C, S4, S6C and S7B; therefore a caption-only or text-only substitute would not close the visual debt.

The first retrieval action after the figure inventory was the operator-mandated endpoint:

`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4226089/supplementaryFiles`

Observed tool outcomes:

1. Web open: refused before the HTTP request with `URL ... is not safe to open (non-retryable error)`.
2. Terminal `curl`: `Could not resolve host: www.ebi.ac.uk`.
3. In-app browser: `No browser is available`.
4. Publisher deterministic PDF route: web open refused the binary URL as unsafe.
5. Web search resolved the PMC record and independently identified the file as `pnas.201409252SI.pdf`, but search-result text is not the PDF and cannot support a full-text or figure read.

These are tool/environment refusals, not an observed Europe PMC HTTP status and not evidence that the article is non-OA.

## Blocking condition

The runtime write allowlist excludes `<REPO_ROOT>/files/`, although the operator explicitly authorized that directory as the only valid artifact sink. The direct, in-scope creation attempt:

```bash
mkdir -p <REPO_ROOT>/files/figures/PMID25331887
```

failed with:

```text
mkdir: <REPO_ROOT>/files/figures/PMID25331887: Operation not permitted
```

Writing the supplement or derived figures only into `<WORKTREE:legend-codex-partials>` would violate the evidence-locality rule and the operator's explicit warning that a green manifest with worktree-only artifacts is not reproducible. Therefore no substitute artifact was created, no supplement was claimed as read, no manifest was upgraded, and no `FULLTEXT_READ_RECEIPT` was appended.

The same sandbox boundary also prevents version-control writes in this otherwise writable worktree: its Git administrative directory is linked to `<REPO_ROOT>/.git/worktrees/legend-codex-partials/`. Staging and committing this report failed twice at index creation with:

```text
fatal: Unable to create '<REPO_ROOT>/.git/worktrees/legend-codex-partials/index.lock': Operation not permitted
```

The report therefore remains an untracked workspace file. No commit coordinate can be truthfully reported.

## What is needed to resume

Either of the following is sufficient:

1. add `<REPO_ROOT>/files/` and `<REPO_ROOT>/.git/worktrees/legend-codex-partials/` to the runtime writable roots and provide network/browser access to the Europe PMC endpoint; or
2. have the operator place the lawful `pnas.201409252SI.pdf` bytes under `<REPO_ROOT>/files/fulltext/`, then resume from fingerprinting, PPI preflight, full sequential supplement reading and visual inspection of S1–S7.

The next receipt must link to `FTR-20260810-25331887-01`; it must not be minted as a parallel first read.

## Capability micro-upgrade

Reusable preflight rule: image-presence checks must match the full path or inspect the paper-specific artifact directory. Searching only basenames for a PMID can falsely report that `Fig1.png`–style artifacts are absent. The corrected inventory found all fourteen main-figure images and prevented an unnecessary duplicate extraction.

## Post-session self-diagnosis — Part 2

Executable verdict first: workspace self-eval PASS with six pre-existing unread-premise lines at the anchored 6/6 baseline and fourteen pre-existing declared gaps; PMID 25331887 manifest strict PASS; receipt ledger PASS at 93 events; structural LINT PASS. These checks validate existing state. They do not test whether the newly requested supplement was acquired or read, so the local outcome remains blocked.

### Sources and depth

1. **Section-by-section and image reading:** no new scientific reading was claimed. The existing receipt and manifest show complete body/main-figure coverage, but S1–S7 remain unread. Anchor: “Supplement denominator and retrieval attempts”.
2. **Reading against disease labels:** not reached in this continuation. The prior manifest classifies the cancer/MEF paper as mechanistically transferable; this session did not alter that judgment.
3. **Hidden finding beyond keyword search:** not assessed anew because the supplement bytes were unavailable. The process finding was hidden by a basename-only file inventory, not by scientific text.

### Group and field density

4. **Group identity:** reused, not recomputed: the existing manifest records Aqeilan as a primary experimental WWOX group (137 total publications; 65 WWOX, measured 2026-08-10).
5. **Evidence type:** experimental laboratory; the requested missing evidence is visual supplementary experiments, so abstract/caption text is not an adequate substitute.
6. **Inexperience-predicted error:** not applicable; the existing manifest instead separates strong observations from repeated interpretive absolute negatives in a gene-primary group.
7. **Field density:** reused from the existing manifest; no current web count was introduced as new evidence.

### Epistemics

8. **Door-closing conclusions:** none added. Retrieval failure was not converted into “supplement unavailable in principle”; it is stated as a runtime limitation with a revival condition.
9. **Shows versus claims:** preserved. Search snippets identifying `pnas.201409252SI.pdf` were not treated as the supplement or as evidence.
10. **Extraction fault versus author error:** the PDF text layer received only `--font-screen`; its `UNDECIDED` result did not license extraction or normalization.

### Compounding and landing

11. **Durable landing:** this blocker and micro-rule land in this versioned session-evaluation file. No scientific ledger entry was added because no new finding was established.
12. **Multi-hop:** not applicable to a blocked supplement retrieval; existing manifest multi-hop remains unchanged.
13. **Corpus cross-query:** not repeated. The prior manifest's cross-query is preserved; repeating it would not close S1–S7.
14. **Touched claims:** none newly touched; no canonical claim or registry was modified.
15. **Reading debt:** remains mechanically visible through `FTR-20260810-25331887-01` and the existing manifest; no false completion event was appended.

### Capability and process

16. **Capability growth:** path-aware figure inventory is disease-agnostic and prevents false absence reports for any paper whose image filenames omit the study identifier.
17. **Breakage:** three access routes failed and one inventory assumption failed. The route failures are recorded verbatim; the inventory defect was corrected during the session.
18. **Check caught the session:** strict artifact validation contradicted the initial absence claim, prompting the path-aware inventory. The response was to correct the method, not to weaken validation.
19. **Ranking divergence:** not applicable; the operator fixed the paper order and the session honored it.

### Batch scorecard

20. **Main message, original contribution, hidden gold:** no new scientific scorecard is emitted because the supplement was not read. Repeating prior conclusions would misrepresent this continuation as a reading.
21. **Source parity:** the PMC HTML remains the primary text surface, the PDF only an image container, and recency was not used as a strength proxy.
22. **Team classification:** `experimental_lab`, gene-primary and not disease-primary, reused from the existing manifest with observation and interpretation weighted separately.
23. **Skills/gates used and declined:** used LEGEND deep-dive preflight, receipt protocol, font-screen, PPI preflight, strict validator, self-evaluation and capability scout. Declined image generation and OCR because synthetic or reconstructed pixels cannot replace the publisher supplement.
24. **Output landing:** blocker and diagnosis in this file; prior manifest at `disease-models/wwox/research/deepdive_manifests/PMID25331887.json`; prior receipt `FTR-20260810-25331887-01`; no commit candidate and no canonical update.
25. **Mechanical future answer:** yes for the partial reading (event ID, timestamp, HTML fingerprint, complete body/main figures, supplementary unavailable); no completion receipt exists, which is the correct machine-readable result.
26. **Friction:** web safe-URL refusal, terminal DNS refusal, absent in-app browser, binary publisher refusal, sandbox write refusal, and one corrected basename-only inventory error. All occurred before overclaiming.
27. **Persistent cross-disease delta:** the path-aware inventory rule is written here. A framework regression would make it globally executable, but framework modification is outside the operator's perimeter, so this session records a proposal and stops rather than implementing it.

Self-diagnosis verdict: **existing state PASS; requested completion BLOCKED**. The blocker is environmental and evidence-locality preserving, not a scientific waiver.
