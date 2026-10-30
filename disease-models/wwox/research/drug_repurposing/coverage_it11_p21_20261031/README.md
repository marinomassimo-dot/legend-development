# IT11 P2.1: why the generation graph did not return the five molecules with a recorded WWOX-system result

`scientist-a`, 2026-10-30 (Europe/Rome: night to 2026-10-31), branch `task/it11-p21` (from main `d6ccf8d1`). Exploratory, computational, read-only toward every earlier package. **Not medical advice. A compatible action of a context-free signed network is not a predicted benefit.**
Reference genotype: a WWOX-DEE genotype class; no individual-level record. Zero spend, no external service called, no e-mail address sent anywhere.

**Disclosure (not blind).** I read the IT10 README (3D), `dispose_it10.py` `phenotype_first()`, `results/phenotype_first.tsv`, the IT9 v3 README and `build_actions_v3.py` BEFORE forming the questions below. The five leads were used to build the IT10 phenotype path, so nothing here is an independent validation of the graph. The WWOX-result contexts were read from the repository's receipted cards, packets and deep-dive manifests (derivatives of the papers with verbatim snippets); **I did not open any primary paper**.

## 1. Decision (first)

| Question | Answer |
|---|---|
| Is "the graph returned 0 of 5" correct? | **No, not as written.** It holds only for the displayed top lists. Lithium (four salt/name-twin families) IS a seed-specific `mimics` hit in Q6 expression under all three nulls (z -12.1 / -8.9 / -6.4), rank 67 to 70 of 232 in v4 (rank 26 to 29 of 247 in IT9 v3, one place beyond the 25-row display cut). IT10 read the truncated `candidates_Q*.tsv` (top 50 opposes / 25 mimics per set) and labelled lithium "scored, never seed-specific"; `test_it10_p1.py` asserts that label. d-APV is also returned, as a direct hit in the Q4 `direct_search` arm (Q_direct -0.5, Z_full_robust -15.8, call `mimics`; "zero score" in IT10 means the indirect part only). |
| Why were the other leads not returned? | **Ethosuximide and vigabatrin cannot be scored at all**: their signed targets (CACNA1G/H/I; ABAT, SLC32A1) are sink or absent nodes of the OmniPath network (no outgoing edge), so no seed set could ever reach them. A51 has no catalogue identity. |
| Is any returned hit about the lead's WWOX result? | **No.** Lithium's Q6 hit concerns MYC expression in a human seed (chain GSK3A -P(-)-> NOTCH1 -T(+)-> MYC), the lead's result is a mouse seizure score that lithium also lowered in wild-type (not WWOX-specific). d-APV's hit is GRIN2C transcript (mouse) versus an ex vivo bursting readout. No seed set has a function-level endpoint. |
| What does zero-of-five (or one-of-five) mean? | Almost nothing about the graph. 7.9 percent of usable families (1,050 of 13,308) are seed-specific in at least one set, so by chance 66 percent of five random families would show none. The five were development inputs. It does show **where the representation is blind** (section 5). |
| Extension of the phenotype-first entry | Implemented as a wrapper (no earlier file edited): full-list lookup (fixes lithium), structural reachability code per lead, WWOX-result context columns, and a same-sign target-class mate list that is a search list, never evidence. 12 tests with inverses pass. The IT10 files need a 4-line patch (`proposed_patch_dispose_it10.diff`, applies cleanly, dry-run checked). |

## 2. Classification (closed list, one primary cause each)

| Molecule (unit) | Primary cause | Subtype | Secondary |
|---|---|---|---|
| Ethosuximide (U17) | **NO_PATH_TO_ANY_SEED** | targets CACNA1G (out 0, in 1), CACNA1H (out 0, in 6), CACNA1I (isolated): sinks | representation gap (channels); function-level endpoint is not a seed |
| Vigabatrin (U20) | **NO_PATH_TO_ANY_SEED** | ABAT, SLC32A1 are not network nodes; the family is not "examined" | OUT_OF_UNIVERSE in the narrow sense (not examined); action runs through a metabolite (GABA) the network cannot express |
| d-APV (U21) | **NULL_CONTRIBUTION** | indirect contribution 0 because the target is the seed; direct part non-zero in `direct_search` (diagnostic arm) | NO_PATH_TO_ANY_SEED for GRIN2A/B/D; level mismatch (transcript seed, receptor antagonist); sibling credit across four GluN2 subunits |
| Lithium (U24) | **LOW_RANK_SCORED** | seed-specific in Q6 expression, rank 67-70/232 | IT10 lookup truncation (label wrong); F1/F5 losses at protein level and in Q3/Q4; NULL_CONTRIBUTION in Q1/Q3/Q7; tested salt LiCl is OUT_OF_UNIVERSE; ion record has NO_ACTION_RECORD |
| A51 (U10) | **IDENTITY_UNRESOLVED** | name exists only in the paper | NO_ACTION_RECORD if the lookalike BTX-A51 were the compound (0 target rows); the identity is not assumed |
| Gene addition (U07), ketogenic diet (U15) | out of method (modality) | not in the closed list | `catalog/non_molecule_modalities.tsv` |

For ethosuximide, vigabatrin and A51 the absence of a row says nothing about the molecule: the graph has no way to speak about them.

## 3. Reconstruction per molecule (full cells: `reconstruction_it11_p21.tsv`; computed parts: `targets.tsv`, `pairs.tsv`, `universe.tsv`)

Pointers use paths under `disease-models/wwox/research/drug_repurposing/` (DR).

**(1) Identity and families.** Ethosuximide: neutral parent, no prodrug (`catalog.jsonl.gz` CHEMBL696 `chemistry.prodrug` 0); families `FAM:CAT:CHEMBL696` and name twin `FAM:CAT:DGIDB:6998a1a2d947`. Vigabatrin: neutral parent; `FAM:CAT:CHEMBL89598` and `FAM:CAT:DGIDB:358b8a817686`; CPP-115 (`CHEMBL146927`) is a separate unit member and not the tested molecule. d-APV: the paper's "d-APV" is mapped to `FAM:CAT:DGIDB:b0ca5cf2303c` "D-Ap5" by the alias declared in `dispose_it10.py` `PHENO_ALIASES` (standard synonym, not re-verified against a chemical identifier in the paper); the GtoPdb ChEMBL assertion CHEMBL84612 is `out_of_selection` in the catalogue, so the family is DGIdb-only. Lithium: the tested form in the cited figure is LiCl (manifest `deepdive_manifests/PMID32000863.json` verbatim_locators entry [0] and the Fig 7d legend snippet), which has **no catalogue family**. The active moiety is Li+; the catalogue carries the ion record (`CHEMBL1201333`, 0 target rows, the identity the G01 card points to), and salt/name-twin families that hold the actions: carbonate (`CHEMBL1200826`, `DGIDB:50ccc7b5c33e`), citrate anhydrous (`CHEMBL1201170`, parent of `CHEMBL2103738`), citrate (`DGIDB:cfa5bd0a6c8c`), a target-less succinate and cation, and `DGIDB:be65bb20ae7f` "Lithium" with 42 claims that carry no action type. Name twins are not merged by design, so the scored salts are not the tested form. A51: no identity (`ranking_it8_p9_20261029/unit_members.tsv` U10); the card (`cards/D01_a51.card.json`, `input.p4_card.identity`) says whether the organoid compound equals the clinical CK1-alpha/CDK7/CDK9 agent is not verified; `FAM:CAT:CHEMBL4754493` BTX-A51 exists (0 target rows) and is **not** attached.

**(2) Universe.** `build_funnel_v3.json`: 40,268 families, 13,308 with a signed HGNC-resolved target (`mnet_usable`), 12,560 "examined" (some target is a network node). Signed-usable: ethosuximide 2 of 2 families, vigabatrin 2 of 2, d-APV 1, lithium 4 of 9 (ion, succinates, cation, DGIdb "Lithium" are not), BTX-A51 0. Examined is not scoreable: of the 13,308 usable families only 8,245 have a signed target with an outgoing edge, i.e. 5,063 (38 percent) can never get an indirect score (`sinkstats_it11.py`, output `sinkstats_it11.txt`). Vigabatrin is not examined (no signed target is a node); ethosuximide is examined but has no row in any proposals table because every arm is exactly 0.

**(3) Targets and actions.** All signed actions are inhibitor/blocker (sign -1): ethosuximide CACNA1G/H/I (ChEMBL PROTEIN FAMILY row, scope complex_or_group; DGIdb rows unspecified); vigabatrin ABAT (ChEMBL single protein; GtoPdb/DGIdb), SLC32A1 (GtoPdb single protein); d-APV GRIN2A/B/C/D (GtoPdb, `single_protein_among_siblings`, one claim per subunit, so the antagonism is not subunit-specific); lithium GSK3A/GSK3B (ChEMBL group, scope complex_or_group) and IMPA1. Unsigned claims (action type None) are never scored: ethosuximide CYP3A4, SCN1A; vigabatrin GABBR1; lithium 42. F2: all targets HGNC-resolved; none appears in the 72 alias-collision or 36 complex-not-credited lists of `build_funnel_v3.json`. F3: no family carries UNCERTAIN_ACTIVE_MOIETY.

**(4) Relevance to Q1-Q7** (v4 engine run on the real network, three regimes per target-seed pair: `all` = no mode filter and no junction rule; `v3` = F1; `v4` = F1+F5; `pairs.tsv` has the chains). Seeds: Q1 WWOX; Q2 glycolysis set; Q3 ISR set; Q4 GRIN2C/GRM3/KCNA2/NPY (expression) and GAD1/GAD2 (protein); Q5 IL1B/IL6/TNF; Q6 MYC (expression, protein); Q7 GSK3B pSer9.
* Ethosuximide, vigabatrin, A51: **no pair in any regime** (`pairs.tsv` has no row; tested in `test_it11_p21.py`). F1/F5 are not involved: there is nothing to filter.
* d-APV: only the direct pair GRIN2C=GRIN2C (Q4 expression). GRIN2A/B/D have outgoing edges (3 each) but no chain within 3 hops reaches GRIN2C, GRM3, KCNA2 or NPY.
* Lithium (GSK3A/GSK3B; IMPA1 isolated), pairs in v4 / lost to F1 / lost to F5: Q1 expression 2/0/0, Q1 protein 0/2/0; Q2 19/1/4; Q3 7/4/9; Q4 expression 0/2/2, Q4 protein 0/4/0; Q5 6/0/0; Q6 expression 2/0/0 (GSK3A -P(-)-> NOTCH1 -T(+)-> MYC; GSK3B -P(+)-> HDAC3 -T(-)-> MYC), Q6 protein 0/1/1; Q7 GSK3B direct hit, the seed is a phospho-site of uncertain direction (arms cancel, Q_net 0). A direct GSK3B -> MYC edge is absent from the loaded SIGNOR file (grep of `signor_omnipath_edges.tsv.gz`); I did not check SIGNOR itself.
* Direct-search cut: the DGIdb "Lithium" family lists IL1B (Q5) and MYC (Q6) as unsigned targets and is a direct-search candidate at position 161 (Q5) and 54 (Q6), beyond the 50-row cap of `make_candidates_v3.py`. It could not score anyway (no action type).

**(5) Can it receive a score?** Ethosuximide no (sinks), vigabatrin no (not nodes), A51 no (no identity), d-APV yes only as a direct hit on GRIN2C, lithium yes (non-zero in Q2, Q5, Q6 expression; tiny magnitudes 1e-4 to 1e-3 whose significance is only against the degree-matched null).

**(6) Phenotype-first entry and context of the WWOX result** (`generation_it10_p1_20261031/results/phenotype_first.tsv`, `phenotype_first_it11.tsv`):

| Lead | System, allele, species | Readout (level) | Direction | Depth, source |
|---|---|---|---|---|
| Ethosuximide | Wwox-/- constitutive null, mouse, whole organism, stage UNKNOWN | PTZ-provoked seizure score, late phase of the hour, graphical reading (function) | decrease | complete_fulltext_read; PMID 32000863 Fig 7b; FTR-20260804-32000863-01, FTR-20261021-32000863-03; `cards_early/EB-ETX-01.packet.json` A-ETX-1 |
| Lithium | Wwox-/- vs +/+ littermates, preweaning mouse, whole organism | behavioural seizure stage after PTZ (function) | decrease in the null panel; same suppression in +/+ and +/- panels, so not Wwox-specific | complete_fulltext_read; PMID 32000863 Fig 7d (manifest entries [0], [5], [22]); `cards/G01_lithium_gsk3.packet.json` DR-LI-001; tested as LiCl 60 mg/kg |
| Vigabatrin | WWOX-DEE patients, mostly predicted null/null, human | cessation or burden of epileptic spasms (clinical) | 2 benefit, 3 null, 1 partial, 1 unresolved | queried_not_full_read, no receipt; `cards_early/EB-VGB-01.packet.json` A-VGB-1..6, A-VGB-10 |
| d-APV | Synapsin-Cre Wwox knockout mouse neocortex, ex vivo slice, about 2 weeks | spontaneous burst frequency (network electrophysiology) | decrease (eliminated, recovered on washout); n=5 slices, 3 animals | complete_fulltext_read; PMID 34634460 Results 2.2; FTR-20260810-34634460-02; `cards/F01_glutamate_receptor_node.packet.json` DR-W2-001 |
| A51 | WWOX-knockout human cerebral organoid, weeks 8-15 | SOX2+MYC+ fraction (cell identity) | decrease; layer-neuron fractions no change | complete_fulltext_read; FTR-20260810-42397075-04; panel values not re-auditable (card) |

## 4. Corrections to IT10 that follow (cite, do not re-do)

1. `generation_it10_p1_20261031/README.md` section 3D ("lithium ... scored but never seed-specific (Q2, Q5, Q6)", "0 of the 5 ... in a seed-specific arm") and `results/phenotype_first.tsv` (lithium `NAME_TWIN_SCORED_NOT_SPECIFIC:Q2,Q5,Q6`) rest on `phenotype_first()` reading `candidates_Q*.tsv`. The full list `results_v4/v3_seed_specific_all_nulls.tsv` has four lithium rows (Q6, mimics). `test_it10_p1.py::PhenotypeFirst` asserts the truncated label; the inverse (the truncated tables hold no seed-specific lithium row) is `test_it11_p21.py::TruncationArtefact`.
2. "DIRECT_HIT_ZERO_SCORE" for d-APV: the zero is `Q_net_ind`; `Q_direct` = -0.5 and Z_full_robust = -15.78 (the ind-null z is 0 because indirect is 0 by construction).
3. The Q6 hit for lithium is on a **single-gene seed set** (MYC): z measures specificity to MYC's regulator neighbourhood, not to WWOX (v3 README section 6). It does not become support for lithium: the tested endpoint is seizure, lithium lowered it in wild-type too, and the Q6 chain rests on NOTCH1/HDAC3 edges whose neural context and activity-level meaning are unverified.

## 5. (a) What zero-of-five does and does not mean

* It does not measure the graph. The five were used to build the phenotype path (development inputs), the sample is five, and the base rate of being seed-specific somewhere is 7.9 percent per usable family, so 0 or 1 of 5 is within chance (assuming independent draws, which the five are not).
* It does not mean the molecules are inactive, nor that the graph is wrong about them: for ethosuximide and vigabatrin the network has no way to speak (target classes absent or sink).
* It does show a structural blind spot, measured: of 2,373 distinct signed target genes 864 have an outgoing edge; ion-channel and receptor-subunit genes (regex CACN|SCN|KCN|GRI|GABR|CHRN|HCN|GLR|P2RX|TRP|ASIC|RYR) 12 of 201; SLC transporters 1 of 80; CYPs 0 of 33; GPCRs 54 of 63. The WWOX-tested antiseizure drugs and tool compounds act on channels, transporters and metabolic enzymes: exactly the classes a TF/kinase signalling network cannot propagate from. A drug-first or seed-first search from this network will therefore be silent on this class by construction, whatever its merit.
* It shows a second mismatch: seeds are transcript/protein/phospho states of genes; all five leads have function-level or clinical readouts (seizure score, bursting, spasms, progenitor fraction). No seed set can be endpoint-matched to a lead; the firewall classes (`intervention_response`, `held_out`, `card`) correctly forbid using the leads' own responses as seeds.
* It does not validate anything for lithium either: the Q6 hit is incidental to the lead's readout.

## 6. (b) Extension of the phenotype-first entry

Smallest useful extension, implemented in `phenotype_first_it11.py` (about 100 lines, wraps `dispose_it10.phenotype_first`, edits nothing; `python3 phenotype_first_it11.py run --out phenotype_first_it11.tsv`):

1. **Full-list graph_status** (fixes lithium; the 4-line change to the IT10 file is `proposed_patch_dispose_it10.diff`, `patch -p1 --dry-run` clean from `drug_repurposing/`). Executable check: `test_it11_p21.py::TruncationArtefact` (new label `IN_SEED_SPECIFIC_ARM:Q6/mimics`) with its inverse (truncated tables hold no such row); other leads unchanged.
2. **Structural reachability code per lead** (`TARGETS_NOT_IN_NETWORK`, `TARGETS_SINK_ONLY`, `TARGETS_HAVE_OUT_EDGES`, `NO_SIGNED_TARGET`) replacing the uninformative `NO_GRAPH_ROW`. Check: toy network codes, inverse (one added edge turns a sink into `TARGETS_HAVE_OUT_EDGES`), and the real leads (ethosuximide SINK, vigabatrin NOT_IN_NETWORK).
3. **Context columns** `ctx_system, ctx_genotype, ctx_species, ctx_endpoint, ctx_direction, ctx_depth, ctx_receipt` from the packets, so a candidate is compared against the same context and readout class as the lead. This is what the lead's WWOX result can legitimately select: the comparator and the endpoint class, not the candidate's rank.
4. **Target-class mates** (`class_mates`): other catalogue families sharing a signed target with the SAME sign (T-type channel blockers for ethosuximide; ABAT inhibitors for vigabatrin; GluN2 antagonists for d-APV; GSK3 inhibitors for lithium). Check: same-sign only; inverse (opposite sign returns the other family); the lead's own name twins excluded. Output column `class_mates_top`. **It is a search list for a measurement, not evidence**: no result of the lead is transferred to a class mate (different molecule, exposure, selectivity; matching_guidance rule on no transfer between molecules).

Not implemented, proposed: declare the leads as **coverage controls, not ranking controls**. A lead is a valid positive control for a seed set only if (i) its signed targets have an outgoing edge and (ii) the seed set contains an endpoint-matched gene state. Today that is satisfied for 0 of 5 (lithium and d-APV pass (i); none passes (ii)). The executable form is the reachability code above plus `pairs.tsv`; report "N of M leads representable" per seed set before any claim that the graph does or does not recover known leads. A second proposal: for A51, if an identity declaration is ever made, the what-if (`whatif_a51.tsv`) shows the card-named CSNK1A1 would connect to Q6 MYC as `mimics` (MYC up), opposite to the MYC suppression the card reports; so Q6 would not be a clean positive control either.

Class mates are listed in `phenotype_first_it11.tsv` (`class_mates_top`, truncated to 400 characters). I did not inspect them one by one, did not check their approval status or exposure, and make no claim that any of them is a candidate.

## 7. Data I could not obtain, and UNVERIFIED

* The primary papers (PMID 32000863, 34634460, 42397075, 42422765, 35573960) were not opened; contexts and the LiCl salt come from the repository's manifests, cards and packets. The lithium panel statement (wild-type also suppressed) is the manifest's reading of Fig 7d, entry [22].
* Whether the organoid "A51" equals BTX-A51 or the CK1-alpha/CDK7/CDK9 phase-1 agent: not verifiable here (card says so).
* SIGNOR/OmniPath source: whether SIGNOR itself lacks a GSK3B -> MYC edge (the loaded file has none); whether the NOTCH1/HDAC3 chain edges hold in neural cells.
* The PMID-level references of any edge in a chain (not in the committed edge tables).
* `d-APV = D-AP5` identity is the IT10 declared alias plus standard pharmacology, not a chemical identifier match from the paper.
* The regex used for the channel/transporter/GPCR counts is by gene-symbol prefix, a coarse class assignment.
* Class mates were not reviewed (above). The 66 percent base-rate figure assumes independent random draws.
* The sink/reachability counts use the typed edge list of the v4 reader (70,542 edges, T and P modes, signed non-zero only); a target absent there could still appear in other networks (not tested).

## 8. Files and commands

`reconstruction_it11_p21.tsv` (one row per lead, all cause columns) · `targets.tsv` · `pairs.tsv` · `universe.tsv` · `phenotype_first_it11.tsv` · `whatif_a51.tsv` · `sinkstats_it11.txt` · scripts `sinkstats_it11.py`, `reconstruct_it11_p21.py`, `build_reconstruction.py`, `phenotype_first_it11.py`, `whatif_a51.py` · `test_it11_p21.py` (12 tests) · `proposed_patch_dispose_it10.diff`.

```
export LEGEND_CATALOG_CACHE=<root>/disease-models/wwox/research/drug_repurposing/catalog/cache
python3 reconstruct_it11_p21.py --out .        # 80 s: v4 engine, three regimes, ten seed sets
python3 build_reconstruction.py
python3 phenotype_first_it11.py run --out phenotype_first_it11.tsv
python3 whatif_a51.py
python3 test_it11_p21.py
```
The 8,245 / 13,308 and class-gene counts come from `sinkstats_it11.py` (`python3 sinkstats_it11.py`, a few seconds), same inputs as `reconstruct_it11_p21.py`; no second reader has re-run it.

## 9. For the batch path

* Record the folder as IT11 P2.1 research material. No registry, card, need or ranking edit is proposed.
* Method note: "the phenotype-first graph status is read from the full seed-specific list and carries a structural reachability code; leads are coverage controls, not ranking controls; class mates are search lists without transfer of the lead's result".
* Apply `proposed_patch_dispose_it10.diff` (dispose_it10.py 4 lines, test_it10_p1.py 1 line) and regenerate `generation_it10_p1_20261031/results/phenotype_first.tsv`; amend IT10 README 3D (lithium returned in Q6 expression; d-APV's zero is the indirect part). This is an orchestrator edit outside my directory.
* Receipts: none proposed for the ledger (no source was read as a full text here). If the orchestrator wants a verifier, the decisive premise to check at source is the Fig 7d wild-type panel (entry [22] of the PMID 32000863 manifest) and the LiCl salt statement.
