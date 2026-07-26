---
name: find-fulltext
description: Find and download the full-text of a scientific paper (PDF preferred, HTML full text accepted), even hard/paywalled cases. Give it a PMID, PMCID, DOI, or title (single paper or a batch, e.g. the HIGH-priority items in full_text_queue_current.md). It runs a tiered cascade — PMC/NCBI open access → Unpaywall → Europe PMC → OpenAlex → Semantic Scholar → preprint servers → Google Scholar [PDF] links → CORE/BASE repositories → publisher landing/HTML → open web search — validates each download is a real full text, saves it to files/fulltext/, and reports which tier worked (or hands off paywalled ones with author-email/foundation/ILL routes). Use whenever a paper is "paywalled — manual PDF needed", before a deep dive, or when the operator says "trovami il full text / il PDF di <paper>".
---

# find-fulltext — full-text retriever for LEGEND

You are running the **full-text retrieval cascade** for the LEGEND system (WWOX). Your job: given a paper reference, locate and **retrieve a real full text** (a validated PDF, or — when no PDF is obtainable — the complete article body as HTML), trying progressively harder sources and validating every download. You retrieve files only — you do **not** classify epistemically, write to any Legend current/registry/queue file, or decide impact on the case. After retrieval the operator can run `fulltext-dossier` / a deep dive on the saved file.

## Mandatory retrieval receipt

Retrieval is not reading. For every paper attempted, return a `FULLTEXT_READ_RECEIPT` to
the caller with `evidence_depth: retrieved_not_read` (or `abstract_only` only when the
abstract itself was deliberately analysed), the resolved PMID/DOI, retrieval workflow,
source locator, SHA-256 for a saved artifact, and the retrieval manifest/handoff as output.
The main session persists it to the configured append-only ledger before reporting the
retrieval complete. Never emit `complete_fulltext_read` from this skill. A cached artifact
reuses the prior receipt; a new event must link `prior_receipt` and explain why retrieval
was repeated.

## Input
Accept any of: **PMID**, **PMCID**, **DOI**, or **title** (or a list / "the HIGH items in `disease-models/wwox/research/full_text_queue_current.md`").

First, **normalize identifiers**. You want PMID + PMCID + DOI for every paper, because different tiers key off different IDs:
- Title only → `mcp__claude_ai_PubMed__search_articles` (or `lookup_article_by_citation`) to get a PMID, then enrich.
- Have one ID → `mcp__claude_ai_PubMed__convert_article_ids` to fill in the others, and `get_article_metadata` for title / first author / year / DOI / corresponding-author email.
- No DOI/PMCID resolvable? You can still try OpenAlex/Scholar/Europe PMC by title.
- **Crossref** is a useful metadata fallback (no API key): `https://api.crossref.org/works/<DOI>` gives authors, journal, and sometimes a `link[]` with a full-text PDF URL; `https://api.crossref.org/works?query.bibliographic=<title>` resolves a title→DOI when PubMed doesn't.

Set up the output dir once: `mkdir -p "files/fulltext"`.

## Filename convention
Save every retrieval as `files/fulltext/PMID<pmid>_<firstauthor><year>.<ext>` (`.pdf` for PDFs, `.md`/`.xml`/`.txt` for HTML/XML full text). If there is no PMID, fall back to `DOI_<doi-slug>_<firstauthor><year>.<ext>` where `<doi-slug>` = the DOI with `/` and `.` replaced by `-`. Keep `<firstauthor>` ASCII (strip diacritics: Baryła→Baryla) and use the true first author. This makes files traceable and collision-free.

## Step 0 — cache & workspace check (before any network call)
Cheap, and it often makes the whole cascade unnecessary:
1. **Manifest cache** — maintain `files/fulltext/_retrieval_manifest.jsonl`, one JSON line per attempt: `{pmid, doi, status, path, won_via, sha256, date}`. Before fetching a paper, look it up:
   - `status: downloaded` and the `path` still exists → **done, skip** (report "cached").
   - `status: paywall|not_found` **and** the entry is **< 60 days old** → skip the cascade, go straight to the handoff card. Older than that → re-check (a closed paper may have become OA).
   After any new result, append/update its line (compute `sha256` for downloaded files to dedupe).
2. **Existing copies in the workspace** — before downloading, grep `files/fulltext/`, `files/`, and `backup/` for the PMID, the DOI-slug, or `<firstauthor><year>` in filenames; if a matching PDF already exists (even under a non-standard name), use it and record it in the manifest instead of re-downloading.

## Fast triage (do this first — saves time on batches)
After normalizing IDs, make ONE quick OA-status check before grinding the cascade (on batches, looping every tier over true paywalls causes timeouts):
- **PMCID present?** → go straight to Tier 0, it almost always wins.
- Else query Unpaywall/OpenAlex once for `is_oa`. **If `is_oa:true`** → run the cascade (Tiers 1-9) to fetch the copy. **If `is_oa:false` AND no PMCID AND not a preprint** → there is no free copy to find: skip Tiers 1-9, and go directly to Tier 10 handoff (plus Scholar Gateway first if it's a Wiley DOI). Don't waste calls confirming a closed paper is closed.
- **Publisher hint (not a rule — layer it on the `is_oa` check):** the DOI prefix predicts difficulty — `10.1002`/`10.1111` = Wiley (if `is_oa:false`, try **Scholar Gateway** before anything else), `10.1016` = Elsevier/ScienceDirect (hard-bot-blocks; but includes OA Cell Press / hybrid like `bneo`, so still check `is_oa`), `10.1007` = Springer (often closed, but `10.1186` is Springer/BMC and usually OA), `10.3390` = MDPI (always OA, Tier 0/8 wins), `10.1101` = bioRxiv/medRxiv preprint (Tier 5). Use the hint to reorder, never to skip the OA check.
- Process batches in small groups (≈5) so one slow paywalled item can't stall the rest.

### Batch ordering (when input is `disease-models/wwox/research/full_text_queue_current.md` or a list)
Process for maximum yield-per-time: first the items marked `Priority: HIGH`, then those that already have a DOI or PMCID (resolvable), then the rest. Within those, do the open-access ones (PMCID present / `is_oa:true`) before the likely-paywalled ones.

## The cascade
Run tiers **in order**. **Stop as soon as you have a validated full text** — a PDF is preferred, but a **readable full-text HTML page also counts** (see "HTML full text is acceptable" below). Each tier yields a candidate URL → download/capture it → if it validates, you're done; if not, fall through to the next tier. Track which tiers you tried for the final report.

> **HTML full text is acceptable — but only if it is genuinely full text.** If no PDF can be obtained but a tier exposes the *complete article body* (publisher HTML for gold/bronze/hybrid-OA, or the PMC/Europe PMC reader / `fullTextXML`), capture it via `WebFetch`/browser MCP and save to `files/fulltext/PMID<pmid>_<author><year>.md` (or `.xml`).
> **Classification gate:** mark it `DOWNLOADED (HTML)` **only if** the captured text contains real body sections — at least a couple of {`Introduction`, `Methods`/`Materials`, `Results`, `Discussion`, `References`}. If it contains only the abstract (+ author/affiliation/refs boilerplate), record it as **`abstract-only`** (NOT downloaded) and keep going down the cascade / to handoff. Reject outright pages that are a "purchase/login" prompt or return HTTP 401/402/403.

### Tier 0 — NCBI / PMC open access (most reliable, fully legit)
- `mcp__claude_ai_PubMed__get_copyright_status` to see if OA, then `mcp__claude_ai_PubMed__get_full_text_article` for PMC text.
- If a **PMCID** exists, the PDF is usually directly downloadable. **Prefer `https://europepmc.org/articles/<PMCID>?pdf=render`** — in testing this worked for nearly all OA PMCIDs. The `https://www.ncbi.nlm.nih.gov/pmc/articles/<PMCID>/pdf/` URL often returns a tiny (~1–2 KB) HTML interstitial instead of the PDF, so use it only as a fallback.
- If a PMCID exists but the `?pdf=render` blob comes back empty/tiny (happens for a few, and for most bioRxiv-in-PMC items), fetch the **full-text XML** instead: `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` — if it has a `<body>`, that's the complete article (save as HTML full text).

### Tier 1 — Unpaywall (best single OA aggregator; needs DOI)
```bash
curl -sL --max-time 25 "https://api.unpaywall.org/v2/<DOI>?email=your-email@example.com"
```
Parse `.best_oa_location.url_for_pdf` (fall back to `.url`), and also scan `.oa_locations[].url_for_pdf` for alternatives. `host_type: repository` entries are author/institutional copies — perfectly usable.

### Tier 2 — Europe PMC (needs DOI or title)
```bash
curl -sL --max-time 25 "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<DOI>&format=json&resultType=core"
```
Read `resultList.result[0]`: if `pmcid` present and `isOpenAccess:"Y"` → use the PMC PDF URLs from Tier 0. Also inspect `fullTextUrlList.fullTextUrl[]` for `documentStyle:"pdf"` entries. If you only have a title, swap the query for `TITLE:"<title>"`.

### Tier 3 — OpenAlex (needs DOI; good for repository copies)
```bash
curl -sL --max-time 25 "https://api.openalex.org/works/doi:<DOI>"
```
Use `.best_oa_location.pdf_url`, then scan `.locations[].pdf_url` for any non-null entry (repository green-OA copies live here).

### Tier 4 — Semantic Scholar (needs DOI/PMID; often has author copies)
```bash
curl -sL --max-time 25 "https://api.semanticscholar.org/graph/v1/paper/DOI:<DOI>?fields=openAccessPdf,externalIds"
```
Use `.openAccessPdf.url`. (Key `PMID:<pmid>` also works.)

### Tier 5 — Preprint servers (for "(preprint)" items — FT-009 etc.)
- bioRxiv/medRxiv by DOI: `https://api.biorxiv.org/details/biorxiv/<DOI>` (or `/medrxiv/<DOI>`) → take the latest `version`, then PDF at `https://www.biorxiv.org/content/<DOI>v<version>.full.pdf` (or `www.medrxiv.org`).
- **Known gotcha:** bioRxiv's `.full.pdf` endpoint returns HTTP 403 to `curl`/`WebFetch` *and* to non-interactive browser requests (separate protection from the article HTML). The reliable route is the **`.full` HTML page** (`https://www.biorxiv.org/content/<DOI>v<n>.full`) via the `playwright` browser MCP — the article HTML passes Cloudflare fine; capture the article body as HTML full text. Treat the PDF as unavailable for bioRxiv and go straight to the HTML.
- Research Square / SSRN / arXiv: resolve via the OpenAlex/Scholar URL found above.

### Tier 6 — Google Scholar [PDF] links (author copies, ResearchGate, institutional repos)
This is the workhorse for **complicated / paywalled** cases. Scholar surfaces legal author and repository copies that the OA APIs miss. **Philosophy:** Scholar is a *manual last-shortcut, never a batch retrieval engine* — the indexed APIs above (Tiers 1-5, 7) do the heavy lifting; Scholar handles only the 2-3 leftovers. On a CAPTCHA/robot page, **stop immediately** and go to handoff; never loop or scrape. For 1-2 truly hard papers, the highest-yield move is often to let the operator run the Scholar query in their own browser and paste the PDF link back.
- **If a Google Scholar MCP server is configured, prefer it over `WebFetch`** for this tier: it runs from the local (residential) IP and hits far fewer CAPTCHAs than a server-side fetch. A browser-automation MCP (Playwright/Chrome), if present, is better still — it drives a real browser, so it both queries Scholar cleanly and can retrieve publisher copies that bot-block `curl`/`WebFetch` (the `OA-but-bot-blocked` cases). Fall back to the `WebFetch` recipe below if neither is available.
- `WebFetch` the results page for the exact title:
  `https://scholar.google.com/scholar?q=<url-encoded title>&hl=en`
  Ask WebFetch to return: the right-hand **`[PDF]` link** for the top matching result, the host (e.g. `researchgate.net`, a `.edu`/`.ac.` repo, the publisher), and the **"All N versions"** link.
- Also try the versions page (`...&cluster=<id>` or the "All versions" URL) — different versions often expose different OA copies.
- **Light touch:** at most 1–2 Scholar fetches per paper. If you get a CAPTCHA / robot page, note "Scholar blocked this run" and move on — do not hammer it.
- ResearchGate/Academia links that say "Request full-text" are **not** a direct PDF — record them as a manual fallback, don't try to scrape them.

### Tier 7 — Repository aggregators (green-OA copies)
These index author manuscripts deposited in institutional/subject repositories — copies the per-DOI APIs above sometimes miss.
- **CORE** (`https://core.ac.uk`): search `https://api.core.ac.uk/v3/search/works?q=<title or DOI>` (a free API key in the `Authorization: Bearer` header raises limits; without one, the public web search at `https://core.ac.uk/search?q=<title>` is WebFetch-able). Look for a `downloadUrl` / direct PDF.
- **BASE** (`https://www.base-search.net/Search/Results?lookfor=<title>`): WebFetch and ask for any result flagged as open-access with a PDF link.
- **OpenAIRE** (`https://api.openaire.eu/search/publications?doi=<DOI>`): aggregates EU/repository deposits; check for an OA full-text URL.
- **DOAJ** (`https://doaj.org/api/search/articles/doi:<DOI>`): confirms the *journal* is fully OA and often links the article — useful to decide a closed-looking DOI is actually free.
- **Zenodo / HAL**: search by title (`https://zenodo.org/api/records?q=<title>`, `https://api.archives-ouvertes.fr/search/?q=<title>&fl=...,files`) — authors sometimes self-deposit the accepted manuscript here.

### Tier 8 — Publisher landing page + HTML full text (gold/bronze/hybrid OA)
- **Publisher-specific direct-PDF patterns** (the *metapub/FindIt* idea — try these constructed URLs before scraping the landing page; they skip a step for OA publishers):
  - MDPI (`10.3390`): `https://www.mdpi.com/<journal>/<vol>/<issue>/<art>/pdf` (or append `/pdf` to the article URL)
  - PLoS (`10.1371`): `https://journals.plos.org/<journal>/article/file?id=<DOI>&type=printable`
  - Frontiers (`10.3389`): article URL + `/pdf`
  - eLife (`10.7554`): `https://elifesciences.org/articles/<id>.pdf`
  - BMC / SpringerOpen (`10.1186`): article URL + `.pdf`
  - Oxford (`10.1093`): landing + `/article-pdf/...` (often bot-blocked → browser MCP / PMC)
  - PNAS/Cell-OA/Nature-OA: take `citation_pdf_url` from the page meta
- Otherwise `WebFetch` the DOI landing page (`https://doi.org/<DOI>`) and extract any direct PDF link, especially the HTML `<meta name="citation_pdf_url">` tag and obvious `.../pdf` / `?type=printable` / `/doi/full/` links.
- If OpenAlex/Unpaywall flagged the work `is_oa` (gold/bronze/hybrid) but no PDF downloaded, the **publisher HTML body is usually free to read** — capture it as HTML full text (see "HTML full text is acceptable"). Note: some publishers (Wiley, Elsevier/ScienceDirect) bot-block `curl` *and* `WebFetch` (HTTP 402/403) even for bronze-OA articles.
- **Configured tools for these blocked cases:** (a) the **`playwright` browser MCP** (installed at user scope) drives a real headless Chromium — use it to open the publisher page and capture full text / trigger the PDF download when `curl`/`WebFetch` get 402/403. (b) For **Wiley journals specifically**, the **Scholar Gateway** connector (Wiley's MCP, free researcher trial) returns Wiley full text directly — prefer it for any Wiley DOI (`10.1002/...`, `10.1111/...`). If neither resolves it, record `OA-but-bot-blocked` with the URL for a manual browser click.

### Tier 9 — Open web search (any publicly posted copy)
Last automated tier — catches copies posted anywhere (author homepages, lab sites, university repositories, conference mirrors, preprint echoes) that no structured index lists.
- `WebSearch` for the exact title in quotes + `pdf` (and a variant with first author + year). Inspect hits for a non-publisher host serving a real PDF/HTML full text; download/capture and validate.
- A domain-specific shortcut for this project: WWOX-DEE clinical papers are sometimes shareable via the **WWOX Foundation** / the patient-advocacy network (several such papers list a Foundation co-author). For a clinically case-relevant paper, flag this as a high-yield manual route.

### Tier 10 — Manual handoff (genuinely paywalled, no free copy anywhere)
Do **not** fabricate or guess content. Every failure must still produce value: emit a **citation-only handoff card** so the operator can act immediately. Save it to `files/fulltext/PMID<pmid>_<author><year>.handoff.md` AND show it:
```
## HANDOFF — PMID <pmid> — <short title>   [FULL TEXT: paywall — manual retrieval needed]
- Title / Authors / Journal / Year
- DOI: <doi>   ·   Publisher URL: https://doi.org/<doi>   ·   PMID: <pmid>
- Direct PDF URL (bot-blocked): <url if known>
- Corresponding author: <name> <email if found via get_article_metadata>
- Email template: "<ready-to-send request, see below>"
- ResearchGate request link: <if any>
```
Then hand the operator concrete next actions, best-yield first:
- **Email the corresponding author** (address from `get_article_metadata`) — fastest, near-always works. Provide a ready template: *"Dear Dr <name>, I'm researching <topic> within the WWOX rare-disease community. Could you kindly share a PDF of your paper '<title>'? Thank you."*
- For WWOX clinical papers: ask via the **WWOX Foundation** / patient network (esp. if a co-author is affiliated with it).
- **Institutional / library access** or **interlibrary loan (ILL)** via the `https://doi.org/<DOI>` link and the publisher URL.
- **Publisher Text-&-Data-Mining (TDM) APIs** (the *article-downloader* idea, fully legitimate): Elsevier (`api.elsevier.com`) and Wiley TDM expose full text via a **free API key** — but the key generally requires an account *with subscription/institutional entitlement*, so it only helps if the operator has such access. Note it as an option, don't assume it.
- The **ResearchGate "Request full-text"** button if one exists.
- **Zotero** (operator-side): "Find Available PDF" runs its own resolver set from the operator's real browser/IP and often gets OA copies this skill can't from a server — a good manual fallback for the leftovers.
- Shadow-library mirrors (e.g. Sci-Hub / LibGen / Anna's Archive) are what many researchers in practice use for paywalled papers, but they distribute copyrighted material without authorization and their legality varies by jurisdiction. That is the operator's own choice — **this skill does not query or download from them.**

## Download & validate (every candidate URL)
**Light two-attempt retry** (helps with simple bot-blockers; do NOT apply to Scholar):
```bash
out="files/fulltext/PMID<pmid>_<firstauthor><year>.pdf"   # see Filename convention
# attempt 1: plain
curl -sL --max-time 90 -o "$out" "<URL>"
# attempt 2 (only if attempt 1 fails validation): browser UA + DOI referrer
curl -sL --max-time 90 -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
  -e "https://doi.org/<DOI>" -o "$out" "<URL>"
```
**Validate** (a paywall often returns an HTML page served at a `.pdf` URL):
- magic bytes `%PDF`: `head -c 5 "$out"` = `%PDF-`; and `file "$out"` says `PDF document`;
- size sane: reject < ~20 KB (error/stub page);
- **content sanity for HIGH-value or ambiguous hits:** `Read` the first page and confirm (a) the title/first-author matches the requested paper (guards against wrong-article redirects) and (b) it is not a cover/paywall page (no "Access Denied", "Purchase PDF", "Sign in to read"). *(We have no `pdfinfo`/`pdftotext`, so page-count/full-text mining isn't available offline — use `Read` for the spot-check.)*

If validation fails: delete the bad file and fall through to the next tier/URL. On success: copy to the final path and **append the result to `_retrieval_manifest.jsonl`** (with `sha256`).

## Output (final message)
For each paper, one block:
- **Paper:** PMID / DOI / short title
- **Result:** `DOWNLOADED` (PDF, + saved path) | `DOWNLOADED (HTML)` (+ saved path) | `cached` (already in workspace/manifest) | `abstract-only` (no body found) | `OA-but-bot-blocked` (URL to open in a browser) | `paywall — manual` (handoff card saved) | `not found`
- **Won via:** which tier + the source host (e.g. "Tier 1 Unpaywall → repository copy")
- **OA status / license** if known
- **Tiers tried** (so a retry knows where to resume)
- For manual cases: the DOI link, publisher PDF URL, corresponding-author email + request template, ResearchGate request link.

If processing a batch, present a summary table first (Paper | Result | Won via | Path), then the per-paper detail for anything that needs manual action.

## Hard rules
- **Retrieve only.** Never write to Legend current / meta / registry / queue files, never assign DATO/INFERENZA/claim states, never conclude relevance to the case. PDFs go only into `files/fulltext/` (gitignored).
- **Validate every download** — never report a saved file without confirming it's a real PDF (`%PDF-`) or a genuine HTML full-text body (Intro/Methods/Results present, not an abstract or login/purchase stub). An HTML paywall page with a `.pdf` name is a failure, not a success.
- **No fabrication.** If you can't get the full text, say so plainly and give the manual handoff. Never fill content from the abstract or prior knowledge and present it as the full text.
- **Respect rate limits.** Scholar = 1–2 light fetches max, no aggressive retries; PMC/Unpaywall/OpenAlex/Europe PMC are the reliable workhorses.
- **Be honest about source legality** (Tier 10) and leave gray-area choices to the operator — this skill does not query shadow libraries.
