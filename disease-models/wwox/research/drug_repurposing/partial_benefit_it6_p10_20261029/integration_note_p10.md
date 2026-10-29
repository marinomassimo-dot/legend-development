# Coverage inputs: what P10 proposes, and what it does not

Actor `scientist-a`, 2026-10-29. Non-canonical. The coverage tables are built by a script; the three curated inputs are
`target_roles.tsv`, `assertion_pertinence.tsv`, `source_artefacts.tsv`, plus `lead_dispositions.json` read by the join.

| Input | Proposed change | Reason |
|---|---|---|
| `target_roles.tsv` | none | it couples a target's activity to the quantity of a **direction-evaluable** need; `NEED-NEUROINFLAMMATION-GLIA` is `uncertain` and exploratory, and IL1R1/CASP1 have no WWOX observation behind them |
| `assertion_pertinence.tsv` | none | it lists the data assertions of cards that carry **drug** assertions; `J01` carries none, exactly as `F02` has no rows |
| `source_artefacts.tsv` | none | no new upstream artefact was found; the DGIdb GFAP and IL6 rows are readout-marker rows the coverage code already never counts as links |
| `lead_dispositions.json` | one entry, below | a reasoned ending of the catalogue search for this need |
| `needs/needs.json` | `needs_patch.diff` | adds IL1R1 and CASP1 as intervention targets, so the refreshed `associations.jsonl.gz` reaches anakinra (IL1R1) and belnacasan (CASP1); expect more `NEED-NEUROINFLAMMATION-GLIA` rows and families after regeneration, none with a WWOX context |

After integration: `python3 -B framework/scripts/repurposing_coverage.py run`, `... check`, then `python3 framework/scripts/repurposing_view.py run` (and regenerate `needs/needs.md` by whatever tool built it; the
tool is not named in `needs/`, UNVERIFIED which one). The patch was applied and checked with `needs/check_needs.py --file` on a scratch copy.

## Proposed entry for `lead_dispositions.json` (`dispositions` array)

```json
{
 "id": "LD-007 (provisional: take the next free id at integration)",
 "need": "NEED-NEUROINFLAMMATION-GLIA",
 "subject": "IL-1-axis and JAK-STAT agents as a class (IL-1 receptor antagonist via IL1R1; caspase-1 inhibitor via CASP1; IL-1beta antibodies; NLRP3 inhibitor; JAK2 inhibitors)",
 "catalogue_ids": [
  "CAT:CHEMBL1201570",
  "CAT:CHEMBL2107819",
  "CAT:CHEMBL1201834",
  "CAT:CHEMBL3989943",
  "CAT:CHEMBL1789941",
  "CAT:CHEMBL2105759"
 ],
 "decision": "abstention",
 "why": "The sign of the glial difference conflicts between species (null and P47T mouse excess; Wwox-mutant rat deficit from PND 5; human organoid no reactive programme), the time order of gliosis and seizures was never measured in the same animals, and every verified compound precedent is acute or post-infectious and uncontrolled or uninformative for long-term outcome, with acute seizure-control reports for anakinra and no usable trial-level VX-765 result (abstract level, NOT WWOX EVIDENCE). Catalogue links exist only as exploration rows (no stated direction for 439 of the 642 non-excluded intervention-target rows; 738 intervention-target rows before 96 exclusions).",
 "reopening_condition": "a time course of glial density against first spike in a Wwox-deficient model showing glia above wild type before the first spike, or any glial endpoint after a compound in a Wwox-deficient system",
 "next_experiment": "time course P5 to P17 with simultaneous recording and glial density in cortex and hippocampus (cycle README section 12); no compound arm",
 "owner": "Scientist (wet-lab design; not done here)",
 "card": "cards/J01_glial_reactivity_modulation.packet.json (after the integrator moves it)",
 "record": "partial_benefit_it6_p10_20261029/README.md#12-the-next-experiment-that-discriminates"
}
```
