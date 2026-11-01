# IT18 P3: an action-direction source whose origin is not ChEMBL or GtoPdb

Non-canonical research material; not medical advice; computational, pharmacological compatibility only. Public edition, WWOX-DEE genotype class. Package written 2026-11-01 by ACTOR_ID scientist.

## Design (written and committed before the comparison was run)

**Gap chosen.** IT18 P0 (`../diagnosis_it18_20261101/README.md`, row "Compound-target-action") and IT17 P3 (`../evaluation_it17_p3_20261101/README.md`, "Not shown") leave two limits on the one field the IT18 matching question (`../matching_it18_p4_20261101/PRE_REGISTRATION.md`) depends on, the compound's action direction at a target: (1) 83 percent of the module's human ChEMBL mechanism pairs have no GtoPdb counterpart, and (2) where they do, ChEMBL and GtoPdb share literature, so their 0.997 agreement is not independent confirmation; six discordances stay unresolved at source. The existing cache does not close this: in the module's DGIdb file only the ChEMBL and GuideToPharmacology rows carry an interaction type (TTD, DTC, NCI, PharmGKB, TdgClinicalTrial, TEND and FDA rows: type NULL, except 94 DTC "inhibitor"), so DGIdb adds no third direction.

**Capability under test.** A third action source whose rows state the origin of the action label: DrugCentral `drug.target.interaction.tsv.gz` (column `ACTION_TYPE`, origin in `MOA_SOURCE`, else `ACT_SOURCE`), joined to the catalogue by the UniChem ChEMBL->DrugCentral whole-source map (`src1src34`, same route and terms as the catalogue's other UniChem maps). IT14 P6 kept DrugCentral at WATCH because it added no *pair* for eight declared compounds; this is a different question (an independent *direction* on pairs the module already has), not a re-run.

**Two routes for the same capability.** (A) direct file plus map, offline after one download; (B) ToolUniverse 1.5.8 `DrugCentral_get_targets` (backend MyChem.info, one call per compound), in a throwaway venv in the scratchpad, on a sample of 20 compounds: the six discordant-pair compounds' parents plus 16 drawn by sorted sha256 of the parent id from the matching universe and the rest of the catalogue. Measured for both: rows, action labels, origin field present, truncation, errors, wall time, requests, disk, dependencies, removability.

**Rules fixed now.**
- Direction vocabulary: the IT17 ChEMBL map (`CHEMBL_DEC`/`CHEMBL_INC` in `direction_task.py`) plus `GATING INHIBITOR` -> DECREASE; partial agonist, modulator, allosteric modulator, binding agent, antibody binding, substrate, releasing agent, chaperone, other -> no direction. Human rows only.
- Origin classes of a DrugCentral action: SHARED = CHEMBL or IUPHAR; INDEPENDENT = DRUG LABEL, SCIENTIFIC LITERATURE, KEGG DRUG, EXPERT CURATOR; OTHER = anything else (WOMBAT-PK, DRUGBANK, DRUG MATRIX, PDSP, UNKNOWN). Origin = `MOA_SOURCE` when filled, else `ACT_SOURCE`. "Independent" means a different curation origin, not a proof of truth: DrugCentral curators may have read ChEMBL or IUPHAR.
- Measures over the module's 11,917 human direct ChEMBL mechanism pairs (IT17 construction, parent ChEMBL id x UniProt): pairs with a determinate DrugCentral direction, by origin class; agreement with the module's direction; pairs with no determinate GtoPdb counterpart that gain one; the six IT17 discordant pairs (DrugCentral label and origin). On the IT18 matching universe: compound x need counts only (compounds with an INDEPENDENT determinate direction on a need target gene); no per-compound label of the universe is written here, so the P4 lock is not anticipated.
- Outcome rule: **adoption** only if INDEPENDENT determinate coverage adds at least 100 module pairs with no determinate GtoPdb counterpart and agreement with the module there has a Wilson lower bound of at least 0.90; **optional circumscribed use** if it adds fewer pairs but resolves at least one discordance or covers at least 10 matching-universe compounds; otherwise **waiting** or **discard** with the reason. ToolUniverse is preferred over route A only if it returns the same labels with the origin field at lower total cost.

## Results

(filled after the run)
