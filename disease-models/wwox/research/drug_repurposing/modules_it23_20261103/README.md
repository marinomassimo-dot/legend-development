# IT23 P2/P5 - disease-module discovery (nf-core/diseasemodulediscovery) as a way to widen the targets the generator reaches

Exploratory, computational, public edition (reference genotype class). Not medical advice. Module membership gives neither a causal
direction nor the benefit of an intervention; nothing in this folder ranks compounds, and nothing here may be used to rank compounds by membership.

## Decision first

**WATCH.** Do not adopt the pipeline, and do not adopt its Drugst.One drug-prioritisation step at all (REJECT for that step).
The three small components (first neighbours, random walk with restart, a DIAMOnD-style test) are re-implemented in
`reproduce_module_probe.py` and may be re-run as an optional exploratory probe once a qualified larger seed set exists.
Reason: LEGEND's current seed sets are at or below the size these algorithms need, the one set pair that reaches 12 genes
(Q2 and Q3, only when the declared process-set members are counted) gives lists that are either trivial (STRING neighbours of a
pathway that is itself the seed) or hub-driven and unstable (LEGEND network used unsigned), and on the engine side only 3 targets
reached by the new methods and not already near the seeds have a signed catalogue action.

What it adds, in one line: an unsigned, undirected PPI-style neighbourhood (STRING) that the signed regulatory network does not hold
(for Q3, an endoplasmic-reticulum stress and protein-quality-control block around EIF2AK3, ERN1, HSP90B1). What it does not add: sign, direction, a compound.

## What was read (current pipeline, dev branch checked 2026-11-03; never run, no Nextflow, no Docker)

Details per component in `pipeline_audit.tsv`.
- Module algorithms wrapped: DOMINO (MIT), DIAMOnD (MIT, a single python script), ROBUST (GPL-3.0), ROBUST bias-aware (GPL-3.0), first neighbours and RWR (pipeline's own scripts, MIT repository). The pipeline repository is MIT.
- Networks accepted: STRING v12 (min 700/900, full and physical), BioGRID 4.4.242, HIPPIE v2.3 (high/medium), IID (March 2025), NeDRex (all/high confidence), or an own edge list. Prepared files are graph-tool `.gt` files on Zenodo (CC BY 4.0 on the record); upstream terms other than STRING's were not re-read.
- **Drugst.One dependency (visible):** the `DRUGPREDICTIONS` step imports the `drugstone` python client (MIT) and calls `drugstone.new_task(...)`, which sends the module's gene list to the Drugst.One web service (`api.drugst.one`; the default database is updated weekly, a yearly "stable" endpoint exists). The ranking (trustrank by default, degree, closeness) runs on the server over NeDRex/BioGRID/IID/IntAct/STRING/APID networks and NeDRex/DrugBank/DrugCentral/ChEMBL/DGIdb drug-target links; DrugBank content needs a licence acceptance. Relative to LEGEND it adds an unsigned network-proximity ranking of drugs. LEGEND already holds the drug-target resources and scores signed actions; a proximity is not an action. It can be skipped with `--skip_drug_predictions` and `--skip_drugstone_export`. Gene lists leaving the machine are public-edition genes only, but the dependency also makes results non-reproducible unless the stable endpoint is pinned.
- Other web calls: g:Profiler enrichment, DIGEST validation (not verified whether it calls a server), NeDRexDB annotation, Zenodo network download.
- Cost: Nextflow >= 26.04 and docker or singularity; default process labels up to 6 cpu / 12 GB / 12 h, and one label asks for 200 GB. graph-tool (conda or docker only) is the shared dependency; the `.gt` networks cannot be read without it. The algorithms themselves are small; the cost is the runner.

## LEGEND's gap, stated exactly

The generator takes a signed seed vector and propagates it backward through the signed SIGNOR + CollecTRI network (K = 3 hops) to score compound families by signed target actions. Seed sets (from `generation_it22_p1_20261103/inputs_it22/seeds_p1/manifest.tsv`):

| Set | Seed rows | Distinct genes (rows only / with declared process-set members) | In STRING v12 min 900 | In LEGEND network |
|---|---|---|---|---|
| Q2 expression | 8 | 7 / 12 | 6 / 11 (LDHB absent) | 7 / 12 |
| Q3 expression | 6 | 5 / 12 | 5 / 12 | 5 / 11 (PSPH absent) |
| Q4 (expression + protein) | 6 | 6 / 6 | 6 | 5 (KCNA2 absent) |
| Q5, Q6, Q8 | 3, 1-2, 1 | 3, 1-2, 1 | not run | not run |

Q1 (WWOX itself, 1 gene), Q7 (1) and Q5/Q6/Q8 are far below any threshold and were not run. The twelve-gene figure for Q2 and Q3 exists only because each table carries one declared
process row (`SET:GLYCOLYSIS_LACTATE_10`, `SET:ISR_TARGETS_12`) with its members; no gene was added by this work. The threshold of about 10 seeds is the caller's statement; the pipeline documentation
checked contains no minimum. Qualifying (borderline): **Q2 and Q3 with process members (12 genes each)**. Q4 (6 genes) was run only as a below-threshold contrast.
Note: the engine's proposal table (`results_p1/proposals_it21.tsv`) holds main targets for Q2, Q4, Q5, Q6 and none for Q3, so "overlap with the engine" is zero for Q3 by absence, not by disagreement.

## What ran (`reproduce_module_probe.py`, 694 s, 4 GB cap, numpy + scipy in a scratch venv)

- Networks: STRING v12 human links, combined score >= 900 (key-less download from the STRING download site, 12,323 nodes, 100,856 edges; these are functional associations, not only physical contacts), and LEGEND's own SIGNOR + CollecTRI network read as unsigned and undirected (8,769 nodes, 69,346 edges).
- Methods (top 50 non-seed nodes each): direct neighbours ranked by number of seed links; RWR with restart probability 0.5 (the pipeline default is 0.8; its meaning was not verified); RWR divided by the degree-proportional steady state (hub control); a DIAMOnD-style hypergeometric connectivity test, 100 added nodes, alpha 1 (written from the published description; the MIT reference script was not copied or read).
- Perturbations: leave one seed out, 20 random removals of 10 % of edges (seed 20261103), removal of the 20 highest-degree non-seed nodes. Output in `sensitivity.tsv` (Jaccard of the top-50 lists; baseline rows give the share of the list in the top 5 % degree).
- Overlaps in `new_targets.tsv` per listed target: direct neighbour; in the engine's main targets for that question; within 3 directed regulator hops of the seeds in the LEGEND network (where the engine can already look); signed catalogue families (`family_actions.tsv.gz`, rows with non-zero mean sign, flags not applied).

## Findings

1. **Seed sensitivity.** STRING, Q2/Q3 with process members: leave-one-seed-out Jaccard 0.83-0.98 except Q3 DIAMOnD (0.91 mean, one run at 0.0). With the 5-7 row-only genes the same test gives 0.68-0.84 for neighbours and RWR and 0.35-0.98 for DIAMOnD on the LEGEND network (see `sensitivity.tsv`). The small sets are therefore not catastrophically unstable under leave-one-out, mostly because the lists are dominated by close neighbours of whichever seeds remain.
2. **Edge sensitivity.** 10 % edge removal: RWR and neighbours 0.75-0.87. DIAMOnD is the fragile one: LEGEND network 0.30-0.33 (Q2/Q3 with process members), STRING Q3 0.48 with a minimum of 0.0.
3. **Hubs.** On the LEGEND network (Q2 / Q3 with process members) the share of the top-50 list in the top 5 % degree is 0.34 / 0.56 for neighbours, 0.66 / 0.70 for RWR, 0.16 / 0.78 for DIAMOnD; removing the 20 highest-degree nodes (SP1, RELA, NFKB1, MYC, JUN and so on) drops the Jaccard to 0.64-0.67 (neighbours), 0.59-0.64 (RWR) and 0.16-0.43 (DIAMOnD). The DIAMOnD list for Q3 on that network contains TNF, IL6, IL4, IFNG, ICAM1, IL10: inflammatory regulators that no ISR-specific observation supports; that is hub domination, not module discovery. The degree-corrected RWR removes the hubs (hub share 0.02) but then shares little with the plain list. On STRING min 900 the top-degree nodes are ribosomal and ubiquitin proteins that never enter the lists (hub share 0.00-0.16), so hub removal changes nothing (Jaccard 0.89-1.0); hub dominance is not the STRING problem, closeness to the seeds is.
4. **New targets, STRING, Q2 and Q3 with process members** (top 50 per method, "new" = not a direct neighbour, not an engine main target, not within 3 regulator hops):

| Set | Method | Direct neighbours | Engine main targets | Within 3 regulator hops | New | New with a signed catalogue action |
|---|---|---|---|---|---|---|
| Q2 | neighbours / RWR / DIAMOnD | 50 / 50 / 50 | 1 / 1 / 0 | 3 / 4 / 1 | 0 / 0 / 0 | 0 |
| Q2 | RWR hub-corrected | 45 | 0 | 2 | 5 | 0 |
| Q3 | neighbours / RWR | 50 / 50 | 0 | 10 / 16 | 0 | 0 |
| Q3 | RWR hub-corrected | 40 | 0 | 9 | 9 | 1 (SLC7A5, 1 family) |
| Q3 | DIAMOnD | 10 | 0 | 17 | 31 | 2 (EIF2AK3, 2 families; HSP90B1, 3 families) |

   For Q2 the lists are the glycolysis paralogues and neighbours of the seeds (GPI, TPI1, ALDOB, PGAM2, ENO2...): the seed set already is a pathway, so the module is the pathway again, with no regulator. For Q3 the DIAMOnD list adds 40 non-neighbour proteins of the ER stress and ER-associated degradation machinery (ERN1, DNAJB9, HYOU1, PDIA4, SEL1L, VCP...); the sign of the interferon-stress-response seeds is unresolved (guard tag `ISR_SIGN_UNRESOLVED`), so no direction attaches to any of them.
   Across both sets, all methods, STRING: 3 distinct new targets have a signed, documented catalogue action (SLC7A5, EIF2AK3, HSP90B1); of 45 distinct new STRING targets, 42 have none. The LEGEND network adds 16 more signed-action targets (e.g. IRAK4 15 families, CXCR1 9, PTGES 8, TNF 15, IL6 8), but that network is the engine's own and the additions are the hub artefact in finding 3, so they are not counted as evidence.
5. **Overlap with the engine.** Q2: STRING lists contain at most 1 of the 11 engine main targets (EGLN2, HIF1A, HDAC5 and others sit outside the glycolysis neighbourhood). Q4 (6 genes, below threshold): 0-1 of 7. The unsigned module lists and the signed engine look at different things; the overlap is about zero.

## Verdict on seed size and the abstention

With 12 genes the result is an abstention for sign and for compounds: modules reproduce the seed pathway (Q2) or a plausible but unsigned stress block (Q3), DIAMOnD on the denser network is unstable, and the only independent network (STRING) adds target names, not documented actions.
Q4, Q5, Q6, Q7, Q8 and Q1 do not qualify. Do not enlarge them by adding genes without a qualified observation.

**Measurement that would give a qualified larger seed set:** a per-contrast gene list from one deposited WWOX-loss comparison (the transcript_contrast tier A readings already used for Q2/Q3, e.g. the organoid and neuron deposits), with a stated significance threshold and direction fixed before looking at modules, giving roughly 30-100 genes with a defined sign per readout level; module discovery would then run on that list with the leave-one-out, edge and hub checks above repeated. Until then the signed propagation remains the method.

## Could not be verified

- No pipeline run; algorithm behaviour was reproduced by re-implementation only, so the numbers describe these re-implementations (RWR restart 0.5 versus pipeline 0.8; DIAMOnD 100 steps and no seed up-weighting) and not the pipeline.
- Licences were taken from the GitHub/PyPI/Zenodo metadata fields; graph-tool, g:Profiler, DIGEST, ROBUST's solver, IID, HIPPIE and NeDRex terms were not read. Whether DIGEST calls a server is not verified.
- STRING min 900 includes text-mining and co-expression channels; physical-only networks were not run. The prepared `.gt` networks (BioGRID, IID, NeDRex, HIPPIE) were not used because graph-tool is not available.
- "Signed catalogue action" counts rows present in the family action table, without its flags.

## Files

`pipeline_audit.tsv`, `sensitivity.tsv`, `new_targets.tsv`, `run_facts.json`, `reproduce_module_probe.py` (run: `python3 -I reproduce_module_probe.py --string-dir DIR` with the two STRING files `9606.protein.links.v12.0.txt.gz` and `9606.protein.info.v12.0.txt.gz`; downloads were not stored in the repository).

## Corrections after the independent verification (IT23 P6)

Q3 is the ISR/ER-stress set (ATF5, CHAC1, TRIB3, ...), not an interferon-stress set. The Drugst.One python client sends the gene list to `api.drugst.one` and turns off TLS certificate checking: a further reason not to adopt its drug step. Abstaining is the right reading of the sensitivity table.
