# CC-20261029-INTEGRATOR-IT7-REGISTRIES-01
- **Class:** ORDINARY, research-layer and registry-note batch. **No working-model statement is contradicted by the iteration-7 results, so no version bump: `target_wm_version` is `WM_v7.29` (preserved).** No claim created, reversed or promoted; no `Status`, `Type`, `Title` or `Summary` changed anywhere; no hypothesis status or ranking changed, no support added. No individual-level data. Not medical advice; nothing here is a clinical recommendation.
- **Author:** ACTOR_ID `integrator` (Integrator worker for the orchestrator), mandate IT7, step registries, task branch `task/it7-batch`.
- **Source material (each independently verified and repaired, already landed in the module, not re-enumerated here):** `drug_repurposing/census_reconciliation_it7_20261029.md` (P0a; section 5 is the verdict list KEEP, NARROW, CORRECT for every global statement of absence), `drug_repurposing/network_comparison_it7_p3_20261029/README.md` (P3), `drug_repurposing/context_differences_it7_p4_20261029/README.md` (P4), with the verifier reports `locator_audits/2026-10-29_it7_p0a_verifier.md`, `..._p3_verifier.md` and `..._p4_verifier.md`. The seven receipts these cycles produced were recorded earlier (ledger at 920).

## What changes and why
1. **Statements of absence carry the perimeter of the search that was run (P0a, section 5).** The IT6 census sentence ('no public record ... in a WWOX-deficient system') was false as written: it had no neural qualifier. It becomes 'no deposited, downloadable record was found for a genetically WWOX-deficient **neural** system; not found by that search is not shown absent', with non-neural records given as examples and not as a complete list (the metabolic search vocabulary was narrow). The sentence is replaced in place in `DL-MECH-173`, `HYP-20261026-10` and the map (R-10). CARVE-OUT, named: those three passages sit in the UPDATE of the previous iteration (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`); they are replaced on the P0a verdict list (C1, C2, C18) because the earlier text was a false global statement, and each replaced passage is tagged '(perimeter wording narrowed by BATCH_20261019_029)'; the historical candidate `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01` (items 4, and its two update bullets) is NOT edited, it is already integrated, and this candidate carries the corrected wording through the same records. The 'fly head RNA' sentence now says the knockdown depth is in Supplementary Figure 1 of the paper (qPCR in newly eclosed heads) and is not in the deposit.
2. **The ovarian paper reads a PERK band shift with a total-PERK antibody, not a phospho-PERK antibody** (receipt `FTR-20261029-28749468-02`); the wording is carried to the registry stub and the literature-log row, with the phospho-eIF2A and phospho-IRE-1 blots named as the phospho-specific readouts. 'Examples' replaces 'listed' for the non-neural metabolic records.
3. **The need `NEED-WWOX-GENE-ADDITION`** now reads 'The only post-onset add-back **found** is organoid hyperexcitability ... its single-cell contrast is against non-treated, not vector-treated, organoids'. **Card J01** (packet and card, rebuilt with the bridge, `check_cards` clean): 'no study in the P10 reading set was found that reads glia and EEG in the same animals over the days that bracket onset'. Committed earlier on this branch.
4. **P3 (network and signature comparison) is registered as a discovery-ledger lead, `DL-MECH-174`** (Status `open`, Tag INFERENZA, EXPLORATORY, COMPUTATIONAL_RESULT): the six-gene glycolysis and lactate module does not transfer conclusively to the P47T deposit (INCONCLUSIVE, hippocampus exact one-sided p = 0.060, 5 of 6 genes); a signed external-only network and a WWOX-enriched network show NO ADDED VALUE; the signature route is NOT DETECTED, NOT EXCLUDED (rho 0.143 against the registered 0.15, interval spanning it). The falsifier and reopening condition (a replicated WWOX-deficient human neural contrast with a matched protein or activity readout, ChEMBL potency, the LINCS phase II signatures) are in the record. Three dated UPDATE bullets on the hypotheses it touches (`HYP-20260709-01`, `HYP-20260709-05`, `HYP-20261026-11`) say that no status changes and no support is added.
5. **P4 (context differences) is a dated UPDATE on `DL-MECH-173`:** the ISR sign stays unresolved with a third system giving no resolvable sign at about 0.3; Atf4 mRNA is lower in sign in all four mouse contrasts but partly as a control-group effect; the WOREE-against-SCAR12 organoid class difference is a source-reported, confounded, unreplicated hypothesis about model systems; no patient subgroup is supported.
6. **Reading updates** on five paper records, one registry stub and six literature-log rows for the papers re-read in IT7 P0a with a recorded receipt (question, depth, what the reading adds).

## What was deliberately NOT registered, and why
- **No working-model change.** Checked against the results: the working model has no PDK1, glycolysis-module or ISR-direction statement (its metabolic line calls the WWOX/HIF1A axis a systems-level state indicator and `CLAIM 025` stays `in observation`, which the inconclusive module transfer neither supports nor contradicts), and its 'durable rescue' lines and the early-window wording were already qualified in `WM_v7.29`. No bump, no history row.
- **No claim created or promoted.** Nothing in P3 or P4 meets the bar; the module transfer is inconclusive and the class difference is a contextual hypothesis. `PAPER 113` carries the only proteome table of a WWOX-deficient cell found, as a reading update, not as a claim.
- **No identity records for non-WWOX precedents**, and no PAPER record is created for the ovarian paper (it stays the stub `CORPUS-STUB-126`).
- **The late complete read of a non-WWOX case report (receipt `FTR-20261019-40183510-02`)** belongs to an earlier iteration and has no IT7 result; not registered here.
- **The P3 compound results are not registered as candidates**: they are module opposition in wild-type neural cells with no exposure and no WWOX-loss relevance; the 256-family universe is a stated subset, not a catalogue screen. No card or need is edited for P3 (the P5 and P6 integration already carries the verified wording).
- **P1, P2, P5, P6 and P8 results** (subnetwork, usable compounds, pharmacological comparison, loop demonstration, scout and licence work) are tool-level or already integrated and state no further registry fact; not touched.
- **No ledger bullet restates a number that the verifier did not reproduce**; the verifier's draw differs slightly from the producer's for the matched-null 95th percentile (0.396 against 0.389), which changes no conclusion and is not quoted.
- **Receipt ledger untouched**, `working_model_*`, `claim_registry_current`, `dismissal_ledger_current`, `experiment_ledger` and `disease_model.md` untouched.

## Version rule (prompt_batch_commit section 7)
No statement in `working_model_current.md` changes, so no bump: `WM_v7.29` is preserved, the working-model history gets no row. A reading update, a ledger bullet and a map sentence are not working-model changes.

## Op lists
`ops_parsed` is declared per file below, 31 record-scoped ops in all (18 in the original lists, 13 in the addendum): working model 0, claim registry 0, paper registry 6, literature log 6 (both through `batch_commit.py propagate`, dry run then `--apply`), discovery ledger 2 and hypotheses ledger 4 (through `record_scoped_edit.py apply`, dry run then `--apply`, because `batch_commit.py propagate` accepts only the four scientific current files). One further ledger change is not an op: the new lead `DL-MECH-174` is appended by `discovery_lead.py append` (numbered and written by the validated writer, spec below). The ledger ops replace the census sentence in the `BATCH_20261019_027` update (the carve-out above) and add one dated UPDATE bullet each; earlier wording is otherwise untouched.

### working_model_current.md (0 ops)
None.

### claim_registry_current.md (0 ops)
None.

### paper_registry_current.md (6 ops)
```json
[
 {
  "op": "replace-within",
  "id": "PAPER 004",
  "old": "n shifts astrocyte-activation-type genes at P17 (Figure 3 legend; heat map not re-opened).",
  "new": "n shifts astrocyte-activation-type genes at P17 (Figure 3 legend; heat map not re-opened).\n**Reading update (2026-10-29, `BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`):** receipt `FTR-20261029-33914858-04`, `partial_fulltext_read`, question-driven (is GSE158681 the deposit of this paper, which Cre drivers and control genotypes; Data and code availability, the Methods paragraph on conditional models, the Figure 3 legend and the RNA-seq Results paragraph in the operator-supplied text layer, used for matching; the supplement workbook headers and dimensions only, rows not analysed). The Methods name Nestin-Cre (N-KO) and Synapsin-Cre (S-KO), with S-Control = Wwox+/+ carrying Synapsin-Cre. The paper states no accession and its data statement is 'available ... upon reasonable request'; the link to GSE158681 rests on identical numbers per arm and on Supplementary Table 2, not on a statement of the paper. No claim, Status or Summary changes."
 },
 {
  "op": "replace-within",
  "id": "PAPER 039",
  "old": "st legends and 3 from one batch in some, not reconciled. See the wave note on `CLAIM 002`.",
  "new": "st legends and 3 from one batch in some, not reconciled. See the wave note on `CLAIM 002`.\n**Reading update (2026-10-29, `BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`):** receipt `FTR-20261029-34268881-12`, `partial_fulltext_read`, question-driven (which arms are in the GEO series GSE156243 and which readouts have an add-back arm; Data and code availability, the Figure 3, Figure 4 and Figure EV2 legends and the series sample list). The add-back arms (stem-cell knock-in and lentivirus) are not in GSE156243, and the add-back readouts are functional, immunostaining, qPCR and immunoblot: no proteome, phospho-protein or flux readout of the integrated stress response or of the metabolic pathways. No claim, Status or Summary changes."
 },
 {
  "op": "replace-within",
  "id": "PAPER 094",
  "old": " search found no inducible neural Wwox model), RECOVERED in a model with these qualifiers.",
  "new": " search found no inducible neural Wwox model), RECOVERED in a model with these qualifiers.\n**Reading update (2026-10-29, `BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`):** receipts `FTR-20261029-42397075-06` (Figure 6 panels A to E and the data-availability and neuron-specific-restoration paragraphs; accepted-manuscript text layer, supplement not on this host) and `FTR-20261029-42397075-07` (the bioRxiv v2 Methods on library preparation and preprocessing and its data-availability paragraph; a different version from the published article, not treated as identical), both `partial_fulltext_read`, question-driven. The single-cell record of this paper is E-MTAB-14792; the preprint methods describe five libraries, one per condition (WT, WWOX-KO, SCAR12, WOREE, WOREE-WWOX; 5,151 cells for the add-back library against 7,687 for WOREE), so cells are not independent units. The single-cell add-back contrast (Figure 6C-E) is against non-treated WOREE, not against AAV9-EGFP-treated organoids (the vector arm exists in the functional assays only). The accession answered 'Study not accessible' on 2026-10-25 and 2026-10-29, so whether the add-back library is inside the deposit is UNVERIFIED. This bounds the sentence above that the organoid add-back is the only genetic add-back after a documented phenotype read in this corpus. No claim, Status or Summary changes."
 },
 {
  "op": "replace-within",
  "id": "PAPER 113",
  "old": "r must not infer from this record that the reading confirmed or changed anything in canon.",
  "new": "r must not infer from this record that the reading confirmed or changed anything in canon.\n**Reading update (2026-10-29, `BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`):** receipt `FTR-20261029-38563965-02`, `partial_fulltext_read`, question-driven (is the endothelial TMT proteome deposited, and what does the public supplement hold; Methods on the proteomic analysis, the first Results section, the Data Availability Statement and the Supplemental Data line, with the public figshare table parsed for the symbols named). NON-NEURAL (siRNA WWOX-silenced human endothelial cells): a TMT proteome table of 2,031 proteins plus 20 decoy rows is public as a journal supplement table, with no ProteomeXchange deposit; the paper also describes a tamoxifen-inducible Cdh5-CreERT2 Wwox deletion in endothelium. It is an example of a WWOX-deficient proteome table that the IT6 census missed, not a complete list, and it carries no neural, integrated-stress-response or flux claim. No claim, Status or Summary changes."
 },
 {
  "op": "replace-within",
  "id": "PAPER 567",
  "old": "ylation not measured). Class-level record; no individual-level detail. Not medical advice.",
  "new": "ylation not measured). Class-level record; no individual-level detail. Not medical advice.\n**Reading update (2026-10-29, `BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`):** receipt `FTR-20261029-42909904-04`, `partial_fulltext_read`, question-driven (does the paper report knockdown depth anywhere, and what does its data-availability statement say; the data-availability paragraph, the Results sentences on ATP and on the CRISPRa mRNA level, and the Supplementary Figure 1 legend in the derived supplement text, matching only, the graph not opened). The main text has no knockdown-efficiency statement; Supplementary Figure 1 reports qPCR of Wwox mRNA in heads for the RNAi and CRISPRa lines (N=3 pools of 15 heads, newly eclosed females). That depth is not in the RNA deposit and was not measured at the day-14 age that was sequenced. No claim, Status or Summary changes."
 },
 {
  "op": "replace-within",
  "id": "CORPUS-STUB-126",
  "old": "**Next action:** screening / triage required\n**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.",
  "new": "**Next action:** screening / triage required\n**Note:** Added during Phase 1 corpus-to-registry alignment. Preserve until processed, filtered out, or upgraded to a full PAPER record.\n**Reading update (2026-10-29, `BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`):** receipt `FTR-20261029-28749468-02`, `partial_fulltext_read`, question-driven (which integrated-stress-response readouts the paper shows, in which clones and cells, and whether anything is deposited; the ER-stress Results section, the Methods on cell lines, and the Figure 4 and Figure 5 legends and images). NON-NEURAL (an ovarian cancer line with a WWOX-null clone and stable WWOX add-back): phospho-eIF2A and phospho-IRE-1 blots with phospho-specific antibodies, and a PERK band shift that the authors read as phosphorylation, made with a TOTAL-PERK antibody and not a phospho-PERK antibody; no deposit. An example of a non-neural isogenic null and add-back pair, not a measurement in a WWOX-deficient neural system. The record stays a stub; no identity change."
 }
]
```

### literature_tracking_log_current.md (6 ops)
```json
[
 {
  "op": "replace-within",
  "id": "LIT-0110",
  "old": "tion scored for delay, weight and survival only. See [[paper_registry_current#PAPER 004]].",
  "new": "tion scored for delay, weight and survival only. See [[paper_registry_current#PAPER 004]]. Reading update 2026-10-29 (`BATCH_20261019_029`): receipt `FTR-20261029-33914858-04`; deposit identity and Cre drivers (Nestin-Cre and Synapsin-Cre, stated in the Methods; no accession in the paper). See [[paper_registry_current#PAPER 004]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0365",
  "old": " add-backs against the first measured phenotype. See [[paper_registry_current#PAPER 039]].",
  "new": " add-backs against the first measured phenotype. See [[paper_registry_current#PAPER 039]]. Reading update 2026-10-29 (`BATCH_20261019_029`): receipt `FTR-20261029-34268881-12`; the add-back arms are not in GSE156243, and their readouts are functional, immunostaining, qPCR and immunoblot. See [[paper_registry_current#PAPER 039]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0139",
  "old": "le: Endothelial knockdown of WWOX increases inflammation in ventilator-induced lung injury",
  "new": "le: Endothelial knockdown of WWOX increases inflammation in ventilator-induced lung injury Reading update 2026-10-29 (`BATCH_20261019_029`): receipt `FTR-20261029-38563965-02`; non-neural: a siRNA endothelial TMT proteome table is public as a supplement (no ProteomeXchange deposit). See [[paper_registry_current#PAPER 113]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0417",
  "old": "otype seen at week 7, radial glia not corrected. See [[paper_registry_current#PAPER 094]].",
  "new": "otype seen at week 7, radial glia not corrected. See [[paper_registry_current#PAPER 094]]. Reading update 2026-10-29 (`BATCH_20261019_029`): receipts `FTR-20261029-42397075-06` and `-07`; the single-cell add-back contrast is against non-treated organoids, one library per condition, the accession is not accessible. See [[paper_registry_current#PAPER 094]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0838",
  "old": "**Note:** class-level record. Not medical advice.",
  "new": "**Note:** class-level record. Not medical advice. Reading update 2026-10-29 (`BATCH_20261019_029`): receipt `FTR-20261029-42909904-04`; the knockdown depth is in Supplementary Figure 1 (qPCR at eclosion), not in the deposit. See [[paper_registry_current#PAPER 567]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0145",
  "old": "WOX sensitises ovarian cancer cells to paclitaxel via modulation of the ER stress response",
  "new": "WOX sensitises ovarian cancer cells to paclitaxel via modulation of the ER stress response Reading update 2026-10-29 (`BATCH_20261019_029`): receipt `FTR-20261029-28749468-02`; non-neural: phospho-eIF2A and phospho-IRE-1 blots and a PERK band shift read with a total-PERK antibody, no deposit. See [[paper_registry_current#CORPUS-STUB-126]]."
 }
]
```

### discovery_ledger_current.md (2 ops, record_scoped_edit.py)
```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-173",
  "old": "A census of public records found none that measures, in a WWOX-deficient system, a proteome or phospho-proteome, translation, eIF2 alpha phosphorylation or PERK/GCN2 activation, ATF4 protein or an enzyme and flux readout (OCR, ECAR, PDH, NAD(H)); the fly head metabolomics deposit is still not public, and the fly head RNA deposits show no visible Wwox change in the deposited counts, so they offer no check of perturbation depth.",
  "new": "A census of public deposits (Europe PMC, GEO, PRIDE keyword search, a MassIVE metadata filter, MetaboLights and ArrayExpress listings; 2026-10-29) did not find a deposited, downloadable proteome, phospho-proteome, translation, eIF2 alpha phosphorylation or PERK/GCN2 activation, ATF4 protein or enzyme and flux record (OCR, ECAR, PDH, NAD(H)) for a genetically WWOX-deficient neural system; not found by that search is not shown absent, and the accession and keyword routes cannot see a table published only as a journal supplement. Non-neural records exist, given as examples and not as a complete list (the metabolic search vocabulary was narrow): a WWOX-silenced endothelial TMT proteome table ([[paper_registry_current#PAPER 113]]); WWOX-null and add-back ovarian cells with phospho-eIF2A and phospho-IRE-1 blots and a PERK band shift read with a TOTAL-PERK antibody, not a phospho-PERK antibody (Janczar 2017, [[paper_registry_current#CORPUS-STUB-126]]); glycolysis and respiration in Wwox-deficient fibroblasts (abstract level, [[paper_registry_current#PAPER 024]]); and a muscle-specific ablation with lower mitochondrial activity. In a neural system the nearest metabolic readout is a lowered mitochondrial redox potential (a dye readout, not an OCR, ECAR, PDH or NAD assay) in WWOX-silenced human neural progenitors. The only candidate found that could reach pyruvate and TCA pools in a WWOX-deficient neural-targeted model, the fly head metabolomics deposit, is not public (checked twice on 2026-10-29). The fly head RNA deposits show no visible Wwox change in the deposited counts; the fly paper's Supplementary Figure 1 reports the knockdown depth by qPCR in newly eclosed heads, so the deposit offers no check of depth at the sequenced age, which is not the same as no evidence of depth."
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-173",
  "old": "independent rerun byte-identical, nine wording defects repaired.",
  "new": "independent rerun byte-identical, nine wording defects repaired.\n- **UPDATE 2026-10-29 (`BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`; IT7 P0a and P4; EXPLORATORY; COMPUTATIONAL_RESULT, descriptive, at transcript level except where a row says otherwise; the Status `open`, the Causal statement and the earlier updates are not edited).** (1) The census sentence of the update above is narrowed in place to a neural perimeter with named non-neural examples, after an independent check of every statement of absence; the narrowing changes no result. (2) The sign of the human ISR transcript signal stays UNRESOLVED when 13 contexts (human organoid, shRNA progenitors and neurons, four mouse contrasts, fly, rat, the P47T knock-in and two patient-line organoid classes) are put side by side in a pre-declared 182-cell matrix with no combined statistic: organoid lower, shRNA progenitors and neurons higher, mouse without a resolvable sign at about 0.3 in every contrast, ISR protein or phospho-protein measured only in the fly among these contexts. Whether the human difference is biology, line state or composition is not decided by the held data. (3) Atf4 mRNA is lower in sign in all four mouse contrasts, but this rests partly on the control group: the Cre-line controls sit above wild type while the knockouts sit below it, and control-against-control differences are as large as the neuron-targeted effect, so only the germline-null contrast against wild type is free of it (2 against 3 animals, not animal-separated); it is an mRNA observation, not an ISR call. Leave-one-animal-out under either statistic leaves the ISR-set sign unstable in three of four mouse contrasts. (4) The WOREE-against-SCAR12 organoid difference (radial-glia proportion, layer markers lower in WOREE and wild-type-like in SCAR12, week-16 firing about 3-fold higher in WOREE) is reported by its source, from lines of three and two individuals, and is confounded with variant type, individual and batch, from one laboratory and unreplicated: a contextual hypothesis about model systems, not a subgroup. NO PATIENT SUBGROUP is supported, no clustering was done and no response label is given to anyone. Sources: `drug_repurposing/census_reconciliation_it7_20261029.md`, `drug_repurposing/context_differences_it7_p4_20261029/README.md`; independent verifier reports `locator_audits/2026-10-29_it7_p0a_verifier.md` and `locator_audits/2026-10-29_it7_p4_verifier.md`."
 }
]
```

New lead appended by `discovery_lead.py append` (`DL-MECH-174`):
```json
{
 "kind": "MECH",
 "status": "open",
 "tag": "INFERENZA",
 "title": "A six-gene glycolysis and lactate module built in two human WWOX-loss transcript systems does not transfer conclusively to the P47T mouse deposit, and a bounded network comparison found no added value for a signed or WWOX-enriched network (EXPLORATORY, COMPUTATIONAL_RESULT; the signature route is not detected, not excluded)",
 "source": "integrator, mandate IT7 registries step; drug_repurposing/network_comparison_it7_p3_20261029/README.md (pre-registered, deviations declared) and the independent verifier report locator_audits/2026-10-29_it7_p3_verifier.md (numbers reproduced, no defect changing a verdict); module and signs from drug_repurposing/subnetwork_it7_p1_20261029; GSE215425 (P47T knock-in, 5 against 5 animals)",
 "causal_statement": "COMPUTATIONAL_RESULT, exploratory, transcript level, no receipt-backed paper reading behind it. (1) Transfer of the module (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down in the human WWOX-loss build systems) to the independent P47T deposit: hippocampus contrast +0.329 (positive = WWOX-loss-like), inside the decile-matched null band (95th percentile 0.389), exact one-sided p = 0.060 over 252 assignments, 5 of 6 genes in the build direction (LDHB against, -0.10); other regions leaned the same way without reaching the registered threshold. The pre-registered verdict is INCONCLUSIVE; the module is not shown to be a reproducible WWOX-loss feature. (2) Method comparison on 256 compound families that have a strict neural signature in both a progenitor-like and a neuron-like LINCS context (a stated subset of the catalogue, not a screen): a signed external-only network (NET) and a WWOX-enriched network (four curated HIF1A edges added) gave no detectable gain over an unsigned overlap reference (NET rho 0.047; enriched minus external-only -0.0015, 90 percent interval -0.004 to +0.0002), so NO ADDED VALUE for the network and for the WWOX-enriched condition at a minimum detectable effect of about rho 0.157. The transcriptional-signature route (the six-gene opposition score read across neural contexts) reached rho 0.143 against the registered 0.15 (90 percent interval 0.039 to 0.243, under its own random-readout null): effect NOT DETECTED, NOT EXCLUDED; it is not evidence that the signature route does not work. The compound results are module opposition in wild-type neural cells and carry no demonstrated WWOX-loss relevance, exposure or efficacy.",
 "falsifier": "Reopen the module-transfer question with a replicated WWOX-deficient human neural contrast that carries a matched protein or activity readout (or a larger P47T-type cohort). Reopen the compound-ranking comparison with a compound-response measurement in a WWOX-deficient human neural system with biological replication, potency taken from the ChEMBL activity endpoint, LINCS phase II (GSE70138) signatures, or a module larger than six genes. A concordant, replicated module in such a system with a matched readout would support using it as a readout; a discordant one (for example LDHB or PDK1 against the build direction again) would remove it.",
 "transfer_limit": "Transcript level only; one partial-loss missense knock-in with 5 against 5 animals, regions not independent; five of the six readout genes are inferred, not measured, in the LINCS platform; the universe is 256 compound families, one concentration and mostly one time point, wild-type cells, no exposure for any compound; the build systems are n=1 per arm in one of the two. No hypothesis status, ranking or support changes; association is not modulation is not rescue. Not medical advice; no dose.",
 "links": []
}
```

### therapeutic_hypotheses_ledger_current.md (4 ops, record_scoped_edit.py, addressed by the exact heading)
```json
[
 {
  "op": "replace-within",
  "heading": "HYP-20261026-10 — Attenuating the integrated stress response in WWOX loss: no signed human readout yet, so the first experiment is the readout",
  "old": "A census of public records found no proteome, phospho-proteome, translation, eIF2 alpha phosphorylation, ATF4 protein or flux record in any WWOX-deficient system, so the first experiment stays",
  "new": "A census of public deposits found no deposited proteome, phospho-proteome, translation, eIF2 alpha phosphorylation, ATF4 protein or flux record for a genetically WWOX-deficient neural system (not found by that search is not shown absent; non-neural records exist, see the discovery-ledger update of 2026-10-29 on the integrated stress response), so the first experiment stays"
 },
 {
  "op": "replace-within",
  "heading": "HYP-20260709-01 — Dieta chetogenica con razionale WWOX-specifico (non solo antiepilettico empirico)",
  "old": "e the null; absence of support, not a demonstrated decrease (see `DL-MECH-020`). Not medical advice.",
  "new": "e the null; absence of support, not a demonstrated decrease (see `DL-MECH-020`). Not medical advice.\n- 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`; IT7 P3; EXPLORATORY; COMPUTATIONAL_RESULT; the Status, the ranking line and the score are unchanged; no support is added)** A six-gene glycolysis and lactate module built in the two human WWOX-loss transcript systems (SLC2A1, HK2, LDHA, LDHB, BNIP3 up; PDK1 down) was tested for transfer to the P47T mouse deposit: the pre-registered verdict is INCONCLUSIVE (hippocampus +0.329, inside the matched null band, exact one-sided p = 0.060, 5 of 6 genes in the build direction; PDK1 -0.08 as predicted, LDHB against). The chain is therefore not shown to be a reproducible WWOX-loss feature; this adds no support to the HIF1A-PDK-PDH premise and removes none. Source: `drug_repurposing/network_comparison_it7_p3_20261029/README.md` and its independent verifier report. Association is not modulation is not rescue. Not medical advice."
 },
 {
  "op": "replace-within",
  "heading": "HYP-20260709-05 — Dicloroacetato (DCA) per riattivare PDH a valle del blocco HIF1α→PDK",
  "old": "on. Card I01 status `controversial`; no favourable compound is offered. Not medical advice; no dose.",
  "new": "on. Card I01 status `controversial`; no favourable compound is offered. Not medical advice; no dose.\n- 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`; IT7 P3; EXPLORATORY; COMPUTATIONAL_RESULT; the Status `parked` is unchanged and no ranking line is added; no support is added)** The same module test bears on the premise of this strand only at the transcript level: PDK1 is the single down-gene of the module and its P47T sign is as predicted but small (-0.08) inside a transfer that is INCONCLUSIVE. A bounded comparison of compound-ranking methods on neuron-like LINCS signatures (256 compound families, a stated subset) found no added value for a signed or WWOX-enriched network and 'not detected, not excluded' for the signature route; it ranks module opposition in wild-type cells and says nothing about dichloroacetate in a WWOX system. The Status `parked` and the closing condition above are unchanged. Source: `drug_repurposing/network_comparison_it7_p3_20261029/README.md` and its independent verifier report. Association is not modulation is not rescue. Not medical advice."
 },
 {
  "op": "replace-within",
  "heading": "HYP-20261026-11 — LDH lowering as a partial-benefit lever: one fly precedent, an approved candidate whose LDH potency is unresolved, no human WWOX datum",
  "old": "m, transcript level; the falsifying experiment is unchanged (see `DL-REPO-004`). Not medical advice.",
  "new": "m, transcript level; the falsifying experiment is unchanged (see `DL-REPO-004`). Not medical advice.\n- 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_029`, `CC-20261029-INTEGRATOR-IT7-REGISTRIES-01`; IT7 P3; EXPLORATORY; COMPUTATIONAL_RESULT; the Status, the absence of a ranking line and the reopening condition are unchanged; no support is added)** In the P47T mouse deposit the glycolysis and lactate module leans in the build direction (5 of 6 genes) but the transfer is INCONCLUSIVE, and LDHB, the gene closest to this lever, is again the discordant one (-0.10), as in the earlier mouse P17 deposits; the lever's premise (raised LDH activity or lactate in WWOX-deficient human neural cells) is not strengthened. The compound-ranking comparison (no added value for a signed or WWOX-enriched network; signature route not detected, not excluded) names no LDH agent as a candidate. The Status `generated`, the absence of a ranking line and the reopening condition are unchanged. Source: `drug_repurposing/network_comparison_it7_p3_20261029/README.md` and its independent verifier report. Association is not modulation is not rescue. Not medical advice."
 }
]
```

### dismissal_ledger_current.md (0 ops)
None.

## Normal edits (files that are not scientific current files or ledgers)
| File | Edit |
|---|---|
| `disease-models/wwox/analysis/mechanism_intervention_map.md` | R-10 update: the census sentence narrowed (deposited, genetically WWOX-deficient neural system, not found by that search is not shown absent); no ledger id named, so the curated SOURCE_IDS of the join keep their meaning |
| `disease-models/wwox/research/drug_repurposing/needs/needs.json` | NEED-WWOX-GENE-ADDITION inferred: 'only post-onset add-back found', single-cell contrast against non-treated organoids |
| `drug_repurposing/cards/J01_glial_reactivity_modulation.packet.json` and `.card.json`, and the same pair under `partial_benefit_it6_p10_20261029/` | 'in the P10 reading set was found'; cards rebuilt with `repurposing_bridge.py` |
| `framework/scripts/test_repurposing_join.py` | new class `RegistriesIT7` (5 tests, positive checks) |
| regenerated | `join/*`, `coverage/coverage_matrix.json`, `p5/*` if inputs changed, `view/index.html`, `view/index_shareable.html`, `view/shareable_package`, handoff, `registries/batch_queue.md`, `coverage_report.md`, `reading_state.md`, pathograph surfaces if inputs changed |

## Proof that the consumers use the corrected wording
`framework/scripts/test_repurposing_join.py::RegistriesIT7`: `DL-MECH-173`, `HYP-20261026-10`, the map R-10 and the need carry the perimeter wording (the map R-10, the need and card J01 do not carry the superseded sentence); the ovarian reading says total-PERK antibody and a band shift; `DL-MECH-174` carries INCONCLUSIVE, NO ADDED VALUE, NOT DETECTED, NOT EXCLUDED and the falsifier; the three hypotheses keep their Status and say that no support is added; the `DL-MECH-173` update carries the unresolved sign, the control-group caveat, the confounded class difference and 'NO PATIENT SUBGROUP'; every receipt named by a reading update of this batch is recorded in the ledger, and the working model keeps the version the manifest declares.

## Needs a verifier
The ledger bullets and reading updates restate independently verified material and add no new reading. Owed to a later actor: whether a reviewer wants the claims `CLAIM 030` or `CLAIM 025` to carry a wave note for the census narrowing or the inconclusive module transfer (not done: no claim text depends on either).

## BATCH DISPOSITION

**Verdict:** PROPAGATED (research layer and registry notes; working model `WM_v7.29` preserved, no bump)
**Batch:** `BATCH_20261019_029` (2026-10-29, MANUAL, ACTOR_ID `integrator`, task `INT-IT7-REGISTRIES-20261029`, registries step)

- **Absence statements with perimeter; ovarian reading as total-PERK band shift:** propagated to `DL-MECH-173`, `HYP-20261026-10`, the map (R-10), the need, card J01, `CORPUS-STUB-126`, `LIT-0145`.
- **P3 module transfer and network comparison:** propagated as the new lead `DL-MECH-174` and UPDATE bullets on `HYP-20260709-01`, `HYP-20260709-05`, `HYP-20261026-11` (no status change, no support added).
- **P4 context differences:** propagated as an UPDATE on `DL-MECH-173` (sign unresolved, control-group caveat, confounded class hypothesis, no patient subgroup).
- **Reading updates:** `PAPER 004`, `PAPER 039`, `PAPER 094`, `PAPER 113`, `PAPER 567`, `CORPUS-STUB-126`, `LIT-0110`, `LIT-0365`, `LIT-0139`, `LIT-0417`, `LIT-0838`, `LIT-0145`.
- **Unchanged:** every `Status`, `Type`, `Title` and `Summary`; the working model; the claim registry; the dismissal ledger; the receipt ledger; the Status and ranking of every hypothesis touched.

## Addendum 2026-10-29 (repair after the independent adversarial review `research/locator_audits/2026-10-29_it7_batch_review.md`; 0 HIGH, 6 MEDIUM, 8 LOW)
Wording repairs only, as record-scoped `replace-within` edits of this batch's own text (and of the three carve-out passages, tagged), each against the receipts and cycle reports; nothing else is touched. The earlier statement that the replaced passages were "this iteration's own" is withdrawn (M2): they were the previous iteration's, replaced on the P0a verdict list, and are now tagged.
- M1: map R-10 row WWOX_DIRECT_EVIDENCE 'none in any WWOX-deficient human system' becomes 'none found in a WWOX-deficient human neural system (non-neural examples: see the discovery-ledger ISR update of 2026-10-29)'.
- M2: carve-out named (above, batch record, test docstring); tag added to the three replaced passages.
- M3: `DL-MECH-174` quotes 'about 0.39 on the producer's and on the verifier's draw', not 0.389.
- M4: card J01 item (3) restricted to the deposited week-15 transcripts and the immunofluorescence finding (GFAP and S100B at weeks 15 and 24; GFAP also marks radial glia) added; packet and card rebuilt with the bridge in `cards/` and `partial_benefit_it6_p10_20261029/`, `check_cards` clean.
- M5: PAPER 567 and PAPER 039 say 'in the sections read' (Methods and Discussion not read per the receipts); LIT-0365 likewise.
- M6: `RegistriesIT7` asserts the real Status lines of the HYP records and more phrases; docstring corrected; per-phrase mutation run recorded in the batch record.
- L1 paired-difference interval and the NET-EXT remark; L2 the module was chosen with the mouse P17 deposit already seen as discordant, the neuron library agreed on 2 of 6 genes; L3 'reports no compound-level result'; L4 fly with and without amyloid, 89 of 182 cells UNKNOWN, Atf4 immunofluorescence; L5 'Wwox-deficient cells (mouse embryonic fibroblasts per the registry record; abstract level)'; L7 'P10 reading set' defined in J01; L8 PAPER 004 attribution to the P4 cycle.
- L6: `rescue_window_it6_20261029.md` rows 'Conditional / inducible' (neural qualifier and the endothelial Cdh5-CreERT2 allele) and the need row ('found', vector-control note) already carry the P0a wording at this branch head; no edit needed.

### Addendum op lists (record-scoped, 13 ops)
discovery ledger (7 ops, record_scoped_edit.py):
```json
[
 {
  "op": "replace-within",
  "id": "DL-MECH-173",
  "old": "which is not the same as no evidence of depth.",
  "new": "which is not the same as no evidence of depth. (perimeter wording narrowed by BATCH_20261019_029)"
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-173",
  "old": "glycolysis and respiration in Wwox-deficient fibroblasts (abstract level, [[paper_registry_current#PAPER 024]])",
  "new": "glycolysis and respiration in Wwox-deficient cells (mouse embryonic fibroblasts per the registry record; abstract level, [[paper_registry_current#PAPER 024]])"
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-173",
  "old": "stays UNRESOLVED when 13 contexts (human organoid, shRNA progenitors and neurons, four mouse contrasts, fly, rat, the P47T knock-in and two patient-line organoid classes) are put side by side in a pre-declared 182-cell matrix with no combined statistic:",
  "new": "stays UNRESOLVED when 13 contexts (human organoid, shRNA progenitors and neurons, four mouse contrasts, fly with and without amyloid, rat, the P47T knock-in and two patient-line organoid classes) are put side by side in a pre-declared 182-cell matrix (89 cells are UNKNOWN: gaps, not zeros) with no combined statistic:"
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-173",
  "old": "ISR protein or phospho-protein measured only in the fly among these contexts.",
  "new": "an ISR protein-level readout (Atf4 immunofluorescence, unchanged without amyloid) exists only in the fly among these contexts."
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-174",
  "old": "inside the decile-matched null band (95th percentile 0.389)",
  "new": "inside the decile-matched null band (95th percentile about 0.39 on the producer's and on the verifier's draw)"
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-174",
  "old": "so NO ADDED VALUE for the network and for the WWOX-enriched condition at a minimum detectable effect of about rho 0.157.",
  "new": "so NO ADDED VALUE for the network (minimum detectable effect about rho 0.157 at 256 families; NET-EXT, upper bound 0.15, is the better-supported negative) and for the WWOX-enriched condition (a paired difference, -0.0015 with a 90 percent interval of -0.004 to +0.0002, four HIF1A edges only; the 0.157 does not apply to it)."
 },
 {
  "op": "replace-within",
  "id": "DL-MECH-174",
  "old": "to the independent P47T deposit:",
  "new": "to the independent P47T deposit (the module was chosen with the mouse P17 deposit already seen as discordant for LDHA and LDHB, and the neuron library agreed on only 2 of 6 genes, so the human side is a two-system observation):"
 }
]
```
hypotheses ledger (2 ops, record_scoped_edit.py):
```json
[
 {
  "op": "replace-within",
  "heading": "HYP-20261026-10 — Attenuating the integrated stress response in WWOX loss: no signed human readout yet, so the first experiment is the readout",
  "old": "not found by that search is not shown absent; non-neural records exist, see the discovery-ledger update of 2026-10-29 on the integrated stress response), so the first experiment stays",
  "new": "not found by that search is not shown absent; non-neural records exist, see the discovery-ledger update of 2026-10-29 on the integrated stress response (perimeter wording narrowed by BATCH_20261019_029)), so the first experiment stays"
 },
 {
  "op": "replace-within",
  "heading": "HYP-20261026-11 — LDH lowering as a partial-benefit lever: one fly precedent, an approved candidate whose LDH potency is unresolved, no human WWOX datum",
  "old": "The compound-ranking comparison (no added value for a signed or WWOX-enriched network; signature route not detected, not excluded) names no LDH agent as a candidate.",
  "new": "The compound-ranking comparison (no added value for a signed or WWOX-enriched network; signature route not detected, not excluded) reports no compound-level result in the P3 README, so no LDH agent is named or excluded."
 }
]
```
paper registry (3 ops, batch_commit.py propagate):
```json
[
 {
  "op": "replace-within",
  "id": "PAPER 567",
  "old": "The main text has no knockdown-efficiency statement; Supplementary Figure 1",
  "new": "In the Results paragraphs and the data-availability paragraph read (Methods and Discussion not read) there is no knockdown-efficiency statement; Supplementary Figure 1"
 },
 {
  "op": "replace-within",
  "id": "PAPER 039",
  "old": "and the add-back readouts are functional, immunostaining, qPCR and immunoblot: no proteome, phospho-protein or flux readout of the integrated stress response or of the metabolic pathways.",
  "new": "and the add-back readouts are functional, immunostaining, qPCR and immunoblot; the legends and Results read show no proteome, phospho-protein or flux readout of the integrated stress response or of the metabolic pathways (Methods and Discussion not read)."
 },
 {
  "op": "replace-within",
  "id": "PAPER 004",
  "old": "rests on identical numbers per arm and on Supplementary Table 2, not on a statement of the paper",
  "new": "rests on identical numbers per arm and on Supplementary Table 2 (both matched in the P4 cycle, not by this receipt), not on a statement of the paper"
 }
]
```
literature log (1 op, batch_commit.py propagate):
```json
[
 {
  "op": "replace-within",
  "id": "LIT-0365",
  "old": "their readouts are functional, immunostaining, qPCR and immunoblot.",
  "new": "their readouts, in the legends and Results read, are functional, immunostaining, qPCR and immunoblot."
 }
]
```
