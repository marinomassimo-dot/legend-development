# WWOX pathograph — inventory of the graph the registries already declare

> **Generated file — do not edit by hand.** Regenerate with:
> ```bash
> python3 framework/scripts/pathograph.py --disease wwox \
>     --out disease-models/wwox/analysis/pathograph_inventory.md \
>     --export disease-models/wwox/analysis/data/pathograph_export.jsonl
> ```
> It is a *view* over the canonical registries plus the deep-dive work
> manifests, never a second source of truth. A regression re-derives it and
> fails if this file has drifted.

> **Public edition — de-identified.** Disease-level only. Nothing here is
> medical advice, and nothing here describes an individual.

## What this page is

The causal layer is assembled, not authored. Every node below is an existing
claim record, every edge is a link the registry already declares, and every
candidate is a sentence already written in this repository. The assembler
adds no relationship and types no edge: a relation type appears here only
when a claim record annotates the link with one, and the count of those
annotations is reported below whatever it happens to be.

## Population and coverage

| Measure | Count |
|---|---|
| Claim nodes | 39 |
| Claim→claim wikilink occurrences | 41 |
| …distinct directed links | 30 |
| …undirected edges they collapse into | 20 |
| Edges carrying a declared relation type | 0 |
| Nodes carrying a biological scale | 0 |
| Deep-dive manifests read | 67 |
| …of which bound to at least one claim | 30 |
| Propositions scanned | 1169 |
| …carrying a relational connective | 322 |
| …locator-backed candidates | 285 |
| …locator-backed and bound to a claim | 111 |

The scanned population is three declared surfaces and no others: every claim
`Title`, every row of the working model's BLOCK 2 mirror, and every
`proposition` in every deep-dive work manifest. `Summary`, `Clinical meaning`
and `Evidence boundary` are prose paragraphs and are **not** scanned —
atomizing a paragraph is a reading operation with its own contract, and a
regex sweep of one would produce fragments wearing an extraction's authority.

## 1 · Nodes

| Node | Declared title | Status | Type | Pathway | Scale | Deg | Papers |
|---|---|---|---|---|---|---|---|
| CLAIM 001 | Vigabatrin associated with VABAM in WWOX-DEE | conflicting evidence | DATO | P2 — GABAergic vulnerability / safety | NOT_ANNOTATED | 3 | 4 |
| CLAIM 002 | WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype | consolidated baseline | DATO + INFERENZA prudente | P1 — Ca²⁺ / network dysregulation; P7 —  | NOT_ANNOTATED | 1 | 2 |
| CLAIM 003 | Neuronal WWOX deletion induces non-cell-autonomous hypomyelination | consolidated baseline | DATO | P4 — myelination / white matter | NOT_ANNOTATED | 2 | 1 |
| CLAIM 004 | AAV9-WWOX neuron-targeted rescue shows multi-domain in vivo improvement | consolidated baseline | DATO | P7 — gene therapy readiness | NOT_ANNOTATED | 2 | 1 |
| CLAIM 005 | Reduced GABAergic interneurons and glial activation in WWOX-KO | consolidated baseline | DATO | P2 — GABAergic vulnerability; P6 — neuro | NOT_ANNOTATED | 4 | 3 |
| CLAIM 006 | P47T model shows progressive neuroinflammation | consolidated baseline | DATO + INFERENZA prudente | P6 — neuroinflammation / glia | NOT_ANNOTATED | 0 | 1 |
| CLAIM 007 | P47T abolishes PPxY binding to WW-domain partners | consolidated baseline | DATO | P3 — MYC/Wnt / interaction logic | NOT_ANNOTATED | 0 | 2 |
| CLAIM 008 | WOREE and SCAR12 form a genotype-phenotype spectrum | consolidated baseline | DATO | Clinical spectrum / genotype-phenotype | NOT_ANNOTATED | 0 | 3 |
| CLAIM 009 | WWOX deficiency plausibly alters mitochondrial quality control, redox and energy efficiency | in observation | INFERENZA | P5 — metabolism / mitochondria / redox / | NOT_ANNOTATED | 5 | 9 |
| CLAIM 010 | Mitophagy may be more relevant than senolytics for WWOX-related mitochondrial dysfunction | background only | IPOTESI | P5 — metabolism / mitochondria / mitopha | NOT_ANNOTATED | 0 | 0 |
| CLAIM 011 | AAV9-hSynI-hWWOX: dose-dependent durable rescue in Wwox-null murine model su domini multipli inc | flagged for review | DATO preclinico (full text reviewed) | P7 — gene therapy readiness; P4 — myelin | NOT_ANNOTATED | 0 | 1 |
| CLAIM 012 | Fenotipo WWOX severo neonatale-fatale con MRI inizialmente normale: genotipo-severità heterogene | consolidated baseline | DATO descrittivo (full text reviewed) | clinical spectrum / genotype-phenotype | NOT_ANNOTATED | 0 | 1 |
| CLAIM 013 | In WWOX-DEE, genotipi biallelici null/null associati a maggiore rischio di crisi, ipertonia e co | in observation | DATO con limiti metodologici dichiarati | Clinical spectrum / genotype-phenotype / | NOT_ANNOTATED | 0 | 2 |
| CLAIM 014 | WWOX loss perturbs prenatal cortical development, neuronal migration and cortical maturation acr | consolidated baseline | DATO | P3 — neurodevelopment / migration / cort | NOT_ANNOTATED | 0 | 3 |
| CLAIM 015 | Part of WWOX-related epileptic encephalopathy likely arises on a structurally misassembled prena | consolidated baseline | INFERENZA strongly supported | P3 / P1 / P4 | NOT_ANNOTATED | 0 | 3 |
| CLAIM 016 | GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency | in observation | DATO (abbondanza, murino) + **DATO mecca | emerging node — GSK3β / seizure suscepti | NOT_ANNOTATED | 3 | 2 |
| CLAIM 017 | WWOX-related human disease spans a spectrum from severe WOREE/WWOX-DEE to milder SCAR12-like phe | consolidated baseline | DATO | human spectrum / genotype-phenotype | NOT_ANNOTATED | 0 | 0 |
| CLAIM 018 | The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exon 6 skipping in humans | consolidated baseline | DATO | genotype / splicing / pathogenicity | NOT_ANNOTATED | 0 | 1 |
| CLAIM 019 | Q230P is pathogenic in severe human compound context and must not be treated as a benign or weak | consolidated baseline | DATO (endpoint funzionale: mRNA normale  | genotype / compound-context interpretati | NOT_ANNOTATED | 7 | 4 |
| CLAIM 020 | Selected WWOX-related trajectories may include survival into adulthood with severe disability an | consolidated baseline | DATO | natural history / clinical spectrum | NOT_ANNOTATED | 0 | 0 |
| CLAIM 021 | WWOX loss directly destabilizes neocortical network physiology through combined synaptic and int | consolidated baseline | DATO | P1 — network hyperexcitability / cortica | NOT_ANNOTATED | 0 | 1 |
| CLAIM 022 | Severe WWOX-null phenotypes can begin prenatally and may include detectable fetal brain abnormal | consolidated baseline | DATO | prenatal developmental architecture / se | NOT_ANNOTATED | 0 | 0 |
| CLAIM 023 | WWOX controls partner-protein function not only by binding, but by phosphorylation-dependent sub | consolidated baseline | DATO | signaling organization / routing / scaff | NOT_ANNOTATED | 0 | 0 |
| CLAIM 024 | WWOX WW-domain function depends on WW1–WW2 tandem cooperativity, not only on isolated domain int | consolidated baseline | DATO | domain architecture / variant interpreta | NOT_ANNOTATED | 0 | 1 |
| CLAIM 025 | The WWOX/HIF1A ratio may function as a systems-level marker of maladaptive biological state, lin | in observation | DATO + INFERENZA | P5 — metabolism / state transition / inf | NOT_ANNOTATED | 0 | 0 |
| CLAIM 026 | WWOX may function as a trafficking–metabolism coupling node linking endomembrane systems with ca | in observation | DATO + INFERENZA | P5 — trafficking / endomembrane systems  | NOT_ANNOTATED | 0 | 1 |
| CLAIM 027 | WWOX may act as an ECM/membrane-to-nucleus signaling node through HYAL-2/SMAD4 complexes, with c | in observation | INFERENZA | ECM / membrane signaling / injury respon | NOT_ANNOTATED | 0 | 0 |
| CLAIM 028 | WWOX biological output is strongly partner- and context-dependent; expression level alone is ins | flagged for review | INFERENZA — principio interpretativo tra | cross-pathway interpretive principle | NOT_ANNOTATED | 4 | 5 |
| CLAIM 029 | WWOX contributes directly to DNA-damage-response competence and genome-stability maintenance, at | in observation | DATO + INFERENZA prudente | genome stability / ATM / DNA damage resp | NOT_ANNOTATED | 0 | 2 |
| CLAIM 030 | In WWOX the severity tracks residual protein FUNCTION, not protein abundance | in observation | DATO (serie allelica su cellule di pazie | genotype / protein function / proteostas | NOT_ANNOTATED | 8 | 5 |
| CLAIM 031 | WWOX-DEE is a developmental AND epileptic encephalopathy: seizure control does not rescue develo | in observation | DATO (osservazione clinica) + INFERENZA  | clinical course / therapeutic strategy | NOT_ANNOTATED | 4 | 2 |
| CLAIM 032 | WWOX haploinsufficiency is not deleterious: the therapeutic threshold is well below full restora | in observation | DATO (topo, ratto, e ogni famiglia umana | P7 — gene therapy readiness / dose-thres | NOT_ANNOTATED | 6 | 12 |
| CLAIM 033 | Biallelic null WWOX carries higher mortality than genotypes with at least one missense — but the | in observation | DATO (statistica di coorte) + IPOTESI (l | genotype-phenotype / prognosis | NOT_ANNOTATED | 3 | 1 |
| CLAIM 034 | In a post-mitotic excitable neuron under metabolic stress, WWOX up-regulation is pro-oxidant — r | in observation | DATO (sistema fotorecettoriale) + ESPANS | P5 — metabolism / redox · secondario P1  | NOT_ANNOTATED | 6 | 2 |
| CLAIM 035 | WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-like docking motif in the SD | in observation | DATO (biochimica, cinque saggi ortogonal | P1 neurosviluppo / GSK3β–Tau–microtubuli | NOT_ANNOTATED | 6 | 1 |
| CLAIM 036 | A systemic constitutive Wwox-null mouse at P18 is metabolically decompensated, so any brain phen | in observation | DATO (le misure) + INFERENZA (la portata | P5 — metabolismo / rene; confondente tra | NOT_ANNOTATED | 5 | 4 |
| CLAIM 037 | The seizure phenotype of the Wwox literature is a rat `lde/lde` phenotype, electrographically do | in observation | DATO | P2 — eccitabilità / epilettogenesi | NOT_ANNOTATED | 6 | 2 |
| CLAIM 038 | Elevated BUN and creatinine recur across Wwox rodent models with two competing explanations — re | in observation | DATO (le misure) + IPOTESI (entrambe le  | P5 — metabolismo / rene | NOT_ANNOTATED | 5 | 3 |
| CLAIM 039 | Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95% versus 0% — and it  | in observation | DATO | P1 — neurosviluppo / funzione motoria | NOT_ANNOTATED | 2 | 1 |

## 2 · Edges declared by the registry

| Edge | Reciprocal | Declared in | Type | Basis | Shared evidence |
|---|---|---|---|---|---|
| CLAIM 001 <-> CLAIM 002 | **one-way** | Clinical meaning | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | — |
| CLAIM 001 <-> CLAIM 031 | yes | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 045 |
| CLAIM 003 <-> CLAIM 004 | yes | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | — |
| CLAIM 005 <-> CLAIM 036 | **one-way** | Evidence boundary | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 057 |
| CLAIM 005 <-> CLAIM 037 | yes | Evidence boundary, Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 058 |
| CLAIM 009 <-> CLAIM 028 | **one-way** | ⚠️ Counter-directional evidence (BATCH_20260726_001) | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 054 |
| CLAIM 009 <-> CLAIM 034 | yes | Summary, ⚠️ Counter-directional evidence (BATCH_20260726_001) | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 054, PAPER 071 |
| CLAIM 016 <-> CLAIM 035 | yes | Meccanismo aggiunto (BATCH_20260726_001), Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 056 |
| CLAIM 019 <-> CLAIM 030 | yes | Source, Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 041, PAPER 042 |
| CLAIM 019 <-> CLAIM 032 | yes | Source, Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 041 |
| CLAIM 019 <-> CLAIM 033 | **one-way** | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 040 |
| CLAIM 028 <-> CLAIM 034 | **one-way** | Clinical meaning | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 054 |
| CLAIM 028 <-> CLAIM 035 | **one-way** | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 056 |
| CLAIM 030 <-> CLAIM 032 | **one-way** | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 039, PAPER 041, PAPER 043 |
| CLAIM 030 <-> CLAIM 033 | **one-way** | Clinical meaning | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | — |
| CLAIM 030 <-> CLAIM 035 | **one-way** | Clinical meaning | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 056 |
| CLAIM 031 <-> CLAIM 032 | **one-way** | Clinical meaning | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 049 |
| CLAIM 036 <-> CLAIM 038 | yes | Summary, Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 057 |
| CLAIM 037 <-> CLAIM 038 | yes | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 058, PAPER 059 |
| CLAIM 037 <-> CLAIM 039 | yes | Wikilinks | UNTYPED | NO_DECLARED_RELATION_ANNOTATION | PAPER 059 |

Every edge carrying `NO_DECLARED_RELATION_ANNOTATION` is an edge that exists
and has never been given a direction of causation, an intermediate, or an
evidence type. Typing it requires reading the evidence behind both endpoints;
the assembler refuses to derive it from the endpoints' declared fields,
because two demonstrated facts are not a demonstrated relation between them.

A Scientist types an edge by annotating the wikilink in the claim record:

```markdown
[[claim_registry_current#CLAIM 004]] (relation: DIRECT — the same experiment
measures both endpoints)
```

Accepted values: `DIRECT` · `INDIRECT_UNKNOWN_INTERMEDIATES` · `ASSOCIATED` · `CONTROVERSIAL_OPEN`. Anything else is
reported as `RELATION_TYPE_UNRECOGNISED` and is never coerced into a type.

## 3 · Where the causal content actually sits

18 of 39 claim titles state a
relation, and every declared edge states none. The causal content of this
model is largely **inside its nodes**: *"Neuronal WWOX deletion induces
non-cell-autonomous hypomyelination"* is a cause, a relation and an effect
compressed into a node label. That is why the edge layer reads as empty —
not because the relationships were never established, but because they were
written where a graph cannot see them.

Decomposing such a title into two entities and a typed relation decides
which half is the cause. That is a reading, and it is Scientist work; the
assembler lists the titles and stops there.

| Node | Connective | Class | Morphology | Declared title |
|---|---|---|---|---|
| CLAIM 001 | `associated with` | ASSOCIATIVE | finite or multiword | Vigabatrin associated with VABAM in WWOX-DEE |
| CLAIM 002 | `causes` | CAUSAL | finite or multiword | WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype |
| CLAIM 003 | `induces` | CAUSAL | finite or multiword | Neuronal WWOX deletion induces non-cell-autonomous hypomyelination |
| CLAIM 004 | `rescue` | CAUSAL | ambiguous bare form | AAV9-WWOX neuron-targeted rescue shows multi-domain in vivo improvement |
| CLAIM 005 | `reduced` | CAUSAL | ambiguous bare form | Reduced GABAergic interneurons and glial activation in WWOX-KO |
| CLAIM 007 | `abolishes` | CAUSAL | finite or multiword | P47T abolishes PPxY binding to WW-domain partners |
| CLAIM 009 | `control` | CAUSAL | ambiguous bare form | WWOX deficiency plausibly alters mitochondrial quality control, redox and energy efficienc |
| CLAIM 011 | `rescue` | CAUSAL | ambiguous bare form | AAV9-hSynI-hWWOX: dose-dependent durable rescue in Wwox-null murine model su domini multip |
| CLAIM 013 | `associati a` | ASSOCIATIVE | finite or multiword | In WWOX-DEE, genotipi biallelici null/null associati a maggiore rischio di crisi, ipertoni |
| CLAIM 014 | `perturbs` | CAUSAL | finite or multiword | WWOX loss perturbs prenatal cortical development, neuronal migration and cortical maturati |
| CLAIM 016 | `contribute to` | CAUSAL | finite or multiword | GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency |
| CLAIM 018 | `causes` | CAUSAL | finite or multiword | The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exon 6 skipping in huma |
| CLAIM 021 | `destabilizes` | CAUSAL | finite or multiword | WWOX loss directly destabilizes neocortical network physiology through combined synaptic a |
| CLAIM 023 | `controls` | CAUSAL | ambiguous bare form | WWOX controls partner-protein function not only by binding, but by phosphorylation-depende |
| CLAIM 024 | `depends on` | DEPENDENCY | finite or multiword | WWOX WW-domain function depends on WW1–WW2 tandem cooperativity, not only on isolated doma |
| CLAIM 031 | `control` | CAUSAL | ambiguous bare form | WWOX-DEE is a developmental AND epileptic encephalopathy: seizure control does not rescue  |
| CLAIM 034 | `reduces` | CAUSAL | finite or multiword | In a post-mitotic excitable neuron under metabolic stress, WWOX up-regulation is pro-oxida |
| CLAIM 035 | `requires` | DEPENDENCY | finite or multiword | WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-like docking motif in  |

### 3.1 Where the two wordings of a node disagree

Each node is written twice — once as a registry `Title`, once as a row of
the working model's BLOCK 2 mirror — and a LINT rule keeps their *status*
in sync. Nothing keeps their relational content in sync, and it has
diverged. Which wording is right is a reading; that they disagree is a
measurement, and normalising it is what this layer is for.

🔴 Not every row here is a difference in content. A multi-word connective
is matched as one string, so an adverb inserted into it — *"contributes
**directly** to"* — reads as absent. Read the two wordings, not the flag.

| Node | Relational in | Connective | That wording | The other wording |
|---|---|---|---|---|
| CLAIM 006 | mirror row only | `→` | P47T model → progressive neuroinflammation | P47T model shows progressive neuroinflammation |
| CLAIM 018 | registry title only | `causes` | The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exo | Exon-6 splice disruption is a confirmed pathogenic mechanism in human  |
| CLAIM 026 | mirror row only | `→` | WWOX as a trafficking–metabolism coupling node (endomembrane → Acetyl- | WWOX may function as a trafficking–metabolism coupling node linking en |
| CLAIM 029 | mirror row only | `contributes to` | WWOX contributes to ATM-linked DDR competence and genome-stability mai | WWOX contributes directly to DNA-damage-response competence and genome |
| CLAIM 035 | registry title only | `requires` | WWOX is a direct, residue-mapped inhibitor of GSK3β through an Axin-li | WWOX is a direct, residue-mapped inhibitor of GSK3β via an Axin-like S |

## 4 · What is absent, separated by *kind* of absence

### 4.1 Annotation gaps — the relationship is in the repository, the edge is not

**One-way links.** One side declares the link and the other does not.

| Edge | Declared | Not declared |
|---|---|---|
| CLAIM 001 <-> CLAIM 002 | CLAIM 001 -> CLAIM 002 | CLAIM 002 -> CLAIM 001 |
| CLAIM 005 <-> CLAIM 036 | CLAIM 036 -> CLAIM 005 | CLAIM 005 -> CLAIM 036 |
| CLAIM 009 <-> CLAIM 028 | CLAIM 009 -> CLAIM 028 | CLAIM 028 -> CLAIM 009 |
| CLAIM 019 <-> CLAIM 033 | CLAIM 033 -> CLAIM 019 | CLAIM 019 -> CLAIM 033 |
| CLAIM 028 <-> CLAIM 034 | CLAIM 034 -> CLAIM 028 | CLAIM 028 -> CLAIM 034 |
| CLAIM 028 <-> CLAIM 035 | CLAIM 035 -> CLAIM 028 | CLAIM 028 -> CLAIM 035 |
| CLAIM 030 <-> CLAIM 032 | CLAIM 030 -> CLAIM 032 | CLAIM 032 -> CLAIM 030 |
| CLAIM 030 <-> CLAIM 033 | CLAIM 033 -> CLAIM 030 | CLAIM 030 -> CLAIM 033 |
| CLAIM 030 <-> CLAIM 035 | CLAIM 035 -> CLAIM 030 | CLAIM 030 -> CLAIM 035 |
| CLAIM 031 <-> CLAIM 032 | CLAIM 032 -> CLAIM 031 | CLAIM 031 -> CLAIM 032 |

**Unlinked prose mentions.** A claim names another claim in prose with no
wikilink, so the relation is asserted in text and invisible to the graph.

| Claim | Names | In field |
|---|---|---|
| CLAIM 025 | CLAIM 009 | Clinical meaning |

**Working-model co-mentions.** Two claims named in one sentence of the
working model with no edge between them in the registry.

| Claims | Sentence |
|---|---|
| CLAIM 025 ↔ CLAIM 026 | *(CLAIM 025 / paper 191; CLAIM 026 / PAPER 032, Hussain 2018.)* |

### 4.2 Isolated nodes

| Node | Verdict | Material found in the repository |
|---|---|---|
| CLAIM 006 | REVIEW_MATERIAL_PRESENT | SHARED_EVIDENTIAL_PAPER |
| CLAIM 007 | REVIEW_MATERIAL_PRESENT | SELF_RELATIONAL_TITLE, SHARED_EVIDENTIAL_PAPER |
| CLAIM 008 | REVIEW_MATERIAL_PRESENT | SHARED_EVIDENTIAL_PAPER |
| CLAIM 010 | NO_RELATION_MATERIAL_IN_REPOSITORY | — |
| CLAIM 011 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND, SELF_RELATIONAL_TITLE |
| CLAIM 012 | NO_RELATION_MATERIAL_IN_REPOSITORY | — |
| CLAIM 013 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND, SELF_RELATIONAL_TITLE, SHARED_EVIDENTIAL_PAPER |
| CLAIM 014 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND, SELF_RELATIONAL_TITLE, SHARED_EVIDENTIAL_PAPER |
| CLAIM 015 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND, SHARED_EVIDENTIAL_PAPER |
| CLAIM 017 | NO_RELATION_MATERIAL_IN_REPOSITORY | — |
| CLAIM 018 | REVIEW_MATERIAL_PRESENT | SELF_RELATIONAL_TITLE, SHARED_EVIDENTIAL_PAPER |
| CLAIM 020 | NO_RELATION_MATERIAL_IN_REPOSITORY | — |
| CLAIM 021 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND, SELF_RELATIONAL_TITLE |
| CLAIM 022 | NO_RELATION_MATERIAL_IN_REPOSITORY | — |
| CLAIM 023 | REVIEW_MATERIAL_PRESENT | SELF_RELATIONAL_TITLE |
| CLAIM 024 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND, SELF_RELATIONAL_TITLE, SHARED_EVIDENTIAL_PAPER |
| CLAIM 025 | ANNOTATION_GAP_CONFIRMED | UNLINKED_PROSE_MENTION, WORKING_MODEL_COMENTION |
| CLAIM 026 | ANNOTATION_GAP_CONFIRMED | WORKING_MODEL_COMENTION |
| CLAIM 027 | NO_RELATION_MATERIAL_IN_REPOSITORY | — |
| CLAIM 029 | REVIEW_MATERIAL_PRESENT | LOCATOR_PROPOSITION_BOUND |

🔴 `NO_RELATION_MATERIAL_IN_REPOSITORY` is a statement about this repository,
not about biology. It means the assembler found nothing here to annotate — no
unlinked mention, no co-mention, no shared evidential paper, no relational
proposition bound to the claim. The literature is not the denominator.

### 4.3 Shared evidence without an edge — review candidates, lowest priority

Two claims resting on the same paper are not thereby related. This list is a
place to look, not a set of missing edges.

| Claims | Shared evidential papers |
|---|---|
| CLAIM 001 ↔ CLAIM 009 | PAPER 017 |
| CLAIM 001 ↔ CLAIM 013 | PAPER 017 |
| CLAIM 002 ↔ CLAIM 030 | PAPER 039 |
| CLAIM 002 ↔ CLAIM 032 | PAPER 039 |
| CLAIM 005 ↔ CLAIM 038 | PAPER 057, PAPER 058 |
| CLAIM 006 ↔ CLAIM 007 | PAPER 007 |
| CLAIM 007 ↔ CLAIM 008 | PAPER 042 |
| CLAIM 007 ↔ CLAIM 019 | PAPER 042 |
| CLAIM 007 ↔ CLAIM 030 | PAPER 042 |
| CLAIM 008 ↔ CLAIM 019 | PAPER 040, PAPER 042 |
| CLAIM 008 ↔ CLAIM 030 | PAPER 042 |
| CLAIM 008 ↔ CLAIM 033 | PAPER 040 |

Showing 12 of 22. The complete list is in the export.

## 5 · Candidate edges — propositions already written, awaiting review

A candidate is a sentence that already exists in the repository and contains a
connective from the closed lexicon. It is **not** an edge. The lexical split
shown in the export is a split on a string; which biological entity sits on
each side is a reading, and every record carries `endpoints_resolved: false`.

| Source | Candidates |
|---|---|
| claim_title | 18 |
| locator_proposition | 285 |
| working_model_mirror_title | 19 |

| Connective class (lexical) | Candidates |
|---|---|
| ARROW | 11 |
| ASSOCIATIVE | 15 |
| CAUSAL | 264 |
| DEPENDENCY | 32 |

A connective class is a property of the word, not a verdict about the
relationship. An `ASSOCIATIVE` connective does not make an edge `ASSOCIATED`.

### 5.1 Candidates bound to a claim node

| Bound to | Source | Connective | Proposition (verbatim) |
|---|---|---|---|
| CLAIM 001 | claim_title | `associated with` | Vigabatrin associated with VABAM in WWOX-DEE |
| CLAIM 002 | claim_title | `causes` | WWOX-LoF causes network hyperexcitability; AAV-WWOX rescues organoid phenotype |
| CLAIM 003 | claim_title | `induces` | Neuronal WWOX deletion induces non-cell-autonomous hypomyelination |
| CLAIM 004 | claim_title | `rescue` | AAV9-WWOX neuron-targeted rescue shows multi-domain in vivo improvement |
| CLAIM 005 | claim_title | `reduced` | Reduced GABAergic interneurons and glial activation in WWOX-KO |
| CLAIM 007 | claim_title | `abolishes` | P47T abolishes PPxY binding to WW-domain partners |
| CLAIM 009 | claim_title | `control` | WWOX deficiency plausibly alters mitochondrial quality control, redox and energy efficiency |
| CLAIM 011 | claim_title | `rescue` | AAV9-hSynI-hWWOX: dose-dependent durable rescue in Wwox-null murine model su domini multipli inclusi ECoG/SWD, mielinizz |
| CLAIM 013 | claim_title | `associati a` | In WWOX-DEE, genotipi biallelici null/null associati a maggiore rischio di crisi, ipertonia e complicanze respiratorie r |
| CLAIM 014 | claim_title | `perturbs` | WWOX loss perturbs prenatal cortical development, neuronal migration and cortical maturation across species |
| CLAIM 016 | claim_title | `contribute to` | GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency |
| CLAIM 018 | claim_title | `causes` | The exon 6 splice-site variant c.517-2A>G is pathogenic and causes exon 6 skipping in humans |

Showing 12 of 148 bound candidates; the
complete set, with evidence and provenance, is in the export. The worklist
in cost order — what needs an annotation, what needs a type, what needs a
decomposition, what needs a reading — is printed by:

```bash
python3 framework/scripts/pathograph.py --disease wwox --queue --limit 20
```

## 6 · Losses

None. Every scanned proposition was either emitted as a candidate or
carried no connective from the lexicon.

## Provenance

Derived from 70 input files; digest
`c60e630c385dbc37`. Sources: the claim, paper and
working-model registries, and every deep-dive work manifest.

