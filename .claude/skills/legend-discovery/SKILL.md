---
name: legend-discovery
description: 'Cumulative DISCOVERY-oriented LEGEND deep-dive. Reads a full text line-by-line through a single lens — "is there a lead here, even a needle in the haystack, useful for hypothesizing new biomarkers that measure WWOX, molecules/therapies that correct a dysregulated pathway, or a drug repurposing?" — and grows a cumulative discovery ledger (compounding effect), then autonomously generates and pursues the follow-up searches. Use it when the operator says "cumulative / discovery deep dive", "squeeze this paper for biomarkers/molecules/repurposing", "what''s useful here beyond the template", or when they want a paper not merely filed but exploited toward the ultimate goals (new biomarkers, new rationales, new molecules). Distinct from legend-deepdive: that produces canonical claims, this accumulates discovery capital and self-propagates.'
---

# legend-discovery — Cumulative discovery deep-dive

Paths are relative to the workspace root.

## The purpose (why this skill exists)
`legend-deepdive` files a paper into the canonical system (PAPER, CLAIM, COMMIT CANDIDATE).
**This skill does something else**: it treats every paper as raw material for a very high, long-horizon goal —
**finding new biomarkers that measure the functional state of WWOX, and molecules/therapies (including drug repurposing) that at least partially correct the pathways dysregulated in WWOX loss-of-function.**

You do not have to succeed today. You have to **accumulate**. Every study adds a brick to a knowledge that becomes progressively denser, and that makes the *next* analysis more powerful. This is the compounding effect: the value is not the single paper, it is the ledger that grows and interconnects.

The guiding question, for every paper, is a single one:
> "Is there something here — a datum, an assay, a reagent, a mechanism, even a detail in the Methods or the supplementary — that can grow my understanding useful for hypothesizing a WWOX biomarker or a helpful molecule? If so, this study is extremely important regardless of everything else."

If the answer is yes, the needle is captured in the ledger **even if it is only IPOTESI or ESPANSIONE** — because it might be the clue to the next step.

💎 **Inviolable rule — every study is gold.** Every study with an available full text condenses years of research. Even if it is on animals, the elderly, cancer, or does not touch WWOX/WOREE, **it is analyzed anyway** — at minimum **Methods + Conclusions** — looking for reusable assays/reagents, mechanisms, pathways, biomarkers, repurposing rationales, safety signals, failure modes or new research lines. **What is mandatory is the reading, not a positive result.** Close each paper with an explicit outcome — for example `NEW_LEAD`, `CORROBORATION_ONLY`, `USEFUL_NEGATIVE`, `METHOD_REFERENCE_ONLY`, `HYPOTHESIS_REFUTED`, `NO_NEW_LEAD` or `SEARCH_FAILED` (examples, not a closed list; plain words do as well) — together with the sections actually covered and, for a null, *why* nothing qualified. A null is earned only by that coverage: if the sections above were not read, the analysis is incomplete and is redone; an empty ledger after a complete reading is a legitimate result, recorded as such — it calibrates future searches.

## Human gate
Starts ONLY from the papers the operator provides (or the papers the skill itself fishes in its self-propagation from that seed). Does not start analysis on its own initiative outside the open thread.

## Discipline (what you may and may not write)
- **Read-only** toward the 4 canonical scientific current files and registries. Everything that becomes canonical (CLAIM, PAPER, validated Tier 1/2 biomarker) leaves **only** as a `COMMIT CANDIDATE` → then `BATCH_COMMIT`. LEGEND discipline stays intact.
- **Writable** outside BATCH_COMMIT, exactly like the researchers-KB carve-out: the **discovery ledger** — structured-append, with explicit epistemic tags, change-log, and a status per lead. **It is not a canonical scientific file and introduces no canonical claims**: it is strategy space. Promotion of a lead to canonical fact happens only via COMMIT CANDIDATE.
- Append discipline: a lead is not deleted, its status changes (`open` → `maturing` → `promoted-to-CC` → `parked` → `refuted`).
- Never present INFERENZA/IPOTESI/ESPANSIONE as DATO. Never self-authorize an URGENT. Patient framing: it supports a decision, it does not replace clinical judgement.

## Epistemic discipline (mandatory)
Every assertion classified: **DATO** (directly supported by this source) / **INFERENZA** (convergence of multiple data) / **IPOTESI** (reasonable, undemonstrated, flagged) / **ESPANSIONE** (outside the direct WWOX domain). In the ledger, IPOTESI and ESPANSIONE are **welcome** — it is their place — provided they are labelled honestly. Canonical claim states (only if you propose a CC) use exclusively: `consolidated baseline | in observation | conflicting evidence | flagged for review | background only | archived`.

## Procedure per paper

**0. Before the source — `context_policy: SOURCE_FIRST`** (defined once, in `framework/protocols/fulltext_read_receipt.md`, *Before reading: context policy*). Before reading the paper, hold only:
- the state manifest (`framework/state/state_manifest_current.md`, `current_state: READY`) and the rules: `framework/instruction/LEGEND_CORE.md`, `framework/protocols/wikilink_schema.md`.
- **Receipt preflight and packet**: `python3 framework/scripts/paper_packet.py packet --pmid <PMID>` — identity, artefacts, prior coverage, acquisition history, and no prior conclusion. Reuse an adequate complete dossier; resume missing sections from a partial receipt. Repeat a complete read only with an explicit `reread_reason` — and a reread that answers a named question is `QUESTION_DRIVEN`: name the question and the prior leads it concerns, and start from them.
- **The lens**: the guiding question above, `references/discovery_lens.md`, and the reference genotype as a lens — its alleles, exons, affected domains, electrophysiology and known phenotype. Every paper is read *against* the case, not in the abstract: the most translatable leads come from the cross-reference paper × genotype. The genotype is a question here, not a conclusion.
- **Full-text-first**: attempt full-text retrieval *before* deep analysis (`find-fulltext`); if paywalled, flag it and proceed in provisional mode (abstract-only leads do not exceed medium belief).

Not before the source: the discovery ledger, the registries, the biomarker file, the working model. They are LEGEND's conclusions, and they enter at step 2b.

**1. Line-by-line reading with the discovery lens.** No skim. Section by section (abstract → intro → **Methods** → **Results, figure by figure, table by table** → discussion → **supplementary**). Methods and supplementary are often the mine: every assay is a possible biomarker *readout*, every reagent/compound/inhibitor is a possible *molecule*. Apply the taxonomy and question bank in `references/discovery_lens.md`.

**2. Extract the leads.** For each useful lead, a ledger entry (4 types): **BIO** (biomarker lead — Tier 1/2 WWOX-linked vs distal), **MOL** (molecule/therapy/compound), **REPO** (drug repurposing — an already-approved drug hitting a relevant target), **MECH** (mechanistic clue / an inconclusive "needle" that seeds the next step). Entry schema in the template. Apply the **discovery methods** in `references/discovery_methods.md`: map each lead onto the **ABC** schema (A=WWOX · B=intermediate · C=target/molecule/biomarker); write the mechanism as an atomic **causal statement** (`Subj —relation→ Obj`, INDRA §7) with a qualitative **belief**; for MOL/REPO leads use the **signature-reversal** lens and, where one would discriminate the lead from its rivals, add a **proposed experiment** with expected readout, feasible in context where possible (Robin §8) — not every lead needs one; anchor the **reasoning chain** to the cited passage (figure/table/sentence), not just to the paper.

**2b. Admit prior knowledge.** When the reading and its `verbatim_locators` are captured, write `FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` and name what you admit. Retrieve by record, never by loading the 598 KB ledger or grepping it (if the ledger does not exist, create it from `references/discovery_ledger_template.md`):
- the paper's own records: `python3 framework/scripts/registry_records.py get --pmid <PMID> --hops 1`;
- related leads: `python3 framework/scripts/registry_records.py get --source discovery_ledger_current --theme <term>` per causal node of each draft lead (`--id DL-…` for a named one), widened deliberately;
- `disease-models/wwox/biomarker_endpoint/biomarker_candidates_current.md` whole (to avoid duplicating registered leads), and the working model and claim registry whole where the novelty check needs the global state.

**3. Compounding — interconnect + stress-test.** For each new lead, search the ledger for existing leads it **strengthens, contradicts, or extends**; link them. Before raising a status (`open`→`maturing`) interrogate the lead from three sides — **supports / refutes / neutral** (anti-confirmation-bias, see discovery_methods §3). Converging hypotheses — from different papers or different agents — may raise the lead's **priority**; they do not raise its epistemic level: IPOTESI becomes INFERENZA only through converging DATO, as the epistemic discipline above defines INFERENZA. Note the convergence either way. This is where value compounds. When a reasoning path works, distill it into the ledger's **Learned heuristics** section (the method compounds too).

**4. Canonical promotion (if it deserves it).** If a lead reaches canonical threshold (supported claim, Tier 1/2 biomarker with a validation paper), produce a complete **COMMIT CANDIDATE** and mark the lead `promoted-to-CC`. Otherwise it stays in the ledger. Biomarker LINT discipline: Tier 1/2 → biomarker file; Tier 3 distal → `disease-models/wwox/biomarker_endpoint/clinical_monitoring_endpoints_current.md`, never mixed.

**5. Self-propagation (multi-perspective ABC curriculum).** Ask yourself: "what is the most useful thing I still *don't know* that is within my reach now?" The best queries come from the **most connected B nodes** (ABC): "which other C nodes — biomarkers/molecules — bind this B and are not yet connected to A=WWOX?". Generate queries from **multiple perspectives** (metabolic/electrophysiology/genetic/structural/immuno/clinical/pharmacological — STORM, see `references/autoresearch_patterns.md` §2) to avoid tunnel vision, and **order the next search as a curriculum** by expected knowledge gain (Voyager §1). Optionally query external KGs DRKG/PrimeKG/Open Targets for drugs on the target (discovery_methods §6). Then **proceed autonomously**: `wwox-scout` to fish the papers, `find-fulltext` to retrieve them; each paper re-enters this skill (multi-hop). Stop when WWOX relevance drops. Record the agenda in the ledger ("Next-search agenda", with the originating perspective).

**6. Assembly, verification, novelty and reflection (cumulative growth).** Before closing the turn: (a) **Ledger assembly** (INDRA §7) — review the leads touched in the hop: merge equivalent causal statements (dedup), mark contradictions (`conflicting`), and **recompute belief** explicitly — `UP`, `DOWN` or `UNCHANGED`, each with its source and one line of reasoning. Weigh each source by its independence: a `RESTATEMENT` (the same claim repeated, or a review citing the same primary) adds nothing; `SHARED_SOURCE` (the same dataset or cohort reused) counts once; `CORRELATED` (same lab lineage, method or reagent) counts but is marked as such; `INDEPENDENT` data carries full weight. A datum the lead predicts no better than its rivals leaves belief `UNCHANGED`; contrary data moves it `DOWN` without waiting for a formal contradiction. No numeric scores. The belief does not update itself: do it explicitly. (b) **self-verification** — do the `maturing` leads survive the stress-test and hold a sustained belief? Otherwise `open` (Voyager §1). (c) **Novelty check** — check the canonical current files and biomarker file: new, or corroboration of an existing claim? Label it (AI-Scientist §4). (d) **Process reflection** — 2–3 lines in the ledger: what gave the best leads, which thread is a dead end, what to do differently (Reflexion §3). Update **Learned heuristics** if you distilled a reusable method.

## Turn output
1. Extracted leads (appended to the ledger, with epistemic tags and interconnections).
2. Any COMMIT CANDIDATEs queued in the commit-candidate log (if ≥5 candidates → suggest `legend-commit`).
3. Next-search agenda + the papers already fished/queued for the next hop.
4. A one-line synthesis: what changed in the discovery capital this turn (e.g. "MOL-007 and MECH-012 converge → new IPOTESI on GSK3β rescue") — or that nothing did, and why.
5. One `FULLTEXT_READ_RECEIPT` for every paper actually analysed, conforming to `framework/protocols/fulltext_read_receipt.md`; the main session must persist it before closing. Capture `verbatim_locators` while the document is open: for every lead the reading carries out, what it is evidence *for*, the sentence quoted **verbatim**, and its position — section, figure or table. `framework/scripts/deepdive_manifest.py` refuses a `complete_fulltext_read` without them, and a discovery lead with no quote behind it is exactly the kind that cannot be defended later.

## When NOT to use it
If the operator only wants to file a paper into the canonical system without the discovery hunt → `legend-deepdive`. If the source is not yet triaged → `legend-ingest` first.
