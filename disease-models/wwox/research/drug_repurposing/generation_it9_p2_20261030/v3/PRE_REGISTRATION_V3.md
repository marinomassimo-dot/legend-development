# PRE-REGISTRATION V3 (Amendment 5 to generation_it9_p2_20261030/PRE_REGISTRATION.md): provenance repair of the generation path

Scientist-b, 2026-10-30, branch task/it9-p2b from main 140b3b79. Written BEFORE any v3 run. The v2 folder and results are untouched; v3 writes only under `generation_it9_p2_20261030/v3/`.
Exploratory. Computational. Not medical advice; a compatible action of a context-free signed network is not a benefit.

## 0. Why

P4b qualified 13 proposals of the v2 candidate tables (P3-01 to P3-13). Ten fail at the provenance of the PROPOSAL CHAIN, not at the compound: (a) a record of the wrong mode is applied to a seed of another level
(OGA->PFKP, an O-GlcNAc-on-enzyme record, applied to a PFKP transcript; CASP1->IL1B, protein cleavage, applied to an IL1B transcript; MTNR1A->GNAO1, a coupling record; ESR2->GAD2, a transcriptional edge applied to a GAD2 protein seed);
(b) symbol is not identity (PDPK1 vs the alias PDK1; implitapide's complex target MTTP+P4HB inherited by the non-catalytic partner P4HB); (c) active moiety (balsalazide's PPARG belongs to mesalamine). What I have seen before this file: the P4b READMEs and edge provenance tables,
the P3 selection table with chains (`exploration_it9_p3_20261030/selected.tsv`), the edge-type counts of the committed network tables (SIGNOR export: 55,638 post_translational + 122 transcriptional; CollecTRI: 51,621 transcriptional), and the catalogue `prodrug` field.
Not seen: any v3 score.

## 1. The three filters, stated as rules

**F1 record mode against seed level (edge typing).** Every network edge gets a mode from the OmniPath `type` of its record: `T` transcriptional (a TF acts on the target's transcript), `P` post-translational (protein-activity, modification, cleavage, stability), `C` coupling
(an edge whose target is a heterotrimeric G-protein subunit gene, GNA*, GNB*, GNG*, in a P record: receptor-G protein coupling), `U` any other or missing type (none exist in the committed tables; counted, excluded). Chains of at most K = 3 edges are admitted only by the seed's level:
* **expression seed** (transcript level): the chain is `P* T`: any number of `P` edges (activity cascade, at most 2) ending in exactly one `T` edge into the seed; no `C` edge anywhere (a coupling record measures G-protein engagement, not a transcript change); no `T` edge before the last (that would turn an mRNA into a regulator without a protein step, the expression=protein equivalence the rules forbid). A direct hop-0 hit (compound target = seed gene) stays a separate arm as in v2 and is not part of NET-IND.
* **protein or phospho seed**: the chain is `P+` (all edges `P`, final edge `P` onto the seed protein); no `T`, no `C`. For a phospho seed the site is not checked (P1 records the site; the network records do not): flagged `SITE_UNCHECKED`; direction was already forced uncertain in v2.
* **function, pathology, state seeds**: not gene seeds (unchanged).
Implementation: the backward propagation is done in stages (final edge type, then `P` edges), exact and linear, so T1/T5-type exactness is kept.

**F2 identity.** (i) Compound targets are resolved to an HGNC id, not a text symbol: ChEMBL rows by UniProt (HGNC complete set, downloaded 2026-10-30, `uniprot_ids`), DGIdb/GtoPdb rows by `gene_concept_id`; network, seed and catalogue symbols are all mapped to the approved symbol of that id (alias/previous symbols only when unambiguous). Rows without a resolvable id are dropped and counted.
(ii) Alias collision: a row from a source with no independent id check (identity state `as_served`) naming gene X is dropped (`ALIAS_COLLISION`) when the same compound has a curated, id-verified target Y whose alias or previous symbols include X's approved symbol (PDK1 vs PDPK1).
(iii) Complex targets (ChEMBL target type PROTEIN COMPLEX or PROTEIN COMPLEX GROUP with more than one member): a member is credited only when its approved symbol or approved name occurs in the ChEMBL target name or mechanism text; members not named are NOT credited and listed (`COMPLEX_MEMBER_NOT_CREDITED`). Paralog families (target type PROTEIN FAMILY, SELECTIVITY GROUP) keep crediting all members, as in v2 (the source states one action on the family).

**F3 active moiety.** A family with any record flagged `prodrug = 1` in the catalogue (ChEMBL) has its target credits marked `UNCERTAIN_ACTIVE_MOIETY`: the active-moiety record is not in the catalogue (metabolite links are not cached), so no credit via a metabolite is possible; such a family is excluded from the robust (z-ranked) candidate arms and listed in a separate `flagged` arm with the flag. (`prodrug = -1`, unknown, is not flagged.)

## 2. Expected effects (written before the run)

* Should FALL out of the seed-specific (z > 3 in both nulls) candidate arms: ceperognastat/OGA->PFKP (F1, P into an expression seed); belnacasan/CASP1->IL1B (F1; also F3); ramelteon/MTNR1A->GNAO1->HES1->BNIP3 (F1, C edge); balsalazide (F3); fosfestrol (F1: ESR2->GAD2 is a T edge into a protein seed; also F3); implitapide (F1 for the protein seed, F2(iii) for P4HB); the Q6 expression-arm proposals harmine, pomalidomide, lenalidomide (artefact control), defosbarasertib, AT9283 and pinometostat (DYRK1A, CUL4A, AURKB, DOT1L->MYC are P edges into an expression seed). The same Q6 compounds are EXPECTED TO SURVIVE in the Q6 protein arm, where a P edge onto the MYC protein is the right mode.
* AR-12: its PDK1 (hgnc 8809) claim from an as_served clinical-trial source falls by F2(ii) from the direct-search arm; the curated PDPK1 target remains.
* Should NOT be lost (not provenance failures): belzutifan (EPAS1->LDHA, T into an expression seed), curcumin (EP300->TNF, T; its failure is the compound class, not the chain), JTE-151 (RORC->IL6, T), the direct hop-0 references dichloroacetate (PDK1, hgnc 8809, correct identity), memantine and felbamate (GRIN2C), and every proposal whose terminal edge is T from a non-prodrug, id-verified, non-coupling chain.
* Overall: the transcriptional edges (51,621 CollecTRI + 122 SIGNOR) remain, so I expect the expression-seed NET arms to shrink but not vanish; I expect the largest loss in the number of non-zero and seed-specific families for protein-level seeds (Q4 protein: ESR2/GAD2-type T edges vanish; few P chains reach GAD1/GAD2/PVALB/NPY proteins) and for Q7, a smaller loss for Q2 and Q5 expression (CollecTRI-rich hubs: HIF1A, EPAS1, NFKB, RORC), and a net loss of roughly a quarter to a half of the v2 seed-specific families in the expression sets. If the filters leave almost nothing, that is a result and the README will say what prevents candidates and what additional data type would be needed.

## 3. Success criteria for the repair (fixed now)

S1 (artefacts out): each of AR-12 (PDK1 direct credit), implitapide, ceperognastat, balsalazide, ramelteon, belnacasan and fosfestrol is absent from the v3 robust candidate arms (opposes and mimics, z > 3 in both nulls) of the seed set it came from, and the reason code is recorded per family.
S2 (non-failures kept): belzutifan, curcumin and JTE-151 remain in the Q2 / Q5 robust arms they came from with z > 3 in both nulls, and dichloroacetate, memantine and felbamate remain in the direct-search arm. If any of these is lost I report it as a failure of the repair (a false removal), not as a success.
S3 (new filters work, mutation tests): (a) a P-mode edge into an expression seed contributes exactly 0 in v3 and contributes in v2 mode (filter switch off); (b) a T-mode edge into a protein seed contributes exactly 0; (c) a coupling edge in a chain contributes 0; (d) a complex member not named in the target name is not credited; (e) an alias-collision row is dropped; (f) a prodrug family is flagged and absent from the robust arm. Each as a unit test that fails if the filter is ignored.
S4 (engine tests): T1, T5 pass as before; T2/T4 reported as registered; guards (T6) unchanged.
S5 (honest comparison): a v2-vs-v3 table per seed set: examined, non-zero, seed-specific counts, the number of v2 seed-specific families that survive in v3, and per filter the number of edges and families removed.

## 4. What is not changed

Seed tables (P1 v2, sha256 76952333...) and the adapter; the guard handling; the null (degree-matched, both variants); the criteria T1-T6; the Z definitions. The v2 NET-IND remains available as `--mode v2` of the v3 engine for the comparison and for the filter-off half of the mutation tests.
