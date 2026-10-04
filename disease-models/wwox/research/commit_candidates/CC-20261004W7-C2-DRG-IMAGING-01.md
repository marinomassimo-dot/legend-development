# CC-20261004W7-C2-DRG-IMAGING-01 — the only DRG imaging endpoint in the corpus measures storage enlargement, not vector injury, and its repeatability band is about a quarter of its mean

`context_policy: SOURCE_FIRST`
**Date:** 2026-10-04 · **Author:** Scientist C2, intake wave 7 · **Change class:** MINOR
**Target records:** `disease-models/wwox/research/discovery_ledger_current.md` (append one lead)
Receipt: `FTR-20261004-41134821-01` (prepared, not recorded) · Manifest `deepdive_manifests/PMID41134821.json` (VERDICT PASS) · Dossier `fulltext_dossiers/PMID41134821.md`
**Nothing here is medical advice. WWOX occurs zero times in the source; this is an earned null for the gene.**

## 1 · What it adds to, bounds, and leaves untouched

- **Adds** a candidate non-terminal DRG endpoint to the restoration spec's off-target-organ-risk row and to the DRG-attribution records, which so far rely on terminal histology and serum NfL.
- **Bounds** it: the method was shown on an enlargement lesion in a Fabry mouse; the AAV effect is a therapeutic normalisation; there is no wild-type AAV-injected group, so the design could not register vector injury; no atrophy or neuronal-loss comparator exists.
- **Corrects** the selection note: "response to AAV treatment conflates benefit and injury in one number" is not what the paper does; it conflates nothing because it measures only the storage-lesion direction.
- **Leaves untouched** the DRG-attribution and immunosuppression candidates of waves 4-6.

## 2 · Op — discovery_ledger_current.md

`op: APPEND` one lead. No `old` text.

```
### DL-METH-xxx (provisional) — A DRG imaging endpoint exists only for storage enlargement; whether it could register vector-associated DRG degeneration is untested

**Tag:** INFERENZA
**Status:** open
**Created:** 2026-10-04 · intake wave 7, Scientist C2
**Causal statement:** A 7 T mouse protocol measuring L4 DRG cross-sectional area from a maximum-intensity projection (ICC 0.9, limits of agreement
-0.060 to 0.066 mm2 on a 0.257 mm2 mean in five wild-type mice) detected a roughly 25 percent enlargement in a Fabry mouse (0.35 vs 0.28 mm2 at 24 weeks)
and its normalisation after AAV9-GLA. It was not tested against any lesion that shrinks or destroys DRG neurons, which is the direction of AAV-associated DRG toxicity,
and the repeatability band is of the same size as the disease effect at the group level.
**Reasoning chain:**
1. The measure is an axial MIP area, a surrogate for volume; slice thickness 0.292 mm; no DRG-cord contrast, so delineation uses adjacent cord images (authors).
2. Test-retest relative differences per DRG ran from about -15 to +19 percent (Table 2, cell-wise).
3. Groups are 3 (untreated Fabry), 5 (AAVnull), 5 (AAVGLA) and 5 wild type; group sizes in Results and Methods disagree (fifteen against thirteen Fabry mice).
4. The AAV9-null Fabry group showed no separate DRG signal from untreated Fabry, but there is no wild-type AAV-treated group to show vector effect on a healthy DRG.
**Counter-evidence / what would refute this lead:** the same protocol detecting a histologically confirmed vector-induced DRG lesion in a toxicity model; a published
larger-group repeatability analysis with a narrower band.
**Falsifying experiment:** image DRG in an animal model with known graded AAV DRG degeneration, with histology as truth; compute detection sensitivity.
**Operational consequence (proposed, not a gate):** a DRG imaging readout must not be cited as a safety endpoint for a vector until it has detected a vector lesion.
**Transfer limit to WWOX:** mouse, storage lesion, 7 T; says nothing about human MRI, the reference genotype, or a WWOX-restoration vector.
**Not medical advice.**
```

### LOCATOR TRIPLES FOR BLIND AUDIT

- (The measure is a cross-sectional area from a maximum-intensity projection used as a stand-in for volume | we used the cross-sectional area (CSA) derived from maximum intensity projection (MIP) images in the axial direction as a surrogate for dorsal root ganglion (DRG) volume | Discussion, Limitations paragraph 1, `files/fulltext/PMID41134821_Zhao2025_PMC.xml`)
- (DRG and cord were not separable by contrast | we used the adjacent spinal cord images for DRG delineation, as no clear contrast between the DRG and spinal cord was observed | Discussion, Limitations paragraph 2, `files/fulltext/PMID41134821_Zhao2025_PMC.xml`)
- (Test-retest agreement in five wild-type mice | Excellent repeatability and reliability were achieved with the limits of agreement from | Results, test-retest paragraph, `files/fulltext/PMID41134821_Zhao2025_PMC.xml`)
- (Fabry DRG about 25 percent larger at 24 weeks | the DRG size in the Fabry mice was ~ 25% larger and statistically different than the DRG size in the wild type mice | Results, DRG enlargement paragraph 3, `files/fulltext/PMID41134821_Zhao2025_PMC.xml`)
- (No difference between AAVGLA-treated Fabry and wild type | There were no statistically significant differences at all the time points between the gene therapy group and the wildtype group. | Results, DRG enlargement paragraph 4, `files/fulltext/PMID41134821_Zhao2025_PMC.xml`)
- (Results state fifteen Fabry mice | a total of fifteen Fabry mice that were separated into 3 groups | Results, DRG enlargement paragraph 1, `files/fulltext/PMID41134821_Zhao2025_PMC.xml`)
