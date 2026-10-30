# IT10 P2.3: Q1 complement - residual function and protein fate when the graph has no way in (scientist-a, 2026-10-30)

Non-canonical research material. Exploratory, not medical advice; no efficacy, safety, wet-lab or clinical claim. Reference genotype class only (a WWOX-DEE genotype class; the Q230P-class missense allele is named, no individual record). No e-mail address or personal datum was sent to any service; key-less endpoints only; no spend, no registration. Retrievals are dated 2026-10-30 (system date; the package folder carries the mandate date 20261031). Nothing here edits a card, need, ranking, registry, the four current files or the receipt ledger.

## 1. Decision (first)

| Question | Answer |
|---|---|
| Can a non-graph logic address part of Q1 with usable material? | **Yes, for one narrow slice, and the slice is a mechanism experiment, not a treatment.** The slice is path (c): the one WWOX-specific degradation factor that a compound can modify, the tyrosine kinase ACK1 (TNK2). It is conditional on WWOX protein being present, so it does **not** apply to the Q230P system as the only datum stands (no band, S001). |
| What else exists? | Lysosomal-pH route arms for the one measured WWOX missense (P252A): a **re-find**, already in the Q230P lever panel and in the P8 design. ITCH raises WWOX half-life but has no compound. Fly and mouse modifier data go the wrong way (WWOX as modifier of other genes) or are existing leads (lithium/GSK3B card G01, HIF card K01). |
| What did I not find? | Any study that gives any compound to a Q230P, splice-allele, P47T, WWOX-null or neural WWOX system with a WWOX protein or function read-out. Any ACK1 inhibitor given to a WWOX system (0 PubMed records). Any suppressor of WWOX deficiency. Any ITCH activator compound. |
| Decisive missing datum | Is the Q230P protein made and cleared, or not made? (S001 is a non-detection with a sensitivity limit; the authors offer translation or turnover as speculation.) Without it, no stability lever can be called on-target for Q230P. |
| Counts | New compound names as units: **1** (bosutinib). New hypotheses on known compounds: **1** (dasatinib via ACK1). Re-finds: chloroquine, ammonium chloride, bafilomycin A1 (lysosomal arms); ITCH lever. New lead needing a datum: albendazole as a reported WWOX binder. |
| Kept / conditional / dropped | **Kept (conditional):** T1 dasatinib, T2 bosutinib as paired ACK1 probes. **Re-find, not new:** T3 lysosomal-pH arms. **Dropped:** hydroxychloroquine (no WWOX datum, evidence not transferable from chloroquine), lorlatinib/entrectinib/ceritinib (TNK2 off-target rows only), Hsp90 inhibitors (indirect, folds into A05), AIM-100 and (R)-9b (identity unresolved, tools), toosendanin and evodiamine (WWOX-replete induction claims; already classed not transferable). |

## 2. Verdict by path (`paths_verdicts.tsv`)

| Path | Verdict | Why in one line |
|---|---|---|
| (a) direct compound recovery of a variant or phenotype | **Re-find; Q230P NEEDS-DATUM** | The only variant-plus-compound datum is P252A over-expressed in a cancer line (lysosome-pH agents restore it; MG-132 and 3-MA do not). Albendazole binding claim: NEEDS-DATUM. |
| (b) genetic modifiers / suppressors | **NO-MATERIAL** (right direction) | Fly Wwox modifies Idh/Sod and respiratory-complex phenotypes; no screen suppresses a Wwox-deficiency phenotype. Mouse leads re-found (G01, K01). |
| (c1) ACK1 degradation factor | **USABLE-NOW (conditional, hypothesis grade)** | Two independent cancer systems (prostate, liver), potent catalogued inhibitors, a clean discriminating test. |
| (c2) ITCH stabilising E3 | **NEEDS-DATUM (no compound)** | Half-life up with ITCH, down in Itch-null cells; no activator exists in ChEMBL; ITCH has many substrates. |
| (c3) RNF138 - hnRNPA0 - WWOX mRNA | **NO-MATERIAL for Q1** | Transcript is normal in the Q230P datum; abstract only. |
| (c4) phospho-forms, SUMO, localisation | **NO-MATERIAL for rescue** | Function-state descriptions; the Zfra agent is a peptide. |
| (d) residual-product rescue (A01-A05, B01-B02, C02, C03, PTC, missense folders) | **Reused, unchanged** | Not re-searched. One restatement: no support for the proteasome class in the only WWOX variant system. |
| (e) bypass | **Out of scope for Q1** | Downstream cards already exist. |

## 3. Path (c1), the USABLE-NOW slice

**The WWOX observation (what it is and is not).** Activated ACK1 over-expressed in LNCaP cells phosphorylates WWOX at Tyr287, then WWOX is polyubiquitinated and degraded; in primary prostate tumours phospho-ACK1 is high and WWOX low (L10, abstract only). ACK1 knockdown raises WWOX in liver-cancer lines and ACK1 correlates inversely with WWOX in 150 paired tissues (L11, abstract only, an independent system). Three open texts that I read restate the mechanism (L06-L08); they are restatements and are **not** counted as confirmations. The E3 ligase on this route is unidentified (L08). Level is the only thing measured: nothing says that more WWOX through this route is more function.

| id | compound -> action | context | hypothesised benefit (level) | discriminating test |
|---|---|---|---|---|
| T1 | dasatinib (parent CHEMBL1421; TNK2 data on hydrate CHEMBL5416410) -> ATP-site inhibition of ACK1 (Kd 5.6 and 6.0 nM, IC50 1.0 nM in ChEMBL) and of SRC/ABL | cells with a WWOX band: ACK1-active cancer lines first, then neural or organoid lines with residual WWOX protein | longer WWOX half-life, higher steady-state protein, if the Tyr287-ACK1 route limits WWOX there | cycloheximide chase and steady state with compound, TNK2 knockdown as genetic comparator, Tyr287Phe WWOX as the insensitive control, route arms (MG-132, chloroquine) in the same cell; function read-out separate from amount |
| T2 | bosutinib (CHEMBL288441) -> ACK1 inhibition (IC50 2.7 nM, Kd 29 nM) and SRC/ABL | same | same | same; the independent-chemotype arm: **concordance rule** - dasatinib, bosutinib and TNK2 knockdown must agree, a response to one only is off-target |

Full rows (observation by system, allele, level, direction; precedent; counter-evidence; unknowns) are in `candidates_it10_p23.tsv`; potency rows in `tnk2_chembl_activities_selected.tsv`; identity in `compound_identity.tsv`.

**Counter-evidence that binds (read at abstract level, which is stated):** a TNK2 missense that removes NEDD4-dependent degradation (more stable ACK1) sits in a family with severe infantile-onset epilepsy (L16; single family, authors call proof pending); ACK1 inhibition sensitised rat cerebellar granule neurons to apoptotic stress (L17); no Tyr287 change in serum-starved MEFs (L07); MG-132 raised neither wild type nor either P252A/P282A construct, so a proteasomal route is not shown in the only variant system (L02); broad kinase inhibitors shift WWOX phospho-forms in cancer cells (L23). **UNVERIFIED speculation, not a claim:** the TNK2 family variant raises ACK1 abundance, which in this model would lower WWOX; if true the epilepsy link would support the axis rather than weaken it. TNK2 carrier cells with a WWOX measurement would test it (R2).

**Why this is a probe, not a candidate for use.** Both molecules are multi-target antineoplastic kinase inhibitors; CNS exposure and tolerability in this setting were not assessed; ACK1 selective tools are unresolved (AIM-100, (R)-9b: identity not assigned). The point of T1/T2 is to learn whether WWOX protein is ACK1-limited in any WWOX-relevant cell.

**Allele fit.** Needs protein: not applicable to a Q230P cell with no band; applicable, in principle, to residual-protein states (the SCAR12 organoid class, S004, whose "very low" signal is itself unread). Missense variants with normal protein (WW1 variants such as P47T) are outside this lever by design. ITCH binds WW1, so a WW1 variant may also lose ITCH-dependent stability: an inference (UNVERIFIED), not a datum.

## 4. Re-find (kept short; do not redo)

T3 lysosomal-pH agents (chloroquine, ammonium chloride; bafilomycin A1 not used in the source). Source datum L01-L05: P252A restored by chloroquine and ammonium chloride, not by 3-MA; HSC70 and chaperone-mediated autophagy are the authors' speculation. These arms are already in the Q230P lever panel and in the P8 design; nothing new is proposed. One refinement for the A02 reading: the proteasome class has no support in this system (L02).

## 5. Novelty relative to cards, ranking and generation (`novelty_check.tsv`)

| Entry | Classification |
|---|---|
| dasatinib via ACK1 -> WWOX stability | new hypothesis on a known compound (name present in 2 priority rows for other needs and in pilot tables; no card, no unit, no v3 candidate) |
| bosutinib via ACK1 | new compound name for any card, ranking unit, priority row or candidate list (present only as a pilot family row) |
| chloroquine, ammonium chloride, bafilomycin A1 | re-find (needs O2, seeds S009, lever panel, P8 arm g, IT6 P6) |
| ACK1 as intervention axis | new as an axis; the mechanism has been held since the activity census (bulk degradation biochemistry) but never carried to a unit |
| ITCH lever | re-find (manifest entries 9-10, DL-MECH-083, DIS-001), no compound |
| albendazole SPR binding | new lead, NEEDS-DATUM (registry "screened" only) |
| counts | new names 1; new hypotheses on known compounds 1 |

## 6. Reading depth (what I read, what I relayed)

* Read by me at full text (Europe PMC XML, own copies outside the repository): 41124647 (P252A), 41677633, 37194323 (ACK review), 35883580 (phospho-form review, screened by sentence), 21075834 (fly Idh/Sod, genetic-interaction sentences only); local text of 29808465 (Q230P).
* **Relayed, not re-read:** 24550385 (ITCH). Every open route is closed (publisher withholds the text; Europe PMC and publisher PDF return 403). Locators L13-L15 come from the repository manifest (complete_fulltext_read receipt FTR-20260810-24550385-02) and are marked as such.
* **Abstract only:** 16288044 and 25738261 (ACK1-WWOX), 23686771, 37263460 (TNK2 neurology), 36257459, 34015398 (HCC compounds), 42275215 (RNF138), 26390919, 26302329, 16007179, 32000863. An abstract is not a read; every claim from them is flagged.
* Supplement Figure S4 of 41124647 (chloroquine under cycloheximide) was not opened.
* No docking or structure prediction was used.

## 7. UNVERIFIED

1. Whether the Tyr287-ACK1 route is proteasomal and whether it operates in neural cells (primary is abstract only; the E3 is unidentified).
2. ACK1 protein in neurons (Human Protein Atlas RNA only; GTEx lookup returned no rows).
3. Salt form of the chloroquine used in 41124647 (vendor code only); the printed units of the ammonium chloride legend look implausible and are not relied on.
4. Whether any approved ACK1 inhibitor reaches the CNS (not assessed).
5. Tyr287 position relative to the Q230P and P252A lesions as a degron in destabilised variants (speculation).
6. The three database lookups proposed in R6 (FlyBase, BioGRID ORCS, DepMap) were not run.
7. ITCH locators are relayed (section 6).
8. Albendazole identity step and binding claim (abstract only).

## 8. Disclosures

No step was blind. Searches were run by me and screened by title for the large result sets (counts in `search_log.tsv`). Guards in the IT9 `guards.tsv` were read; none applies to a Q1 action. No generator was re-run. No receipt was written.

## 9. For the batch path

1. Record this folder as IT10 P2.3 research material with the method note: "Q1 has no graph route; a complementary logic (regulators of WWOX protein stability) yields one usable mechanism-experiment slice (ACK1) and one re-find (lysosomal-pH arms)".
2. Proposed, not made: add `T1`/`T2` as a mechanism-probe unit ("ACK1 axis of WWOX protein stability, conditional on protein present") to the ranking only after the reading of 16288044 is available, with `what_would_reopen` = R2 or R3.
3. Proposed need annotation (no edit made): under NEED-WWOX-MISSENSE-PROTEIN-RESCUE add the ACK1 and ITCH observations as O3 and O4 with the locators above, and the TNK2 counter-evidence in its limits.
4. Optional generator follow-up: `proposed_ptm_edges.tsv` lists curated signed protein-level edges (TNK2 -| WWOX, ITCH -> WWOX). A Q1 protein rerun with them would be built on one edge per factor, so it can only restate T1/T2; do it only as a test that the engine reaches the seed, not as a ranking.
5. Add the reopenable searches R1-R7 (`reopen_searches.tsv`) to the triggers table; R1 is the one that gates everything.

## 10. Files

`README.md` · `paths_verdicts.tsv` · `candidates_it10_p23.tsv` · `evidence_locators.tsv` · `compound_identity.tsv` · `tnk2_chembl_activities_selected.tsv` · `novelty_check.tsv` · `search_log.tsv` · `reopen_searches.tsv` · `proposed_ptm_edges.tsv`
