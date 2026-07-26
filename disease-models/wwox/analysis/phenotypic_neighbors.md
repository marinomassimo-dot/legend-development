# WWOX / WOREE — Phenotypic-similarity neighbours & MAXO crosswalk

**A reusable, offline capability that (a) ranks the diseases phenotypically nearest to WOREE from public HPO annotations, as a discovery/repurposing lead generator, and (b) crosswalks WWOX therapeutic-modality classes to the Medical Action Ontology (MAXO).**

> Public, disease-level analysis. Inputs are a disease identifier and public ontologies (HPO, MONDO, MAXO) — **no individual is referenced**, and no patient data is used or required. Phenotypic proximity is a *reading-queue ordering*, **not** mechanistic transfer: every neighbour is a lead to read, never a conclusion (`ESPANSIONE`).

---

## Why this matters

For a rare disease, two questions recur: *which other disorders resemble it phenotypically* (they may share a druggable pathway or an already-human therapy → repurposing/discovery leads), and *how do we describe candidate interventions in a standard, interoperable vocabulary* (so a therapeutic portfolio is machine-readable and can feed a knowledge base such as DisMech). This folder answers both with public ontology tooling, reproducibly and offline.

## Capability 1 — Phenotypic neighbours of WOREE

- **Engine:** information-content-weighted Resnik best-match, symmetric ("phenodigm"-style) average — the same score family as Monarch's `semsimian`/OAK, re-implemented dependency-free in `../../../scripts/phenotypic_neighbors.py` (Python standard library only).
- **Corpus:** HPO `phenotype.hpoa` (12,956 annotated diseases) + the HPO `hp.obo` is_a graph; IC computed over the annotation corpus.
- **Query:** WOREE = **OMIM:616211** (Developmental and epileptic encephalopathy 28), 50 annotated HPO terms.
- **Runtime:** whole-corpus ranking in ~15 s on a laptop, fully offline.
- **Output:** [`data/WWOX_WOREE_phenotypic_neighbors.tsv`](data/WWOX_WOREE_phenotypic_neighbors.tsv) (top 40).

### What the ranking says — and does not

**Sanity check (passes):** the top ~20 neighbours are other developmental/epileptic encephalopathies (DEE-14, EIEE-13, DEE-112/119/121/122, Dravet syndrome, DEE-16/18/19…). This is exactly what an IC-weighted phenotype match *should* return for WOREE, and it confirms the engine measures what it claims.

**Where the discovery value is:** not the top-1. Numbered "DEE-N" neighbours confirm the phenotype but rarely add a *new lever* (like WOREE case reports: consistent but descriptive). The repurposing value sits in neighbours with a **distinct mechanism** that carry a druggable pathway or an already-human therapy. Selected `ESPANSIONE` leads from the top-40, offered **to read, not to assume**:

| Neighbour (public) | Why it is an interesting seed | Falsifiable next step |
|---|---|---|
| MCAHS2 (OMIM:300868) | GPI-anchor / PIG-pathway family — a distinct metabolic axis | full text: causal gene + any supplementation rationale |
| Pitt-Hopkins-like 1 (OMIM:610042) | synaptic-adhesion axis (CNTNAP2/NRXN1 family) | verify pathway and overlap with network-protection levers |
| Microcephaly-seizures-spasticity-brain-calcification (OMIM:251280) | calcification / metabolic axis | full text: cause + candidate biomarker |

> ⚠️ The pathway/gene attributions above are *prior expectations to verify*, not extracted from the annotation file (which contains no genes). They must be checked against primary literature before being cited — no claim is made here.

**Honest limits (why this stays `ESPANSIONE`):** annotations describe *diseases*, not genes/drugs, so the bridge to repurposing needs a second gene→therapy hop (not yet done); IC carries an annotation bias (well-studied diseases weigh more); a richly annotated query (50 terms) favours matches with equally rich annotation.

## Capability 2 — WWOX therapeutic modalities → MAXO crosswalk

Crosswalk of the WWOX/WOREE therapeutic-modality classes (see [`../therapeutics/therapeutic_strategies_current.md`](../therapeutics/therapeutic_strategies_current.md)) to Medical Action Ontology terms, verified against a local MAXO release: [`data/WWOX_layer9_maxo_crosswalk.tsv`](data/WWOX_layer9_maxo_crosswalk.tsv).

- **Solid MAXO anchors:** antisense oligonucleotide therapy (`MAXO:0001593`), incl. **intrathecal** CNS delivery (`MAXO:0020026`); gene editing therapy (`MAXO:0001484`); gene therapy (`MAXO:0001001`); anticonvulsant agent therapy (`MAXO:0000167`); electroencephalography (`MAXO:0000932`).
- **Three real MAXO gaps** (candidate contributions, alongside the WWOX disorder absent from DisMech): pharmacological chaperone / proteostasis modulator; a lithium/mood-stabiliser action term; and an *active neuro-surveillance* term (only "surveillance for malignancies" exists).
- **Granularity note:** MAXO does not separate transcriptional up-regulation (CRISPRa) or gene addition vs editing under `gene therapy`.

## Reproduce

```bash
curl -L -o phenotype.hpoa https://purl.obolibrary.org/obo/hp/hpoa/phenotype.hpoa
curl -L -o hp.obo         https://purl.obolibrary.org/obo/hp.obo
python3 ../../../scripts/phenotypic_neighbors.py \
    --hpoa phenotype.hpoa --hp-obo hp.obo --query OMIM:616211 --top 40
```

Unit tests (synthetic ontology, no downloads): `python3 ../../../scripts/test_phenotypic_neighbors.py`.

> In-silico predictions are hypotheses that prioritize reading and experiments; they are not experimental validation, and nothing here is medical advice.
