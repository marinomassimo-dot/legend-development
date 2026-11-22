# ADV-176 frozen design (IT, 2026-11-22), written BEFORE the path was run on this case

Hypothesis level; no dose; not medical advice; reference genotype class only. A FUNCTIONAL evaluation of the real generation path (relations table, `generation_it41_20261109/action_search.py`, a comparison in the `comparisons_it41.md` layout), not a predictive one. No ranking change, no WWOX efficacy claim.

## Step 0: the Kv7 default is NOT fresh; motivated pivot
* IT41 Case 4 abstained on Kv7 opening (relation S3), and the same relation S3 was RUN in IT44 (`generation_it44_20261110/relations_s3.tsv`, with S11 Kir/K2P, S12 Kir4.1, S13 NMDA block); IT46 ran S5 (GABA-A), IT49 ran I1 to I3 (ISR), IT43 ran S9 and S10 (PDK, NRF2). Relations S1 to S13 and I1 to I3 are all used.
* ADV-173 already answered the question the default asks: Dirkx 2026 (KCNQ2 iNeurons) is an adjacent channel-gene model with one current measurement and no treated control; it moves neither Case 4 condition (a measured difference current near E_K in Wwox neurons, E3; a matched-effect control, M10). Re-running would re-abstain for the same named reason and add nothing.
* Chosen case instead: **ERBB4 / NRG1 signalling in PV interneurons (RP-038, INV-15, brief add-on (e3))**. Fresh: ERBB4 has never been a relation in any `relations_*.tsv` (only catalogue rows inside proposal tables). Held and qualified: RP-038 RESULT (SCI, 2026-11-21): CONDITIONAL class, an NRG1 EGF-domain peptide, adult intracerebroventricular benefit only, a developmental-timing conflict (a neonatal regimen is a published schizophrenia-like model), sign premise untested; Sun 2016 (ADV-167, state-conditional and PV-ErbB4-dependent response in juvenile visual cortex, adjacent model). Opposite-direction comparator: ERBB4 kinase inhibition (the sign premise is untested, so the opposite direction is equally plausible). The path's job is direction: separate molecules that act on the target from molecules that act in the WANTED direction.

## Frozen input
* `relations_adv176.tsv` (this folder), SHA-256 8e6d621f25c025f39c89ad6dfaa53ef2c79f13f0e20c6bfea84fece38e019ad9: E1 (enhancing, wanted_direction up), E2 (inhibition, down, the opposite-direction comparator), E0 (the SIMPLE ROUTE: the same target, no direction, no site rule, which makes every source row a candidate).
* Catalogue and GtoPdb cache as pinned by `catalog/cache_manifest.json` (interactions.csv sha256 prefix cdbd18c66cf99d1a; the run prints it). Run: `LEGEND_RELATIONS=<file> LEGEND_SEARCH_OUT=<scratch dir> python3 generation_it41_20261109/action_search.py` with `LEGEND_CATALOG_CACHE` pointing to the root checkout's cache. No other input, no new tool, no network.
* What I had seen: I ran `action_search.py` once by mistake (it has no `--help`) with the IT41 relations (no ERBB4 relation): its outputs were byte-identical to the tracked files (git status clean). I have NOT looked at any ERBB4 row of the catalogue or of any search output.

## Comparators
* **Simple route (frozen):** E0, the target-only reading: count the distinct parent molecules with any ChEMBL curated mechanism or GtoPdb row on ERBB4, direction ignored; and, as the "current ordering", RP-038's own statement (the handle question "never asked"; the held class is an NRG1 peptide).
* **Real path:** E1 and E2 through the path's qualification (direction, site policy, unknown fields, label conflict): per relation the verdicts CANDIDATE (reason `ok` or `unknown_fields`), EXCLUDED (`direction_opposite`) and UNKNOWN, each source row kept separate, nothing scored or ranked.

## Endpoint and the ONE before/after choice
Endpoint: for E0, E1, E2: distinct parent molecules; source rows; verdict counts; the E1 candidates with their source, species, action text, primary-target flag and quantity; the molecules in E0 that the path moves out of the wanted direction. The choice a reader would act on: **"does the catalogue hold a handle for RP-038's wanted (enhancing) direction, or only molecules of the opposite direction?"** Before (simple route): "N molecules act on ERBB4: handles exist." After (path): the wanted-direction set and the opposite-direction set separately, each with its source rows.

## Abstention condition (named before running)
The path ABSTAINS from nominating a tool arm or handle for the enhancing direction (output = the knowledge that decides it, not a list) if NO E1 row is a CANDIDATE with a documented ERBB4-directed action in the wanted direction from a curated or primary source that states species and an assay context, and carries the primary-target flag or an ERBB4-specific value; rows that are only family-level or unknown-direction stay UNKNOWN and do not nominate. It also does NOT nominate where the catalogue cannot carry the held qualifiers (adult-only benefit, neonatal conflict, brain exposure): such a row is output as "candidate by action, held conditions not evaluated", never as a handle. An abstention is a valid result.

## Rejecting observation (the path adds nothing)
The path's wanted-direction molecule set equals the simple route's set (no direction information separates them), OR the reader's action would be the same after reading both outputs. Either is recorded plainly as "the path adds nothing over the simple route on this case".

## Predictions fixed before running (priors, not tuned on the output)
(a) E0 is larger than E1 and E2 is most of E0; (b) E1 is small (zero to a few) and, if non-empty, mostly peptide ligands, none with brain exposure; (c) the abstention condition is probably met for a handle, with the neonatal-conflict qualifier not evaluable by the path. These are guesses from general pharmacology, not from any catalogue read here.

## Intake and delivery
Mechanism intake: the relation rows above carry the held mechanism and context; after the run the folder gets a `hypotheses_only` row in `hypothesis_packages.tsv` for INV-15 only if `hypothesis_package.validate_manifest` accepts it without new files or tools (otherwise the validator's message is a finding). Comparison written in the `comparisons_it41.md` layout (four elements, how a result moves the alternative). The simple route's own output is reported beside the path's. Nothing predictive is created; anything that becomes predictive goes to the existing ledger against a future observation.
