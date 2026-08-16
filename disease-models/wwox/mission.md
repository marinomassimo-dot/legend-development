# MISSION AND OBJECTIVES — LEGEND-WWOX

> **North-star, not canonical scientific state.** This file defines why
> LEGEND-WWOX exists, what it is trying to build, how progress is measured and
> which boundaries it will not cross. It contains objectives and operating
> commitments, not treatment recommendations or claims of scientific
> completeness.
>
> **Public disease-level scope.** LEGEND-WWOX uses public evidence and does not
> contain or reconstruct an individual clinical record. Public variant examples
> are evaluated independently and are never assembled into a person's genotype.

---

## 1. Mission

> **Build a cumulative, auditable and continuously improving mechanistic
> intelligence system for WWOX: one that connects the full cross-domain
> literature to disease mechanisms, biomarkers, therapeutic hypotheses and the
> decisive experiments needed to test them.**

LEGEND-WWOX is not merely a bibliography, a static knowledge base or a set of
AI-generated summaries. Its purpose is to make the WWOX evidence landscape
navigable, challengeable and progressively more useful for research.

The project has two inseparable products:

1. a growing, provenance-tracked body of WWOX knowledge; and
2. a growing research system capable of reading, connecting, questioning and
   testing that knowledge more effectively over time.

Knowledge growth without capability growth eventually becomes unmanageable.
Capability growth without disciplined evidence becomes speculation. LEGEND
requires both to grow together.

### The horizon this is built for

The destination is a platform holding the knowledge of everything connected to
WWOX and WOREE — **directly, indirectly, or by inference** — and to the pathways
that cascade from them.

The order of attack is deliberate:

1. the **WOREE field leaders**, read completely, because a model that cites the
   people who generate the evidence without having read them is resting on
   authority rather than on evidence;
2. **all of WWOX**;
3. everything that **cascades**: MYC, WNT, the genotype and phenotype space,
   therapies aimed at specific symptoms;
4. every new study as it appears, and whatever further literature the inferences
   — and the inferences upon inferences — turn out to require.

The intended scale is **hundreds of thousands of full texts and beyond**. That
number is a direction, not a ceiling.

🔴 **Read the current numbers as a starting point, never as the design target.**
Growth is deliberately slow at this stage because the infrastructure is being
built now so that nobody has to reopen it at scale later. Every check, constant,
ratchet, seal and baseline in this repository must therefore answer one question
before it ships — *will this still be informative at the thousandth batch?* The
binding consequences are in [`designed_for_growth.md`](../../framework/master/designed_for_growth.md).

---

## 2. Scientific scope — the whole WWOX literature

The long-horizon objective is to identify, deduplicate and process the public
literature relevant to the **WWOX gene and protein**, not only publications
whose titles mention WOREE/WWOX-DEE or SCAR12.

The scope includes, whenever WWOX biology or a reusable method is present:

- developmental and epileptic encephalopathy, ataxia and the human allelic
  spectrum;
- cancer biology and tumour-suppressor research;
- Alzheimer’s disease, dementia and other neurodegenerative contexts;
- metabolism, mitochondria, redox biology and cellular stress;
- neurodevelopment, neuronal networks, glia, myelination and inflammation;
- protein structure, folding, stability, turnover, localization and
  interaction biology;
- developmental biology, model organisms and cross-disease mechanistic work;
- assays, datasets and methods that can resolve a WWOX question even when WWOX
  is not the paper's headline.

Disease-label proximity never determines whether a study deserves to be read.
Oncology and apparently distant biology can contain the most mature WWOX
mechanistic evidence. Ranking may order work; it may not erase it.

**Scope is an objective, not a completion claim.** A study counts as processed
only when its identity, access state, reading depth and integration state are
explicitly recorded.

---

## 3. Full-text commitment — the gold is in the details

For every lawfully accessible full text, LEGEND aims to read the complete
article in depth: abstract, introduction, methods, results, figures, tables,
discussion, limitations and available supplementary material.

The method is not keyword extraction. `grep`, search and automated retrieval
may locate or deduplicate material; they cannot decide what a study means.

Every full-text analysis must:

1. produce a coverage map that distinguishes fully read, partially read,
   unavailable and supplementary-material states;
2. preserve experimental context — variant, species, model, tissue, cell type,
   developmental stage, intervention, comparator and assay;
3. separate `DATO` (data), `INFERENZA` (inference), `IPOTESI`
   (hypothesis) and `ESPANSIONE` (extension);
4. identify limitations, contradictions and assumptions;
5. ask what the study changes mechanistically;
6. brainstorm possible bridges to assays, biomarkers, therapies and research
   questions without presenting those bridges as demonstrated facts;
7. record what evidence or experiment would falsify the important inferences;
8. create explicit reading debt for anything not completely reviewed.

No source silently becomes “processed” because its abstract was screened. No
unavailable source silently disappears. The decisive detail may be located
anywhere in the paper, especially where its title promises nothing.

---

## 4. The semantic wiki — the research interface

The wiki is not the end product; it is the navigable interface through which
the research model remains inspectable and cumulative.

LEGEND-WWOX maintains connected, provenance-aware views of:

- literature records and reading state;
- claims and their supporting or conflicting papers;
- mechanisms and pathways;
- variants and molecular consequences;
- therapeutic strategies and hypotheses;
- candidate biomarkers and distal endpoints;
- active research lines and candidate research lines;
- negative conclusions, their premises and `REVIVAL_TRIGGER`s;
- learned failure modes and reusable guardrails.

Wikilinks are functional infrastructure, not decoration. Stable identifiers,
exact headings and link-integrity tests must keep the graph navigable in
Obsidian. A disposable standalone view can be generated with
`framework/scripts/generate_semantic_graph.py`; generated views never replace
the canonical registries.

Primary navigation:

- disease model: [[disease_model]]
- claims: [[claim_registry_current]]
- papers: [[paper_registry_current]]
- literature lifecycle: [[literature_tracking_log_current]]
- therapeutic portfolio: [[therapeutic_strategies_current]]
- biomarkers: [[biomarker_candidates_current]]
- research lines: [[research_lines_current]]
- candidate research lines: [[research_candidates_current]]
- discovery memory: [[discovery_ledger_current]]
- dismissed hypotheses: [[dismissal_ledger_current]]

---

## 5. Therapeutic and biomarker objectives

Gene replacement is a central causal strategy, but it is not the boundary of
the search. LEGEND-WWOX systematically investigates additional public-evidence
research directions while keeping prediction, experimental validation and
clinical actionability strictly separate.

The portfolio includes:

- WWOX functional-state biomarkers and proximal pathway readouts;
- distal experimental and clinical-response endpoints, kept distinct from
  biomarkers;
- drug repurposing and pathway-modulation hypotheses;
- network, glial, metabolic, inflammatory and proteostasis mechanisms;
- pharmacological-chaperone or stabilizer hypotheses where a variant-specific
  folding or stability defect is demonstrated or testable;
- splice-correction, antisense-oligonucleotide and RNA-processing hypotheses
  only when the molecular lesion is mechanistically compatible;
- CRISPR, base-editing, prime-editing and transcriptional-modulation hypotheses;
- gene replacement, delivery, expression-control and timing questions;
- experimental strategies that protect measurable biological function while
  causal therapies are being developed.

Every proposed lever must declare:

- evidence level;
- applicable genotype or disease population;
- mechanistic rationale;
- decisive next experiment;
- result that would falsify or park it;
- principal safety and translation uncertainties;
- whether it is a research hypothesis, experimentally supported strategy or
  validated intervention.

Nothing in this portfolio is medical advice. Computational prioritization does
not establish efficacy, safety, rescue or clinical suitability.

### Strategic tracks

- **Track A — variant-independent WWOX loss of function:** gene replacement,
  downstream mechanism interrogation, biomarker development and protection of
  measurable biological function.
- **Track B — variant or allele-class specific:** experimentally conditional
  chaperones, RNA strategies, editing strategies and assays designed around a
  defined molecular lesion.
- **Track C — drug repurposing:** already-approved or already-characterized
  compounds mapped onto dysregulated WWOX-linked nodes. Declared as an
  objective, deliberately staged; see below.

A variant-specific result may ultimately serve a recurrent molecular subgroup;
that possibility must be demonstrated rather than presumed.

### Drug repurposing — a declared objective, deliberately staged

Drug repurposing is one of the stated objectives of this project, not an
incidental by-product of hypothesis generation. For a rare disease with no
approved therapy it is the shortest route from a mechanism to something a
laboratory, and eventually a clinical team, can actually test: pharmacology,
formulation, dosing and often paediatric exposure data already exist.

It is staged on purpose. A repurposing candidate named before the underlying
biology is resolved is a lottery ticket carrying a safety cost. The track
matures as four preconditions are satisfied, and every candidate must state
which of them it currently meets:

1. **WWOX gene and protein function** — which function is lost, in which cell
   population, at which developmental stage.
2. **Dysregulated pathways with direction** — a signed map of downstream nodes
   (does WWOX loss raise or lower the node?), not a list of associated
   pathways. An unsigned association cannot support choosing a drug, which is
   exactly what the `KG_EDGE_HAS_NO_SIGN` guardrail exists to prevent.
3. **A proximal readout** — a Tier 1/2 biomarker able to report whether the
   compound moved WWOX-linked biology, distinct from a distal clinical
   endpoint.
4. **Safety and CNS exposure** — blood–brain-barrier penetration, paediatric
   tolerability and BLOCK-1 triage treated as an entry condition, not a late
   filter.

Until those hold for a given node, repurposing entries remain hypotheses: the
`REPO` section of [[discovery_ledger_current]], the levers recorded in
[[therapeutic_hypotheses_ledger_current]] and the scored rows of
[[therapeutic_strategies_current]]. They are never described as candidate
treatments, and a compound that fails the safety precondition stays flagged
rather than quietly ranked.

Meanwhile the work that makes the track viable continues by design: pathway
direction, druggable nodes, and existing-drug bridges are frequently recovered
from oncology and adult-neurology literature, where the same nodes have already
been drugged in humans. Negative repurposing conclusions enter the dismissal
ledger with a `REVIVAL_TRIGGER`, so that a later mechanistic datum reopens them
instead of leaving a silently closed door.

### Current WWOX implementation map

This is an orientation map, not canonical scientific state. Evidence, scores
and next actions live in [[therapeutic_strategies_current]]. Each row is a
research program whose assumptions can be revised or rejected.

| Program | Scope | Current epistemic position | Decisive question |
|---|---|---|---|
| Neuron-targeted WWOX gene replacement | Broad WWOX loss of function | Preclinical rescue is documented; human timing, delivery, expression control and eligibility remain research questions | Which dose, cell population, developmental stage and functional readout distinguish benefit from inadequate or excessive expression? |
| Conditional rescue of the recurrent Q230P missense example | Molecular subgroup | Public fibroblast evidence reports normal transcript with protein not detected; impaired translation, insolubility and premature turnover remain competing mechanisms | Can synthesis, solubility, turnover route and recovered function be measured separately before any stabilizer screen? |
| Editing of a canonical splice-acceptor example | Allele-specific | Editing is a hypothesis; an oligonucleotide cannot simply be assumed to recreate a destroyed acceptor | Which transcript is produced, does it escape nonsense-mediated decay, and which editing or RNA strategy is mechanistically compatible? |
| Wnt/MYC, GSK3β, network and downstream modulation | Variant-independent hypothesis space | Cross-context evidence supplies mechanisms and druggable nodes, not automatic treatment predictions | Which node has the correct direction, CNS exposure, safety margin and disease-model readout? |
| Repurposing | Variant-independent hypothesis space | Existing examples remain hypotheses pending mechanism confirmation and safety triage | Does the candidate alter a proximal WWOX-linked readout rather than only a nonspecific endpoint? |
| Protection of measurable biological function while causal approaches develop | Disease-level research | WWOX-DEE is developmental and epileptic; seizure control alone must not be equated with developmental rescue | Which stage-sensitive biological functions are experimentally measurable and genuinely modifiable? |
| Endogenous WWOX upregulation | Conditional, allele-dependent | Parked until the causal bottleneck and recovered function are known | Would more transcript produce functional protein, or amplify the wrong molecular state? |

Partial molecular or cellular rescue can be scientifically meaningful without
being described as clinical benefit. Likewise, absence of evidence is a prompt
for a discriminating experiment, not permission to convert plausibility into a
recommendation.

One reusable lesson came from cross-domain reading: an apparently distant
infection-biology study exposed a WWOX–GSK3β interaction motif and therefore a
testable pathway bridge. The bridge remains subject to direction, model,
exposure and safety checks. Its importance here is methodological: remote
literature can reveal an assay or mechanism that disease-title filtering would
miss.

---

## 6. Variant atlas and experiment prioritization

LEGEND-WWOX aims to catalogue publicly documented WWOX variants without
collapsing distinct alleles into one mechanism.

For each variant or allele class, the atlas should distinguish:

1. public source and disease/model context;
2. DNA and predicted RNA consequence;
3. measured transcript, protein abundance, solubility, localization, turnover
   and function;
4. direct experimental evidence versus computational prediction;
5. unresolved competing mechanisms;
6. transferability limits across variants and models;
7. laboratory experiments capable of discriminating among those mechanisms;
8. conditional therapeutic hypotheses, if any.

The key question is not only “is this variant predicted damaging?” but:

> **Which measurement would reveal why it is damaging, whether any function is
> recoverable and which intervention class is mechanistically compatible?**

Predictions can prioritize laboratory work. They cannot substitute for it.
Protein abundance cannot substitute for protein function, and evidence from one
variant cannot silently establish the mechanism of another.

---

## 7. From knowledge to discriminating experiments

Every non-background finding should make its research consequence explicit:

- which mechanism or uncertainty it changes;
- which assay can read that change;
- which hypothesis it supports or weakens;
- which competing explanations remain;
- what outcome would change the next decision.

`actionability: none — background` is a legitimate result. It affects
downstream prioritization but never authorizes superficial reading or deletion
from historical memory. Closing an attractive but mechanistically incompatible
road is useful when the reason and the evidence needed to reopen it are
recorded.

The therapeutic map remains a portfolio rather than a single bet: gene
replacement, mechanism-specific rescue, downstream modulation, biomarkers and
experimental-window questions can coexist, with their evidence levels and
uncertainties kept explicit.

---

## 8. Capability growth and controlled compounding

LEGEND develops the research system alongside the knowledge base. Every
substantive cycle must leave at least one proportional, reusable capability
improvement, such as:

- a better retrieval or deduplication procedure;
- a fuller coverage or provenance check;
- a new connection between evidence layers;
- a contradiction or mechanism-transfer detector;
- an improved inference, brainstorming or falsification procedure;
- a safer variant-analysis or therapeutic-triage workflow;
- a clearer visualization or semantic-graph entry point;
- a new regression fixture derived from a real failure;
- a documented exclusion criterion that prevents unproductive repetition.

The ambition is not to claim that the system will stop making mistakes. It is
to make errors visible, preserve their history and convert each observed
failure class into a named guardrail or executable regression whenever
possible. The practical principle is:

> **Do not silently repeat known errors. Make future errors informative, then
> turn what they teach into durable capability.**

This creates a controlled compounding loop:

```text
new evidence
    → better connected knowledge
    → new questions and contradictions
    → improved tools, skills and guardrails
    → deeper and safer analysis of the next evidence
```

Compounding never lowers the evidentiary threshold. More links are not more
truth; more hypotheses are not more evidence; a new tool is retained only if
it improves an observable research task.

---

## 9. A scalable method for rare-disease research

WWOX is the first disease-gene implementation of a method intended to be
portable to other rare diseases.

The reusable unit is:

```text
gene or variant
    → complete disease-specific and cross-domain literature map
    → full-text, context-preserving evidence extraction
    → semantic claim and mechanism graph
    → contradictions and unresolved mechanisms
    → biomarkers, therapeutic hypotheses and research priorities
    → discriminating experiments
    → reusable improvements to the research system
```

Scaling does not mean copying WWOX conclusions into another disease. It means
reusing the method while rebuilding the evidence model from the target gene's
own literature. The portable elements are the epistemic discipline, provenance
model, reading-debt controls, semantic-link contract, falsification procedures,
failure-aware evaluation and capability-growth loop.

---

## 10. Progress metrics and definition of done

“All literature processed” must be demonstrable, not rhetorical. Progress
should be reported using at least these metrics:

### Corpus coverage

- unique studies discovered and deduplicated;
- full texts lawfully accessible;
- complete full texts read;
- partial full texts and unread sections;
- unavailable full texts;
- supplementary materials reviewed or outstanding;
- explicit reading debt.

### Knowledge graph

- papers, claims, pathways and research lines represented;
- claims with supporting and conflicting evidence;
- unresolved contradictions;
- valid versus broken wikilinks;
- orphan records requiring review.

### Variant and experimental readiness

- variants catalogued;
- variants with direct functional evidence;
- variants supported only by prediction;
- unresolved molecular mechanisms;
- hypotheses paired with a discriminating experiment;
- biomarker candidates with a defined validation path;
- repurposing candidates that satisfy all four preconditions of Track C
  (function, signed pathway node, proximal readout, safety and CNS exposure),
  reported separately from candidates supported only by an association.

### Capability growth

- learned guardrails and regression fixtures added;
- previously observed failure classes re-detected automatically;
- workflows experimentally retained, revised or discarded;
- external tools audited, pinned or explicitly left untrusted.

Completion is not a raw paper count. For a defined corpus snapshot it requires:

1. every discovered record to have an explicit lifecycle state;
2. every accessible full text to have an honest coverage state;
3. every important assertion to preserve context and provenance;
4. every unresolved gap to remain visible as debt or a research question;
5. every canonical change to pass integrity, privacy and publication gates.

---

## 11. Boundaries and non-goals

LEGEND-WWOX does not:

- provide medical advice or replace researchers, laboratories or treating
  clinical teams;
- reconstruct an individual from public case reports;
- present predictions as laboratory validation;
- present hypotheses as treatments;
- bypass lawful access restrictions;
- equate literature volume with evidentiary strength;
- erase negative results, superseded conclusions or unresolved uncertainty;
- claim corpus completeness without a dated, reproducible coverage report.

Privacy, provenance, safety and epistemic discipline are not administrative
constraints around the mission. They are part of the scientific method that
makes the mission credible.

---

## 12. Operating references

- operating core: [[LEGEND_CORE]]
- epistemic discipline: [[epistemic_discipline]]
- gold-in-the-details principle: [[gold_is_in_the_details]]
- full-text queue: [[full_text_queue_current]]
- wikilink contract: [[wikilink_schema]]
- learned guardrails: [[learned_gates_registry]]

---

> **North-star:** make the complete public WWOX evidence landscape readable,
> connected and testable — while making the system that studies it more capable
> with every well-audited cycle.
