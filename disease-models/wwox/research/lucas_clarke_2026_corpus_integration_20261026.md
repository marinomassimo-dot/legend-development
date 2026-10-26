# Lucas-Clarke 2026 (Brain Communications, fcag385): what LEGEND already holds, what it bears on, and what it leaves open

> **Research layer, integration note. Not medical advice. No dose, administration, suitability or ranking statement is made anywhere in this note.**
> Author: ACTOR_ID `scientist-b`, 2026-10-26, task `SCIB-LUCASCLARKE-INTEGRATION-20261026`, from `main` at `1a5ece5e`.
> **What was read.** The preprint's dossier and its paper-registry record in full; the named LEGEND records by targeted query (`registry_records.py`, line-range reads, `git grep -F`). **The published paper (PMID 42909904) was NOT read by this actor**: its content below is taken from the dispatch statement and from the preprint (DOI 10.1101/2025.05.01.651195) as LEGEND holds it. Scientist A reads the published full text in parallel; any difference between preprint and published version is unverified here and belongs to that reading.
> **What was not touched.** No ledger, registry, receipt or current-file edit; nothing staged in the receipt ledger.

## Summary (the five answers and the next step)

1. **Held already:** the preprint is `PAPER 158` (research layer, `partial_fulltext_read`, `FTR-20261003-PPR1015434-01`, Claim links: none); it moves CLAIM 025 only as a footnote, and through the Obeid review (`PAPER 029`) rather than in its own right.
2. **Bears on:** CLAIM 025/009, DL-MECH-020/034/023/013, DL-BIO-008, DL-THER-115, HYP-20260709-01/-05, N-06, N-08: supports lactate-up in a second organism, contradicts the HIF1A route, leaves PDK/PDH and the ketogenic bypass untouched.
3. **Direction:** lactate-up agrees with the mouse serum datum and the human fibroblast datum, disagrees with the single human brain MRS datum and with the human normal screen only in a weak sense; seven competing readings, each with one separating measurement (section 3).
4. **Handles:** LDHA/LDHB, ATF4/EIF2AK3, PDK1/PDHA1, MAT2A/MTHFD1/CBS queried on 2026-10-26; adapters return target and tractability facts only, NOT WWOX EVIDENCE, no score, no ranking; ISRIB is NO_MATCH_FOUND in ChEMBL by that name on that date (section 4).
5. **Scope:** a fly amyloid model with RNAi and CRISPRa at about 2-fold mRNA; it transfers a mechanism hypothesis and a design (two-direction dose), not a human result (section 5).
6. **Most informative next step:** measure lactate, Atf4 and a HIF1A reporter side by side in WWOX-null human neural cells (or organoids) with and without a proteostasis stressor, which separates readings R1, R3 and R7 at once.

---

## 1 · What LEGEND already holds about the preprint

**Identity and depth.** `PAPER 158` in `paper_registry_current.md` (line 8808): DOI 10.1101/2025.05.01.651195, bioRxiv PPR1015434, no PMID; status `processed`; registry role "research layer — a preprint founds no claim"; `Evidence depth: partial_fulltext_read`, receipt `FTR-20261003-PPR1015434-01` (coverage: abstract, introduction, methods, results, discussion, references read; figures and supplementary captions only; tables not present); dossier `research/fulltext_dossiers/PPR1015434.md`; Transferability T3; clinical relevance LOW-MODERATE "class of lever, not clinical evidence". **`Claim links: none`.** Integrity status clean. No manifest (a preprint without peer review). The literature-tracking record is at `literature_tracking_log_current.md` line 13049. Data deposits named: ArrayExpress E-MTAB-14948 and E-MTAB-14949, MetaboLights MTBLS12344.

**What LEGEND concluded from the preprint** (dossier section 3 and the registry Note): knockdown shortens life and is synergistic with Abeta42 (Cox interaction p < 0.0001), raising soluble Abeta42; the route is PERK to Atf4 to Ldh to lactate, and Ldh knockdown rescues the climbing deficit; **the HIF1-alpha homologue reporter sima:GFP does not move (p = 0.5185) and Xbp1 splicing does not move**, "a direct negative on the WWOX/HIF1A axis in this system"; upregulation (CRISPRa, measured at about 2-fold as **mRNA only**, no WWOX protein measured anywhere) reduces amyloid and rescues life and locomotion **without lowering lactate**, lowering L-methionine instead, so the rescue does not run the mechanism backwards. Negatives recorded: no myelin or white-matter endpoint (the fly CNS has no myelin), no heterozygous or null allele (RNAi only), nothing in a mammal, rescue prophylactic or concurrent only, and the preprint itself notes that Ldh knockdown is detrimental in fly Abeta42 models, so "lower lactate" is not a safe target. The dossier verdict: INGEST, research layer only; "the most therapeutically shaped result in the group, in the least transferable organism".

**Exact wording of CLAIM 025** (`claim_registry_current.md`, line 501; Status `in observation`, Type DATO + INFERENZA, Pathway P5):
- Title: *"The WWOX/HIF1A ratio may function as a systems-level marker of maladaptive biological state, linking glycolysis, inflammatory tone and Wnt-related signaling."*
- The preprint appears only in this appended paragraph (line 516): *"**Nuance (Obeid 2026 review / Lucas-Clarke 2025):** a Drosophila model shows a WWOX metabolic effect that is HIF1α-INDEPENDENT (via ATF4/UPR; neuroprotection via methionine suppression, not lactate). Not a direct contradiction (different system) but it tempers the HIF1A-centric framing of this claim. Status unchanged (in observation); primary queued FT-009."*
- A parallel passage sits in `meta_metabolism_current.md` line 162 ("Nuance — HIF1α-independent axis ... [in observation]": "a tension to reconcile"; "CLAIM 025 annotated accordingly").
- 🔴 **Provenance gap worth stating.** That nuance was written on 2026-04 from the **Obeid review** (`PAPER 029`, PMID 42128308), before the preprint was read. The first-person reading of the preprint (2026-10-03) confirmed the sima and Xbp1 negatives but **no commit has re-sourced the CLAIM 025 nuance to the preprint's own text**, and the nuance's phrase "ATF4/UPR" is looser than the preprint (PERK-Atf4 with Xbp1 splicing unchanged, so the IRE1 arm is not engaged in that readout). The phrase "neuroprotection via methionine suppression" is the review's compression of the CRISPRa arm; the preprint's own statement is that the up-arm's only interaction metabolite is L-methionine, down.

**Which claims cited the preprint in support.** None in the sense of support: it is cited in **one** claim, CLAIM 025, as a nuance (a tension), and in `PAPER 029`'s claim-links line ("025 nuanced (HIF1α-independent tension, Lucas-Clarke 2025)"). The preprint's own `PAPER 158` record has `Claim links: none`. A second use is non-claim: the Obeid-review manifest (`deepdive_manifests/PMID42128308.json`) carries two propositions about it, one tagged ESPANSIONE ("a metabolic axis with a signed direction and a dissociated rescue ... lactate would be a biomarker that reports the genotype and not the treatment") and one noting that the review's myelin cell-autonomy claim rests on a different, unrefereed preprint. The preprint is also listed in the interventions batch selection (`interventions_batch_selection_20261019.md` line 256).

## 2 · What LEGEND holds that this paper bears on

Verdicts are for the **fly result as LEGEND holds it from the preprint**, not for the published paper. "Supports" means direction or route agrees in a different system; none of these is WWOX-DEE evidence.

| Identifier | One line | Verdict |
|---|---|---|
| CLAIM 025 | WWOX/HIF1A ratio as a state marker; nuance already attached | **Contradicts the HIF1A route in the fly** (sima flat); leaves the ratio-as-state-marker proposition untouched |
| CLAIM 009 (`claim_registry_current.md` line 177) | WWOX as bioenergetic governor, INFERENZA in observation | **Supports** lactate-up in a second organism; ATP unchanged in the fly head, so "bioenergetic failure" is not supported there |
| DL-MECH-020 | Warburg-like WWOX loss via HIF1A; rationale for ketogenic diet; superseded in part by DL-MECH-095 and weakened by the 2026-09-21 reading (PDK-to-PDH block rests on PDK transcript only; PDH activity unchanged) | **Contradicts the route, supports the lactate output**; the PDH-block arm is untouched (no Pdk or PDH measurement in the fly) |
| DL-MECH-034 | Steinberg 2021 organoids: OXPHOS down, glycolysis enriched (transcriptome, n = 2 versus 4) | **Supports** direction of a glycolytic shift in neural tissue; fly ATP unchanged argues against reading a shared OXPHOS deficit |
| DL-BIO-008 | Lactate high in mouse serum; "extremely low" in the one human brain MRS (confounded by an HSPG2 variant); human metabolic screen normal | **Supports the mouse half, disagrees with the human MRS half**; see section 3 |
| DL-BIO-007 / DL-BIO-005 | Serum lactate (mouse) and HIF1A/GLUT1/PKM2 panel as biomarker candidates; already downgraded | Lactate-up supports the observation; **"lactate reports the genotype, not the rescue"** (CRISPRa arm) reinforces the existing downgrade |
| DL-BIOM-014 | Glycolytic gene set that reports WWOX loss is context-dependent (PKM2 versus PDK1/LDHA1/ENO1) | **Supports** context-dependence; the fly adds an Ldh transcript rise under Atf4, not under HIF1 |
| DL-MECH-120 | Sign of the metabolic target must be fixed by a brain measurement before a dietary rationale is chosen | **Strengthens the need**; adds a third signed datum (fly Ldh reduction rescues) |
| DL-MECH-123 | A diet alone raises neonatal brain lactate about 2.7-fold, so a lactate difference is not by itself a HIF1A shift | **Bears on any comparison**; the fly design controls diet, a mammalian replication must |
| DL-MECH-155 | Glucose uptake sign is condition-specific in WWOX-depleted fibroblasts | **Untouched** (no uptake assay in the fly arm as held) |
| DL-MECH-157 / `PAPER 363` | Fly design in which reduced WWOX worsens a mitochondrial-deficiency phenotype; primary unread | **Adjacent**: a second fly genetic-enhancer design; the preprint is another gene-by-stress interaction |
| DL-MECH-023 | WWOX biases ER-stress outcome; Janczar 2017 states PERK activation does not change with WWOX status (ovarian line, drug stress) | **Tension**: fly Atf4 rises under WWOX knockdown plus Abeta42 (PERK-Atf4 named); different cell type and stressor |
| CLAIM 044 / `PAPER 140` | Direction of WWOX activity in stressed neurons unresolved; one rat record makes activated WWOX pro-death | **Supports the pro-survival direction** of WWOX in an Abeta42-stressed neuron (restoration rescues); does not resolve the rat record |
| DL-THER-115 | In three systems, WWOX restoration raises stress-induced apoptotic sensitivity; in the fly under Egr/TNF, WWOX reduction protects | 🔴 **Opposite direction in the same genus**: under Abeta42, reduction harms and a 2-fold increase protects. The stressor, not the species, may set the sign; a statement of dose and context for any WWOX-raising strategy |
| CLAIM 043 / `PAPERS 136, 139, 146` | WWOX-TRAPPC6AΔ/TIAF1-tau-Abeta cascade, one laboratory, no neuron with a WWOX genotype | **A link from a laboratory other than the one behind the cascade**: WWOX level modifies Abeta42 load (soluble led) in a fly neuron; does not test the TRAPPC6AΔ/TIAF1 steps |
| DL-MECH-013 / `PAPER 135` | Sleep: human intronic GWAS (suggestive) plus fly hypomorph, reduced and fragmented daytime sleep, increased night sleep | **Partly different**: the preprint's RNAi knockdown increases sleep and sleep pressure without circadian disruption (dossier); RNAi versus hypomorph, different readout sets; not reconciled here |
| HYP-20260709-01 | Ketogenic diet, rationale via HIF1A-PDK-PDH bypass; `IPOTESI` | **Untouched** (no ketone, PDH or diet arm); its premise lactate-high-via-HIF1A is weakened as a route, not as an output |
| HYP-20260709-05 | Dichloroacetate to reactivate PDH; `parked`, dominated by HYP-01 | **Untouched**; if lactate in the fly runs through Atf4-Ldh, a PDK-PDH rationale has no support from this paper |
| CLAIM 042 | One WOREE series, three of five reported improved on a ketogenic diet, count unstated | **Untouched** |
| N-06 (`mechanism_intervention_map.md` line 698) | Lactate as WWOX readout is a biomarker not measuring the mechanism | **Supports the conclusion** by a new route (lactate marks the lesion in the fly and not the rescue) |
| N-08 (line 740) | DCA: peripheral-nerve signal; never measured in a WWOX system; only WWOX anchor is DL-MECH-020 | **Untouched in substance**; its one WWOX anchor loses route support in the fly |
| DL-MECH-069 | WWOX may modulate NMD via UPF1 | Untouched |

**ISR/UPR/ATF4/PDK/LDH/methionine/sleep literature already in the registries** (theme queries, the two large registries not loaded): `PAPER 432` (Abbink 2019, EIF2B-related disease and integrated stress response as a target; labelled NOT WWOX EVIDENCE, the artefact contains no WWOX occurrence); `PAPER 262` (an LDHA-bearing record, not opened); `DL-MECH-023` and the CORPUS stub for the ovarian-ER-stress paper (Janczar 2017, `CORPUS-STUB-126`); `PAPER 557`/`562` (DCA, class-level). The theme queries returned **no record at all** for "2-hydroxyglutarate" and "cysteine", and **no ISRIB record outside the repurposing knowledge-graph lookups** (a `git grep` hit in `drug_repurposing/gse156243/kg_lookup/*` and a few manifests, none about the ISR). Methionine appears only in CLAIM 025's nuance. Absence from the registries is a statement about these queries, not about the literature.

## 3 · The directional question (not resolved)

**Datum by datum, fly lactate-up under Wwox knockdown plus Abeta42** (dossier: L-lactate +1.30 log2, p_adj 0.0174, the single interaction metabolite; Ldh transcript +1.33 log2):

| LEGEND datum | Direction in that datum | Agrees with the fly? |
|---|---|---|
| Mouse Wwox-KO serum (`PAPER 024`; DL-BIO-007) | lactate up | Agrees in direction; compartment differs (serum versus head), and the mouse route is HIF1A where the fly route is Atf4 |
| MEF Wwox-KO (DL-MECH-020) | lactate up, ATP down, OCR down | Agrees in lactate; **disagrees** on ATP (fly unchanged) and on route |
| Human fibroblast WWOX silencing (Baryla; `PAPER 023`) | lactate the only coherent readout across four conditions; PDH activity unchanged; glucose-uptake sign flips | Agrees in lactate; compatible with the fly's unchanged ATP |
| Human brain organoid transcriptome (DL-MECH-034) | glycolysis enriched, OXPHOS down (expression, not flux) | Agrees in direction at transcript level only |
| Human brain MRS, one case, HSPG2 confound (DL-BIO-008) | lactate "extremely low" | **Disagrees** |
| Human metabolic screen, one WOREE null case (`PAPER 043`) | serum lactate normal | Neutral to mildly disagrees: a peripheral normal does not test a brain interaction effect |

Two facts make the fly datum **not a direct test** of any human datum: (a) in the fly the lactate rise is the metabolite of the **interaction** with Abeta42, so the dossier does not establish a lactate rise under knockdown alone; (b) the human WWOX-DEE brain carries no Abeta42 and has a developing, not ageing, nervous system.

**Competing readings under which every datum could hold at once, each with the one measurement that would separate it:**

| Reading | Statement | The one separating measurement |
|---|---|---|
| R1 species or model | Mouse and fly raise lactate; human brain does not (or the single MRS case is off) | Brain lactate by the same method in a Wwox-null or hypomorphic mouse and in at least a second WWOX patient (a case-report MRS scan in the manner of DL-MECH-143), so the human number is no longer n = 1 |
| R2 compartment or cell type | Serum and fly head (neuron-dominated, glia present) differ from human tissue-average MRS; neuron lactate up, bulk low | A lactate sensor with cell-type resolution (neuron versus astrocyte) in the same WWOX-deficient neural system |
| R3 stress-conditional | Lactate rises only when a proteostatic stressor engages PERK-Atf4 (Abeta42 in the fly); the unstressed human brain has none | Lactate, p-eIF2alpha and Atf4 in WWOX-null human neural cells with and without a stated proteostasis stressor (and a knockdown-alone fly arm if the published paper lacks it) |
| R4 developmental versus ageing | Lactate effect is an ageing or chronic-stress phenomenon (fly 14 to 28 days of age on a lifespan scale; mouse null dies at about 4 weeks) | Age-resolved brain lactate in a conditional or hypomorphic Wwox model, developmental versus adult onset |
| R5 route multiplicity | Two routes to lactate, HIF1A (mouse, MEF) and Atf4-Ldh (fly), each context-dependent | HIF1 activity reporter and Atf4 readout side by side in the same WWOX-null neural cells |
| R6 lesion marker versus rescue marker | Lactate reports the lesion, and neither its rise nor its fall is the mechanism of harm or rescue (the CRISPRa arm lowers methionine, not lactate) | In a system where the lesion is repaired, lactate and the methionine axis before and after restoration, each with its own control; the fly already shows the dissociation, a mammal does not |
| R7 assay or dose | A 2-fold-mRNA CRISPRa dose versus RNAi knockdown versus null are different points on one dose curve | A titrated WWOX dose series in one system, with protein measured |

Nothing above promotes any reading; DL-MECH-120's statement that the human sign of WWOX-deficient metabolism is **unmeasured** still stands after this paper.

## 4 · Pharmacological handles the paper implies that LEGEND does not yet track

**Scope of the answer.** Only what the existing adapters answer, queried 2026-10-26 with `framework/scripts/repurposing_adapter.py query` (read-only, key-less). ChEMBL source `ChEMBL_37` (2026-05-01); Open Targets `api 26.9.0 / data 26.09`; PubTator3 counts are relation records over PubMed/PMC, not evidence about WWOX. **🔴 Every row is NOT WWOX EVIDENCE.** No score, no ranking, no order of preference is implied; the table is alphabetical within class. Gene symbols were mapped to Ensembl identifiers by hand for Open Targets, and the returned `symbol` field was checked to equal the symbol queried in every case.

| Handle (class) | Gene | ChEMBL gene query (targets returned) | Open Targets (associated diseases total; drug or clinical candidates; small-molecule tractability buckets true) | PubTator3 relation count |
|---|---|---|---|---|
| Ldh inhibition | LDHA | 6 targets, human CHEMBL4835 among them, plus a VHL/LDHA protein-protein-interaction target | 882; 1; Structure with Ligand, High-Quality Ligand, High-Quality Pocket, Druggable Family | 2099 |
| Ldh inhibition | LDHB | 6 targets, human CHEMBL4940 among them | 316; 0; same four buckets | 568 |
| ISR / Atf4 | ATF4 | 1 target, human CHEMBL6067624 | 1410; 0; no small-molecule bucket true | 2717 |
| ISR / PERK | EIF2AK3 | 2 targets, human CHEMBL6030 | 1112; 0; Structure with Ligand, High-Quality Ligand, Druggable Family | 3602 |
| Pyruvate dehydrogenase axis (already in HYP-20260709-05) | PDK1 | 6 targets, human CHEMBL4766 among them | 485; 1; Approved Drug, Structure with Ligand, High-Quality Ligand, Med-Quality Pocket, Druggable Family | 2148 |
| Pyruvate dehydrogenase axis | PDHA1 | 3 targets, human CHEMBL2092 | 342; 0; Structure with Ligand, Med-Quality Pocket | 462 |
| Methionine / cysteine | CBS | 20 name-match records, of which only CHEMBL3399911 is the target of interest | 2621; 0; Structure with Ligand, High-Quality Ligand, High-Quality Pocket | 1633 |
| Methionine / cysteine | MAT2A | 4 targets, human CHEMBL3313835 among them | 241; 0; same three | 417 |
| Methionine / folate cycle | MTHFD1 | 2 targets, human CHEMBL2541 | 248; 0; same three | 257 |

Drug-name queries to ChEMBL on the same date: `ISRIB` returned **NO_MATCH_FOUND**, which is an answer about this query on this date, never absence of the compound; `oxamate` returned one record, CHEMBL15976, typed `molecule_without_mechanism` (no curated mechanism of action). Other ISR modulators and other LDH inhibitors were not queried.

**Cautions on what the adapters returned.**
- The ChEMBL gene query is a **name search**: "PDK1" also returned the unrelated 3-phosphoinositide-dependent protein kinase 1 target (CHEMBL2534) and a PI3K-alpha/PDK1 interaction target; "CBS" returned 20 records, most unrelated by name collision. Read the target names, not the count.
- The adapters carry no information about WWOX, Abeta or the fly; the Open Targets disease lists (top associations returned: for LDHA a glycogen-storage disease and cancers; for ATF4 and EIF2AK3 "neurodegenerative disease"; for PDHA1 pyruvate dehydrogenase E1-alpha deficiency, Leigh syndrome and neurodevelopmental terms; for MTHFD1 neural-tube and immunodeficiency terms) are gene-level and not WWOX-level.
- The fly preprint notes that Ldh knockdown is itself detrimental in fly Abeta models (dossier section 5), so the existence of a target is not a statement about direction of benefit.
- ISR modulation has a precedent record in LEGEND only for a non-WWOX leukodystrophy (`PAPER 432`); methionine/cysteine and 2-hydroxyglutarate have none.

## 5 · The honest scope

This is a *Drosophila* Alzheimer model: RNAi (two constructs) and CRISPRa (about 2-fold *Wwox* mRNA; no WWOX protein measured in the preprint as held) in neurons on an Arctic-mutant human Abeta42 background, behaviours in adult flies, head transcriptome and metabolome, and no mammal. **What can transfer:** a hypothesis about a mechanism (WWOX level modifies proteotoxic-stress output through the PERK-Atf4 arm and lactate), a design (move the same gene up and down in one model and measure the dose), the demonstration that the marker that moves with the lesion (lactate) need not be the marker that moves with the rescue (methionine), and a reason to measure Atf4 beside HIF1A in WWOX-null neural cells. **What cannot transfer:** any claim about WWOX-DEE: the human disease is a developmental, biallelic loss-of-function encephalopathy with no amyloid, whereas the fly model is an ageing, amyloid-driven, RNAi-partial-loss system; fly glia and myelin differ from human; "AD risk gene" is a GWAS/eQTL attribution to an intergenic variant between *WWOX* and *MAF*, not a WWOX-DEE statement; the up-arm is prophylactic and transcript-only; no heterozygous or null allele is studied; and no prediction follows for lactate, Atf4 or methionine in a WWOX-DEE brain until measured there. Peer review upgrades the source's standing but not its organism; LEGEND status of every record named here is unchanged by this note.

## Provenance and limits of this note

Built from `PAPER 158`, `PPR1015434.md`, `FTR-20261003-PPR1015434-01` (summary fields), CLAIM 025/009/042/043/044, DL-MECH-013/020/023/034/069/120/123/155/157, DL-BIO-005/007/008, DL-BIOM-014, DL-THER-115, HYP-20260709-01/-05, N-06 and N-08, by targeted record and line-range reads; the adapter outputs were produced on 2026-10-26 and are held in this actor's scratchpad only (not committed). `DL-THER-115`, `PAPER 262`, `PAPER 432` and the CORPUS stub were read at header or first-paragraph level only. The sleep difference in section 2 is dossier-level (RNAi versus hypomorph), not a panel reading. No claim-level proposal is made; a re-sourcing of the CLAIM 025 nuance to the preprint's own text (and, if Scientist A's reading allows, to the published paper) is the integrator's decision.
