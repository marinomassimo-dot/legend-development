# WWOX — Variant Landscape & In-Silico Triage Pipeline

**A reusable computational pipeline that turns the full public WWOX variant set into a prioritized list of *which variants deserve wet-lab investigation, and with which therapeutic lever.***

> Public, disease-level analysis. Data from public databases (NCBI ClinVar, AlphaFold DB, UniProt, GTEx). No patient is referenced. Specific variants (e.g. p.Gln230Pro, c.1057-2A>G) appear as **worked examples**; the pipeline is designed to be re-run across **all** reported WWOX variants (planned future work, resources permitting).

---

## Why this matters

The rare-disease bottleneck is not ideas — it is **which expensive wet-lab experiment to run first.** For a gene with hundreds of variants of uncertain significance, an in-silico triage that predicts *mechanism* (and therefore *lever*) focuses functional work where it will pay off:

- **folding/stability-defective variants** → candidates for **chaperone / proteostasis** rescue;
- **splice / nonsense / null variants** → candidates for **ASO** (splice-switching) or **gene addition**.

## The variant landscape (public, NCBI ClinVar)

- **Gene:** WWOX, 16q23.1 (common fragile site FRA16D; tumor suppressor). Reference: NM_016373.4 / NP_057457.1 (414 aa).
- **Diseases:** WOREE (WWOX-related epileptic encephalopathy; ClinVar DEE1/DEE28) and SCAR12 (autosomal-recessive spinocerebellar ataxia 12). Null / severely hypomorphic alleles → encephalopathic phenotype (WOREE); milder biallelic combinations → ataxic phenotype (SCAR12).
- **Records analyzed:** 1,327 WWOX variants (ClinVar E-utilities, `WWOX[gene]`).

| Classification | N |
|---|---|
| Uncertain significance (VUS) | 529 |
| Likely benign | 424 |
| **Pathogenic** | **141** |
| Benign | 87 |
| **Likely pathogenic** | **42** |
| Conflicting | 40 |
| Benign/Likely benign | 23 |
| **Pathogenic/Likely pathogenic** | **17** |

→ **200 clinically actionable (P/LP) variants**; the majority (529 VUS) remain uninterpretable — exactly where functional/biomarker work adds value.

**Molecular consequence of the 200 P/LP (loss-of-function signature):** CNV/structural 132 · nonsense/stop-gain 27 · splice-region 23 · missense 13 · frameshift/indel 5. Dominant signature = complete or partial protein loss (consistent with the FRA16D fragile site, prone to large deletions). No single hotspot; point variants distributed across both WW domains and the enzymatic SDR domain.

**Disease association (200 P/LP):** both DEE/WOREE and SCAR12 82 · DEE/WOREE spectrum 49 · other/cancer 38 · unspecified 28 · SCAR12 3.

## Pipeline components

| Stage | Tools (all public) | Output |
|---|---|---|
| Variant ingest | NCBI ClinVar E-utilities | full variant table (HGVS c./p., GRCh38, SPDI, classification, traits) |
| Structural impact | AlphaFold DB (AF-Q9NZC7-F1), biotite (SSE, SASA) | burial, secondary structure, H-bond context per residue |
| Stability (ΔΔG) | ThermoMPNN (structure-based, deep learning), ESM-2 650M (evolutionary LLR) | saturation ΔΔG map (414 × 20), per-site substitution scores |
| Splice impact | Ensembl VEP + SpliceAI + MaxEntScan | acceptor/donor loss/gain, cryptic-site prediction |
| Tissue proxy | GTEx | accessible-tissue readout validity (biomarker feasibility) |
| Lever assignment | mechanism → modality mapping | chaperone-amenable vs ASO-amenable vs gene-addition |

## The pathograph layer — the causal graph, assembled rather than authored

[`pathograph_inventory.md`](pathograph_inventory.md) is a generated view of the graph the
registries **already** declare: claims as nodes, claim→claim wikilinks as edges, and every
relational proposition already written in a claim title, in the working model's claim mirror
or in a deep-dive work manifest, extracted as a *candidate* awaiting review. The machine-
readable form is [`data/pathograph_export.jsonl`](data/pathograph_export.jsonl).

It adds nothing. An edge appears only where a registry declares one, and an edge carries a
relation type only where a claim record annotates the link with one — so the current count of
typed edges is reported at whatever it happens to be, and deriving a type from the endpoints'
declared fields is refused in code and in a regression. Typing an edge is a reading against
evidence, which is Scientist work; this layer prepares the packet and reads the verdict back.

```bash
python3 framework/scripts/pathograph.py --disease wwox
```

## The DisMech export pipeline

A second, independent line of work lives in this folder: turning LEGEND's canonical claims into
entries for **[DisMech](https://dismech.monarchinitiative.org/)**, the Monarch Initiative's
Disorder Mechanisms knowledge base. DisMech holds ~1000 disorders and **no WWOX entry**.

This is a *contribution* pipeline, not an analysis one, and it is deliberately hard to satisfy.
Its job is to **refuse**, not to produce plausible YAML: an entry may only carry a proposition
that a specific sentence in a specific read paper supports.

| Phase | What it does | Status |
|---|---|---|
| 1 — Specification | the export contract: what may leave, in what form, under which rules | `IMPLEMENTED` — [`dismech_export_spec.md`](dismech_export_spec.md) |
| 2 — Sidecar + verification | claims → assertion candidates → occurrences → evidence assertions, with two loss ledgers | `IMPLEMENTED` — [`dismech_sidecar_phase2.md`](dismech_sidecar_phase2.md) |
| 3 — Exporter dry run | emits DisMech YAML **to `staging/` only**; opens no pull request | `IMPLEMENTED` |
| 4 — Validation | offline against the pinned schema blob; upstream `just qc` still outstanding | `PARTIAL` — offline passes, `just qc` needs the DisMech clone and network |
| 5 — Upstream PR | submission | `NOT STARTED` — nothing has been sent |

**Nothing has been submitted to DisMech.** Phase 3 writes to `staging/`, which is gitignored.

### Why a reading without verbatim locators cannot be exported

Every exported node carries the **sentence** behind it, quoted verbatim, with its section anchor
and the receipt of the reading that produced it. A conclusion reached carefully but without its
quote cannot enter — the pipeline has no way to attach evidence to it.

This is why the deep-dive contract requires `verbatim_locators` at reading time rather than
afterwards: see [`deep_dive_manual.md`](../../../framework/manuals/deep_dive_manual.md) §4.5.

### Independent-derivation check

The sidecar was re-derived blind by a second actor from an isolated input bundle and the two runs
compared: an off-by-one in sentence indexing was found and fixed, under-splitting was found by
blind human review and repaired, and the equivalence axis was measured at roughly two-thirds
inter-rater agreement. The negative result is recorded too:
[`dismech_axis4_result.md`](dismech_axis4_result.md) closes exact-text deduplication as
structurally unable to compare cross-run partitions.

### Runnable

```bash
python3 disease-models/wwox/analysis/scripts/derive_dismech_sidecar.py --report
python3 disease-models/wwox/analysis/scripts/export_dismech_dryrun.py --out-dir staging/dismech_dryrun
python3 disease-models/wwox/analysis/scripts/dismech_independent_protocol.py verify-baseline
```

The exporter re-derives the sidecar and **refuses to run if the committed one is stale**, so a
landed reading cannot be exported from superseded state.

## Files in this folder

- `README.md` — this overview
- **DisMech export** — `dismech_export_spec.md` (the contract) · `dismech_sidecar_phase2.md` ·
  `dismech_phase3_dryrun_result.md` · `dismech_blind_derivation_contract.md` ·
  `dismech_independent_derivation_design.md` · `dismech_independent_comparison_rev12.md` and
  `_rev13.md` · `dismech_axis3_*` (blind review sheets, prompts and both rounds of results) ·
  `dismech_axis4_result.md` · `dismech_spectrum_reading_result.md`
- **Reading-contract record** — `locator_contract_live_test.md`: four papers taken end to end
  through the verbatim-locator contract, with the defects each reading exposed
- `scripts/` — the derivation, exporter, validator, blind-protocol and baseline-reseal tools,
  each with its own test suite
- `variant_structural_pipeline.md` — worked example: a buried-core SDR missense (p.Gln230Pro), structural + ΔΔG analysis
- `variant_triage_rescuability.md` — the mechanism → lever triage (chaperone vs ASO), with two worked examples
- `proteostasis_rationale.md` — the written rationale behind the chaperone lever and the proteostasis figures, **published together with the 2026-07-14 repair that narrowed it**
- `therapy_levers.md` — literature-anchored therapeutic levers for WWOX/WOREE (public PMIDs)
- *(data/figure artifacts — ClinVar tables, ΔΔG maps, AlphaFold model — added after per-file clean-check)*

> Every result is anchored to public data or a real PMID. In-silico predictions are hypotheses that prioritize experiments; they are not experimental validation, and nothing here is medical advice.
