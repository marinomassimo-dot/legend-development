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

💎 **Inviolable rule — every study is gold.** No study with an available full text gives "zero leads": it condenses years of research. Even if it is on animals, the elderly, cancer, or does not touch WWOX/WOREE, **it is analyzed anyway** — at minimum **Methods + Conclusions** — looking for reusable assays/reagents, mechanisms, pathways, biomarkers, repurposing rationales, safety signals, failure modes or new research lines. If the ledger comes out empty for a full-text paper, **the analysis was shallow or not done**: redo it. If it is genuinely low-yield, record *why* (that too is information useful to calibrate future searches).

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

**0. Load the compounding context.** Before reading the paper, read:
- the discovery ledger (if it does not exist, create it from the template in `references/discovery_ledger_template.md`) — so you link new leads to those already accumulated.
- the state manifest (`framework/state/state_manifest_current.md`), the paper registry and claim registry (dedup + current WM version), and `disease-models/wwox/biomarker_endpoint/biomarker_candidates_current.md` (to avoid duplicating already-registered leads).
- `framework/instruction/LEGEND_CORE.md` and `framework/protocols/wikilink_schema.md` (rules + wikilinks).
- **Anchor on the real case**: the actual genotype (alleles, exons, affected domains), electrophysiology and known phenotype. Every paper is read *against* the case, not in the abstract — the most translatable leads come from the cross-reference paper × genotype, not from the paper in isolation.
- **Full-text-first**: attempt full-text retrieval *before* deep analysis (`find-fulltext`); if paywalled, flag it and proceed in provisional mode (abstract-only leads do not exceed medium belief).
- **Receipt preflight**: resolve PMID/DOI and check prior read receipts. Reuse an adequate complete dossier; resume missing sections from a partial receipt. Repeat a complete read only with an explicit `reread_reason`.

**1. Line-by-line reading with the discovery lens.** No skim. Section by section (abstract → intro → **Methods** → **Results, figure by figure, table by table** → discussion → **supplementary**). Methods and supplementary are often the mine: every assay is a possible biomarker *readout*, every reagent/compound/inhibitor is a possible *molecule*. Apply the taxonomy and question bank in `references/discovery_lens.md`.

**2. Extract the leads.** For each useful lead, a ledger entry (4 types): **BIO** (biomarker lead — Tier 1/2 WWOX-linked vs distal), **MOL** (molecule/therapy/compound), **REPO** (drug repurposing — an already-approved drug hitting a relevant target), **MECH** (mechanistic clue / an inconclusive "needle" that seeds the next step). Entry schema in the template. Apply the **discovery methods** in `references/discovery_methods.md`: map each lead onto the **ABC** schema (A=WWOX · B=intermediate · C=target/molecule/biomarker); write the mechanism as an atomic **causal statement** (`Subj —relation→ Obj`, INDRA §7) with a qualitative **belief**; for MOL/REPO leads use the **signature-reversal** lens and add a **proposed experiment** with expected readout, feasible in context where possible (Robin §8); anchor the **reasoning chain** to the cited passage (figure/table/sentence), not just to the paper.

**3. Compounding — interconnect + stress-test.** For each new lead, search the ledger for existing leads it **strengthens, contradicts, or extends**; link them. Before raising a status (`open`→`maturing`) interrogate the lead from three sides — **supports / refutes / neutral** (anti-confirmation-bias, see discovery_methods §3). Two converging IPOTESI from different papers can rise to INFERENZA: update the status and note the convergence. This is where value compounds. When a reasoning path works, distill it into the ledger's **Learned heuristics** section (the method compounds too).

**4. Canonical promotion (if it deserves it).** If a lead reaches canonical threshold (supported claim, Tier 1/2 biomarker with a validation paper), produce a complete **COMMIT CANDIDATE** and mark the lead `promoted-to-CC`. Otherwise it stays in the ledger. Biomarker LINT discipline: Tier 1/2 → biomarker file; Tier 3 distal → `disease-models/wwox/biomarker_endpoint/clinical_monitoring_endpoints_current.md`, never mixed.

**5. Self-propagation (multi-perspective ABC curriculum).** Ask yourself: "what is the most useful thing I still *don't know* that is within my reach now?" The best queries come from the **most connected B nodes** (ABC): "which other C nodes — biomarkers/molecules — bind this B and are not yet connected to A=WWOX?". Generate queries from **multiple perspectives** (metabolic/electrophysiology/genetic/structural/immuno/clinical/pharmacological — STORM, see `references/autoresearch_patterns.md` §2) to avoid tunnel vision, and **order the next search as a curriculum** by expected knowledge gain (Voyager §1). Optionally query external KGs DRKG/PrimeKG/Open Targets for drugs on the target (discovery_methods §6). Then **proceed autonomously**: `wwox-scout` to fish the papers, `find-fulltext` to retrieve them; each paper re-enters this skill (multi-hop). Stop when WWOX relevance drops. Record the agenda in the ledger ("Next-search agenda", with the originating perspective).

**6. Assembly, verification, novelty and reflection (cumulative growth).** Before closing the turn: (a) **Ledger assembly** (INDRA §7) — review the leads touched in the hop: merge equivalent causal statements (dedup), mark contradictions (`conflicting`), and **recompute belief**: each new independent source or convergence raises the linked lead's belief. The belief does not update itself: do it explicitly. (b) **self-verification** — do the `maturing` leads survive the stress-test and hold a sustained belief? Otherwise `open` (Voyager §1). (c) **Novelty check** — check the canonical current files and biomarker file: new, or corroboration of an existing claim? Label it (AI-Scientist §4). (d) **Process reflection** — 2–3 lines in the ledger: what gave the best leads, which thread is a dead end, what to do differently (Reflexion §3). Update **Learned heuristics** if you distilled a reusable method.

## Turn output
1. Extracted leads (appended to the ledger, with epistemic tags and interconnections).
2. Any COMMIT CANDIDATEs queued in the commit-candidate log (if ≥5 candidates → suggest `legend-commit`).
3. Next-search agenda + the papers already fished/queued for the next hop.
4. A one-line synthesis: what grew in the discovery capital this turn (e.g. "MOL-007 and MECH-012 converge → new IPOTESI on GSK3β rescue").
5. One `FULLTEXT_READ_RECEIPT` for every paper actually analysed, conforming to `framework/protocols/fulltext_read_receipt.md`; the main session must persist it before closing.

## When NOT to use it
If the operator only wants to file a paper into the canonical system without the discovery hunt → `legend-deepdive`. If the source is not yet triaged → `legend-ingest` first.
