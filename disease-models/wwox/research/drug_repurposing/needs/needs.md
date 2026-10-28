# Biological needs of WWOX-DEE, for the repurposing module

Non-canonical research material (iteration 3, `scientist-b`, 2026-10-27/28). It does not change the four scientific
current files, ranks nothing and is not medical advice. No paper was newly read: each observation is carried from a
curated card, a verbatim-locator manifest entry, a registry record or a repository analysis, and points at it.

A **need** is a place where the record observed something about WWOX loss and an intervention could be aimed at it. It is
a search seed for the catalogue ("which compounds act on these targets?"), not a hypothesis and not a claim that the
intervention helps. Hypotheses stay in
[`therapeutic_hypotheses_ledger_current.md`](../../therapeutic_hypotheses_ledger_current.md); a need only cites their ids.

Files: [`needs.json`](needs.json) (the table) · this note · [`check_needs.py`](check_needs.py) (offline checker) ·
[`test_check_needs.py`](test_check_needs.py) (its regression; the release runner finds it by file name).

## Fields

Per need: `id`, `label`, `family`, `track` and `goal` (two separate objects, each with its basis), `basis`
(`observed` or `exploratory_question`), `observed[]`, `inferred[]`, `intervention_direction`, `counter_evidence[]`, `sources`,
`targets[]`, `pathways[]`, `evidence_scope[]`, `coverage`, `notes`.

- `observed[]`: statement, model type, species, genotype, tissue/cells, age/stage, comparison, readout, readout level
  (transcript, protein, phospho, activity, flux, functional, clinical, computational), direction observed, evidence scope,
  the limits the source states, PMID and locators. Locators are manifest entries (with an anchor text found in that entry),
  repository documents, or registry ids.
- `inferred[]`: what the record does not measure.
- `intervention_direction`: direction (`up`, `down`, `restore`, `modulate`, `uncertain`), target, rationale, certainty,
  `do_not_assume`. A direction is never derived only by reversing an observed change. Where the sign is unresolved the value
  is `uncertain` and the rationale says why (12 of 22 needs).
- `targets[]`: HGNC symbol and id, role, `target_kind` (`intervention_target`, `pathway_member`, `readout_marker`,
  `disease_gene_product`, `effector_constraint`, `identity_guard`) and a collision note where the symbol is confusable. A
  differentially expressed gene is a `readout_marker`, not a target.
- `evidence_scope` (per observation; the need-level list is the union of its observations): the bridge's labels (`WWOX_EXPERIMENT_IN_DEE_SYSTEM`, `WWOX_BIOLOGY_OTHER_CONTEXT`,
  `OTHER_DISEASE_PRECEDENT`, `COMPUTATIONAL_RESULT`) plus `UNVERIFIED_HYPOTHESIS`; the model type (mouse null, neuron-specific
  deletion, organoid, patient cells, case report, fly) is on each observation. Computational results are repository analyses of
  deposited data, not experiments. Scope labels follow the bridge's definition; non-neural systems (fibroblasts, mouse embryonic fibroblasts, blood) are labelled `WWOX_EXPERIMENT_IN_DEE_SYSTEM` where they are patient-derived or engineered knockout cells, and the observation says they are non-neural.
- `coverage`: `NOT_ASSESSED` everywhere; the module sets it.

**Track** A = variant-independent, B = variant- or lesion-specific. **Goal** = `deep_recovery` (restore the lost function) or
`partial_benefit`. They are independent and each need justifies both: gene addition is A + deep recovery; splice correction,
read-through, missense rescue and an expression boost are B + deep recovery (the boost works only on an allele that yields
residual functional protein); downstream levers are A + partial benefit.

## The table (22 needs, 63 observations; computed from `needs.json`)

| Need | Label | Track | Goal | Direction | Basis | Scope(s) present | Intervention targets (first five) |
|---|---|---|---|---|---|---|---|
| `WWOX-GENE-ADDITION` | Restore WWOX protein in neurons by gene addition (AAV-type vector) | A | deep | restore | observed | WWOX in DEE-relevant system | - |
| `WWOX-SPLICE-CORRECTION` | Restore correct WWOX transcript from a canonical splice-acceptor allele (splice-switching, editing) | B | deep | restore | observed | WWOX in DEE-relevant system; computational | - |
| `WWOX-PTC-READTHROUGH` | Read-through of a premature stop codon in a WWOX nonsense allele | B | deep | restore | exploratory question | unverified | - |
| `WWOX-MISSENSE-PROTEIN-RESCUE` | Rescue a destabilised SDR-domain missense WWOX protein (folding, quality control, degradation) | B | deep | up | observed | WWOX in DEE-relevant system; WWOX other context | - |
| `WWOX-ENDOGENOUS-BOOST` | Raise endogenous WWOX expression (CRISPRa, anti-miR, small-molecule activators) | B | deep | up | observed | WWOX in DEE-relevant system; WWOX other context | - |
| `ISR-ATTENUATION` | Integrated stress response (eIF2alpha-ATF4) activity: attenuate a possible over-activation | A | partial | uncertain | observed | WWOX other context; other-disease precedent; computational | EIF2AK3, EIF2B1, EIF2B2, EIF2B3, EIF2B4 ... |
| `PDH-PYRUVATE-AXIS` | Pyruvate entry into the TCA cycle (HIF1A-PDK-PDH axis; glycolytic shift) | A | partial | uncertain | observed | WWOX in DEE-relevant system; computational | PDK1, PDK2, PDK3, PDK4 |
| `LACTATE-LDH` | Lactate and lactate dehydrogenase activity: lower an elevated LDH/lactate state | A | partial | uncertain | observed | WWOX in DEE-relevant system; WWOX other context; computational | LDHA, LDHB, SLC16A1, SLC16A7 |
| `MITOCHONDRIAL-RESPIRATION` | Mitochondrial respiration / OXPHOS capacity (including complex I) as a possible WWOX-dependent deficit | A | partial | uncertain | observed | WWOX in DEE-relevant system; WWOX other context; computational | - |
| `EXCITATORY-GAIN-GLUTAMATE-RECEPTOR` | Excitatory network gain and bursting: glutamate-receptor node (NMDAR, AMPAR); gap-junction/pannexin untested | A | partial | down | observed | WWOX in DEE-relevant system; other-disease precedent | GRIN1, GRIN2A, GRIN2B, GRIA1, GRIA2 ... |
| `INHIBITORY-HYPOFUNCTION` | Inhibitory drive: reduced spontaneous inhibition and PV/GABAergic marker deficit | A | partial | uncertain | observed | WWOX in DEE-relevant system; computational | ABAT |
| `GABA-CHLORIDE-GRADIENT` | Chloride gradient and GABA polarity (NKCC1/KCC2): premise unmeasured | A | partial | uncertain | exploratory question | computational; unverified | SLC12A2 |
| `SEIZURE-CONTROL-SYMPTOMATIC` | Seizure and spasm control as a symptom-level need (distinct from developmental protection) | A | partial | down | observed | WWOX in DEE-relevant system | ABAT, CACNA1G |
| `T-TYPE-CALCIUM` | T-type calcium channel dependence of provoked seizure in Wwox loss | A | partial | down | observed | WWOX in DEE-relevant system | CACNA1G, CACNA1H, CACNA1I |
| `MYELINATION` | Hypomyelination: restore myelin / white-matter development | A | partial | restore | observed | WWOX in DEE-relevant system; computational | CHRM1 |
| `GSK3B-DEREPRESSION` | GSK3beta de-repression (loss of WWOX docking inhibition) | A | partial | uncertain | observed | WWOX in DEE-relevant system; WWOX other context | GSK3B |
| `WNT-BETA-CATENIN` | Wnt/beta-catenin readout elevated in WWOX-deficient organoids (direction observed; confounded by maturity) | A | partial | uncertain | observed | WWOX in DEE-relevant system; WWOX other context; computational | TNKS, TNKS2 |
| `MYC-PROGENITOR-PROLIFERATION` | MYC elevation and progenitor-state shift in WWOX-deficient radial glia (prenatal developmental substrate) | A | partial | uncertain | observed | WWOX in DEE-relevant system | - |
| `MTOR-AUTOPHAGY` | mTOR signalling and autophagy: direction unmeasured at protein level | A | partial | uncertain | observed | WWOX in DEE-relevant system | MTOR |
| `NEUROINFLAMMATION-GLIA` | Neuroinflammation and gliosis (microglia/astrocytes, IL-1beta/TNF/NF-kB signalling) | A | partial | uncertain | observed | WWOX in DEE-relevant system | IL1B, NLRP3, TNF, NFKB1, RELA ... |
| `REDOX-OXIDATIVE-STRESS` | Redox balance / reactive oxygen species: sign is context-dependent | A | partial | uncertain | observed | WWOX other context | - |
| `SYSTEMIC-GLYCAEMIA-GROWTH` | Systemic metabolic decompensation: hypoglycaemia and failure to thrive (endpoint and confounder) | A | partial | restore | observed | WWOX in DEE-relevant system | - |

## Limits, stated

- Exploratory questions with no WWOX measurement: `WWOX-PTC-READTHROUGH`, `GABA-CHLORIDE-GRADIENT`. For read-through, nonsense alleles are recorded in the repository's census but no read-through or NMD measurement exists in the sources read. They are kept so the gap is a recorded gap.
- Computational observations (organoid transcript analyses made in this repository) are transcript, not flux, on six libraries
  (four knockout, two wild type) and confounded with maturity; they carry `COMPUTATIONAL_RESULT`.
- Human clinical entries are uncontrolled case reports or series, and some rest on a card or a registry record, not on a manifest
  entry (marked by locator kind).
- A manifest anchor shows the text the pointer lands on, not that the entry supports every word of the statement; a reader
  should open the entry. Statements were audited by the author on 2026-10-28 and then by an independent verifier on eight needs (`locator_audits/2026-10-28_it3_needs_independent_verification.md`); the corrections of both are applied, and the other fourteen needs have had the author's second pass only.
- Gene Ontology ids were looked up against the EBI QuickGO term service on 2026-10-28 (one was obsolete and was replaced); a
  pathway id is a search hint, not a claim that WWOX acts in the process.
- HGNC ids and collision notes were taken from `hgnc_complete_set_20261022.json`, which sits in the untracked shared files tree and
  is not in git; they cannot be re-derived from a clean clone (its sha256 is in the JSON).
- `coverage` is not computed here. `not_included` in the JSON lists what was considered and left out, with reasons.

## Symbol collisions

`PDK1` (pyruvate dehydrogenase kinase 1) is also an alias of `PDPK1`; `TCF4` is now a different gene from the Wnt factor the papers
call TCF4 (`TCF7L2`); `MBP` is also maltose-binding protein and an alias of two other genes; `NDUFA4` is no longer an approved symbol
(now `COXFA4`, complex IV), though the organoid "oxidative arm" panel lists it; `GRIN1` is an alias of `GPRIN1`; `PVALB` of `MB`.
Search by HGNC id, not by string.

## Using it

Pick a need, take the `hgnc_id`s of its `intervention_target` entries, and run the target-to-compound query
(`framework/scripts/repurposing_join.py targets --dir <census folder> SYMBOL...`). Keep the need's `track`, `goal`, `basis`,
`evidence_scope`, `do_not_assume` and `counter_evidence` attached to every compound that returns. A compound whose action opposes
a need's direction (for example a complex I inhibitor against a support-oxidation need) is flagged, not scored.

## Adding a study

1. Prefer a study with a manifest of verbatim locators; otherwise use a document or registry locator and say so.
2. Write the observation with the six-part context, readout level, direction observed, evidence scope and the limits the source states.
3. If it fits an existing need's target or pathway, append it and re-read that need's `inferred`, `intervention_direction` and
   `counter_evidence`; otherwise open a new need with the full field set.
4. Keep track and goal as two fields; cite hypothesis ids and never copy their status.
5. Edit `needs.json` like any file and run `python3 disease-models/wwox/research/drug_repurposing/needs/check_needs.py`.

The checker verifies ids, required fields, track/goal values, the scope vocabulary and that pointers resolve (manifest entry in range
with its anchor text present, documents, registry ids, hypotheses, cards). It does not judge content.
