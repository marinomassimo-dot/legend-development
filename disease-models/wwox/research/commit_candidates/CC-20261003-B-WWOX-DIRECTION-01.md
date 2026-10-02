# COMMIT CANDIDATE — CC-20261003-B-WWOX-DIRECTION-01

**Status:** `PROPOSED — NOT PROPAGATED`
**Author:** ACTOR_ID `scientist` (Scientist B), intake wave 2 2026-10-03, branch `task/sci-B-20261003`.
**context_policy:** `SOURCE_FIRST` for all six readings; LEGEND's own records were opened only after each first pass was written (see `research/intake_wave_20261003_B.md`).
**Not medical advice.** Class-level statements about published models and genotypes only.

## Target
- `claim_registry_current.md`: **create** `CLAIM 044`, inserted after `CLAIM 043`.
- `full_text_queue_current.md`: **replace-within** `FT-159` — discharge the declared debt and record the audit's confirmation at source.

**Numbers are provisional** and `CLAIM 044` depends on `CLAIM 043` existing, so this candidate is applied **after** `CC-20261003-B-CASCADE-INDEPENDENCE-01`.

## Change class
**MINOR** (§ 7). A new claim at `in observation` plus a queue discharge. It narrows no `consolidated baseline` record. It does raise a directional caution that any WWOX-raising therapeutic hypothesis must answer, which is why it is a claim and not a note.

## Ordering
`CC-20261003-B-CASCADE-INDEPENDENCE-01` first (anchor), then this, then `CC-20261003-B-REGISTRY-01` (`PAPER 123` links to `044`).

## Why a claim and not a dismissal
Nothing here is rejected. The source's direction may be right; what the reading establishes is that the directional statement is a cell-line reporter result, that the in-vivo accumulation it is drawn from is not lateralised, and that the percentages quoted from it are bins of a categorical map. Recording that as an open ambiguity is honest; recording it as a refutation would not be.

## Op list — `claim_registry_current.md` (record-scoped; dry run 2026-10-02 against `main` f5f9468, run as a three-op sequence with `CLAIM 043` and the `CLAIM 032` qualification because this op anchors on a record the first candidate creates: exit 0, 3 ops, keys `['CLAIM 042', 'CLAIM 043', 'CLAIM 032']`; this op inserted 3904 bytes, replaced 0; scope proof clean)

```json
[
 {
  "op": "insert-after",
  "id": "CLAIM 043",
  "text": "\n## CLAIM 044\n**Title:** The direction of WWOX activity in stressed neurons is unresolved: one in-vivo record makes activated WWOX pro-death, and it is not reconciled anywhere\n**Status:** in observation\n**Type:** DATO (the injury time course and its bounds) + INFERENZA (the consequence for a WWOX-raising strategy)\n**Pathway:** P3 — neuronal injury and WWOX directionality\n**Genotype/model relevance:** none — wild-type rats; the measurement is of endogenous WWOX **gain** of nuclear activity under stress, not of a loss-of-function allele\n**Transferability:** T3\n**clinical relevance:** MODERATE-HIGH — it is the one published direction that points against a strategy which raises WWOX activity, and it has never been tested by anyone else\n**Summary:** In rat dorsal root ganglia after sciatic transection, `Wwox` mRNA rises within 30 minutes, Tyr33-phosphorylated WWOX accumulates in neuronal nuclei over two months, and the authors conclude that WWOX inhibits the pro-survival CREB and enhances pro-apoptotic NF-κB signalling — i.e. that activated WWOX is pro-death. Read at source (2026-10-03), three bounds hold. **(1)** The directional claim is a **Gal4-fusion luciferase assay after transient over-expression in HEK-293 fibroblasts**; no panel of the figure that carries it contains a neuron. The in-neuron work is binding — FRET in primary DRG cultures and immuno-EM in tissue — never transcriptional output. **(2)** The chronic accumulation is **not lateralised**: at month 2 the uninjured contralateral ganglion shows ≈ 72% of small neurons with nuclear p-WOX1 against ≈ 71% ipsilaterally, and sham animals already sit at 31–37%, so axotomy is not its sufficient cause. **(3)** The abstract's *«>65%»* and *«40–65%»* are **bin labels of a categorical heat map** with no n, no error and no test, and neuronal death at the endpoint is *«less than 5%»*. The corpus's only attempt to reconcile this with the protective framing of the same group's later papers is a two-phospho-state proposal (pY33 protective, pS14 pathogenic) whose own review says the pathways *«remain to be established»*.\n**Clinical meaning:** For a loss-of-function genotype class the practical consequence is narrow but real: a strategy that **raises** WWOX activity in stressed neurons has one in-vivo record pointing the wrong way, and that record is unreplicated — PubMed `WWOX AND \"dorsal root ganglion\"` returns exactly one paper, this one. Restoring WWOX to a deficient neuron and over-activating WWOX in a sufficient one are not the same intervention, and nothing published measures the second in a WWOX-deficient background. Not medical advice.\n**Source:** [[paper_registry_current#PAPER 123]] (PMID 19918364) · [[paper_registry_current#PAPER 124]] (the two-phospho-state proposal, PMID 34359949)\n**Wikilinks:** [[paper_registry_current#PAPER 123]] · [[paper_registry_current#PAPER 124]] · [[claim_registry_current#CLAIM 043]]\n**Impact on Working Model:** none to BLOCCO 1. It records a directional ambiguity that any WWOX-raising therapeutic hypothesis must answer, and names what would settle it.\n🔴 **`DO_NOT_INFER`:** this record does **not** say that restoring WWOX is harmful. The source measures stress-induced activation of an intact gene in wild-type animals; it contains no WWOX-deficient neuron and no restoration arm.\n🔴 **Attribution correction carried from the source (discharges `FT-159`):** the paper classifies neurons **by soma diameter only** (<20, 20–30, >30 µm). The strings `nocicept`, `unmyelin`, `IB4`, `CGRP` and `substance P` occur **zero times** in the fingerprinted artefact. Any size→modality reading of this paper is LEGEND's imported convention and must be attributed to LEGEND, not to the authors.\n**`REVIVAL_TRIGGER`:** a CREB- or NF-κB-dependent transcriptional readout measured in neurons with a defined WWOX genotype, by any laboratory.\n"
 }
]
```

## Op list — `full_text_queue_current.md` (record-scoped; dry run 2026-10-02 against `main` f5f9468: exit 0, 1 op, key `['FT-159']`, `replaced_bytes` 66, `inserted_bytes` 818, scope proof clean)

```json
[
 {
  "op": "replace-within",
  "id": "FT-159",
  "old": "**Priority:** **LOW** — read at served depth; the debt is formal",
  "new": "**Priority:** **LOW** — read at served depth; the debt is formal — 🟢 **DISCHARGED 2026-10-03** by `CC-20261003-B-WWOX-DIRECTION-01` (intake wave 2, Scientist B): the JATS deposit, all eight figures and all nine supplementary TIFFs were acquired and a receipt was written (`FTR-20261003-19918364-01`, `complete_fulltext_read`), with manifest `deepdive_manifests/PMID19918364.json`. The audit's finding is **confirmed at source** — the paper classifies by soma diameter only and `nocicept`, `unmyelin`, `IB4`, `CGRP` and `substance P` occur zero times — and three further bounds were added in [[claim_registry_current#CLAIM 044]]: the directional claim is a HEK-293 reporter assay, the chronic accumulation is equal on the uninjured side, and the headline percentages are bin labels of a categorical heat map."
 }
]
```

### LOCATOR TRIPLES FOR BLIND AUDIT

(The paper's own size definition is morphometric | `accumulated in the nuclei of small neurons (&lt;20` | PMID 19918364, Results, 'Axotomy Induces Protein Expression and Activation of WOX1 in DRG Neurons')

(The chronic co-activation is reported in the uninjured side too | `dramatic co-activation of WOX1 (&gt;65% of cells), CREB` | PMID 19918364, Results, 'Dramatic Co-Activation of WOX1 with Transcription Factor CREB and NF-kB in Small Neurons at Month 2 Post-Injury Correlates with Initiation of Neuronal Death')

(The directional claim comes from over-expression in a kidney fibroblast line | `EGFP-WOX1 was transiently overexpressed` | PMID 19918364, Figure 5 legend, panels B-D)

(The death the title calls a delayed loss | `Approximately less than 5% neuronal death was observed post axotomy` | PMID 19918364, Results, 'Rapid Upregulation of Wwox Gene Expression in DRG Neurons upon Sciatic Nerve Transection')

(Two mechanistic steps are unpublished data of the same laboratory | `, unpublished). This binding may result in accumulation of` | PMID 19918364, Discussion, paragraph on NF-κB transcriptional activation)

(Figure attestation: the lateralisation numbers | `[figure attestation - pixels cannot be quote-matched] Supplementary Fig. S3, two bar charts 'Contralateral' and 'Ipsilateral', y-axis '% Neurons with nuclear p-WOX1', x-axis Sham, 6 h, 1 d, 7 d, 2 m, black = small neurons and white = medium-large. Contralateral small: ~37, ~36, ~30, ~43, ~72. Ipsilateral small: ~31, ~50, ~41, ~63, ~71.` | PMID 19918364, Supplementary Figure S3, `files/figure_renders/PMID19918364/pone.0007820.s003.png`)

(Figure attestation: the time course is a categorical heat map | `[figure attestation - pixels cannot be quote-matched] Fig 4 is a table-like grid, rows p-WOX1 / c-Jun / p-JNK / ATF3 / p-CREB / NF-kB / Smad4 x Contra and Ipsi x small and med/large, columns 0.5 h, 6 h, 1 d, 3-7 d, 2 m, cells coloured by a five-step key: none 0%, very low <20%, low 20-40%, moderate 40-65%, high >65%; two p-CREB cells marked n.d.` | PMID 19918364, Figure 4, `files/figures/PMID19918364/native/pone.0007820.g004.jpg`)

(Figure attestation: no panel of the reporter figure contains a neuron | `[figure attestation - pixels cannot be quote-matched] Fig 5A Gal4 response-element schematic; 5B 'Control' Gal4-CMV; 5C 'Activated by WOX1' c-Jun and Elk-1; 5D 'Inhibited by WOX1' CREB, CRE, AP-1 as vector-versus-WOX1 pairs; 5E WWOX domain map with fold-activation 4.69 (WOX1), 7.90 (WW domains), 0.02 (SDR), 0.00 (ECFP).` | PMID 19918364, Figure 5, `files/figures/PMID19918364/native/pone.0007820.g005.jpg`)
