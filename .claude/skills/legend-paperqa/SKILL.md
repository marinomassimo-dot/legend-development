---
name: legend-paperqa
description: 'High-accuracy cited scientific RAG over LEGEND''s local full-text corpus, using PaperQA2 (Future-House). Queries the already-collected PDFs/full texts (files/fulltext/) and answers with sentence-by-sentence cited answers, summaries and cross-paper contradiction detection. It sits downstream of find-fulltext (which downloads the PDFs) and upstream of deep-dive/Q&A. Use it when the operator says "what do the papers say about X", "query the corpus", "find confirmations/contradictions across studies", "summarize with citations", "RAG over the full texts". READ-ONLY toward the current files: a PaperQA answer is NOT a claim and changes nothing; if a promotable datum emerges it goes through the pipeline (INGEST→DEEP_DIVE→COMMIT). CAUTION: PaperQA2 uses an LLM+embeddings with an API key → external traffic to authorize; do not send sensitive clinical detail in the queries.'
---

# legend-paperqa — Cited RAG over the full-text corpus

Paths are relative to the workspace root.

## Why this skill exists
LEGEND accumulates full texts (`files/fulltext/`, fed by `find-fulltext`). **PaperQA2** turns that corpus into a **cited** answer engine: it retrieves the relevant passages, generates an answer citing the source for every statement, and can do **summarization** and **contradiction detection** across studies. It is the evidence engine that makes deep-dive and Q&A faster and verifiable — without inventing, because every sentence points to a real paper.

It fits like this: `find-fulltext` (downloads the PDFs) → **`legend-paperqa`** (indexes and queries with citations) → `legend-deepdive`/Q&A (uses the answers as verifiable raw material).

## ⚠️ Cautions before starting (read them)
- **External traffic + API key:** PaperQA2 calls an LLM and an embedding model. By default these are remote services (a key is needed, e.g. `OPENAI_API_KEY` or equivalent) → **explicit operator authorization** before using them. Alternatively, **local** models (Sentence-Transformers for embeddings, a self-hosted LLM) → no data leaves: preferable for privacy.
- **Patient privacy:** the papers are public, but **a query can contain sensitive clinical context**. Do not put identifying/clinical patient detail into the question if you are using remote services. Phrase questions about the *mechanism/variant/pathway*, not about the patient.
- **A gitignored `_qa/` folder:** if you save a Q&A trace, it goes there, never in tracked files.

## Human gate
Starts on request. It needs a corpus (`files/fulltext/` or a list of PDFs) and, in remote mode, confirmation on the API-key use.

## Discipline — what you may and may not write
- **READ-ONLY** toward the 4 current files and all registries. **A PaperQA answer is not a claim.** It touches nothing canonical.
- If a promotable datum emerges → you do **not** write it here: open the `INGEST → DEEP_DIVE → COMMIT CANDIDATE → BATCH_COMMIT` pipeline.
- Admissible output: a cited answer in chat; optionally a trace in a gitignored `_qa/` folder (append, with sources and a disclaimer). Never in tracked files.

## Epistemic discipline (mandatory)
Every statement in the answer inherits the strength of the **cited source**: robust primary paper → `DATO`; convergence → `INFERENZA`; extrapolation → `IPOTESI`/`ESPANSIONE`. **Always report the citation**; an answer without a source is unusable. Explicitly flag **contradictions** between papers instead of smoothing them over.

## Procedure

**0. Prepare the corpus.** Check `files/fulltext/` (or receive the list). If key PDFs are missing → `find-fulltext` first.

**1. Setup (one-off).**
```bash
pip install paper-qa    # PaperQA2
# remote: export OPENAI_API_KEY=...  (only after authorization)
# local: configure Sentence-Transformers embeddings + a self-hosted LLM (privacy-safe)
```
See `references/paperqa_setup.md` for the index/query commands and the local mode.

**2. Index.** Build the index over the corpus (or reuse an existing one).

**3. Query.** Ask the question about the *mechanism/pathway/variant* (not the patient). PaperQA2 returns an answer + citations. For comparisons, use the **contradiction detection** mode across papers.

PaperQA retrieval is `queried_not_full_read`: it does not emit a complete
`FULLTEXT_READ_RECEIPT` and does not remove a paper from reading debt. If the task expands
into a true section-by-section complete analysis, route it through the full-text protocol and
emit/persist the receipt there.

**4. Return.** In chat: the answer with citations, any contradictions, and the epistemic level inherited from the sources. If an element deserves to become canonical, flag it as a **pipeline candidate**, not as an established fact.

## Closing (mandatory in chat)
1. Concise answer with precise **citations**.
2. Contradictions/uncertainties across the sources, if any.
3. Any promotable elements → flagged for INGEST/DEEP_DIVE (not written into the canonical layer).
4. If remote mode was used: note that external traffic occurred.
5. Disclaimer: **"Literature synthesis with citations; not medical advice. Nothing here is a claim until it passes the LEGEND pipeline."**

## What NOT to do
- Do not send sensitive clinical detail to remote services.
- Do not present a RAG answer as a canonical claim or a promoted datum.
- Do not save Q&A traces in tracked files (only the gitignored `_qa/`).
- Do not use the remote API key without explicit authorization.
