# PaperQA2 — setup and operational use

## ✅ Local environment ALREADY READY (tested 2026-07-04/05, zero cost, offline)
An all-local stack installed **outside the repo** (unversioned, ~7G):
- venv: `~/.legend-venvs/paperqa/` (Python 3.12 via uv; paper-qa 2026.3.18, sentence-transformers, llama-cpp-python, pillow)
- local LLMs: `~/.legend-venvs/models/qwen2.5-3b-instruct-q4_k_m.gguf` (**practical default**, ~1.8G) and `qwen2.5-7b-instruct-q4_k_m.gguf` (~4.4G, better quality but see the perf note)
- runner: `~/.legend-venvs/paperqa/run_local.py` (index persisted to disk, serialized calls, `use_doc_details`/`multimodal` OFF to stay offline)
- embeddings: `st-multi-qa-MiniLM-L6-cos-v1` (SentenceTransformers, offline)
- cached index: `~/.legend-venvs/paperqa/index_<corpus>_<sig>.pkl` (depends only on corpus+embedding, reusable with any LLM)

**Workflow (from the workspace root):**
```bash
# 1) start the local LLM server (OpenAI-compatible on 127.0.0.1:8080)
~/.legend-venvs/paperqa/bin/python -m llama_cpp.server \
  --model ~/.legend-venvs/models/qwen2.5-3b-instruct-q4_k_m.gguf \
  --model_alias qwen --host 127.0.0.1 --port 8080 --n_ctx 8192 --chat_format qwen &

# 2) (one-off) build+save the index — needs the server up
PQA_BUILD_ONLY=1 ~/.legend-venvs/paperqa/bin/python \
  ~/.legend-venvs/paperqa/run_local.py files/fulltext build

# 3) query (uses the cache, nothing leaves the machine)
~/.legend-venvs/paperqa/bin/python ~/.legend-venvs/paperqa/run_local.py \
  files/fulltext "Question on mechanism/pathway/variant. Cite sources."

# at end of session: pkill -f llama_cpp.server   (frees RAM)
```
Env: `PQA_CONCURRENCY` (default 1, ideal for CPU), `PQA_EVIDENCE_K` (default 5), `PQA_TIMEOUT` (default 600s).

**⚠️ Performance/hardware note (Mac 16GB, CPU).**
- indexing **requires the LLM server up** (you cannot index with the server down → empty index).
- **3B** = practical default: index build ~5 min (one-off), then each query ~1–2 min with cache. ✔ tested, correct cited answers.
- **7B** = better quality but on 16GB CPU it hits RAM pressure and summarization timeouts fire (very slow build, fragile queries). **Not interactively usable here**: only worthwhile with more RAM or a GPU. To use it anyway: start the server with the 7B GGUF, raise `PQA_TIMEOUT` and keep `PQA_CONCURRENCY=1`.

---

## Installation from scratch (if the environment above is absent)

PaperQA2 (Future-House, `paper-qa` on PyPI, Apache-2.0). High-accuracy cited RAG over PDF/full-text/Office/code.

## Installation
```bash
pip install paper-qa      # requires a recent Python
```

## Two modes — choose by privacy

### A. Local (privacy-safe, preferred where possible)
No data leaves the machine.
- **Embedding**: local Sentence-Transformers (e.g. an `st-` model).
- **LLM**: a self-hosted model (Ollama/llama.cpp/vLLM) via a compatible interface.
- Slower and slightly less accurate than the top remote, but **no external traffic**.

### B. Remote (more accurate, but external traffic — ONLY after authorization)
- Needs a key, e.g. `export OPENAI_API_KEY=...` (or another provider supported via litellm).
- ⚠️ The query and retrieved chunks transit the provider. **Do not include sensitive clinical detail** in the question.

## CLI — index and query
```bash
# index a full-text folder
pqa index files/fulltext/

# a cited-answer question
pqa ask "What is WWOX's role in the myelination pathway according to these studies?"
```

## Python — fine control
```python
from paperqa import Settings, ask

answer = ask(
    "Are there contradictions on WWOX's role in lipid metabolism across the papers?",
    settings=Settings(paper_directory="files/fulltext/"),
)
print(answer.formatted_answer)   # answer + per-sentence citations
```

## Key functions to exploit
- **Per-statement citation**: every sentence points to the source → verifiability (a LEGEND cornerstone).
- **Summarization**: multi-paper synthesis.
- **Contradiction detection**: surface conflicts across studies instead of smoothing them over → feeds the `conflicting evidence` state at eventual COMMIT time (but here you stay READ-ONLY).

## Hygiene
- Reuse the index across sessions (avoid re-embedding).
- Optional Q&A trace → only a gitignored `_qa/` folder. Never in tracked files.
- Phrase questions on mechanism/variant/pathway, not on the patient, in remote mode.
