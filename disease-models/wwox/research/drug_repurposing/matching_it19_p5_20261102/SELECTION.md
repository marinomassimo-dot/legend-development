# IT19 P5 step 1 — selection rule and reference protocol (written before any new reference outcome is opened)

Written 2026-11-02 by the Scientist, before any new reference source (DrugCentral, ChEMBL activity or assay records, literature) was opened for the selected pairs. Non-canonical research material; not medical advice; pharmacological compatibility only, no benefit claim. Public edition, WWOX-DEE genotype class.

The IT18 package (`../matching_it18_p4_20261101/`, pre-registration, locked answers, results, controls) and the sealed IT17 freeze are read, never modified. The thresholds of IT18 (the 40-row floor) belong to that experiment and are not reused here as a block.

## Task, stated precisely

For a bounded set of IT18 directed (need, compound) pairs that had **no determinate reference**, build a reference label at the resolution the need is written in, and use it to answer two questions:

1. **Coverage:** how many of these pairs can carry a usable reference once sources other than the GtoPdb join are read, and why the rest cannot.
2. **Module decision:** on the pairs that become determinate, which attribution of the module was right, wrong or a justified abstention — in particular whether a group-level ChEMBL action transferred to member genes (the IT18 DEV defect) produces attributions the reference does not support.

It is not a test of general superiority of the contextual path over target-only. With about 30 pairs, any figure is a case series with an interval.

## Universe and exclusions

The 76 IT18 directed rows (needs EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, SEIZURE-CONTROL-SYMPTOMATIC, T-TYPE-CALCIUM; all "down"), minus the 8 rows already determinate in IT18 (listed in `controls_result.json`): **68 unresolved pairs**. Nothing outside the IT18 universe is added.

## Rule (deterministic, outcome-blind; `select_pairs.py`)

Each unresolved pair is placed in one stratum from module-side facts only: the class of the ChEMBL mechanism record(s) that bring the compound to the need (single protein; defined complex; group or family whose components are at least half the module's intervention targets = *homogeneous*; otherwise *heterogeneous*), the ChEMBL action, and whether the compound carries other ChEMBL mechanisms on genes outside every directed need. Within a stratum, compounds are ordered by `sha256("IT19P5|" + parent ChEMBL id)` (a salt different from IT18's case table, so the choice does not reproduce it) and the quota is taken from the top. For the two calcium needs a chosen compound is taken on **both** needs, because the two needs ask at different resolution (SEIZURE lists CACNA1G alone; T-TYPE lists CACNA1G/H/I); those two rows share a compound and are not independent.

| Stratum | Contrast it carries | Available (compounds / pairs) | Taken (compounds) |
|---|---|---|---|
| S01 | heterogeneous 26-component calcium-channel group, BLOCKER — the IT18 transfer defect; L v1 compatible vs L v2 abstain: informative abstention or false exclusion? | 4 / 8 | all 4 |
| S02 | same group, MODULATOR (gabapentinoids) — too-generic link, unknown must stay unknown | 5 / 10 | 1 |
| S03 | homogeneous T-type family, BLOCKER — family evidence valid at the family need; does it reach CACNA1G alone? | 6 / 12 | 2 |
| S04 | single protein (Ca_v3.2), BLOCKER | 1 / 1 | all |
| S05 | homogeneous NMDA receptor group, clean down action, single mechanism | 10 / 10 | 4 |
| S06 | same group, clean down action, compound also has mechanisms off the directed needs — relevant mechanism vs secondary link | 5 / 5 | 2 |
| S07 | NMDA group, PARTIAL AGONIST — ambiguous modulation | 2 / 2 | all |
| S08 | NMDA group, positive allosteric modulator — opposite | 1 / 1 | all |
| S09 | defined GRIN1/GRIN2B complex, ANTAGONIST — direct subunit-level action | 4 / 4 | 2 |
| S10 | homogeneous AMPA group, ANTAGONIST | 7 / 7 | 2 |
| S11 | AMPA group, positive allosteric modulator — opposite | 6 / 6 | 2 |
| S12 | single-protein records on the glutamate need | 2 / 2 | all |

Result: **32 pairs, 25 compounds** (`selection.tsv`). Every stratum has data; none was left out.

**Why this size.** Each stratum carries one contrast the task names (single vs family vs complex; direct vs ambiguous; compatible vs opposite vs indeterminable; abstention vs false exclusion; relevant vs generic). Where a stratum is homogeneous in its module-side facts (ten NMDA-group antagonists with the same record and the same action), more compounds repeat the same attribution question and only narrow an interval that cannot support a general claim anyway; the heterogeneous-group and single-record strata, where the attribution question differs, are taken whole. Thirty-two pairs is enough to see each kind of outcome and small enough to read every reference at the depth it needs.

**Not chosen for ease.** The rule takes every heterogeneous-group blocker, both partial agonists, both single-record glutamate compounds and the lone NMDA PAM regardless of what the reference might say; six of the 32 pairs are IT18 `opposite` or `indeterminable` labels. One selected compound (memantine, P19) is a compound the needs were written from (IT18 controls, construction leakage); it is kept and flagged, not swapped.

## Reference protocol (fixed now)

**Label per pair**: `compatible` (a determinate DECREASE of the target's activity at the need's resolution), `opposite` (determinate INCREASE), `indeterminable` (evidence exists but not at the required resolution, or the action is ambiguous, mixed, state-dependent without a net direction, or binding without function), `unknown` (no source found within the bounded search). Unknown is never negative.

**Required resolution.**
- T-TYPE-CALCIUM: an action on Ca_v3.1, 3.2 or 3.3 (recombinant subunit) or on a native T-type current — the need names T-type current, so family-level evidence is at the question's level.
- SEIZURE-CONTROL-SYMPTOMATIC (CACNA1G): an action measured on Ca_v3.1. A native T-type current or another Ca_v3 isoform is recorded as family-level and labels the pair `indeterminable` at this resolution (reported separately, never discarded).
- EXCITATORY-GAIN-GLUTAMATE-RECEPTOR: an action on NMDA receptors (native, or recombinant GluN1 with GluN2A/2B/2D) for NMDA records; on AMPA receptors (native or recombinant GluA1-4) for AMPA records. The need and the role table work at receptor-class level, so receptor-level evidence is at the question's level; a subunit is never given a direction only because it belongs to a measured receptor.
- A group record's action is **never** attributed to a member gene. An action measured on one Ca_v type (L-type, N-type) says nothing about Ca_v3.

**Measure type**: functional (electrophysiology, calcium flux, functional assay with a direction) is determinate; binding or displacement alone is `indeterminable` for direction; a clinical or behavioural outcome is not a target measurement.

**Sources, in order**: (1) existing LEGEND material (GtoPdb cache, IT18 receipts and dossiers, `nmdar_pharmacology_it6_p9_20261029`, other packages); (2) DrugCentral rows with their action-origin class (adapter `framework/adapters/drugcentral.py`); (3) ChEMBL activity and assay records (assay type, target and its type, document) through public GETs; (4) the primary-literature passage needed, read in full text where an experimental detail is required; an abstract settles only what it states.

**Dependencies.** For every label the construction source is recorded: if the reference rests on the document the ChEMBL mechanism itself cites, or on DrugCentral/DGIdb rows whose origin is ChEMBL or IUPHAR, it is marked `shared_derivation` and is not counted as independent of the module's input.

**Error attribution.** A group annotation can be correct in the source (ChEMBL says "voltage-gated calcium channel blocker" without naming a type) and become improper only through LEGEND's expansion to member genes; the label records which.

## Predictions, written before reading (preregistered, not used to select)

- S01: the heterogeneous-group action will be unsupported at Ca_v3 resolution for most of the four compounds (L v2 abstention justified), and supported for at least one (bepridil has a T-type literature) — so a blanket abstention would hide available information for that one.
- S03: family-level T-type block documented; Ca_v3.1-specific evidence present for the older succinimide/oxazolidinedione only if a recombinant study exists.
- S07/S08/S11: direction at the receptor will be ambiguous for the partial agonists and an increase for the PAMs.
- S06: the NMDA action of the multi-mechanism compounds will be weak or secondary; it may still be a determinate decrease (relevance is a separate axis from direction).

## Stages that follow (commits show the order)

Step 2 builds the reference (`reference_it19_p5.tsv`) without the module answers in view. Step 3 writes the module's answers from the code alone (active path `framework/scripts/repurposing_search.py`, plus the IT18 locked L labels carried unchanged) and commits them with a digest before the join. Step 4 repairs the active path if the transfer defect is confirmed there. Step 5 joins and reports.
