# Gold Is in the Details — Parity of Sources

**A superordinate principle: it overrides every gate, score, tier, and matrix.**

> **There is no hierarchy of importance among studies. There is no study that "does not deserve" to be read.** Every study is analyzed under the principle *the gold is in the details* — and the decisive detail can live anywhere, especially where the title promises nothing.

This is not an aspiration. It is a lesson paid in real research.

## The worked example (public literature)

On **2026-07-12**, a paper on **thyroid cancer**, filed `Tier C` and shelved as low-signal background, turned out to carry the degradation biology of a WWOX SDR-domain missense variant — **P252A, and not Q230P**: normal mRNA, accelerated turnover, **no rescue with the proteasome inhibitor MG-132**, rescue with lysosomal probes, HSC70 co-immunoprecipitation, LAMP1 colocalization. *(Zhang X et al., Adv Sci 2025 — public.)*

The consequence for method was decisive: it showed that a degradation assay **limited to the proteasome** could not exclude other turnover routes — so a negative there risks being mistaken for a **false negative** rather than an *uninformative* result. It forced separating **synthesis, solubility, turnover, route, and function** as distinct questions. The subsequent undue transfer of that route to **Q230P → CMA** was itself corrected on audit.

The case demonstrates, together: **the value of cross-context reading** and **the risk of mechanistic over-transfer.**

## Why the intuitive hierarchy is exactly inverted

- 🧬 **Oncology studies** — often *decades ahead* on the molecular biology (folding, stability, degradation routes, partners, localization, rescue). For a tumor-suppressor gene, the biology needed to interrogate an allele may emerge *there*, more than in case reports.
- 🧠 **Adult neurology** (Alzheimer, Parkinson, ALS, tau, neurodegeneration) — fully relevant: shared pathways, proteostasis, biomarkers, endpoints, and human-tested drugs.
- 📋 **Syndrome-specific case reports** — the most *phenotype-consistent*, but largely **descriptive**: they photograph the disease, rarely provide a lever. Consistency ≠ usefulness.
- 🐄 **The "noise"** (livestock, coronaviruses, plants, basic biology) — still material to squeeze: a method, an assay, a partner, a heuristic.

## Binding operational rules

1. **No tier, score, or category authorizes NOT reading.** `background`, `discard_low_signal`, `out_of_scope_likely`, `Tier C` mean **only "later in the queue" — never "never."** They are *transient* states, not destinations.
2. **Ranking orders reading. It does not replace or negate it.** If a ranking ends up discarding a study, **the ranking is broken** — fix the ranking, don't lose the study.
3. **Disease context is never a reason to downgrade.** A paper on thyroid, breast, or lymphoma that touches the gene is worth as much as — and often more than — a syndrome case report.
4. **`grep` / keyword is forbidden as a method of analysis** — only for technical file search, dedup, or post-reading audit. Never to decide what a paper says.
5. For every available full text: inspect beyond abstract/conclusions (Methods, Results, figures/tables, limits, supplementary) and produce a **coverage map**. `Evidence depth: full text reviewed` requires `coverage_status: complete_fulltext_read`; otherwise declare `partial full text` or `FULL TEXT LARGE — COMPLETE READING IN PROGRESS`.
6. **Reading debt is explicit and must be honored:** what is not read today enters a tracked-debt queue — it does not vanish.
7. **Universal full-text trace:** every route that actually analyses a full text emits a `FULLTEXT_READ_RECEIPT`, and the calling session persists it before reporting the paper as read. Check prior receipts first; a repeated complete read needs an explicit `reread_reason`. Retrieval, indexing, RAG queries and selected passages are not a complete read. Contract: [[fulltext_read_receipt]].
8. **A local abstract corpus is a map, never the territory.** Triage, ranking, census and export pre-flight are permitted; an `abstract_only` event is honest but clears no reading debt. **Un abstract non è una lettura.** Rule 4 already forbids `grep` as a method of analysis; this is the same rule pointed at the corpus, and the hazard is not that anyone decides to cut corners — it is that hundreds of abstracts sitting locally and greppable make answering from them *feel* like working. Enforced at the authoritative append primitive and mutation-tested, not merely stated.

## The evidentiary surface — rules 5b to 5e

Rule 5 says *read all of it*. These four say **what you are allowed to have read**, and each was learned by paying for it. The operational detail and the machine enforcement live in [[fulltext_read_receipt]] and in `deepdive_manifest.py`; what follows is the binding form.

**5b · Capture the verbatim locator while the document is open.** For every statement a reading will carry out, record what it is evidence *for*, the sentence quoted **verbatim**, and where it sits — section, figure or table. 🔴 A receipt attests that a document was read; it does not attest which sentence supports which statement. On 2026-08-04 an export found that *no verbatim locator existed anywhere in the canonical state*, across every complete read in the ledger; fourteen had to be recovered by reopening papers already read. Capturing costs seconds, recovering costs the reading twice. If a reading supports no statement, waive with an argument — waiving is legitimate, silence is not.

**5c · A verbatim locator may only be verified against text extracted deterministically.** The question is not which tool is best — tools age. The question is whether the character sequence you match against is *the author's*. 🔴 **A model that converts a PDF to Markdown reconstructs**: it normalises, re-flows, occasionally paraphrases. A quote checked against that output can pass while matching **the reconstruction and not the paper** — the gate would report `verified` on a sentence nobody wrote. That is the worst class of false positive this system can produce, because it is silent and wears the badge of having been checked. **ML converters are legitimate reading aids and must never be declared as the artifact behind a locator.** A derived text artifact **declares its extraction method**, and the reading declares both artifacts fingerprinted: the original as `article_binary`, the extracted text as `article_text`. **Figures are a separate surface, inspected at original resolution and never read through a text conversion** — on 2026-08-04 a figure panel reversed a conclusion the running text did not contain, and on 2026-08-06 an unmarked asterisk was the difference between "not significant" and "not tested".

**5d · In this corpus the rendered page is the reference surface, and the text layer is the convenient derivative.** `PMID 33914858` extracts as `P 5 0.05` where the page prints `P < 0.05`, and three independent extractors agree on the wrong character because they read the same defective text layer — **cross-checking extractors detects nothing.** 33 of 51 local PDFs carry the defect, and it eats exactly what matters: `Wwox\x01/\x01` is `Wwox⁻/⁻` while `Wwox\x02/\x01` is `Wwox⁺/⁻`, the load-bearing distinction of a knockout paper carried entirely by control characters. Roughly 80% of the damage is printable, so no control-character check can see it. Consequences: **prefer XML/HTML PMC over the PDF, always, and record the absence** — where no structured surface exists, the paper enters a **different class and the full-text queue must say so**; a `SUSPECT` derived surface is **refused, never normalised**, because cleaning it launders the defect into every quote drawn from it; and **never hand-correct a corrupted surface** — re-derive it, or anchor the affected locators to the rendered page and say so.

**5e · A page adjudication is published as a recipe, never as the image.** The crop that proves what the author wrote *is* a reproduction of what the author wrote — the property that makes it evidence is the property that makes it someone else's to redistribute. The state records source-PDF digest, page, crop rectangle in PDF points, dpi and SHA-256 of the image, and `regenerate_adjudications.py` turns that back into the identical bytes from a reader's own copy. **Publish the derivation, not the derived** — the same rule `files/` has always followed. Two conditions are machine-checked rather than argued: `crop_contains_span` for every locator adjudicated, re-checked after any rounding, and a digest that regenerates. **33 of 51 local PDFs will eventually need adjudicating, so this is a standing policy, not a one-off.**

🔴 **The privacy gate does not and cannot cover this.** `public_release_gate.py` looks for patient re-identification and does it well; **copyright is outside its domain**. Before any push to a public remote, read `git diff origin/main..main --stat -- disease-models/` yourself. It is the one judgement no gate here makes for you, and publishing is not reversible.
