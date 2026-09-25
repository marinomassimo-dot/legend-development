# Which tool answers which question

**This file routes. It does not legislate** — every rule lives in the protocol or the tool's own
docstring, and where this file and one of those disagree, the other wins.

It exists because the residual retrieval defect in this repository is no longer **size** — it is
**routing**. Selective registry access cut a MINIMAL session's load by 82 %
([`registry_records.py`](registry_records.py), 2026-09-11), and the tools below answer between
them almost every question a session actually asks. But they are spread across three directories,
and a session that does not know a tool exists does the thing this repository has
named as its characteristic failure twice in writing: it greps, and **a fragment is how a caveat
dies**. Measured before `registry_records.py` existed: zero `Read` calls on either large registry
across four transcripts, and 24 ad-hoc `Bash` calls naming them.

No count of the tools is written here on purpose. One was, in the first draft, and it is exactly
the constant `growth_anchors.py` calls *a quiet birthday* — a number a human must remember to
update, which is a defect waiting rather than a measurement. The population is enumerated from
the git index by the suite below, every time it runs.

> 🔴 **Never grep the two large registries.**
> `paper_registry_current.md` and `literature_tracking_log_current.md` (449 and 418 records
> when this was written; `registry_records.py index` prints today's) are read **by record**,
> with [`registry_records.py`](registry_records.py). A grep hit is a fragment: it drops the
> caveat two lines below it, it cannot tell an `identity` match from an incidental `mention`,
> and it names no commit. See § 1.

Every path below is checked to exist, and every tool is checked to be routed from exactly one
section, by [`../../scripts/test_tool_routing.py`](../../scripts/test_tool_routing.py) — two rows
inside one section are fine, two sections leave a reader unable to tell which place is current.
Adding a tool without routing it turns that suite red — which is the point: updating the constraint costs at least as
much as complying with it ([`growth_anchors.py`](growth_anchors.py)).

Run everything as `python3 <path> --help` first. Paths are repo-relative.

---

## 1 · I need a record, a paper or a claim — without loading a registry

| You want | Run |
|---|---|
| the whole record(s) for a PMID / DOI / record id / theme, with identity separated from mention, ambiguities named, links resolved one hop, and the commit it was read at | `framework/scripts/registry_records.py get --pmid <PMID> --hops 1` |
| the technical state of one paper before reading it — artefacts, bytes, coverage so far, acquisition history, applicable checks, **and no prior conclusion** | `framework/scripts/paper_packet.py packet --pmid <PMID>` |
| …and then to run the checks that apply to that paper's actual surfaces, in one call | `framework/scripts/paper_packet.py check --pmid <PMID>` |
| what a claim rests on, down to the species and reading depth of its foundation | `framework/scripts/trace_claim_foundation.py` |
| high-relevance corpus placeholders that were never read — the gold already at home | `framework/scripts/unread_gold.py` |
| a cross-paper query over what the deep-dive manifests already evidence (derived, never written to disk) | `framework/scripts/build_evidence_index.py` |
| **which fields each registry declares, and what values they take** — derived from the files, because no vocabulary is declared anywhere | `framework/scripts/registry_records.py fields` |
| records whose **declared field** carries a value — composable with `--theme`, `--pmid`, `--id` | `framework/scripts/registry_records.py get --field "Status=consolidated baseline" --theme myelin` |
| **one row per record** of a surface — id, title, line, and any declared fields as columns with their denominators — projected at call time and never stored | `framework/scripts/registry_records.py catalog --source discovery_ledger_current --column Status` |

> 🔴 **A field value in this corpus is free prose, and the filter says so.** `--field` matches a
> declared field as a case-insensitive substring, so `Type=INFERENZA` returns 14 of the 39 records
> declaring `Type` — of which only 2 declare a bare `INFERENZA`; the rest read `DATO + INFERENZA
> prudente` and the like. The answer prints the denominator and every distinct value it matched,
> and does not choose for you. Note also that the epistemic level lives in `Type`; `Status` is the
> claim's lifecycle (`consolidated baseline`, `in observation`, …). Run `fields` before guessing.
>
> For *"has a full text but was never deep-dived"* the tool is `unread_gold.py` (§ 1) and for
> reading depth it is `reading_state.py` / `coverage_report.py` (§ 2). The registries declare no
> full-text field, so `--field` cannot answer that question and does not pretend to.

## 2 · What has actually been read, and what is owed

| You want | Run |
|---|---|
| per-paper reading state, summed across every receipt rather than taken from the last one | `framework/scripts/reading_state.py` |
| the reading debt with an honest denominator | `framework/scripts/coverage_report.py` |
| which reading surface exists per paper, and whether it can be trusted | `framework/scripts/surface_census.py` |
| to validate, append to or query the hash-chained receipt ledger | `framework/scripts/fulltext_receipts.py verify` · `… record` |
| to apply an **operator-authorized, scope-limited** edit to one record of an append-only JSONL ledger — or to be refused | `framework/scripts/scoped_record_edit.py --file … --id … --field … --old … --new …` (dry run; add `--apply`) |
| to find out **which string counts an extracted full-text artifact can answer**, before offering a zero as evidence | `framework/scripts/extraction_damage_report.py files/fulltext/<artifact>.txt` |
| whether a deep-dive work manifest satisfies the gate, or which waiver it owes | `framework/scripts/deepdive_manifest.py` |
| do the bytes a manifest fingerprints exist in **this** checkout | `framework/scripts/evidence_presence.py` |
| a resumable work queue from a dated bibliography snapshot | `framework/scripts/batch_queue.py` |
| what the papers in a lot are to each other, resolved before the reading rather than after | `framework/scripts/lot_internal_edges.py` |

## 3 · Is this quotation real

| You want | Run |
|---|---|
| does every locator's quote actually occur in the artifact it was taken from | `framework/scripts/locator_audit.py` |
| which readings contradicted an already-persisted locator, and were they audited | `framework/scripts/locator_contradiction_audit.py` |
| where the identifiers inside a locator's proposition came from | `framework/scripts/locator_identifier_provenance.py` |
| do the quotations inside prose dossiers occur in a paper anybody can point at | `framework/scripts/dossier_quote_audit.py` |
| re-take a snippet whose text moved because normalisation moved, not because the reader did | `framework/scripts/recapture_snippets.py` |
| does any locator stand on a panel its own erratum corrected | `framework/scripts/erratum_scope_check.py` |
| a manifest flag that IMPROVED without the work behind it | `framework/scripts/manifest_flag_drift.py` |
| does a manifest's queued multi-hop id name **this** paper's debt | `framework/scripts/manifest_queue_id_crosscheck.py` |
| does a candidate, ledger or analysis file cite an `FT-` entry that was never written | `framework/scripts/manifest_queue_id_crosscheck.py --prose` |
| does the registry's declared locator count still match the manifest it names | `framework/scripts/locator_count_crosscheck.py` |
| every number in an orchestration record sitting beside what produced it | `framework/scripts/record_number_provenance.py` |

## 4 · Is this surface trustworthy

| You want | Run |
|---|---|
| does the DECLARED genre of an article agree with what its own deposit measures | `framework/scripts/genre_discriminator.py` |
| page furniture that has landed INSIDE a sentence in an extracted text | `framework/scripts/text_surface_intrusion_check.py` |
| are the figure captions inside the `<body>` of the surface you are about to declare | `framework/scripts/caption_census.py` |
| a PDF's raster information ceiling, before rendering its pages | `framework/scripts/figure_ppi_preflight.py` |
| regenerate page-adjudication crops from the source PDF and verify them by digest | `framework/scripts/regenerate_adjudications.py` |
| every degraded state of that verification, graded | `framework/scripts/adjudication_state_matrix.py` |
| replay an acquisition recipe and diff the digest | `framework/scripts/reacquire.py` |
| the case where every DOI-keyed open-access index says CLOSED and all of them are wrong | `framework/scripts/oa_status_dissent.py` |
| which external extractors this deployment actually has | `framework/scripts/tool_preflight.py` |
| a variant label, superscript or figure legend that the PMC/abstract extraction silently DELETED | re-query the same body through `Scholar_Gateway semanticSearch` — publisher-side text keeps superscripts as `^…^` and retains figure legends (passage retrieval, not a whole-body fetch; no substitute for a read or a receipt) |
| whether a claimed term census reproduces at a git ref — and which files contaminate the working tree you were about to check it on | `framework/scripts/census_verify.py` |
| 🔴 to assert that a phrase is **absent** from the repository | run the sweep **unscoped**, or state the file-type scope in the claim. `--include=*.md` is the reflex here because the prose is Markdown — but attestations, manifests, locator sets and receipts live in `.json`/`.jsonl`, which is exactly where a load-bearing sentence gets written **once** and never repeated. A Markdown-only sweep already produced one false "not located" on 2026-09-22 for a rule that was sitting in a `deepdive_manifests/*.json` string field |

## 5 · Bring literature in

| You want | Run |
|---|---|
| harvest a PubMed corpus into a record-level JSONL, a seed TSV and a manifest — **a census, not evidence** | `framework/scripts/pubmed_corpus_harvest.py` |
| turn a PubMed Clipboard export into a de-identified dated seed | `framework/scripts/pubmed_clipboard_to_seed.py` |
| fetch a public PMC binary behind the cloud-viewer proof-of-work page | `framework/scripts/pmc_pow_fetch.py` |
| read the text layer of a PDF the operator supplied, and count terms in it **only after positive controls prove the extractor read it** — an unverified zero is a reading of the tool, not of the paper | `framework/scripts/pdf_text_extract.py` |

## 6 · Screen the model itself

| You want | Run |
|---|---|
| structural LINT over the canonical state — the gate before any `BATCH_COMMIT` | `framework/scripts/legend_lint.py .` |
| claim pairs that state incompatible things about one entity and endpoint — **a screen, not a verdict** | `framework/scripts/cross_claim_contradiction_census.py` |
| what a paper DEPENDS ON, screened rather than the paper alone | `framework/scripts/dependency_integrity.py` |
| the causal graph LEGEND already declares, with every untyped edge named as untyped | `framework/scripts/pathograph.py` |
| a non-canonical Markdown/Obsidian semantic graph from the public registries | `framework/scripts/generate_semantic_graph.py` |
| registry cardinality and both debt ratchets | `framework/scripts/growth_anchors.py check` |
| how this repository's caught errors were caught | `framework/scripts/attribution_census.py` |
| phenotypic-similarity neighbours of a disease from public HPO annotations — **reading order, not mechanistic transfer** | `scripts/phenotypic_neighbors.py` |

## 7 · Close a session, commit, land

| You want | Run |
|---|---|
| the post-batch self-evaluation gate | `framework/scripts/session_self_eval.py` |
| the mechanical backup/restore phases of `BATCH_COMMIT` | `framework/scripts/batch_commit.py` |
| land a committed, verified task, detach its worktree, delete its branch | `framework/scripts/task_close.py` |
| what is not on `main` and how old it is — the weekly §21e sweep | `framework/scripts/branch_hygiene.py` |
| push a ref only when the gate PASSes on the EXACT commit being pushed | `framework/scripts/safe_push.py` |
| wait for a job to finish — by PID, `PID:START`, pid file or completion file, **never by name**, and always with a `--timeout` | `framework/scripts/process_wait.py` |
| refuse to derive a surface whose inputs are uncommitted, or state why it is safe | `framework/scripts/derived_inputs.py` |
| when the shared checkout moved, and when it deliberately did not | `framework/scripts/sync_epochs.py` |
| classify, hand off, resume or sync a laboratory across hosts | `framework/scripts/legend_handoff.py` |
| what harness work is due at session start | `framework/scripts/harness_session_start.py` |

## 8 · Before publishing

| You want | Run |
|---|---|
| the fail-closed publication gate | `scripts/public_release_gate.py` |
| every release suite at once | `scripts/run_release_regressions.py` |
| an independent, read-only privacy scan of the staging tree | `scripts/independent_privacy_scan.py` |
| a ref-scoped privacy scan of **commit metadata** | `scripts/commit_metadata_scan.py` |

## 9 · Governance and control plane

| You want | Run |
|---|---|
| the per-role governance fingerprint | `governance/scripts/governance_fingerprint.py compose --all` |
| `CANDIDATE_CONTENT_HASH` over the candidate content domain | `governance/scripts/candidate_content_hash.py` |
| the approval-queue lineages as one deterministic view | `governance/scripts/consolidate_approval_queue.py` |
| a mutation battery against the two control-plane readers | `governance/scripts/mutate_governance_tools.py` |
| derived `ORCHESTRATOR_LEASE` state — never the stored STATUS field | `framework/scripts/lease_state.py` |
| the P7 activity/event ledger, and its derived consolidated view | `framework/scripts/event_ledger.py` |
| one control-plane reader asked the same question from several directories, and the answers diffed | `framework/scripts/control_plane_probe.py` |
| what each commit candidate declares, so an integrator can route without opening all of them | `framework/scripts/candidate_durability_index.py` |
| an ordered integration of candidate branches simulated, to measure what only composition moves | `framework/scripts/integration_matrix.py` |
| enumerate and classify LEGEND artifacts — discovery, never a gate | `framework/scripts/artifact_index.py` |

## 10 · Measuring the harness itself

| You want | Run |
|---|---|
| whether each tool's own suite ever drives the tool | `framework/scripts/self_test_coverage.py` |
| the benchmark input surface — built, proven, frozen | `framework/scripts/benchmark_input_surface.py` |
| **Benchmark I** — whether targeted claim retrieval reaches the claim a paper changed (I1, deterministic, over the repository's own history) | `framework/scripts/claim_retrieval_bench.py i1` |
| **Benchmark I · I2** — whether a model finds the affected claim as reliably in the retrieved records as in the whole registry (repeated `claude -p` runs, blind deterministic grading) | `framework/scripts/claim_attention_bench.py grade` |

## 11 · Disease-model analysis (public, WWOX)

| You want | Run |
|---|---|
| the public structural-context analyser | `scripts/legend/residue_context.py` |
| the public KFERQ geometry analyser | `scripts/legend/kferq_geometry.py` |

> Both need `numpy` (`requirements-analysis.txt`). The rest of this table is standard library.

## 12 · Libraries, not commands

These three are imported by other tools and have no `__main__`. They are listed so the routing is
**complete** rather than tidy — a reader who finds one and cannot run it should learn why here,
not by running it.

| Module | What it defines |
|---|---|
| `framework/scripts/repo_root.py` | where the repository authority root is — one answer or a refusal, never a guess |
| `framework/scripts/screen_verdict.py` | the verdict contract every screen in `framework/scripts/` returns |
| `framework/scripts/corpus_firewall.py` | what a bibliographic corpus is, and how every guard recognises one |
