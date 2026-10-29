# Usable compounds for two candidate methods — census, pilot subset, bidirectional query (IT7 P2, roadmap R2)

Scientist-b, task `ORCH-ROADMAP-IT7-20261029`, package P2, 2026-10-29. **A census of input requirements, not a result.** No compound
was scored, ranked or evaluated; nothing here is evidence about WWOX, an efficacy statement or medical advice. "Usable" means
"has the input a method needs", never "would work".

**Actually evaluated = 0** (records, families and compounds alike). The catalogue's own figure (`compounds_evaluated_against_WWOX_needs: 0`) is unchanged.

Files: `counts.json` (the funnel, machine-readable), `pilot_subset.tsv` (one row per family, 595 rows), `pilot_net_actions.tsv` (one row per
signed action, 1 425), `pilot_lincs_contexts.tsv` (one row per compound x cell x concentration x time, 3 531), `need_links.tsv` (per need),
`record_usability.tsv.gz` (the flag of every catalogue record, so a verifier can recompute any count), `usable_census.py` (builds all of them),
`usable_query.py` (the bidirectional query).

## 1. The two methods, defined by their input needs

| Method | Needs (per compound) | Does NOT need | Known limit carried from earlier iterations |
|---|---|---|---|
| **M-sig** transcriptional-signature reversal | a compound perturbagen with an L1000/LINCS signature (`trt_cp`) in a stated **cell context** (cell id, concentration, time); plus, outside this census, a disease signature | a documented target or action | the S1 reversal query was **inconclusive and then negative**: one signature family fills both tails, 43 percent of top reversers are frequent hitters, a within-knockout split reaches the same top score, the local level 5 analysis was negative for that contrast (`gse156243/lincs_iteration2_interpretation_20261027.md`, `gse156243/lincs_it3_local_level5_20261027.md`). A knockout signature is not a rescue signature. **Not repeated here as evidence.** |
| **M-net** light signed-network | a compound with a **documented action carrying a sign** (target activity down or up) on a **human target with a stable identifier** | any expression data | a documented link is a source statement, not potency and not relevance to WWOX; direction toward a need is resolved only where `coverage/target_roles.tsv` has a role row |

What the three LINCS surfaces expose (from the adapter and tool-survey records of iterations 1 to 3; **not re-queried live in this package**):
the iLINCS adapter (`framework/adapters/ilincs.py`, `SignatureMeta`) returns one row per signature with `compound`, `cellline`, `tissue`,
`concentration`, `time`, `libraryid` and no concordance value; SigCom LINCS `enrich/ranktwosided` returns a ranking with a total but only top-N, with
`metadata-api` signature metadata (cell line, dose, time, compound name); L1000FWD returns signature ids carrying BRD code, cell, time and dose, capped at 50
per direction, without compound names. All three are one lineage with the GEO deposits. For a **census** the GEO metadata tables are the complete
and checksummed form of the same fact, so the census was made from them: `GSE92742` (phase I) and `GSE70138` (phase II, downloaded 2026-10-29 into
scratch; `pert_info`, `sig_info`, `cell_info`, each SHA-512 verified against the series `SHA512SUMS`; the hashes are in `counts.json`, key `lincs`).
Phase II was not previously on disk in this checkout; including it adds 107 404 compound signatures to the 205 034 of phase I.

## 2. Units and definitions (prose; the denominator is always named)

* **Record** — one catalogue entry: a source-level substance record (a salt, a stereoisomer, a formulation or a source-only row each count once). 44 211 records.
  *Not* distinct drugs.
* **Family** (the "compound" of this census) — records joined by ChEMBL parent/child link or identical InChIKey first block, plus the 485 source-only records
  joined by the GtoPdb ligand reconciliation; every other source-only record is its own family because identity is unresolved and **never merged on name**.
  40 268 families (16 475 ChEMBL families + 23 793 source-only records without identifier link). Because source-only records are not merged, the same drug can
  sit in two families (example: ethosuximide is a ChEMBL family and a separate DGIdb-only family), so 40 268 is an **upper bound** of distinct compounds.
  A family counts at a step if **any** of its records qualifies; a family can therefore be usable by both methods through two different records
  (this is why "both" is 578 for families and 376 for records).
* **L1 any target row** — the record has at least one ChEMBL curated-mechanism row or DGIdb interaction row.
* **L2 documented pharmacological action** — at least one row with a *stated* action (ChEMBL `action_type` present; DGIdb `interaction_type` present and not
  `other/unknown` and not a source conflict) that passes the catalogue's own artefact rules (`repurposing_search.artefact_reason`: unconfirmed identity, source
  artefacts, alias risk) and is not a placeholder name. Unit: records or families; denominator: all records or all families.
* **L3 = M-net usable** — an L2 row whose action maps to a **sign** on the target's activity (down: inhibitor, antagonist, blocker, negative modulators, inverse
  agonist, degrader, antisense/RNAi inhibitor; up: agonist, activator, positive modulators, opener, potentiator) **on a human target with a stable identifier**
  (ChEMBL: Homo sapiens, target id and UniProt; DGIdb: HGNC concept id). Modulator, binding agent, antibody, vaccine and unstated are documented but **not signed**.
  The sign is the source's effect on the target, not an effect on the disease.
* **M-sig usable (any context)** — the record's InChIKey first block (the catalogue's own family key) equals that of a LINCS compound perturbagen with at least one
  `trt_cp` signature in either series. **M-sig usable (neural, strict)** — at least one such signature in a cell id from `NPC`, `NPC.CAS9`, `NPC.TAK`, `NEU`, `NEU.KCL`,
  `MNEU.E` (iPSC-derived neural progenitors and neurons; in `cell_info`: primary site central nervous system, or modification text "differentiated … neurons").
  `FIBRNPC` (no modification text, primary site skin) is kept apart as lineage UNKNOWN; every FIBRNPC compound also has a strict signature, so strict = extended in counts.
  `SHSY5Y` has **0** compound signatures. `ASC` is adipose stem cells, **not astrocytes**: no glial compound context exists. All LINCS neural cells are
  wild-type for WWOX (UNKNOWN genotype is not assumed otherwise).
* **Overlap** — both / only one / neither, over **all** records (or families); "neither" therefore includes the 22 557 DGIdb-only and other source-only records that have no structure key.
* **Need-link counts** (section 6) — records linked to a need's intervention targets by identifier. This is a *target association*. It is **not** a directional
  prediction, not an observed effect, and a share of pathways or targets linked is **not** a share of the disease treated.

## 3. Funnel (counts.json, key `funnel`; recomputed by `usable_census.py run`)

| Step | Records (of 44 211) | Families (of 40 268) |
|---|---:|---:|
| L0 source records / families catalogued | 44 211 | 40 268 |
| L1 with any target row | 24 423 | 23 425 |
| L2a stated action on any row, before artefact rules | 16 424 | 15 508 |
| **L2 documented pharmacological action** (rule-passing) | **16 362** | **15 447** |
| **M-net usable** (signed action, human target, stable id) | **14 125** | **13 379** |
| **M-sig usable, any context** (trt_cp signature, either phase) | **2 478** | **2 310** |
| **M-sig usable, neural strict** | **1 008** | **931** |
| **Actually evaluated** | **0** | **0** |

Overlap, M-net vs **M-sig neural**: both 376 records / **578 families**; only M-net 13 749 / 12 801; only M-sig 632 / 353; neither 29 454 / 26 536.
Overlap, M-net vs **M-sig any context**: both 880 / 1 280; only M-net 13 245 / 12 099; only M-sig 1 598 / 1 030; neither 28 488 / 25 859.

Reading: of 40 268 families, 33 percent are M-net usable and 2.3 percent are M-sig usable in a neural context (5.7 percent in any context); 1.4 percent are usable by both.
These are shares of the **catalogue**, whose composition is set by what the sources list (it is not the bioactive universe: ChEMBL declares 2 921 148 distinct compounds, 19 933 enumerated here).

### 3.1 M-net by source (records; the three groups are redundant, not independent votes)

Groups: **ChEMBL** = curated mechanism `action_type`; **GtoPdb** = DGIdb rows whose claim source is GuideToPharmacology (target verified or corrected through GtoPdb ids; this is the form in which the
catalogue carries the GtoPdb action); **DGIdb-other** = DGIdb interaction type from every other claim source (ChEMBL claims v33, DTC, CancerCommons, MyCancerGenome, TALC, ...; identity as served, unchecked).

| Region (usable signed rows from exactly these groups) | Records | Families |
|---|---:|---:|
| ChEMBL only | 3 758 | 3 017 |
| GtoPdb only | 6 267 | 6 227 |
| DGIdb-other only | 2 277 | 2 256 |
| ChEMBL + GtoPdb | 1 | 37 |
| ChEMBL + DGIdb-other | 535 | 551 |
| GtoPdb + DGIdb-other | 1 274 | 1 140 |
| all three | 13 | 151 |
| **any (M-net usable)** | **14 125** | **13 379** |

Any row of the group: ChEMBL 4 307 records / 3 756 families; GtoPdb 7 555 / 7 555; DGIdb-other 4 099 / 4 098. (The family counts of single regions can exceed record counts of
the same region only because a family pools its members' groups.) Only 4 330 of the usable records are ChEMBL-origin records; 9 795 are DGIdb-only source records,
whose modality is `unknown` (10 124 usable records have modality unknown) — an antibody or a peptide cannot be told apart from a small molecule there.
Modality of usable records: small molecule 3 167, antibody 397, protein/peptide 287, oligonucleotide 69, ADC 46, oligosaccharide 16, gene product 15, enzyme 4, unknown 10 124.

Row level (all 106 315 catalogue target rows): 41 945 carry a stated action; 39 129 are signed before the identity and artefact rules; 10 747 rows are excluded by those rules.

### 3.2 M-sig: what the LINCS side contains (counts.json, key `lincs`)

* `trt_cp` signatures: 205 034 (phase I) + 107 404 (phase II) = **312 438**; **21 299** distinct compound perturbagens with a signature, 21 236 with an InChIKey (63 cannot be matched), 9 893 distinct connectivity layers, 2 312 of them also present in the catalogue.
* Neural strict signatures (compound, `trt_cp`): NPC 5 538 (3 625 compounds), NEU 4 440 (2 659), NPC.TAK 1 207 (212), NPC.CAS9 1 032 (169), MNEU.E 355 (63); FIBRNPC 1 312 (626, lineage UNKNOWN). **3 685** perturbagens have a strict neural signature, of which 931 families are in the catalogue.
* Context richness of those 931 families: median 2 neural signatures per family (max 99); 485 have signatures in 2 or more neural cell ids; only **100** have two or more concentrations at one neural cell and time (a dose-response); most neural signatures are a **single concentration (10 uM) at 24 h or 6 h**. The census does not say whether a signature is of good quality (`sig_metrics` not applied) or whether the concentration is pharmacologically relevant to the target.
* Match rule: connectivity layer (the catalogue's own family key). By full InChIKey only 2 068 records match (stereo/salt differences), 2 478 by layer. 28 969 records have no structure key (source-only) and **cannot** be matched: UNKNOWN, not negative. Name matching is not used.

## 4. Pilot subset

Definition: families usable by **both** methods (M-net, and M-sig in a neural context) **union** the families linked to a curated card (`catalog/card_links.json`).
Size: **578** (both) + **17** card-linked not in both = **595 families**. The 19 card-linked families: 14 M-net usable, 3 M-sig neural usable, 2 both. No card-linked compound is
evaluated. Characterisation of the 578: 575 small molecules, 2 protein/peptide, 1 oligosaccharide; status class approved-any-source 408, clinical candidate 134, tool probe 29, phase unknown 5,
marketed unapproved US 2; access evidence (overlapping): prescription 296, OTC 39, supplement 2, experimental 190, unknown/unverified 345.

Per-family fields in `pilot_subset.tsv` (rectangular; headers are self-describing): ids and members, card ids, modality, status class, access categories, M-net rows and an action summary
(`target|action|sign|source`), selectivity summary, LINCS neural cell ids, **concentrations and times**, signature counts, ChEMBL route flags, brain-penetration field, source safety flags,
`safety_assessment = NOT_ASSESSED`, `actually_evaluated = 0`. Detail per signed action (`pilot_net_actions.tsv`): action, sign, target stable id, scope (single protein, among siblings, complex), selectivity, assay
context, concentration, source affinity value (source value, not interpreted), references. Detail per LINCS context (`pilot_lincs_contexts.tsv`): perturbagen id, cell id, tier, concentration, time, number of signatures, series.

### 4.1 What is known and what is UNKNOWN in the pilot (595 families, 1 425 signed rows)

| Field wanted | Where it could come from | Known | UNKNOWN |
|---|---|---|---|
| Action and sign | ChEMBL / GtoPdb / DGIdb | 1 425 rows over 590 families (the 578 plus 12 card-linked families); 14 of the 19 card-linked families | 5 card-linked families have no signed action on a stable target (labelled `none`) |
| Assay context of the action | GtoPdb `Assay Description` only | 16 rows (11 families) | 1 409 rows: ChEMBL curated mechanisms carry no assay; DGIdb-other claims carry none |
| Concentration of the action | GtoPdb `concentration Range` | **0** rows | all 1 425 rows |
| Affinity (source value) | GtoPdb original affinity | 156 rows (66 families); reported as the source gives it | the rest |
| Selectivity | GtoPdb `Selectivity`; ChEMBL `selectivity_comment` | 89 rows with a statement (56 families); another 135 GtoPdb rows say "Not Determined" (kept as is, not counted as known) | the rest. Selectivity is never inferred from a target count or a family (GluN2B-type subunit questions stay open) |
| Concentration and time of the **signature** | LINCS | all 578 M-sig neural families: 478 have one concentration (466 of them 10 uM), 100 have two or more; times: 24 h 449, 6 h 14, both 115 | cell genotype and a disease contrast are not in LINCS |
| Exposure / brain penetration | catalogue and cached ChEMBL fields | **none**: neither the catalogue nor the cached ChEMBL fields carry CSF, brain or BBB data | **UNKNOWN for all 595.** ChEMBL route flags (oral, parenteral, topical) are carried for the 595 and are a route of administration, **not** an exposure. No prediction (including ADMET-AI) was run: a prediction is not an observation and would be an inference |
| Safety evidence | source flags | 163 families have a ChEMBL record with `black_box_warning = 1`, 31 a withdrawn flag (source statements, scope = ChEMBL) | everything else; `safety_assessment = NOT_ASSESSED` for all |

## 5. Access categories: source, country, date (counts.json, keys `access_category_sources`, `eu_registers`)

"Supplement", "OTC" and "prescription" are **categories of recorded access evidence**, not approval, availability, appropriateness or safety. Overlapping counts (records): prescription 2 101, OTC 906, supplement 238, experimental 13 021, unknown/unverified 28 234.

| Category | Source | Country / jurisdiction | Date | Strength | Records |
|---|---|---|---|---|---:|
| prescription | openFDA NDC finished human prescription products, matched by UNII | US | export 2026-10-27, retrieved 2026-10-27 | identifier match | 2 101 |
| OTC | openFDA NDC finished human OTC non-homeopathic products, matched by UNII (may be a combination product) | US | export 2026-10-27 | identifier match | 906 |
| supplement | NIH ODS DSLD label database v9 (API v9.4.0): a label ingredient name, or a DSLD ingredient-group name or synonym, equals the record's name | US labels only | retrieved 2026-10-28; 971 of 4 697 planned bulk names probed plus 75 targeted: **unprobed names are UNKNOWN, not negative** | **name only** (DSLD has no chemical identifier) | 238 |
| EU nutrition/health-claims register and Novel Food status catalogue | EU Open Data Portal datasets (DG SANTE) | European Union level, **not Italy or any national list** | dataset last modified 2024-08-13, downloaded 2026-10-28 | name match on probe strings only (`catalog/eu_context_probe.tsv`, 67 probes); **no catalogue record carries an EU access category** | 0 |
| Italian register of notified supplements | Ministry of Health site | Italy | attempted 2026-10-28 | answered with an anti-bot challenge page, not worked around; **not obtained** | 0 |
| experimental | ChEMBL ChEMBL_37 2026-05-01: clinical candidate or probe statement and no approval statement | none (says nothing about obtainability) | 2026-05-01 release | source statement | 13 021 |
| unknown/unverified | no source used states how it is obtained, or an approval is stated but no NDC product matched | none | | none | 28 234 |

**Diets are complex interventions**, never a single molecule: the ketogenic diet and a ketogenic-lactate axis diet are recorded in `catalog/non_molecule_modalities.tsv` as `dietary_intervention`
(composition and course, not a compound) and have no record in any funnel step; vectors, CRISPR systems and oligonucleotide programmes are likewise outside the compound count.
A supplement hit is a product label listing an ingredient name in the US; it says nothing about dose, form, quality or use in a WWOX-deficient system.

## 6. Bidirectional exploration (`usable_query.py`)

```
python3 disease-models/wwox/research/drug_repurposing/usable_compounds_it7_p2_20261029/usable_query.py --help      # answers without work
... usable_query.py needs                                  # the 22 needs
... usable_query.py need NEED-T-TYPE-CALCIUM [--limit N] [--json]   # need -> catalogue compounds on its intervention targets, with link sign and M-net / M-sig flags
... usable_query.py genes GRIN2B,GRIN1 [--limit N]         # ad-hoc pathway (HGNC symbols) -> compounds, always labelled EXPLORATION
... usable_query.py compound ethosuximide [--json]         # compound -> needs touched, and the inputs each method still lacks
```

Standard library only, offline, deterministic (the JSON output is byte-identical between runs), reads the catalogue, `needs.json`, `target_roles.tsv`, `record_usability.tsv.gz`; link rules are
those of `framework/scripts/repurposing_search.py` (identifier links only; artefact rows excluded; uncertain direction gives an exploration list). Example: ethosuximide has
two catalogue records, a ChEMBL one (M-net usable; LINCS signatures exist but none in a neural context) and a DGIdb-only one (M-net usable; no structure key, so UNKNOWN for M-sig); the query returns both and chooses none.

`need_links.tsv` (records linked to each need's intervention targets and how many each method can use). **Reading:** a count of compounds with a documented link to a target of the need; it is not a directional prediction
(10 of 22 needs carry a direction other than `uncertain`, and a role row is also required to call a link consistent or opposed), not an observed effect, and not coverage of the disease. Columns: `records_signed_on_this_need_target` = the link to this need's target states an up/down action; `records_Mnet_usable_anywhere` = the record has a signed documented action on some stable target (not necessarily this one: read the two together, as the first is never larger in meaning).
Selected rows (linked / signed on the need's target / M-net anywhere / M-sig neural / both): NEED-NEUROINFLAMMATION-GLIA 521 / 183 / 331 / 4 / 4 (exploration);
NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR 179 / 121 / 143 / 1 / 1; NEED-T-TYPE-CALCIUM 67 / 36 / 44 / 1 / 1; NEED-MYELINATION 214 / 145 / 168 / 3 / 3; NEED-MTOR-AUTOPHAGY 185 / 86 / 137 / 5 / 5 (exploration). Each of the five WWOX-restoration needs links
the same 3 records (two cancer-drug records and a recombinant protein record that DGIdb lists on WWOX with no stated action; 0 signed on WWOX, 0 M-sig): they are listings, not interventions on the gene. Four needs link **0** records (mitochondrial respiration, MYC progenitor, redox, systemic glycaemia): "no link in this catalogue" with the sources' states, never "no pathway biology".

## 7. Gaps and limits (stated, not repaired)

1. **M-sig neural coverage is small and thin**: 931 of 40 268 families; 100 with a dose-response; one concentration (10 uM) and mostly one time point for the rest; all cell contexts are wild-type iPSC-derived cells, no glia, no WWOX-deficient context, no signature quality filter applied. The known confound (one signature family dominating both tails, frequent hitters) applies to any M-sig use and is not re-measured here.
2. **Source-only records (22 557 DGIdb-only, 1 219 openFDA-only, 502 MATRIX-only) have no structure key** and cannot be matched to LINCS: their M-sig status is UNKNOWN, not negative. They can be M-net usable (9 795 are).
3. **Duplicate families**: the same compound can appear as a ChEMBL family and as a DGIdb-only family (8 751 source-only records share a normalised name with a ChEMBL record, flagged, not merged); family counts are upper bounds on distinct compounds.
4. **M-net usable is a documented sign on a stable target, not a measured one**: no potency is carried; concentration is UNKNOWN for all pilot rows; assay context is known for 16 rows; selectivity for 89. Complex-level ChEMBL mechanisms (301 pilot rows) are not subunit-specific.
5. **Exposure and BBB are UNKNOWN for all 595 pilot families** in the sources held; the next acquisition would be a documented brain/CSF exposure source or ChEMBL activity/ADME rows, labelled as measured, not predicted. The ChEMBL activity endpoint is not cached.
6. **DGIdb export is dated 2024-06-10** (its ChEMBL claims are ChEMBL 33) and its licence is not cleared for public release as a whole (catalogue README); the GtoPdb and ChEMBL fields are share-alike with attribution. Rows here are counts and identifiers, not a redistribution of those fields beyond the derived tables.
7. **GSE70138 was downloaded for this package** (public, checksummed; not committed). A verifier needs `GSE92742_Broad_LINCS_{pert,sig,cell}_info` and the GSE70138 equivalents named in the script docstring, plus `LEGEND_CATALOG_CACHE` for the pilot detail fields (counts do not depend on the cache).
8. **No method comparison or evaluation was made** (that is R3). The funnel stops at "usable"; the next measurable step is a declared compound subset (the 578 are the natural candidate pool, not a selection) and a pre-declared comparison.

## 8. Reproduce

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 usable_census.py run --geo92 <dir with GSE92742 metadata> --geo70 <dir with GSE70138 metadata>
```

Output is byte-identical on a second run (`counts.json`, `pilot_subset.tsv`, `record_usability.tsv.gz` checked). Source files for the GEO metadata: `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/` and `.../GSE70nnn/GSE70138/suppl/`
(GEO terms; citation of the LINCS L1000 resource, Subramanian et al. 2017, Cell). No registration, contact address, spend or access control was involved.
