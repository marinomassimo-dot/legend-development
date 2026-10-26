# ToolUniverse — one capability test: a second, independent signature-reversal service (2026-10-26)

Scientist `scientist-c`, package P3B-2. The verdict is about this capability only; the earlier PDK2 verdict (`lucas_clarke_followup_20261026/tooluniverse_trial.md`, WATCH for that query) is unchanged.

## Why this capability
The repository's only reversal route is SigCom LINCS, and the GSE156243 query on it ended INCONCLUSIVE with a context-dominated ranking (`gse156243/prediction_lincs_context_stratification_20261026.md`). A second reversal service on a **different library** is missing today, and writing and maintaining a new adapter for it (request format, entity or symbol handling, retry, licence text, selftest, acknowledgements) is the cost the roadmap line P6c asked to avoid by reusing ToolUniverse. The roadmap named its CLUE tool; **that tool is not in 1.5.7** (see below).

## Discovery without loading the catalogue
Isolated environment outside the repository (`uv venv` in the session scratch directory, `tooluniverse` 1.5.7, Apache-2.0, as in the PDK2 trial; no global install). `load_tools()` registers 2719 tools; they were never shown to the model. A name-substring scan of the tool dictionary (`clue`, `lincs`, `sigcom`, `l1000`, `cmap`, `enrichr`) returned **8 names**: `LINCS_search_signatures`, `LINCS_list_libraries`, `L1000FWD_sig_search`, and five Enrichr tools; **no CLUE tool**. The tool specification (parameters, required fields, return schema) was read for the one candidate, `L1000FWD_sig_search` (up and down gene symbols; `n_results` 1-1000; `mode` similar or opposite; no key).

## Test, on the declared sets (same four gene sets as the SigCom runs)
Asked for 100 results per set in `opposite` mode: S1, S0 (random expressed genes), and the two direction-shuffled S1 sets (S1P, S1P2). Raw: `gse156243/tool_responses/l1000fwd_via_tooluniverse_results.json`; script `gse156243/tooluniverse_l1000fwd_trial.py`. About 24 s per query. Original L1000 chemical library (cell lines HCC515, MCF7, PC3, HA1E, VCAP and others); **no MCLF signature appears in any of the four results.**

| Set | Returned (asked 100) | q < 0.05 | Cell lines in the returned list |
|---|---|---|---|
| S1 | **50** | **7** (q 0.001-0.046) | 17 |
| S0 | 50 | 0 | 12 |
| S1P | 50 | 0 | 11 |
| S1P2 | 50 | 0 | 14 |

Overlap of the returned signature ids: S1 with S0 0, with S1P 1, with S1P2 5, S0 with the shuffles 0.

## What it gives, and what it loses
- **Gives:** a direction-sensitive readout where SigCom returned nothing. In the original library S1 yields 7 opposite-direction signatures at q < 0.05, all in oncology-derived lines (HCC515, MCF7, SKB, HA1E, PC3), 6-24 h, and the same-gene, shuffled-direction controls yield none; this is the control that the SigCom run could not supply (its shuffles returned an empty ranking). It is the same LINCS data lineage, so it is **not an independent vote** on the biology, only on the query's behaviour; and it does not reproduce SigCom's list (of the 48 distinct perturbagen codes returned for S1, only 3 have a name in the SigCom metadata I hold, and 2 of those are among SigCom's S1 top-100 reversers, one of them itself a BRD code).
- **Loses / hides:** (a) **truncation**: 100 requested, 50 returned, for every set, with no total and no flag (the call's own `n_results` field echoes the 50 that came back); (b) **no compound name**: the signature id carries a BRD code, batch, cell line, time and dose, so mapping to a compound needs a second source; (c) **no tissue or disease field**; (d) one summary score per hit (combined score, p, q, z), with no per-gene or per-arm breakdown.
- **Cost saved:** no adapter written for this service; the discovery and one working call cost two short scripts. Cost added: an isolated environment of about 489 MB and 111 packages, kept out of the repository; the repository would still need the isolated-environment step to repeat this.

## Outcome: **useful use, narrow**
For this capability and this query: ToolUniverse supplies a working, key-less second reversal route that the repository lacks, with the four losses above kept visible. It stays an optional isolated tool, not a dependency: nothing was added to the adapters, no install into the repository, no change to `repurposing_adapter.py`. **Reopening / next use:** if the result is to be relied on, the L1000FWD service is queried directly (without ToolUniverse) to get the total, the compound names and the licence terms, and written as a one-file adapter only if a second use appears.
Not tested: the CLUE route (absent from this version), `LINCS_search_signatures` (compound census, overlaps the iLINCS adapter), any of the other 2700 tools.

## Claims a verifier should check
1. The scan found 8 matching names and no CLUE tool in 1.5.7 (`tooluniverse` 1.5.7, `all_tool_dict`).
2. For all four sets 100 results were requested and 50 returned, in the stored raw file.
3. S1 has 7 results with q < 0.05; S0, S1P and S1P2 have none; no `MCLF` string in any returned signature id.
4. The signature ids carry no compound name (BRD codes only).
