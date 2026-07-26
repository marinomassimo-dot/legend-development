# Autoresearch patterns and cumulative growth

These patterns come from autonomous research agents and lifelong-learning systems. They exist so that `legend-discovery` is not an analyzer that restarts from scratch every time, but a **system that grows**: every hop makes it more capable and steers, on its own, where to look next. Apply them in phases 3, 5 and in phase 6 (reflection).

## 1. Automatic curriculum + self-verification (from Voyager, MineDojo/Voyager)
Voyager learns for life thanks to three things: a growing skill library, an **automatic curriculum** that proposes the right next task, and **self-verification** before saving a skill. Transfer:
- **Curriculum**: the next-search agenda is not a flat list. Order the queries by **expected knowledge gain**: prioritize what, if true, unlocks the most downstream leads or fills the biggest hole in the causal network. The guiding question: "what is the most useful thing I still *don't know* that is within my reach now?".
- **Self-verification**: a lead does not pass `open → maturing` on enthusiasm. First verify: does the causal statement hold? Is the belief supported by ≥1 independent source? Did it survive the "refutes" side? If not, it stays `open`. This stops the discovery capital from inflating with noise.

## 2. Multi-perspective question-asking (from STORM, stanford-oval/storm)
STORM gets depth by interrogating a topic from **different perspectives** before writing. To avoid tunnel vision on a single pathway, when you generate the next-search agenda (phase 5) generate queries from multiple angles:
- **Metabolic/lipidomic** · **Electrophysiological (EEG/channels)** · **Genetic/transcriptomic** · **Structural/neuroimaging** · **Immuno/neuroinflammation** · **Clinical/phenotypic** · **Pharmacological (druggable targets)**.
- For each angle relevant to the thread, one query. Often the needle is in the angle you would not have looked at. Mark which perspective each `NS-…` comes from.

## 3. Process reflection (from Reflexion, noahshinn/reflexion)
Reflexion improves by writing a **verbal reflection** to memory on what went wrong, and re-reads it on the next attempt. Failures too are capital. At the end of every paper/hop, write 2–3 lines in the ledger's **Process reflections** section:
- what worked (which type of section/assay gave the best leads),
- which thread turned out to be a **dead end** (so you do not reopen it),
- what you would do differently on the next hop.
This, together with "Discarded leads", prevents re-walking dead roads — the error is not repeated, it is capitalized.

## 4. Novelty check (from AI Scientist, SakanaAI/AI-Scientist)
The AI Scientist includes a **review/novelty** step to avoid re-proposing the already-known. Before maturing a lead (especially BIO/REPO), ask: is it really new in the WWOX context, or is it already a consolidated fact in the canonical current files / the biomarker candidates? Use Grep on the current files. If already known → it is not a discovery lead, at most a **corroboration** of an existing claim (note it as such, it still has value for the belief). The ledger's merit is to flag what is *new and actionable*.

## 5. Ledger-as-graph and path-sampling (from SciAgents, MIT; PaperQA2, Future-House/paper-qa)
SciAgents generates hypotheses by sampling **paths** in an ontological graph built from the literature; PaperQA2 traverses the **citation graph** and anchors every statement to a cited passage. Transfer:
- Treat the ledger as an implicit graph: nodes are the concepts inside the causal statements, edges the relations. The **interconnections** between leads are the edges. A new hypothesis comes from sampling a path that crosses multiple leads/papers (ABC extended to multi-hop: A→B→C→D).
- **Passage-level provenance**: every statement/lead cites not only the paper but *where* in the paper (figure, table, Methods sentence). A reasoning chain is valid only if every link is anchored. No statements without an anchor.

## Operational synthesis
Compounding now has three layers that grow together, not one:
1. **Facts** (the BIO/MOL/REPO/MECH leads and their causal statements).
2. **Method** (the Learned heuristics).
3. **Process** (the Reflections: what to avoid, where to look next).
It is this layering that makes each session structurally more powerful than the last.
