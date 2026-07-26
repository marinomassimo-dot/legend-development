# LEGEND → DisMech

How LEGEND's WWOX disease model lands in **[DisMech](https://dismech.monarchinitiative.org/)**, the Monarch Initiative's Disorder Mechanisms Knowledge Base.

> Public, disease-level, de-identified throughout. Nothing here involves individual-level data, and nothing here is medical advice.

---

## Why this pairing is not arbitrary

DisMech's curation asks for something most literature pipelines cannot supply: that **every evidence snippet be an exact, verifiable quote from the cited source**. That is not a formatting rule — it is a defence against fabricated or drifted attribution.

LEGEND was built around the same anxiety, from the opposite end. It does not check quotes at submission time; it makes an unverifiable claim **hard to produce in the first place**. The two systems therefore meet at their strongest shared constraint rather than at a convenient interface.

Concretely, three mechanisms already run in this repository:

| Mechanism | What it enforces | Where |
|---|---|---|
| **Full-text read receipts** | Every full text read emits a hash-chained, tail-anchored event with section-level coverage and a **SHA-256 fingerprint of the exact document**. Retrieval, indexing and keyword search are separate, weaker states and cannot be reported as reading. | [`framework/protocols/fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md) |
| **Work-manifest gate** | A `complete_fulltext_read` is **refused** unless a manifest evidences group assessment, field density, multi-hop expansion, corpus cross-query and a retraction check — or waives each with an argument long enough to disagree with. | [`framework/scripts/deepdive_manifest.py`](framework/scripts/deepdive_manifest.py) |
| **Negative discipline** | Every rejection names its load-bearing premise, tags it, and declares a `REVIVAL_TRIGGER`. Negatives are auditable instead of silent. | [`disease-models/wwox/research/dismissal_ledger_current.md`](disease-models/wwox/research/dismissal_ledger_current.md) |

**A worked example of why this matters for a knowledge base.** On 2026-07-26 LEGEND read a 2012 paper whose main text *and* published supplementary legend both stated that a figure demonstrated the absence of a protein–protein interaction. The figure contains no such blot. A text-only extractor — human or machine — would have curated a negative finding that the underlying data do not support, and a downstream knowledge graph would have inherited it. It was caught only because the coverage contract requires figures to be inspected **as images**, and the episode produced a new coverage value, `captions_only`, which now downgrades any receipt that rests on captions alone.

---

## The grant answer

*Section: "How specifically will Claude's capabilities be used in your research" — 297 words.*

> Claude Code is the execution layer of LEGEND, our open research system for WWOX-related disorders (WOREE/WWOX-DEE, SCAR12). It runs 20 skills and 5 agents that triage literature, read full texts and maintain a provenance-tracked disease model — currently 46 curated papers and 35 numbered claims drawn from a 459-record corpus.
>
> Two properties make this directly useful to DisMech.
>
> **First, epistemic typing.** Every statement is classified at one of four levels — direct data, inference, hypothesis, out-of-domain expansion — and every rejection carries a tagged load-bearing premise plus an explicit revival trigger, so negative findings remain auditable instead of silently closing a line of inquiry. Claim status is drawn from a fixed vocabulary and enforced by a structural linter.
>
> **Second, verifiable reading.** Claude Code writes a hash-chained, tail-anchored receipt for every full text it reads, recording section-level coverage and a SHA-256 fingerprint of the exact document. A complete-read claim is refused unless a work manifest evidences the research group's profile, the density of the field, multi-hop reference expansion and a retraction check. This is the guarantee DisMech's curation requires — that each evidence snippet is an exact, verifiable quote — enforced upstream rather than at review.
>
> Under this grant we will extend LEGEND's output into DisMech's native agentic curation workflow. Claude Code will run `/curate` over WWOX disorder entries, emitting schema-valid YAML with MONDO, HPO, GO and MAXO bindings, and open a pull request reviewable by Monarch maintainers using their standard tooling. Groundwork already exists and is version-controlled: a MAXO crosswalk of WWOX therapeutic modalities and an HPO-derived phenotypic-neighbour ranking for WOREE.
>
> The result turns a hand-curated model into a continuously maintained public contribution, giving an ultra-rare disorder visibility inside a knowledge graph clinicians and researchers already consult. No individual-level data is involved.

### What changed from the first draft, and why

| Change | Reason |
|---|---|
| "three explicit epistemic levels" → **four** | Factual correction. LEGEND uses `DATO` · `INFERENZA` · `IPOTESI` · `ESPANSIONE`. A reviewer who opens the repository would find the mismatch immediately. |
| "continuously monitors and analyzes the WWOX literature" → concrete mechanics | Unfalsifiable adjectives weaken a technical claim. Receipts, fingerprints and a refusal gate are checkable; "continuously monitors" is not. |
| "days after each new publication appears" → removed | A latency promise nothing in the system enforces. Cutting it costs nothing and removes the one sentence a reviewer could disprove. |
| Non-hallucination reframed as **upstream** rather than a validation step | The draft presented exact-quote checking as something the DisMech workflow does *to* our output. The stronger and more accurate claim is that the same discipline already governs how the output is produced. |
| Added: groundwork already exists | "We will build" is weaker than "this exists, we will extend it" — and both artefacts are in the repository. |
| Added: explicit privacy sentence | An ultra-rare-disease grant invites the question. Answering it unprompted is cheaper than being asked. |
| Removed: "no new infrastructure required" | Reads as reassurance rather than substance, and the space buys a verifiable claim instead. |

---

## Field mapping

What LEGEND holds today, and where it lands in a DisMech entry.

| LEGEND source | DisMech target | Notes |
|---|---|---|
| `claim_registry_current.md` — numbered claims with pathway, transferability, status | mechanism statements | Only `consolidated baseline` and `in observation` claims are eligible. `background only` and `archived` never propagate. |
| `paper_registry_current.md` + receipt ledger | evidence + provenance | Each citation carries PMID/PMCID/DOI **and** the reading depth actually achieved. |
| `disease-models/wwox/meta/` — per-axis syntheses | pathophysiology narrative | Metas are the reasoning layer; see the caveat below. |
| [`WWOX_layer9_maxo_crosswalk.tsv`](disease-models/wwox/analysis/data/) | treatment / medical action | 10 modality classes, each MAXO id verified against a local MAXO release. |
| [`WWOX_WOREE_phenotypic_neighbors.tsv`](disease-models/wwox/analysis/data/) | phenotype context | 40 ranked neighbours of WOREE (OMIM:616211) from public HPO annotations. **Reading-queue ordering, not mechanistic transfer.** |
| `dismissal_ledger_current.md` | *(no target — deliberately)* | Rejections are internal epistemic hygiene, not curated disease knowledge. |
| Private N-of-1 overlay | **never** | Excluded by architecture, not by filtering. |

---

## Honest limits

- **The reasoning layer is not yet fully backed by reading.** `session_self_eval.py` measures how many papers cited as *support for conclusions* have no complete-read receipt, no registry full-text declaration and no queued reading debt. The current count is **17 of 18**, ratcheted in the state manifest so it can fall but not rise. Metas must be reconciled against that debt before they feed a public knowledge base — this is the single largest piece of work between here and a clean submission.
- **DisMech specifics are taken on the collaboration's authority.** The `/curate` command, the YAML schema and the PR review flow are described as the Monarch side operates them; this repository has not independently exercised that workflow.
- **Curation is a proposal, not a promotion.** LEGEND's own canonical files change only through a gated `BATCH_COMMIT`; a DisMech pull request is likewise a proposal reviewed by Monarch maintainers. Neither system's automation is the authority.
- **Ontology bindings are annotations, not validated claims.** A MAXO term describing a therapeutic modality is a vocabulary alignment, never evidence that the intervention works.

## Related

[`README.md`](README.md) · [`CAPABILITIES.md`](CAPABILITIES.md) (item 30) · [`DATA_SOURCES.md`](DATA_SOURCES.md) (licensing for Monarch, HPO, MAXO, MONDO) · [`FAQ.md`](FAQ.md) · [`framework/protocols/fulltext_read_receipt.md`](framework/protocols/fulltext_read_receipt.md)
