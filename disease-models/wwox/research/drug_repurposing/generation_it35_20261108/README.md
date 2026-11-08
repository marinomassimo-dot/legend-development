# IT35 P3-P6: where knowledge stops feeding generation, a small link, and a guided/unguided comparison

Non-canonical. Not medical advice. Public edition, WWOX-DEE reference genotype class. Zero spend, no contact. What is measured here is consumption and reach, not predictive skill.

## P3 Diagnosis on contrasting cases (more than one experimental origin)
Break-point classes: knowledge not retrieved / relation not represented / tool available but not called / action unresolved / absent from the graph / no probe / scientific limit.

| Case (origin) | Chain as far as it went | Where it stopped | Class | What changed |
|---|---|---|---|---|
| Sag and intrinsic excitability (neuron-deleted mouse slices, PMID 34634460) | observation, qualified, scored in IT14 P3 | no need, no investigation | relation not represented | IT34: need + INV-18 (a manual structural addition, declared as such: the need search then reached Ih tools without naming them) |
| GSK3 to eIF2B epsilon (Wwox-null brain blot, plus CHO cells, rat heart, mouse retina) | two needs hold GSK3B and EIF2B5 separately; the package found the precedent link | the two needs were not connected: a GSK3 inhibitor was invisible under the ISR need and an eIF2B tool under the GSK3 need | relation not represented | IT35 bridge table (below) |
| HDAC5 to SLC2A1 (human primary muscle knockdown) | INV-16, 20 proposals tied to it in IT32 | HDAC5 compounds were invisible under the PDH need, whose SLC2A1 is only a readout marker | relation not represented | IT35 bridge table (below) |
| MYC role (organoids, another-disease progenitors, chick and mouse tissue) | INV-17 and 555 proposals tied to it in IT33 | the role of MYC is unresolved | scientific limit (no MYC-selective perturbation of a WWOX system in the routes searched) | nothing to add to the engine |
| ISR tool compound (published tool in many labs) | the thread names it as a probe (hypothesis H4 of the GSK3 package) | not in the catalogue by name; EIF2B2 to EIF2B5 have no catalogue records; ChEMBL holds the molecule (CHEMBL4303573, an unnamed record whose structure is the published one) and the target (eIF2B epsilon, CHEMBL5725120) but no curated mechanism and no activity linking them | no probe in the source the catalogue is built from | not fixed: adding it needs an identity-checked tool-compound entry, not a generator change |
Independent origins: the cases rest on different experimental systems and groups; the sag case and the carbenoxolone case of IT34 share one paper and are not counted twice.

## P6 The smallest general link: precedent bridges in the need search
`needs/bridges_it35.tsv` holds two curated precedent relations (GSK3B with EIF2B5; HDAC5 with SLC2A1), each with status `observed_other_context`, context, evidence pointer and what is not shown. `repurposing_search.py need <id> --bridges <file>` adds, for each bridge touching a target of the need, the other gene as a **pathway member** carrying the bridge. Pathway members are counted apart from the headline links, a bridged row can never be `consistent` or `opposed` (the code sets `direction_unresolved`: no sign crosses a bridge), and every bridged row says "HYPOTHESISED BRIDGE (not an observed link in a WWOX system)" with its evidence. Off by default.

| Need searched | Headline links (records / families) | Rows listed without bridges | with bridges |
|---|---|---|---|
| NEED-ISR-ATTENUATION (+ GSK3B) | 12 / 12 both | 78 | 171 |
| NEED-PDH-PYRUVATE-AXIS (+ HDAC5) | 8 / 8 both | 209 | 293 |
| NEED-GSK3B-DEREPRESSION (+ EIF2B5) | 81 / 80 both | 588 | 588 (EIF2B5 has no catalogue records) |
Ablation: with no bridge file the lists are identical to before. Tests: `framework/scripts/test_repurposing_search_bridges.py` (the headline is unchanged, no sign, the limit text is present, the table is well formed; the catalogue-dependent test skips without the local cache). Classification: **reach**, not a new relation and not prediction: the bridge widens what a researcher sees under a need; it is an addition by a curator, declared as such. Nothing is promoted and no ranking changes. Reopening: if a further bridge is needed, add a row with its evidence pointer; if the table grows past a few dozen rows it deserves its own review.

## P4/P5 Guided against unguided on one phenotype (depolarised rest, larger sag and rebound, higher input resistance, NMDAR-dependent bursts)
Condition A (unguided): a delegate (sonnet, effort medium) received only the phenotype and context, no compound names and no repository file; it used PubMed at abstract level (`unguided_a/output/`). Condition B: what LEGEND already held (IT14 P3 scoring of nine functions, IT34 need and INV-18). Limits: not a prospective validation; the search tool returned the source paper's own abstract for a plain query, so the condition did not fully isolate the question from the paper; abstracts only; this does not show that a model ignores prior knowledge.

| Measure | A unguided | B held by LEGEND | Only after the other |
|---|---|---|---|
| distinct rationales (by reason, not synonym) | 7 (K+ leak, Ih gain, immaturity or cell size, consequence of bursting, reduced tonic GABA shunt, membrane lipids and cholesterol, Na/K-ATPase) | the Ih arm with 3 roles, Kv7 and chloride and gap junction scored, intrinsic state R2 | A alone: immaturity/cell size, consequence of bursting, lipids, Na/K-ATPase (the last without any supporting source); B alone: the heterozygote logic, Table 1 pseudoreplication, the burst counts |
| link types | transferred and hypothesised only (abstract level) | observed WWOX data plus transferred | - |
| a constraint that emerged only unguided | **input resistance is higher in both mutants, the opposite of what a larger Ih alone gives** (the converse is supported by PMID 21795624 in a dysplasia model); this points to a second or alternative change such as a resting K+ conductance | not in INV-18 before | now **Branch D** of INV-18 (weakened if blocker-sensitive K+ currents do not differ), with the need's inference; the mechanism and voltage range of the relation are background knowledge, not sourced |
| agents reached with identity | tool compounds and classes named, identities not verified | identities resolved through the catalogue | - |
| counter-evidence found | reduced Ih in dysplasia gives the opposite phenotype; in an HCN1 gain-of-function mouse a Kv7 opener increased ECoG spiking (so neither blocking Ih nor opening Kv7 is assumed protective) | discordant Ih precedents cited in the paper | both |
| consumption | about 74k output tokens for the producer, about 36k for the verifier (separate transcripts, not a share of any plan) | already paid | - |
Verifier (separate context, abstracts and one full text): 5 decisive items, the Ih-input-resistance premise only partly sourced (the abstracts say Ih regulates membrane potential and input resistance; the direction comes from the dysplasia paper; the mechanism is background knowledge), the dysplasia phenotype has a hyperpolarised rest and so is not a mirror image, the retigabine finding is ECoG spiking in vivo with other antiseizure drugs reducing it, the cholesterol finding concerns gating kinetics and trafficking in CHO cells (isoform-specific, HCN1 included): all four corrections are in the INV-18 and need texts.
What A adds that a researcher can use: one cheap discriminating measurement (potassium currents sensitive to a Kv7 blocker and a Kir blocker, input resistance with transmission blocked) and a reason to doubt a pure Ih reading. What it does not give: a candidate, a direction, or a validated prediction.
