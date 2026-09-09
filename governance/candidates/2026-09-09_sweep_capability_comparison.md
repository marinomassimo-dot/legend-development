# Sweep capability comparison — 2026-09-09

**Actor:** `scout-census` · **Scope:** the problems the Aqeilan free-full-text sweep actually hit,
compared against the tools and repositories **this repository has already censused** — not against
general knowledge. Read-only toward every canonical file; nothing installed, nothing adopted, no
external spend. The three network probes recorded below are free, key-less public endpoints.

Sources for the problem list: [`2026-09-09.md`](../../disease-models/wwox/analysis/orchestration_reviews/2026-09-09.md)
§6 and §7, [`2026-09-08.md`](../../disease-models/wwox/analysis/orchestration_reviews/2026-09-08.md).

---

## 1 · What census material exists, and what is versioned

`git ls-files` was the test in every row. "Versioned" means tracked; "present" means on disk.

| Census surface | Path | Versioned | What it actually holds |
|---|---|---|---|
| **External computational workshop manifest** | `_external_repos/MANIFEST.md` | ✅ tracked (the **only** tracked file under `_external_repos/`) | The real census. ~45 external projects across two tables, most with a **pinned commit**, a licence, a runtime class, a privacy rule and a status of `DESCRIBED` / `AUDITED` / `REPRODUCED` / `REJECTED` / `LEGACY_UNREPRODUCIBLE`. Four entries are `REJECTED` for a named reason (`NO LICENCE FILE FOUND`), which is a census doing its job. |
| **Capability scout log** | `disease-models/wwox/research/capability_scout_log.md` | ✅ tracked, 503 lines | Per-session gap → candidate → verdict tables. Six entries; five of them dated today. Verdicts are `IMPORT` / `AUDIT` / `MONITOR` / `SKIP` / `ADOPT` / `REJECT` / `REFUSED`, with reasons. |
| **Surface census** | `disease-models/wwox/research/surface_census.md` | ✅ tracked, generated | Per-paper local surface + `SUSPECT`/`clean` sentinel. Census date 2026-09-09. |
| **Tool preflight** | `framework/scripts/tool_preflight.py` | ✅ tracked | Declares the extractors this deployment needs. Ran clean here: `fitz`, `pdftotext`, `pdftoppm`, `pdfimages`, `git`, `flock` — **6/6 present**. |
| **Acquisition tier list** | `.claude/skills/find-fulltext/SKILL.md` | ✅ tracked | The 19-tier cascade, per-publisher gotchas, and the named external routes (playwright browser MCP, Scholar Gateway/Wiley MCP, Zotero operator-side). |
| **Release-surface contract over the census** | `scripts/test_external_manifest.py` | ✅ tracked | The manifest is regression-tested, not merely written. |
| **Agent-framework prior art** | `governance/design_records/prior_art_review_v3.1.md` | ✅ tracked | A second, separate census: 17 external agent primitives (Paperclip, Microsoft Agent Framework, Google ADK 2.0, A2A, OpenHands, Pydantic AI, Letta/`.af`, Temporal, Restate, DBOS, Prefect, OpenAI Agents SDK, AgentScope, Agno…) with per-source verification status and `KEEP`/`ADAPT`/`REJECT` verdicts. Dates, not commits. External durable runtimes are **REJECTED** wholesale — *"extract patterns, not dependencies."* Directly relevant to **long-run orchestration** (§7's three session terminations): that problem *has* been censused, and answered by refusal. |
| **Licence / data-provenance census** | `THIRD_PARTY_NOTICES.md`, `DATA_SOURCES.md` | ✅ tracked | Licence status for every shipped or derived third-party item. |
| **Measured extractor comparison** | `framework/eval/finding_20260809_text_surface_fidelity.md` | ✅ tracked | The one place three external tools were **run and compared** rather than described. See §3. |
| **Declared Python environment** | `requirements-analysis.txt`, `environment-md.yml` | ✅ tracked | `numpy==2.0.2` pinned; the MD environment is optional and opt-in. **PyMuPDF appears in neither**, despite being load-bearing — see §4.2. |
| **Weekly harness scout reports** | `governance/candidates/HARNESS-SCOUT-<YYYY>-W<WW>.md` | ❌ **absent — none has ever been committed** | See §1.1. |

### 1.1 · Referenced but missing

- 🔴 **The entire weekly harness-scout channel is empty.** `governance/candidates/` holds 38 tracked
  files and **not one** matches `HARNESS-SCOUT-<YYYY>-W<WW>.md`. `git log --all --diff-filter=A`
  shows none was ever added. It is required in four places:
  [`framework/instruction/LEGEND_CORE.md:572`](../../framework/instruction/LEGEND_CORE.md),
  [`roles/plan.md:79`](../../roles/plan.md),
  [`roles/junior_harness.md:44,73`](../../roles/junior_harness.md), and
  [`framework/scripts/harness_session_start.py:18`](../../framework/scripts/harness_session_start.py).
  The harness agrees it is missing — run today it prints
  `HARNESS_SCOUT 2026-W37 SCOUT_DUE`. **This file is not that file** and must not be mistaken
  for it: it is a one-off comparison against a named sweep, not the weeklythree-source mine.
  *Nothing here was reconstructed from memory to fill the gap.*
- 🔴 **`files/fulltext/_retrieval_manifest.jsonl` does not exist.** `.gitignore` line 81 names it as
  the designated home for retrieval outcomes when browser artefacts are discarded
  (*"the retrieval outcome belongs in `files/fulltext/_retrieval_manifest.jsonl` and the handoff card
  instead"*). The file is absent — **and it sits under `files/`, so it would be unversioned even if
  written.** The acquisition record has no versioned home at all. This is the root of §2.2.
- ⚠️ **The playwright browser MCP is described as configured and is not present here.**
  `find-fulltext/SKILL.md:122` states it is *"installed at user scope"*; `.playwright-mcp/` is absent
  and no browser MCP is exposed to this session. That is exactly the capability §6.1 hands back to a
  human for `33914858`. The Wiley **Scholar Gateway** MCP *is* exposed.
- ⚠️ **`_external_repos/` vendors nothing**, by design and correctly — so every censused pin is a
  claim about an upstream repository, not something this checkout can execute.

### 1.2 · The finding that governs everything below

**The censused external portfolio and the problems this sweep hit do not overlap.**

Sort `_external_repos/MANIFEST.md` by what a tool is *for* and the shape is stark: knowledge graphs
(PrimeKG, DRKG, RTX, RTX-KG2, BioCypher), repurposing (TxGNN, MATRIX, DrugRepurposing), molecular and
protein design (RFdiffusion, BindCraft, LigandMPNN, BoltzGen, ESM, ThermoMPNN), ASO and CRISPR design,
ADMET, ontologies, and multi-agent discovery loops (Robin, Co-Scientist, Biomni, MEDEA). **Every one
of them sits downstream of a reading that already happened.**

Exactly **one** entry touches the literature layer — **PaperQA** (`d7675d7b7ed`, Apache-2.0,
`AUDITED`) — and it is reserved out of this sweep on both orchestration records because it needs a
model provider, i.e. external spend.

So the sweep's five problem clusters — evidence non-locality, acquisition fragility, surface fidelity,
citation provenance, long-run orchestration — were met with **zero censused external coverage**. The
repository built its own tools instead, in-session and well: `oa_status_dissent.py`,
`evidence_presence.py`, `text_surface_intrusion_check.py`, `manifest_flag_drift.py`,
`erratum_scope_check.py`, `pmc_pow_fetch.py`, `figure_ppi_preflight.py`. That is a healthy response,
but it means the census is silent precisely where this sweep hurt, and a proposal that ignores the
census is not thereby unfounded — it is filling a hole the census has.

Two further measurements sharpen the point. Of ~45 censused routes, **only six ever reached
`REPRODUCED`** (OAK, semsimian, MAXO, MONDO, HPO, the bundled `kg_thin_slice.py`) — and two of those
were reproduced by *reimplementing the capability dependency-free* rather than installing the
upstream, which is this repository's most successful adoption pattern and the one P2 and P3 follow.
And `~/.legend-venvs/`, the environment root that `legend-paperqa`, `legend-safety-triage` and the
workshop routing all assume, **does not exist in this deployment**: those routes would fail at the
first command, not degrade gracefully. The census is a map of intentions, honestly labelled as such
by its own `DESCRIBED` ≠ runnable rule.

---

## 2 · Three proposals

Ordered by measured evidence, strongest first. Each names the problem from §6/§7 it attacks.

### P1 · Crossref-hosted Retraction Watch dataset + Crossref reference lists → **dependency-integrity propagation**

> **Problem attacked (§7.3):** *"A per-PMID retraction check cannot see the integrity status of the
> papers a paper depends on — exactly the case where reagents descend from a paper under an
> expression of concern."* `CC-20260909-18460020-01` proposes a `Reagent provenance:` field; this
> supplies the mechanical half. It is also `scientist-c`'s §7.1 finding — *convergence is
> manufactured* — turned into something a script can compute.

| | |
|---|---|
| **Resource** | Retraction Watch database, hosted by Crossref: `https://api.labs.crossref.org/data/retractionwatch?<email>` |
| **Version** | Snapshot fetched 2026-09-09, **72,450 rows**, 66,568,304 bytes, `content-disposition: retractions.csv`. Pin by SHA-256 of the snapshot, as `MANIFEST.md`'s inclusion contract requires. |
| **Censused?** | **No — and the absence is total.** A repo-wide sweep finds **zero occurrences** of *Retraction Watch*, *retractiondatabase*, *Crossmark* or *PubPeer* anywhere outside one prose mention of retraction-watching as a *practice* (`learning/scientist/SCIENTIST_OPERATING_PRACTICE_v1.md:139`). The shipped `retraction_check.py` queries **NCBI ESummary**, which is per-PMID by construction — which is precisely why §7.3's gap exists. |
| **Licence** | **CC0** (Crossref publishes the Retraction Watch data under CC0 under the 2023 agreement). Verify the notice at adoption, per the manifest's fail-closed rule. |
| **Cost** | **Zero.** No key, no registration, no spend. One HTTP GET; screening is offline thereafter. Reference lists come from `api.crossref.org/works/<doi>`, already used by `oa_status_dissent.py` — no new dependency. |
| **Integration** | **4–6 h.** A fetch-and-pin script, a CSV→index loader, a screen over `reference` DOIs already carried in the deep-dive manifests, ~6 regressions, one row in `MANIFEST.md`. Python stdlib (`csv`, `urllib`) only. |
| **Constraints** | ✅ No spend. ✅ No individual-level record — the input is DOIs of published papers. ✅ Append-only safe: it writes a **new dated snapshot + a derived report**, never an edit to a ledger. ✅ Rule 5c safe: it is a *screen*, not a text surface, and it never becomes a declared artefact. |

**Evidence it works — measured here, today, not asserted.**

1. **Positive control.** The dataset independently reproduces the finding `scientist-c` reached by
   hand this morning, with no WWOX-specific input:
   ```
   Title:  WWOX gene restoration prevents lung cancer growth in vitro and in vivo
   OriginalPaperDOI: 10.1073/pnas.0505485102   OriginalPaperPubMedID: 16223882
   RetractionNature: Expression of concern     RetractionPubMedID: 28373548
   Reason: Concerns/Issues about Data; Duplication of/in Image; Error in Image;
           Investigation by Company/Institution; Original Data and/or Images not Provided…
   ```
   Note the `Reason` field: *duplication of / error in image*. That is the same class of concern §7.1
   identified as *"precisely the loading-control panel that would license quantitative comparison."*
   The corpus-wide direct hit rate is 1 of 81 manifests — which is exactly why a per-PMID check finds
   almost nothing and feels safe.

2. **The actual result — the dependency direction.** Screening **12 corpus papers' Crossref
   reference lists (400 reference DOIs)** against the same snapshot, ~4 minutes, zero cost:

   | Corpus PMID | refs | with DOI | integrity-flagged dependency |
   |---|---:|---:|---|
   | 17360458 | 28 | 23 | `10.1073/pnas.0505485102` — Expression of concern |
   | 18460020 | 50 | 36 | `10.1073/pnas.0505485102` — EoC; `10.1038/sj.onc.1209323` — Correction |
   | 18487609 | 41 | 38 | `10.1073/pnas.0505485102` — Expression of concern |
   | 18974271 | 27 | 25 | `10.1073/pnas.0505485102` — Expression of concern |
   | 19936220 | 28 | 25 | `10.1073/pnas.0505485102` — Expression of concern |

   **5 of the first 12 papers screened depend on the paper under expression of concern**, and that
   paper is the WWOX-restoration primary — the one §7.2 states *"nothing in this lot licenses a
   WWOX-restoration claim for the reference genotype"* about. A per-PMID check sees **1**; a
   dependency check sees **at least 5 more**, in a 15 % sample of the corpus.

3. **Reference lists are already there.** `api.crossref.org` returned all 64 references for
   `10.1093/brain/awab174` in one key-less call, and manifest `PMID20146584.json` records 90 of 90
   references already resolved to PMIDs *from the deposit itself*. The graph does not need building.

**How a later session measures whether adopting it helped**

| Metric | Baseline today | Reading |
|---|---|---|
| Corpus papers with ≥1 integrity-flagged dependency | **unmeasurable** — no tool computes it | run over all 81 manifests; the number is the first measurement |
| Reference DOIs screened / total references declared | 400 / ~4,000 (sampled by hand) | coverage of the screen |
| Claims whose primary chain touches a flagged paper | unknown | the number that matters; > 0 is a reading debt, not a defect |
| False-positive rate | — | every flag adjudicated by a human; a `Correction` is not an `Expression of concern` is not a `Retraction`, and the tool must never collapse them |
| Snapshot staleness | — | days since the pinned snapshot; a re-fetch that changes row count is a signal |

**Failure modes to declare up front:** references without DOIs are invisible (17 of 400 here, ~4 %);
`RetractionNature: Correction` is noise if treated as an integrity signal; and a flag is a **prompt to
read**, never a claim about the citing paper. The screen must emit `SCREENED_CLEAN` vs
`UNSCREENABLE_NO_DOI` separately — the lesson of `scientist-c`'s wave 3, *"the screen that returns
CLEAN without screening anything."*

---

### P2 · Generalise the page-adjudication recipe to acquisitions → **evidence non-locality**

> **Problem attacked (§6.1, §7):** `files/` is gitignored by design, so a fresh checkout holds none
> of the bytes its manifests fingerprint; every verification of a prior reading requires
> re-acquisition, and re-acquisition is the fragile thing. §6.1's own words: *"The previously held
> PDF (`960569a9…`) did not survive the empty `files/` tree, so the position is worse than the queue
> records suggest."* `test_surface_census` is red for the same reason.

**This is not a new idea — it is this repository's own proven pattern, applied one layer up.**

`framework/scripts/regenerate_adjudications.py` already solves the identical constraint for page
crops, and its docstring states the principle exactly:

> *"So this repository publishes the **recipe**, not the reproduction: source PDF digest, page, crop
> rectangle in PDF points, dpi, and the SHA-256 of the resulting image. A reader holding their own
> copy of the PDF regenerates the identical bytes and verifies the digest. Nothing is lost — the
> verification is exactly as strong — and nothing copyrighted is republished. It is the same rule the
> rest of the state already follows: `files/` is gitignored while every artifact in it is
> fingerprinted. **Page adjudications were the one place doing the opposite.**"*

Today's measurement shows the last sentence is now wrong. Acquisitions are the *other* place doing
the opposite: they carry a digest and **no recipe**.

| | |
|---|---|
| **Resource** | Internal. Zero new dependency. Precedent: `regenerate_adjudications.py` + `test_regenerate_adjudications.py` + `test_regenerate_adjudications_fails_closed.py` (all tracked, both fail-open and fail-closed tested). |
| **Proposal** | An `acquisition_recipe` block per `source_artifacts[]` entry in the deep-dive manifest schema — resolved URL, HTTP method, the tier that won, User-Agent policy (§7.3's *send no UA*), date, and the resulting SHA-256 that is already declared. Plus `_retrieval_manifest.jsonl` **moved out of `files/` into a versioned path**, since `.gitignore` already promises it and `files/` guarantees it is lost. |
| **Cost** | **6–10 h.** Schema field + validator branch in `deepdive_manifest.py`, a `reacquire.py` that replays a recipe and diffs the digest, regressions, and a back-fill pass that is *declaredly incomplete* for historical artefacts whose route was never recorded. |
| **Licence / spend** | None. Stdlib. Zero spend. |
| **Constraints** | ✅ Publishes the derivation, not the derived — no copyrighted byte is added to the repository, which is the whole point of the `files/` rule. ✅ Append-only: recipes are written once with the manifest. ✅ No individual-level record. |

**Evidence, and the honest negative.** Measured repo-wide today with the peer-shipped
`evidence_presence.py`:

```
manifests: 81 | artifacts: 616 | present: 218 | absent: 398 | digest_mismatch: 0 | no_digest: 0
git ls-files files/  ->  0        find files -type f  ->  251
```

**0 of 616 declared artefacts are versioned; 398 are absent right now; 0 digests have drifted.** The
digest half of the chain is in perfect health and the transport half does not exist.

**External candidates considered against the census and rejected, with reasons** (the census records
none of these, so this is a first assessment, flagged as such):

| Candidate | Verdict |
|---|---|
| **git-annex** / **git-lfs** | **REJECT.** Both version *content*. The bytes are all-rights-reserved and cannot be redistributed — that is why `files/` is ignored. They solve a problem this repository is forbidden to have. (`git-lfs` is also absent from this host.) |
| **DVC** (Apache-2.0) | **REJECT for this purpose.** Its value is content-addressing plus a remote cache; the manifests already content-address (0 mismatches over 616), and any remote holding the bytes has the same copyright problem. It would add a dependency and a lockfile that duplicates `source_artifacts[].sha256`. |
| **OCFL / BagIt** | **WATCH.** Sound preservation grammar, and closer to correct than the above because a BagIt `fetch.txt` *is* a re-acquisition recipe. But it is a packaging standard, not a retrieval engine, and adopting the format buys less than adopting the idea — which is what this proposal does. |
| **WARC capture** (`wget --warc`, already on this host) | **TRIAL-worthy as a component of P2, not on its own.** A WARC preserves the exact HTTP transaction, which is strictly stronger provenance than a URL string. But a WARC contains the copyrighted bytes, so it lives under `files/` and is lost with everything else. Its value is *within* a session, not across checkouts. |

**How a later session measures it**

| Metric | Baseline today | Target reading |
|---|---|---|
| Declared artefacts carrying a replayable recipe | **0 / 616** | the ratchet |
| Re-acquisition success rate on a clean checkout | unmeasurable | run `reacquire.py` over N absent artefacts; report `RECOVERED / FAILED / NO_RECIPE` |
| Digest match on re-acquired bytes | — | the real test: a recipe that returns *different* bytes is a finding about the publisher, not a bug |
| `test_surface_census` | 🔴 red (asserts on evidence this checkout lacks) | green, or explicitly re-scoped to recipes |
| Papers re-verifiable without a human | 0 | the number that decides whether P2 was worth it |

**A determinism risk P2 must declare, surfaced by this scout.** The page-adjudication precedent
regenerates *identical bytes* from a recipe — but that guarantee is only as stable as the extractor.
Extraction receipts were written under **PyMuPDF 1.26.5** (`PMID42397075_partial_locators.md:27,162`;
`PMID42128308_partial_locators.md:31`), `surface_census.md:15` now says **1.28.2**, and that is what is
installed here. **PyMuPDF is declared in no requirements file at all** — the gap is already filed as
finding **F-07** in `learning/orchestrator/LEGEND_DEVELOPMENT_BOOTSTRAP_AUDIT_v1.md:213-223`, where 13
CI tests skip with *"PyMuPDF unavailable"*. A recipe that regenerates a figure at native resolution
under a different MuPDF may not reproduce its declared SHA-256. **P2 must therefore record the
extractor version inside the recipe**, and a digest mismatch on replay must resolve to
`EXTRACTOR_DRIFT` rather than to `TAMPERED`. Pinning PyMuPDF is a prerequisite, not a nicety.

**Predicted partial failure, stated in advance:** for `33914858` the recipe will replay to a
Cloudflare wall and for `20146584` to a reCAPTCHA. P2 does not fix those — **it converts them from
rediscovery into a measured, dated `FAILED` with a named cause**, which is what §6.1 had to
reconstruct by hand after a 19-tier cascade.

---

### P3 · A binary supplement kind in `ARTIFACT_KINDS` → **surface fidelity**

> **Problem attacked (§ surface fidelity):** *"`.pptx` supplements that are undeclarable because
> `ARTIFACT_KINDS` has no binary supplement kind."* Registered by two actors today and deliberately
> left unbuilt — `capability_scout_log.md:207` (`REGISTERED, not built`) and
> `2026-09-09_scientist-b-wave6.md:162` (*"stayed escalated and unbuilt"*).

| | |
|---|---|
| **Resource** | Internal. `zipfile` (stdlib) — a `.pptx` is an OPC zip; slide XML is reachable with no dependency. Confirmed available here. |
| **Version / licence** | n/a — no third party. |
| **Cost** | **2–3 h.** One member added to `ARTIFACT_KINDS` at `framework/scripts/deepdive_manifest.py:140`, a `.pptx` branch in `_artifact_text` that declares and fingerprints the **container** while routing its text through the existing verifier, and regressions. |
| **Constraints** | ✅ Zero spend, zero dependency, zero licence risk. ✅ Rule 5c intact: the container is declared as a binary, so nothing reconstructs text and calls it a surface — which is exactly why the current schema refuses it. |

**Evidence it is needed, measured:** four `.pptx` files sit on disk right now and cannot be declared —
```
files/fulltext/PMID38499540_BidanyMizrahi2024_supplement/41420_2024_1878_MOESM{1,2,4}_ESM.pptx
files/supplement/PMID33916893/s001/supplementary materials/Supplemental Figure 1.pptx
```
`PMID38499540.md:429` records the consequence in the reader's own words: *"The three containers are
therefore **not declared at all**; the extracted images that were inspected are declared and
fingerprinted."* Evidence that was read is invisible to `evidence_presence.py`, to
`fulltext_receipts.py` and to any future audit — a silent hole in the coverage map, not a friction.

**How a later session measures it:** count of `.pptx`/binary supplements present on disk but absent
from any manifest — **4 today, target 0**; plus `evidence_presence.py` artefact count rising by the
same number without any new `digest_mismatch`.

**Why it is third and not first:** it is the smallest of the three. It is included because it is
cheap, it is already twice-registered, and an item that two independent actors escalate and neither
builds is precisely the item that never gets built.

---

## 3 · Considered and deliberately not proposed

| Candidate | Why not |
|---|---|
| **GROBID**, **Docling**, **nougat**, **marker** (PDF→structured ML) | **REJECT, on this repository's own reasoning.** `capability_scout_log.md:140` skips ML layout models because *"an ML layout model would also violate rule 5c if its output were ever declared as an artifact"*, and `:388` rejects a table-region detector as *"the same class of fix that just failed — keyed to layout rather than to a document property."* The same objection §6.1 raises against `WebFetch` on publisher HTML — *"returns a model reconstruction, not the author's bytes"* — applies with full force. A reconstruction cannot be an evidence surface here, however good. **And the census contains the decisive measurement:** `framework/eval/finding_20260809_text_surface_fidelity.md:28` records `fitz`, `pdfplumber` and `pypdf` run against the same page — **all three agreed on the same wrong character**, rendering `P < 0.05` as `P 5 0.05`. Adding a fourth extractor does not detect the fault; agreement between extractors is not evidence. That is the strongest anti-adoption result in this repository and it is already written down. None of these is censused; none should be. |
| **PaperQA** (`d7675d7b7ed`, Apache-2.0, `AUDITED`) | **REFUSED, not rejected** — the census's own distinction. It is the one censused literature-layer tool and it needs a model provider. Both orchestration records reserve it explicitly. Recording the refusal so no later session reads its absence as "it was evaluated and found wanting." |
| **Memento TimeTravel aggregator** (for §6.1's *"Wayback empty on four prefixes"*) | **DROPPED after probing.** `timetravel.mementoweb.org` returned no connection at all (`http=000`) on both HTTP and HTTPS from this host. A proposal resting on an unreachable service is not a proposal. |
| **A new OA index** for the acquisition cascade | **REJECT — the cascade is not short of indexes.** `PMID20146584.json` records Europe PMC `fullTextXML`, `supplementaryFiles`, `?pdf=render`, NCBI `oa.fcgi`, OpenAlex, Semantic Scholar, Unpaywall, publisher, and open web all tried and failed; Europe PMC confirms `isOpenAccess: N` for `PMC2832309` — it is a green author manuscript, so `oa.fcgi`'s 404 is *correct*. The residual obstacle is a bot challenge, not missing knowledge. The remedy is a real browser (§1.1), which is an operator action already on the list. |
| **Wiley TDM API** | Already **REFUSED** at `capability_scout_log.md:389` as API-keyed. Unchanged. |

---

## 4 · Findings that contradict an assumption in the brief

Recorded because a comparison that only confirms its brief has not been run.

1. 🔴 **"248/248 absent across 31 manifests" does not reproduce at repository scale.**
   `evidence_presence.py` over the whole model today: **81 manifests, 616 artefacts, 218 present,
   398 absent, 0 digest_mismatch.** The stronger claim is nonetheless *more* true than the brief
   states: `git ls-files files/` returns **0** against 251 files on disk, so **0 of 616 declared
   artefacts are versioned** — a fresh checkout holds nothing, exactly as the brief says, but the
   248/248 figure is a subset measurement and a later session re-running it will get different
   numbers. Cite the tool, not the number.

2. 🔴 **PyMuPDF is present in this deployment.** `capability_scout_log.md:140` skips PyMuPDF/`fitz`
   on the ground that *"`fitz` is already absent in this environment and a red suite proves it."*
   Here `import fitz` succeeds (**PyMuPDF 1.28.2**), `tool_preflight.py` reports **6/6 tools present
   including `fitz`**, and `surface_census.md` names *"PDF text via PyMuPDF 1.28.2"* as the sentinel's
   own extractor. The SKIP verdict may still be right on rule-5c grounds, but its stated premise is
   false in this checkout — actor sessions evidently do not share an environment, and a capability
   verdict keyed to one session's environment does not generalise. **Worth a preflight line in the
   scout template.**

3. ⚠️ **`archive.org` rate-limits this host.** The Wayback availability API returned
   **HTTP 429 Too Many Requests** during this scout. §6.1 records *"Wayback empty on four prefixes"*
   for `33914858`. Those are not distinguishable after the fact. This is **not** a refutation — it is
   a reason to re-test that specific negative with a backoff before treating "no archive copy" as
   established, since it is load-bearing for a paper that founds `CLAIM 003`.

4. 🔴 **The declared Python environment does not match the running one, in both directions.**
   `requirements-analysis.txt` pins `numpy==2.0.2`; the installed numpy is **2.5.3**. And PyMuPDF —
   the one non-numpy import repo scripts actually depend on — is pinned **nowhere**, while receipts
   carry 1.26.5 and the host carries 1.28.2. Every digest declared over a PyMuPDF-derived artefact
   inherits that unpinned version. This is the quiet counterpart of contradiction 2 and it bears
   directly on P2.

5. ⚠️ **The acquisition record has no versioned home**, so "re-acquisition" is not merely expensive —
   it is *undirected*. See §1.1 and P2.

6. ⚠️ **The weekly census channel the brief points at has never produced a file.** The comparison
   asked for was made against `_external_repos/MANIFEST.md` and `capability_scout_log.md`, which are
   real and good. The `HARNESS-SCOUT-*` series is not late; it does not exist.

---

## 5 · What this file does and does not claim

Nothing here is adopted, installed, or authorised. No entry may be added to
`_external_repos/MANIFEST.md` on the strength of this file: the inclusion contract requires a pinned
commit or release, a verified licence, a minimum reproducible invocation and known failure modes, and
P1 has the first three but its `Reason`-field semantics need one adjudicated run before its failure
modes are honestly written. P2 and P3 are internal and touch reserved schema surfaces
(`ARTIFACT_KINDS`, the manifest schema), so both are **referred, not written**.

The three network probes made here — Crossref works, the Crossref-hosted Retraction Watch CSV, and the
Europe PMC core record — were free and key-less. **No external spend of any kind occurred.**
